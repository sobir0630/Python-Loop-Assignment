parol = "1234"
count = 3

for i in range(count):
    user = input("parolni kritng: ")
    if user == parol:
        print("tugri")
        break
    else:
        print("xato! qayta urining")
    if i == count - 1: 
        print("biloklandiz")
        break