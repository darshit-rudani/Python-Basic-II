some_list = ['a','a','b','c','d','h']

duplicate = []

for i in some_list:

	if(i not in duplicate):
		duplicate.append(i)

print(duplicate)



for value in some_list:

    if some_list.count(value) > 1:

        if value not in duplicate:

            duplicate.append(value)

print(duplicate)
