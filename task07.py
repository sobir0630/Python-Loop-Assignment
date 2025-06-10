katta_son = None

for i in range(5):
    son = int(input(f"{i+1}- sonni kritng: "))
    if katta_son is None or son > katta_son:
        katta_son = son
    print("hozirgi katta son", katta_son)