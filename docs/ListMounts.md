# ListMounts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PagedLinks**](PagedLinks.md) |  | [optional] 
**items** | [**List[Mount]**](Mount.md) |  | [optional] 

## Example

```python
from dofusdude.models.list_mounts import ListMounts

# TODO update the JSON string below
json = "{}"
# create an instance of ListMounts from a JSON string
list_mounts_instance = ListMounts.from_json(json)
# print the JSON string representation of the object
print(ListMounts.to_json())

# convert the object into a dict
list_mounts_dict = list_mounts_instance.to_dict()
# create an instance of ListMounts from a dict
list_mounts_from_dict = ListMounts.from_dict(list_mounts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


