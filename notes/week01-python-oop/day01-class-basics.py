# Week 01: Python面向对象

## 2026.09.03 - 2026.09.07

### 今日学习（09.03）
"""练习1：银行账户
创建一个名为 BankAccount 的类，为其方法 init() 设置属性 owner（账户持有人）和 balance（余额，默认值为0）。
创建一个名为 deposit() 的方法，接受一个参数 amount， 将 amount 加到余额上，并打印"存入 XX 元，当前余额：XX 元"。
创建一个名为 withdraw() 的方法，接受一个参数 amount， 如果余额足够，扣除 amount 并打印"取出 XX 元，当前余额：XX 元"，
如果余额不足，打印"余额不足，当前余额：XX 元"。
创建一个名为 get_balance() 的方法，打印"XX 的账户余额为：XX 元"。
根据这个类创建一个名为 account 的实例，分别调用存款、取款、查余额方法。 """

# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"存入{amount}元， 当前余额：{self.balance}元")
#
#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print(f"取出{amount}元，当前余额：{self.balance}元")
#         else:
#             print(f"余额不足，当前余额：{self.balance}元")
#
#     def get_balance(self):
#         print(f"{self.owner}的账户余额为：{self.balance}元")

# account = BankAccount("陆鸣", 3000 )
# account.get_balance()
# account.deposit(2000)
# account.withdraw(6000)
# account.get_balance()




"""练习2：银行账户进阶
在为完成练习1而编写的程序中，添加一个名为 account_number 的属性， 由系统自动生成（格式为"ACC" + 6位数字，如"ACC000001"）。 
添加一个类属性 total_accounts = 0，每创建一个账户自动加1。 
添加一个名为 transaction_history 的属性，默认值为空列表， 用于记录每笔交易（存入或取出的金额）。 
添加一个名为 show_history() 的方法，打印所有交易记录。 
添加一个名为 transfer() 的方法，接受另一个 BankAccount 实例和金额作为参数， 将当前账户的金额转到另一个账户，并分别记录双方的交易历史。 
创建两个账户实例，互相转账，测试所有功能。 """

class BankAccount:
    # 新增：类属性，用于记录创建的账户总数，初始值为0
    total_accounts = 0

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

        # 每创建一个账户自动加1
        BankAccount.total_accounts += 1

        # 新增：自动生成账户编号
        # str() 将数字转为字符串，zfill(6) 表示在左侧补0直到总长度为6位
        self.account_number = f"ACC{str(BankAccount.total_accounts).zfill(6)}"

        # 新增：初始化交易历史列表，默认为空列表
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        #新增:将存款记录添加到历史交易列表中
        self.transaction_history.append(f"存入{amount}元")
        print(f"存入{amount}元， 当前余额：{self.balance}元")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            # 新增:将取款记录添加到历史交易列表中
            self.transaction_history.append(f"取出{amount}元")
            print(f"取出{amount}元，当前余额：{self.balance}元")
        else:
            print(f"余额不足，当前余额：{self.balance}元")

    def get_balance(self):
        print(f"{self.owner}(账号: {self.account_number})的账户余额为：{self.balance}元")

    def show_history(self):
        print(f"\n--- {self.owner} 的交易记录 ---")
        # 判断列表是否为空
        if not self.transaction_history:
            print("暂无交易记录。")
        else:
            # 遍历列表，逐行打印每一条交易记录
            for record in self.transaction_history:
                print(record)
        print('-'*20)

    def transfer(self,target_account, amount):
        # 先检查余额是否足够
        if self.balance >= amount:
            self.balance -= amount
            target_account.balance += amount

            # 记录转账的交易历史
            self.transaction_history.append(f"转账给{target_account.owner}{amount}元")
            target_account.transaction_history.append(f"收到来自{self.owner}的转账{amount}元")
            print("转账成功")

        else:
            print(f"转账失败：{self.owner} 的余额不足，当前余额：{self.balance} 元")

# --- 测试代码 ---
if __name__ == "__main__":
    #创建账户
    account01 = BankAccount("萧炎", 3000 )
    account02 = BankAccount("林动", 2000 )
    print(BankAccount.total_accounts)

    #测试存取款
    account01.deposit(5000)
    account02.deposit(1000)
    account01.withdraw(3000)
    account02.withdraw(2000)

    #测试转账
    account01.transfer(account02, 2000)

    #查看余额和历史
    account01.get_balance()
    account02.get_balance()
    account01.show_history()
    account02.show_history()

