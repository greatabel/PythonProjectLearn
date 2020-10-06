from django.http import HttpResponse
from django.shortcuts import render
import psycopg2

from .models import Item, Warehouse, Stock
# conn = psycopg2.connect(database="TPCC", user="postgres", password="postgres", host="localhost", port="5432")
# print("Opened database successfully")

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    wlist = None

    item_parameter = request.GET.get('item', '')
    print('item_parameter=', item_parameter)
    if item_parameter != '':

        item_queryset = Item.objects.filter(
            i_name__startswith=item_parameter
            ).values_list('i_id', flat=True)
        item_ids = list(item_queryset)
        print('0 item_ids=', item_ids)

        if len(item_ids) != 0:
            stock_queryset = Stock.objects.filter(i_id__in=item_ids).values_list('w_id', flat=True)
            w_ids = list(stock_queryset)
            print('0 w_ids=', w_ids)
            

            warehouse_queryset = Warehouse.objects.filter(w_id__in=w_ids).values('w_id', 'w_name')

            wlist = list(warehouse_queryset)

    warehouse_parameter = request.GET.get('warehouse', '')
    print('warehouse_parameter=', warehouse_parameter)
    if warehouse_parameter != '':
        warehouse_queryset = Warehouse.objects.filter(
            w_name__startswith=warehouse_parameter
            ).values_list('w_id', flat=True)
        w_ids = list(warehouse_queryset)
        print('1 w_ids=', w_ids, 'item_ids=', item_ids) 
        stock_queryset = Stock.objects.filter(w_id__in=w_ids, i_id__in=item_ids).values('w_id', 'i_id', 's_qty')
        print('1 stock=', stock_queryset, len(stock_queryset))
    # print('wlist=', wlist)
    context = {
        'wlist': wlist,

    }    
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'AppLine/index.html', context=context)