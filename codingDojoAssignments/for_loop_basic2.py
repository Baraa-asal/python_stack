# # ######################## 1 Biggie Size:
# # from array import array
# # def change_to_big(array):
# #     for i in range (len(array)):
# #         if array[i]>0:
# #             array[i] = "big"
# #     return array
# # print(change_to_big([1,-1,2,4,-9,-2,2,2,2,2,0]))

# # ######################## 2 Count Positives:

# # def count_positives(list):
# #     count = 0
# #     for i in range (len(list)):
# #         if list[i] > 0:
# #             count += 1
# #     list[len(list)-1] = count
# #     return list
# # print(count_positives([-1,1,1,1,1,0,-1,0]))

# # ######################## 3 Sum Total :

from traceback import print_tb


def sum_total(Arr):
    listSum = 0
    for num in Arr:
        listSum += num
    return listSum
# print(sum_total([1,2,3,4]))

# # ######################## 4 Average :

def avrg(Arr):
    listSum = 0
    avrg = 0
    for num in Arr:

        listSum += num
    avrg = listSum/len(Arr)
    return avrg
# print(avrg([1,2,3,4]))

# # ######################## 5 Length :

def length(list):
    len = 0
    for element in list:
        len += 1
    return len
# print(length([1,2,3,'dog','cat']))

# # ######################## 6 Minimum :

def minimun(myArr):
    minVal = 0
    if len(myArr) == 0:
        return False
    else: 
        for i in range(len(myArr)):
            if myArr[i] < minVal:
                minVal = myArr[i]
    return minVal
# print(minimun([-100,37,-22,1,-44,0]))
# print(minimun([]))

# # ######################## 7 Maximum :

def maximum(myArr):
    maxVal = 0
    if len(myArr) == 0:
        return False
    else: 
        for i in range(len(myArr)):
            if myArr[i] > maxVal:
                maxVal = myArr[i]
    return maxVal
# print(maximum([37,2,1,50,-9,100]))
# print(maximum([]))

# ######################## 8 Ultimate Analysis  :

# def ultimate_analysis(list):
#     new_dictionary = {'sumTotal': sum_total(list),
#                        'average': avrg(list),
#                        'minimun': minimun(list),
#                        'maximum': maximum(list),
#                        'length': length(list)}
#     return new_dictionary
# print(ultimate_analysis([37,2,1,-9]))

# ######################## 9 Reverse List  :

def reverse_list(list):
    temp = 0
    j = len(list)-1
    half_length = int(len(list)/2)
    for i in range(0, half_length, 1):
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
        j-=1
    return list
print(reverse_list([1,2,3,4,5,6,7]))




