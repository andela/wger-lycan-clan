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
    all_activities = FitbitActivities.objects.all()
    return render(request, 'exercise/fitbit_activities.html', all_activities)

@login_required
def getweight(request, token=None):
    if token:
        client_secret = os.environ.get('FITBIT_SECRET')
        client_key = os.environ.get('FITBIT_KEY')
        token = token

        authorized_client = fitbit.Fitbit(client_key, client_secret,
                                     access_token=token, refresh_token=token)
        
        if authorized_client.get_bodyweight()['weight']:
            weight_data = authorized_client.get_bodyweight()['weight'][0]
            date = weight_data['date']
            weight = weight_data['weight']
            try:
                weight_object = WeightEntry.objects.create(date=date, weight=weight, user=request.user)
                weight_object.save()
            except IntegrityError as e:
                messages.info(request, _("You have already logged today's weight"))

        if authorized_client.activities()['activities']:
            activities = authorized_client.activities()['activities']
            if not ExerciseCategory.objects.filter(name='Fitbit Exercises').exists():
                exercise_category = ExerciseCategory()
                exercise_category.name = 'Fitbit Exercises'
                exercise_category.save()
            for activity in activities:
                exercise_object = Exercise.objects.create(
                    name_original=activity['activityParentName'],
                    name=activity['activityParentName'],
                    description=activity['description'],
                    category=ExerciseCategory.objects.get(name='Fitbit Exercises'),
                    language=Language.objects.get(short_name='en'),
                    user=request.user,
                    status=2
                    )

            # for activity in activities:
            #     exercise = Exercise()
            #     exercise.name_original = activity['activityParentName']
            #     exercise.name = activity['activityParentName']
            #     exercise.description = activity['description']
            #     exercise.category = ExerciseCategory.objects.get(name='Fitbit Exercises')
            #     exercise.language = Language.objects.get(short_name='en')
            #     exercise.user = request.user
            #     exercise.status = 2
                try:
                    exercise_object.save()
                    messages.success(request, _("You have successfully synced your exercise data."))
                except IntegrityError as e:
                    messages.info(request, _("You have already logged today's exercises"))

    return redirect('/en/weight/overview/' + str(request.user))

