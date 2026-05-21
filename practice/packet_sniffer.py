from scapy.all import sniff, IP

# Process captured packets
def process_packet(packet):

    if packet.haslayer(IP):

        ip_layer = packet[IP]

        print("\n--- Packet Captured ---")
        print(f"Source IP      : {ip_layer.src}")
        print(f"Destination IP : {ip_layer.dst}")
        print(f"Protocol       : {ip_layer.proto}")

# Start sniffing
def start_sniffing():
    print("Sniffing network packets...")
    print("Press Ctrl + C to stop.\n")

    sniff(
        prn=process_packet,
        store=False
    )

# Main
if __name__ == "__main__":
    start_sniffing()