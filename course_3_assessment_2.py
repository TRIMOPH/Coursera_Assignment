# Write code to assign to the variable map_testing all the elements in lst_check while adding the string “Fruit: ” to the beginning of each element using mapping.

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']
map_testing = map(lambda str: "Fruit: " + str, lst_check)
print(map_testing)

# Below, we have provided a list of strings called countries. Use filter to produce a list called b_countries that only contains the 
#strings from countries that begin with B.
countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
b_countries=filter(lambda word: 'B' in word, countries)
print(b_countries)

# Below, we have provided a list of tuples that contain the names of Game of Thrones characters. Using list comprehension, 
#create a list of strings called first_names that contains only the first names of everyone in the original list.
# Methon1
people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
def name(st):
    return st[1]
first_names=map(name,people)
print(first_names)

#Method2 by list coprehension
people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
first_names=[st[1] for st in people]
print(list(first_names))

# Use list comprehension to create a list called lst2 that doubles each element in the list, lst.
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
lst2 =[i*2 for i in lst]
print(lst2)

# Below, we have provided a list of tuples that contain students’ names and their final grades in PYTHON 101. Using list comprehension, 
#create a new list passed that contains the names of students who passed the class (had a final grade of 70 or greater).
# my using for loop method1

students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]
passed=[]
for st in students:
    if st[1]>=70:
        passed.append(st[0])
print(passed)

# method2
students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]
passed=[st[0] for st in students if st[1]>=70]
print(passed)

# Write code using zip and filter so that these lists (l1 and l2) are combined into one big list and assigned to the 
#variable opposites if they are both longer than 3 characters each.

# method 1 unsing for loop
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
def length(str):
    length3=[]
    for st in str:
        if len(st[:][:])>3:
            length3.append(st)
    return length3
x=tuple(length(l1))
y=tuple(length(l2))
opposites= zip(x,y)
print(opposites)

#method 2 using zip and filter

l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
l3=zip(l1,l2)
print(l3)
opposites=list(filter(lambda st: len(st[0])>3 and len(st[1])>3,l3))
print(opposites)

# Below, we have provided a species list and a population list. Use zip to combine these lists into one list of tuples called pop_info. 
#From this list, create a new list called endangered that contains the names of species whose populations are below 2500.

species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']
population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]
pop_info=list(zip(species,population))
print(pop_info)
endangered = [x1 for (x1, x2) in pop_info if x2<2500]
print(endangered)
