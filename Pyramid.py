a = int(input("N = "))
char = ord("a")
for i in range (1,a+1):
    for j in range (i):
        if char%2!=0:
            print(chr(char).upper(), end=" ")
        else:
            print(chr(char), end=" ")
        char += 1
    print()

