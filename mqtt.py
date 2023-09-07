import paho.mqtt.client as mqtt

client_get = mqtt.Client(client_id='my_client', protocol=mqtt.MQTTv31)
client_get.connect('test.mosquitto.org', 1883)
client_get.loop_start()

def callback(client, userdata, message):
    print(str(message.payload.decode("utf-8")))

client_get.on_message = callback
client_get.subscribe('topic', qos=1)