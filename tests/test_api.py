from bridge_app.api import index

def test_api():
    assert index()['message'] == 'API sanity check successful'