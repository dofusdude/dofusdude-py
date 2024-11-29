# Error


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | HTTP status code | [optional] 
**error** | **str** | HTTP status as text | [optional] 
**code** | **str** | API specific error identifier for switch-case handling | [optional] 
**message** | **str** | General, human-friendly error description | [optional] 
**details** | **str** | Detailed, human-friendly problem description adopting specific inputs of the request | [optional] 

## Example

```python
from dofusdude.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print(Error.to_json())

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_from_dict = Error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


