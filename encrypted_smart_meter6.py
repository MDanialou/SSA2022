import paho.mqtt.client as mqtt
from random import randrange, uniform
import time
from cryptography.fernet import Fernet

client = mqtt.Client("smart_meter")
client.username_pw_set("username", "password")
client.connect("broker.emqx.io", 1883)
username = 'emqx'
password = 'public'

cipher_key = b'70JZaJg4c5F7RIOhrSXNjq0Y0iGp1QtBy2gyVMSdHHY='
cipher = Fernet(cipher_key)


sum_of_units = 0
while True:
    sum_of_units = sum_of_units + randrange(10)
    message = str(sum_of_units)
    encrypted_message = cipher.encrypt(message.encode())
    out_message = encrypted_message.decode()
    client.publish("UNITS1221", out_message, qos = 1)    
    print("Published " + message + " to Topic UNITS1221")
    print("Encrypted as " + out_message + " to Topic UNITS1221")
    time.sleep(2)