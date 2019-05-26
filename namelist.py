def namelist(names):
    newnames = []
    for name in names:
        newnames.append(name['name'])

    if not newnames[:-2]:
        return ' & '.join(newnames)
    elif not newnames [-2:]:
        return ', '.join(newnames)
    else:
        return ', '.join(newnames[:-2]) + ', ' + ' & '.join(newnames[-2:])

print(namelist([{'name': 'Matheus'}]))
print(namelist([{'name': 'Matheus'}, {'name': 'Alves'}, {'name': 'Gomes'}]))
print(namelist([{'name': 'Matheus'}, {'name': 'Alves'}]))
