# I wanted to use Docker as per a tutorial, but is a bit of an overkill for my small app. 
FROM python:3.10
COPY requirements.txt /dogsapp/requirements.txt
WORKDIR /dogsapp
RUN pip install -r requirements.txt
COPY . /dogsapp
ENTRYPOINT [ "python" ]
CMD [ "run.py" ]
