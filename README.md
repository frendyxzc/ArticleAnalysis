# ArticleAnalysis
文本分析
`python`
`jieba`
`sklearn`
`flask`
`chartkick`

<br>
>最近在集成Tinker、在开发安卓的SDK，周末得闲跳出舒适圈研究下内容分析，基于机器学习做文本分类和文本情感倾向分析。
>
>内容分析在大众传播研究中的应用主要体现在以下几个方面：
>描述传播内容的倾向性或特征、从信息内容推测信息传播者的态度、研究媒介内容的真实性、从媒介内容推论传播效果、建立媒介效果研究的起点等。
<br>

###1.单个文本分析

####a).原始文章
>./data/2869885.html，神级逆袭！女排3-1塞尔维亚 时隔12年奥运再登顶
>![image](https://raw.githubusercontent.com/frendyxzc/ArticleAnalysis/master/screenshot/20161203202855.png)<br>

####b).Quick Start
>![image](https://raw.githubusercontent.com/frendyxzc/ArticleAnalysis/master/screenshot/20161203195514.png)<br>

####c).四组特征标签
>![image](https://raw.githubusercontent.com/frendyxzc/ArticleAnalysis/master/screenshot/20161203200223.png)<br>
>![image](https://raw.githubusercontent.com/frendyxzc/ArticleAnalysis/master/screenshot/20161203200259.png)<br>
>![image](https://raw.githubusercontent.com/frendyxzc/ArticleAnalysis/master/screenshot/20161203200330.png)<br>
>![image](https://raw.githubusercontent.com/frendyxzc/ArticleAnalysis/master/screenshot/20161203200353.png)<br>

###2.机器学习分析

####a).获取训练和测试数据
>./data/*，文本已上传，根据训练情况后续再补充，文本数据源不便公开见谅
>![image](https://raw.githubusercontent.com/frendyxzc/ArticleAnalysis/master/screenshot/20161204173310.png)<br>

####b).构建简单的朴素贝叶斯分类器进行学习和预测
>![image](https://raw.githubusercontent.com/frendyxzc/ArticleAnalysis/master/screenshot/20161204171928.png)<br>

####c).构建机器学习神经元（待实现）
>![image](https://raw.githubusercontent.com/frendyxzc/ArticleAnalysis/master/screenshot/20161203215048.png)<br>
<br>

# Todo List:
> ✔ 提取文本<br>
> ✔ 提取单个文本四组特征标签<br>
> ✔ 获取训练和测试数据，构建朴素贝叶斯分类器进行学习和预测<br>
> ✎ 构建四个神经元做机器学习<br>
> ✎ 实现文本分类<br>
> ✎ 实现文本情感倾向分析<br>