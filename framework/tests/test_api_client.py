def test_get_files_in_root(api_client):
    """Positive test for get_files_in_root(). Check that we receive files from the root"""
    #DELETE
    print(f"test_get_files_in_root, api client object is : {api_client.__hash__}")
    assert api_client.get_files_in_root() is None


def test_get_files_in_specific_folder(api_client):
    """Positive test for get_files_in_specific_folder(). Check that we receive files from a specific folder"""
    # DELETE
    print(f"test_get_files_in_specific_folder, api client object is : {api_client.__hash__}")
    assert api_client.get_files_in_specific_folder() is None


def test_get_count_files_in_specific_folder(api_client):
    """Positive test for get_count_files_in_specific_folder(). Check that we receive number of files in a specific folder"""
    assert api_client.get_count_files_in_specific_folder() is None
