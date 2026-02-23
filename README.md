# 🏦 Banking System

A comprehensive banking system built with Python, demonstrating Object-Oriented Programming principles such as inheritance, encapsulation, and polymorphism.

---

## 📋 Features

### 💳 Account Types

#### 🔹 Checking Account
- Overdraft protection (R$ 500 limit)
- R$ 2.50 withdrawal fee
- Unlimited withdrawals

#### 🔹 Savings Account
- Monthly interest rate (0.5%)
- 3 free withdrawals per month
- R$ 5.00 fee for additional withdrawals

---

### ⚙️ Core Functionality

- ✅ Create and manage multiple accounts  
- ✅ Deposit and withdraw funds  
- ✅ Transfer money between accounts  
- ✅ Transaction history tracking  
- ✅ Account balance inquiries  
- ✅ Apply monthly interest (Savings accounts)  
- ✅ Data persistence (JSON storage)  

---

## 🛠️ Technologies

- Python 3.x  
- JSON (for data persistence)  

### OOP Principles:
- Inheritance  
- Encapsulation  
- Polymorphism  

---

## 📂 Project Structure

```text
banking-system/
├── account.py              # Base Account class
├── checking_account.py     # CheckingAccount (inherits from Account)
├── saving_account.py       # SavingsAccount (inherits from Account)
├── bank.py                 # Bank class - manages all accounts
├── accounts.json           # Persistent storage
└── README.md
```

---

## 🚀 Getting Started

### 📌 Prerequisites

- Python 3.7 or higher

### 📥 Installation

Clone the repository:

```bash
git clone https://github.com/igordobronx/banking-system.git
cd banking-system
```

Run the system:

```bash
python bank.py
```

---

## 💻 Usage

The system provides an interactive menu with the following options:

```text
1 - Create account
2 - Deposit
3 - Withdraw
4 - Transfer
5 - View account
6 - View all accounts
7 - Transaction history
8 - Apply interest (Savings only)
9 - Delete account
0 - Exit
```

---

## 📝 Example Usage

### Creating an Account

```text
Choose option: 1
Holder name: John Doe
Account type (checking/savings): checking
Initial deposit: 1000.00
✅ Account #1001 created successfully!
```

### Making a Transfer

```text
Choose option: 4
From account: 1001
To account: 1002
Amount: 250.00
✅ Transfer completed successfully!
```

---

## 🏗️ Architecture

### 📊 Class Hierarchy

```text
Account (Base Class)
├── CheckingAccount
└── SavingsAccount

Bank (Manages accounts)
```

---

## 🧠 Key OOP Concepts Demonstrated

- **Inheritance** – `CheckingAccount` and `SavingsAccount` inherit from `Account`
- **Encapsulation** – Private attributes with getter methods
- **Polymorphism** – Overridden `withdraw()` method with different behaviors
- **Composition** – `Bank` class contains and manages `Account` objects

---

## 📊 Features in Detail

### 🔹 Account Features
- Auto-generated unique account numbers  
- Complete transaction history with timestamps  
- Balance validation before operations  
- Fee calculation and tracking  

### 🔹 Checking Account Specifics
- Overdraft Limit: R$ 500.00  
- Withdrawal Fee: R$ 2.50 per transaction  
- Available Balance: Regular balance + overdraft limit  

### 🔹 Savings Account Specifics
- Interest Rate: 0.5% monthly  
- Free Withdrawals: First 3 per month  
- Additional Withdrawal Fee: R$ 5.00  
- Interest Application: Applied monthly via menu  

---

## 💾 Data Persistence

- Accounts are automatically saved to `accounts.json`  
- Data persists between sessions  
- Automatic loading on startup  

---

## 🔒 Security Features

- Balance validation before withdrawals  
- Overdraft limit enforcement  
- Account deletion requires zero balance  
- Transaction history for auditing  

---

## 🧪 Built-in Validations

- Amount validation (must be positive)  
- Sufficient funds verification  
- Account existence checks  
- Transfer validation (both accounts must exist)  

---

## 📝 Example Scenarios

### Scenario 1: Regular Banking Operations

```python
# User creates checking account with R$ 1000
# Makes deposit of R$ 500 → Balance: R$ 1497.50
# Withdraws R$ 300 → Balance: R$ 1195.00
# Transaction history shows all operations
```

### Scenario 2: Overdraft Usage

```python
# Checking account balance: R$ 100
# Withdraws R$ 400 → Successful (uses R$ 300 from overdraft)
# New balance: -R$ 302.50 (includes R$ 2.50 fee)
```

### Scenario 3: Savings Account Interest

```python
# Savings account balance: R$ 2000
# Apply interest → New balance: R$ 2010 (0.5% = R$ 10)
# Free withdrawal counter resets to 3
```

---

## 🤝 Contributing

This is a learning project, but suggestions are welcome!

You can:

1. Fork the repository  
2. Create a feature branch  
3. Make your changes  
4. Submit a pull request  

---

## 📫 Contact

**Igor Dobronx**  

GitHub: https://github.com/igordobronx  
Project Link: https://github.com/igordobronx/banking-system  

---

## 🎓 Learning Objectives

This project demonstrates:

- ✅ Class design and inheritance hierarchies  
- ✅ Method overriding and polymorphism  
- ✅ Encapsulation with private attributes  
- ✅ File I/O and data persistence  
- ✅ User input validation  
- ✅ Business logic implementation  
- ✅ Clean code organization and modularity  

---

## 📄 License

This project is open source and available for educational purposes.

---

⭐ If you found this project helpful, consider giving it a star!
