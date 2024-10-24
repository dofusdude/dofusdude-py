# coding: utf-8

"""
    dofusdude

    # A project for you - the developer. The all-in-one toolbelt for your next Ankama related project.  ## Client SDKs - [Javascript](https://github.com/dofusdude/dofusdude-js) `npm i dofusdude-js --save` - [Typescript](https://github.com/dofusdude/dofusdude-ts) `npm i dofusdude-ts --save` - [Go](https://github.com/dofusdude/dodugo) `go get -u github.com/dofusdude/dodugo` - [Python](https://github.com/dofusdude/dofusdude-py) `pip install dofusdude` - [PHP](https://github.com/dofusdude/dofusdude-php) - [Java](https://github.com/dofusdude/dofusdude-java) Maven with GitHub packages setup  Everything, including this site, is generated out of the [Docs Repo](https://github.com/dofusdude/api-docs). Consider it the Single Source of Truth. If there is a problem with the SDKs, create an issue there.  Your favorite language is missing? Please let me know!  # Main Features - 🥷 **Seamless Auto-Update** load data in the background when a new Dofus version is released and serving it within 10 minutes with atomic data source switching. No downtime and no effects for the user, just always up-to-date.  - ⚡ **Blazingly Fast** all data in-memory, aggressive caching over short time spans, HTTP/2 multiplexing, written in Go, optimized for low latency, hosted on bare metal in 🇩🇪.  - 📨 **Discord Integration** Ankama related RSS and Almanax feeds to post to Discord servers with advanced features like filters or mentions. Use the endpoints as a dev or the official [Web Client](https://discord.dofusdude.com) as a user.  - 🩸 **Dofus 2 Beta** from stable to bleeding edge by replacing /dofus2 with /dofus2beta.  - 🗣️ **Multilingual** supporting _en_, _fr_, _es_, _pt_ including the dropped languages from the Dofus website _de_ and _it_.  - 🧠 **Search by Relevance** allowing typos in name and description, handled by language specific text analysis and indexing.  - 🕵️ **Complete** actual data from the game including items invisible to the encyclopedia like quest items.  - 🖼️ **HD Images** rendering game assets to high-res images with up to 800x800 px.  ... and much more on the Roadmap on my [Discord](https://discord.gg/3EtHskZD8h). 

    The version of the OpenAPI document: 0.9.4
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
from dofusdude.models.set_effects_entry import SetEffectsEntry
from typing import Optional, Set
from typing_extensions import Self

class SetListEntry(BaseModel):
    """
    SetListEntry
    """ # noqa: E501
    ankama_id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    items: Optional[StrictInt] = Field(default=None, description="amount")
    level: Optional[StrictInt] = None
    effects: Optional[List[List[SetEffectsEntry]]] = None
    equipment_ids: Optional[List[StrictInt]] = None
    is_cosmetic: Optional[StrictBool] = None
    __properties: ClassVar[List[str]] = ["ankama_id", "name", "items", "level", "effects", "equipment_ids", "is_cosmetic"]

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
        """Create an instance of SetListEntry from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in effects (list of list)
        _items = []
        if self.effects:
            for _item_effects in self.effects:
                if _item_effects:
                    _items.append(
                         [_inner_item.to_dict() for _inner_item in _item_effects if _inner_item is not None]
                    )
            _dict['effects'] = _items
        # set to None if effects (nullable) is None
        # and model_fields_set contains the field
        if self.effects is None and "effects" in self.model_fields_set:
            _dict['effects'] = None

        # set to None if equipment_ids (nullable) is None
        # and model_fields_set contains the field
        if self.equipment_ids is None and "equipment_ids" in self.model_fields_set:
            _dict['equipment_ids'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SetListEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ankama_id": obj.get("ankama_id"),
            "name": obj.get("name"),
            "items": obj.get("items"),
            "level": obj.get("level"),
            "effects": [
                    [SetEffectsEntry.from_dict(_inner_item) for _inner_item in _item]
                    for _item in obj["effects"]
                ] if obj.get("effects") is not None else None,
            "equipment_ids": obj.get("equipment_ids"),
            "is_cosmetic": obj.get("is_cosmetic")
        })
        return _obj


