# dofusdude.AlmanaxApi

All URIs are relative to *https://api.dofusdu.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_almanax_date**](AlmanaxApi.md#get_almanax_date) | **GET** /dofus3/v1/{language}/almanax/{date} | Single Almanax Date
[**get_almanax_range**](AlmanaxApi.md#get_almanax_range) | **GET** /dofus3/v1/{language}/almanax | Almanax Range


# **get_almanax_date**
> Almanax get_almanax_date(language, var_date)

Single Almanax Date

Get a single date. There are not more details in the returned object than the normal range endpoint.

### Example


```python
import dofusdude
from dofusdude.models.almanax import Almanax
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
    api_instance = dofusdude.AlmanaxApi(api_client)
    language = 'fr' # str | code
    var_date = 'Tue Jul 14 00:00:00 UTC 2020' # date | yyyy-mm-dd

    try:
        # Single Almanax Date
        api_response = api_instance.get_almanax_date(language, var_date)
        print("The response of AlmanaxApi->get_almanax_date:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanaxApi->get_almanax_date: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| code | 
 **var_date** | **date**| yyyy-mm-dd | 

### Return type

[**Almanax**](Almanax.md)

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

# **get_almanax_range**
> List[Almanax] get_almanax_range(language, filter_bonus_type=filter_bonus_type, range_from=range_from, range_to=range_to, range_size=range_size, timezone=timezone)

Almanax Range

Get a range of dates, defaults to today + 6 following days but can specified by the query parameters.   filter[bonus_type] can be used seperately and does not have an effect on the other parameters.  range[from] changes the start date, everything else defaults to 6 following dates from this start date.  range[to] when used without anything else, it will use today as start date and this parameter as end. All ranges are inclusive.  range[from] + range[to] = inclusive range over the specified dates, should never be farther apart than 35 days.  range[from|to] + range[size] no need to specify the date, just following days with [from] (0 is today) or go backwards in time with only [to] and [size].  Not all combinations are listed but this should give you an idea how to they could work.

### Example


```python
import dofusdude
from dofusdude.models.almanax import Almanax
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
    api_instance = dofusdude.AlmanaxApi(api_client)
    language = 'fr' # str | code
    filter_bonus_type = 'experience-points' # str | ids from meta/{language}/almanax/bonuses (optional)
    range_from = 'Thu Sep 15 00:00:00 UTC 2016' # date | yyyy-mm-dd (optional)
    range_to = 'Wed Sep 28 00:00:00 UTC 2016' # date | yyyy-mm-dd (optional)
    range_size = -1 # int | size of the returned range (optional)
    timezone = 'Europe/Paris' # str | determine what the current time is. If you live in Brazil, \"today\" will be hours apart from Paris. Use your timezone to get results relative to your location. (optional) (default to 'Europe/Paris')

    try:
        # Almanax Range
        api_response = api_instance.get_almanax_range(language, filter_bonus_type=filter_bonus_type, range_from=range_from, range_to=range_to, range_size=range_size, timezone=timezone)
        print("The response of AlmanaxApi->get_almanax_range:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlmanaxApi->get_almanax_range: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**| code | 
 **filter_bonus_type** | **str**| ids from meta/{language}/almanax/bonuses | [optional] 
 **range_from** | **date**| yyyy-mm-dd | [optional] 
 **range_to** | **date**| yyyy-mm-dd | [optional] 
 **range_size** | **int**| size of the returned range | [optional] 
 **timezone** | **str**| determine what the current time is. If you live in Brazil, \&quot;today\&quot; will be hours apart from Paris. Use your timezone to get results relative to your location. | [optional] [default to &#39;Europe/Paris&#39;]

### Return type

[**List[Almanax]**](Almanax.md)

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

