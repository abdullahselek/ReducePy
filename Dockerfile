FROM python:3.4-alpine
ADD reducepy/ /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "reducepy/app.py"]
