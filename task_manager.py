
# ______________________________FUNCTIONS_____________________________#

# *********FUNCTION - Register user***********(R)
def reg_user():
    new_username_acc = False
    count = 0
    users = 0
    username_list= []

# Get current user list
    with open('user.txt', 'r') as f:
        for line in f:
            username, pasword = line.split(',')
            username_list.append(username)

    users = len(username_list)

    # Set loop to get new username input, check against existing usernames,
    #   and save the new username once complete.
    while new_username_acc == False:
        new_username = input("New Username: ")
          
        while count < users:
            if new_username in username_list:
                print("That username is already in use.")
                new_username = input("New Username: ")
            else:
                count += 1
        if count == users:
            new_username_acc = True

    # Set loop for password entry and confirmation
    if new_username_acc == True:
        new_pword=input("New password: ")
        # Password confirmation
        confirm_pword=input("Confirm password: ")

        # LOOP - Failed password confirmation
        while new_pword != confirm_pword:
            print("Password confirmation failed.")
            new_pword = input("New Password: ")
            confirm_pword = input("Confirm Password: ")

        # EXPORT ACCESS - Append new user details to 'user.txt',
        # dependent on successful password confirmation
        if new_pword == confirm_pword:
            # FORMAT - new line of user detail
            new_login=(new_username +", " + new_pword)

            # EXPORT - Append new line to 'user.txt'
            with open('user.txt', 'a') as f:
                f.write(new_login+"\n")

# **************FUNCTION - Add task************
def add_task():
    owner = input("Username of person the task is assigned to: ")
    title = input("Task title: ")
    descr = input("Task description: ")
    due   = input("Due date: ")
    status= "No"

    # SYSTEM INPUT - ASSIGNED DATE: get current date
    from datetime import date
    assigned=date.today()

    # FORMAT - list of task details to write to 'user.txt'
    #          (date to be format to DD MON YYYY, e.g. 09 AUG 2020)
    task_list = [owner, title, descr, assigned.strftime("%d %b %Y"), due, status]

    # FORMAT - New Task line for append to 'tasks.txt'
    new_task=", ".join(task_list)

    # EXPORT - Append new task to 'tasks.txt'
    with open('tasks.txt', 'a') as g:
        g.write(new_task+"\n")
    
# **************FUNCTION - View all tasks*************
def view_all():
    n = 1

    # OPEN FILE - in read mode
    with open('tasks.txt','r') as g:
        for line in g:
            # DISPLAY - Heading per task
            print("\n"+"TASK " + str(n))

            # IMPORT - Details of task in list
            task_data = line.split(", ")
            owner, title, descr, own_date, due, status = task_data

            # FORMAT - Strip any line breaks contained in last value of
            #          each line ('status')
            comp = status.strip("\n")
                    
            # DISPLAY - Tasks in reader-friendly format
            print("User assigned:" + "\t" + owner +"\nTask Title:" + "\t" + title
                  +"\nAssigned:" + "\t" + own_date + "\nDue date:" + "\t" + due
                  + "\nComplete:" + "\t" + comp + "\nDescription:" + "\n" + descr)  

            # Update task number for heading per task
            n +=1

