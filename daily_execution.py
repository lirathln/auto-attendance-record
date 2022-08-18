from datetime import datetime
import calendar_verification
import frequency
import schedule
import logging
import time

# armazena horários que pontos deverão ser registrados
TIME_WORK = []


# converte texto da agenda para itens da lista
def convert_to_list(string):
    return list(string.split(';'))


# verifica se existe o evento de expediente no google calendar, pelo arquivo calendar_verification.py
def verify_calendar():
    global TIME_WORK

    logging.info('Realizando verificação em agenda ...')
    calendar_summary = calendar_verification.main()
    TIME_WORK = convert_to_list(calendar_summary) if calendar_summary else []

    if TIME_WORK:
        logging.info('Dia com expediente. Pontos do dia: {}'.format(TIME_WORK))
        schedule_points()
    else:
        logging.info('Dia sem expediente. Nenhum ponto para hoje.')


# agenda o registro dos pontos nos horários em agenda, caso exista o evento para o dia
def schedule_points():
    try:
        for hour in TIME_WORK:
            schedule.every().day.at(hour).do(frequency.main)
        logging.info('Pontos agendados com sucesso.')
    except Exception as e:
        logging.error('Falha no agendamento dos pontos. Erro: {}'.format(str(e)))


# agenda a verificação do calendário diariamente, no horário expecificado
def main():
    try:
        schedule.every().day.at('07:58').do(verify_calendar)
        while 1:
            schedule.run_pending()
            time.sleep(1)
        logging.info('Execução encerrada às {}.'.format(datetime.now().strftime("%H:%M:%S")))
    except Exception as e:
        logging.critical('Execução parou. Erro: {}'.format(str(e)))


if __name__ == '__main__':
   main()
