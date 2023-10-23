FROM python:3.9

WORKDIR /app
COPY . ./
RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt