import os

HOME_DIR = './'
IN_FILE = 'U2.txt'
OUT_FILE = 'U2_rez.txt'
users_data = {}
finish_data = {}

def _line_parser(line):
    clear_line = line.strip()
    words = []
    nums = []
    for element in clear_line:
        try:
            int(element)
            break
        except ValueError:
            words.append(element)
    skip = False
    for element in range(len(line)):
        if skip:
            skip = False
            continue
        try:
            int(line[element])
            try:
                int(line[element + 1])
                num = int(line[element] + line[element + 1])
                nums.append(num)
                skip = True
            except ValueError:
                nums.append(int(line[element]))
        except ValueError:
            pass
    sec = (nums[0] * 60 * 60) + (nums[1] * 60) + nums[2]
    return ''.join(words), sec

in_file_path = os.path.expanduser(f'{HOME_DIR}/{IN_FILE}')
with open(in_file_path, 'r') as file:
    lines = file.readlines()
    n = int(lines[0])
    m = n + 2
    for line in range(m, len(lines)):
        name, sec =_line_parser(lines[line])
        finish_data[name] = {'name':name, 'sec':sec}

    for line in range(1, n):
        name, sec =_line_parser(lines[line])
        if name in finish_data:
            sec = int(finish_data[name]['sec']) - int(sec)
            hour = int(sec / 60 / 60)
            if hour < 1:
                sec -= int(hour * 60 * 60)
                min = int(sec / 60)
                sec -= int(min * 60)
                time = [min, sec]
                users_data[name] = {'name': name, 'time': time}

users_data = sorted(users_data.items(), key=lambda x: x[1]['name'], reverse=True)
out_file_path = os.path.expanduser(f'{HOME_DIR}/{OUT_FILE}')
with open(out_file_path, 'w') as file:
    for name, time in users_data:
        file.write(f"{name:<20} {time['time'][0]} {time['time'][1]}\n")