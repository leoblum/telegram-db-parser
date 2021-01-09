import json


class TableSpec:
    table_id = 0
    conn = None

    @classmethod
    def get_all_raw(cls, conn=None):
        return conn.execute('select * from t%d' % cls.table_id)

    def __init__(self, k_buffer, v_buffer):
        self._buffer = bytes()
        self._result = []
        self._offset = 0

        if isinstance(k_buffer, int):
            self.key = k_buffer
        else:
            self._reset(k_buffer)
            self._parse_key()
            assert len(self._buffer) == 0
            self.key = self._result

        self._reset(v_buffer)
        self._parse_val()
        assert len(self._buffer) == 0
        self.val = self._result

    def __str__(self):
        # todo: same keys will be deleted
        # print(dict([('a', 1), ('a', 2)]))
        key = dict(self.key) if isinstance(self.key, list) else self.key
        val = dict(self.val)
        res = dict(key=key, val=val)
        return json.dumps(res, ensure_ascii=False)

    def _reset(self, buffer=None):
        self._buffer = [] if buffer is None else buffer
        self._result = []
        self._offset = 0

    def _read(self, size, name, d_type=None, big_endian=False):
        d_type = int if d_type is None else d_type

        data = self._buffer[:size]
        self._buffer = self._buffer[size:]
        self._offset += size

        if d_type == int:
            data = data[::-1] if big_endian else data
            data = int(data.hex(), 16)
        if d_type == str:
            data = data.decode()
        if d_type == bytes:
            data = bytes(data)

        self._result.append((name, data))

    def _skip(self, size):
        self._buffer = self._buffer[size:]
        self._offset += size

    def _last(self):
        return self._result[-1][1]

    def _parse_key(self):
        pass

    def _parse_val(self):
        pass
