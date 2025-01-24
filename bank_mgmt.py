bank = []

demo_data = [
        {"id": 1, "name": "Alice", "balance": 500},
        {"id": 2, "name": "Bob", "balance": 1500},
        {"id": 3, "name": "Charlie", "balance": 250},
        {"id": 4, "name": "Diana", "balance": 800},
        {"id": 5, "name": "Eve", "balance": 1000},
]

bank.extend(demo_data)

def gen_id():
    return len(bank)+1

def create_acc():
    print("---- CREATE ACCOUNT ----")
    name = input("Enter your name: ")
    balance = input("Enter initial deposit (minimum $50): ")
    ids= gen_id()
    bank_data = {
        "id":ids,
        "name":name,
        "balance":balance,
    }
    bank.append(bank_data)
    print(f"Account created successfully! Your account number is: {ids}")

def chk_balance():
    print("---- CHECK BALANCE ----")
    acc_num = int(input("Enter your account number: "))
    for i in bank:
        if acc_num == i['id']:
            print(f"Account Holder: {i['name']}, Balance: ${i['balance']}")

def deposit():
    print("---- DEPOSIT MONEY ----")
    acc_num = int(input("Enter your account number: "))
    for i in bank:
        if acc_num == i['id']:
            balance_amt = int(input("Enter amount to deposit: "))
            i['balance'] += balance_amt
            print(f"Deposit successful! New balance: ${i['balance']}")

def withdraw():
    print("---- WITHDRAW MONEY ----")
    acc_num = int(input("Enter your account number: "))
    for i in bank:
        if acc_num == i['id']:
            balance_amt = int(input("Enter amount to deposit: "))
            i['balance'] -= balance_amt
            print(f"Withdraw successful! New balance: ${i['balance']}")

def view_bank():
    for i in bank:
        print(i)
        
def view_account_balance(acc):
    for i in bank:
        if acc == i["id"]:
            print(f"Account Holder: {i['name']}, Balance: ${i['balance']}")

def transfer_amt():
    print("---- TRANSFER AMOUNT ----")
    sender = int(input("Enter sender account number: "))
    receiver = int(input("Enter receiver account number: "))
    amt = int(input("Enter amount to send: "))
    print("Current Balance")
    view_account_balance(sender)
    print("Initiating Transaction")
    for i in bank:
        if sender == i['id']:
            i["balance"] -=amt
        if receiver == i['id']:
            i["balance"] +=amt
    print("Transaction Successful")
    print("Current Balance")
    view_account_balance(sender)

def main_menu():
    while True:
        print("===== Simple Banking System =====")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_acc()
        elif choice == "2":
            chk_balance()
        elif choice == "3":
            deposit()
        elif choice == "4":
            withdraw()
        elif choice == "5":
            transfer_amt()
        elif choice == "6":
            print("GoodBye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
