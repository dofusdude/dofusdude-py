# dofusdude.AlmanaxApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_almanax_date**](AlmanaxApi.md#get_almanax_date) | **GET** /dofus2/{language}/almanax/{date} | Single Almanax Date
[**get_almanax_range**](AlmanaxApi.md#get_almanax_range) | **GET** /dofus2/{language}/almanax | Almanax Range


# **get_almanax_date**
> AlmanaxEntry get_almanax_date(language, date)

Single Almanax Date

Get a single date. There are not more details in the returned object than the normal range endpoint.

### Example


```python
import time
import dofusdude
from dofusdude.api import almanax_api
from dofusdude.model.almanax_entry import AlmanaxEntry
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = almanax_api.AlmanaxApi(api_client)
    language = "en" # str | code
    date = "date_example" # str | yyyy-mm-dd

    # example passing only required values which don't have defaults set
    try:
        # Single Almanax Date
        api_response = api_instance.get_almanax_date(language, date)
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling AlmanaxApi->get_almanax_date: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| code |
 **date** | **str**| yyyy-mm-dd |

### Return type

[**AlmanaxEntry**](AlmanaxEntry.md)

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

# **get_almanax_range**
> [AlmanaxEntry] get_almanax_range(language)

Almanax Range

Get a range of dates, defaults to today + 6 following days but can specified by the query parameters.   filter[bonus_type] can be used seperately and does not have an effect on the other parameters.  range[from] changes the start date, everything else defaults to 6 following dates from this start date.  range[to] when used without anything else, it will use today as start date and this parameter as end. All ranges are inclusive.  range[from] + range[to] = inclusive range over the specified dates, should never be farther apart than 35 days.  range[from|to] + range[size] no need to specify the date, just following days with [from] (0 is today) or go backwards in time with only [to] and [size].  Not all combinations are listed but this should give you an idea how to they could work.

### Example


```python
import time
import dofusdude
from dofusdude.api import almanax_api
from dofusdude.model.almanax_entry import AlmanaxEntry
from pprint import pprint
# Defining the host is optional and defaults to https://api.dofusdu.de
# See configuration.py for a list of all supported configuration parameters.
configuration = dofusdude.Configuration(
    host = "https://api.dofusdu.de"
)


# Enter a context with an instance of the API client
with dofusdude.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = almanax_api.AlmanaxApi(api_client)
    language = "en" # str | code
    filter_bonus_type = "experience-points" # str | ids from meta/{language}/almanax/bonuses (optional)
    range_from = "range[from]_example" # str | yyyy-mm-dd (optional)
    range_to = "range[to]_example" # str | yyyy-mm-dd (optional)
    range_size = 1 # int | size of the returned range (optional)
    timezone = "Europe/Paris" # str | determine what the current time is. If you live in Brazil, \"today\" will be hours apart from Paris. Use your timezone to get results relative to your location. (optional) if omitted the server will use the default value of "Europe/Paris"

    # example passing only required values which don't have defaults set
    try:
        # Almanax Range
        api_response = api_instance.get_almanax_range(language)
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling AlmanaxApi->get_almanax_range: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Almanax Range
        api_response = api_instance.get_almanax_range(language, filter_bonus_type=filter_bonus_type, range_from=range_from, range_to=range_to, range_size=range_size, timezone=timezone)
        pprint(api_response)
    except dofusdude.ApiException as e:
        print("Exception when calling AlmanaxApi->get_almanax_range: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| code |
 **filter_bonus_type** | **str**| ids from meta/{language}/almanax/bonuses | [optional]
 **range_from** | **str**| yyyy-mm-dd | [optional]
 **range_to** | **str**| yyyy-mm-dd | [optional]
 **range_size** | **int**| size of the returned range | [optional]
 **timezone** | **str**| determine what the current time is. If you live in Brazil, \&quot;today\&quot; will be hours apart from Paris. Use your timezone to get results relative to your location. | [optional] if omitted the server will use the default value of "Europe/Paris"

### Return type

[**[AlmanaxEntry]**](AlmanaxEntry.md)

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

