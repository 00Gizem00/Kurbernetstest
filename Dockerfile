FROM python:3.12.3-slim

COPY . /app

WORKDIR /app

RUN python3 -m venv /opt/env

RUN pip install --upgrade pip
RUN /opt/env/bin/pip install -r requirements.txt
RUN chmod +x /app/entrypoint.sh

CMD [ "/app/entrypoint.sh" ]


