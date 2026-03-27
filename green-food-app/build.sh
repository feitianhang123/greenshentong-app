#!/bin/bash
# 绿申通 Docker 打包脚本

echo "🚀 开始使用Docker打包绿申通APK..."

# 检查Docker是否安装
if ! command -v docker &> /dev/null; then
    echo "❌ Docker未安装，请先安装Docker Desktop"
    exit 1
fi

# 构建Docker镜像
echo "📦 构建Docker镜像..."
docker build -t greenshentong-builder .

# 运行打包
echo "🔨 开始打包APK..."
docker run -v "$(pwd):/app" greenshentong-builder

# 检查是否生成APK
if [ -f "bin/*.apk" ]; then
    echo "✅ 打包成功！APK文件在 bin/ 目录下"
    ls -la bin/
else
    echo "❌ 打包失败，请检查错误信息"
    exit 1
fi