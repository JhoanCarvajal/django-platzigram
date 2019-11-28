from datetime import datetime
from django.http import HttpResponse
import json
def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hi! Current server time is {now}'
    .format(now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    
    ))

def sort_integers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    #import pdb; pdb.set_trace()
    data = {
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'integes sorted successfully.'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def say_hi(request, name, age):
    if age < 12:
        message = 'sorry {}, you arent allowed here'.format(mame)
    else:
        message = 'hello, {}! welcome to my house'.format(name)
    return HttpResponse(message)