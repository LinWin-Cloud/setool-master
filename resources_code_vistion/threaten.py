
import os
import requests
import urllib
import webbrowser
def threaten_options():
    print("""
    1:threaten modle   enter:1
    """)

def threaten():
    print("[!]Enter 'exit' to exit")
    print("[!]Enter 'show options' to show all project")
    def threaten_main():
        options = input("Setool-Master~/Main Console~/Threaten//")
        if options == "exit":
            import setool
            setool.main()
            return True
        if options == "show options":
            threaten_options()
            threaten_main()
            return True
        if options == "1":
            def threaten_modle():
                import os
                if os.name == "nt":
                    #windows
                    os.system("del /f /s /q index.html")
                if os.name == "posix":
                    #linux
                    os.system("rm -f index.html")
                else:
                    print("[!]Unknow Optioning System")
                try:
                    print("[*]Make a threaten Web age")
                    a_1 = input("[1]Enter the title:")
                    a_2 = input("[2]Enter the E-mail adress:")
                    a_3 = input("[3]Enter the content:")
                    a_4 = input("[4]Enter other information:")
                    a_5 = input("[5]Enter website to visit:")
                    a_6 = input("[6]Enter the last:")
                    #make the webpage
                    #use html code
                    with open("index.html" , "a") as f:
                        f.write("<title>"+a_1+"</title>") #write the title to the file
                        f.write("<link href='threaten/index.css' rel='stylesheet' />")
                        f.write("<script src='threaten/attack.js'></script>")
                        f.write("<div class='space'></div>")
                        f.write("<div align='center' class='maindiv'>")
                        f.write("    <div class='border' align='center'>")
                        f.write("       <h1 class='font'>WORRY!</h1>")
                        f.write("       <a class='href' align='center' href='mailto:"+a_2+"'>"+"Email:"+a_2+"</a>") #write the email to the file
                        f.write("       <div align='center' style='width:80%;height:auto'>")
                        f.write("           <p>"+a_3+"</p>")
                        f.write("           <br />")
                        f.write("           <p>"+a_4+"</p>")
                        f.write("           <br />")
                        f.write("           <a class='href' align='center' href='"+a_5+"'>Visit Web Site:"+a_5+"</a>")
                        f.write("           <br />")
                        f.write("           <p>"+a_6+"</p>")
                        f.write("           <br />")
                        f.write("           <div id='data'></div>")
                        f.write("       </div>")
                        f.write("   </div>")
                        f.write("</div>")
                    f.close()
                    return True
                except:
                    print("[!]Finish the threaten web page make")
                    return False
            threaten_modle()
            threaten_main()
        else:
            threaten_main()
            return False
    threaten_main()
