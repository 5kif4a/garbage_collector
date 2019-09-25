from django.shortcuts import render, get_object_or_404
from trash_map.models import Dump, Event
from trash_map.forms import DumpForm, EventForm
from django.core.files.storage import FileSystemStorage
import json


# Create your views here.
def index(request):
    dumps_ = Dump.objects.all()
    events_ = Event.objects.all()
    dumps_json = []
    events_json = []
    for dump in dumps_:
        d = {
            'id': dump.id,
            'long': dump.long,
            'lat': dump.lat,
            'description': dump.description,
            'street': dump.street,
            'photo_url': dump.photo.url,
            'status': dump.status
             }
        dumps_json.append(d)
    for event in events_:
        e = {
            'id': event.id,
            'name': event.name,
            'long': event.long,
            'lat': event.lat,
            'description': event.description,
            'street': event.street,
            'org_phone': event.org_phone,
            'org_email': event.org_email,
            'rating':  event.rating,
             }
        events_json.append(e)
    dumps_json = json.dumps(dumps_json, indent=4, ensure_ascii=False)
    events_json = json.dumps(events_json, indent=4, ensure_ascii=False)
    dump_form = DumpForm()
    event_form = EventForm()
    context = {
        'dump_form': dump_form,
        'event_form': event_form,
        'dumps_json': dumps_json,
        'events_json': events_json
    }
    if request.method == 'POST':
        print(request.POST)
        is_event = True if request.POST.get('org_email', False) else False
        if is_event:
            form = EventForm(request.POST)
            if form.is_valid():
                form = EventForm(request.POST)
                form.save()
        else:
            form = DumpForm(request.POST, request.FILES)
            file = request.FILES['photo']
            fs = FileSystemStorage()
            if form.is_valid():
                fs.save(file.name, file)
                form.save()
        return render(request, 'new_team/index.html', context)
    else:
        return render(request, 'new_team/index.html', context)


def dumps(request):
    dumps = Dump.objects.all()
    context = {
        'dumps': dumps
    }
    return render(request, 'new_team/dumps.html', context)


def events(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'new_team/events.html', context)


def dump_by_id(request, id):
    dump = get_object_or_404(Dump, id=id)
    context = {
        'dump': dump,
    }
    return render(request, 'new_team/dump.html', context)


def event_by_id(request, id):
    event = get_object_or_404(Event, id=id)
    context = {
        'event': event,
    }
    return render(request, 'new_team/event.html', context)
