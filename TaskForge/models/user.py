from typing import List
from models import Task


class User:
    def __init__(self, username: str):
        self.username: str = username
        self.tasks: List[Task] = []