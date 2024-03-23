# ItemsListPaged


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**LinksPaged**](LinksPaged.md) |  | [optional] 
**items** | [**List[ItemListEntry]**](ItemListEntry.md) |  | [optional] 

## Example

```python
from dofusdude.models.items_list_paged import ItemsListPaged

# TODO update the JSON string below
json = "{}"
# create an instance of ItemsListPaged from a JSON string
items_list_paged_instance = ItemsListPaged.from_json(json)
# print the JSON string representation of the object
print(ItemsListPaged.to_json())

# convert the object into a dict
items_list_paged_dict = items_list_paged_instance.to_dict()
# create an instance of ItemsListPaged from a dict
items_list_paged_form_dict = items_list_paged.from_dict(items_list_paged_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


