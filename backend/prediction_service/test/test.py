import os

def run_main_py():
    # 打印当前工作目录，确保我们在正确的位置
    print(f"当前工作目录: {os.getcwd()}")
    
    # 指定 main.py 脚本的路径，这里假设它在当前工作目录
    script_path = './main.py'
    
    # 构建命令字符串
    command = f'python {script_path}'
    
    # 使用 os.system 执行命令
    status = os.system(command)
    
    # 检查命令执行状态
    if status == 0:
        print("Script executed successfully")
    else:
        print("Script execution failed")

# 调用函数
run_main_py()
