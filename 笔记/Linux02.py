今日内容博客地址：
https://www.cnblogs.com/pyyu/articles/9314206.html

作业详解：

1.查看linux的path变量
    echo $PATH
2.简述linux的文档目录结构
    根目录下有一些子目录，子目录有着自己的不同的作用
3.递归创建文件夹/tmp/oldboy/python/{alex,wusir,nvshen,xiaofeng}
    mkdir -p /tmp/wzy/python/1 /tmp/wzy/python/2 /tmp/wzy/python/3  (p就是parent的意思)
4.显示/tmp/下所有内容详细信息
    ls -al
5.简述 /  ~  - 的含义
    / 为系统根目录
    ~ 为系统家目录   也就是/root目录
    - 为切换到上一次目录所在位置
6.请简述你如何使用vi命令
    vi/ 文件名
    i/o/a 从命令模式变为输入模式
    esc 从输入模式变为命令模式
    shift+: 从命令模式变为底部命令模式
    wq!

7.查看/etc/passwd的内容并且打印行号
    cat /etc/passwd -n
    cat -n /etc/passwd
8.查看文本有哪些命令？
    cat more less head tail
9.linux xshell常用快捷键？
    ctrl+l:
    ctrl+c:
10.如何用echo清空一个文件？
    echo '' > first.py (文件名)
    echo > filename
11.复制/tmp/下所有内容到/home，在修改文件前，先拷贝一份，防止内容被破坏
    cp -r ww ww.back
    cp -r ww wzy/
12.重命名test.py为my.py
    mv first.py second.py
13.强制删除/tmp下内容
    rm -rf /tmp/*
14.找到服务器上的settings.py
    find /tmp/ -name "first*"
15.找到/etc下的网卡配置文件，提示网卡配置文件名是ifc开头
    find /etc -name 'ifc*'
    vi /etc/sysconfig/network-scripts/ifcfg-enp0s3
这里题目，请先cp /etc/passwd /tmp/   拷贝文件
16.过滤出/tmp/passwd下有关root的信息
    root@localhost tmp]# grep 'root' passwd -i
17.过滤出/tmp/passwd下除了/sbin/nologin的信息，且打印行号
    [root@localhost tmp]# grep '/sbin/nologin' passwd -ivn
18.查看/tmp/passwd前25行
    head -25 passwd
19.查看/tm/passwd后3行
    [root@localhost tmp]# tail -3 passwd
20.不间断打印/var/log/py.log的信息
    tail -f /var/log/py.log
23.配置rm别名为“禁止你用rm，谢谢”，然后取消别名
    alias rm='echo 禁止使用'
    unalias rm
24.将服务器1的/tmp/my.py远程传输到服务器2的/opt/目录下
    scp /tmp/my.py root@xx.xx.xx.xx:/opt/      -r为目录递归拷贝
25.将服务器2的/opt/test.py拷贝到服务器1的/home目录下
    scp root@xx.xx.xx.xx:/opt/test.py /home/   -r为目录递归拷贝
26.统计/var/log/文件夹大小
    [root@localhost tmp]# du -sh /var/log
27.简述top的常见参数
    top 命令用于动态地监视进程活动与系统负载等信息
统计信息区
    第一行 (uptime)
    系统时间 主机运行时间 用户连接数(who) 系统1，5，15分钟的平均负载
    第二行:进程信息
    进程总数 正在运行的进程数 睡眠的进程数 停止的进程数 僵尸进程数
    第三行:cpu信息
    1.5 us：用户空间所占CPU百分比
    0.9 sy：内核空间占用CPU百分比
    0.0 ni：用户进程空间内改变过优先级的进程占用CPU百分比
    97.5 id：空闲CPU百分比
    0.2 wa：等待输入输出的CPU时间百分比
    0.0 hi：硬件CPU中断占用百分比
    0.0 si：软中断占用百分比
    0.0 st：虚拟机占用百分比
    第四行：内存信息（与第五行的信息类似与free命令）
    8053444 total：物理内存总量
    7779224 used：已使用的内存总量
    274220 free：空闲的内存总量（free+used=total）
    359212 buffers：用作内核缓存的内存量
    第五行：swap信息
    8265724 total：交换分区总量
    33840 used：已使用的交换分区总量
    8231884 free：空闲交换区总量
    4358088 cached Mem：缓冲的交换区总量，内存中的内容被换出到交换区，然后又被换入到内存，但是使用过的交换区
    没有被覆盖，交换区的这些内容已存在于内存中的交换区的大小，相应的内存再次被换出时可不必再对交换区写入。
28.给settings.py加锁，禁止删除
    chattr +a settings.py
    解锁
    lsattr -a settings.py
29.同步服务器时间到ntp.aliyun.com
    ntpdate -u ntp.aliyun.com
30.下载http://pythonav.cn/xiaobo.jpg图片
    wget 链接
查看linux命令网址
http://linux.51yip.com/
http://man.linuxde.net/
