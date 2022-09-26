<a name="__pageTop"></a>
# dofusdude.apis.tags.resources_api.ResourcesApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_items_resources_list**](#get_all_items_resources_list) | **get** /{game}/{language}/items/resources/all | List All Resources
[**get_items_resource_search**](#get_items_resource_search) | **get** /{game}/{language}/items/resources/search | Search Resources
[**get_items_resources_list**](#get_items_resources_list) | **get** /{game}/{language}/items/resources | List Resources
[**get_items_resources_single**](#get_items_resources_single) | **get** /{game}/{language}/items/resources/{ankama_id} | Single Resources

# **get_all_items_resources_list**
<a name="get_all_items_resources_list"></a>
> ItemsListPaged get_all_items_resources_list(languagegame)

List All Resources

Retrieve all resource items with one request. This endpoint is just an alias for the a list with disabled pagination (page[size]=-1) and all fields[type] set.  If you want everything unfiltered, delete the other query parameters.  Be careful with testing or (god forbid) using /all in your browser, the returned json is huge and will slow down the browser!  Tip: set the HTTP Header 'Accept-Encoding: gzip' for saving bandwidth. You will need to uncompress it on your end. Example with cURL: ``` curl -sH 'Accept-Encoding: gzip' <api-endpoint> | gunzip - ```

### Example

```python
import dofusdude
from dofusdude.apis.tags import resources_api
from dofusdude.model.items_list_paged import ItemsListPaged
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)

# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = resources_api.ResourcesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'language': "en",
        'game': "dofus2",
    }
    query_params = {
    }
    header_params = {
    }
    try:
        # List All Resources
        api_response = api_instance.get_all_items_resources_list(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling ResourcesApi->get_all_items_resources_list: %s\n" % e)

    # example passing only optional values
    path_params = {
        'language': "en",
        'game': "dofus2",
    }
    query_params = {
        'sort[level]': "desc",
        'filter[type_name]': "miscellaneous resources",
        'filter[min_level]': 160,
        'filter[max_level]': 190,
    }
    header_params = {
        'Accept-Encoding': "gzip",
    }
    try:
        # List All Resources
        api_response = api_instance.get_all_items_resources_list(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling ResourcesApi->get_all_items_resources_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
sort[level] | SortLevelSchema | | optional
filter[type_name] | FilterTypeNameSchema | | optional
filter[min_level] | FilterMinLevelSchema | | optional
filter[max_level] | FilterMaxLevelSchema | | optional


# SortLevelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["asc", "desc", ] 

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

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept-Encoding | AcceptEncodingSchema | | optional

# AcceptEncodingSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["gzip", ] 

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
200 | [ApiResponseFor200](#get_all_items_resources_list.ApiResponseFor200) | Resources Found
400 | [ApiResponseFor400](#get_all_items_resources_list.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#get_all_items_resources_list.ApiResponseFor404) | Not Found

#### get_all_items_resources_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ItemsListPaged**](../../models/ItemsListPaged.md) |  | 


#### get_all_items_resources_list.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_all_items_resources_list.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_items_resource_search**
<a name="get_items_resource_search"></a>
> [ItemListEntry] get_items_resource_search(languagegamequery)

Search Resources

Search in all names and descriptions of resource items with a query.

### Example

```python
import dofusdude
from dofusdude.apis.tags import resources_api
from dofusdude.model.item_list_entry import ItemListEntry
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)

# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = resources_api.ResourcesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'language': "en",
        'game': "dofus2",
    }
    query_params = {
        'query': "snowdew",
    }
    try:
        # Search Resources
        api_response = api_instance.get_items_resource_search(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling ResourcesApi->get_items_resource_search: %s\n" % e)

    # example passing only optional values
    path_params = {
        'language': "en",
        'game': "dofus2",
    }
    query_params = {
        'query': "snowdew",
        'filter[type_name]': "plant",
        'filter[min_level]': 150,
        'filter[max_level]': 200,
    }
    try:
        # Search Resources
        api_response = api_instance.get_items_resource_search(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling ResourcesApi->get_items_resource_search: %s\n" % e)
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
200 | [ApiResponseFor200](#get_items_resource_search.ApiResponseFor200) | Resources Found
400 | [ApiResponseFor400](#get_items_resource_search.ApiResponseFor400) | Bad Request  Possibilities: - empty or no query 
404 | [ApiResponseFor404](#get_items_resource_search.ApiResponseFor404) | Not Found  Possibilities: - no hits for query

#### get_items_resource_search.ApiResponseFor200
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
[**ItemListEntry**]({{complexTypePrefix}}ItemListEntry.md) | [**ItemListEntry**]({{complexTypePrefix}}ItemListEntry.md) | [**ItemListEntry**]({{complexTypePrefix}}ItemListEntry.md) |  | 

#### get_items_resource_search.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_items_resource_search.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_items_resources_list**
<a name="get_items_resources_list"></a>
> ItemsListPaged get_items_resources_list(languagegame)

List Resources

Retrieve a list of resource items.

### Example

```python
import dofusdude
from dofusdude.apis.tags import resources_api
from dofusdude.model.items_list_paged import ItemsListPaged
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)

# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = resources_api.ResourcesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'language': "en",
        'game': "dofus2",
    }
    query_params = {
    }
    try:
        # List Resources
        api_response = api_instance.get_items_resources_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling ResourcesApi->get_items_resources_list: %s\n" % e)

    # example passing only optional values
    path_params = {
        'language': "en",
        'game': "dofus2",
    }
    query_params = {
        'sort[level]': "desc",
        'filter[type_name]': "miscellaneous resources",
        'filter[min_level]': 160,
        'filter[max_level]': 190,
        'page[size]': 10,
        'page[number]': 1,
        'fields[item]': ["recipe"],
    }
    try:
        # List Resources
        api_response = api_instance.get_items_resources_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling ResourcesApi->get_items_resources_list: %s\n" % e)
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
sort[level] | SortLevelSchema | | optional
filter[type_name] | FilterTypeNameSchema | | optional
filter[min_level] | FilterMinLevelSchema | | optional
filter[max_level] | FilterMaxLevelSchema | | optional
page[size] | PageSizeSchema | | optional
page[number] | PageNumberSchema | | optional
fields[item] | FieldsItemSchema | | optional


# SortLevelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["asc", "desc", ] 

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

# PageSizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# PageNumberSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FieldsItemSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["recipe", "description", "conditions", "effects", ] 

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
200 | [ApiResponseFor200](#get_items_resources_list.ApiResponseFor200) | Resources Found
400 | [ApiResponseFor400](#get_items_resources_list.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#get_items_resources_list.ApiResponseFor404) | Not Found

#### get_items_resources_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ItemsListPaged**](../../models/ItemsListPaged.md) |  | 


#### get_items_resources_list.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_items_resources_list.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_items_resources_single**
<a name="get_items_resources_single"></a>
> Resource get_items_resources_single(languageankama_idgame)

Single Resources

Retrieve a specific resource item with id.

### Example

```python
import dofusdude
from dofusdude.apis.tags import resources_api
from dofusdude.model.resource import Resource
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)

# Enter a context with an instance of the API client
with dofusdude.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = resources_api.ResourcesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'language': "en",
        'ankama_id': 7295,
        'game': "dofus2",
    }
    try:
        # Single Resources
        api_response = api_instance.get_items_resources_single(
            path_params=path_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling ResourcesApi->get_items_resources_single: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
language | LanguageSchema | | 
ankama_id | AnkamaIdSchema | | 
game | GameSchema | | 

# LanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["en", "fr", "de", "it", "es", "pt", ] 

# AnkamaIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# GameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["dofus2", "dofus2beta", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_items_resources_single.ApiResponseFor200) | Resource Found
400 | [ApiResponseFor400](#get_items_resources_single.ApiResponseFor400) | Bad Request  Possibilities: - invalid ankama id format 
404 | [ApiResponseFor404](#get_items_resources_single.ApiResponseFor404) | Not Found  Possibilities: - nothing found for this ankama_id

#### get_items_resources_single.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Resource**](../../models/Resource.md) |  | 


#### get_items_resources_single.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_items_resources_single.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

