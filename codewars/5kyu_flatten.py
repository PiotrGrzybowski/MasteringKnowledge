# https://www.codewars.com/kata/513fa1d75e4297ba38000003


def flatten(*args):
    result = []

    for elem in args:
        if isinstance(elem, list):
            for r in flatten(*elem):
                result.append(r)
        else:
            result.append(elem)
    return result


print(flatten(1, 2, [3]))
print(flatten(['hello', 2, ['text', [4, 5]]], [[]], '[list]'))
