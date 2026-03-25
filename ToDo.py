class Task:
    def __init__(self,number,title,status="pending"):
        
        self.number = number
        self.title = title
        self.status = status
        
        

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self,task):
        self.tasks.append(f"{task}\n")
        

    def show_task(self): 
        with open ("data.txt", "r") as file:
            l=file.readlines()
            print(l)
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}", end="")

    def mark_as_done(self):
        self.show_task()
        done=(input("Which task you want to mark as done?\n"))
        if 1 <= done <= len(self.tasks):
            self.tasks[done - 1 ] = self.tasks[done - 1].replace("\n" , "-done\n")
        else:
            print("There is no task with that number")
    def save_and_exit(self):
        with open("data.txt" , "a") as file:
            file.writelines(self.tasks)
        exit()    

do=TaskManager() 

while True:
    Choice = int(input("1. Add task\n2. Show tasks\n3. Mark as done\n4.Save and exit\n"))

    if Choice == 1:
        t=input("New Task:")
        do.add_task(t)

    elif Choice == 2:
        do.show_task()

    elif Choice == 3:
        do.mark_as_done()

    elif Choice == 4:
        do.save_and_exit()

