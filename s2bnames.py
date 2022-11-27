
extensions = ['_csgo', '_go', '_njv', '_fix',
              '_kzg', '_sns', '_ksf', '_refix', '_fixed', '_final', '_nsf', '_rg', '_e', '_GO', '_official', '_nsf_v2', '_v2', '_rat']
removes = ['_ksf', '_fix', '_njv', '_refix',
           '_source', '_fixed', '_final', '_v1', '_beta1']

replaces = {'2': '_v2'}

# ksf to csgo
renames = {'surf_halloween_tf2': 'surf_halloween_tf',
           'surf_water_run_ksf': 'surf_water-run_banjo_skill', 'surf_blackout': 'surf_blackout_v1', 'surf_bluewall_v2': 'surf_bluewall', 'surf_marbleblast_intermediate': 'surf_marbleblast_e', 'surf_network_2008final': 'surf_network_2008_final', 'surf_theunexpected': 'surf_the_unexpected'}


renamemaps = []
with open('renamedmaps.txt') as f:
    for line in f:
        renamemaps.append(line.replace('\n', ''))


csgomaps = []
with open('csgomaps.txt') as f:
    for line in f:
        csgomaps.append(line.replace('\n', ''))


newnames = {}
i = 0
for map in renamemaps:
    if map in renames:
        newnames[map] = renames[map]
        continue
    for key, value in replaces.items():
        map2 = map.replace(key, value)
        if map2 in csgomaps:
            newnames[map] = map2
            break
    else:
        for add in extensions:
            map2 = map + add

            if map2 in csgomaps:
                newnames[map] = map2
                break
        else:
            for remove in removes:
                map2 = map.replace(remove, '')
                if map2 in csgomaps:
                    newnames[map] = map2
                    break
                for add in extensions:
                    map3 = map2 + add
                    if map3 in csgomaps:
                        newnames[map] = map3
                        break

            else:
                if map not in newnames:
                    i += 1
                    # print(map)

print(len(newnames))
print(i)
