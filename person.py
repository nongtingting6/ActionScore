import datetime
class Person:

    def __init__(self,score):
        self.score = score
        self.action_and_time=[]



    def action(self, action_id):

        action_score = {'1': 4, '2': 5}

        cur_score=action_score.get(action_id,0)
        cur_day=str(datetime.datetime.now())
        cur_time = cur_day.split(".")[0]

        self.score=self.score+cur_score
        self.action_and_time = self.action_and_time + [action_id,str(cur_time)]


