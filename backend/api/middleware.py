from django.utils.deprecation import MiddlewareMixin


class AsyncMiddleware(MiddlewareMixin):
    async def __call__(self, request):
        response = await super().__call__(request)
        # Custom processing
        return response
