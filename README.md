# You Got This
#### The web application allows users to view, add, vote on, and comment on one minute pitches, May 5, 2020 
#### By **Waithera-m**
## Description
You Got This is a simple flask application that  allows users to view, vote and comment on pitches. Users can also use provided links to add new pitches in different categories.

## Setup/Installation Requirements
To use the application, users need internet access and web browsers, preferably  Chrome, Safari, and Firefox. Users also need an authenticated account to access comment, vote, and add pitch features.
## Set-Up a Local Project
### Prerequisites
* Python version 3.6 or later
* pip
* flask
* flask-uploads
* flask-login
* flask-wtf
* flask-mail
* flask-sqlalchemy
* postgresql account and database

To set up a local project:
* Fork the repository
* Clone the repository using the git clone command
* Activate a virtual environment
* Install all prerequisites
## Known Bugs
* None at the moment.
## Behavior Driven Development (BDD)
### Landing Page
![image](https://user-images.githubusercontent.com/60571734/81081782-0af53900-8efb-11ea-8e6d-7ba16dda813f.png)

### Category View
![image](https://user-images.githubusercontent.com/60571734/81085746-49d9bd80-8f00-11ea-80bc-92323033be6a.png)

### Pitch View
![image](https://user-images.githubusercontent.com/60571734/81085899-7a215c00-8f00-11ea-8967-a49083eb7254.png)

### Profile View
![image](https://user-images.githubusercontent.com/60571734/81086008-99b88480-8f00-11ea-9dc2-071da33479db.png)

|Behavior                |Input                            |Output                             |
|------------------------|----------------------------------|----------------------------------|
|The landing page loads |Users scroll | Users see sample pitches and links to different categories|
|The landing page loads|Users click on videos|Sample pitches videos play|
|The landing page loads|Users click on category links in navbar|Users are directed to views that display different categories of pitches|
|The landing page loads|Users click on sign in button|Users are directed to sign in/ register view, users sign in if they have an account or click on the sign up link to create an account|
|The landing page loads|Users click on profile navbar link|Users see they profiles and options to edit or upload profile image|
|The category view loads|Users see added pitches, add pitch and vote and comment buttons|Users click on add pitch button and if they are authenticated are directed to add pitch form; users click on vote and comment button and if authenticated get to vote and comment on added pitches|
|The landing page loads|Users click on sign out link in the navbar|Users are logged out|
## Technologies Used
* HTML - HTML dictates the structure of webpages.
* CSS & Bootstrap - CSS determines the appearance of webpages. The styling language was used to add background images and colors and style the site's content.
* Python 3.8.2 - The language was used to create classes, testcases, and functions to retrieve data 
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) -  Flask is a Python microframework.The framework's templates were used to refactor code and promote code maintenance. Inbuilt filters,classes, and methods were used to initialize the application and extensions and loop through and display pitches and navigate to different views. 
## Support and contact details
You are free to suggest and improve the code. To make your changes:
* Fork the repo
* Create a new branch
* Create, add, commit, and push your changes to the branch
* Create a pull request
* You can also contact the creator via this email address: njihiamary11@gmail.com
## Demo
You can view changes made to the website by visiting this working live demo: 
### License
*MIT*
MIT License Copyright (c) 2020 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE
Copyright (c) 2020 **Waithera-m**