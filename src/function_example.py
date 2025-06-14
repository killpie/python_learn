# 最简单的函数定义
def simple_function():
    print("这是一个没有参数的函数")

# 带参数的函数
def greet(name):
    print(f"你好，{name}")

# 带类型提示的函数
def add_numbers(a: int, b: int) -> int:
    return a + b

# 带默认参数的函数
def greet_with_time(name: str, time: str = "早上") -> str:
    return f"{time}好，{name}"

# 测试这些函数
if __name__ == "__main__":
    # 调用简单函数
    simple_function()
    
    # 调用带参数的函数
    greet("小明")
    
    # 调用带类型提示的函数
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")
    
    # 调用带默认参数的函数
    print(greet_with_time("小红"))  # 使用默认的time参数
    print(greet_with_time("小红", "下午"))  # 指定time参数 