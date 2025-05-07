from shuler.cldy import business_mappings

def test_get_business_mappings_exists():
    assert hasattr(business_mappings, "get_business_mappings")

def test_get_business_mapping_index_exists():
    assert hasattr(business_mappings, "get_business_mapping_index")

def test_get_business_mapping_exists():
    assert hasattr(business_mappings, "get_business_mapping")

def test_update_business_mapping_exists():
    assert hasattr(business_mappings, "update_business_mapping")

def test_create_business_mapping_exists():
    assert hasattr(business_mappings, "create_business_mapping")

def test_delete_business_mapping_exists():
    assert hasattr(business_mappings, "delete_business_mapping")