#!python

# textMyself.py - Contains textmyself() function that texts a message

# passed to it as a string

sid="XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
token="XXXXXXXXXXXXXXXXXXXXXXXXXXXX"

myNumber="+XXXXXXXXXXXXX"
twilioNumber="+XXXXXXXXXXXX"

from twilio.rest import TwilioRestClient

def textmyself(message):
    twilioClient=TwilioRestClient(sid,token)
    twilioClient.messages.create(body=message,from_=twilioNumber,to=myNumber)
    
# textmyself("Hello There")  will send "Hello There" message on my mobile number  
