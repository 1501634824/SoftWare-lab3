from Task import *
from datetime import datetime
from queue import PriorityQueue


class Reminder:


    def __init__(self, task: Task,time: datetime,message:str):
        self.task = task
        self.time = time
        self.message = message


    def __lt__(self, other):
        if self.time != other.time:
            return self.time < other.time
        return self.task.priority > other.task.priority  # 大优先级的任务排在前面


    def __repr__(self) -> str:
        return (
            f"{self.task}, "
            f"RemindTime: {self.time}"
        )


    def remind(self):
        if self.task.status < TaskStatus.IN_PROGRESS:
            if self.task.status == TaskStatus.READY_TO_START:
                self.task.update_status(TaskStatus.IN_PROGRESS)
            print("Find Task which need to remind")
            print(self)


class NotificationManager:


    def __init__(self):
        self.Notifications = PriorityQueue()


    def addNotification(self,notification:Reminder):
        self.Notifications.put(notification)


    def remind(self):
        print("Ready to search Tasks which need to remind")
        time = datetime.now()
        tempList = []
        while not self.Notifications.empty():
            task = self.Notifications.get()
            tempList.append(task)
            if task.time <= time:
                task.remind()
            else:
                break
        if self.Notifications.empty():
            print("Empty")
        for task in tempList:
            self.Notifications.put(task)

