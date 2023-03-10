# coding:utf-8
import json
import os
import pytest
from apis.device_management.device_account.apis_device_account import Apis, CommonApis

pid = ""


def setup():
    '''
    根据企业名称获取pid
    :return:
    '''
    try:
        global pid
        company_name = os.getenv("company_name")
        pid = CommonApis().get_company_id_with_company_name(company_name)
        assert pid is not None, "根据企业名称获取企业ID失败"

    except Exception as e:
        raise e


@pytest.mark.bvt
@pytest.mark.device
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_crud_asset_operator():
    """
    获取企业位置信息
    """
    try:
        global pid

        data = {
            "AssetType": "Organization",
            "sign": "get",
            "data": {
                "id": pid
            }
        }

        res = Apis().api_crud_asset_operator(data=data)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"
        company_type = os.getenv("company_type")
        if company_type != "":  # 专业版不存在企业类型
            assert json.loads(res.text)['data']['industry'] == company_type, f"企业类型错误:{company_type}"

    except Exception as e:
        raise e
