import pandas
from urllib.request import urlopen

players = []
for i in range(65, 91):
    url = 'https://www.pro-football-reference.com/players/' + chr(i) + '/'
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("latin-1")
    startindex = html.find('<div class="section_content" id="div_players">')
    endindex = html.find("</div>", startindex)
    playersHTML = html[startindex:endindex]
    playerindex=0
    temp=0
    while(playerindex!=-1):
        playerindex = playersHTML.find(".htm\">", temp)
        if playerindex  == -1:
            break
        playerendindex = playersHTML.find("<", playerindex)
        temp = playerendindex
        player = playersHTML[playerindex+6:playerendindex]
        players.append(player)