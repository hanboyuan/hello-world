from important import *
from sqlalchemy import *
db = create_engine("mysql://{0}:{1}@{2}/conference".format(conference_username, conference_password, conference_host))
meta = MetaData(db)
db.echo = True
users_table = Table('users', meta,
                    Column('user_name', String(40), primary_key=True),
                    Column('password', String(40))
                    )
users_table.create()
conference_table = Table('conferences', meta,
                         Column('conference_item', String(40),primary_key=True),
                         Column('conference_date', String(40)),
                         Column('conference_person_num', Integer),
                         Column('conference_added_person',String(1000))
                         )
conference_table.create()
