import pytest

from label_tools import get_label_id


class TestUnit:
    def test_get_label_id_correct(self):
        labels = [{'id': 'CATEGORY_PERSONAL', 'name': 'CATEGORY_PERSONAL', 'type': 'system'}, {'id': 'CATEGORY_SOCIAL', 'name': 'CATEGORY_SOCIAL', 'type': 'system'}, {'id': 'Label_1', 'name': '[Imap]/Trash', 'type': 'user'}, {'id': 'CATEGORY_FORUMS', 'name': 'CATEGORY_FORUMS', 'type': 'system'}, {'id': 'Label_2', 'name': '[Imap]/Sent', 'type': 'user'}, {'id': 'IMPORTANT', 'name': 'IMPORTANT', 'messageListVisibility': 'hide', 'labelListVisibility': 'labelShow', 'type': 'system'}, {'id': 'CATEGORY_UPDATES', 'name': 'CATEGORY_UPDATES', 'type': 'system'}, {'id': 'CHAT', 'name': 'CHAT', 'messageListVisibility': 'hide', 'labelListVisibility': 'labelHide', 'type': 'system'}, {'id': 'SENT', 'name': 'SENT', 'messageListVisibility': 'hide', 'labelListVisibility': 'labelShow', 'type': 'system'}, {'id': 'INBOX', 'name': 'INBOX', 'messageListVisibility': 'hide', 'labelListVisibility': 'labelShow', 'type': 'system'}, {'id': 'TRASH', 'name': 'TRASH', 'messageListVisibility': 'hide', 'labelListVisibility': 'labelHide', 'type': 'system'}, {'id': 'CATEGORY_PROMOTIONS', 'name': 'CATEGORY_PROMOTIONS', 'type': 'system'}, {'id': 'DRAFT', 'name': 'DRAFT', 'messageListVisibility': 'hide', 'labelListVisibility': 'labelShow', 'type': 'system'}, {'id': 'SPAM', 'name': 'SPAM', 'messageListVisibility': 'hide', 'labelListVisibility': 'labelHide', 'type': 'system'}, {'id': 'STARRED', 'name': 'STARRED', 'messageListVisibility': 'hide', 'labelListVisibility': 'labelShow', 'type': 'system'}, {'id': 'UNREAD', 'name': 'UNREAD', 'type': 'system'}]

        for label in labels:
            assert(label['id'] == get_label_id(labels, label['name']))
