import uuid

from ninja import NinjaAPI, Schema

from deep4.prototype.models import Location, PlainText, RichText

api = NinjaAPI()


class STOut(Schema):
    id: uuid.UUID
    content: str


class RTOut(Schema):
    id: uuid.UUID
    content: str


class LocOut(Schema):
    id: uuid.UUID
    content_type: str
    object_id: uuid.UUID


@api.get("/pt_list", response=list[STOut], url_name="pt_list")
def get_plain_text_list(request):
    pts = PlainText.objects.all()
    return list(pts)


@api.get("/pt/{item_id}", response=STOut, url_name="pt_item")
def get_plain_text_item(request, item_id):
    st = PlainText.objects.get(id=item_id)
    return st


@api.get("/rt_list", response=list[RTOut], url_name="rt_list")
def get_rich_text_list(request):
    rts = RichText.objects.all()
    return list(rts)


@api.get("/rt/{item_id}", response=RTOut, url_name="rt_item")
def get_rich_text_item(request, item_id):
    rt = RichText.objects.get(id=item_id)
    return rt


@api.get("/loc/{item_id}", response=LocOut, url_name="loc_item")
def get_item(request, item_id):
    sr = Location.objects.get(id=item_id)
    return sr


@api.get("/loc_list", response=list[LocOut], url_name="loc_list")
def get_location_list(request):
    rts = RichText.objects.all()
    return list(rts)
