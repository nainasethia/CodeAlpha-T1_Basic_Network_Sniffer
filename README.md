# CodeAlpha Basic Network Sniffer

## Overview

In cybersecurity, visibility is everything—without insight into network activity, defending against threats becomes nearly impossible. This project, developed during my cybersecurity internship at CodeAlpha, focuses on building a **Basic Network Sniffer** using Python.

The tool captures live network traffic and analyzes it by extracting key details such as IP addresses, transport protocols, and raw payload data. It provides a clear understanding of how data flows across a network and highlights potential security risks like unencrypted transmissions.

---

## Key Features

- Captures live network packets using the Scapy library
- Extracts source and destination IP addresses (Layer 3)
- Identifies transport protocols such as TCP, UDP, and ICMP (Layer 4)
- Retrieves and displays raw packet payloads in a readable format

---

## Requirements

Before running the project, ensure you have:

- Python 3 installed
- Scapy library installed (`pip install scapy`)

---

## Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/YOUR_USERNAME/CodeAlpha_BasicNetworkSniffer.git
   cd CodeAlpha_BasicNetworkSniffer
   ```

2. Install required dependencies:

   ```bash
   pip install scapy
   ```

3. Run the script with administrator privileges:

   ```bash
   python sniffer.py
   ```

---

## Project Goals

This project was designed to achieve the following:

- Capture and analyze network packets in real time
- Break down packet structures to understand protocols like TCP, UDP, and ICMP
- Inspect payload data to detect unencrypted or sensitive information
- Configure and work with network drivers (Npcap) on Windows systems
- Deliver a well-documented and professional project using version control

---

## Tools and Technologies

- **Command Prompt / PowerShell (Admin Mode):** Required to access network interfaces and enable packet capture
- **Visual Studio 2022:** Used for writing, debugging, and managing Python code
- **GitHub:** Used for version control and hosting the project repository

---

## Skills Developed

Working on this project helped strengthen several important cybersecurity skills:

- Understanding real-time packet flow and network communication
- Using Python and Scapy for network-level automation
- Troubleshooting Windows networking restrictions and driver dependencies
- Developing a security-focused mindset by identifying risks in unencrypted traffic

---

## Importance in Cybersecurity

Network sniffing plays a crucial role in both security and system management:

- **Threat Detection:** Helps identify suspicious activity such as unauthorized connections or data leaks
- **Security Auditing:** Ensures sensitive information is not transmitted without encryption
- **Network Troubleshooting:** Assists in diagnosing connectivity issues, packet loss, and misconfigurations

---

## Implementation Steps

1. Installed Scapy on Windows using `pip install scapy`
2. Created a project directory named `CodeAlpha_BasicNetworkSniffer`
3. Developed the packet-sniffing script using Python
4. Generated network traffic by pinging external servers (e.g., google.com)
5. Executed the script in administrator mode to capture live packets

---

## Final Summary

This project demonstrates the successful development of a basic packet-sniffing tool on a Windows 11 system using Python and Scapy. By integrating the Npcap driver, the tool captures live network data, identifies key protocols, and displays payload information in real time.

The project highlights the importance of packet-level monitoring in cybersecurity, emphasizing how visibility into network traffic enables organizations to detect vulnerabilities, prevent data exposure, and respond effectively to potential threats.

---

## 📌 Project By

**Naina Sethia**  
CodeAlpha Cybersecurity Intern
