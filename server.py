"""Server script receives total energy units used
from the smart meter via the public broker
"""
import time
import paho.mqtt.client as mqtt
from cryptography.fernet import Fernet


def on_connect(client, userdata, flags, r_c):
    """Check connection"""
    if r_c == 0:
        print("Connected\n")
        # Subscribe to TOPIC 1 with QOS = 1
        sub(client, TOPIC1, QOSS)
    else:
        print("Not connected\n")


def on_message(client, userdata, message):
    """On receiving a message:  decrypt it, convert to an integer
    display the number of units used and current cost (to 4 x decimal points)
    kick off the publish function."""
    decrypted_message = CIPHER.decrypt(message.payload)
    msg = int(decrypted_message.decode("utf-8"))
    print("Total Units = ", str(decrypted_message.decode("utf-8")))
    rounded = msg * 0.00039
    print("Total Cost (@£0.00039 per unit): £", round(rounded, 4))
    pub(client, TOPIC2, msg, QOSS)


def pub(client, topic, msg, qos):
    """Confirm total back to smart meter, encrypted via TOPIC2
    (used to prevent unit total resetting to 0)."""
    message = str(msg)
    encrypted_message = CIPHER.encrypt(message.encode())
    out_message = encrypted_message.decode()
    client.publish(topic, out_message, qos)
    time.sleep(4)


def sub(client, topic, qos):
    """Subscribe to TOPIC1 with QOS = 1."""
    client.subscribe(topic, qos)


# Set Constants for server
QOSS = 1
BROKER = "broker.emqx.io"
TOPIC1 = "UNITS1221"
TOPIC2 = "UNITS1222"
PORT = 1883
CIPHER_KEY = b'70JZaJg4c5F7RIOhrSXNjq0Y0iGp1QtBy2gyVMSdHHY='
CIPHER = Fernet(CIPHER_KEY)

inp = input("Welcome to the SSA prototype:\n Press ENTER to connect to broker")

# Setup client, connect to broker, and register callbacks to functions
client = mqtt.Client("ServerSSA")
client.connect(BROKER, PORT)
client.on_connect = on_connect
client.on_message = on_message

# Check message buffers
client.loop_start()
time.sleep(2)

# Give the user a way to end the program
inp = input("\nWaiting to continue.  Press ENTER any time to end program)\n")
print("Ending")
client.loop_stop()
