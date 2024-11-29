# MountFamily


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** | localized name | [optional] 

## Example

```python
from dofusdude.models.mount_family import MountFamily

# TODO update the JSON string below
json = "{}"
# create an instance of MountFamily from a JSON string
mount_family_instance = MountFamily.from_json(json)
# print the JSON string representation of the object
print(MountFamily.to_json())

# convert the object into a dict
mount_family_dict = mount_family_instance.to_dict()
# create an instance of MountFamily from a dict
mount_family_from_dict = MountFamily.from_dict(mount_family_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


