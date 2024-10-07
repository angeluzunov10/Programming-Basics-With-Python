balance = 0
command = input()

while command != "NoMoreMoney":
    deposit = float(command)

    if deposit < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {deposit:.2f}")
    balance += deposit
    command = input()

print(f"Total: {balance:.2f}")
