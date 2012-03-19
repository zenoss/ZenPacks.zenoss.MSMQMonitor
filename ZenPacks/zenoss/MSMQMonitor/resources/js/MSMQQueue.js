/*
###########################################################################
#
# Copyright (C) 2010, Zenoss Inc.
#
###########################################################################
*/

(function(){

var ZC = Ext.ns('Zenoss.component');

var ZEvActions = Zenoss.events.EventPanelToolbarActions;

ZC.MSMQQueuePanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            autoExpandColumn: 'queueName',
            componentType: 'MSMQQueue',
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'queueName'},
                {name: 'messagesInQueueThreshold'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                width: 60
            },{
                id: 'queueName',
                dataIndex: 'queueName',
                header: _t('Queue')
            },{
                id: 'messagesInQueueThreshold',
                dataIndex: 'messagesInQueueThreshold',
                header: _t('Threshold')
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                width: 60
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons
            }]
        });
        ZC.MSMQQueuePanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('MSMQQueuePanel', ZC.MSMQQueuePanel);

})();
