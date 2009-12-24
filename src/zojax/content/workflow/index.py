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
from zc.catalog.catalogindex import ValueIndex
from zojax.catalog.utils import Indexable
from zojax.workflow.interfaces import IWorkflowState


def workflowState():
    return ValueIndex(
        'value', Indexable('zojax.content.workflow.index.WorkflowState'))


class WorkflowState(object):

    def __init__(self, content, default=None):
        self.value = default

        state = IWorkflowState(content, None)
        if state is not None:
            self.value = state.getState().id
