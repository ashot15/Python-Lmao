import time
x = int(input("Write Number:\t"))
for i in range(0, 10000000):
    if i * i == x:
        print(round(i))
    else:
        print("Sqr is not exist")
        time.sleep(2)
        exit()
