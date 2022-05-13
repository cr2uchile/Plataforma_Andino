FROM python:3.8.0-buster

WORKDIR /App

COPY . .

COPY requirements.txt .
COPY * ./
RUN pip install -r requirements.txt

#COPY . App/ 

EXPOSE 8071

CMD ["python","/App/Inicio.py"]

