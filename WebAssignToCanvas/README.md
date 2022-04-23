In this folder, you will see three csv files: webassignNAMELESS, canvasNAMELESS and webassignCLEAN. 

This python script in this folder will take both of these csv files and create a cleaner version that will make importing grades into canvas much easier.

One feature that is not really illustrated with the nameless csv examples is that this script will take both the canvas and webassign csv files and will drop students from webassign who are not added on canvas and it will add students to webassign who, for whatever reason, never signed up for the online homework. 

The scrip is not affected by upper or lower case letters. For example, if a student enters their name as BILL SMITH in webassign and Bill Smith in canvas, the script will still count this as the same student. 

Its important to note that this script is highly specific for my current semester of teaching with canvas and webassign. It will need to be tweaked for use in futer classes. For example, I dropped all the homework columns in webassign because homeowrk is not graded. If this is not the case then you will want to keep these columns. 

Each section in the script starts with a comment and ends with a hash tag:

\# Descritpion of what this section does 

	code
\#

\# Description of next section

	code
\# 


