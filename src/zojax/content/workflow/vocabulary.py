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
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

from zojax.workflow.interfaces import IWorkflowInfo


def WorkflowStates(content):
    wf = IWorkflow(content, None)
    if wf is None:
        return SimpleVocabulary(())

    terms = []
    for state in wf.getStates():
        term = SimpleTerm(state.id, state.id, state.title)
        term.state = state.description

        terms.append((state.title, term))

    terms.sort()
    return SimpleVocabulary([term for _t, term in terms])


def WorkflowTransitions(content):
    wfinfo = IWorkflowInfo(content, None)
    if wfinfo is None:
        return SimpleVocabulary(())

    terms = []
    for transition in wfinfo.getTransitions():
        term = SimpleTerm(transition.id, transition.id, transition.title)
        term.description = transition.description

        terms.append((transition.title, term))

    terms.sort()
    return SimpleVocabulary([term for _t, term in terms])
