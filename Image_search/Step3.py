# -*- coding:utf-8 -*-
# Step3.py：用cherryPy做交互界面，显示结果
import cherrypy, os, urllib, pickle
import imtools
from numpy import *
import imagesearch

# cherryPy页面
# 网页根目录在配置文件service.conf中设置
# 默认端口是8080
class SearchImage:
    
    def __init__(self):
        # 加载图片名字列表
        self.imlist = imtools.get_imlist('static/')
        self.nbr_images = len(self.imlist)
        self.ndx = range(self.nbr_images)
        
        # 加载生成好的单词文件
        f = open('vocabulary.pkl', 'rb')
        self.voc = pickle.load(f)
        f.close()
        
        # 设置开始显示的图片数目
        self.maxres = 15
        
        # 设置页面的结构
        self.header = """
            <!doctype html>
            <head>
            <title>Image Search</title>
            </head>
            <body>
            """
        self.footer = """
            </body>
            </html>
            """

    # 响应index页面
    # 没有搜索的时候随机显示图片
    # 搜索的时候显示与该图片相似的图片，根据视觉单词
    def index(self,query=None):
        self.src = imagesearch.Searcher('images.db', self.voc)
        
        html = self.header
        html += """
            <br />
            Please click a image to shearch Or Show <a href='?query='> random images. </a> 
            <br /><br />
            """
        if query:
            # 显示查询结果的图片
            res = self.src.query(query)[:self.maxres]
            for dist,ndx in res:
                imname = self.src.get_filename(ndx)
                html += "<a href='?query="+imname+"'>"
                html += "<img src='"+imname+"' width='100' />"
                html += "</a>"
        else:
            # 随机显示图片
            random.shuffle(self.ndx)
            for i in self.ndx[:self.maxres]:
                imname = self.imlist[i]
                html += "<a href='?query="+imname+"'>"
                html += "<img src='"+imname+"' width='100' />"
                html += "</a>"
                
        html += self.footer
        return html
    
    index.exposed = True

# 启动应用
cherrypy.quickstart(SearchImage(), '/', os.path.join(os.path.dirname(__file__), 'service.conf'))
