# Week 01: Python 面向对象编程

## 学习目标
- 掌握类和对象的基本概念
- 理解继承、封装、多态等面向对象核心特性
- 学会设计、实现并测试实用的类
- 能用 OOP 思路拆解并解决实际问题

## 学习进度

| 日期 | 内容 | 文件 | 状态 |
|------|------|------|------|
| 09.03 | 类的基础概念和银行账户系统 | day01-class-basics.py | ✅ 完成 |

## 总览（思维导图）

类与对象
  ├── 类属性（全局共享）
  ├── 实例属性（个体独立）
  └── 实例方法（操作个体数据）

继承
  ├── 子类复用父类代码（super()）
  ├── 子类新增属性和方法
  └── 方法重写 → 多态

类方法 / 静态方法
  ├── @classmethod：操作类属性或实现工厂方法
  ├── @staticmethod：独立工具函数
  └── 工厂模式：统一入口创建不同类型对象

---

## 核心内容

### 1. 基本语法与示例

```python
class ClassName:
    def __init__(self, param):
        self.attribute = param
```

- `class`：定义类
- `__init__()`：构造方法，在创建对象时自动调用
- `self`：代表当前实例，通过 `self.xxx` 访问实例数据

### 2. 类属性 vs 实例属性

- 类属性（class attribute）：定义在 class 体内、方法外，由类和所有实例共享；通过 `ClassName.attr` 或 `instance.__class__.attr` 访问/修改
- 实例属性（instance attribute）：定义在 `__init__` 中，通常以 `self.xxx` 形式，每个实例各自独立

示例：

```python
class BankAccount:
    total_accounts = 0          # ← 类属性：所有账户共用这一个

    def __init__(self, owner, balance=0):
        self.owner = owner      # ← 实例属性：每个账户各有一份
        self.balance = balance  # ← 实例属性：每个账户各有一份
        self.transaction_history = []
        BankAccount.total_accounts += 1  # 每次创建实例，计数器+1
```

### 3. 继承与方法重写

- 使用 `class Sub(Parent):` 声明继承关系
- `super()` 可调用父类方法或构造器以复用父类逻辑
- 子类可重写父类方法以实现不同的行为（多态）

示例：

```python
class CreditAccount(BankAccount):
    def __init__(self, owner, balance=0, credit_limit=5000):
        super().__init__(owner, balance)
        self.credit_limit = credit_limit
        self.current_debt = 0

    def withdraw(self, amount):
        # 支持透支：允许余额+可用信用覆盖取款
        available = self.balance + (self.credit_limit - self.current_debt)
        if amount <= available:
            if amount <= self.balance:
                self.balance -= amount
            else:
                overdraft = amount - self.balance
                self.current_debt += overdraft
                self.balance = 0
            self.transaction_history.append(('withdraw', amount))
            return True
        return False
```

### 4. 类方法与静态方法

- `@classmethod`：方法第一个参数是 `cls`，常用于操作类属性或作为工厂方法
- `@staticmethod`：无 `self` 或 `cls`，用于把函数放到类命名空间但不依赖实例或类状态

示例：

```python
class Bank:
    accounts = {}

    @classmethod
    def open_account(cls, account_type, *args, **kwargs):
        # 简单工厂：根据 account_type 创建不同账户
        if account_type == 'savings':
            acc = SavingsAccount(*args, **kwargs)
        elif account_type == 'credit':
            acc = CreditAccount(*args, **kwargs)
        else:
            acc = BankAccount(*args, **kwargs)
        cls.accounts[acc.owner] = acc
        return acc

    @staticmethod
    def total_balance():
        return sum(acc.balance for acc in Bank.accounts.values())
```

### 5. 常见设计思路（练习说明）

Day 01: 银行账户系统练习（从易到难）
- 练习1：BankAccount 基础（属性：owner, balance；方法：deposit, withdraw, get_balance）
- 练习2：进阶（自动生成 account_number、类属性 total_accounts、transaction_history、transfer, show_history）
- 练习3：CreditAccount（继承 BankAccount，新增 credit_limit、current_debt，重写 withdraw，新增 pay_debt）
- 练习4：SavingsAccount（继承 BankAccount，新增 interest_rate，calculate_interest, add_interest，deposit 的奖励逻辑）
- 练习5：Bank 管理类（accounts 字典、开户/销户/查询/统计等）

## 相关概念快速回顾

| 概念 | 说明 |
|------|------|
| 封装 | 将数据和方法封装在类中，控制对内部状态的访问 |
| 继承 | 子类继承父类的属性和方法，复用代码 |
| 多态 | 不同子类对同一方法有不同实现，调用者无需关心具体类型 |
| 类属性 | 由类本身持有，所有实例共享 |
| 实例属性 | 由实例持有，每个实例各自独立 |

## 扩展思考（可作为作业或挑战题）
- 添加账户密码验证与登录权限控制（安全考虑）
- 记录操作时间戳与操作来源（日志）
- 实现定期自动计息（可用调度或手动触发）
- 防止异常操作（如负数存/取、超大转账）并使用异常处理（raise）
- 为 Bank 增加持久化（保存到 JSON/CSV/数据库）和单元测试覆盖

## 运行方式

```bash
# 运行示例脚本
python day01-class-basics.py

# 或在交互环境中载入
python
>>> exec(open('day01-class-basics.py').read())
```

---

*Last Updated: 2026.09.04*
