from .TableSpec import TableSpec
from ..postbox import decoder


class PeerTable(TableSpec):
    table_id = 2

    def _parse_val(self):
        read, skip, last = self._read, self._skip, self._last

        self._result = decoder(self._buffer, '_')
        self._buffer = bytes()
