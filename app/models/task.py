from app import db


class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True )
    title = db.Column(db.String)
    description = db.Column(db.String)
    completed_at = db.Column(db.DateTime, nullable=True, default=None)



    def to_dict(self):
        is_complete=True if self.completed_at else False 
        """
        if self.completed_at:
            is_complete = True
        else:
            is_complete = False
        """
        return{
            "id":self.task_id,
            "title":self.title,
            "description":self.description,
            "is_complete":is_complete
        }



