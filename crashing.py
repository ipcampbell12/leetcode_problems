

a = [[1, 2, 6],
     [2, 3, 1],
     [3, 4, 2]]

# this is a way to switch the arrays
li = [list(i) for i in zip(*a)]

print(li)
# def crashing_weights(weights):

#     new_arr = []

#     # this is the same as what li is above
#     for index, arr in enumerate(weights):
#         new_arr.append([arr[index] for arr in weights])

#     return new_arr


# print(li)


def crashing_weights(weights):
    lst = [0] * len(weights[0])
    for line in weights:
        lst = [b if a <= b else a+b for a, b in zip(lst, line)]
        print(list(zip(lst, line)))
    return lst


# print(crashing_weights(a))
