from scapy.all import sniff, IP, TCP, UDP, Raw


def packet_callback(packet):

    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        protocol_name = "Other"
        if proto == 6:
            protocol_name = "TCP"
        elif proto == 17:
            protocol_name = "UDP"
        elif proto == 1:
            protocol_name = "ICMP"

        print(
            f"\n[+] Packet Captured: {ip_src} ----({protocol_name})----> {ip_dst}")

        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print(f"    [Payload Data]: {str(payload)[:100]}")


def main():
    print("="*60)
    print("        CODE ALPHA - BASIC NETWORK SNIFFER (WINDOWS 11)        ")
    print("="*60)
    print("[*] Initializing sniffer... Press Ctrl+C to stop.")

    sniff(prn=packet_callback, store=False)

    from scapy.all import sniff, IP, TCP, UDP, Raw


def packet_callback(packet):

    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        protocol_name = "Other"
        if proto == 6:
            protocol_name = "TCP"
        elif proto == 17:
            protocol_name = "UDP"
        elif proto == 1:
            protocol_name = "ICMP"

        print(
            f"\n[+] Packet Captured: {ip_src} ----({protocol_name})----> {ip_dst}")

        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print(f"    [Payload Data]: {str(payload)[:100]}")


def main():
    print("="*60)
    print("        CODE ALPHA - BASIC NETWORK SNIFFER (WINDOWS 11)        ")
    print("="*60)
    print("[*] Initializing sniffer... Press Ctrl+C to stop.")

    sniff(prn=packet_callback, store=False)


if __name__ == "__main__":
    main()
