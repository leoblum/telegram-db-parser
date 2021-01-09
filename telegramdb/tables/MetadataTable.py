from .TableSpec import TableSpec


class MetadataTable(TableSpec):
    table_id = 0

    def _parse_val(self):
        read, skip, last = self._read, self._skip, self._last

        if self.key == 1:
            read(4, 'userVersion')
        if self.key == 2:
            # Coding.swift:684
            raise TypeError
        if self.key == 3:
            read(8, 'transactionStateVersion')
        if self.key == 4:
            read(8, 'masterClientId')
        if self.key == 5:
            raise TypeError
        if self.key == 6:
            read(4, 'remoteContactCount')
