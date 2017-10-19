#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 16:53:12 2017

@author: abhi
"""

from telesign.voice import VoiceClient
from telesign.messaging import MessagingClient


customer_id = "2C1097F6-3917-4A53-9D38-C45A3C8ADD2B"
api_key = "FTgHUVjcPWvgzCvtksi2v+tMLTAXbh5LLVEl1Wcl4NAtszxElZL4HS/ZwJqJufRkEmRpwUTwULxsZgL2c649vQ=="

phone_number = "15102039956"
message = "We will have a meeting at 10 pm"
message_type = "ARN"

messaging = MessagingClient(customer_id, api_key)
response2 = messaging.message(phone_number, message, message_type)


voice = VoiceClient(customer_id, api_key)
response1 = voice.call(phone_number, message, message_type)

