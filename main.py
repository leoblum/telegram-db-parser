from telegramdb.db import get_macos_accounts, get_macos_db_conn
from telegramdb.tables import *

DEBUG_RECORD_ID = None

accounts = get_macos_accounts()
conn = get_macos_db_conn(accounts[0])

# Table = MessageHistoryTable
Table = PeerTable
# Table = MetadataTable
# Table = ChatListTable
# Table = ChatListIndexTable

count = 0
# DEBUG_RECORD_ID = 1
for k, v in Table.get_all_raw(conn):
    count += 1
    if isinstance(DEBUG_RECORD_ID, int) and count < DEBUG_RECORD_ID:
        continue
    if isinstance(DEBUG_RECORD_ID, int) and count > DEBUG_RECORD_ID:
        break

    try:
        record = Table(k, v)
        print(record)
    except Exception as e:
        print('error on %d' % count)
        raise e

print('total_count: %d' % (count,))
