# HOW TO PULL SONA BOOKINGS INTO GOOGLE CALENDAR 

Nick Willmot, School of Psycholgy, University of Queensland
nick.willmot2@gmail.com

So you have your massive study setup on SONA and you're getting plenty of signups but it's kind of hard to keep up with all the appointments 
because the SONA interface isn't too user friendly.

Wouldn't it be nice if SONA automatically exported your time slots to your own google calendar... well it doesn't and probably won't anytime soon... 
BUT you can do it yourself with a few Python files, Google API and crontab.

Credit to Meng Du, UCLA for doing most of the code for this <https://github.com/MetaD/SONA2Calendar> 

All I have done here is make edits to get the code to work with crontab and added step-by-step instructions to prevent others 
going through the pain I did getting this to work. If you hit any issues email me or search on stackoverflow.

Note these instructions are for MacOS. They should work fine on Linux aswell but will need tweaking for 
Windows when you get to the Crontab section.

Preparation:
1. Grab some beer, wine, coffee or all 3 because one or more typos in your code can make this a long painful process of screaming at terminal
2. Create a new folder somewhere handy (this will be your project directory) and download the code files from 
3. Use a decent coding platform like Visual Studio Code https://code.visualstudio.com and ensure your Python is up to date https://www.python.org/downloads/mac-osx/
4. Install pip (follow steps here https://pypi.org/project/pip/c)
5. Setup a gmail account (if you don't already have one) and then setup a calendar for your study
    
    _You need one calendar per SONA study_
    
6. Setup a Google Cloud project (https://developers.google.com/workspace/guides/create-project)
7. Enable the Google Calendar API for above project (https://developers.google.com/workspace/guides/enable-apis) 
8. Create access credentials (https://developers.google.com/workspace/guides/create-credentials#oauth-client-id) 
    
    _You need OAuth credentials for a 'Desktop app'_
    
    _Follow instructions above and download the .json file to your project directory_
   
    _Change name of .json file to 'credentials.json'_
    
    _This must be a single line file_
9. Using macOS terminal (Launchpad > Other) or in VS Code (View > Terminal) enter the below code

    `python3 pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`
    
    _You can use py instead of python3 but I use the latter to distinguish it from older py packages I have installed_
    
10. Navigate to your working directory
    `cd /Users/macbook/...wherever your folder is/`
    _In macOS terminal if a folder in your path has a space like /Google Drive/ you need to write it as /Google\ Drive/_
11. Install required packages

    `python3 pip install -r requirements.txt` 

12. Edit the sona2calendar.py file as needed 
    - Line 1        :   '#! /usr/bin/python3' - edit this shebang to make sure it reflects the path to your python3
    
    _Find your path to python3 by typing `which python` into terminal_
    
    - Line 29       :   Insert the absolute path of your credentials.json file you downloaded from google.
    - Line 38       :   Insert the absolute path of your token.json file (this is created after your first login and is the same path as above).
    - Line 56       :   Edit the hyperlink text if running multi-part study. You need to create a new sona2calendar.py file for each part (but not each study).
    - Line 119-123  :   These are deactivated in the file. You can reactivate them if you want, but it won't work with crontab.
    - Line 125      :   Insert your SONA User id e.g., ('S3456789') or ('SteveJobs') etc.
    - Line 126      :   Insert your SONA password e.g., ('SecretPassword1%').
13. Edit the constants.py file as needed
    - Line 2        :   Insert your SONA domain (the page you log in)
    - Line 5        :   Not needed if entered into sona2calendar.py
    - Line 9        :   Enter your EXACT SONA study title into the first part and then your google calendar id into the second part
    
    _Google Calendar ID can be found via Settings and sharing> Integrate Calendar_
    
    _You can add more studies to this part, just use a comma to separate studies_
    
    - Line 16       :   Enter your EXACT SONA study title into the first part and your preferred nickname for the study in the second part 
    - Line 24       :   You can play around with colours if you want - handy if you have multiple parts or more than one study
    - Line 29       :   Shorten the name that appears in your calendar 
14. Run the script 
    > python3 sona2calendar.py
    
    _It might ask you to sign in to Google this first time, but that login will then be saved in token.json_
    
15. Scream at your laptop because it didn't work (or rejoice because it did)
    - Go over the steps above, if it can't find a file make sure the paths are correct, if credentials is an issue than recheck your Google credentials.json file
    
    - You should end up with a printout like below;
    ```Connecting to SONA..
    Logging in...
    Login successful
    Fetching study list...
    Fetching timeslots for Your_SONA_Study...
    Found 1 upcoming timeslot(s) for Your_SONA_Study
    Connecting to Google calendar...
    Fetching events from Google calendar...
    Event "SONA/ User (Participant_Name)" added
    Done

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Ok, hopefully you are at this point because you got it to work and are now seeing your SONA appointments in Google calendar. 
BUT you can only get it to update by manually running the code in terminal every now and then like some kind of mid-90's hackerman 
in charge of security at Jurassic Park. 
You're a busy person with a busy life, can't we automate this process? 
Yes, yes we can... with the help of Crontab.

Crontab is a native feature on macOS and Linux. It receives certain inputs and will then run a code automatically whenever you want it to... 
however the way you tell it to run, say every 5 minutes, is via some kind of pre-WW2 code system of astericks and numbers that is easy to mess up.
* Go to https://crontab.guru/ and play around with the tool there to find the right option for you. Note; running every minute or every 5 minutes can be intense for your computer and your internet connection. 
* You might only want every hour or so, which would be [0  *   *   *   *]
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
16. In terminal type the following;
    `env EDITOR=nano crontab -e`
17. In the Nano editor screen that has now appeared type the following (substitute in your own crontab code, the example here is hourly)
    >  0    *   *   *   *   /usr/bin/python3    /Users/macbook/path_to_your_project/sona2calendar.py
    
    _Use tabs to separate everything, not spaces_
    
18. Save the file (^O). Press enter to accept filename then close crontab editor (^X)
19. You should get a message saying the crontab is being installed, you will see a pop-up asking for Admin rights, click [Allow]
20. Check the crontab is saved by typing the below into terminal 
    `crontab -l`
20. Crontab sends emails when it executes the task (or fails to execute) To check this email type the following into terminal
    `mail`
21. Select the number of the message you want to read by typing the number, e.g.,
    `2`
    
    _Continue checking emails until it works, if no error messages are in your email then it is working. You can also sign up as a participant in SONA using a dummy account and test if your dummy bookings appear in the google calendar._
    
22. Exit mail (^Z)
21. If if is all working as it should then you can turn off email by entering the editor again;
    `env EDITOR=nano crontab -e`
22. Then add this to the TOP of the crontab file to turn off emails
    `MAILTO=""`


# CONGRATULATIONS you did it. 

So now sit back and relax and watch your SONA appointments effortlessly appear in your Google calendar. A few notes;

1. This only works when your computer is on and connected to internet. If you need it to run constantly then consider using a small computer 
(Raspberry Pi) that is constantly connected to internet. But if you run it off the computer you work on each day then it should be fine.

2. You can parcel up the python code using pyinstaller and make it an .exe that can be run by Windows scheduler software or other apps. 
See pyinstaller for more details. You might run into issues with accessing the credentials files when you parcel into .exe, a work around 
is to add credentials as a dictionary inside the python code... Just google it.

3. It's more complicated when you run multi-part studies in SONA (like I did). You need to create a .py file for each Part of your study; e.g., sona2calendar_p1.py, sona2calendar_p2.py then edit the `['_HyperlinkTimeSlot']` extension on Line 56 to reflect each part; e.g., `['_HyperlinkPart1TimeSlot']`. Funnily enough though you can run the .py code for multiple studies. For example if you have two multi-part 
studies in SONA (like me) you can have the one .py code scrape Part 1 (or 2, 3,4 etc) appointments for both studies in the one routine. 

4. There's probably a way to have your SONA sign-up emails forwarded to Google and then auto-added to your calendar. This would work similar 
to the code here, but instead of scraping SONA it would scrape your inbox. Issues I could foresee with that method would be having the cancellation 
emails remove the appt instead of adding a new one in.







