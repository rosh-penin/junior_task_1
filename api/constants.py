from os import getenv

DB_ENGINE = getenv('DB_ENGINE', None)
DB_USER = getenv('POSTGRES_USER', None)
DB_PASS = getenv('POSTGRES_PASSWORD', None)
DB_NAME = getenv('DB_NAME', None)
DB_HOST = getenv('DB_HOST', None)
DB_PORT = getenv('DB_PORT', None)
SHEET_NAME = 'data'
COLUMNS_LIMIT = 102
ROWS_LIMIT = 100001
