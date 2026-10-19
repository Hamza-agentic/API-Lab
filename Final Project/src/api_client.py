
import requests


def make_safe_request(url):
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return response.json()

        elif response.status_code == 400:
            print("Bad Request (400)")

        elif response.status_code == 401:
            print("Unauthorized (401)")

        elif response.status_code == 404:
            print("Request failed. Status Code: 404 | Resource not found.")

        elif response.status_code == 429:
            print("Rate limit exceeded (429)")

        elif response.status_code == 500:
            print("Server Error (500)")

        else:
            print(f"HTTP Status: {response.status_code}")

    except requests.exceptions.Timeout:
        print("Error: Request timed out.")

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

    return None


# Test 404 only when this file is run directly
if __name__ == "__main__":
    make_safe_request(
        "https://jsonplaceholder.typicode.com/posts/999999"
    )
