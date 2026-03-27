# 使用多阶段构建优化镜像大小
FROM beevelop/android:2022.04.1 AS builder

# 设置工作目录
WORKDIR /app

# 安装必要的工具
RUN apt-get update && apt-get install -y \
    python3-pip \
    git \
    zip \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# 安装Buildozer和项目依赖
RUN pip3 install buildozer

# 复制项目文件
COPY . .

# 安装Python依赖
RUN pip3 install -r requirements.txt

# 构建APK
RUN buildozer android debug

# 最终阶段 - 只包含APK文件
FROM alpine:3.16

WORKDIR /output

# 从构建阶段复制APK文件
COPY --from=builder /app/bin/*.apk ./

# 设置入口点
CMD ["ls", "-la", "./"]