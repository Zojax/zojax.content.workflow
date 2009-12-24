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
from zope.component import getUtility, queryAdapter, getAdapters
from zope.lifecycleevent.interfaces import IObjectCreatedEvent
from zojax.controlpanel.configlet import Configlet
from zojax.workflow.interfaces import IWorkflow, IWorkflowInfo
from zojax.content.type.interfaces import IContent, IContentType

from interfaces import \
    IWorkflowType, IContentWorkflowAware, IWorkflowConfiglet, IDefaultWorkflow


class WorkflowConfiglet(Configlet):
    interface.implements(IWorkflowConfiglet)

    def getWorkflow(self, content):
        ct = IContentType(content)
        if not IWorkflowType.providedBy(ct):
            return None

        name = self.data.get(ct.name, '')

        wf = queryAdapter(ct, IWorkflow, name)
        if wf is not None:
            return wf

        wf = queryAdapter(ct, IDefaultWorkflow)
        if wf is not None:
            return wf

        for name, wf in getAdapters((ct,), IWorkflow):
            return wf

    def getWorkflowName(self, contenttype):
        name = self.data.get(contenttype.name, '')
        if not name:
            wf = queryAdapter(contenttype, IDefaultWorkflow)
            if wf is not None:
                return wf.name

        return name

    def setWorkflowName(self, contenttype, value):
        self.data[contenttype.name] = value


@component.adapter(IContentWorkflowAware)
@interface.implementer(IWorkflow)
def contentWorkflow(content):
    return getUtility(IWorkflowConfiglet).getWorkflow(content)
