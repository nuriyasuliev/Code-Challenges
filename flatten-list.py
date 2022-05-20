def flatten(list_of_lists):
    new_list =[]
    for sub_list in list_of_lists: new_list.extend(sub_list)
    return new_list
print(flatten([[4, 6], [8, 10]]))
print(flatten([[2, 0], [12, 13], [14, 15]]))