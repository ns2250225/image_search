# -*- coding:utf-8 -*-
# Step2.py:根据单词文件，将图片单词入sqlite数据库
import pickle
import sift
import imagesearch
import imtools

# 图片名字的列表
imlist = imlist = imtools.get_imlist('static/')
# 图片的数量
nbr_images = len(imlist)
# 对应图片特征文件的列表
featlist = [ imlist[i][:-3]+'sift' for i in range(nbr_images)]

# 载入单词文件
# 将单词，图片名，地址存进数据库images.db
with open('vocabulary.pkl', 'rb')as f:
    voc = pickle.load(f)

indx = imagesearch.Indexer('images.db', voc)
indx.create_tables()

for i in range(nbr_images):
    locs,descr = sift.read_features_from_file(featlist[i])
    indx.add_to_index(imlist[i],descr)

indx.db_commit()

