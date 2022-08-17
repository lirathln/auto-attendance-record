# auto-attendance-record
Automation created to register attendance on the Pontomais website

Código criado com o intuito de registro automático de frequência no site Pontomais.
A implementação ocorreu em uma versão anterior do sistema, portanto, poderá não executar devidamente, devido mensagens e links modificados ao longo do tempo.

## Funcionamento
A execução desse código foi projetada para funcionar da seguinte forma:

1º Verificação do calendário pessoal do usuário, através de liberação ao Google Calendar, buscando por evento nomeado 'Trabalhado'. Esse evento deverá conter o horário para registro dos ponto na descrição do evento, por exemplo: 
    
    08:00;12:00;14:00;18:00

Obs.: Os horários deverão ser separados por ponto e vírgula (;), para que o código consiga separar os dados.
Obs.: O código fará o agendamento para execução nos horários especificados nessa descrição.

2º O código tentará realizar o registro da frequência, nos horários coletados na etapa anterior. Caso obtenha sucesso no registro, será encaminhada uma mensagem de sucesso ao aparelho celular do usuário, pelo aplicativo IFTTT. Entretanto, caso o código não obtenha sucesso, será realizada uma ligação ao aplicativo IFTTT, com a mensagem de erro ocorrida, permitindo assim que o usuário acesso a site e faça o registro manualmente.


### Informações importantes

* O código pode ser definido para executar em um agendados de tarefas. Exxecute inicialmente o arquivo 'daily_execution.py'. 

* Todas as informações durante a execução ficarão disponíveis em log, para auxiliar em correções futuras.

* Os dados de acesso do usuário poderão ser adicionados no arquivo 'app_data.json', para facilitar alterações, caso necessário.