# **********FUNCTION - View (and edit) my tasks*********
def view_mine(user_id):

    # COUNTERS
    # for task heading to 1
    n = 1
    # for number of assigned tasks to 0
    tasks=0
    # for numbering full task list
    # (For full task list dictionary)
    task_num = 1

    # LISTS (To zip for dictionaries)
    # Keys for full task list dict
    task_key_list = []
    # Values for full task list dict
    fulltasklist = []
    # Keys for user task number dict
    key_list=[]
    # Values for user task number dict 
    usertasknum_list= []
    # BOOLEAN for main menu
    main_menu = False

    # DISPLAY SECTION        
    # OPEN FILE - in read mode
    with open('tasks.txt','r') as f:
        
        for line in f:
            # IMPORT - Details of task in list
            task_data=line.split(", ")

            # FORMAT - Save items in list as variables
            owner, title, descr, own_date, due, status = task_data

            # LIST UPDATE - Key list (with task number) for task list dictionary 
            task_key = task_num
            task_key_list.append(task_key)

            # LIST UPDATE - Value list (task items in list form) for task list dictionary
            fulltasklist.append(task_data)

            # LIST UPDATE - Task numbers for username (only incomplete tasks listed)
            if owner == user_id:
                comp = status.strip("\n")
                if comp == "No":
                    usertasknum_list.append(task_num)

            # COUNTER UPDATE (for full task list)
            task_num +=1
                       
            # DISPLAY - All tasks assigned to logged in user
            if user_id == owner:
                comp = status.strip("\n")
                key = n
                print("Task ", n,"\n", "{:<15}{}{:<20}".format("Task Title: ","\t", title), "\n", "{:<15}{}{:<20}".format("Assigned: ","\t",own_date), "\n",
                      "{:<15}{}{:<20}".format("Due date:","\t",due), "\n", "{:<15}{}{:<20}".format("Complete: ","\t", comp),
                      "\n", "{:<15}{}{}".format("Description:","\t", descr), "\n")

                # COUNTER UPDATE (for task heading)
                n +=1

                # COUNTER UPDATE (number of tasks assigned to user)
                tasks +=1

                # LIST UPDATE (user task numbers)
                key_list.append(key)
      
        # DISPLAY - For users with no assigned tasks
    if tasks==0:
        print("You have no tasks assigned.")

    # USER INPUT - Exit to menu (-1) or edit task 
    if tasks != 0:
               
        # ESCAPE - For users with no incomplete tasks (no edit option)
        if len(usertasknum_list) == 0:

            print("All tasks assigned to you have been completed.\n")

        # VIEW MINE MENU - Only for incomplete tasks
        #                           Options: Ecape to main menu, Mark task as complete, Edit task
        elif len(usertasknum_list) > 0:
            # DICTIONARY - Used to relay task changes to full list
            usertask_dict = dict(zip(key_list, usertasknum_list))
            print(usertask_dict)

            # DICTIONARY - For editing and writing to "tasks.txt'  
            task_dict = dict(zip(task_key_list, fulltasklist))

            # USER INPUT - View Mine menu choice
            editmenu_choice = int(input("\nEnter task number to edit task or enter '-1' to exit to main menu. \n"))
                
            # Exit to menu
            if editmenu_choice == -1:
                    
                print("Main Menu")
                # BOOLEAN - exit to main menu
                main_menu == True    

            # Edit selected task
            elif editmenu_choice >= 1:
                if editmenu_choice in usertask_dict.keys():
                    # Translate user-specific task number to task number in full task list
                    for k in usertask_dict:
                        if editmenu_choice == k:
                            task_key = usertask_dict[k]

                            # Use task number (from full list) to locate selected task 
                            for key, value in task_dict.items():
                                if task_key == key:
                                    owner, title, descr, own_date, due, status = value

                                    if status == "No\n":
                                        # TASK EDIT MENU - Mark task as complete task or edit task
                                        print("\nEnter desired action:\n1 - Mark the task as complete\n2 - Edit the task")
                                        edit_choice = int(input("(1/2): "))

                                        # Mark task as complete
                                        if edit_choice == 1:
                                            status = "Yes\n"
                                            task_dict[key] = owner, title, descr, own_date, due, status

                                        # EDIT MENU - Edit task assignment (username) or edit task due date
                                        elif edit_choice == 2:
                                            print("\nEnter desired action: \n1 - Reassign the task to a different user\n2 - Edit the due date")
                                            edittask_choice = int(input("(1/2)"))

                                            # Reassign task
                                            if edittask_choice == 1:
                                                owner = input("Enter the username of the new task owner:\n")
                                                task_dict[key] = owner, title, descr, own_date, due, status
                                
                                            # Edit task due date
                                            elif edittask_choice == 2:
                                                due = input("Enter the new due date (DD MON YYYY):\n")
                                                task_dict[key] = owner, title, descr, own_date, due, status
                                                
                                    # EXPORT - Update 'user.txt' with new task details
                                    with open('tasks.txt', 'w') as f: 
                                        for key, value in task_dict.items():
                                            task = ", ".join(task_dict[key])
                                            f.write(task)
                    
                else:
                    print("The selected task is complete and cannot be edited.")
                       
