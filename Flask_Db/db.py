from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

#step1 create engine
engine = create_engine('postgresql://postgres:admin@127.0.0.1:5432/FlaskMovie')

#step2 create declarative base
Base = declarative_base(engine)


#step3 make sessionmaker
Session = sessionmaker(bind=engine)


def create_db():
    Base.metadata.create_all()

#creating models and mapping tables.
class Task(Base):
     __tablename__ = 'tasks'

     id = Column(Integer, primary_key=True)
     uid = Column(Integer)
     task = Column(String)
     status = Column(String)

     def __repr__(self):
        return "<User(id='%s', task='%s', status='%s')>" % (
                             self.id, self.task, self.status)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)


    def __repr__(self):
        return "<User(id='%s', name='%s', password='%s')>" % (
            self.id, self.name, self.password)
# def get_user(uname):
#     sql = "select * from users where name='{}'".format(uname)
#     cursor.execute(sql)
#     user = None
#     user_record = cursor.fetchone()
#     if user_record:
#
#         user = { 'id' : user_record[0],
#                  'uname' : user_record[1],
#                  'password' : user_record[2]
#                  }
#     return user


def get_users():
    session = Session()
    users = session.query(Task)
    for user in users:
        print("{}, {}".format(user.id, user.task))

def get_details():
    session = Session()
    users = session.query(User)
    for user in users:
        print("{}, {},{}".format(user.id,user.name,user.password))



def updatetasks(id, task):
       session = Session()
       user = session.query(Task).filter_by(id=id).first()

       if task:
         user.task = task
         session.commit()
       #print("Updated !!")
       return "Updated"

if __name__ == '__main__':
    import pdb; pdb.set_trace()