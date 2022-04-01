import methods

while True:
    methods.print_menu()
    option = int(input("\nExecute? : "))
    userConsole = None
    if option == 1:
        userConsole = input("""
            1. Instructor
            2. Department
            3. Course

            Which table's content would you like to see? Type the table name :         
            """)
        methods.display(userConsole)
    elif option == 2:
        department = input("please enter a department name: ")
        building = input("please enter a building name: ")
        budget = float(input("Please enter an amount of budget: "))
        print(f"""Please check your data:
            department = {department}
            building = {building}
            budget = {budget}
         """)
        confirmation = input("Insert? (y/n) :")
        confirmation = confirmation.lower()
        if confirmation == 'y':
            methods.insert_department(department, building, budget)
        else:
            pass
    elif option == 3:
        print("Department list:")
        methods.dept_list()
        department = input("please select a department that you want to modify it's budget: ")
        print("Selected department data: ")
        methods.dept_data(department)
        new_budget = float(input("\nNew budget of this department: "))
        methods.modify_budget(department, new_budget)
    elif option == 4:
        print("Department list:")
        methods.dept_list()
        department = input("please select a department that you want to delete: ")
        print("Selected department data: ")
        methods.dept_data(department)

        confirmation = input("Are you sure? (y/n) :")
        confirmation = confirmation.lower()
        if confirmation == 'y':
            methods.delete_department(department)
        else:
            pass
    elif option == 5:
        methods.exit_program()
        break
    else:
        print("Please Read the menu carefully!")
