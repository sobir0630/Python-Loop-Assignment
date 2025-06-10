n = int(input("son kritng: "))

for i in range(1, n + 1):
    result = ""
    if i % 3 == 0:
        result += "Fizz"
    elif i % 5 == 0:
        result += "Buzz"

    print(result or i)
