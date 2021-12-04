import paho.mqtt.client as mqtt
import time
import getch

broker="127.0.0.1"
pub = mqtt.Client("Publisher") #Creating a Client Instance: client =mqtt.Client(client_name)
pub.connect(broker)  #establish connection to a broker

#========================================
#Once we have a connection established we can start to publish messages.
#To do this we use the publish method.

while True:
    msg = input("Please enter the message: ")
    pub.publish("mqtt/printer",msg)
    print("Published message to topic","mqtt/printer")
    time.sleep(1)
    print('Press esc to quit program or any other key to continue')
    print('\n')
    c = getch.getch()
    if c == chr(27):
        print("exiting")
        pub.disconnect()
        break
    else:
        pass
#========================================
