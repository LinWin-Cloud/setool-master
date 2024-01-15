# Setool Master

`SetoolMaster`是一款让你入门即入狱的python3开发的进阶型社会工程学工具。包括了全球定位、Ngrok内网穿透、Seeker高精度定位、网页钓鱼、病毒攻击、恐吓勒索信、爬虫、网站克隆、物联网设备搜索等，同时拥有中文支持，内置大量钓鱼模板，设计用于组织级别红队渗透测试，用于团队组织设备型协同，经过非常多的实战演练，效果出众，远超同行产品

你看过电影里面的黑客么，手指在键盘上不停的在打字，屏幕上运行的数不清的计算机命令，<br />
没过一会儿，便可以入侵、盗取别人的计算机密码、QQ和微信等。<br />

没错,`Setool Master`就是这样一款黑客工具，设计用于红队的社会工程学攻击。比起传统<br />
的漏洞利用，社会工程学攻击会更加的高效和安全，而且对于使用者的门槛会非常低，入门<br />
linux的也能快速掌握。使用python3开发，有更加良好的发展属性和可读性、运行效率<br />
非常的高，设计用于对组织级别的攻击

1. 绝对不要使用Setool Master去攻击一个你不认识的人，或者你可能会遇到许麻烦
2. 你不能将这些源代码用于商业用途
3. 本开源项目内包含第三方工具，在这里说说明：ngrok，seeker-master
4. 本开源项目允许引用，但受到Apache2开源条约限制
5. 作者：LinWinCloud

# 版本维护
1. 安卓源代码版本   持续维护 v
2. Linux安装包版本 部分维护 v
3. 安卓编译版本    不再维护 X
4. linux编译版本   不再维护 X
5. 源代码        持续维护 V

# 安装教程
```bash
git clone https://github.com/LinWin-Cloud/setool-master
cd setool-master
pip3 install whois
pip3 install requests
```

1.源代码版本、安卓源代码版本
```bash
cd resources_code_vistion （这个是源代码版本） 或者 cd Android_Resources_code
python3 setool.py
```

2.Linux安装包版本
```bash
7z x Setool-Master.7z
cd Setool-Master
cd Setool-Master
python3 install_linux.py
```
软件将安装在 `/var/Setool-Master`，环境请自行配置<br />

3.编译版本、安卓编译版本
```bash
cd build_vistion（这个是编译版本） 或者 cd Termax_Android_vistion （这个是安卓编译版本）
chmod +x ./setool<br />
bash ./setool
```

# 使用文档
<li>1. <a href='https://github.com/LinWin-Cloud/setool-master/blob/main/Help(English).md'>使用文档（英文版本）</a></li>
<li>2. <a href='https://github.com/LinWin-Cloud/setool-master/blob/main/%E5%B8%AE%E5%8A%A9%E6%96%87%E6%A1%A3%E4%B8%AD%E6%96%87.md'>使用文档（中文版本）</a></li>

# 注意
1. 本工具集内Web Console密码linwin用户名linwin

# 更新日志
 1. v1.0.0 2022.1.5 发布Setool Linux轻量个人版本
 2. v2.1.1 2022.3.5 发布Setool Master源代码版本
 3. v2.1.2 2022.3.5 发布Setool Master安装包版本
 4. v2.1.3 2022.3.15 发布Setool Master预编译版本
 5. v2.1.4 2022.4.1 更新配置文件、告示
 6. v2.2.1 2022.5.1 修改部分源代码
 7. v2.3.2 2022.5.4 修改配置文件
 8. v2.4.1 2022.5.7 修改配置文件，更新版本信息
 9. v2.4.2 2022.5.8 修改配置文件和源代码
 10. v2.5.1 2022.5.15 发布安卓Termux编译版本
 11. v2.5.2 2022.5.17 更新安卓Termux编译版本
 12. v2.5.3 2022.5.19 更新部分源代码
 13. v2.5.4 2022.5.28 发布安卓Termux源代码版本
 14. v2.5.5 2022.5.29 更新版本信息、更新源代码
 15. v2.5.6 2022.5.30 修复部分代码错误、更新部分配置文件
 16. v2.5.7 2022.5.31 更新 Setool Master编译版本 版本信息、配置文件
 17. v2.5.8 2022.6.2 更新配置、版本信息
 18. v2.5.9 2022.6.6 更新源代码版本代码
 19. v2.6.0 2022.6.7 创建使用文档文档
 20. v2.6.1 2022.6.10 更新 使用文档（英文版本）
 21. v2.6.2 2022.6.11 更新版本信息、配置信息
 22. v2.6.2 2022.6.12 更新配置文件
 23. v2.6.3 2022.6.13 更新 安卓源代码版本 源代码
 24. v2.6.4 2022.6.15 更新使用文档、配置文件
 25. v2.6.5 2022.6.16 更新配置文件
 26. v2.6.6 2022.6.20 更新源代码
 27. v2.6.7 2022.6.21 更新英语文档，创建中文文档
 28. v2.6.8 2022.6.22 更新配置文件
 29. v2.6.9 2022.6.24 更新安卓源代码，更新配置文件
 30. v2.7.0 2022.6.26 修复源代码错误，修复帮助和配置
 31. v2.7.1 2022.6.28 更新版本信息、更新配置文件
 32. v2.7.2 2022.6.30 更新配置文件
 33. v2.7.3 2022.7.3 更新配置文件，修复源码错误
 34. v2.7.4 2022.7.5 更新项目为Setool Master LTS长期支持版本
 35. v2.7.5 2022.7.6 更新源代码、修复IO操作漏洞
 36. v2.7.6 2022.7.13 更新配置文件
 37. v2.7.7 2022.7.22 更新配置文件，说明
 38. v2.7.8 2022.7.23 更新中文帮助、更新配置文件
 39. v2.7.9 2022.8.9 更新配置文件
 40. v2.8.0 2022.8.31 更新配置文件、修复错误
 41. v2.8.1 2022.9.12 修改文档
 42. v2.8.2 2022.9.16 删除了Linux编译版本，不再维护此版本、修改了源代码、修改了说明文件
 43. v2.8.3 2022.10.15 删除了部分无用文件、更新文档
 44. v2.9.0 2023.12.29 更新源代码版本文档、更新原代码、更新配置文件

## About

  Setool Master is a open resources social enginnering tools for linux.android(termux).
<br />
It is free.You do not pay some money for these tools.

  Setool Master use Python Code language.It is very easy and funny.You can use these 
  
resources code to make a new tools and so on.If you want to get Setool-Master,you can 

goto https://github.com/LinWin-Cloud/setool-master. https://gitee.com/LinWin-CLoud/setool-master

Setool Master是一个适用于Linux、Android（termux）的开源的社会工程学
<br />
工具。它是免费的。你不需要为这些工具支付费用。Setool Master使用Python
<br />
编程语言。非常简单并且有趣，你能用这些源代码去创造一个新的工具等等。如果你
<br />
想获取SetoolMaster，你能够访问
<br />
https://github.com/LinWin-Cloud/setool-master. https://gitee.com/LinWin-CLoud/setool-master

# 该项目会持续维护，吸收大家的建议
项目维护真的不容易，开源项目不赚钱，本项目将保证永远也不进行商业收费
<br />
真心希望屏幕前面的你能够给开发者一些动力来维护更新这更好的项目
<br />
捐赠 1 元 人民币，给开发者一些动力，您可以选择忽略。项目同样会维护和更新，您依旧可以像原来那样操作本项目。
<img src='https://github.com/LinWin-Cloud/setool-master/blob/main/183_1656074545_hd.jpeg' />
