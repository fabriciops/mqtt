# publisher
import paho.src.paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('localhost', 1883)

while True:
    client.publish("LINTANGtopic/test", input('Message : '))
