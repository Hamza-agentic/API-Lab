
import requests

print("-" * 30)
print("Task 13")
print("-" * 30)

# Send a GET request to the API
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

# Check the status code
print("Status:", response.status_code)

# Read the JSON response
if response.status_code == 200:
    post = response.json()

    # Print post details
    print("Post ID:", post["id"])
    print("Title:", post["title"])
    print("Body:", post["body"])
else:
    print("Request failed!")

print("-" * 30)
print("Task 14")
print("-" * 30)

# Base URL for multiple posts
url = "https://jsonplaceholder.typicode.com/posts/"

# Retrieve posts 1, 2, and 3
for post_id in range(1, 4):
    response = requests.get(url + str(post_id))

    # Check the status code
    if response.status_code == 200:
        post = response.json()
        print(f"Post {post_id}: {post['title']}")
    else:
        print(f"Failed to retrieve Post {post_id}")
print("-" * 35)
print("Task 15 - Retrieve and Process a Collection")
print("-" * 35)

# API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Send a GET request
response = requests.get(url)

# Check the status code
print("Status:", response.status_code)

# Convert JSON response into Python data
if response.status_code == 200:
    posts = response.json()

    # Count the total number of posts
    total_posts = len(posts)

    print("Total Posts:", total_posts)
else:
    print("Request failed!")

print("-" * 35)