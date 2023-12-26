from datetime import datetime

from dbconfig import db


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime)

    def __repr__(self):
        # This represents how you want to see task and date information after a query.
        return '<Task: {task}, Created Date: {created_date}>'.format(task=self.task, created_date=self.created_date)
