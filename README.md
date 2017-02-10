Kathabhidhana: Audio recording for Odia Wiktionary
===================================
What comes to your mind when you think of a dictionary? A boring huge book that you never wanted to open? Or may be a mobile app that you open while struggling with understanding a few new words in any write-up? But think of a dictionary that also pronounces the words rather than just showing them in [International Phonetic Alphabet] (https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) (IPA).

Wikipedia has a sister project called [Wiktionary](https://wiktionary.org). And it's multilingual. Though it's easier to search any word in Google with a suffix "meaning" to hear the pronunciation of the word, there are not many [open-licensed] (https://en.wikipedia.org/wiki/Open_Content_License) audio recordings that you can hear, download, and even use for your own work. <b>Kathabhidhana</b> is a community project led by [Subhashish Panigrahi] (http://meta.wikimedia.org/wiki/User:Psubhashish/) to create an open source solution for recording large chunks of words and then uploading them under open licenses so that they can useful for projects like Wiktionary. The project draws its inspiration largely from another open source [software] (https://github.com/tshrinivasan/voice-recorder-for-tawictionary) created by by [Shrinivasan T] (https://github.com/tshrinivasan).

Currently several Odia-language words are being [recorded] (https://commons.wikimedia.org/wiki/Category:Odia_pronunciation), uploaded on [Wikimedia Commons] (https://commons.wikimedia.org), and are being used in [Odia Wiktionary] (https://or.wiktionary.org), the Odia-language version of Wiktionary. The purpose of creating this audio library is multi-folded—apart from using them on Wiktionary, we also aim at using them for any [Natural Language Processing] (http://en.wikipedia.org/wiki/Natural Language Processing) (NLP) project (and you are free to use [with attribution] (https://github.com/OdiaWikimedia/Kathabhidhana/blob/master/README.md#attribution) any resource available in this page).

![alt tag](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1f/A_home_recording_setup_for_the_Kathabhidhana_project_for_Wiktionary.jpg/250px-A_home_recording_setup_for_the_Kathabhidhana_project_for_Wiktionary.jpg)

* [Tutorial to learn and use it] (http://www.youtube.com/watch?v=zd4KNbNX4_Y) (in English)
* [Audio recording of words that were made using this tool] (https://commons.wikimedia.org/wiki/Category:Audio_files_created_using_Kathabhidhana)

<i>An Odia version of the resources and tutorial is available [here](https://or.wiktionary.org/s/ppq). We are currently working on building more tutorials so that you can learn more about bettering your home studio setup—ssuming you don't have access to a fancy recording studio but if you have please do leverage that, tips and tricks about batch renaming files, cleaning up using open source tools like Audacity, setting up files for batch upload on Wikimedia Commons, etc. So stay tuned.</i> 

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
* Project led by Subhashish Panigrahi. All the media and text content are available under a [CC-BY-SA 4.0] (https://creativecommons.org/licenses/by-sa/4.0/) license
* All the software component is licensed under [GNU General Public License (GPL) version 3] (https://www.gnu.org/licenses/gpl.html)
* This project and part of the documentation are based on the [Voice recorder for Tawiktionary] (https://github.com/tshrinivasan/voice-recorder-for-tawictionary) project created by [Shrinivasan T] (https://github.com/tshrinivasan) (Please attribute Shrinivasan T if you're making a derivative of the software)***

Other resources
--------------
* [Pronuncify by Asaf Bartov] (https://github.com/abartov/pronuncify), a similar command line tool for both Linux/Mac and Windows.
* [Sample Wikimedia Commons description] (https://docs.google.com/spreadsheets/d/1Vh08Dd6V743Q58ceCnNLc9BASaZQMAsGu1BOaa_dMQQ/pub?output=ods) that you're free to download, replace with your details and use.
