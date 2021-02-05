from time import time
from books.models import Log


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time()
        response = self.get_response(request)
        end = time()
        print_log = Log.objects.create(path=request.path, method=request.method, time=end-start)

        print(f"Path: {print_log.path}")
        print(f"Method: {print_log.method}")
        print(f"Requset-response took: {print_log.time}")

        return response
