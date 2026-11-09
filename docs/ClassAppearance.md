# ClassAppearance

Structured client appearance data for an asset renderer. Bone and skin IDs are not image URLs. Use the parent record's image_urls for ready-to-display artwork.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bones_id** | **int** |  | 
**skin_ids** | **List[int]** |  | 
**scale_percent** | [**ClassAppearanceScalePercent**](ClassAppearanceScalePercent.md) |  | 
**default_colors** | **List[int]** |  | 

## Example

```python
from dofusdude.models.class_appearance import ClassAppearance

# TODO update the JSON string below
json = "{}"
# create an instance of ClassAppearance from a JSON string
class_appearance_instance = ClassAppearance.from_json(json)
# print the JSON string representation of the object
print(ClassAppearance.to_json())

# convert the object into a dict
class_appearance_dict = class_appearance_instance.to_dict()
# create an instance of ClassAppearance from a dict
class_appearance_from_dict = ClassAppearance.from_dict(class_appearance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


