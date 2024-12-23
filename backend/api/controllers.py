from ninja_extra import api_controller, http_get
from .services import MyService
from ninja_extra import get_injector


@api_controller()
class MyController:
    @get_injector
    def __init__(self, service: MyService):
        self.service = service

    @http_get("/perform")
    def perform(self, request):
        result = self.service.perform_action()
        return {"result": result}
