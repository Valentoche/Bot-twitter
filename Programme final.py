
import tweepy
from random import randint
import time
import os
import youtube


youtube
#Fonction pour le choix de la vidéo
def choix_texte() :	
	global choix
	with open('Status.txt', 'r', encoding="utf-8") as f:
		liste = f.read().splitlines()
	test = int(randint(0,4))
	print(test)
	choix = str(liste[test])

#Fonction pour le choix de l'image
def choix_image() :
	choiximg = str (randint(1, 6))
	choix = "img%s.jpg" %choiximg

#Fonction pour vérifier qu'il n'est pas dans la poubelle
def poubelle() :
	with open('poubelle.txt', 'r', encoding="utf-8") as f:
			liste = f.read().splitlines()
	lol = liste.count(choix)
	while lol >0:
		print("Dèjà publié")
		time.sleep(5)
		choix_texte(), choix




#Connexion à twitter
consumer_key = 'YOUR KEY'
consumer_secret = ''		
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.me()
print (user.name)	#Affiche le nom de compte



while True :
	
	#Publication de l'image
	if int(randint(1,2)) == 1 :
		print("Publication d'une image.")
		#Appelle des deux fonctions
		choix()
		poubelle()
		#Ecrtiture dans la poubelle
		open("poubelle.txt", "a").writelines("\n%s" %choix)
		print(choix)
		#Publication vers twitter
		api.media_upload(choix)
		api.update_with_media(choix)												
		print ("Image publiée")
		time.sleep(10)	#Pause de 10s					
		
	#Publication d'un texte
	else : 											
		print("Publication d'un texte")
		#Appelle des deux fonctions
		choix_texte()
		poubelle()
		#Ecriture dans la poubelle
		open("poubelle.txt", "a", encoding="utf-8").writelines("\n%s" %choix)
		fin = "https://www.youtube.com/watch?v=%s" %choix
		print("https://www.youtube.com/watch?v=%s" %choix)
		#Publication
		api.update_status(fin)											
		print("Publié")
		time.sleep(15)	#Pause de 15s														
		

