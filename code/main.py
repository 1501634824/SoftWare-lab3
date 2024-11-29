from User import *
from time import sleep
from threading import Thread
import re
from datetime import datetime, timedelta


MainFlag = False

def initTodoList():
    print("========================================================================================================")
    print("WelCome to Couple TodoList")
    print("Please Log in First")
    for i in range(10):
        print("\r"+"Loading"+'.'*i,end="",flush=True)
        sleep(1)
    print("\nSuccess to Log in!")
    user1 = User(
        name = "ZZN",
        prefers_minimal_ui = True, 
        forgetful = True, 
        taskList = None, 
        notification = NotificationManager()
    )
    user2 = User(
        name = "LYL",
        prefers_minimal_ui = True, 
        forgetful = True, 
        taskList = None, 
        notification = NotificationManager()
    )
    couple = CoupleAccount(user1,user2)
    print("USER1 is",end="")
    print(user1)
    print("USER2 is",end="")
    print(user2)
    print("Another nice day in your life")
    print("Lets checkout our TodoList!")
    global MainFlag
    MainFlag = True
    return user1, user2, couple


def getUserName(user1,user2):
    print("请输入用户：")
    c_ = input()
    if c_ == "1":
        user = user1
    elif c_ == "2":
        user = user2
    else:
        print("无效用户")
        return None
    return user


