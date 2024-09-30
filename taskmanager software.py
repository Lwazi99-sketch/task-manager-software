#TASK MANAGER SOFTWARE 
#Lwazi Somtsewu

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        
        print("Your Tasks:")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def remove_task(self, task_number):
        try:
            task = self.tasks.pop(task_number - 1)
            print(f"Task '{task}' removed.")
        except IndexError:
            print("Invalid task number. Please try again.")

def main():
    task_manager = TaskManager()
    
    while True:
        print("\nSimple Task Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            task_manager.add_task(task)
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            task_manager.view_tasks()
            task_number = int(input("Enter the task number to remove: "))
            task_manager.remove_task(task_number)
        elif choice == '4':
            print("Exiting the Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
