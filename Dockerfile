FROM python:3.10.4
ADD src/requirements.txt ./app/requirements.txt
RUN pip install -r ./app/requirements.txt
ADD src/ ./
#RUN source .venv/bin/activate
# CMD openvpn ValentinQuevy.ovpn
CMD python3 wsgi.py
EXPOSE 8080/TCP