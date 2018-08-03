from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.
from manager.utils import getitemlist


class ItemController(object):

    @staticmethod
    def getitembyid(request):
        return render_to_response('manager/item-param-list.html')

    @staticmethod
    def getitemlist(request):
        page = request.GET.get('page', 1)
        rows = request.GET.get('rows', 30)
        response = getitemlist(page, rows)
        return render_to_response('manager/item-list.html', context={'tbitem': response})

    @staticmethod
    def saveitem(request):
        pass

    @staticmethod
    def additem(request):
        return render_to_response('manager/item-add.html')


def index(request):
    return render(request, 'manager/index.html')


class ContentController(object):

    @staticmethod
    def getcontent(request):
        return render_to_response('manager/content.html')


class ContentCategoryController(object):
    @staticmethod
    def getcontentcategorylist(request):
        pass

    @staticmethod
    def updatecontentcategory(request):
        pass

    @staticmethod
    def createcontentcategory(request):
        pass

    @staticmethod
    def deletecontentcategory(request):
        pass
