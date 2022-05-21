function logon() {
    var usersname = document.getElementById("usersname").value;
    var pwd = document.getElementById("pwd").value;
    if (usersname == "") {
        alert("用户名不可为空")
        return false
    }
    if (pwd == "") {
        alert("密码不可为空")
        return false
    }
    else {
        console.log("usersname:" + usersname)
        console.log("password:" + pwd)
        info = "InfoMation-->" + "'" + "usersname=" + usersname + ";" + "password=" + pwd + "'"
        window.location.href = info
    }
}