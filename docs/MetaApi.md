# dofusdude.MetaApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_game_search_types**](MetaApi.md#get_game_search_types) | **GET** /{game}/v1/meta/search/types | Available Game Search Types
[**get_item_types**](MetaApi.md#get_item_types) | **GET** /{game}/v1/meta/items/types | Available Item Types
[**get_meta_almanax_bonuses**](MetaApi.md#get_meta_almanax_bonuses) | **GET** /dofus3/v1/meta/{language}/almanax/bonuses | Available Almanax Bonuses
[**get_meta_almanax_bonuses_search**](MetaApi.md#get_meta_almanax_bonuses_search) | **GET** /dofus3/v1/meta/{language}/almanax/bonuses/search | Search Available Almanax Bonuses
[**get_meta_elements**](MetaApi.md#get_meta_elements) | **GET** /{game}/v1/meta/elements | Effects and Condition Elements
[**get_meta_version**](MetaApi.md#get_meta_version) | **GET** /{game}/v1/meta/version | Game Version


# **get_game_search_types**
> List[str] get_game_search_types(game)

Available Game Search Types

Get all types for /{game}/v1/{lang}/search available for filtering. All names are english for comparing them inside applications. Order is fixed so you can compare indices instead of strings.

### Example


```python
import dofusdude
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
    api_instance = dofusdude.MetaApi(api_client)
    game = 'dofus3' # str | game main 'dofus3' or beta channel 'dofus3beta'

    try:
        # Available Game Search Types
        api_response = api_instance.get_game_search_types(game)
        print("The response of MetaApi->get_game_search_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->get_game_search_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**| game main &#39;dofus3&#39; or beta channel &#39;dofus3beta&#39; | 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_item_types**
> List[str] get_item_types(game)

Available Item Types

Get all types of all items. Primarily used for filtering more detailed types in listings or search endpoints. All names are english for comparing them inside applications. Ordering is not guaranteed to persist with game updates.

### Example


```python
import dofusdude
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
    api_instance = dofusdude.MetaApi(api_client)
    game = 'dofus3' # str | game main 'dofus3' or beta channel 'dofus3beta'

    try:
        # Available Item Types
        api_response = api_instance.get_item_types(game)
        print("The response of MetaApi->get_item_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->get_item_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**| game main &#39;dofus3&#39; or beta channel &#39;dofus3beta&#39; | 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meta_almanax_bonuses**
> List[GetMetaAlmanaxBonuses200ResponseInner] get_meta_almanax_bonuses(language)

Available Almanax Bonuses

Get all the available bonuses and their id for filtering them in the range endpoint.

### Example


```python
import dofusdude
from dofusdude.models.get_meta_almanax_bonuses200_response_inner import GetMetaAlmanaxBonuses200ResponseInner
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
    api_instance = dofusdude.MetaApi(api_client)
    language = 'fr' # str | a valid language code

    try:
        # Available Almanax Bonuses
        api_response = api_instance.get_meta_almanax_bonuses(language)
        print("The response of MetaApi->get_meta_almanax_bonuses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->get_meta_almanax_bonuses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code | 

### Return type

[**List[GetMetaAlmanaxBonuses200ResponseInner]**](GetMetaAlmanaxBonuses200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meta_almanax_bonuses_search**
> List[GetMetaAlmanaxBonuses200ResponseInner] get_meta_almanax_bonuses_search(language, query, limit=limit)

Search Available Almanax Bonuses

Search all the available bonuses and their id for filtering them in the range endpoint.

### Example


```python
import dofusdude
from dofusdude.models.get_meta_almanax_bonuses200_response_inner import GetMetaAlmanaxBonuses200ResponseInner
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
    api_instance = dofusdude.MetaApi(api_client)
    language = 'fr' # str | a valid language code
    query = 'abond' # str | case sensitive search query
    limit = 56 # int | maximum number of returned results (optional)

    try:
        # Search Available Almanax Bonuses
        api_response = api_instance.get_meta_almanax_bonuses_search(language, query, limit=limit)
        print("The response of MetaApi->get_meta_almanax_bonuses_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->get_meta_almanax_bonuses_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| a valid language code | 
 **query** | **str**| case sensitive search query | 
 **limit** | **int**| maximum number of returned results | [optional] 

### Return type

[**List[GetMetaAlmanaxBonuses200ResponseInner]**](GetMetaAlmanaxBonuses200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meta_elements**
> List[str] get_meta_elements(game)

Effects and Condition Elements

Get the mappings for all specific elements that are linked in the dataset. All names are english. Translations are not needed because of a global unique id which is the index inside the array. Future elements will get a higher id.

### Example


```python
import dofusdude
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
    api_instance = dofusdude.MetaApi(api_client)
    game = 'dofus3' # str | game main 'dofus3' or beta channel 'dofus3beta'

    try:
        # Effects and Condition Elements
        api_response = api_instance.get_meta_elements(game)
        print("The response of MetaApi->get_meta_elements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->get_meta_elements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**| game main &#39;dofus3&#39; or beta channel &#39;dofus3beta&#39; | 

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_meta_version**
> Version get_meta_version(game)

Game Version

The current game version of the hosted data.

### Example


```python
import dofusdude
from dofusdude.models.version import Version
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
    api_instance = dofusdude.MetaApi(api_client)
    game = 'dofus3' # str | game main 'dofus3' or beta channel 'dofus3beta'

    try:
        # Game Version
        api_response = api_instance.get_meta_version(game)
        print("The response of MetaApi->get_meta_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetaApi->get_meta_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**| game main &#39;dofus3&#39; or beta channel &#39;dofus3beta&#39; | 

### Return type

[**Version**](Version.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

