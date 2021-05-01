# -*- encoding: utf-8 -*-
import os
import subprocess
from concurrent.futures import ProcessPoolExecutor


def m0():
    '''os.system()是最简单直接的方法，它可以执行一个命令并将其输出显示在标准输出上。
    避免使用os.system()：因为它不提供任何方式来捕获命令的输出或检查其返回状态。此外，它容易被注入攻击（例如，通过构造恶意的命令行参数）。'''
    os.system('ls')  # 在Unix/Linux系统上列出目录内容
    os.system('ls -al')  # 在Windows系统上列出目录内容


def m1():
    '''os.popen()提供了一个文件对象，你可以像读取文件一样读取命令的输出。'''
    with os.popen("ls -l") as pipe:
        lines = pipe.readlines()
        for line in lines:
            print(line, end="")


def m2():
    '''subprocess.Popen()允许更细粒度的控制，例如异步执行命令。它返回一个Popen对象，你可以用它来读取输出、等待进程结束等。'''
    process = subprocess.Popen(['ls', '-l'], cwd='~/abc', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    print(stdout)


def m3():
    '''subprocess.run()是推荐的方法，因为它提供了更多的控制和灵活性。例如，你可以捕获命令的输出，设置超时时间，或者改变工作目录等。
    使用subprocess.run()：因为它既安全又灵活，特别是通过capture_output=True可以安全地捕获输出。对于需要更高级功能的情况，如需要更细粒度的控制，可以使用subprocess.Popen()。
    避免直接在命令中插入变量：如果需要在命令中包含变量，应该使用列表的方式来构建命令（如subprocess.run(['ls', '-l', directory_name])），而不是字符串格式化（这可能会引入安全漏洞）。'''
    # 捕获输出
    # result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
    # print(result.stdout)

    # 捕获输出并检查执行状态
    completed = subprocess.run(['ls', '-l'], capture_output=True, text=True)
    # print(completed.stdout)
    if completed.returncode == 0:
        print("命令执行成功")
    else:
        print("命令执行失败")


def run_cmd(command: str, cwd: str=None) -> str:
    cmd_list = command.split()
    completed = subprocess.run(cmd_list, cwd=cwd, capture_output=True, text=True)
    print(completed.stdout)
    if completed.returncode == 0:
        print("命令执行成功:", command)
    else:
        print("命令执行失败:", command)
    return completed.stdout

# def run_cmds(commands: list, cwd: str=None) -> list[str]:
#     output = []
#     for command in commands:
#         cmd_list = command.split()
#         completed = subprocess.run(cmd_list, cwd=cwd, capture_output=True, text=True)
#


def ppp():
    # 创建子进程列表
    processes = [subprocess.Popen(['command1', 'arg1'], cwd=""), subprocess.Popen(['command2', 'arg2'])]

    # 等待所有子进程完成
    for process in processes:
        process.wait()

    print("所有子进程已完成")

def _run_command(cmd):
    return subprocess.run(cmd, cwd=r"/Users/cosmos/okj/资料2-x", text=True, capture_output=True)

def safe_run_cmds(commands: list[str], cwd: str=None):
    # for command in commands:

    # 命令列表
    # commands = [['command1', 'arg1'], ['command2', 'arg2']]

    # 使用ProcessPoolExecutor运行命令
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(_run_command, cmd.split()) for cmd in commands]
        for future in futures:
            # 等待每个进程完成并获取结果（可选）
            result = future.result()
            print(result.stdout)  # 打印每个命令的输出

    print("所有子进程已完成")





if __name__ == '__main__':
    # m0()
    # m1()
    # m2()
    # m3()
    output = run_cmd("ls -l")
    print(output)
