# ConditionLeaf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_operand** | **bool** | always \&quot;true\&quot; for the leaf of a tree | [optional] [default to True]
**condition** | [**Condition**](Condition.md) |  | [optional] 

## Example

```python
from dofusdude.models.condition_leaf import ConditionLeaf

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionLeaf from a JSON string
condition_leaf_instance = ConditionLeaf.from_json(json)
# print the JSON string representation of the object
print(ConditionLeaf.to_json())

# convert the object into a dict
condition_leaf_dict = condition_leaf_instance.to_dict()
# create an instance of ConditionLeaf from a dict
condition_leaf_from_dict = ConditionLeaf.from_dict(condition_leaf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


