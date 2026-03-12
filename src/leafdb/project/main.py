from fastapi import FastAPI, HTTPException
from typing import Any
from json import loads, dumps
from pathlib import Path
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import unquote


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "db.json"


class Item(BaseModel):
    value: Any


def read_db() -> dict:
    with open(DB_PATH, "r", encoding="utf-8") as f:
        return loads(f.read())


def write_db(content: dict) -> None:
    with open(DB_PATH, "r+", encoding="utf-8") as f:
        f.seek(0)
        f.write(dumps(
            content,
            indent=2,
            ensure_ascii=False,
            sort_keys=False
        ))
        f.truncate()


@app.get("/")
def view_data() -> dict:
    return read_db()


@app.post("/")
def add_data(field: dict) -> None:
    content = read_db()
    if not isinstance(field, dict):
        raise HTTPException(
            status_code=400,
            detail=f"Invalid structure: \n{field}"
        )

    for key in field:
        if key in content:
            raise HTTPException(
                status_code=400,
                detail=f"field key already exists: {key}"
            )

    content.update(field)
    write_db({
        unquote(str(key)): unquote(str(value))
        for key, value in content.items()
    })


@app.delete("/{field}")
def delete_data(field: Any) -> None:
    content = read_db()

    if field not in content:
        raise HTTPException(
            status_code=404,
            detail=f"No field found in database: {field}"
        )
    if len(content) < 1:
        return
    del content[field]
    write_db(content)


@app.get("/{item}")
def view_spec(item: Any) -> Any:
    content = read_db()

    if item not in content:
        raise HTTPException(
            status_code=404,
            detail=f"No field found: {item}"
        )

    return content[item]


@app.put("/{key}")
def edit_item(key: Any, value: Item) -> None:
    content = read_db()

    if not (key in content):
        raise HTTPException(
            status_code=404,
            detail=f"No field found: {key}"
        )

    content[key] = value.value
    write_db(content)