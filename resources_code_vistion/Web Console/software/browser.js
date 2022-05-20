window.onload = function()
{
    console.log("[*]web broswer finish")
    
    var search = document.getElementById("search") ;

    search.onmouseover = function()
    {
        search.style.backgroundColor = "green" ;
        search.style.color = "black" ;

        search.onmouseout = function()
        {
            search.style.backgroundColor = "black" ;
            search.style.color = "green" ;
        }
    }
    //if the mouse onclick the id value:search
    search.onclick = function()
    {
        var inth = document.getElementById("inth") ;
        var text = inth.value ;
        console.log("Search Url:"+text)
        var iframe = document.getElementById("iframe");
        iframe.src = text ;
    }
    var renew = document.getElementById("renew") ;
    renew.onclick = function()
    {
        iframe.src = "https://www.bing.com" ;
    }
    renew.onmouseover = function()
    {
        renew.style.backgroundColor = "green" ;
        renew.style.color = "black" ;
        renew.onmouseout = function(){
            renew.style.backgroundColor = "black" ;
            renew.style.color = "green" ;
        }
    }
}