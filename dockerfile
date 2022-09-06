FROM python
LABEL Author="Salim Said Hemed"
LABEL Version="0.0.1"
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD flask run --host=0.0.0.0