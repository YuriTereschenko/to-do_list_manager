import user_actions


def to_do_list():
    while True:
        user_actions.print_xml()
        action = input('Choose an action:\n"+" to add a new task\n"-" to delete a task\n'
                       '"*" to mark a task as completed\n"l" to view logs\n"cl" to clean logs\n"e" to exit the program\n')
        match action:
            case '+':
                name = input('Enter task name: ')
                description = input('Enter the task description: ')
                user_actions.add_task(name, description)
            case '-':
                id = int(input("Enter the task's id to delete: "))
                user_actions.del_task(id)
            case '*':
                id = int(input("Enter the task's id to mark it as completed: "))
                user_actions.change_status(id)
            case 'e':
                exit(0)
            case 'l':
                user_actions.print_log()
            case 'cl':
                user_actions.clean_log()
            case _:
                print("\033[1;31m <It's not a correct action> \033[0m")
