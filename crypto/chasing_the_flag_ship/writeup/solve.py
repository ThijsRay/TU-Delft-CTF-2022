#!/usr/bin/env python3

import requests
from MTRecover import MT19937Recover
from textwrap import wrap
from ipaddress import ip_address

URL = "http://[2a02:c206:2101:8992::]/"

base_ip = URL[8:-4]

def bits_to_hex(bits):
    return ':'.join(wrap(hex(bits)[2:].rjust(8, '0'), 4))

def find_first_url(text):
    begin = text.find("http://")
    end = text[begin:].find("'")
    return text[begin:begin+end]

def get_random_bits_from_url(url):
    ip = ip_address(url[8:-1])
    island_group = int.from_bytes(ip.packed[8:12], byteorder='big')
    island = int.from_bytes(ip.packed[12:16], byteorder='big')
    return island_group, island


def get_random_samples(start_url):
    random_samples = list()
    url = start_url
    while len(random_samples) < 700:
        print("requesting", url)
        r = requests.get(url)
        url = find_first_url(r.text)
        
        r1, r2 = get_random_bits_from_url(url)
        random_samples.append(r2)
        random_samples.append(r1)
    return list(reversed(random_samples))

def create_mersenne_predictor(samples):
    predictor = MT19937Recover()
    return predictor.go(samples)

r = requests.get(URL)
start = find_first_url(r.text)
random_samples = get_random_samples(start)
predictor = create_mersenne_predictor(random_samples)

while True:
    r1 = predictor.getrandbits(32)
    r2 = predictor.getrandbits(32)
    ip = f"{base_ip}:{bits_to_hex(r1)}:{bits_to_hex(r2)}"
    possible_next_url = f"http://[{str(ip_address(ip))}]"
    response = requests.get(possible_next_url).text
    if "TUDCTF" in response:
        print(response)
        break
