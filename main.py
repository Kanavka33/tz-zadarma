import requests
import logging
from base64 import b64encode

logging.basicConfig(filename='call_logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

api_key = 'api_key'
secret_key = 'key'
url = 'https://api.zadarma.com/v1/request/callback/'

to_number = input("номер (в формате +7...): ")
from_number = 'номер(ваш)'

credentials = b64encode(f"{api_key}:{secret_key}".encode()).decode()
headers = {
    'Authorization': f'Basic {credentials}'
}

try:
    response = requests.post(url, headers=headers, data={
        'from': from_number,
        'to': to_number
    })

    if response.status_code == 200:
        logging.info(f"Звонок на номер {to_number} инициирован. Ответ: {response.json()}")
    else:
        logging.error(f"Ошибка при звонке: {response.status_code}, {response.text}")

except Exception as e:
    logging.error(f"Ошибка при звонке: {str(e)}")