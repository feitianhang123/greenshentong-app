#!/bin/bash
# 绿申通持续部署脚本

set -e  # 遇到错误立即退出

echo "🚀 绿申通持续部署开始..."

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 日志函数
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# 检查Docker
check_docker() {
    if ! command -v docker &> /dev/null; then
        log_error "Docker未安装，请先安装Docker Desktop"
        exit 1
    fi
    
    if ! docker info &> /dev/null; then
        log_error "Docker守护进程未运行，请启动Docker"
        exit 1
    fi
    
    log_info "Docker检查通过"
}

# 清理旧构建
clean_previous() {
    log_info "清理旧构建文件..."
    docker-compose down --volumes --remove-orphans 2>/dev/null || true
    rm -rf bin/ *.log
    mkdir -p bin
}

# 构建Docker镜像
build_image() {
    log_info "构建Docker镜像..."
    docker build -t greenshentong-builder .
}

# 运行测试
run_tests() {
    log_info "运行应用测试..."
    
    # 启动开发服务器
    docker-compose up -d dev
    sleep 5
    
    # 测试应用是否正常
    if curl -f http://localhost:5000 > /dev/null 2>&1; then
        log_info "应用测试通过"
    else
        log_error "应用测试失败"
        docker-compose logs dev
        exit 1
    fi
    
    docker-compose down
}

# 构建APK
build_apk() {
    log_info "开始构建APK..."
    
    # 运行构建
    if docker-compose run --rm builder; then
        log_info "APK构建成功"
    else
        log_error "APK构建失败"
        docker-compose logs builder
        exit 1
    fi
}

# 提取APK文件
extract_apk() {
    log_info "提取APK文件..."
    
    if docker-compose run --rm apk-extractor; then
        # 检查APK文件
        if [ -n "$(ls -la bin/*.apk 2>/dev/null)" ]; then
            APK_FILE=$(ls bin/*.apk | head -1)
            log_info "APK文件: ${APK_FILE}"
            log_info "文件大小: $(du -h "${APK_FILE}" | cut -f1)"
        else
            log_error "未找到APK文件"
            exit 1
        fi
    else
        log_error "APK提取失败"
        exit 1
    fi
}

# 主函数
main() {
    log_info "=== 绿申通持续部署 ==="
    
    check_docker
    clean_previous
    build_image
    run_tests
    build_apk
    extract_apk
    
    log_info "✅ 部署完成！"
    log_info "📦 APK文件位置: bin/"
    log_info "📱 可以安装到手机进行测试"
    
    # 显示APK文件信息
    echo ""
    echo "生成的文件:"
    ls -la bin/*.apk 2>/dev/null || echo "未找到APK文件"
}

# 运行主函数
main "$@"