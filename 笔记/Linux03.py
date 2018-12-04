请问你使用的Linux发行版是什么？查看Linux发行版的命令是？
    centos7
    #查看ubuntu操作系统详细信息
    cat /etc/os-release
    #查看centos7系统版本信息
    cat /etc/redhat-release
请问你公司服务器环境是物理机？还是虚拟化？
    虚拟机，成本低
    物理机，成本高
请写出操作文件/文件夹的基本命令
    文件：
        编辑文件：vim vi 对不存在的文件有touch的 作用
        查：cat more less head tail
        删：rm -rf filename
        改：mv oldfilename newfilename
        增：touch
        touch
    文件夹：
        增：mkdir
        查： ll   ls -l
        删： rmdir 删除空文件夹
            rm -rf dirname
        进入：cd dirname
        改：  mv olddirname  newdirname   改名和移动


使用grep过滤出/opt/mysite/mysite/settings.py的ALLOWED_HOSTS配置，(请忽略大小写)
    grep -i 'ALLOWED_HOSTS' /opt/mysite/mysite/settings.py
找到目录/opt/下所有的以.py结尾的文件
    find /opt -type f --name '*.py'
    ls /opt | grep *.py
linux如何切换普通用户oldboy?
    su - oldboy
如何使用root身份执行命令ls /root/*
    1.编辑 vi /etc/sudoers 写入你想通过sudo执行命令的用户信息
    sudo ls /root/*
linux文件权限的755,700是什么意思？转化为rwx格式是什么？
            755                      700
    user    可读可写可执行 rwx        可读可写可执行   rwx
    group   可读可执行    r-x        没有任何权限     ---
    other   可读可执行    r-x        没有任何权限     ---
如何创建/usr/bin/python3软连接，链接到/opt/python34/bin/python3
    ln -s 目标文件  软连接文件
    ln -s /opt/python34/bin/python3  /usr/bin/python3
已知test.py文件权限是rwxr--r--，如何修改权限为rw-rw-rw
    chmode 666 test.py
解压缩Python源码包Python-3.7.tgz.gz
    x 解压缩参数
    f 指定压缩文件
    tar -zxvf Python-3.7.tgz.gz
将/tmp/下所有内容压缩成All_log.tar.gz并且放到/home/下
    c 是压缩的参数
    f 指定压缩文件
    -z 调用gzip压缩格式，可以大大的减少磁盘占用，压缩率提高60%
    tar -zcf /home/All_log  /tmp/*
    
    tar -cf 即将压缩的文件名  我要压缩的内容
    tar -cf all_log.tar  all_log/
    gzip all_log.tar
    mv all_log.tar.gz /home
查看mysql端口是否存活
    netstat -tunlp | grep mysql
检测mysql服务是否启动
    systemctl status mysql
    只有通过yum安装的软件，才能通过systemctl管理
    systemctl status/start/stop/restart ngix

如何查看django的进程
    ps -ef | grep django
如何杀死django进程
    kill django进程号（PID）

强制删除进程
    kill -9 PID

在登录Linux时，一个具有唯一进程ID号的shell将被调用，这个ID是什么(B)?
A.NID       B.PID        C.UID        D.CID

下面哪个目录存放用户密码信息（B）
A./boot        B./etc        C./var        D./dev

(D)不是流行的Linux操作系统。
A.Red Hat Linux B.Mac OS C.Ubuntu Linux D.Red Flag Linux 

用自动补全功能时，输入命令名或文件名的前1个或几个字母后按什么键？ ( B)
A.【Ctrl】键 B.【Tab】键 C.【Alt】键 D.【Esc】键 

在vi中退出不保存的命令是？(D )
A. :q B. :w C. :wq D. :q! 

pwd命令功能是什么? ( C)
A. 设置用户的口令 
B. 显示用户的口令 
C. 显示当前目录的绝对路径 
D. 查看当前目录的文件 

文件权限读、写、执行的三种标志符号依次是(A )。
A rwx B xrw C rdx D srw 

某文件的组外成员的权限为只读；所有者有全部权限；组内的权限为读与写，则该文件的权限为(D )。
A 467 B 674 C 476 D 764 

改变文件所有者的命令为 (C )。
A chmod B touch C chown D cat 
chgrp 跟改组
当运行在多用户模式下时，可以切换多少虚拟用户终端（ B ）
A、3 B、6 C、12 D、1

观察系统当前进程的运行情况的命令是（ C ）
A、free B、dmesg C、top D、last

如果执行命令 chmod 746 file.txt，那么该文件的权限是（A）。
 A.rwxr--rw-

 B.rw-r--r—

 C.--xr--rwx

 D.rwxr--r—


 如果您想列出当前目录以及子目录下所有扩展名为“.txt”的文件，那么您可以使用的命令是（ B）。
 A.ls *.txt

 B.find –name “*.txt”

 C.ls –d .txt

 D.find . “.txt”
