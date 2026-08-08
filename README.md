# Django 5 + Aiogram 3 webhook template
A template for webhooking a telegram bot in Django made in the aiogram 3 library. In the example of a simple bot!
___
### Management commands
#### 1. Create a Virtual Environment and activate environment:
   ```
   python3 -m venv myenv
   source venv/bin/activate
   ```
#### 2. Install all required packages
   ```pip install -r requirements.txt```
#### 3. Next, make a copy of the .env.example file for the Environment variables and create .env file in core/data


#### 4. Create migration files based on changes made to Django models and to apply the changes to the database
   ```
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
#### 5. To create an admin user in Django
   ```python3 manage.py createsuperuser```
#### 6. To gather all static files from your project and its apps into a single directory
   ```python3 manage.py collectstatic```
#### 7. To create a public URL for your local web server, allowing external access to it over the internet or domain.
   ```ngrok http 8000```
#### 8. SET webhook_domain to .env file from ngrok and configure environment variables as like .env.example
#### 9. Set webhook to your bot
   ```python3 manage.py setwebhook```
#### 10. Run an ASGI (Asynchronous Server Gateway Interface) application with Uvicorn
   ```uvicorn core.asgi:application --host 0.0.0.0 --port 8000```
___
### Bot commands: 
1. **/start**  starts the bot and create user in database
2. **/help**   show commands to user

### Bot ADMIN commands: 
1. **/allusers**  send users.xlsx to admin which contains all users in database
2. **/reklama**   send ad to all users
___
### If you have questions for this project, join and ask to me: 
*https://t.me/goldendevuz* <br><br>
*11.11.2024 - Project is ready to use.*


<p align="center">
<img style="width: 60%;" src="https://i.postimg.cc/PxkQS59n/breakdancing-together.gif">
</p>
