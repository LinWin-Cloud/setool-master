
def py_tools():
    import os
    print("[*]Enter 'exit' to exit")
    print("[*]Enter 'show options' to show all project")

    def py_tools_options():     #show all project for the pt_tools payload
        print("""
    1:Requests To Website               enter:1
    2:Get Web page 's resouces code     enter:2
    3:Get Website status code           enter:3
    4:Get webpage information           enter:4
    5:Whois                             enter:5
        """)
        return True

    def main_py_tools():

        options = input("Setool-Master~/Main Console~/py_tools//")
        headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }

        if options == "show options":   #show all project for the py_tools
            py_tools_options()
            main_py_tools()
            return True
        
        if options == "exit":
            import setool as setool
            setool.main()
            return True

        if options == "1":
            #Requests To Website 
            def Requests_web_site():
                import requests 
                url = input("Enter URL:")
                try:
                    geturl = requests.get(url)
                    print("Get The Requests:"+url)
                    if geturl.status_code == 200:
                        headers = {
                            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
                        }
                        print("")
                        print("     Send Get requests to "+url)
                        print("     Reture : true")
                        print("")
                        return True
                    else: #if the function running error than run this function
                        geturl = requests.get(url)
                        print("")
                        print("     [!]Error status code")
                        print("     Send Get requests to "+url)
                        print("     [!]Status Code:"+geturl.status_code)
                        print("")
                        return False
                except:
                    print("[!]Error Running")
                    return False
            Requests_web_site()
            main_py_tools() #retrue to the main function
            return True
        if options == "2":
            #get web page resouces code
            def get_webpage_resouces_code():
                import requests
                url = input("Enter URL:")
                if url == "exit":
                    main_py_tools()
                    return True
                else:
                    getcode = requests.get(url)
                    print("Get Web Page:"+url)
                    print("")
                    getcode.encoding = "utf8"
                    print(getcode.text) 
                    print("")
                    chose = input("[?]Do you want to write to a file[Y or N]:")
                    if chose == "Y" or chose == "y":
                        with open("file" , "w") as f:
                            f.write(getcode.text)
                        f.close()
                        print("[*]wirte the file true")
                        return True
                    if chose == "N" or chose == "n":
                        print("Exit The Optioning")
                        return False
                return True
            get_webpage_resouces_code()
            main_py_tools()

        if options == "3":
            def get_webpage_code():
                try:
                    import requests 
                    headers = {
                         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
                    }
                    import requests as requests   #import requests payload
                    url = input("Enter URL:")
                    print("[*]Get status code form "+url)
                    geturl = requests.get(url)
                    print("The Status Code:")
                    print(geturl.status_code)
                    print("")
                    return True
                except:
                    print("[!]Error Running")
                    return False
            get_webpage_code()
            main_py_tools()
            return True
        if options == "4":
            def get_webpage_info():
                import os
                import requests
                try:
                    url = input("Enter URL:")
                    geturl = requests.get(url)
                    import urllib
                    print("")
                    print("URL:"+url)
                    print("Server Info:"+geturl.headers)
                    print("")
                    return True
                except:
                    print("[!]Error Running")
                    return False

            get_webpage_info()
            main_py_tools()
            return True
        if options == "5":
            #whois
            try:
                import whois
                url = input("Enter URL:")
                print("==================================")
                print(whois.whois(url))
                print("==================================")
                main_py_tools()
                return
            except: 
                print("[!]Error Runnning")
                main_py_tools()
                return False
            return True

        else:
            main_py_tools()  #reture to main function
            return False
            
    main_py_tools()
        