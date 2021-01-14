import os
import json
from natsort import natsorted
from collections import OrderedDict
from datetime import datetime
from telegramdb.db import *
from telegramdb.tables import *

accounts = get_macos_accounts()
conn = get_macos_db_conn(accounts[0])

def get_author_name(author_):
    if author_ is None:
        return ''
    name = [author_['val']['firstName'], author_['val']['lastName']]
    name = ' '.join([x for x in name if x is not None])
    if author_['val']['username'] is not None:
        name += ' (@%s)' % author_['val']['username']
    return name

def deduplicate_dict_key(dict_, key_):
    if key_ not in dict_:
        return key_

    key_ = key_.split(' ')
    try:
        num_ = int(key_[-1], 10)
        key_[-1] = str(num_ + 1)
    except Exception:
        key_.append(str(1))

    return deduplicate_dict_key(dict_, ' '.join(key_))


peers = {}
for k, v in PeerTable.get_all_raw(conn):
    record = PeerTable(k, v)
    record = record.to_dict()
    peers[k] = record

messages_by_peer = {}
for k, v in MessageHistoryTable.get_all_raw(conn):
    record = MessageHistoryTable(k, v)
    record = record.to_dict()

    peer_id = record['key']['peerId']
    try:
        if peers[peer_id]['val']['_type'] != 'TelegramUser':
            continue
    except TypeError as e:
        print(e, record)
        continue

    storage = messages_by_peer.setdefault(peer_id, [])
    storage.append([
        record['key']['timestamp'],
        get_author_name(peers.get(record['val'].get('varAuthorId'))),
        record['val']['text'],
    ])

result = {}
for k, v in messages_by_peer.items():
    messages = sorted(v, key=lambda x: x[0])
    for i, x in enumerate(messages):
        messages[i][0] = '%s | %s' % (str(datetime.fromtimestamp(x[0])), x[1])
        del messages[i][1]

    name = get_author_name(peers.get(k))
    name = deduplicate_dict_key(result, name)
    result[name] = messages


print('messages: %s' % len(result.keys()))
# sort by last message ts
result = natsorted(result.items(), key=lambda x: x[1][-1][0], reverse=True)
with open('data/messages.json', 'w') as fp:
    json.dump(OrderedDict(result), fp, ensure_ascii=False, indent=2)
