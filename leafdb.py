import requests
from typing import Any, Callable
from fastapi import HTTPException
from functools import wraps
from json import dumps, loads


class Leafdb:

    def __init__(self):
        self.__url = "http://localhost:8000"

    def set_port(self, port: int) -> Any:
        """Sets the port to the URL of the database"""
        if not isinstance(port, int):
            raise ValueError(f"Invalid value: {port}")
        self.__url = f"http://localhost:{port}"

    def view(self, key: Any = None) -> dict | None:
        """Views database items.
        key -- If given, it's value from the database is returned, otherwise returns all the database
        """
        if key is None:
            res = requests.get(self.__url)
            return res.json()

        res = requests.get(f"{self.__url}/{key}")

        return res.json()

    def insert(self, data: dict) -> None:
        """Inserts <data> dictionary object to the database"""
        if not isinstance(data, dict):
            raise TypeError(f"invalid data structure: \n {data}")
        requests.post(self.__url, json=data)

    def delete(self, *items: list[Any]) -> None:
        """Deletes <items> from the database"""
        for item in items:
            requests.delete(f"{self.__url}/{item}")

    def edit(self, key: Any, value: Any) -> None:
        """Changes `key`'s value to `value` in the database"""
        requests.put(
            f"{self.__url}/{key}",
            json={"value": value}
        )

    def get_url(self) -> str:
        return self.__url


__all__ = ["Leafdb"]
