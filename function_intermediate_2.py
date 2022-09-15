#  O  N  E  ######################################################################
# x = [ [5,2,3], [10,8,9] ]                     # list of lists
# students = [                                  #a list that contains dictionary
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# sports_directory = {                          #this is a dictionary that has keys inside it, containing lists
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]                    #a list of one dictionary

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
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
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

for key, value in students:
    print (key, value)


# T  H  R  E  E  #####################################################################

# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# def printInfo(dojo):
#     for person in dojo:
#         print(len(dojo[person]), person,'\n')
#         for x in dojo[person]:
#             print(x)

# printInfo(dojo)
