from time import time
from books.models import Log


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()
        response = self.get_response(request)
        end = time()

        Log.objects.create(path=request.path, method=request.method, time=end-start)

        return response
