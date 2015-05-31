# coding:utf-8


import MySQLdb


def get_database_conn():
    conn = MySQLdb.connect(host='localhost', user='root', passwd='dashou', 
        charset = 'utf8', use_unicode=False, db= 'dashou')
    return conn

def execute_sql(sql, conn):
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()

# 建立登录用户密码表
def create_user_login(conn):
    sql = '''create table if not exists user_login(
        id int(16) not null auto_increment,
        user_name varchar(16) not null,
        passwd varchar(16) not null,        
        primary key (id),
        UNIQUE KEY `user_name` (user_name)
        )ENGINE=InnoDB  DEFAULT CHARSET=utf8 
        '''
    execute_sql(sql, conn)

# 建立用户注册信息表
def create_register_table(conn):
    sql = '''use dashou;
        create table if not exists user_register(
        id int(16) not null auto_increment,
        user_name varchar(16) not null,
        nickname varchar(32) default null,
        gender int(4) default null,
        school varchar(16) default null,
        grade varchar(16) default null,
        primary key (id),
        Unique key user_name (user_name)
        )ENGINE=InnoDB  DEFAULT CHARSET=utf8
        ''' 
    execute_sql(sql, conn)



if __name__ == '__main__':
    conn = get_database_conn()
    create_user_login(conn)
    create_register_table(conn)
    conn.close()
