# Phase 02: HTTP Requests, Responses & REST Analysis
## Task 04 — Analyze a URL
URL analyzed: `https://api.example.com/students/101`
| Component | Value |
|---|---|
| Protocol | `https`|
| Host | `api.example.com`|
| Path | `/students/101`|
| Resource | `students`|
| Resource identifier | `101`|
---

## Task 05 — Build a REST API Operation Table

| Operation | HTTP Method | Endpoint |
|---|---|---|
| Retrieve all students | GET | `/students`|
| Create a student | POST | `/students`|
| Retrieve student 101 | GET | `/students/101`|
| Update student 101 | PUT | `/students/101`|
| Delete student 101 | DELETE  | `/students/101`|

### Why Different HTTP Methods Are Used
Different HTTP methods are used for different operations (GET, POST, PUT, DELETE) to clearly define the action being performed on a REST resource:
* **GET** is used to retrieve existing resources.
* **POST** is used to create new resources.
* **PUT** is used to update existing resources.
* **DELETE** is used to remove resources.

## Task 06 — Test GET Requests
### Request 1
* **Endpoint:** `/posts/1`
* **HTTP Method:** `GET`
* **Status Code:** `200 OK`
* **Response Body:**
  ```json
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  }
  ```
### Request 2
* **Endpoint:** `/posts/2`
* **HTTP Method:** `GET`
* **Status Code:** `200 OK`
* **Response Body:**
  ```json
  {
  "userId": 1,
  "id": 2,
  "title": "qui est esse",
  "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
  }
  ```
 ### Request 3
* **Endpoint:** `/posts/3`
* **HTTP Method:** `GET`
* **Status Code:** `200 OK`
* **Response Body:**
  ```json
  {
    "userId": 1,
    "id": 3,
    "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
    "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
  }
  ```

## Task 07 — Test POST
### HTTP Method
POST

### Endpoint
`https://jsonplaceholder.typicode.com/posts`

### Request Body
```json
{
  "title": "My API Lab",
  "body": "Testing POST request",
  "userId": 1
}
```

### Response Status Code
`201 Created`

### Response Body
```json
{
  "title": "My API Lab",
  "body": "Testing POST request",
  "userId": 1,
  "id": 101
}
```
## Task 08 — Update a Resource Using PUT

### Request Method
PUT

## Endpoint
`https://jsonplaceholder.typicode.com/posts/1`

### Request Body
```json
{
  "id": 1,
  "title": "Updated API Lab",
  "body": "Testing PUT request",
  "userId": 1
}
```

### Status Code
`200 OK`

### Response Body
```json
{
  "id": 1,
  "title": "Updated API Lab",
  "body": "Testing PUT request",
  "userId": 1
}
```

## Task 09 — Test DELETE

### Request Method
DELETE

### Endpoint
`https://jsonplaceholder.typicode.com/posts/1`

### Status Code
`200 OK`

### Response
```json
{}
```
