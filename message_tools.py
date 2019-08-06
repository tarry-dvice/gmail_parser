from apiclient import errors

import base64
import email


def get_message_body_text(data, f):
    mime_type = data['mimeType']

    if mime_type == 'text/plain' or mime_type == 'text/html':
        if data['body']['size'] == 0:
            if data['parts'][0]['body']['size'] != 0:
                if data['parts'][0]['mimeType'] == 'text/plain' or data['parts'][0]['mimeType'] == 'text/html':
                    data = data['parts'][0]

        try:
            msg = base64.urlsafe_b64decode(data['body']['data'].encode('ASCII'))
            mime_msg = email.message_from_string(msg.decode('utf-8'))

            f.write(str(mime_msg))

        except KeyError:
            # For non-text messages
            pass

    elif mime_type == 'multipart/alternative' or mime_type == 'multipart/mixed':
        get_message_body_text(data['parts'][0], f)


def get_message_body(service, user_id, msg_id, f):
    """
        Search a Message body with given ID and call function for print data.

        Args:
            service: Authorized Gmail API service instance.
            user_id: User's email address. The special value "me"
                     can be used to indicate the authenticated user.
            msg_id: The ID of the Message required.
    """

    try:
        message = service.users().messages().get(userId=user_id, id=msg_id).execute()

        data = message['payload']

        get_message_body_text(data, f)

    except errors.HttpError as error:
        print('An error occurred: ', error)


def list_messages_with_labels(service, user_id, label_id):
    """
        List all Messages of the user's mailbox with label_ids applied.

        Args:
            service: Authorized Gmail API service instance.
            user_id: User's email address. The special value "me"
            can be used to indicate the authenticated user.
            label_id: Only return Messages with this labelIds applied.

        Returns:
            List of Messages that have all required Labels applied. Note that the
            returned list contains Message IDs, you must use get with the
            appropriate id to get the details of a Message.
    """

    try:
        response = service.users().messages().list(userId=user_id, labelIds=label_id).execute()
        messages = []

        if 'messages' in response:
            messages.extend(response['messages'])

        while 'nextPageToken' in response:
            page_token = response['nextPageToken']
            response = service.users().messages().list(userId=user_id,
                                                       labelIds=label_id,
                                                       pageToken=page_token).execute()
            messages.extend(response['messages'])

        return messages

    except errors.HttpError as error:
        print('An error occurred: ', error)
