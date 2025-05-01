import requests
import json

class TestProjects:
    BASE_URL = "https://yougile.com/api-v2/"
    TOKEN = "KaNnXVKorxQ6rC2Vg-u+NowZh+n9truUCLZ+D7jzmBopqDtPtgQ2+KP5-1uqnY6P"

    @classmethod
    def setup_class(cls):
        cls.create_project("Skypro")  # Создаем проект с названием "Skypro"

    @classmethod
    def teardown_class(cls):
        if hasattr(cls, 'project_id'):
            delete_response = requests.delete(f"{cls.BASE_URL}/projects/{cls.project_id}", headers={"Authorization": f"Bearer {cls.TOKEN}"})
            assert delete_response.status_code in [200, 204], "Удаление проекта завершилось неудачей."

    @staticmethod
    def create_project(title="Skypro"):  # создаем проект с именем "Skypro"
        response = requests.post(
            f"{TestProjects.BASE_URL}/projects",
            headers={
                "Authorization": f"Bearer {TestProjects.TOKEN}",
                "Content-Type": "application/json"
            },
            data=json.dumps({"title": title})
        )
        assert response.status_code == 201, "Проект не был создан."
        project_data = response.json()
        TestProjects.project_id = project_data["id"]  # Сохраняем идентификатор проекта
        print(f"Проект создан с ID: {TestProjects.project_id}")  # Отображаем ID проекта
        return response

# Позитивные тесты
def test_create_project_positive():
    """Создание проекта с названием 'Skypro'."""
    try:
        response = TestProjects.create_project()
        assert response.status_code == 201
        assert "id" in response.json()
    except Exception as e:
        print(e)

def test_get_project_positive():
    """Получение информации о проекте с использованием сохраненного ID."""
    if not hasattr(TestProjects, 'project_id'):
        raise ValueError("Project ID is missing.")

    get_response = requests.get(
        f"{TestProjects.BASE_URL}/projects/{TestProjects.project_id}",
        headers={
            "Authorization": f"Bearer {TestProjects.TOKEN}"
        }
    )
    assert get_response.status_code == 200, "Запрос на получение проекта завершился неудачно."
    retrieved_project = get_response.json()
    assert retrieved_project["id"] == TestProjects.project_id, "ID полученного проекта не совпадает с ожидаемым."
def test_update_project_positive():
    """Обновление названия проекта."""
    new_title = "Updated Project Name"
    update_response = requests.put(
        f"{TestProjects.BASE_URL}/projects/"f"{TestProject_id
        headers={
            "Authorization": f"Bearer {TestProjects.TOKEN}",
            "Content-Type": "application/json"
        },
        data=json.dumps({"title": new_title})
    )
    assert update_response.status_code == 200, "Обновление проекта завершилось неудачей."
    updated_project = update_response.json()
    assert updated_project["title"] == new_title, "Название проекта не обновлено успешно."

def test_get_project_positive():
    """Получение информации о проекте."""
    get_response = requests.get(
        f"{TestProjects.BASE_URL}/projects/{TestProjects.project_id}",
        headers={
            "Authorization": f"Bearer {TestProjects.TOKEN}"
            "project_id==045421f0-5789-432b-b836-30b7d24d8ea4
    )
    assert get_response.status_code == 200, "Запрос на получение проекта завершился неудачно."
    retrieved_project = get_response.json()
    assert retrieved_project["id"] == TestProjects.project_id, "ID полученного проекта не совпадает с ожидаемым."

# Негативные тесты
def test_create_project_negative_missing_field():
    """Попытка создать проект без обязательного поля 'title'."""
    response = requests.post(
        f"{TestProjects.BASE_URL}/projects",
        headers={"Authorization": f"Bearer {TestProjects.TOKEN}"},
        data=json.dumps({}),  # Нет обязательных полей
    )
    assert response.status_code == 400