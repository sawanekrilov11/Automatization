import pytest
from Lesson9.Pages.Employee import Employer
from Lesson9.Pages.Database import DataBase


db = DataBase("postgresql+psycopg2://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")
api = Employer("https://x-clients-be.onrender.com")

#1.Создание компании,сотрудника,сравнение с бд и апи, удаление с бд
def test_get_list_of_employers():
    db.create_company('Ptz', 'Resp_city')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Sasha", "Nekrylov", "88005553535")
    db_employer_list = db.get_list_employer(max_id)
    api_employer_list = api.get_list(max_id)
    assert len(db_employer_list) == len(api_employer_list)
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    db.delete_employer(employer_id)
    db.delete(max_id)

#2.Добавление сотрудника в бд и сравнение статуса и тд.
def test_add_new_employer():
    db.create_company('ptz_new', 'employer')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Sasha", "Nekrylov", 88005553535)
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    assert response["companyId"] == max_id
    assert response["firstName"] == "Sasha"
    assert response["isActive"] == True
    assert response["lastName"] == "Nekrylov"
    db.delete_employer(employer_id)
    db.delete(max_id)


#3.Сравнение ифн по сотруднику при создании в бд
def test_assertion_data():
    db.create_company('Employer get id company', 'new')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Sasha", "Nekrylov", 88005553535)
    employer_id = db.get_employer_id(max_id)
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info["firstName"] == "Sasha"
    assert get_api_info["lastName"] == "Nekrylov"
    assert get_api_info["phone"] == "88005553535"
    db.delete_employer(employer_id)
    db.delete(max_id)

 #4.Сравненеи инф по сотруднику после изменения в бд
def test_update_user_info():
    db.create_company('Ptz update', 'new update')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Sasha", "Nekrylov", 88005553535)
    employer_id = db.get_employer_id(max_id)
    db.update_employer_info("Alex", employer_id)
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info["firstName"] == "Alex"
    assert get_api_info["lastName"] == "Nekrylov"
    assert get_api_info["isActive"] == True
    db.delete_employer(employer_id)
    db.delete(max_id)