task_tuple = ['pem', 'paper', 10, False, 2.5]
type(task_tuple)
task_tuple = tuple(task_tuple)
type(task_tuple)
index = task_tuple.index(False)
bool1 = task_tuple[index]
print(bool1)
