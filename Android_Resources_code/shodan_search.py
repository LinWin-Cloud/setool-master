def shodansearch():
    import os
    print("[*]Optioning System:"+os.name)
    print("[*]Work path:"+os.getcwd())
    print("")
    print("[!]Server form https://shodan.io")
    
    def shodan_search_main():
        options = input ("Setool-Master~/Main Console~/Shodan_Search//")
        if options == "exit": #reture to setool console
            import setool as setool
            setool.main()
            return True

        if options == "show options":
            def shodan_options():
                print("""
    1:shodan command    enter:1
    2:exit              enter:exit
                """)
                return True
            shodan_options()
            shodan_search_main()
            return True
        
        if options == "1":
            print("[*]Enter 'exit' to exit")
            def shodan_search_run():
                command = input("Enter shodan command:")
                if command == "exit":
                    shodan_search_main()
                    return True
                
                else:
                    import webbrowser
                    webbrowser.open("https://www.shodan.io/search?query="+command)
                    shodan_search_run()
                    return True
            shodan_search_run()
        else:
            shodan_search_main()
            return False
    shodan_search_main()