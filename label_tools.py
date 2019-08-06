from apiclient import errors


def get_label_id(labels, label_name):
    """
        Get a list all labels in the user's mailbox.

        Args:
            labels: List of dict with labels and metadata
            label_name: Label name of message

        Returns:
            A list all Labels in the user's mailbox.
    """

    try:
        for label in labels:
            if label_name == label['name']:
                return label['id']

        else:
            print('Not correct label name, please')

    except errors.HttpError as error:
        print('An error occurred: ', error)
