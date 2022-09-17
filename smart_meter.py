"""Smart_meter script generates simulated energy usage and appends to total
units integer, then transmits this to the server via the public broker
"""
import time
from random import randrange
import paho.mqtt.client as mqtt
from cryptography.fernet import Fernet


def on_connect(client, userdata, flags, r_c):
    """Check connection"""
    if r_c == 0:
        print("Connected")
        # Subscribe to TOPIC 2 with QOS = 1
        sub(client, TOPIC2, QOSS)
    else:
        print("Not connected")


def on_message(client, userdata, message):
    """On receiving new message:
    Decrypt message, convert to integer, display to user the units and
    set msgflag to True for handling running total (without resetting to 0)
    then kick off publish function"""
    decrypted_message = CIPHER.decrypt(message.payload)
    msg = int(decrypted_message.decode("utf-8"))
    print("Unit total from server = ", str(decrypted_message.decode("utf-8")))
    pub(client, TOPIC1, msg, QOSS)


def sub(client, topic, qos):
    """Subscribe to TOPIC2"""
    client.subscribe(topic, qos)


def pub(client, topic, msg, qos):
    """Publish encrypted unit total (simulated by adding a random numer)"""
    msg = msg + randrange(10)
    message = str(msg)
    encrypted_message = CIPHER.encrypt(message.encode())
    out_message = encrypted_message.decode()
    client.publish(topic, out_message, qos, True)
    time.sleep(4)


# Set Constants for smart meter
QOSS = 1
BROKER = 'broker.emqx.io'
TOPIC1 = "UNITS1221"
TOPIC2 = "UNITS1222"
PORT = 1883
CIPHER_KEY = b'70JZaJg4c5F7RIOhrSXNjq0Y0iGp1QtBy2gyVMSdHHY='
CIPHER = Fernet(CIPHER_KEY)

# Setup client, connect to broker, and register callbacks to functions
client = mqtt.Client("Smart_Meter")
client.connect(BROKER, PORT)
client.on_connect = on_connect
client.on_message = on_message

# Check message buffers
while True:
    client.loop_start()
    time.sleep(2)
    client.loop_stop()
