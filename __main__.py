#########################################
# by staticsploit for education
#########################################
# if you want to reuse code and make your own password generator with python it is unlicensed
# So do whatever you want with this code. Read that for support yourself at python or upgrade it
# and make your own password generator tool.


# first of all we must create a main menu function
def mainmenu():
	print("hello,")
	print("this program has been made by staticsploit(for education)")
	print("what do you want >")
	print("[1] make a password list by given informations\n[2] make a password list by random informations\n\n\n")
	answer = input("your choice >>>")
	if(answer == "1"):
		# we will write here 
	elif(answer == "2"):
		# we will write here
	else:
		print("you have just two choices : 1 or 2")
		print("please try again")
		exit()

def choice_1():
	print("okay, so please answer the questions. If you dont know asked questions answer, make it blank\n\n")
	input("if you are ready, lets go by enter key...")
	print("\n\n")
	targetsname = input("target name >")
	targetsurname = input("target surname >")
	favouriteteam = input("targets favourite football team >")
    targetspartnername = input("targets partner name >")
    targetspartnersurname = input("targets partner surname >")
    targetsfathername = input("targets father name >")
    targetsmothersname = input("targets mothers name >")
    targetsmothersurname = input("targets mothers surname >")
    # I think thats enough for now
    # we will create a list and use that in wordlist
    infos = [targetsname, targetsurname, favouriteteam, targetspartnername, 
    targetspartnersurname, targetsfathername, targetsmothersname, targetsmothersurname]
    print("\n\n\n\n")
    fname = input("what is your wordlist files name >")
    fname = open(fname, "w")

    print("[+] Your file has been opened")

    print("[+] and started to writing passwords in to the file")

    for word in infos:
    	fname.write(word+"\n")
    	fname.write(word.lower()+"\n")
    	fname.write(word.upper()+"\n")
    	fname.write(word.capitalize()+"\n")
    for word1 in infos:
    	for word2 in infos:
    		fname.write(word1+word2+"\n")
            fname.write(word1.lower()+word2.lower()+"\n")
            fname.write(word1.upper()+word2.upper()+"\n")
            fname.write(word1.capitalize()+word2.capitalize()+"\n")
    for word1 in infos:
    	for word2 in infos:
    		for word3 in infos:
                fname.write(word1+word2+word3)
    			fname.write(word1.lower()+word2.lower()+word3.lower()+"\n")
                fname.write(word1.upper()+word2.upper()+word3.upper()+"\n")
                fname.write(word1.capitalize()+word2.capitalize()+word3.capitalize()+"\n")

    for number in range(10000):
    	for word in infos:
            number = str(number)
            fname.write(word++"\n")
            fname.write(word.lower()+"\n")
            fname.write(word.upper()+"\n")
            fname.write(word.capitalize()+"\n")