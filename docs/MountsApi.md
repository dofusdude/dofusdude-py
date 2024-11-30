# dofusdude.MountsApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_mounts_list**](MountsApi.md#get_all_mounts_list) | **GET** /{game}/v1/{language}/mounts/all | List All Mounts
[**get_mounts_list**](MountsApi.md#get_mounts_list) | **GET** /{game}/v1/{language}/mounts | List Mounts
[**get_mounts_search**](MountsApi.md#get_mounts_search) | **GET** /{game}/v1/{language}/mounts/search | Search Mounts
[**get_mounts_single**](MountsApi.md#get_mounts_single) | **GET** /{game}/v1/{language}/mounts/{ankama_id} | Single Mounts


# **get_all_mounts_list**
> ListMounts get_all_mounts_list(language, game, filter_family_name=filter_family_name, accept_encoding=accept_encoding, filter_family_id=filter_family_id)

List All Mounts

Retrieve all mounts with one request. This endpoint is just an alias for the a list with disabled pagination (page[size]=-1) and all fields[type] set.  If you want everything unfiltered, delete the other query parameters.  Be careful with testing or (god forbid) using /all in your browser, the returned json is huge and will slow down the browser!  Tip: set the HTTP Header 'Accept-Encoding: gzip' for saving bandwidth. You will need to uncompress it on your end. Example with cURL: ``` curl -sH 'Accept-Encoding: gzip' <api-endpoint> | gunzip - ```

### Example


```python
import dofusdude
from dofusdude.models.list_mounts import ListMounts
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
    game = 'dofus3beta' # str | game main 'dofus3' or beta channel 'dofus3beta'
    filter_family_name = 'Dragoturkey' # str | only results with the translated family name (optional)
    accept_encoding = 'accept_encoding_example' # str | optional compression for saving bandwidth (optional)
    filter_family_id = 56 # int | only results with the unique family id (optional)

    try:
        # List All Mounts
        api_response = api_instance.get_all_mounts_list(language, game, filter_family_name=filter_family_name, accept_encoding=accept_encoding, filter_family_id=filter_family_id)
        print("The response of MountsApi->get_all_mounts_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MountsApi->get_all_mounts_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code | 
 **game** | **str**| game main &#39;dofus3&#39; or beta channel &#39;dofus3beta&#39; | 
 **filter_family_name** | **str**| only results with the translated family name | [optional] 
 **accept_encoding** | **str**| optional compression for saving bandwidth | [optional] 
 **filter_family_id** | **int**| only results with the unique family id | [optional] 

### Return type

[**ListMounts**](ListMounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mounts_list**
> ListMounts get_mounts_list(language, game, filter_family_name=filter_family_name, page_size=page_size, page_number=page_number, fields_mount=fields_mount, filter_family_id=filter_family_id)

List Mounts

Retrieve a list of mounts.

### Example


```python
import dofusdude
from dofusdude.models.list_mounts import ListMounts
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
    game = 'dofus3beta' # str | game main 'dofus3' or beta channel 'dofus3beta'
    filter_family_name = 'Dragoturkey' # str | only results with the translated family name (optional)
    page_size = 10 # int | size of the results from the list. -1 disables pagination and gets all in one response. (optional)
    page_number = 1 # int | page number based on the current page[size]. So you could get page 1 with 8 entrys and page 2 would have entries 8 to 16. (optional)
    fields_mount = ['[\"effects\"]'] # List[str] | adds fields from their detail endpoint to the item list entries. Multiple comma separated values allowed. (optional)
    filter_family_id = 56 # int | only results with the unique family id (optional)

    try:
        # List Mounts
        api_response = api_instance.get_mounts_list(language, game, filter_family_name=filter_family_name, page_size=page_size, page_number=page_number, fields_mount=fields_mount, filter_family_id=filter_family_id)
        print("The response of MountsApi->get_mounts_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MountsApi->get_mounts_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code | 
 **game** | **str**| game main &#39;dofus3&#39; or beta channel &#39;dofus3beta&#39; | 
 **filter_family_name** | **str**| only results with the translated family name | [optional] 
 **page_size** | **int**| size of the results from the list. -1 disables pagination and gets all in one response. | [optional] 
 **page_number** | **int**| page number based on the current page[size]. So you could get page 1 with 8 entrys and page 2 would have entries 8 to 16. | [optional] 
 **fields_mount** | [**List[str]**](str.md)| adds fields from their detail endpoint to the item list entries. Multiple comma separated values allowed. | [optional] 
 **filter_family_id** | **int**| only results with the unique family id | [optional] 

### Return type

[**ListMounts**](ListMounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mounts_search**
> List[Mount] get_mounts_search(language, game, query, filter_family_name=filter_family_name, limit=limit)

Search Mounts

Search in all names and descriptions of mounts with a query.

### Example


```python
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
    language = 'fr' # str | a valid language code
    game = 'dofus3beta' # str | game main 'dofus3' or beta channel 'dofus3beta'
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
 **game** | **str**| game main &#39;dofus3&#39; or beta channel &#39;dofus3beta&#39; | 
 **query** | **str**| case sensitive search query | 
 **filter_family_name** | **str**| only results with the translated family name | [optional] 
 **limit** | **int**| maximum number of returned results | [optional] [default to 8]

### Return type

[**List[Mount]**](Mount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mounts_single**
> Mount get_mounts_single(language, ankama_id, game)

Single Mounts

Retrieve a specific mount with id.

### Example


```python
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
    game = 'dofus3beta' # str | game main 'dofus3' or beta channel 'dofus3beta'

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
 **game** | **str**| game main &#39;dofus3&#39; or beta channel &#39;dofus3beta&#39; | 

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
**200** |  |  -  |
**400** |  |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

