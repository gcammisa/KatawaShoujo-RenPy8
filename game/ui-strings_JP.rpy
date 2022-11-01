init -2 python:



    init_language("jp")
    jpfont = "font/VL-PGothic-Regular.ttf"

    def jpw(string):
        return "{font=" + jpfont + "}" + string + "{/font} "

    displayDict["jp"].styleoverrides = {"font": jpfont,
                                        "language": "eastasian",
                                        "line_spacing": -3}

    displayDict["jp"].timeformat = "%m/%d, %H:%M"
    displayDict["jp"].selector_padding = -1
    displayDict["jp"].nvl_paragraph_distance = 10

    displayDict["jp"].sayfont = jpfont


    displayDict["jp"].quote_outer_open = u"「"
    displayDict["jp"].quote_outer_close = u"」"
    displayDict["jp"].quote_inner_open = u"『"
    displayDict["jp"].quote_inner_close = u"』"

    displayDict["jp"].activeLanguage = jpw(u"日本語")
    displayDict["jp"].allLanguages = {}
    displayDict["jp"].allLanguages["en"] = jpw(u"英語")


    displayDict["jp"].allLanguages["fr"] = jpw(u"フランス語")
    displayDict["jp"].allLanguages["es"] = jpw(u"スペイン語")
    displayDict["jp"].allLanguages["jp"] = displayDict["jp"].activeLanguage

    displayDict["jp"].act_term = u"Act"
    displayDict["jp"].window_name = u"かたわ少女"

    displayDict["jp"].main_menu_start = u"はじめから"
    displayDict["jp"].main_menu_load = u"つづきから"
    displayDict["jp"].main_menu_extra = u"おまけ"
    displayDict["jp"].main_menu_config = u"環境設定"
    displayDict["jp"].main_menu_quit = u"終了"

    displayDict["jp"].game_menu_return = u"戻る"
    displayDict["jp"].game_menu_show = u"ウインドウ消去"
    displayDict["jp"].game_menu_history = u"テキストログ"
    displayDict["jp"].game_menu_skip = u"スキップ"
    displayDict["jp"].game_menu_auto = u"オート"
    displayDict["jp"].game_menu_config = u"環境設定"
    displayDict["jp"].game_menu_save = u"セーブ"
    displayDict["jp"].game_menu_load = u"ロード"
    displayDict["jp"].game_menu_main = u"タイトル"
    displayDict["jp"].game_menu_quit = u"ゲーム終了"
    displayDict["jp"].game_menu_current_scene = u"現在のシーン"
    displayDict["jp"].game_menu_current_music = u"BGM"
    displayDict["jp"].game_menu_replay_indicator = u"リプレイ"

    displayDict["jp"].return_button_text = u"戻る"

    displayDict["jp"].hdisabled_label = u"成人向けコンテンツ無効"
    displayDict["jp"].config_page_caption = u"環境設定"
    displayDict["jp"].config_fullscreen_label = u"フルスクリーンモード"
    displayDict["jp"].config_transitions_label = u"画面効果オフ"
    displayDict["jp"].config_skip_unseen_label = u"未読テキストもスキップ"
    displayDict["jp"].config_skip_after_choice_label = u"選択肢の後もスキップ継続"
    displayDict["jp"].config_textspeed_label = u"テキスト表示速度"
    displayDict["jp"].config_afmspeed_label = u"オートモード待ち時間"
    displayDict["jp"].config_musicvol_label = u"BGM音量"
    displayDict["jp"].config_musicvol_jukebox_label = u"音量"
    displayDict["jp"].config_sfxvol_label = u"SE音量"
    displayDict["jp"].config_sfxtest_label = u"テスト"
    displayDict["jp"].config_gamepad_label = u"ゲームパッド設定…"





    displayDict["jp"].config_language_sel = jpw(u"言語選択…")
    displayDict["jp"].config_language_caption = jpw(u"設定 > 言語選択")
    displayDict["jp"].config_language_restart_note = jpw(u"注意：セッション中に言語を変更すると、ゲーム進行が章の最初に戻ります。")

    displayDict["jp"].gamepad_caption = u"設定 > ゲームパッド設定"
    displayDict["jp"].gamepad_key_na = u"未定義"
    displayDict["jp"].gamepad_request_key = u"“%s” に割り当てる\nボタンを押して下さい\nセレクトボタンまたは\nクリックで解除します"

    displayDict["jp"].yesno_yes = u"はい"
    displayDict["jp"].yesno_no = u"いいえ"
    displayDict["jp"].yesno_okay = u"続ける"
    displayDict["jp"].yesno_savesuccess = u"\nセーブが完了しました。"
    displayDict["jp"].yesno_quit = u"\nゲームを終了しますか？"
    displayDict["jp"].yesno_return_to_main = u"\nタイトル画面に戻りますか？"
    displayDict["jp"].save_page_caption = u"セーブ"
    displayDict["jp"].new_save_button = u"状態をセーブする"
    displayDict["jp"].load_page_caption = u"ロード"
    displayDict["jp"].yesno_load_in_game = u"状態が失われますが\nよろしいですか？"
    displayDict["jp"].yesno_save_overwrite = u"セーブデータを上書きしても\nよろしいですか？"
    displayDict["jp"].yesno_delete_savegame = u"このデータを削除しても\nよろしいですか？"
    displayDict["jp"].play_time_label = u"経過時間"
    displayDict["jp"].show_manual_saves = u"手動"
    displayDict["jp"].show_auto_saves = u"自動"

    displayDict["jp"].text_history_caption = u"テキストログ"
    displayDict["jp"].text_history_note = u"メモ"

    displayDict["jp"].extra_menu_caption = u"おまけ"
    displayDict["jp"].extra_music_button_label = u"音楽室"
    displayDict["jp"].extra_gallery_button_label = u"美術室"
    displayDict["jp"].extra_scene_button_label = u"図書室"
    displayDict["jp"].extra_omake_button_label = u"おまけ"
    displayDict["jp"].extra_opening_button_label = u"視聴覚室"
    displayDict["jp"].commentary_label = u"コメンタリー表示"

    displayDict["jp"].video_page_caption = "おまけ > 視聴覚室"


    displayDict["jp"].music_page_caption = u"おまけ > 音楽室"
    displayDict["jp"].music_stop_button_text = u"停止"
    displayDict["jp"].music_now_playing = u"演奏中"

    displayDict["jp"].gallery_page_caption = u"おまけ > 美術室"
    displayDict["jp"].gallery_onelocked = u"残りCG：1"
    displayDict["jp"].gallery_manylocked = u"残りCG：%d"
    displayDict["jp"].gallery_singlelocked = u"CG %d / %d はロックされています"
    displayDict["jp"].gallery_num_page_prefix = u"{size=17}ページ {/size}" 
    displayDict["jp"].gallery_num_page_error = u"表示するCGがありません"

    displayDict["jp"].scene_page_caption = u"おまけ > 図書室"
    displayDict["jp"].scene_completion_label = u"進捗率: %s%%"
    displayDict["jp"].scene_playthrough_label = u"リプレイフローを使用 (推奨)"
    displayDict["jp"].scene_launch_path = "ルートを最初から\n開始しますか？"


    displayDict["jp"].joy_left = u"左"
    displayDict["jp"].joy_right = u"右"
    displayDict["jp"].joy_up = u"上"
    displayDict["jp"].joy_down = u"下"
    displayDict["jp"].joy_dismiss = u"選択／読む"
    displayDict["jp"].joy_rollback = u"テキストログ"
    displayDict["jp"].joy_holdskip = u"押している間スキップ"
    displayDict["jp"].joy_toggleskip = u"スキップモード"
    displayDict["jp"].joy_hide = u"ウインドウ消去"
    displayDict["jp"].joy_menu = u"メニュー表示"



    displayDict["jp"].name_hi = u"久夫"

    displayDict["jp"].name_ha = u"華子"
    displayDict["jp"].name_emi = u"笑美"
    displayDict["jp"].name_rin = u"琳"
    displayDict["jp"].name_li = u"リリー"
    displayDict["jp"].name_shi = u"静音"
    displayDict["jp"].name_mi = u"ミーシャ"

    displayDict["jp"].name_ke = u"健二"
    displayDict["jp"].name_mu = u"武藤"
    displayDict["jp"].name_nk = u"ナース"
    displayDict["jp"].name_no = u"野宮"
    displayDict["jp"].name_yu = u"優子"
    displayDict["jp"].name_sa = u"さえ"
    displayDict["jp"].name_aki = u"晃"
    displayDict["jp"].name_hh = u"秀明"
    displayDict["jp"].name_hx = u"治五郎"
    displayDict["jp"].name_emm = u"芽依子"
    displayDict["jp"].name_sk = "店主"
    displayDict["jp"].name_mk = "美貴"

    displayDict["jp"].name_mystery = "？？？"

    displayDict["jp"].name_ha_ = u"紫色の髪の少女"
    displayDict["jp"].name_emi_ = u"ツインテールの少女"
    displayDict["jp"].name_rin_ = u"謎の少女"
    displayDict["jp"].name_li_ = u"ウェーブヘアの少女"
    displayDict["jp"].name_mi_ = u"笑っている少女"
    displayDict["jp"].name_ke_ = u"眼鏡をかけた生徒"
    displayDict["jp"].name_mu_ = u"背の高い男"
    displayDict["jp"].name_yu_ = u"司書"
    displayDict["jp"].name_no_ = u"白髪の男"
    displayDict["jp"].name_sa_ = u"画廊のオーナー"
    displayDict["jp"].name_aki_ = u"身なりの良い人"
    displayDict["jp"].name_nk_ = u"笑っている男"
    displayDict["jp"].name_hh_ = u"スリムな少女"
    displayDict["jp"].name_emm_ = u"三つ編みの女性"
    displayDict["jp"].name_hx_ = u"大男"

    displayDict["jp"].videos = ((u"オープニング", "video/base_op_1.mp4"),
                                (u"笑美", "video/base_tc_act2_emi.mp4"),
                                (u"華子", "video/base_tc_act2_hanako.mp4"),
                                (u"リリー", "video/base_tc_act2_lilly.mp4"),
                                (u"琳", "video/base_tc_act2_rin.mp4"),
                                (u"静音", "video/base_tc_act2_shizune.mp4"),
                               )

    ##If we're on iOS we override the videos displaydict with the correct iOS videos:
    if (renpy.ios):
        displayDict["jp"].videos = (("オープニング", "video/ios_op_1.mp4"),
                                    ("笑美", "video/ios_tc_act2_emi.mp4"),
                                    ("華子", "video/ios_tc_act2_hanako.mp4"),
                                    ("リリー", "video/ios_tc_act2_lilly.mp4"),
                                    ("琳", "video/ios_tc_act2_rin.mp4"),
                                    ("静音", "video/ios_tc_act2_shizune.mp4"),
                                )



    displayDict["jp"].s_scenes = (("プロローグ", rp_actmark, rp_actmark, ("Act 1","Prologue")),
                                    ("寒空", "NOP1", "雪の降る寒い日、久夫の叶いかけた夢が、突然の心臓発作によって打ち砕かれる。", ("Act 1","Prologue")),
                                    ("失意の久夫", "NOP2", "久夫は山久学園のことを聞く。そこは、高校生活の残りを送ることになる場所。", ("Act 1","Prologue")),
                                    ("Act 1: 推定寿命", rp_actmark, rp_actmark, "Act 1"),
                                    
                                    ("入り口効果", "A1", "山久学園に足を踏み入れた久夫は、学級担任の武藤と会う。", "Act 1"),
                                    
                                    ("舞台上手へ", "A2", "クラスへの自己紹介、学級委員とその通訳との出会い。", "Act 1"),
                                    
                                    ("医療棟で", "A3", "ミーシャと静音に食堂へと案内された後、久夫はナースに会いに行く。", "Act 1"),
                                    
                                    ("空虚な部屋", "A4", "久夫は新しい部屋に移る途中、隣室の健二と会う。", "Act 1"),
                                    
                                    ("おしゃべり", "A5", "静音とミーシャは、久夫に学園祭が近いことを教え、昼食に誘う。", "Act 1"),
                                    
                                    ("リスクと報酬", "A6", "静音と久夫は、世界制覇を賭けたゲーム「リスク」で戦う。", "Act 1"),
                                    
                                    ("安らぎの紅茶", "A7", "図書室を探していて迷った久夫は、空き教室でリリーと出会う。", "Act 1"),
                                    
                                    ("図書室で二人", "A8", "図書室にたどり着いた久夫は華子と出会うが、彼女は怯えて逃げてしまう。", "Act 1"),
                                    
                                    ("奇怪千万", "A9", "健二が山久の隠された秘密を打ち明ける。", "Act 1"),
                                    
                                    ("昼ごはん進化論", "A10", "昼食を食べる場所を決める前に、静音とミーシャは久夫を生徒会に勧誘する。", "Act 1"),
                                    
                                    ("鋭い衝撃", "A11_1", "ミーシャと静音と一緒に昼食に行こうとした久夫は、廊下で笑美と衝突する。", "Act 1"),
                                    
                                    ("最悪の出会い", "A11_2", "華子とリリーと一緒に昼食に行こうとした久夫は、走ってきた笑美と衝突する。", "Act 1"),
                                    
                                    ("行きつく所へ", "A12", "静音とミーシャは、2人のお気に入りの茶館『上海』に久夫を連れていく。", "Act 1"),
                                    
                                    ("ティータイム (その1)", "A13", "久夫はリリーと華子と一緒に、穏やかな昼食をとる。", "Act 1"), 
                                    
                                    ("習慣形成", "A15", "武藤は久夫に大事な話をしようとするが、ミーシャが割り込んで久夫に用事を頼む。", "Act 1"),
                                    
                                    ("遅弁", "A16", "資材を探していると、久夫は美術室で風変わりな少女と出会う。", "Act 1"),
                                    
                                    ("待ち伏せ", "A17", "琳を手伝ってペンキを運んでいると、久夫はナースに問い詰められる。", "Act 1"),
                                    
                                    ("あの緑", "A18", "久夫は琳が壁画を描くところを眺める。", "Act 1"),
                                    
                                    ("駆ける少女", "A19", "朝の運動に励もうとした久夫は、競技場のトラックで笑美と出会う。", "Act 1"),
                                    
                                    ("石鹸", "A20", "金を手に入れようとして、健二はシャワー室で久夫を狙う。", "Act 1"),
                                    
                                    ("冷戦", "A21", "静音とリリーは予算請求の件で火花を散らす。", "Act 1"),
                                    
                                    (u"やる気の証", "A22", "静音とミーシャは、生徒会に入るよう久夫をしつこく勧誘する。", "Act 1"),
                                    
                                    ("事象の地平線", "A22_2", "静音とミーシャは、生徒会に入るよう久夫をしつこく勧誘する。", "Act 1"),
                                    
                                    ("さらに上を目指して", "A23_1", "久夫は生徒会の崇高な責務について講義を受ける。", "Act 1"),
                                    
                                    ("自分ができること", "A23_2", "静音とミーシャの魔の手から逃れた久夫は、またも琳を手伝う。", "Act 1"),
                                    
                                    ("ペンキ塗り", "A24", "華子と久夫は、リリーのクラスの屋台作りに協力する。", "Act 1"),
                                    
                                    ("運動", "A25", "早朝、久夫と笑美はふたたび一緒にトラックを走る。", "Act 1"),
                                    
                                    ("透明帽子", "A26", "健二は久夫に、人付き合いの仕方についての秘訣を伝授する。", "Act 1"),
                                    
                                    ("ホームグラウンドの利点", "A26_1", "静音とミーシャは、授業に行こうと部屋を出る久夫を拉致する。", "Act 1"),
                                    
                                    ("回復不可能", "A27", False, "Act 1"),
                                    
                                    ("緩やかな回復", "A27_1", "心臓の動悸から回復し、久夫はようやく授業に出席する。", "Act 1"),
                                    
                                    ("回復不可能", "A27_2", "生徒会に連れ去られた後、久夫は授業に戻ろうと悪戦苦闘する。", "Act 1"),
                                    
                                    ("無料の昼食なんてない", "A28", "正式なメンバーとして初めて、久夫は生徒会室に行く。", "Act 1"),
                                    
                                    ("足と口", "A29", "笑美は久夫を屋上まで連れて行き、琳と一緒に昼食をとる。", "Act 1"),
                                    
                                    ("足元に注意", "A30", "久夫とリリーは買い物に行き、帰り道で混乱状態の琳と会う。", "Act 1"),
                                    
                                    ("支え", "A31", "久夫にとって初めての土曜日の授業は、武藤の説教でしめくくられる。", "Act 1"),
                                    
                                    ("美学", "A32", "笑美は放課後に暇を持て余している久夫を見つけ、またしても琳の手伝いに駆り出す。", "Act 1"),
                                    
                                    ("産みの苦しみ", "A33", "琳が壁画を描いている間に、久夫は美術教師の野宮と出会う。", "Act 1"),
                                    
                                    ("適度な運動", "A34", "笑美と久夫は、健康維持の大切さについて話し合う。", "Act 1"),
                                    
                                    ("ティータイム (その2)", "A35", "暇をつぶすため、久夫は学園の周りを散歩する。", "Act 1"),
                                    
                                    ("上海航路", "A36", "静音とミーシャと一緒に『上海』へ。お茶、ケーキ、そして勝負。", "Act 1"),
                                    
                                    ("お静かに", "A37", "学園祭の前日、華子と久夫は読書をする。", "Act 1"),
                                    
                                    ("あわてるな", "A38", "学園祭当日、目を覚ました久夫はやかましく騒ぐ健二に迎えられる。", "Act 1"),
                                    
                                    ("学園祭 !", "A39", "笑美は久夫が揚げ物を食べているところを捕まえ、罰として久夫にお供をさせる。", "Act 1"),
                                    
                                    ("チェックメイト", "A42", "リリーの屋台を手伝えなかった久夫は、学園祭の中で華子を探す。", "Act 1"),
                                    
                                    ("ムーブメント", "H2", "リリーは自分の仕事を終えて、華子と久夫を上海のお茶でもてなす。", "Act 1"), 
                                    
                                    ("時の約束", "A41", "リリーの屋台で骨の折れる午前を過ごした後、久夫は彼女といっしょに華子を探す。", "Act 1"),
                                    
                                    ("私の頭の中の雲", "A40", "久夫は、琳と完成した壁画のそばで過ごす。", "Act 1"),
                                    
                                    ("ボール投げ", "A44", "約束通りに、久夫は静音とミーシャと一緒に一日を過ごす。", "Act 1"),
                                    
                                    ("どん底", "A43", "学園祭を楽しむかわりに、健二と久夫は屋上で男らしいピクニックをする。", "Act 1"),
                                    
                                    ("Act 2: フォーム", rp_actmark, rp_actmark, ("Act 2","Emi")),
                                    
                                    ("朝練", "E3", "笑美とのたくさんのランニングのはじまり。", ("Act 2","Emi")),
                                    
                                    ("雲と時間旅行と汝", "E4", "再び笑美と琳と一緒の屋上の昼食。笑美は久夫に、陸上競技会を見に行くと約束させる。", ("Act 2","Emi")),
                                    
                                    ("答えの必要な質問 !", "E5", "笑美と久夫のたわいないおしゃべり。久夫は笑美に琳との関係をもっと詳しくたずねる。", ("Act 2","Emi")),
                                    
                                    ("2度目が一番最悪", "E6", "2度目の朝のランニング。久夫はじたばた叫びながらトラックのまわりを半ばひきずられていく。", ("Act 2","Emi")),
                                    
                                    ("一日一個のリンゴ", "E7", "久夫は笑美とともにナースを訪問し、以前から2人が知り合い同士だということを知る。", ("Act 2","Emi")),
                                    
                                    ("陸上競技会", "E8", "陸上競技会の日。笑美の性格の別の側面が明らかになる。", ("Act 2","Emi")),
                                    
                                    ("その薬、今すぐ飲め", "E9", "ナースの診察の際に久夫は胸の痛みのことを話し、説教を食らう。", ("Act 2","Emi")),
                                    
                                    ("大海原の海賊稼業", "E10", "久夫は屋上で笑美と海賊稼業について話し合うが、岩魚子からの手紙が彼の一日を台無しにする。", ("Act 2","Emi")),
                                    
                                    ("名台詞", "E11", "笑美、琳、久夫の3人でピクニックに出かけるが、すぐに雨によって台無しになってしまう。", ("Act 2","Emi")),
                                    
                                    ("欠席調査", "E12", "久夫は普段通りにトラックに行くが、笑美は来ない。", ("Act 2","Emi")),
                                    
                                    ("立ち寄り", "E13", "病気の笑美を見舞いに行ったとたん、事態は急展開する。", ("Act 2","Emi")),
                                    
                                    ("事後の朝", "E14", "久夫は昨日の出来事を回想し、笑美を助けるためになにかしようと決意する。", ("Act 2","Emi")),
                                    
                                    ("（本当の）始まり", "E15", "いつも通りの、しかし琳のいない、屋上でのランチタイム。", ("Act 2","Emi")), 
                                    
                                    ("Act 3: パースペクティブ", rp_actmark, rp_actmark, ("Act 3","Emi")),
                                    
                                    (u"それは……科学です", "E16", "武藤は久夫に、将来について短い議論をする。", ("Act 3","Emi")),
                                    
                                    ("定義", "E17", "笑美と久夫はもう一度ピクニックを試みる、今度は母なる自然からの邪魔は入らない。", ("Act 3","Emi")),
                                    
                                    ("目に見えない岩", "E18", "いつも通りの、朝のトラックでの走り込み……と思いきや。", ("Act 3","Emi")),
                                    
                                    ("お昼ご飯と科学", "E19", "久夫は科学の道に進むことについて、武藤に再び相談する。", ("Act 3","Emi")),
                                    
                                    ("上がって、下がって、また上がり", "E20", "笑美からの取り乱した電話で久夫は笑美の部屋へ急ぐ。そこで2つの驚きが待っている。", ("Act 3","Emi")),
                                    
                                    ("体育倉庫", "E21", "笑美は久夫を陸上倉庫へと誘い込む。", ("Act 3","Emi")),
                                    
                                    ("放課後の予定", "E22", "次の試験について笑美は久夫と真剣な話をする。", ("Act 3","Emi")),
                                    
                                    ("切り離されて", "E23", "久夫は笑美との関係についてあれこれ考え込む。", ("Act 3","Emi")), 
                                    
                                    ("幻肢痛", "E24", "久夫が笑美に心配していることを伝えようとするが、不本意な結果に終わる。", ("Act 3","Emi")),
                                    
                                    ("議論は疑念の現れ", "E25", "久夫は、笑美の振る舞いと笑美の家への招待に混乱する。", ("Act 3","Emi")),
                                    
                                    (u"お客さんは……やっぱりなし", "E26", "茨崎家での夕食。", ("Act 3","Emi")),
                                    
                                    ("リプレイ映像", "E27", "ついにトラックで事情が明らかになる。", ("Act 3","Emi")),
                                    
                                    ("Act 4: モーション", rp_actmark, rp_actmark, ("Act 4","Emi")),
                                    
                                    ("空振り", "E28", "久夫は笑美に避けられているのではと怪しむ。", ("Act 4","Emi")),
                                    
                                    ("セービングスロー", "E29", "ついに屋上で事情が明らかになる。", ("Act 4","Emi")),
                                    
                                    ("過去のささやき", "E30", "久夫、笑美、そして笑美の母親は墓参りに出かける。", ("Act 4","Emi")),
                                    
                                    ("靴下バンザイ", "E31", "セックス、ドラッグ、しかしロックンロールはなし。", ("Act 4","Emi")),
                                    
                                    ("きれいな歯", "E32", "久夫が目を覚ますと、笑美が自分の隣で眠っている。", ("Act 4","Emi")),
                                    
                                    ("Act 2: かくれんぼ", rp_actmark, rp_actmark, ("Act 2","Hanako")),
                                    
                                    ("町へ、町へ", "H3", "華子と一緒にコンビニまでお買いもの。", ("Act 2","Hanako")),
                                    
                                    ("茶葉", "H4", "華子は、リリーと一緒に昼食を食べようと久夫を誘う。", ("Act 2","Hanako")),
                                    
                                    ("懺悔の生徒会室", "H5_1", "久夫とミーシャは華子の苦境について話し合う。", ("Act 2","Hanako")),
                                    
                                    ("チェスとジェットコースター", "H5_2", "久夫は生徒会を放り出して、華子と一緒に本を読む。", ("Act 2","Hanako")),
                                    
                                    ("朝の目覚め", "H6", "リリーからの放課後ティーパーティーへの誘い。", ("Act 2","Hanako")),
                                    
                                    ("マッド・ハッター", "H7", "華子、久夫そしてリリーは一緒に集まって、リリーの部屋で紅茶を飲む。", ("Act 2","Hanako")),
                                    
                                    ("小さな変化", "H8", "健二は借金の返済を強いられる。", ("Act 2","Hanako")),
                                    
                                    ("無断欠席", "H9", "久夫とリリーは華子の出席状況について話し合う。", ("Act 2","Hanako")),
                                    
                                    ("等価交換", "H10", "久夫の心臓について知ったことのお返しに、華子は久夫に自分の過去の一部を打ち明ける。", ("Act 2","Hanako")),
                                    
                                    ("Act 3: キャスリング", rp_actmark, rp_actmark, ("Act 3","Hanako")),
                                    
                                    ("招待", "H11", "リリーは久夫が紅茶部屋を片付けているのを見つけ、華子の誕生日のことを話す。", ("Act 3","Hanako")),
                                    
                                    ("怪しい邂逅", "H12", "過去への回想と、思いがけない美貴との雑談。", ("Act 3","Hanako")),
                                    
                                    ("アンティークとパイ", "H13", "リリーと久夫は、街でプレゼントのための買い物をする。", ("Act 3","Hanako")),
                                    
                                    ("落下", "H14", "華子が授業中にパニック発作を起こす。", ("Act 3","Hanako")),
                                    
                                    ("ゆっくりと前へ", "H15", "リリーは久夫と華子に悪い知らせを伝える。", ("Act 3","Hanako")),
                                    
                                    ("手を伸ばして", "H16", "久夫は引きこもる華子に手を差し伸べる。", ("Act 3","Hanako")),
                                    
                                    ("もう一年", "H17", "華子の誕生日を祝っていると、我らが三人衆に意外なゲストが加わる。", ("Act 3","Hanako")),
                                    
                                    ("一枚の紙片", "H18", "久夫は初めての二日酔いを味わったあと、やっかいな手紙を受け取る。", ("Act 3","Hanako")),
                                    
                                    ("ソリッドとストライプ", "H19", "ポケットビリヤードで遊ぶ間の、率直な話し合い。", ("Act 3","Hanako")),
                                    
                                    ("終わりの始まり", "H20", "リリーの旅立ち。", ("Act 3","Hanako")),
                                    
                                    ("Act 4: キズアト", rp_actmark, rp_actmark, ("Act 4","Hanako")),
                                    
                                    ("ずる休み", "H21", "生徒会との昼食、そして閉じこもる華子への憂慮。", ("Act 4","Hanako")),
                                    
                                    ("遠くにありて", "H22", "華子はさらに一日引きこもり、久夫はリリーに助言を求めて電話する。", ("Act 4","Hanako")),
                                    
                                    ("つまずき", "H23", "久夫は華子を部屋から引き出そうとするが、驚愕する結果になる。", ("Act 4","Hanako")),
                                    
                                    ("切られた花弁", "H24", "久夫は、華子との自分の未来の関係が、早すぎる終わりを告げたことを知る。", ("Act 4","Hanako")),
                                    
                                    ("続くメロディ", "H25", "華子はクラスに戻り、久夫は安心する。", ("Act 4","Hanako")),
                                    
                                    ("上海で勉強", "H26", "気が散らないように、久夫は上海で勉強しようとする。", ("Act 4","Hanako")),
                                    
                                    ("彼の過去", "H27", "華子ともっと親しくなるために、久夫は自分の過去を華子と分かち合う。", ("Act 4","Hanako")),
                                    
                                    ("シティ・ランデブー", "H28", "2人は街でデートする。", ("Act 4","Hanako")),
                                    
                                    ("ささやきと接触", "H29", "久夫と華子は一夜を共に過ごす。", ("Act 4","Hanako")),
                                    
                                    ("不確かな未来", "H30", "昨夜の出来事が久夫に重くのしかかる。", ("Act 4","Hanako")),
                                    
                                    ("成熟", "H31", "2人の子供たちの終わり、2人の大人たちの始まり。", ("Act 4","Hanako")),
                                    
                                    ("Act 2: 過去", rp_actmark, rp_actmark, ("Act 2","Lilly")),
                                    
                                    ("アールグレイ", "L1", "昨日の疲れから回復し、久夫は華子とリリーと一緒の昼休みの最初の一日を、共に過ごす。", ("Act 2","Lilly")),
                                    
                                    ("1ポンド貨", "L2", "健二からリリーの国籍を問われた久夫は、それよりもっと詳しく調べようとする。", ("Act 2","Lilly")),
                                    
                                    ("プレゼントと存在", "L3", "華子のプレゼントを探している間、リリーと久夫は晃と彼女のいとこに出会う。", ("Act 2","Lilly")),
                                    
                                    ("未確認飲料物体", "L4", "3人は華子のために誕生日パーティーを開くが、きょうだいの突然の登場に中断される。", ("Act 2","Lilly")),
                                    
                                    ("あくる日", "L5", "目覚めた久夫とリリーは、昨夜の出来事から回復しようとする。", ("Act 2","Lilly")),
                                    
                                    ("華子、『タイム』を所望する", "L6", "久夫とリリーは食料品を買いに出かける。", ("Act 2","Lilly")),
                                    
                                    ("小さな翼", "L7", "屋上でみんなと分け合う昼食は残念な展開になる。", ("Act 2","Lilly")),
                                    
                                    ("旅立ち", "L8", "リリーと晃は見送られながら、スコットランドの家族に会いに旅立つ。", ("Act 2","Lilly")),
                                    
                                    ("Act 3: 現在", rp_actmark, rp_actmark, ("Act 3","Lilly")),
                                    
                                    ("一日、一日", "L9", "久夫はぼんやりと、リリーのいない日々が過ぎるにまかせ、山久について武藤と話す。", ("Act 3","Lilly")),
                                    
                                    ("小さな諍い", "L10", "久夫は健二と昼食をとり、気がかりなほど黙りこくっている華子にプリントを渡す。", ("Act 3","Lilly")),
                                    
                                    ("不協和音", "L11", "完全に引きこもる華子。久夫はできる限りの助けを申し出てから、リリーに電話する。", ("Act 3","Lilly")),
                                    
                                    ("遠い世界", "L12", "久夫は安心する一方、自分とリリーの関係について思いを巡らせる。", ("Act 3","Lilly")),
                                    
                                    ("再生", "L13", "久夫、華子、そして秀明は、スコットランドから帰ってきた晃とリリーを出迎える。", ("Act 3","Lilly")),
                                    
                                    ("北への旅", "L14", "3人で、北海道での休暇。", ("Act 3","Lilly")),
                                    
                                    ("前奏", "L15", "朝の散歩から、一連の出来事が始まる。", ("Act 3","Lilly")),
                                    
                                    ("クレッシェンド", "L16", "リリーの本当の気持ちが、果てしない黄金色の小麦畑で語られる。" , ("Act 3","Lilly")),
                                    
                                    ("ディミニュエンド", "L17", "一緒に過ごす初めての夜。", ("Act 3","Lilly")),
                                    
                                    ("前途は灰色", "L18", "夏の別荘に閉じ込められ、リリーと久夫は自分たちの関係を受け入れざるをえない。", ("Act 3","Lilly")),
                                    
                                    ("ラプソディ・イン・ブルー", "L19", "久夫が風呂に入りながらリリーとの関係を考えていると、何者かが一緒に入ってくる。", ("Act 3","Lilly")),
                                    
                                    ("一瞬の今", "L20", "山久に戻る旅路の間、久夫とリリーはぼんやりと2人で話す。", ("Act 3","Lilly")),
                                    
                                    ("Act 4: 未来", rp_actmark, rp_actmark, ("Act 4","Lilly")),
                                    
                                    ("ワルツの前のスローステップ", "L21", "学校に戻ると、北海道での出来事が話題になる。", ("Act 4","Lilly")),
                                    
                                    ("パジャマとスーツ", "L22", "日常生活に戻る。お茶会の間、晃が3人に加わる。", ("Act 4","Lilly")),
                                    
                                    ("正しい手順", "L23", "久夫とリリーはデートの約束をする。その後、晃が顔を出す。", ("Act 4","Lilly")),
                                    
                                    ("外出", "L24", "久夫とリリーは初めてのデートに行き、お互いの過去について知る。", ("Act 4","Lilly")),
                                    
                                    ("朝のまどろみ", "L25", "久夫とリリーは将来の抱負について話し合う。", ("Act 4","Lilly")),
                                    
                                    ("ブラックアウト", "L26", "3人は、近々やってくる休みについて考えにふけり、久夫はリリーの見ている視界を経験する。", ("Act 4","Lilly")),
                                    
                                    ("ことの成り行き", "L27", "久夫は晃に呼び出され、2人はリリーのことについて話す。", ("Act 4","Lilly")),
                                    
                                    ("遠い未来", "L28", "リリーはスコットランドの家族と一緒に暮らそうという家族の申し出を明らかにする。", ("Act 4","Lilly")),
                                    
                                    ("別れ", "L29", "2人が日本を離れる前の晩、晃とリリーにお別れを告げる。", ("Act 4","Lilly")),
                                    
                                    ("偽終止", "L30", "リリーの葛藤に気付いた久夫は、リリーに正面から向き合うために駆けつける。", ("Act 4","Lilly")),
                                    
                                    ("涙降る空の下で", "L31", "病院で目覚めた久夫は、自分の人生を受け入れようとして葛藤する。", ("Act 4","Lilly")),
                                    
                                    ("輝く空の下で", "L32", "リリーは久夫の元に戻り、2人は一緒の人生を新しく歩み始める。", ("Act 4","Lilly")),
                                    
                                    ("元気に前へ !", "L33", "リリーと久夫は晃を見送る。", ("Act 4","Lilly")),
                                    
                                    ("Act 2: すれ違い", rp_actmark, rp_actmark, ("Act 2","Rin")),
                                    
                                    ("広い視野", "R1", "久夫は昼休みを屋上で雲を見ながら琳と過ごす。", ("Act 2","Rin")),
                                    
                                    ("灰色の研究", "R2", "初めての美術部の活動で、琳と久夫はお互いのポートレートを描く。", ("Act 2","Rin")),
                                    
                                    (u"割り込み", "R3", "健二は久夫に「借りた」本を貸す。", ("Act 2","Rin")),
                                    
                                    ("自習", "R4", "ミーシャと静音は授業の間、瞑想にふけりながらいたずら書きをしている久夫を捕まえる。", ("Act 2","Rin")),
                                    
                                    ("久夫の笑顔", "R5", "琳は久夫に、彼の幸福な表情、あるいはその欠落について話す。", ("Act 2","Rin")),
                                    
                                    ("好きなもの", "R6", "本と山久について、優子との簡単な物思い。", ("Act 2","Rin")),
                                    
                                    ("対象視聴者", "R7", "陸上競技会の日。笑美のいろいろな面と琳のいろいろな性格が明らかになる。", ("Act 2","Rin")),
                                    
                                    ("永遠の1時間", "R8", "野宮が部活動で芸術について議論を喚起する。", ("Act 2","Rin")),
                                    
                                    ("水の中、名を持つ楓", "R9", "琳は久夫を森林へといざない、そこで2人は近い将来のことをじっくり考える。", ("Act 2","Rin")),
                                    
                                    ("岩魚子の後悔", "R10", "岩魚子からの手紙が届く。", ("Act 2","Rin")),
                                    
                                    ("彼女自身のイメージで", "R11", "久夫は琳が自分の作品の展覧会を開くのを後押しする。", ("Act 2","Rin")),
                                    
                                    ("傘と論理とケーキ", "R12", "笑美、久夫そして琳は雨に降られて、上海に避難する。", ("Act 2","Rin")),
                                    
                                    ("天国に6メートル近く", "R13", "琳と久夫は、笑美がいないのが明らかなので、屋上で昼食を食べ「ない」。", ("Act 2","Rin")),
                                    
                                    ("優柔不断", "R14", "笑美は風邪を治すが、今度は琳が風邪を引いてしまう。", ("Act 2","Rin")),
                                    
                                    ("シグナル・インタフェース", "R15", "久夫は琳を部屋に訪ねる。", ("Act 2","Rin")),
                                    
                                    ("たんぽぽ", "R16", "丘の上で結論が下される。", ("Act 2","Rin")),
                                    
                                    ("Act 3: 溝", rp_actmark, rp_actmark, ("Act 3","Rin")),
                                    
                                    ("22番目の角", "R17", "美術部チームは琳の将来の展覧会のために画廊を下見する。", ("Act 3","Rin")),
                                    
                                    ("光の薫り", "R18", "久夫は美術室で眠っている琳に偶然遭遇する。", ("Act 3","Rin")),
                                    
                                    ("諦められないもの", "R19", "笑美と久夫は琳の人となりについて話し合う。", ("Act 3","Rin")),
                                    
                                    ("バターン !", "R20", "モチベーションについての、優子の考察。", ("Act 3","Rin")),
                                    
                                    ("バラ色メガネを通して", "R21", "野宮は芸術を職業とすることについて長々と説明する。", ("Act 3","Rin")),
                                    
                                    ("世界の果て", "R22", "久夫は琳に告白して、振られる。本当に？", ("Act 3","Rin")),
                                    
                                    ("琳の状況", "R23", "アトリエの奇妙でしんとした午後。", ("Act 3","Rin")),
                                    
                                    ("早送り", "R23_2", "展覧会の準備は奇妙なパターンにはまる。", ("Act 3","Rin")),
                                    
                                    ("自己破壊", "R24", "琳は創造性について新鮮な見方をするために、たばこを試す。", ("Act 3","Rin")),
                                    
                                    ("非現実逃避", "R25", "久夫は琳を夜道の散歩へと連れ出す。", ("Act 3","Rin")),
                                    
                                    ("限界の欠如", "R26", "さえと野宮は久夫に芸術家の生き様についていくつかの見識を説く。", ("Act 3","Rin")),
                                    
                                    ("錯乱", "R27", "久夫はアトリエで自暴自棄になっている琳を驚かす。", ("Act 3","Rin")),
                                    
                                    ("大嫌いなもの", "R28", "信じられない夜の不愉快な結末。", ("Act 3","Rin")),
                                    
                                    ("怒りのかけら", "R29", "緊迫した2人の関係はバラバラに吹き飛ぶ。", ("Act 3","Rin")),
                                    
                                    ("Act 4: 夢", rp_actmark, rp_actmark, ("Act 4","Rin")),
                                    
                                    ("人々のための幻想", "R30", "久夫は自分の不安を野宮に伝えるが、ほとんど効果はない。", ("Act 4","Rin")),
                                    
                                    ("物思いから醒まされて", "R31", "久夫の忍耐は終わりを迎える。", ("Act 4","Rin")),
                                    
                                    ("問題のシーン", "R32", "展覧会のオープニングでの、琳との遭遇。", ("Act 4","Rin")), 
                                    
                                    ("波長", "R35", "久夫は、試験の最終日、無気力にダラダラと過ごす。", ("Act 4","Rin")),
                                    
                                    ("青の時代", "R36", "雨の降る日、22nd Corner、そしてピカソの略史。", ("Act 4","Rin")),
                                    
                                    ("君だけに見える世界", "R37", "琳と久夫は雨のあとで、別れる。", ("Act 4","Rin")),
                                    
                                    ("絶望的な栄光", "R34", "取り乱した野宮は久夫に琳の居場所について問いただす。", ("Act 4","Rin")), 
                                    
                                    ("自己参照論理の問題", "R38", "久夫は琳が隠れているのを見つけ、野宮に謝るよう説得する。", ("Act 4","Rin")),
                                    
                                    ("影を測る", "R39", "琳の美術教師への謝罪は、歓迎されない。", ("Act 4","Rin")),
                                    
                                    (u"レゾンデートル", "R40", "久夫は動転する琳をなぐさめる。", ("Act 4","Rin")),
                                    
                                    ("息もなく、音もなく", "R41", "夏休みの初めの日に、琳が久夫の部屋にやってくる。", ("Act 4","Rin")),
                                    
                                    ("存在の証明", "R42", "たんぽぽに覆われた丘の上で、すべてがあるべき場所に収まる。", ("Act 4","Rin")),
                                    
                                    ("Act 2: 読む練習", rp_actmark, rp_actmark, ("Act 2","Shizune")),
                                    
                                    ("伝言のやりとり", "S8", "静音と久夫はコミュニケーションの手段を探る。", ("Act 2","Shizune")),
                                    
                                    ("手に向かって話しかけて", "S9", "久夫は新しい言語を勉強し始め、個人指導者が登場する。", ("Act 2","Shizune")),
                                    
                                    ("伝言ゲーム", "S10", "健二は久夫に無理矢理頼み事をするが、久夫はさまざまな困難に見舞われる。", ("Act 2","Shizune")),
                                    
                                    ("上級ゲーム理論", "S11", "もうリスクゲームでは静音の飢えを満たせない。さらに新しい敵までもが登場する。", ("Act 2","Shizune")),
                                    
                                    ("じゃん・けん・パン", "S12", "一切れのパンが突然強烈な興味の対象になり、けだるげな午後が劇的なものに変わる。", ("Act 2","Shizune")),
                                    
                                    ("インターフェイス", "S13", "静音と久夫はつながりを見出す。", ("Act 2","Shizune")),
                                    
                                    ("即時対応", "S14", "久夫はリリーと静音の仲裁をするはめになるが、幸い最後には丸く収まる。", ("Act 2","Shizune")),
                                    
                                    ("過去不完全型", "S15", "上海でくつろいでいる間、生徒会は過去の年月を回想する。", ("Act 2","Shizune")),
                                    
                                    ("星々が抱き合うとき", "S16", "ついに七夕の日が来た！", ("Act 2","Shizune")),
                                    
                                    ("Act 3: 器用な手つき", rp_actmark, rp_actmark, ("Act 3","Shizune")),
                                    
                                    ("フォースフィードバック", "S17", "久夫は静音が実家に戻るのを知って、ついて行くことに成功する。", ("Act 3","Shizune")),
                                    
                                    ("国際連合", "S18", "静音の実家への旅、彼女の弟との出会い、そして突然の魚釣り競争。", ("Act 3","Shizune")),
                                    
                                    ("使用と言及の区別", "S19", "秀明は久夫をもてなそうとするが、あまりうまくいかない。", ("Act 3","Shizune")),
                                    
                                    ("家族陰謀", "S20", "我らが三人衆は静音の父に会い、すぐさま早々に引き上げる。", ("Act 3","Shizune")),
                                    
                                    ("パングラム", "S21", "秀明の手話を学びたいという要望は、治五郎との怒鳴りあいという予想外の事態に発展する。", ("Act 3","Shizune")),
                                    
                                    ("もっとそばに", "S22", "静音と久夫は、はじめて、ひとつになる。", ("Act 3","Shizune")),
                                    
                                    ("対決", "S23", "治五郎が生徒会を過小評価するので、久夫はその挑戦を受けて立つ。", ("Act 3","Shizune")),
                                    
                                    ("錨", "S24", "山久に戻る。岩魚子からの手紙と、ガールフレンドの詳細について健二の長話。", ("Act 3","Shizune")),
                                    
                                    ("ロードマップ", "S25", "生徒会は自分たちの後任について心配し、久夫はなぜかミーシャにパフェをおごるはめになる。", ("Act 3","Shizune")), 
                                    
                                    ("鋭角三角関係", "S26", "静音との午後の仕事で、久夫は静音とミーシャの仲がぎくしゃくしていることを見て取る。", ("Act 3","Shizune")),
                                    
                                    ("十進分類法", "S27", "優子は久夫に図書室の番を頼む。健二の到着で、その試みは半分失敗、半分成功する。", ("Act 3","Shizune")),
                                    
                                    ("もつれる舌", "S28", "ミーシャは久夫を部屋に訪ねる。そして物事は予想しない方向へ向かう。", ("Act 3","Shizune")),
                                    
                                    ("脇を見て", "S29_1", "久夫は落ち込んだミーシャと屋上で出会う。そしてミーシャと静音を無理矢理引き合わせる。", ("Act 3","Shizune")),
                                    
                                    ("正面を見て", "S29_2", "久夫は落ち込んだミーシャと屋上で出会う。静音は2人に合流し、みんなを仕事にひき戻す。", ("Act 3","Shizune")),
                                    
                                    ("Act 4: もう一人の私へ", rp_actmark, rp_actmark, ("Act 4","Shizune")),
                                    
                                    ("大戦略", "S30", "静音は久夫に自身の目標と失敗を告白する。", ("Act 4","Shizune")),
                                    
                                    ("わずかなずれ", "S31", "ミーシャを元気づけようという失敗した試みは、久夫と静音の即興デートに変化する。", ("Act 4","Shizune")),
                                    
                                    ("侵略", "S32", "治五郎と秀明が突然静音を訪れるが、どこか不愉快なものに終わる。", ("Act 4","Shizune")),
                                    
                                    ("パフェ", "S33", "久夫と静音はミーシャのあとをつける。久夫はとうとうミーシャを追い詰め、きちんと話をする。", ("Act 4","Shizune")),
                                    
                                    ("現在形", "S38", "久夫は昼食の時、リリーに偶然出会い、2人は静音について話す。", ("Act 4","Shizune")), 
                                    
                                    ("らせん", "S39", "その場しのぎの言い逃れ、はぐらかし、そして健二の夜襲。", ("Act 4","Shizune")),
                                    
                                    ("終焉", "S40", "沈黙の学園で静音と早朝の会話。", ("Act 4","Shizune")),
                                    
                                    ("頂点", "S34", "健二と静音が久夫の部屋で邂逅する。奇跡的に、何も爆発しない。", ("Act 4","Shizune")), 
                                    
                                    ("引き継ぎ", "S35", "「課外活動」に従事する前に、在任中の生徒会が後任を鍛え上げる。", ("Act 4","Shizune")),
                                    
                                    ("隠密行動", "S36", "ミーシャが示した決意は、静音がより広い物事に目を向けるのに拍車をかける。", ("Act 4","Shizune")),
                                    
                                    ("無限", "S37", "卒業を間近に控え、我らが3人は友情を新しくする。", ("Act 4","Shizune")),
                                    )




    displayDict["jp"].creditstring = u"""{image=ui/flourish_left.png} {b}ライター{/b} {image=ui/flourish_right.png}
Anonymous22
Aura
cpl_crud
Suriko
TheHivemind

{image=ui/flourish_left.png} {b}編集{/b} {image=ui/flourish_right.png}
Kagami
Losstarot
Silentcook

{image=ui/flourish_left.png} {b}音楽{/b} {image=ui/flourish_right.png}
Blue123
NicolArmarfi

{image=ui/flourish_left.png} {b}美術{/b} {image=ui/flourish_right.png}
gebyy-terar
Kamifish
moekki
pimmy
raemz
Raide

{image=ui/flourish_left.png} {b}美術補{/b} {image=ui/flourish_right.png}
climatic
Doomfest
yujovi

{image=ui/flourish_left.png} {b}アニメーション{/b} {image=ui/flourish_right.png}
Mike Inel

{image=ui/flourish_left.png} {b}ディレクション{/b} {image=ui/flourish_right.png}
delta
Raide
yujovi

{image=ui/flourish_left.png} {b}技術{/b} {image=ui/flourish_right.png}
delta

{image=ui/flourish_left.png} {b}翻訳{/b} {image=ui/flourish_right.png}
a-park
Ace Toyoda
an tuck
Blackmountain Big
colul
Daice
EEE boy
gaksh
hardwired Okano
hatayan
hir
Koumoto
KyoDong Ryo
laich
Mirai
Nishimori Reo
Nagi
naita
Rushhh
tomoya
TextAdventureFreak
TK
zig5z7
秋茄子トマト
ゴン太

{image=ui/flourish_left.png} {b}プロデューサー{/b} {image=ui/flourish_right.png}
cpl_crud
Suriko


{image=ui/flourish_center.png}


{image=ui/flourish_left.png} {b}謝辞{/b} {image=ui/flourish_right.png}
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

{image=ui/flourish_left.png} {b}スペシャルサンクス{/b} {image=ui/flourish_right.png}
hir
PyTom
RAITA"""


    displayDict["jp"].drugs_wordlist  =  [u"ジソピラミド",
                        u"ワルファリン",
                        u"ジルチアゼム",
                        u"フェロジピン",
                        u"プロプラノロール",
                        u"ペンブトロール",
                        u"カルテオロール",
                        u"プロカインアミド",
                        u"ヘパリン",
                        u"フェニトイン",
                        u"ベラパミル",
                        u"キニジン",
                        u"フレカイニド",
                        u"5mg/日",
                        u"400mg/日",
                        u"15ml/日",
                        u"100mg/日",
                        u"10ml/48時間",
                        u"10ml/日",
                        u"200mg/12時間",
                        u"50mg/12時間",
                        u"500mg/48時間",
                        u"125mg/12時間",
                        u"25ml/日",
                        u"悪夢",
                        u"集中力低下",
                        u"徐脈",
                        u"鬱病",
                        u"不眠症",
                        u"勃起不全",
                        u"視覚異常",
                        u"心臓麻痺",
                        u"悪心",
                        u"眩暈",
                        u"幻覚",
                        u"気管支痙攣",
                        u"呼吸困難",
                        u"疲労",
                        u"低血圧",
                        u"心臓ブロック",
                        u"四肢冷感",
                        u"下痢",
                        u"心停止",
                        u"心室細動",
                        u"失調症",
                        u"喘息"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
