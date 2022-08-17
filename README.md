#Task 1 - GitHub skill test
Task preparation:
  - slides session 4
  - creation of repository on GitHub
  Task implementation: following slides session 4
  Task troubleshooting: no problems encountered
  Task verification:l ![image](https://user-images.githubusercontent.com/3658831/182939494-8bfea0bd-517c-48f4-9e61-d2513ecca207.png)
#############################################################################################################################################
#Task 10 : Filtering DNAC  Response DATA
Task preparation
-----------------
  Reading the course and google the commands
Task implementation
------------------
  Type the Pythonscript with the 'missing links' filled
Task troubleshooting
-------------------
  POST bij request and no GET
  timedata.timedate.now(): some trail and error
  typo's like missing ' and : in stead of =
Task verification:
-------------------
DEBUG: Filter response DATA
===
{'type': 'Cisco 3504 Wir
devasc@labvm:~/Devasc_Skills/dnac$  cd /home/devasc/Devasc_Skills/dnac ; /usr/bin/env /bin/python3 /home/devasc/.vscode/extensions/ms-python.python-2022.2.1924087327/pythonFiles/lib/python/debugpy/launcher 36515 -- /home/devasc/Devasc_Skills/dnac/dnac-pgy.py 
Current data en time: 
2022-08-08 17:05:00.022073
DEBUG: token request
DEBUG: inventory request
DEBUG: Filter response DATA
===
Hostname: c3504.abc.inc
Familiy: Wireless Controller
MAC: ac:4a:56:6c:7c:00
IP: 10.10.20.51
Software version: 8.5.140.0
Reachability: Reachable
===
Hostname: leaf1.abc.inc
Familiy: Switches and Hubs
MAC: 84:8a:8d:05:76:00
IP: 10.10.20.81
Software version: 17.3.3
Reachability: Reachable
===
Hostname: leaf2.abc.inc
Familiy: Switches and Hubs
MAC: 68:ca:e4:37:8d:80
IP: 10.10.20.82
Software version: 16.11.1c
Reachability: Reachable
===
Hostname: spine1.abc.inc
Familiy: Switches and Hubs
MAC: 70:1f:53:73:8d:00
IP: 10.10.20.80
Software version: 16.11.1c
#############################################################################################################################################################################################################################################################################################
#Task 6  : Webex team API
Task preparation
-----------------
  Reading the course  and slides,  and google the commands
Task implementation
------------------
  starting with the information from session 3 with trail and error
Task troubleshooting
-------------------
  difference between cisco spark and webexteam
  each run creates new room with same name
  uploading of jpeg
Task verification:
-------------------
adding a second account to webex and check for the output

##################################################
Task name: Task 7: bash
################################################## 
Task preparation
---------------
  reading the examples in session 9 + Google 
  
Task implementation:
--------------------
  curl with options and testing Task troubleshooting
  part 1: output is not as desired. Probably minor error with passing of paramaters to curl part 2: formating of json output not succesfull with commands like 'lq' and 'mjson.tool' 
  
Task verification
------------------
  Screenshots and comments

conclusion:
-----------
  not fully terminated but still 'on good track'

########################################################
 Task 5 -- REST API & RESTCONF ***
 Task preparation
 ---------------
reading the different exercises and task 7 of the skill examen
Google documentation

Task implementation:
--------------------
usage of skelleton of task 7 with modification


Task troubleshooting
---------------------
passing of 'severety' gives a problem
formating of output is still not conform



Task verification
-----------------
Major parts of the scripts are prepared
Minor errors, like format of output by non working Json() 

Score: 2/3. Rather moving on than spending an other day try and error


####################################
########################################################
 Task 3 -- Docker ***
 Task preparation
 ---------------
 reading the DevNet sessions and Google Docker documentation

Task implementation:
--------------------
writing Dockerfile from examples
writing shell script by try and error


Task troubleshooting
---------------------
typing errors
confusion about /var/www/html or /usr/local/apache/html as location of index files


Task verification
-----------------
OK: website can be reached

#########################################"
########################################################
 Task 2 -- Ansible ***
 Task preparation
 ---------------
Reading of documentation, slides from session 7 and examples on github of instructor. 
Task implementation:
--------------------
Start with try and error based on documentation on the internet, with a lot of mistakes
Testing and copying the files of the instructor


Task troubleshooting
---------------------
Started with a  lot of error during the try
Once the files of the instructor are used, it seems to work well

Task verification
-----------------
Green screen during execution of the playbook with command 
      ansible-playbook ios_facts.yml -vvv
screenshots taken after each step

It is not perfect and a little bit to much copying from instructorfiles, but it works without red remarks


########################################################
 Task 4 -- Jenkings *
 Task preparation
 ---------------
reading slides from session 6
watching YouTube video's like https://www.youtube.com/watch?v=3g1DX_0VXyw&ab_channel=edureka%21



Task implementation:
--------------------
Starting as seen in lab 6.3.6-lab---build-a-ci-cd-pipeline-using-jenkins.pdf
and with elements from session 6


Task troubleshooting
---------------------
find my way in Jenkins with starting an agent and the connection



Task verification
-----------------
Task abandoned due to lack of time.
Minimal number of points has  been reached already

