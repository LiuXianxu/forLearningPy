#搭建virtualenv环境，解决多个项目不用同一个python版本的问题
# sudo pip3 install virtualenv    
#用镜像源 下载网速更快
# sudo pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple virtualenv
#查看virtualenv的版本 pip3 freeze | grep virtualenv
#在当前目录下创建 env 虚拟环境  -p 选择python版本 venv虚拟环境名称
# virtualenv -p python3 venv
#在当前目录下激活虚拟环境
# source ./venv/bin/activate
#进入虚拟环境后命令行提示符前面有虚拟环境的名称
#在虚拟环境中安装flask
# pip3 install flask

