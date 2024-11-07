import pymysql

class SQL_querys():

    def __init__(self):
        self.connected = pymysql.connect(host='sql7.freesqldatabase.com', user='sql7743092', passwd='7cL2iyGXM6', db='sql7743092')
        self.UserName = 'Gérard'

    def deconection(self):
        self.connected.close()

    def insert(self,difficulty,highest_combo,score):
        cursor = self.connected.cursor()
        sql_query = f"INSERT INTO Leaderboard_Data_Base(UserName,Difficulty,Highest_Combo,Score) VALUES ('{self.UserName}','{difficulty}',{highest_combo},{score});"
        cursor.execute(sql_query)
        self.connected.commit()
        cursor.close()

    def get_first_ten(self):
        cursor = self.connected.cursor()
        sql_query = f"SELECT UserName,Difficulty,Highest_Combo,Score FROM Leaderboard_Data_Base ORDER BY Score DESC, Highest_Combo DESC,Difficulty DESC LIMIT 10;"
        cursor.execute(sql_query)
        top_10_leaderboard = cursor.fetchall()
        cursor.close()
        return top_10_leaderboard