Kathabhidhana: Audio recording for Odia Wiktionary
===================================

[Odia Wiktionary] (https://or.wiktionary.org) is an online dictionary that shows meaning of other language words in Odia apart from Odia-language words. Being a dictionary audio recordings are very essential for the words. This tool helps record pronunciation of words and upload them to [Wikimedia Commons] (https://commons.wikimedia.org/wiki/Category:Odia_pronunciation).

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
