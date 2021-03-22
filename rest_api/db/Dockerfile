#Build db
FROM postgres:13 as dumper

COPY test_dump.sql /docker-entrypoint-initdb.d/

RUN ["sed", "-i", "s/exec \"$@\"/echo \"skipping...\"/", "/usr/local/bin/docker-entrypoint.sh"]

ENV POSTGRES_USER=ase_user
ENV POSTGRES_PASSWORD=aseisgreat
ENV PGDATA=/data

RUN ["/usr/local/bin/docker-entrypoint.sh", "postgres"]

# run postgres
FROM postgres:13

COPY --from=dumper /data $PGDATA