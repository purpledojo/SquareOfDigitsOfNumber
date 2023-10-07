# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
num = input("Give number")
if int(num) <= 0:
    print("Error")
else:
    a = []
    while int(num):
        ans1 = int(num) % 10
        ans = int(ans1) * int(ans1)
        a.append(ans)
        num = int(num) // 10
    w = sum(a)
    print (w)