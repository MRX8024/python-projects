import os
HOME_DIR = './'
FILE_PATH = os.path.expanduser(f'{HOME_DIR}/data1.txt')

users = {}
line = 0

with open(FILE_PATH, 'r') as file:
    city_count = int(file.readline())
    k = len(list(file))
    while k:
        line += 1
        data = list(file[line]).strip()
        city = data.strip(' ')[0]
        users_ct = data.strip(' ')[1]
        for user in users_ct:
            line += 1
            data = file[line].strip()
            name = data.strip(' ')[0]
            nonmistake = data.strip(' ')[1]
            mistake = data.strip(' ')[2]
            users[name] = {'nonmistake':nonmistake, 'mistake': mistake}

