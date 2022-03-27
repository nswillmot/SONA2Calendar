# URL of your SONA system
sona_domain = 'https://uqpsych-p.sona-systems.com/' # Amend to your school's SONA domain

# A file that includes your SONA username (on the 1st line) and password (on the 2nd line)
sona_credentials_file = 'sona_credentials.txt' # Not needed if entered directly into sona2calendar.py file

# Google calendar id (find it in your Calendar Settings -> Calendar ID)
# Make sure the keys in this dictionary match the study names in the SONA system
google_calendar_ids = {'My Very First Study': 'lhk678kj456k3j4klfb4@group.calendar.google.com', 
                       'How much pain can an undergrad endure? $20!': 'lkh456lkad65q9v4nnm4@group.calendar.google.com'
                       }

# This dictionary defines the study names to be displayed in the calendar, if different from the study names in SONA.
# Example: {"A long and unclear study name being used in the SONA system": "Short Study Name"}
# Change this to an empty dictionary if you want the study names to be same as in the SONA system
calendar_study_names = {'My Very First Study': '1st',
                        'How much pain can an undergrad endure? $20!': 'Pain'}

# Color scheme for calendar events: if all words (separated by spaces) in a key string of this dictionary can be
# found in the information of a study timeslot, the corresponding color (value in this dictionary) will be applied
# to the calendar event of the study timeslot.
# Example: {'Rm101 Alice': '1', 'Rm102 Alice': '2', 'Rm102 Bob': '3', 'Rm103': '4'}
# For a reference of event colors see https://developers.google.com/google-apps/calendar/v3/reference/colors/get
color_scheme = {'1st': '1', 'Pain': '3'}

# If the researcher has a perferred name (other than their first name) to be shown on the calendar,
# put it in this dictionary.
# The key here should match the researcher name on SONA, the value is their preferred name. 
researcher_names = {'Burrhus Frederic Skinner': 'B.F'}
