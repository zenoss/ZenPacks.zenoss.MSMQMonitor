######################################################################
#
# Copyright 2010 Zenoss, Inc.  All Rights Reserved.
#
######################################################################

from zope.interface import Attribute, Interface

from Products.Zuul.form import schema
from Products.Zuul.infos.component import IComponentInfo


class IMSMQQueueInfo(IComponentInfo):
    """
    Info adapter for MSMQQueue components.
    """

    queueName = schema.TextLine(title=u'Queue Name', group=u'Overview', readonly=True, order=-1)
    messagesInQueueThreshold = schema.TextLine(title=u'Queued Messages Threshold', group='Overview', readonly=False)
