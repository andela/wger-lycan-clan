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
# along with Workout Manager.  If not, see <http://www.gnu.org/licenses/>.

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from wger.weight.forms import WeightCsvImportForm
from wger.weight import views


urlpatterns = [
    url(r'^add/$',
        login_required(views.WeightAddView.as_view()),
        name='add'),

    url(r'^get-token/$',
        login_required(views.WeightAddView.get_token),
        name='get-token'),

    url(r'^get-weight/(?P<token>[\w.@+-_d]+)$',
        login_required(views.WeightAddView.get_weight),
        name='get-weight'
        ),

    url(r'^(?P<pk>\d+)/edit/$',
        login_required(views.WeightUpdateView.as_view()),
        name='edit'),

    url(r'^export-csv/$',
        views.export_csv,
        name='export-csv'),
    url(r'^import-csv/$',
        login_required(views.WeightCsvImportFormPreview(WeightCsvImportForm)),
        name='import-csv'),

    url(r'^overview/(?P<username>[\w.@+-]+)$',
        views.overview,
        name='overview'),

    url(r'^authorize-fitbit/$',
        views.authorize_fitbit,
        name='authorize-fitbit'),

    url(r'^sync-fitbit/$',
        views.sync_fitbit_data,
        name='sync-with-fitbit'),

    # url(r'^overview/$',
    #     views.overview,
    #     name='overview'),
    url(r'^api/get_weight_data/(?P<username>[\w.@+-]+)$',  # JS
        views.get_weight_data,
        name='weight-data'),
    url(r'^api/get_weight_data/$',  # JS
        views.get_weight_data,
        name='weight-data'),
]
