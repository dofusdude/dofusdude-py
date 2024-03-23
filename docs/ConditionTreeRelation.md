# ConditionTreeRelation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_operand** | **bool** | always \&quot;false\&quot; for relations | [optional] [default to False]
**relation** | **str** | \&quot;and\&quot;, \&quot;or\&quot; | [optional] [default to 'and']
**children** | [**List[ConditionTreeNode]**](ConditionTreeNode.md) |  | [optional] 

## Example

```python
from dofusdude.models.condition_tree_relation import ConditionTreeRelation

# TODO update the JSON string below
json = "{}"
# create an instance of ConditionTreeRelation from a JSON string
condition_tree_relation_instance = ConditionTreeRelation.from_json(json)
# print the JSON string representation of the object
print(ConditionTreeRelation.to_json())

# convert the object into a dict
condition_tree_relation_dict = condition_tree_relation_instance.to_dict()
# create an instance of ConditionTreeRelation from a dict
condition_tree_relation_form_dict = condition_tree_relation.from_dict(condition_tree_relation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


