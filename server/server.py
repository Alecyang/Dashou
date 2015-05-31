# coding:utf-8


import json
import MySQLdb
from flask import Flask, request
app = Flask(__name__)


def get_database_conn():
    conn = MySQLdb.connect(host='localhost', user='root', passwd='dashou', 
        charset = 'utf8', use_unicode=False, db= 'dashou')
    return conn


@app.route('/')
def hello():
    conn = get_database_conn()
    return 'hello world'


@app.route('/logincheck', methods = ['GET', 'POST'])
def login_check():
    args = request.args if request.method == 'GET' else request.form
    user_name = args.get('username')
    passwd = args.get('passwd')
    conn = get_database_conn()
    cursor = conn.cursor()
    sql = ''' select id from user_login where 
        user_name = '%s' and passwd = '%s';''' % (user_name, passwd)
    cursor.execute(sql)
    index = cursor.fetchone()
    cursor.close()
    conn.close()
    if index:
        return '1'
    else:
        return '0'


@app.route('/registerone', methods = ['POST'])
def register_one():
    args = request.args if request.method == 'GET' else request.form
    user_name = args.get('user_name')
    passwd = args.get('passwd')
    conn = get_database_conn()
    cursor = conn.cursor()
    sql = '''select * from user_login where user_name = %s;'''
    cursor.execute(sql, (user_name, ))
    index = cursor.fetchone()
    if index:
        return '2'

    sql = '''insert into user_login (user_name, passwd) 
        values(%s, %s);'''
    try: 
        cursor.execute(sql, (user_name, passwd))
    except Exception,e :
        return '0'
    
    conn.commit()
    cursor.close()
    conn.close()
    return '1'


@app.route('/registertwo', methods = ['POST'])
def register_two():
    args = request.args if request.method == 'GET' else request.form
    user_name = args.get('user_name')
    nickname = args.get('nickname')
    grade = args.get('grade')
    school = args.get('school')
    gender = args.get('gender')
    conn = get_database_conn()
    cursor = conn.cursor()
    sql = '''insert into user_register (user_name, 
        nickname, grade, school, gender) values(%s, %s, %s, %s, %s)
        on duplicate key update nickname =%s, grade=%s, school=%s,
        gender = %s;
        ;'''
    
    try:
        cursor.execute(sql, (user_name, nickname, grade, school, gender,
            nickname, grade, school, gender))
    except:
        return '0'
    
    conn.commit()
    cursor.close()
    conn.close()
    return '1'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
