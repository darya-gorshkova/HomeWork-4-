import requests
import json

class TestProjects:
    BASE_URL = "https://yougile.com/api-v2/"
    TOKEN = "value"

    @classmethod
    def setup_class(cls):
        cls.create_project("Test Project")
    @classmethod
    def teardown_class(cls):
        if hasattr(cls, 'project_id'):
            delete_response = requests.delete(f"{cls.BASE_URL}/projects/{cls.project_id}", headers={"Authorization": cls.TOKEN})
            assert delete_response.status_code in [200, 204], "Удаление проекта завершилось неудачей."

    @staticmethod
    def create_project(title="New Project"):
        response = requests.post(
            f"{TestProjects.BASE_URL}/projects",
            headers={
                "Authorization": TestProjects.TOKEN,
                "Content-Type": "application/json"
            },
            data=json.dumps({"title": title})
        )
        assert response.status_code == 201, "Проект не был создан."
        project_data = response.json()
        TestProjects.project_id = project_data["id"]
        print(f"Проект создан с ID: {TestProjects.project_id}")
        return response

    #Позитивные тесты

    def test_create_project_positive(self):
        """создание проекта."""
        response = self.create_project()
        assert response.status_code == 201
        assert "id" in response.json()

    def test_update_project_positive(self):
        """обновление названия проекта."""
        updated_response = self.update_project(self.project_id)
        assert updated_response.status_code == 200
        assert updated_response.json()["title"] == "Updated Title"

    
    ### Негативные тесты ###

    def test_create_project_negative_missing_field(self):
        """Попытка создать проект без обязательного поля 'title'."""
        response = requests.post(
            f"{self.BASE_URL}/projects",
            headers={"Authorization": self.TOKEN},
            data=json.dumps({})
        )
        assert response.status_code == 400

    def test_update_project_negative_invalid_id(self):
        "Попытка обновить несуществующий проект."
        invalid_id = "invalid-id"
        response = self.update_project(invalid_id)
        assert response.status_code == 404

    def test_get_project_negative_nonexistent_id(self):
        """Попытка загрузить несуществующий проект."""
        non_existent_id = "non-existent-project-id"
        response = self.get_project(non_existent_id)
        assert response.status_code == 404

