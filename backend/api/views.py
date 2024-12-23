from asgiref.sync import sync_to_async
from django.http import JsonResponse
from ninja_extra import NinjaExtraAPI
from .models import Mobiles

api = NinjaExtraAPI()


@api.get("/items")
async def list_items(request):
    items = await sync_to_async(list)(Mobiles.objects.values())
    return JsonResponse({"items": items}, safe=False)
