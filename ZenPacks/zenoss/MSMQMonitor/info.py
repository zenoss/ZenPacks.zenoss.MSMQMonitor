######################################################################
#
# Copyright 2010 Zenoss, Inc.  All Rights Reserved.
#
######################################################################

from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo

from ZenPacks.zenoss.MSMQMonitor.interfaces import *


class MSMQQueueInfo(ComponentInfo):
    implements(IMSMQQueueInfo)

    queueName = ProxyProperty('queueName')
    messagesInQueueThreshold = ProxyProperty('messagesInQueueThreshold')
