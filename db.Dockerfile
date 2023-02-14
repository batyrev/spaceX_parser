FROM postgres:13

ENV POSTGRES_DB spacex
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD admin

COPY init.sql /docker-entrypoint-initdb.d/