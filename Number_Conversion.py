def print_formatted(number):
    # # your code goes here decimal octal hex binary
    # for i in range(n):
    #     print(i," ",oct(i)," ",hex(i)," ",bin(i))
    w = len(str(bin(number)).replace('0b',''))

    for num in range(1, number+1):

        dec = str(num)
        oc_ = str(oct(num)).replace('0o','')
        he_ = str(hex(num)).replace('0x','')
        bi_ = str(bin(num)).replace('0b','')

        print(dec.rjust(w), oc_.rjust(w), he_.upper().rjust(w), bi_.rjust(w), sep=' ')
        # print("{} {} {} {}")

    # x = "String_Prince"
    # print(x.replace('_',' + '))
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)