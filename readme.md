# Phillips HUE controller for Linux terminal

A python3 written phillips hue lights controller for linux terminal

## How to install?
1. Install requirements.txt
2. Place the hue.py and hue-api.py files in your /usr/local/bin folder
3. Rename the 'hue.py' file to 'hue'
4. Make sure your python3 binary is in #!/usr/bin/python3

## How to configure with your hue?
1. Find the IP address of your hue bridge by scanning your network or checking the router logs
2. Fill in the IP in the hue file located in /usr/local/bin
3. Create a username at your hue bridge following the tutorial at https://developers.meethue.com/develop/get-started-2/
4. Fill in the username in the hue file located in /usr/local/bin
5. Fill in the group ID in the hue file located in /usr/local/bin. See this tutorial to check your group ID https://developers.meethue.com/develop/hue-api/groupds-api/

## How to use?
1. Turn lights on by running 'hue' from the linux terminal
2. Turn lights off by running 'hue off' from the linux terminal
3. To change the brightness to 50% run 'hue bri 50'
4. To lsit the available scenes run 'hue scene'
5. To change the scene to option 1 run 'hue scene 1'
