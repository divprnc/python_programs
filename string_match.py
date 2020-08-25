def count_substring(string, sub_string):
    sub = len(sub_string)
    stri = len(string)
    count = 0

    # for i in range(stri - sub + 1):
    #     j=0
    #     for j in range(sub):
    #         if (string[i+j] != sub_string[j]):
    #             break

    #     if (j==sub-1):
    #         count+=1
    #         j=0
    # return count
    # return string.count(sub_string)
    for i in range(stri):
        if (string[i:i + sub] == sub_string):
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)