for num in range (0, 101):
    if num <= 1:
        continue
    if num <= 3:
        print (num, end=" ")
    if num % 2 == 0 or num % 3 == 0:
        continue
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            break
        i += 6
    else:
        print (num, end=" ")
