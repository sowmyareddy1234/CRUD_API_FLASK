# Simple CRUD API Documentation

## Overview

This documentation outlines the usage of a simple CRUD (Create, Read, Update, Delete) API built with Flask. The API allows you to manage items with basic information such as name and description.

**Web URL:** https://sowmya.pythonanywhere.com/

## Endpoints

### 1. Get All Items

**Endpoint:** `GET /items`

**Description:** Retrieve a list of all items.

**Example Response:**
```json
{
  "1": {"name": "Item 1", "description": "Description for Item 1"},
  "2": {"name": "Item 2", "description": "Description for Item 2"}
}
```

### 2. Get a Specific Item

**Endpoint:** `GET /items/<int:item_id>`

**Description:** Retrieve details of a specific item by providing its ID.

**Example Response:**
```json
{
  "item_id": 1,
  "name": "Item 1",
  "description": "Description for Item 1"
}
```

### 3. Create a New Item

**Endpoint:** `POST /items`

**Description:** Create a new item by providing a JSON payload with `name` and `description`.

**Example Request:**
```json
{
  "name": "New Item",
  "description": "Description for New Item"
}
```

**Example Response:**
```json
{
  "message": "Item created successfully",
  "item_id": 3
}
```

### 4. Update an Existing Item

**Endpoint:** `PUT /items/<int:item_id>`

**Description:** Update the details of an existing item by providing its ID and a JSON payload with updated information.

**Example Request:**
```json
{
  "name": "Updated Item",
  "description": "Updated description for Item"
}
```

**Example Response:**
```json
{
  "message": "Item updated successfully"
}
```

### 5. Delete an Item

**Endpoint:** `DELETE /items/<int:item_id>`

**Description:** Delete a specific item by providing its ID.

**Example Response:**
```json
{
  "message": "Item deleted successfully"
}
```

## Error Handling

- If an item with the specified ID is not found, the API returns a 404 error with the message: `{"error": "Item not found"}`.
- For other errors, the API returns a 400 error with details in the format: `{"error": "Error message"}`.

