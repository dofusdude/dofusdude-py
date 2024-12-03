# coding: utf-8

"""
    dofusdude

    # Open Ankama Developer Community The all-in-one toolbelt for your next Ankama related project.  ## Versions - [Dofus 2](https://docs.dofusdu.de/dofus2/) - [Dofus 3](https://docs.dofusdu.de/dofus3/)   - v1 [latest] (you are here)   ## Client SDKs - [Javascript](https://github.com/dofusdude/dofusdude-js) `npm i dofusdude-js --save` - [Typescript](https://github.com/dofusdude/dofusdude-ts) `npm i dofusdude-ts --save` - [Go](https://github.com/dofusdude/dodugo) `go get -u github.com/dofusdude/dodugo` - [Python](https://github.com/dofusdude/dofusdude-py) `pip install dofusdude` - [Java](https://github.com/dofusdude/dofusdude-java) Maven with GitHub packages setup  Everything, including this site, is generated out of the [Docs Repo](https://github.com/dofusdude/api-docs). Consider it the Single Source of Truth. If there is a problem with the SDKs, create an issue there.  Your favorite language is missing? Please let me know!  # Main Features - 🥷 **Seamless Auto-Update** load data in the background when a new Dofus version is released and serving it within 10 minutes with atomic data source switching. No downtime and no effects for the user, just always up-to-date.  - ⚡ **Blazingly Fast** all data in-memory, aggressive caching over short time spans, HTTP/2 multiplexing, written in Go, optimized for low latency, hosted on bare metal in 🇩🇪.  - 📨 **Almanax Discord Integration** Use the endpoints as a dev or the official [Web Client](https://discord.dofusdude.com) as a user.  - 🩸 **Dofus 3 Beta** from stable to bleeding edge by replacing /dofus3 with /dofus3beta.  - 🗣️ **Multilingual** supporting _en_, _fr_, _es_, _pt_, _de_.  - 🧠 **Search by Relevance** allowing typos in name and description, handled by language specific text analysis and indexing.  - 🕵️ **Official Sources** generated from actual data from the game.  ... and much more on the Roadmap on my [Discord](https://discord.gg/3EtHskZD8h). 

    The version of the OpenAPI document: 1.0.0-rc.8
    Contact: stelzo@steado.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from dofusdude.models.effect import Effect
from typing import Optional, Set
from typing_extensions import Self

class ListEquipmentSet(BaseModel):
    """
    ListEquipmentSet
    """ # noqa: E501
    ankama_id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    items: Optional[StrictInt] = Field(default=None, description="amount")
    level: Optional[StrictInt] = None
    effects: Optional[Dict[str, Annotated[List[Effect], Field(min_length=0)]]] = None
    equipment_ids: Optional[List[StrictInt]] = None
    contains_cosmetics: Optional[StrictBool] = None
    contains_cosmetics_only: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["ankama_id", "name", "items", "level", "effects", "equipment_ids", "contains_cosmetics", "contains_cosmetics_only"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ListEquipmentSet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each value in effects (dict of array)
        _field_dict_of_array = {}
        if self.effects:
            for _key_effects in self.effects:
                if self.effects[_key_effects] is not None:
                    _field_dict_of_array[_key_effects] = [
                        _item.to_dict() for _item in self.effects[_key_effects]
                    ]
            _dict['effects'] = _field_dict_of_array
        # set to None if equipment_ids (nullable) is None
        # and model_fields_set contains the field
        if self.equipment_ids is None and "equipment_ids" in self.model_fields_set:
            _dict['equipment_ids'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListEquipmentSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ankama_id": obj.get("ankama_id"),
            "name": obj.get("name"),
            "items": obj.get("items"),
            "level": obj.get("level"),
            "effects": dict(
                (_k,
                        [Effect.from_dict(_item) for _item in _v]
                        if _v is not None
                        else None
                )
                for _k, _v in obj.get("effects", {}).items()
            ),
            "equipment_ids": obj.get("equipment_ids"),
            "contains_cosmetics": obj.get("contains_cosmetics"),
            "contains_cosmetics_only": obj.get("contains_cosmetics_only")
        })
        return _obj


