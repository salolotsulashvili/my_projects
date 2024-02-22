import random
gamosacnobi_ricxvi = random.randint(1, 10)
cdebis_raodenoba = 0

while True:
            cdebis_raodenoba += 1
            print()
            user_guess = int(input("sheiyvanet ricxvi 1-dan 10-mde: "))
            
            if user_guess == gamosacnobi_ricxvi:
                    print(f"TQVEN GAMOICANIT! gamosacnobi ricxvi iko: {gamosacnobi_ricxvi}")
                    break
            elif user_guess > gamosacnobi_ricxvi:
                    print("gamosacnobi ricxvi ufro naklebia, sheiyvanet xelaxla.")
            else:
                    print("gamosacnobi ricxvi ufro metia, sheiyvanet xelaxla.")
            print()
            
print("\nTamashi dasrulebulia!")
print(f"cdebis raodenoba = {cdebis_raodenoba}")

