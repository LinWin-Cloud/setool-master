

def web_gp():
    print("[*]Enter 'exit' to exit")
    print("[*]Enter 'show options' show all project")

    def main():
        def projects():
            print("""
    1:Web Page Global Positioning   enter:1
            """)
            return True
        Options = input("Setool-Master~/Main Console~/Web_GP//")
        if Options == "show options":
            projects()
            main()
            return True
        if Options == "exit":
            #qiut to the main console
            import setool as setool
            setool.main()
            return True
        if Options == "1":
            #start to attack
            print("""
    1:Baidu Network Disk       enter:1
            """)
            import os
            if os.name == 'nt':
                os.system("del /f index.html")
                os.system("del /f index.js")
                os.system("copy GPS/index.html ./")
                os.system("python -m http.server 8080")
                main()
                return True
            if os.name == "posix":
                os.system("rm -f index.html")
                os.system("rm -f index.js")
                os.system("cp GPS/index.html ./")
                os.system("python3 -m http.server 8080")
                main()
                return True
            else:
                print("[!]Unknow Optioning System")
                main()
                return False
        else:
            main()
            return False
    main()