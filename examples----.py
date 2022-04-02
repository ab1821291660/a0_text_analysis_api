# -*- coding: utf-8 -*-
from text_analysis_api import KmeansClustering
from text_analysis_api import DbscanClustering
#
#
#
#
from text_analysis_api import Fasttext
from text_analysis_api import SentimentAnalysis
from text_analysis_api import CosionSimilarity
from text_analysis_api import EditSimilarity
from text_analysis_api import SimHashSimilarity
#
from text_analysis_api import TripleExtraction
#
#caption
#
#mrc
#
from text_analysis_api import TfidfSummarization
from text_analysis_api import TextRankSummarization
#
#
#
#
from text_analysis_api import SpellCorrect

from text_analysis_api import TfidfKeywords
from text_analysis_api import TextRankKeywords
from text_analysis_api import KeyPhraseExtraction
from text_analysis_api import TopicKeywords

from text_analysis_api import Word2VecSynonym
from text_analysis_api import SynonymDict



"""
文本聚类：
kmeans_cluster
dbscan_cluster
"""
def kmeans_cluster(data_path="./test_data/test_data_cluster.txt",
                   n_clusters=5):
    """
    KMEANS文本聚类
    :param data_path: 需要聚类的文本路径，每条文本存放一行
    :param n_clusters: 聚类个数
    :return: {'cluster_0': [0, 1, 2, 3, 4], 'cluster_1': [5, 6, 7, 8, 9]}   0,1,2....为文本的行号
    """
    Kmeans = KmeansClustering()
    result = Kmeans.kmeans(data_path, n_clusters=n_clusters)
    print("keams result: {}\n".format(result))


def dbscan_cluster(data_path="./test_data/test_data_cluster.txt",
                   eps=0.05, min_samples=3, fig=False):
    """
    基于DBSCAN进行文本聚类
    :param data_path: 文本路径，每行一条
    :param eps: DBSCA中半径参数
    :param min_samples: DBSCAN中半径eps内最小样本数目
    :param fig: 是否对降维后的样本进行画图显示，默认False
    :return: {'cluster_0': [0, 1, 2, 3, 4], 'cluster_1': [5, 6, 7, 8, 9]}   0,1,2....为文本的行号
    """
    dbscan = DbscanClustering()
    result = dbscan.dbscan(corpus_path=data_path, eps=eps, min_samples=min_samples, fig=fig)
    print("dbscan result: {}\n".format(result))




"""
文本分类
"""
def fasttext_classification():
    """
     fasttext 文本分类
    fasttext
        :param save_model_path: 模型保存路径
        :param train_data_path: 训练样本路径
        :param test_data_path: 测试样本路径
        :param type: 模式：“train/predict”
        :param k: 返回结果个数
        :param threshold: 阈值
        :param epoch: 训练轮数
        :param pretrainedVectors: 预训练词向量路径
        :param label: 标签前缀
        :param lr: 学习率
        :param dim: 词向量维度
    """
    # Train model
    train_data_path = "./test_data/test_fasttext_cls.txt"
    test_data_Path = train_data_path
    save_model_path = "fasttext.model.bin"
    fasttext = Fasttext(train_data_path=train_data_path, test_data_path=test_data_Path,
                        save_model_path=save_model_path, type="train")
    fasttext.train()

    # Predict
    save_model_path = "fasttext.model.bin"
    fasttext = Fasttext(save_model_path=save_model_path, type="predict", k=2, threshold=0.0)
    ret = fasttext.predict(["黄蜂 vs 湖人 首发 ： 科比 冲击 七 连胜   火箭 两旧 将 登场 新浪 体育讯 北京 时间 3 月 28 日 ， NBA 常规赛 洛杉矶 湖人",
                            "历届 华表奖 新人 浮沉 录 ： 曾经 新 丁 今何在 ？ 新浪 娱乐 讯   近日 ， 第十四届 华表奖 十八个 奖项 提名 名单 公布 "],
                           )
    print(ret)

"""
情感分析--情感词典方法
"""
def sentiment_analysis():
    senti = SentimentAnalysis()
    senti = senti.analysis("今天天气好晴朗")
    print("sentiment result: {}".format(senti))

