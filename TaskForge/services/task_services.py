from datetime import datetime
from typing import List, Optional
from uuid import uuid4

from models import Task, User


class TaskService:
    """
    Handles business logic related to a user's tasks.
    """

    def add_task(
        self,
        user: User,
        title: str,
        description: str,
        deadline: datetime
    ) -> Task:
        task_id = str(uuid4())
        created_at = datetime.now()

        task = Task(
            task_id = task_id,
            title = title,
            description = description,
            created_at = created_at,
            deadline = deadline
        )

        user.tasks.append(task)
        return task

    def list_tasks(self, user: User) -> List[Task]:
        return user.tasks

    def get_task_by_id(
        self,
        user: User,
        task_id: str
    ) -> Optional[Task]:
        for task in user.tasks:
            if task.task_id == task_id:
                return task
        return None

    def mark_task_completed(
        self,
        user: User,
        task_id: str
    ) -> bool:
        task = self.get_task_by_id(user, task_id)
        if task is None:
            return False

        task.mark_completed()
        return True

    def delete_task(
        self,
        user: User,
        task_id: str
    ) -> bool:
        task = self.get_task_by_id(user, task_id)
        if task is None:
            return False

        user.tasks.remove(task)
        return True
