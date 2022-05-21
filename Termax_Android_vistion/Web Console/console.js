window.onload = function()
{
    var desktopbtn = document.getElementById("desktop") ;
        desktopbtn.onmouseover = function()
        {
            desktopbtn.style.backgroundColor = "green" ;
            desktopbtn.style.color = "black" ;
            desktopbtn.onmouseout = function()
            {
                desktopbtn.style.backgroundColor = "black" ;
                desktopbtn.style.color = "green" ;
            }
        }
    desktopbtn.onclick = function()
    {
        var iframe = document.getElementById("iframe") ;
        iframe.src = "terminal/terminal.html" ;
    }
    /**
     * the body 's background and script , css
     * auther : windows observer
     */
    var body = document.getElementById("body") ;

    body.style.backgroundColor = "black" ;
    //the btn1 's css and script
    var btn1 = document.getElementById("btn1") ;

    btn1.style.width = "100%" ;

    btn1.style.height = "40px" ;

    btn1.style.backgroundColor = "black" ;

    btn1.style.border = "1px solid green" ;

    btn1.style.color = "green" ;

    btn1.onmouseover = function()
    {
        btn1.style.backgroundColor = "green" ;

        btn1.style.color = "black" ;

        btn1.onmouseout = function()
        {
            btn1.style.backgroundColor = "black" ;

            btn1.style.color = "green" ;
        }
    }
    //end the btn1's script
    //-------------------------------------------------

    var btn2 = document.getElementById("btn2") ;

    btn2.style.width = "100%" ;

    btn2.style.height = "40px" ;

    btn2.style.color = "green" ;

    btn2.style.backgroundColor = "black" ;

    btn2.style.border = "1px solid green" ;

    btn2.onmouseover = function()
    {
        btn2.style.backgroundColor = "green" ; btn2.style.color = "black" ;
    }
    btn2.onmouseout = function()
    {
        btn2.style.backgroundColor = "black" ;

        btn2.style.color = "green" ;
    }
    //end the btn2's script and css
    /**
     * --------------------------------------------
     */
    var btn3 = document.getElementById("btn3") ;

    btn3.style.width = "100%" ; btn3.style.height = "40px" ;

    btn3.style.backgroundColor = "black" ; btn3.style.color = "green" ;

    btn3.style.border = "1px solid green" ;

    btn3.onmouseover = function()
    {
        //if onmouseover will run this function

        btn3.style.backgroundColor = "green" ;

        btn3.style.color = "black" ;

        btn3.onmouseout = function()
        {
            btn3.style.backgroundColor = "black" ; btn3.style.color = "green" ;
        }
    }
    /**
     * end the btn3 's script and css
     */
     var btn4 = document.getElementById("btn4") ;

     btn4.style.width = "100%" ; btn4.style.height = "40px" ;
 
     btn4.style.backgroundColor = "black" ; btn4.style.color = "green" ;
 
     btn4.style.border = "1px solid green" ;
 
     btn4.onmouseover = function()
     {
         //if onmouseover will run this function
 
         btn4.style.backgroundColor = "green" ;
 
         btn4.style.color = "black" ;
 
         btn4.onmouseout = function()
         {
             btn4.style.backgroundColor = "black" ; btn4.style.color = "green" ;
         }
     }
     
     //the iframe 's css

     var iframe = document.getElementById("iframe") ;

     var pageheight = window.screen.height ;
     
    var documentpage = pageheight - 200 ;

    iframe.style.width = "100%" ;

     iframe.style.height = documentpage + "px" ;

     iframe.style.border = "1px solid green"

     var codehosting = document.getElementById("codehosting") ;

codehosting.onmouseover = function()
{
    codehosting.style.backgroundColor = "green" ;

    codehosting.style.color = "black"
}

codehosting.onmouseout = function()
{
    codehosting.style.backgroundColor = "black" ;

    codehosting.style.color = "green" ;
}

    //if run this function , that will goto the https://www.bing.com

    btn4.onclick = function()
    {
        var iframe = document.getElementById("iframe").src = "https://www.bing.com" ;

        console.log
        (
            "the iframe goto the url : https://www.bing.com"
        ) ;
    }

    //if onclick the btn1 will run this function
    btn1.onclick = function()
    {
        iframe.src = "tel.html" ;

        console.log("the firame page goto the url : tel.html")
    }

    btn2.onclick =function()
    {   
        //change the iframe src="email.html"

        iframe.src = "email.html" ;

        console.log("the iframe page goto the url : email.html") ;
    }

    /**
     * if users onclick the btn3 will run this unction
     * the iframe id will goto the page to the sms.html
     */
    btn3.onclick = function()
    {
        iframe.src = "sms.html" ;

        console.log("the iframe page goto the url : sms.html") ;

    }

    //run this function you can goto he github , 
    //but if use <iframe src="https://github.com"></iframe> function will lose your visit

    codehosting.onclick = function()
    {
        //use window.open function can fix the programe

        window.open("https://github.com") ;

        console.log("open the new table to , url : https://github.com")
    }

    /**
     * the back id value
     * the back id value 's script 
     * onmouseover and onmouseout and onclick 
     */

    var back = document.getElementById("back") ;

    back.onmouseover = function()

    {

        back.style.backgroundColor = "green" ; back.style.color = "black" ;

        back.onmouseout = function()
        {

            back.style.backgroundColor = "black" ; back.style.color = "green" ;

        }
    }
    back.onclick = function()
    {

        var a = document.getElementById("doreal").style.display = "block" ;

        var yes = document.getElementById("yes") ;

        var no = document.getElementById("no") ;

        yes.onclick = function()
        {

            window.location.href = "index.html" ;

        }
        no.onclick = function()
        {

            var a=document.getElementById("doreal").style.display = "none" ;

        }

    }
}
