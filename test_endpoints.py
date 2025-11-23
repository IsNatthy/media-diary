import requests
import sys

BASE_URL = "http://127.0.0.1:5000"

def test_auth_flow():
    session = requests.Session()
    
    with open("results.txt", "w", encoding="utf-8") as f:
        # 1. Register
        f.write("Testing Register...\n")
        register_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "password123"
        }
        # We might get 400 if user already exists, which is fine for repeated tests
        response = session.post(f"{BASE_URL}/auth/register", json=register_data)
        f.write(f"Register Status: {response.status_code}\n")
        f.write(f"Register Response: {response.json()}\n")
        
        # 2. Login
        f.write("\nTesting Login...\n")
        login_data = {
            "username": "testuser",
            "password": "password123"
        }
        response = session.post(f"{BASE_URL}/auth/login", json=login_data)
        f.write(f"Login Status: {response.status_code}\n")
        f.write(f"Login Response: {response.json()}\n")
        
        if response.status_code != 200:
            f.write("Login failed, stopping test.\n")
            return

        # 3. Get Me
        f.write("\nTesting Get Me...\n")
        response = session.get(f"{BASE_URL}/auth/me")
        f.write(f"Get Me Status: {response.status_code}\n")
        f.write(f"Get Me Response: {response.json()}\n")

        # 4. Logout
        f.write("\nTesting Logout...\n")
        response = session.post(f"{BASE_URL}/auth/logout")
        f.write(f"Logout Status: {response.status_code}\n")
        f.write(f"Logout Response: {response.json()}\n")

        # 5. Get Me after Logout (should fail)
        f.write("\nTesting Get Me after Logout...\n")
        response = session.get(f"{BASE_URL}/auth/me")
        f.write(f"Get Me (after logout) Status: {response.status_code}\n")
        f.write(f"Get Me (after logout) Response: {response.json()}\n")

        # 6. Test Catalog (Public)
        f.write("\nTesting Catalog...\n")
        response = requests.get(f"{BASE_URL}/catalog/")
        f.write(f"Catalog Status: {response.status_code}\n")
        f.write(f"Catalog Response: {response.json()}\n")

if __name__ == "__main__":
    try:
        test_auth_flow()
    except Exception as e:
        print(f"An error occurred: {e}")
