# amount_due=50

# while amount_due>0:
#     print("Amount Due: ", amount_due)

#     coint=int(input("Insert Coin: "))

#     if coint in [25,10,5]:
#         amount_due-=coint

# change_owed=abs(amount_due)
# print("Change Owed: ", change_owed)

amount_due = 50
coins = [5, 10, 25]

while amount_due > 0:
    print(f"Amount Due: {amount_due}")

    coin = int(input("Insert Coin: "))

    if coin in coins:
        amount_due -= coin

print(f"Change Owed: {abs(amount_due)}")
