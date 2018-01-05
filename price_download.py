import requests
import pandas
import argparse
import datetime
import os

def download_prices(currencies, from_date):
    """Download prices to USD of a list of currencies ticker.
    Args:
    -----
    currencies: list of crypto tickers
    from_date: datetime to start downloading historical data from
    
    Returns: pandas dataframe with the crypto tickers as columns and datetimes
    as rows.
    """
    if from_date is None:
        from_date = datetime.datetime.now() - datetime.timedelta(days=30)
    delta = (datetime.datetime.now() - from_date).days
    delta = delta if delta >= 1 else 1
    base_url = "https://min-api.cryptocompare.com/data/histoday?fsym={curr}&tsym=USD&limit={delta}&aggregate=1"
    tmp = []
    for currency in currencies:
        r = requests.get(base_url.format(curr=currency, delta=str(delta)))
        prices = pandas.DataFrame(r.json()['Data'])
        prices['time'] = pandas.to_datetime(prices['time'], unit='s')
        prices = prices.set_index('time')['close']
        prices = prices.rename(currency)
        tmp.append(prices) 
    
    return pandas.DataFrame(tmp).transpose()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--from_date', help='The first date of data',
                        default=None)
    parser.add_argument('--currencies', nargs='+', 
                        help='<Required> Set of currencies', required=True)
    parser.add_argument('--out_file', default="crypto_prices.csv")
    args = parser.parse_args()
    print(args)
    cwd = os.getcwd()
    filepath = os.path.join(cwd, args.out_file)
    from_date = pandas.to_datetime(args.from_date)
    prices = download_prices(args.currencies, from_date)
    prices.to_csv(filepath)
    
