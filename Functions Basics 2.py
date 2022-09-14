#1 CountDown
# def countDown(number):
#     for i in range(number, -1,-1):
#         print(i)

# num = int(input("Please enter a number: "))
# countDown(num)

################################################################################

#2 Print and Return 
# def printAndReturn(numArr):
#     print(numArr[0])
#     return(numArr[1])
# array = [1,3]
# printAndReturn(array)

################################################################################

#3 First Plus Length
# def first_plus_length(numArr):
#     return(numArr[0] + len(numArr))
# x = [1,2,3,4,5]
# print(first_plus_length(x))

################################################################################

#4 Values Greater than Second 
# def values_greater_than_second(list):
#     newlist = []
#     if len(list) < 2:
#         return False
#     for n in list:
#         if n > list[1]:
#             newlist.append(n)
#     print(len(newlist))
#     return newlist
# x = [5,2,3,2,1,4]
# print(values_greater_than_second(x))

################################################################################

#5 This Length, That Value
#solution ONE

# def length_and_value(size, value):
#     array = []
#     for i in range(0, size):    
#         array.append(value)
#     return array
# print(length_and_value(4,7))

#5 This Length, That Value
#solution TWO (SHORTHAND):

# def length_and_value2(size, value):
#     array = [value] * size   
#     return array
# print(length_and_value2(4,7))