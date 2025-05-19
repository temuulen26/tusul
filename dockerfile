FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt ./

RUN pip install flask
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
ENV FLASK_APP=app.py

CMD ["python3", "-m","flask", "run", "--host=0.0.0.0"]
