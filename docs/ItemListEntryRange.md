# ItemListEntryRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** |  | [optional] 
**max** | **int** |  | [optional] 

## Example

```python
from dofusdude.models.item_list_entry_range import ItemListEntryRange

# TODO update the JSON string below
json = "{}"
# create an instance of ItemListEntryRange from a JSON string
item_list_entry_range_instance = ItemListEntryRange.from_json(json)
# print the JSON string representation of the object
print(ItemListEntryRange.to_json())

# convert the object into a dict
item_list_entry_range_dict = item_list_entry_range_instance.to_dict()
# create an instance of ItemListEntryRange from a dict
item_list_entry_range_from_dict = ItemListEntryRange.from_dict(item_list_entry_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


