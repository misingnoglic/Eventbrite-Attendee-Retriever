Hello!
This script is fairly simple to use (I think)
First make sure you have all the requirements (basically the eventbrite python sdk), they're in the requirements.txt file
Then in the secrets.py make sure to have these variables set
event_id = 'whatever
oauth_key = 'whatever'

Where 'whatever' are the values that eventbrite gives you for your event.

Then set the ticket types at the top (e.g. where mine are ticket_types = {'mentor':'34401141', 'cadet':'33834335'} )
I don't know a concise way of getting them besides looking at all the registrations given to you by the eventbrite API

Then at the bottom you can either get a question from the profile (in which you would call profile_count), or a question from the custom questions that you created (where you would call question_count)

Feel free to fork this, it's pretty lazily coded but it's saved me a lot of "How many vegetarians are at our event again?"