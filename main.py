from database import engine,LocalSession
from models import Base, User, Task


Base.metadata.create_all(engine)


def add_user():
    
    session = LocalSession()
    
    user = User(
        telegram_id=45345234,
        first_name = "Ali",
        
    )
    
    user01 = User(
        telegram_id=45334,
        first_name = "Vali",
        
    )
    
    user02 = User(
        telegram_id=4534,
        first_name = "Xohha",
        
    )
    session.add_all([user,user01,user02])
    session.commit()
    session.refresh(user)


def update_user():
    
    session = LocalSession()
    
    user = session.query(User).filter(User.id==2).first()
    user.first_name = "Joxa"
    
    
    session.commit()

def add_task():
    
    session = LocalSession()
    
    tasks = Task(
        name = "Yugurush",
        user_id = 1,
        
    )
    
    tasks01 = Task(
        name = "Uyqu ",
        user_id = 2,
        
    )
    
    tasks02 = Task(
        name="Kitob oqish",
        user_id = 3
    )
    
    session.add_all([tasks,tasks01,tasks02])
    session.commit()

# add_user()
# add_task()
    
update_user()