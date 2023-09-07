# The callback for when the client receives a CONNACK response from the server.
from datetime import datetime as dt
from paho.mqtt.client import connack_string as ack

# The callback for when the client connects to the broker the function return 0 if all good
def on_connect(client, userdata, flags, rc, v5config=None):
    print(dt.now().strftime("%H:%M:%S.%f")[:-2] + " Connection returned result: "+ack(rc))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, message,tmp=None):
    print(dt.now().strftime("%H:%M:%S.%f")[:-2] + " Received message " + str(message.payload) + " on topic '"
        + message.topic + "' with QoS " + str(message.qos))


# The callback for when a PUBLISH message is sent to the server.
def on_publish(client, userdata, mid,tmp=None):
    print(dt.now().strftime("%H:%M:%S.%f")[:-2] + " Published message id: "+str(mid))


# The callback for when a client SUBSCRIBE to the topic
def on_subscribe(client, userdata, mid, qos,tmp=None):
    if isinstance(qos, list):
        qos_msg = str(qos[0])
    else:
        qos_msg = f"and granted QoS {qos[0]}"
    print(dt.now().strftime("%H:%M:%S.%f")[:-2] + " Subscribed " + qos_msg)
