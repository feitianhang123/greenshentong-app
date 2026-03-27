#!/usr/bin/env python3
"""
绿申通 - 绿色食品申报通系统
主程序入口，整合所有模块功能
"""

import os
import sys
import threading
from flask import Flask, render_template_string, request, jsonify
import pandas as pd

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 创建主应用
app = Flask(__name__)

# ==================== 模块一：产品目录 ====================

def load_product_catalog():
    """加载产品目录数据"""
    try:
        # 这里应该加载Excel文件，暂时使用模拟数据
        products = [
            {"category": "蔬菜类", "product": "西红柿", "standard": "NY/T 1045-2021"},
            {"category": "水果类", "product": "苹果", "standard": "NY/T 1046-2021"},
            {"category": "粮油类", "product": "大米", "standard": "NY/T 1047-2021"}
        ]
        return products
    except Exception as e:
        print(f"加载产品目录错误: {e}")
        return []

@app.route('/module1')
def module1_index():
    """模块一：产品目录"""
    products = load_product_catalog()
    
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>产品目录 - 绿申通</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }
            .header { background: linear-gradient(135deg, #4CAF50, #66BB6A); color: white; padding: 20px; text-align: center; }
            .back-btn { color: white; text-decoration: none; font-weight: bold; }
            .product-card { background: white; margin: 10px; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>绿色食品申报目录</h1>
            <p>绿色食品产品适用标准目录（2023版）</p>
            <a href="/" class="back-btn">← 返回主界面</a>
        </div>
        
        <div style="padding: 20px;">
            <h2>产品类别列表</h2>
            {% for product in products %}
            <div class="product-card">
                <h3>{{ product.category }} - {{ product.product }}</h3>
                <p>标准: {{ product.standard }}</p>
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    '''
    
    return render_template_string(html_template, products=products)

# ==================== 模块二：现行标准库 ====================

def load_standards():
    """加载标准数据"""
    standards = [
        {"name": "绿色食品 啤酒", "code": "NY/T 273-2021", "downloadUrl": "#"},
        {"name": "绿色食品 葡萄酒", "code": "NY/T 274-2023", "downloadUrl": "#"},
        {"name": "绿色食品 茶叶", "code": "NY/T 288-2018", "downloadUrl": "#"}
    ]
    return standards

@app.route('/module2')
def module2_index():
    """模块二：现行标准库"""
    standards = load_standards()
    
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>现行标准库 - 绿申通</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }
            .header { background: linear-gradient(135deg, #4CAF50, #66BB6A); color: white; padding: 20px; text-align: center; }
            .back-btn { color: white; text-decoration: none; font-weight: bold; }
            .standard-card { background: white; margin: 10px; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>现行标准库</h1>
            <p>智能搜索系统</p>
            <a href="/" class="back-btn">← 返回主界面</a>
        </div>
        
        <div style="padding: 20px;">
            <div class="stats">总共 143 个标准 | 现行产品标准: 129 个 | 现行准则标准: 14 个</div>
            
            {% for standard in standards %}
            <div class="standard-card">
                <h3>{{ standard.name }}</h3>
                <p>标准号: {{ standard.code }}</p>
                <a href="{{ standard.downloadUrl }}" download>📥 下载标准</a>
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    '''
    
    return render_template_string(html_template, standards=standards)

# ==================== 模块三：材料清单 ====================

MATERIALS_DATA = [
    {
        "code": "CGFDC-SQ-08/2025", 
        "name": "种植产品申请材料清单",
        "downloadUrl": "#",
        "surveyUrl": "#"
    },
    {
        "code": "CGFDC-SQ-09/2025", 
        "name": "畜禽产品申请材料清单",
        "downloadUrl": "#", 
        "surveyUrl": "#"
    }
]

@app.route('/module3')
def module3_index():
    """模块三：材料清单"""
    
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>材料清单 - 绿申通</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: #f5f5f5; }
            .header { background: linear-gradient(135deg, #4CAF50,极66BB6A); color: white; padding: 20px; text-align: center; }
            .back-btn { color: white; text-decoration: none; font-weight: bold; }
            .material-card { background: white; margin: 10px; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>材料清单系统</h1>
            <p>6类申报材料清单</p>
            <a href="/" class="back-btn">← 返回主界面</a>
        </div>
        
        <div style="padding: 20px;">
            <div class="stats">总共 6 个材料清单</div>
            
            {% for material in materials %}
            <div class="material-card">
                <h3>{{ material.name }}</h3>
                <p>代码: {{ material.code }}</p>
                <a href="{{ material.downloadUrl }}" download>📥 下载文档</a>
            </div>
            {% endfor %}
        </div>
    </body>
    </html>
    '''
    
    return render_template_string(html_template, materials=MATERIALS_DATA)

# ==================== 主界面 ====================

@app.route('/')
def main_index():
    """主界面"""
    
    html_template = '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>绿申通 - 绿色食品申报通系统</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                margin: 0; 
                padding: 20px; 
                background: linear-gradient(135deg, #E8F5E8 0%, #C8E6C9 100%);
                min-height: 100vh;
            }
            .container { max-width: 800px; margin: 0 auto; }
            .header { 
                background: linear-gradient(135deg, #4CAF50, #66BB6A); 
                color: white; 
                padding: 30px; 
                text-align: center; 
                border-radius: 15px;
                margin-bottom: 30px;
                box-shadow: 0 4px 15px rgba(76, 175, 80, 0.3);
            }
            .modules-grid { 
                display: grid; 
                grid-template-columns: 1fr; 
                gap: 20px; 
            }
            .module-card { 
                background: white; 
                padding: 25px; 
                border-radius: 12px; 
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
                text-align: center;
                cursor: pointer;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
                border-left: 5px solid #4CAF50;
            }
            .module-card:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            }
            .module-title { 
                color: #2E7D32; 
                font-size: 1.4em; 
                margin-bottom: 10px; 
                font-weight: bold;
            }
            .module-desc { 
                color: #666; 
                font-size: 0.95em; 
                margin-bottom: 15px;
            }
            .coming-soon { 
                opacity: 0.6; 
                background: #f0f0f0;
                border-left: 5px solid #9E9E9E;
            }
            .footer { 
                text-align: center; 
                margin-top: 40px; 
                color: #666; 
                font-size: 0.9em;
                padding: 20px;
                border-top: 1px solid #E0E0E0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🌱 绿申通</h1>
                <p>绿色食品申报通系统</p>
            </div>

            <div class="modules-grid">
                <!-- 产品目录 -->
                <div class="module-card" onclick="window.location.href='/module1'">
                    <div class="module-title">产品目录</div>
                    <div class="module-desc">查看绿色食品适用标准目录</div>
                </div>
                
                <!-- 现行标准 -->
                <div class="module-card" onclick="window.location.href='/module2'">
                    <div class="module-title">现行标准</div>
                    <div class="module-desc">产品类及准则类标准查询</div>
                </div>
                
                <!-- 材料清单 -->
                <div class="module-card" onclick="window.location.href='/module3'">
                    <div class="module-title">材料清单</div>
                    <div class="module-desc">6类申报材料清单</div>
                </div>
                
                <!-- 预审核 -->
                <div class="module-card coming-soon">
                    <div class="module-title">预审核</div>
                    <div class="module-desc">敬请期待</div>
                </div>
            </div>

            <div class="footer">
                <p>本软件内容均来源于中国绿色食品发展中心官网，如果存在问题请联络：QQ:10780329</p>
            </div>
        </div>

        <script>
            // 确保点击事件在移动端正常工作
            document.querySelectorAll('.module-card').forEach(card => {
                card.addEventListener('click', function() {
                    if (!this.classList.contains('coming-soon')) {
                        window.location.href = this.getAttribute('onclick').split("'")[1];
                    }
                });
            });
        </script>
    </body>
    </html>
    '''
    
    return render_template_string(html_template)

# ==================== 启动应用 ====================

if __name__ == '__main__':
    print("启动绿申通系统...")
    print("主界面: http://127.0.0.1:5000")
    print("模块一: http://127.0.0.1:5000/module1")
    print("模块二: http://127.0.0.1:5000/module2")
    print("📄 模块三: http://127.0.0.1:5000/module3")
    
    # 在移动端使用 0.0.0.0 以便外部访问
    app.run(host='0.0.0.0', port=5000, debug=False)