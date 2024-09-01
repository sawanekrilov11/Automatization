import pytest
import allure
from Lesson9.Pages.Employee import Employer
from Lesson9.Pages.Database import DataBase


db = DataBase("postgresql+psycopg2://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")
api = Employer("https://x-clients-be.onrender.com")

@allure.epic("X-clients")
@allure.title("Список сотрудников")
@allure.description("Получение списка сотрудников из BD и API и их сравнение")
@allure.feature("Тест 1")
@allure.severity(severity_level='normal')
def test_get_list_of_employers():
    with allure.step("BD - Создание компании"):
        db.create_company('Ptz', 'Resp_city')
    with allure.step("BD - Получение ID последней созданной компании"):
        max_id = db.last_company_id()
    with allure.step("BD - Добавление нового сотрудника в компанию"):
        db.create_employer(max_id, "Sasha", "Nekrylov", "88005553535")
    with allure.step("BD - Получение списка сотрудников из последней созданной компании"):
        db_employer_list = db.get_list_employer(max_id)
    with allure.step("API - Получение списка сотрудников из последней созданной компании"):
        api_employer_list = api.get_list(max_id)
    with allure.step("Сравнение списка сотрудников из BD и API"):
        assert len(db_employer_list) == len(api_employer_list)
    with allure.step("BD - Удаление созданного сотрудника"):
        response = (api.get_list(max_id))[0]
        employer_id = response["id"]
        db.delete_employer(employer_id)
    with allure.step("BD - Удаление последней созданной компании"):
        db.delete(max_id)

@allure.epic("X-clients")
@allure.title("Добавление сотрудников")
@allure.description("Добавление сотрудника в BD и сравнение с API(данные)")
@allure.feature("Тест 2")
@allure.severity(severity_level='critical')
def test_add_new_employer():
    with allure.step("BD - Создание компании"):
        db.create_company('ptz_new', 'employer')
    with allure.step("BD - Получение ID последней созданной компании"):
        max_id = db.last_company_id()
    with allure.step("BD - Добавление нового сотрудника в компанию"):
        db.create_employer(max_id, "Sasha", "Nekrylov", 88005553535)
    with allure.step("Сравнение данных о сотруднике, удаление сотрудника"):
        response = (api.get_list(max_id))[0]
        employer_id = response["id"]
        assert response["companyId"] == max_id
        assert response["firstName"] == "Sasha"
        assert response["isActive"] == True
        assert response["lastName"] == "Nekrylov"
        db.delete_employer(employer_id)
    with allure.step("BD - Удаление последней созданной компании"):
        db.delete(max_id)

@allure.epic("X-clients")
@allure.title("Список сотрудников")
@allure.description("Получение информации о сотруднике по ID")
@allure.feature("Тест 3")
@allure.severity(severity_level='normal')
def test_assertion_data():
    with allure.step("BD - Создание компании"):
        db.create_company('Employer get id company', 'new')
    with allure.step("BD - Получение ID последней созданной компании"):
        max_id = db.last_company_id()
    with allure.step("BD - Добавление нового сотрудника в компанию"):
        db.create_employer(max_id, "Sasha", "Nekrylov", 88005553535)
    with allure.step("BD - Поиск сотрудника в последней созданой компании"):
        employer_id = db.get_employer_id(max_id)
    with allure.step("API - Получение информации о сотруднике и удаление сотрудника"):
        get_api_info = (api.get_info(employer_id)).json()
        assert get_api_info["firstName"] == "Sasha"
        assert get_api_info["lastName"] == "Nekrylov"
        assert get_api_info["phone"] == "88005553535"
        db.delete_employer(employer_id)
    with allure.step("BD - Удаление последней созданной компании"):
        db.delete(max_id)

@allure.epic("X-clients")
@allure.title("Изменение информации о сотруднике")
@allure.description("Получение списка сотрудников из BD и API и их сравнение")
@allure.feature("Тест 4")
@allure.severity(severity_level='critical')
def test_update_user_info():
    with allure.step("BD - Создание компании"):
        db.create_company('Ptz update', 'new update')
    with allure.step("BD - Получение ID последней созданной компании"):
        max_id = db.last_company_id()
    with allure.step("BD - Добавление нового сотрудника в компанию"):
        db.create_employer(max_id, "Sasha", "Nekrylov", 88005553535)
    with allure.step("BD - Поиск сотрудника в последней созданой компании"):
        employer_id = db.get_employer_id(max_id)
    with allure.step("BD - Изменение данных сотрудника"):
        db.update_employer_info("Alex", employer_id)
    with allure.step("API - Получение информации о сотруднике и удаление сотрудника"):
        get_api_info = (api.get_info(employer_id)).json()
        assert get_api_info["firstName"] == "Alex"
        assert get_api_info["lastName"] == "Nekrylov"
        assert get_api_info["isActive"] == True
        db.delete_employer(employer_id)
    with allure.step("BD - Удаление последней созданной компании"):
        db.delete(max_id)