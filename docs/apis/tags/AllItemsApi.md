<a name="__pageTop"></a>
# dofusdude.apis.tags.all_items_api.AllItemsApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_items_all_search**](#get_items_all_search) | **get** /{game}/{language}/items/search | Search All Items

# **get_items_all_search**
<a name="get_items_all_search"></a>
> [ItemsListEntryTyped] get_items_all_search(languagegamequery)

Search All Items

Search in all names and descriptions of Dofus items (including all subtypes) with a query.

### Example

```python
import dofusdude
from dofusdude.apis.tags import all_items_api
from dofusdude.model.items_list_entry_typed import ItemsListEntryTyped
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)

# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = all_items_api.AllItemsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'language': "en",
        'game': "dofus2",
    }
    query_params = {
        'query': "atcham",
    }
    try:
        # Search All Items
        api_response = api_instance.get_items_all_search(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling AllItemsApi->get_items_all_search: %s\n" % e)

    # example passing only optional values
    path_params = {
        'language': "en",
        'game': "dofus2",
    }
    query_params = {
        'query': "atcham",
        'filter[type_name]': "Bottes",
        'filter[min_level]': 190,
        'filter[max_level]': 200,
    }
    try:
        # Search All Items
        api_response = api_instance.get_items_all_search(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling AllItemsApi->get_items_all_search: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query | QuerySchema | | 
filter[type_name] | FilterTypeNameSchema | | optional
filter[min_level] | FilterMinLevelSchema | | optional
filter[max_level] | FilterMaxLevelSchema | | optional


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FilterTypeNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FilterMinLevelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

# FilterMaxLevelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
language | LanguageSchema | | 
game | GameSchema | | 

# LanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["en", "fr", "de", "it", "es", "pt", ] 

# GameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["dofus2", "dofus2beta", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_items_all_search.ApiResponseFor200) | Items Found
400 | [ApiResponseFor400](#get_items_all_search.ApiResponseFor400) | Bad Request  Possibilities: - empty or no query 
404 | [ApiResponseFor404](#get_items_all_search.ApiResponseFor404) | Not Found  Possibilities: - no hits for query

#### get_items_all_search.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ItemsListEntryTyped**]({{complexTypePrefix}}ItemsListEntryTyped.md) | [**ItemsListEntryTyped**]({{complexTypePrefix}}ItemsListEntryTyped.md) | [**ItemsListEntryTyped**]({{complexTypePrefix}}ItemsListEntryTyped.md) |  | 

#### get_items_all_search.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_items_all_search.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

