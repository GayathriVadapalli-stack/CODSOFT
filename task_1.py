#To-Do List
def add_todolist(to_do_list):
    num_elements=int(input("Enter the number of tasks you want to add: "))
    print("Enter your tasks")
    for i in range(num_elements):
        to_do_list.append(input().lower())
    print("Your Tasks have been added")
def update_todolist(to_do_list):
    task=input("Enter the tasks you've already done: ").lower()
    to_do_list.remove(task)
    print("Your list has been updated")
def show_todolist(to_do_list):
    for i in range(len(to_do_list)):
        print(to_do_list[i])
to_do_list=[]
print(5*'*'+"To-Do List"+5*'*')
print("Create your To-Do List now")
while True:
    print("1.Create Task \n2.Update Task \n3.Track your to-do list")
    user_choice= int(input('Enter your choice: '))
    if user_choice == 1:
        add_todolist(to_do_list)
    elif user_choice ==2:
        update_todolist(to_do_list)
    elif user_choice==3:
        show_todolist(to_do_list)
    else:
        print("Enter Valid choice")
    interest=input(("Do you want to make any changes in the to-do list?(Type 'yes' or 'no'): ")).lower()
    if interest=='no':
        print("Thank you ")
        break