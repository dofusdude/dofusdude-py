# Mount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ankama_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**family** | [**MountFamily**](MountFamily.md) |  | [optional] 
**image_urls** | [**Images**](Images.md) |  | [optional] 
**effects** | [**List[Effect]**](Effect.md) |  | [optional] 

## Example

```python
from dofusdude.models.mount import Mount

# TODO update the JSON string below
json = "{}"
# create an instance of Mount from a JSON string
mount_instance = Mount.from_json(json)
# print the JSON string representation of the object
print(Mount.to_json())

# convert the object into a dict
mount_dict = mount_instance.to_dict()
# create an instance of Mount from a dict
mount_from_dict = Mount.from_dict(mount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


