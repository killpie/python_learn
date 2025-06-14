def say_hello(name: str) -> str:
    """
    一个简单的问候函数
    
    Args:
        name (str): 要问候的人的名字
        
    Returns:
        str: 问候语
    """
    return f"你好，{name}！欢迎学习Python！"

if __name__ == "__main__":
    print(say_hello("初学者")) 