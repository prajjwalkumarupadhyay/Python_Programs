class BankAccount:
    def __init__(self,accountHolder):
        self._balance=0
        self._name=accountHolder
        with open(self._name+'ledger.txt','a') as LedgerFile:
            LedgerFile.write('Balance is 0 \n')
    def deposit(self,amount):
        if amount<=0:
            return
        self._balance+=amount
        with open(self._name+'Ledger.txt','a') as LedgerFile:
            LedgerFile.write('Deposit'+str(amount)+'\n')
            LedgerFile.write('Balance is '+ str(self._balance)+'\n')
    def withdraw(self,amount):
        if self._balance<amount or amount<0:
            return 
        self._balance-=amount
        with open(self._name_+'Ledger.txt','a') as LedgerFile:
            LedgerFile.write('Withdraw'+str(amount)+'\n')
            LedgerFile.write('Balance is '+str(self._balance)+'\n')
acct=BankAccount('Alice')
acct.deposit(120)
acct.withdraw(40)
