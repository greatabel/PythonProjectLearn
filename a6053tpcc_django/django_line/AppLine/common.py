from django.db import connection
from django.db import transaction


def handle_stock_update(slist, qty, action):

    subs = []
    total = 0
    if action == 'order':
        for s in slist:
            total += s['s_qty']
            
            if total >= qty:
                too_much = total - qty
                subs.append([s['w_id'], s['i_id'], too_much])
                break
            else:
                subs.append([s['w_id'], s['i_id'], 0])
    elif action == 'delivery':
        subs = [[slist[0]['w_id'], slist[0]['i_id'], slist[0]['s_qty']+qty]]

    print('#'*10, subs)

    with transaction.atomic():
        # This code executes inside a transaction
         my_custom_sql(subs)


def my_custom_sql(subs):
    with connection.cursor() as cursor:
        for sub in subs:
            sql = "UPDATE stock SET s_qty = " + str(sub[2]) +\
                             " WHERE w_id = " + str(sub[0]) + " and i_id = " + str(sub[1]) + ";" 
            print(sql)
            cursor.execute(sql)
            


