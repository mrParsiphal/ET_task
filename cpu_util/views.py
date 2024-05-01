from django.shortcuts import render
from .models import CPU_util_input
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def cpu_input(request):
    if request.method == 'POST':
        input = CPU_util_input(ip_address=request.get_host(), cpu_util=request.GET['cpu_util'])
        input.save()                      #в задаче не было указано подчищать БД. Рано или поздно место закончится.
        return HttpResponse(status=202)

def index(request):
    ip = request.get_host()
    l = list(range(100))
    content = {'ip': ip, 'length': l}
    return render(request, 'cpu_util/index.html', content)


@csrf_exempt
def index_js(request):
    if request.method == 'GET':
        ip = request.get_host()
        try:
            cpu = CPU_util_input.objects.all().order_by('-pk').values_list(
                'ip_address', 'cpu_util', 'date_time')[:100]
        except:
            return HttpResponse(status=500)
        cpu_len = len(cpu)
        cpu_util = {i: [*cpu[i]] for i in range(cpu_len)}
        return JsonResponse({'ip': ip, 'cpu_util': cpu_util, 'length': cpu_len})
