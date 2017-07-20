# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)

# StorageId: DOM Storage identifier.
class StorageId(ChromeTypeBase):
    def __init__(self,
                 securityOrigin: Union['str'],
                 isLocalStorage: Union['bool'],
                 ):

        self.securityOrigin = securityOrigin
        self.isLocalStorage = isLocalStorage


# Item: DOM Storage item.
Item = [str]

class DOMStorage(PayloadMixin):
    """ Query and modify DOM storage.
    """
    @classmethod
    def enable(cls):
        """Enables storage tracking, storage events will now be delivered to the client.
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )

    @classmethod
    def disable(cls):
        """Disables storage tracking, prevents storage events from being sent to the client.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def clear(cls,
              storageId: Union['StorageId'],
              ):
        """
        :param storageId: 
        :type storageId: StorageId
        """
        return (
            cls.build_send_payload("clear", {
                "storageId": storageId,
            }),
            None
        )

    @classmethod
    def getDOMStorageItems(cls,
                           storageId: Union['StorageId'],
                           ):
        """
        :param storageId: 
        :type storageId: StorageId
        """
        return (
            cls.build_send_payload("getDOMStorageItems", {
                "storageId": storageId,
            }),
            cls.convert_payload({
                "entries": {
                    "class": [Item],
                    "optional": False
                },
            })
        )

    @classmethod
    def setDOMStorageItem(cls,
                          storageId: Union['StorageId'],
                          key: Union['str'],
                          value: Union['str'],
                          ):
        """
        :param storageId: 
        :type storageId: StorageId
        :param key: 
        :type key: str
        :param value: 
        :type value: str
        """
        return (
            cls.build_send_payload("setDOMStorageItem", {
                "storageId": storageId,
                "key": key,
                "value": value,
            }),
            None
        )

    @classmethod
    def removeDOMStorageItem(cls,
                             storageId: Union['StorageId'],
                             key: Union['str'],
                             ):
        """
        :param storageId: 
        :type storageId: StorageId
        :param key: 
        :type key: str
        """
        return (
            cls.build_send_payload("removeDOMStorageItem", {
                "storageId": storageId,
                "key": key,
            }),
            None
        )



class DomStorageItemsClearedEvent(BaseEvent):

    js_name = 'Domstorage.domStorageItemsCleared'
    hashable = ['storageId']
    is_hashable = True

    def __init__(self,
                 storageId: Union['StorageId', dict],
                 ):
        if isinstance(storageId, dict):
            storageId = StorageId(**storageId)
        self.storageId = storageId

    @classmethod
    def build_hash(cls, storageId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class DomStorageItemRemovedEvent(BaseEvent):

    js_name = 'Domstorage.domStorageItemRemoved'
    hashable = ['storageId']
    is_hashable = True

    def __init__(self,
                 storageId: Union['StorageId', dict],
                 key: Union['str', dict],
                 ):
        if isinstance(storageId, dict):
            storageId = StorageId(**storageId)
        self.storageId = storageId
        if isinstance(key, dict):
            key = str(**key)
        self.key = key

    @classmethod
    def build_hash(cls, storageId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class DomStorageItemAddedEvent(BaseEvent):

    js_name = 'Domstorage.domStorageItemAdded'
    hashable = ['storageId']
    is_hashable = True

    def __init__(self,
                 storageId: Union['StorageId', dict],
                 key: Union['str', dict],
                 newValue: Union['str', dict],
                 ):
        if isinstance(storageId, dict):
            storageId = StorageId(**storageId)
        self.storageId = storageId
        if isinstance(key, dict):
            key = str(**key)
        self.key = key
        if isinstance(newValue, dict):
            newValue = str(**newValue)
        self.newValue = newValue

    @classmethod
    def build_hash(cls, storageId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class DomStorageItemUpdatedEvent(BaseEvent):

    js_name = 'Domstorage.domStorageItemUpdated'
    hashable = ['storageId']
    is_hashable = True

    def __init__(self,
                 storageId: Union['StorageId', dict],
                 key: Union['str', dict],
                 oldValue: Union['str', dict],
                 newValue: Union['str', dict],
                 ):
        if isinstance(storageId, dict):
            storageId = StorageId(**storageId)
        self.storageId = storageId
        if isinstance(key, dict):
            key = str(**key)
        self.key = key
        if isinstance(oldValue, dict):
            oldValue = str(**oldValue)
        self.oldValue = oldValue
        if isinstance(newValue, dict):
            newValue = str(**newValue)
        self.newValue = newValue

    @classmethod
    def build_hash(cls, storageId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h