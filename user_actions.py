import file_working
import xml.etree.ElementTree as ET


def add_task(name, description):
    file_working.change_text('tasks.xml', '</task_list>')

    id = file_working.get_last_id("tasks.xml")
    xml = f'<task id = "{id}">\n'
    xml += f'\t<task_name>{name}</task_name>\n'
    xml += f'\t<description>{description}</description>\n'
    xml += '\t<status>in progress</status>\n'
    xml += '</task>\n'
    xml += '</task_list>'

    file_working.write_file('tasks.xml', xml)
    file_working.logs(id, 'created')


def change_status(id_of_task):
    tree = ET.parse('tasks.xml')
    root = tree.getroot()
    ids = []
    for i in range(len(root)):
        ids.append(int(root[i].attrib['id']))
    if id_of_task in ids:
        for i in range(0, len(root)):
            if id_of_task == int(root[i].attrib['id']):
                root[i][2].text = 'completed'
                tree.write('tasks.xml')
                file_working.logs(id_of_task, 'completed')
    else:
        print("\033[1;31m <There isn't this id> \033[0m")


def del_task(id_of_task):
    tree = ET.parse('tasks.xml')
    root = tree.getroot()
    ids = []
    for i in range(len(root)):
        ids.append(int(root[i].attrib['id']))
    if id_of_task in ids:
        for i in root:
            if id_of_task == int(i.attrib['id']):
                root.remove(i)
                tree.write('tasks.xml')
                file_working.logs(id_of_task, 'deleted')
                break
    else:
        print("\033[1;31m <There isn't this id> \033[0m")


def print_xml():
    tree = ET.parse('tasks.xml')
    root = tree.getroot()
    text1 = []
    text2 = []
    if len(root) > 0:
        for i in range(len(root)):
            text1.append(root[i].attrib['id'])
            for j in range(len(root[i])):
                text1.append(root[i][j].text)
            text2.append(text1)
            text1 = []
        print("|| {0:3} || {1:15} || {2:30} || {3:13}||".format('id', 'name', 'description', 'status'))
        print('-' * 78)
        for i in range(len(text2)):
            print("|| {0:3} || {1:15} || {2:30} || {3:13}||".format(text2[i][0], text2[i][1], text2[i][2], text2[i][3]))
        print('-' * 78)


def print_log():
    logs = file_working.read_file('logs.txt')
    print(logs)
    input('Press enter to continue')


def clean_log():
    agrement = input("\033[1;31m <Enter 'YES' if you sure> \033[0m")
    if agrement == 'YES':
        file_working.rewrite_file('logs.txt', '')
    else:
        print('\033[32m Action aborted \033[0m')