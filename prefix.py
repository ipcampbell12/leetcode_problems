# 1. The problem is asking me to find the logest prefix that is shared by all the strings in an array

# 2.Input/ouput:
# strs = ["flower","flow","flight"]
# Output: "fl"
# the return value will be the prefix string shared by all the stirngs in the array


# 3 Contraints:
# Array and strings in array will will have length of less thant 200
# all letters will be lower case

# 4. Edge Cases:
# no common prefix returns an empty string

input = ["flower", "flow", "flight"]
# Output: "fl"

input2 = ["dog", "racecar", "car"]
# Output: ""

input3 = ["work", 'worker', 'workmanship']
# Output: "work"

input4 = ["cir", "car"]
# Output: "c"


def lowest_commone_prefix(arr):

    hm = {}

    prefix_count = 0

    for key in range(min(len(word) for word in arr)):
        hm[key] = [word[key] for word in arr]
        if len(set(hm[key])) == 1:
            prefix_count += 1
        else:
            break

    return arr[0][0:prefix_count]


print(lowest_commone_prefix(input4))
