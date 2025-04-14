from django.http import HttpResponse


def test_celery(request):
    return HttpResponse('发送成功')

