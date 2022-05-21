window.onload = function()
{
    //the input 's css
    var inth = document.getElementById("in") ;
    inth.style.height = '30px';
    inth.style.fontSize = "15px" ;
    inth.style.width = "400px" ;
    inth.style.backgroundColor = "black" ;
    inth.style.border ="none" ;
    inth.style.outline = "none" ;
    inth.style.color = "green" ;
    
    var oTest = document.getElementById("command");
    var newNode = document.createElement("p");
    var new_1 = document.createElement("p") ;
    var new_2 = document.createElement("p") ;
    newNode.innerHTML = "[*]Web Terminal For Setool-Master 2022" ;
    new_1.innerHTML = "[*]https://gitee.com/LinWin-Cloud/" ;
    new_2.innerHTML = "[*]https://github.com/LinWin-Cloud"
    setTimeout(function() {
        oTest.appendChild(newNode);
        oTest.appendChild(new_1)
        oTest.appendChild(new_2)
    }, 500);
    
}
function main()
{
    var keyCode = event.keyCode ? event.keyCode : event.which ? event.which : event.charCode;
    if (keyCode == 13) {
        var inth = document.getElementById("in").value ;
        if (inth == "setool -vistion"){
            var oTest = document.getElementById("command");
            var newNode = document.createElement("p");
            newNode.innerHTML = "LinWinCloud"+"<br />"
            +"Setool-Master vistion:2.1"+"<br />"
            +"Web Console vistion:3.1";
            //appendchild method
            oTest.appendChild(newNode);
            var inth = document.getElementById("in").value = "" ;
            console.log(inth)
            return true
        }

        if (inth == "shodan_search")
        {
            //use shodan command to search iot information
           window.location.href = "shodan_search.html" ;
           console.log("1231")
           return true
        }
        /*
            var oTest = document.getElementById("command");
            var newNode = document.createElement("p");
            oTest.appendChild(newNode);
         */
        if (inth == "color white")
        {
            console.log("[!]color white")
            var body = document.getElementById("body") ;
            var oTest = document.getElementById("command");
            var run = document.getElementById("run") ;
            var inth = document.getElementById("in") ;
            run.style.color = "white"
            body.style.color = "white" ;
            oTest.style.color = "white" ;
            inth.style.color = "white" ;
            var oTest = document.getElementById("command");
            var newNode = document.createElement("p");
            newNode.innerHTML = "[*]Change color:white"
            oTest.appendChild(newNode);
            var inth = document.getElementById("in").value = "" ;
            return true
        }
        if(inth == "color green")
        {
            var body = document.getElementById("body") ;
            var oTest = document.getElementById("command");
            var run = document.getElementById("run") ;
            var inth = document.getElementById("in") ;
            run.style.color = "green" ;
            body.style.color = "green" ;
            oTest.style.color = "green" ;
            inth.style.color = "green" ;
            var oTest = document.getElementById("command");
            var newNode = document.createElement("p");
            newNode.innerHTML = "[*]Change color:green" ;
            oTest.appendChild(newNode);
            var inth = document.getElementById("in").value = "" ;
            return true
        }
        if(inth == "web_site goto")
        {
            var url = prompt("Enter the url:")
            if(url){
                window.open(url)
            }
            console.log("[!]start the url:"+url)
            var oTest = document.getElementById("command");
            var newNode = document.createElement("p");
            newNode.innerHTML = "[*]Goto the url:"+url
            oTest.appendChild(newNode);
            var inth = document.getElementById("in").value = "" ;
            return true
        }
        if(inth == "help")
        {
            var oTest = document.getElementById("command");
            var newNode = document.createElement("p");
            newNode.innerHTML = "&nbsp &nbsp 1:shodan_search     Enter:shodan_search"+
            "<br />"+
                                "&nbsp &nbsp 2:web_site goto     Enter:web_site goto"
                                +"<br />"+
                                "&nbsp &nbsp 3:chinge color      Enter:color white/green"
                                +"<br />"+
                                "&nbsp &nbsp 4:settool's vistion Enter:setool -vistion"
                                +"<br />"+
                                "&nbsp &nbsp 5:new terminal      Enter:new terminal" 
                                +"<br />"+
                                "&nbsp &nbsp 6:search ip,domain  Enter:search ip_info" 
                                +"<br />"+
                                "&nbsp &nbsp 7:get own ip adress Enter:get my_ip"
            oTest.appendChild(newNode);
            var inth = document.getElementById("in").value = "" ;
            return true
        }
        if(inth == "new terminal")
        {
            window.open("terminal.html")
            var inth = document.getElementById("in").value = "" ;
            return true
        }
        if(inth == "get my_ip")
        {
            //get users own ip adress
            console.log("[!]user ip search")
            var oTest = document.getElementById("command");
            var newNode = document.createElement("p");
            setTimeout(function(){
                var new_1 = document.createElement("p") ;
                var oTest = document.getElementById("command");
                new_1.innerHTML = "[*]import a script from https://pv.sohu.com/cityjson?ie=utf-8" ;
                oTest.appendChild(new_1) ;
            } , 200)
            newNode.innerHTML = "<script src='https://pv.sohu.com/cityjson?ie=utf-8'></script>"
            oTest.appendChild(newNode) ;
            new_iframe_1 = document.createElement("p") ;
            new_iframe_1.innerHTML = "<iframe scroll='no' style='color:green;border:none;width:700px;height:50px;background-color:green' src='https://pv.sohu.com/cityjson?ie=utf-8'></iframe>" ;
            oTest.appendChild(new_iframe_1) ;
            var inth = document.getElementById("in").value = "" ;        
        }
        if(inth == "search ip_info"){
            //use api
            //all the information from ip.cn
            var url = prompt("Search The IP:")
            if(url){
                //use the ip.cn api
                window.open("https://ip.cn/ip/"+url+".html")
                var oTest = document.getElementById("command");
                var newNode = document.createElement("p");
                newNode.innerHTML = "&nbsp &nbsp &nbsp &nbsp &nbsp[*]Search the ip:"+url ;
                oTest.appendChild(newNode);
                var inth = document.getElementById("in").value = "" ; 
                return true
            }
        }
        if(inth == "renew")
        {
            for(i = 1 ; i<= 1 ; i++)
            {
                window.location.href = "" ;
                //renew the terminal 's window
                return true
            }
        }
    else{
        var oTest = document.getElementById("command") ;
        var newNode = document.createElement("p") ;
        newNode.innerHTML = "Do not find command:"+inth+""
        oTest.appendChild(newNode)
        var inth = document.getElementById("in").value = "" ;
        return false
        }
    }
}