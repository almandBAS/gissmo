# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _


"""
Allowed states for a given Station

States:

  1 : INSTALLATION : Installation in progress
  2 : OPERATION : Operation in progress
  3 : DEFAUT : Failure
  4 : PANNE : Waste
  5 : FERMEE : Closed
  6 : AUTRE : Other
  7 : EN_TEST : Test in progress
"""
INSTALLATION = 1
OPERATION = 2
DEFAUT = 3
PANNE = 4
FERMEE = 5
AUTRE = 6
EN_TEST = 7
STATION_STATES = (
    (INSTALLATION, _('Installing')),
    (EN_TEST, _('Testing')),
    (OPERATION, _('Running')),
    (DEFAUT, _('Broken')),
    (PANNE, _('Failure')),
    (FERMEE, _('Closed')),
    (AUTRE, _('Other')),
)
