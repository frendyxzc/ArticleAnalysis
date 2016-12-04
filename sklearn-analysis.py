# coding: utf-8
__author__ = 'frendy'

import pandas as pd
import jieba
import numpy
import traceback
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.svm import LinearSVC

channels = [1, 2, 21, 23];

if __name__ == "__main__":
	# 加载数据
	tmp_tags = [];
	tmp_words = [];
	for channel in channels:
		content = open('./result/newsid_' + str(channel) + '.txt', 'rb').read();
		ids = content.split(',');
		print 'Channel ' + str(channel) + ' number of sample: %d' % len(ids);
		
		for id in ids:
			try:
				content = open('./data/' + id + '.txt', 'rb').read();
				tmp_tags.append(channel);
				tmp_words.append(content);
			except:
				#traceback.print_exc();
				if id != "":
					print 'Error: ' + str(id);
				
	# 数据预处理
	tags = pd.Series(tmp_tags);
	words = pd.Series(tmp_words);

	# 生成训练集和测试集
	train_tags, test_tags = train_test_split(tags, test_size=0.2);
	train_words, test_words = train_test_split(words, test_size=0.2);
	print "Number of train set: %d; Number of test set: %d" % (len(train_words), len(test_words));

	# 分词
	comma_tokenizer = lambda x: jieba.cut(x, cut_all=True)
	vectorizer = TfidfVectorizer(tokenizer=comma_tokenizer)
	train_data = vectorizer.fit_transform(train_words)
	test_data = vectorizer.transform(test_words)

	# 分类
	# clf = LogisticRegression()
	clf = MultinomialNB(alpha=0.01)
	# clf = svm.SVC()
	# clf = LinearSVC()
	clf.fit(train_data, numpy.asarray(train_tags))

	# 验证
	actual = numpy.asarray(test_tags)
	pred = clf.predict(test_data)
	m_precision = metrics.precision_score(actual, pred)
	m_recall = metrics.recall_score(actual, pred)
	print 'Precision: {0:.3f}'.format(m_precision)
	print 'Recall: {0:0.3f}'.format(m_recall)
