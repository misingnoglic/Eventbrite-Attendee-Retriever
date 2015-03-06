__author__ = 'arya'
from secrets import event_id, oauth_key
from eventbrite import Eventbrite

from collections import Counter

eventbrite = Eventbrite(oauth_key)
def profile_count(item):
    last_page = False
    current_page = 1

    accumulator = []

    while not last_page:
        event = eventbrite.get('/events/'+event_id+'/attendees/',{'page':current_page})
        if current_page == event['pagination']['page_count']:
            last_page = True

        attendees = event['attendees']
        for person in attendees:
            try:
                accumulator.append(person['profile'][item])
            except KeyError:
                accumulator.append('NA')
        current_page+=1
    return Counter(accumulator)

def question_count(seeked_question):
    last_page = False
    current_page = 1

    accumulator = []

    while not last_page:
        event = eventbrite.get('/events/'+event_id+'/attendees/',{'page':current_page})
        if current_page == event['pagination']['page_count']:
            last_page = True

        attendees = event['attendees']
        for person in attendees:
            try:
                for question in person['answers']:
                    if seeked_question in question['question']:
                        accumulator.append(question['answer'])
            except KeyError:
                accumulator.append('No Answer')
        current_page+=1
    return Counter(accumulator)

print question_count("hardware-related hack")
