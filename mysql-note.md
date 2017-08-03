## [mysql学习](https://www.w3schools.com/sql/sql_insert.asp)

[参考连接一](http://c.biancheng.net/cpp/html/1455.html)    


1：下载，安装，启动服务

如果没有“已启动”字样，说明MySQL服务未启动。启动方法为：“开始”－〉“运行”，输入“cmd”，回车，弹出XP命令提示符界面（类似DOS命令行，以后简称命令行）。然后输入“net start mysql”就启动MySQL服务了，停止MySQL服务“net stop mysql”（注意，这里输入的是MySQL服务的名字。如果你的MySQL服务的名字是DB或其它名字，你应该输入“net start DB”或其它名）



2：登陆数据库方式

```
mysql –h localhost –u root –p

mysql –h host_name –u user_name –p    // 链接mysql的格式
下面介绍选项的含义：

 -h host_name （另一种写法：--host=host_name） 

    希望连接的服务器主机。如果此服务器运行在与mysql 相同的机器上，这个选项一般可省略。 

 -u user_name （另一种写法：--user=user_name） 

    您的MySQL 用户名。如果使用UNIX且您的MySQL 用户名与注册名相同，则可以省去这个选项；mysql 将使用您的注册名作为您的MySQL 名。在Windows 下，缺省的用户名为 root 。 

 -p（另一种写法：--password=your_password） 

    这个选项告诉mysql 提示键入您的MySQL 口令。注意：可用 -pyour_password 的形式在命令行上键入您的口令。选择-p不跟口令告诉mysql 在连接时提示您键入口令。例如：
    
mysql>mysql --host=host_name –user=user_name –password
Enter password:


```

```
mysql>mysql –uroot –p123
 //  最好不要这样写
```

#### 链接远端的某个数据库

如果连接到远程度某个服务器上，需要用 –h 指定主机名。例如该主机为db.kysf.net，则相应的命令如下：

```
mysql –h db.xia8.net:3306 –u root –p
```



