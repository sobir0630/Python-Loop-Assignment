import random

pin_kod = random.randint(1000, 9999)
urinishlar = 7
urinish = 0

while urinish < urinishlar:
    taxmin = input(f"{urinish + 1}- kodni kritng: ")

    if not taxmin.isdigit() or len(taxmin) != 4:
        print("faqat raqam kritng")
        continue

    taxmin = int(taxmin)
    urinish += 1

    if taxmin == pin_kod:
        print(f"tabriklaymiz {pin_kod} ni siz topdingiz ")
        break
    
    elif taxmin < pin_kod:
        print("juda kichchik son")

    else:
        print("katta son")

    print(f"qolgan urinishlar {urinishlar - urinish}")

else:
    print(f"afsuski Urinishlar tugdi, pin kod {pin_kod}")

