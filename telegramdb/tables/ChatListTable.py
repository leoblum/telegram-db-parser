from .TableSpec import TableSpec


class ChatListTable(TableSpec):
    table_id = 9

    def _parse_key(self):
        read, skip, last = self._read, self._skip, self._last

        read(4, 'groupId')
        read(2, 'pinningIndex')
        read(4, 'messageIndexTimestamp')
        read(1, 'messageIndexNamespace')
        read(4, 'messageIndexId')
        read(8, 'peerId')
        read(1, 'type')

    def _parse_val(self):
        read, skip, last = self._read, self._skip, self._last

        read(4, 'idNamespace')
        read(4, 'idId', big_endian=True)
        read(4, 'idTimestamp', big_endian=True)
