import os
from PyQt6.QtGui import QIcon

SEND_ICON_NAME = 'send.png'
FORK_ICON_NAME = 'fork.png'
DELETE_ICON_NAME = 'delete.png'
NEW_CONVERSATION_ICON_NAME = 'new_conversation.png'
SELECTED_ITEM_ICON_NAME = 'selected_item.png'

def get_icon(name: str):
    script_path = os.path.dirname(__file__)
    icon_path = os.path.join(script_path, "../resources", name)
    return QIcon(icon_path)

