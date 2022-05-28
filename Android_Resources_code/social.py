
#social tools function


def socialtools():
    def show():
        openconfig = open ("config/lang" , "r+") #read the config
        readconfig = openconfig.read()
        def entools():
            opentools = open ("config/tools" , "r+")
            readtools = opentools.read()
            print(readtools)

        if readconfig == "zh-cn":  #if the config is zh-cn than use chinese
            def zhtools():
                opentools = open ("config/tools-zh" , "r+")
                readtools = opentools.read()
                print(readtools)
            zhtools()

        else:
            entools() #use en-us

    tools = input("Setool-Master~/Main Console~/Social Attack//")
    if tools == "show options":
        show()
        socialtools()
    
    elif tools == "exit":
        import setool as setool
        setool.main()
    
    elif tools == "1":
        #use qq attack
        import socialattack as socialattack
        socialattack.socialqqattack()
    elif tools == "2":
        #use qq mail attack
        import socialattack as socialattack
        socialattack.qqmail()
    if tools == "3":
        #use 163 mail Attack
        import socialattack as socialattack
        socialattack.netease()
    if tools == "4":
        import socialattack as socialattack
        socialattack.microsoftattack()
    
    if tools == "5":
        #use wechat attack
        import socialattack as socialattack
        socialattack.wechat()
    
    if tools == "6":
        #use alipay attack
        import socialattack as socialattack
        socialattack.alipay()
    
    else:
        socialtools()