
from api_client import make_safe_request
print("=" * 40)
print("TASK 26 - COMPLETE API CLIENT")
print("=" * 40)

url = "https://jsonplaceholder.typicode.com/posts/1"

print("HTTP Method: GET")
print("Endpoint:", url)

post = make_safe_request(url)

if post is not None:
    print("\nRequest successful!")
    print("Post ID:", post.get("id"))
    print("User ID:", post.get("userId"))
    print("Title:", post.get("title"))
    print("Body:", post.get("body"))
else:
    print("Could not retrieve post information.")
