#for loop

for item in (1,2,3,4,5):
  print(item)
  print(item)
print(item)

for item in (1,2,3,4,5):
  for x in ['a','b','c','d','e']:
    print(item,x)
print('')


#iterables


user = {

  'name': 'darshit',
  'age': 20,
  'borth plase' : 'surat'
}

for item in user.items():
  print(item)
print('')

for item in user.values():
  print(item)
print('')

for item in user.keys():
  print(item)
print('')
