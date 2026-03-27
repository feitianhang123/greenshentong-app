#!/bin/bash
# Ubuntu虚拟机环境设置脚本

echo "🔄 设置Ubuntu打包环境..."

# 更新系统
sudo apt update
sudo apt upgrade -y

# 安装必要工具
sudo apt install -y \
    python3-pip \
    git \
    zip \
    unzip \
    openjdk-11-jdk \
    android-sdk

# 安装Buildozer
pip3 install buildozer

# 配置Android SDK
export ANDROID_SDK_ROOT="/usr/lib/android-sdk"
export PATH="$PATH:$ANDROID_SDK_ROOT/tools:$ANDROID_SDK_ROOT/platform-tools"

# 创建项目目录
mkdir -p ~/projects
echo "✅ 环境设置完成！"
echo "📁 项目目录: ~/projects"
echo "🔧 现在可以开始打包: buildozer android debug"