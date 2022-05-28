window.onload = function()
{

    var tel = document.getElementById("tel") ;

    tel.style.width = "200px" ; tel.style.height = "35px" ;

    tel.style.border = "1px solid green" ; tel.style.color = "green" ;

    tel.style.backgroundColor = "black" ;

    tel.style.outline = "none" ; tel.style.float = "left" ;

    //if onmouse over than run this funtions

    var phone = document.getElementById("phone") ;

    phone.onmouseover = function()

    {

        phone.style.backgroundColor = "green" ;

        phone.style.color = "black" ;

        phone.onmouseout = function()
        {

            phone.style.backgroundColor = "black" ;

            phone.style.color = "green" ;

        }

    }

    var re = document.getElementById("re") ;

    re.onmouseover = function()

    {

        re.style.backgroundColor = "green" ;

        re.style.color = "black" ;

    }

    re.onmouseout = function()

    {

        re.style.backgroundColor = "black" ; re.style.color = "green" ;

    }

    re.onclick = function()

    {

        window.location.href = "" ;

        console.log ( "onclick the id value : re" )

    }

}

function phone()

{

    //make a id value to the tel

    var tel = document.getElementById("tel").value ;

    console.log

    (

        "tel number : " + tel

    ) ;

    if

    (
        tel == ""   //if the tel value is space
    )
    {

        var alert = document.getElementById("alert") ;

        alert.innerHTML = "<p style='color:red'>[*]The Tel Number Is Space !</p>"

        return false
    }
    else 
    {

        var alert = document.getElementById("alert") ;

        alert.innerHTML = "<a style='color:green;height:20px' href='tel:" + tel + "'>" + "tel:"+tel + "</a>"

        return true
    }

}