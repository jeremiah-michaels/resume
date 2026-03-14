from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI(
    title="File API",
    description="API for retrieving files and file counts from local folders.",
    version="1.0.0"
)

# Allow requests from GitHub Pages (and any other origin for testing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Root folder that the API is allowed to serve files from
FILES_ROOT = Path("./files").resolve()


@app.get(
    "/files/{folder}/{filename}",
    summary="Get a file",
    description="Retrieve a file by name from a specified folder inside the files directory."
)
def get_file(folder: str, filename: str):
    file_path = (FILES_ROOT / folder / filename).resolve()

    # Block path traversal attacks (e.g. ../../etc/passwd)
    if not str(file_path).startswith(str(FILES_ROOT)):
        raise HTTPException(status_code=400, detail="Invalid path.")

    if not file_path.exists():
        raise HTTPException(status_code=404, detail=f"File '{filename}' not found in folder '{folder}'.")

    if not file_path.is_file():
        raise HTTPException(status_code=400, detail=f"'{filename}' is not a file.")

    return FileResponse(file_path)


@app.get(
    "/files/{folder}/count",
    summary="Get file count",
    description="Returns the number of files in a specified folder inside the files directory."
)
def get_file_count(folder: str):
    folder_path = (FILES_ROOT / folder).resolve()

    # Block path traversal attacks
    if not str(folder_path).startswith(str(FILES_ROOT)):
        raise HTTPException(status_code=400, detail="Invalid path.")

    if not folder_path.exists():
        raise HTTPException(status_code=404, detail=f"Folder '{folder}' not found.")

    if not folder_path.is_dir():
        raise HTTPException(status_code=400, detail=f"'{folder}' is not a folder.")

    file_count = len([f for f in folder_path.iterdir() if f.is_file()])

    return {"folder": folder, "file_count": file_count}