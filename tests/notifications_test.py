from datetime import datetime
from pathlib import Path

import pytest
from flask import render_template, url_for


@pytest.mark.parametrize(
    ('update', 'available', 'comment', 'snapshot_name'),
    (
        (False, False, False, 'new-unavailable-nocomment.txt'),
        (False, False, True, 'new-unavailable-comment.txt'),
        (False, True, False, 'new-available-nocomment.txt'),
        (False, True, True, 'new-available-comment.txt'),
        (True, False, False, 'update-unavailable-nocomment.txt'),
        (True, False, True, 'update-unavailable-comment.txt'),
        (True, True, False, 'update-available-nocomment.txt'),
        (True, True, True, 'update-available-comment.txt'),
    ),
)
def test_replied_email_plaintext(snapshot, update, available, comment, snapshot_name):
    answers = []
    if available:
        answers = [
            (datetime(2020, 9, 23, 10), False),
            (datetime(2020, 9, 23, 12), True),
            (datetime(2020, 9, 24, 11), False),
        ]

    text = render_template(
        'replied_email.txt',
        update=update,
        participant='Arthas Menethil',
        title='Unleashing the scourge',
        comment='You are not prepared' if comment else '',
        answers=answers,
        summary_link=url_for('newdle_summary', code='foo', _external=True),
    )

    snapshot.snapshot_dir = Path(__file__).parent / 'emails'
    snapshot.assert_match(text, snapshot_name)
