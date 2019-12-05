from django.shortcuts import render
from datetime import datetime
posts = [
    {
        'title': 'mont blac',
        'user': {
            'name': 'jhoan carvajal',
            'picture': 'https://picsum.photos/60/60/?image=1027'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/1036/800/600',
    },
    {
        'title': 'via lactea',
        'user': {
            'name': 'jhoan carvajal',
            'picture': 'https://picsum.photos/60/60/?image=1005'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/903/800/800',
    },
    {
        'title': 'nuevo auditorio',
        'user': {
            'name': 'jhoan carvajal',
            'picture': 'https://picsum.photos/60/60/?image=883'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/id/1076/500/700',
    },
]



def list_posts(request):

    return render(request, 'feed.html', {'posts': posts})