# ***********FUNCTIONS - Generate Reports**************
#Task Report
def tot_tasks():
    tot_tasks_num = 0                           
    with open('tasks.txt', 'r') as g:
        for line in g:
            line = line.strip('\n')
            tot_tasks +=1                    

    return tot_tasks_num

def comp_tasks():
    comp_task_num = 0
    
    with open('tasks.txt','r') as g:
        for line in g:
            line = line.strip('\n')
            task_data = line.split(', ')
            status = task_data[5]
            if status == "Yes":
                comp_task_num += 1

    return comp_task_num

def incomp_tasks():
    incomp_task_num = 0
    
    with open('tasks.txt','r') as g:
        for line in g:
            line = line.strip('\n')
            task_data = line.split(', ')
            status = task_data[5]
            if status == "No":
                incomp_task_num += 1

    return incomp_task_num

def overdue_tasks():
    duedate_dict = {}
    incomp_num = 0
    overdue_num = 0

    with open('tasks.txt','r') as g:
        for line in g:
            line = line.strip('\n')
            task_data = line.split(', ')
            status = task_data[5]
            due = task_data[4]
          
            from datetime import datetime
            format = '%d %b %Y'
            due_date = datetime.strptime(due, format).date()

            from datetime import date
            date_today = date.today()
           
            
            if status == "No":
                incomp_num += 1
                if due_date < date_today:
                    overdue_num += 1

    return overdue_num

def tasks_report():
    task_report_list = []

    header_list = ['Total tasks:','Completed tasks:', 'Uncompleted tasks:',
                   'Overdue tasks:', '% Incomplete:', '% Overdue:']

    incomp_percent = int((100 *incomp_tasks()) / tot_tasks())
    over_percent = int((100*overdue_tasks())/tot_tasks())
      
    with open('task_overview.txt','w') as h:
        h.write("{:>18}{:>5}{}".format(header_list[0], tot_tasks(),"\n"))
        h.write("{:>18}{:>5}{}".format(header_list[1], comp_tasks(),"\n"))
        h.write("{:>18}{:>5}{}".format(header_list[2], incomp_tasks(),"\n"))
        h.write("{:>18}{:>5}{}".format(header_list[3], overdue_tasks(),"\n"))
        h.write("{:>18}{:>5}{}".format(header_list[4], incomp_percent,"\n"))
        h.write("{:>18}{:>5}{}".format(header_list[5], over_percent,"\n"))


# **********FUNCTIONS - Generate Reports (User Report)***********
# FUNCTION - Total tasks in 'tasks.txt' (int)
def tot_users():
    tot_users = 0
    with open('user.txt', 'r') as c:
        for line in c:
            line = line.strip('\n')
            tot_users += 1
    return tot_users

def tot_tasks():
    tot_tasks = 0
    with open('tasks.txt', 'r') as g:
        for line in g:
            line = line.strip('\n')
            tot_tasks +=1

    return tot_tasks

# FUNCTION - Usernames in 'tasks.txt' (list)
def userlist():
    users_list = []
    owned_perc_list = []
   
    with open('tasks.txt', 'r') as g:
        for line in g:
            line = line.strip("\n")
            task_data = line.split(", ")
            owner = task_data[0]
            if owner not in users_list:
                users_list.append(owner)

    return users_list

# FUNCTION - Tasks assigned count per user (dict)
def user_owned():
    users_list = userlist()
    owned_count_list = []
    userstats_dict = {}
    
               
    for i in range(len(users_list)):
        owned_count = 0
        with open('tasks.txt', 'r') as g:
            for line in g:
                line = line.strip("\n")
                task_data = line.split(", ")
                owner = task_data[0]
                if owner == users_list[i]:
                    owned_count += 1
        owned_count_list.append(owned_count)

        userowned_dict = dict(zip(users_list,owned_count_list))
    return userowned_dict

