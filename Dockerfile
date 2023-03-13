FROM python:3.9.7-slim-buster

COPY . .

RUN pip install -r requirements.txt

EXPOSE 3040

RUN chmod u+x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]