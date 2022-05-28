

from asyncore import read
from operator import truediv


def payload_web_page_attack():
    #read the language config
    lang = open("config/lang" , "r+")
    langset = lang.read()
    if langset == "zh-cn":
        #chinese
        openconfig = open("config/payload/web_page_attack-zh" , "r+")
        readconfig = openconfig.read()
        print(readconfig)
        return True
    else:
        #english
        openconfig = open("config/payload/web_page_attack-en" , "r+")
        readconfig = openconfig.read()
        print(readconfig)
        return True

def payload_web_console():
    #read the language config
    lang = open("config/lang" , "r+")
    langset = lang.read()
    if langset == "zh-cn":
        #chinese
        openconfig = open("config/payload/web_console-zh" , "r+")
        readconfig = openconfig.read()
        print(readconfig)
        return True
    else:
        #english
        openconfig = open("config/payload/web_console-en" , "r+")
        readconfig = openconfig.read()
        print(readconfig)
        return True

def payload_web_threaten():
    try:
        openconfig = open("config/lang" , "r+") ;
        lang = openconfig.read() 
        if lang == "zh-cn":
            #chinese
            readpayload = open("config/payload/web_threaten-zh" , "r+")
            payload = readpayload.read()
            print(payload)
            return True
        else:
            #english
            readpayload = open("config/payload/web_threaten-en" , "r+")
            payload = readpayload.read()
            print(payload)
            return True
        return True
    except:
        print("[!]Error Running")
        return False
def payload_web_ip():
    openconfig = open("config/lang" , "r+") ;
    lang = openconfig.read() 
    if lang == "zh-cn":
        #chinese
        readpayload = open("config/payload/web_ip-zh" , "r+")
        payload = readpayload.read()
        print(payload)
        return True
    else:
        #english
        readpayload = open("config/payload/web_ip-en" , "r+")
        payload = readpayload.read()
        print(payload)
        return True
    return True

def payload_web_gp():
    openconfig = open("config/lang" , "r+") ;
    lang = openconfig.read() 
    if lang == "zh-cn":
        #chinese
        readpayload = open("config/payload/web_gp-zh" , "r+")
        payload = readpayload.read()
        print(payload)
        return True
    else:
        #english
        readpayload = open("config/payload/web_gp-en" , "r+")
        payload = readpayload.read()
        print(payload)
        return True
    return True