"""
文本相似性
cosion_sismilarity
edit_similarity
simhash_similarity
"""
def cosion_sismilarity():
    """
    基于余弦计算文本相似性
    :return: 余弦值
    """
    text1 = "小明，你妈妈喊你回家吃饭啦"
    text2 = "回家吃饭啦，小明"
    cosion = CosionSimilarity()
    similiar = cosion.similarity(text1, text2)
    print("cosion similarity result: {}\n".format(similiar))
def edit_similarity():
    """
    采用编辑距离计算文本之间的相似性
    :return: 编辑距离
    """
    edit = EditSimilarity()
    edit_dis = edit.edit_dist("abc", "ab")
    print("edit distance: {}\n".format(edit_dis))
def simhash_similarity():
    """
    采用simhash计算文本之间的相似性
    :return:
    """
    simhash = SimHashSimilarity()
    sim = simhash.run_simhash("你妈妈叫你回家吃饭了，小明", "小明, 妈妈让你回家吃饭了")
    print("simhash result: {}\n".format(sim))



"""
文本三元组抽取
"""
def triple_extraction():
    text = "履行反洗钱义务的机构及其工作人员依法提交大额交易和可疑交易报告，受法律保护。"
    extractor = TripleExtraction()
    res = extractor.triples_main(text)
    print(res)
    # ---------------------------------------------
    #Downloading: 100%|██████████| 164M/164M [02:24<00:00, 1.14MB/s]##===================================默认下载到win这个位置C:\Users\tianxia\.cache\torch\ltp
    # 履行反洗钱义务的机构及其工作人员依法提交大额交易和可疑交易报告，受法律保护。
    # [['机构及其工作人员', '履行', '反洗钱义务'],
    #  ['履行反洗钱义务机构及其工作人员', '提交', '大额交易和可疑交易报告'],
    #  ['履行反洗钱义务机构及其工作人员', '受', '法律保护']]
    # ---------------------------------------------

"""
caption
"""



"""
mrc
"""



"""
文本摘要
tfidf_summarization
"""
def tfidf_summarization(ratio=0.2):
    """
    采用tfidf进行摘要抽取
    :param ratio: 摘要占文本长度的比例
    :return:
    """
    with open('./test_data/test_summarization.txt', encoding="utf-8") as f:
        doc = f.read()
    summ = TfidfSummarization(ratio=ratio)
    summ = summ.analysis(doc)
    print("tfidf summarization result: {}\n".format(summ))

def textrank_summarization(ratio=0.2):
    """
    采用tfidf进行摘要抽取
    :param ratio: 摘要占文本长度的比例
    :return:
    """
    with open('./test_data/test_summarization.txt', encoding="utf-8") as f:
        doc = f.read()
    summ = TextRankSummarization(ratio=ratio)
    summ = summ.analysis(doc)
    print("textrank summarization result: {}\n".format(summ))
####===================================================================================================================================
####===================================================================================================================================
####===================================================================================================================================
####===================================================================================================================================
####===================================================================================================================================
####===================================================================================================================================
####===================================================================================================================================
####===================================================================================================================================
"""
文本纠错
"""
def spell_correct(corpus_path="./test_data/水浒传.txt",
                  train=True, ret_num=10, model_dir="./spell_correct_model"):
    """
    中文文本纠错
    :param corpus_path: 训练文本路径，这里以水浒传作为测试
    :param train: 是否进行训练
    :param ret_num: 按照可能性返回纠错后词汇
    :param model_dir: 训练后生成文件存储路径
    :return:
    """
    spell_correct = SpellCorrect(corpus_path=corpus_path, train=train, ret_num=ret_num, model_dir=model_dir)
    ret1 = spell_correct.correct('松江')
    ret2 = spell_correct.correct('李奎')
    print("spell correct result: {}=>{}  {}=>{}\n".format('松江', ret1, '李奎', ret2))


