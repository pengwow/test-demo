# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云(BlueKing) available.
Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
"""

from django.db import models


class TEST(models.Model):
    A = models.CharField(u"功能code", max_length=64, unique=True)
    B = models.IntegerField(u"ss")
    C = models.TextField()

    class Meta:
        db_table = 'lp_test'


class HostDisk(models.Model):
    host_name = models.CharField(max_length=64)
    host_path = models.CharField(max_length=64)
    os = models.CharField(max_length=64)
    host_ip = models.CharField(max_length=64)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'host'
