import os

HOME_DIR = './'
IN_FILE = 'U2.txt'
OUT_FILE = 'U2_rez.txt'

def _line_parser(line):
    words = []
    for element in line:
        try:
            num = int(element)
        except ValueError:
            words.append(element)
    return ' '.join(words), num

in_file_path = os.path.expanduser(f'{HOME_DIR}/{IN_FILE}')
with open(in_file_path, 'r') as file:
    users, zuv_vert, zuv_total_weight = {}, {}, {}
    lines = file.readlines()
    users_count = int(lines[0].strip())
    line = 1
    for _ in range(users_count):
        name, zuv_count = _line_parser(lines[line].split())
        users[name] = []
        line += 1
        for _ in range(zuv_count):
            zuv_name, zuv_weight = _line_parser(lines[line].split())
            zuv_total_weight[zuv_name] = int(zuv_total_weight.get(zuv_name, 0)) + zuv_weight
            users[name].append({'name': zuv_name, 'weight': zuv_weight})
            line += 1

    for i in range(line, len(lines)):
        zuv_name, zuv_coeff = _line_parser(lines[i].split())
        zuv_vert[zuv_name] = zuv_coeff

# Calculate tasks
for name in users:
    task = 0
    for zuv in users[name]:
        task += 30 if zuv['weight'] > 200 else 10
        if zuv['name'] in zuv_vert:
            task += zuv_vert[zuv['name']]
    users[name] = task

# Formation out file
out_data = [f'Dalyviai']
users = sorted(users.items(), key=lambda item: item[1], reverse=True)
for name, task in users:
    out_data.append(f'{name:<20}{task}')

for zuv_name in zuv_vert:
    if zuv_name not in zuv_total_weight:
        if zuv_name != '':
            zuv_total_weight[zuv_name] = 0

sorted_zuv = dict(sorted(zuv_total_weight.items(), key=lambda item: item[1], reverse=True))
for zuv_name, weight in sorted_zuv.items():
    out_data.append(f"{zuv_name:<20}{weight}")

out_file_path = os.path.expanduser(f'{HOME_DIR}/{OUT_FILE}')
with open(out_file_path, 'w') as file:
    for line in out_data:
        file.write(f"{line}\n")

if __name__ != '__main__':
    raise exit(1)