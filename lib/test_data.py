"""
Various lists and dictionaries used for testing purposes
"""

ENDPOINTS = ["pokemon", "ability", "item", "move", "type", "berry", "evolution-chain"]

POKEMON_TEST_CASES = [
    {"id": 1, "name": "bulbasaur"},
    {"id": 4, "name": "charmander"},
    {"id": 39, "name": "jigglypuff"},
    {"id": 25, "name": "pikachu"},
    {"id": 133, "name": "eevee"},
    {"id": 135, "name": "jolteon"},
    {"id": 435, "name": "skuntank"},
]


def generate_evolution_chain(chain_id, chain, baby_trigger_item=None):
    """Set the evolution_chain object"""
    return {
        "id": chain_id,
        "chain": chain,
        "baby_trigger_item": baby_trigger_item,
    }


def generate_chain_link(species_name, evolution_details, evolves_to, is_baby=False):
    """Set the chain_link field in the evolution_chain"""
    if evolves_to is None:
        evolves_to = []
    return {
        "species_name": species_name,
        "evolution_details": evolution_details,
        "evolves_to": evolves_to,  # ChainLink
        "is_baby": is_baby,
    }


def generate_evolution_details(details):
    """Set the evolution_details field in the chain_link object"""
    return {
        "item": details.get("item"),
        "gender": details.get("gender"),
        "held_item": details.get("held_item"),
        "known_move": details.get("known_move"),
        "known_move_type": details.get("known_move_type"),
        "location": details.get("location"),
        "min_level": details.get("min_level"),
        "min_happiness": details.get("min_happiness"),
        "min_beauty": details.get("min_beauty"),
        "min_affection": details.get("min_affection"),
        "needs_overworld_rain": details.get("needs_overworld_rain"),
        "party_species": details.get("party_species"),
        "party_type": details.get("party_type"),
        "relative_physical_stats": details.get("relative_physical_stats"),
        "time_of_day": details.get("time_of_day"),
        "trade_species": details.get("trade_species"),
        "turn_upside_down": details.get("turn_upside_down"),
        "trigger_name": details.get("trigger_name"),
    }


# fmt: off
EVOLUTION_CHAIN_TEST_CASES = [
    # Bulbasaur chain
    generate_evolution_chain(
        1,
        generate_chain_link(
            "bulbasaur",
            None,
            generate_chain_link(
                "ivysaur",
                generate_evolution_details({
                    "min_level": 16,
                    "trigger_name": "level-up"
                }),
                generate_chain_link(
                    "venusaur",
                    generate_evolution_details({
                        "min_level": 32,
                        "trigger_name": "level-up"
                    }),
                    None
                )
            )
        )
    ),
    # Pichu chain: notable for having is_baby = true
    generate_evolution_chain(
        10,
        generate_chain_link(
            "pichu",
            None,
            generate_chain_link(
                "pikachu",
                generate_evolution_details({
                    "min_happiness": 220,
                    "trigger_name": "level-up"
                }),
                generate_chain_link(
                    "raichu",
                    generate_evolution_details({
                        "item": "thunder-stone",
                        "trigger_name": "use-item"
                    }),
                    None
                )
            ),
            True
        )
    ),
    # Oddish evolution chain: notable for having a branched evolution chain
    generate_evolution_chain(
        18,
        generate_chain_link(
            "oddish",
            None,
            generate_chain_link(
                "gloom",
                generate_evolution_details({
                    "min_level": 21,
                    "trigger_name": "level-up"
                }),
                [
                    generate_chain_link(
                        "vileplume",
                        generate_evolution_details({
                            "item": "leaf-stone",
                            "trigger_name": "use-item"
                        }),
                        None
                    ),
                    generate_chain_link(
                        "bellossom",
                        generate_evolution_details({
                            "item": "sun-stone",
                            "trigger_name": "use-item"
                        }),
                        None
                    )
                ]
            )
        )
    ),
    # Pinsir chain: notable for having no evolutions
    generate_evolution_chain(
        62,
        generate_chain_link(
            "pinsir",
            None,
            None
        )
    )
]
# fmt: on
