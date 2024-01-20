# ItemListEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**ItemsListEntryTypedType**](ItemsListEntryTypedType.md) |  | [optional] 
**level** | **int** |  | [optional] 
**image_urls** | [**ImageUrls**](ImageUrls.md) |  | [optional] 
**recipe** | [**List[RecipeEntry]**](RecipeEntry.md) |  | [optional] 

## Example

```python
from dofusdude.models.item_list_entry import ItemListEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ItemListEntry from a JSON string
item_list_entry_instance = ItemListEntry.from_json(json)
# print the JSON string representation of the object
print ItemListEntry.to_json()

# convert the object into a dict
item_list_entry_dict = item_list_entry_instance.to_dict()
# create an instance of ItemListEntry from a dict
item_list_entry_form_dict = item_list_entry.from_dict(item_list_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


