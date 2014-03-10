# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView

class MobileApp(TemplateView):
    template_name = 'mobile_app.html'

def reply_to_sms_messages(request):
    # r = Response()
    # r.sms('Thanks for the SMS message!')
    # t = TextPhone()
    # t.run('what up!!!')
    # r = '<Response><Sms>Thanks for the SMS message!</Sms></Response>'
    l = list()
    for key, value in request.GET.iteritems():
        l.append((key),(value))
    
    r = HttpResponse('<Response><Sms>Your phone number is {}</Sms></Response>'.format(l), 'text/XML')
    return r