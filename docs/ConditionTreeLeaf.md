# ConditionTreeLeaf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_operand** | **bool** | always \&quot;true\&quot; for the leaf of a tree | [optional] [default to True]
**condition** | [**ConditionEntry**](ConditionEntry.md) |  | [optional] 

## Example

```python
from dofusdude.models.condition_tree_leaf import ConditionTreeLeaf

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionTreeLeaf from a JSON string
condition_tree_leaf_instance = ConditionTreeLeaf.from_json(json)
# print the JSON string representation of the object
print(ConditionTreeLeaf.to_json())

# convert the object into a dict
condition_tree_leaf_dict = condition_tree_leaf_instance.to_dict()
# create an instance of ConditionTreeLeaf from a dict
condition_tree_leaf_from_dict = ConditionTreeLeaf.from_dict(condition_tree_leaf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


