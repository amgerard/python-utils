
def restore_mysql_column(host, user, passwd, db, dump_file_path, table, column, columnIndex):
	import MySQLdb
	import re

	db = MySQLdb.connect(host=host, user=user, passwd=passwd, db=db)
	cur = db.cursor()
	#x = cur.fetchall();

	with open(dump_file_path, 'r') as f:
		data = f.read()
		items = re.findall('\((.+?)\)', data)
		for itemStr in items:
			item = itemStr.split(',')
			id = item[0]
			value = item[columnIndex]
			update_sql = 'update ' + table + ' set ' + column + ' = ' + value + ' where Id = ' + id + ';'
			print update_sql
			cur.execute(update_sql)
	db.commit()
	db.close()
