O arquivo Broker nesse projeto não esta sendo utilizado.

Para trabalhar com esse repositório, basta fazer as instalações das dependências e utilizar o pub.py que será o emissor e os demais arquivos "rasp1.py e rasp2.py"
simulando o recptor que receberá uma mensagem ou objeto.

O objetivo desse projeto é alimentar uma variável cache toda vez que houver um cadastro na base de dados.

# mqtt
O projeto / experimento consistirá de uma aplicação Python capaz de escrever na tela todas as mensagens recebidas pelo broker em um determinado tópico.

Você pode instalar de forma global https://pypi.org/project/paho-mqtt/

Ou utilizar o dir "paho", diretamente no projeto.



Eclipse Mosquitto é um agente de mensagens de código aberto que implementa MQTT versão 5, 3.1.1 e 3.1

docker pull eclipse-mosquitto

Configuração
Ao executar a imagem, os valores de configuração padrão são usados. Para usar um arquivo de configuração personalizado, monte um arquivo de configuração local para/mosquitto/config/mosquitto.conf

$ docker run -it -p 1883:1883 -p 9001:9001 -v mosquitto.conf:/mosquitto/config/mosquitto.conf eclipse-mosquitto
A configuração pode ser alterada para:

persistir dados para /mosquitto/data
logar para /mosquitto/log/mosquitto.log
ou seja, adicione o seguinte a mosquitto.conf:

persistence true
persistence_location /mosquitto/data/
log_dest file /mosquitto/log/mosquitto.log
Nota : Se um volume for usado, os dados persistirão entre os contêineres.

Run
Execute um contêiner usando a nova imagem:

$ docker run -it -p 1883:1883 -p 9001:9001 -v mosquitto.conf:/mosquitto/config/mosquitto.conf -v /mosquitto/data -v /mosquitto/log eclipse-mosquitto
Nota : se a configuração mosquitto (mosquitto.conf) foi modificada para usar portas não padrão, o comando docker run precisará ser atualizado para expor as portas que foram configuradas.
