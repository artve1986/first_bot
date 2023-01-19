import requests

'''Приклад api get запросу. Положення космічної станції'''

api_url =  'http://numbersapi.com/43'
res = requests.get(api_url)
print(res.text)