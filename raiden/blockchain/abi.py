# -*- coding: utf8 -*-
import os

from ethereum.abi import normalize_name

import raiden

__all__ = (
    'get_contract_path',

    'REGISTRY_ABI',
    'ASSETADDED_EVENT',
    'ASSETADDED_EVENTID',

    'CHANNEL_MANAGER_ABI',
    'CHANNELNEW_EVENT',
    'CHANNELNEW_EVENTID',

    'NETTING_CHANNEL_ABI',
    'CHANNELNEWBALANCE_EVENT',
    'CHANNELNEWBALANCE_EVENTID',
    'CHANNELCLOSED_EVENT',
    'CHANNELCLOSED_EVENTID',
    'CHANNELSECRETREVEALED_EVENT',
    'CHANNELSECRETREVEALED_EVENTID',
    'CHANNELSETTLED_EVENT',
    'CHANNELSETTLED_EVENTID',

    'HUMAN_TOKEN_ABI',
)


def get_contract_path(contract_name):
    project_directory = os.path.dirname(raiden.__file__)
    contract_path = os.path.join(project_directory, 'smart_contracts', contract_name)
    return os.path.realpath(contract_path)


def get_event(full_abi, event_name):
    for description in full_abi:
        name = description.get('name')

        # skip constructors
        if name is None:
            continue

        normalized_name = normalize_name(name)

        if normalized_name == event_name:
            return description


def get_eventname_types(event_description):
    if 'name' not in event_description:
        raise ValueError('Not an event description, missing the name.')

    name = normalize_name(event_description['name'])
    encode_types = [
        element['type']
        for element in event_description['inputs']
    ]
    return name, encode_types
