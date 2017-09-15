# I originally misunderstood the question

# def firstDuplicate(a):
#     if (len(a) == 0):
#         return -1
#     else:
#         k = a[0]
#         for i in range(1, len(a)):
#             if (k == a[i]):
#                 a.pop(0)
#                 if (secondDuplicate(a) != -1):
#                     return secondDuplicate(a)
#                 else:
#                     return k
#         a.pop(0)
#         return (firstDuplicate(a))
#
# def secondDuplicate(a):
#     if (len(a) == 0):
#         return -1
#     else:
#         k = a[0]
#         for i in range(1, len(a)):
#             if (k == a[i]):
#                 return k
#         a.pop(0)
#         return (secondDuplicate(a))

def firstDuplicate(a): 
    d = {}
    for i in a:
       if i in d:
           return i
       else:
           d[i] = 1
    return -1
