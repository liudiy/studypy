monster_speed = 2
people_speed = 3
distance = 100
time = distance/(monster_speed + people_speed )
print(time)

with open('d:/gui-config.json') as file_object:
    contents = file_object.read()
    print( contents)

    zhangsan_name = 'zhangsan'
    zhangsan_sheming = 1000

with open('d:/gui-config.json','a') as file_object:
    file_object.write('\n')
    file_object.write(zhangsan_name)
    file_object.write('\n')
    file_object.write(str(zhangsan_sheming) )