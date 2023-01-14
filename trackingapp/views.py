from django.shortcuts import render
from yahoo_fin import stock_info as si

# Create your views here.
def stockPicker(request):
    stock_picker = si.tickers_nifty50()
    print(len(stock_picker), " : ",stock_picker)
    return render(request, 'trackingapp/stockpicker.html', {"stockpicker":stock_picker}) 

def stockTracker(request):
    return render(request, 'trackingapp/stocktracker.html') 