Kathabhidhana: Audio recording for Odia Wiktionary
===================================
![alt tag](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/A_home_recording_setup_for_the_Kathabhidhana_project_for_Wiktionary.jpg/250px-A_home_recording_setup_for_the_Kathabhidhana_project_for_Wiktionary.jpg)

Kathabhidhana is a community project to create an open source solution for recording large chunks of words (and then uploading them under open licenses so that they can useful for projects like [Wiktionary]). The project draws its inspiration largely from another [software] (https://github.com/tshrinivasan/voice-recorder-for-tawictionary) created by by [Shrinivasan T] (https://github.com/tshrinivasan).

Currently several Odia-language words are being [recorded] (https://commons.wikimedia.org/wiki/Category:Odia_pronunciation), uploaded on [Wikimedia Commons] (https://commons.wikimedia.org), and are being used in [Odia Wiktionary] (https://or.wiktionary.org), an online dictionary that shows meaning of other language words in Odia apart from Odia-language words.

* [Tutorial to learn and use it] (http://www.youtube.com/watch?v=zd4KNbNX4_Y) (in English)
* [Audio recording of words that were made using this tool] (https://commons.wikimedia.org/wiki/Category:Audio_files_created_using_Kathabhidhana)

How to install?
--------------

Read from [here](https://github.com/OdiaWikimedia/Kathabhidhana/blob/master/install) for installing in Ubuntu 14.04 and above, or Apple Mac.


How to execute?
--------------
[<i>Read in Odia</i>] (https://goo.gl/hqXeG3)

1. Fill the words you want to recoed in a textfile named "file"
2. run the below command

python voice-record.py 2> err

this will record the sounds in ogg and wav formats.

3. To upload all the ogg files to Wikimedia Commons

3. a) Edit the file mediawiki-uploader.py 
Fill the commons api url, username and password

3. b) run the below command
python mediawiki-uploader.py

Attribution
-----------
This project and part of the documentation are based on the [Voice recorder for Tawiktionary] (https://github.com/tshrinivasan/voice-recorder-for-tawictionary) project created by [Shrinivasan T] (https://github.com/tshrinivasan).

Other resources
--------------
* [Pronuncify by Asaf Bartov] (https://github.com/abartov/pronuncify), a similar command line tool for both Linux/Mac and Windows.
