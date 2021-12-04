Instructions!

- First step is to run the mosquitto server in linux by typing 'mosquitto -v' command in the terminal. All of the control messages will be displayed on this console.

- Open another terminal and type 'python3 subscriber.py' to run the subscriber client. All the received messages on the topic 'mqtt/printer' will be shown on this console.

- Open another terminal and type 'python3 publisher.py' to run the publisher client. From this console the messages will be typed and sent to the topic 'mqtt/printer'.

Please find the 'subscriber.py' and 'publisher.py' files in this folder. Also see the screenshoot of output.
