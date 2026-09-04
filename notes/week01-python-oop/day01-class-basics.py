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

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"存入{amount}元， 当前余额：{self.balance}元")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"取出{amount}元，当前余额：{self.balance}元")
        else:
            print(f"余额不足，当前余额：{self.balance}元")

    def get_balance(self):
        print(f"{self.owner}的账户余额为：{self.balance}元\n")
print("----1.银行账户----")
account = BankAccount("陆鸣", 3000 )
account.get_balance()
account.deposit(2000)
account.withdraw(6000)
account.get_balance()




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

print("----2.进阶账户----")
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

"""练习3：信用卡账户
信用卡账户是一种特殊的银行账户。编写一个名为 CreditCard 的类， 让它继承为完成练习1或练习2而编写的 BankAccount 类。 
添加一个名为 credit_limit 的属性，表示信用额度（默认值为10000）。 
添加一个名为 current_debt 的属性，表示当前欠款（默认值为0）。 
重写 withdraw() 方法：当余额不足时，如果未超过信用额度， 允许透支并打印"已透支 XX 元，当前欠款：XX 元"， 如果超过信用额度，打印"超出信用额度，交易失败"。 
添加一个名为 pay_debt() 的方法，接受一个金额， 用于还款，减少 current_debt 并增加 balance。 
添加一个名为 show_credit_info() 的方法，打印信用额度、当前欠款、可用额度。 
创建一个 CreditCard 实例，测试透支、还款、查信用信息等功能。 """

class CreditCard(BankAccount):
    def __init__(self, owner, balance=0,credit_limit=10000,current_debt=0):
        # super()找到父类
        # .__init__(owner, balance)调用父类的构造方法
        super().__init__(owner, balance)
        # 信用卡特有属性：信用额度 当前欠款
        self.credit_limit = credit_limit
        self.current_debt = current_debt

    def withdraw(self, amount):
        # 余额足够，正常取款
        if self.balance >= amount:
            self.balance -= amount
            print(f"取出{amount}元，当前余额：{self.balance}元")
        # 余额不足，尝试透支
        else:
            # 透支金额 = 取款金额 - 当前余额
            need_overdraft = amount - self.balance
            # 总欠款 = 当前欠款 + 本次透支金额
            new_debt = self.current_debt + need_overdraft

            if new_debt <= self.credit_limit:
                self.balance = 0
                self.current_debt = new_debt
                print(f"已透支{need_overdraft}元，当前欠款：{self.current_debt}元")
            else:
                print("超出信用额度，交易失败")

    def pay_debt(self, amount):
        if amount <= 0:
            print("还款金额必须大于0！")
        else:
            # 如果还款金额 <= 当前欠款，全部用来还债
            if amount <= self.current_debt:
                self.current_debt -= amount
                print(f"还款{amount}元，当前欠款：{self.current_debt}元")
            # 如果还款金额 > 当前欠款，先还清欠款，多余部分回到余额
            else:
                extra = amount - self.current_debt
                self.current_debt = 0
                self.balance += extra
                print(f"还款{amount}元，欠款已还清，多余{extra}元已存入余额，当前余额：{self.balance}元")

    def show_credit_info(self):
        available = self.credit_limit - self.current_debt
        print(f"{self.owner}的信用卡信息：")
        print(f" 信用额度：{self.credit_limit}元")
        print(f" 当前欠款：{self.current_debt}元")
        print(f" 可用额度：{available}元")

print("----3.信用账户----")
card = CreditCard("张三", balance=3000, credit_limit=10000)
card.show_credit_info()
card.withdraw(2000)
card.withdraw(5000)
card.withdraw(9000)
card.pay_debt(1000)
card.pay_debt(6000)
card.show_credit_info()
card.deposit(500)
card.get_balance()






"""练习4：储蓄账户
储蓄账户是另一种特殊的银行账户。编写一个名为 SavingsAccount 的类， 让它继承 BankAccount 类。 
添加一个名为 interest_rate 的属性，表示年利率（默认值为0.03）。 
添加一个名为 calculate_interest() 的方法，计算并返回一年的利息金额。 
添加一个名为 add_interest() 的方法，将利息加到余额上， 并打印"利息已到账：XX 元，当前余额：XX 元"。 
重写 deposit() 方法：每次存入金额时，如果存入金额 >= 1000， 额外奖励10元并打印"大额存款奖励10元已到账"。 
创建一个 SavingsAccount 实例，测试存款、计算利息、加利息等功能。 """

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.03):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        #返回利息
        return interest

    def add_interest(self):
        interest = self.calculate_interest()
        self.balance += interest
        print(f"利息已到账：{interest}元，当前余额：{self.balance}元")

    def deposit(self, amount):
        self.balance += amount
        print(f"存入{amount}元，当前余额：{self.balance}元")
        if amount >= 1000:
            self.balance += 10
            print("大额存款奖励10元已到账")

