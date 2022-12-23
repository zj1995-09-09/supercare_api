# coding:utf-8
import json,pytest
from apis.device_management.device_account.apis_device_account import Apis, CommonApis


@pytest.mark.bvt
@pytest.mark.device
@pytest.mark.flaky(reruns=3, reruns_delay=3)
def test_by_asset_types():
    try:

        res = Apis().api_by_asset_types()
        assert res.status_code <= 200, "Http请求状态码错误"
        assert len(json.loads(res.text)) == 234, "业务接口返回类型数量缺少"

    except Exception as e:
        raise e
