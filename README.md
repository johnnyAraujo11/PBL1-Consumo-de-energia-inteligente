

<h1 align="center">PBL-Consumo-de-energia-inteligente</h1>
Com o objetivo de automatizar o processo de obteção de energia elétrica de casa e proatividade de reparos nos medidores, bem como a concientização dos usuários sobre o consumo de energia foi pensado em um dispositivo que monitora o uso de energia elétrica das casas.
Esse dispositivo envia dados constantimente para o servidor da concessionária armazenando os dados referentes a cada dispositivo. Nesse contexto o clientes podem acessar os dados dos consumo especificando um intervalo de dadas e horas desejáveis, receber alertas de variação de consumo ou consumo execessivo de energia elétrica.

<h2>Restrições:</h2>

i) O sistema dever desenvolvido e testado através de um container docker;</br>
ii) As intefaces devem ser desenvolvidas baseado em uma API REST e testadas através do Isominia ou Postman;</br>
iii) Os dados gerado pelos dispositivos devem ser simulados por software e testado em um container docker separado em cada máquina;</br>
iv) Uma interface para poder aumentar ou diminuir o consumo de energia;</br>
v) Nenhum framework deve ser utilizado, apenas as bibliotecas nativas da linguagem escolhida.</br>


<h2>Tecnologias utilizadas no desenvolvimento:</h2>

linguagem: python3.10.6
Virtualização: docker
Ambiente de testes do cliente: Insomina


Para criar o servidor centralizado, onde serão recebido os dados, tanto das requisições do cliente quanto os dados dos dispositivos foi utilizado o socket. o socket permite a comunicação entre processos que executam em máquinas diferentes, funcionado na arquitetura Cliente/servidor.


<h2 align="center"><a href="https://www.hostgator.com.br/blog/o-que-e-protocolo-tcp-ip/">TCP/IP</a></h2>

Foi utilizado o TCP/IP, Transmission Control Protocol(TCP) e IP(IP address) entre a comunição do cliente com o servidor fazendo as requisições e enviando dados e a dos dispositivos. Esses protocolos funcionam em cima de outros protocolos como, por exemplo, o protocolo de transferência de dados, HTTP(Hypertext Transfer Protocol). O TCP/IP possui 4 camadas, no qual foram abstraídas das camadas do modelo OSI que possui 7 camadas, são elas: Aplicação, Transporte, Elance e Rede. 
Focando na camada de transporte onde é específicado a maneira como enviar os dados por TCP ou UDP  (User Datagram Protocol). No TCP o envio dos dados passar por uma série etapas para garantir que o destinatário receba a mensagem. já no protocolo UDP não necessita estabelecer uma conexão e os dados enviados não são garantidos que chegue ao destino indicado. A vantagem da utilizição do UPD é que ele é mais rápido que o TCP.

<h2 align="center"><a href="">Thread</h2>


<h2 align="center"><a href="">Docker</h2>


<h2>Desenvolvimento</h2>

Foi utilizado o protocolo http para a comunicação entre o cliente(Insomina) e o servidor e UDP entre o dispositivo e o servidor.
No código descrito foram utilizadas de threads para que o programa contínue a esperar requisições de usuários e dispositivos.


<h3>Instruções:</h3>

 ```sh
 1. git clone "https://github.com/johnnyAraujo11/PBL1-Consumo-de-energia-inteligente.git"
 ```
 2. Entrar na pasta Controller.
 3. Você pode optar por usar um ambiente ou ir direto para o passo 4:

    ```sh
    python3 -m venv venv
    ```
    No Windows, use:
    
    ```sh
     venv\Scripts\activate.bat
     ```

    No Linux, use:
    ```sh
     source venv/bin/activate
    ```
4. Executando o servidor: 

    ```sh
    python3 main.py
    ```

Após executar o código você poderá observar no terminal que o server estará esperando as mensagem do dispositivo ou do cliente nas portas especificadas.

5. O mesmo processo pode ser realizado para executar o dispositivo.
    1. Entrar na pasta Measurer a partir de outro terminal

    2. Criar um ambiente virtual(opcional)

    3. Executar o dispositivo:

    ```sh
    measurer.py
    ```


<h2>Insomia</2>

[![Run in Insomnia}](https://insomnia.rest/images/run.svg)](https://insomnia.rest/run/?label=Teste%20API&uri=https%3A%2F%2Fraw.githubusercontent.com%2FjohnnyAraujo11%2FPBL1-Consumo-de-energia-inteligente%2Fdev%2FInsomnia_2023-03-20.json)