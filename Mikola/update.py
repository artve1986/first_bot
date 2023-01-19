import requests
import time
with open('Mikolaj.txt', 'r', encoding= 'utf - 8') as F:
    tok = F.read()

API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = tok
TEXT: str = 'Я тебе чую, не кричи'
Max_counter: int = 100

offset: int = -2
counter: int = 0
chat_id: int

while counter < Max_counter:
    print('attampt=', counter)    #Бачимо у консолі роботу коду

    update = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    if update['result']:
        for res in update['result']:
            offset = res['update_id']
            if 'message' in res:
                chat_id = res['message']['from']['id']
            elif 'edited_message' in res:
                break
            requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1)
    counter += 1
