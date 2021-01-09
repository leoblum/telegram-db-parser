class ValueType:
    Int32 = 0
    Int64 = 1
    Bool = 2
    Double = 3
    String = 4
    Object = 5
    Int32Array = 6
    Int64Array = 7
    ObjectArray = 8
    ObjectDictionary = 9
    Bytes = 10
    Nil = 11
    StringArray = 12
    BytesArray = 13


_type_decoders = {}


def add_type_decoder(t_hash, fn):
    _type_decoders[t_hash] = fn


def get_int(buffer, offset, size):
    return int(buffer[offset:offset + size][::-1].hex(), 16)


def get_str(buffer, offset, size):
    return buffer[offset:offset + size].decode()


def decoder_skip(buffer: bytes, offset: int, d_type: int):
    # PostboxCoding.swift:419 skipValue()
    i = offset
    if d_type == ValueType.Int32:
        return i + 4
    if d_type == ValueType.Int64:
        return i + 8
    if d_type == ValueType.Bool:
        return i + 1
    if d_type == ValueType.Double:
        return i + 8
    if d_type == ValueType.String:
        d_size = get_int(buffer, i, 4)
        return i + 4 + d_size
    if d_type == ValueType.Object:
        d_size = get_int(buffer, i, 4)
        return i + 8 + d_size
    if d_type == ValueType.Int32Array:
        pass
    if d_type == ValueType.Int64Array:
        pass
    if d_type == ValueType.ObjectArray:
        length = get_int(buffer, i, 4)
        i += 4
        for x in range(length):
            d_size = get_int(buffer, i + 4, 4)
            i += 4 + 4 + d_size
        return i
    if d_type == ValueType.ObjectDictionary:
        pass
    if d_type == ValueType.Bytes:
        pass
    if d_type == ValueType.Nil:
        return i
    if d_type in (ValueType.StringArray, ValueType.BytesArray):
        pass

    raise ValueError(d_type)


def decoder(buffer: bytes, key: str):
    key = key.encode()
    buffer_len = len(buffer)

    i = 0
    while i < buffer_len:
        k_size = int(buffer[i])
        k_name = buffer[i + 1:i + 1 + k_size]
        d_type = int(buffer[i + 1 + k_size])
        i += 1 + k_size + 1

        # print(key, k_size, k_name, d_type)
        if k_name != key:
            i = decoder_skip(buffer, i, d_type)
            continue
        if d_type == ValueType.Int32:
            return get_int(buffer, i, 4)
        if d_type == ValueType.Int64:
            return get_int(buffer, i, 8)
        if d_type == ValueType.String:
            d_size = get_int(buffer, i, 4)
            return get_str(buffer, i + 4, d_size)
        if d_type == ValueType.Object:
            t_hash = get_int(buffer, i, 4)
            d_size = get_int(buffer, i + 4, 4)
            i += 4 + 4
            if t_hash not in _type_decoders:
                print('TypeHash %s has no decoder.' % t_hash, key)
                return None
            return _type_decoders[t_hash](buffer[i:i + d_size])
        if d_type == ValueType.ObjectArray:
            length = get_int(buffer, i, 4)
            i += 4
            for x in range(length):
                t_hash = get_int(buffer, i, 4)
                d_size = get_int(buffer, i + 4, 4)
                i += 4 + 4
                # todo: need to call decoder for t_hash
                i += d_size
            return []


def type_decoder_2657658155(buffer):
    # TelegramUser
    mapping = {
        'peerId': 'i',
        'accessHash': 'ah',
        'accessHashType': 'aht',
        'firstName': 'fn',
        'lastName': 'ln',
        'username': 'un',
        'phone': 'p',
        'photo': 'ph'
    }
    return {k: decoder(buffer, v) for k, v in mapping.items()}


def type_decoder_1721859409(buffer):
    # TelegramGroup
    mapping = {
        'peerId': 'i',
        'title': 't',
        'photo': 'ph',
        'participantCount': 'pc',
        'role': 'rv',
        'roleValue': 'r',
        'membership': 'm',
        'flags': 'f',
        'migrationPeerId': 'mr.i',
        'migrationAccessHash': 'mr.a',
        'creationDate': 'd',
        'version': 'v',
    }
    return {k: decoder(buffer, v) for k, v in mapping.items()}


def type_decoder_1667961306(buffer):
    # TelegramChannel
    mapping = {
        'peerId': 'i',
        'accessHash': 'ah',
        'accessHashType': 'aht',
        'title': 't',
        'username': 'un',
        'photo': 'ph',
        'creationDate': 'd',
        'version': 'v',
        'participationStatus': 'ps',
        # 'info': 'ps',  # todo
        'flags': 'ƒl',
        # 'restrictionInfo': 'ri',  # todo
        # 'adminRights': 'ar',  # todo
        # 'bannedRights': 'br',  # todo
        # 'defaultBannedRights': 'dbr',  # todo
    }
    return {k: decoder(buffer, v) for k, v in mapping.items()}


def type_decoder_2584608734(buffer):
    # TelegramGroupRole
    # https://github.com/TelegramMessenger/Telegram-iOS/blob/7fb0b48ded4b83297453444c9aba89139c4a726a/submodules/SyncCore/Sources/TelegramGroup.swift#L8
    # todo
    return {
        '_v': decoder(buffer, '_v'),
    }


for k in [x for x in list(locals().keys()) if x.startswith('type_decoder_')]:
    add_type_decoder(int(k.split('type_decoder_')[1]), locals()[k])
