FROM python:3

WORKDIR /app

COPY api_contact.py /app

COPY requirements.txt /etc/

RUN pip3 install -r /etc/requirements.txt

EXPOSE 5000

CMD ["python3","api_contact.py"]
