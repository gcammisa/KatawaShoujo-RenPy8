init -3 python:





    init_language("en")

    displayDict["en"].styleoverrides = {"font": mainfont,
                                        "language": "western",
                                        "line_spacing": 0}

    displayDict["en"].timeformat = "%b %d, %H:%M"

    displayDict["en"].selector_padding = 0 
    displayDict["en"].nvl_paragraph_distance = 10 

    displayDict["en"].sayfont = mainfont

    displayDict["en"].quote_outer_open = u"“"
    displayDict["en"].quote_outer_close = u"”"
    displayDict["en"].quote_inner_open = u"‘"
    displayDict["en"].quote_inner_close = u"’"

    displayDict["en"].activeLanguage = "English"
    displayDict["en"].allLanguages = {}
    displayDict["en"].allLanguages["en"] = displayDict["en"].activeLanguage
    displayDict["en"].allLanguages["de"] = "German"
    displayDict["en"].allLanguages["it"] = "Italian"
    displayDict["en"].allLanguages["fr"] = "French"
    displayDict["en"].allLanguages["es"] = "Spanish"
    displayDict["en"].allLanguages["jp"] = "Japanese"

    displayDict["en"].act_term = u"Act"
    displayDict["en"].window_name = u"Katawa Shoujo"

    displayDict["en"].main_menu_start = u"Start"
    displayDict["en"].main_menu_load = u"Load"
    displayDict["en"].main_menu_extra = u"Extras"
    displayDict["en"].main_menu_config = u"Options"
    displayDict["en"].main_menu_quit = u"Quit"

    displayDict["en"].game_menu_return = u"Return"
    displayDict["en"].game_menu_show = u"Show image"
    displayDict["en"].game_menu_history = u"Text history"
    displayDict["en"].game_menu_skip = u"Skip mode"
    displayDict["en"].game_menu_auto = u"Auto mode"
    displayDict["en"].game_menu_config = u"Options"
    displayDict["en"].game_menu_save = u"Save"
    displayDict["en"].game_menu_load = u"Load"
    displayDict["en"].game_menu_main = u"Main menu"
    displayDict["en"].game_menu_quit = u"Quit"
    displayDict["en"].game_menu_current_scene = u"Current scene"
    displayDict["en"].game_menu_current_music = u"Current music track"
    displayDict["en"].game_menu_replay_indicator = u"Replay"

    displayDict["en"].return_button_text = u"Return"

    displayDict["en"].hdisabled_label = u"Disable adult content"
    displayDict["en"].config_page_caption = u"Options"
    displayDict["en"].config_fullscreen_label = u'Fullscreen mode'
    displayDict["en"].config_transitions_label = u'Disable transitions'
    displayDict["en"].config_skip_unseen_label = u'Skip unread text'
    displayDict["en"].config_skip_after_choice_label = u'Keep skipping after choices'
    displayDict["en"].config_textspeed_label = u'Text speed'
    displayDict["en"].config_afmspeed_label = u'Auto mode delay'
    displayDict["en"].config_musicvol_label = u"Music volume"
    displayDict["en"].config_musicvol_jukebox_label = u"Vol."
    displayDict["en"].config_sfxvol_label = u"SFX volume"
    displayDict["en"].config_sfxtest_label = u"Test"
    displayDict["en"].config_gamepad_label = u"Gamepad keymap…"

    displayDict["en"].config_language_sel = u"Language selection…"
    displayDict["en"].config_language_caption = u"Options > Language selection"
    displayDict["en"].config_language_restart_note = "Note: Changing the language while a session is in progress will return the game to the latest script node."

    displayDict["en"].gamepad_caption = u"Options > Gamepad keymap"
    displayDict["en"].gamepad_key_na = u"Not assigned"
    displayDict["en"].gamepad_request_key = u"Press the button you want to assign “%s” to.\nClick the mouse or the select button to clear the mapping."

    displayDict["en"].yesno_yes = u"Yes"
    displayDict["en"].yesno_no = u"No"
    displayDict["en"].yesno_okay = u"Continue"
    displayDict["en"].yesno_savesuccess = u"Progress successfully saved."
    displayDict["en"].yesno_quit = u"Are you sure you want to\nquit Katawa Shoujo?"
    displayDict["en"].yesno_return_to_main = u"Are you sure you want to\nreturn to the main menu?"
    displayDict["en"].save_page_caption = u"Save"
    displayDict["en"].new_save_button = u"Create new save state"
    displayDict["en"].load_page_caption = u"Load"
    displayDict["en"].yesno_load_in_game = u"Are you sure you want to\ndiscard your progress?"
    displayDict["en"].yesno_save_overwrite = u"Are you sure you want to\noverwrite your save?"
    displayDict["en"].yesno_delete_savegame = u"Are you sure you want to\ndelete this save?"
    displayDict["en"].play_time_label = u"Play time"
    displayDict["en"].show_manual_saves = u"Manual"
    displayDict["en"].show_auto_saves = u"Auto"

    displayDict["en"].text_history_caption = u"Text history"
    displayDict["en"].text_history_note = u"Note"

    displayDict["en"].extra_menu_caption = "Extras"
    displayDict["en"].extra_music_button_label = "Jukebox"
    displayDict["en"].extra_gallery_button_label = "Gallery"
    displayDict["en"].extra_scene_button_label = "Library"
    displayDict["en"].extra_omake_button_label = "Omake"
    displayDict["en"].extra_opening_button_label = "Cinema"
    displayDict["en"].commentary_label = "Enable commentary"

    displayDict["en"].video_page_caption = "Extras > Cinema"


    displayDict["en"].music_page_caption = "Extras > Jukebox"
    displayDict["en"].music_stop_button_text = "Stop"
    displayDict["en"].music_now_playing = "Now playing"

    displayDict["en"].gallery_page_caption = "Extras > Gallery"
    displayDict["en"].gallery_onelocked = "One further image not unlocked."
    displayDict["en"].gallery_manylocked = "%d further images not unlocked."
    displayDict["en"].gallery_singlelocked = "Image %d of %d is not unlocked."
    displayDict["en"].gallery_num_page_prefix = "Page"
    displayDict["en"].gallery_num_page_error = "No images to display"

    displayDict["en"].scene_page_caption = "Extras > Library"
    displayDict["en"].scene_completion_label = "Completion: %s%%"
    displayDict["en"].scene_playthrough_label = "Use replay flow (recommended)"
    displayDict["en"].scene_launch_path = "Do you wish to start\nthe entire path?"

    displayDict["en"].joy_left = "Left"
    displayDict["en"].joy_right = "Right"
    displayDict["en"].joy_up = "Up"
    displayDict["en"].joy_down = "Down"
    displayDict["en"].joy_dismiss = "Select/Advance"
    displayDict["en"].joy_rollback = "Text history"
    displayDict["en"].joy_holdskip = "Hold to skip"
    displayDict["en"].joy_toggleskip = "Skip mode"
    displayDict["en"].joy_hide = "Show image"
    displayDict["en"].joy_menu = "Show menu"



    displayDict["en"].name_hi = "Hisao"

    displayDict["en"].name_ha = "Hanako"
    displayDict["en"].name_emi = "Emi"
    displayDict["en"].name_rin = "Rin"
    displayDict["en"].name_li = "Lilly"
    displayDict["en"].name_shi = "Shizune"
    displayDict["en"].name_mi = "Misha"

    displayDict["en"].name_ke = "Kenji"
    displayDict["en"].name_mu = "Mutou"
    displayDict["en"].name_nk = "Nurse"
    displayDict["en"].name_no = "Nomiya"
    displayDict["en"].name_yu = "Yuuko"
    displayDict["en"].name_sa = "Sae"
    displayDict["en"].name_aki = "Akira"
    displayDict["en"].name_hh = "Hideaki"
    displayDict["en"].name_hx = "Jigoro"
    displayDict["en"].name_emm = "Meiko"
    displayDict["en"].name_sk = "Shopkeep"
    displayDict["en"].name_mk = "Miki"

    displayDict["en"].name_mystery = "???"

    displayDict["en"].name_ha_ = "Purple-haired girl"
    displayDict["en"].name_emi_ = "Twintails girl"
    displayDict["en"].name_rin_ = "Strange girl"
    displayDict["en"].name_li_ = "Wavy-haired girl"
    displayDict["en"].name_mi_ = "Laughing girl"
    displayDict["en"].name_ke_ = "Bespectacled hallmate"
    displayDict["en"].name_mu_ = "Tall man"
    displayDict["en"].name_yu_ = "Librarian"
    displayDict["en"].name_no_ = "Silver-haired man"
    displayDict["en"].name_sa_ = "Gallery owner"
    displayDict["en"].name_aki_ = "Well-dressed person"
    displayDict["en"].name_nk_ = "Smiling man"
    displayDict["en"].name_hh_ = "Slim girl"
    displayDict["en"].name_emm_ = "Woman with braid"
    displayDict["en"].name_hx_ = "Huge man"

    displayDict["en"].videos = (("Opening", "video/base_op_1.mp4"),
                                ("Emi", "video/base_tc_act2_emi.mp4"),
                                ("Hanako", "video/base_tc_act2_hanako.mp4"),
                                ("Lilly", "video/base_tc_act2_lilly.mp4"),
                                ("Rin", "video/base_tc_act2_rin.mp4"),
                                ("Shizune", "video/base_tc_act2_shizune.mp4"),
                               )

    ##If we're on iOS we override the videos displaydict with the correct iOS videos:
    if (renpy.ios):
        displayDict["en"].videos = (("Opening", "video/ios_op_1.mp4"),
                                    ("Emi", "video/ios_tc_act2_emi.mp4"),
                                    ("Hanako", "video/ios_tc_act2_hanako.mp4"),
                                    ("Lilly", "video/ios_tc_act2_lilly.mp4"),
                                    ("Rin", "video/ios_tc_act2_rin.mp4"),
                                    ("Shizune", "video/ios_tc_act2_shizune.mp4"),
                                )





    displayDict["en"].s_scenes = (("Prologue", rp_actmark, rp_actmark, ("Act 1","Prologue")),
                                    ("Out Cold", "NOP1", "On a cold, snowy day, Hisao's dreams were about to be realized, only to be cut short by a sudden heart attack.", ("Act 1","Prologue")),
                                    ("Bundle of Hisao", "NOP2", "Hisao is told about Yamaku Academy, where he will likely spend the rest of his high school days.", ("Act 1","Prologue")),
                                    ("Act 1: Life Expectancy", rp_actmark, rp_actmark, "Act 1"),
                                    ("Gateway Effect", "A1", "Hisao steps into Yamaku Academy for the first time, and meets his homeroom teacher, Mutou.", "Act 1"),
                                    ("Enter Stage Left", "A2", "Introductions to the class, and meeting with the class representative and her interpreter.", "Act 1"),
                                    ("In the Nursery", "A3", "Misha and Shizune show Hisao the cafeteria, after which he goes to see the nurse.", "Act 1"),
                                    ("Nobody's Room", "A4", "Hisao moves into his new room, meeting his hallmate Kenji in the process.", "Act 1"),
                                    ("Smalltalk", "A5", "Shizune and Misha tell Hisao about the upcoming festival and invite him to lunch.", "Act 1"),
                                    ("Risk vs. Reward", "A6", "Shizune and Hisao battle for the world in a game of Risk.", "Act 1"),
                                    ("Pseudo Tea Cosy", "A7", "Looking for the library, Hisao gets lost and finds Lilly in a disused classroom.", "Act 1"),
                                    ("Shared Library", "A8", "Finally finding his way to the library, Hisao meets and scares off Hanako.", "Act 1"),
                                    ("Bizarre and Surreal", "A9", "Kenji reveals the dark secrets of Yamaku.", "Act 1"),
                                    ("Lunch Evolution Theory", "A10", "Shizune and Misha badger Hisao into joining the Student Council before discussing lunch.", "Act 1"),
                                    ("Short Sharp Shock", "A11_1", "On his way to lunch alongside Misha and Shizune, Hisao collides with Emi in the hallway.", "Act 1"),
                                    ("Meet Cute", "A11_2", "Hisao collides with a rampaging Emi on his way to lunch with Hanako and Lilly.", "Act 1"),
                                    ("Detour Ahead", "A12", "Shizune and Misha take Hisao to their favourite teahouse, the Shanghai.", "Act 1"),
                                    ("Sip (Part 1)", "A13", "Hisao has a peaceful lunch with Lilly and Hanako.", "Act 1"), 
                                    ("It Builds Character", "A15", "Mutou tries to have a D&M talk with Hisao, but Misha interrupts and puts Hisao to work.", "Act 1"),
                                    ("A Private Lunch", "A16", "Searching for supplies, Hisao happens across a strange girl in the art room.", "Act 1"),
                                    ("Waylay", "A17", "While helping Rin carry some paint, Hisao is quizzed by the nurse.", "Act 1"),
                                    ("The Other Green", "A18", "Hisao watches Rin paint her mural.", "Act 1"),
                                    ("The Running Girl", "A19", "When attempting to do some morning exercise, Hisao meets Emi at the running track.", "Act 1"),
                                    ("Soap", "A20", "Kenji ambushes Hisao in the shower in an attempt to get some cash.", "Act 1"),
                                    ("Cold War", "A21", "Shizune and Lilly face off over budget requests.", "Act 1"),
                                    ("Proof of Competency", "A22", "Shizune and Misha assault Hisao in an attempt to get him to join the Student Council.", "Act 1"),
                                    ("Event Horizon", "A22_2", "Shizune and Misha assault Hisao in an attempt to get him to join the Student Council.", "Act 1"),
                                    ("Above and Beyond", "A23_1", "Hisao gets a lecture about the noble duties of a Student Council.", "Act 1"),
                                    ("Things You Can Do", "A23_2", "After escaping from the clutches of Shizune and Misha, Hisao helps out Rin again.", "Act 1"),
                                    ("Paint by Numbers", "A24", "Hanako and Hisao lend a hand to Lilly's class by volunteering to help build their stall.", "Act 1"),
                                    ("Exercise", "A25", "Another early morning sees Hisao running at the track with Emi.", "Act 1"),
                                    ("Invisible Hat", "A26", "Kenji gives Hisao a few insider tips on how to socialize.", "Act 1"),
                                    ("Home Field Advantage", "A26_1", "Shizune and Misha hijack Hisao as he leaves his room for class.", "Act 1"),
                                    ("No Recovery", "A27", False, "Act 1"), 
                                    ("Slow Recovery", "A27_1", "Recovering from his heart flutter, Hisao eventually makes it to class.", "Act 1"),
                                    ("No Recovery", "A27_2", "Hisao struggles to class after his hijacking by the Student Council.", "Act 1"),
                                    ("No Free Lunch", "A28", "Hisao is escorted to the student council office for his first official day there.", "Act 1"),
                                    ("Foot and Mouth", "A29", "Emi drags Hisao to the roof to have lunch with Rin.", "Act 1"),
                                    ("Mind Your Step", "A30", "Hisao and Lilly go shopping, meeting a very confused Rin on the way back.", "Act 1"),
                                    ("Support", "A31", "Hisao has his first Saturday lesson, complete with a talking to from Mutou.", "Act 1"),
                                    ("An Aesthetics", "A32", "Emi finds Hisao slacking around after class and recruits him to help Rin once again.", "Act 1"),
                                    ("Creative Pain", "A33", "Hisao meets the art teacher, Nomiya, as Rin paints her mural.", "Act 1"),
                                    ("Proper Exercise", "A34", "Emi and Hisao discuss the importance of being in shape.", "Act 1"),
                                    ("Sip (Part 2)", "A35", "In an attempt to kill time, Hisao goes for a walk around the school.", "Act 1"),
                                    ("Shanghaied", "A36", "Tea, cake and competitions with Shizune and Misha at the Shanghai.", "Act 1"),
                                    ("Quiet", "A37", "Hanako and Hisao read books for the festival.", "Act 1"),
                                    ("Don't Panic", "A38", "After waking up on the day of the festival, Hisao is greeted by a ranting Kenji.", "Act 1"),
                                    ("Is Carnival!", "A39", "Emi catches Hisao eating fried food and makes him accompany her as punishment.", "Act 1"),
                                    ("Nc5xb3", "A42", "Unable to help Lilly at her stall, Hisao searches for Hanako at the festival.", "Act 1"),
                                    ("Movement", "H2", "Lilly finishes her duties and treats Hanako and Hisao to tea at the Shanghai.", "Act 1"), 
                                    ("Promise of Time", "A41", "After a trying morning at her stall, Hisao takes Lilly to find Hanako.", "Act 1"),
                                    ("Clouds in My Head", "A40", "Hisao keeps Rin and her now-finished mural company.", "Act 1"),
                                    ("Throwing Balls", "A44", "True to his word, Hisao spends the day with Shizune and Misha.", "Act 1"),
                                    ("The Deep End", "A43", "Kenji and Hisao share a manly picnic on the roof instead of going to the festival.", "Act 1"),
                                    ("Act 2: Form", rp_actmark, rp_actmark, ("Act 2","Emi")),
                                    ("Morning Run", "E3", "The first of Hisao's many morning runs with Emi.", ("Act 2","Emi")),
                                    ("Clouds, Time Travel, and Thou", "E4", "Another rooftop lunch with Emi and Rin. Emi extracts from Hisao a promise to come see the track meet.", ("Act 2","Emi")),
                                    ("Questions That Need Answering!", "E5", "Idle chat between Emi and Hisao. Hisao asks Emi a few more questions about her relationship with Rin.", ("Act 2","Emi")),
                                    ("Second Time's the Worst", "E6", "The second morning run. Hisao is almost dragged kicking and screaming around the track.", ("Act 2","Emi")),
                                    ("An Apple a Day", "E7", "Hisao pays a visit to the nurse along with Emi, finding out that the two have known each other for a while.", ("Act 2","Emi")),
                                    ("Track Meeting", "E8", "The day of the track meet. Another facet of Emi's personality is revealed.", ("Act 2","Emi")),
                                    ("Down that Medicine Now", "E9", "Hisao mentions a pain in his chest during a visit to the nurse and receives a lecture.", ("Act 2","Emi")),
                                    ("Piracy on the High Seas", "E10", "Hisao discusses his future as a pirate with Emi on the rooftop, then a letter from Iwanako spoils his day.", ("Act 2","Emi")),
                                    ("Famous Last Words", "E11", "Emi and Rin take Hisao along for a picnic, soon to be spoiled by rain.", ("Act 2","Emi")),
                                    ("Tracking Absences", "E12", "Hisao goes to the track as usual, but Emi is missing.", ("Act 2","Emi")),
                                    ("Dropping By", "E13", "A bedside visit for a sick Emi, which quickly changes to something else entirely.", ("Act 2","Emi")),
                                    ("The First Morning After", "E14", "Hisao reminisces about last evening, deciding to do something to help Emi.", ("Act 2","Emi")),
                                    ("The (Real) Beginning", "E15", "Another lunchtime on the rooftop, sans Rin.", ("Act 2","Emi")),
                                    ("Act 3: Perspective", rp_actmark, rp_actmark, ("Act 3","Emi")),
                                    (u"Eet Ees… Scienca", "E16", "Mutou pulls Hisao into a short discussion about his future.", ("Act 3","Emi")),
                                    ("Definitions", "E17", "Emi and Hisao attempt another picnic, this time without any intervention from Mother Nature.", ("Act 3","Emi")),
                                    ("Invisible Rock", "E18", "Back to the track in the morning, with business as usual… or so it seems.", ("Act 3","Emi")),
                                    ("Lunch and Science", "E19", "Hisao sees Mutou again about his future in the sciences.", ("Act 3","Emi")),
                                    ("Up, Down, and Up Again", "E20", "A frantic call from Emi brings Hisao to her room, where two surprises await him.", ("Act 3","Emi")),
                                    ("Storage Space", "E21", "Emi coaxes Hisao into the track storage shed.", ("Act 3","Emi")),
                                    ("After-School Plans", "E22", "Emi has a serious talk with Hisao about the incoming exams.", ("Act 3","Emi")),
                                    ("Detached", "E23", "Hisao broods about his relationship with Emi.", ("Act 3","Emi")), 
                                    ("Phantom Pain", "E24", "Hisao's attempt to show Emi his concern doesn't go nearly as well as he hoped.", ("Act 3","Emi")),
                                    ("Debate Expresses Doubt", "E25", "Hisao is confused by Emi's behavior and by an invitation to her house.", ("Act 3","Emi")),
                                    (u"Guess Who's Coming… Never Mind", "E26", "Dinner at the Ibarazaki's.", ("Act 3","Emi")),
                                    ("Instant Replay", "E27", "Things finally come to a head at the track.", ("Act 3","Emi")),
                                    ("Act 4: Motion", rp_actmark, rp_actmark, ("Act 4","Emi")),
                                    ("A Swing and a Miss", "E28", "Hisao wonders if Emi is purposefully avoiding him.", ("Act 4","Emi")),
                                    ("Saving Throw", "E29", "Things finally come to a head on the rooftop.", ("Act 4","Emi")),
                                    ("Whispers of the Past", "E30", "Hisao, Emi and her mom go for a graveside visit.", ("Act 4","Emi")),
                                    ("Hooray for Socks", "E31", "Sex, drugs, but no rock and roll.", ("Act 4","Emi")),
                                    ("Clean Teeth", "E32", "Hisao wakes up, finding Emi sleeping next to him.", ("Act 4","Emi")),
                                    ("Act 2: Hide and Seek", rp_actmark, rp_actmark, ("Act 2","Hanako")),
                                    ("To Town, To Town", "H3", "A shopping trip at the convenience store with Hanako.", ("Act 2","Hanako")),
                                    ("Tea Leaves", "H4", "Hanako invites Hisao to have lunch with her and Lilly.", ("Act 2","Hanako")),
                                    ("Office Confessional", "H5_1", "Hisao and Misha discuss the plight of Hanako.", ("Act 2","Hanako")),
                                    ("Chess and Slides", "H5_2", "Hisao ditches the Student Council to read with Hanako.", ("Act 2","Hanako")),
                                    ("Rise and Shine", "H6", "An invitation from Lilly to a tea party after hours.", ("Act 2","Hanako")),
                                    ("Mad Hatter", "H7", "Hanako, Hisao and Lilly meet together to have tea in Lilly's room.", ("Act 2","Hanako")),
                                    ("Small Change", "H8", "Kenji is forced to repay his loan.", ("Act 2","Hanako")),
                                    ("Absenteeism", "H9", "Hisao and Lilly discuss Hanako's school attendance.", ("Act 2","Hanako")),
                                    ("Equivalent Exchange", "H10", "In return for learning about his heart, Hanako reveals part of her past to Hisao.", ("Act 2","Hanako")),
                                    ("Act 3: Castling", rp_actmark, rp_actmark, ("Act 3","Hanako")),
                                    ("Invitation", "H11", "Lilly finds Hisao cleaning up the Tea Room and tells him about Hanako's birthday.", ("Act 3","Hanako")),
                                    ("Shady Encounter", "H12", "An unexpected chat with Miki while reminiscing about the past.", ("Act 3","Hanako")),
                                    ("Antiques and Pie", "H13", "Lilly and Hisao shop for a present in the city.", ("Act 3","Hanako")),
                                    ("Falling", "H14", "Hanako has a panic attack during class.", ("Act 3","Hanako")),
                                    ("Treading Softly", "H15", "Lilly has bad news to discuss with Hisao and Hanako.", ("Act 3","Hanako")),
                                    ("Reaching Out", "H16", "Hisao reaches out to a withdrawn Hanako.", ("Act 3","Hanako")),
                                    ("One More Year", "H17", "Our trio is joined by an unexpected guest as they celebrate Hanako's birthday party.", ("Act 3","Hanako")),
                                    ("One Piece of Paper", "H18", "Hisao enjoys his first hangover, before receiving a troubling letter.", ("Act 3","Hanako")),
                                    ("Stripes and Solids", "H19", "Heart-to-heart during a game of pool.", ("Act 3","Hanako")),
                                    ("Beginning of the End", "H20", "Lilly's departure for her trip.", ("Act 3","Hanako")),
                                    ("Act 4: Scars", rp_actmark, rp_actmark, ("Act 4","Hanako")),
                                    ("Truancy", "H21", "Lunch with the Student Council and worry about Hanako shutting herself in.", ("Act 4","Hanako")),
                                    ("Faraway Presence", "H22", "Hisao phones Lilly for advice after Hanako secludes herself for another day.", ("Act 4","Hanako")),
                                    ("Misstep", "H23", "Hisao tries to pull Hanako out of her room, with startling results.", ("Act 4","Hanako")),
                                    ("Cut Petals", "H24", "Hisao finds his future relationship with Hanako prematurely ended.", ("Act 4","Hanako")),
                                    ("Continuing Melody", "H25", "Hanako returns to class, to Hisao's relief.", ("Act 4","Hanako")),
                                    ("Shanghai Studiousness", "H26", "Attempting to avoid distractions, Hisao tries studying at the Shanghai.", ("Act 4","Hanako")),
                                    ("His Past", "H27", "In an attempt to come closer to Hanako, Hisao shares a part of his past with her.", ("Act 4","Hanako")),
                                    ("City Rendezvous", "H28", "The two share a date in the city.", ("Act 4","Hanako")),
                                    ("Whispered Touch", "H29", "Hisao and Hanako spend the night together.", ("Act 4","Hanako")),
                                    ("Indeterminate Future", "H30", "The events of the previous night weigh heavily on Hisao.", ("Act 4","Hanako")),
                                    ("Adulthood", "H31", "The end of two children, the beginning of two adults.", ("Act 4","Hanako")),
                                    ("Act 2: Past", rp_actmark, rp_actmark, ("Act 2","Lilly")),
                                    ("Earl Grey", "L1", "Hisao shares the first of many lunchbreaks with Hanako and Lilly, recovering from the day before.", ("Act 2","Lilly")),
                                    ("A Pound Sterling", "L2", "Questioned by Kenji on Lilly's nationality, Hisao decides to investigate and finds out a great deal more.", ("Act 2","Lilly")),
                                    ("Presents and Presence", "L3", "While out in search of a present for Hanako, Lilly and Hisao meet Akira and her cousin.", ("Act 2","Lilly")),
                                    ("Unidentified Drinking Object", "L4", "The trio hold a birthday party for Hanako, interrupted by the surprise appearance of a sibling.", ("Act 2","Lilly")),
                                    ("The Day After", "L5", "Hisao and Lilly awaken and try to recuperate from the previous evening's events.", ("Act 2","Lilly")),
                                    ("A Brief History of Thyme", "L6", "Hisao and Lilly go to get some groceries.", ("Act 2","Lilly")),
                                    ("Little Wing", "L7", "A shared lunch on the roof takes an unfortunate turn.", ("Act 2","Lilly")),
                                    ("Bon Voyage", "L8", "Lilly and Akira get seen off as they leave for a trip to their family in Scotland.", ("Act 2","Lilly")),
                                    ("Act 3: Present", rp_actmark, rp_actmark, ("Act 3","Lilly")),
                                    ("Day by Day", "L9", "Hisao idly lets a day without Lilly slip by, having a talk with Mutou about Yamaku.", ("Act 3","Lilly")),
                                    ("Minor Discord", "L10", "Hisao has lunch with Kenji, then gives some handouts to an alarmingly silent Hanako.", ("Act 3","Lilly")),
                                    ("Dissonance", "L11", "With Hanako withdrawing into herself completely, Hisao offers what little help he can before calling Lilly.", ("Act 3","Lilly")),
                                    ("A World Away", "L12", "Hisao's reassured mind begins to wonder about the relationship between he and Lilly.", ("Act 3","Lilly")),
                                    ("Renewal", "L13", "Hisao, Hanako, and Hideaki welcome Akira and Lilly after their return from Scotland.", ("Act 3","Lilly")),
                                    ("Northern Sojourn", "L14", "The trio begins their holiday in Hokkaido.", ("Act 3","Lilly")),
                                    ("Prelude", "L15", "A morning walk begins a chain of events.", ("Act 3","Lilly")),
                                    ("Crescendo", "L16", "Lilly's true feelings are told in the endless gold of the wheat fields." , ("Act 3","Lilly")),
                                    ("Diminuendo", "L17", "Our couple shares their first night together.", ("Act 3","Lilly")),
                                    ("Gray Outlook", "L18", "Confined to the summerhouse, Lilly and Hisao are forced to come to terms with their relationship.", ("Act 3","Lilly")),
                                    ("Rhapsody in Blue", "L19", "A bathing Hisao reflects on where he and Lilly are in life, before being joined by someone.", ("Act 3","Lilly")),
                                    ("The Momentary Present", "L20", "Traveling back to Yamaku, Hisao and Lilly idly talk between themselves.", ("Act 3","Lilly")),
                                    ("Act 4: Future", rp_actmark, rp_actmark, ("Act 4","Lilly")),
                                    ("Slow Steps 'Fore a Waltz", "L21", "Back at the school, the events of Hokkaido come to the fore.", ("Act 4","Lilly")),
                                    ("Pajamas and Suits", "L22", "Settling back into daily life. Akira joins the trio during one of their tea parties.", ("Act 4","Lilly")),
                                    ("Correct Procedure", "L23", "Hisao and Lilly arrange a date, before Akira swings by.", ("Act 4","Lilly")),
                                    ("Out and About", "L24", "Hisao and Lilly go on their first date, finding out about each other's pasts.", ("Act 4","Lilly")),
                                    ("A Morning's Reverie", "L25", "Hisao and Lilly discuss their ambitions for the future.", ("Act 4","Lilly")),
                                    ("Blackout", "L26", "The trio muse on the upcoming holidays, before Hisao experiences sight as Lilly does.", ("Act 4","Lilly")),
                                    ("Context", "L27", "Hisao gets called out by Akira and the two talk about her sibling.", ("Act 4","Lilly")),
                                    ("A Faraway Future", "L28", "Lilly reveals her family's offer to join them in Scotland.", ("Act 4","Lilly")),
                                    ("Farewell", "L29", "Farewells to Akira and Lilly the evening before they leave Japan.", ("Act 4","Lilly")),
                                    ("False Cadence", "L30", "Hisao rushes to confront Lilly, realizing her conflict.", ("Act 4","Lilly")),
                                    ("Under a Maudlin Sky", "L31", "Waking in the hospital ward, Hisao struggles to come to terms with his life.", ("Act 4","Lilly")),
                                    ("Under a Bright Sky", "L32", "Lilly rejoins Hisao, the two beginning their life together anew.", ("Act 4","Lilly")),
                                    ("Forwards, with Gusto!", "L33", "Lilly and Hisao see off Akira.", ("Act 4","Lilly")),
                                    ("Act 2: Disconnect", rp_actmark, rp_actmark, ("Act 2","Rin")),
                                    ("A Wider Field of Vision", "R1", "Hisao spends a lunch break with Rin watching clouds on the rooftop.", ("Act 2","Rin")),
                                    ("Studies in Grayscale", "R2", "Rin and Hisao draw portraits of each other at his first art club meeting.", ("Act 2","Rin")),
                                    (u"Interstitial", "R3", "Kenji lends a “borrowed” book to Hisao.", ("Act 2","Rin")),
                                    ("Self Study", "R4", "Misha and Shizune catch Hisao meditatively doodling during class.", ("Act 2","Rin")),
                                    ("Hisao's Smile", "R5", "Rin talks to Hisao about his happy expressions, or lack of them.", ("Act 2","Rin")),
                                    ("Things You Like", "R6", "Brief musings with Yuuko about books and Yamaku.", ("Act 2","Rin")),
                                    ("Target Audience", "R7", "The day of the track meet. Facets of Emi's and Rin's personalities get revealed.", ("Act 2","Rin")),
                                    ("Eternity In an Hour", "R8", "Nomiya incites discussion of art during a club meeting.", ("Act 2","Rin")),
                                    ("Underwater and a Maple with a Name", "R9", "Rin leads Hisao into the woods, where they ponder their immediate future.", ("Act 2","Rin")),
                                    ("Iwanako's Regret", "R10", "A letter from Iwanako arrives.", ("Act 2","Rin")),
                                    ("In Her Own Image", "R11", "Hisao pushes Rin to have her own art exhibition.", ("Act 2","Rin")),
                                    ("Umbrella Logic Cake", "R12", "Emi, Hisao and Rin get rained on and seek refuge in the Shanghai.", ("Act 2","Rin")),
                                    ("Six Meters Closer to Heaven", "R13", "Rin and Hisao DON'T eat lunch on the roof, due to a distinct lack of Emi.", ("Act 2","Rin")),
                                    ("Indecision", "R14", "Emi gets rid of her cold, while Rin catches her own.", ("Act 2","Rin")),
                                    ("Signal Interference", "R15", "Hisao goes visit Rin in her room.", ("Act 2","Rin")),
                                    ("Dandelions", "R16", "Conclusions get drawn on a hilltop.", ("Act 2","Rin")),
                                    ("Act 3: Distance", rp_actmark, rp_actmark, ("Act 3","Rin")),
                                    ("22nd Corner", "R17", "The art club team checks out the gallery for Rin's future exhibition.", ("Act 3","Rin")),
                                    ("The Scent of Light", "R18", "Hisao happens upon a sleeping Rin in the art room.", ("Act 3","Rin")),
                                    ("Things You Can't Give Up", "R19", "Emi and Hisao discuss Rin's personality.", ("Act 3","Rin")),
                                    ("BADAAN!", "R20", "Yuuko's thoughts on motivation.", ("Act 3","Rin")),
                                    ("Rose-Tinted Glasses", "R21", "Nomiya expounds at length about art as a career.", ("Act 3","Rin")),
                                    ("The Edge of the World", "R22", "Hisao confesses to Rin and gets shot down. Or does he?", ("Act 3","Rin")),
                                    ("The Context of Rin", "R23", "An awkward and silent afternoon at the atelier.", ("Act 3","Rin")),
                                    ("Fast Forward", "R23_2", "The preparations for the exhibition settle into a strange routine.", ("Act 3","Rin")),
                                    ("Self-Destruction", "R24", "Rin experiments with smoking to get a fresh look at creativity.", ("Act 3","Rin")),
                                    ("Reverse Escapism", "R25", "Hisao takes Rin on a walk through the night streets.", ("Act 3","Rin")),
                                    ("Boundless", "R26", "Sae and Nomiya give Hisao some insight on artists' lives.", ("Act 3","Rin")),
                                    ("Delirium", "R27", "Hisao surprises a desperate Rin in the atelier.", ("Act 3","Rin")),
                                    ("Things You Hate", "R28", "Unpleasant aftermath of an incredible night.", ("Act 3","Rin")),
                                    ("Shards of Ire", "R29", "The strained relationship between the two blows apart.", ("Act 3","Rin")),
                                    ("Act 4: Dream", rp_actmark, rp_actmark, ("Act 4","Rin")),
                                    ("Illusions for People", "R30", "Hisao talks about his misgivings to Nomiya, to little effect.", ("Act 4","Rin")),
                                    ("Demused", "R31", "Hisao's patience comes to an end.", ("Act 4","Rin")),
                                    ("The Scene", "R32", "Meeting with Rin at the exhibition opening.", ("Act 4","Rin")), 
                                    ("Wavelength", "R35", "Hisao lethargically whiles away the last day of exams.", ("Act 4","Rin")),
                                    ("Blue Period", "R36", "A rainy day, the 22nd Corner, and a brief history of Picasso.", ("Act 4","Rin")),
                                    ("The World Only You Can See", "R37", "Rin and Hisao part after the rain.", ("Act 4","Rin")),
                                    ("Desperate Glory", "R34", "A frantic Nomiya queries Hisao about Rin's whereabouts.", ("Act 4","Rin")), 
                                    ("Problems of Self-Referential Logic", "R38", "Hisao finds Rin in her hiding place, and convinces her to reconcile with Nomiya.", ("Act 4","Rin")),
                                    ("Measuring Shadows", "R39", "Rin's apology to the art teacher isn't well-received.", ("Act 4","Rin")),
                                    (u"Raison d'être", "R40", "Hisao comforts an upset Rin.", ("Act 4","Rin")),
                                    ("Without Breathing, Without a Sound", "R41", "On the first day of summer vacation, Rin comes to Hisao's room.", ("Act 4","Rin")),
                                    ("Proof of Existence", "R42", "Everything comes together on that dandelion-covered hilltop.", ("Act 4","Rin")),
                                    ("Act 2: Learning to Read", rp_actmark, rp_actmark, ("Act 2","Shizune")),
                                    ("Message Passing", "S8", "Shizune and Hisao explore methods of communication.", ("Act 2","Shizune")),
                                    ("Talk to the Hand", "S9", "Hisao begins studying a new language, and a tutor appears.", ("Act 2","Shizune")),
                                    ("Chinese Whispers", "S10", "Kenji manages to coerce Hisao to do a favor for him, but Hisao runs into trouble in many forms.", ("Act 2","Shizune")),
                                    ("Advanced Game Theory", "S11", "RISK isn't enough any more to satiate Shizune's hunger. What's worse, a new opponent makes her appearance.", ("Act 2","Shizune")),
                                    ("Bread, Scissors, Paper", "S12", "A lazy afternoon becomes dramatic as suddenly a piece of bread becomes an object of extreme interest.", ("Act 2","Shizune")),
                                    ("Interface", "S13", "Shizune and Hisao find a connection.", ("Act 2","Shizune")),
                                    ("Spring into Action", "S14", "Hisao has to mediate between Lilly and Shizune, but luckily things work out in the end.", ("Act 2","Shizune")),
                                    ("Past Imperfective", "S15", "The Student Council reminisces about past years while relaxing at the Shanghai.", ("Act 2","Shizune")),
                                    ("When Stars Embrace", "S16", "It's finally time for Tanabata!", ("Act 2","Shizune")),
                                    ("Act 3: Sleight of Hand", rp_actmark, rp_actmark, ("Act 3","Shizune")),
                                    ("Force Feedback", "S17", "Hisao finds out that Shizune is going to visit her family, and manages to come along.", ("Act 3","Shizune")),
                                    ("United Nations", "S18", "The trip to Shizune's house, meeting her little brother, and a sudden fishing contest.", ("Act 3","Shizune")),
                                    ("Use-Mention Distinction", "S19", "Hideaki tries to entertain Hisao for a day, meeting with little success.", ("Act 3","Shizune")),
                                    ("Family Plot", "S20", "Our trio meets Shizune's father and immediately beats a hasty retreat.", ("Act 3","Shizune")),
                                    ("Pangrammatic Window", "S21", "A request from Hideaki to learn sign language unexpectedly escalates into a shouting match with Jigoro.", ("Act 3","Shizune")),
                                    ("Closer", "S22", "Shizune and Hisao join together for the first time.", ("Act 3","Shizune")),
                                    ("Confrontation", "S23", "Jigoro belittles the Student Council and Hisao rises up to the challenge.", ("Act 3","Shizune")),
                                    ("The Anchor", "S24", "Back to Yamaku. A letter from Iwanako prompts a lengthy discussion from Kenji on the finer points of girlfriends.", ("Act 3","Shizune")),
                                    ("Roadmap", "S25", "The Student Council worries about their replacement, and Hisao ends up treating Misha to a parfait somehow.", ("Act 3","Shizune")), 
                                    ("Acute Triangle", "S26", "An afternoon of work with Shizune shows Hisao that something is amiss between the girls.", ("Act 3","Shizune")),
                                    ("Dewey Decimated", "S27", "Yuuko gets Hisao to watch the library for her. The arrival of Kenji makes the attempt meet with mixed success.", ("Act 3","Shizune")),
                                    ("Tongue-Tied", "S28", "Misha visits Hisao in his room, and things go in an unexpected direction.", ("Act 3","Shizune")),
                                    ("Look Aside", "S29_1", "Hisao meets a depressed Misha on the roof. He ends up pushing her and Shizune together.", ("Act 3","Shizune")),
                                    ("Look Ahead", "S29_2", "Hisao meets a depressed Misha on the roof. Shizune joins them and pulls the whole council back to work.", ("Act 3","Shizune")),
                                    ("Act 4: To My Other Self", rp_actmark, rp_actmark, ("Act 4","Shizune")),
                                    ("Grand Strategy", "S30", "Shizune confesses to Hisao some of her goals and failures.", ("Act 4","Shizune")),
                                    ("Off by One", "S31", "A failed attempt to cheer up Misha gets converted into an impromptu date for Hisao and Shizune.", ("Act 4","Shizune")),
                                    ("Invasion", "S32", "Jigoro and Hideaki pay Shizune an unexpected and somewhat unpleasant visit.", ("Act 4","Shizune")),
                                    ("Parfait", "S33", "Hisao and Shizune stalk Misha. Hisao finally manages to corner her and discuss things properly.", ("Act 4","Shizune")),
                                    ("Present Tense", "S38", "Hisao stumbles into Lilly at lunch, and the two talk about Shizune.", ("Act 4","Shizune")), 
                                    ("Spiral", "S39", "Runaround, stonewalling, and Kenji nighttime ambush.", ("Act 4","Shizune")),
                                    ("Terminal", "S40", "An early-morning talk with Shizune in the silent school.", ("Act 4","Shizune")),
                                    ("The Summit", "S34", "Kenji and Shizune meet in Hisao's room. Miraculously, nothing explodes.", ("Act 4","Shizune")), 
                                    ("Succession", "S35", "The current Student Council shapes up their successors before engaging in “extracurricular activities.”", ("Act 4","Shizune")),
                                    ("Sneaking Mission", "S36", "The show of Misha's determination spurs Shizune to set her sights on greater things.", ("Act 4","Shizune")),
                                    ("Infinity", "S37", "Our trio renews their friendship, with their graduation looming close ahead.", ("Act 4","Shizune")),
                                    )



    displayDict["en"].creditstring = """{image=ui/flourish_left.png} {b}Writing{/b} {image=ui/flourish_right.png}
Anonymous22
Aura
cpl_crud
Suriko
TheHivemind

{image=ui/flourish_left.png} {b}Editing{/b} {image=ui/flourish_right.png}
Kagami
Losstarot
Silentcook

{image=ui/flourish_left.png} {b}Music{/b} {image=ui/flourish_right.png}
Blue123
NicolArmarfi

{image=ui/flourish_left.png} {b}Art{/b} {image=ui/flourish_right.png}
gebyy-terar
Kamifish
moekki
pimmy
raemz
Raide

{image=ui/flourish_left.png} {b}Additional Art{/b} {image=ui/flourish_right.png}
climatic
Doomfest
yujovi

{image=ui/flourish_left.png} {b}FMV Animation{/b} {image=ui/flourish_right.png}
Mike Inel

{image=ui/flourish_left.png} {b}Directing{/b} {image=ui/flourish_right.png}
delta
Raide
yujovi

{image=ui/flourish_left.png} {b}Engineering{/b} {image=ui/flourish_right.png}
delta

{image=ui/flourish_left.png} {b}Production{/b} {image=ui/flourish_right.png}
cpl_crud
Suriko


{image=ui/flourish_center.png}


{image=ui/flourish_left.png} {b}Thanks{/b} {image=ui/flourish_right.png}
Ambi07
abscess
Anonymous
Celiest
ContinualNaba
Dark_Mercury
DuaneMoody
Fink
frumplstlskn
Ismuth
Japesland
Juno
kekekeke
konflikti
Magaran
Mirage_GSM
OverCoat
Peorth
Petaru
silentkyon
skim
stirfriedweasel
Syureria
TcDohl
tottori
VCR

{image=ui/flourish_left.png} {b}Special Thanks{/b} {image=ui/flourish_right.png}
hir
Paisseon
PyTom
RAITA
replicated"""


    displayDict["en"].drugs_wordlist  =  ["Disopyramide",
                        "Warfarin",
                        "Diltiazem",
                        "Felodipine",
                        "Propanolol",
                        "Penbutolol",
                        "Carteolol",
                        "Procainamide",
                        "Heparin",
                        "Phenytoin",
                        "Verapamil",
                        "Quinidine",
                        "Flecainide",
                        "5mg/day",
                        "400mg/day",
                        "15ml/day",
                        "100mg/day",
                        "10ml/48hrs",
                        "10ml/day",
                        "200mg/12hrs",
                        "50mg/12hrs",
                        "500mg/48hrs",
                        "125mg/12hrs",
                        "25ml/day",
                        "nightmares",
                        "decreased concentration",
                        "bradycardia",
                        "clinical depression",
                        "insomnia",
                        "erectile dysfunction",
                        "abnormal vision",
                        "heart failure",
                        "nausea",
                        "dizziness",
                        "hallucinations",
                        "bronchospasm",
                        "dyspnea",
                        "fatigue",
                        "hypotension",
                        "heart block",
                        "cold extremities",
                        "diarrhea",
                        "cardiac arrest",
                        "ventricular fibrillation",
                        "ataxia",
                        "asthma"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
