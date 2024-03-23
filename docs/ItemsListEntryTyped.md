# ItemsListEntryTyped


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**ItemsListEntryTypedType**](ItemsListEntryTypedType.md) |  | [optional] 
**item_subtype** | **str** | The API item category. Can be used to build the request URL for this particular item. Always english. | [optional] 
**level** | **int** |  | [optional] 
**image_urls** | [**ImageUrls**](ImageUrls.md) |  | [optional] 

## Example

```python
from dofusdude.models.items_list_entry_typed import ItemsListEntryTyped

# TODO update the JSON string below
json = "{}"
# create an instance of ItemsListEntryTyped from a JSON string
items_list_entry_typed_instance = ItemsListEntryTyped.from_json(json)
# print the JSON string representation of the object
print(ItemsListEntryTyped.to_json())

# convert the object into a dict
items_list_entry_typed_dict = items_list_entry_typed_instance.to_dict()
# create an instance of ItemsListEntryTyped from a dict
items_list_entry_typed_form_dict = items_list_entry_typed.from_dict(items_list_entry_typed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


