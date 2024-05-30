import os

HOME_DIR = './'
IN_FILE = 'U2.txt'
OUT_FILE = 'U2_rez.txt'
data = []

def _line_parser(line):
    words = []
    line = line.strip()
    for en, symbol in enumerate(line):
        try:
            int(symbol)
            point = en
            break
        except ValueError:
            words.append(symbol)
    nums = line[point:].split(' ')
    return ''.join(words), nums

in_file_path = os.path.expanduser(f'{HOME_DIR}/{IN_FILE}')
with open(in_file_path, 'r') as file:
    lines = file.readlines()

line = 1
group = 0
n = int(lines[0])
for names in range(n):
    block = int(lines[line])
    data.append([])
    line +=1
    for name in range(block):
        name, min = _line_parser(lines[line])
        sec = int(min[0]) * 60 + int(min[1])
        min = ' '.join(min)
        data[group].append({'name':name, 'min':min, 'sec':sec})
        line +=1
    group +=1

data_ap = []
for group in range(len(data)):
    data[group] = sorted(data[group], key=lambda x: x['sec'])
    cut = int(len(data[group]) / 2)
    for name in data[group][:cut]:
        data_ap.append(name)

data_ap = sorted(data_ap, key=lambda x: x['sec'])
out_file_path = os.path.expanduser(f'{HOME_DIR}/{OUT_FILE}')
with open(out_file_path, 'w') as file:
    for line in data_ap:
        file.write(f"{line['name']:<20} {line['min']}\n")