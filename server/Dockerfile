FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN echo "Running server"

ENV FLASK_APP=backend.py

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]