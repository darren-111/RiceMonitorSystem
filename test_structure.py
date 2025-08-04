import os

required_dirs = [
    'core', 'core/models', 'core/models/weights',
    'data', 'data/datasets', 'data/samples', 'data/labels',
    'utils', 'config', 'tests', 'docs'
]

# 自动创建缺失目录
for dir_path in required_dirs:
    os.makedirs(dir_path, exist_ok=True)  # exist_ok=True 表示如果目录已存在不会报错
    print(f"Checked/created: {dir_path}")

print(" 所有目录结构验证通过！")
