import wzz_模块
while True:
    wzz_模块.show_menu()
    action_str = input("选择希望执行的操作：")
    print("你要选择的操作是(%s)" % action_str)
    if action_str in ["1","2","3"]:
        if action_str == "1":
            wzz_模块.phone_str()
        elif action_str == "2":
            wzz_模块.show_all()
        elif action_str == "3":
            wzz_模块.search_card()
