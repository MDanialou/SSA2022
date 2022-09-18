# SSA_PCOM7E | DEVELOPMENT TEAM PROJECT - CODE DEVELOPMENT

----

## <ins>Prerequisite</ins>
The following should be installed already before setup.
- Python3 ([Download](https://www.python.org/) 3.6 or later.)

## <ins>Requirements</ins>
- **paho-mqtt** (enable apps to connect to a MQTT broker in order to publish messages, as well as subscribe to topics and receive published messages) (paho-mqtt, 2022)
- **cryptography** (contains standard cryptography methods including symmetric cyphers, message digests, and key derivation functions) (cryptography, 2022)
- **fernet** (communication encrypted using it cannot be altered or read without the key) (Fernet (symmetric encryption), 2022)

```
pip install -r requirements.txt
```

## <ins>Programs</ins>
***Running in Linux or Windows from the downloaded directory.***

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

## <ins>Private Broker Program</ins>

***For users with private broker setup (e.g. Eclipse Mosquito)***

Client connect anonymously without TLS
```
mosquitto_sub -t test/topic -h <broker address>
```
Client connect with username and no password without TLS
```
mosquitto_sub -t test/topic -u <username> -h <broker address>
```
Client connect with username and password without TLS
```
mosquitto_sub -t test/topic -u <username> -P <password> -h <broker address>
```
Subscribe to the $SYS topic and see information about the broker
```
mosquitto_sub -t '$SYS/#' -v -h <broker address>
```
Client connect using TLS
```
mosquitto_sub -t test/topic -h <broker address> -p 8883 --capath /etc/ssl/certs
```
Client subscribes to all topics
```
mosquitto_sub -t '#' -v
```
*Repeat all the above when publishing as well.*

## <ins>Reflection</ins>

IoT is a novel architecture concept that enables data transfer and service delivery through networks. It enables users to transform everyday objects into smart devices capable of gathering data and performing tasks, aided by an increasing number of interconnected nodes. The shifting threat landscape and increased amount of sophisticated cyberattacks necessitate creative techniques to characterise and quantify risks to keep systems secure (Kordy et. al., 2014). An IoT network for a smart home has been presented with some threats mitigated. It includes a coordinator, smart video doorbell, and smart energy meter connected via LoRa and MQTT.

Find below threats, how they apply to our IoT network, and mitigation techniques.

| **Threats**                      | **Vulnerable (Y/N)** | **Mitigation Details**                                                                                                             |
| -------------------------------- | -------------------- |------------------------------------------------------------------------------------------------------------------------------------|
| SQL Injection                    | N                    | \- No database is being used in this project                                                                                       |
| Cross Site Scripting (XSS)       | N                    | \- No front-end development                                                                                                        |
| Broken Authentication            | N                    | \- User is prompted to enter a password when connecting to the broker<br/>\- Cipher key being used to encrypt and decrypt messages |
| Privilege Escalation             | N                    | \- User is prompted to enter a password when connecting to the broker                                                              |
| Session Hijack                   | Y                    | \- Public brokers don’t support security certificates to provide authorization                                                     |
| Man in the Middle                | Y                    | \- Public brokers don’t support security certificates to provide authorization                                                     |
| Wireless Key Compromise          | N                    | \- Not applicable for this project                                                                                                 |
| Eavesdropping                    | Y                    | \- Although on an unsecured port (1833), cipher key being used to encrypt and decrypt messages provide confidentiality             |
| Resource Exhaustion              | N                    | \- If an incorrect password is entered, the program ends                                                                           |
| Port Scanning                    | Y                    | \- Using unsecured MQTT port 1833 for transmission as MQTT over SSL on port 8883 is not supported on public brokers                |
| Malicious Code Scanning          | Y                    | \- Malware tools are not being used                                                                                                |
| Connections from unknown devices | N                    | \- User is prompted to enter a password when connecting to the broker<br/>\- Cipher key being used to encrypt and decrypt messages |
| Access and Compromise of Devices | N                    | \- No physical devices                                                                                                             |

A key consideration for this project was where the MQTT broker was hosted - publicly or privately. This determined what technical controls could be employed to mitigate threats based on the inherited vulnerabilities of the MQTT broker. Only the devices you choose can publish to and subscribe to the topics on a private broker. Use this for both production and prototyping. Any device can publish topics on a public broker and subscribe to those topics. There is no privacy, hence should not be used for production, instead for testing/prototyping (Chen, Huo, Zhu and Fan, 2020).

With this project, we’ve achieved confidentiality and availability to a certain degree and lacked in developing controls to strengthen the integrity of our IoT network. This was primarily because we’re using a public MQTT broker and couldn’t configure the broker disabling us from leveraging other security controls. Because MQTT is a simple protocol built for low-powered devices, it seeks to minimise the processing needed to send messages, causing major security issues (Hernández Ramos, S. et al., 2018). Most flaws can be fixed with proper protocol settings on the client and broker. On a private broker, additional security measures could mitigate threats the project is vulnerable to – TLS with certificate credentials for all connections (providing secure authentication and authorization), only TCP/IP ports 8883 would be open on the server (secure MQTT protocol) and limiting MQTT publishing and subscribing (prevent resource exhaustion, assuring availability) (Kotak, J. et al., 2019).

## <ins>References</ins>

Chen, F., Huo, Y., Zhu, J. and Fan, D., 2020. A Review on the Study on MQTT Security Challenge. 2020 IEEE International Conference on Smart Cloud (SmartCloud),.

PyPI. 2022. cryptography. [online] Available at: <https://pypi.org/project/cryptography/> [Accessed 17 September 2022].

Cryptography.io. 2022. Fernet (symmetric encryption). [online] Available at: <https://cryptography.io/en/latest/fernet/> [Accessed 16 September 2022].

Fortinet (N.D.) Eavesdropping. Available from: https://www.fortinet.com/resources/cyberglossary/eavesdropping [Accessed 18 September 2022].

Fortinet. (N.D.) What Is A Port Scan? How To Prevent Port Scan Attacks?. Available from: https://www.fortinet.com/resources/cyberglossary/what-is-port-scan [Accessed 18 September 2022].

Hernández Ramos, S. et al. (2018) MQTT Security: A Novel Fuzzing Approach. Wireless communications and mobile computing. [Online] 20181–11.

Kaspersky. (2019) What is Malicious code?. Available from: https://www.kaspersky.com/resource-center/definitions/malicious-code [Accessed 18 September 2022].

KirstenS. (2020) Cross Site Scripting (XSS). Available from: https://owasp.org/www-community/attacks/xss [Accessed 18 September 2022].

Kotak, J. et al. (2019) ‘A Comparative Analysis on Security of MQTT Brokers’, in 2nd Smart Cities Symposium (SCS 2019). [Online]. 2019 Stevenage, UK: IET. p. 7–.

Levis, M., Helfert, M. & Brady, Malcolm. (2008) Website Design Quality and Form Input Validation: An Empirical Study on Irish Corporate Websites. Journal of Service Science and Management 1(01): 91-100. DOI: https://doi.org/10.4236/jssm.2008.11009

Malgaonkar, S., Patil, R., Rai, A. & Singh, A. (2017) Research on Wi-Fi Security Protocols. International Journal of Computer Applications 164(3): 30-36. DOI: https://doi.org/10.5120/ijca2017913601

Mohamed, T. S. (2019) Security of Multifactor Authentication Model to Improve Authentication Systems. Information and Knowledge Management 6: DOI: https://doi.org/10.13140/RG.2.2.18515.53288

Nife, F. & Kotulski, Z. (2020) Application-Aware Firewall Mechanism for Software Defined Networks. Journal of Network and Systems Management 28: 605-626 DOI: https://doi.org/10.1007/s10922-020-09518-z

NIST (N.D.) man-in-the-middle attack (MitM). Available from https://csrc.nist.gov/glossary/term/man_in_the_middle_attack [Accessed 18 September 2022].

PyPI. 2022. paho-mqtt. [online] Available at: <https://pypi.org/project/paho-mqtt/> [Accessed 18 September 2022].

PortSwigger. (2019) SQL Injection. Available from: https://portswigger.net/web-security/sql-injection [Accessed 18 September 2022].

OWASP. (2017) A2:2017-Broken Authentication. Available from: https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication [Accessed 18 September 2022].

OWASP. (2020) Session hijacking attack. Available from: https://owasp.org/www-community/attacks/Session_hijacking_attack [Accessed 18 September 2022].


