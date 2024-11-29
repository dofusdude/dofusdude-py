# AlmanaxTributeItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**image_urls** | [**Images**](Images.md) |  | [optional] 
**name** | **str** |  | [optional] 
**subtype** | **str** |  | [optional] 

## Example

```python
from dofusdude.models.almanax_tribute_item import AlmanaxTributeItem

# TODO update the JSON string below
json = "{}"
# create an instance of AlmanaxTributeItem from a JSON string
almanax_tribute_item_instance = AlmanaxTributeItem.from_json(json)
# print the JSON string representation of the object
print(AlmanaxTributeItem.to_json())

# convert the object into a dict
almanax_tribute_item_dict = almanax_tribute_item_instance.to_dict()
# create an instance of AlmanaxTributeItem from a dict
almanax_tribute_item_from_dict = AlmanaxTributeItem.from_dict(almanax_tribute_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


