def getdata():
    import datetime
    return datetime.datetime.now().strftime("%d %b %y at %I:%M %p")

client_list = {1: "Monil", 2: "Anshu", 3: "Harry"}
log_list = {1: "Diet", 2: "Exercise"}

print("==========Health Management System==========\n")

try:
    for key, value in client_list.items():
        print(f"Press {key} for {value}")
    name_input = int(input("Enter your choice: "))
    print()
    print(f"Selected Client: {client_list[name_input]}\n")

    print("Press 1 for Log")
    print("Press 2 for Retrieve")
    log_or_retrieve = int(input("Enter your choice: "))
    print()

    # Log
    if log_or_retrieve == 1:
        for key, value in log_list.items():
            print(f"Press {key} to log {value}")
        d_or_e = int(input("Enter your choice: "))
        print()

        with open(client_list[name_input] + "_" + log_list[d_or_e] + ".txt", "a") as f:
            k = "y"
            while k != "n":
                mytext = input(f"Add {log_list[d_or_e]}: ")
                f.write(f"[{getdata()}]: {mytext}\n")
                k = input(f"Add More? y/n: ")
                print()
    # Retrieve
    elif log_or_retrieve == 2:
        for key, value in log_list.items():
            print(f"Press {key} to Retrieve {value}")
        dORE = int(input("Enter your choice: "))
        print()
        with open(client_list[name_input] + "_" + log_list[dORE] + ".txt") as f:
            content = f.read()
        print(content)

    else:
        print("Invalid Input!")





except Exception as e:
    print(e)