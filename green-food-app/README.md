# 🌱 绿申通 - Docker持续部署

## 📦 快速开始

### 方式一：一键部署（推荐）
```bash
# 运行完整部署流程
./deploy.sh
```

### 方式二：分步部署
```bash
# 1. 构建Docker镜像
docker build -t greenshentong-builder .

# 2. 测试应用
docker run --rm -p 5000:5000 greenshentong-builder python main.py
# 访问 http://localhost:5000 测试

# 3. 构建APK
docker run --rm -v "$(pwd)/bin:/app/bin" greenshentong-builder buildozer android debug

# 4. 获取APK
ls -la bin/
```

### 方式三：使用Docker Compose
```bash
# 开发模式
docker-compose up dev

# 构建模式
docker-compose run --rm builder

# 仅提取APK
docker-compose run --rm apk-extractor
```

## 🐳 Docker命令参考

### 构建镜像
```bash
docker build -t greenshentong-builder .
```

### 运行测试
```bash
docker run --rm greenshentong-builder python -m pytest tests/ -v
```

### 构建APK
```bash
docker run --rm -v "$(pwd)/bin:/app/bin" greenshentong-builder buildozer android debug
```

### 交互式调试
```bash
docker run -it --rm -v "$(pwd):/app" greenshentong-builder /bin/bash
```

## 📁 项目结构

```
green-food-app/
├── main.py                 # 主应用（整合所有模块）
├── Dockerfile              # Docker多阶段构建配置
├── docker-compose.yml      # Docker Compose配置
├── deploy.sh               # 自动部署脚本
├── requirements.txt        # Python依赖
├── buildozer.spec          # Buildozer配置
├── tests/                  # 测试文件
│   └── test_basic.py       # 基础测试
├── assets/                 # 资源文件
│   └── icon.png           # 应用图标
├── bin/                    # 输出目录（APK文件）
└── .github/workflows/      # GitHub Actions配置
    └── build.yml           # 持续集成配置
```

## ⚙️ 配置说明

### Buildozer配置 (buildozer.spec)
- 应用名称：绿申通
- 包名：org.greenshentong
- 目标API：Android 5.0+
- 权限：INTERNET

### Docker配置
- 多阶段构建优化镜像大小
- 使用官方Android构建环境
- 自动缓存依赖加速构建

## 🚀 部署流程

1. **环境检查** - 验证Docker和环境
2. **清理构建** - 删除旧文件
3. **构建镜像** - 创建Docker构建环境
4. **运行测试** - 验证应用功能
5. **构建APK** - 生成Android包
6. **提取结果** - 获取APK文件

## 📊 输出结果

构建成功后，在 `bin/` 目录生成：
- `greenshentong-1.0-debug.apk` - 调试版APK
- `greenshentong-1.0-release.apk` - 发布版APK

## 🔧 故障排除

### 常见问题

1. **Docker权限问题**
   ```bash
   sudo usermod -aG docker $USER
   ```

2. **构建失败**
   - 检查网络连接
   - 查看详细日志：`docker-compose logs builder`

3. **APK无法安装**
   - 检查Android版本兼容性
   - 验证签名配置

### 查看日志
```bash
# 查看构建日志
docker-compose logs builder

# 详细构建日志
buildozer -v android debug
```

## 📞 支持

如果遇到问题：
1. 检查Docker是否正常运行
2. 查看详细错误日志
3. 确保磁盘空间充足

## 📜 许可证

MIT License

---

💡 **提示**：首次构建可能需要较长时间下载Android SDK组件，后续构建会利用缓存加速。