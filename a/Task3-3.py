# 任务 3-4
score = {'Math' : 96, 'English' : 86, 'Chinese' : 95.5, 'Biology' : 86, 'Physics' : None}

score['History'] = 88 # 添加新的键值对
del score['History'] # 删除制定的键值对
new_value = round(score['Chinese'])
score['Chinese'] = new_value # 四舍五入分数并重新赋值
print(score['Math'])
print(score)
