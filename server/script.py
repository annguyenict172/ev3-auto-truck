import httplib2
import json

h = httplib2.Http() 

send_finish_request = h.request(
    uri='http://localhost:5000/robots',
    method='PUT',
    headers={
        'Content-Type': 'application/json',
    },
    body=json.dumps({
        'status': 'Finish'
    })
)