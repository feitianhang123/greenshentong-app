#!/usr/bin/env python3
"""
绿申通应用测试脚本
用于验证应用功能是否正常
"""

import requests
import time
import sys

def test_application():
    """测试应用功能"""
    print("🚀 开始测试绿申通应用...")
    
    base_url = "http://127.0.0.1:5000"
    
    # 等待应用启动
    print("⏳ 等待应用启动...")
    time.sleep(2)
    
    # 测试主界面
    try:
        response = requests.get(base_url, timeout=10)
        if response.status_code == 200:
            print("✅ 主界面: 正常")
        else:
            print(f"❌ 主界面: 错误 {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ 主界面: 连接失败 - {e}")
        return False
    
    # 测试模块一
    try:
        response = requests.get(f"{base_url}/module1", timeout=10)
        if response.status_code == 200:
            print("✅ 模块一(产品目录): 正常")
        else:
            print(f"❌ 模块一: 错误 {response.status_code}")
    except Exception as e:
        print(f"❌ 模块一: 连接失败 - {e}")
    
    # 测试模块二
    try:
        response = requests.get(f"{base_url}/module2", timeout=10)
        if response.status_code == 200:
            print("✅ 模块二(现行标准): 正常")
        else:
            print(f"❌ 模块二: 错误 {response.status_code}")
    except Exception as e:
        print(f"❌ 模块二: 连接失败 - {e}")
    
    # 测试模块三
    try:
        response = requests.get(f"{base_url}/module3", timeout=10)
        if response.status_code == 200:
            print("✅ 模块三(材料清单): 正常")
        else:
            print(f"❌ 模块三: 错误 {response.status_code}")
    except Exception as e:
        print(f"❌ 模块三: 连接失败 - {e}")
    
    print("\n🎉 测试完成！")
    print("📋 下一步:")
    print("1. 确保所有功能正常")
    print("2. 在Linux环境中运行 buildozer android debug")
    print("3. 安装生成的APK文件进行测试")
    
    return True

if __name__ == "__main__":
    # 首先启动应用
    print("🌱 启动绿申通应用...")
    
    # 这里可以添加自动启动应用的代码
    # 或者手动启动: python main.py
    
    input("请先手动运行: python main.py ，然后按回车键开始测试...")
    
    test_application()