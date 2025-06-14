# 定义一个简单的函数
def calculate_sum(a, b):
    return a + b

# 这个print语句会在文件被导入时执行
print("这个文件被导入了！")

# 这个代码块只会在文件直接运行时执行
if __name__ == "__main__":
    print("这个文件是作为主程序运行的！")
    result = calculate_sum(5, 3)
    print(f"5 + 3 = {result}") 