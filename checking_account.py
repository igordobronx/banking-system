from account import Account

class CheckingAccount(Account):
    def __init__(self, account_number, holder_name, balance, overdraw_limit=500.0):
        
        super().__init__(account_number, holder_name, balance, "Checking")
        
        self.overdraw_limit = overdraw_limit
        self.withdraw_fee = 2.50

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "overdraw_limit": self.overdraw_limit,
            "withdraw_fee": self.withdraw_fee,
        })
        return data

    @classmethod
    def from_dict(cls, data):
        acct = cls(
            data["account_number"],
            data["holder_name"],
            data.get("balance", 0),
            data.get("overdraw_limit", 500.0),
        )
        acct.withdraw_fee = data.get("withdraw_fee", 2.50)
        acct._transactions = data.get("transactions", [])
        return acct

    def withdraw(self, amount):
        if amount > 0:

            total_deduction = amount + self.withdraw_fee

            if (self._balance + self.overdraw_limit) >= total_deduction:
                self._balance -= total_deduction

                self._add_transaction(f"withdraw : ${amount:.2f} (Fee: ${self.withdraw_fee:.2f})")
                print(f"\nwithdraw in the value of ${amount} has been done. Fee of {self.withdraw_fee}\n.")
            else:
                print("\n Balance and overdraw Limit invalid for this withdraw\n")
        else:
            print("\nInvalid Value\n")



