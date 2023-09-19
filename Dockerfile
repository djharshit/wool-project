FROM python

WORKDIR /home/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "server.py"]
