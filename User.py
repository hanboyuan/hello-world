# -*- coding=utf- 8 -*-
##########################


from Jiami import jiami
from sqlalchemy import *
from important import *
from sqlalchemy.orm import Mapper, sessionmaker

conference_url = "mysql://{0}:{1}@{2}/{3}".format(conference_username, conference_password, conference_host,
                                                  conference_dbname)


class user(object):
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def __repr__(self):
        return "%s(%r,%r)" % (self.__class__.__name__, self.user_name, self.password)


class User(object):
    def __init__(self):
        self.db = create_engine(conference_url)
        self.db.echo = False  # 如果此处设置为True的话，就会把创建数据库的sql语句显示回来
        self.meta = MetaData(self.db)
        self.users_table = Table('users', self.meta, autoload=True)
        Mapper(user, self.users_table)
        self.Session = sessionmaker(bind=self.db)
        self.session = self.Session()

    def __str__(self):
        return "%s" % (self.__class__.__name__)

    __repr__ = __str__

    def registration(self, username_argc, password_argc):
        try:
            password_argc = jiami(password_argc)
            tmp = self.session.query(user).filter(user.user_name == username_argc)
            if tmp.first():
                return False
            else:
                user_tmp = user(user_name=username_argc, password=password_argc)
                self.session.add(user_tmp)
                self.session.commit()
                return True

        except Exception, e:
            print e

    def login(self, username_argc, password_argc):
        try:
            password = jiami(password_argc)
            tmp = self.session.query(user).filter(user.user_name == username_argc)
            if tmp.first():
                db_password = tmp.one().password
                if password == db_password:
                    return True
                return False
            else:
                return False

        except Exception, e:
            print e


if __name__ == "__main__":
    '''
        注册个用户xiaobai，密码都是123456
        数据信息存取到数据库中
    '''
    a = User()

    print a.registration('xiaobai', '123456')
    print a.login('xiaobai', '123456')
