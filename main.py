from __future__ import print_function
from message_tools import get_message_body, list_messages_with_labels
from label_tools import get_label_id
from access import access


def main():
    """
        Print list of gmail message body
    """

    service = access()

    # User input
    user_id = 'me'
    label_name = input('Enter label name: ')
    response = service.users().labels().list(userId=user_id).execute()
    labels = response['labels']

    # Call the Gmail API
    label_id = get_label_id(labels, label_name)

    f = open("out.txt", 'w')

    # Get all message body
    for msg in list_messages_with_labels(service, user_id, label_id):
        get_message_body(service, user_id, msg['id'], f)

    f.close()


if __name__ == '__main__':
    main()
