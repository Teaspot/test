sort_list = [1, 8, 2, 6, 3, 9, 4, 12, 0, 56, 45]

#TODO Sorting
for i in range(len(sort_list)):
    for j in range(len(sort_list)):
        if(sort_list[i] > sort_list[j]):
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]

print(sort_list)
