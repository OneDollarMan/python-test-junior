#!/bin/bash

cd src || { echo "Directory 'src' not found."; exit 1; }

alembic revision --message="Events table" --autogenerate
alembic upgrade head
