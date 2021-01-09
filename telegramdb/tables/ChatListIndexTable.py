from .TableSpec import TableSpec


class ChatListIndexTable(TableSpec):
    table_id = 8

    def _parse_val(self):
        read, skip, last = self._read, self._skip, self._last
        read(1, 'flagsValue')
        if last() == (1 << 0):
            read(4, 'idNamespace', big_endian=True)
            read(4, 'idId', big_endian=True)
            read(4, 'idTimestamp', big_endian=True)

        read(1, 'inclusionId')
        if last() == 1:
            read(2, 'pinningIndexValue', big_endian=True)
            read(1, 'hasMinTimestamp')
            if last() != 0:
                read(4, 'minTimestampValue', big_endian=True)
            read(4, 'groupIdValue')
