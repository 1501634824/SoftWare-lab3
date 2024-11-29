
from enum import Enum
from datetime import datetime
from typing import List, Optional
from Task import *
from Notification import *


# User Class
class User:
    def __init__(self, name: str, prefers_minimal_ui: bool = True, forgetful: bool = True, taskList: Optional[List[Task]] = None, notification:NotificationManager = NotificationManager()):
        # 用户名
        self.name = name
        # 风格喜好
        self.prefers_minimal_ui = prefers_minimal_ui
        # 是否健忘
        self.forgetful = forgetful
        # 情侣空间
        self.couple = None
        #任务列表
        self.TaskList = taskList or []
        #通知管理器
        self.notification = notification


    def __repr__(self):
        return f"User(name={self.name}, prefers_minimal_ui={self.prefers_minimal_ui}, forgetful={self.forgetful})"


    #创建任务，不通知
    def createTask(self,*args):
        task = Task(*args)
        self.TaskList.append(task)
        return task


    #创建通知
    def setReminder(self, task:Task, remindTime: datetime, message: str):
        self.notification.addNotification(Reminder(task,remindTime,message))


    #打印任务列表所有任务
    def printTasks(self):
        for task in self.TaskList:
            if task.__repr__() is not None:
                print(task)

    def findTask(self,name:str):
        for task in self.TaskList:
            if task.title == name:
                return task
        return None

#CoupleAccount Class
class CoupleAccount:
    def __init__(self,partnerA: User,partnerB: User):
        assert(partnerA.couple == None and partnerB.couple == None)
        self.partnerA = partnerA
        self.partnerB = partnerB
        self.partnerA.couple = self
        self.partnerB.couple = self


    #创建共同任务
    def createTask(self,isHidden:bool,*args):
        if isHidden:
            task = HiddenTask(*args)
        else:
            task = Task(*args)
        self.partnerA.TaskList.append(task)
        self.partnerB.TaskList.append(task)
        return task


    #清除任务
    def removeSharedTask(self, task:Task):
        task.update_status(TaskStatus.COMPLETED)


    def setSharedReminder(self, *arg):
        self.partnerA.setReminder(*arg)
        self.partnerB.setReminder(*arg)
