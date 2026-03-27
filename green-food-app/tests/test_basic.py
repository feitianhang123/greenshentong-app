#!/usr/bin/env python3
"""
绿申通基础测试
"""

import unittest
import sys
import os

# 添加项目根目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class TestBasicFunctionality(unittest.TestCase):
    """基础功能测试"""
    
    def test_import_main(self):
        """测试主模块是否可以导入"""
        try:
            from main import app
            self.assertIsNotNone(app)
            print("✅ 主模块导入成功")
        except ImportError as e:
            self.fail(f"主模块导入失败: {e}")
    
    def test_flask_app_creation(self):
        """测试Flask应用创建"""
        from main import app
        
        self.assertEqual(app.name, 'main')
        self.assertTrue(hasattr(app, 'route'))
        print("✅ Flask应用创建成功")
    
    def test_module_routes(self):
        """测试模块路由"""
        from main import app
        
        # 检查路由是否注册
        routes = []
        for rule in app.url_map.iter_rules():
            routes.append(str(rule))
        
        expected_routes = ['/', '/module1', '/module2', '/module3']
        for route in expected_routes:
            self.assertIn(route, routes)
            print(f"✅ 路由 {route} 注册成功")

def test_requirements():
    """测试依赖是否满足"""
    try:
        import flask
        import pandas
        import openpyxl
        import requests
        print("✅ 所有依赖包可用")
        return True
    except ImportError as e:
        print(f"❌ 依赖包缺失: {e}")
        return False

if __name__ == '__main__':
    # 运行测试
    print("🚀 运行绿申通基础测试...")
    
    # 测试依赖
    if not test_requirements():
        sys.exit(1)
    
    # 运行单元测试
    unittest.main(verbosity=2)