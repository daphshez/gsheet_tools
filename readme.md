An example for accessing Google Sheets using API v. 4

In order to use it you need to install Google APIs Client Library for Python

   pip install google-api-python-client

You'll also need a file called client_secret.json, which is expected to be in the script directory. To get it: 

1. Go to [dev console](https://console.developers.google.com/)
2. Create new project 
3. Turn on Google Sheets API 
4. Create & download credentials

To run, call

​	`python -m csv_to_gsheet  name_of_spreadsheets file1 file2 file3 ...`



Resources about using the API:

* [Quick start](https://developers.google.com/sheets/quickstart/python) - not overly self explanatory
* Wesley's Chun (@wescpy):
  * [Import data from SQLite](http://wescpy.blogspot.co.uk/2016/06/using-new-google-sheets-api.html). Shows how to write & read a range. [There's also a walk through video](https://gsuite-developers.googleblog.com/2016/06/introducing-google-sheets-api-v4.html). There are links inside the video to two previous videos with instructions to creating Google Code project, and writing the Python code for OAuth2. 
  * More relevant posts
* [Reference](https://developers.google.com/sheets/reference/rest/) 