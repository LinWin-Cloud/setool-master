window.onload = function()
{
    var d = new Date();
    console.log("[*]users visit this page")
    console.log('[!]year:'+d.getFullYear()); //year
    var mouth = d.getMonth() ;
    console.log('[!]mouth:'+mouth);  //mouth
    console.log('[!]date:'+d.getDate()) //date
    console.log('[!]hour:'+d.getHours()) //hours
    console.log('[!]minutes:'+d.getMinutes()) //minutes
    console.log('[!]seconds:'+d.getSeconds()) //seconds
}