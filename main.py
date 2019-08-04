from __future__ import print_function
from message_tools import get_message_body, list_messages_with_labels
from label_tools import get__label_id
from access import access


def main():
    """
        Print list of gmail message body
    """

    service = access()

    # User input
    user_id = 'me'
    label_name = input('Enter label name: ')

    # Call the Gmail API
    label_id = get__label_id(service, user_id, label_name)

    # Get all message body
    for msg in list_messages_with_labels(service, user_id, label_id):
        get_message_body(service, user_id, msg['id'])


if __name__ == '__main__':
    main()
