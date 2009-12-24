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
import zojax.content
from zope import schema, interface, component
from zope.configuration.fields import GlobalObject

from zojax.workflow.interfaces import IWorkflow
from zojax.content.type.interfaces import IContentType

from interfaces import IDefaultWorkflow, IContentWorkflowAware


class IWorkflowDirective(interface.Interface):

    type = schema.TextLine(
        title = u"Content type",
        required = True)

    workflow = GlobalObject(
        title = u'Workflow object',
        required = True)

    default = schema.Bool(
        title = u'Default',
        default = False,
        required = False)


class ContentWorkflow(object):

    def __init__(self, workflow):
        self.workflow = workflow

    def __call__(self, context, default=None):
        return self.workflow


def contentWorkflowHandler(_context, type, workflow, default=False):
    _context.action(
        discriminator = ('zojax:workflow', workflow.name, type),
        callable = contentWorkflow,
        args = (type, workflow))

    if default:
        interface.alsoProvides(workflow, IDefaultWorkflow)
        _context.action(
            discriminator = ('zojax:workflow-default', type),
            callable = defaultContentWorkflow,
            args = (type, workflow))


def contentWorkflow(type, workflow):
    sm = component.getGlobalSiteManager()

    ct = sm.queryUtility(IContentType, type)
    if ct is None:
        ct = component.getSiteManager().getUtility(IContentType, type)

    interface.classImplements(ct.klass, IContentWorkflowAware)

    iface = getattr(zojax.content, type.replace('.', '_').replace('-', '_'))

    sm.registerAdapter(
        ContentWorkflow(workflow), (iface,), IWorkflow, workflow.name)


def defaultContentWorkflow(type, workflow):
    iface = getattr(zojax.content, type.replace('.', '_').replace('-', '_'))

    component.getGlobalSiteManager().registerAdapter(
        ContentWorkflow(workflow), (iface,), IDefaultWorkflow)
