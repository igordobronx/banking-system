from account import Account

class SavingsAccount(Account):
    
    def __init__(self, account_number, holder_name, balance, interest_rate=0.5):
        
        super().__init__(account_number, holder_name, balance, "Savings")
        
        self._interest_rate = interest_rate
        self._withdraw_this_month = 0
        self.withdraw_fee = 5.00

    def to_dict(self):
        data = super().to_dict()
        data.update({
            "interest_rate": self._interest_rate,
            "withdraw_this_month": self._withdraw_this_month,
            "withdraw_fee": self.withdraw_fee,
        })
        return data

    @classmethod
    def from_dict(cls, data):
        acct = cls(
            data["account_number"],
            data["holder_name"],
            data.get("balance", 0),
            data.get("interest_rate", 0.5),
        )
        acct._withdraw_this_month = data.get("withdraw_this_month", 0)
        acct.withdraw_fee = data.get("withdraw_fee", 5.00)
        acct._transactions = data.get("transactions", [])
        return acct

    def apply_interest(self):
        if self._balance > 0:
            interest_amount = self._balance * (self._interest_rate / 100)
            self._balance += interest_amount

            self._add_transaction(f"Interest Applied: +{interest_amount:.2f}\n")
            print(f"interest of {interest_amount} has been applied.\n")

        else:
            print("\nbalance is 0 or negative, Invalid.\n")

    def withdraw(self, amount):
        if amount > 0:
            if self._withdraw_this_month < 3:
                fee = 0
            else: 
                fee = self.withdraw_fee
            total_deduction = amount + fee

            if self._balance >= total_deduction:
                self._balance -= total_deduction
                self._withdraw_this_month += 1 #conta mais um saque no mês

                if fee > 0:
                    self._add_transaction(f"withdraw of ${amount:.2f} (fee{fee:.2f})")
                else:
                    self._add_transaction(f"withdraw of ${amount:.2f}")

        
