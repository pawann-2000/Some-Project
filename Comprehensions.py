some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

some_set = set(some_list)

some_set2 = [dup for dup in some_list if dup.count(some_list) > 1]

print(some_set2)
