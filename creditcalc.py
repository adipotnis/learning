
# write your code here
def para_search(args, name, floatflag = False):
    for index in args:
        if name in index:
            if floatflag:
                return True, float(index.split('=')[1])
            return True, int(round(float(index.split('=')[1])))
    return False, 0

import sys
from math import ceil, log, floor
args = sys.argv[1:]
totalpay = 0
periods = para_search(args, 'periods')[1]
principal = para_search(args, 'principal')[1]
interest = para_search(args, 'interest', True)[1] / 1200
payment = para_search(args, 'payment', True)[1]

#negative test
if (para_search(args, 'principal')[1] < 0) or (para_search(args, 'periods')[1] < 0) or (para_search(args, 'interest')[1] < 0) or (para_search(args, 'payment')[1] < 0):
    print('Incorrect parameters')

    #diff or annuity type mistakes or missing parameters
elif len(args) < 4 or 'type' not in args[0] or not ('diff' in args[0] or 'annuity' in args[0]):
    print('Incorrect parameters')
#------------- pending incorrect parameters

#-------------------------------
elif 'diff' in args[0]:
    if para_search(args, 'payment')[0]:
        print('Incorrect parameters')
    else:
        for month in range(1, periods+1):
            monthpay = ceil((principal / periods) + (interest * (principal - (principal * (month-1)/periods))))
            print('Month {}: paid out {}'.format(month, monthpay))
            totalpay += monthpay
        overpay = totalpay - principal
        print()
        print('Overpayment = {}'.format(overpay))


elif 'annuity' in args[0]:
    if not para_search(args, 'principal')[0]:
        principal = payment / ((interest * pow(1 + interest, periods)) / (pow(1 + interest, periods) - 1))

        print('Your annuity payment = {}!'.format(floor(principal)))
        overpay = periods * payment - principal

    elif not para_search(args, 'periods')[0]:
        periods = int(ceil(log( (payment/(payment - interest * principal)), 1 + interest)))
        years = floor(periods/12)
        months = periods - years * 12

        if months == 0:
            print('You need {} year{} to repay this credit!'.format(years, 's'*int(years!=1)))
        elif years == 0:
            print('You need {} month{} to repay this credit!'.format(months, 's'*int(months!=1)))
        else:
            print('You need {} year{} {} month{} to repay this credit!'.format(years, 's'*int(years!=1), months, 's'*int(months!=1)))
        overpay = payment * periods - principal

    elif not para_search(args, 'payment')[0]:
        payment = ceil(principal * (interest * pow(1 + interest, periods)) / (pow(1 + interest, periods) - 1))
        print('Your annuity payment = {}!'.format(payment))
        overpay = payment * periods - principal

    print()
    print('Overpayment = {}'.format(ceil(overpay)))
