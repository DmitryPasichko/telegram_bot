# telegram_bot
Task list:
- DTB-1(feature) Add django into the project(DONE);
- DTB-2 (feature) Add djangorestframework and get following api endpoints:
  1. Register new user by Telegram account
  2. Get possibility to get info about your account (Name)
  3. Create new model - task
  4. Get possibility to execute following type of request with task: POST(create)
  , GET(get info about task or tasks), PUT(update task), DELETE(archive task)
- DTB-3(feature) Add roles for user - Manager and Developer
- DTB-4(feature) create docker compose file to run project into the docker containers
- DTB-4(feature) Add possibility for User with role admin can create task for developer
and user with role developer can get list of active task and assign it to himself;



python manage.py makemigrations - create migrations
python manage.py migrate - execute migrations
python manage.py createsuperuser - create superuser