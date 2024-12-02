# import subprocess
# heroku_app_name = "john-app-postgres-db"
# raw_db_url = subprocess.run(
#     ["heroku", "config:get", "DATABASE_URL", "--app", heroku_app_name],
#     capture_output=True  # capture_output arg is added in Python 3.7
# ).stdout 

# print(raw_db_url)

# ---------------------------------------------------------------------------------------------------------------

import subprocess
from sqlalchemy.engine.create import create_engine

# Get the Database URL using Heroku CLI
# -------------------------------------
# Running the following from Python: $heroku config:get DATABASE_URL --app your-app-name
heroku_app_name = "john-app-postgres-db"

# Assumption: HEROKU_API_KEY is set in your terminal
# You can confirm that it's set by running the following python command os.environ["HEROKU_API_KEY"]
raw_db_url = subprocess.run(
    ["heroku", "config:get", "DATABASE_URL", "--app", heroku_app_name],
    capture_output=True  # capture_output arg is added in Python 3.7
).stdout 

print(raw_db_url)

# Convert binary string to a regular string & remove the newline character
db_url = raw_db_url.decode("ascii").strip()

# Convert "postgres://<db_address>"  --> "postgresql+psycopg2://<db_address>" needed for SQLAlchemy
# lstrip() is more suitable here than replace() function since we only want to replace postgres at the start!
final_db_url = "postgresql+psycopg2://" + db_url.lstrip("postgres://") 

# ---------------------------------------------------------------------------------------------------------------

# Create SQLAlchemy engine
# ------------------------
engine = create_engine(final_db_url)

import pandas as pd
from sqlalchemy.types import Integer, DateTime

DATA_URL = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/latest/owid-covid-latest.csv"
df = pd.read_csv(DATA_URL)

df.to_sql(
    "covid19",  # table name
    con=engine,
    if_exists='replace',
    index=False,  # In order to avoid writing DataFrame index as a column
    dtype={
        "last_updated_date": DateTime(),
        "total_cases": Integer(),
        "new_cases": Integer()
    }
)
# engine.execute("DROP TABLE covid19") 