def getOrder(user1:User,user2:User,couple:CoupleAccount):
    global MainFlag
    try:
        Help = [
            "Welcome to TodoList",
            "Please choose your serve",
            "1: addTask",
            "2: addRemind",
            "3: addTask and add Remind",
            "4: addSharedTask",
            "5: addSharedRemind",
            "6: addSharedTask and add SharedRemind",
            "7: Update Task Status",
            "8: Print Task List",
            "exit: exit the TodoList",
            "help: print help"
        ]


        def printHelp():
            for str in Help:
                print(str)


        printHelp()
        while MainFlag:
            c = input()
            if c == "exit":
                MainFlag = False
            elif c == "help":
                printHelp()
            # add Task
            elif c == '1':
                user = getUserName()
                if user is not None:
                    print("请创建Task:")
                    print("请依次输入：")
                    print("Title:")
                    title = input()
                    print("详情描述:")
                    description = input()
                    print("DDL: ")
                    due_date = datetime.now() + timedelta(int(input()))
                    print("Priority: ")
                    c_ = input()
                    if c_ == "LOW":
                        priority = TaskPriority.LOW
                    elif c_ == "MEDIUM":
                        priority = TaskPriority.MEDIUM
                    elif c_ == "HIGH":
                        priority = TaskPriority.HIGH
                    else:
                        priority = TaskPriority.LOW
                    print("Label: ")
                    labels = input()
                    user.createTask(title,description,due_date,priority,labels)
            # add Remind
            elif c == '2':
                user = getUserName(user1,user2)
                if user is not None:
                    print("请输入Task")
                    c = input()
                    task = user.findTask(c)
                    if task is None:
                        print("没有找到Task")
                    else:
                        print("请输入提醒时间")
                        ddl = input()
                        print("请输入提醒内容")
                        message = input()
                        user.setReminder(task,datetime.now() + timedelta(seconds=int(ddl)),message)
            # add Task and Remind
            elif c == '3':
                user = getUserName(user1,user2)
                if user is not None:
                    print("请创建Task:")
                    print("请依次输入：")
                    print("Title:")
                    title = input()
                    print("详情描述:")
                    description = input()
                    print("DDL: ")
                    due_date = datetime.now() + timedelta(seconds=int(input()))
                    print("Priority: ")
                    c_ = input()
                    if c_ == "LOW":
                        priority = TaskPriority.LOW
                    elif c_ == "MEDIUM":
                        priority = TaskPriority.MEDIUM
                    elif c_ == "HIGH":
                        priority = TaskPriority.HIGH
                    else:
                        priority = TaskPriority.LOW
                    print("Label: ")
                    labels = input()
                    task = user.createTask(title,description,due_date,priority,labels)
                    print("请输入提醒时间")
                    ddl = input()
                    print("请输入提醒内容")
                    message = input()
                    user.setReminder(task,datetime.now() + timedelta(int(ddl)),message)
            elif c == '4':
                print("请创建Task:")
                print("请依次输入：")
                print("是否隐藏：")
                is_hidden = bool(input())
                print("Title:")
                title = input()
                print("详情描述:")
                description = input()
                print("DDL: ")
                due_date = datetime.now() + timedelta(int(input()))
                print("Priority: LOW MEDIUM or HIGH")
                c_ = input()
                if c_ == "LOW":
                    priority = TaskPriority.LOW
                elif c_ == "MEDIUM":
                    priority = TaskPriority.MEDIUM
                elif c_ == "HIGH":
                    priority = TaskPriority.HIGH
                else:
                    priority = TaskPriority.LOW
                print("Label: ")
                labels = input()
                couple.createTask(is_hidden,title,description,due_date,priority,labels)
            # add Remind
            elif c == '5':
                print("请输入Task")
                c = input()
                task = couple.findTask(c)
                if task is None:
                    print("没有找到Task")
                else:
                    print("请输入提醒时间")
                    ddl = input()
                    print("请输入提醒内容")
                    message = input()
                    couple.setReminder(task,datetime.now() + timedelta(seconds=int(ddl)),message)
            # add Task and Remind
            elif c == '6':
                print("请创建Task:")
                print("请依次输入：")
                print("是否隐藏：")
                is_hidden = bool(input())
                print("Title:")
                title = input()
                print("详情描述:")
                description = input()
                print("DDL: ")
                due_date = datetime.now() + timedelta(seconds=int(input()))
                print("Priority: ")
                c_ = input()
                if c_ == "LOW":
                    priority = TaskPriority.LOW
                elif c_ == "MEDIUM":
                    priority = TaskPriority.MEDIUM
                elif c_ == "HIGH":
                    priority = TaskPriority.HIGH
                else:
                    priority = TaskPriority.LOW
                print("Label: ")
                labels = input()
                task = couple.createTask(is_hidden,title,description,due_date,priority,labels)
                print("请输入提醒时间")
                ddl = input()
                print("请输入提醒内容")
                message = input()
                user.setReminder(task,datetime.now() + timedelta(int(ddl)),message)
            # update Status
            elif c == '7':
                user = getUserName(user1,user2)
                if user is not None:
                    print("请输入Task")
                    c = input()
                    task = user.findTask(c)
                    if task is None:
                        print("没有找到Task")
                    else:
                        c = input()
                        if c == "Not Started":
                            status = TaskStatus.NOT_STARTED
                        elif c == "Ready to Start":
                            status = TaskStatus.NOT_STARTED
                        elif c == "In Progress":
                            status = TaskStatus.NOT_STARTED
                        elif c == "Completed":
                            status = TaskStatus.NOT_STARTED
                        else:
                            print("错误的Status")
                            status = TaskStatus.NOT_STARTED
                        task.update_status(status)
            elif c == '8':
                user = getUserName(user1,user2)
                user.printTasks()
            else:
                print("Wrong order,try again!")
                print("If you need help,input 'help'")
    except:
        MainFlag = False
  




def remind(user1,user2):
    while MainFlag:
        startime = datetime.now()
        while (datetime.now() - startime).total_seconds() < 5:
            pass
        user1.notification.remind()
        user2.notification.remind()


    
def main():
    user1, user2, couple = initTodoList()
    thead1 = Thread(
        target = getOrder,
        args = (user1,user2,couple,)
    )

    thead2 = Thread(
        target = remind,
        args = (user1,user2,)
    )

    thead1.start()
    thead2.start()

    thead1.join()
    thead2.join()
    

    print("Bye~")
    


if __name__ == "__main__":
    main()