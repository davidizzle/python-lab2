from sys import argv

filename = argv[1]
tasklist = []
target = open(filename, "r")

for task in target:
    tasklist.append(task)




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
        tasklist.append(string + "\n")
    elif choice == "2":
        string = input("Insert the task you want to remove")
        tasklist.remove(string + "\n")
    elif choice == "3":
        tasklist = sorted(tasklist)
        for task in tasklist:
            print(task, end =" ")
    elif choice == "4":
        target = open(filename, "w")
        for item in tasklist:
            target.write(item)
        flag = 0
    else:
        print("Not a valid choice!")

