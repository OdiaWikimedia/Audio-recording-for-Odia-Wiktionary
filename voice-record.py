import sys
import os
import record
import readline
import subprocess

os.system('clear')
print "Welcome to the Kathabhidhana!"




def process_word():
	os.system('clear')

	fin = open( 'file', "r" )
	data_list = fin.readlines()
	fin.close()

	
	print "\n"
	print "\n"

	word = data_list[:1][0].replace('\n','')

	print word

	print "\n"
	print "\n"

	record.record_audio(word)

	print "\n"
	print "\n"

	confirm = raw_input("Recorded? Y/N : ")
	confirm = confirm.lower()
	
	if confirm == 'y':

		completed=open("completed_words","a")
		completed.writelines(data_list)
		completed.close()



		del data_list[:1]

		fout = open("file", "w")
		fout.writelines(data_list)
		fout.close()
		
		subprocess.call(["oggenc", '-Q', word + '.wav'])


	        play_confirm = raw_input("\nPlay?:   " + word + " ?  Y/N : ")
        	play_confirm = play_confirm.lower()

        	if play_confirm == 'y':
                	print ("\nPlaying...: " + word)
                	os.system("ogg123 " + word + ".ogg")

        	elif play_confirm == 'n':
                	print "\nHappy? Type N for next. "

		#play_confirm = "n"
		
	if confirm == 'n':
	
		process_word()



def process_next_word():
	print "\n"
	print "\n"

        next_word = raw_input( "Next word? Y/N : ")

        next_word = next_word.lower()
        if next_word ==  'y':
                process_word()
                process_next_word()
        elif next_word ==  'n':
                print "Thank you!"
        else:
                print "Enter Y or N"


answer = raw_input("Ready? Y/N : ")

if answer.lower() ==  'y':
	process_word()
	process_next_word()
elif answer.lower() ==  'n':
	print "Thanks"
	sys.exit()





