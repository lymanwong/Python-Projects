# Make a program that filters a list of strings and returns a list with only your friends name in it. All your friends only have four letter in their name.

# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

def friend(x):
  list = []
  for name in x:
    if len(name) == 4:
      list.append(name)
  return list

print friend(["Ryan", "Kieran", "Mark",]) #["Ryan", "Mark"]
