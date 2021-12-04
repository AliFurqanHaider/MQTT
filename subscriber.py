import paho.mqtt.client as mqtt
import time

#======================================================================    
#When the client receives messages it generate the on_message callback.
def on_message(client, userdata, message):
    print("Received message: " ,str(message.payload.decode("utf-8")).upper())
#======================================================================    

broker="127.0.0.1"
print("creating new client instance")
sub = mqtt.Client("Subscriber") #Creating a Client Instance: client =mqtt.Client(client_name)
sub.connect(broker) #establish connection to a broker

#========================================
#subscribing to a topic
print("Subscribing to topic","mqtt/printer")
sub.subscribe("mqtt/printer")
sub.on_message=on_message        #attach function to callback

sub.loop_forever()
