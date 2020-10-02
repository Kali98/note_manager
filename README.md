# What is required for running the project
Python3 along with the Django framework and PGAdmin for managing the PostgreSQL database. All of the other unmentioned requirements are listed within 'requirements.txt'. To install; firstly navigate to the directory where the project was cloned and proceed to activate a virtual environment and install the requirements using command below:
```
pip install -r requirements.txt
```
# Steps how to run scripts that will setup database for the project
1.  Since this webservice is accomodated with a PostgreSQL backend; first of all go to settings.py located under: 
    
    **note_manager\restful_api_web_app\restful_api_web_app\settings.py**
    
    Scroll down to database specs and replace the password value with your passoword from pgAdmin (the default username should be 'postgres')

2. Make migrations for the django generated tables with command:
```
python manage.py makemigrations restful_api_web_app
```
3. Make migrations for the model tables (note & notechange):
```
python manage.py makemigrations note_api
```
4. Confirm and create all migrations
```
python manage.py migrate
```
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
curl --location --request PUT 'http://127.0.0.1:8000/api/note-modify/1/' --header 'Content-Type: application/json' --data-raw '{"title": "My New Note","content": "I Actually do not like this note"}'
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