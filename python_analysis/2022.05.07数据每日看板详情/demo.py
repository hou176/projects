import pandas as pd 
import numpy as np 
import matplotlib
import pymysql
import time



def jdt_db(sql):
	start_time  = time.time()
	jdt_db_data = pymysql.connect(host='172.16.1.231',user='jdys_select',password ='jdys_select2020' ,db= 'jdt_db',charset = 'utf8')
	data = pd.read_sql(sql,jdt_db_data)
	elapsed = (time.time() - start_time)
	print(elapsed)
	return data



