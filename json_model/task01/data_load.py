import json
from table_vis.models import table_vis

def load_data():
    with open('stock_market_data.json') as f :
        data = json.load(f)
    print(data)
    for i in data:
        tb = table_vis(date=i['date'], trade_code = i['trade_code'],high = i['high'], low =i['low'], open=i['open'], close = i['close'], volume = i['volume'] )
        tb.save()