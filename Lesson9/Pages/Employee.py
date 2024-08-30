import json
import requests
from Lesson9.websait import URL

path = '/employee/' #Создал перменную для "пути". Для того чтобы, в случае изменения пути не переписывать код полностью, а заменить только данные в переменной.

class Employer:
    def __init__(self, web_url = URL):
        self.web_url = web_url

#1.[GET] /employee Получить список сотрудников для компании.
    def get_list(self, company_id: int):
        company = {
            'company': company_id
        }
        response = requests.get(self.web_url + path, params=company)
        return response.json()
    
#2.[POST] /employee Добавить нового сотрудника.
    def add_new(self, token: str, body: json):
        headers = {
            'x-client-token': token
        }
        responce = requests.post(self.web_url + path, headers=headers, json=body)
        return responce.json()

#3.[GET] /employee/{id} Получить сотрудника по ID.
    def get_info(self, employee_id: int):
        responce = requests.get(self.web_url + path + str(employee_id))
        return responce
    
#4.[PATCH] /employee/{id} Изменить информацию о сотруднике.
    def change_info(self, token: str, employee_id: int, body: json):
        headers = {
            'x-client-token': token
        }
        responce = requests.patch(self.web_url + path + str(employee_id), headers=headers, json=body)
        return responce
    
