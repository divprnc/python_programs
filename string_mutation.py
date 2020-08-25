def mutate_string(string, position, character):
    lst = []
    for i in string:
        lst.append(i)
    lst[position] = character

    return "".join(lst)


if __name__ == '__main__':
    print(mutate_string(input(),int(input()),input()))