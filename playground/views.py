from django.shortcuts import render
import logging
import requests
from rest_framework.views import APIView

logger = logging.getLogger(__name__) # playground,views


class HelloView(APIView):
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')

        return render(request,
                      'hello.html',
                      {'name': data})
