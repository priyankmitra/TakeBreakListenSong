"""
    Program that schedules breaks throughout the day
    reminding that who works really long hours on the computer,
    to listen to music, get up and dance to their favorite Song,
    or just walk away from the computer every once in a while.
    As test case, List of Some Songs provided as myPlaylist.

    @itskshitizsh
    
"""

import time
import webbrowser
repeat = 0
myPlaylist = ["https://www.youtube.com/watch?v=UVbcaG2tfSE", # Chalti Hai Kya 9 Se 12 (Judwaa 2)
           "https://www.youtube.com/watch?v=O3-hJuKpt8c", # Maine Tujhko Dekha (Golmaal Again)
           "https://www.youtube.com/watch?v=8R4NDog2690", # Aa To Sahii (Judwaa 2)
           "https://www.youtube.com/watch?v=DzBa71rNJ5Y", # Socha Hai (Baadshaho)
           "https://www.youtube.com/watch?v=2ll4IA146YI", # Hawa Hawa (Mubarakan)
           "https://www.youtube.com/watch?v=1ac9FLyQo88", # Main Tera Boyfriend (Raabta)
           "https://www.youtube.com/watch?v=rxMmistOjCA", # Nachange Saari Raat (JUNOONIYAT)
           "https://www.youtube.com/watch?v=Ek17-Sh7jtA", # Cheez Badi (Machine)
           "https://www.youtube.com/watch?v=6CVVd9RB7CI", # GF BF Video Song
           "https://www.youtube.com/watch?v=Bl7t4bK4hPA"  # Suit Suit Karda (Hindi Medium)
           ]
    # 60*60 : 60 Minutes or 1 Hour Between Next Break.
sec = 10 # Seconds after which you want to take break.
print("This Program Started On"+time.ctime())
while (repeat < 10):
    time.sleep(sec)
    url = myPlaylist[repeat]
    webbrowser.open(url,new=2)
    repeat=repeat+1
