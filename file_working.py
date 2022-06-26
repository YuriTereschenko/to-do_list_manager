import datetime as dt
from bs4 import BeautifulSoup as BS


def readlines_file(path):
    with open(path, 'r') as txt:
        file_data = txt.readlines()
        txt.close()
    return file_data


def read_file(path):
    with open(path, 'r') as txt:
        file_data = txt.read()
        txt.close()
    return file_data


def write_file(path, data_to_write):
    with open(path, 'a') as txt:
        txt.write(data_to_write)
        txt.close()


def rewrite_file(path, data_to_write):
    with open(path, 'w') as txt:
        txt.writelines(data_to_write)
        txt.close()


def logs(id, change):
    date = dt.datetime.now()
    write_file('logs.txt', f'{date} Task "{id}" {change}.\n')


def change_text(path, text_del):
    file = readlines_file(path)
    file.remove(text_del)
    rewrite_file(path, file)


def get_last_id(path):
    last_id = 0
    fd = open(path, 'r')
    xml_file = fd.read()
    soup = BS(xml_file, 'lxml')
    for tag in soup.findAll("task"):
        last_id = tag["id"]
    last_id = int(last_id) + 1
    return last_id
