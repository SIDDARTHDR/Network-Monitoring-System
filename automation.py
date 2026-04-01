import os

def restart_interface(ip):
    print(f"[AUTO-ACTION] Attempting fix for {ip}")

    # Example: restart network (Windows)
    os.system("netsh interface set interface name=\"Wi-Fi\" admin=disable")
    os.system("netsh interface set interface name=\"Wi-Fi\" admin=enable")

    print(f"[AUTO-ACTION] Interface restarted for {ip}")
    