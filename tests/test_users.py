from utils.api_client import APIClient

class TestUsers:

    def setup_method(self):
        # Create API client before every test
        self.client = APIClient()

    def test_get_all_users(self):
        # GET all users — should return 10
        response = self.client.get("/users")
        data = response.json()
        assert response.status_code == 200
        assert len(data) == 10
        print(f"Got {len(data)} users")

    def test_get_single_user(self):
        # GET user with id 1
        response = self.client.get("/users/1")
        data = response.json()
        assert response.status_code == 200
        assert data["id"] == 1
        print(f"Got user: {data['name']}")

    def test_user_has_required_fields(self):
        # Verify user has all required fields
        response = self.client.get("/users/1")
        data = response.json()
        assert "id" in data        # user id exists
        assert "name" in data      # name exists
        assert "email" in data     # email exists
        assert "phone" in data     # phone exists
        assert "address" in data   # address exists
        print("All required fields present")

    def test_user_email_format(self):
        # Verify email contains @ symbol
        response = self.client.get("/users/1")
        data = response.json()
        assert "@" in data["email"]
        print(f"Valid email: {data['email']}")

    def test_invalid_user(self):
        # GET non-existent user — should return 404
        response = self.client.get("/users/9999")
        assert response.status_code == 404
        print("Invalid user returns 404")

    def test_user_response_time(self):
        # API must respond within 2 seconds
        response = self.client.get("/users")
        time_taken = response.elapsed.total_seconds()
        assert time_taken < 2
        print(f"Response time: {time_taken}s")