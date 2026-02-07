from datetime import datetime


class Task:
    def __init__(
        self,
        task_id: int,
        title: str,
        description: str,
        created_at: datetime,
        deadline: datetime,
        completed: bool = False
    ):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.created_at = created_at
        self.deadline = deadline
        self.completed = completed

    def mark_completed(self) -> None:
        self.completed = True