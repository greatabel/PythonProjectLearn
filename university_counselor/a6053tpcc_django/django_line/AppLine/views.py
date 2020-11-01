from django.http import HttpResponse
from django.shortcuts import render
import psycopg2

from .models import Item, Warehouse, Stock
from .common import handle_stock_update
# conn = psycopg2.connect(database="TPCC", user="postgres", password="postgres", host="localhost", port="5432")
# print("Opened database successfully")

# changed according to new requirement
def index_v1(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    all_item_queryset = Item.objects.all().order_by('i_name').values('i_id', 'i_name')
    all_item_list = list(all_item_queryset)

    wlist, slist = None, None
    still_can_order_flag = 'T'

    item_id_parameter = request.GET.get('item_id', '')
    warehouse_id_parameter = request.GET.get('warehouse_id', '')
    action_parameter = request.GET.get('action', '')
    qty_parameter = request.GET.get('qty', '')

    print('item_id_parameter=', item_id_parameter,
          'warehouse_id_parameter=', warehouse_id_parameter,
          'qty_parameter=', qty_parameter=='')
    if item_id_parameter != '':
        item_ids = [int(item_id_parameter)]

        print('0 item_ids=', item_ids)

        if len(item_ids) != 0:
            stock_queryset = Stock.objects.filter(i_id__in=item_ids).values_list('w_id', flat=True)
            w_ids = list(stock_queryset)
            print('0 w_ids=', w_ids)
            

            warehouse_queryset = Warehouse.objects.filter(w_id__in=w_ids).values('w_id', 'w_name')

            wlist = list(warehouse_queryset)
            print('0 wlist=', wlist)



    if warehouse_id_parameter != '':
        w_ids = [int(warehouse_id_parameter)]
        print('1 w_ids=', w_ids, 'item_ids=', item_ids) 
        stock_queryset = Stock.objects.filter(w_id__in=w_ids, 
                        i_id__in=item_ids).values('w_id', 'i_id', 's_qty')
        print('1 stock=', stock_queryset, len(stock_queryset))
        slist = list(stock_queryset)
        print(slist)
    if qty_parameter != '':
        qty = int(qty_parameter)
    else:
        qty = 0

    if  qty > 0:
        total = 0
        for s in slist:
            total += s['s_qty']

        if total < qty and action_parameter == 'order':
            still_can_order_flag = 'F'

        handle_stock_update(slist, qty, action_parameter)
        # db is changed, so should query again
        stock_queryset = Stock.objects.filter(w_id__in=w_ids, 
                        i_id__in=item_ids).values('w_id', 'i_id', 's_qty')
        print('2 stock=', stock_queryset, len(stock_queryset))
        slist = list(stock_queryset)

    elif qty == 0:
        still_can_order_flag = 'D'
    # print('wlist=', wlist)
    print('still_can_order_flag=', still_can_order_flag)
    context = {
        'all_item_list': all_item_list,
        'wlist': wlist,
        'slist': slist,

        'still_can_order_flag': still_can_order_flag,

    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'AppLine/index_v1.html', context=context)


# def index(request):
#     # return HttpResponse("Hello, world. You're at the polls index.")
#     wlist, slist = None, None
#     still_can_order_flag = 'T'

#     item_parameter = request.GET.get('item', '')
#     warehouse_parameter = request.GET.get('warehouse', '')
#     action_parameter = request.GET.get('action', '')
#     qty_parameter = request.GET.get('qty', '')

#     print('item_parameter=', item_parameter,
#           'warehouse_parameter=', warehouse_parameter,
#           'qty_parameter=', qty_parameter=='')
#     if item_parameter != '':

#         item_queryset = Item.objects.filter(
#             i_name__startswith=item_parameter
#             ).values_list('i_id', flat=True)
#         item_ids = list(item_queryset)
#         # print('0 item_ids=', item_ids)

#         if len(item_ids) != 0:
#             stock_queryset = Stock.objects.filter(i_id__in=item_ids).values_list('w_id', flat=True)
#             w_ids = list(stock_queryset)
#             # print('0 w_ids=', w_ids)
            

#             warehouse_queryset = Warehouse.objects.filter(w_id__in=w_ids).values('w_id', 'w_name')

#             wlist = list(warehouse_queryset)



#     if warehouse_parameter != '':
#         warehouse_queryset = Warehouse.objects.filter(
#             w_name__startswith=warehouse_parameter
#             ).values_list('w_id', flat=True)
#         w_ids = list(warehouse_queryset)
#         print('1 w_ids=', w_ids, 'item_ids=', item_ids) 
#         stock_queryset = Stock.objects.filter(w_id__in=w_ids, 
#                         i_id__in=item_ids).values('w_id', 'i_id', 's_qty')
#         print('1 stock=', stock_queryset, len(stock_queryset))
#         slist = list(stock_queryset)
#         print(slist)
#     if qty_parameter != '':
#         qty = int(qty_parameter)
#     else:
#         qty = 0

#     if  qty > 0:
#         total = 0
#         for s in slist:
#             total += s['s_qty']

#         if total < qty and action_parameter == 'order':
#             still_can_order_flag = 'F'

#         handle_stock_update(slist, qty, action_parameter)
#         # db is changed, so should query again
#         stock_queryset = Stock.objects.filter(w_id__in=w_ids, 
#                         i_id__in=item_ids).values('w_id', 'i_id', 's_qty')
#         print('2 stock=', stock_queryset, len(stock_queryset))
#         slist = list(stock_queryset)

#     elif qty == 0:
#         still_can_order_flag = 'D'
#     # print('wlist=', wlist)
#     print('still_can_order_flag=', still_can_order_flag)
#     context = {
#         'wlist': wlist,
#         'slist': slist,

#         'still_can_order_flag': still_can_order_flag,

#     }

#     # Render the HTML template index.html with the data in the context variable
#     return render(request, 'AppLine/index.html', context=context)