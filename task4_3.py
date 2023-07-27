"""
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
✔ Любое действие выводит сумму денег
- Разбейте её на отдельные операции — функции.
- Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""


def atm():
    balance = 0
    transactions = []  # список для хранения операций
    count = 0  # счётчик операций

    while True:
        print(f"Ваш баланс: {balance} у.е.")
        action = input("Выберите действие (пополнить, снять, выйти): ")

        if action == "пополнить":
            amount = int(input("Введите сумму (кратную 50): "))
            if amount % 50 != 0:
                print("Сумма должна быть кратна 50")
                continue
            balance += amount
            transactions.append(f"Пополнение на {amount} у.е.")
            count += 1
            if count % 3 == 0:
                bonus = int(balance * 0.03)
                balance += bonus
                transactions.append(f"Начисление бонуса: {bonus} у.е.")

        elif action == "снять":
            amount = int(input("Введите сумму (кратную 50): "))
            if amount % 50 != 0:
                print("Сумма должна быть кратна 50")
                continue
            if amount > balance:
                print("Недостаточно средств")
                continue
            tax = 0
            if balance >= 5000000:
                tax = int(amount * 0.1)
                balance -= tax
                transactions.append(f"Вычет налога на богатство: {tax} у.е.")
            pay = max(int(amount * 0.015), 30)
            pay = min(pay, 600)
            balance -= (amount + pay)
            transactions.append(f"Снятие: {amount} у.е., комиссия: {pay} у.е.")
            count += 1
            if count % 3 == 0:
                bonus = int(balance * 0.03)
                balance += bonus
                transactions.append(f"Начисление бонуса: {bonus} у.е.")

        elif action == "выйти":
            print("Ждём Вас снова!")
            break

        else:
            print("Некорректное действие")

    print("Операции:")
    for t in transactions:
        print(t)


atm()
