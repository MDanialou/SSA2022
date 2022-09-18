# SSA_PCOM7E | DEVELOPMENT TEAM PROJECT - CODE DEVELOPMENT

----

## <ins>Prerequisite</ins>
The following should be installed already before setup.
- Python3 ([Download](https://www.python.org/) 3.6 or later.)

## <ins>Requirements</ins>
- **paho-mqtt** (enable apps to connect to a MQTT broker in order to publish messages, as well as subscribe to topics and receive published messages) (paho-mqtt, 2022)
- **cryptography** (contains standard cryptography methods including symmetric cyphers, message digests, and key derivation functions) (cryptography, 2022)
- **fernet** (communication encrypted using it cannot be altered or read without the key) (Fernet (symmetric encryption), 2022)
- **pandas** (data analysis and manipulation)

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

## <ins>Design Document - Threats and Mitigations</ins>

### **Threats**

| **Application Threats**    | **Description**                                                                                                                                              |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| SQL Injection              | Web application vulnerability allowing attackers to manipulate databases through queries (PortSwigger, 2019)                                                 |
| Cross Site Scripting (XSS) | Malicious scripts injected into web forms giving unauthorised access to sensitive files such as session cookies, allowing session hijacking (KirstenS, 2020) |
| Broken Authentication      | Exploits credentials allowing privileged account access (OWASP, 2017)                                                                                        |
| Privilege Escalation       | Programming errors could allow attackers unauthorised access to applications and privileged resources (OWASP, 2020)                                          |

| **Network Threats**              | **Description**                                                                                                                         |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Session Hijack                   | Exploits web session control mechanisms.  Gives unauthorised webserver access using compromised session tokens (OWASP, 2020)            |
| Man in the Middle                | Attacker positioned between two communicating parties manipulates passing data, compromising integrity and confidentiality (NIST, N.D.) |
| Wireless Key Compromise          | Wireless key obtained and used for unauthorised resource access                                                                         |
| Eavesdropping                    | Hackers intercept unencrypted data transmitted between two devices (Fortinet, N.D.)                                                     |
| Resource Exhaustion              | Exploits vulnerabilities, compromising service availability and rendering legitimate service unavailable (Antunes et al., 2008)         |
| Port Scanning                    | Used to discover open services or weak entry points in networks and systems (Fortinet, N.D.)                                            |
| Malicious Code Download          | Downloading harmful programs to exploit system vulnerabilities (Kaspersky, 2019)                                                        |
| Connections from unknown devices | Connections of unsolicited devices, leaving the IoT network compromised                                                                 |

| **Physical Threat**               | **Description**                             |
| --------------------------------- | ------------------------------------------- |
| Access and Compromise of Devices. | Physical breach, damage or theft of devices |


### **Threat Mitigations**

| **Application Threat Mitigations**                      | **Description**                                                                                                                                                           |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Layer 7 Firewall with DDoS capability                   | Firewall accepting traffic on ports but blocking traffic containing known vulnerabilities through deep packet inspection (Nife & Kotulski, 2020).  Can detect DoS attacks |
| Input Validation / Sanitisation                         | Prevents execution of malicious queries designed for unauthorised data access (Levis et al., 2008)                                                                        |
| Strict Authentication (Unique IDs and Strong Passwords) | Mitigates authentication-based attacks as attackers are less likely to guess user credentials                                                                             |
| Multi Factor Authentication                             | Further mitigates unauthorised system access (Mohamed, 2019)                                                                                                              |
| Standard User accounts with restricted privileges       | Limits the damage extent, if compromised                                                                                                                                  |

| **Network Threat Mitigations**                                                | **Description**                                                                                    |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| WPA2 (or greater) Wireless Encryption                                         | Provides data encryption by TKIP which used strong encryption mechanisms (Malgaonkar et al., 2017) |
| In-built TPM chip for IoT devices and coordinator                             | Supports cryptographic algorithms and secure boot on devices                                       |
| Patch Management                                                              | Continuous mitigation of discovered IoT vulnerabilities                                            |
| Credential hygiene (e.g., change default credentials and keeping them secret) | Minimises the chance of credentials being guessed.                                                 |

| **Physical Threat Mitigations**      | **Description**                                                           |
| ------------------------------------ | ------------------------------------------------------------------------- |
| External door locks                  | Prevents unauthorised access to facilities where IoT equipment is located |
| External walls and gate, if possible | Deters and delays intruders                                               |


## <ins>Reflection</ins>

600 WORD REFLECTION - WORKING ON IT


|             Threats              | Mitigated (Y/N) |
|:--------------------------------:|:---------------:|
|          SQL Injection           |        N        |
|    Cross Site Scripting (XSS)    |        N        |
|      Broken Authentication       |        N        |
|       Privilege Escalation       |        N        |
|          Session Hijack          |        N        |
|        Man in the Middle         |        Y        |    
|     Wireless Key Compromise      |        N        |
|          Eavesdropping           |        Y        |
|       Resource Exhaustion        |        Y        |
|          Port Scanning           |        Y        |
|     Malicious Code Scanning      |        Y        |
| Connections from unknown devices |        Y        |
| Access and Compromise of Devices |        Y        |


## <ins>References</ins>

PyPI. 2022. cryptography. [online] Available at: <https://pypi.org/project/cryptography/> [Accessed 17 September 2022].

Cryptography.io. 2022. Fernet (symmetric encryption). [online] Available at: <https://cryptography.io/en/latest/fernet/> [Accessed 16 September 2022].

Fortinet (N.D.) Eavesdropping. Available from: https://www.fortinet.com/resources/cyberglossary/eavesdropping [Accessed 28 August 2022].

Fortinet. (N.D.) What Is A Port Scan? How To Prevent Port Scan Attacks?. Available from: https://www.fortinet.com/resources/cyberglossary/what-is-port-scan [Accessed 28 August 2022].

Kaspersky. (2019) What is Malicious code?. Available from: https://www.kaspersky.com/resource-center/definitions/malicious-code [Accessed 28 August 2022].

KirstenS. (2020) Cross Site Scripting (XSS). Available from: https://owasp.org/www-community/attacks/xss [Accessed 28 August 2022].

Levis, M., Helfert, M. & Brady, Malcolm. (2008) Website Design Quality and Form Input Validation: An Empirical Study on Irish Corporate Websites. Journal of Service Science and Management 1(01): 91-100. DOI: https://doi.org/10.4236/jssm.2008.11009

Malgaonkar, S., Patil, R., Rai, A. & Singh, A. (2017) Research on Wi-Fi Security Protocols. International Journal of Computer Applications 164(3): 30-36. DOI: https://doi.org/10.5120/ijca2017913601

Mohamed, T. S. (2019) Security of Multifactor Authentication Model to Improve Authentication Systems. Information and Knowledge Management 6: DOI: https://doi.org/10.13140/RG.2.2.18515.53288

Nife, F. & Kotulski, Z. (2020) Application-Aware Firewall Mechanism for Software Defined Networks. Journal of Network and Systems Management 28: 605-626 DOI: https://doi.org/10.1007/s10922-020-09518-z

NIST (N.D.) man-in-the-middle attack (MitM). Available from https://csrc.nist.gov/glossary/term/man_in_the_middle_attack [Accessed: 29 August 2022].

PyPI. 2022. paho-mqtt. [online] Available at: <https://pypi.org/project/paho-mqtt/> [Accessed 18 September 2022].

PortSwigger. (2019) SQL Injection. Available from: https://portswigger.net/web-security/sql-injection [Accessed 28 August 2022].

OWASP. (2017) A2:2017-Broken Authentication. Available from: https://owasp.org/www-project-top-ten/2017/A2_2017-Broken_Authentication [Accessed 28 August 2022].

OWASP. (2020) Session hijacking attack. Available from: https://owasp.org/www-community/attacks/Session_hijacking_attack [Accessed 28 August 2022].


