#!flask/bin/python
from flask import request, render_template, Flask
import  os, sys, json
import requests
app = Flask(__name__)

from random import randint
from telesign.messaging import MessagingClient
from telesign.voice import VoiceClient

@app.route('/')
def index():
    return  "hello"

@app.route('/send')
def send():
    customer_id = "2C1097F6-3917-4A53-9D38-C45A3C8ADD2B"
    api_key = "FTgHUVjcPWvgzCvtksi2v+tMLTAXbh5LLVEl1Wcl4NAtszxElZL4HS/ZwJqJufRkEmRpwUTwULxsZgL2c649vQ=="
    phone_number = "14084299128"
    message = "We will have a meeting at 10 pm"
    message_type = "ARN"
    messaging = MessagingClient(customer_id, api_key)
    response2 = messaging.message(phone_number, message, message_type)
    voice = VoiceClient(customer_id, api_key)
    response1 = voice.call(phone_number, message, message_type)
    
if __name__ == '__main__':
	app.secret_key = os.urandom(12)
	#app.run(debug=True)
