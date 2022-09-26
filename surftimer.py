from ck_newmaps import ck_newmaps
from faker import Faker

fake = Faker()

maps = []
with open('csgomaps.txt') as f:
    for line in f:
        maps.append(line.replace('\n', ''))

newmaps = [i[0] for i in ck_newmaps]

command = 'INSERT INTO `ck_newmaps` VALUES '

for m in maps:
    if m not in newmaps:
        date = fake.date_time_between(start_date='-30d', end_date='now')

        dt_str = date.strftime("%Y-%m-%d %H:%M:%S")
        command += f"('{m}','{dt_str}'),"

command = command[:-1]+';'
with open('surftimer/ck_newmaps.sql', 'w') as f:
    f.write(command)
