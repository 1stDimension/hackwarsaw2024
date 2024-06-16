FROM python:3.11.5-slim
WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir .

CMD [ "uvicorn", "localhub.main:app", "--port", "80", "--host", "0.0.0.0" ]

EXPOSE 80