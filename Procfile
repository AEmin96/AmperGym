web: sh -c 'cd ampergym && daphne ampergym.asgi:application --port $PORT --bind 0.0.0.0'
web: python project/manage.py collectstatic --noinput; gunicorn --pythonpath project project.wsgi