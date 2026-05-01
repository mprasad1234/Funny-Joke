FROM python:stable-alpine as firststage
WORKDIR /myapp
COPY requirements.txt .
RUN pip install -r requirements.txt --production
COPY . .

FROM firststage as final
RUN pip install -r requirements.txt --production
COPY . .
CMD ["python" , "app.py"]


