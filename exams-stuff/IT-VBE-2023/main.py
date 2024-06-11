import os

def calc(in_file_path):
    data = {}
    with open(in_file_path, 'r') as file:
        file = file.readlines()
    for line in file[1:]:
        line = line.strip().split(' ')
        user = line[0]
        zingsn_len = line[1]
        total_count = 0
        if '0' in line[2:]:
            continue
        for count in line[2:]:
            total_count += int(count)
        total_travel = total_count * int(zingsn_len)
        total_travel /= 10**5 # cm in km
        if user in data:
            data[user]['total_travel'] += total_travel
            data[user]['users'] += 1
        else:
            data[user] = {'total_travel':total_travel, 'users':1}
    return data

if __name__ == '__main__':
    path = './'
    in_file_path = os.path.expanduser(path + 'U1.txt')
    out_file_path = os.path.expanduser(path + 'U1_rez.txt')
    data = calc(in_file_path)
    with open(out_file_path, 'w') as file:
        for i in data:
            file.write(f"{i} {data[i]['users']} {round(data[i]['total_travel'], 2)}\n")
