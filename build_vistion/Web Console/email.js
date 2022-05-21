window.onload = function()

{

    //make a id value with the e-mail target

    var target = document.getElementById("target") ;

    target.style.width = "500px" ;

    target.style.height = "35px" ;

    target.style.border = "1px solid green" ;

    target.style.backgroundColor = "black" ; target.style.color = "green" ;

    target.style.outline = "none" ;

    //the text box 's css and script

    var text = document.getElementById("text") ;

    text.style.width = "500px" ;

    text.style.height = "200px" ;

    text.style.border = "1px solid green" ;

    text.style.backgroundColor = "black" ; text.style.color = "green" ;

    text.style.outline = "none" ;


    var send = document.getElementById("send") ;

    send.onmouseover = function()
    {

        send.style.backgroundColor = "green" ;

        send.style.color = "black" ;

        send.onmouseout = function()
        {

            send.style.backgroundColor = "black" ;

            send.style.color = "green" ;

        }

    }

    var re = document.getElementById("re") ;

    re.style.width = "300px" ; re.style.height = "25px" ; re.style.border = "1px solid green" ;

    re.style.color = "green" ;re.style.backgroundColor = "black" ;

    re.onmouseover = function(){

        re.style.backgroundColor = "green" ; re.style.color = "black" ;

        re.onmouseout = function(){

            re.style.backgroundColor = "black" ;

            re.style.color = "green" ;


        }

    }
}

function mail()
{

    console.log("send the e-mail")

    var mail = document.getElementById("target").value ;

    var content = document.getElementById("text").value ;

    if(mail == "" && content == "")
    {

        var li = document.getElementById("li") ;

        console.log("[*]the content and target is space") ;

        li.innerHTML = "<p style='color:red'>[*]The Target and Content Is Space!</p>"

        return true

    }

    if(mail == ""){

        var li = document.getElementById("li") ;

        console.log("the target is space!")

        li.innerHTML = "<p style='color:red'>[*]The Target Is Space !</p>"
        
        return true

    }
    if(content == "")
    {

        var li = document.getElementById("li") ;

        console.log("[*]the content is space") ;

        li.innerHTML = "<p style='color:red'>[*]The Content Is Space!</p>" ;

        return true

    }

    else
    {
        if(subject == ""
        )
        {
            console.log("[*]the subject is space!")

            var subject = document.getElementById("subject").value ;
    
            var li = document.getElementById("li") ;
    
            li.innerHTML = "<p style='color:yellow'>[*]The Subject is space!</p>"

        }
        else
        {

            var target = document.getElementById("target").value ;

            console.log(target) ; console.log(content) ;

            var li = document.getElementById("li") ;

            var subject = document.getElementById("subject").value ;

            var printhtml = "<a style='color:green' href='mailto:"+target+"?subject="+subject+"&body="+content+"'>send mail:"+target+"</a>"

            console.log(printhtml) ;

            li.innerHTML = printhtml ;


        }

    }

}

function re()

{

    window.location.href = "" ;

    return true

}