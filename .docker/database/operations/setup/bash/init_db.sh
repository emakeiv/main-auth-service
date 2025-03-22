#!/bin/bash

set -euo pipefail

echo "database initialization started"

# preventing race conditions during startup.
until pg_isready $POSTGRES_USER -d $POSTGRES_DB; do
    echo "waiting for database to start."
    sleep 5
done

psql -v ON_ERROR_STOP=1 -U "$POSTGRES_USER" -d "$POSTGRES_DB" <<-EOSQL
  \echo 'running create_database_user.sql'
  \i /docker-entrypoint-initdb.d/create_database_user.sql

  \echo 'running create_database.sql'
  \i /docker-entrypoint-initdb.d/create_database.sql

  \echo 'running create_users_table.sql'
  \i /docker-entrypoint-initdb.d/create_users_table.sql
EOSQL