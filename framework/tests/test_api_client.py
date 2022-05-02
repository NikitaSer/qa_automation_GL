def test_get_files_in_root(api_session):
    """Positive test for get_files_in_root().
    Check that the root folder is not empty"""
    assert api_session.get_files_in_root().get("total") > 0


def test_get_files_in_specific_folder(api_session):
    """Positive test for get_files_in_specific_folder().
    Check that the specific folder is not empty"""
    assert (
        api_session.get_files_in_specific_folder(
            folder_id="84c966d5-8dce-429d-8f92-44d5e28b1581"
        ).get("total")
        > 0
    )


def test_get_count_files_in_specific_folder(api_session):
    """Positive test for get_count_files_in_specific_folder().
    Check that we receive 'total' number of files in a specific folder
    and this folder is not empty"""
    assert (
        api_session.get_count_files_in_specific_folder(
            folder_id="84c966d5-8dce-429d-8f92-44d5e28b1581"
        ).get("total")
        > 0
    )


def test_get_runs_for_specific_file(api_session):
    """Positive test for get_runs_for_specific_file().
    Check that we receive 'runs' for a specific file"""
    assert (
        api_session.get_runs_for_specific_file(
            file_id="7f4c7326-0a4e-4b56-a8d0-8ce002191672"
        ).get("runs")
        is not None
    )


def test_get_analysis_for_specific_run(api_session):
    """Positive test for get_analysis_for_specific_run().
    Check that we receive 'analysis' for a specific run"""
    assert (
        api_session.get_analysis_for_specific_run(
            run_id="437ef8e4-b595-4fd8-a2f5-64221831e925"
        ).get("analysis")
        is not None
    )


def test_get_artifacts_for_specific_run(api_session):
    """Positive test for get_artifacts_for_specific_run().
    Check that we receive 'artifacts' for a specific run"""
    assert (
        api_session.get_artifacts_for_specific_run(
            run_id="437ef8e4-b595-4fd8-a2f5-64221831e925"
        ).get("artifacts")
        is not None
    )
