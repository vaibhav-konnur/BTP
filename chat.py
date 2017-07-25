import os, sys
from flask import Flask, request
from pymessenger import Bot

 # Our flask object with root name
app = Flask(__name__) 

PAGE_ACCESS_TOKEN = 'EAACRf9B6c5kBAEpV8T8ALuUSaJAm2dYC2uT1kCOpqkAUdDntZCHXhDlZAw9Y9iScRDv3P3LhYQFCZCzwwooCoibHUj868oBZCLgOqnls09jBlqpoeEWL9J2NBUShRZBN0ZAjfH8ckwCAjgwIDtVpUHtYLO31oRDHjYMCZCObZA1DkAZDZD'
bot = Bot(PAGE_ACCESS_TOKEN)

# Facebook API sends an HTTP GET Request

@app.route('/',methods = ['GET'])
def verify():
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
		if not request.args.get("hub.verify_token") == "hello": #Verification token
			return "Verification token mismatch", 403
		return request.args["hub.challenge"], 200
	
	return "Hello World", 200

# To receive messages from the messenger chat using HTTP Post msg
@app.route('/',methods = ['POST'])
def webhook():
	data = request.get_json()
	log(data)

	if data['object']=='page':
		for entry in data['entry']:
			for messaging_event in entry['messaging']:

				#Extracting Ids
				sender_id = messaging_event['sender']['id']
				recipient_id = messaging_event['recipient']['id']

				if messaging_event.get('message'):
					if 'text' in messaging_event['message']:
						messaging_text = messaging_event['message']['text']
					else:
						messaging_text= 'no text'

					response = messaging_text
					bot.send_text_message(sender_id,response)    # Used to reply back to the messenger		

	return "ok",200

def log(message):
	print(message)
	sys.stdout.flush()


if __name__== "__main__":
	app.run(debug= True, port=5000)