window.onload = function()

{

    var send = document.getElementById("send") ;

    send.onmouseover = function()

    {

        send.style.backgroundColor = "green" ; send.style.color = "black" ;

        send.onmouseout = function()

        {

            send.style.backgroundColor = "black" ; send.style.color = "green" ;

        }

    }

    var re = document.getElementById("re") ;

    re.onmouseover = function()

    {

        re.style.backgroundColor = "green" ; re.style.color = "black" ;

        re.onmouseout = function()

        {

            re.style.backgroundColor = "black" ;

            re.style.color = "green" ;

        }

    }

    re.onclick = function()

    {

        window.location.href = "" ; return true ;

    }

    send.onclick = function()

    {

        var sms = document.getElementById("sms").value ;

        var text = document.getElementById("text").value ;

        console.log(send) ; console.log(text) ;

        var li = document.getElementById("li") ;

        li.innerHTML = "<a style='color:green' href='sms:"+sms+"?body="+text+"'>sms:"+sms+"</a>"

    }

}