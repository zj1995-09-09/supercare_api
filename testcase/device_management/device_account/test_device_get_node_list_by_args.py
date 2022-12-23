# coding:utf-8
import json,pytest
from apis.device_management.device_account.apis_device_account import Apis, CommonApis

pid = ""

def setup():
    '''
    根据企业名称获取pid
    :return:
    '''
    try:
        global pid
        company_name = '111'
        pid = CommonApis().get_company_id_with_company_name(company_name)
        assert pid is not None, "根据企业名称获取企业ID失败"

    except Exception as e:
        raise e


@pytest.mark.bvt
@pytest.mark.device
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_get_node_list_by_args():
    try:
        global pid
        data = {
            "type": "asset",
            "parentId": pid,
            "checkedIds": [],
            "all": False,
            "openVibrationZone": False,

        }
        res = Apis().api_get_node_list_by_args(data=data)
        assert res.status_code <= 200, "Http请求状态码错误"
        assert json.loads(res.text)['success'] is True, "业务接口返回False"
        assert len(json.loads(res.text)['data']) == 1, "业务数据获取异常"

    except Exception as e:
        raise e


# def teardown()