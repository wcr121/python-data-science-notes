# Week 01: Python面向对象编程

## 学习目标
- 掌握类和对象的基本概念
- 理解继承、多态等面向对象核心特性
- 学会设计和实现实用的类
- 应用OOP思想解决实际问题

## 学习进度

| 日期 | 内容 | 文件 | 状态 |
|------|------|------|------|
| 09.03 | 类的基础概念和银行账户系统 | day01-class-basics.py | ✅ 完成 |

## 核心内容

### Day 01: 类的基础与银行账户系统

#### 练习1：银行账户基础
- **概念**：创建基础的 `BankAccount` 类
- **关键方法**：
  - `__init__()`：初始化账户信息
  - `deposit()`：存款
  - `withdraw()`：取款
  - `get_balance()`：查询余额

#### 练习2：银行账户进阶
- **新增属性**：
  - `account_number`：自动生成的账户��（ACC + 6位数字）
  - `total_accounts`：类属性，记录账户总数
  - `transaction_history`：交易历史记录
- **新增方法**：
  - `show_history()`：显示交易历史
  - `transfer()`：转账功能

#### 练习3：信用卡账户（继承）
- **继承 BankAccount 类**
- **新增属性**：
  - `credit_limit`：信用额度
  - `current_debt`：当前欠款
- **方法重写**：
  - `withdraw()`：支持透支功能
- **新增方法**：
  - `pay_debt()`：还款
  - `show_credit_info()`：显示信用信息

#### 练习4：储蓄账户（继承）
- **继承 BankAccount 类**
- **新增属性**：
  - `interest_rate`：年利率
- **新增方法**：
  - `calculate_interest()`：计算利息
  - `add_interest()`：添加利息
- **方法重写**：
  - `deposit()`：大额存款有奖励

#### 练习5：银行管理系统
- **Bank 类**：统一管理所有账户
- **关键特性**：
  - 类属性 `accounts`：字典存储所有账户
  - `@classmethod`：开户、销户、查询
  - `@staticmethod`：计算银行总余额
- **核心功能**：
  - 多账户类型管理
  - 账户的创建与销毁
  - 统计功能

## 核心知识点

### 1. 类与对象
```python
class ClassName:
    def __init__(self, param):
        self.attribute = param
```

### 2. 类属性 vs 实例属性
- **类属性**：所有实例共享，在 class 下定义
- **实例属性**：每个实例独立，在 `__init__` 中定义
```class BankAccount:
    total_accounts = 0          # ← 类属性：所有账户共用这一个
```
    
```def __init__(self, owner, balance):
       self.owner = owner      # ← 实例属性：每个账户各有一份
       self.balance = balance  # ← 实例属性：每个账户各有一份
       BankAccount.total_accounts += 1  # 每次创建实例，计数器+1
```
### 3. 继承
```python
class ChildClass(ParentClass):
    def __init__(self, param):
        super().__init__(param)
```

### 4. 装饰器
- `@classmethod`：类方法，第一个参数是 `cls`
- `@staticmethod`：静态方法，不需要 `self` 或 `cls`

### 5. 方法重写（Polymorphism）
- 子类可以重写父类方法
- 使用 `super()` 调用父类方法

## 运行方式

```bash
# 运行整个文件
python day01-class-basics.py

# 或在Python交互环境中
python
>>> exec(open('day01-class-basics.py').read())
```

## 相关概念

| 概念 | 说明 |
|------|------|
| 封装 | 将数据和方法封装在类中 |
| 继承 | 子类继承父类的属性和方法 |
| 多态 | 同一方法在不同对象上表现不同 |
| 类属性 | 由类本身持有，所有实例共享 |
| 实例属性 | 由实例持有，每个实例各自独立 |

## 扩展思考

- 如何添加账户密码验证功能？
- 如何记录操作时间戳？
- 如何实现定期自动计息？
- 如何防止异常操作（如负数转账）？

## 下一步学习计划

- 📚 装饰器（Decorators）
- 📚 生成器（Generators）
- 📚 异常处理（Exception Handling）
- 📚 SQL复杂查询

---

*Last Updated: 2026.09.03*
