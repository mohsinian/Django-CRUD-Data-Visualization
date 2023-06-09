from django.shortcuts import render
import json
import uuid
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, request
from django.template.loader import render_to_string
from .models import TableStockData
import django_tables2 as tables
from django.contrib import messages
from table_vis.models import TableStockData
from table_vis.forms import edit_form
import plotly.express as px
from django.views.generic import TemplateView
# def tableview(request):
#     queryset = TableStockData.objects.all()
#     return render (request, "tableview.html", {'queryset':queryset})

# class SimpleTable(tables.Table):
#     class Meta:
#         model = TableStockData
#         fields =("date","trade_code","high","low","open","close",'volume')


# class tableview(tables.SingleTableView):
#     table_class = SimpleTable
#     queryset = TableStockData.objects.all()
#     template_name = 'tableview.html'

def tableview(request):
    tabledata = TableStockData.objects.all()
    context = {'tabledata': tabledata}
    return render(request, 'tableview.html', context)


def data_insert(request):
    if request.POST.get('date') and request.POST.get('trade_code') and request.POST.get('high') and request.POST.get('low') and request.POST.get('open') and request.POST.get('close') and request.POST.get('volume'):
        save_data = TableStockData()
        id = uuid.uuid4()
        save_data.id = str(id)
        save_data.date = request.POST.get('date')
        save_data.trade_code = request.POST.get('trade_code')
        save_data.high = request.POST.get('high')
        save_data.low = request.POST.get('low')
        save_data.open = request.POST.get('open')
        save_data.close = request.POST.get('close')
        save_data.volume = request.POST.get('volume')
        save_data.save()
        messages.success(request, "Saved!")
        return render(request, "create.html")
    else:
        return render(request, "create.html")


def data_edit(request, id):
    edit_data = TableStockData.objects.get(id=id)
    return render(request, 'edit.html', {"edit_data": edit_data})


def data_update(request, id):
    data_update = TableStockData.objects.get(id=id)
    form = edit_form(request.POST, instance=data_update)
    if form.is_valid():
        form.save()
        messages.success(request, "data updated")
        return render(request, "edit.html", {"data_update": data_update})
    else:
        messages.success(request, "somehting wrong")
        return render(request, "edit.html", {"data_update": data_update})


def data_delete(request, id):
    data_delete = TableStockData.objects.get(id=id)
    data_delete.delete()
    tabledata = TableStockData.objects.all()
    context = {'tabledata': tabledata}
    return render(request, 'tableview.html', context)


def chart(request):
    date_col = []
    close_col = []
    dateobj = TableStockData.objects.values_list('date', flat=True)
    closeobj = TableStockData.objects.values_list('close', flat=True)
    for i in dateobj:
        date_col.append(i)
    for i in closeobj:
        close_col.append(i)
    fig = px.line(
        x=date_col,
        y=close_col
    )
    volumeobj = TableStockData.objects.values_list('volume', flat=True)
    volume_col=[]
    for i in volumeobj:
        volume_col.append(i)
    fig2  = px.bar(
        x = date_col,
        y = volume_col
    )
    chart = fig.to_html()
    chart2 = fig2.to_html()
    fig.add_bar(
        x = date_col,
        y = volume_col
    )
    chart3 = fig.to_html()
    context = {"chart": chart, "chart2":chart2, "chart3":chart3}
    return render(request, 'chart.html', context)

# def chart(request):
#     date_col = TableStockData.objects.values_list('date',flat=True)
#     close_col = TableStockData.objects.values_list('close',flat=True)
#     context = {
#         "date_col" : date_col,
#         "close_col" : close_col,
#     }
#     return render(request,'tableview.html',context)
