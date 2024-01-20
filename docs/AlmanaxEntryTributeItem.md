# AlmanaxEntryTributeItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**image_urls** | [**ImageUrls**](ImageUrls.md) |  | [optional] 
**name** | **str** |  | [optional] 
**subtype** | **str** |  | [optional] 

## Example

```python
from dofusdude.models.almanax_entry_tribute_item import AlmanaxEntryTributeItem

# TODO update the JSON string below
json = "{}"
# create an instance of AlmanaxEntryTributeItem from a JSON string
almanax_entry_tribute_item_instance = AlmanaxEntryTributeItem.from_json(json)
# print the JSON string representation of the object
print AlmanaxEntryTributeItem.to_json()

# convert the object into a dict
almanax_entry_tribute_item_dict = almanax_entry_tribute_item_instance.to_dict()
# create an instance of AlmanaxEntryTributeItem from a dict
almanax_entry_tribute_item_form_dict = almanax_entry_tribute_item.from_dict(almanax_entry_tribute_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


