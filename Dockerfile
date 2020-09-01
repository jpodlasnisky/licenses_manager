FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /license_portal
WORKDIR /license_portal
COPY requirements.txt /license_portal/
RUN pip install -r requirements.txt
COPY . /license_portal/