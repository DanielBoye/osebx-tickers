ticker_count = 0
price_count = 1


values = [('AEGA', '0.9010'), ('AGLX', '30.00'), ('AIRX', '3.7000'), ('AKAST', '10.48')]


for value in values:
    ticker = value[0]
    price = float(value[1])
    if price.is_integer():
        print(f"{ticker} = {int(price)} kr")
    else:
        print(f"{ticker} = {price} kr")
