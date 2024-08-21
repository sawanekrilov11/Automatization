import requests
import pytest
from Lesson8.Pages.Employee import Employee, Company

employee = Employee()
company = Company()

#Тест на авторизацию
def test_auth(get_token):
    token = get_token
    assert token is not None
    assert isinstance(token, str)

#Тест на получение id компании
def test_get_company_id():
    company_id = company.active_company_id()
    assert company_id is not None
    assert str(company_id).isdigit()

#Тест на добавление нового сотрудника
def test_add_new(get_token):
    token = str(get_token)
    comp_id = company.active_company_id()
    request_body = {
        'id': 0,
        'firstName': 'Alex',
        'lastName': 'Nekrylov',
        'middleName': 'string',
        'companyId': comp_id,
        'email': 'AlexN@mail.ru',
        'url': 'string',
        'phone': '+79991234567',
        'birthdate': '2024-08-21T00:02:28.783Z',
        'isActive': 'true'
    }
    new_employee_id = (employee.add_new(token, request_body))['id']
    assert new_employee_id is not None
    assert str(new_employee_id).isdigit()
    
    info = employee.get_info(new_employee_id)
    #assert info.status_code == 200
    assert info.json()['id'] == new_employee_id
    assert info.status_code == 200
    

def test_add_new_employee_withouttoken(): #проверка без токена
    comp_id = company.active_company_id()
    token = ""
    request_body = {
        "id": 0,
        "firstName": "Alex",
        "lastName": "Nekrylov",
        "middleName": "string",
        "companyId": comp_id,
        "email": "AlexN@mail.ru",
        "url": "string",
        "phone": "+79991234567",
        "birthdate": "2024-08-21T00:02:28.783Z",
        "isActive": 'true'
    }
    new_employee_id = employee.add_new(token, request_body)
    assert new_employee_id['message'] == 'Unauthorized'

def test_add_new_employee_withoutbody(get_token): #проверка без тела запроса
    token = str(get_token)
    comp_id = company.active_company_id()
    request_body = {}
    new_employee_id = employee.add_new(token, request_body)
    assert new_employee_id['message'] == 'Internal server error'
 
# Тест на получение списка сотрудников (1get)
def test_employee_get():
    comp_id = company.active_company_id()
    list_employee = employee.get_list(comp_id)
    assert isinstance(list_employee, list)

def test_employee_get_withoutid(): #без idшника компании
    try:
        employee.get_list()
    except TypeError as e:
        assert str(e) == "Employee.get_list() missing 1 required positional argument: 'company_id'"

# тест на редактировние сотрудника
def test_change_info(get_token):
    token = str(get_token)
    comp_id = company.active_company_id()
    request_body = {
        "id": 0,
        "firstName": "Alex",
        "lastName": "Nekrylov",
        "middleName": "string",
        "companyId": comp_id,
        "email": "AlexN@mail.ru",
        "url": "string",
        "phone": "+79991234567",
        "birthdate": "2024-08-21T00:02:28.783Z",
        "isActive": 'true'
    }
    before_employee = employee.add_new(token, request_body)
    id = before_employee['id']
    body_after_employee = {
        "lastName": "Nekrylov",
        "email": "AlexN1@mail.ru",
        "url": "string",
        "phone": "string",
        "isActive": "true"
    }
    after_employee = employee.change_info(token, id, body_after_employee)
    assert after_employee.status_code == 200
    assert id == after_employee.json()['id']
    assert (after_employee.json()["email"]) == body_after_employee.get("email")

def test_employers_missing_id_token_body():
    try:
        employee.change_info()
    except TypeError as e:
        assert str(e) == "Employee.change_info() missing 3 required positional arguments: 'token', 'employee_id', and 'body'"




