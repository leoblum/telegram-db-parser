class TypeDecoderError(Exception):
    pass


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


class TypesMapping:
    # See _generate_hash_mapping.py
    AccountBackupData = 2603348544
    AccountBackupDataAttribute = 3489360759
    AccountEnvironmentAttribute = 796680841
    AccountSortOrderAttribute = 78375557
    ActiveCall = 2014638251
    AppChangelogState = 4041908766
    AppConfiguration = 2011889088
    ArchivedStickerPacksInfo = 2153941692
    ArchivedStickerPacksInfoId = 3048679639
    AuthorSignatureMessageAttribute = 1616326675
    AuthorizedAccountState = 1601241862
    AutodownloadPresetSettings = 154255577
    AutodownloadSettings = 167916131
    AutoremoveTimeoutMessageAttribute = 2149502027
    BotCommand = 2805217313
    BotInfo = 3997916609
    BotUserInfo = 1454014293
    BotUserInfoFlags = 1018137400
    CacheStorageSettings = 2601488342
    CachedChannelData = 381818197
    CachedChannelFlags = 1380448872
    CachedChannelParticipantsSummary = 2125496454
    CachedGroupData = 2838358049
    CachedGroupFlags = 463222230
    CachedGroupParticipants = 2033956191
    CachedItemCollection = 1951667398
    CachedLocalizationInfos = 2210324235
    CachedPeerBotInfo = 1546348633
    CachedRecentPeers = 3167136104
    CachedResolvedByNamePeer = 3472353222
    CachedSecretChatData = 1315950667
    CachedSecureIdConfiguration = 2592383032
    CachedStickerPack = 1384809303
    CachedStickerQueryResult = 3860219635
    CachedThemesConfiguration = 2531852049
    CachedUserData = 1981783441
    CachedWallpapersConfiguration = 1342233915
    ChannelMessageStateVersionAttribute = 987966334
    ChannelMigrationReference = 1838382711
    ChannelState = 2004128665
    CloudChatClearHistoryOperation = 3472750055
    CloudChatRemoveChatOperation = 3883533992
    CloudChatRemoveMessagesOperation = 2298174218
    CloudDocumentMediaResource = 486562374
    CloudDocumentMediaResourceId = 2833703474
    CloudDocumentSizeMediaResource = 2165717516
    CloudDocumentSizeMediaResourceId = 26313096
    CloudFileMediaResource = 3755719516
    CloudFileMediaResourceId = 2523172382
    CloudPeerPhotoSizeMediaResource = 923090569
    CloudPeerPhotoSizeMediaResourceId = 2546468442
    CloudPhotoSizeMediaResource = 1226791958
    CloudPhotoSizeMediaResourceId = 2301120304
    CloudStickerPackThumbnailMediaResource = 3844767077
    CloudStickerPackThumbnailMediaResourceId = 2099345596
    ConsumableContentMessageAttribute = 3697912752
    ConsumablePersonalMentionMessageAttribute = 3987196230
    ConsumePersonalMessageAction = 1576536431
    ContactsSettings = 2022849046
    ContentPrivacySettings = 1333008690
    ContentRequiresValidationMessageAttribute = 2795382466
    EditedMessageAttribute = 2454659353
    EmbeddedMediaStickersMessageAttribute = 2289904539
    EmojiKeywordCollectionInfo = 665094754
    EmojiKeywordItem = 3213893980
    EmojiSearchQueryMessageAttribute = 2516999099
    EmptyMediaResource = 2924760212
    EmptyMediaResourceId = 4188402381
    ExportedInvitation = 1793100903
    FeaturedStickerPackItem = 3919807286
    FeaturedStickerPackItemId = 3453052078
    Flags = 1880682112
    ForwardCountMessageAttribute = 2348423079
    ForwardSourceInfoAttribute = 2134678541
    GlobalNotificationSettings = 3062885535
    GlobalNotificationSettingsSet = 2721588836
    HttpReferenceMediaResource = 2608980082
    HttpReferenceMediaResourceId = 535153526
    ImportableDeviceContactData = 528033417
    InlineBotMessageAttribute = 938328096
    InstantPage = 2178607703
    InstantPageCaption = 1746376877
    InstantPageRelatedArticle = 2071896585
    InstantPageTableCell = 1030551558
    InstantPageTableRow = 2486256404
    ItemCollection = 1552183937
    LegacyPeerSummaryCounterTags = 2856933512
    LimitsConfiguration = 4073941137
    LocalFileMediaResource = 711798229
    LocalFileMediaResourceId = 2588345790
    LocalFileReferenceMediaResource = 1868491758
    LocalFileReferenceMediaResourceId = 1617586109
    Localization = 2416414107
    LocalizationComponent = 4029559992
    LocalizationEntryFlags = 3301840456
    LocalizationInfo = 344619798
    LocalizationListState = 2097045112
    LocalizationSettings = 11787741
    LoggedOutAccountAttribute = 1009792572
    LoggingSettings = 781482463
    MapVenue = 597738840
    Media = 334513851
    MediaDictionary = 679280226
    Message = 3674891629
    MessageNotificationSettings = 4099462802
    MessageReaction = 3327428476
    MessageReference = 3831820255
    MessageTextEntity = 2102529310
    NamedGeoPlace = 270689451
    Namespaces = 4164021473
    NetworkSettings = 110448300
    NotificationInfoMessageAttribute = 964991203
    NotificationInfoMessageAttributeFlags = 4219704210
    OperationLogTags = 1724253988
    OrderedItemList = 3444984500
    OutgoingChatContextResultMessageAttribute = 363782357
    OutgoingContentInfoFlags = 3186255192
    OutgoingContentInfoMessageAttribute = 3208800792
    OutgoingMessageInfoAttribute = 3236661724
    OutgoingMessageInfoFlags = 1876867940
    OutgoingScheduleInfoMessageAttribute = 1116861967
    Peer = 1671124377
    PeerAccessRestrictionInfo = 31971757
    PeerGeoLocation = 3644606585
    PeerGroup = 2542154657
    PeerGroupMessageStateVersionAttribute = 2177598922
    PeerStatusSettings = 3061841520
    PendingReactionsMessageAttribute = 926432208
    PixelDimensions = 377814750
    PreferencesKeys = 2501748062
    PreviousPeerItemId = 4124154142
    ProxyServerSettings = 2121438949
    ProxySettings = 1983529493
    ReactionsMessageAttribute = 210987334
    RecentHashtagItem = 3089824311
    RecentMediaItem = 3055171221
    RecentMediaItemId = 3207126905
    RecentPeerItem = 2255117259
    RecentPeerItemId = 634897864
    RegularChatState = 820639795
    RemoteStorageConfiguration = 2751856824
    ReplyMarkupButton = 1614954246
    ReplyMarkupMessageAttribute = 3862080957
    ReplyMarkupMessageFlags = 1121705828
    ReplyMarkupRow = 404369907
    ReplyMessageAttribute = 478003709
    ReplyThreadMessageAttribute = 1816506932
    RestrictedContentMessageAttribute = 3136073322
    RestrictionRule = 983930648
    SavedStickerItem = 731080572
    SearchBotsConfiguration = 312453444
    SecretChatEncryptionConfig = 2410972032
    SecretChatFileReference = 4080904201
    SecretChatIncomingDecryptedOperation = 3171968682
    SecretChatIncomingEncryptedOperation = 2207543022
    SecretChatKey = 3094502953
    SecretChatKeyFingerprint = 4219154593
    SecretChatKeySha1Fingerprint = 3265165676
    SecretChatKeySha256Fingerprint = 1681658674
    SecretChatKeychain = 2508182652
    SecretChatLayerNegotiationState = 1697318997
    SecretChatOperationSequenceInfo = 3748508802
    SecretChatOutgoingFile = 202172557
    SecretChatOutgoingOperation = 852549282
    SecretChatRekeySessionState = 3846748341
    SecretChatSequenceBasedLayerState = 3781945300
    SecretChatSettings = 227420065
    SecretChatState = 498427512
    SecretFileEncryptionKey = 2925785305
    SecretFileMediaResource = 2062784145
    SecretFileMediaResourceId = 3348817415
    SecureFileMediaResource = 3123195421
    SecureFileMediaResourceId = 2768854810
    SecureIdConfiguration = 2277630845
    SecureIdFileReference = 1901871281
    SendScheduledMessageImmediatelyAction = 801655178
    SharedDataKeys = 1059739078
    Solution = 1137239075
    SourceReferenceMessageAttribute = 1566678339
    State = 3634606460
    StickerMaskCoords = 370748693
    StickerPackCollectionInfo = 2112923154
    StickerPackCollectionInfoFlags = 3996881120
    StickerPackItem = 1345525277
    SuggestedLocalizationEntry = 3398677088
    SynchronizeAppLogEventsOperation = 110105017
    SynchronizeChatInputStateOperation = 3840916142
    SynchronizeConsumeMessageContentsOperation = 2064539370
    SynchronizeEmojiKeywordsOperation = 2310895830
    SynchronizeGroupedPeersOperation = 2705138787
    SynchronizeInstalledStickerPacksOperation = 3362855600
    SynchronizeLocalizationUpdatesOperation = 2688494423
    SynchronizeMarkAllUnseenPersonalMessagesOperation = 3456871522
    SynchronizeMarkFeaturedStickerPacksAsSeenOperation = 2167584831
    SynchronizePinnedChatsOperation = 527224992
    SynchronizeRecentlyUsedMediaOperation = 3234172465
    SynchronizeSavedGifsOperation = 2338046462
    SynchronizeSavedStickersOperation = 2756542404
    SynchronizeableChatInputState = 3621296141
    TelegraMediaWebpageThemeAttribute = 2711370314
    TelegramChannel = 1667961306
    TelegramChannelBroadcastFlags = 3671228991
    TelegramChannelBroadcastInfo = 2049467571
    TelegramChannelFlags = 4187129966
    TelegramChannelGroupFlags = 3462659119
    TelegramChannelGroupInfo = 154747718
    TelegramChatAdminRights = 2325279738
    TelegramChatAdminRightsFlags = 2591850898
    TelegramChatBannedRights = 620104239
    TelegramChatBannedRightsFlags = 3294231130
    TelegramGroup = 1721859409
    TelegramGroupFlags = 1774029020
    TelegramGroupToChannelMigrationReference = 3279902969
    TelegramMediaAction = 3161982849
    TelegramMediaContact = 49483725
    TelegramMediaDice = 3400482591
    TelegramMediaExpiredContent = 62379663
    TelegramMediaFile = 665733176
    TelegramMediaGame = 2065888375
    TelegramMediaImage = 2343444628
    TelegramMediaImageFlags = 1485014109
    TelegramMediaImageRepresentation = 1774815102
    TelegramMediaInvoice = 74610450
    TelegramMediaInvoiceFlags = 1465864820
    TelegramMediaMap = 3156724623
    TelegramMediaPoll = 4129203158
    TelegramMediaPollOption = 1568747767
    TelegramMediaPollOptionVoters = 1071815536
    TelegramMediaPollResults = 938539408
    TelegramMediaUnsupported = 1232696171
    TelegramMediaVideoFlags = 3168273798
    TelegramMediaWebFile = 1692255778
    TelegramMediaWebpage = 3633645140
    TelegramMediaWebpageLoadedContent = 372084582
    TelegramPeerNotificationSettings = 3885444966
    TelegramSecretChat = 566849114
    TelegramTheme = 9122308
    TelegramThemeSettings = 4118942268
    TelegramUser = 2657658155
    TelegramUserPresence = 1408098419
    TemporaryTwoStepPasswordToken = 150359403
    TextEntitiesMessageAttribute = 4041978083
    ThemeSettings = 1026636738
    UnauthorizedAccountState = 3110456593
    UnauthorizedAccountTermsOfService = 822990030
    UnorderedItemList = 1286378251
    UpdateMessageReactionsAction = 564911308
    UserInfoFlags = 69022226
    ValidationMessageAttribute = 3724710986
    VideoRepresentation = 3960919709
    VideoThumbnail = 3893327833
    ViewCountMessageAttribute = 3334891517
    VoipConfiguration = 3684403883
    WalletCollection = 4083498123
    WalletCollectionItem = 853449601
    WallpaperSettings = 726027516
    WasScheduledMessageAttribute = 1033489696
    WebFileReferenceMediaResource = 1849437543
    WebFileReferenceMediaResourceId = 1046217333
    WebpageReference = 114509915


