import json
import requests
import allure
from Lesson9.conftest import URL

path = '/employee/' #Создал перменную для "пути". Для того чтобы, в случае изменения пути не переписывать код полностью, а заменить только данные в переменной.

class Employer:
    def __init__(self, web_url = URL):
        self.web_url = web_url

    @allure.step("Получение списка сотрудников компании по id компании")
    def get_list(self, company_id: int):
        company = {
            'company': company_id
        }
        response = requests.get(self.web_url + path, params=company)
        return response.json()
    
    @allure.step("Добавить нового сотрудника в компанию")
    def add_new(self, token: str, body: json):
        headers = {
            'x-client-token': token
        }
        responce = requests.post(self.web_url + path, headers=headers, json=body)
        return responce.json()

    @allure.step("Получить информацию по сотруднику (ID)")
    def get_info(self, employee_id: int):
        responce = requests.get(self.web_url + path + str(employee_id))
        return responce
    
    @allure.step("Изменение информации о сотруднике")
    def change_info(self, token: str, employee_id: int, body: json):
        headers = {
            'x-client-token': token
        }
        responce = requests.patch(self.web_url + path + str(employee_id), headers=headers, json=body)
        return responce
    
