
def attack():

    print("[*]Enter 'exit' to exit")
    print("[*]Enter 'show options' show all the project")
    
    def main_attack():
        options = input("Setool-Master~/Main Console~/Web_Page_Attack//")
        if options == "show options":
            def show_options():
                print("""
    1:pop-up window_1
    2:pop-up window_2
                """)
            show_options()
            main_attack()
            return True
        if options == "exit":
            import setool
            setool.main()
            return True
        if options == "1":
            def pop_up_1():
                import os
                if os.name == "posix":
                    #linux
                    os.system("cp webpage_attack/index_1/index.html ./")
                    os.system("python3 -m http.server 8080")
                    main_attack()
                    return True
                if os.name == "nt":
                    os.system("copy webpage_attack/index_1/index.html ./")
                    os.system("python -m http.server 8080")
                    main_attack()
                    return True
                else:
                    print("[!]Unknow Optioning system")
                    return False
                return True
            pop_up_1()
        if options == "2":
            def pop_up_2():
                import os
                if os.name == "posix":
                    #linux
                    os.system("cp webpage_attack/index_2/index.html ./")
                    os.system("python3 -m http.server 8080")
                    main_attack()
                    return True
                if os.name == "nt":
                    os.system("copy webpage_attack/index_2/index.html ./")
                    os.system("python -m http.server 8080")
                    main_attack()
                    return True
                else:
                    print("[!]Unknow Optioning system")
                    return False
                return True
            pop_up_2()
        else:
            main_attack()
            return False
    main_attack()