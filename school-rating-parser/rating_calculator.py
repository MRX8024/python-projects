import os
import plotly.graph_objects as go
import plotly.io as pio
HOME_DIR = './'
FILE_PATH = os.path.expanduser(f'{HOME_DIR}/data.txt')

users = {}
tab_len = {}

def average(data):
    num = 0
    for i in data:
        num += i
    return num / len(data)

def median(data):
    data = sorted(data)
    if len(data) % 2 == 0:
        return (data[len(data) // 2 - 1] + data[len(data) // 2]) / 2
    else:
        return data[len(data) // 2]

with open(FILE_PATH, 'r') as file:
    n = int(file.readline())
    for line in file:
        line = line.strip()
        clas = line.split(' ')[0]
        name = []
        for i in range(1, n + 1):
            try:
                int(line.split(' ')[i])
                start_point = i
                break
            except:
                name.append(line.split(' ')[i])
        name = ' '.join(name)
        grades_ct = line.split(' ')[start_point]
        grades = list(map(int, line.split(' ')[start_point + 1:]))
        min_gr, max_gr = min(grades), max(grades)
        avg_gr, md_gr = round(average(grades), 2), round(median(grades), 2)
        users[name] = {'class': clas, 'grades_ct': grades_ct, 'grades': grades,
                       'min_gr': min_gr, 'max_gr': max_gr, 'avg_gr': avg_gr, 'md_gr': md_gr}

types = {'имена':'1', 'классы':'2', 'оценки':'3'}
type = input(f'Выберите тип сортировки: {str(types)} \n')
if type not in types and type not in types.values(): raise exit(1)
print('\n')

if type == 'имена' or type == '1':
    sorted_users = sorted(users)
elif type == 'классы' or type == '2':
    sorted_users = sorted(users.keys(), key=lambda name: users[name]['class'])
elif type == 'оценки' or type == '3':
    sorted_users = reversed(sorted(users.keys(), key=lambda name: users[name]['avg_gr']))
else:
    exit(1)

tab_len['name'] = max(len(name) for name in users)
tab_len['grades_ct'] = max(len(str(user['grades_ct'])) for user in users.values())
tab_len['min_gr'] = max(len(str(user['min_gr'])) for user in users.values())
tab_len['max_gr'] = max(len(str(user['max_gr'])) for user in users.values())
tab_len['avg_gr'] = max(len(str(user['avg_gr'])) for user in users.values())
tab_len['md_gr'] = max(len(str(user['md_gr'])) for user in users.values())

num = 1
colors = ['', '#2F4F4F', '#12B57F', '#9DB512', '#DF8816', '#1297B5', '#5912B5', '#B51284', '#127D0C']
fig = go.Figure()
for param in sorted_users:
    x = users[param]
    print(f"{param:<{tab_len['name']}} | "
          f"Класс: {x['class'].upper()} | "
          f"Колво оценок: {x['grades_ct']:<{tab_len['grades_ct']}} | "
          f"Минимальная: {x['min_gr']:<{tab_len['min_gr']}} | "
          f"Максимальная: {x['max_gr']:<{tab_len['max_gr']}} | "
          f"Средняя: {x['avg_gr']:<{tab_len['avg_gr']}} | "
          f"Медианная: {x['md_gr']:<{tab_len['md_gr']}}")
    num += 1
    fig.add_trace(go.Bar(x=[param + ' | ' + 'Класс: ' + users[param]['class'].upper()],
                         y=[users[param]['avg_gr']], marker_color=colors[num] if num <= 8 else num - 8,
                         orientation='v', showlegend=True))
print('\n')
open = input('Открыть график?')
if open == '' or open == 'y' or open == 'yes':
    fig.update_layout(title='Super puper graph', xaxis_title='Ученики',
                    yaxis_title='Средние оценки', coloraxis_showscale=True)
    plot_html_path = os.path.join(f'{HOME_DIR}/plot.html')
    pio.write_html(fig, plot_html_path, auto_open=True)