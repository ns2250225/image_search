# 用图片单词搜索相似的图片
## 准备文件 ##
- vlfeat：解压完之后把bin目录加到系统Path中，确保cmd能执行sift命令
- pysqlite：pip install pysqlite
- cherryPy：pip install cherrypy
- matplotlib：pip install matplotlib
- PIL：pip install pil

## 使用方法 ##
- 修改好service.conf中的网页跟目录路径,即本文件夹的路径
- 执行Step1.py，生成单词文件
- 执行Step2.py, 生成数据库
- 执行Step3.py，开启cherryPy服务器
- 浏览：127.0.0.1:8080


##注意##
- 尽量使用CMD命令执行.py文件，不然容易出错
