import requests
'''Приклад api get запросу. Положення космічної станції'''

api_url = 'http://api.open-notify.org/iss-now.json'
res = requests.get(api_url)
if res.status_code == 200:   #200 показує, що запрос вдалий
    print(res.text)
else: print(res.status_code)

