Kathabhidhana: Open Source toolkit to record large number of words in any language
===================================
<a href="http://www.youtube.com/watch?feature=player_embedded&v=UGMxwPtqDJY
" target="_blank"><img src="http://img.youtube.com/vi/UGMxwPtqDJY/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>  ![alt tag](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7c/Home-studio_recording_setup_for_Kathabhidhana_%28wide%29.jpg/495px-Home-studio_recording_setup_for_Kathabhidhana_%28wide%29.jpg)

What comes to your mind when you think of a dictionary? A huge boring book that you never wanted to open? Or maybe a mobile app that you open while struggling with understanding a few new words in any write-up? But think of a dictionary that also pronounces the words rather than just showing them in [International Phonetic Alphabet](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) (IPA), and without any advertisements. Also, think of an open source version of Siri or Google Assistant or Kortana that you can not just use but also can change and make it speak your dialect in a human voice. For all of these you would need a huge pronunciation library in an open standard. Furthermore, India, my home country alone is home to 15 million visually disabled people that currently do not have open source assistant in their language with a human voice.

Wikipedia has a sister project called [Wiktionary](https://wiktionary.org). And it's multilingual. Though it's easier to search any word in Google with a suffix "meaning" to hear the pronunciation of the word, there are not many [open-licensed](https://en.wikipedia.org/wiki/Open_Content_License) audio recordings that you can hear, download, and even use for your own work. <b>Kathabhidhana</b> is a community project led by [Subhashish Panigrahi](http://meta.wikimedia.org/wiki/User:Psubhashish/) to create an open source toolkit for anyone to learn how to record large chunks of words and then upload them under open licenses so that they can be useful for projects like Wiktionary. We have borrowed the code for one of the software components from a [software](https://github.com/tshrinivasan/voice-recorder-for-tawictionary) created by by [Shrinivasan T](https://github.com/tshrinivasan). The [iOS version](https://github.com/OdiaWikimedia/Kathabhidhana/tree/master/Kathabhidhana%20for%20iOS) of Kathabhidhana was created by Prateek Pattanaik.

Currently several Odia-language words are being [recorded](https://commons.wikimedia.org/wiki/Category:Odia_pronunciation), uploaded on [Wikimedia Commons](https://commons.wikimedia.org), and are being used in [Odia Wiktionary](https://or.wiktionary.org), the Odia-language version of Wiktionary. The purpose of creating this audio library is multi-folded—apart from using them on Wiktionary, we also aim at using them for any [Natural Language Processing](http://en.wikipedia.org/wiki/Natural_Language_Processing) (NLP) project (and you are free to use [with attribution](https://github.com/OdiaWikimedia/Kathabhidhana/blob/master/README.md#attribution) any resource available in this page).

* [Tutorial to learn and use it](http://www.youtube.com/watch?v=zd4KNbNX4_Y) (in English)
* [Audio recording of words that were made using this tool](https://commons.wikimedia.org/wiki/Category:Audio_files_created_using_Kathabhidhana)
* An [ideal format needed for uploading multiple file](https://docs.google.com/spreadsheets/d/1Vh08Dd6V743Q58ceCnNLc9BASaZQMAsGu1BOaa_dMQQ/edit?usp=sharing)

<i>An Odia version of the resources and tutorial is available [here](https://or.wiktionary.org/s/ppq). We are currently working on building more tutorials so that you can learn more about bettering your home studio setup, assuming you don't have access to a fancy recording studio (if you do have access to a fancy recording studio please leverage that resource), tips and tricks about batch renaming files, cleaning up using open source tools like [Audacity](http://www.audacityteam.org/download/), setting up files for batch upload on Wikimedia Commons, etc. So stay tuned.</i> 

Prerequisites
--------------
<b>Using a computer?</b>
* Linux or macOS
* Linux running in a virtual machine

<b>Using an iOS device? ([check more here](https://github.com/pattaprateek/Kathabhidhana/tree/master/Kathabhidhana%20for%20iOS))</b>
* iOS (iPad or iPhone)
* An app called Workflow

How to execute?
--------------
(<i>you need to run the command in Linux or Mac, or Linux in a [virtual machine](https://en.wikipedia.org/wiki/Virtual_machine) if you're on Windows</i>)
[<i>Read in Odia</i>](https://goo.gl/hqXeG3)

1. Fill the words you want to record in a textfile named "file"
2. run the below command

First dive into the folder, for instance it is the "Kathabhidhana" folder under "Documents for me:
![alt tag](https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Kathabhidhana_-_starting_the_tool.png/800px-Kathabhidhana_-_starting_the_tool.png)

Then run:
<code>python voice-record.py</code>

The next steps are quite self-explanatory. You need to choose "Y" for yes and "N" for no in the following options inside your terminal.

3. To upload all the ogg files to Wikimedia Commons
This will record the sounds in .ogg and .wav formats. You can then use a tool like [Pattypan](https://github.com/yarl/pattypan) to batch-upload either the .WAV or the .ogg files on Wikimedia Commons.

Findings so far
-----------
* It takes about <b>20-25 mins<b> to record <b>100 words</b>
* A batch processing to convert and do overall auto-cleanup using Audacity will take about 5 mins
* It takes an average of <b>30 secs</b> for <b>1 word</b> to manually clean up, check quality, trim extra portions and other such editing work (meaning it will take about 45 mins to clean up a batch of 100 words) using Audacity
* It takes about <b>5-10 mins</b> for setting up Pattypan to upload the cleaned up words on Wikimedia Commons
* On an average one would spend roughly about <b>1.5 hrs</b> from recording to cleaning up to uploading for a batch of <b>100 words</b>

Attribution
-----------
* Project led by Subhashish Panigrahi and the [iOS tool](https://github.com/OdiaWikimedia/Kathabhidhana/tree/master/Kathabhidhana%20for%20iOS) is led by Prateek Pattanaik. All the media and text content are available under a [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license
* All the software component is licensed under [GNU General Public License (GPL) version 3](https://www.gnu.org/licenses/gpl.html) (read the [License](https://github.com/OdiaWikimedia/Kathabhidhana/blob/master/License.md) page for more details)
* This project and part of the documentation are based on the [Voice recorder for Tawiktionary](https://github.com/tshrinivasan/voice-recorder-for-tawictionary) project created by [Shrinivasan T](https://github.com/tshrinivasan) (please attribute Shrinivasan T if you're making a derivative of the software)

Other resources
--------------
* [Pronuncify by Asaf Bartov](https://github.com/abartov/pronuncify), a similar command line tool for both Linux/Mac and Windows.
* [Sample Wikimedia Commons description](https://docs.google.com/spreadsheets/d/1Vh08Dd6V743Q58ceCnNLc9BASaZQMAsGu1BOaa_dMQQ/pub?output=ods) that you're free to download, replace with your details and use.

Shoutouts
----------
* Ojha, Bikash. Mishra, Chinmayee. Pattanaik, Prateek. Panigrahi, Subhashish. Patnaik, Sailesh. Elsharbaty, Samir. [Community digest: As Odia Wikisource turns two, a project to digitize rare books kicks off; news in brief](https://blog.wikimedia.org/2017/03/30/digest-odia-wikisource/). Wikimedia Blog (March 30, 2017)
* Rezwan. ["A New Audio Uploading Tool for Crowdsourced Wiktionary Project in Odia Language"](https://globalvoices.org/2017/02/12/a-new-audio-uploading-tool-for-crowdsourced-wiktionary-project-in-odia-language/). Global Voices (February 13, 2017)
