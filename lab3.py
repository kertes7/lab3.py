import random

digits = list("0123456789")
random.shuffle(digits)
secret_code = digits[:4]
print("Гра 'Таємний код'. Вгадайте 4-значне число з унікальними цифрами.")

attempts = 0
while True:
    guess = input("Введіть вашу спробу: ")
    
    if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
        print("Некоректне введення. Введіть 4 різні цифри.")
        continue

    attempts += 1
    bulls = 0
    cows = 0

    for i in range(4):
        if guess[i] == secret_code[i]:
            bulls += 1
        elif guess[i] in secret_code:
            cows += 1

    print(f"Бики: {bulls}, Корови: {cows}")

    if bulls == 4:
        print(f"Ви вгадали код {''.join(secret_code)} за {attempts} спроб!")
        break
