#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import channels
import json
import django.test


from otree import constants_internal
# import otree.common_internal
from otree.common_internal import get_admin_secret_code
from otree.db import models
from otree.models.session import Session

client = django.test.Client()

ADMIN_SECRET_CODE = get_admin_secret_code()


def advance_participant(participant):
    p = participant
    unvisited_participants = []
    if p._index_in_pages == 0:
        unvisited_participants.append(p)
        client.get(p._start_url(), follow=True)

    if unvisited_participants:
        return

    try:
        if p._current_form_page_url:
            resp = client.post(
                p._current_form_page_url,
                data={
                    constants_internal.timeout_happened: True,
                    constants_internal.admin_secret_code: ADMIN_SECRET_CODE
                },
                follow=True
            )
        else:
            resp = client.get(p._start_url(), follow=True)
    except:
        logging.exception("Failed to advance participant.")
        raise

    assert resp.status_code < 400
    channels.Group(
        'auto-advance-{}'.format(p.code)
    ).send(
        {'text': json.dumps(
            {'auto_advanced': True})}
    )


def ws_connect(message, session_code):
    print('somebody connected from session:::', session_code)


def ws_message(message, session_code):
    curparticipant_code = json.loads(message.content['text'])['participant_code']
    cursession = Session.objects.get(code=session_code)
    participant = cursession.participant_set.get(code=curparticipant_code)
    advance_participant(participant)


# Connected to websocket.disconnect
def ws_disconnect(message, session_code):
    print('somebody disconnected...')
