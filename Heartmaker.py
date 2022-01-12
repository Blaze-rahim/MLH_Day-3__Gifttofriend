import time

while True:
    a = int(input("Enter Your number between 6 - 20 : "))
    n = a // 2
    name = input("Enter the name 1 - 7 chars: ")
    b = len(name)
    spc = ""
    for i in range(b):
        spc += " "

    for i in range(n):
        for j in range(n - i - 1):
            print(spc, end="")
        for j in range(i + 1):
            print(name + spc, end="")
            time.sleep(.02)
        if a % 2 == 0:
            for j in range(2 * (n - i - 1)):
                print(spc, end="")
        else:
            for j in range(2 * (n - i - 1) + 1):
                print(spc, end="")

        for j in range(i + 1):
            print(name + spc, end="")
            time.sleep(0.02)

        print()
    for i in range(a, 0, -1):
        for j in range(a - i):
            print(spc, end="")
        for j in range(i, 0, -1):
            print(name + spc, end="")
            time.sleep(.25)

        print()
    ver = input("do you wanna continue, y/n").lower()
    if ver == "n":
        break
    elif ver == "y":
        continue
    else:
        print("Its neither y or n sorry we breaking")
        break

for i in range(5, -1, -1):
    print(f"Closing in {i}")
    time.sleep(0.5)

