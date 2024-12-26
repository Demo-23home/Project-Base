
FROM docker.io/python:3.12.2-slim-bookworm AS python 

# Stage1: Building Dependency Wheels.
FROM python AS python-build-stage

ARG BUILD_ENVIRONMENT=local

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev

COPY ./requirements .

RUN pip wheel --wheel-dir /usr/src/app/wheels \
    -r ${BUILD_ENVIRONMENT}.txt

# Stage2: Python Run Stage.
FROM python AS python-run-stage

ARG BUILD_ENVIRONMENT=local

ARG APP_HOME=/app

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

ENV BUILD_ENV {BUILD_ENVIRONMENT}

WORKDIR ${APP_HOME}

RUN apt-get update && apt-get install --no-install-recommends -y \
    sudo git bash-completion nano ssh

RUN addgroup --system django && \
    adduser --system --ingroup django django && \
    mkdir -p {APP_HOME}/staticfiles && \
    chown django:django {APP_HOME}/staticfiles && \
    chmod 755 {APP_HOME}/staticfiles

RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

COPY --from=python-build-stage /usr/src/app/wheels /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/

# entrypoint configurations    
COPY --chown=django:django ./docker/local/django/entrypoint.sh /entrypoint
RUN sed -i "s/\r$//g" /entrypoint
RUN chmod +x /entrypoint

# start configurations 
COPY --chown=django:django ./docker/local/django/start.sh/ /start
RUN sed -i "s/\r$//g" /start
RUN chmod +x /start

# celeryworker configurations 
COPY --chown=django:django ./docker/local/django/celery/worker/start.sh /start-celeryworker
RUN sed -i "s/\r$//g" /start-celeryworker
RUN chmod +x /start-celeryworker

# celerybeat configurations
COPY --chown=django:django ./docker/local/django/celery/beat/start.sh /start-celerybeat
RUN sed -i "s/\r$//g" /start-celerybeat
RUN chmod +x /start-celerybeat

# celerybeat configurations
COPY --chown=django:django ./docker/local/django/celery/flower/start.sh /start-flower
RUN sed -i "s/\r$//g" /start-flower
RUN chmod +x /start-flower

# app code configurations
COPY --chown=django:django . {APP_HOME}
RUN chown django:django {APP_HOME}

USER django

# USER root

ENTRYPOINT [ "/entrypoint" ]
