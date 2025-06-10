user = input("matn kritng: ")
unlilar = ["a", "i", "e", "o", "u"]
counter = 0

for harf in user:
    if harf in unlilar:
        counter += 1
print("matn ichida unlilar", {counter})