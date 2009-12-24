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
from zope import interface, schema
from zope.i18nmessageid import MessageFactory
from zojax.workflow.interfaces import IWorkflowAware

_ = MessageFactory('zojax.content.workflow')


class IWorkflowType(interface.Interface):
    """ content type type with workflow support """


class IContentWorkflowAware(IWorkflowAware):
    """ content workflow aware """


class IWorkflowConfiglet(interface.Interface):
    """ workflow configlet """

    def getWorkflow(content):
        """ return IWorkflow object for content """

    def getWorkflowName(contenttype):
        """ return workflow name for content type """


class IDefaultWorkflow(interface.Interface):
    """ marker interface for default workflow """


class IWorkflowActivityRecord(interface.Interface):
    """ workflow activity record """

    source = interface.Attribute('Source state')
    sourceId = interface.Attribute('Source state')
    destination = interface.Attribute('Destination state')
    destinationId = interface.Attribute('Destination state')
    comment = interface.Attribute('Comment object')
