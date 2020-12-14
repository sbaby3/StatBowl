import pandas
from player import Player
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
    nameindex=0
    temp=0
    while(nameindex!=-1):
        nameindex = playersHTML.find(".htm\">", temp)
        if nameindex  == -1:
            break
        nameendindex = playersHTML.find("<", nameindex)
        temp = nameendindex
        name = playersHTML[nameindex+6:nameendindex] 

        positionindex = playersHTML.find(" (", nameendindex)
        positionendindex = playersHTML.find(")", positionindex)
        position = playersHTML[positionindex+2:positionendindex]
        
        yearindex = playersHTML.find(" ", positionendindex)
        if yearindex  == -1:
            break
        yearendindex = playersHTML.find("</p>", yearindex)
        years = playersHTML[yearindex+1:yearendindex]
        
        if("2020" in years):
            year = playersHTML[yearindex+1:yearindex+5]
            p = Player(name, position, int(year))
            players.append(p)