class TypeDecoder:
    debug = False

    @classmethod
    def decode(cls, t_hash, buffer):
        t_name = get_type_name(t_hash)
        handler = getattr(cls, '_decode_%s' % t_name, None)
        if handler is None:
            msg = 'No decoder for %s' % get_type_name(t_hash, True)
            if cls.debug:
                raise TypeDecoderError(msg)
            else:
                # print(msg)
                return None

        data = handler(buffer)
        data.update({'_type': t_name})
        return data

    @classmethod
    def _decode_TelegramUser(cls, buffer):
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

    @classmethod
    def _decode_TelegramGroup(cls, buffer):
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

    @classmethod
    def _decode_TelegramChannel(cls, buffer):
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

    @classmethod
    def _decode_AuthorizedAccountState(cls, buffer):
        mapping = {
            'isTestingEnvironment': 'isTestingEnvironment',
            'masterDatacenterId': 'masterDatacenterId',
            'peerId': 'peerId',
            'state': 'state',
        }
        return {k: decoder(buffer, v) for k, v in mapping.items()}

    @classmethod
    def _decode_State(cls, buffer):
        mapping = {
            'pts': 'pts',
            'qts': 'qts',
            'date': 'date',
            'seq': 'seq',
        }
        return {k: decoder(buffer, v) for k, v in mapping.items()}

    @classmethod
    def _decode_TelegramSecretChat(cls, buffer):
        mapping = {
            'id': 'i',
            'regularPeerId': 'r',
            'accessHash': 'h',
            'creationDate': 'd',
            'role': 'o',
            'embeddedState': 's',
            'messageAutoremoveTimeout': 'at',
        }
        return {k: decoder(buffer, v) for k, v in mapping.items()}

    @classmethod
    def _decode_TextEntitiesMessageAttribute(cls, buffer):
        mapping = {
            'entities': 'entities',
        }
        return {k: decoder(buffer, v) for k, v in mapping.items()}

    @classmethod
    def _decode_ViewCountMessageAttribute(cls, buffer):
        mapping = {
            'count': 'c'
        }
        return {k: decoder(buffer, v) for k, v in mapping.items()}

    @classmethod
    def _decode_ForwardCountMessageAttribute(cls, buffer):
        mapping = {
            'count': 'c'
        }
        return {k: decoder(buffer, v) for k, v in mapping.items()}

    @classmethod
    def _decode_MessageTextEntity(cls, buffer):
        data = {
            'start': decoder(buffer, 'start'),
            'end': decoder(buffer, 'end'),
            'type': decoder(buffer, '_rawValue')
        }

        if data['type'] == 10:
            data['value'] = decoder(buffer, 'url')
        if data['type'] == 11:
            data['value'] = decoder(buffer, 'peerId')
        if data['type'] > 16:
            data['value'] = decoder(buffer, 'type')

        return data

    @classmethod
    def _decode_ReplyThreadMessageAttribute(cls, buffer):
        mapping = {
            'count': 'c',
            'latestUsers': 'u',
            'commentsPeerId': 'cp',
            'maxMessageId': 'mm',
            'maxReadMessageId': 'mrm',
        }
        return {k: decoder(buffer, v) for k, v in mapping.items()}

    @classmethod
    def _decode_ChannelMessageStateVersionAttribute(cls, buffer):
        mapping = {
            'pts': 'p',
        }
        return {k: decoder(buffer, v) for k, v in mapping.items()}

    @classmethod
    def _decode_EditedMessageAttribute(cls, buffer):
        mapping = {
            'date': 'd',
            'isHidden': 'h',
        }
        return {k: decoder(buffer, v) for k, v in mapping.items()}

    @classmethod
    def _decode_TelegramMediaImage(cls, buffer):
        mapping = {
            'width': 'w',
            'height': 'h',
            'resource': 'r',
            'startTimestamp': 's',
        }
        return {k: decoder(buffer, v) for k, v in mapping.items()}

    @classmethod
    def _decode_TelegramMediaImageRepresentation(cls, buffer):
        mapping = {
            'width': 'dx',
            'height': 'dy',
            'resource': 'r',
            'progressiveSizes': 'ps',
        }
        return {k: decoder(buffer, v) for k, v in mapping.items()}

    @classmethod
    def _decode_CloudPhotoSizeMediaResource(cls, buffer):
        mapping = {
            'datacenterId': 'd',
            'photoId': 'i',
            'accessHash': 'h',
            'sizeSpec': 's',
            'volumeId': 'v',
            'localId': 'l',
            'size': 'n',
            'fileReference': 'fr',
        }
        return {k: decoder(buffer, v) for k, v in mapping.items()}

    @classmethod
    def _decode_TelegramMediaWebpage(cls, buffer):
        data = {
            'webpageId': decoder(buffer, 'i'),
        }

        if decoder(buffer, 'ct') == 0:
            data['content'] = {
                'pendingDate': decoder(buffer, 'pendingDate'),
                'pendingUrl': decoder(buffer, 'pendingUrl'),
            }
        else:
            # todo:
            # data['content'] = cls._decode_TelegramMediaWebpageLoadedContent(buffer)
            data['content'] = None

        return data

    @classmethod
    def _decode_TelegramMediaWebpageLoadedContent(cls, buffer):
        mapping = {
            'url': 'u',
            'displayUrl': 'd',
            'hash': 'ha',
            'type': 'ty',
            'websiteName': 'ws',
            'title': 'ti',
            'text': 'tx',
            'embedUrl': 'eu',
            'embedType': 'et',
            'embedSizeWidth': 'esw',
            'embedSizeHeight': 'esh',
            'duration': 'du',
            'author': 'au',
            'image': 'im',  # TelegramMediaImage
            'file': 'fi',  # TelegramMediaFile
            'instantPage': 'ip',  # InstantPage
        }

        data = {k: decoder(buffer, v) for k, v in mapping.items()}
        attributes = []
        attributes.append(decoder(buffer, 'attr'))  # TelegramMediaWebpageAttribute[]
        attributes.append(decoder(buffer, 'fis'))  # TelegramMediaFile[]
        data['attributes'] = attributes
        return data

    @classmethod
    def _decode_TelegramMediaFile(cls, buffer):
        mapping = {
            'width': 'w',
            'height': 'h',
            'resource': 'r',  # todo: TelegramMediaResource
        }
        return {k: decoder(buffer, v) for k, v in mapping.items()}

    @classmethod
    def _decode_CloudDocumentMediaResource(cls, buffer):
        mapping = {
            'datacenterId': 'd',
            'fileId': 'f',
            'accessHash': 'a',
            'size': 'n',
            'fileReference': 'fr',
            'fileName': 'fn',
        }
        return {k: decoder(buffer, v) for k, v in mapping.items()}

    @classmethod
    def _decode_AuthorSignatureMessageAttribute(cls, buffer):
        mapping = {
            'signature': 's',
        }
        return {k: decoder(buffer, v) for k, v in mapping.items()}

    @classmethod
    def _decode_ReplyMarkupMessageAttribute(cls, buffer):
        mapping = {
            'rows': 'r',
            'flags': 'f',
        }
        return {k: decoder(buffer, v) for k, v in mapping.items()}

    @classmethod
    def _decode_ReplyMarkupRow(cls, buffer):
        mapping = {
            'buttons': 'b',
        }
        return {k: decoder(buffer, v) for k, v in mapping.items()}

    @classmethod
    def _decode_ReplyMarkupButton(cls, buffer):
        mapping = {
            'title': '.t',
            'titleWhenForwarded': '.tf',
            'action': 'v',  # todo: ReplyMarkupButtonAction
        }
        return {k: decoder(buffer, v) for k, v in mapping.items()}


