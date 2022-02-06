#!/bin/bash

apt-get update
apt-get install -y postgresql
sudo service postgresql start

sudo -u postgres psql -c "create user $PGUSER with password '$PGPASSWORD'"
sudo -u postgres createdb $PGDATABASE -O $PGUSER

pipx install poetry
poetry install

git submodule update --init

poetry run dbt deps --project-dir dbt_projects/poffertjes_shop
poetry run dbt build --project-dir dbt_projects/poffertjes_shop
poetry run dbt docs generate --project-dir dbt_projects/poffertjes_shop
poetry run dbt snapshot --project-dir dbt_projects/poffertjes_shop
poetry run dbt source freshness --project-dir dbt_projects/poffertjes_shop