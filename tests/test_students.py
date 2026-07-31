
def test_get_students(client):

    response = client.get("/api/v1/students")

    assert response.status_code == 200


def test_post_student(client):
    response = client.post(
        "/students",
        json={
            "name": "Test user",
            "age": 20,
            "user_id": 5,
            "department_id": 1
        }
    )

    assert response.status_code == 201