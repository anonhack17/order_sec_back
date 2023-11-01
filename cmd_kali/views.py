from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .cmd.main import execute_command_in_kali

@csrf_exempt
def executeCommandView(request):
        command = request.GET['command']
        print('command============>')
        print(command)
        print('command============>')

        response_data = {"message": execute_command_in_kali(command)}
        print('response_data============>')
        print(response_data)
        print('response_data============>')

        return JsonResponse(response_data)

