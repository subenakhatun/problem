'''
Write a Python function that takes two lists and returns True if they have
at least one common member.
'''

# def re(list1,list2):
#     result = False;
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 result = True;
#     return result
# print(re([4,5,6,8,9,10,20],[8,2,11,12,15,17]))

A = [[1,2,3],[4,5,6],[7,8,9]]
f = 1
for i in range(0,3):
    f *= 10
    for j in range(0,3):
        A[i][j] *= f
print(A)