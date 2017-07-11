# My Scripts

These are some very basic scripts that I use almost everyday to make my life easier. While each independent script might not achieve anything mighty, they make life convenient when used with other services.

#### The List


| Script       | Purpose           |
| ------------- |:-------------:| 
| wifi-reset.sh      | restarts the wireless interface after a certain time | 
| anagram.py     | finds all the anagrams for a given word      |  
| text.py | sends a text message with the required information     |   
| filenameAsDate.py | saves a file with required information, with the filename as current time      |   
| nameGenerator.py | generates a random firstname and lastname beginning with desired alphabet      |   
| pingpong.py | generates constant pings to prevent heroku dyno from sleeping      |   



#### For cron tabs

 `chmod +x <jobname>`
 
 //scheduling your crontab according to your specific time requirements
 
  `00 09-18 * * * wifi-reset.sh`



