import os

HOME_DIR = './'
IN_FILE = 'data.txt'
OUT_FILE = 'out.txt'

product = {}
in_file_path = os.path.expanduser(f'{HOME_DIR}/{IN_FILE}')
with open(in_file_path, 'r') as file:
    n = int(file.readline())
    for line in file:
        name = []
        line = line.strip()
        print(line)
        # print(line.split(' '))
        for i in range(len(line.split(' '))):
            try:
                # print(line.split(' ')[i])
                int(line.split(' ')[i])
                start_point = i
                break
            except:
                # print(i)
                name.append(line.split(' ')[i])
        name = ' '.join(name)
        # print(start_point)
        count = line.split()[start_point]
        price = line.split()[start_point + 1]
        if name in product.keys():
            product[name]['name'] = product[name]['name'] + name
            product[name]['count'] = product[name]['count'] + count
            product[name]['price'] = product[name]['price'] + price
        else:
            product[name] = {'name': name, 'count': count, 'price':price}

for i in product:
    print(name, count, price)

    