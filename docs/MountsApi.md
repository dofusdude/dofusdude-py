# dofusdude.MountsApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_mounts_list**](MountsApi.md#get_all_mounts_list) | **GET** /{game}/{language}/mounts/all | List All Mounts
[**get_mounts_list**](MountsApi.md#get_mounts_list) | **GET** /{game}/{language}/mounts | List Mounts
[**get_mounts_search**](MountsApi.md#get_mounts_search) | **GET** /{game}/{language}/mounts/search | Search Mounts
[**get_mounts_single**](MountsApi.md#get_mounts_single) | **GET** /{game}/{language}/mounts/{ankama_id} | Single Mounts


# **get_all_mounts_list**
> MountsListPaged get_all_mounts_list(language, game, filter_family_name=filter_family_name, accept_encoding=accept_encoding)

List All Mounts

Retrieve all mounts with one request. This endpoint is just an alias for the a list with disabled pagination (page[size]=-1) and all fields[type] set.  If you want everything unfiltered, delete the other query parameters.  Be careful with testing or (god forbid) using /all in your browser, the returned json is huge and will slow down the browser!  Tip: set the HTTP Header 'Accept-Encoding: gzip' for saving bandwidth. You will need to uncompress it on your end. Example with cURL: ``` curl -sH 'Accept-Encoding: gzip' <api-endpoint> | gunzip - ```

### Example

```python
import time
import os
import dofusdude
from dofusdude.models.mounts_list_paged import MountsListPaged
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.MountsApi(api_client)
    language = 'language_example' # str | a valid language code
    game = 'dofus2' # str | 
    filter_family_name = 'Dragoturkey' # str | only results with the translated family name (optional)
    accept_encoding = 'accept_encoding_example' # str | optional compression for saving bandwidth (optional)

    try:
        # List All Mounts
        api_response = api_instance.get_all_mounts_list(language, game, filter_family_name=filter_family_name, accept_encoding=accept_encoding)
        print("The response of MountsApi->get_all_mounts_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MountsApi->get_all_mounts_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code | 
 **game** | **str**|  | 
 **filter_family_name** | **str**| only results with the translated family name | [optional] 
 **accept_encoding** | **str**| optional compression for saving bandwidth | [optional] 

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

# **get_mounts_list**
> MountsListPaged get_mounts_list(language, game, filter_family_name=filter_family_name, page_size=page_size, page_number=page_number, fields_mount=fields_mount)

List Mounts

Retrieve a list of mounts.

### Example

```python
import time
import os
import dofusdude
from dofusdude.models.mounts_list_paged import MountsListPaged
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.MountsApi(api_client)
    language = 'language_example' # str | a valid language code
    game = 'dofus2' # str | 
    filter_family_name = 'Dragoturkey' # str | only results with the translated family name (optional)
    page_size = 10 # int | size of the results from the list. -1 disables pagination and gets all in one response. (optional)
    page_number = 1 # int | page number based on the current page[size]. So you could get page 1 with 8 entrys and page 2 would have entries 8 to 16. (optional)
    fields_mount = ['[\"effects\"]'] # List[str] | adds fields from their detail endpoint to the item list entries. Multiple comma separated values allowed. (optional)

    try:
        # List Mounts
        api_response = api_instance.get_mounts_list(language, game, filter_family_name=filter_family_name, page_size=page_size, page_number=page_number, fields_mount=fields_mount)
        print("The response of MountsApi->get_mounts_list:\n")
        pprint(api_response)
    except Exception as e:
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
 **fields_mount** | [**List[str]**](str.md)| adds fields from their detail endpoint to the item list entries. Multiple comma separated values allowed. | [optional] 

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
> List[MountListEntry] get_mounts_search(language, game, query, filter_family_name=filter_family_name, limit=limit)

Search Mounts

Search in all names and descriptions of mounts with a query.

### Example

```python
import time
import os
import dofusdude
from dofusdude.models.mount_list_entry import MountListEntry
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.MountsApi(api_client)
    language = 'fr' # str | a valid language code
    game = 'dofus2' # str | 
    query = 'Dorée' # str | case sensitive search query
    filter_family_name = 'Dragodinde' # str | only results with the translated family name (optional)
    limit = 8 # int | maximum number of returned results (optional) (default to 8)

    try:
        # Search Mounts
        api_response = api_instance.get_mounts_search(language, game, query, filter_family_name=filter_family_name, limit=limit)
        print("The response of MountsApi->get_mounts_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MountsApi->get_mounts_search: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code | 
 **game** | **str**|  | 
 **query** | **str**| case sensitive search query | 
 **filter_family_name** | **str**| only results with the translated family name | [optional] 
 **limit** | **int**| maximum number of returned results | [optional] [default to 8]

### Return type

[**List[MountListEntry]**](MountListEntry.md)

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
import os
import dofusdude
from dofusdude.models.mount import Mount
from dofusdude.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dofusdude.MountsApi(api_client)
    language = 'language_example' # str | a valid language code
    ankama_id = 180 # int | identifier
    game = 'dofus2' # str | 

    try:
        # Single Mounts
        api_response = api_instance.get_mounts_single(language, ankama_id, game)
        print("The response of MountsApi->get_mounts_single:\n")
        pprint(api_response)
    except Exception as e:
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

