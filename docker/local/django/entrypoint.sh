#!/bin/bash

set -o errexit

set -o pipefail

set -o nounset

python << END
import sys 
import time 
import psycopg2
suggest_unrecoverable_after = 30
start = time.time()
while True: 
    try: 
        psycopg2.connect(
            dbname = "${POSTGRES_DB}", 
            user = "${POSTGRES_USER}", 
            password = "${POSTGRES_PASSWORD}", 
            host = "${POSTGRES_HOST}", 
            port = "${POSTGRES_PORT}"
        )
        break
    except psycopg2.OperationalError as error:
        sys.stderr.write("Waiting for postgres to become available.... :( \n")
        if time.time() - start > suggest_recoverable_after: 
            sys.stderr.write("This is taking longer than expected, that might be an indicator of an irrecoverable error, '{error}' \n".format(error))
            sys.stderr.write("You might wanna check your '.env.local' :( ")
            time.sleep(1)
END

>&2 echo "Postgres is Available !"

exec "$@"


