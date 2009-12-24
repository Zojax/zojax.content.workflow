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
from rwproperty import setproperty, getproperty
from zope import interface
from zope.location import Location
from zope.component import getAdapters
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

from zojax.layoutform import Fields, PageletEditForm
from zojax.workflow.interfaces import IWorkflow
from zojax.content.type.interfaces import IContentType

from interfaces import IContentWorkflow


class ContentWorkflow(Location):
    interface.implements(IContentWorkflow)

    def __init__(self, context, request, contenttype):
        self.context = context
        self.request = request
        self.contenttype = contenttype

        self.__name__ = contenttype.name
        self.__parent__ = context

    @property
    def title(self):
        return self.contenttype.title

    @property
    def description(self):
        return self.contenttype.description

    @getproperty
    def workflow(self):
        return self.context.getWorkflowName(self.contenttype)

    @setproperty
    def workflow(self, value):
        self.context.setWorkflowName(self.contenttype, value)


class EditContentWorkflow(PageletEditForm):

    fields = Fields(IContentWorkflow)

    @property
    def label(self):
        return self.context.contenttype.title


def contentWorkflows(context):
    terms = []
    for name, wf in getAdapters((IContentType(context.contenttype),), IWorkflow):
        terms.append((wf.title, name))

    terms.sort()
    return SimpleVocabulary(
        [SimpleTerm(name, name, title) for title, name in terms])