# FUNCTION - Tasks completed count per user (dict)
def user_complete():
    users_list = userlist()
    comp_count_list = []
    user_owned()

    for i in range(len(users_list)):
        comp_count = 0
        with open('tasks.txt', 'r') as g:
            for line in g:
                line = line.strip("\n")
                task_data = line.split(", ")
                owner = task_data[0]
                status = task_data[5]
                if owner == users_list[i]:
                    if status == "Yes":
                        comp_count += 1
        comp_count_list.append(comp_count)

        usercomp_dict = dict(zip(users_list, comp_count_list))
                
    return usercomp_dict


# FUNCTION - Tasks uncompleted count per user (dict)
def user_incomp():
    users_list = userlist()
    incomp_count_list = []

    for i in range(len(users_list)):
        incomp_count = 0
        with open('tasks.txt', 'r') as g:
            for line in g:
                line = line.strip("\n")
                task_data = line.split(", ")
                owner = task_data[0]
                status = task_data[-1]
                if owner == users_list[i]:
                    if status == "No":
                        incomp_count += 1

        incomp_count_list.append(incomp_count)
            
    userincomp_dict =dict(zip(users_list, incomp_count_list))

    return userincomp_dict

# FUNCTION - Tasks overdue count per user (dict)
def user_over():
    users_list = userlist()
    overdue_count_list = []

    for i in range(len(users_list)):
        overdue_count = 0
        with open('tasks.txt', 'r') as g:
            for line in g:
                line = line.strip("\n")
                task_data = line.split(", ")
                owner = task_data[0]
                status = task_data[-1]
                due = task_data[4]
                from datetime import datetime
                format = '%d %b %Y'
                due_date = datetime.strptime(due, format).date()
                #print(due_date)

                from datetime import date
                date_today = date.today()
            
                if owner == users_list[i]:
                    if status == "No":
                        if due_date < date_today:
                            overdue_count += 1

            overdue_count_list.append(overdue_count)

        useroverdue_dict = dict(zip(users_list, overdue_count_list))

    return useroverdue_dict

# FUNCTION - Percentage of total tasks assigned per user (dict)
def userowned_perc():
    users_list = userlist()
    user_tot = user_owned()
    owned_perc_list = []
              
    for user in users_list:
        owned_perc = round((100*user_tot[user])/tot_tasks())
        owned_perc_list.append(owned_perc)

    usertot_perc = dict(zip(users_list,owned_perc_list))

    return usertot_perc

# FUNCTION - Percentage of assigned tasks completed per user (dict)
def usercomplete_perc():
    users_list = userlist()
    user_tot = user_owned()
    usercomp_dict = user_complete()
    comp_perc_list = []

    for user in users_list:
        comp_perc = round((100*usercomp_dict[user])/user_tot[user])
        comp_perc_list.append(comp_perc)

    usercomp_perc = dict(zip(users_list,comp_perc_list))

    return usercomp_perc

# FUNCTION - Percentage of assigned tasks uncompleted per user (dict)
def userincomplete_perc():
    users_list = userlist()
    user_tot = user_owned()
    userincomp_dict = user_incomp()
    incomp_perc_list = []

    for user in users_list:
        incomp_perc = round((100*userincomp_dict[user])/user_tot[user])
        incomp_perc_list.append(incomp_perc)

    userincomp_perc = dict(zip(users_list,incomp_perc_list))

    return userincomp_perc

# FUNCTION - Percentage of assigned tasks overdue per user (dict)
def useroverdue_perc():
    users_list = userlist()
    user_tot = user_owned()
    userover_dict = user_over()
    overdue_perc_list = []

    for user in users_list:
        overdue_perc = round((100*userover_dict[user])/user_tot[user])
        overdue_perc_list.append(overdue_perc)

    userover_perc = dict(zip(users_list,overdue_perc_list))

    return userover_perc

