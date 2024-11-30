# coding: utf-8

"""
    dofusdude

    # Open Ankama Developer Community The all-in-one toolbelt for your next Ankama related project.  ## Versions - [Dofus 2](https://docs.dofusdu.de/dofus2/) - [Dofus 3](https://docs.dofusdu.de/dofus3/)   - v1 [latest] (you are here)   ## Client SDKs - [Javascript](https://github.com/dofusdude/dofusdude-js) `npm i dofusdude-js --save` - [Typescript](https://github.com/dofusdude/dofusdude-ts) `npm i dofusdude-ts --save` - [Go](https://github.com/dofusdude/dodugo) `go get -u github.com/dofusdude/dodugo` - [Python](https://github.com/dofusdude/dofusdude-py) `pip install dofusdude` - [Java](https://github.com/dofusdude/dofusdude-java) Maven with GitHub packages setup  Everything, including this site, is generated out of the [Docs Repo](https://github.com/dofusdude/api-docs). Consider it the Single Source of Truth. If there is a problem with the SDKs, create an issue there.  Your favorite language is missing? Please let me know!  # Main Features - 🥷 **Seamless Auto-Update** load data in the background when a new Dofus version is released and serving it within 10 minutes with atomic data source switching. No downtime and no effects for the user, just always up-to-date.  - ⚡ **Blazingly Fast** all data in-memory, aggressive caching over short time spans, HTTP/2 multiplexing, written in Go, optimized for low latency, hosted on bare metal in 🇩🇪.  - 📨 **Almanax Discord Integration** Use the endpoints as a dev or the official [Web Client](https://discord.dofusdude.com) as a user.  - 🩸 **Dofus 3 Beta** from stable to bleeding edge by replacing /dofus3 with /dofus3beta.  - 🗣️ **Multilingual** supporting _en_, _fr_, _es_, _pt_, _de_.  - 🧠 **Search by Relevance** allowing typos in name and description, handled by language specific text analysis and indexing.  - 🕵️ **Official Sources** generated from actual data from the game.  ... and much more on the Roadmap on my [Discord](https://discord.gg/3EtHskZD8h). 

    The version of the OpenAPI document: 1.0.0-rc.4
    Contact: stelzo@steado.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class TwitterWebhook(BaseModel):
    """
    TwitterWebhook
    """ # noqa: E501
    id: Optional[StrictStr] = None
    whitelist: Optional[List[StrictStr]] = None
    blacklist: Optional[List[StrictStr]] = None
    subscriptions: Optional[List[StrictStr]] = None
    format: Optional[StrictStr] = None
    preview_length: Optional[Annotated[int, Field(le=280, strict=True, ge=0)]] = None
    created_at: Optional[datetime] = None
    last_fired_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    __properties: ClassVar[List[str]] = ["id", "whitelist", "blacklist", "subscriptions", "format", "preview_length", "created_at", "last_fired_at", "updated_at"]

    @field_validator('format')
    def format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['discord']):
            raise ValueError("must be one of enum values ('discord')")
        return value

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
        """Create an instance of TwitterWebhook from a JSON string"""
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
        # set to None if whitelist (nullable) is None
        # and model_fields_set contains the field
        if self.whitelist is None and "whitelist" in self.model_fields_set:
            _dict['whitelist'] = None

        # set to None if blacklist (nullable) is None
        # and model_fields_set contains the field
        if self.blacklist is None and "blacklist" in self.model_fields_set:
            _dict['blacklist'] = None

        # set to None if last_fired_at (nullable) is None
        # and model_fields_set contains the field
        if self.last_fired_at is None and "last_fired_at" in self.model_fields_set:
            _dict['last_fired_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TwitterWebhook from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "whitelist": obj.get("whitelist"),
            "blacklist": obj.get("blacklist"),
            "subscriptions": obj.get("subscriptions"),
            "format": obj.get("format"),
            "preview_length": obj.get("preview_length"),
            "created_at": obj.get("created_at"),
            "last_fired_at": obj.get("last_fired_at"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


