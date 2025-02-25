#!/usr/bin/env python3.12
import os
import requests 
import sys

from argparse import ArgumentParser

parser =  ArgumentParser(description= 'get the current weather information')
parser.add_argument('zip', help='zip/postal code to get the weather for')
parser.add_argument('--country', default='fr', help='country zip/ postal belongs to, default is "fr"')

args = parser.parse_args()
api_key = os.getenv('OWM_API_KEY')

if not api_key:
    print("Error: no 'OWM_API_KEY' provided")
    sys.exit(1)
url = f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip}{args.country}&appid={api_key}"

res = requests.get(url)

if res.status_code != 200:
    print(f"error talking to weather porvider:{res.status_code} ")
    sys.exit(1)

print(res.json())