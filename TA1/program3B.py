#Program 3B
i = 1
while i <= 7:
    if i % 2 != 0:
        j = 1
        while j <= i:
            print(i, end="")
            j += 1
        print("")
    i += 1