FROM python:latest
LABEL Author="Salim Said Hemed"
LABEL Version="0.0.1"
WORKDIR /app
ADD requirements.txt /app/ 
EXPOSE 5000
ENV FLASK_DEBUG=0
RUN pip install -r requirements.txt
CMD ["python","app.py"]