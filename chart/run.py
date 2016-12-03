from flask import Flask, jsonify, render_template, request  
import chartkick
import re
import json
import sys

reload(sys);
sys.setdefaultencoding('utf-8');
  
app = Flask(__name__, static_folder=chartkick.js());
app.jinja_env.add_extension("chartkick.ext.charts");

file_name_1 = sys.argv[1]
file_name_2 = sys.argv[2]

class CCode:  
	def str(self, content, encoding='utf-8'):  
		return json.dumps(content, encoding=encoding, ensure_ascii=False, indent=4)  
		pass
	pass
 
@app.route('/')  
@app.route('/index')  
def index():
	cCode = CCode();
	
	# file 1
	#results = file('../result/2869885_tags.txt').read();
	file_name = file_name_1;
	results = file(file_name + '.txt').read();
	pattern = re.compile(r'(.+?),(.+?);', re.S);
	datas = re.findall(pattern, results);
	dict_1 = {};
	for data in datas:
		dict_1[data[0]] = data[1];
	
	results = file(file_name + '_a.txt').read();
	pattern = re.compile(r'(.+?),(.+?);', re.S);
	datas = re.findall(pattern, results);
	dict_2 = {};
	for data in datas:
		dict_2[data[0]] = data[1];
		
	results = file(file_name + '_ns.txt').read();
	pattern = re.compile(r'(.+?),(.+?);', re.S);
	datas = re.findall(pattern, results);
	dict_3 = {};
	for data in datas:
		dict_3[data[0]] = data[1];

	results = file(file_name + '_v.txt').read();
	pattern = re.compile(r'(.+?),(.+?);', re.S);
	datas = re.findall(pattern, results);
	dict_4 = {};
	for data in datas:
		dict_4[data[0]] = data[1];

	return render_template('index.html', datas_1=cCode.str(dict_1), datas_2=cCode.str(dict_2), datas_3=cCode.str(dict_3), datas_4=cCode.str(dict_4));
  
  
if __name__ == "__main__":  
    app.run(debug=True);