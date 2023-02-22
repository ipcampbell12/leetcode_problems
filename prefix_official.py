
input = ["flower", "flow", "flight"]
# Output: "fl"

input2 = ["dog", "racecar", "car"]
# Output: ""

input3 = ["work", 'worker', 'workmanship']
# Output: "work"

input4 = ["cir", "car"]
# Output: "c"


def lowest_commone_prefix(strs):
    if len(strs) == 0:
        return ''

    prefix = strs[0]

    for word in strs:
        while word.index(prefix) != 0:
            prefix = prefix[0:len(prefix)-1]
            if len(prefix) == 0:
                return ''


print(lowest_commone_prefix(input4))


# learnings:
