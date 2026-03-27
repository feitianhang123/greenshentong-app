# 📦 绿申通 APK 打包指南

## 🎯 打包方案选择

### 方案一：使用 Linux 环境打包（推荐）
由于Buildozer在Windows上支持有限，建议在Linux环境中打包：

#### 在 Ubuntu 中打包步骤：
```bash
# 1. 安装依赖
sudo apt update
sudo apt install -y python3-pip git zip

# 2. 安装Buildozer
pip3 install buildozer

# 3. 安装Android SDK依赖
sudo apt install -y android-sdk

# 4. 进入项目目录
cd green-food-app

# 5. 初始化Buildozer（如果还没有buildozer.spec）
buildozer init

# 6. 打包APK
buildozer android debug
```

### 方案二：使用 Google Colab 在线打包
1. 上传 `green-food-app` 文件夹到Google Drive
2. 在Colab中运行打包脚本
3. 下载生成的APK文件

### 方案三：使用第三方打包服务
- **Python-for-Android**: 在线打包服务
- **BeeWare**: 跨平台Python应用打包
- **Kivy Launcher**: 在手机上直接运行Python代码

## 📋 项目文件说明

### 现有文件结构：
```
green-food-app/
├── main.py              # 主程序（整合所有模块）
├── buildozer.spec       # Buildozer配置文件
├── requirements.txt     # Python依赖
└── assets/
    └── icon.png         # APP图标
```

### buildozer.spec 关键配置：
```ini
[app]
title = 绿申通
package.name = greenshentong
package.domain = org.greenshentong
requirements = python3,flask,pandas,openpyxl,requests
orientation = portrait
icon.filename = %(source.dir)s/assets/icon.png
android.permissions = INTERNET
```

## 🚀 快速开始

### 1. 环境准备（Linux）
```bash
# 克隆项目
git clone <your-repo>
cd green-food-app

# 安装依赖
pip install -r requirements.txt

# 测试应用
python main.py
```

### 2. 打包APK
```bash
# 确保在Linux环境
buildozer android debug

# 生成的APK文件位置
# bin/greenshentong-1.0-debug.apk
```

### 3. 安装测试
```bash
# 安装到连接的Android设备
buildozer android deploy

# 或者手动安装APK
adb install bin/greenshentong-1.0-debug.apk
```

## 🔧 故障排除

### 常见问题：
1. **Buildozer在Windows报错**：建议使用WSL或Linux虚拟机
2. **Android SDK问题**：确保安装了正确的Android SDK版本
3. **依赖冲突**：检查requirements.txt中的版本兼容性

### 资源需求：
- Android SDK API 28+
- Python 3.8+
- 至少4GB空闲内存

## 📱 手机端测试

### 安装后测试：
1. 允许应用访问互联网权限
2. 打开应用检查主界面显示
3. 测试各个模块的导航功能
4. 验证数据加载和搜索功能

### 预期行为：
- ✅ 主界面显示四个模块卡片
- ✅ 点击模块可以正常跳转
- ✅ 各模块功能完整可用
- ✅ 界面适配移动端屏幕

## 📞 支持信息

如果遇到打包问题：
1. 检查Buildozer日志：`buildozer.spec` 中的 `log_dir`
2. 查看详细错误：`buildozer -v android debug`
3. 确保所有文件路径正确

## ⚡ 替代方案

如果无法完成本地打包，可以考虑：

### Web应用部署：
```bash
# 部署到PythonAnywhere或Heroku
pip install gunicorn
# 配置Procfile和运行时
```

### 混合应用：
- 使用WebView封装现有Web界面
- 使用React Native重写前端
- 使用Flutter开发跨平台应用

---

💡 **建议**：对于快速测试，可以先将Web应用部署到服务器，然后在手机浏览器中测试功能。确认功能完整后再进行APK打包。