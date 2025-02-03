#!/bin/bash

# Start Redis in the background
redis-server &

# Apply migrations
python manage.py migrate

# Start Django server
python manage.py runserver 127.0.0.1:8000

