import pandas as pd

def playerstats(name):
    
    url = 'https://www.pro-football-reference.com/players/M/MurrKy00.htm'
    df = pd.read_html(url)[0]
    df1 = df[[('Passing', 'Cmp'), ('Passing', 'Att'), ('Passing', 'Cmp%'), ('Passing', 'Yds'), ('Passing', 'TD'), ('Passing', 'Int'), ('Passing', 'Rate'), ('Rushing', 'Rush'), ('Rushing', 'Yds'), ('Rushing', 'Y/A'), ('Rushing', 'TD')]]
    print(df1)

