# publisher
import paho.mqtt.client as mqtt

# config_data={
#     "temperature":"45",
#     "humidity":"90",
#     "location":{
#         "latitude":"45.56565",
#         "longitude":"88.418556"
#     }
# }

client = mqtt.Client()
client.connect('mqtt.eclipse.org', 1883)

while True:
    
    client.publish("mqtt/fabricio", input('Message : '))
