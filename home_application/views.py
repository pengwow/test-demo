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

from common.mymako import render_mako_context, render_json
from blueking.component.shortcuts import get_client_by_request
from models import TEST,HostDisk
import json

def home(request):
    """
    首页
    """

    # yewu = [
    #     {'id': 1, "name": u"业务1"},
    #     {'id': 2, "name": u"业务2"},
    #     {'id': 3, "name": u"业务3"},
    # ]

    # 从环境配置获取APP信息，从request获取当前用户信息
    client = get_client_by_request(request)

    kwargs = {}
    result = client.cc.search_business(kwargs)
    print(result)
    yewu = result['data']['info']
    return render_mako_context(request, '/home_application/home.html',
                               {
                                   "yewu": yewu,
                                   "AAA": u"业务列表"
                               })


def submit_template(request):
    """
    首页
    """
    print(request.body)
    return render_json({"1111111": "dddddddddd"})


def dev_guide(request):
    """
    开发指引
    """
    return render_mako_context(request, '/home_application/dev_guide.html')


def contactus(request):
    """
    联系我们
    """
    return render_mako_context(request, '/home_application/contact.html')


def tijiao(request):
    data = json.loads(request.body)
    print(type(data))
    sss = TEST(**data)
    sss.save()
    return render_json({"DATA":"AAAAAAAA"})


def host_disk(request):
    host_list = HostDisk.objects.all()
    re_list = list()
    for item in host_list:
        temp_dict = dict()
        temp_dict['os'] = item.os
        temp_dict['host_ip'] = item.host_ip
        temp_dict['host_name'] = item.host_name
        temp_dict['host_path'] = item.host_path
        temp_dict['create_time'] = item.create_time
        re_list.append(temp_dict)

    print(re_list)
    return render_mako_context(request,
                               '/home_application/host_disk.html',
                               {'host_all': re_list}
                               )

def host_tijiao(request):
    data = request.body
    print(type(data))
    data = json.loads(data)

    host = HostDisk(**data)
    host.save()
    return render_json({"status":"OK"})