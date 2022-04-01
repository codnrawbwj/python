from db import univDB


def print_menu():
    print(""" 
    1. Display Contents
    2. Insert Record to the Department
    3. Modify Budget of a Department
    4. Delete a Department
    5. Exit
    """)


def display(table):
    dbcursor = univDB.cursor()
    table = table.lower()
    if table == "instructor":
        dbcursor.execute("select * from instructor")
        dbcontent = dbcursor.fetchall()
        for data in dbcontent:
            print(data)
    elif table == "department":
        dbcursor.execute("select * from department")
        dbcontent = dbcursor.fetchall()
        for data in dbcontent:
            print(data)
    elif table == "course":
        dbcursor.execute("select * from course")
        dbcontent = dbcursor.fetchall()
        for data in dbcontent:
            print(data)
    else:
        print("Please check your input!")


def insert_department(department, building, budget):
    dbcursor = univDB.cursor()
    query = "insert into department (dept_name, building, budget) values (%s, %s, %s)"
    insert_value = (department, building, budget)
    dbcursor.execute(query, insert_value)
    univDB.commit()
    print("Data has been inserted.")


def dept_list():
    dbcursor = univDB.cursor()
    dbcursor.execute("select dept_name from department")
    dbcontent = dbcursor.fetchall()
    for data in dbcontent:
        print(data)


def dept_data(dept):
    dbcursor = univDB.cursor()
    query = "select dept_name, building, budget from department where dept_name = %s"
    insert_value = (dept,)
    dbcursor.execute(query, insert_value)
    dbcontent = dbcursor.fetchall()
    print(dbcontent)


def modify_budget(dept, budget):
    dbcursor = univDB.cursor()
    query = "update department set budget = %s where dept_name = %s"
    insert_value = (budget, dept)
    dbcursor.execute(query, insert_value)
    univDB.commit()
    print("\nDatabase updated!\nNew data:")

    new_query = "select dept_name, building, budget from department where dept_name = %s"
    insert_value = (dept,)
    dbcursor.execute(new_query, insert_value)
    dbcontent = dbcursor.fetchall()
    print(dbcontent)


def delete_department(dept):
    dbcursor = univDB.cursor()
    query = "delete from department where dept_name = %s"
    insert_value = (dept,)
    dbcursor.execute(query, insert_value)
    univDB.commit()
    print("\nData deleted!")


def exit_program():
    print("\nThank your for using our program!")
