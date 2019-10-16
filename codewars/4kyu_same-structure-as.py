# https://www.codewars.com/kata/520446778469526ec0000001/train/python


def same_structure_as(original, other):
    if isinstance(original, list) and isinstance(other, list):
        if len(original) != len(other):
            return False
        else:
            for elem1, elem2 in zip(original, other):
                if isinstance(elem1, list) and isinstance(elem2, list):
                    if not same_structure_as(elem1, elem2):
                        return False
                elif isinstance(elem1, list) or isinstance(elem2, list):
                    return False

        return True
    elif type(original) != type(other):
        return False
    else:
        return True


# should return True
print(same_structure_as([1, 1, 1], [2, 2, 2]))
print(same_structure_as([1, [1, 1]], [2, [2, 2]]))
#
# # should return False
print(same_structure_as([1, [1, 1]], [[2, 2], 2]))
print(same_structure_as([1, [1, 1]], [[2], 2]))
#
# # should return True
print(same_structure_as([[[], []]], [[[], []]]))
#
# # should return False
print(same_structure_as([[[], []]], [[1, 1]]))
print(same_structure_as(1, []))
print(same_structure_as([1, '[', ']'], ['[', ']', 1]))
