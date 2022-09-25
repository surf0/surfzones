from ck_maptier import ck_maptier
# read css maps
cssmaps = []
with open('cssmaps.txt') as f:
    for line in f:
        cssmaps.append(line.replace('\n', ''))

mapnamelist = [i[0] for i in ck_maptier]
maps = list(set(cssmaps) & set(mapnamelist))
notcommon = [value for value in cssmaps if value not in mapnamelist]

print(len(maps))

# maptiers


def add_maptiers():
    maptiers = 'INSERT INTO `maptiers` VALUES '

    for m in maps:
        item = [value for value in ck_maptier if m in value][0]
        maptiers += (f"('{item[0]}', {item[1]}),")

    maptiers = maptiers[:-1]+';'

    with open('bhoptimer/maptiers.sql', 'w') as f:
        f.write(maptiers)
# add_maptiers()

# zones
