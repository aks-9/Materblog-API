import requests

BASE_URL = "http://127.0.0.1:5002/api/posts"

def test_search():
    print("Testing search endpoint...")
    
    # Test title search
    print("\n1. Searching for title 'First'...")
    response = requests.get(f"{BASE_URL}/search", params={"title": "First"})
    if response.status_code == 200:
        posts = response.json()
        print(f"Status: {response.status_code}, Found: {len(posts)} posts")
        for post in posts:
            print(f" - {post['title']}")
    else:
        print(f"Failed! Status: {response.status_code}")

    # Test content search
    print("\n2. Searching for content 'second'...")
    response = requests.get(f"{BASE_URL}/search", params={"content": "second"})
    if response.status_code == 200:
        posts = response.json()
        print(f"Status: {response.status_code}, Found: {len(posts)} posts")
        for post in posts:
            print(f" - {post['content']}")
    else:
        print(f"Failed! Status: {response.status_code}")

    # Test both title and content search
    print("\n3. Searching for title 'First' and content 'first'...")
    response = requests.get(f"{BASE_URL}/search", params={"title": "First", "content": "first"})
    if response.status_code == 200:
        posts = response.json()
        print(f"Status: {response.status_code}, Found: {len(posts)} posts")
        for post in posts:
             print(f" - {post['title']}: {post['content']}")
    else:
        print(f"Failed! Status: {response.status_code}")

    # Test no results
    print("\n4. Searching for something that doesn't exist...")
    response = requests.get(f"{BASE_URL}/search", params={"title": "NONEXISTENT"})
    if response.status_code == 200:
        posts = response.json()
        print(f"Status: {response.status_code}, Found: {len(posts)} posts (Expected 0)")
    else:
        print(f"Failed! Status: {response.status_code}")

if __name__ == "__main__":
    try:
        test_search()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server. Make sure the backend is running at http://127.0.0.1:5002")
