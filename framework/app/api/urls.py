class Urls:
    """Class with URLs using in the API methods"""
    LOGIN = '/api/v1/login'
    FILES_IN_ROOT = '/api/metagenid/v2/files?breadcrumbs=1&offset=0&limit=1000&_=1622700773180'
    FILES_IN_SPECIFIC_FOLDER = '/api/metagenid/v2/files?breadcrumbs=1&offset=0&limit=1000&_=1622700773180&folder_id=84c966d5-8dce-429d-8f92-44d5e28b1581'
    COUNT_FILES = 'https://app.cosmosid.com/api/metagenid/v2/files/count?folder_id=84c966d5-8dce-429d-8f92-44d5e28b1581&_=1622700773179'
    FILE_RESULTS_GET_RUN = 'https://app.cosmosid.com/api/metagenid/v1/files/7f4c7326-0a4e-4b56-a8d0-8ce002191672/runs?_=1622700773181'
    FILE_RESULTS_GET_ANALYSIS = 'https://app.cosmosid.com/api/metagenid/v1/runs/437ef8e4-b595-4fd8-a2f5-64221831e925/analysis?filter=total&_=1622700773184'
    FILE_RESULTS_GET_ARTIFACT = 'https://app.cosmosid.com/api/metagenid/v1/runs/437ef8e4-b595-4fd8-a2f5-64221831e925/artifacts?_=1622700773185'
