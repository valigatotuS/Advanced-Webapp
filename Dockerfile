FROM python:3.10.4
ADD src/requirements.txt ./webapp/requirements.txt
RUN pip install -r ./webapp/requirements.txt
ADD src/ ./
#RUN source .venv/bin/activate
CMD python3 wsgi.py
EXPOSE 8080/TCP