def long_repeat(line):
    count = 1
    result = []
    if len(line) > 2:
        for k in range(len(line) - 1):
            if line[k] == line[k + 1]:
                count += 1
            else:
                result.append(count)
                count = 1
        return max(result)
    elif len(line) == 2 and line[0] == line[1]:
        return 2
    elif len(line) == 1:
        return 1
    else:
        return 0


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')