# ListItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PagedLinks**](PagedLinks.md) |  | [optional] 
**items** | [**List[ListItem]**](ListItem.md) |  | [optional] 

## Example

```python
from dofusdude.models.list_items import ListItems

# TODO update the JSON string below
json = "{}"
# create an instance of ListItems from a JSON string
list_items_instance = ListItems.from_json(json)
# print the JSON string representation of the object
print(ListItems.to_json())

# convert the object into a dict
list_items_dict = list_items_instance.to_dict()
# create an instance of ListItems from a dict
list_items_from_dict = ListItems.from_dict(list_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


