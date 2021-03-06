#  Copyright (c) 2018 Red Hat, Inc.
#
#  This file is part of ARA Records Ansible.
#
#  ARA is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  ARA is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with ARA.  If not, see <http://www.gnu.org/licenses/>.

from rest_framework import viewsets

from ara.api import models, serializers


class LabelViewSet(viewsets.ModelViewSet):
    queryset = models.Label.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.ListLabelSerializer
        elif self.action == "retrieve":
            return serializers.DetailedLabelSerializer
        else:
            # create/update/destroy
            return serializers.LabelSerializer


class PlaybookViewSet(viewsets.ModelViewSet):
    queryset = models.Playbook.objects.all()
    filter_fields = ("name", "status")

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.ListPlaybookSerializer
        elif self.action == "retrieve":
            return serializers.DetailedPlaybookSerializer
        else:
            # create/update/destroy
            return serializers.PlaybookSerializer


class PlayViewSet(viewsets.ModelViewSet):
    queryset = models.Play.objects.all()
    filter_fields = ("playbook", "uuid")

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.ListPlaySerializer
        elif self.action == "retrieve":
            return serializers.DetailedPlaySerializer
        else:
            # create/update/destroy
            return serializers.PlaySerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    filter_fields = ("playbook",)

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.ListTaskSerializer
        elif self.action == "retrieve":
            return serializers.DetailedTaskSerializer
        else:
            # create/update/destroy
            return serializers.TaskSerializer


class HostViewSet(viewsets.ModelViewSet):
    queryset = models.Host.objects.all()
    filter_fields = ("playbook",)

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.ListHostSerializer
        elif self.action == "retrieve":
            return serializers.DetailedHostSerializer
        else:
            # create/update/destroy
            return serializers.HostSerializer


class ResultViewSet(viewsets.ModelViewSet):
    filter_fields = ("playbook",)

    def get_queryset(self):
        statuses = self.request.GET.getlist("status")
        if statuses:
            return models.Result.objects.filter(status__in=statuses)
        return models.Result.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.ListResultSerializer
        elif self.action == "retrieve":
            return serializers.DetailedResultSerializer
        else:
            # create/update/destroy
            return serializers.ResultSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = models.File.objects.all()
    filter_fields = ("playbook", "path")

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.ListFileSerializer
        elif self.action == "retrieve":
            return serializers.DetailedFileSerializer
        else:
            # create/update/destroy
            return serializers.FileSerializer


class RecordViewSet(viewsets.ModelViewSet):
    queryset = models.Record.objects.all()
    filter_fields = ("playbook", "key")

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.ListRecordSerializer
        elif self.action == "retrieve":
            return serializers.DetailedRecordSerializer
        else:
            # create/update/destroy
            return serializers.RecordSerializer
