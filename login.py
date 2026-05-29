def login():
    # 预设的正确凭证（实际应用中不应明文存储密码！）
    CORRECT_USERNAME = "admin"
    CORRECT_PASSWORD = "123456"  # 仅为演示，生产环境必须加密存储；后天完成
    
    max_attempts = 3 #登录次数限制
    attempts = 0

    print("=== 简易登录系统 ===")
    
    # 这里用 while True 配合 break 来实现
    while True:
        if attempts >= max_attempts:
            print("\n⚠️ 失败次数过多，程序强制退出！")
            break

    	# 获取用户输入
    	username = input("请输入用户名: ").strip()
    	password = input("请输入密码: ").strip()
    
    	# 验证逻辑
    	if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        	print("\n✅ 登录成功！欢迎使用系统。")
        	#return True
		break#登录成功就可以跳过剩余的循环
    else:
		attempts+=1
		print("\n❌ 用户名或密码错误，请重试。")
        	#return False

# 程序入口
if __name__ == "__main__":
    login()