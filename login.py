def login():
    # 预设的正确凭证（实际应用中不应明文存储密码！）
    CORRECT_USERNAME = "admin"
    CORRECT_PASSWORD = "123456"  # 仅为演示，生产环境必须加密存储

    print("=== 简易登录系统 ===")
    
    # 获取用户输入
    username = input("请输入用户名: ").strip()
    password = input("请输入密码: ").strip()
    
    # 验证逻辑
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print("\n✅ 登录成功！欢迎使用系统。")
        return True
    else:
        print("\n❌ 用户名或密码错误，请重试。")
        return False

# 程序入口
if __name__ == "__main__":
    login()