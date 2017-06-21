#sends test messages 
#!python

sid="XXXXXXXXXXXXXXXXXXXXXXXXXXX"
token="XXXXXXXXXXXXXXXXXXXX"

myNumber="+XXXXXXXXXXXX"
twilioNumber="+XXXXXXXXXXX"

from twilio.rest import TwilioRestClient

def textme(message):
    twilioClient=TwilioRestClient(sid,token)
    twilioClient.messages.create(body=message,from_=twilioNumber,to=myNumber)
    