_types_mapping = {
    getattr(TypesMapping, x): x for x in dir(TypesMapping)
    if not x.startswith('_') and not callable(getattr(TypesMapping, x))
}


def get_type_name(t_hash, is_full=False):
    name = _types_mapping.get(t_hash)
    return '%s#%s' % (name, t_hash) if is_full else name


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
        d_size = get_int(buffer, i, 4)
        return i + 4 + d_size * 4

    if d_type == ValueType.Int64Array:
        d_size = get_int(buffer, i, 4)
        return i + 4 + d_size * 8

    if d_type == ValueType.ObjectArray:
        length = get_int(buffer, i, 4)
        i += 4
        for x in range(length):
            d_size = get_int(buffer, i + 4, 4)
            i += 4 + 4 + d_size
        return i

    if d_type == ValueType.ObjectDictionary:
        raise NotImplementedError('No decoder_skip for ObjectDictionary')

    if d_type == ValueType.Bytes:
        d_size = get_int(buffer, i, 4)
        return i + 4 + d_size

    if d_type == ValueType.Nil:
        return i

    if d_type in (ValueType.StringArray, ValueType.BytesArray):
        raise NotImplementedError('No decoder_skip for StringArray')

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

        # print('*', key, k_size, k_name, d_type)
        if k_name != key:
            i = decoder_skip(buffer, i, d_type)
            continue

        if d_type == ValueType.Int32:
            return get_int(buffer, i, 4)

        if d_type == ValueType.Int64:
            return get_int(buffer, i, 8)

        if d_type == ValueType.Bool:
            raise NotImplementedError('No decoder for Bool')

        if d_type == ValueType.Double:
            raise NotImplementedError('No decoder for Double')

        if d_type == ValueType.String:
            d_size = get_int(buffer, i, 4)
            return get_str(buffer, i + 4, d_size)

        if d_type == ValueType.Object:
            t_hash = get_int(buffer, i, 4)
            d_size = get_int(buffer, i + 4, 4)
            i += 4 + 4
            return TypeDecoder.decode(t_hash, buffer[i:i + d_size])

        if d_type == ValueType.Int32Array:
            d_size = get_int(buffer, i, 4)
            i += 4
            values = []
            for x in range(d_size):
                values.append(get_int(buffer, i, 4))
                i += 4
            return values

        if d_type == ValueType.Int64Array:
            d_size = get_int(buffer, i, 4)
            i += 4
            values = []
            for x in range(d_size):
                values.append(get_int(buffer, i, 8))
                i += 8
            return values

        if d_type == ValueType.ObjectArray:
            length = get_int(buffer, i, 4)
            i += 4
            values = []
            for x in range(length):
                t_hash = get_int(buffer, i, 4)
                d_size = get_int(buffer, i + 4, 4)
                i += 4 + 4
                values.append(TypeDecoder.decode(t_hash, buffer[i:i + d_size]))
                i += d_size
            return values

        if d_type == ValueType.ObjectDictionary:
            raise NotImplementedError('No decoder for ObjectDictionary')

        if d_type == ValueType.Bytes:
            d_size = get_int(buffer, i, 4)
            i += 4
            return buffer[i:i + d_size].hex()

        if d_type == ValueType.Nil:
            return None

        if d_type == ValueType.StringArray:
            raise NotImplementedError('No decoder for StringArray')

        if d_type == ValueType.BytesArray:
            raise NotImplementedError('No decoder for BytesArray')
