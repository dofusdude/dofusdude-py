# dofusdude.MountsApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mounts_list**](MountsApi.md#get_mounts_list) | **GET** /{game}/{language}/mounts | List Mounts
[**get_mounts_search**](MountsApi.md#get_mounts_search) | **GET** /{game}/{language}/mounts/search | Search Mounts
[**get_mounts_single**](MountsApi.md#get_mounts_single) | **GET** /{game}/{language}/mounts/{ankama_id} | Single Mounts


# **get_mounts_list**
> MountsListPaged get_mounts_list(language, game)

List Mounts

Retrieve a list of mounts.

### Example


```python
import time
import dofusdude
from dofusdude.api import mounts_api
from dofusdude.model.mounts_list_paged import MountsListPaged
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mounts_api.MountsApi(api_client)
    language = "en" # str | a valid language code
    game = "dofus2" # str | 
    filter_family_name = "filter[family_name]_example" # str | only results with the translated family name (optional)
    page_size = -1 # int | size of the results from the list. -1 disables pagination and gets all in one response. (optional)
    page_number = 0 # int | page number based on the current page[size]. So you could get page 1 with 8 entrys and page 2 would have entries 8 to 16. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Mounts
        api_response = api_instance.get_mounts_list(language, game)
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling MountsApi->get_mounts_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Mounts
        api_response = api_instance.get_mounts_list(language, game, filter_family_name=filter_family_name, page_size=page_size, page_number=page_number)
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling MountsApi->get_mounts_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code |
 **game** | **str**|  |
 **filter_family_name** | **str**| only results with the translated family name | [optional]
 **page_size** | **int**| size of the results from the list. -1 disables pagination and gets all in one response. | [optional]
 **page_number** | **int**| page number based on the current page[size]. So you could get page 1 with 8 entrys and page 2 would have entries 8 to 16. | [optional]

### Return type

[**MountsListPaged**](MountsListPaged.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mounts Found |  -  |
**400** | Bad Request  |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mounts_search**
> [MountListEntry] get_mounts_search(language, game, query)

Search Mounts

Search in all names and descriptions of mounts with a query.

### Example


```python
import time
import dofusdude
from dofusdude.api import mounts_api
from dofusdude.model.mount_list_entry import MountListEntry
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mounts_api.MountsApi(api_client)
    language = "en" # str | a valid language code
    game = "dofus2" # str | 
    query = "almond" # str | case sensitive search query
    filter_family_name = "rhineetle" # str | only results with the translated family name (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search Mounts
        api_response = api_instance.get_mounts_search(language, game, query)
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling MountsApi->get_mounts_search: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Mounts
        api_response = api_instance.get_mounts_search(language, game, query, filter_family_name=filter_family_name)
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling MountsApi->get_mounts_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code |
 **game** | **str**|  |
 **query** | **str**| case sensitive search query |
 **filter_family_name** | **str**| only results with the translated family name | [optional]

### Return type

[**[MountListEntry]**](MountListEntry.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mounts Found |  -  |
**400** | Bad Request  Possibilities: - empty or no query  |  -  |
**404** | Not Found  Possibilities: - no hits for query |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mounts_single**
> Mount get_mounts_single(language, ankama_id, game)

Single Mounts

Retrieve a specific mount with id.

### Example


```python
import time
import dofusdude
from dofusdude.api import mounts_api
from dofusdude.model.mount import Mount
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = mounts_api.MountsApi(api_client)
    language = "en" # str | a valid language code
    ankama_id = 180 # int | identifier
    game = "dofus2" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Single Mounts
        api_response = api_instance.get_mounts_single(language, ankama_id, game)
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling MountsApi->get_mounts_single: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code |
 **ankama_id** | **int**| identifier |
 **game** | **str**|  |

### Return type

[**Mount**](Mount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mount Found |  -  |
**400** | Bad Request  Possibilities: - invalid ankama id format  |  -  |
**404** | Not Found  Possibilities: - nothing found for this ankama_id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

