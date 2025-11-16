import time
from django.http import StreamingHttpResponse
from django.views.decorators.http import condition

def event_stream():
    # generator that yields SSE-formatted messages
    # in real use, replace with pub/sub listener (Redis) or shared queue
    while True:
        data = {"time": time.time()}
        yield f"data: {data}\n\n"
        time.sleep(2)

def ai_v1_view(request):
    response = StreamingHttpResponse(event_stream(), content_type='text/event-stream')
    # disable Django's default buffering (let server/proxy handle keepalive)
    response['Cache-Control'] = 'no-cache'
    return response