# FUNCTION - Print dictionaries to 'user_overview'
def user_report():
    users_list = userlist()
    keys = users_list

    userstats_dict =  {x:[] for x in keys}
    
    # REFERENCE - user_owned() - dictionary
    user_tot = user_owned()
    user_tot_perc = userowned_perc()
    usercomp_perc = usercomplete_perc()
    userincomp_perc = userincomplete_perc()
    userover_perc = useroverdue_perc()
    keys = users_list

    # FORMAT - Combining all user data dictionaries for user_overview export
    userstats_dict =  {x:[] for x in keys}
    for x in [user_tot,user_tot_perc,usercomp_perc,userincomp_perc,userover_perc]:
        for k, v in x.items():
            userstats_dict[k].append(v)
    
    # Headings for columns in user_overview
    heading_list = ['Assigned','% Assigned', '% Complete', '% Incomplete', '% Overdue']
    
    with open("user_overview.txt","w") as j:
        j.write("{:<15}{:<5}{}".format("Total users:",tot_users(),"\n"))
        j.write("{:<15}{:<5}{}".format("Total tasks:",tot_tasks(),"\n"))

        j.write("{:>16}".format("User:"))
        for header in heading_list:
            j.write("{:>15}".format(header))

        j.write("{}".format("\n"))
        for key,value in userstats_dict.items():
                assigned, assignper, compper, incompper, overper = value
                j.write("{:>15}{}{:>15}{:>15}{:>15}{:>15}{:>15}{}".format(key,":", assigned, assignper, compper, incompper, overper, "\n"))

def gen_reports():
    tasks_report()
    user_report()

# *************FUNCTIONS - Display Statistics****************

# Print Task Overview
def displaystat_task():

    # Heading
    print("\tTask Overview")

    # Row headers & values
    # Split lines from text file
    with open('task_overview.txt','r') as k:
        for line in k:
            heading, value = line.split(":")

            # Format for print
            heading = heading.strip(" ")
            heading = heading + ":"
            value = int(value.strip(" "))
            
            #Print Task Overview statistics
            print("{:<18}{:>5}{:>3}".format(heading,"\t",value))
        

#Print User Overview
def displaystat_user():

    #*Heading - print*
    print("\n\tUser Overview")

    #*Row headers & values - print*

    # Save split lines from user_overview
    with open('user_overview.txt','r') as m:
        usertable = [line.split(": ") for line in m.read().splitlines()]

    # Lines with single values - print
    totals_list = usertable[:2]
    # Split lines from text file
    for line in totals_list:
        heading, value = line

        # Format for print
        heading = heading.strip(" ") + ":"
        value =  value.strip(" ")

        # Print single-value lines
        print("{:<18}{:>5}{:>3}".format(heading, "\t", value))

    # List for column headings (headings for values in table)
    colheader_list = []

    # Column headings for user breakdown - print
    heading_list = usertable[2]

    header_1 = heading_list[0].strip(" ")

    # Update column header list to correct format
    colheader_list.append(header_1)
    
    columns = heading_list[1:]
    for item in columns:
        item = item.strip(" ")
        
        item = item.split("%")
        for val in item:
            val = val.strip(" ")
            
            colheader_list.append(val)
    col1 = colheader_list[0] + ":"
    col2 = colheader_list[1]
    col3 = "% " + colheader_list[2]
    col4 = "% " + colheader_list[3]
    col5 = "% " + colheader_list[4]
    col6 = "% " + colheader_list[5]

    # Print column headers in reader-friendly format
    print("{:<2}{:<5}{:>2}{:>14}{:>16}{:>16}{:>15}{:>15}".format("\t", col1, "\t", col2, col3, col4, col5, col6))

    #*Row headers & values list - print*
    userstats_rows = []

    # User breakdown - Print
    userstats_raw = usertable[3:]
    
    # Split row headers from values
    for line in userstats_raw:
        row_head = line[0].strip(" ") + ":"
        user_values= line[-1].split()
        v1, v2, v3, v4, v5 = user_values
        print("{:<2}{:<7}{:>2}{:>16}{:>20}{:>21}{:>19}{:>19}".format("\t", row_head,"\t", v1,v2, v3, v4, v5))

