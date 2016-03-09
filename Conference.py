# -*- coding=utf- 8 -*-
##########################

from sqlalchemy import *
from important import *
from sqlalchemy.orm import Mapper, sessionmaker

conference_url = "mysql://{0}:{1}@{2}/{3}".format(conference_username, conference_password, conference_host,
                                                  conference_dbname)


class conference(object):
    def __init__(self, conference_item, conference_date, conference_person_num, conference_added_person):
        self.conference_item = conference_item
        self.conference_date = conference_date
        self.conference_person_num = conference_person_num
        self.conference_added_person = conference_added_person

    def __repr__(self):
        return "%s(%r,%r,%r)" % (
            self.__class__.__name__, self.conference_item, self.conference_date, self.conference_person_num)


class Conference(object):
    def __init__(self, name):
        self.name = name
        self.db = create_engine(conference_url)
        self.db.echo = False  # 如果此处设置为True的话，就会把创建数据库的sql语句显示回来
        self.meta = MetaData(self.db)

    def __str__(self):
        return "%s" % (self.__class__.__name__)

    __repr__ = __str__

    def __session(self):
        conferences_table = Table('conferences', self.meta, autoload=True)
        Mapper(conference, conferences_table)
        Session = sessionmaker(bind=self.db)
        session = Session()
        return session

    def publish(self, conference_item, conference_date, conference_person_num):
        try:
            session = self.__session()
            tmp = session.query(conference).filter(conference.conference_item == conference_item)
            if tmp.first():
                return False
            else:
                conference_tmp = conference(conference_item=conference_item, conference_date=conference_date,
                                            conference_person_num=conference_person_num,
                                            conference_added_person='%s' % self.name)
                session.add(conference_tmp)  # 数据的插入
                session.commit()
                return True


        except Exception, e:
            print e

    def add_conference(self, conference_item):
        try:
            session = self.__session()
            tmp = session.query(conference).filter(conference.conference_item == conference_item)  # 数据的查
            result = tmp.first()
            if result:
                current_add = result.conference_added_person.split()
                if self.name not in current_add:
                    current_add.append(self.name)
                    current_add_str = " ".join(current_add)
                    session.query(conference).filter(conference.conference_item == conference_item).update(
                            {'conference_added_person': current_add_str})  # 数据的改
                    session.commit()
                    return True, current_add_str
                else:
                    return False
            else:
                return False

        except Exception, e:
            print e


if __name__ == "__main__":
    '''

    '''
    a = Conference('xiaobai1')
    b = Conference('xiaobai2')
    c = Conference('xiaobai3')

    # print a.publish('Python核心编程', '2016-3-9 16:00', 30)
    print a.publish('Python-flask2', '2016-3-10 16:00', 30)
    # # print a.add_conference('Python-flask')
    # print b.add_conference('Python-flask')
    # print b.add_conference('Python核心编程')
    #print c.publish('Python-flaskxxxx', '2016-3-10 16:00', 30)
    print c.add_conference('Python-flask2')
