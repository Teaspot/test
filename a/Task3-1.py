list = [110, "dog", "cat", 120, "apple"]
list.insert(3, [])
list.remove("apple")
list.index("dog")
list_index = list.index(110)
list[list_index] *= 10

print(list)
