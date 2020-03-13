
import tweepy
from random import randint
import time
import os
import tkinter
import youtube

youtube

def choix_texte() :	
	global ligne, lien															#creation d'une variable
	with open('Status.txt', 'r', encoding="utf-8") as f:
		liste = f.read().splitlines()
   

	print(liste)
	test = int(randint(0,5))
	
	while test%2 != 0 :
		test = int(randint(0,5))
		ligne = str(liste[test])
		
		lien = str(liste[test+1])
		





consumer_key = 'cyMxWpRjwftCPewhOuus3e0D9'										#connexion a twitter grâce au clée du compte
consumer_secret = 'NUemznaeHEeZ1157eZsbf5WVljFBnolFNLDEIrniDqOYhy8DK5'		
access_token = '1124347082595340288-pwpKyfxSzutl76bl0hlyurmQllSebs'
access_token_secret = 'DcQTphvXI3zgv13uAtbeieq2fF4TOpJRkcPEfN3bLbXyi'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
user = api.me()
print (user.name)           													#confirmation de la connexion en renvoyant le nom du compte



while True :																	#tlt vrai = boucle a l'infinie
	
	if int(randint(1,2)) == 3 :
		print("Publication d'une image.")
		choiximg = str (randint(1, 6))											#choix d'un nombre
		img = "img%s.jpg" %choiximg
		poubelle = open("poubelle.txt", "r")									#ouverture du fichier poubelle
		ligne_3 = poubelle.readlines()											#lecture du fichier
		poubelle.close
		while ligne_3.count(img) >= 1 :											#vérifie si l'image a déjà été choisi sinon il rechoisit une image et revérification
			print("Je l'ai dans la poubelle")
			choiximg = str (randint(1, 6))										#choix d'un nombre
			img = "img%s.jpg" %choiximg
		
		open("poubelle.txt", "a").writelines("\n%s" %img)						#puis ecrit le nom de l'image pour pas la rechoisir la prochaine fois
		print(img)

		api.media_upload(img)
		api.update_with_media(img)												#publication
		print ("Image publiée")
		time.sleep(10)															#pause du programme de 10s
		
	else : 																		#publication d'un texte
		print("Publication d'un texte")
		poubelle = open("poubelle.txt", "r", encoding="utf-8")									#ouverture du fichier poubelle
		choix_texte()															#renvoie à la def choix_texte
		ligne_2 = poubelle.readlines()											#lecture du fichier poubelle
		poubelle.close
		while ligne_2.count(ligne) and ligne_2.count(lien) >= 1:										#vérification si il n'est pas dans la poubelle sinon rechoisit un texte
			print("Je l'ai dans la poubelle")
			choix_texte()	
		
		open("poubelle.txt", "a", encoding="utf-8").writelines("\n%s" %ligne)						#ecriture du texte pour ne pas le rechoisir
		open("poubelle.txt", "a", encoding="utf-8").writelines("\n%s" %lien)
		print(ligne, lien)
		fin = "https://www.youtube.com/watch?v=%s" %lien
		print("https://www.youtube.com/watch?v=", lien)
		api.update_status(fin)												#publication du texe
		print("Publié")
		time.sleep(10)															#pause de 10s
		

