# noinspection PyPep8
# noinspection PyArgumentList

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from chromewhip.protocol import runtime as Runtime
from chromewhip.protocol import network as Network

# LogEntry: Log entry.
class LogEntry(ChromeTypeBase):
    def __init__(self,
                 source: Union['str'],
                 level: Union['str'],
                 text: Union['str'],
                 timestamp: Union['Runtime.Timestamp'],
                 url: Optional['str'] = None,
                 lineNumber: Optional['int'] = None,
                 stackTrace: Optional['Runtime.StackTrace'] = None,
                 networkRequestId: Optional['Network.RequestId'] = None,
                 workerId: Optional['str'] = None,
                 ):

        self.source = source
        self.level = level
        self.text = text
        self.timestamp = timestamp
        self.url = url
        self.lineNumber = lineNumber
        self.stackTrace = stackTrace
        self.networkRequestId = networkRequestId
        self.workerId = workerId


# ViolationSetting: Violation configuration setting.
class ViolationSetting(ChromeTypeBase):
    def __init__(self,
                 name: Union['str'],
                 threshold: Union['float'],
                 ):

        self.name = name
        self.threshold = threshold


class Log(PayloadMixin):
    """ Provides access to log entries.
    """
    @classmethod
    def enable(cls):
        """Enables log domain, sends the entries collected so far to the client by means of the <code>entryAdded</code> notification.
        """
        return (
            cls.build_send_payload("enable", {
            }),
            None
        )

    @classmethod
    def disable(cls):
        """Disables log domain, prevents further log entries from being reported to the client.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def clear(cls):
        """Clears the log.
        """
        return (
            cls.build_send_payload("clear", {
            }),
            None
        )

    @classmethod
    def startViolationsReport(cls,
                              config: Union['[ViolationSetting]'],
                              ):
        """start violation reporting.
        :param config: Configuration for violations.
        :type config: [ViolationSetting]
        """
        return (
            cls.build_send_payload("startViolationsReport", {
                "config": config,
            }),
            None
        )

    @classmethod
    def stopViolationsReport(cls):
        """Stop violation reporting.
        """
        return (
            cls.build_send_payload("stopViolationsReport", {
            }),
            None
        )



class EntryAddedEvent(BaseEvent):

    js_name = 'Log.entryAdded'
    hashable = []
    is_hashable = False

    def __init__(self,
                 entry: Union['LogEntry', dict],
                 ):
        if isinstance(entry, dict):
            entry = LogEntry(**entry)
        self.entry = entry

    @classmethod
    def build_hash(cls):
        raise ValueError('Unable to build hash for non-hashable type')