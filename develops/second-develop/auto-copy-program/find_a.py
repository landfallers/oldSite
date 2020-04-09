import random
print(random.seed(10))
print(random.seed())
from jinja2 import Template, Environment, FileSystemLoader
import csv
with open("Book1.csv", encoding="utf-8") as f:
    table = list(csv.reader(f))
del table[0]

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('find_a.html.j2')
rendered = []
for i in range(126):
    row = table[i]
    data = {
        "url": "https://landfaller.com/pdf/" + row[4] + "/" + row[3],
        "title": row[1],
        "name": row[2],
    }
    rendered.append(template.render(data))
print(rendered)
with open("find_a.html",  'w', encoding="utf-8") as f:
    for i in range(126):
        f.write(rendered[i])
