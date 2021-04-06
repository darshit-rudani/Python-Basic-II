# if else

is_old = False
is_licenced = True

if is_old:
  print("you are not eligible for driving")

elif is_licenced:
  print("your age is enough to drive")

else:
  print("chack your code")

#2nd type trully and fallsy


is_old = bool(5)
is_licenced = bool('hello')

print(bool(5))

print(bool(5))

if is_old and is_licenced:
  print("your age is enough to drive")


else:
  print("chack your code")

#3 type ternary operator

is_friend = True

can_massage = "allowed " if is_friend else "not allowed"

print(can_massage)

#4 and or operator

friend = True
user = False

if friend or user:
  print('we are est friend')
