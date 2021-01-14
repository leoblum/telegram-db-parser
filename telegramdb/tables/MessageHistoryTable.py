from .TableSpec import TableSpec
from ..decoder import decoder


class MessageHistoryTable(TableSpec):
    # MessageHistoryTable.swift:2114 readIntermediateEntry
    table_id = 7

    def _parse_key(self):
        read, skip, last = self._read, self._skip, self._last

        read(8, 'peerId')
        read(4, 'namespace')
        read(4, 'timestamp')
        read(4, 'id')

    def _parse_val(self):
        read, skip, last = self._read, self._skip, self._last

        read(1, 'type')
        read(4, 'stableId')
        read(4, 'stableVersion')

        read(1, 'dataFlagsValue')
        data_flags_value = last()
        read(8, 'globallyUniqueId') if data_flags_value & (1 << 0) else None
        read(4, 'globalTags') if data_flags_value & (1 << 1) else None
        read(8, 'groupingKey') if data_flags_value & (1 << 2) else None
        read(4, 'groupInfo') if data_flags_value & (1 << 3) else None
        read(4, 'localTags') if data_flags_value & (1 << 4) else None
        read(8, 'threadId') if data_flags_value & (1 << 5) else None

        read(4, 'flagsValue')
        read(4, 'tagsValue')

        read(1, 'forwardInfoFlags')
        forward_info_flags = last()
        if forward_info_flags != 0:
            read(8, 'forwardAuthorId')
            read(4, 'forwardDate')
            if forward_info_flags & (1 << 1) != 0:
                read(8, 'forwardSourceIdValue')
            if forward_info_flags & (1 << 2) != 0:
                read(8, 'forwardSourceMessagePeerId')
                read(4, 'forwardSourceMessageNamespace')
                read(4, 'forwardSourceMessageIdId')
            if forward_info_flags & (1 << 3) != 0:
                read(4, 'signatureLength', big_endian=True)
                read(last(), 'authorSignature', str)
            if forward_info_flags & (1 << 4) != 0:
                read(4, 'psaTypeLength', big_endian=True)
                read(4, 'psaTypeLength_', str)

        read(1, 'hasAuthor')
        read(8, 'varAuthorId', big_endian=True) if last() == 1 else None
        read(4, 'textLength', big_endian=True)
        read(last(), 'text', str)

        read(4, 'attributeCount', big_endian=True)
        for i in range(last()):
            read(4, 'attributeLength', big_endian=True)
            data = decoder(self._buffer[:last()], '_')
            skip(last())
            self._result.append(('attributeValue', data))

        read(4, 'embeddedMediaCount', big_endian=True)
        for i in range(last()):
            read(4, 'mediaLength', big_endian=True)
            data = decoder(self._buffer[:last()], '_')
            skip(last())
            self._result.append(('mediaValue', data))

        read(4, 'referencedMediaIdsCount', big_endian=True)
        for i in range(last()):
            read(4, 'referencedMediaIds.idNamespace')
            read(8, 'referencedMediaIds.idId')
