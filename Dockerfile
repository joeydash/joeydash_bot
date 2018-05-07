FROM python:3.4
COPY ./ /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
CMD ["python","app.py"]
