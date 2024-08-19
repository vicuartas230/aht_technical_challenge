FROM python:3.12.5-alpine3.20

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV DB_USER=root

ENV DB_PASSWORD=YjzaocHbnuEBSljCQIcjEXAYEKJDLnet

ENV DB_HOST=autorack.proxy.rlwy.net:40127

ENV DB_NAME=railway

CMD [ "flask", "run", "--host=0.0.0.0" ]
