# voters.py
import datetime

class Person(object):
    def __init__(self):
        self.name = ''
        self.dob = None
        self.gender = ''
        
    @property
    def age(self):
        if self.dob is not None:
            return (datetime.datetime.now() - self.dob).days/365
        else:
            return None

    def save(self):
        try:
            connection = sqlite3.connect('voters.db')
            sql = """
                INSERT INTO people
                (name, dob, gender)
                values (?, ?, ?);
            """
            connection.execute(sql, (self.name, self.dob, self.gender))
            connection.commit()
        except sqlite3.IntegrityError:
            pass
#            print self.number, "already added"    
        
        connection.close        
        
        
    @staticmethod
    def CreateTable():
        sql = """
            create table 
            people 
            (
                id integer primary key autoincrement not null, 
                name text not null, 
                dob date not null, 
                gender varchar(1) not null
            );
        """