import requests
import json
import time
import sys

#sys.argv[1] = site
#sys.argv[2] = dns type

def go(site, dns_type):
    API_KEY="YOUR API KEY HERE"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36"} 
    r = requests.get("https://api.viewdns.info/dnsrecord/?domain="+str(site)+"&recordtype="+str(dns_type)+"&apikey="+str(API_KEY)+"&output=json", headers=header)
    r_json = json.loads(r.text)
    
    #parsing json data query
    tag_pai_query = r_json['query']
    domain = tag_pai_query['domain']
    record_type = tag_pai_query['recordtype']

    #parsing json data response
    tag_pai_response = r_json['response']
    tag_filho_response = tag_pai_response['records']
    #print(r_json)
    for itens in tag_filho_response:
        name = itens['data']
        ttl = itens['ttl']
        record_type = itens['type']
        ip_address = itens['data']
        
        print("\nDOMAIN: "+str(domain)+" ->> IP ADDRESS FOUND: "+str(ip_address))

def banner():
    print(" /$$$$$$$  /$$   /$$  /$$$$$$        /$$   /$$  /$$$$$$  /$$$$$$$$")
    print("| $$__  $$| $$$ | $$ /$$__  $$      | $$  | $$ /$$__  $$|__  $$__/")
    print("| $$  \ $$| $$$$| $$| $$  \__/      | $$  | $$| $$  \ $$   | $$   ")
    print("| $$  | $$| $$ $$ $$|  $$$$$$       | $$$$$$$$| $$$$$$$$   | $$   ")
    print("| $$  | $$| $$  $$$$ \____  $$      | $$__  $$| $$__  $$   | $$   ")
    print("| $$  | $$| $$\  $$$ /$$  \ $$      | $$  | $$| $$  | $$   | $$   ")
    print("| $$$$$$$/| $$ \  $$|  $$$$$$/      | $$  | $$| $$  | $$   | $$   ")
    print("|_______/ |__/  \__/ \______/       |__/  |__/|__/  |__/   |__/   ")
    print("\n ----Coded by anhax0r/siemexpert/sup3rm4n\n ----contact goncalv3s2017@gmail.com----")
                                                                                                                                                                                                  
try:
    site = sys.argv[1]
    dns_type = sys.argv[2]
    banner()
    time.sleep(1)
    go(site, dns_type)

except Exception as erro:
    print("use example: python dnshat.py site.com A")
    print("use example: python dnshat.py site.com MX")

