window.onload = function()
{

    //make a id value to the html code : <input />
    //the users id value

    var users = document.getElementById("users") ;

    users.style.width = "100%" ; users.style.height = "35px" ;

    users.style.border = "1px solid green" ; users.style.outline = "none" ;

    users.style.color = "green" ;

    users.style.backgroundColor = "black" ;

    //the password 's id value

    var password = document.getElementById("password") ;

    password.style.width = "100%" ;

    password.style.height = "35px" ;

    password.style.border = "1px solid green" ; password.style.color = "green" ;

    password.style.outline = "none" ;

    password.style.backgroundColor = "black" ;

    //the logon button 's id value , css and script

    var btn = document.getElementById("btn") ;

    btn.style.width = "100%" ; btn.style.height = "35px" ; btn.style.backgroundColor = "black" ;

    btn.style.border = "1px solid green" ; btn.style.color = "green" ;

    btn.onmouseover = function()
    {

        btn.style.backgroundColor = "green" ; btn.style.color = "black" ;

        btn.onmouseout = function()

        {

            btn.style.backgroundColor = "black" ; btn.style.color = "green" ;

        }

    }

    btn.onclick = function()
    {

        var users = document.getElementById("users").value ;

        var password = document.getElementById("password").value ;

        console.log
        (
            "usersname="+users
        ) ;

        console.log(
            "password="+password
        ) ;

        if( users == "" )

        {

            var li = document.getElementById("li") ;

            li.innerHTML = "<p style='color:red'>[*]Usersname Is Space!</p>"

            console.log("[*]the usersname is space")

            return true

        }

        if( password == "" )

        {

            console.log("[*]the password is space")

            var li = document.getElementById("li") ;

            li.innerHTML = "<p style='color:red'>[*]Password Is Space!</p>"

            return true

        }
        
        if(users == "linwin" && password == "linwin")

        {

            window.location.href = "console.html" ;

            return true

        }
        else

        {

            var li = document.getElementById("li") ;

            li.innerHTML = "<p style='color:red'>[*]Your Password Or Usersname Is Null</p>"

            return false

        }

    }

}