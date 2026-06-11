import requests

# 示例接口测试用例
def test_sample_api():
    url = "https://httpbin.org/get"
    response = requests.get(url)
    # 断言接口返回状态码是200
    assert response.status_code == 200
