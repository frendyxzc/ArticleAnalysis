# coding: utf-8
__author__ = 'frendy'

channels = ['1', '2', '21', '23'];

for channel in channels:
	content = open("./result/newsid_" + channel + ".txt", 'rb').read();
	ids = content.split(',');

	list = [];
	for id in ids:
		if id not in list:
			list.append(id);
			
	# save in file
	f = file("./result/newsid_" + channel + ".txt", "w+");
	for item in list:
		f.write(str(item) + ",");
	f.close();
	
print "finished to clean data"