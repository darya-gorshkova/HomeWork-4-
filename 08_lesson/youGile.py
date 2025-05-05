import requests

BASE_URL = "value"
TOKEN = "value"


# Позитивные тесты
def test_create_project_positive(): #Создание нового проекта.

    data = {'title': "New Project"}

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + TOKEN
    }

    response = requests.post("https://ru.yougile.com/api-v2/projects", json=data, headers=headers)
    assert response.status_code == 201
    assert "id" in response.json()
    return response, "id"


def test_update_project():
    data = {"title": "Updated Project"}   #Изменение названия проекта.

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + TOKEN
    }

    response = requests.put(f'{BASE_URL}projects/{"3f2570e1-6e11-4f0d-ae74-74ce2ee60607"}', headers=headers, json=data)
    assert response.status_code == 200

def test_get_project_by_id_positive():
    project_id = '3f2570e1-6e11-4f0d-ae74-74ce2ee60607' #Получение информации о проекте по id.
    data = {'title': "New Project"}

    headers = {
         "Content-Type": "application/json",
        "Authorization": "Bearer " + TOKEN
    }

    response = requests.get( f'{BASE_URL}projects/{project_id}', headers=headers, json=data)
    print(response.text)  # Выведем текст ответа сервера
    assert response.status_code == 200
    assert "id" in response.json(), "Информация о проекте получена успешно."


# Негативные тесты:
def test_create_project_error_title():        # создание проекта с запрещенными символами.

    invalid_data = {'title': "$$$"}

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + TOKEN
    }

    response = requests.post(BASE_URL + "/projects", json=invalid_data, headers=headers)
    assert response.status_code != 201
    assert "error" in response.json(), "Ошибка должна возникнуть при попытке создать проект без названия."

def test_update_project_invalid_id():        #Изменение несуществующего проекта
    invalid_id = 'non-id'
    data = {"title": "Test Update"}

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + TOKEN
    }

    response = requests.put(f"{BASE_URL}/projects/{invalid_id}", json=data, headers=headers)
    assert response.status_code != 200
    assert "error" in response.json()

def test_get_project_by_invalid_id():  #получение информации о несуществующем проекте
    non_project_id = 'non-id'
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + TOKEN
    }
    response = requests.get(f"{BASE_URL}/projects/{non_project_id}", headers=headers)
    assert response.status_code != 200
    assert "error" in response.json()