print("----4.储蓄账户----")
sa = SavingsAccount("李四", balance=5000)
sa.deposit(500)
sa.deposit(2000)
sa.add_interest()
sa.get_balance()












"""练习5：银行系统管理
编写一个名为 Bank 的类，用于管理所有账户。 
添加一个类属性 accounts = {}，用字典存储所有账户（键为账户号，值为账户对象）。 
添加一个名为 open_account() 的类方法，接受账户类型（"普通"/"信用卡"/"储蓄"） 和持有人姓名，创建对应类型的账户并加入 accounts。 
添加一个名为 close_account() 的类方法，接受账户号，从 accounts 中删除该账户。 
添加一个名为 show_all_accounts() 的类方法，打印所有账户的基本信息。 
添加一个名为 total_bank_balance() 的静态方法，计算并返回银行所有账户的总余额。 
创建多种类型的账户，测试开户、销户、查询、统计等功能。 """

#                 类属性	               实例属性
# 定义位置	class 下面、方法外面	     __init__ 里面
# 访问方式	Bank.accounts	         account.owner
# 特点	    所有对象共享同一份	         每个对象各自独立

# | 概念 | 说明 |
# |------|------|
# | `accounts = {}`          | 类属性，所有实例共享，用来存所有账户 |
# | `@classmethod`           | 类方法，第一个参数是 `cls`（类本身），可以直接操作类属性 |
# | `@staticmethod`          | 静态方法，不需要 `self` 也不需要 `cls`，独立函数 |
# | `account_counter`        | 用来自动生成递增的账户号 |
# | `type(account).__name__` | 获取对象的类名，用来显示账户类型 |





class Bank:
    accounts = {}
    account_counter = 1001  # 用于自动生成账户号

    @classmethod
    def open_account(cls, account_type, owner):
        if account_type == "普通":
            account = BankAccount(owner)
        elif account_type == "信用卡":
            account = CreditCard(owner)
        elif account_type == "储蓄":
            account = SavingsAccount(owner)
        else:
            print("不支持的账户类型")
            return

        # 生成卡号
        account_num = str(cls.account_counter)
        # 把账户存进银行系统
        cls.accounts[account_num] = account
        # 计数器+1，下次开户用下一个号
        cls.account_counter += 1
        # 告诉用户开户成功
        print(f"开户成功！卡号：{account_num}，类型：{account_type}，持有人：{owner}")

    @classmethod
    def close_account(cls, account_num):
        if account_num in cls.accounts:
            account = cls.accounts[account_num]
            del cls.accounts[account_num]
            print(f"销户成功！账户号：{account_num}，持有人：{account.owner}")
        else:
            print(f"账户号 {account_num} 不存在")

    @classmethod
    def show_all_accounts(cls):
        if not cls.accounts:
            print("当前没有任何账户")
            return
        print("===== 所有账户信息 =====")
        # for 卡号, 账户 in Bank.accounts.items():
        #     print(卡号, type(账户))
        for account_num, account in cls.accounts.items():
            account_type = type(account).__name__
            print(f"账户号：{account_num}，类型：{account_type}，持有人：{account.owner}，余额：{account.balance}元")

    @staticmethod
    def total_bank_balance():
        total = 0  # 初始化总余额为0
        for account in Bank.accounts.values():  # 遍历所有账户对象
            # .values() 就是拿出所有账户对象：
            # [张三的账户, 李四的账户, 王五的账户]
            total += account.balance  # 把每个账户的余额累加到total
        return total  # 返回总余额

print("----5.账户管理----")

# 1. 开户
Bank.open_account("普通", "张三")
Bank.open_account("信用卡", "李四")
Bank.open_account("储蓄", "王五")
Bank.open_account("基金", "赵六")  # 不支持的类型，会提示错误

print()

# 2. 查询所有账户
Bank.show_all_accounts()

print()

# 3. 存款、取款测试
Bank.accounts["1001"].deposit(5000)
Bank.accounts["1002"].deposit(3000)
Bank.accounts["1003"].deposit(8000)

print("----- 存取款后 -----")
Bank.show_all_accounts()

print()

# 4. 统计总余额
print(f"银行总余额：{Bank.total_bank_balance()}元")

print()

# 5. 销户
Bank.close_account("1002")

print()

# 6. 销户后再查询
Bank.show_all_accounts()
print(f"银行总余额：{Bank.total_bank_balance()}元")
