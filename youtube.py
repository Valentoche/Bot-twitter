from apiclient.discovery import build
import apiclient.discovery
import os

global contenu



DEVELOPER_KEY = "AIzaSyAbG930U6kJPV3ikwoYkBqz7tuftNIYPKM"   #variable pour la connexion à youtube
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

search_response = youtube.search().list(q='sao',part='snippet',maxResults=3).execute()    # recherche sur youtube sur 1 thèmes

for search_result in search_response.get("items"):                                                   # trie pour séparer video, playlist et chaine
    if search_result["id"]["kind"] == "youtube#video":                                      #réccuperation des ID et titre des vidéo 
        contenu = search_result["snippet"]["title"]
        contenu2 = search_result["id"]["videoId"]
        
        list = [str(contenu), str(contenu2)]
        
        

        with open('Status.txt', 'a', encoding="utf-8") as f:
            for item in list:
                f.write(f'{item}\n')

        




    
    elif search_result["id"]["kind"] == "youtube#channel" :                                 #réccuperation des ID et titre des chaines 
        print(search_result["snippet"]["title"], search_result["id"]["channelId"])







