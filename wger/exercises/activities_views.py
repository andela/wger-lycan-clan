# -*- coding: utf-8 -*-

# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

import datetime
import fitbit
import os

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils import formats
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy
from django.db.models import Min
from django.db.models import Max
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.db import IntegrityError
from django.contrib import messages

from rest_framework.response import Response
from rest_framework.decorators import api_view

from formtools.preview import FormPreview

from wger.core.models import Language
from wger.weight.forms import WeightForm
from wger.weight.models import WeightEntry
from wger.exercises.models import (FitbitActivities, ExerciseCategory)
from wger.weight import helpers
from wger.utils.helpers import check_access
from wger.utils.generic_views import WgerFormMixin



@login_required
def get_activities(request):
    all_activities = FitbitActivities.objects.all().filter(user=request.user)
    if all_activities is None:
        messages.warning(request, _("There are no activities saved in the database"))
    activities = []
    for activity in all_activities:
        act = {}
        act.update({'name': activity.name})
        act.update({'description': activity.description})
        messages.info(request, _(str(activity['name'])+'    '+str(activity['description']))
        activities.append(act)


    if len(activities) < 1:
        messages.warning(request, _("User currently has no activities logged."))    

    return render(request, 'exercise/fitbit_activities.html', {'activities': activities})
