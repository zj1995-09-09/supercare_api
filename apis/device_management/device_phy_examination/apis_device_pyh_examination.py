# coding:utf-8

import json
import os
from datetime import datetime
from apis.device_management.base import Base
from common.tools import retry


class Apis(Base):
    """
    单接口
    """

    def __init__(self):

        super(Apis, self).__init__()
        self.url = "http://192.168.1.211:31000"

    def api_get_report_year(self, data=None, params=None, headers=None):
        """
        :return:
        """
        try:

            self.headers_default = {
                "Authorization": os.getenv("cookies")
            }
            self.data_default = {}
            self.params_default = {
                "_t": datetime.now()
            }
            method = "get"
            url = self.url + "/api/PhysicalExaminationReport/GetReportYear"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res
        except Exception as e:
            raise e

    def api_get_reports(self, data=None, params=None, headers=None):
        """
        :return:
        """
        try:

            self.headers_default = {
                "Authorization": os.getenv("cookies")
            }
            self.data_default = {}
            self.params_default = {
                "_t": datetime.now()
            }
            method = "get"
            url = self.url + "/api/PhysicalExaminationReport/GetReports"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res
        except Exception as e:
            raise e

    def api_get_user_manage_device_tree(self, data=None, params=None, headers=None):
        """
        :return:
        """
        try:

            self.headers_default = {
                "Authorization": os.getenv("cookies"),
                "Content-Type": "application/json"
            }
            self.data_default = {}
            self.params_default = {
                "_t": datetime.now()
            }
            method = "post"
            url = self.url + "/api/basicService/api/app/manageAsset/getUserManageDeviceTree"
            res = self.apis(data=data, params=params, headers=headers, method=method, url=url)
            return res
        except Exception as e:
            raise e


class CommonApis(Apis):
    """
    常用业务方法
    """

    @retry(5, 3)
    def get_company_id_with_company_name(self, cname):
        """
        根据企业名称，获取企业id
        :param cname:
        :return:
        """
        pid = None
        res = self.api_get_children()
        for i in json.loads(res.text)['data']['items']:
            if i['name'] == cname:
                pid = i['id']

        return pid
