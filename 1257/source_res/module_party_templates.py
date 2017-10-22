from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################

party_templates = [

("none", "none", icon_gray_knight, 0, fac_commoners, aggressiveness_0|courage_7, []),
("rescued_prisoners", "Rescued Prisoners", icon_gray_knight, 0, fac_commoners, aggressiveness_0|courage_7, []),
("enemy", "Enemy", icon_gray_knight, 0, fac_undeads, aggressiveness_0|courage_7, []),
("hero_party", "Hero Party", icon_gray_knight, 0, fac_commoners, aggressiveness_0|courage_7, []),
("village_defenders", "Village Defenders", icon_peasant, 0, fac_commoners, aggressiveness_0|courage_7, [(trp_farmer, 10, 20, 0),(trp_peasant_woman, 0, 4, 0)]),
("cattle_herd", "Cattle Herd", icon_cattle|carries_goods(10), 0, fac_neutral, aggressiveness_0|courage_11, [(trp_cattle, 80, 120, 0)]),
("looters", "Fures", icon_axeman|carries_goods(8), 0, fac_outlaws, 312, [(trp_looter, 15, 50, 0)]),
("manhunters", "Manhunters", icon_gray_knight, 0, fac_manhunters, aggressiveness_8|aggressiveness_0|courage_9, [(trp_manhunter, 9, 40, 0)]),
("curonians", "Kursi", icon_axeman|carries_goods(2), 0, fac_kingdom_35, aggressiveness_8|aggressiveness_0|courage_9, [(trp_balt_skirmisher, 7, 10, 0),(trp_balt_footman, 7, 10, 0),(trp_balt_jav, 7, 10, 0),(trp_balt_veteran_jav, 1, 4, 0),(trp_balt_billman, 7, 10, 0),(trp_balt_spearman, 7, 10, 0)]),
("prussians", "Pruteni", icon_axeman|carries_goods(2), 0, fac_kingdom_34, aggressiveness_8|aggressiveness_0|courage_9, [(trp_balt_skirmisher, 7, 10, 0),(trp_balt_footman, 7, 10, 0),(trp_balt_jav, 7, 10, 0),(trp_balt_veteran_jav, 1, 4, 0),(trp_balt_billman, 7, 10, 0),(trp_balt_spearman, 7, 10, 0)]),
("samogitians", "Zemaiciai", icon_axeman|carries_goods(2), 0, fac_kingdom_36, aggressiveness_8|aggressiveness_0|courage_9, [(trp_balt_skirmisher, 7, 10, 0),(trp_balt_footman, 7, 10, 0),(trp_balt_jav, 7, 10, 0),(trp_balt_veteran_jav, 1, 4, 0),(trp_balt_billman, 7, 10, 0),(trp_balt_spearman, 7, 10, 0)]),
("yotvingians", "Jotvingiai", icon_axeman|carries_goods(2), 0, fac_kingdom_33, aggressiveness_8|aggressiveness_0|courage_9, [(trp_balt_skirmisher, 7, 10, 0),(trp_balt_footman, 7, 10, 0),(trp_balt_jav, 7, 10, 0),(trp_balt_veteran_jav, 1, 4, 0),(trp_balt_billman, 7, 10, 0),(trp_balt_spearman, 7, 10, 0)]),
("welsh", "Cymry", icon_axeman|carries_goods(2), 0, fac_kingdom_37, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_welsh_bowman, 24, 31, 0)]),
("guelphs", "Guelphs", icon_gray_knight, 0, fac_kingdom_40, aggressiveness_8|aggressiveness_0|courage_9, [(trp_iberian_knight, 1, 8, 0),(trp_iberian_billman, 15, 30, 0),(trp_iberian_veteran_crossbowman, 10, 15, 0),(trp_iberian_veteran_spearman, 10, 15, 0),(trp_iberian_light_cavalry, 10, 15, 0)]),
("ghibellines", "Ghibellines", icon_gray_knight, 0, fac_kingdom_41, aggressiveness_8|aggressiveness_0|courage_9, [(trp_iberian_knight, 1, 4, 0),(trp_merc_euro_guisarmer, 10, 15, 0),(trp_merc_euro_range, 10, 15, 0),(trp_merc_euro_spearman, 10, 15, 0),(trp_iberian_light_cavalry, 10, 15, 0)]),
("crusaders", "Crusaders", icon_crusaders, 0, fac_crusade, aggressiveness_8|aggressiveness_0|courage_9, [(trp_euro_horse_4, 10, 25, 0),(trp_euro_spearman_2, 150, 200, 0),(trp_merc_euro_range, 50, 100, 0),(trp_merc_euro_guisarmer, 50, 100, 0),(trp_merc_euro_spearman, 50, 100, 0),(trp_merc_euro_horse, 25, 50, 0)]),
("merc_party", "Angry band of alchoholics", icon_gray_knight|pf_show_faction, 0, fac_commoners, aggressiveness_8|aggressiveness_0|courage_9, []),
("crusader_raiders", "Crusaders", icon_crusaders|pf_show_faction, 0, fac_kingdom_23, aggressiveness_8|aggressiveness_0|courage_9, [(trp_iberian_knight, 1, 4, 0),(trp_iberian_light_cavalry, 5, 10, 0),(trp_iberian_town_footman_1, 10, 15, 0),(trp_iberian_veteran_spearman, 5, 8, 0),(trp_iberian_veteran_crossbowman, 5, 15, 0),(trp_iberian_billman, 1, 10, 0)]),
("jihadist_raiders", "Jihadists", icon_khergit|pf_show_faction, 0, fac_kingdom_25, aggressiveness_8|aggressiveness_0|courage_9, [(trp_bedouin_spearman, 8, 20, 0),(trp_halqa_archer, 5, 8, 0),(trp_bedouin_cav_2, 4, 10, 0),(trp_halqa_cav_2, 1, 3, 0),(trp_mamluke_turkoman_2, 10, 15, 0)]),
("teutonic_raiders", "Crusaders", icon_crusaders|pf_show_faction, 0, fac_kingdom_1, aggressiveness_8|aggressiveness_0|courage_9, [(trp_teu_horse_3, 1, 3, 0),(trp_teu_town_2_2, 2, 6, 0),(trp_teu_ger_1, 3, 10, 0),(trp_teu_ger_2_1, 5, 10, 0),(trp_teu_town_2_1, 10, 16, 0),(trp_teu_town_3_2, 5, 8, 0)]),
("manor", "Manor", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, 312, [(trp_manor_master, 1, 2, 0)]),
("farm", "Farm", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, 312, [(trp_manor_master, 1, 2, 0)]),
("linen", "Linen Workshop", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, 312, [(trp_manor_master, 1, 2, 0)]),
("salt", "Salt Trader", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, 312, [(trp_manor_master, 1, 2, 0)]),
("furs", "Hunter", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, 312, [(trp_manor_master, 1, 2, 0)]),
("iron", "Iron Trader", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, 312, [(trp_manor_master, 1, 2, 0)]),
("silk", "Silk Trader", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, 312, [(trp_manor_master, 1, 2, 0)]),
("iron_mine", "Iron Mine", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, 312, [(trp_manor_master, 1, 2, 0)]),
("salt_mine", "Salt Mine", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, 312, [(trp_manor_master, 1, 2, 0)]),
("weapon", "Weapon Smithy", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, 312, [(trp_manor_master, 1, 2, 0)]),
("armor", "Armor Smithy", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, 312, [(trp_manor_master, 1, 2, 0)]),
("fletchery", "Fletchery", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, 312, [(trp_manor_master, 1, 2, 0)]),
("breeder", "Horse Breeder", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, aggressiveness_8|aggressiveness_0|courage_9, []),
("monastery", "Monastery", icon_manor_icon|pf_is_static|pf_hide_defenders, 0, fac_commoners, aggressiveness_8|aggressiveness_0|courage_9, []),
("peasant_rebels_euro", "Peasant Rebels", icon_peasant, 0, fac_peasant_rebels, aggressiveness_8|aggressiveness_0|courage_9, []),
("steppe_bandits", "Sicarii Orientis", icon_khergit|carries_goods(2), 0, fac_outlaws, 312, [(trp_steppe_bandit, 15, 58, 0)]),
("taiga_bandits", "Sicarii Borealis", icon_axeman|carries_goods(2), 0, fac_outlaws, 312, [(trp_taiga_bandit, 15, 58, 0)]),
("desert_bandits", "Sicarii Vasti", icon_vaegir_knight|carries_goods(2), 0, fac_outlaws, 312, [(trp_desert_bandit, 15, 58, 0)]),
("forest_bandits", "Silvae Sicarii", icon_axeman|carries_goods(2), 0, fac_outlaws, 312, [(trp_forest_bandit, 15, 52, 0)]),
("mountain_bandits", "Montes Sicarii", icon_axeman|carries_goods(2), 0, fac_outlaws, 312, [(trp_mountain_bandit, 15, 60, 0)]),
("sea_raiders", "Piratae", icon_axeman|carries_goods(2), 0, fac_outlaws, 312, [(trp_sea_raider, 20, 50, 0)]),
("robber_knights", "Roving Robber Knight Band", icon_axeman|carries_goods(8), 0, fac_outlaws, 312, [(trp_euro_horse_4, 1, 2, 0),(trp_raider, 5, 12, 0)]),
("deserters", "Deserti", icon_vaegir_knight|carries_goods(3), 0, fac_deserters, 312, []),
("merchant_caravan", "Merchant Caravan", icon_gray_knight|pf_auto_remove_in_town|pf_quest_party|carries_goods(20), 0, fac_commoners, aggressiveness_0|courage_11, [(trp_caravan_master, 1, 1, 0),(trp_merc_euro_horse, 5, 15, 0)]),
("troublesome_bandits", "Troublesome Bandits", icon_axeman|pf_quest_party|carries_goods(9), 0, fac_outlaws, 312, [(trp_bandit, 14, 55, 0)]),
("bandits_awaiting_ransom", "Bandits Awaiting Ransom", icon_axeman|pf_auto_remove_in_town|pf_quest_party|carries_goods(9), 0, fac_neutral, 312, [(trp_bandit, 24, 58, 0),(trp_kidnapped_girl, 1, 1, 1)]),
("kidnapped_girl", "Kidnapped Girl", icon_woman|pf_quest_party, 0, fac_neutral, aggressiveness_0|courage_7, [(trp_kidnapped_girl, 1, 1, 0)]),
("village_farmers", "Village Farmers", icon_peasant|pf_civilian, 0, fac_innocents, aggressiveness_0|courage_7, [(trp_farmer, 8, 18, 0)]),
("spy_partners", "Unremarkable Travellers", icon_gray_knight|pf_default_behavior|pf_quest_party|carries_goods(3), 0, fac_neutral, aggressiveness_0|courage_7, [(trp_spy_partner, 1, 1, 0),(trp_merc_euro_horse, 5, 11, 0)]),
("runaway_serfs", "Runaway Serfs", icon_peasant|pf_default_behavior|pf_quest_party|carries_goods(8), 0, fac_neutral, aggressiveness_0|courage_7, [(trp_farmer, 6, 7, 0),(trp_peasant_woman, 3, 3, 0)]),
("spy", "Ordinary Townsman", icon_gray_knight|pf_default_behavior|pf_quest_party|carries_goods(3), 0, fac_neutral, aggressiveness_0|courage_7, [(trp_spy, 1, 1, 0)]),
("sacrificed_messenger", "Sacrificed Messenger", icon_gray_knight|pf_default_behavior|pf_quest_party|carries_goods(3), 0, fac_neutral, aggressiveness_0|courage_7, []),
("forager_party", "Foraging Party", icon_gray_knight|pf_show_faction|carries_goods(5), 0, fac_commoners, aggressiveness_0|courage_7, []),
("scout_party", "Scouts", icon_gray_knight|pf_show_faction|carries_goods(1), 0, fac_commoners, 312, []),
("patrol_party", "Custodes", icon_gray_knight|pf_show_faction|carries_goods(2), 0, fac_commoners, aggressiveness_8|aggressiveness_0|courage_9, []),
("messenger_party", "Messenger", icon_gray_knight|pf_show_faction, 0, fac_commoners, aggressiveness_0|courage_7, []),
("raider_party", "Raiders", icon_gray_knight|pf_quest_party|carries_goods(16), 0, fac_commoners, 312, []),
("raider_captives", "Raider Captives", 0, 0, fac_commoners, aggressiveness_0, [(trp_peasant_woman, 6, 30, 1)]),
("kingdom_caravan_party", "Caravan", icon_mule|pf_show_faction|carries_goods(45), 0, fac_commoners, aggressiveness_0|courage_7, [(trp_caravan_master, 1, 1, 0),(trp_merc_euro_horse, 1, 8, 0)]),
("prisoner_train_party", "Prisoner Train", icon_gray_knight|pf_show_faction|carries_goods(5), 0, fac_commoners, aggressiveness_0|courage_7, []),
("default_prisoners", "Default Prisoners", 0, 0, fac_commoners, aggressiveness_0, [(trp_bandit, 5, 10, 1)]),
("routed_warriors", "Routed Enemies", icon_vaegir_knight, 0, fac_commoners, aggressiveness_8|aggressiveness_0|courage_9, []),
("center_reinforcements", "Reinforcements", icon_axeman|carries_goods(16), 0, fac_commoners, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_euro_spearman, 9, 50, 0)]),
("kingdom_hero_party", "War Party", icon_flagbearer_a|pf_default_behavior|pf_show_faction, 0, fac_commoners, aggressiveness_8|aggressiveness_0|courage_9, []),
("kingdom_teutonic_reinforcements_a", "{!}kingdom teutonic reinforcements a", 0, 0, fac_kingdom_1, aggressiveness_8|aggressiveness_0|courage_9, [(trp_teu_horse_1, 1, 3, 0),(trp_teu_village_recruit, 4, 9, 0),(trp_teu_town_1, 4, 9, 0)]),
("kingdom_teutonic_reinforcements_b", "{!}kingdom teutonic reinforcements b", 0, 0, fac_kingdom_1, aggressiveness_8|aggressiveness_0|courage_9, [(trp_teu_town_2_2, 2, 6, 0),(trp_teu_ger_1, 1, 3, 0),(trp_teu_balt_1, 1, 3, 0),(trp_teu_town_2_1, 1, 3, 0)]),
("kingdom_teutonic_reinforcements_c", "{!}kingdom teutonic reinforcements c", 0, 0, fac_kingdom_1, aggressiveness_8|aggressiveness_0|courage_9, [(trp_teu_horse_4, 3, 6, 0)]),
("kingdom_baltic_reinforcements_a", "{!}kingdom baltic reinforcements a", 0, 0, fac_kingdom_2, aggressiveness_8|aggressiveness_0|courage_9, [(trp_balt_noble_recruit, 1, 3, 0),(trp_balt_skirmisher, 4, 10, 0),(trp_balt_footman, 4, 8, 0)]),
("kingdom_baltic_reinforcements_b", "{!}kingdom baltic reinforcements b", 0, 0, fac_kingdom_2, aggressiveness_8|aggressiveness_0|courage_9, [(trp_balt_archer, 1, 3, 0),(trp_balt_jav, 1, 3, 0),(trp_balt_veteran_jav, 1, 3, 0),(trp_balt_billman, 1, 3, 0),(trp_balt_spearman, 1, 3, 0),(trp_balt_noble_1, 1, 3, 0)]),
("kingdom_baltic_reinforcements_c", "{!}kingdom baltic reinforcements c", 0, 0, fac_kingdom_2, aggressiveness_8|aggressiveness_0|courage_9, [(trp_balt_medium_cavalry, 1, 2, 0),(trp_balt_noble_3, 1, 3, 0)]),
("kingdom_mongol_reinforcements_a", "{!}kingdom mongol reinforcements a", 0, 0, fac_kingdom_3, aggressiveness_8|aggressiveness_0|courage_9, [(trp_tatar_skirmisher, 5, 14, 0),(trp_tatar_tribesman, 3, 7, 0)]),
("kingdom_mongol_reinforcements_b", "{!}kingdom mongol reinforcements b", 0, 0, fac_kingdom_3, aggressiveness_8|aggressiveness_0|courage_9, [(trp_tatar_horse_archer, 3, 8, 0),(trp_tatar_horseman, 1, 5, 0),(trp_tatar_lancer, 1, 2, 0)]),
("kingdom_mongol_reinforcements_c", "{!}kingdom mongol reinforcements c", 0, 0, fac_kingdom_3, aggressiveness_8|aggressiveness_0|courage_9, [(trp_tatar_veteran_horse_archer, 1, 2, 0),(trp_tatar_heavy_lancer, 1, 1, 0)]),
("kingdom_nordic_reinforcements_a", "{!}kingdom nordic reinforcements a", 0, 0, fac_kingdom_4, aggressiveness_8|aggressiveness_0|courage_9, [(trp_nordic_village_recruit, 5, 12, 0),(trp_nordic_town_recruit, 6, 9, 0)]),
("kingdom_nordic_reinforcements_b", "{!}kingdom nordic reinforcements b", 0, 0, fac_kingdom_4, aggressiveness_8|aggressiveness_0|courage_9, [(trp_nordic_veteran_archer, 1, 2, 0),(trp_nordic_crossbowman, 1, 3, 0),(trp_nordic_billman, 1, 3, 0),(trp_nordic_veteran_spearman, 1, 3, 0),(trp_nordic_spearman, 1, 3, 0)]),
("kingdom_nordic_reinforcements_c", "{!}kingdom nordic reinforcements c", 0, 0, fac_kingdom_4, aggressiveness_8|aggressiveness_0|courage_9, [(trp_nordic_knight, 1, 2, 0),(trp_nordic_swords_sergeant, 2, 3, 0)]),
("kingdom_western_reinforcements_a", "{!}kingdom western reinforcements a", 0, 0, fac_kingdom_5, aggressiveness_8|aggressiveness_0|courage_9, [(trp_euro_horse_1, 3, 7, 0),(trp_euro_village_recruit, 3, 7, 0),(trp_euro_town_recruit, 3, 7, 0)]),
("kingdom_western_reinforcements_b", "{!}kingdom western reinforcements b", 0, 0, fac_kingdom_5, aggressiveness_8|aggressiveness_0|courage_9, [(trp_euro_archer_2, 1, 3, 0),(trp_euro_xbow_2, 1, 3, 0),(trp_euro_guisarm_2, 1, 3, 0),(trp_euro_spearman_3, 1, 3, 0),(trp_euro_spearman_2, 1, 3, 0)]),
("kingdom_western_reinforcements_c", "{!}kingdom western reinforcements c", 0, 0, fac_kingdom_5, aggressiveness_8|aggressiveness_0|courage_9, [(trp_euro_horse_2, 2, 5, 0)]),
("kingdom_rus_reinforcements_a", "{!}kingdom rus reinforcements a", 0, 0, fac_kingdom_8, aggressiveness_8|aggressiveness_0|courage_9, [(trp_rus_horse_1, 1, 3, 0),(trp_rus_vil_1, 6, 13, 0),(trp_rus_town_1, 2, 5, 0)]),
("kingdom_rus_reinforcements_b", "{!}kingdom rus reinforcements b", 0, 0, fac_kingdom_8, aggressiveness_8|aggressiveness_0|courage_9, [(trp_rus_vil_3_2, 2, 6, 0),(trp_rus_vil_3_1, 1, 3, 0),(trp_rus_town_4_2, 1, 3, 0),(trp_rus_town_3_2, 1, 3, 0)]),
("kingdom_rus_reinforcements_c", "{!}kingdom rus reinforcements c", 0, 0, fac_kingdom_8, aggressiveness_8|aggressiveness_0|courage_9, [(trp_rus_horse_2, 1, 2, 0),(trp_rus_horse_4, 1, 3, 0)]),
("kingdom_scot_reinforcements_a", "{!}kingdom scot reinforcements a", 0, 0, fac_kingdom_12, aggressiveness_8|aggressiveness_0|courage_9, [(trp_euro_horse_1, 1, 3, 0),(trp_scottish_village_recruit, 4, 9, 0),(trp_euro_town_recruit, 4, 9, 0)]),
("kingdom_scot_reinforcements_b", "{!}kingdom scot reinforcements b", 0, 0, fac_kingdom_12, aggressiveness_8|aggressiveness_0|courage_9, [(trp_euro_archer_2, 1, 3, 0),(trp_euro_xbow_2, 1, 3, 0),(trp_scottish_clansman, 1, 3, 0),(trp_euro_spearman_2, 1, 3, 0),(trp_scottish_forinsec_spearman, 1, 3, 0)]),
("kingdom_scot_reinforcements_c", "{!}kingdom scot reinforcements c", 0, 0, fac_kingdom_12, aggressiveness_8|aggressiveness_0|courage_9, [(trp_euro_horse_2, 2, 5, 0)]),
("kingdom_gaelic_reinforcements_a", "{!}kingdom gaelic reinforcements a", 0, 0, fac_kingdom_13, aggressiveness_8|aggressiveness_0|courage_9, [(trp_gaelic_light_cavalry, 1, 3, 0),(trp_gaelic_village_recruit, 4, 9, 0),(trp_gaelic_village_recruit, 4, 9, 0)]),
("kingdom_gaelic_reinforcements_b", "{!}kingdom gaelic reinforcements b", 0, 0, fac_kingdom_13, aggressiveness_8|aggressiveness_0|courage_9, [(trp_gaelic_archer_1, 1, 3, 0),(trp_gaelic_archer_2, 1, 3, 0),(trp_gaelic_infantry_2, 1, 3, 0),(trp_gaelic_spearman_2, 1, 3, 0),(trp_merc_gaelic_spearman, 1, 3, 0)]),
("kingdom_gaelic_reinforcements_c", "{!}kingdom gaelic reinforcements c", 0, 0, fac_kingdom_13, aggressiveness_8|aggressiveness_0|courage_9, [(trp_gaelic_knight, 2, 5, 0)]),
("kingdom_iberain_reinforcements_a", "{!}kingdom iberain reinforcements a", 0, 0, fac_kingdom_16, aggressiveness_8|aggressiveness_0|courage_9, [(trp_iberian_light_cavalry, 1, 3, 0),(trp_iberian_village_recruit, 4, 9, 0),(trp_iberian_town_recruit, 4, 9, 0)]),
("kingdom_iberain_reinforcements_b", "{!}kingdom iberain reinforcements b", 0, 0, fac_kingdom_16, aggressiveness_8|aggressiveness_0|courage_9, [(trp_iberian_archer, 1, 3, 0),(trp_iberian_veteran_crossbowman, 1, 3, 0),(trp_iberian_billman, 1, 3, 0),(trp_iberian_spears_sergeant, 1, 3, 0),(trp_iberian_veteran_spearman, 1, 3, 0)]),
("kingdom_iberain_reinforcements_c", "{!}kingdom iberain reinforcements c", 0, 0, fac_kingdom_16, aggressiveness_8|aggressiveness_0|courage_9, [(trp_iberian_knight, 2, 5, 0)]),
("kingdom_italian_reinforcements_a", "{!}kingdom italian reinforcements a", 0, 0, fac_kingdom_40, aggressiveness_8|aggressiveness_0|courage_9, [(trp_italian_light_cavalry, 1, 3, 0),(trp_italian_village_recruit, 4, 9, 0),(trp_italian_town_recruit, 4, 9, 0)]),
("kingdom_italian_reinforcements_b", "{!}kingdom italian reinforcements b", 0, 0, fac_kingdom_40, aggressiveness_8|aggressiveness_0|courage_9, [(trp_italian_archer, 1, 3, 0),(trp_italian_veteran_crossbowman, 1, 3, 0),(trp_italian_billman, 1, 3, 0),(trp_iberian_spears_sergeant, 1, 3, 0),(trp_italian_veteran_spearman, 1, 3, 0)]),
("kingdom_italian_reinforcements_c", "{!}kingdom italian reinforcements c", 0, 0, fac_kingdom_40, aggressiveness_8|aggressiveness_0|courage_9, [(trp_italian_knight, 2, 5, 0)]),
("kingdom_andalus_reinforcements_a", "{!}kingdom andalus reinforcements a", 0, 0, fac_kingdom_20, aggressiveness_8|aggressiveness_0|courage_9, [(trp_andalus_village_recruit, 13, 32, 0)]),
("kingdom_andalus_reinforcements_b", "{!}kingdom andalus reinforcements b", 0, 0, fac_kingdom_20, aggressiveness_8|aggressiveness_0|courage_9, [(trp_andalus_spearman_1, 2, 5, 0),(trp_andalus_spearman_2, 2, 5, 0),(trp_andalus_town_xbow_1, 3, 12, 0)]),
("kingdom_andalus_reinforcements_c", "{!}kingdom andalus reinforcements c", 0, 0, fac_kingdom_20, aggressiveness_8|aggressiveness_0|courage_9, [(trp_andalus_horse_4, 2, 5, 0)]),
("kingdom_byzantium_reinforcements_a", "{!}kingdom byzantium reinforcements a", 0, 0, fac_kingdom_22, aggressiveness_8|aggressiveness_0|courage_9, [(trp_byz_castle_1, 1, 3, 0),(trp_byz_village_1, 4, 9, 0),(trp_byz_town_1, 4, 9, 0)]),
("kingdom_byzantium_reinforcements_b", "{!}kingdom byzantium reinforcements b", 0, 0, fac_kingdom_22, aggressiveness_8|aggressiveness_0|courage_9, [(trp_byz_village_3_1, 1, 3, 0),(trp_byz_village_3_2, 1, 3, 0),(trp_byz_town_3_1, 2, 6, 0),(trp_byz_town_3_2, 1, 3, 0)]),
("kingdom_byzantium_reinforcements_c", "{!}kingdom byzantium reinforcements c", 0, 0, fac_kingdom_22, aggressiveness_8|aggressiveness_0|courage_9, [(trp_byz_castle_4, 2, 5, 0)]),
("kingdom_mamluke_reinforcements_a", "{!}kingdom mamluke reinforcements a", 0, 0, fac_kingdom_25, aggressiveness_8|aggressiveness_0|courage_9, [(trp_halqa_recruit, 4, 9, 0),(trp_mamluke_turkoman_1, 1, 3, 0),(trp_bedouin_recruit, 4, 9, 0),(trp_mamluke_turkoman_1, 0, 1, 0)]),
("kingdom_mamluke_reinforcements_b", "{!}kingdom mamluke reinforcements b", 0, 0, fac_kingdom_25, aggressiveness_8|aggressiveness_0|courage_9, [(trp_bedouin_spearman, 1, 3, 0),(trp_halqa_archer, 1, 3, 0),(trp_bedouin_cav_2, 1, 3, 0),(trp_halqa_cav_2, 1, 3, 0),(trp_mamluke_turkoman_2, 1, 3, 0)]),
("kingdom_mamluke_reinforcements_c", "{!}kingdom mamluke reinforcements c", 0, 0, fac_kingdom_25, aggressiveness_8|aggressiveness_0|courage_9, [(trp_mamluke_turkoman_3, 2, 5, 0)]),
("kingdom_marinid_reinforcements_a", "{!}kingdom marinid reinforcements a", 0, 0, fac_kingdom_28, aggressiveness_8|aggressiveness_0|courage_9, [(trp_marinid_village_rabble, 13, 32, 0)]),
("kingdom_marinid_reinforcements_b", "{!}kingdom marinid reinforcements b", 0, 0, fac_kingdom_28, aggressiveness_8|aggressiveness_0|courage_9, [(trp_marinid_light_spearmen, 2, 5, 0),(trp_marinid_light_lancer, 2, 5, 0),(trp_marinid_mounted_skirmisher_2, 3, 12, 0)]),
("kingdom_marinid_reinforcements_c", "{!}kingdom marinid reinforcements c", 0, 0, fac_kingdom_28, aggressiveness_8|aggressiveness_0|courage_9, [(trp_marinid_mounted_skirmisher_2, 3, 6, 0),(trp_marinid_mounted_skirmisher_2, 3, 6, 0)]),
("kingdom_serbian_reinforcements_a", "{!}kingdom serbian reinforcements a", 0, 0, fac_kingdom_29, aggressiveness_8|aggressiveness_0|courage_9, [(trp_serbian_horse_1, 1, 6, 0),(trp_serbian_vil_recruit, 6, 11, 0),(trp_serbian_town_recruit, 2, 4, 0)]),
("kingdom_serbian_reinforcements_b", "{!}kingdom serbian reinforcements b", 0, 0, fac_kingdom_29, aggressiveness_8|aggressiveness_0|courage_9, [(trp_serbian_vil_spearman, 2, 6, 0),(trp_serbian_vil_archer, 1, 3, 0),(trp_serbian_vil_spearman_veteran, 1, 3, 0),(trp_serbian_vil_axeman, 1, 3, 0),(trp_serbian_vil_archer, 1, 3, 0)]),
("kingdom_serbian_reinforcements_c", "{!}kingdom serbian reinforcements c", 0, 0, fac_kingdom_29, aggressiveness_8|aggressiveness_0|courage_9, [(trp_serbian_horse_2, 1, 2, 0),(trp_serbian_horse_4, 1, 3, 0)]),
("kingdom_balkan_reinforcements_a", "{!}kingdom balkan reinforcements a", 0, 0, fac_kingdom_30, aggressiveness_8|aggressiveness_0|courage_9, [(trp_balkan_horse_1, 1, 3, 0),(trp_balkan_vil_1, 2, 7, 0),(trp_balkan_town_1, 6, 11, 0)]),
("kingdom_balkan_reinforcements_b", "{!}kingdom balkan reinforcements b", 0, 0, fac_kingdom_30, aggressiveness_8|aggressiveness_0|courage_9, [(trp_balkan_vil_3_2_1, 2, 6, 0),(trp_balkan_vil_3_1, 1, 3, 0),(trp_balkan_town_3_1, 1, 3, 0),(trp_balkan_town_3_2, 1, 3, 0)]),
("kingdom_balkan_reinforcements_c", "{!}kingdom balkan reinforcements c", 0, 0, fac_kingdom_30, aggressiveness_8|aggressiveness_0|courage_9, [(trp_balkan_horse_2, 1, 2, 0),(trp_balkan_horse_4, 1, 3, 0)]),
("kingdom_welsh_reinforcements_a", "{!}kingdom welsh reinforcements a", 0, 0, fac_kingdom_37, aggressiveness_8|aggressiveness_0|courage_9, [(trp_welsh_horse_1, 1, 2, 0),(trp_welsh_recruit, 5, 10, 0),(trp_welsh_archer_1, 4, 9, 0)]),
("kingdom_welsh_reinforcements_b", "{!}kingdom welsh reinforcements b", 0, 0, fac_kingdom_37, aggressiveness_8|aggressiveness_0|courage_9, [(trp_welsh_archer_2, 3, 6, 0),(trp_welsh_horse_2, 1, 1, 0),(trp_welsh_spearman_1, 1, 2, 0),(trp_welsh_spearman_2, 1, 2, 0),(trp_welsh_archer_1, 1, 2, 0)]),
("kingdom_welsh_reinforcements_c", "{!}kingdom welsh reinforcements c", 0, 0, fac_kingdom_37, aggressiveness_8|aggressiveness_0|courage_9, [(trp_welsh_archer_2, 1, 2, 0),(trp_welsh_horse_4, 1, 3, 0)]),
("steppe_bandit_lair", "Steppe Bandit Lair", icon_bandit_lair|pf_is_static|pf_hide_defenders|carries_goods(2), 0, fac_neutral, 312, [(trp_steppe_bandit, 15, 58, 0)]),
("taiga_bandit_lair", "Tundra Bandit Lair", icon_bandit_lair|pf_is_static|pf_hide_defenders|carries_goods(2), 0, fac_neutral, 312, [(trp_taiga_bandit, 15, 58, 0)]),
("desert_bandit_lair", "Desert Bandit Lair", icon_bandit_lair|pf_is_static|pf_hide_defenders|carries_goods(2), 0, fac_neutral, 312, [(trp_desert_bandit, 15, 58, 0)]),
("forest_bandit_lair", "Forest Bandit Camp", icon_bandit_lair|pf_is_static|pf_hide_defenders|carries_goods(2), 0, fac_neutral, 312, [(trp_forest_bandit, 15, 58, 0)]),
("mountain_bandit_lair", "Highway Bandit Hideout", icon_bandit_lair|pf_is_static|pf_hide_defenders|carries_goods(2), 0, fac_neutral, 312, [(trp_mountain_bandit, 15, 58, 0)]),
("sea_raider_lair", "Sea Raider Landing", icon_bandit_lair|pf_is_static|pf_hide_defenders|carries_goods(2), 0, fac_neutral, 312, [(trp_sea_raider, 15, 50, 0)]),
("robber_knight_lair", "Robber Knight's Hideout", icon_bandit_lair|pf_is_static|pf_hide_defenders|carries_goods(2), 0, fac_neutral, 312, [(trp_euro_horse_4, 1, 1, 0),(trp_raider, 15, 25, 0)]),
("looter_lair", "Kidnappers' Hideout", icon_bandit_lair|pf_is_static|pf_hide_defenders|carries_goods(2), 0, fac_neutral, 312, [(trp_looter, 15, 25, 0)]),
("bandit_lair_templates_end", "{!}bandit lair templates end", icon_axeman|pf_is_static|carries_goods(2), 0, fac_outlaws, 312, [(trp_sea_raider, 15, 50, 0)]),
("leaded_looters", "Band of robbers", icon_axeman|pf_quest_party|carries_goods(8), 0, fac_neutral, 312, [(trp_looter_leader, 1, 1, 0),(trp_looter, 3, 3, 0)]),
("pagan_stronghold", "Pagan Stronghold", icon_bandit_lair|pf_is_static|pf_hide_defenders|carries_goods(2), 0, fac_neutral, 312, [(trp_balt_skirmisher, 5, 7, 0),(trp_balt_footman, 5, 7, 0),(trp_balt_jav, 5, 7, 0),(trp_balt_veteran_jav, 1, 3, 0),(trp_balt_billman, 5, 7, 0),(trp_balt_spearman, 5, 7, 0)]),
("dplmc_spouse", "Your spouse", icon_woman|pf_show_faction|pf_civilian, 0, fac_neutral, aggressiveness_0|courage_7, []),
("dplmc_gift_caravan", "Your Caravan", icon_mule|pf_show_faction|carries_goods(25), 0, fac_commoners, aggressiveness_0|courage_11, [(trp_caravan_master, 1, 1, 0),(trp_merc_euro_horse, 10, 35, 0)]),
("dplmc_recruiter", "Recruiter", icon_gray_knight|pf_show_faction, 0, fac_neutral, aggressiveness_0|courage_7, [(trp_dplmc_recruiter, 1, 1, 0)]),
("crusaders_teutonic", "{!}crusaders teutonic", 0, 0, fac_kingdom_23, aggressiveness_8|aggressiveness_0|courage_9, [(trp_teu_horse_3, 1, 6, 0),(trp_teu_horse_4, 1, 3, 0)]),
("crusaders_templar", "{!}crusaders templar", 0, 0, fac_kingdom_23, aggressiveness_8|aggressiveness_0|courage_9, [(trp_templar_half_brother, 1, 6, 0),(trp_templar_knight, 1, 3, 0)]),
("crusaders_hospitaller", "{!}crusaders hospitaller", 0, 0, fac_kingdom_23, aggressiveness_8|aggressiveness_0|courage_9, [(trp_hospitaller_half_brother, 1, 6, 0),(trp_hospitaller_knight, 1, 3, 0)]),
("crusaders_lazarus", "{!}crusaders lazarus", 0, 0, fac_kingdom_23, aggressiveness_8|aggressiveness_0|courage_9, [(trp_saint_lazarus_half_brother, 1, 6, 0),(trp_saint_lazarus_knight, 1, 3, 0)]),
("crusaders_santiago", "{!}crusaders santiago", 0, 0, fac_kingdom_23, aggressiveness_8|aggressiveness_0|courage_9, [(trp_santiago_half_brother, 1, 6, 0),(trp_santiago_knight, 1, 3, 0)]),
("crusaders_calatrava", "{!}crusaders calatrava", 0, 0, fac_kingdom_23, aggressiveness_8|aggressiveness_0|courage_9, [(trp_calatrava_half_brother, 1, 6, 0),(trp_calatrava_knight, 1, 3, 0)]),
("crusaders_saint_thomas", "{!}crusaders saint thomas", 0, 0, fac_kingdom_23, aggressiveness_8|aggressiveness_0|courage_9, [(trp_saint_thomas_half_brother, 1, 6, 0),(trp_saint_thomas_knight, 1, 3, 0)]),
("teutonic_reinforcements_a", "{!}teutonic reinforcements a", 0, 0, fac_kingdom_23, aggressiveness_8|aggressiveness_0|courage_9, [(trp_teu_horse_1, 1, 3, 0),(trp_teu_village_recruit, 4, 9, 0),(trp_teu_town_1, 4, 9, 0)]),
("teutonic_reinforcements_b", "{!}teutonic reinforcements b", 0, 0, fac_kingdom_23, aggressiveness_8|aggressiveness_0|courage_9, [(trp_teu_town_2_2, 2, 6, 0),(trp_teu_ger_1, 1, 3, 0),(trp_teu_balt_1, 1, 3, 0),(trp_teu_town_2_1, 1, 3, 0)]),
("teutonic_reinforcements_c", "{!}teutonic reinforcements c", 0, 0, fac_kingdom_23, aggressiveness_8|aggressiveness_0|courage_9, [(trp_teu_horse_4, 3, 6, 0)]),
("templar_reinforcements_a", "{!}templar reinforcements a", 0, 0, fac_kingdom_23, aggressiveness_8|aggressiveness_0|courage_9, [(trp_crusader_turkopole, 1, 3, 0),(trp_iberian_village_recruit, 4, 9, 0),(trp_iberian_town_recruit, 4, 9, 0)]),
("templar_reinforcements_b", "{!}templar reinforcements b", 0, 0, fac_kingdom_23, aggressiveness_8|aggressiveness_0|courage_9, [(trp_iberian_archer, 1, 3, 0),(trp_iberian_veteran_crossbowman, 1, 3, 0),(trp_iberian_billman, 1, 3, 0),(trp_iberian_spears_sergeant, 1, 3, 0),(trp_iberian_veteran_spearman, 1, 3, 0)]),
("templar_reinforcements_c", "{!}templar reinforcements c", 0, 0, fac_kingdom_23, aggressiveness_8|aggressiveness_0|courage_9, [(trp_templar_knight, 3, 6, 0)]),
("hospitaller_reinforcements_a", "{!}hospitaller reinforcements a", 0, 0, fac_kingdom_23, aggressiveness_8|aggressiveness_0|courage_9, [(trp_crusader_turkopole, 1, 3, 0),(trp_iberian_village_recruit, 4, 9, 0),(trp_iberian_town_recruit, 4, 9, 0)]),
("hospitaller_reinforcements_b", "{!}hospitaller reinforcements b", 0, 0, fac_kingdom_23, aggressiveness_8|aggressiveness_0|courage_9, [(trp_iberian_archer, 1, 3, 0),(trp_iberian_veteran_crossbowman, 1, 3, 0),(trp_iberian_billman, 1, 3, 0),(trp_iberian_spears_sergeant, 1, 3, 0),(trp_iberian_veteran_spearman, 1, 3, 0)]),
("hospitaller_reinforcements_c", "{!}hospitaller reinforcements c", 0, 0, fac_kingdom_23, aggressiveness_8|aggressiveness_0|courage_9, [(trp_hospitaller_knight, 3, 6, 0)]),
("kingdom_21_reinforcements_a", "{!}kingdom 21 reinforcements a", 0, 0, fac_papacy, aggressiveness_8|aggressiveness_0|courage_9, [(trp_euro_horse_1, 1, 3, 0),(trp_euro_village_recruit, 4, 9, 0),(trp_euro_town_recruit, 4, 9, 0)]),
("kingdom_21_reinforcements_b", "{!}kingdom 21 reinforcements b", 0, 0, fac_papacy, aggressiveness_8|aggressiveness_0|courage_9, [(trp_euro_archer_2, 1, 3, 0),(trp_euro_xbow_2, 1, 3, 0),(trp_euro_guisarm_2, 1, 3, 0),(trp_euro_spearman_3, 1, 3, 0),(trp_euro_spearman_2, 1, 3, 0)]),
("kingdom_21_reinforcements_c", "{!}kingdom 21 reinforcements c", 0, 0, fac_papacy, aggressiveness_8|aggressiveness_0|courage_9, [(trp_euro_horse_2, 2, 5, 0)]),
("roman_reinforcements_a", "{!}roman reinforcements a", 0, 0, fac_kingdom_22, aggressiveness_8|aggressiveness_0|courage_9, [(trp_byz_castle_1, 1, 3, 0),(trp_byz_village_1, 4, 9, 0),(trp_byz_town_1, 4, 9, 0)]),
("roman_reinforcements_b", "{!}roman reinforcements b", 0, 0, fac_kingdom_22, aggressiveness_8|aggressiveness_0|courage_9, [(trp_byz_village_3_1, 1, 3, 0),(trp_byz_village_3_2, 1, 3, 0),(trp_byz_town_3_1, 2, 6, 0),(trp_byz_town_3_2, 1, 3, 0)]),
("roman_reinforcements_c", "{!}roman reinforcements c", 0, 0, fac_kingdom_22, aggressiveness_8|aggressiveness_0|courage_9, [(trp_byz_castle_2, 1, 2, 0),(trp_byz_castle_4, 2, 3, 0),(trp_varangian_guard, 1, 5, 0)]),
("armenian_reinforcements_c", "{!}armenian reinforcements c", 0, 0, fac_kingdom_23, aggressiveness_8|aggressiveness_0|courage_9, [(trp_anatolian_heavy_cavalry, 2, 5, 0)]),
("seljuk_reinforcements_c", "{!}seljuk reinforcements c", 0, 0, fac_kingdom_27, aggressiveness_8|aggressiveness_0|courage_9, [(trp_anatolian_turkoman_3, 2, 5, 0)]),
("almogabar", "{!}Lance", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_almogabar, 20, 20, 0)]),
("welsh_merc", "{!}Lance", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_welsh_bowman, 20, 25, 0),(trp_merc_welsh_bowman_commander, 1, 5, 0)]),
("sicilian_merc_1", "{!}Lance", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_sicily_infantry_2, 5, 5, 0),(trp_merc_sicily_infantry_1, 15, 15, 0)]),
("sicilian_merc_2", "{!}Lance", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_sicily_foot_archer_2, 5, 5, 0),(trp_merc_sicily_foot_archer_1, 15, 15, 0)]),
("sicilian_merc_3", "{!}Lance", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_sicily_horse_archer_2, 5, 5, 0),(trp_merc_sicily_horse_archer_1, 15, 15, 0)]),
("zanata_merc", "{!}Lance", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_maghreb_horse, 10, 10, 0),(trp_merc_maghreb_spearman, 10, 10, 0),(trp_merc_maghreb_range, 10, 10, 0)]),
("generic_euro", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_euro_spearman, 12, 15, 0),(trp_merc_euro_guisarmer, 5, 7, 0),(trp_merc_euro_range, 6, 10, 0),(trp_merc_euro_horse, 3, 7, 0)]),
("generic_balt", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_balt_spearman, 12, 15, 0),(trp_merc_balt_guisarmer, 5, 7, 0),(trp_merc_balt_range, 6, 10, 0),(trp_merc_balt_horse, 3, 7, 0)]),
("generic_maghreb", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_maghreb_spearman, 14, 23, 0),(trp_merc_maghreb_range, 6, 10, 0),(trp_merc_maghreb_horse, 3, 7, 0)]),
("generic_rus", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_rus_spearman, 12, 15, 0),(trp_merc_rus_guisarmer, 5, 7, 0),(trp_merc_rus_range, 6, 10, 0),(trp_merc_rus_horse, 3, 7, 0)]),
("generic_latin", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_latin_spearman, 10, 13, 0),(trp_merc_latin_guisarmer, 4, 6, 0),(trp_merc_latin_range, 5, 8, 0),(trp_merc_latin_horse, 2, 5, 0),(trp_merc_latin_light, 7, 12, 0)]),
("generic_balkan", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_balkan_spearman, 12, 15, 0),(trp_merc_balkan_guisarmer, 5, 7, 0),(trp_merc_balkan_range, 6, 10, 0),(trp_merc_balkan_horse, 3, 7, 0)]),
("generic_scan", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_scan_spearman, 12, 15, 0),(trp_merc_scan_guisarmer, 5, 7, 0),(trp_merc_scan_range, 6, 10, 0),(trp_merc_scan_horse, 3, 7, 0)]),
("generic_gaelic", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_gaelic_spearman, 12, 15, 0),(trp_merc_gaelic_axeman_1, 5, 7, 0),(trp_merc_gaelic_spearman_2, 6, 10, 0),(trp_merc_gaelic_axeman_2, 3, 7, 0)]),
("generic_mamluk", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_mamluke_spearman, 12, 15, 0),(trp_merc_mamluke_javalin, 7, 10, 0),(trp_merc_mamluke_range, 5, 7, 0),(trp_merc_mamluke_syrian, 3, 7, 0)]),
("company_genoese", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_genoese_crossbowman, 25, 32, 0),(trp_genoese_crossbowman_commander, 1, 5, 0)]),
("company_brabantine", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_brabantine_spearman, 12, 15, 0),(trp_merc_brabantine_guisarm, 4, 7, 0),(trp_merc_brabantine_xbow, 6, 10, 0)]),
("company_welsh", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_welsh_bowman, 12, 15, 0),(trp_merc_kern_infantry, 10, 15, 0),(trp_merc_welsh_bowman_commander, 1, 3, 0)]),
("company_mamlukes", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_mamluke_medium_horse_archer, 5, 8, 0),(trp_mamluke_heavy_horse_archer, 2, 3, 0),(trp_mamluke_elite_horse_archer, 1, 3, 0)]),
("company_sicily", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_merc_sicily_infantry_1, 12, 15, 0),(trp_merc_sicily_infantry_2, 4, 7, 0),(trp_merc_sicily_foot_archer_1, 6, 10, 0),(trp_merc_sicily_foot_archer_2, 1, 5, 0),(trp_merc_sicily_horse_archer_1, 1, 5, 0),(trp_merc_sicily_horse_archer_2, 1, 5, 0)]),
("company_cuman", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_cuman_skirmisher, 12, 15, 0),(trp_cuman_horseman, 4, 7, 0),(trp_cuman_horse_archer, 6, 10, 0),(trp_cuman_veteran_horse_archer, 3, 7, 0),(trp_cuman_lancer, 1, 3, 0),(trp_cuman_heavy_lancer, 1, 3, 0)]),
("company_georgian", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_georgian_lancer, 12, 18, 0),(trp_goergian_horse_archer, 10, 18, 0)]),
("company_turkopoles", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_crusader_turkopole, 18, 32, 0)]),
("company_varangian", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_varangian_guard, 18, 32, 0)]),
("company_kwarezmian", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_kwarezmian_range, 12, 15, 0),(trp_kwarezmian_light_horse, 10, 18, 0),(trp_kwarezmian_medium_horse, 6, 8, 0)]),
("company_mordovian", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_mordovian_foot, 12, 18, 0),(trp_mordovian_range, 4, 7, 0),(trp_mordovian_horse, 6, 10, 0)]),
("company_kipchak", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_kipchak_range, 10, 15, 0),(trp_kipchak_light_horse, 5, 9, 0),(trp_kipchak_medium_horse, 5, 7, 0)]),
("company_teutons", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_teu_horse_3, 1, 6, 0),(trp_teu_horse_4, 1, 2, 0)]),
("company_hospitalier", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_hospitaller_half_brother, 1, 6, 0),(trp_hospitaller_knight, 1, 2, 0)]),
("company_templar", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_templar_half_brother, 1, 6, 0),(trp_templar_knight, 1, 2, 0)]),
("company_lazarus", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_saint_lazarus_half_brother, 1, 6, 0),(trp_saint_lazarus_knight, 1, 2, 0)]),
("company_santiago", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_santiago_half_brother, 1, 6, 0),(trp_santiago_knight, 1, 2, 0)]),
("company_calatrava", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_calatrava_half_brother, 1, 6, 0),(trp_calatrava_knight, 1, 2, 0)]),
("company_thomas", "{!}Company", 0, 0, fac_neutral, aggressiveness_8|aggressiveness_0|courage_9, [(trp_saint_thomas_half_brother, 1, 6, 0),(trp_saint_thomas_knight, 1, 2, 0)]),
("mongolian_camp", "Mongolian horde", icon_khergit|pf_show_faction|carries_goods(5), 0, fac_commoners, aggressiveness_8|aggressiveness_0|courage_9, [(trp_tatar_veteran_horse_archer, 1, 2, 0),(trp_tatar_heavy_lancer, 1, 1, 0),(trp_tatar_skirmisher, 10, 14, 0),(trp_tatar_tribesman, 8, 13, 0)]),

]