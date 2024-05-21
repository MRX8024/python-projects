import os

HOME_DIR = './'
IN_FILE = 'data.txt'
OUT_FILE = 'out.txt'
MAX_MISTAKES = 5
MISTAKES_COEFF = 10
FIELD_SIZE = 10

def results(users):
    result = []
    max_points = max(users[user]['total_points'] for user in users)
    result.append(max_points)
    for user in reversed(users):
        if users[user]['total_points'] == max_points:
            result.append(f"{user:<{FIELD_SIZE}} {users[user]['city']}")
    if any(users[user]['mistakes'] > MAX_MISTAKES for user in users):
        result.append('Diskvalifikuoti:')
        for user in users:
            if users[user]['mistakes'] > MAX_MISTAKES:
                result.append(user)
    return result

users = {}
in_file_path = os.path.expanduser(f'{HOME_DIR}/{IN_FILE}')
with open(in_file_path, 'r') as file:
    lines = file.readlines()
    city_count = int(lines[0])
    line_num = 1
    for _ in range(city_count):
        city, users_ct = lines[line_num].split()
        line_num += 1
        for _ in range(int(users_ct)):
            name, points, mistakes = lines[line_num].split()
            points, mistakes = int(points), int(mistakes)
            total_points = points - (mistakes * MISTAKES_COEFF)
            users[name] = {'city': city, 'total_points': total_points, 'mistakes': mistakes}
            line_num += 1

out_file_path = os.path.expanduser(f'{HOME_DIR}/{OUT_FILE}')
with open(out_file_path, 'w') as file:
    for line in results(users):
        file.write(str(line) + '\n')
