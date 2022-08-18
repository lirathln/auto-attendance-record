# Auto Attendance Record
Automation created to register attendance on the Pontomais website.
![logo da aplicação](https://uploaddeimagens.com.br/images/003/986/262/original/Automação.jpg?1660848656)

<center>

| [Descrição](#descrição) | [Funcionalidades](#funcionalidades) | [Executar Projeto](#executar-projeto) | [Tecnologias Utilizadas](#tecnologias-utilizadas) | [Autor](#autor) |
|:-----------:|:-----------------:|:------------------:|:------------------------:|:-------:|

</center>
<br/><br/>

## Descrição
Código criado com o intuito de registro automático de frequência no site [Pontomais](https://pontomais.com.br).
A implementação ocorreu em uma versão anterior do sistema, portanto, poderá não executar devidamente, devido mensagens e links modificados ao longo do tempo.
<br/><br/>

## Status
:white_check_mark: **Projeto finalizado** :white_check_mark:
<br/><br/>

## Funcionalidades
- **`Verificação de Google Calendar`**: Verificação do calendário pessoal do usuário, através de liberação ao [Google Calendar](https://calendar.google.com/calendar/), buscando por evento nomeado 'Trabalho'. Esse evento deverá conter o horário para registro dos ponto na descrição do evento, por exemplo: 
    
        :clock3: 08:00;12:00;14:00;18:00

    **Obs.:** Os horários deverão ser separados por ponto e vírgula (;), para que o código consiga separar os dados.

     **Obs.:** O código fará o agendamento para execução nos horários especificados nessa descrição.

- **`Instância de browser invisível`**: O código fará a criação de uma instância do [Google Chrome](https://chromedriver.chromium.org/downloads) por meio da ferramenta [Selenium](https://www.selenium.dev), para acesso ao site da frequência. Essa instãncia é executada em segundo plano, não interrompendo seu uso ou abrindo nenhuma interface gráfica.

- **`Automação de acesso e registro de ponto`**: O código fará o acesso ao site da Pontomais, com os usuário informadosno arquivo 'app_data.json' e tentará realizar o registro da frequência, sem qualquer necessidade de entradas pelo usuário.

- **`Fique por dentro de tudo`**: Todas as informações durante a execução ficarão disponíveis em log, para auxiliar correções futuras.

- **`Sem necessidade de entradas manuais`**: Agende no Agendador de Tarefas de seu computador, com a ação de executar o arquivo 'daily_execution.py'. Os dados de acesso do usuário poderão ser adicionados no arquivo 'app_data.json', para automatizar totalmente seu acesso e registro, além disso, serve para facilitar alterações, caso seja necessário.

- **`Notificação personalizada`**: Caso obtenha sucesso no registro, será encaminhada uma mensagem de sucesso ao aparelho celular do usuário, pelo aplicativo [IFTTT](https://ifttt.com). Entretanto, caso o código não obtenha sucesso, será realizada uma ligação ao aplicativo [IFTTT](https://ifttt.com), com a mensagem de erro ocorrida (ditada por bot), permitindo assim que o usuário acesso a site e faça o registro manualmente.
<br/><br/>

## Executar Projeto
Após baixar o projeto, você pode abrí-lo com o [Visual Studio Code](https://code.visualstudio.com/download), ou qualquer outro editor / IDE de sua preferência.

* Garanta que você tenha o Python instalado em seu computador, priorize usar a versão **[3.6](https://www.python.org/downloads/)** em diante;

* Faça a importação dos requerimentos, que constam no projeto como 'requirements.txt';  

        pip install -r /path/to/requirements.tx

* Crie suas [credenciais no Google Workspace](https://developers.google.com/workspace/guides/create-credentials), para obter sua ID e SECRET e altere-as no arquivo 'credentials_google.json';

* Crie um trigger no site IFTTT para receber as notificações e ligações do código;

* Preencha o arquivo 'app_data.json' com seus dados de acesso ao Pontomais;

* Execute o arquivo 'daily_verification.py', para iniciar toda a execução do código.
Obs.: Para uma automação total da tarefa, faça o agendamento dessa etapa pelo Agendador de Tarefas em seu computador.
<br/><br/>

## Tecnologias Utilizadas
* `Python`
* `Selenium`
* `Google Workspace`
* `IFTTT`
<br/><br/>

## Autor
[<img src="https://avatars.githubusercontent.com/u/64272235?s=96&v=4&h=300&w=300&fit=cover&mask=circle&maxage=7d" width=115/><br><sub>Thalyson Lira Nunes</sub>](https://github.com/lirathln)