# task_manager

## Purpose
The program manages a list of tasks and their respective data. 
The program is meant to help a work team manage tasks assigned to each team member.
The program also allows for reporting on various task and team statistics.

## Access Control
The logins are saved in a text file - user.txt.

Entry to the main menu is dependent on successful login. 

Entry to the restricted menu options is dependent on a successful 'admin' login.

## Main Menu
*The main menu options are:*
  ###   Add task
 * Prompts user to enter task details.
 * Assigns the curent date as the task's value for "assigned date".
 * Assigns "No" as the task's value for "status" (complete/incomplete)
 * Updates the task list tasks.txt.
### View all tasks 
 * Displays all tasks in tasks.txt in a reader-friendly format.
### View my tasks
 * Display all tasks assigned to the logged-in user.
 * Allows user to select a task or exit to the main menu.
 * Allows the user to edit a selected task or mark a selected task as complete.
	* Edit task - allows user to reassign the task or change the due date.
	* Mark as complete - changes incomplete tasks' status to "Yes" (complete)
### Generate Reports
 * Task Overview - gathers task statistics calculated from task list tasks.txt, and
 creates report text file task_overview.txt.
 * User Overview - gathers user & task statistics from both txt files and
 creates report text file user_overview.txt.

## Restricted Menu Options
*Additional options for the admin user includes:*
### Register user
 * Allows admin user to add the new username for a new user.
 * Checks if the username already exists before accepting.
 * Allows admin user to enter the password for the new user.
 * Asks for the password to be confirmed before accepting.
 * Updates the user log (user.txt).
### Display Statistics
 * Generates/updates task_overview.txt & user_overview.txt.
 * Reads and displays task_overview.txt in a reader-friendly manner.
 * Reads and displays user_overview.txt in a reader-friendly manner.


