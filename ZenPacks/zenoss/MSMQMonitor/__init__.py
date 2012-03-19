###########################################################################
#
# Copyright 2009-2010 Zenoss, Inc. All Rights Reserved.
#
###########################################################################

import Globals


# Add the msmqueues relation to all devices.
from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

Device._relations += (('msmqqueues', ToManyCont(ToOne,
    'ZenPacks.zenoss.MSMQMonitor.MSMQQueue', 'msmqserver')), )


from Products.ZenModel.ZenPack import ZenPackBase
class ZenPack(ZenPackBase):
    packZProperties = [
        ('zMSMQIgnoreQueues', '^tcp', 'string'),
        ]

    def install(self, app):
        ZenPackBase.install(self, app)
        self.rebuildRelations(app.zport.dmd)

    def upgrade(self, app):
        ZenPackBase.upgrade(self, app)
        self.rebuildRelations(app.zport.dmd)

    def remove(self, app, leaveObjects=False):
        Device._relations = tuple(
            [x for x in Device._relations if x[0] != 'msmqqueues'])
        self.rebuildRelations(app.zport.dmd)
        ZenPackBase.remove(self, app, leaveObjects)

    def rebuildRelations(self, dmd):
        for d in dmd.Devices.getSubDevices():
            d.buildRelations()

