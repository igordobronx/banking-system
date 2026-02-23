import json

from account import Account
from checking_account import CheckingAccount
from saving_account import SavingsAccount

class Bank:
    """Gerencia todas as contas do banco"""
    
    def __init__(self, name, persistence_file="accounts.json"):
        self._name = name
        self._accounts = []
        self._persistence_file = persistence_file
        # try to load existing accounts from disk
        self.load_accounts(persistence_file)
    
    def create_account(self, holder_name, account_type, initial_deposit=0):
        account_number = len(self._accounts) + 1000

        if account_type == "checking":
            new_account = CheckingAccount(account_number, holder_name, initial_deposit)
        elif account_type == "saving":
            new_account = SavingsAccount(account_number, holder_name, initial_deposit)
        else:
            print("invalid account type, try again")
            return None
        
        self._accounts.append(new_account)
        print(f"\n Account created succesfully, Your account number is {account_number}\n")
        return account_number
    
    def find_account(self, account_number):
        
        for account in self._accounts:
            if account.get_account_number() == account_number:
                return account
    
    def delete_account(self, account_number):
        account_to_delete = self.find_account(account_number)

        if account_to_delete:
            if account_to_delete.get_balance() == 0:
                self._accounts.remove(account_to_delete)
                print(f"\naccount {account_to_delete} removed succesfully.\n")
            else:
                print(f"\nthis account have a balance of {account_to_delete.get_balance()}")
                print("make sure the account have 0 balance.\n")
        else:
            print("account not found.\n")
        
    
    def transfer(self, from_account_number, to_account_number, amount):
        print("-" * 30)
        print("TRANSFERING")
        print("-" * 30)
        from_account = self.find_account(from_account_number)
        to_account = self.find_account(to_account_number)

        if not from_account:
            print("\nOrigin account not founded.\n")
            return
        if not to_account:
            print("\nDestination account not founded\n")
            return
        
        if from_account == to_account:
            print(" you cannot transfer to the same account\n")
            return
        
        if amount > 0 and from_account.get_balance() >= amount:
            print("\nProcessing Transfer...\n" * 3)

            

            from_account.withdraw(amount)
            to_account.deposit(amount) 
        else:
            print("invalid amount or insuficient balance")

    
    def display_all_accounts(self):
        print("-" * 30)
        print("All accounts: \n")
        print("-" * 30)

        if not self._accounts:
            print("\n no accounts registered in the bank yet.\n")
            return

        for indice, account in enumerate(self._accounts, start=1):
            print(f"\n-------Account #{indice}----------")
            account.display_info()
        print("-" * 30)

    def get_total_balance(self):
        total = 0.0
        for account in self._accounts:
            total += account.get_balance()
        
        print("-" * 30)
        print(f"Total bank balance: ${total:.2f}")
        print("-" * 30)
        return total

    def save_accounts(self, filename=None):
        if filename is None:
            filename = self._persistence_file
        data = [acct.to_dict() for acct in self._accounts]
        try:
            with open(filename, "w") as f:
                json.dump(data, f, indent=4)
            print(f"\nAccounts saved to {filename}\n")
        except Exception as e:
            print(f"Error saving accounts: {e}")

    def load_accounts(self, filename=None):
        
        if filename is None:
            filename = self._persistence_file
        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            return
        except Exception as e:
            print(f"Error loading accounts: {e}")
            return

        for acct_data in data:
            acct_type = acct_data.get("account_type", "").lower()
            if acct_type.startswith("checking"):
                acct = CheckingAccount.from_dict(acct_data)
            elif acct_type.startswith("saving"):
                acct = SavingsAccount.from_dict(acct_data)
            else:
                # unknown type: skip
                continue

            self._accounts.append(acct)
    
    def menu_principal(self):
        """Menu interativo"""
        while True:
            print("\n" + "="*50)
            print(f"  {self._name.upper()}")
            print("="*50)
            print("1 - Create account")
            print("2 - Deposit")
            print("3 - Withdraw")
            print("4 - Transfer")
            print("5 - View account")
            print("6 - View all accounts")
            print("7 - Transaction history")
            print("8 - Apply interest (Savings only)")
            print("9 - Delete account")
            print("10 - Save accounts")
            print("0 - Exit")
            print("="*50)
            
            choice = input("\nChoose: ")
            
            if choice == "1":
                holder_name = str(input("type your name: "))
                print("\n Type of Accounts: \n")
                print("1- Checking Account\n")
                print("2- Saving Account\n")
                choice = input("Choose the option (1 / 2): ")

                if choice == "1":
                    account_type = "checking"
                elif choice == "2":
                    account_type = "saving"

                else:
                    print("invalid type, returning to menu\n")
                    continue

                initial_deposit = float(input("make a initial deposit for your new account: "))
                self.create_account(holder_name, account_type, initial_deposit)
            
            elif choice == "2":
                try:
                    acc_num = int(input("type the account number: "))
                    account = self.find_account(acc_num)
                    if account:
                        amount = int(input("insert an amount you wan to deposit: "))
                        account.deposit(amount)
                    else:
                        print("\n account not founded.\n")
                except ValueError:
                    print("\n Invalid, try numbers only\n")
            
            elif choice == "3":
                try:
                    acc_num = int(input("type the account number: "))
                    account = self.find_account(acc_num)
                    if account:
                        amount = int(input("insert an amount you wan to deposit: "))
                        account.withdraw(amount)
                    else:
                        print("\n account not founded.\n")
                except ValueError:
                    print("\n Invalid, try numbers only\n")
            
            elif choice == "4":
                try:
                    from_account_number = int(input("type your number's account: "))
                    to_account_number = int(input("type number's account do u want to transfer: "))
                    amount = float(input("how much do you want to transfer"))

                    self.transfer(from_account_number, to_account_number, amount)
                except ValueError: 
                    print("\nInvalid, try numbers only.\n")
                pass
            
            elif choice == "5":
                try: 
                    acc_num = int(input("type the account number: "))
                    found_account = self.find_account(acc_num)

                    if found_account:
                        found_account.display_info()
                    else:
                        print("\n account not founded.")
                except ValueError:
                    print("Invalid input: numbers only, try again.")
            
            elif choice == "6":
                self.display_all_accounts()
            
            elif choice == "7":
                try:
                    acc_num = int(input("type the account number: "))
                    account = self.find_account(acc_num)
                    if account:
                        print("---Transactions history --- \n")
                        account.display_transactions()
                    else:
                        print("\nAccount NOT FOUNDED\n")
                except ValueError:
                    print("\n Invalid, try numbers only.\n")

                print("-" * 30)
            
            elif choice == "8":
                try:
                    acc_num = int(input("type the account number: "))
                    account = self.find_account(acc_num)

                    if account:
                        if isinstance(account, SavingsAccount):
                            account.apply_interest()
                        else:
                            print("interest can be applied just in Saving's Account")
                    else:
                        print("\n your account was not founded.\n")
                except ValueError:
                    print("\ninvalid, try numbers only \n")
                
            elif choice == "9":
                    try:
                        acc_num = int(input("type the account number: "))
                        self.delete_account(acc_num)
                    except ValueError:
                        print("Invalid, try again.")
                    
            elif choice == "10":
                # persist accounts to JSON file
                self.save_accounts()

            elif choice == "0":
                # save automatically before exit
                self.save_accounts()
                print("\n👋 Thank you for using our bank!")
                break
            
            else:
                print("❌ Invalid option!")


# --- EXECUÇÃO ---
if __name__ == "__main__":
    bank = Bank("Jewish Bank")
    bank.menu_principal()