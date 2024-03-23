# RecipeEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**item_ankama_id** | **int** |  | [optional] 
**item_subtype** | **str** |  | [optional] 
**quantity** | **int** |  | [optional] 

## Example

```python
from dofusdude.models.recipe_entry import RecipeEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RecipeEntry from a JSON string
recipe_entry_instance = RecipeEntry.from_json(json)
# print the JSON string representation of the object
print(RecipeEntry.to_json())

# convert the object into a dict
recipe_entry_dict = recipe_entry_instance.to_dict()
# create an instance of RecipeEntry from a dict
recipe_entry_form_dict = recipe_entry.from_dict(recipe_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


