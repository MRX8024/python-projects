import os

HOME_DIR = './'
IN_FILE = 'U2.txt'
OUT_FILE = 'U2_rez.txt'

product = {}
in_file_path = os.path.expanduser(f'{HOME_DIR}/{IN_FILE}')
with open(in_file_path, 'r') as file:
    n = int(file.readline())
    for line in file:
        line = line.strip()
        name = []
        for i in range(len(line.split(' '))):
            try:
                int(line.split(' ')[i])
                start_point = i
                break
            except:
                name.append(line.split(' ')[i])
        name = ' '.join(name)
        count = int(line.split()[start_point])
        price = float(line.split()[start_point + 1])
        if name in product:
            product[name]['name'] += name
            product[name]['price'] += price * count
        else:
            product[name] = {'name': name, 'price': price * count}

product = sorted(product.values(), key=lambda x: x['price'], reverse=True)
out_file_path = os.path.expanduser(f'{HOME_DIR}/{OUT_FILE}')
with open(out_file_path, 'w') as file:
    for i in product:
        file.write(f"{i['name']:<20} {round(i['price'], 2)}\n")
