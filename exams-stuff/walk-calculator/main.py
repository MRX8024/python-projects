import os

HOME_DIR = './'
IN_FILE = 'U2.txt'
OUT_FILE = 'U2_rez.txt'

data = {}
in_file_path = os.path.expanduser(f'{HOME_DIR}/{IN_FILE}')
with open(in_file_path, 'r') as file:
    n = int(file.readline())
    for line in file:
        line = line.strip()
        name = []
        for i in range(3):
            try:
                len = int(line.split(' ')[i])
                break
            except:
                name.append(line.split(' ')[i])
        name = ' '.join(name)
        if name in data:
            actual_len = data[name]
            actual_len = int(actual_len)
            total_len = actual_len + len
            data[name] = total_len
        else:
            data[name] = len

data = sorted(data.items(), key=lambda item: (-item[1], item[0]))
out_file_path = os.path.expanduser(f'{HOME_DIR}/{OUT_FILE}')
with open(out_file_path, 'w') as file:
    for name, length in data:
        file.write(f"{name:<20} {length}\n")
