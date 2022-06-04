import requests
import pytest

def test_get_client():
    response = requests.get("http://localhost:3000/")
    assert response.status_code == 200
    
def test_create_user():
    response = requests.post("http://localhost:3000/api/users/1", params={"email":"test@mail.ru", "first_name":"test", "last_name":"test"})
    print(response.text)
    assert response.status_code == 201
    
def test_put_user():
    response = requests.put("http://localhost:3000/api/users/1", params={"email":"test1@mail.ru", "first_name":"test1", "last_name":"test1"})
    print(response.text)
    assert response.status_code == 201
    
def test_delete_user():
    response = requests.delete("http://localhost:3000/api/users/1")
    print(response.text)
    assert response.status_code == 204
    
def test_check_list_users():
    response = requests.get("http://localhost:3000/api/users/0")
    print(response.text)
    assert response.status_code == 200
    
    
    

