print("FOR em ordem crescente")
for andar in range(1, 21, 1):
    if andar == 13:
        continue
    print(andar)

andar = 1
print("WHILE em ordem crescente")
while andar <= 20:
    if andar != 13:
        print(andar)
    andar += 1

print("FOR em ordem decrescente")
for andar in range(20, 0, -1):
    if andar == 13:
        continue
    print(andar)

andar = 20
print("WHILE em ordem decrescente")
while andar > 0:
    if andar != 13:
        print(andar)
    andar -= 1