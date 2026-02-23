class Account:
    def __init__(self, account_number, holder_name, balance, account_type):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self._balance = balance
        self.__account_type = account_type
        self._transactions = []

    def get_account_number(self):
        return self.__account_number
    
    def get_holder_name(self):
        return self.__holder_name
    
    def get_balance(self):
        return self._balance
    
    def get_account_type(self):
        return self.__account_type
    
    def get_transactions(self):
        return self._transactions
    
    def _add_transaction(self, description):
        self._transactions.append(description)
    
    def deposit(self, amount, description="deposit"):
        if amount > 0:
            self._balance += amount
            self._add_transaction(f"{description}: +{amount}")
            print(f"\n{description} of {amount} has been done.\n")
        else:
            print("\ninvalid value.\n")

    def withdraw(self, amount, description="withdraw"):
        # ensure we reference the protected _balance attribute
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            self._add_transaction(f"{description}: -{amount}")
            print(f"{description} of ${amount} has been done.\n")
        else:
            print("Invalid value\n")

    def display_info(self):
        print(f"Name: {self.get_holder_name()}")
        print(f"Balance: {self.get_balance()}")
        print(f"Account Number: {self.get_account_number()}")
        print(f"account Type: {self.get_account_type()}\n")

    
    def display_transactions(self):
        print("\n---TRANSACTION HISTORY ---\n")

        if not self._transactions:
            print("no transaction yet.")
        else:
            for transaction in self._transactions:
                print(f"{transaction}")
        print("-" * 30)

    # serialization helpers
    def to_dict(self):
        return {
            "account_number": self.get_account_number(),
            "holder_name": self.get_holder_name(),
            "balance": self.get_balance(),
            "account_type": self.get_account_type(),
            "transactions": self.get_transactions(),
        }

    @classmethod
    def from_dict(cls, data):
        # This base implementation will not normally be used directly since
        # we instantiate subclasses in Bank.load_accounts(), but it's
        # provided for completeness.
        acct = cls(data["account_number"], data["holder_name"], data["balance"], data.get("account_type"))
        acct._transactions = data.get("transactions", [])
        return acct

    