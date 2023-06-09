from django.shortcuts import render

# Create your views here.
import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
from django.template.loader import render_to_string

# Create your views here.

# with open('stock_market_data.json') as d:
#     data = json.load(d)


# def load_json_table_format(request):
#     print(data)
#     html = render_to_string()
#     return HttpResponse({'d':data}, 'tableview.html', content_type="application/html")
from json2html import *

# def read_data(): 
#     with open('task01/stock_market_data.json', 'r') as f: 
#         input_data = json.load(f)
#         print(input_data)
#     done = json2html.convert(json=input_data)
#     with open(".//templates//tableview.html",'w') as f:
#         f.writelines(done)
#         print(done)
#     return render(request, 'tableview.html')
#     return JsonResponse(safe=False)
data = open('stock_market_data.json').read()
jsonData = json.loads(data)
#print(jsonData)
def tablev(self):
    # result_list = list(jsonData.objects.all()\
    #             .values('date', 
    #                     'trade_code',
    #                     'high',

    #                     'low',
    #                     'open',
    #                     'close',
    #                     'volume',
    #                    ))
    return JsonResponse(jsonData,safe=False)
def tableview(request):
    context ={}
    return render(request, 'tableview.html', context)

