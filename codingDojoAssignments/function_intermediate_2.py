#  O  N  E  ######################################################################
x = [ [5,2,3], [10,8,9] ]                     # list of lists
students = [                                  #a list that contains dictionary
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {                          #this is a dictionary that has keys inside it, containing lists
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]                    #a list of one dictionary

# #1
# x[1][0] = 15
# print(x)

# #2 
# students[0]['last_name'] = "Bryant"
# print(students[0])

# #3
# sports_directory['soccer'][0] = "Andres"
# print(sports_directory)

# #4
# z[0]['y'] = 30
# print(z)

# T  W  O  #####################################################################

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'x' : 'John', 'last_name' : 'Rosales'},
         {'z' : 'Mark', 'last_name' : 'Guillen'},
         {'m' : 'KB', 'last_name' : 'Tonel'}
    ]

# def iterateDictionary(students):
#     for i in range(len(students)):
#         print("first_name " + "- " + students[i]['first_name'] + ", " + ("last_name " + "- " + students[i]['last_name']))
# iterateDictionary(students) 

# def iterateDictionary2(key_name, some_list):
#     for i in range(len(students)):
#         print(some_list[i][key_name])

# iterateDictionary2('first_name', students)
# iterateDictionary2('last_name', students)

for i in range(len(students)):
    # print (key, value[key])
    sentence = ""
    for key, val in students[i].items():
        sentence += key + ' - ' + val +", "
    print(sentence)



# T  H  R  E  E  #####################################################################

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    for key in dojo:
        print(len(dojo[key]), key,'\n')   #we can access the value using the key
        for person in dojo[key]:
            print(person)

printInfo(dojo)
