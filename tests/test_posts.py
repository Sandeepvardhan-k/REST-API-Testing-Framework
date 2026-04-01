from utils.api_client import APIClient

class TestPosts:

    def setup_method(self):
        # Create API client before every test
        self.client = APIClient()

    def test_get_all_posts(self):
        # GET all posts
        response = self.client.get("/posts")
        assert response.status_code == 200
        assert len(response.json()) == 100
        print("✅ Got all 100 posts")

    def test_get_single_post(self):
        # GET post with id 1
        response = self.client.get("/posts/1")
        data = response.json()
        assert response.status_code == 200
        assert data["id"] == 1
        assert "title" in data
        assert "body" in data
        print(f"✅ Got post: {data['title']}")

    def test_create_post(self):
        # POST — create new post
        new_post = {
            "title": "Test Post",
            "body": "This is test body",
            "userId": 1
        }
        response = self.client.post("/posts", new_post)
        data = response.json()
        assert response.status_code == 201
        assert data["title"] == "Test Post"
        assert data["body"] == "This is test body"
        print(f"Created post with id: {data['id']}")

    def test_update_post(self):
        # PUT — update existing post
        updated_post = {
            "title": "Updated Title",
            "body": "Updated body",
            "userId": 1
        }
        response = self.client.put("/posts/1", updated_post)
        data = response.json()
        assert response.status_code == 200
        assert data["title"] == "Updated Title"
        print("Post updated successfully")

    def test_delete_post(self):
        # DELETE — delete post
        response = self.client.delete("/posts/1")
        assert response.status_code == 200
        print("Post deleted successfully")

    def test_invalid_post(self):
        # GET non-existent post — should return 404
        response = self.client.get("/posts/9999")
        assert response.status_code == 404
        print("Invalid post returns 404")

    def test_response_time(self):
        # Test API responds within 2 seconds
        response = self.client.get("/posts")
        time_taken = response.elapsed.total_seconds()
        assert time_taken < 2
        print(f"Response time: {time_taken} seconds")