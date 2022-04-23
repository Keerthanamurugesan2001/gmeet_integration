from datetime import datetime, timedelta

from pyramid.view import view_config
from pyramid.response import Response
import json

d = datetime.now().isoformat()

from .cal_setup import get_calendar_service


@view_config(route_name='listevents', renderer='gmeetapiapp:templates/list.jinja2')
def listevents(request):
    service = get_calendar_service()
    # Call the Calendar API
    print('Getting list of calendars')
    calendars_result = service.calendarList().list().execute()

    calendars = calendars_result.get('items', [])

    # if not calendars:
    #     return Response('No calendars found.')
    # for calendar in calendars:
    #     summary = calendar['summary']
    #     id = calendar['id']
    #     primary = "Primary" if calendar.get('primary') else ""
    #     print("%s\t%s\t%s" % (summary, id, primary))
    return {'calendars': calendars}


@view_config(route_name='createevents', renderer='gmeetapiapp:templates/event.jinja2')
def createevents(request):
    # creates one hour event tomorrow 10 AM IST
    service = get_calendar_service()

    d = datetime.now().date()
    tomorrow = datetime(d.year, d.month, d.day, 10) + timedelta(days=1)
    start = tomorrow.isoformat()
    end = (tomorrow + timedelta(hours=1)).isoformat()

    event_result = service.events().insert(calendarId='primary',
                                           body={
                                               "summary": 'Automating calendar',
                                               "description": 'This is a tutorial example of automating google calendar with python',
                                               "start": {"dateTime": start, "timeZone": 'Asia/Kolkata'},
                                               "end": {"dateTime": end, "timeZone": 'Asia/Kolkata'},
                                           }
                                           ).execute()

    # print("created event")
    # print("id: ", event_result['id'])
    # print("summary: ", event_result['summary'])
    # print("starts at: ", event_result['start']['dateTime'])
    # print("ends at: ", event_result['end']['dateTime'])
    return {'event': event_result}


@view_config(route_name='createmeeting', renderer='gmeetapiapp:templates/event.jinja2')
def createmeeting(request):
    service = get_calendar_service()
    today = datetime.now().date()
    start = datetime(today.year, today.month, today.day) + timedelta(hours=21)
    start = start.isoformat()
    today = datetime.now().date()
    end = datetime(today.year, today.month, today.day) + timedelta(hours=22)
    end = end.isoformat()
    event = {
        'summary': "Meeting is gonna start",
        'location': "Chennai",
        'description': "Tried to create meeting by api",
        'start': {
            'dateTime': start,
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end,
            'timeZone': 'Asia/Kolkata',
        },
        'recurrence': [],
        'attendees': [
            {'email': 'keerthana.murugesan@softsuave.com'},
            {'email': 'keerthanamurugesan094.ss@gmail.com'},

        ],
        'reminders': {
            'useDefault': 'true',
        },
        'conferenceData': {
            'createRequest': {
                'conferenceSolutionKey': {
                    'type': 'hangoutsMeet',
                },
                'requestId': 'keerthanamurugesan0',
            },

        },

    };

    event_result = service.events().insert(calendarId='primary',
                                           body=event,
                                           conferenceDataVersion=1,
                                           ).execute()

    return {'event': event_result}