# Display Statistics Function
def display_stat():
    gen_reports()
    displaystat_task()
    displaystat_user()

###-----------------PROGRAM START--------------------###   

# BOOLEAN VALUES - Set to False 
user = False
passw = False
logged_in = False
main_menu = False

#---------------------------LOG IN---------------------------
# LOOP - Username entry
while logged_in == False:
    user_entry = input("Enter username: ")

    # OPEN FILE - in read mode
    with open('user.txt','r') as f:
        for line in f:

            # IMPORT - Create lists for usernames & passwords
            username, password_1 = line.split(", ")

            # FORMAT - Strip all new line breaks from password values
            password  = password_1.strip("\n")

            # BOOLEAN TEST - Username
            if user_entry == username:
                user = True
                
                # LOOP - Password entry
                while passw == False:
                    passw_entry = input("Enter password: ")

                    #OPEN FILE - in read mode
                    with open('user.txt', 'r') as f:
                        for line in f:

                            # BOOLEAN TEST - Password                                           
                            if passw_entry == password:
                                passw = True

                                # BOOLEAN TEST - Log in
                                logged_in = True

                                
                                # Save user ID for user specific options
                                user_id = user_entry
                                
                    # ERROR MSG - Password entry
                    if passw == False:
                        print("Invalid password.")

                    
    # ERROR MSG - Username entry        
    if user == False:
        print("Invalid username.")

#-----------------------------MENU ACCESS----------------------------
# MENU ACCESS - Dependent on successful log in.
if logged_in:
    # BOOLEAN TEST - Main menu                                
    main_menu = True

    # BOOLEAN - Escape to main menu
    while main_menu:

        #-------------------RESTRICTED ACCESS MENU-----------------------
            # RESTRICTED MENU ACCESS - Dependent on 'admin' log-in.
        if user_id == "admin":
            # DISPLAY - Restricted menu (R)
            menu_choice=input("Please select one of the following options:" + "\nr - register user"
                              + "\na - add task" + "\nva - view all tasks" + "\nvm - view my tasks"
                              +"\ngr - generate reports" + "\nds - display statistics" + "\ne - exit" +"\n""")

            # Register new user details to 'user.txt' (R)
            if menu_choice == "r":
                print("New User")
                reg_user()
                main_menu = False

            # Add new task details in 'task.txt' (R)
            elif menu_choice == "a":
                print("New Task")
                add_task()
                main_menu = False

            # View all tasks in 'tasks.txt' (R)
            elif menu_choice == "va":
                view_all()
                main_menu = False

            # View all tasks in 'tasks.txt' assigned to logged in user (R)
            elif menu_choice == "vm":
                view_mine(user_id)

            # Generate Reports (R)
            elif menu_choice == "gr":
                gen_reports()
                main_menu = False

            # Display Statistics (R)
            elif menu_choice == "ds":
                display_stat()
                main_menu = False

            # Exit Menu (R)
            elif menu_choice == "e":
                main_menu = False
                logged_in = False
                print("\nLogged out.")

    #----------------------------------------MAIN MENU------------------------------------------------

        # MAIN MENU ACCESS - If not 'admin log-in
        if user_id != "admin":
            # DISPLAY - Main Menu
            menu_choice=input("Please select one of the following options:" + "\na - add task"
                              + "\nva - view all tasks" + "\nvm - view my tasks" + "\ngr - generate reports"
                              + "\ne - exit" +"\n")

            # Add new task details in 'task.txt'
            if menu_choice == "a":
                print("Add New Task")
                add_task()
                main_menu = False

            # View all tasks in 'tasks.txt'
            elif menu_choice == "va":
                print("All Tasks")
                view_all()
                main_menu = False

            # View all tasks in 'tasks.txt' assigned to logged in user
            elif menu_choice == "vm":
                view_mine(user_id)
                
            # Generate Reports
            elif menu_choice == "gr":
                gen_reports()
                main_menu = False

            # Exit Menu
            elif menu_choice == "e":
                main_menu = False
                logged_in = False
                print("\nLogged out.")

#--------------------------------END-------------------------------------

