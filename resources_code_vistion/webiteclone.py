
def website_clone():
    def options():
        print("""
    1:Html5 webisite clone
    2:python3 website clone
        """)
        return True
    
    def clone():
        option = input ("Setool-Master~/Main Console~/website_clone//")
        if option == "1":
            print("[*]Html5 website clone")
            url = input("Enter Url To Clone:")
            #del the index.html in this place
            def rm():
                import os
                if os.name == "posix": #linux
                    os.system("rm -f index.html")
                    return True
                if os.name == "nt" : #windows
                    os.system("del /s /f index.html")
                    return True
                else:
                    print("[*]Unknow system!")
                    return False
            rm()

            with open("index.html" , "a") as f:
                f.write("<link href='iframe.css' rel='stylesheet' />")
                f.write("<iframe class='iframe' src='"+url+"'"+"></iframe>")
            f.close()
            def portstart():
                import os
                if os.name == "posix":
                    #linux
                    os.system("python3 -m http.server 8080")
                    return True
                if os.name == "nt":
                    #windows
                    os.system("python -m http.server 8080")
                    return True
                else:
                    print("[*]Do not start a port on your system!")
                    return False
            portstart()
            clone()

            return True

        if option == "2":
            print("[*]python3 website clone")
            def pyclone():
                import requests
                url = input ("Enter CLone Url:")
                re = requests.get(url)
                print(type(re)) 
                re.encoding = 'utf-8'
                print(re.text)
                with open("index.html" , "w") as f:
                    f.write(re.text)
                f.close()
                def osname():
                    import os
                    if os.name == "posix": #linux
                        import os
                        os.system("python3 -m http.server 8080")
                        return True
                    if os.name == "nt": #windows
                        import os
                        os.system("python -m http.server 8080")
                        return True
                    else:
                        print("[*]Unknow System!")
                        return False
                osname()
            
            pyclone()
            clone()
            return True

        if option == "exit":
            import setool as setool
            setool.main()
            return True
        
        if option == "show options": #show all clone method
            options()
            clone()
            return True

        else:
            clone()
            return False

    clone()