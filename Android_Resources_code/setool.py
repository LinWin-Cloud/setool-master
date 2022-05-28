
#LinWin-Cloud 
#auther : linwin-cloud
#setool-master


def main():
    print("")
    options = input("Setool-Master~/Main Console//")
    if options == "help":
        a=open("config/help" , "r+")
        b=a.read()
        print(b)
        main()
        return True
    if options == "payload web_gp":
        import payload as payload
        payload.payload_web_gp()
        main()
        return True
    if options == "use web_gp":
        import web_gp as web_gp
        web_gp.web_gp()
        return True
    if options == "payload web_ip -info":
        import payload as payload
        payload.payload_web_ip()
        main()
        return True
    if options == "use web_ip":
        #get ip adress
        import getip as getip
        getip.main_get_ip()
        return True
    if options == "payload web_threaten -info":
        import payload as payload
        payload.payload_web_threaten()
        main()
        return True
    if options == "use web_threaten":
        #use web_threaten
        def web_threaten():
            import threaten as threaten
            threaten.threaten()
        web_threaten()
        return True

    if options == "use py_tools":
        import py_tools as py_tools
        py_tools.py_tools()
        return True
    if options == "payload py_tools -info":
        def payload_py_tools():
            #show the payload of the py_tools
            #py_tools
            lang = open("config/lang" , "r+")
            langset = lang.read()
            if langset == "zh-cn":
                #chinese
                openpaylaod = open("config/payload/py_tools-zh" , "r+")
                readpayload = openpaylaod.read()
                print(readpayload)
                return True
            else:
                #english
                openpaylaod = open("config/payload/py_tools-en" , "r+")
                readpayload = openpaylaod.read()
                print(readpayload)
                return True
        payload_py_tools()
        main()   #reture to the main function
        return True

    if options == "use web_page_attack": #use the payload:web_page_attack
        import web_page_attack as web_page_attack
        web_page_attack.attack()
        main()
        return True
    if options == "payload web_page_attack":
        import payload as payload
        payload.payload_web_page_attack()
        main()
        return True
    if options == "payload web_console -info":
        import payload as payload
        payload.payload_web_console()
        main()
        return True
    if options == "use web_console":
        import os
        if os.name == "posix":
            import os , webbrowser
            os.system("cp 'Web Console/index/index.html' ./")
            os.system("python3 -m http.server 8080")
            return True
        if os.name == "nt":
            import os , webbrowser
            os.system("copy 'Web Console/index/index.html' ./")
            os.system("python -m http.server 8080")
            return True
        else:
            print("[!]Unknow Optioning System")
    
    if options == "payload exploit_virus -info":
        def payload_exploit_virus():
            lang = open("config/lang" , "r+")
            langset = lang.read()
            if langset == "zh-cn":
                openpaylaod = open("config/payload/exploit_virus-zh" , "r+")
                readpayload = openpaylaod.read()
                print(readpayload)
                main()
                return True
            else:
                openpaylaod = open("config/payload/exploit_virus-en" , "r+")
                readpayload = openpaylaod.read()
                print(readpayload)
                main()
                return True
        payload_exploit_virus()

    if options == "use exploit_virus":
        #use virus attack
        import exploit_virus as exploit_virus
        exploit_virus.exploit_virus()
        return True

    if options == "use shodan_search":
        import shodan_search as shodan_search
        shodan_search.shodansearch()
        return True

    if options == "payload shodan_search -info":
        #show the payload shodan_search 's info
        lang = "config/lang" #the language set file
        openlang = open(lang , "r+")
        setlang = openlang.read()
        if setlang == "zh-cn":
            openpaylaod = open("config/payload/shodan_search-zh" , "r+")
            readpayload = openpaylaod.read()
            print(readpayload)
            main()
            return True
        else:
            #english
            openpaylaod = open("config/payload/shodan_search-en" , "r+")
            readpayload = openpaylaod.read()
            print(readpayload)
            main()
            return True
        return True

    if options == "payload web_clone -info":
        #show the inforamtion for the web_clone
        def payload_web_clone():
            lang = "config/lang" #the language set file
            openlang = open(lang , "r+")
            setlang = openlang.read()
            
            if setlang == "zh-cn":
                def read_web_clone():
                    openpaylaod = open("config/web_clone-zh" , "r+")
                    readpayload = openpaylaod.read()
                    print(readpayload)
                    return True
                read_web_clone()
            
            else:
                def read_web_clone_en():
                    openpaylaod = open("config/web_clone-en" , "r+")
                    readpayload = openpaylaod.read()
                    print(readpayload)
                    return True

                read_web_clone_en()
        
        payload_web_clone()
        main()
        return True

    if options == "use web_clone":
        #use web site clone 
        import webiteclone as websiteclone
        websiteclone.website_clone()
        return True

    if options == "payload /?":
        print("")
        print("payload [payload name] -info")
        main()
    if options == "use exploit_seeker": #use seeker-master
        def startseeker():
            #only linux can start
            import os
            os.system("bash ./startseeker.sh")
        def exploit_seeker():
            def oschose():
                import os
                print("")
                print("[*]Optioning System:"+os.name) #get os name
                print("[*]Work Path:"+os.getcwd()) #get work path
                if os.name == "posix":
                    #Linux os
                    startseeker()
                    return True
                else:
                    print("[*]Do not start the seeker-master on your system!")
                    return False
            oschose()
                    
        exploit_seeker()
        main()

    if options == "use exploit_social": #show the payload exploit_social info
        def setool():
            import social as social
            social.socialtools()
        setool()
        return True
    
    elif options == "payload exploit_social -info":
        def exploit_social_info():
            openconfig = open("config/lang" , "r+") #open language config 
            readconfig = openconfig.read() #read language config
            if readconfig== "zh-cn": #if the language is chinese than run this function
                #chinese
                def readsocial_zh():
                    opensocial = open ("config/socialpayload-zh" , "r+")
                    socialinfo = opensocial.read()
                    print(socialinfo)
                    return True
                readsocial_zh()
            else:
                #english
                def readsocial_en():
                    openconfig = open("config/socialpayload-en" , "r+") #open social payload config
                    socialinfo = openconfig.read()
                    print (socialinfo)
                    return True
                readsocial_en()
        exploit_social_info()
        main()

    elif options == "clear":
        def clear():
            import os
            print("System:" + os.name) #get os 
            print("WorkPath:"+os.getcwd()) #get work path
            if os.name == "posix":
                #Linux
                import os
                os.system("rm -f index.html")
                os.system("rm -f index.js")
                os.system("rm -f logo.jpeg")
                os.system("rm -f pass.PNG")
                os.system("rm -f qqlogon.jpg")
                os.system("rm -f users.PNG")
                os.system("rm -f pass.html")
                os.system("rm -f logo.png")
                print("[*]clear work path OK!")
                return True
            
            if os.name == "nt":
                #windows
                os.system("del /F /S /Q index.html")
                os.system("del /F /S /Q index.js")
                os.system("del /F /S /Q logo.jpeg")
                os.system("del /F /S /Q pass.PNG")
                os.system("del /F /S /Q qqlogon.jpg")
                os.system("del /F /S /Q users.PNG")
                os.system("del /F /S /Q pass.html")
                os.system("del /F /S /Q logo.png")
                print("[*]clear work path OK!")
                return True
            else:
                print("[*]Unknow Optioning System , do not clear the work path!")
                return False
        clear()
        main()
        
    if options == "setool -info":
        def info(): #show setool's vistion anf information
            openconfig = open ("config/info" , "r+")
            readconfig = openconfig.read()
            print(readconfig)

        info()
        main()
    if options == "set language":  #set language
        def languageset():
            print("""
            1:English Enter:1 
            2:Chinese Enter:2
            """)
            #enter 1 set language english
            #enter 2 set language chinese
            lang = input ("Setool-Master~/Main Console~/Language Setting//")

            if lang == "1":
                with open ("config/lang" , "w") as f:
                    f.write ("en-us")
                f.close()
            
            if lang == "2":
                with open ("config/lang" , "w") as f:
                    f.write ("zh-cn")
                f.close()   
        languageset()
        main()

    if options == "payload ngrok -info":
        #show the info for the ngrok
        def payload_ngrok():
            lang = open("config/lang" , "r+")
            langconfig = lang.read()

            if langconfig == "zh-cn": #chinese
                def read_ngrok_zh():
                    openngrok = open("config/payload/ngrok-zh" , "r+")
                    readngrok = openngrok.read()
                    print(readngrok)

                    return True    
                read_ngrok_zh()
                main()
                return True
            else:
                openngrok = open("config/payload/ngrok-en" , "r+")
                readngrok = openngrok.read()
                print(readngrok)
                main()
                return True
        payload_ngrok()
        return True

    if options == "show options":
        
        lang = open("config/lang" , "r+")
        langset = lang.read()
        if langset == "en-us":
        #the English language
            
            openoptions = open("config/options" , "r+")
            readoptions = openoptions.read()
            print(readoptions)
            main()
        
        #the chinese language

        if langset == "zh-cn":

            openoptions = open("config/options-zh" , "r+")
            readoptions = openoptions.read()
            print(readoptions)
            main()
        else:
            openoptions = open("config/options" , "r+") #en-us
            readoptions = openoptions.read()
            print(readoptions)
            main() #use main function 
    if options == "exit":
        exit() #qiut
    
    if options == "use ngrok":
        def ngrok():
            import os
            if os.name == "posix":
                #Linux
                print("[!]You must logon for the ngrok than can use ngrok server!")
                print("[!]Logon to ngrok in url:https://www.ngrok.com/")
                print("[*]Enter 'exit' to retrue console")
                ngrokoptions = input("Enter http port to start:")

                if ngrokoptions == "exit":
                    main()
                    return True

                else:
                    import os
                    os.system("./ngrok/ngrok http "+ngrokoptions) #use ngrok
                    ngrok()
                    return False
            else:
                print("[*]The System do not run this software!")
                return False
        
        ngrok()
    
    else:
        def oscommand():
            import os
            os.system(options) #run the system command

        oscommand()    
        main()

def startlogo():  #logo
    print("""
------------------S e t o o l - M a s t e r-------------------
//////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////
 ____                      
/ ___\                        _________
\ \__  __________ _   _  _   / /\   /\ \  __    __ _______ ___ 
 \__ \ |__  |  | / \ / \ |  | |  | |  | |/  \  /  \ | |__  |  
___/  \|    |  ||   |   ||  | |  | |  | |   \| \__  | |    | 
\_____/|___ |  | \_/ \_/ |__|_|  |_|  |_|\__/\ \__\ | |____|_ 

//////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////
                     <-LinWin-Cloud->
         Vision For Windows,Linux,Android Termux 2.1
                      Setool-Master
              https://github.com/LinWin-Cloud
              https://gitee.com/LinWin-Cloud
            =================================
/////////////////////////////////////////////////////////////
    """)
    print("[!]Enter 'help' to get help")
    def chose_os():
        import os
        if os.name == "posix": #linux
            main()
            return True
        if os.name == "nt": #windows
            main()
            return True
        else:
            print("[!]Unknow Optioning System")
            return False
    chose_os()

startlogo()
