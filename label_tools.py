"""
    Get a list of Labels from the user's mailbox.
"""

from apiclient import errors


def get__label_id(service, user_id, label_name):
    """
        Get a list all labels in the user's mailbox.

        Args:
            service: Authorized Gmail API service instance.
            user_id: User's email address. The special value "me"
                     can be used to indicate the authenticated user.
            label_name: Label name of message

        Returns:
            A list all Labels in the user's mailbox.
    """

    try:
        response = service.users().labels().list(userId=user_id).execute()
        labels = response['labels']

        for label in labels:
            if label_name == label['name']:
                return label['id']

        else:
            print('Enter correct label name, please')

    except errors.HttpError as error:
        print('An error occurred: ', error)
