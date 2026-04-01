from utils.api_client import APIClient

class TestTodos:

    def setup_method(self):
        # Create API client before every test
        self.client = APIClient()

    def test_get_all_todos(self):
        # GET all todos — should return 200
        response = self.client.get("/todos")
        data = response.json()
        assert response.status_code == 200
        assert len(data) == 200
        print(f"✅ Got {len(data)} todos")

    def test_get_single_todo(self):
        # GET todo with id 1
        response = self.client.get("/todos/1")
        data = response.json()
        assert response.status_code == 200
        assert data["id"] == 1
        assert "title" in data
        print(f"✅ Got todo: {data['title']}")

    def test_todo_has_required_fields(self):
        # Verify todo has all required fields
        response = self.client.get("/todos/1")
        data = response.json()
        assert "id" in data           # id exists
        assert "title" in data        # title exists
        assert "completed" in data    # completed status exists
        assert "userId" in data       # userId exists
        print("All required fields present")

    def test_completed_todos_exist(self):
        # Verify some todos are completed
        response = self.client.get("/todos")
        data = response.json()
        # Filter only completed todos
        completed = [todo for todo in data if todo["completed"] == True]
        assert len(completed) > 0
        print(f" Found {len(completed)} completed todos")

    def test_incomplete_todos_exist(self):
        # Verify some todos are not completed
        response = self.client.get("/todos")
        data = response.json()
        # Filter only incomplete todos
        incomplete = [todo for todo in data if todo["completed"] == False]
        assert len(incomplete) > 0
        print(f"Found {len(incomplete)} incomplete todos")

    def test_invalid_todo(self):
        # GET non-existent todo — should return 404
        response = self.client.get("/todos/9999")
        assert response.status_code == 404
        print("Invalid todo returns 404")