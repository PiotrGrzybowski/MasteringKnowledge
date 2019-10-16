# https://www.codewars.com/kata/strip-comments/solutions/python


def solution(string, markers):
    lines = string.split('\n')
    result = []
    for line in lines:
        for marker in markers:
            line = line.split(marker)[0]
        result.append(line.strip())
    return '\n'.join(result)
