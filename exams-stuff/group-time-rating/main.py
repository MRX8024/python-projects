import os

HOME_DIR = './'
IN_FILE = 'U2.txt'
OUT_FILE = 'U2_rez.txt'
data = {}

def _line_parser(line):
    words = []
    num = []
    line = line.strip()
    for element in line:
        try:
            num.append(int(element))
        except ValueError:
            words.append(element)
    return ''.join(words), num

in_file_path = os.path.expanduser(f'{HOME_DIR}/{IN_FILE}')
with open(in_file_path, 'r') as file:
    lines = file.readlines()
    n = int(lines[0])
    line = 1
    group = 1
    for names in range(n):
        block = int(lines[line])
        line +=1
        data[group] = []
        for name in range(block):
            name, min = _line_parser(lines[line])
            try:
                mins = str(min[0]) + ' ' + str(min[1]) + str(min[2])
            except:
                mins = str(min[0]) + ' ' + str(min[1])
            try:
                min[2]
            except:
                min.append(0)
            sec = min[0] * 60 + min[1] + min[2]
            data[group].append({'name':name, 'min':mins, 'sec':sec})
            line +=1
        group +=1
data_ap = []
for group in data:
    data[group] = sorted(data[group], key=lambda x: x['sec'])
    cut = int(len(data[group]) / 2)
    for name in data[group][:cut]:
        data_ap.append(name)

data_ap = sorted(data_ap, key=lambda x: x['sec'])
out_file_path = os.path.expanduser(f'{HOME_DIR}/{OUT_FILE}')
with open(out_file_path, 'w') as file:
    for line in data_ap:
        name = line['name']
        min = line['min']
        file.write(f"{name:<20} {min}\n")