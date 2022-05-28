

def projects():
    print("""
    1:Web Page (Use API get IP adress)
    """)

def main_get_ip():
    print("[*]Enter 'exit' to exit")
    print("[*]Enter 'show options' to show all project")
    def main():
        options = input("Setool-Master~/Main Console~/Web_IP//")
        if options == "show options":
            projects()
            main()
            return True
        if options == "exit":
            import setool
            setool.main()
            return True
        if options == "1":
            #get ip
            import os
            if os.name == "posix":
                #linux
                os.system("rm -f index.html")
                os.system("cp web_ip/index.html ./")
                print("[!]You can Search on Internet.")
                os.system("python3 -m http.server 8080")
                main()
                return True
            import os

            if os.name == "nt":
                #windows
                import os
                os.system("del /f index.html")
                os.system("copy web_ip/index.html ./")
                print("[!]You can Search on Internet.")
                os.system("python -m http.server 8080")
                main()
                return True
            else:
                print("[!]Unknow Optioning System")
                return False

        else:
            main()
            return False
    main()