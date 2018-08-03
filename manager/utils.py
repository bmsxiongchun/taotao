from manager.models import TbItem


def getitemlist(page, rows):
    tbItem = TbItem.objects.all()
    return tbItem