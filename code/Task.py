from enum import Enum
from datetime import datetime
from typing import List, Optional
# Enum for Task Status
class TaskStatus(Enum):
    NOT_STARTED = "Not Started"
    READY_TO_START = "Ready to Start"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


    def __lt__(self,other):
        status_order = {"Not Started": 1, "Ready to Start": 2, "In Progress": 3, "Completed": 4}
        
        # 比较当前枚举值的优先级
        return status_order[self.value] < status_order[other.value]



#Enum for Task Priority
class TaskPriority(Enum):
    LOW = "Low Priority"
    MEDIUM = "Medium Priority"
    HIGH = "High Priority"

    def __lt__(self,other):
        priority_order = {"Low Priority": 1, "Medium Priority": 2, "High Priority": 3}
        
        # 比较当前枚举值的优先级
        return priority_order[self.value] < priority_order[other.value]


# Task Class
class Task:
    def __init__(
        self,
        title: str = "",
        description: str = "",
        due_date: datetime = datetime.now(),
        priority: TaskPriority = TaskPriority.LOW,
        labels: Optional[List[str]] = None
    ):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.labels = labels or []
        self.status = TaskStatus.NOT_STARTED
        self.UpTasks = []  # Tasks that this task depends on
        self.Subtasks = []  # Subtasks

    def add_UpTask(self, task):
        self.UpTasks.append(task)

    def add_Subtask(self, task):
        self.Subtasks.append(task)

    def update_status(self, new_status: TaskStatus):
        self.status = new_status

    def set_priority(self, priority: str):
        self.priority = priority

    def add_label(self, label: str):
        self.labels.append(label)

    def __repr__(self):
        if self.status == TaskStatus.COMPLETED:
            return None
        return (
            f"Task(title={self.title}, "
            f"status={self.status.value}, "
            f"due_date={self.due_date}, "
            f"priority={self.priority})"
        )
    

class HiddenTask(Task):
    def __init__(
        self,
        *args
    ):
        super().__init__(*args)
        self.isHidden = True


    def checkCondition(self):
        for task in self.UpTasks:
            if(task.status != TaskStatus.COMPLETED):
                return False
        return True


    def __repr__(self):
        if not self.isHidden:
            return super().__repr__()
        if self.checkCondition():
            self.isHidden = False
            return super().__repr__()
        return None