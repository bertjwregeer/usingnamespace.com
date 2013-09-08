from pyramid.events import BeforeRender
from pyramid.events import subscriber

from ..views.helpers import URLHelper

@subscriber(BeforeRender, is_management=False)
def view_helpers(event):
    if "h" in event:
        print "Someone else got here before us ..."
        return

    h = {}
    h['url'] = URLHelper(event['req'])

    event['h'] = h
