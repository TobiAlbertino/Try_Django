from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    contex = {
        'title' : 'Home Page',
        'content' : 'ini adalah home page dari website ini',
    }
    return render(request, 'index.html', contex)

def link(request, page):
    str = "<h1> {} </h1>".format(page)
    return HttpResponse(str)

def angka(request, input):
    heading = "<h1>Page Angka</h1>"
    str = heading = input
    return HttpResponse(str)

def tanggal(request,**input):
    print(input)
    tahun = input['tahun']
    bulan = input['bulan']
    hari = input['hari']
    heading = "<h1> Page Tnggal </h1>"
    formatTanggal = "<h2> {}/{}/{} </h2>".format(tahun,bulan,hari)
    return HttpResponse(heading + formatTanggal)

#def tanggal(request,tahun, bulan, hari):
#    print(input)
#    heading = "<h1>Page Tanggal</h1>"
#    strTahun = "Tahun: " + tahun
#    strBulan = "bulan: " + bulan
#    strHari = "hari: " + hari
#    str = heading + strTahun + "<br>" + strBulan +"<br>" + strHari
#    return HttpResponse(str)

