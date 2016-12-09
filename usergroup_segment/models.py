# coding: utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import Group
from django.db import models
from django.utils import six
from django.utils.functional import lazy
from django.utils.translation import ugettext_lazy as _
from aldryn_segmentation.models import SegmentBasePluginModel


class UserGroupSegmentPluginModel(SegmentBasePluginModel):
    group = models.ForeignKey(Group, verbose_name=_('Group'))

    class Meta:
        app_label = 'usergroup_segment'

    @property
    def configuration_string(self):

        def wrapper():
            return self.group.name

        return lazy(
            wrapper,
            six.text_type
        )()
