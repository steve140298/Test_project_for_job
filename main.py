import callback
import os
import paho.mqtt.client as mqtt
import request
import ssl
from dotenv import load_dotenv

# Loading the .env file
load_dotenv()

# Load broker and port
broker = 'test.mosquitto.org'
port = 8885

# Loading login and password from .env file
login = os.getenv('Login')
password = os.getenv('Password')

# Creating topics
temperature_topic = '/api/temperature/'
status_topic = '/api/status'

# Creating client
client = mqtt.Client()

# User authentication
client.username_pw_set(login, password)

# SSL encryption
client.tls_set(ca_certs=None, certfile=None, keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
               tls_version=ssl.PROTOCOL_SSLv23, ciphers=None)

# Connecting a client to a broker
client.connect(broker, port, 60)

# Loading parsed data
weather = request.station_temperature()
status = request.status_api()

# Creating topics, subscribing to them and publishing the temperature of a particular station
for i in weather:
    id_temp = str(i.keys())[12:-3]
    temperature = i.get(id_temp)
    mytopic = temperature_topic + id_temp
    message = temperature
    client.subscribe(mytopic)
    client.publish(mytopic, message)

# Subscribing and publishing API status
client.subscribe(status_topic)
client.publish(status_topic, status)

# Calling functions from callback
client.on_connect = callback.on_connect
client.on_message = callback.on_message
client.on_publish = callback.on_publish
client.on_subscribe = callback.on_subscribe

# Starting an eternal loop
client.loop_forever()


