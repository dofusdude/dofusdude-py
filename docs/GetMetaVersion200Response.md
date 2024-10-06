# GetMetaVersion200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**release** | **str** |  | [optional] 
**update_stamp** | **str** |  | [optional] 

## Example

```python
from dofusdude.models.get_meta_version200_response import GetMetaVersion200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetaVersion200Response from a JSON string
get_meta_version200_response_instance = GetMetaVersion200Response.from_json(json)
# print the JSON string representation of the object
print(GetMetaVersion200Response.to_json())

# convert the object into a dict
get_meta_version200_response_dict = get_meta_version200_response_instance.to_dict()
# create an instance of GetMetaVersion200Response from a dict
get_meta_version200_response_from_dict = GetMetaVersion200Response.from_dict(get_meta_version200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


