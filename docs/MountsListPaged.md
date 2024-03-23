# MountsListPaged


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**LinksPaged**](LinksPaged.md) |  | [optional] 
**items** | [**List[MountListEntry]**](MountListEntry.md) |  | [optional] 

## Example

```python
from dofusdude.models.mounts_list_paged import MountsListPaged

# TODO update the JSON string below
json = "{}"
# create an instance of MountsListPaged from a JSON string
mounts_list_paged_instance = MountsListPaged.from_json(json)
# print the JSON string representation of the object
print(MountsListPaged.to_json())

# convert the object into a dict
mounts_list_paged_dict = mounts_list_paged_instance.to_dict()
# create an instance of MountsListPaged from a dict
mounts_list_paged_form_dict = mounts_list_paged.from_dict(mounts_list_paged_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


