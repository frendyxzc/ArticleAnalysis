import sys
sys.path.append('../')

import jieba
import jieba.analyse
from optparse import OptionParser

USAGE = "usage:    python extract_tags.py [file name] -k [top k]"

parser = OptionParser(USAGE)
parser.add_option("-k", dest="topK")
opt, args = parser.parse_args()


if len(args) < 1:
    print(USAGE)
    sys.exit(1)

file_name = args[0]

if opt.topK is None:
    topK = 10
else:
    topK = int(opt.topK)

content = open(file_name, 'rb').read()

# total
tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=True)
#for tag in tags:
#	print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))
result_file_name = file_name.split('/')[2].split('.')[0];
f=file('./result/' + result_file_name + '_tags.txt',"w+");
for tag in tags:
	f.writelines(tag[0] + ',' + bytes(tag[1]) + ';');
f.close();

# detail a
tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=True, allowPOS=('a'))
#for tag in tags:
#	print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))
f=file('./result/' + result_file_name + '_tags_a.txt',"w+");
for tag in tags:
	f.writelines(tag[0] + ',' + bytes(tag[1]) + ';');
f.close();

# detail ns
tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=True, allowPOS=('ns'))
#for tag in tags:
#	print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))
f=file('./result/' + result_file_name + '_tags_ns.txt',"w+");
for tag in tags:
	f.writelines(tag[0] + ',' + bytes(tag[1]) + ';');
f.close();

# detail v
tags = jieba.analyse.extract_tags(content, topK=topK, withWeight=True, allowPOS=('v'))
#for tag in tags:
#	print("tag: %s\t\t weight: %f" % (tag[0],tag[1]))
f=file('./result/' + result_file_name + '_tags_v.txt',"w+");
for tag in tags:
	f.writelines(tag[0] + ',' + bytes(tag[1]) + ';');
f.close();