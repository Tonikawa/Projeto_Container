FROM python:3

WORKDIR /app

COPY requirementes.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "app.py"]