# simple while and for

my_list = [1,2,3]
for item in my_list:
	print(item)

	
		
i=0
while i < len(my_list):
	print(my_list[i])
	i = i + 1

print("  ")
# break statment

my_list = [1,2,3]
for item in my_list:
	print(item)
	break
	
		
i=0
while i < len(my_list):
	print(my_list[i])
	i = i + 1
	break

print("  ")

#continue

my_list = [1,2,3]
for item in my_list:
	continue
	print(item)
	
		
i=0
while i < len(my_list):
	i = i + 1
	continue
	print(my_list[i])


print("  ")

#pass

my_list = [1,2,3]
for item in my_list:
	print(item)
	pass
	
		
i=0
while i < len(my_list):
	print(my_list[i])
	i = i + 1
	pass

     
