FROM python:3.10.4
ADD src/requirements.txt ./app/requirements.txt
RUN pip install -r ./app/requirements.txt
ADD src/ /app/
#RUN source .venv/bin/activate
CMD python3 /app/wsgi.py
EXPOSE 8080/TCP