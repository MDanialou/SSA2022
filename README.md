# SSA_PCOM7E | DEVELOPMENT TEAM PROJECT - CODE DEVELOPMENT

---

# Prerequisite
The following should be installed already before setup.
- Python3 ([Download](https://www.python.org/) 3.6 or later.)

# Requirements
```
pip install -r requirements.txt
```

# Programs
Running in Linux or Windows from the downloaded directory.

Run to begin publishing encrypted meter data to the public broker:
```
python3 /PATH/encrypted_smart_meter.py
```

Run to retrieve and decrypt meter data:
```
python3 /PATH/subscriber_app.py
```
Decrypted meter output will be displayed:
```
Total Units =  42
Total Cost (@£0.00039 per unit): £ 0.0164
message topic= UNITS1221
message qos= 1
message retain flag= 0
cipher =  <cryptography.fernet.Fernet object at 0x104c554b0>
message =  <paho.mqtt.client.MQTTMessage object at 0x1048ff220>
message payload =  b'gAAAAABjJh-ggjEprmISiulhyDIVqwRIgHJnSjdNsIdv_rCJ4rUWOWNYdKSV3IHB3GuWZ__PA0HtlS5aKMwbvmcSnFBiNes1-w=='

Total Units =  48
Total Cost (@£0.00039 per unit): £ 0.0187
message topic= UNITS1221
message qos= 1
message retain flag= 0
cipher =  <cryptography.fernet.Fernet object at 0x104c55540>
message =  <paho.mqtt.client.MQTTMessage object at 0x1048ff220>
message payload =  b'gAAAAABjJh-iO1LtsJEIiRjizOdHGQvvjRlFwRegtOcY4BX7oGT6q5-Ir5HtHt60W4Wy16Qr3O-46_0L-hyfYhHUDZD32A3HYQ=='

Total Units =  48
Total Cost (@£0.00039 per unit): £ 0.0187
message topic= UNITS1221
message qos= 1
message retain flag= 0
cipher =  <cryptography.fernet.Fernet object at 0x104c555d0>
message =  <paho.mqtt.client.MQTTMessage object at 0x1048ff220>
message payload =  b'gAAAAABjJh-kBWxOWLFy3DZezipMXjHoGF0IvfvwabG7JD66KQusZ3Y0UzeFtlW9qbCvVW40ZbQO2LvVjsgk8BcIj2r6fUf2aA=='

Total Units =  52
Total Cost (@£0.00039 per unit): £ 0.0203
message topic= UNITS1221
message qos= 1
message retain flag= 0
```
