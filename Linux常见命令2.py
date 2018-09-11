一、配置yum源管理与软件管理。yum常见工具 tree  telnet  sl  cowsay
1.
yum install tree   #安装tree命令，以树形目录显示

#由于每次安装都由是否确认的提示，取消默认安装在命令后面加上-y。如下

 yum install  tree  telnet -y   #安装tree 命令和telnet 命令
#怎么查看软件安装上了没有，一般会提示
Complete!
或者
Package tree-1.5.3-3.el6.x86_64 already installed and latest version
Package 1:telnet-0.17-48.el6.x86_64 already installed and latest version


=============查询软件是否安装==============

killall yum  #把所有的yum杀掉

rpm -qa  tree telnet #查看是否安装上了

==============查询软件包的内容=============

rpm -ql tree telnet   #查看内容  

tree -L 1 /   #显示根目录下第一层

history  #显示你都敲过什么命令

=============挂载光盘====================

 ls -l /dev/cdrom 

#挂载：相当于给设备开一个（入口）洞

mount /dev/cdrom  /mnt/    #mnt临时入口

cd /mnt/

ls Pageages/　　|head


总结：
linux 下安装软件

1、常用：yum install tree xxx -y
2、rpm
　　rpm -qa  查询软件是否安装  
　　rpm -ql   查询软件包的内容
　　rpm  -ivh 安装rpm包
3、df -h 显示磁盘使用的情况
　　mount 挂载
　　head  显示前几行的内容 默认 显示前10行
　　head *5 /etc/passwd   查看前5行
　　tail  显示最后几行的内容  默认最后10行


临时：关闭当前正在运行的
/etc/init.d/iptables stop
永久:关闭开机自启动
chkonfig iptables off 

ll /var/log/secure # 用户访问系统的记录，谁在什么时间链接了你的服务器，什么时候链接了

#安装lrzsz
yum install lrzsz -y
rz   #windows文件上传到linux
sz   #吧linux文件下载到windows
rpm -pa lrzsz  #查看安装好了没有


.tar.gz  
.zip #这种格式的压缩包是linux和windows默认支持的
unzip secure-20161219.zip   #解压

xshell  #远程连接 
xftp     #ftp工具 
https://www.netsarang.com/download/down_form.html?code=523 

#查看文件内容用cat ,,看日志的时候不用这个
#查看日志
    1、less
    2、head/dail
    3、grep 
f或空格 #向下翻页
b #想上翻页
grep 'Failed password' secure-20161219




























