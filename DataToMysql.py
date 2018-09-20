import pymysql


class DataToMysql:
    def __init__(self, host='127.0.0.1', port=3306, user=None, passwd=None, db=None, charset='utf8'):
        try:
            self.conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db, charset=charset)  # 链接数据库
            self.cursor = self.conn.cursor()
        except pymysql.Error as e:
            print("数据库连接信息报错")
            raise e

    def write(self, table_name, info_dict):
        """
        根据table_name与info自动生成建表语句和insert插入语句
        :param table_name: 数据需要写入的表名
        :param info_dict: 需要写入的内容，类型为字典
        :return:
        """
        sql_key = ''  # 数据库行字段
        sql_value = ''  # 数据库值
        for key in info_dict.keys():  # 生成insert插入语句
            sql_value = (sql_value + '"' + pymysql.escape_string(str(info_dict[key])) + '"' + ',')
            sql_key = sql_key + ' ' + key + ','
        insert_sql = f"INSERT INTO {table_name} ({sql_key[:-1]}) VALUES ({sql_value[:-1]})"
        try:
            self.cursor.execute(insert_sql)
            self.conn.commit()  # 提交当前事务
        except pymysql.Error as e:
            if e.args[0] == 1146:  # 当表不存在时，生成建表语句并建表
                sql_key_str = ''  # 用于数据库创建语句
                columnStyle = ' text'  # 数据库字段类型
                for key in info_dict.keys():
                    sql_key_str = sql_key_str + ' ' + key + columnStyle + ','
                self.cursor.execute(f'CREATE TABLE {table_name} ({sql_key_str[:-1]})')
                self.cursor.execute(insert_sql)
                self.conn.commit()  # 提交当前事务
            else:
                print('写入失败')
                raise e


if __name__ == '__main__':
    mysql = DataToMysql('localhost', 3306, 'root', '', 'hsw')
    di = {'title': '易刚：增加外汇市场深度 降低外汇市场的顺周期性', 'content': '\u3000\u30009月16日，纪念中国改革开放四十年暨50人论坛成立二十周年学术研讨会在北京举行。 上海证券报图', 'get_time': '2018-09-17 09:16:58'}
    mysql.write('shw_itemddd', di)
