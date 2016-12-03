#!/usr/bin/python
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


soup = BeautifulSoup(open("./data/2869885.html"));

f=file('./data/2869885.txt',"w+");
f.write(soup.div.get_text());
f.close();


soup = BeautifulSoup(open("./data/4634116.html"));

f=file('./data/4634116.txt',"w+");
f.write(soup.div.get_text());
f.close();