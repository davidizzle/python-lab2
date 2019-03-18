
tasklist = []

flag = 1
i = 0

while flag == 1:
    print("Hi, I am your personal assistant! You want to:\n"
          "1.insert a new task\n"
          "2.remove a task\n"
          "3.show all existing tasks,sorted in alphabetic order\n"
          "4.close the program")

    choice = input("What will you do?\n")

    if choice == "1":
        string = input("Insert the new task:")
        tasklist.append(string)
    elif choice == "2":
        string = input("Insert the task you want to remove")
        tasklist.remove(string)
    elif choice == "3":
        tasklist = sorted(tasklist)
        for task in tasklist:
            print(task)
    elif choice == "4":
        flag = 0
    else:
        print("Not a valid choice!")

        