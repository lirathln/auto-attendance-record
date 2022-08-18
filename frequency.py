from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from datetime import datetime
import requests
import logging
import json
import time

# carrega os dados gerais do usuário
app_data = open('app_data.json')
data = json.load(app_data)


# cria uma instância do navegador (Chrome)
def create_browser():
    browser_options = Options()
    browser_options.add_argument("--disable-extensions")
    browser_options.add_argument("--headless")
    #browser_options.add_experimental_option('prefs', {'geolocation': True}) # faz uso da latitude e longitude em app_data.json
    logging.info('Criando browser.')

    return webdriver.Chrome(executable_path="C:\dev\chromedriver", options=browser_options)


# verifica se a conexão com o site foi estabelecida, buscando por texto na página
def check_connection(browser):
    if browser.find_element_by_xpath("//*[contains(text(),'Seu e-mail ou CPF*')]"):
        logging.info('Verificação de conexão bem sucedida.')
        return True
    logging.warning('Falha na verificação de conexão.')
    return False


# verifica se frequência foi registrada com sucesso, através da mensagem informada por javascript
def check_success(browser):
    if browser.find_element_by_xpath("//*[contains(text(),'Ponto registrado com sucesso!')]"):
        logging.info('Verificação de registro de ponto bem sucedida.')
        return True
    logging.warning('Falha na verificação de registro de ponto.')
    return False


# encaminha uma notificação ao usuário, com as informações de sucesso ou falha no registro
# do ponto, através do aplicativo IFTTT 
def send_notification(result, description):
    # In IFTTT:
    # IF    Receive a web request (notification_event)
    # THEN  Send a notification from the IFTTT app (Frequência retornou: {{Value1}} - {{Value2}}!)
    try:
        url = data['notification_url'].format(data['notification_event'] if result == 'Sucesso' else data['call_event'])
        message = {'value1' : result, 'value2' : description}
        requests.post(url, message)
        logging.info('Envio de notificação bem sucedida.')
    except Exception as e:
        logging.warning('Falha no envio de notificação. Erro: {}'.format(e))


# finaliza isntância do navegador
def close_browser(browser):
    logging.info('Fechando browser.')
    browser.close()


# modifica a localização no sistema Pontomais
def geo_location(browser):
    coordinates = dict({"latitude":data['latitude'],
                        "longitude":data['longitude'],
                        "accuracy":data['accuracy']})
    browser.execute_cdp_cmd("Emulation.setGeolocationOverride", coordinates)
    logging.info('Localização enviada ao navegador: {}.'.format(coordinates))


# acessa o site do Pontomais
def access(browser):
    logging.info('Acessando site no browser.')
    browser.get(data['site'])

    time.sleep(10)

    if check_connection(browser):
        browser.find_element_by_name('login').send_keys(data['login'])
        browser.find_element_by_name('password').send_keys(data['password'])
        browser.find_element_by_class_name('btn-primary').click()  
        logging.info('Acesso ao site realizado com sucesso.')
    else:
        logging.warning('Falha ao acessar site, sem internet.')
        send_notification('Erro', 'sem internet')
        close_browser(browser)


# realiza o registro da frequência
def register_frequency(browser):    
    try:
        logging.info('Endereço identificado: {}'.format(browser.find_element_by_css_selector('li[class="list-group-item ng-scope"]').text))
        btn_register = browser.find_element_by_css_selector('button[ng-click="save()"]')
        browser.execute_script("arguments[0].click()", btn_register)
        hour = datetime.now().strftime("%H:%M:%S")
        logging.info('Frequência registrada com sucesso.')

        time.sleep(20)

        if check_success(browser):
            send_notification('Sucesso', 'registrado às {}'.format(hour))
        else:
            logging.warning('Ponto não foi registrado.')
            send_notification('Erro', 'falha ao registrar frequência: {}'.format(e))
            close_browser(browser)
    except Exception as e:
        logging.warning('Falha ao realizar o registro da frequência. Erro: {}'.format(e))
        send_notification('Erro', 'falha ao registrar frequência: {}'.format(e))
        close_browser(browser)


def main():
    try:
        browser = create_browser()
        access(browser)
        time.sleep(10)
        register_frequency(browser)
        time.sleep(5)
        close_browser(browser)
    except Exception as e:
        logging.critical('Erro crítico ocorrido: {}'.format(e))
        send_notification('Erro crítico', e)


if __name__ == '__main__':
    main()
