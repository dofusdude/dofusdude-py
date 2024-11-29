# AlmanaxTribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item** | [**AlmanaxTributeItem**](AlmanaxTributeItem.md) |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from dofusdude.models.almanax_tribute import AlmanaxTribute

# TODO update the JSON string below
json = "{}"
# create an instance of AlmanaxTribute from a JSON string
almanax_tribute_instance = AlmanaxTribute.from_json(json)
# print the JSON string representation of the object
print(AlmanaxTribute.to_json())

# convert the object into a dict
almanax_tribute_dict = almanax_tribute_instance.to_dict()
# create an instance of AlmanaxTribute from a dict
almanax_tribute_from_dict = AlmanaxTribute.from_dict(almanax_tribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


