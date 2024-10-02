from pathlib import Path
import pendulum
import yfinance
from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
from airflow.macros import ds_add

TICKERS = [
    "AAPL",
    "MSFT",
    "GOOG",
    "TSLA"
]

@task()
def get_history(ticker, ds=None, ds_nodash=None):
    file_path = f"/data/{ticker}/{ticker}_{ds_nodash}.csv"
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    yfinance.Ticker(ticker).history(
        period="1d", 
        interval="1h",
        start=ds_add(ds, -1),
        end=ds,
        prepost=True,
    ).to_csv(file_path)

@dag(
    schedule_interval="0 0 * * *",
    start_date=pendulum.datetime(2024, 7, 20, tz="UTC"),
    catchup=True
)
def get_crypto_dag():
    for ticker in TICKERS:
        get_history(ticker, ds="{{ ds }}", ds_nodash="{{ ds_nodash }}").task_id = f"get_history_{ticker}"

dag = get_crypto_dag()