from app import index_page

def test_index():
    assert index_page() == 'Hello, World'