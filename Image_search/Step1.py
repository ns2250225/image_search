# -*- coding:utf-8 -*-
import pickle
import vocabulary
import imtools
import sift

# imlist是图片名字的列表，图片放在static文件夹下
imlist = imtools.get_imlist('static/')

# 图片的总数
nbr_images = len(imlist)

# 将每张图片的特征点存放进对应的.sift特征文件中
featlist = [ imlist[i][:-3]+'sift' for i in range(nbr_images)]

for i in range(nbr_images):
        sift.process_image(imlist[i], featlist[i])

# 利用k-means对图片特征文件聚类训练出对应的单词
# 时间关系，这里只用了46张图做例子，所以只创建46个单词
voc = vocabulary.Vocabulary('imagewords')
voc.train(featlist, 46, 10)

# 将单词都保存到vocabulary.pkl中
with open('vocabulary.pkl', 'wb') as f:
	pickle.dump(voc,f)

print 'vocabulary is:', voc.name, voc.nbr_words

