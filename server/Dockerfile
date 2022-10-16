FROM python:3.9

ADD ./ /server
ADD requirements.txt /server/

WORKDIR /server

RUN pip install -r requirements.txt

# CMD ["python3", "main.py"]
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]