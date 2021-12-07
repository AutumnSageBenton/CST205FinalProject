# CST205FinalProject
Welcome to the Boredom Fixation Station

In this documentation you will find the steps necessary to set up your operating system and the command lines to run the code. 



Download all the files in this repository  
Be sure it is unzipped and inside a folder with a virtual enviroment

Getting your machine set up in the command line:
  Install Flask and Bootstrap Flask by pasting the below into the command line

  pip install flask
  pip install bootstrap-flask

Running the program: 
  Ensure your inside the CST205FinalProject folder in the command line
  Paste the below into the command line to run the application

  $env:FLASK_APP = “homePage.py"
  $env:FLASK_DEBUG = "1"
  flask run

Opening the application: 
  After a few seconds the operating system will display some text in the command line. 
  Find the line that states "Running on ..." 
  Copy the web address, it will look something like this (http://127.0.0.1:5000/)
  Paste it into a web engine and press enter
