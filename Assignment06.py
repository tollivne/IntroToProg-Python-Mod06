# ------------------------------------------------------------------------ #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# N. Tolliver,5.23.2020, Created script from starter file
# N. Tolliver, 5.23.2020, Created & call function to collect task & priority from user
# N. Tolliver, 5.23.2020, Created & call function to write task list to a file
# N. Tolliver, 5.24.2020, Added a function to Get a Task to be removed
# N. Tolliver, 5.24.2020, Added a function to get a yes/no answer from the user
# N. Tolliver, 5.24.2020, Added a function to display an optional message and press enter to continue
# N. Tolliver, 5.24.2020, Renamed functions to be consistent with new starter code posted on Canvas
# N. Tolliver, 5.24.2020, Re-ordered functions to be consistent with new starter code
# N. Tolliver, 5.24.2020, Added variables strTask, strPriority, and strStatus to the Data section
# N. Tolliver, 5.24.2020, Removed menu option 1 for displaying current items in the list
# N. Tolliver, 5.24.2020, Renumbered menu items and options in the code
# N. Tolliver, 5.24.2020, Made displaying items in the list automatic at the start of the while loop
# N. Tolliver, 5.24.2020, Solved problem in code for removing a task by returning the Boolean value to controller
# N. Tolliver, 5.25.2020, Added "Success" as a return value for all processing functions
# N. Tolliver, 5.25.2020, Changed call to all processing functions to unpack tuple to get strStatus
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A dictionary that acts as a 'table' of rows
strChoice = ""  # Capture the user option selection
strTask = "" # Captures the user task data
strPriority = "" # Captures the user priority data
strStatus = "" # Captures the status of the processing function

# Processing  ------------------------------------------------------------- #
class Processor:
    """ Processing the data to and from a text file """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """
        Desc - Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows, Status
        """
        file = open(file_name, "r")
        for line in file:
            data = line.split(",")
            row = {"Task": data[0].strip(), "Priority": data[1].strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, "Success"

    @staticmethod
    def add_data_to_list (task, priority, list_of_rows):
        """ This function adds a Task and Priority to the Table
        param: Task and Priority
        return: Updated list Table, Status
        """
        dicRow = {"Task": task, "Priority": priority}  # Create a new dictionary row
        list_of_rows.append(dicRow)  # Add the new row to the list/table
        return list_of_rows, "Success"

    @staticmethod
    def remove_data_from_list(task, list_of_rows, item_removed_status):
        """ This function finds a task that the user wants to remove
        :param: Task to be Removed, ToDo List, Removed Status
        :return: ToDo List, Removed Status, Status
        """
        intRowNumber = 0  # Create a counter to identify the current dictionary row in the loop

        # Step 3.3.b - Search though the table or rows for a match to the user's input
        while (intRowNumber < len(lstTable)):
            if (strKeyToRemove == str(list(dict(lstTable[intRowNumber]).values())[0])):  # Search current row column 0
                del lstTable[intRowNumber]  # Delete the row if a match is found
                item_removed_status = True  # Set the flag so the loop stops
            intRowNumber += 1  # Increase counter to get next row

        return list_of_rows, item_removed_status, "Success"

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        # TODO: Add code Here - Done
        """ This function writes the task list to a text file
        :param: File Name, ToDo List
        :return: ToDo List, Status
        """
        objFile = open(file_name, "w")
        for dicRow in list_of_rows:  # Write each row of data to the file
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()
        return list_of_rows, "Success"
    # TODO: Create more functions that perform various Processing task as needed

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ A class for performing Input and Output """

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new item.
        2) Remove an existing item.
        3) Save Data to File
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 6] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_tasks_in_list(list_of_rows):
        """ Shows the current items in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current items ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    # TODO: Create more functions that perform various IO tasks as needed
    @staticmethod
    def input_yes_no_choice(message):
        """  Get a yes or no choice from the user
             param: Question to be asked of the user
             return: y or n answer
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message):
        """ Pause the program and display a message before continuing
        param: optional_message:  An optional message to display to the user
        return: nothing
        """
        print(optional_message)
        input("Press the [Enter] key to return to menu.")

    @staticmethod
    def input_new_task_and_priority ():
        """ This function prompts the user to enter the task & priority
        param: none
        return: Task name & Task priority (High/Low)
        """
        task = str(input("What is the task? - ")).strip()  # Get task from user
        priority = str(input("What is the priority? [high|low] - ")).strip()  # Get priority from user
        print()  # Add an extra line for looks
        return(task, priority)

    # Note, removing the task is in processing, however, getting the task is IO
    @staticmethod
    def input_task_to_remove():
        remove = input("Which TASK would you like removed? - ")  # get task user wants deleted
        return (remove)

# Main Body of Script  ---------------------------------------------------- #

# Step 1 - When the program starts, Load data from ToDoFile.txt.

lstTable, strStatus = Processor.read_data_from_file(strFileName, lstTable)

# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Step 4 - Process user's menu choice

    if(strChoice.strip() == '1'): # Add a new task

        # Ask user for new task and priority
        # Moved IO task to a function

        strTask, strPriority = IO.input_new_task_and_priority() # unpack tuple

        # Add item to the List/Table
        # Moved processing code to a function

        lstTable, strStatus = Processor.add_data_to_list(strTask, strPriority, lstTable)

        continue  # to show the menu

    # Remove a task from the list/Table
    elif(strChoice == '2'):

        # Step 3.3.a - Ask user for item and prepare searching while loop

        strKeyToRemove = IO.input_task_to_remove() # get task user wants deleted

        blnItemRemoved = False  # Create a boolean Flag for loop

        # Moved processing code to a new function

        lstTable, blnItemRemoved, strStatus = \
            Processor.remove_data_from_list(strKeyToRemove, lstTable, blnItemRemoved)  # unpack tuple

        # Update user on the status of the search
        if(blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")
        print()  # Add an extra line for looks

        continue  # to show the menu

    # Save tasks to the ToDoFile.txt file
    elif(strChoice == '3'):

        #Show the current items in the table
        IO.print_current_tasks_in_list(lstTable)  # Show current data in the list/table

       # Ask if user if they want save that data
        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):  # Double-check with user

            # Placed processing code in a New function

            lstTable, strStatus = Processor.write_data_to_file(strFileName, lstTable)

            IO.input_press_to_continue("Data saved to file!")

        else:  # Let the user know the data was not saved

            IO.input_press_to_continue("New data was NOT Saved, but previous data still exists!")

        continue  # to show the menu

    # Reload data from the ToDoFile.txt file (clears the current data from the list/table)
    elif (strChoice == '4'):
        print("Warning: This will replace all unsaved changes. Data loss may occur!")  # Warn user of data loss

        strYesOrNo = IO.input_yes_no_choice ("Reload file data without saving? [y/n] - ")   # Double-check with user

        if (strYesOrNo.lower() == 'y'):
            lstTable.clear()  # Added to fix bug 1.1.2030
              # Replace the current list data with file data
            lstTable, strStatus = Processor.read_data_from_file(strFileName, lstTable)
        else:
            IO.input_press_to_continue("File data was NOT reloaded!")

        continue  # to show the menu

    # Step 3.6 - Exit the program
    elif (strChoice == '5'):
        break   # and Exit

# Main Body of Script  ---------------------------------------------------- #