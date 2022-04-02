# -*- coding: utf-8 -*-


import gensim


class Word2VecSynonym:
    def __init__(self, word_embedding_path, topn=10):
        print("loading word embedding ......")
        self.word_embedding = gensim.models.KeyedVectors.load_word2vec_format(word_embedding_path, binary=False)
        self.topn = topn
        print("DONE !!!")

    def synonym(self, words):
        try:
            ret = self.word_embedding.most_similar(words, topn=self.topn)
        except:
            ret = []
        return ret
# if __name__ == '__main__':
#     # 加载词向量
#     word2vec = Word2VecSynonym(word_embedding_path="./test_data/sgns.target.word-word.dynwin5.thr10.neg5.dim300.iter5",
#                                topn=5)
#     # 生成同义词
#     ret = word2vec.synonym("苹果")
#     print(ret)
#     ret = word2vec.synonym("上海")
#     print(ret)
####===================================================================================================================================
####===================================================================================================================================
####===================================================================================================================================
####===================================================================================================================================
# https://zhuanlan.zhihu.com/p/125649158
# 小白篇--3分钟学会使用word2vec词向量计算
# 小舰
# 中国人民大学 计算机应用技术硕士
# #
# 用word2vec计算词向量，对于研究机器学习相关的同学来说很简单，但如果你是一个后端/前端或者各种端的开发者，可能只知道它，偶尔会用到它，那么怎么使用呢？
# 我们最常听或者常说的可能就是：
# “你能不能给我一个API，我输入一个词能够给我返回一个词的向量值；我输入两个值能够给我返回这两个词的相似度...“
# 嗯，现在我就是简单的来回答这样一个问题，而不是讲解word2vec。
# 1.库准备
# pip install gensim
# 2.最全的中文词向量下载【自家师兄的工作】
# https://github.com/Embedding/Chinese-Word-Vectors
# 假设你下载了下面 这个词向量包
# 解压一下，然后准备工作就做完啦～
# #3.使用
# 3.1 模型预加载：
# 先进行模型加载，等加载完毕就可以使用了，根据你机器性能有快有慢，我大约一分钟才OK##===================================
# import gensim.models.keyedvectors as word2vec
# model_baike = word2vec.KeyedVectors.load_word2vec_format('/你的目录/sgns.target.word-word.dynwin5.thr10.neg5.dim300.iter5',binary=False, encoding="utf8",  unicode_errors='ignore')
# print('loading finished!')
# 3.2 调用“API”
# 需求1：输入一个词，输出这个词的词向量
# #输入 ‘服装’
# print(model_baike.wv['服装'])
# 需求2:输入两个词，求出这两个词的相似度
# #输入 “服装” “女装”
# model_baike.similarity(u"服装",u"女装")
# 需求3:求一个词最相似的几个词
# #输入 “服装” 3  =>最相似的3个词
# model_baike.most_similar(u'服装',topn = 3)




