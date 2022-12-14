<a name="__pageTop"></a>
# dofusdude.apis.tags.consumables_api.ConsumablesApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_items_consumables_list**](#get_all_items_consumables_list) | **get** /{game}/{language}/items/consumables/all | List All Consumables
[**get_items_consumables_list**](#get_items_consumables_list) | **get** /{game}/{language}/items/consumables | List Consumables
[**get_items_consumables_search**](#get_items_consumables_search) | **get** /{game}/{language}/items/consumables/search | Search Consumables
[**get_items_consumables_single**](#get_items_consumables_single) | **get** /{game}/{language}/items/consumables/{ankama_id} | Single Consumables

# **get_all_items_consumables_list**
<a name="get_all_items_consumables_list"></a>
> ItemsListPaged get_all_items_consumables_list(languagegame)

List All Consumables

Retrieve all consumable items with one request. This endpoint is just an alias for the a list with disabled pagination (page[size]=-1) and all fields[type] set.  If you want everything unfiltered, delete the other query parameters.  Be careful with testing or (god forbid) using /all in your browser, the returned json is huge and will slow down the browser!  Tip: set the HTTP Header 'Accept-Encoding: gzip' for saving bandwidth. You will need to uncompress it on your end. Example with cURL: ``` curl -sH 'Accept-Encoding: gzip' <api-endpoint> | gunzip - ```

### Example

```python
import dofusdude
from dofusdude.apis.tags import consumables_api
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
    api_instance = consumables_api.ConsumablesApi(api_client)

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
        # List All Consumables
        api_response = api_instance.get_all_items_consumables_list(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling ConsumablesApi->get_all_items_consumables_list: %s\n" % e)

    # example passing only optional values
    path_params = {
        'language': "en",
        'game': "dofus2",
    }
    query_params = {
        'sort[level]': "asc",
        'filter[type_name]': "Chest",
        'filter[min_level]': 150,
        'filter[max_level]': 180,
    }
    header_params = {
        'Accept-Encoding': "gzip",
    }
    try:
        # List All Consumables
        api_response = api_instance.get_all_items_consumables_list(
            path_params=path_params,
            query_params=query_params,
            header_params=header_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling ConsumablesApi->get_all_items_consumables_list: %s\n" % e)
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
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FilterMaxLevelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

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
200 | [ApiResponseFor200](#get_all_items_consumables_list.ApiResponseFor200) | Consumables Found
400 | [ApiResponseFor400](#get_all_items_consumables_list.ApiResponseFor400) | Bad Request 
404 | [ApiResponseFor404](#get_all_items_consumables_list.ApiResponseFor404) | Not Found

#### get_all_items_consumables_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ItemsListPaged**](../../models/ItemsListPaged.md) |  | 


#### get_all_items_consumables_list.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_all_items_consumables_list.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_items_consumables_list**
<a name="get_items_consumables_list"></a>
> ItemsListPaged get_items_consumables_list(languagegame)

List Consumables

Retrieve a list of consumable items.

### Example

```python
import dofusdude
from dofusdude.apis.tags import consumables_api
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
    api_instance = consumables_api.ConsumablesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'language': "en",
        'game': "dofus2",
    }
    query_params = {
    }
    try:
        # List Consumables
        api_response = api_instance.get_items_consumables_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling ConsumablesApi->get_items_consumables_list: %s\n" % e)

    # example passing only optional values
    path_params = {
        'language': "en",
        'game': "dofus2",
    }
    query_params = {
        'sort[level]': "asc",
        'filter[type_name]': "Chest",
        'filter[min_level]': 150,
        'filter[max_level]': 180,
        'page[size]': 2,
        'page[number]': 1,
        'fields[item]': ["recipe"],
    }
    try:
        # List Consumables
        api_response = api_instance.get_items_consumables_list(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling ConsumablesApi->get_items_consumables_list: %s\n" % e)
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
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# FilterMaxLevelSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

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
200 | [ApiResponseFor200](#get_items_consumables_list.ApiResponseFor200) | Consumables Found
400 | [ApiResponseFor400](#get_items_consumables_list.ApiResponseFor400) | Bad Request 
404 | [ApiResponseFor404](#get_items_consumables_list.ApiResponseFor404) | Not Found

#### get_items_consumables_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ItemsListPaged**](../../models/ItemsListPaged.md) |  | 


#### get_items_consumables_list.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_items_consumables_list.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_items_consumables_search**
<a name="get_items_consumables_search"></a>
> [ItemListEntry] get_items_consumables_search(languagegamequery)

Search Consumables

Search in all names and descriptions of consumable items with a query.

### Example

```python
import dofusdude
from dofusdude.apis.tags import consumables_api
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
    api_instance = consumables_api.ConsumablesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'language': "en",
        'game': "dofus2",
    }
    query_params = {
        'query': "Wholewrite",
    }
    try:
        # Search Consumables
        api_response = api_instance.get_items_consumables_search(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling ConsumablesApi->get_items_consumables_search: %s\n" % e)

    # example passing only optional values
    path_params = {
        'language': "en",
        'game': "dofus2",
    }
    query_params = {
        'query': "Wholewrite",
        'filter[type_name]': "Bread",
        'filter[min_level]': 1,
        'filter[max_level]': 200,
        'limit': 8,
    }
    try:
        # Search Consumables
        api_response = api_instance.get_items_consumables_search(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling ConsumablesApi->get_items_consumables_search: %s\n" % e)
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
limit | LimitSchema | | optional


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

# LimitSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 8

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
200 | [ApiResponseFor200](#get_items_consumables_search.ApiResponseFor200) | Consumables Found
400 | [ApiResponseFor400](#get_items_consumables_search.ApiResponseFor400) | Bad Request  Possibilities: - empty or no query 
404 | [ApiResponseFor404](#get_items_consumables_search.ApiResponseFor404) | Not Found  Possibilities: - no hits for query

#### get_items_consumables_search.ApiResponseFor200
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

#### get_items_consumables_search.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_items_consumables_search.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_items_consumables_single**
<a name="get_items_consumables_single"></a>
> Resource get_items_consumables_single(languageankama_idgame)

Single Consumables

Retrieve a specific consumable item with id.

### Example

```python
import dofusdude
from dofusdude.apis.tags import consumables_api
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
    api_instance = consumables_api.ConsumablesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'language': "en",
        'ankama_id': 17206,
        'game': "dofus2",
    }
    try:
        # Single Consumables
        api_response = api_instance.get_items_consumables_single(
            path_params=path_params,
        )
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling ConsumablesApi->get_items_consumables_single: %s\n" % e)
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
200 | [ApiResponseFor200](#get_items_consumables_single.ApiResponseFor200) | Consumable Found
400 | [ApiResponseFor400](#get_items_consumables_single.ApiResponseFor400) | Bad Request  Possibilities: - invalid ankama id format 
404 | [ApiResponseFor404](#get_items_consumables_single.ApiResponseFor404) | Not Found  Possibilities: - nothing found for this ankama_id

#### get_items_consumables_single.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Resource**](../../models/Resource.md) |  | 


#### get_items_consumables_single.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### get_items_consumables_single.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

