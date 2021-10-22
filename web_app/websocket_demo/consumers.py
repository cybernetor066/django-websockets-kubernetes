from django.http import HttpResponse
from channels.handler import AsgiHandler
# from channels.consumer import SyncConsumer
# from channels.consumer import AsyncConsumer

import os, sys, time, datetime, json, requests, logging, trace, threading
from base64 import b64encode
from sys import platform

# Accessing files in directories
if getattr(sys, 'frozen', False):
    # running in a bundled form
    base_dir = sys._MEIPASS # pylint: disable=no-member
else:
    # running normally
    base_dir = os.path.dirname(os.path.abspath(__file__))


# def ws_message(message):
#     # Make standard HTTP response - access ASGI path attribute directly
#     response = HttpResponse("Hello world! You asked for %s" % message.content['path'])
#     # Encode that response into message format (ASGI)
#     for chunk in AsgiHandler.encode_response(response):
#         message.reply_channel.send(chunk)




# # In consumers.py
# def ws_message(message):
#     # ASGI WebSocket packet-received and send-packet message types
#     # both have a "text" key for their textual data.
#     message.reply_channel.send({
#         "text": message.content['text'],
#     })


# # Not working, so probably we will just have to write different consumers for different tasks
# # In consumers.py
# def ws_message(message):
#     # ASGI WebSocket packet-received and send-packet message types
#     # both have a "text" key for their textual data.
#     if message == "echo":
#         message.reply_channel.send({
#            'text': json.dumps({
#             'codename': 'Alpha',
#             })
#         })



# # In consumers.py
# def ws_message(message):
#     # ASGI WebSocket packet-received and send-packet message types
#     # both have a "text" key for their textual data.
#     message.reply_channel.send({
#         'text': json.dumps({
#         'codename': 'Alpha',
#         })
#     })





# myBooks = [
#     {
#         "Book ID": "1",
#         "Book Name": "Computer Architecture",
#         "Category": "Computers",
#         "Price": "125.60"
#     },
#     {
#         "Book ID": "2",
#         "Book Name": "Asp.Net 4 Blue Book",
#         "Category": "Programming",
#         "Price": "56.00"
#     },
#     {
#         "Book ID": "3",
#         "Book Name": "Popular Science", 
#         "Category": "Science",
#         "Price": "210.40"
#     }
# ]




# # In consumers.py
# def ws_message(message):
#     # ASGI WebSocket packet-received and send-packet message types
#     # both have a "text" key for their textual data.
#     message.reply_channel.send({
#         'text': json.dumps({
#         'codename': {'Alpha': myBooks},
#         })
#     })






















# # In consumers.py
# def ws_message(message):
#     # ASGI WebSocket packet-received and send-packet message types
#     # both have a "text" key for their textual data.
#     message.reply_channel.send({
#         'text': json.dumps({
#         'codename': {'Alpha': 'data_json'},
#         })
#     })





# def firstFunc():
#     a = 1
#     b = 2
#     c = 3
#     print('I am here')
#     time.sleep(300)
#     return a, b, c


# firstFunc()

# # Using tuples
# result = firstFunc()[0]
# print(result)



# In consumers.py
def ws_message(message):
    # ASGI WebSocket packet-received and send-packet message types
    # both have a "text" key for their textual data.
    # print('Message received from client end is:', message.content['path'])
    print('Message received from client end is:', message.content['text'])
    message.reply_channel.send({
        'text': json.dumps({
        'codename': {
            'Alpha1': 'echo dragon sky, Hello from Alpha1',
            'Alpha6': 'false',
            },
        })
    })





# # In consumers.py
# def ws_message(message):
#     # ASGI WebSocket packet-received and send-packet message types
#     # both have a "text" key for their textual data.
#     time.sleep(6)
#     message.reply_channel.send({
#         'text': json.dumps({
#         'codename': {
#             'Alpha3': 'Hello Cybernetor',
#             'Alpha6': 'false',
#             },
#         })
#     })



# # In consumers.py
# def ws_message(message):
#     # ASGI WebSocket packet-received and send-packet message types
#     # both have a "text" key for their textual data.
#     # time.sleep(6)
#     message.reply_channel.send({
#         'text': json.dumps({
#         'codename': {
#             'Alpha': list(scrappers()),
#             'Alpha6': 'false',
#             # 'Alpha66': f'{datetime.datetime.now()}',
#             },
#         })
#     })
