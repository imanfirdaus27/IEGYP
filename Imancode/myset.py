# python set we use {}
# set does not allow duplicates
# set is not ordered
# set is not indexed

myset = {1, 2, 3, 4, 5}
print(myset)
print(type(myset))

# we can also create set using set() function

# set cannot do selection and indexing
# cannot select the item using index
#but we always itertate using for loop
# print(fruits[0])

# for fruit in fruits:
#     print(fruit)

# Modifiable

fruits = ["apple", "rambutan", "orange", "durian", "mango", "papaya", "banana", "grapes"]
fruits = set(fruits)
print(fruits)
fruits.add("kiwi")
print(fruits)

# Update
# fruits[2]

#Drop fruit
# fruit is an object or instance of a set class
# remove is a methof inside the object fruits
fruits.remove("kiwi")

print(fruits)

#pop randomly remove an item
fruits.pop()
print(fruits)

# NLP =  Natural Language Processing
# Use library = NLTK

overseafruits = {"apple", "rambutan", "orange", "durian", "mango", "papaya","banana"}
localfruits =  {"cempedak","mangosteen", " banana"}

print(overseafruits.union(localfruits))

print(overseafruits.intersection(localfruits))

print(overseafruits.difference(localfruits))

print(localfruits.difference(overseafruits))

favouritefruits = {"durian","rambutan","mangosteen"}
print(favouritefruits.issubset(localfruits))
print(localfruits.issuperset(favouritefruits))
print(localfruits.isdisjoint(overseafruits))

content = 

words = content.split()
print(len(words))

uniquewords = set(words)

print(len(uniquewords))

print(uniquewords)

cleanwords = []
for word in words:
    word = word.remove(","," ")
    word = word.replace

