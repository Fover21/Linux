
创建一个目录 /data
    mkdir /data
    ls  -l  /data/
    cd   /data/
    pwd
        相对路径与绝对路径
        1.绝对路径 从根开始的路径 /data
        2.相对路径 不是从跟开始  相对于当前路径   data

在/data下面创建文件filename.txt
    touch  /data/filename.txt
    为filename.txt增加内容"I am studying linux."
        方法一：
            1.vim /data/filename.txt
            2.进入编辑模式 按i
            3.退出编辑模式 按esc
            4.保存并退出 :wq
            5.检查   cat /data/filename.txt
        方法二：
            echo "I am studying linux." >> /data/filename.txt
>>   追加输出重定向 把内容追加到文件的结尾
    >    重定向         先清空文件，把内容追加到文件的结尾

vi/vim快捷键：
    剪切复制粘贴
    复制当前行    yy
    粘贴          p
    剪切          dd
    其他操作
    撤销          u
    恢复         ctrl + r

把filename.txt拷贝(复制)到/tmp下
    cp /data/filename.txt  /tmp/

把 /data 移动到 /root目录下面
    mv  /data/   /root/

备份：
    cp filename.txt filename.txt.bak

重命名：
    mv filename.txt filename.avi

进入/root目录下的data目录，删除filename.txt文件
    rm filename.txt  -f

man rm：查看命令帮助

在系统中查找出名字叫 filename.txt的文件
    #find /         -type f -name "filename.txt"
    #find 在哪里找  -类型 f -名字  ""
    
    find /tmp         -type f -name "*.txt"
    
    -type  f (file)
    -type  d (dir)
    
    find /  -type f -size +1M    在根目录下找文件大小大于1M的

..   当前目录的上级目录
.    当前目录

管道
    find命令与其他命令配合
    find + |xargs
    find /root/ -type f -name "*.log" |xargs ls -l   查找root下的以.log结尾的文件，然后执行ls -l命令

打印配置文件nginx.conf内容的行号及内容，该如何做？
    seq 10 -1 1  >nginx.conf    将10-1 覆盖添加到nginx.conf
    1、cat -n nginx.conf    打印文件内容并打印行号
    2、进入vim；   :set nu  显示行号    set nonu   隐藏行号
        快速到达文件的最后一行  G
        快速到达文件的第一行    gg
        快速到达文件的某一行    10gg

递归创建目录：
    mkdir -p  /dirname/test

只查看ett.txt文件（共100行）内第20到第30行的内容
#awk   'NR==20'  ett.txt
#awk   'NR>=20 && NR<=30'  ett.txt

文件内容的替换：
    sed 's#fileboy#filegirl#g' t.sh
        xxx     yyy        file    将文件file里的xxx替换为yyy并显示

# sed -i.bak   's#fileboy#filegirl#g' t.sh
# # 先备份源文件 t.sh.bak
# # 然后修改文件内容

备份多个文件  打包压缩
    #创建压缩包
    z ==== gzip    软件进行压缩   .tar.gz
    c ==== create  打包 创建包
    v ==== verbose 显示过程
    f ==== file    指定压缩包
        tar zcf /tmp/etc.tar.gz    /etc/   将etc目录打包成etc.tar.gz
            #查看压缩包
            tar tf /tmp/etc.tar.gz

#解压-解压到当前目录
tar xf etc.tar.gz

软件安装的方法：
    yum install package
    rpm  包
    编译安装    ./configure  make   make install
