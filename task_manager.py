task = []
demo_data = [
    {"id": 1, "description": "Finish coding project", "priority": "High", "date": "2025-01-25", "status": "Pending"},
    {"id": 2, "description": "Prepare presentation slides", "priority": "Medium", "date": "2025-01-27", "status": "Pending"},
    {"id": 3, "description": "Submit project report", "priority": "High", "date": "2025-01-30", "status": "Completed"},
    {"id": 4, "description": "Review team feedback", "priority": "Low", "date": "2025-02-01", "status": "Pending"},
    {"id": 5, "description": "Plan weekend trip", "priority": "Low", "date": "", "status": "Completed"}
]

task.extend(demo_data)

def generate_id():
    return len(task) + 1

def get_priority():
    priority_map = {
        "h": "High",
        "m": "Medium",
        "l": "Low"
    }
    while True:
        priority = input("Enter Priority: High(h), Medium(m), Low(l): ").lower()
        if priority in priority_map:
            return priority_map[priority]
        else:
            print("Invalid input. Please enter 'h', 'm', or 'l'.")

def add_task():
    print("----- ADD TASK -----")
    status = "Pending"
    description = input("Enter Description: ")
    priority = get_priority()
    due_date = input("Enter due date (YYYY-MM-DD, leave blank for no due date): ")
    
    task_data = {
        'id':generate_id(),
        "description":description,
        "priority":priority,
        "date": due_date if due_date else "No due date",
        "status":status
    }
    task.append(task_data)
    print("Task Added Successfully")
    print(task_data)

def view_single_task():
    print("----- VIEW SINGLE TASK -----")
    task_id = int(input("Enter Id to view: "))
    for i,k in enumerate(task):
        if task_id == k['id']:
            print(f"Id: {k['id']}, Description: {k['description']}, Priorty: {k['priority']}, Due Date: {k['date']}, Status: {k['status']}")

def view_task():
    print("----- VIEW TASKS -----")
    for i in task:
        print(f"Id: {i['id']}, Description: {i['description']}, Priorty: {i['priority']}, Due Date: {i['date']}, Status: {i['status']}")
    

def mark_as_done():
    print("----- MARK AS DONE TASK -----")
    view_task()
    task_id = int(input("Enter Id to be Marked as Done: "))
    for i in task:
        if task_id == i['id']:
            if i['status']!="Completed":
                i['status']="Completed"
                print(f"task having ID: {i['id']} Marked as Complete")
                print(i)
            else:
                print(f"task having ID: {i['id']} is already Completed")
            break

def delete_task():
    print("----- DELETE TASK -----")
    view_task()
    task_id = int(input("Enter task ID to delete: "))
    for i,k in enumerate(task):
        if task_id == k['id']:
            print(i)
            task.pop(i)
    print("Task Deleted Successfully")
    view_task()

def main_menu():
    while True:
        print("===== CLI Task Manager =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice =="1":
            add_task()
        elif choice =="2":
            choice2 = input("View Mode:\nFor Single View PRESS (S) and for All View PRESS ENTER: ")
            if choice2.capitalize() =="S":
                view_single_task()
            else:
                view_task()
        elif choice =="3":
            mark_as_done()
        elif choice =="4":
            delete_task()
        elif choice =="5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
