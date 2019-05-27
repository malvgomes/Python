def tower_builder(n_floors):
    tower = []
    imp = 1
    for i in range(n_floors):
        tower.append(imp * "*")
        imp += 2
    return tower


def tower_addspaces(tower):
    i = len(tower) - 1
    for x in range(i, -1, -1):
        tower[i - x] = x*" " + tower[i - x] + x*" "
    return tower


print(tower_addspaces(tower_builder(2)))
