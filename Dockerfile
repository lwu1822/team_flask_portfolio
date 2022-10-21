FROM docker.io/python:3.9

WORKDIR /app

# --- [Install python and pip] ---
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y python3 python3-pip git
RUN git clone https://github.com/lwu1822/team_flask_portfolio.git /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install gunicorn

ENV GUNICORN_CMD_ARGS="--workers=1 --bind=0.0.0.0:8056"

EXPOSE 8056

CMD [ "gunicorn", "main:app" ]
