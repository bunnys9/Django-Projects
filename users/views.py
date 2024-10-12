from django.shortcuts import render
from django.http import HttpResponse
from BankApp import *

import random
import sqlite3 as sql
# Create your views here.


# Generating numbers from 1000 to 9999, which are assigned to Customer Account numbers

def Accn_Num():
    mylist_accn_num = list(map(int, range(1000, 10000, 7)))
    accn_num = random.choice(mylist_accn_num)
    cust_accn_list = []

    if accn_num not in cust_accn_list:
        cust_accn_list.append(accn_num)
        return accn_num

    else:
        Accn_Num()

def home(request):
    cust_name = request.POST.get('cust_name')
    cust_dob = request.POST.get('cust_dob')
    cust_phno = request.POST.get('cust_phno')
    cust_add = request.POST.get('cust_add')
    bal = 0

    return render(request, 'home.html')