from pyramid.view import view_config
from pyramid.response import Response
import json


from gmeetapiapp.gmeetapiapp.views.cal_setup import get_calendar_service


@view_config(route_name='auth')
def authen(request):
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
        return Response(json.dumps(calendars))

