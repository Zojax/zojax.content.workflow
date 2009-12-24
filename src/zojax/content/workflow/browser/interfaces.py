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
from zojax.widget.radio.field import RadioChoice
from zojax.content.workflow.interfaces import _


class IContentWorkflow(interface.Interface):
    """ content workflow """

    contenttype = interface.Attribute('IContentType object')

    workflow = RadioChoice(
        title = _(u'Workflow'),
        description = _('Select workflow for this content type.'),
        vocabulary = 'zojax.content.workflow.contentworkflows',
        required = True)
