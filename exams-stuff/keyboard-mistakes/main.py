import os
HOME_DIR = './'
FILE_PATH = os.path.expanduser(f'{HOME_DIR}/data.txt')

def results(users):
    result = []
    max_points = max(users[user]['total_points'] for user in users)
    result.append(max_points)
    for user in reversed(users):
        if users[user]['total_points'] == max_points:
            result.append(f"{user:<10} {users[user]['city']}")
    if any(users[user]['mistake'] > 5 for user in users):
        result.append('Diskvalifikuoti:')
    for user in users:
        if users[user]['mistake'] > 5:
            result.append(f"{user:<10}")
    return result

users = {}
with open(FILE_PATH, 'r') as file:
    lines = file.readlines()
    city_count = int(lines[0])
    line_num = 1
    for _ in range(city_count):
        city, users_ct = lines[line_num].split()
        line_num += 1
        for _ in range(int(users_ct)):
            name, points, mistake = lines[line_num].split()
            points, mistake = int(points), int(mistake)
            total_points = points - (mistake * 10)
            users[name] = {'city': city, 'total_points': total_points, 'mistake': mistake}
            line_num += 1

for line in results(users):
    print(line)
