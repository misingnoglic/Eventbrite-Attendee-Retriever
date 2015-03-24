__author__ = 'arya'
from secrets import event_id, oauth_key
from eventbrite import Eventbrite

from collections import Counter
ticket_types = {'mentor':'34401141', 'cadet':'33834335'}


eventbrite = Eventbrite(oauth_key)
def profile_count(item,ticket_class):
    ticket_type_id = ticket_types[ticket_class]
    last_page = False
    current_page = 1

    accumulator = []

    while not last_page:
        event = eventbrite.get('/events/'+event_id+'/attendees/',{'page':current_page})
        if current_page == event['pagination']['page_count']:
            last_page = True
        print event
        attendees = event['attendees']
        for person in attendees:
            if person['ticket_class_id']==ticket_type_id:
                try:
                    accumulator.append(person['profile'][item])
                except KeyError:
                    accumulator.append('No Answer')
        current_page+=1
    return accumulator

def question_count(seeked_question,ticket_class):
    last_page = False
    current_page = 1

    accumulator = []
    ticket_type_id = ticket_types[ticket_class]


    while not last_page:
        event = eventbrite.get('/events/'+event_id+'/attendees/',{'page':current_page})
        if current_page == event['pagination']['page_count']:
            last_page = True
        attendees = event['attendees']
        for person in attendees:
            organizer = False
            if person['ticket_class_id']==ticket_type_id:
                #try:
                for question in person['answers']:
                    if 'school' in question['question']:
                        try:
                            if 'organizer' in question['answer']:
                               organizer = True
                        except KeyError:
                            pass
                for question in person['answers']:
                    if seeked_question in question['question'] and not organizer:
                        try:
                            accumulator.append(question['answer'].lower())
                        except KeyError:
                            print person
                            accumulator.append('No Answer')
        current_page+=1
    return accumulator

print Counter(question_count("dietary",'cadet'))
