# What is required for running the project
To run the project you'll primarily need Python3 to execute '.py' files and pgAdmin to setup the database. All of the other unmentioned requirements such as Django and Django REST frameworks are listed within the 'requirements.txt' file. To install the contents of this file; navigate to the directory where you'll clone/install the project. Create and activate a virtual environment, clone the project and proceed to it's directory ( **cd note_manager** ).

To install the contents of 'requirements.txt'; enter the command below.
```
pip install -r requirements.txt
```
# Steps how to run scripts that will setup database for the project
1.  Start up pgAdmin, login and create a new database (i.e 'note_manager_db') 

2.  Edit the settings.py file located under: 
    
    **note_manager\restful_api_web_app\restful_api_web_app\settings.py**
    
    Scroll down to database specifications and replace the password value with your password from pgAdmin (the default username should be 'postgres') and if you have created a database with a different name then appropriately change that piece of information as well.

3.  Navigate into the first **restful_api_web_app** folder with the terminal where the 'manage.py' file will be accessible and create migrations for the model and the django generated tables using command below:
```
python manage.py migrate
```
At this point if you refresh the database in pgAdmin you'll see all of the newly generated tables.

# Steps how to build and run the project
1.  Run the server with command:
```
python manage.py runserver
```
2.  Navigate to the web api with the address displayed in the terminal for example:
    http://127.0.0.1:8000/api/

# Example Usages
## Regular usage examples:
- GET all notes:    http://127.0.0.1:8000/api/note-list/
- GET note by id:   http://127.0.0.1:8000/api/note-list/1/
- POST create new note: http://127.0.0.1:8000/api/note-create/
- PUT update note:  http://127.0.0.1:8000/api/note-modify/1/
- DELETE delete note:   http://127.0.0.1:8000/api/note-modify/1/
- GET all note changes: http://127.0.0.1:8000/api/notehistory-list/
- GET note changes by note id:  http://127.0.0.1:8000/api/notehistory-list/1/

## cUrl examples:
- Get all notes:
```
curl -i -H "Accept:application/json" -H "Content-Type:application/json" -XGET "http://127.0.0.1:8000/api/note-list/"
```
- GET note by ID:
```
curl -i -H "Accept:application/json" -H "Content-Type:application/json" -XGET "http://127.0.0.1:8000/api/note-list/1/"
```
- POST create new:
```
curl -i -H "Accept:application/json" -H "Content-Type:application/json" -XPOST "http://127.0.0.1:8000/api/note-create/" -d '{"title":"My New Note", "content":"I have created this new note with utter most passion"}'
```
- PUT update note:
```
curl -i -H "Accept:application/json" -H "Content-Type:application/json" -XPUT "http://127.0.0.1:8000/api/note-modify/1/" -d '{"title": "My New Note","content": "I actually do not like this note"}'
```
- DELETE delete note:
```
curl -i -H "Accept:application/json" -H "Content-Type:application/json" -XDELETE "http://127.0.0.1:8000/api/note-modify/1/"
```
- GET all note changes:
```
curl -i -H "Accept:application/json" -H "Content-Type:application/json" -XGET "http://127.0.0.1:8000/api/notehistory-list/"
```
- GET note changes by note id:
```
curl -i -H "Accept:application/json" -H "Content-Type:application/json" -XGET "http://127.0.0.1:8000/api/notehistory-list/1"
```
## Additional Notes
To run intergration tests; use command:
```
python manage.py test
```
