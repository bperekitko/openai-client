import os

from PyQt6.QtGui import QIcon

SEND_ICON_NAME = 'send.png'
FORK_ICON_NAME = 'fork.png'
DELETE_ICON_NAME = 'delete.png'
NEW_CONVERSATION_ICON_NAME = 'new_conversation.png'
SELECTED_ITEM_ICON_NAME = 'selected_item.png'

SPINNER_GIF_NAME = 'spinner.gif'

def get_icon(name: str):
    icon_path = get_resource_path(name)
    return QIcon(icon_path)

def get_resource_path(resource):
    return os.path.join(os.path.dirname(__file__), '../resources', resource)
