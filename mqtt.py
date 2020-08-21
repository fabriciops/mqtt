import paho.src.paho.mqtt.client as mqtt
import ssl
import sys

#definições
broker = "0.0.0.0"
portaBroker = 1883
keepAliveBroker = 60
topicoSuncribe ="teste" #topico de subcribe

#callback - conexão ao broker realidade
def on_connect(client, userdata, flags, rc):
    print("[STATUS] Conected (%s) " % client._client_id)
    client.subcribe(topic="teste", qos=2)

#calback - message received from the broker
def on_message( client, userdata, message):
    print("-------------------------------")
    print('topic: %s' % message.topic)
    print('payload: %s' % message.payload)
    print('qos: %s' % message.qos)
    

def main():
        
    try:
        print("[STATU] Starting MQTT...")
        client = mqtt.Client()
        # client = mqtt.Client(client_id='Fabricio', clean_session=False)
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(broker, portaBroker, keepAliveBroker)
        client.loop_forever()

    except KeyboardInterrupt:
        print("\Ctrl+c stop system")
        sys.exit(0)

#main

main()

