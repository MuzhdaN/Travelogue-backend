# Travelogue Backend


## Issues 
#### Deployement issues: 

- When deploying the api in heroku I would get this “`Application labels aren't unique, duplicates: registration`", the error I was encountering indicated that I have two applications with the same label 'registration' in my **`INSTALLED_APPS`**setting in Django.
    
    **Solved** it by checking the **`INSTALLED_APPS`** list in the Django settings file (usually **`settings.py`**) and removed one of the duplicated applications. 
    
- H10 error while deploying the api, the issue was that in the Procfile there was a name type of the app.
- “Bad Request 400” error, to solve this issue in the setting added the correct name of my api in the Heroku “**`ALLOWED_HOSTS = ['localhost', '<your_app_name>.herokuapp.com']`"**