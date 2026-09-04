# Python 面向对象编程 - Week 01

**学习周期：** 2026.09.03 - 2026.09.07

## 📌 核心知识点

### 1. 类的基础概念 (Class Basics)

#### 什么是类？
- **类** 是创建对象的蓝图或模板
- **对象** 是类的实例
- 类封装了数据（属性）和行为（方法）

#### 类的定义
```python
class ClassName:
    def __init__(self, parameters):
        # 初始化属性
        self.attribute = value
    
    def method(self):
        # 方法实现
        pass
```

---

### 2. 属性 (Attributes)

#### 2.1 实例属性 (Instance Attributes)
- 定义在 `__init__()` 方法内
- 每个对象各自独立拥有一份
- 访问方式：`object.attribute`
- **示例**：BankAccount 的 owner 和 balance

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner        # 实例属性
        self.balance = balance    # 实例属性
```

#### 2.2 类属性 (Class Attributes)
- 定义在类下面、方法外面
- 所有对象共享同一份
- 访问方式：`ClassName.attribute` 或 `self.attribute`
- **示例**：BankAccount 的 total_accounts

```python
class BankAccount:
    total_accounts = 0  # 类属性，所有实例共享
    
    def __init__(self, owner, balance=0):
        BankAccount.total_accounts += 1
```

#### 2.3 属性对比表

| 概念 | 定义位置 | 访问方式 | 特点 |
|------|---------|---------|------|
| **实例属性** | `__init__()` 内 | `self.attribute` | 每个对象各自独立 |
| **类属性** | class 下面、方法外 | `ClassName.attribute` | 所有对象共享同一份 |

---

### 3. 方法 (Methods)

#### 3.1 实例方法 (Instance Methods)
- 第一个参数是 `self`（表示当前对象）
- 可以访问实例属性和类属性
- 在对象上调用

```python
def deposit(self, amount):
    self.balance += amount
    print(f"存入{amount}元，当前余额：{self.balance}元")

# 调用方式
account.deposit(1000)
```

#### 3.2 类方法 (Class Methods)
- 用 `@classmethod` 装饰器标记
- 第一个参数是 `cls`（表示类本身）
- 用于操作类属性

```python
@classmethod
def open_account(cls, account_type, owner):
    cls.accounts[account_num] = account
    cls.account_counter += 1

# 调用方式
Bank.open_account("普通", "张三")
```

#### 3.3 静态方法 (Static Methods)
- 用 `@staticmethod` 装饰器标记
- 不需要 `self` 也不需要 `cls`
- 是独立的函数

```python
@staticmethod
def total_bank_balance():
    total = 0
    for account in Bank.accounts.values():
        total += account.balance
    return total

# 调用方式
Bank.total_bank_balance()
```

---

### 4. 继承 (Inheritance)

#### 4.1 继承的概念
- 子类继承父类的属性和方法
- 减少代码重复，提高代码复用性
- 语法：`class ChildClass(ParentClass):`

#### 4.2 调用父类方法
- 使用 `super()` 调用父类的方法
- 通常用于调用父类的 `__init__()` 方法

```python
class CreditCard(BankAccount):
    def __init__(self, owner, balance=0, credit_limit=10000):
        super().__init__(owner, balance)  # 调用父类初始化
        self.credit_limit = credit_limit  # 子类特有属性
```

#### 4.3 方法重写 (Method Overriding)
- 子类可以重新定义父类的方法
- 实现不同的行为

```python
# 父类
def withdraw(self, amount):
    if self.balance >= amount:
        self.balance -= amount
        print(f"取出{amount}元")

# 子类（CreditCard）- 重写
def withdraw(self, amount):
    if self.balance >= amount:
        self.balance -= amount
    else:
        # 支持透支
        need_overdraft = amount - self.balance
        new_debt = self.current_debt + need_overdraft
        if new_debt <= self.credit_limit:
            self.current_debt = new_debt
```

---

### 5. 项目实战：银行系统

通过5个递进式练习，从基础到高级：

#### 练习 1：基础银行账户
- **核心**：类、属性、方法的基本使用
- **功能**：存款、取款、查余额
- **类名**：`BankAccount`

#### 练习 2：进阶银行账户
- **核心**：类属性、自动生成ID、交易记录
- **新增**：
  - 类属性 `total_accounts` 自动计数
  - 自动生成账户号（ACC + 6位数字）
  - 交易历史列表 `transaction_history`
  - 转账方法 `transfer()`

#### 练习 3：信用卡账户（继承）
- **核心**：继承、方法重写
- **继承自**：`BankAccount`
- **新增**：
  - 信用额度 `credit_limit`
  - 当前欠款 `current_debt`
  - 透支功能
  - 还款方法 `pay_debt()`
  - 信用信息查询 `show_credit_info()`

#### 练习 4：储蓄账户（继承）
- **核心**：继承、方法重写
- **继承自**：`BankAccount`
- **新增**：
  - 年利率 `interest_rate`
  - 计算利息 `calculate_interest()`
  - 加利息 `add_interest()`
  - 大额存款奖励（存入 ≥ 1000元额外奖励10元）

#### 练习 5：银行系统管理
- **核心**：类方法、静态方法、系统设计
- **类名**：`Bank`
- **核心功能**：
  - 类属性 `accounts = {}` 存储所有账户
  - 开户 `open_account()` - 支持多种账户类型
  - 销户 `close_account()`
  - 查询所有账户 `show_all_accounts()`
  - 统计总余额 `total_bank_balance()` - 静态方法

---

## 🔑 关键概念总结

### `__init__()` 构造方法
- 对象创建时自动调用
- 用于初始化属性
- 第一个参数必须是 `self`

```python
def __init__(self, owner, balance=0):
    self.owner = owner
    self.balance = balance
```

### 自动生成ID
- 使用类属性计数器
- 每次创建对象时递增

```python
class BankAccount:
    total_accounts = 0
    
    def __init__(self, owner):
        BankAccount.total_accounts += 1
        self.account_number = f"ACC{str(BankAccount.total_accounts).zfill(6)}"
```

### 字符串格式化技巧

| 技巧 | 用途 | 示例 |
|------|------|------|
| `f"文本{变量}文本"` | f-string 格式化 | `f"余额：{balance}元"` |
| `str().zfill(n)` | 左侧补0至n位 | `"1".zfill(6)` → `"000001"` |
| `type(obj).__name__` | 获取对象类名 | 显示账户类型 |

---

## 📚 学习资源与应用

### 设计模式应用
- **工厂模式**：Bank.open_account() 根据类型创建不同对象
- **多态**：不同账户类型有不同的 withdraw() 行为

### 代码复用性
- 通过继承避免重复代码
- 每个子类只需编写自己特有的逻辑

### 实际应用场景
- 银行系统、电商平台、库存管理等

---

## 📝 练习检查清单

- [ ] 理解类与对象的关系
- [ ] 掌握实例属性和类属性的区别
- [ ] 能够编写实例方法、类方法、静态方法
- [ ] 理解继承和方法重写的概念
- [ ] 能够使用 super() 调用父类方法
- [ ] 完成5个银行系统练习
- [ ] 理解 `__init__()` 构造方法的作用
- [ ] 掌握 f-string 字符串格式化

---

**更新日期：** 2026-09-04  
**课程类型：** Python 面向对象编程基础
