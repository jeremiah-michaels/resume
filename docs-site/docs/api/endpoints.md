# Endpoints

## Get a File

Retrieves a file by name from a specified folder.

```
GET /files/{folder}/{filename}
```

### Path Parameters

| Parameter  | Type   | Required | Description                        | Example   |
|------------|--------|----------|------------------------------------|-----------|
| `folder`   | string | Yes      | The folder to look in              | `folder1` |
| `filename` | string | Yes      | The name of the file to retrieve   | `doc1.txt`|

### Example Request

```bash
curl http://localhost:8000/files/folder1/doc1.txt
```

### Responses

| Status | Description                          |
|--------|--------------------------------------|
| `200`  | Returns the file as a binary stream  |
| `400`  | Invalid path                         |
| `404`  | File not found                       |

### Example Error Response

```json
{
  "detail": "File 'doc1.txt' not found in folder 'folder1'."
}
```

---

## Get File Count

Returns the number of files in a specified folder.

```
GET /files/{folder}/count
```

### Path Parameters

| Parameter | Type   | Required | Description                          | Example   |
|-----------|--------|----------|--------------------------------------|-----------|
| `folder`  | string | Yes      | The folder to count files in         | `folder1` |

### Example Request

```bash
curl http://localhost:8000/files/folder1/count
```

### Responses

| Status | Description                             |
|--------|-----------------------------------------|
| `200`  | Returns folder name and file count      |
| `400`  | Invalid path                            |
| `404`  | Folder not found                        |

### Example Response

```json
{
  "folder": "folder1",
  "file_count": 3
}
```

### Example Error Response

```json
{
  "detail": "Folder 'folder1' not found."
}
```