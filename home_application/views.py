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
from models import TEST, HostDisk,ScriptExecInfo
import json
import base64


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
    return render_json({"DATA": "AAAAAAAA"})


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
    return render_json({"status": "OK"})


def host_script(request):
    # 根据作业id查询日志
    data = ScriptExecInfo.objects.all()
    client = get_client_by_request(request)
    script_all = list()
    for item in data:
        temp_dict = dict()
        kwargs = {}
        kwargs['bk_biz_id'] = item.bk_biz_id
        kwargs['job_instance_id'] = item.job_instance_id
        result = client.job.get_job_instance_log(kwargs)
        log_content = result['data'][0]['step_results'][0]['ip_logs'][0]['log_content']
        temp_dict['host_ip'] = item.host_ip
        temp_dict['log_content'] = log_content
        temp_dict['script_content'] = item.script_content
        temp_dict['create_time'] = item.create_time
        script_all.append(temp_dict)

    return render_mako_context(request,
                               '/home_application/host_script.html',
                               {'script_all':script_all},
                               )


def script_tijiao(request):
    try:
        print(request.user.username)
    except Exception as e:
        print(str(e))
    data = json.loads(request.body)
    client = get_client_by_request(request)
    kwargs = {}
    result = client.cc.search_business(kwargs)
    bk_biz_id = result['data']['info'][0]['bk_biz_id']



    script_content = base64.b64encode(data['script_content']).decode("utf-8")
    kwargs = {}
    kwargs['bk_biz_id'] = bk_biz_id
    kwargs['script_content'] = script_content
    kwargs["account"] = "root"
    kwargs['ip_list'] = [{'bk_cloud_id':0,"ip":data['host_ip']}]
    result = client.job.fast_execute_script(kwargs)

    script_dict = dict()
    script_dict["host_ip"] = data['host_ip']
    script_dict["script_content"] = data['script_content']
    script_dict["job_instance_id"] = result['data']['job_instance_id']
    script_dict['bk_biz_id'] = bk_biz_id
    scriptexecinfo = ScriptExecInfo(**script_dict)
    scriptexecinfo.save()

    return render_json({"status": "OK"})
