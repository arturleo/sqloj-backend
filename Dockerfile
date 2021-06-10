# following flask-restplus-server-example

FROM frolvlad/alpine-python3

ENV API_SERVER_HOME=/app
WORKDIR "$API_SERVER_HOME"
COPY "./requirements.txt" "./"
COPY "./wsgi.py" "./"
COPY "./sqloj_backend" "./sqloj_backend"
COPY "./deploy/supervisord.conf" "./"
COPY "./deploy/nginx/nginx.conf" "./"

RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.6/main' >> /etc/apk/repositories
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.6/community' >> /etc/apk/repositories

RUN apk add --no-cache --virtual=.build_dependencies musl-dev gcc python3-dev libffi-dev linux-headers
RUN apk add --no-cache nginx mongodb supervisor
RUN cd /app && \
    mkdir log && \
    pip install -r requirements.txt && \
    rm -rf ~/.cache/pip && \
    apk del .build_dependencies

VOLUME ["/data/db"]

EXPOSE 12333,5366

CMD ["/usr/bin/supervisord", "-c", "/app/supervisord.conf"]