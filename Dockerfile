FROM python:3.9.16-alpine3.16

COPY . .

WORKDIR /backend/

RUN pip install -r requirements.txt

EXPOSE 3040

CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "3040" ]