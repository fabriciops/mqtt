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

#Montar broker
# client.connect('localhost', 8080)

#Utilizando a API do eclipse
client.connect('mqtt.eclipse.org', 1883)

def sendMessage(message):

    msg = message
    client.publish("mqtt/fabricio", (msg))
    main()

def main():

    msg = input("message: ")
    sendMessage(msg)


if __name__ == "__main__": 
    main()
