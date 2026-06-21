# File API Overview

The File API is a locally hosted REST API built with Python and FastAPI. 
It serves files and file metadata from a structured folder directory on the host machine.

This API was built as a portfolio project to demonstrate API development and 
documentation practices, including AI-assisted development workflows using Claude Desktop.

## Base URL

| Environment | URL                     |
|-------------|-------------------------|
| Local       | `http://localhost:8000` |

## Endpoints Summary

| Method | Path                            | Description              |
|--------|---------------------------------|--------------------------|
| GET    | `/files/{folder}/{filename}`    | Retrieve a file          |
| GET    | `/files/{folder}/count`         | Get file count in folder |

## Security

This API uses enterprise-level security practices for endpoints exposed to the internet.
All requests are validated server-side, and path traversal attacks are mitigated via
input validation on the `folder` and `filename` parameters.

## Error Handling

All errors return a JSON object with a `detail` field describing the issue.

```json
{
  "detail": "File 'doc1.txt' not found in folder 'folder1'."
}
```

See [Endpoints](endpoints.md) for the full list of error responses per endpoint.