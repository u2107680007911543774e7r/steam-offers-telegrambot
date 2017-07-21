import requests 
from news_parser import random_links
from time import sleep

TOKEN = '309376826:AAGHmxKMDQUEJVt1QlWuk57H1g8O0G_wPEc'
URL = 'https://api.telegram.org/bot{}/'.format(TOKEN)
global last_update_id 
last_update_id = 0

def get_updates():
    url = URL + 'getUpdates'
    r = requests.get(url)
    return r.json()

def get_message():
    #response only for new messages
    #getting update_id
    data = get_updates()
    last_object = data['result'][-1]
    current_update_id = last_object['update_id']
    
    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        chat_id = last_object['message']['chat']['id']
        text = last_object['message']['text']
        message = {'chat_id': chat_id,
               'text': text}
        return message
    return None

def send_message(chat_id, text):
    url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)
    
def main():
    while True:
        answer = get_message()
        if answer != None:
            chat_id = answer['chat_id']
            text = answer['text']
            if text == '/get_offer':
                send_message(chat_id, random_links())
            if text == '/start':
                send_message(chat_id, 'Hello! Welcome to Steam offers bot. Use command /help to see available commands for this bot.')
            if text == '/help':
                send_message(chat_id, '/get_offer - Get one of the top offers on Steam.')
            else:
                continue
        sleep(1)
        
        
if __name__ == '__main__':
    main()