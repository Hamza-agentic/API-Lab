# Agent Tool Specification

- **Tool Name:** `get_post`
- **Description:** Retrieves post information using post ID.
- **HTTP Method:** GET
- **Endpoint:** `https://jsonplaceholder.typicode.com/posts/{post_id}`
- **Required Inputs:** `post_id` (integer)
- **Optional Inputs:** None
- **Expected Output:** `{ "id": 1, "title": "...", "body": "...", "userId": 1 }`
- **Possible Errors:** 404 (Not Found), 429 (Rate Limit), 500 (Server Error), Timeout
- **Authentication Required:** No