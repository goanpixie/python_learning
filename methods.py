# language list
language = ['French']

# language tuple
language_tuple = ('Spanish', 'Portuguese')

# language set
language_set = {'Chinese', 'Japanese'}

language.extend(language_set)
#print(language)

language.append(language_set)
#print(language)

#index:
# vowels list
# vowels = ['a', 'e', 'i', 'o', 'i', 'u']
# index = vowels.index('e')
#print('index of e', index )

#insert:
#list.insert(i, elem)
# vowel list
# vowel = ['a', 'e', 'i', 'u']
# vowel.insert(3, 'o')
#print(vowel)

#remove:
# animals list
animals = ['cat', 'dog', 'rabbit', 'guinea pig']
#deleting rabbit:
animals.remove('rabbit')
#print("animals",animals)

#count()

#pop()
# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
return_value = languages.pop(3)
#print('Return Value:', return_value)

#reverse()

#sort() and #sorted()

#list.sort(key=..., reverse=...), does not return anything , mutates original array, can be used with any parameters
#list.sorted(list, key=..., reverse=...), does not mutate original array, return new list
# vowels list
vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort()
print(vowels)

#sort in descending order
# vowels.sort(reverse=True)
descendingSorted = sorted(vowels, reverse=True)
print(descendingSorted, vowels)

#optional key parameter taking a fnx:
list = ["pri", "priyanka","priya"]
list.sort(key=len)
print("sorted by len", list)

# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

def get_name(employees):
  return employees.get('Name')

employees.sort(key=get_name)
print(employees, end='\n\n')

#one line fnx can be written as lambda
employees.sort(key = lambda x:x.get('salary'), reverse=True)
print(employees)

#copy():
#copies the original list to new list without modifying original list
# mixed list
my_list = ['cat', 0, 6.7]

# copying a list
new_list = my_list.copy()
print("copied list", new_list)

#copying using slicing:
list = [1,2,3]
new_list = list[:]
print(new_list)

#clear():empties list
list1 = [1, 2, 3]
list.clear()
print(list)
list2 = [1, 2]
del list2[:]
print(list2)












