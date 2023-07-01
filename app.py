from database import add_entry, view_entries

menu = """Please select one of the following options:
    1) Add new entry for today
    2) View entries
    3) Exit.
    
Your selection: """
welcome = "Welcome to the programming diary !"

# entries = [
#     {"content": "Today I started learning programing", "date":"01-01-2023"},
#     {"content": "Blabla ", "date":"02-01-2023"},
#     {"content": "Blablabla", "date":"03-01-2023"},
#     {"content": "Blablablabla", "date":"04-01-2023"},
# ]


while user_input (user_input := input(menu)) != "3":
    #content 
    if user_input == "1":
        add_entry()
    elif user_input == "2":
        view_entries()
    else: 
        print("Invalid option, please try again")

    