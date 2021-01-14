import json
from telegramdb.db import *
from telegramdb.tables import *
from telegramdb.decoder import TypeDecoder, TypeDecoderError

DEBUG_RECORD_ID = None
TypeDecoder.debug = True

accounts = get_macos_accounts()
conn = get_macos_db_conn(accounts[0])

# Table = MessageHistoryTable
# Table = PeerTable
Table = MetadataTable
# Table = ChatListTable
# Table = ChatListIndexTable

count = 0
# DEBUG_RECORD_ID = 12

_not_implemented_types = []
for k, v in Table.get_all_raw(conn):
    count += 1
    if isinstance(DEBUG_RECORD_ID, int) and count < DEBUG_RECORD_ID:
        continue
    if isinstance(DEBUG_RECORD_ID, int) and count > DEBUG_RECORD_ID:
        break

    try:
        record = Table(k, v).to_dict()
        print(record)
        # print(json.dumps(record, ensure_ascii=False, indent=2))
    except TypeDecoderError as e:
        _not_implemented_types.append(str(e).split(' ')[-1])
    except Exception as e:
        print('error on %d' % count)
        raise e

print('total_count: %d' % (count,))
for x in set(_not_implemented_types):
    print(x)
