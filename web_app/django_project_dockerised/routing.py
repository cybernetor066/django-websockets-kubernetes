# In routing.py
import channels
from channels.routing import route
from websocket_demo.consumers import ws_message
# from realTimeStockFeedsApp.consumers import MyConsumer


channel_routing = [
    route("websocket.receive", ws_message),
]

# channel_routing = [
#     route("websocket.receive", MyConsumer),
# ]