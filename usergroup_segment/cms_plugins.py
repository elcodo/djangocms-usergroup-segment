# coding: utf-8
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from aldryn_segmentation.cms_plugins import SegmentPluginBase
from cms.plugin_pool import plugin_pool
from .models import UserGroupSegmentPluginModel


@plugin_pool.register_plugin
class UserGroupSegmentPlugin(SegmentPluginBase):
    model = UserGroupSegmentPluginModel
    name = _('Segment by user group')

    def is_context_appropriate(self, context, instance):
        request = context.get('request')
        if request.user.is_authenticated and \
                request.user.groups.filter(pk=instance.group.pk).exists():
            return True
        return False
