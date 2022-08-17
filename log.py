import logging
import daily_execution


# cria um arquivo de log, nomeado como logfile.log
def main():
    try:
        logging.basicConfig(format='%(asctime)s : %(levelname)s - %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S',level=logging.DEBUG,handlers=[logging.FileHandler('logfile.log', 'w', 'utf-8')])

        logging.info('Aplicação inicializada ...')
        daily_execution.main()
        logging.info('Aplicação finalizada!')
    except Exception as e:
        logging.critical('Erro crítico ocorrido: {}'.format(e))


if __name__ == '__main__':
    main()