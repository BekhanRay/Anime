# Anime
👋 Hey there!

Let me tell you about an exciting project called Anime 🎌. This project has an API built on Django 3.2 and DRF, and it allows users to register, add anime, watch anime, and write comments 📝.

The Anime project is perfect for anime lovers who want to keep track of their favorite shows and share their thoughts with others. With the user registration feature, users can create accounts and keep track of the anime they've watched, mark their favorites, and leave comments for others to see.

The project's API makes it easy for developers to access the data stored on the server, allowing them to build their own applications using the Anime data. This feature opens up a whole new world of possibilities for developers who love anime and want to create their own apps.

Overall, Anime is a fun and exciting project that's perfect for anime lovers and developers alike. So why not give it a try and join the community today? 😊

# Running this project
To get this project up and running you should start by having Python installed on your computer. It's advised you create a virtual environment to store your projects dependencies separately. You can install virtualenv with

```
pip install virtualenv
```
Clone or download this repository and open it in your editor of choice. In a terminal (mac/linux) or windows terminal, run the following command in the base directory of this project

```
virtualenv env
```
That will create a new folder env in your project directory. Next activate it with this command on mac/linux:

```
source env/bin/active
```
That will create a new folder env in your project directory. Next activate it with this command on Windows:
```
>env\Scripts\activate
```
Then install the project dependencies with

```
pip install -r requirements.txt
```
Now you can run the project with this command

```
python manage.py runserver
```
Note if you want payments to work you will need to enter your own Stripe API keys into the .env file in the settings files.
