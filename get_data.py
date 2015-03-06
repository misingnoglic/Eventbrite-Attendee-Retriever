__author__ = 'arya'
from secrets import event_id, oauth_key
from eventbrite import Eventbrite
eventbrite = Eventbrite(oauth_key)
from collections import Counter

last_page = False
current_page = 1

genders = []

while not last_page:
    event = eventbrite.get('/events/'+event_id+'/attendees/',{'page':current_page})
    if current_page == event['pagination']['page_count']:
        last_page = True

    attendees = event['attendees']
    for person in attendees:
        try:
            genders.append(person['profile']['gender'])
        except KeyError:
            genders.append('NA')
    current_page+=1
print Counter(genders)
