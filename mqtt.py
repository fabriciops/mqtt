import paho.src.paho.mqtt.client as mqtt
import sys

#definições
broker = "0.0.0.0"
portaBroker = 1883
keepAliveBroker = 60
topicoSuncribe ="PAHOMQTTRasPi4" #topico de subcribe

#callback - conexão ao broker realidade
def on_connect(client, userdata, flags, rc):
    print("[STATUS] Conected to the broker. REsult: " +str(rc))

    #maked subscibe automatic on the topic
    client.subcribe(topicoSuncribe)

#calback - message received from the broker
def on_message( client, userdata, message):

    messageReceived = str(msg.payload)

    print("[MSG RECEIVED] Topic: "+message.topic+" /Message: "+messageReceived)

def main():
        
    try:
        print("[STATU] Starting MQTT...")
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        client.connect(broker, portaBroker, keepAliveBroker)
        client.loop_forever()

    except KeyboardInterrupt:
        print("\Ctrl+c stop system")
        sys.exit(0)