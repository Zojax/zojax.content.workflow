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
from zope import interface
from zope.component import getUtility
from zope.app.security.interfaces import IAuthentication
from zojax.statusmessage.interfaces import IStatusMessage
from zojax.wizard.step import WizardStep
from zojax.workflow.interfaces import _
from zojax.workflow.interfaces import IWorkflow, IWorkflowInfo, IWorkflowState


class WorkflowHistory(WizardStep):

    def isAvailable(self):
        if self.workflow is None:
            return False

        return super(WorkflowHistory, self).isAvailable()

    def update(self):
        request = self.request
        context = self.context

        self.workflow = IWorkflow(context, None)
        if self.workflow is None:
            return

        self.state = IWorkflowState(context)
        self.info = IWorkflowInfo(context)
        self.info.fireAutomatic()

        if 'form.workflow.change' in request:
            newtid = request.get('transition', '')
            if not newtid:
                IStatusMessage(request).add(
                    _('Please select workflow transition.'), 'warning')

            info = IWorkflowInfo(context)
            ids = [t.id for t in info.getTransitions()]
            if newtid in ids:
                info.fireTransition(newtid, request.get('comment',u''))
                IStatusMessage(request).add(
                    _(u'Workflow state has been changed.'))
            else:
                IStatusMessage(request).add(
                    _(u'Workflow state transition is not available.'), 'warning')

        auth = getUtility(IAuthentication)

        history = []
        for entry in self.state.history()[::-1]:
            rec = dict(entry)
            rec['actor'] = _('Unknwon')
            for actor in entry.get('actor', ()):
                try:
                    principal = auth.getPrincipal(actor)
                    rec['actor'] = principal.title
                    break
                except:
                    pass

            state = self.workflow.getState(entry.get('state', ''))
            if state:
                rec['state'] = state.title
            else:
                rec['state'] = _('Unknown')

            history.append(rec)

        self.history = history

        transitions = []
        for trans in self.info.getTransitions():
            transitions.append(
                (trans.title, {'id': trans.id,
                               'title': trans.title,
                               'description': trans.description}))
        transitions.sort()
        self.transitions = [item for _t, item in transitions]
