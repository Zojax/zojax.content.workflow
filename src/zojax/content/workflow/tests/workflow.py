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
from zojax.workflow import State, NullState, Workflow
from zojax.workflow import ManualTransition, AutomaticTransition

stateVisible = State('visible', 'Visible')
statePrivate = State('private', 'Private')


transInit = AutomaticTransition(
    'init', 'Init workflow', (NullState,), stateVisible)
transVisible = ManualTransition(
    'visible', 'Visible', (statePrivate,), stateVisible)
transPrivate = ManualTransition(
    'private', 'Private', (stateVisible,), statePrivate)


wf = Workflow('default', 'Default Workflow',
              [transInit, transVisible, transPrivate])


wf2 = Workflow('simple', 'simple Workflow',
               [transInit, transVisible, transPrivate])
