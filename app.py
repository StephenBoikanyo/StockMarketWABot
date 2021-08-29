from flask import Flask
from flask import request
from twilio.rest import Client
from marketstack import get_stock_price
import os 

app = Flask(__name__)
#Environment variables 
twilio_id = os.environ.get('twilio_id')
twilio_token = os.environ.get('twilio_token')
twilio_client = Client(twilio_id,twilio_token)
twilio_number = 'whatsapp:+14155238886'
#Data from immutable object
form_content = request.form
sender_message  = form_content['Body']
sender = form_content['From']
#Sending a message back to user 
def send_message(sender_message,sender):
    client.messages.create(
        from_= twilio_number,
        body = sender_message,
        to = sender
    )
#Processing received message 
def process_message(sender_message):
    response = ''
    if sender_message == 'Hi' 'HI' or 'hi':
        response = 'Hello. Welcome to the stock market bot. '
        response += 'This bot will provide you with the latest stock price you wish to know. '
        response += 'Reply with the stock symbol to get the last price. '
        usr_input = sender_message.split()
        stock_symbol = usr_input[0]
        stock_price  = get_stock_price(stock_symbol)
        last_price   = stock_price['last_price']
        last_price_str = str(last_price)
        response = 'The stock price of ' + stock_symbol + ' is $ ' + last_price_str
    else:
        response ='Please say Hi, HI or hi to get started'
    return response
#first route to called when flast is run 
@app.route('/',methods=['POST'])
def stockbot_response():
    response = process_message(sender_message)
    send_message(response,sender)




