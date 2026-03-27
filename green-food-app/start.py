#!/usr/bin/env python3
"""
绿申通应用启动脚本
"""

import os
import sys
import subprocess

def start_application():
    """启动应用"""
    print("🌱 启动绿申通应用...")
    
    # 检查是否安装了依赖
    try:
        import flask
        print("✅ Flask 已安装")
    except ImportError:
        print("❌ Flask 未安装，正在安装...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
    
    # 启动应用
    try:
        print("🚀 启动服务器...")
        print("📱 主界面: http://127.0.0.1:5000")
        print("📊 模块一: http://127.0.0.1:5000/module1")
        print("📋 模块二: http://127.0.0.1:5000/module2") 
        print("📄 模块三: http://127.0.0.1:5000/module3")
        print("\n⏹️  按 Ctrl+C 停止服务器")
        
        # 启动主程序
        subprocess.check_call([sys.executable, "main.py"])
        
    except KeyboardInterrupt:
        print("\n🛑 服务器已停止")
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        return False
    
    return True

if __name__ == "__main__":
    start_application()