# t = ("TestingAcademiy", "for", "TestingAcademiy)
#     print(set(t))


# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# new_set = set1.union(set2)
# print(new_set)


set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
my_set = set1.intersection(set2)    # gives common values out of both set
print(my_set)


# my_set = set1.difference(set2)
my_set = set2.difference(set1)
print(my_set)


