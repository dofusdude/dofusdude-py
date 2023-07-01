# MountListEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**family_name** | **str** |  | [optional] 
**image_urls** | [**ImageUrls**](ImageUrls.md) |  | [optional] 

## Example

```python
from dofusdude.models.mount_list_entry import MountListEntry

# TODO update the JSON string below
json = "{}"
# create an instance of MountListEntry from a JSON string
mount_list_entry_instance = MountListEntry.from_json(json)
# print the JSON string representation of the object
print MountListEntry.to_json()

# convert the object into a dict
mount_list_entry_dict = mount_list_entry_instance.to_dict()
# create an instance of MountListEntry from a dict
mount_list_entry_form_dict = mount_list_entry.from_dict(mount_list_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


