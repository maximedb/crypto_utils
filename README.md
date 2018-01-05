# crypto_utils
Utilities functions for crypto currencies

## Crypto currencies price download with Python
´crypto_prices.py´ easily download prices of cypto currencies with Python

You can use it with the command line: 
´python crypto_prices.py --currencies ETH BTC XRP XLM --from_date 01/09/2016´

or with Python:
´´´
from crypto_prices import download_prices
prices = download_prices(['ETH', 'BTC'], '01/01/2018')
´´´
