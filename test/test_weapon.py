# coding: utf-8

"""
    dofusdude

    # A project for you - the developer. The all-in-one toolbelt for your next Ankama related project.  ## Client SDKs - [Javascript](https://github.com/dofusdude/dofusdude-js) `npm i dofusdude-js --save` - [Typescript](https://github.com/dofusdude/dofusdude-ts) `npm i dofusdude-ts --save` - [Go](https://github.com/dofusdude/dodugo) `go get -u github.com/dofusdude/dodugo` - [Python](https://github.com/dofusdude/dofusdude-py) `pip install dofusdude` - [PHP](https://github.com/dofusdude/dofusdude-php) - [Java](https://github.com/dofusdude/dofusdude-java) Maven with GitHub packages setup  Everything, including this site, is generated out of the [Docs Repo](https://github.com/dofusdude/api-docs). Consider it the Single Source of Truth. If there is a problem with the SDKs, create an issue there.  Your favorite language is missing? Please let me know!  # Main Features - 🥷 **Seamless Auto-Update** load data in the background when a new Dofus version is released and serving it within 10 minutes with atomic data source switching. No downtime and no effects for the user, just always up-to-date.  - ⚡ **Blazingly Fast** all data in-memory, aggressive caching over short time spans, HTTP/2 multiplexing, written in Go, optimized for low latency, hosted on bare metal in 🇩🇪.  - 📨 **Discord Integration** Ankama related RSS and Almanax feeds to post to Discord servers with advanced features like filters or mentions. Use the endpoints as a dev or the official [Web Client](https://discord.dofusdude.com) as a user.  - 🩸 **Dofus 2 Beta** from stable to bleeding edge by replacing /dofus2 with /dofus2beta.  - 🗣️ **Multilingual** supporting _en_, _fr_, _es_, _pt_ including the dropped languages from the Dofus website _de_ and _it_.  - 🧠 **Search by Relevance** allowing typos in name and description, handled by language specific text analysis and indexing.  - 🕵️ **Complete** actual data from the game including items invisible to the encyclopedia like quest items.  - 🖼️ **HD Images** rendering game assets to high-res images with up to 800x800 px.  ... and much more on the Roadmap on my [Discord](https://discord.gg/3EtHskZD8h). 

    The version of the OpenAPI document: 0.9.4
    Contact: stelzo@steado.de
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dofusdude.models.weapon import Weapon

class TestWeapon(unittest.TestCase):
    """Weapon unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Weapon:
        """Test Weapon
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Weapon`
        """
        model = Weapon()
        if include_optional:
            return Weapon(
                ankama_id = 56,
                name = '',
                description = '',
                type = dofusdude.models.items_list_entry_typed_type.Items_List_Entry_Typed_type(
                    name = '', 
                    id = 56, ),
                is_weapon = True,
                level = 56,
                pods = 56,
                image_urls = dofusdude.models.image_urls.Image-Urls(
                    icon = '', 
                    sd = '', 
                    hq = '', 
                    hd = '', ),
                effects = [
                    dofusdude.models.effects_entry.Effects-Entry(
                        int_minimum = 56, 
                        int_maximum = 56, 
                        type = dofusdude.models.set_effects_entry_type.Set_Effects_Entry_type(
                            name = '', 
                            id = 56, 
                            is_meta = True, 
                            is_active = True, ), 
                        ignore_int_min = True, 
                        ignore_int_max = True, 
                        formatted = '', )
                    ],
                conditions = [
                    dofusdude.models.condition_entry.Condition-Entry(
                        operator = '', 
                        int_value = 56, 
                        element = dofusdude.models.items_list_entry_typed_type.Items_List_Entry_Typed_type(
                            name = '', 
                            id = 56, ), )
                    ],
                condition_tree = None,
                critical_hit_probability = 56,
                critical_hit_bonus = 56,
                is_two_handed = True,
                max_cast_per_turn = 56,
                ap_cost = 56,
                range = dofusdude.models.weapon_range.Weapon_range(
                    min = 56, 
                    max = 56, ),
                recipe = [
                    dofusdude.models.recipe_entry.Recipe-Entry(
                        item_ankama_id = 56, 
                        item_subtype = '', 
                        quantity = 56, )
                    ],
                parent_set = dofusdude.models.item_list_entry_parent_set.Item_List_Entry_parent_set(
                    id = 56, 
                    name = '', )
            )
        else:
            return Weapon(
        )
        """

    def testWeapon(self):
        """Test Weapon"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
