def to_binary(num):
    bin_num = ""

    while num > 0:
        bin_num += str(num % 2)
        num //= 2
    return bin_num

print(to_binary(45))


