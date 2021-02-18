FROM python:3.7
WORKDIR /usr/src/app
COPY ./app ./app
RUN pip install fastapi uvicorn
EXPOSE 8000
RUN chmod 777 ./app/main.py
USER 1000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]