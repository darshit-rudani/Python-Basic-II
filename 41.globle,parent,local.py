a = 5

#local scop

def local():
	a = 10
	return a

print(local())
print(a)

# parent scop

def parent():
	a = 20
	def scop():
	  return a
	return scop()

print(parent())
print(a)

# globle scop

print(a)






