FROM python:3.9

COPY requirements.txt /tmp/requirements.txt

#RUN apt update -y && apt install -y curl

RUN pip3 install -r /tmp/requirements.txt

WORKDIR /app

ENV MODE=runserver
ENV PYTHONPATH "/app/app"

COPY . .

EXPOSE 8000

CMD bash -C "./start.sh"
#CMD ["python3", "./app/manage.py", "runserver", "0:8000"]
#CMD ["python3", "./app/manage.py", "runserver", "8000"]
#ENTRYPOINT