##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from zope import interface, component
from zope.component import getUtility

from zojax.activity.record import ActivityRecord
from zojax.activity.interfaces import IActivity, IActivityRecordDescription
from zojax.content.activity.interfaces import IContentActivityRecord
from zojax.workflow.interfaces import IWorkflowTransitionEvent

from interfaces import _, IWorkflowActivityRecord


class WorkflowActivityRecord(ActivityRecord):
    interface.implements(IWorkflowActivityRecord, IContentActivityRecord)

    type = u'workflow'
    verb = _('state changed')


class WorkflowActivityRecordDescription(object):
    interface.implements(IActivityRecordDescription)

    title = _(u'Workflow')
    description = _(u'Content workflow state changed.')


@component.adapter(IWorkflowTransitionEvent)
def stateChangedHandler(event):
    getUtility(IActivity).add(
        event.object, WorkflowActivityRecord(
            source = event.source.title,
            sourceId = event.source.id,
            destination = event.destination.title,
            destinationId = event.destination.id,
            comment = event.comment))
