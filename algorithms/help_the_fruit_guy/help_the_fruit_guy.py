# Our fruit guy has a bag of fruits (array of strings) where some fruits are rotten, he wants to replace all the rotten fruits by good ones. For example, given this array ["apple","rottenbanana","apple"] the replaced array should be ["apple","banana","apple"]. Your task is to implement a method that will take as an argument an array of strings containing fruits and should return an array of strings where all the rotten fruits are replaced by good ones.

# Note: if the array is null or empty you should return empty array ([]). the rotten fruit name will be in this format rottenFruitname where is the 1st letter of the fruit name is uppercase. NB: The returned array should be in LOWER case.

def removeRotten(bagOfFruits):
  goodfruits=[]
  for fruit in bagOfFruits:
      if len(bagOfFruits) == 0:
          return goodfruits
      elif fruit[0:6] == 'rotten':
         goodfruits.append(fruit[6:].lower())
      else:
          goodfruits.append(fruit.lower())
  return goodfruits


print removeRotten(["rottenApple","rottenBanana","rottenApple","rottenPineapple","rottenKiwi"]) #["apple","banana","apple","pineapple","kiwi"])
print removeRotten([]), #[]
print removeRotten(["Apple","banana","rottenApple","rottenPineapple","rottenKiwi"]), ["apple","banana","apple","pineapple","kiwi"])
