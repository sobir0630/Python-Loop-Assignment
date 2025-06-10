user = input("matn kritng: ")
unlilar = ["a", "i", "e", "o", "u"]
katta_harf = 0

for harf in user:
    if harf.isupper():
        katta_harf += 1
print("matn ichida hatta kafr", {katta_harf})