from django.http import HttpResponse
from showdb.models import conlog
from django.utils import timezone
def hello(request):
	p=conlog(who='someone',when=timezone.now())
	p.save()
	html="<html><body><p>Hello World!</p>"
	for entry in conlog.objects.all():
		html=html+'<p>'+entry.who+' connected at ' + str(entry.when)+'</p>'
	html=html+"</body></html>"		
	return HttpResponse(html)

