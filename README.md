# hndx stagetwo

## How to run the application 
The application is built using django and django restframework(drf)
 
 To get the apllication up and running, you will need to install the requirments.txt file by using the command

```pip install requirments.txt```

This process will install the necessary libries to run the application.


## API Endpoints

### 1. Create a Person

**Endpoint:** `POST /api/`

**Request:**
```json
{
    "name": "Mark Essien"
}
```

**Response:**
```json
{
    "id": 1,
    "name": "Mark Essien"
}
```
### 2. Retrieve all in database

**Endpoint:** `GET /api/get/`

**Response:**
```json
{
    "id": 1,
    "name": "Mark Essien"
},
{
    "id": 1,
    "name": "Jimmy James"
},
{
    "id": 1,
    "name": "Top Boy"
}
```

### 3. Retrieve a Person

**Endpoint:** `GET /api/{user_id}`

**Response:**
```json
{
    "id": 1,
    "name": "Mark Essien"
}
```

### 4. Update a Person

**Endpoint:** `PUT /api/{user_id}`

**Request:**
```json
{
    "name": "Mark Essien Updated"
}
```

**Response:**
```json
{
    "id": 1,
    "name": "Mark Essien Updated"
}
```

### 5. Delete a Person

**Endpoint:** `DELETE /api/{user_id}`

**Response:**
```json
{
    "message": "Person has been deleted"
}
```



## Error Handling

- **400 Bad Request:** If the request is malformed or missing required fields.
- **404 Not Found:** If the requested `Person` does not exist.
- **405 Method Not Allowed:** If an unsupported HTTP method is used on an endpoint.


