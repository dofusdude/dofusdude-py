# TargetMask

Determines who an effect may affect. Combine the resolved selectors and conditions using logic. This is distinct from the zone geometry and from the event that triggers the effect.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**raw** | **str** | Original game mask retained for lossless debugging. | 
**logic** | **str** |  | [optional] 
**conditions** | [**List[CombatCondition]**](CombatCondition.md) |  | [optional] 
**selectors** | [**List[TargetSelector]**](TargetSelector.md) |  | 

## Example

```python
from dofusdude.models.target_mask import TargetMask

# TODO update the JSON string below
json = "{}"
# create an instance of TargetMask from a JSON string
target_mask_instance = TargetMask.from_json(json)
# print the JSON string representation of the object
print(TargetMask.to_json())

# convert the object into a dict
target_mask_dict = target_mask_instance.to_dict()
# create an instance of TargetMask from a dict
target_mask_from_dict = TargetMask.from_dict(target_mask_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


