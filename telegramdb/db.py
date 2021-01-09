import os
from pysqlcipher3 import dbapi2 as sqlite3

MACOS_BASE = os.path.expanduser('~/Library/Group Containers/6N38VWS5BX.ru.keepcoder.Telegram')


def get_macos_accounts():
     return [x for x in os.listdir(MACOS_BASE) if x.startswith('account-')]


def get_macos_db_key():
    with open(os.path.join(MACOS_BASE, '.tempkey'), 'rb') as fp:
        return fp.read().hex()


def get_macos_db_conn(account, key=None):
    key = get_macos_db_key() if key is None else key
    db_path = os.path.join(MACOS_BASE, account, 'postbox/db/db_sqlite')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('PRAGMA cipher_plaintext_header_size=32;')
    cursor.execute('PRAGMA cipher_default_plaintext_header_size=32;')
    cursor.execute('PRAGMA key="x\'%s\'"' % key)
    return cursor


if __name__ == '__main__':
    print(get_macos_accounts())
    print(get_macos_db_key())