"""
关键词抽取
"""
def tfidf_keywords(delete_stopwords=True, topK=20, withWeight=True):
    """
    tfidf 提取关键词
    :param delete_stopwords: 是否删除停用词
    :param topK: 输出关键词个数
    :param withWeight: 是否输出权重
    :return: [(word, weight), (word1, weight1)]
    """
    tfidf = TfidfKeywords(delete_stopwords=delete_stopwords, topK=topK, withWeight=withWeight)
    keywords = tfidf.keywords("小明的妈妈让你回家吃饭了")
    print("tfidf keywords result: {}\n".format(keywords))
def textrank_keywords(delete_stopwords=True, topK=20, withWeight=True):
    """
    tfidf 提取关键词
    :param delete_stopwords: 是否删除停用词
    :param topK: 输出关键词个数
    :param withWeight: 是否输出权重
    :return: [(word, weight), (word1, weight1)]
    """
    textrank = TextRankKeywords(delete_stopwords=delete_stopwords, topK=topK, withWeight=withWeight)
    keywords = textrank.keywords("小明的妈妈让你回家吃饭了")
    print("textrank keywords result: {}\n".format(keywords))
"""
关键短语抽取
"""
def keyphrase_extract(topk=100, method='tfidf', with_word=True, save_pic="./wordcloud.png", with_mask=True):
    """
    关键短语抽取
    :param topk: 提取多少关键词组成短语
    :param method: 提取关键词的方法
    :param with_word: 关键词是否作为短语进行输出
    :param save_pic: 是否生成词云图片，保存路径
    :param with_mask: 生成图片是否使用背景
    :return:
    """
    with open('./test_data/test_keyphrase.txt', encoding='utf-8') as f:
        text = f.read()
    key_phrase_extractor = KeyPhraseExtraction(topk=topk, method=method, with_word=with_word)
    key_phrase = key_phrase_extractor.key_phrase_extraction(text)
    print("keyphrase result: {}\n".format(key_phrase))
    if save_pic:
        key_phrase_extractor.wordcloud(key_phrase, save_path=save_pic, with_mask=True)
        print("word cloud save to: {}\n".format(save_pic))
"""
主题关键词提取
"""
def topic_keywords(n_components=5, n_top_words=10, max_iter=10):
    """
    根据LDA，提取文本主题关键词
    :param train_data: 文本数据，列表格式, 每条文本一行
    :param n_components: 划分成多少个主题
    :param n_top_words: 每个主题提取多少个关键词
    :param max_iter: 训练迭代次数
    :return:
    """
    with open('./test_data/test_data_cluster.txt', encoding='utf-8') as f:
        train_data = f.readlines()
    topic_keywords = TopicKeywords(train_data=train_data, n_components=n_components,
                                   n_top_words=n_top_words, max_iter=max_iter)
    keywords = topic_keywords.analysis()
    print("topic keywords: {}\n".format(keywords))


"""
同义词，近义词
word2vec_synonym: 采用预训练词向量，生成同义词、近义词
synonym_dict: 根据词典返回同义词(收集词数较少...)
"""

def word2vec_synonym():
    """
    word_embedding_path: 预训练词向量路径，由于词向量太大，需用户自己下载
                        下载参考：https://github.com/Embedding/Chinese-Word-Vectors
    topn: 返回同义词个数
    :return: 同义词列表 [(word, score)],若查询词在词向量词表中不存在，返回[].
    """
    # 加载词向量
    word2vec = Word2VecSynonym(word_embedding_path="./test_data/sgns.target.word-word.dynwin5.thr10.neg5.dim300.iter5",
                               topn=5)
    # 生成同义词
    ret = word2vec.synonym("苹果")
    print(ret)
    ret = word2vec.synonym("上海")
    print(ret)
def synonym_dict():
    """
    若词典中不存在查询词，返回[]
    :return:
    """
    synonym = SynonymDict()
    ret = synonym.synonym("狗仗人势")
    print(ret)
    ret = synonym.synonym("人才济济")
    print(ret)
####===================================================================================================================================
####===================================================================================================================================
####===================================================================================================================================
####===================================================================================================================================
####===================================================================================================================================
####===================================================================================================================================
####===================================================================================================================================
####===================================================================================================================================
if __name__ == "__main__":
    word2vec_synonym()##===================================#loading word embedding ......





