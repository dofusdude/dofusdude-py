# Images

All images except icon are rendered in the background which can take some time (up to hours if all data is completely generated from scratch). Because of this, they can be null if they are not yet rendered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon** | **str** | 64x64 px, always available | [optional] 
**sd** | **str** | around 2x the resolution of icon | [optional] 
**hq** | **str** | around 2x the resolution of sd | [optional] 
**hd** | **str** | around 2x the resolution of hd | [optional] 

## Example

```python
from dofusdude.models.images import Images

# TODO update the JSON string below
json = "{}"
# create an instance of Images from a JSON string
images_instance = Images.from_json(json)
# print the JSON string representation of the object
print(Images.to_json())

# convert the object into a dict
images_dict = images_instance.to_dict()
# create an instance of Images from a dict
images_from_dict = Images.from_dict(images_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


