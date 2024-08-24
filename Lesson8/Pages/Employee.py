import json
import requests
from Lesson8.websait import URL

path = '/employee/' #Создал перменную для "пути". Для того чтобы, в случае изменения пути не переписывать код полностью, а заменить только данные в переменной.
path2 = '/company' #Аналогично с путём для сотрудника.

class Company:
    def __init__(self, web_url = URL):
        self.web_url = web_url

    def create_new_company(self, token: str, body: json):
        headers = {
            'x-client-token': token
        }
        responce = requests.post(self.web_url + path2, headers=headers, params=body)
        return responce.json()
    
    #Второй вариант
    #def create_new_company(name, description=''):
    #    compamy = {
    #        "name": name,
    #        "description": description
    #    }
    #    headers1 = {}
    #    headers1["x-client-token"] = self.get_token()
    #    resp = requests.post(self.web_url, + path2, json = compamy, headers = headers1)
    #    return resp.json()
    
    def active_company_id(self):
        active_params = {
            'active': 'true'
        }
        responce = requests.get(self.web_url + path2, params=active_params)
        return responce.json()[-1]["id"]
        

class Employee:
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
    
