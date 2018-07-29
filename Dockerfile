FROM python:3.6-slim
WORKDIR /home
EXPOSE 8000
RUN mkdir app
WORKDIR /home/app
ADD . /home/app
RUN pip install -r requirements.txt &&\
python manage.py migrate &&\
python manage.py loaddata initdata
CMD python manage.py runserver 0:8000