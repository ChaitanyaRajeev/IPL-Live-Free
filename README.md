# IPL-Live-Free
Watch ipl live run this script after every 10 min. Dont need to clear cache.


Step 1 - Install Python 3.7
link : https://www.python.org/downloads/windows/

Step 2 - Go to Command Prompt and type 
         pip install selenium 
         
Step 3 - After installation of Selenium and Python download the clone repository 
link : https://github.com/ChaitanyaRajeev/IPL-Live-Free.git

Step 4: After downloading install Chromedriver from the folder.

Step 5 : Open ipl.py file and edit this line 

driver = webdriver.Chrome(executable_path="")

Where add the location of the chromedriver with in the quotes for say example
driver = webdriver.Chrome(executable_path="E:/Software/chromedriver.exe")

Note: Add you own path else it will not work.

Now that you are done click on F5 to Run the script.

Before completion of 10 min you can again click on f5 on the ipl.py file. 

voilaaa you are done. 

Cheers.


