from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

factions = [

("no_faction", "No_Faction", 0, 0.900000, [], [], 0xAAAAAA),
("commoners", "Commoners", 0, 0.100000, [("outlaws", -0.600000), ("player_faction", 0.100000), ("mountain_bandits", -0.200000), ("forest_bandits", -0.200000), ("undeads", -0.700000)], [], 0xAAAAAA),
("outlaws", "Outlaws", max_player_rating(-30), 0.500000, [("commoners", -0.600000), ("innocents", -0.050000), ("merchants", -0.500000), ("player_faction", -0.150000), ("player_supporters_faction", -0.050000), ("kingdom_1", -0.050000), ("kingdom_2", -0.050000), ("kingdom_3", -0.050000), ("kingdom_4", -0.050000), ("kingdom_5", -0.050000), ("kingdom_6", -0.050000), ("kingdom_7", -0.050000), ("kingdom_8", -0.050000), ("kingdom_9", -0.050000), ("kingdom_10", -0.050000), ("kingdom_11", -0.050000), ("kingdom_12", -0.050000), ("kingdom_13", -0.050000), ("kingdom_14", -0.050000), ("kingdom_15", -0.050000), ("kingdom_16", -0.050000), ("kingdom_17", -0.050000), ("kingdom_18", -0.050000), ("kingdom_19", -0.050000), ("kingdom_20", -0.050000), ("papacy", -0.050000), ("kingdom_22", -0.050000), ("kingdom_23", -0.050000), ("kingdom_24", -0.050000), ("kingdom_25", -0.050000), ("kingdom_26", -0.050000), ("kingdom_27", -0.050000), ("kingdom_28", -0.050000), ("kingdom_29", -0.050000), ("kingdom_30", -0.050000), ("kingdom_31", -0.050000), ("kingdom_32", -0.050000), ("kingdom_33", -0.050000), ("kingdom_34", -0.050000), ("kingdom_35", -0.050000), ("kingdom_36", -0.050000), ("kingdom_37", -0.050000), ("kingdom_38", -0.050000), ("kingdom_39", -0.050000), ("kingdom_40", -0.050000), ("kingdom_41", -0.050000), ("kingdom_42", -0.050000), ("manhunters", -0.600000), ("crusade", -0.050000)], [], 0x888888),
("neutral", "Neutral", 0, 0.100000, [], [], 0xFFFFFF),
("innocents", "Innocents", ff_always_hide_label, 0.500000, [("outlaws", -0.050000), ("dark_knights", -0.900000)], [], 0xAAAAAA),
("merchants", "Merchants", ff_always_hide_label, 0.500000, [("outlaws", -0.500000), ("deserters", -0.500000), ("mountain_bandits", -0.500000), ("forest_bandits", -0.500000)], [], 0xAAAAAA),
("dark_knights", "{!}Dark_Knights", 0, 0.500000, [("innocents", -0.900000), ("player_faction", -0.400000)], [], 0xAAAAAA),
("culture_finnish", "{!}culture_finnish", 0, 0.900000, [], [], 0xAAAAAA),
("culture_mazovian", "{!}culture_mazovian", 0, 0.900000, [], [], 0xAAAAAA),
("culture_serbian", "{!}culture_serbian", 0, 0.900000, [], [], 0xAAAAAA),
("culture_welsh", "{!}culture_welsh", 0, 0.900000, [], [], 0xAAAAAA),
("culture_teutonic", "{!}culture_teutonic", 0, 0.900000, [], [], 0xAAAAAA),
("culture_balkan", "{!}culture_balkan", 0, 0.900000, [], [], 0xAAAAAA),
("culture_rus", "{!}culture_rus", 0, 0.900000, [], [], 0xAAAAAA),
("culture_nordic", "{!}culture_nordic", 0, 0.900000, [], [], 0xAAAAAA),
("culture_baltic", "{!}culture_baltic", 0, 0.900000, [], [], 0xAAAAAA),
("culture_marinid", "{!}culture_marinid", 0, 0.900000, [], [], 0xAAAAAA),
("culture_mamluke", "{!}culture_mamluke", 0, 0.900000, [], [], 0xAAAAAA),
("culture_byzantium", "{!}culture_byzantium", 0, 0.900000, [], [], 0xAAAAAA),
("culture_iberian", "{!}culture_iberian", 0, 0.900000, [], [], 0xAAAAAA),
("culture_italian", "{!}culture_italian", 0, 0.900000, [], [], 0xAAAAAA),
("culture_andalus", "{!}culture_andalus", 0, 0.900000, [], [], 0xAAAAAA),
("culture_gaelic", "{!}culture_gaelic", 0, 0.900000, [], [], 0xAAAAAA),
("culture_anatolian_christian", "{!}culture_anatolian", 0, 0.900000, [], [], 0xAAAAAA),
("culture_anatolian", "{!}culture_anatolian", 0, 0.900000, [], [], 0xAAAAAA),
("culture_scotish", "{!}culture_scotish", 0, 0.900000, [], [], 0xAAAAAA),
("culture_western", "{!}culture_western", 0, 0.900000, [], [], 0xAAAAAA),
("culture_mongol", "{!}culture_mongol", 0, 0.900000, [], [], 0xAAAAAA),
("player_faction", "Player_Faction", 0, 0.900000, [("commoners", 0.100000), ("outlaws", -0.150000), ("dark_knights", -0.400000), ("player_supporters_faction", 1.000000), ("black_khergits", -0.300000), ("manhunters", 0.100000), ("deserters", -0.100000), ("mountain_bandits", -0.150000), ("forest_bandits", -0.150000), ("undeads", -0.500000), ("peasant_rebels", -0.400000)], [], 0xCCCCCC),
("player_supporters_faction", "Player's_Supporters", 0, 0.900000, [("outlaws", -0.050000), ("player_faction", 1.000000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0x468493),
("kingdom_1", "Ordo_Teutonicus", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_4", 0.100000), ("kingdom_6", 0.500000), ("kingdom_8", -0.200000), ("kingdom_14", 0.100000), ("black_khergits", -0.020000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0xE9E9E9),
("kingdom_2", "Regnum_Litus", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_3", 0.100000), ("kingdom_33", 0.500000), ("kingdom_34", 0.500000), ("kingdom_35", 0.500000), ("kingdom_36", 0.500000), ("black_khergits", -0.020000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000), ("crusade", -0.500000)], [], 0xBADEB2),
("kingdom_3", "Altan_Ordyn_Uls", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_2", 0.100000), ("kingdom_5", -1.000000), ("kingdom_7", -1.000000), ("kingdom_8", 0.100000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000), ("crusade", -0.500000)], [], 0xA33E32),
("kingdom_4", "Regnum_Daniae", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_1", 0.100000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0x9B1A1A),
("kingdom_5", "Regnum_Poloniae", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_3", -1.000000), ("kingdom_7", 0.100000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0xFF0000),
("kingdom_6", "Sacrum_Imperium_Romanum", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_1", 0.500000), ("kingdom_38", 0.500000), ("kingdom_41", 1.000000), ("kingdom_42", 1.000000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0xFFCC00),
("kingdom_7", "Regnum_Hungariae", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_3", -1.000000), ("kingdom_5", 0.100000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0x289327),
("kingdom_8", "Novgorod_Weliki", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_1", -0.200000), ("kingdom_3", 0.100000), ("kingdom_14", -0.200000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0x9E0B6F),
("kingdom_9", "Regnum_Angliae", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_37", -1.000000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0x931124),
("kingdom_10", "Regnum_Franciae", 0, 0.900000, [("outlaws", -0.050000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0x002395),
("kingdom_11", "Kongeriket_Norge", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_12", -0.200000), ("kingdom_13", -0.200000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0x6669D6),
("kingdom_12", "Regnum_Scotiae", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_11", -0.200000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0x22D8A7),
("kingdom_13", "Scotia_Maior", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_11", -0.200000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0x77B322),
("kingdom_14", "Konungariket_Sverige", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_1", 0.100000), ("kingdom_8", -0.200000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0x3254B5),
("kingdom_15", "Regnum_Galiciae_et_Lodomeriae", 0, 0.900000, [("outlaws", -0.050000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0xECE874),
("kingdom_16", "Regnum_Portugaliae", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_20", -40.000000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0x003399),
("kingdom_17", "Corona_Aragonae", 0, 0.900000, [("outlaws", -0.050000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0x07B233),
("kingdom_18", "Regnum_Castiliae", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_20", -40.000000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0xD85AC4),
("kingdom_19", "Regnum_Navarrae", 0, 0.900000, [("outlaws", -0.050000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0xF7F497),
("kingdom_20", "Imarat_al_Nasri", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_16", -40.000000), ("kingdom_18", -40.000000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000), ("crusade", -0.500000)], [], 0xABC904),
("papacy", "Patrimonium_Sancti_Petri", 0, 0.900000, [("outlaws", -0.050000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000), ("crusade", -0.500000)], [], 0xFFF17A),
("kingdom_22", "Basileia_ton_Rhomaion", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_26", -1.000000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0x760D0D),
("kingdom_23", "Regnum_Hierosolymitanum", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_25", -1.000000), ("kingdom_27", 0.100000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0xF3EFB8),
("kingdom_24", "Regnum_Siciliae", 0, 0.900000, [("outlaws", -0.050000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0x799CB5),
("kingdom_25", "Sultanat_al_Mamalik", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_23", -1.000000), ("kingdom_27", -1.000000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000), ("crusade", -0.500000)], [], 0xEBE800),
("kingdom_26", "Imperium_Romaniae", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_22", -1.000000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0xB26248),
("kingdom_27", "Ilkhanate", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_23", 0.100000), ("kingdom_25", -1.000000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000), ("crusade", -0.500000)], [], 0xE19004),
("kingdom_28", "Sultanat_al_Hafsi", 0, 0.900000, [("outlaws", -0.050000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000), ("crusade", -0.500000)], [], 0xA48460),
("kingdom_29", "Kraljevstvo_Srbsko", 0, 0.900000, [("outlaws", -0.050000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0xB38263),
("kingdom_30", "Balgarsko_Tsarstvo", 0, 0.900000, [("outlaws", -0.050000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0x76A296),
("kingdom_31", "Sultanat_al_Marini", 0, 0.900000, [("outlaws", -0.050000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000), ("crusade", -0.500000)], [], 0xC1272D),
("kingdom_32", "Repubblica_di_Venezia", 0, 0.900000, [("outlaws", -0.050000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0xC1172D),
("kingdom_33", "Jotvingiai", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_2", 0.500000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000), ("crusade", -0.500000)], [], 0x3E7583),
("kingdom_34", "Pruteni", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_2", 0.500000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000), ("crusade", -0.500000)], [], 0x65C0D7),
("kingdom_35", "Kursi", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_2", 0.500000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000), ("crusade", -0.500000)], [], 0x3E7583),
("kingdom_36", "Zemaiciai", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_2", 0.500000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000), ("crusade", -0.500000)], [], 0x529CAE),
("kingdom_37", "Cymry", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_9", -1.000000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0x00DC00),
("kingdom_38", "Respublica_Ianuensis", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_6", 0.500000), ("kingdom_39", -0.500000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000), ("crusade", -0.500000)], [], 0xE1900A),
("kingdom_39", "Respublica_Pisarum", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_38", -0.500000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0x07E233),
("kingdom_40", "Comuni_Guelfi", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_41", -0.800000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0x3254E5),
("kingdom_41", "Comuni_Ghibellini", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_6", 1.000000), ("kingdom_40", -0.800000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0x9E026A),
("kingdom_42", "??esk??_Kr??lovstv??", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_6", 1.000000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0xE8E8E8),
("kingdoms_end", "{!}kingdoms_end", 0, 0.000000, [], [], 0xAAAAAA),
("robber_knights", "{!}robber_knights", 0, 0.100000, [], [], 0xAAAAAA),
("khergits", "{!}Khergits", 0, 0.500000, [], [], 0xAAAAAA),
("black_khergits", "{!}Black_Khergits", 0, 0.500000, [("player_faction", -0.300000), ("kingdom_1", -0.020000), ("kingdom_2", -0.020000)], [], 0xAAAAAA),
("manhunters", "Captivos_Proscriptorum", 0, 0.500000, [("outlaws", -0.600000), ("player_faction", 0.100000), ("deserters", -0.600000), ("mountain_bandits", -0.600000), ("forest_bandits", -0.600000)], [], 0xAAAAAA),
("deserters", "Deserti", 0, 0.500000, [("merchants", -0.500000), ("player_faction", -0.100000), ("player_supporters_faction", -0.020000), ("kingdom_1", -0.020000), ("kingdom_2", -0.020000), ("kingdom_3", -0.020000), ("kingdom_4", -0.020000), ("kingdom_5", -0.020000), ("kingdom_6", -0.020000), ("kingdom_7", -0.020000), ("kingdom_8", -0.020000), ("kingdom_9", -0.020000), ("kingdom_10", -0.020000), ("kingdom_11", -0.020000), ("kingdom_12", -0.020000), ("kingdom_13", -0.020000), ("kingdom_14", -0.020000), ("kingdom_15", -0.020000), ("kingdom_16", -0.020000), ("kingdom_17", -0.020000), ("kingdom_18", -0.020000), ("kingdom_19", -0.020000), ("kingdom_20", -0.020000), ("papacy", -0.020000), ("kingdom_22", -0.020000), ("kingdom_23", -0.020000), ("kingdom_24", -0.020000), ("kingdom_25", -0.020000), ("kingdom_26", -0.020000), ("kingdom_27", -0.020000), ("kingdom_28", -0.020000), ("kingdom_29", -0.020000), ("kingdom_30", -0.020000), ("kingdom_31", -0.020000), ("kingdom_32", -0.020000), ("kingdom_33", -0.020000), ("kingdom_34", -0.020000), ("kingdom_35", -0.020000), ("kingdom_36", -0.020000), ("kingdom_37", -0.020000), ("kingdom_38", -0.020000), ("kingdom_39", -0.020000), ("kingdom_40", -0.020000), ("kingdom_41", -0.020000), ("kingdom_42", -0.020000), ("manhunters", -0.600000), ("crusade", -0.020000)], [], 0x888888),
("mountain_bandits", "Montes_Sicarii", 0, 0.500000, [("commoners", -0.200000), ("merchants", -0.500000), ("player_faction", -0.150000), ("player_supporters_faction", -0.050000), ("kingdom_1", -0.050000), ("kingdom_2", -0.050000), ("kingdom_3", -0.050000), ("kingdom_4", -0.050000), ("kingdom_5", -0.050000), ("kingdom_6", -0.050000), ("kingdom_7", -0.050000), ("kingdom_8", -0.050000), ("kingdom_9", -0.050000), ("kingdom_10", -0.050000), ("kingdom_11", -0.050000), ("kingdom_12", -0.050000), ("kingdom_13", -0.050000), ("kingdom_14", -0.050000), ("kingdom_15", -0.050000), ("kingdom_16", -0.050000), ("kingdom_17", -0.050000), ("kingdom_18", -0.050000), ("kingdom_19", -0.050000), ("kingdom_20", -0.050000), ("papacy", -0.050000), ("kingdom_22", -0.050000), ("kingdom_23", -0.050000), ("kingdom_24", -0.050000), ("kingdom_25", -0.050000), ("kingdom_26", -0.050000), ("kingdom_27", -0.050000), ("kingdom_28", -0.050000), ("kingdom_29", -0.050000), ("kingdom_30", -0.050000), ("kingdom_31", -0.050000), ("kingdom_32", -0.050000), ("kingdom_33", -0.050000), ("kingdom_34", -0.050000), ("kingdom_35", -0.050000), ("kingdom_36", -0.050000), ("kingdom_37", -0.050000), ("kingdom_38", -0.050000), ("kingdom_39", -0.050000), ("kingdom_40", -0.050000), ("kingdom_41", -0.050000), ("kingdom_42", -0.050000), ("manhunters", -0.600000), ("crusade", -0.050000)], [], 0x888888),
("forest_bandits", "Silvae_Sicarii", 0, 0.500000, [("commoners", -0.200000), ("merchants", -0.500000), ("player_faction", -0.150000), ("player_supporters_faction", -0.050000), ("kingdom_1", -0.050000), ("kingdom_2", -0.050000), ("kingdom_3", -0.050000), ("kingdom_4", -0.050000), ("kingdom_5", -0.050000), ("kingdom_6", -0.050000), ("kingdom_7", -0.050000), ("kingdom_8", -0.050000), ("kingdom_9", -0.050000), ("kingdom_10", -0.050000), ("kingdom_11", -0.050000), ("kingdom_12", -0.050000), ("kingdom_13", -0.050000), ("kingdom_14", -0.050000), ("kingdom_15", -0.050000), ("kingdom_16", -0.050000), ("kingdom_17", -0.050000), ("kingdom_18", -0.050000), ("kingdom_19", -0.050000), ("kingdom_20", -0.050000), ("papacy", -0.050000), ("kingdom_22", -0.050000), ("kingdom_23", -0.050000), ("kingdom_24", -0.050000), ("kingdom_25", -0.050000), ("kingdom_26", -0.050000), ("kingdom_27", -0.050000), ("kingdom_28", -0.050000), ("kingdom_29", -0.050000), ("kingdom_30", -0.050000), ("kingdom_31", -0.050000), ("kingdom_32", -0.050000), ("kingdom_33", -0.050000), ("kingdom_34", -0.050000), ("kingdom_35", -0.050000), ("kingdom_36", -0.050000), ("kingdom_37", -0.050000), ("kingdom_38", -0.050000), ("kingdom_39", -0.050000), ("kingdom_40", -0.050000), ("kingdom_41", -0.050000), ("kingdom_42", -0.050000), ("manhunters", -0.600000), ("crusade", -0.050000)], [], 0x888888),
("undeads", "{!}Undeads", max_player_rating(-30), 0.500000, [("commoners", -0.700000), ("player_faction", -0.500000)], [], 0xAAAAAA),
("slavers", "{!}Slavers", 0, 0.100000, [], [], 0xAAAAAA),
("peasant_rebels", "{!}Peasant_Rebels", 0, 1.000000, [("player_faction", -0.400000), ("player_supporters_faction", -0.100000), ("kingdom_1", -0.100000), ("kingdom_2", -0.100000), ("kingdom_3", -0.100000), ("kingdom_4", -0.100000), ("kingdom_5", -0.100000), ("kingdom_6", -0.100000), ("kingdom_7", -0.100000), ("kingdom_8", -0.100000), ("kingdom_9", -0.100000), ("kingdom_10", -0.100000), ("kingdom_11", -0.100000), ("kingdom_12", -0.100000), ("kingdom_13", -0.100000), ("kingdom_14", -0.100000), ("kingdom_15", -0.100000), ("kingdom_16", -0.100000), ("kingdom_17", -0.100000), ("kingdom_18", -0.100000), ("kingdom_19", -0.100000), ("kingdom_20", -0.100000), ("papacy", -0.100000), ("kingdom_22", -0.100000), ("kingdom_23", -0.100000), ("kingdom_24", -0.100000), ("kingdom_25", -0.100000), ("kingdom_26", -0.100000), ("kingdom_27", -0.100000), ("kingdom_28", -0.100000), ("kingdom_29", -0.100000), ("kingdom_30", -0.100000), ("kingdom_31", -0.100000), ("kingdom_32", -0.100000), ("kingdom_33", -0.100000), ("kingdom_34", -0.100000), ("kingdom_35", -0.100000), ("kingdom_36", -0.100000), ("kingdom_37", -0.100000), ("kingdom_38", -0.100000), ("kingdom_39", -0.100000), ("kingdom_40", -0.100000), ("kingdom_41", -0.100000), ("kingdom_42", -0.100000), ("noble_refugees", -1.000000), ("crusade", -0.100000)], [], 0xAAAAAA),
("noble_refugees", "{!}Noble_Refugees", 0, 0.500000, [("peasant_rebels", -1.000000)], [], 0xAAAAAA),
("crusade", "Crusaders", 0, 0.900000, [("outlaws", -0.050000), ("kingdom_2", -0.500000), ("kingdom_3", -0.500000), ("kingdom_20", -0.500000), ("papacy", -0.500000), ("kingdom_25", -0.500000), ("kingdom_27", -0.500000), ("kingdom_28", -0.500000), ("kingdom_31", -0.500000), ("kingdom_33", -0.500000), ("kingdom_34", -0.500000), ("kingdom_35", -0.500000), ("kingdom_36", -0.500000), ("kingdom_38", -0.500000), ("deserters", -0.020000), ("mountain_bandits", -0.050000), ("forest_bandits", -0.050000), ("peasant_rebels", -0.100000)], [], 0xFFF17A),
("end_minor_faction", "Village_Idiots", 0, 0.900000, [], [], 0xFFF17A),

]