
label jp_L21:

window hide None

scene bg school_scienceroom
with locationchange

nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5, 1.0, channel="music")
play music music_normal fadein 1.0



n "\n\n\n北海道旅行を存分に楽しんだ後では、こんなにも早く日常生活に戻ってくるのがおかしな感じがする。まさしく、いつもと全く変わらない、普通の一日みたいだ。"



n "\nまあとにかく、俺はそう思いたい。"


n "\n本当のことを言うと、クラス全体、いや、学校全体の雰囲気が変わってしまっている。"



n "以前も静かな恐怖がひっそりと教室内に充満していたけど、試験が目の前に迫る今となっては、普段はめったにお目にかかれない、必死に勉強をする光景がひろがっている。"





n "試験が始まるまであと一日しかない。勉強をする代わりに北への旅行で時間を浪費したことが本当に恐ろしい。俺たちはあんなに模範的な生徒だったっていうのに。"


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

show misha invis_close:
    xanchor 0.5 xpos -0.1
with None

show misha perky_confused_close:
    xpos 0.1
show bg school_scienceroom at bgright
with dissolvecharamove

window show



"教室内を見回してみると、あの元気でいつも活気に満ちていたミーシャまで妙にしょんぼりしているみたいだ。武藤先生が教壇に立って授業をしているあいだ、ミーシャは神経質そうにペンを噛んでいる。"




"いや待て……よく見ると、本当に食べているみたいだぞ。"


show misha invis_close:
    xpos -0.1
show bg school_scienceroom at center
with dissolvecharamove

hide misha
with None



"その気の毒な光景から目を引き離して、俺は他へと注意を向ける。"



show hanako invis:
    xanchor 0.5 xpos 1.1
with None

show hanako defarms_strain:
    xpos 0.94
show bg school_scienceroom at bgleft
with dissolvecharamove




"華子はノートに食い入るように顔を近づけながら、大急ぎで書き殴っている。武藤先生の口から出る言葉を一言一句書きつけようとしているみたいだ。"



show shizu invis:
    xanchor 0.5 xpos 0.0
show misha invis_close:
    xanchor 0.5 xpos -0.1
with None

show shizu basic_normal:
    xanchor 0.5 xpos 0.3
show misha perky_confused_close:
    xpos 0.1
show hanako invis:
    xpos 1.1
show bg school_scienceroom at bgright
with dissolvecharamove

hide hanako
with None


"静音は、ええと……静音だ。落ち着き払った様子で、全ての注意を教室の前方に向けながら黙々とノートを取っている。"




"本当なら俺もそうしていないといけないところだ。でも今の授業の内容は大体把握できているという確信が俺にはあった。"





"リリーはどうしてるかなあ。頭はいいけど、俺と違って他にもやることがたくさんある。学級委員の仕事に、華子の世話に、他の人付き合いに、英語の独習……本当にいろいろなことをやってるよな。"



scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell




"昼休みのチャイムが鳴り、教室中からほっとしたため息が漏れる。武藤先生も例外じゃない。"
"たった今までやっていた、試験対策の授業の慌ただしいペースより、普段の授業のもっとのんびりした雰囲気の方が先生の好みなんだろうという気がする。"




mi "ひっちゃ～ん……"

show misha invis_close:
    xanchor 0.5 xpos 0.1
with None

show misha perky_sad_close at twoleft
show bg school_scienceroom at bgright
with dissolvecharamove


mi "助けて～……"



"俺はまぶたを半分閉じて、ミーシャの希望に添うつもりは全くないことをはっきりと示す。"



mi "助けて、助けて、助けてよ～……"


hi "うまくいってないのか？"

show misha perky_confused_close
with charachange



mi "しっちゃんは大丈夫だけど、わたしもう死んじゃうかも。ひっちゃん、わたし死んじゃうの？　ひっちゃんはわたしがこの苦役で死んじゃってもいいの？"




"お涙ちょうだいかよ。ミーシャがクラス一聡明でもなければ勤勉でもないということを考えると、試験勉強に苦労しているのも無理はない。"




hi "悪いなミーシャ。でも俺も自分の勉強をしないと。それに、ミーシャと静音はこの長い連休のあいだ、一緒に勉強してたんだと思ってたけど？"




show misha sign_sad_close
with charachange



mi "週末に勉強なんてつまんないよ、ひっちゃん！　一緒に買い物に行くほうがよっぽど楽しいよね、しっちゃん？"


show shizu behind_blank at tworight behind misha
with charaenter



"このときになって初めて、静音が俺たちを見ていて、その間もミーシャがずっと腕を動かしていたらしいことに気づく。今まで気づかなかったなんて、よほどぼんやりしていたに違いない。"






hi "そもそも、女の子の買い物っていったい何なんだ？ リリーと華子にも何回か付き合わされたことがあるけど"




show misha hips_grin_close
with charachange



mi "でも、結局行ったんでしょ？　買い物好きの男子って、珍しいよね～……"





hi "うーん、俺の役割はせいぜい荷物持ちだし。ミーシャみたいに買い物するのが楽しいって気持ちにはならないよ"





hi "それで、試験のことだけどさ。静音は休暇から帰って来た後、勉強してたんだよな？"

show shizu basic_normal2
with charachange


shi "……"

show misha sign_smile_close
with charachange


mi "もちろんよ、ひっちゃん。ちゃんと前もって勉強をするのが賢いやり方……"

show misha perky_sad_close
with charachange


mi "うぐぅ～"



"一番の親友にも裏切られた自分の愚かさに気づいて、ミーシャがどさっと自分の机の上に突っ伏しながら、牛の断末魔にも似た声を上げる。"


show shizu basic_angry
with charachange


"とてもいらついた表情でミーシャを見る静音の態度から察するに、彼女はたぶん自分と同じように勉強するようミーシャに言っていたんだろう。"


hi "心配するなよ、今から勉強を始めれば少しは点数も上がるぞ"


hi "たぶん"



"ミーシャにとってはあまり慰めになっていなさそうだ。まるで不朽の陽気さを持つ風船が無残にも割れてしまったみたいだ。"


show shizu behind_blank
with charachange


shi "……"

show shizu behind_blank_close
with characlose

with Pause(0.3)

show shizu adjust_frown_close
show misha perky_confused_close
with vpunch


"ふさぎ込むミーシャは静音の手話に気づいていない。肩を素早く突っつかれたミーシャが、間髪置かずに我に返る。"

show misha hips_smile_close
with charachange


mi "あっ、そうだ、それで、週末は何してたの、ひっちゃん？"


hi "ちょっとリリーと華子と一緒に北へ旅行してたんだ。結構よかったぞ"

show misha perky_smile_close
show shizu behind_blank_close
with charachange



"２人が明らかにいやらしそうに目を細めて俺を見る。２人の抱く疑惑に根拠があるという事実が、よけいに状況を気まずくする。"




hi "ただ勉強と観光してただけだぞ。それ以上のことは何もない"

show misha cross_smile_close
with charachange


mi "ふ～ん……"




"こんな見え透いたうそをついてしまった後で、今のはベストな回答じゃなかったかもと気づく。静音はリリーと親類関係だし、うそをついていると疑った相手を詰問するときは全く容赦しないし。"






"静音が俺の返答をどうとらえたのかは全くわからないけど、まあいつかは分かることだ。何はともあれ、俺が誰と付き合おうが静音の知ったことじゃないだろう。"




hi "あと、リリーと俺は今付き合ってるから"


show misha hips_grin_close
show shizu basic_normal2_close
with charachange



"そのニュースを聞いて、ミーシャは熱狂的な笑顔を見せる。静音は、冷めた表情で多少隠してはいるけど、少し驚いた様子を見せる。"


show shizu behind_blank_close
with charachange


shi "……"

show misha sign_smile_close
with charachange


mi "誰と付き合おうとひっちゃんの勝手だけど。うまくいくといいわね"



"この件について、これ以上寛大な扱いはない、という表情を見せるミーシャ。実際、俺にはこれで十分だ。"


show shizu basic_normal2_close
with charachange


"だけど、ミーシャがそう言った後、静音が何か別のことを手話で伝え始める。そして手話を止め、ミーシャに向かって首を振り翻訳しないように伝える。"

hide shizu
with charaexit

hide misha
with charaexit



"それだけで十分変に思うところだけど、ミーシャと立ち去る前に静音が不自然なくらいにさりげなく手を振ってきたので、ますます混乱する。静音は本音を隠したり、考えなしに会話したりするような人間じゃない。"





"あのコンビの奇妙な態度に肩をすくめると、華子の机に目をやる。だけど席は空っぽだ。さっきまで確かにそこにいたけど、きっと俺を待つような気分じゃなかったんだろう。"




"じゃあ１人で飯を買いに行くとするか。"


stop music fadeout 2.0

scene bg school_hallway2
with shorttimeskip



"廊下を進み、ある３人の生徒にとって第２の家となった未使用の部屋へと向かう。俺は手の中のラップで巻かれたサラダロールとジュースを悲しみの目で見下ろす。"





"食堂の飯には全く食欲をそそられない。これはさっき犯した過ちに対する罰と考えることにするか。"







"ドアを開けると、予想とは違って物静かな人物の姿が１人足りないのに気づく。"

scene ev lilly_tearoom
with whiteout

play music music_lilly fadein 3.0



"おかしな気分だ。知り合ってもう何か月にもなるのに、最初にこのドアを開けて日の光の中に静かにたたずむリリーに出会った時のことを思い起こさずにはいられない。"


show ev lilly_tearoom_open
with charachange



"あの時もそうしたように、リリーはゆっくりと目を開け、まなざしを動かすことなく、穏やかに俺に話しかける。"



li "おはようございます、久夫さん"


hi "もう昼だと思うけど"


hi "華子来なかった？　俺が気づく前にさっさと教室を出て行っちゃったんだ"

scene bg school_miyagi
show lilly basic_listen_close:
    center
    ypos 1.1
with locationchange



"リリーは考え込むように両手で頬杖をつく。俺が席に着くと、机の一番近い脚にかばんをもたせかけ、満足とはほど遠い食事を俺の前にきちんと並べる。"


show lilly basic_reminisce_close
with charachange


li "来ましたよ……さっき。試験勉強をしなければいけないからと言って、図書室に行ってしまったけれど"





"俺もリリーも、華子の言うことを完全には信じていない。"




hi "まあ、少なくとも華子の意図は正しいほうに向いてるわけだ"


show lilly basic_concerned_close
with charachange



li "華ちゃんは優しいですけど、こんなに私たちに気を使う必要はないんです。一度このことについて話そうと思います"




hi "それがいいな、たぶん"

show lilly basic_weaksmile_close
with charachange





"しばらくのあいだ、黙ったまま昼食を取る。リリーは優雅にサンドイッチを口にし、紅茶をすする。俺は乾いたパン生地に挟まれた庭みたいな味がするものを食べる。"







"雰囲気が少し張り詰めているように感じる。軽いおしゃべりが途切れてしまった今、俺たち２人ともお互いに何を話せばいいのかよくわからない。"



"やがて俺もリリーも昼食を食べ終わる。会話が途切れたまま、しばらく時が過ぎる。だけどついに、リリーの柔らかな声が沈黙を破る。"


show lilly basic_reminisce_close
with charachange



li "あの時、いろんなことがありました……ね？"



hi "うん"



"再び沈黙。２人とも同じことについて考えているけど、俺は自分の気持ちの整理はついていると思う。"




hi "成り行きがちょっと急だったと思うけど……北海道で起こったこと、俺は何も後悔してないよ。何ひとつ"


show lilly basic_oops_close
with charachange


li "久夫さん……？"



"少し緊張しながら、リリーの両手を取る。半分は彼女を感じるために、もう半分は俺の気持ちを落ち着かせるために。"




hi "あの時の言葉は嘘じゃないよ、リリー。君が好きだ。リリーを置いてどこにも行ったりしない。俺の望みは、リリーも同じ考えでいてほしいってだけだ"


show lilly basic_weaksmile_close
with charachange



"長い間、永遠とも思えるような間、リリーは静かに考え込む。"


show lilly invis_close at center
with dissolvecharamove


"物思いにふけっていたリリーがふいに自分の片手を俺の手の中から引き、その上に乗せる。そのまま前方に体を伸ばし、椅子から立ち上がる。"



"ほんの少しためらった後、リリーが少し物憂げな表情を見せ、その唇がわずかな間だけ俺の唇に触れる。"


show lilly behind_cheerful_close:
    ypos 1.1
with dissolvecharamove



"その瞬間、まるで思考が停止してしまったような感じがする。再び椅子に座って頬をほんのりと赤く染めながら俺に笑いかけているリリーにも、ほとんど気づかない。"




show lilly basic_smileclosed_close
with charachange



li "そう言ってくれて、とても幸せです、久夫さん。一緒にいられたら嬉しいです"




hi "今までより、もう少しスローダウンした方がいいかもしれないな。まだ学校も、試験もあるんだし"


show lilly basic_giggle_close
with charachange



"リリーがいたずらっぽく、くすくすと笑う。俺もつられて笑ってしまう。"



show lilly basic_smileclosed_close
with charachange



li "確かにいい考えかもしれませんね"


show lilly basic_smile_close
with charachange


li "久夫さんは試験は自信ありますか？　久夫さんの言うとおり、試験まであと一日しかないけれど"


hi "もうちょっと勉強すべきだったとは思うけど、まあ何とかなると思うよ"


hi "そうは言っても、ミーシャと静音を追い払わなきゃいけなかったけど。リリーのクラスも、うちと同じくらい試験の心配してるの？"



show lilly basic_weaksmile_close
with charachange


"それが図星だと言わんばかりに、リリーがうんざりしたようなため息を漏らす。場の雰囲気が少し軽くなって、俺はほっとする。"



li "ええ、そうですね。もう２人のクラスメイトから助けを頼まれましたよ。もっと増えるでしょうね"



hi "たぶん、教師になるための最初の訓練と考えたらいいんじゃないかな？"

show lilly basic_smile_close
with charachange



li "そういうとらえ方をする方がいいんでしょうね"


show lilly basic_smileclosed_close
with charachange



li "ところで、久夫さんは英語の勉強はどうですか？　たしか久夫さんの得意教科とはほど遠かったと思いますけど。母と話すために暗記した少しの文だけでは十分ではないでしょうし"




"くそっ、ドンピシャだ。"



hi "まいったな。もしよかったら、ひょっとしたらその件について助けていただけたりしませんか？　お願いしますよ？"



show lilly basic_planned_close
with charachange



li "喜んでお助けいたしますわ、久夫さん。だけど、そのかわり……"




"リリーがじっとりとした目で俺を見る。彼女のなまめかしい側面が一瞬だけ表に現れる。"






hi "もちろんさ。でも勉強について言えば、リリーも助けを借りる方がいいと思うけどな"


show lilly behind_cheerful_close
with charachange



"リリーが笑顔を投げかける。その女の子っぽい勝ち誇りぶりに俺の顔は赤くなる。リリーはどういう表情を見せれば俺の気持ちを操れるか分かってるんだろう。もうちょっと警戒した方がよさそうだ。"




"だけど差し当たっては、２人で勉強することはお互いの苦手な部分を補い合うのに好都合ともいえる。"

play sound sfx_warningbell



"チャイムが鳴り、時が立ち止まってはくれないことを俺たちは思い出す。"




hi "はあ、もう昼休みも終わりか。ここにいると、つい時間を忘れちゃうな"

show lilly basic_weaksmile_close
with charachange



li "この部屋は他のクラブや活動の場からはとても離れているから、ほとんど何も聞こえてきません。きっとそれが大きな理由でしょうね"


show lilly basic_weaksmile_close at center
with charamove



"他の誰からも遠く離れ、ただ彼女の愛する人物だけが一緒にいる。リリーが立ち上がってかばんと杖を取ろうとしているあいだ、俺の心は北海道で過ごした時の思い出へと旅立っている。"



show lilly basic_satisfied_close
with charachange



li "そうだ、教室に戻る前に。明日、部屋で姉さんと私でおかえりパーティをするんです。久夫さんも来てくれますか？"






"……そしてまた戻ってくる。"



hi "他に予定もないし、勉強時間の合間でも十分時間を取れると思うよ"


show lilly basic_smileclosed_close
with charachange


li "それを聞けて嬉しいですよ、久夫さん"


hi "何はともあれ、リリーがスコットランドから帰ってきてくれて嬉しいよ。試験が終わったら、俺たちももっと２人の時間を持てるだろうし"

show lilly basic_smile_close
with charachange


li "ええ。すぐに休みも始まりますしね"


hi "じゃあ、休みは七夕祭りから始めるか。学園祭の時に約束したよな"

show lilly basic_arablush_close
with charachange


"リリーがあの時の出来事を思い出し、手を頬に持っていくと少しおどおどした調子で笑う。俺はそのことを思い出せた自分自身にこっそり感謝する。"



"リリーがこんな反応をするのは俺には奇妙に思える。彼女が困惑した様子を見せるのはこれが初めてではないけど。"

show lilly basic_weaksmile_close
with charachange


li "もう……行かないと。さようなら、久夫さん"


hi "じゃあな"

hide lilly
with charaexit

stop music fadeout 6.0



"ただの習慣なのか、あるいは意地でも普段のささいなしぐさを続けたいだけなのか、俺はいつもと同じ調子で手を上げて別れを告げる。少なくとも今、自分がそうしていることは自覚している。"




"俺は今までにないくらい大きな展望を見い出し始めていると思う。リリーとのことだけじゃなく、将来の人生についても。"


"ようやく過去のしがらみから解き放たれようとしているんだ。"

scene black
with dissolve




label jp_L22:

$ renpy.music.set_volume(0.8, 0.0, channel="music")
play music music_ease fadein 4.0

scene bg school_girlsdormhall
with locationchange


"今では少し慣れ親しんだ女子寮の廊下を歩いていくと、前方からかすかに笑い声が聞こえてくる。"

show bg school_girlsdormhall at bgleft
with charamove



"その声がリリーの部屋からのものだと気づくのにそう時間はかからない。低い女の人の声色は明らかにリリーでなく、晃さんのものだけど。"


play sound sfx_doorknock2



"いつも通りに、拳でドアを軽く３回叩いたとたんに、すごい勢いでドアが開く。"



show akira invis:
    xanchor 0.5 xpos 1.0
with None

show akira basic_smile:
    xpos 0.9
with dissolvecharamove


aki "よう、久夫"


hi "どうも。やあ、リリー、華子"

scene ev lilly_bedroom:
    truecenter
    zoom 1.0 subpixel True
    acdc_warp 8.0 zoom 1.03
with locationchange



"華子がためらいがちに俺を見上げる。彼女の手はぶかぶかのピンク色の寝巻に埋まってしまっている。リリーは自分のいる側から俺の声のする方へと顔を横に向けて微笑む。"





"俺がパジャマ姿のリリーの光景を嫌いだと言ったら、それは明らかな嘘だ。"



"知ったような顔をして横目でこっちを見ながらニヤニヤしている晃さんに気づいて、俺はキッとにらみ返す。"


scene bg school_dormlilly at bgleft
with locationchange




"俺の意図を汲んで、晃さんは肩をすくめながら部屋の真ん中にあるローテーブルに戻る。俺もそこに加わると、リリーが会釈をして俺に紅茶を注いでくれる。"



show hanagown distant:
    twoleft
    ypos 1.14
show akira basic_smile:
    tworight
    ypos 1.14
with charaenter



hi "また会えて嬉しいよ、華子。最近はいろんな人と関わってるみたいだな"





"リリーは集中した顔つきで、いつものように指で注意深く測りながら、薄茶色の液体をティーポットからカップへと注いでいく。"




li "華ちゃんは、新聞部で久夫さんたちのクラスメイトの人を手伝っているみたいですよ。直美さん、でしたっけ？"


show hanagown normal
with charachange


"華子が同意するようにうなずく。"



"もう２か月も教室で一緒に過ごしているのに、ほとんど会話をしないクラスメイトの名前は今でもなかなか覚えられずにいる。"




"顔と名前を一致させるのにしばらく思考をこねくり回す必要があったけど、俺はついに教室の後ろの方で、華子の隣の席に座っている女子を思い出す。"




"井上直美。見かけはかなり平凡な子だ。染められた金髪以外は。"





"井上の陽気でまっすぐな性格を考えると、華子から入部について聞かれた時に、即座にそれを新聞部へ引き入れるチャンスと見て取ったのかもしれない。"




"どっちにしろ、自分の可能性を広げている華子を見られて嬉しい。初めて華子に会った時なんか、華子がリリー以外の誰かとクラブに参加するなんて、どう考えても笑い話だと思っただろう。"



hi "それで忙しそうにしてたのか。楽しい？"

show hanagown smile
with charachange



ha "えっと。すごく……面白いよ"




"いつものように、華子はおしゃべりとは程遠い。世の中には決して変わらないものがあるけど、華子の性格はその一つのように思える。これからもずっと、社交的になりすぎることを避け続けるのだろう。"


show hanagown smile:
    center
    ypos 1.14
show akira basic_smile:
    right
    ypos 1.14
show bg school_dormlilly at center
with charamove

show lilly invis at left
with None

show lilly basic_smileclosed_paj:
    ypos 1.17
with dissolvecharamove



"リリーが紅茶を俺の前にそっと置く。その音に気づき、俺は礼を言ってじっくりとすする。華子とリリーは自分たちのお茶に集中し、晃さんは香りの強いブラックコーヒーをマグからがぶ飲みしている。"



show akira basic_laugh
with charachange


aki "ラッキーな野郎だな、久夫"


hi "は？"


"口に押し当てたままのマグの端からもありありとうかがえる、晃さんのからかうような笑顔を見て、俺は顔をしかめずにはいられない。"

show akira basic_ending
with charachange



aki "あたしの妹のパジャマ姿を見られるなんてさ。久夫と場所を代わってほしい奴は腐るほどいるぞ"





"それよりはるかにすごいものをとっくに見てますよ。言いはしないけど。"


show lilly basic_emb_paj
with charachange


li "姉さん！"

show akira basic_smile
with charachange


aki "やあ、からかっただけだよ"



"晃さんは俺にめいっぱいもたれかかると、いじわるそうににやけながら俺に耳打ちする。"


show akira basic_kill
with charachange



aki "それに華子もな。このスケベ"




hi "ちょっと、パーティしようって言ったのはリリーですよ"


show hanagown distant_blush
with charachange


ha "あの、私……あの……"


"俺たちが華子に目を向けると、彼女はうつむいて寝巻姿の膝の上で指をもじもじさせている。"

show hanagown smile
with charachange


ha "久夫くんなら……気にしない……から……"




"あちゃあ、これはまずいぞ。華子は本当に純真だから、こういうことで深読みをしすぎたりはしないって分かってはいるけど、晃さんは明らかに恐ろしい表情を俺に向けている。"



show lilly basic_concerned_paj
show hanagown normal
with charachange


li "もう……姉さん……お願いだから……"



"リリーも、自分で見えはしなくても、晃さんの気配が突然変わったことを俺と同じくらいに感じ取れているみたいだ。"



show akira basic_boo
with charachange



"晃さんがゆっくりと俺から視線を外す。まるでぎりぎりのところで主人にひもでつながれた猟犬のようだ。安堵した俺はほっと息を漏らす。"





"話題を変えるチャンスは今しかない。"




hi "晃さん、差支えなかったら教えてほしいんですけど、晃さんはどんな仕事をしてるんですか？　スーツ姿以外の晃さんを見たことがないから"

show akira basic_laugh
with charachange


aki "卒業した後にどうしようか考えてる、そうだろ？"

show akira basic_smile
with charachange


aki "あたしは弁護士なんだ。ほとんどは家族が経営する会社の日本支社にある法務部で働いてる"


aki "たぶん、一番つまんない答えだろうな。法律なんてほとんどの人にとってすごく味気ないし"


hi "そんな感じですね"

show akira basic_lost
with charachange


aki "おい、そこは同意する所じゃないだろ"

show lilly basic_giggle_paj
show hanagown normal
show akira basic_smile
with charachange


"リリーがティーカップと受け皿を持ったままおかしそうにクスクスと笑う。華子もすぐにそれに加わる。"



"この和気あいあいとした雰囲気こそ、リリーと晃さんがいなかった間に恋しく思っていたものだ。俺は華子に対して何も役に立てなかったけど、たぶんリリーがいないというだけで雰囲気が変わってしまっていたんだ。"


show lilly basic_smileclosed_paj
with charachange


li "帰って来られて嬉しいです。久夫さん、会えなくて寂しかったですよ。華ちゃん、あなたもね"



hi "俺たち２人も同じだよ。リリーのクラスメイトもリリーが帰ってきて嬉しいだろうな"

show lilly basic_ara_paj
with charachange


li "ある意味では、そうでしょうね"

show akira basic_laugh
with charachange


"愉快そうに鼻を鳴らす晃さんは、こういう言葉のあやに対してリリーがどういう態度を取るかよく知っているんだろう。２人が一緒にいる時間を考えれば、それも当然だ。"

show hanagown normal
with charachange


ha "スコットランドは楽しかった？"

$ renpy.music.set_volume(0.1, 2.0, channel="music")


"リリーが帰ってからもう大分経つのに、なぜ華子はこんなことを聞くんだろう。俺はしばらく考えて、そして今まで起きたことを思い出す。試験や北海道旅行のせいで、リリーの滞在について話す時間がなかったんだ。"

show lilly basic_reminisce_paj
show akira basic_annoyed
with charachange


"リリーがしばらくうつろな表情を見せる。晃さんが真っ先にリリーの方を見やったのを俺は見逃さない。それでもなお、リリーはすぐに冷静さを取り戻す。"

$ renpy.music.set_volume(0.8, 0.4, channel="music")

show akira basic_smile
show lilly basic_weaksmile_paj
with charachange



li "良かった……ですよ。私……私たちは……ずっと長い間家族と会っていなかったから、再会できてとても嬉しかったわ"


show akira basic_boo
with charachange


aki "ああ、そうだな。だけど一番良かったのは、家が海岸沿いにあったってことだ"



"今の軽蔑するような物言いを聞くと、晃さんはリリーほどには家族のことを好きじゃないんだという感じがする。"


show lilly basic_giggle_paj
with charachange



li "それは姉さんがようやく遊ぶ時間が取れたからってだけでしょう"



show akira basic_ending
with charachange



aki "あたしがリリーより泳ぐの得意だからって……"


show lilly basic_smileclosed_paj
with charachange



li "私は一族の運動能力を受け継いでない、ってだけですよ"


show akira basic_laugh
with charachange



aki "まあ、少なくとも身長の遺伝子は受け継いでるから、安心しなよ"



show akira basic_boo
with charachange


aki "それから、胸の遺伝子もな……"

show lilly basic_weaksmile_paj
with charachange



li "そんなこと、他の人の前で言うものじゃないでしょう……"



"リリーは晃さんを叱るそぶりを見せるけど、そうしている彼女の顔にも明らかに少し小生意気な笑みが浮かんでいる。"

show hanagown distant_blush
with charachange



"無頓着な表情からして、晃さんはそれほど気にしていないみたいだ。俺も気にはしていないけど、華子は俺の隣で顔を真っ赤にしてうつむいている。"




"この姉妹の道化ぶりは置いておくとして、２人の両親はまさにブルジョア的な生活をしている。"




"リリーや晃さんの今までの暮らしぶりとはまさに大違いみたいだな。リリーたちにとっては現実こそが最優先だろう。"




"だけど、裕福でよい家柄の出身という事実は、リリーが持っているように見える高貴な雰囲気をさらに増すだけだ。それが晃さんにはまったく受け継がれていないように見えるのは少し驚きだけど。"





"本当にこの２人は姉妹とは思えないほどに違う。似ているところがあるとすれば、２人が共有して持っている自信だけだ。それは時に愛らしくもあり、頭痛の種でもある。"


stop music fadeout 2.0

scene bg school_dormlilly
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.17
show akira basic_smile:
    tworight
    ypos 1.14
with shorttimeskip


"その夜の大部分はいつもどおり過ぎていく。やがて華子が就寝のために自分の部屋に戻り、砂藤姉妹と俺が後に残される。"



"しばらくの間、リリーがゆっくりとお茶を飲む時にティーカップと受け皿が立てるかすかな音しか聞こえない。リリーと俺がその話題が出るのを待つ間、張り詰めた沈黙が場を支配する。"





show akira basic_boo
with charachange


aki "さてと……"

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_dreamy fadein 4.0

show lilly basic_weaksmile_paj
with charachange


"リリーが礼儀正しくカップを置き、姉の方に一心に注意を向ける。"






"リリーと俺がローテーブルの片側に座り、晃さんは向かい側に座っている。まるで裁判官が判決を下しているみたいだ。"



show akira basic_smile
with charachange


aki "２人は今、付き合ってるんだってな？"



"横目でちらりとリリーを見て、彼女が晃さんに伝えたのかどうか確認する。リリーは晃さんに向かってゆっくりとうなずき、俺も同じ仕草で同意する。"




"今がそうするのにふさわしい時と場所だと決心すると、リリーの人生の大部分において親に最も近い存在である晃さんに向かって、俺は床に手をついて深く頭を下げる。"




hi "晃さん、妹さんを大切にします。約束します"

show lilly basic_smile_paj
with charachange



li "ね？　久夫さんは素敵な男性ですよ"



"リリーには俺の声が普段より低い位置から聞こえたに違いない。"


"俺はゆっくりと起き上がると、上目づかいでためらいがちに晃さんを見る。"



"正直言うと、このスーツ姿の裁判官は何も反対しないだろうという自信がある。この人は間違いなく、異論があれば率直に表に出すタイプだ。それについてはある種の尊敬の念すら感じる。"





show akira basic_laugh
with charachange



aki "昔風な感じってか?　まあ、リリーが好きそうなタイプの奴だとは思ってたよ"



show akira basic_smile
with charachange



aki "あたしに異存はないよ。お幸せにな。大体、仮に気に入らなかったとしても、あたしがどうこうできるわけじゃないしな"




"俺はうなずいて晃さんに感謝の意を示し、リリーはほっと安堵のため息を漏らす。それはきっと責任感からだろう。晃さんが俺たちの関係を不満に思うかも、と心配していたからじゃない。"


show akira basic_evil
with charachange



aki "だけど……家族や親戚はどう思うだろうな。特に山久にいる誰かさんが。あの子にはもう言ったのか？"


show lilly basic_listen_paj
with charachange



"晃さんがあからさまに悪意のある笑顔を見せ、俺たちの微笑はしかめっ面に変わる。最も近しい人ほど、人の一番痛いところを知っている、ということだ。"



show lilly basic_weaksmile_paj
with charachange



li "『受け入れている』というのがこの状況に一番ふさわしい言葉でしょうね。そう思いませんか、久夫さん？"




hi "うん、そんな感じだな。少なくとも理性的でいてくれてるよ"


show akira basic_boo
with charachange



aki "それは何よりだな。あの子はただでさえ扱いが手に余るからさ"


show akira basic_smile
with charachange



aki "旅行中や帰った直後に、何度か連絡を取ってたんだけど、戻ってきたらあたしが秀明をずっとほったらかして彼氏に会ってたことをすごく責められてさ。あの子はチビ助のことをほんとに心配してるよ"





"リリーとの関係について話した時の静音の奇妙な反応を思い起こすけど、それは言わないでおく。単に２人が仲が悪いのが原因なのは間違いないし、晃さんのコメントはそれを裏付けるだけだ。"



show akira basic_boo
with charachange


aki "さてと、じゃあ、この件は落着だな。明日の仕事も早いし、そろそろ帰るかな"

show akira basic_smile at tworight
with charamove


"晃さんが膝の上の手に力を込めて、テーブルからよいしょと立ち上がる。帰り際、俺たちに背を向ける前に、晃さんがほんの数秒間リリーを名残惜しそうに見ているのに気づく。"

hide akira
with charaexit


"ドアから出て行った後、晃さんは立ち止まって思わしげに上を見ると、最後にもう一度俺たちの方へと振り返る。"

show akira invis:
    xanchor 0.5 xpos 1.0
with None

show akira basic_lost:
    xpos 0.9
with dissolvecharamove


aki "おっ、そうだ。言い忘れるとこだった"

show akira basic_ending
with charachange



aki "避妊はしろよ。必ずな"






"俺は口の中のお茶で思いっきりむせ返る。俺とは対照的に、リリーはまるで何事もなかったかのように完璧に平静さを保っている。なんだか少し感心する。"


show lilly basic_smile_paj
with charachange



li "大丈夫よ。心配しないで"


show akira basic_smile
with charachange


aki "いい子だ。じゃあな"

show akira invis:
    xanchor 0.5 xpos 1.0
with dissolvecharamove

hide akira
with None



"その言葉とともに晃さんは俺たちに背を向け、手を高く上げながら暗い廊下の向こうへと大股で歩み去る。そして部屋のドアが閉じる。"



show lilly basic_smile_paj:
    center
    ypos 1.17
show bg school_dormlilly at bgright
with charamove



"俺にできる反応と言えば、テーブルの上に身を投げ出すことだけだ。晃さんのせいですっかりクタクタになってしまった。スーツ姿の悪魔の前でも自分を失わずにいられるリリーの能力は尊敬に値する。"




hi "晃さんは本当にありえないくらい率直だな。俺があのエネルギーに付いて行けるとはとても思えないよ"



show lilly basic_smileclosed_paj_close:
    center
    ypos 1.1
with characlose




"リリーの柔らかな手が俺の手の上に乗せられるのを感じて、俺は顔を横に向けると、隣にいるリリーの優しい笑顔を見る。長い間、俺たちはただ静かに寄り添い続ける。"





"疑いようもない並外れた長身からして、リリーの身長は俺とほとんど変わらない。いや、もしかしたら数センチ高いかもしれない。こうしていると、それよりもっと高く見えるくらいだ。"




"俺の手に触れているリリーの色白な柔らかい手。その感触がとても心地いい。そして体の丸みと鎖骨をあらわにする、薄いシルクのパジャマを着た姿も。"



show lilly basic_smile_paj_close
with charachange



li "そうは言っても、久夫さんはとてもうまくいっていますよ"



hi "まあね。ほら、リリーと晃さんって、俺が最初に会った時に感じたよりも実際はずっとよく似てるし"

show lilly basic_cheerful_paj_close
with charachange



li "では、久夫さんが姉さんを狙ったりしないよう、私がすぐに止めてあげてよかったですよね？"




"リリーは冗談のつもりだろうけど、物理的であれ精神的であれ、晃さんにはついていけないだろうという俺の自己評価は、いたって真面目なものだ。"



"リリーのゆったりしてお嬢様的な、ほとんど母性ともいえる性質こそ、山久に来たばかりの時の俺にとってたぶん一番助けになったものだ。"


"そういえば……"



hi "待てよ……避妊なんてしてたっけ？"



show lilly basic_pout_paj_close
with charachange


"俺がもの好きそうな様子で横を見ると、リリーはぷりぷりと怒りながら頬を膨らませる。"



li "久夫さんと違って、私は覚えていましたよ。ちゃんと流しの横の戸棚の中に薬が入ってます"



"じゃあ、薬を飲んでいるのは俺だけじゃないわけだ。今にしてみれば、そのことに全く考えが及ばず、リリーに任せきりにしたのは思慮が足りなかったと思う。"






"リリーが言った戸棚のほうを見ていると、周りにある膝の高さまで積まれた本の山にまた気づく。前に来た時にもあったものだ。テーブルの周りを空けるために、その大半は壁際に並べられている。"





hi "本棚を買って本を片付けたらどう？　床に積んであるだけってのは変だよ。それを除けば、部屋の中はすごくきちんと整とんされてるから、余計に目立つし"


show lilly basic_smileclosed_paj_close
with charachange


li "こうしておく方が本を見つけやすいんです。どの本がどこに積まれているか、全部覚えていますよ"


hi "本をそれぞれ別の棚に置いた後でも覚えられない？"

show lilly basic_weaksmile_paj_close
with charachange



li "そうかもしれません、けど……"



"つまり、リリーもやっぱり怠惰には勝てないわけだ。"



hi "リリーはほんとにたくさん本を持ってるな。俺たちがお互いに本を貸し借りできないのがなんだか残念だよ。２人ともこんなに読書家なのにさ"


show lilly basic_giggle_paj_close
with charachange


"リリーがくすくすと短く笑う。"



hi "そういえば、リリーはどうして優子さんに本の注文を頼むの？　点字本なら、特に英語のは注文できるサイトがネットにいっぱいあると思うけど。文書読み上げソフトもたくさんあるし"


show lilly basic_displeased_paj_close
with charachange



"リリーが俺から顔を少し背ける。その反応にちょっと驚かされる。"




li "私は、ただ……パソコンが苦手なので。タイプライターや点字タイプライターなら問題ありませんが……それ以上は"


"そう言うリリーの声を聞いて、俺は吹き出しそうになる。プライドの高い彼女にとって、そのことを認めるのは簡単じゃないはずだ。"



"つまり、リリーは機械オンチというわけだ。彼女の古風な性格を考えれば、別に驚くようなことでもない。"


hi "大丈夫だよ。パソコンが苦手な人も多いし、リリーだってすごく特殊ってわけでもないよ"

show lilly basic_concerned_paj_close
with charachange


li "『すごく』特殊……"




"リリーは余計に落ち込んでしまう。傷を癒すどころか、余計に傷つけてしまったみたいだ。"



show lilly basic_weaksmile_paj_close
with charachange



"俺は少し体をよじってリリーに近寄り、ためらいがちに彼女の腰に片手を回して抱きしめる。いまだにこういう物理的な愛情表現には慣れていないけど、リリーは気に入ってくれているみたいだ。"


scene ev lilly_kissing
with whiteout



"リリーが振り返りながら俺に笑顔を向け、こちらから折れたことへのご褒美としてキスしてくれる。リリーは俺を抱き寄せ、自分の上唇で俺のそれを撫で、そして互いに押し付ける。"




"こうしていると、全ての感覚がリリーで満たされていく。髪のかすかな匂い、つかの間に舌が触れ合う時の味覚、唇の柔らかさ。俺の心に満ちるリリーのイメージ、静寂を破る彼女のかすかな吐息……"





"キスは前にもしたかもしれない。だけど、それが単なる愛情のキス以外の何物でもないとしても、それは今でも新鮮で心地のいい感覚だ。"

scene bg school_dormlilly at bgright
show lilly basic_cheerfulblush_paj_close:
    center
    ypos 1.1
with locationchange



"身を引いた時に鮮やかに顔を赤らめるリリーを見る限り、彼女も俺と同じ気持ちなのは明らかだ。完全に２人きりでいても、それでもお互いにこんなに心を許しあうのはまだ少し恥ずかしい。"


show lilly basic_smileclosed_paj_close
with charachange



li "目の前のことを１日ごとにやっていけば、それがベストだと思うんです。少しずつ、ね？"




hi "ああ。少しずつな"



"一緒に過ごせる時間はまだたっぷりある。学校を卒業した後だって。一緒に進んでいくかぎり、何もかもうまくいくと思う。俺たちのどちらも、すぐにどこかに去ってしまうわけではないんだから。"




"今はただ、２人で過ごすことのできた、この短いひと時に感謝するだけだ。"


stop music fadeout 2.0

scene black
with dissolve




label jp_L23:

scene bg school_nursehall
with locationchange



"さっきから少なくとも十数分ほど、俺はナースの部屋のドアの前に立ったまま、身動きもせずに突っ立っている。"





"その小さなベージュ色の部屋に初めて立ち入るってわけじゃないし、ここを訪れることに子供じみた不安を感じているわけでもない。"




"ナースの部屋は懺悔室に似ているから、かも知れない。自分の体が傷ものだと認めるのと同じ意味なのだと。そういう事実がナースと俺の間で完全に機密扱いされると知っていても、ほとんど慰めにはならない。"



"昼休みの終わりを告げるベルがもうすぐ鳴ることを思い出して、俺はため息をついてドアを開ける。重荷はもうしばらく俺の上にのしかかり続けるだろう。"

play music music_nurse fadein 0.5

scene bg school_nurseoffice
show nurse neutral at center
with locationchange




nk "おっ、久夫くんじゃないか。よく来たね"



show nurse grin
with charachange



nk "いや、よくはないかもな。僕がナースであることを考えると"




"自分の小ネタに自分でウケて、ナースが小さく笑う。センスがないし、ちょっと失礼だと俺は思うけど、ナースがこんな状況も軽くあしらうことができることにはなんだか慰められる。少なくとも気は紛れる。"



show nurse neutral
with charachange


"短い余興は終わり、ナースはパンと両手を鳴らして仕事に戻る。彼に促されて、俺は椅子に座る。"


"教室の椅子もこれぐらい心地よかったらなあ。俺は辺りに素早く視線を走らせながら、気持ちが散漫になっているのを感じる。前に来た時からの部屋の中の小さな変化にいちいち気が向いてしまう。"

show nurse fabulous
with charachange



nk "さあて、何があったのかな？　それほど頻繁に顔を見せないことを考えると、最近は調子がいいのかな？"



hi "ええと、だいたいは"

show nurse neutral
with charachange


nk "へえ"



"俺が消え入るように言うと、ナースの笑顔が消える。少し罪悪感を覚える。自分が『普通』だと理性的に言えないとき、俺は本当にナースと会いたくなくなる。自分が他の人と違うと認めるのと同じことだからだ。"



stop music fadeout 5.0



hi "週末休みの間に旅行している途中で、少し心臓の調子が悪くなったんです"




"ナースはとても真剣にうなりながらうなずいて、話を続けるよう促す。"





hi "あれは……うん、けっこう長い距離を歩いていた時だったと思います。心臓の粗動って言うんじゃないかと思います"





hi "突然ひざがふらつき出したかと思うと、まるで軽い心臓発作が起こったみたいに感じて、でも３０秒ぐらいでおさまったんです。だけどその後もすごく疲れてて、吐き気もありました"


show nurse concern
with charachange



nk "ふむ、良くないね。それは全く良くない"




nk "それは正確には何日前のことかな？　それが起こる前に、体に負担をかける以外に何か特別なことをしたかい？　薬はちゃんと飲んだかな？"



"ナースがやっかいな冗談好きから真剣な医療専門家へとモードを変える。てきぱきと質問をして、メモを取り、パソコンから必要なデータを引き出す。"


"俺はあの日の朝と前日の夜に薬を飲み忘れたことをナースに伝える。飲み忘れた俺もバカだったけど、今さらどうにもならない。今はただ、正直に答えて歯を食いしばるだけだ。"


"ナースの真剣な表情はやがてしかめっ面に変わり、会話は簡易検査へと発展する。"

hide nurse
with shorttimeskip


"シャツのボタンをかけ終わると、再びナースの前に座るように指図される。"

show nurse concern at center
with charaenter



nk "今回心臓に問題が起きたのは、山久に来てから初めてかな？"




hi "ちょっとした胸の痛みは以前もありました。数回だけですけど、でも今回のに比べれば、不快感って程度でした"





"ナースが椅子の上でふんぞり返る。まるで白衣を着た探偵ポワロが謎めいた心臓粗動事件を解こうと考え込んでいるみたいだ。"






"ナースの唇が左右に動いて、彼が考え中であることを示す。存在しない口ヒゲもぴくぴくと動く。やがてナースは結論に達する。"


show nurse fabulous
with charachange

play music music_nurse fadein 1.0



nk "まあ、君は生き延びたんだ。何はともあれ、それはいいことさ"




"俺はそれを聞いて目をぱちくりさせる。そしてナースが『どうだ』という表情をしているのに気づく。"







"実際、それは俺にとっていくらか安心できることだ。もし本当に深刻ならナースだってこんな冗談は飛ばさないだろう。それで俺は黙ってこの屈辱に耐える。"


show nurse neutral
with charachange



nk "君の主治医と話さなきゃいけないな。だけど今のところは、単に体の疲労が原因だと思う"




nk "以前僕が言ったように、定期的な軽い運動を続けてるかい？"




hi "毎日それなりの距離を歩くようにしています。少し汗をかくにはだいたいそれで十分ですけど、そうは言っても以前ほど健康ってわけじゃないですから"




nk "なら、それで十分だよ。重要なのは定期的に軽い運動をするということだ。瞬発的な激しい運動のたぐいじゃなくてね"



hi "分かりました。病院を出てから、あまり運動ができないことを忘れようという思いもあって、勉強の方により気持ちを集中させていたんです"

show nurse grin
with charachange



nk "上手くやっているようでよかったよ。生活スタイルが突然変わると、やっぱり大変だろうからね。君がすべてを順調にこなしているようでよかったよ。いや、ほとんどすべて、か"



show nurse neutral
with charachange



nk "とはいえ、しばらくは君のことを注意深く見守りたい。ただの経過観察だけどね。症状が下り坂になっていないことを確認するためだ。分かるね"



"それは、俺が絶対に聞きたくなかったひと言。山久に来てからの俺は、可能な限り普通の人生を送りたいということだけを望んできたんだ。"



"『観察』は、入院中に俺が最も嫌いになった言葉の一つだ。医者たちがあんなにやりたがった、あの『観察』さえなければ、俺はすぐにでも退院できたんじゃないかとずっと思っていた。"




hi "もちろんです。もっと頻繁に来たほうがいいですか？"



"ナースがパソコンの隣に置かれたカレンダーをチェックする。それが眉をひそめるような厄介な状況を彼に突きつけているらしい。チェックが終わるとナースはくるりと回って俺のほうを向く。"

show nurse concern
with charachange


nk "タイミングを考えたら、夏休みというのはちょっときついね……"



nk "君の主治医と話して、この状況をきちんと把握できるようにするのと、今後の彼の意向を確かめておくよ。だけど今のところは、君はゆっくり気をつけて過ごすべきだと思う"




nk "君の話してくれた症状は、すぐに再発するようなものじゃなさそうだ。だけど、しばらくゆっくりしているに越したことはないだろうね、念のために"




hi "今日はどうすればいいですか？"




"ナースが俺の肩越しにドアの上に掛かっている時計を見る。彼の視線を目で追わなかったら、その時計には絶対に気づかなかっただろう。"


show nurse fabulous
with charachange




nk "もうすぐ授業時間も終わりだし、早退していいよ"






"ナースがいたずらっぽくウインクをして、自分が一肌脱いだということを俺に念押しする。"




hi "まあ、ナースの命令なら。どうも"

show nurse grin
with charachange


nk "何といっても、僕はこのためにいるんだからね"

show nurse neutral
with charachange



nk "こんなこと聞きたくはないだろうけど、健康状態については気を付けてなきゃいけないよ。もしまた何か問題が起きたり、他に聞きたいことがあったりしたら、遠慮なくここにおいで。じゃあね"


hide nurse
with charaexit


"ナースはぐるりと回って机のほうを向くと、目の前のパソコンに向かって再びタイプを始める。俺は他にこれといってすることもないし、門でリリーを待つ前に読書でもしようか。"

stop music fadeout 3.0



"部屋を出て行くときも、ナースの言葉が俺の心の中で繰り返される。俺の状態は山久の他の生徒たちほど大変なものじゃないし、リリーにそのことで心配をかけさせるのもいやだ。"




"ただ普通に生活して、鋭い衝撃を避けていれば、俺は大丈夫なんだ。自分の境遇に支配されてたまるか。"


scene bg school_gate_ss
show lilly cane_smileclosed_ss at center
with shorttimeskip

play music music_tranquil fadein 3.0

play sound sfx_normalbell



"一日の授業の終わりを告げるベルが鳴ってすぐに、リリーの姿が視界に入る。反対方向へと向かうたくさんのクラスメイトたちに別れを告げて、毎週恒例になっているコンビニへの買い出しに向かっている。"




hi "こんにちは、リリー"

show lilly cane_smile_ss
with charachange



"俺の存在に気づいて即座に見せる優しい笑顔とリラックスした態度に、思いがけず嬉しくなる。"



li "あら、久夫さん。ごきげんよう"

show lilly cane_smileclosed_close_ss
with characlose



"リリーはわずかにためらうけど、結局顔を前に傾けて目を閉じる。俺の唇とリリーの唇が、かすかに震えながら触れる。それから俺たちは手をつないで歩き出す。"





"俺たちの身長がそれほど変わらないというのは、時折便利なこともある。お互いに相手の背に合わせるために上や下を向いたりせずに済む。"


scene bg school_road_ss
with locationchange




"俺たちのはるか後ろにいる他の生徒たちの喧騒から離れるのに、それほど時間はかからない。リリーが空いた手に持つ杖で地面を突く音だけが聞こえる。"





"静寂。至福の静寂。それだけが、夕暮れの光の中をゆっくり歩いている俺とリリーを迎えてくれる。"




hi "俺もこの街が本当に好きになってきたよ。雄大な緑の野山が広がってて、木々がそこらじゅうにあって、ちょっとひなびた感じの小さな建物があって……"


show lilly cane_smile_close_ss at center
with charaenter



li "それでは、この静けさも良いと思えるようになったんですか？"




hi "うん。東京に近い大きな街から来たから、最初に来た時はここの静けさは本当に性に合わなかった"




hi "でも、しばらくしたらとてもいいと思えるようになった。今は喧騒だらけの地元の街よりこっちの方がいいかもな"


show lilly cane_smileclosed_close_ss
with charachange




li "私はこの田舎町に来た時からここの静けさが気に入っていましたけど、きっとそれは、ここに来る前に静かな土地で育ったからでしょうね"



show lilly cane_weaksmile_close_ss
with charachange




li "華ちゃんも、この周りはとてもきれいだと言っていました"





"リリーは気軽そうに言うけど、他の誰かが周りの景色を美しいとかきれいとか表現している、ということを彼女の口から聞くたびに、俺は少し戸惑ってしまう。"





"リリーが何か聞かれるのを待っているようなそぶりをしているのに気づく。誰かが思っていることを言わずにいるとき、リリーはいつもそれを敏感に感じ取る。それなら、率直に言ったほうがいいだろう。"



hi "ちょっと思うんだけど……ええと、どう言ったらいいか……"



hi "自分の目で……ありのままを見られなくて、悔しくなったりしない？　最近そんなことを考えてたんだけどさ"


show lilly cane_listen_close_ss
with charachange


"リリーがしばらく慎重に考え込む。"

show lilly cane_smileclosed_close_ss
with charachange


li "久夫さんは、お部屋の反対側にいる人たちのささやき声が聞こえなくて悔しくなったりしますか？"

show lilly cane_smile_close_ss
with charachange



li "個人的なことしか言えませんが、目が見えないという状態でしか、私は人生を過ごしてきたことがありません。久夫さんにできて私にできないことがあるように、私にできてあなたにできないこともありますよ"



show lilly cane_weaksmile_close_ss
with charachange



li "この世界が目の見える人のために作られているおかげで、苦労をするときもあります。でもその世界のありようのせいで、私よりももっと苦労をしている人が本当にいっぱいいるんです"



hi "言ってることは分かるけど、それでも、リリーが経験できないことをリリーに説明するのはなんだか気が引けるよ"

show lilly cane_surprised_close_ss
with charachange


"まるで俺の発言の意味が全く分からないという様子で、リリーがいぶかしげに頭を傾ける。"


li "だけど、私は経験できますよ"

show lilly cane_smile_close_ss
with charachange



li "さっき久夫さん自身が、周りの様子のおかげでここを気に入っていると言いましたよね。私も久夫さんと全く同じ理由でここが好きです"



show lilly cane_smileclosed_close_ss
with charachange





li "ここが木々に囲まれた、ひなびた小さな街というおかげで、学校の騒音や、都市の喧騒、それに臭いからも離れて、いくらか平和で静かな時を過ごせるんです"







"たぶん、リリーが晃さんと一緒に過ごした家もほとんどそんな感じなんだろう。"



"リリーの考えはとても理にかなっている。俺自身に比べて、リリーが自分の症状をはるかにうまく理解できていることも当然だなと思う。"





"山久の環境に似た所から来たことで短期間でここに馴染むことができたように、リリーは生まれつき目が見えないということを自ら受け入れていて、それが彼女のものの見方に影響を与えている。"






"もうこのことを気にしすぎるのはやめるべきだ。でも山久の人々のほとんどがその境遇にしかたなく折り合いをつけてきたというのに、自分はリリーに頼りすぎてきたという気持ちがどうしても離れない。"






hi "よく分かったよ。リリーは説明がすごくうまいな、いつものことだけど"



hi "そういえば、華子はどうした？　昼食の時は一緒にいたのに"

show lilly cane_weaksmile_close_ss
with charachange



li "勉強が忙しいみたいです。試験もまだまだ続きますし、華ちゃんも去年よりいい成績を取りたいと言っていました"




hi "その熱心さには感心するけど、最近華子はずいぶん俺たちに気を利かせてくれてるよな"



show lilly cane_reminisce_close_ss
with charachange



li "華ちゃんはそういう性格の子ですから。いつも自分より他人を優先させてしまうような。過去にどんなに傷ついたとしても、華ちゃんは心優しい子ですよ"


show lilly cane_weaksmile_close_ss
with charachange



li "よく分からないけれど……華ちゃんは今初めて、今までよりも私から少し距離を置いて、自分自身を真剣に探しているような気がします"


show lilly cane_smile_close_ss
with charachange


li "華ちゃんに自信が出てきたのはやはり、私でなくて久夫さんのおかげですね"


"俺はリリーの手の中から自分の手を引くと、彼女の手の上に優しく乗せる。"



hi "大切なのは、リリーが華子のためにそばにいたってことだよ。リリーみたいな人がいなかったら華子がどうなっていたか、俺には想像もつかない。リリーがスコットランドにいた間にはっきりわかったよ"





hi "俺たちは今でも友達なんだから、華子を信じてやらなきゃ。華子はきっといい人になると思う。それは、華子が一番必要だった時にリリーがそばにいてくれたおかげだよ。俺のそばにいてくれたみたいにね"



show lilly cane_weaksmile_close_ss
with charachange


li "久夫さんのそんな聡明な発言を聞くと、自分が少し子供っぽく思えてしまいます"



hi "まあ、そうあろうとがんばってるよ"


hi "もしかして、この週末は何か予定ある？"

show lilly cane_surprised_close_ss
with charachange


li "特には思い当りませんが。どうしてですか？"



hi "じゃあ、日曜にデートなんてどう？　試験勉強の息抜きにちょうどいいと思うけど"



show lilly cane_smileclosed_close_ss
with charachange


"心臓をドキドキさせている俺に対して、リリーはただ笑ってうなずく。"


li "それは素敵ですね"


hi "どこに行きたい？"

show lilly cane_displeased_close_ss
with charachange


"突然、リリーの顔が俺の発言をはねつけるかのような表情に変わる。"



li "そんなのだめですよ、久夫さん。それはずるです"




hi "そんなのって、何が？"




li "紳士はレディにデートの場所を聞いたりはしないものです"


hi "ああ……そうなの"

show lilly cane_smile_close_ss
with charachange



"すぐにリリーの笑顔が戻って、今のが本気じゃなかったことがわかる。"


show lilly cane_smileclosed_close_ss
with charachange


li "冗談ですよ。どこに行くか、考えておきますね"



hi "じゃあ、お願いするよ。だけどその代わり、次のデートは俺が決めるから"


stop music fadeout 4.0


"俺たちの週末の計画が決まり、残りの丘を下るあいだ沈黙が続く。"



"だけど、そんな時間が少しでも長く続いてほしいという願いは、俺たちに向かって手を高々と上げている見慣れた待ち人の登場で打ち砕かれる。"


show lilly cane_smileclosed_close_ss at twoleft
show bg school_road_ss at bgleft
with charamove

show akira basic_smile_ss at tworight
with charaenter


aki "よう"

scene bg suburb_konbiniint
with shorttimeskip

play music music_daily fadein 0.5



"店員" "ありがとうございました。またお越しくださいませ！"


scene bg suburb_konbiniext_ss
with locationchange



"コンビニの外に出ると、温度の違いのせいで背筋に震えが走る。まるで夏が終わり始めているかのようだ。"


show lilly cane_weaksmile_ss at center
with charaenter



"横に目をやると、リリーも同じように感じているみたいだけど、でも俺とは違い、それを隠すことはできていない。最初は気づかなかったことだけど、リリーの体は華子のような人たちと比べてもとても繊細だ。"




"例えるなら、それは陶磁器製の人形のような。"

show akira basic_ending_ss at center behind lilly
with charaenter

show lilly cane_surprised_ss
with vpunch

show lilly cane_reminisce_ss at twoleft
show akira basic_ending_ss at tworight
show bg suburb_konbiniext_ss at bgleft
with dissolvecharamove



"晃さんがリリーの背後に歩み寄って彼女の肩をポンポンと強く叩き、リリーがびくりとする。俺は２人の仲の良さがうらやましいけど、リリーはそれと同じくらい、一人っ子という俺の立場をうらやんでいるようだ。"






show lilly cane_listen_ss
show akira basic_boo_ss
with charachange



"俺が袋の中を整理している間、リリーと晃さんがしばらく何かを話している。２人の声が小さすぎて俺にはよく聞こえないけど、結局２人は離れ、俺たちは学校に向けて歩き出す。"


scene bg school_road_ss
show akira basic_smile_ss at tworight
with locationskip



aki "ああ、あの窮屈なオフィスから出るのは気持ちいいな。君らみたいな子供にはこのありがたみは分からないよ"



show lilly cane_displeased_ss at twoleft
with charaenter



li "子供って……"


show akira basic_laugh_ss
with charachange



aki "おや。じゃあ、『君ら２人』。最近は子供もすぐ成長するからな"


show lilly cane_pout_ss
with charachange


li "姉さんもそんなことを言えるほど年を取っていませんよ"

show akira basic_lost_ss
with charachange



aki "どうだろうな。秀明といると、自分がすごく年寄りに感じるよ。すごくませててさ、小さかったころのリリーを思い出すな"


show lilly cane_weaksmile_ss
with charachange



li "秀明くんはいい子ですよ。静音が彼にあまり影響を与えすぎるようなことがあったら、それは残念なことよ"


show akira basic_laugh_ss
with charachange



"反感を見せる妹に対して晃さんは楽しげに鼻を鳴らして答える。晃さんはそれを騒ぎ立てるようなこととは思っていないように見える。むしろ子供のいさかいくらいにしか考えていないんだろう。"



show akira basic_smile_ss
with charachange


"俺の存在を明らかに今思い出したかのように、晃さんがこちらを振り返る。そして、後ろのポケットに手を伸ばしながら俺ににやりと笑いかける。"


hi "何ですか？"

show akira basic_ending_ss
with charachange


aki "ちょっと待ってろよ、探し出すから……"


"相当苦労したあと、晃さんが後ろのポケットから革製の黒い財布を取り出し、その中からすばやく折りたたまれた紙のようなものを引き出す。"


"何が起こっているのか全く気づいていないリリーをよそに、晃さんはその紙切れを広げて俺に手渡す。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show stallphoto_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"古い写真……今より幼く見えるリリーと静音が焼きそば屋台を切り盛りしていて、背後にもう１人女の子がいる。この子、何となく見覚えがある気がするけど、どうしてそう思うのかよく分からない。"

show lilly cane_smile_ss
with None

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show stallphoto_insert:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide stallphoto_insert
with None


li "姉さん、何ですか？"

show akira basic_boo_ss
with charachange


aki "リリーなら分かると思うぞ"

show lilly cane_listen_ss
with charachange


"リリーはしばらく考え込んだ後、はっとひらめく。"

show lilly cane_surprised_ss
with charachange


li "姉さん……そんなもの……"

show akira basic_smile_ss
with charachange



aki "別にいいだろ？　それにリリーが山久に入学して以来、この２人がいがみ合わずに一緒に写ってる写真はこの１枚しか持ってないからな"



$ renpy.music.set_volume(0.5, 1.0, channel="music")

show stallphoto_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"手元の写真に再び目をやる。"



"リリーと静音がお互い反目する様子もなく、一緒にがんばって働いている姿を見るのは、変な気分だ。もしこの写真が山久の学園祭で撮られたものなら、間違いなく１年前か２年前ということになる。"





"言い換えれば、２人が生徒会で一緒にいた頃か。"


hi "後ろにいる女の子は誰ですか？　見たことあるような気がするけど"


aki "あはっ、分かんないだろうと思ったよ。ミーシャだよ、血迷って髪をピンク色に染める前の"





hi "これがミーシャ？　まさか……"




"あの独特すぎる髪型をしていないミーシャを見るなんて、ものすごく変な気分だ。今の言い方からすると、晃さんはミーシャのファッションセンスを評価していないみたいだ。"




"この写真から見える事実は今の状況の奇妙さをより際立たせるように感じる。以前のみんなはこんなにも仲が良かったんだ……彼女たちが仲直りできるよう、俺に何かできたらいいのに。"



li "なんだかとても静かですね、久夫さん"



hi "リリーたちがこんなに仲が良さそうにしているのを見て、ちょっと妙な気分になっただけさ"



"リリーが何かを言いかけて、再び口をつぐむ。結局のところ、これは俺の問題じゃない。これは静音とリリーの問題であって、それ以外の誰の問題でもない。"



li "物事は変わるんです。残念ですが"


$ renpy.music.set_volume(1.0, 1.0, channel="music")

stop music fadeout 6.0

show akira basic_resigned_ss
show lilly cane_reminisce_ss
with None

show stallphoto_insert:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide stallphoto_insert
with None


"俺は写真を晃さんに返し、晃さんはため息交じりに写真を折りたたんで財布にしまう。それは静かに隠され、しばらく後に再び日の目を見るであろうはずの小さな記憶。"


aki "ああ、そうだな"


"晃さんのこういう反応も、ただリリーと静音の状況に対してのものなんだろう、と初めは考える。だけど、それにしては妙に落胆しているように見える。リリーの表情まで曇ってしまっている。"


hi "どうしたんですか？"

show akira basic_boo_ss
with charachange



aki "ああ、もうすぐスコットランドに行くから、それでさ"




hi "またスコットランドに発つんですか？"

show akira basic_lost_ss
with charachange



"かなりの時間、晃さんが驚いた様子を見せる。晃さんには不似合いな表情だ。"



"リリーをちらりと見た後、まるで何事もなかったかのように俺に向き直る。"

show akira basic_resigned_ss
with charachange



aki "ああ。数週間後にインヴァネスに飛んで、そこの本社で働くんだ。役職もかなり上がるし、こんなチャンスはそうそう巡ってくるもんじゃないからな"






"じゃあ、晃さんは日本を離れるのか。おそらく永久的に……"





"この隔絶された小さな世界で、みんなで楽しんで幸せに時を過ごす、そんな思い込みが終わりを迎えようとしている。そう感じずにはいられなくなって、動揺してしまう。"





"普段はこういうことを前もって伝えてくれるのに、今回は何も教えてくれなかったリリーに少し驚いて、俺は彼女のほうを見る。"



"リリーは顔をまっすぐ前に向けたまま歩き続ける。彼女がどんな表情をしているのか、何を考えているのかすら俺には分からない。普段はどちらも簡単に読み取れていただけに、不安が募る。"






"初めてのデートらしきものの直前に、上海でリリーにばったり会った時のことを思い出す。あの時は原因もわからずに彼女を慰めることしかできなかった。それは今も変わらないような気がする。"





scene bg school_dormext_full_ni
show akira basic_resigned_ni at tworight
show lilly cane_reminisce_ni at twoleft
with shorttimeskip


"ついに学校の寮に再び帰り着き、俺たちの周りには気まずい感じの沈黙がただよっている。それを感じているのは俺だけじゃないはずだ。"


hi "じゃあまた明日な、リリー。さようなら、晃さん"

show lilly cane_weaksmile_ni
with charachange


li "おやすみなさい、久夫さん"

show akira basic_smile_ni
with charachange


aki "じゃあな"

hide lilly
hide akira
with charaexit


"そんな言葉を残して、２人は女子寮へと歩いていく。"


"男子寮のドアを開きかけて俺は立ち止まり、振り返ってリリーと晃さんが重い木製のドアの向こうに消えるのを見届ける。"


"晃さんが日本を去ると言った時……奇妙な瞬間だった。俺の新しい人生に対する考えに疑問が投げかけられるのはこれが最初ではないにしても、これほど深く考えさせられるのは今回がたぶん初めてだ。"



"それにしても、晃さんのあの反応をどう考えたらいいのかわからない。リリーに関してはなおさらだ。"



"何か手がかりをつかむ前に、夜の冷え込みが俺に部屋に戻る途中だったことを思い出させる。持っている袋がより重みを増して俺の腕にのしかかる。"



"とにかく、週末はリリーとデートなんだ。俺はただ考えすぎるのをやめて、成り行きに任せるべきなんだ。"





"試験だってまだ続いている。もうすぐ学期が終わって夏休みも始まるし、やることは山ほどあるだろう。"




"あくびをしながら建物の中に入ると、リリーは週末のランデブーの舞台をどこに定めるつもりなのか、ということに俺の興味が移っていく。"


scene black
with dissolve



label jp_L24:



scene bg city_restaurant at Fullpan(10.0)
with dissolve

play music music_jazz


"デートの場所が決まったとリリーが言った時、俺はこんな所だとは夢にも思っていなかった。それは間違いない。"



"男性も女性も最高の正装としか言いようのない服を着ていて、周りの雰囲気もそれに引けを取らない。豪勢な赤い壁紙が壁を飾り、はるかな眼下では夜景が光り輝く。"




"周囲から聞こえる静かな話し声と、食器とワイングラスの立てる高い音が混ざり合う。雰囲気はとてもフォーマルだけどゆったりとしていて、初めての正式なデートにしては俺も堅苦しく感じずに済んでいる。"




"俺たちが席に着くと、ウェイターはリリーからの感謝の会釈を見届けた後、軽くお辞儀をして他の客のもとへと向かう。"



"慣れない環境にもかかわらず、リリーはこれまで俺に全く頼らず、驚くほどたやすく身をこなしている。そこここにすっと触れるだけで、リリーはとても器用に望み通りの方向へと体を動かしていく。"



$ ksgallery_unlock("evul lilly_restaurant_listen")
scene ev lilly_restaurant_listen at restaurant_out
with whiteout


"俺はリリーの目を見つめる。その表情から、俺が周囲を一生懸命見ているのと同じくらい、リリーが周囲の音を聞くことに集中しているのが分かる。"



"だけど正直言うと、店の中を見回すたびに、俺の視線はリリーの姿に引きつけられる。"
"リリーが着ている赤いチャイナドレスは彼女のスタイルを強調して、脚線美もあらわにする。髪は上げられていて、かすかに香水の匂いがする。"




"俺の着ている黒のスーツはレンタルだけど、ぴったりなものを選ぶことができた。スーツをほとんど着ない俺にとっても驚くほど着心地がよくて、リリーの服装と同じくらいこの場にふさわしい。"


hi "こういうのって、俺たち両方にとって初めての経験、だよな？"

$ ksgallery_unlock("evul lilly_restaurant_sheepish")
show ev lilly_restaurant_sheepish at restaurant_out
with charachange



"リリーが少しおどおどした様子になる。"



li "ええ、こういう場所に来るのは私も初めてです"



hi "とんでもない初デートだってのは確かだよ。俺がこれを乗り越えるのはかなり大変だろうな"




"くすくすと笑うリリー。こうしている間も、俺たちの緊張はほぐれつつある。"




"テーブルの中心に向かってリリーの手が滑り、その動きがメニューに触れて止まる。リリーはメニューを両手で取って、顔に近づける。"



li "あの、久夫さん？"


"リリーがラミネート加工されたベージュ色のメニューをちょうど彼女の目の下まで下げる。またおどおどした様子だ。"



"ウェイターに点字のメニューを頼むのは無駄だろうな。"



hi "ああ、俺が読み上げるよ。問題ないさ"

scene bg city_restaurant at right
with locationchange


"俺は自分のメニューを取って中をさっと読む。そこで俺の笑顔が消える。"




hi "ええと、やっぱり問題あるかも"




show lilly basic_weaksmile_che_close:
    center
    ypos 1.1
with charaenter


li "どうしたんですか？"


hi "メニューの品目がいっぱいあってさ……どう読んだらいいのかよく分からないのもいくつかあるし"


"つらつらと羅列されている豪華料理たち。ほとんどは日本語なんだろうけど、英語やフランス語で書かれたものもいくつかある。想定の範囲内であっても、いくつかの品はそれが何なのか全く見当がつかない。"


"あっ、これなら俺にも分かるぞ。いや、ちょっと待て……"


hi "……これ、料理できるの？"

show lilly basic_giggle_che_close
with charachange


"楽しそうなくすくす笑いが紙のメニューの向こう側からかすかに聞こえる。"


hi "いや、全部読み上げられるだろうけど、たぶん何時間もかかっちゃうよ"

show lilly basic_smile_che_close
with charachange


li "何かお魚が入ったものはありますか？"


hi "ええと……"


"違う。違う。違う。違う。これ、毒じゃないのか？　これも、これも、これも違う。こんなもの食うのか？　違う、違う、違う、違う……あ、これなら。"


hi "ツナサラダなんていいんじゃないかな。写真を見る限り、ボリュームも結構ありそうだ"

show lilly basic_smileclosed_che_close
with charachange



li "それが無難そうですね"




hi "じゃあ、２つ頼もう。ここの料理には間違いなく材料に毒を持ってる生き物を使ってるのがいくつかあるよ。命がけのゴタゴタはもう勘弁だ"


show lilly basic_weaksmile_che_close
with charachange



"リリーは笑顔を浮かべ続けているけど、明らかに本心から笑っていない。リリーはブラックユーモアをお気に召さないらしい。俺も今のは大しておかしいとは思ってないけど。"



li "確かに、辺りには興味深い匂いがたくさん漂っています。きっとここの光景もそれと同じくらい興味深いんでしょうね"



hi "俺は今までこんな所に来たことないよ。しゃれた日本的な喫茶店なら１、２回行ったことはあるけど、こんな贅沢で西洋風なスタイルの店は初めてだ"




"俺が言葉を継ごうとすると、痛々しいほどにぴっちりしたベストを着た巨体のウェイターが注文を取りに俺たちのテーブルにやって来る。"



hi "プロヴァンサル・ツナ・サラーダ・ニソワーズを、２つ"







"今の発音があまりひどくなかったならいいけど。もしひどかったとしても、ウェイターがそれを態度に示すことはない。"


show lilly behind_cheerful_che_close
with charachange


li "それから、シャルドネを一杯いただけるかしら。久夫さんは？"


hi "えっ、ああ、同じものを"



"ウェイターがうなずいてその場を去ると、リリーの注文をぼんやりと繰り返していた俺は突然、自分が今言ったことに気づく。すぐに後悔の念が押し寄せる。"




hi "酒……"

show lilly basic_pout_che_close
with charachange


li "少しだけですよ"




"この子は妙に物事にはまりやすい性質があるな。間違いない。"






hi "年を確認をされなかったのが驚きだよ"




hi "でもそうすると、俺たち２人は実年齢より大人っぽく見えるんだろうな"


show lilly basic_smileclosed_che_close
with charachange



li "久夫さんの言うことを信じるしかないですね。でも付け加えるなら、ここはそんなことを聞いたりするような場所ではないので"



hi "そうだな"


"息苦しいほど形式ばった周りの雰囲気から少しでも気を紛らわせようと、俺たちはそれぞれの椅子に少しリラックスして座る。"


"そうしているとすぐに、さっきと同じウェイターが２つの空のグラスとワインボトルを手に再び俺たちのテーブルにやってくる。彼は慣れた手つきで素早くワインをグラスに注ぐ。"

scene ev lilly_restaurant_wine:
    zoom 1.05 xalign 0.0 yalign 0.5 subpixel True
    easeout 8.0 zoom 1.0
with flash



"ウェイターの去り際に俺たちは丁寧にうなずく。リリーはグラスを手に取ると、それを優しく左右に振る。中のワインがグラスに沿って揺れ動きながら光を放つ。"
"それを見る俺の中で、同じものを頼んだ後悔の念が少し薄れてきているのを認めざるを得ない。"





"グラスの中の液体の動きを、その重心だけを頼りに知るのはきっと骨の折れることだろう。リリーにとっては折り紙と似ているのかも知れない。器用さを鍛えるために、どんな小さなチャンスも逃さないんだ。"





hi "リリーがこういう場所を知ってたとしても、別に驚くようなことじゃないんだろうな。お金持ちならよく知ってるんだろうし"




"それは、俺とリリーの境遇がいかに違ったものであるかを思い起こさせる。生徒がみんな同じ制服を着て同じ寮に住む山久では、それぞれの社会的、経済的な差を簡単に忘れてしまう。"


scene bg city_restaurant at right
show lilly basic_smile_che_close:
    center
    ypos 1.1
with flash



li "まあ、ここを教えてくれたのは姉さんですけど。姉さんは一度ここに来たことがあるみたいですね"



"じゃあ、リリーと晃さんの金曜日の秘密会議は、これのことだったのか。"



hi "で、リリーは俺がずるをしてるって責めるわけ？"


show lilly basic_displeased_che_close
with charachange



li "これはずるではありません。ただ個人的なつながりを活用しているだけです"




hi "そう言うなら、それでいいよ。俺よりもリリーの方がこういうレストランにお似合いに見えるって今でも感じるな"



show lilly basic_reminisce_che_close
with charachange

with Pause(0.5)

show lilly basic_smileclosed_che_close
with charachange


"リリーが物思わしげな表情を浮かべて少し黙り、それから優しく微笑む。俺の褒め言葉は彼女のムードを明るくしたようだ。"

show lilly basic_planned_che_close
with charachange



li "私が以前いた学校のおかげです。もし私がそう見えないなら、あそこの人々は私にひどく失望したでしょうね"




"前の学校についてはリリーも以前話してくれたことがあるけど、なんだか興味が湧いてきた。過去のことはよく思い返しているみたいだから、別に聞いても構わないだろう。"



hi "そこはどんな感じだったの？"

show lilly basic_smile_che_close
with charachange


li "ミッション系の名門女子校です。両親がそういう学校を私に選んだんです。裕福な家庭出身の女の子たちがたくさん通っていました"



hi "聞いた感じからすると、そこの生活はすごく厳しかったんだろうな"


show lilly basic_weaksmile_che_close
with charachange




li "それがつらかったとは言いませんが……そうですね。とても厳格でした。ありがたいことですけど、私はそこにうまく馴染むことができて、友人もたくさんできました"




show lilly basic_reminisce_che_close
with charachange



li "あいにく、姉さんはそうはいきませんでした。学校の雰囲気と宗教的な側面が息苦しかったようで、仕事を見つけて働けるようになったとたんに中退してしまったんです"


show lilly basic_weaksmile_che_close
with charachange


"リリーが少し自嘲気味に笑う。"



li "だけど、そのことに不満を言うべきではありませんね。多くの人はそんな学校に通うチャンスさえ得られないのだし"




hi "リリーは……リリーをそこに入学させて離れてしまった両親のこと、恨んでる？"



"リリーがゆっくりと首を横に振る。"

show lilly basic_reminisce_che_close
with charachange


li "私の家庭はとても父権的で、仕事人間の父は、私をどう扱ったらいいのか全く分からなかったんです"

show lilly basic_weaksmile_che_close
with charachange


li "最終的に父は、私が家族と一緒にいることよりも、私の教育の方を優先しました"


li "父はただ、私のためを思ってそうしてくれたんです"



"そんなことをいとも簡単に言ってのける。信じられない子だ。とはいえ、リリーはその扱いを盲目のせいだとは全く思っていない、というのが少し驚きだ……俺が彼女の家族に厳しい目を向けすぎなんだろうけど。"



hi "リリーは優しすぎるよ。そう思わない？"

show lilly basic_surprised_che_close
with charachange


li "えっ？"


hi "ほとんどの人はそんなことされたら親を恨むと思うよ"

show lilly basic_weaksmile_che_close
with charachange



li "まあ、そういう人も確かに……"




"眉をつり上げる俺に気づくことなく、グラスから一口飲む。ワインはいともたやすく減っていく。アルコールの風味が苦にならないくらい、リリーはワインが好きみたいだ。俺には真似できない。"



show lilly basic_smile_che_close
with charachange



li "久夫さんはどうなんです？　学校生活はどうでした？"




hi "俺？　そうだなあ……"



hi "俺のはいたって普通の公立校で、たぶん標準よりはちょっと忙しかったかな"



hi "クラスでは結構うまくやってたし、サッカー部にいたんだ。俺は一人っ子で、両親は共働きで２人とも働きづめだったから、３人の友達と一緒にゲーセンに入り浸ってお金を無駄使いしてたよ"




hi "だけど、どの台で何回プレイしても、舞には絶対勝てなかったな。拓海や伸だって、舞にはいつも負けてた。そしたら伸と舞はまた対戦し始めるから、俺は保護者役をするはめになってた"





hi "その４人だけで、目的もなく青春を謳歌してた。くだらない楽しい時間だったな"





"ぼーっとし始めている自分に気づいて、俺は我に返る。前の学校での日々は消え去り、窓の外には夜空と鮮やかな街の明かりがあった。"




"リリーは好奇心と同情心の混じった複雑な表情をしている。リリーの厳しい学校生活を考えると、こんな生活は彼女が知っていた唯一の生活とは面白いくらいに正反対なんだろうな。"



show lilly basic_satisfied_che_close
with charachange



li "以前の学校生活はとても楽しかったみたいですね"




hi "そのうちどれくらいがただのノスタルジーなのかはわからないけど、いい思い出もあるよ"




hi "でもそれは昔のことさ。もうあの頃には戻れないけど、俺は発作のおかげで新しい人生を見つけたんだ。こんな人生を送ることになるなんて、思いもよらなかった"





hi "山久の静かで安らかな雰囲気、科学という将来の新しい進路、静音やミーシャ、華子との友情、そして何よりも、リリーを"


scene ev lilly_touch_cheong
with whiteout



"リリーが俺のほうに手を差し出し、心からの笑顔を見せる。彼女の指が俺の顔をかすかに探り、そして頬を優しく撫でる。"


scene bg city_restaurant at right
show lilly basic_smileclosed_che_close:
    center
    ypos 1.1
with whiteout


"ウェイターが料理を持ってこちらにやって来るのに気づき、リリーが温かい沈黙をほんの少し保ってから名残惜しそうに手を引っ込める。"



"沈黙を保つウェイターのせいで会釈をする向きがほんの少しずれていることを除けば、リリーの振る舞いはとても手際が良く、目が見えないことをほとんど感じさせない。"





"リリーは本当に人前でできるだけ普通に見えるよう懸命に努力している。前から気づいてはいたけど、それが特別扱いをされたくないからなのか、ちょっとした見栄なのか、その両方か、今でもよく分からない。"



scene ev lilly_restaurant_eat
with shorttimeskip



"並べられた料理はサラダという名前に見合っていて、量も満足のいく多さだ。スライスされた卵とトマトが盛りつけられ、とても食欲をそそる。"




"リリーは片方の手にナイフ、もう片方の手にフォークを持つと、さっそく俺と同じように料理を食べ始める。普段の夕食より遅い時間なので、２人とも夢中になって食べる。"


scene ev lilly_restaurant_chew
with locationchange




"俺が葉っぱと、恐らく肉だと思われる立方体を用心深くフォークで突き刺している間、リリーは黙ったまま正確にサラダをつつき、咀嚼する。"




"時々料理に入っている食材の側面あたりをつついてその輪郭を探るしぐさだけが、リリーの目が見えないことの唯一の証だ。"



scene bg city_restaurant at right
with locationchange



"俺はすぐに料理を平らげる。リリーは俺が見守る中、最後の一口を食べ終える。"


show lilly basic_smile_che_close:
    center
    ypos 1.1
with charaenter


li "久夫さん、食べ終わりました？"



hi "ああ。すごくおいしかった"




"それは本心だ。単なるサラダがこんなにうまくて腹を満たすものだとは思わなかった。だけど、やっぱりそこがこの店の食事がこんなに高く付く理由なんだろう。"


show lilly basic_smileclosed_che_close
with charachange


"俺の評価に満足して、はっきりと同意するようにリリーが小さくうなずく。"


hi "あのさ、リリーはハーフで外国風な外見だし、すごく可愛いし、今まで誰もリリーに告白しなかったのが驚きだよ"


show lilly basic_planned_che_close
with charachange



li "誰もしなかったと思ってるんですね"




"その簡単な言葉に虚を突かれる。驚いちゃだめだ、俺だってたった今リリーを褒めたじゃないか。"



hi "ほんとに？"

show lilly basic_smile_che_close
with charachange



li "何度か告白されましたよ。ここの学校でも、前の学校でも"


show lilly basic_weaksmile_che_close
with charachange


li "青春って、おかしな時間です"


"まるでそれがリリーにとって遠い過去であるかのような言い方をしてるな……"


hi "へえ、そんなこと簡単に言うんだ"

show lilly basic_surprised_che_close
with charachange

with Pause(0.5)

show lilly basic_cheerful_che_close
with charachange


"リリーがしばらく驚いたような様子を見せ、それからおどけた薄笑いを浮かべる。"


li "嫉妬……しているの？"


hi "何だって？　いや、違うよ"

show lilly basic_giggle_che_close
with charachange



li "久夫さんは、嘘が下手です。それは覚えておいてくださいね"


show lilly basic_smileclosed_che_close
with charachange



li "でもやっぱり、私は久夫さんの誠実さが好きです。時にはそんなつもりじゃないことがあるとしても"




li "他の人に向き合う時、久夫さんの正直さは必ずあなたのためになると思います"




"俺は今言われたことを全部否定するふりをして咳払いし、どうにか話題を変えようとする。"



hi "でも正直言うと、俺は人に囲まれているよりは１人でいる方が好きだな。俺がリリーみたいに社交的な関係を保てるとは思えないよ"

show lilly basic_listen_che_close
with charachange


"それを聞いて、リリーがしばらく考え込む。"

show lilly basic_smile_che_close
with charachange



li "それも本当じゃないと思いますよ"


show lilly basic_smileclosed_che_close
with charachange



li "久夫さんが華ちゃんのことをどれだけ優しく気を使っているか、他人と、ほとんど知らない人とさえとてもうまくやっているのを、私は知ってます。久夫さんはいろいろな人付き合いがとても上手だと思いますよ"



show lilly basic_cheerful_che_close
with charachange



li "だけどその話をするなら、久夫さん、あなたの受けた告白は？　久夫さんのような男性に憧れる人が、少なくとも１人は絶対にいたはずです"




"それに答えようと口を開いた時、自分の表情が少し陰るのを感じる。こんな時ばかりは、リリーが俺の表情を見られないということを密かにありがたく思ってしまう。"




hi "１人……だけ。岩魚子って子が"


hi "心臓の発作が起きたのが、彼女から告白を受けた時なんだ。真冬の森の中で"

show lilly basic_oops_che_close
with charachange


"話題がこんな方に向いてしまうことを予想していなかったリリーは、押し黙ってしまう。"



"俺の健康状態は今までずっとリリーの心配の種だった。できる限り心配をかけないよう努力をつくしてきた。体のほうは全力でそれに抗っていたけど。"







hi "その後、俺が入院しているあいだ、岩魚子はしばらく見舞いに来てくれた。何週間も通いに来て、話をしていたよ。だいたいは世間話とか、クラスのうわさ話とか、でもそれだけで十分だった"





hi "だけどそのうちに……岩魚子は来なくなった"




hi "毎日来てくれてたんだ。それから一日おきになって。週一回になって。そしてとうとう、ある日を境に、完全に来なくなってしまった"


show lilly basic_sleepy_che_close
with charachange



li "岩魚子さんには……また会えましたか？"




label jp_choiceL24:
menu:
    with menueffect
    "自分の生きる世界のみにとらわれた俺は、首を横に振ってから、そのしぐさに意味がないことを思い出す。"
    "手紙のことを話す":






        return m1
    "話題をそらす":


        return m2








label jp_L24a:



"岩魚子が送ってきた一通の手紙が頭に浮かぶ。"




hi "それ以来会ってない。だけど、俺が山久学園に転入した後に……手紙が来たんだ"




"リリーが俺のよく知っている表情を見せる。関心を引いてしまったんだ。それがただの好奇心からでしかないということに少し傷つくけど、リリーは自分の反応を隠すのがあまり得意じゃないしな。"





hi "今考えてみても、別にどうってことない手紙だったんだ。俺がいたクラスがどうなってるとか、彼女の調子はどうだとか。それから、ほとんど思い付きみたいに、たぶんもうお互いに会わない方がいい、って"




hi "それを読んだ後、もう吹っ切れたと思っていたたくさんのことを、また考え直すはめになった。大体は、俺のまわりの世界はずっと動き続けてたこととか、そこから俺があまりにかけ離れてしまったこととか"





hi "それから……たぶん、俺が失ってしまったものにも気づかされたんだろうな"


show lilly basic_emb_che_close
with charachange



"リリーはしばらく考えた後、はっとひらめいたような表情に変わる。間違いなく、この手紙のせいで俺が屋上の昼食時に悩んでいた、ということに勘づいたんだ。"




"リリーがこんなに長い間、言葉を失っているのは珍しい光景だ。最初は熱心そうに興味を示していたのが、今は全身の気配がちょっと落ち込んでいる。"
"誰にも劣らないカリスマの持ち主ではあるけど、それが人生や人間関係の経験の代わりにはなるわけではないんだ。"





show lilly basic_reminisce_che_close
with charachange




li "たぶん……手紙を送らないよりも、送って良かったと思います"



hi "どうして？"

show lilly basic_weaksmile_che_close
with charachange



li "長い間会っていない人とコミュニケーションを取るときに、一番いい方法を考えるのが難しいこともあると思います。久夫さんと岩魚子さんのそれぞれの状況を考えれば、なおさらです"




li "岩魚子さんは安易な解決法を取らずに、久夫さんと最後のお話をするために勇気を振り絞ったんです。岩魚子さん本人のためだけではなく、そのお話から察すると、久夫さんのためにも"




hi "そうかもね。そのことで岩魚子を嫌ったりはしないよ、今までに嫌いだと思ったことなんてないけど……分かんないな"




"たぶん、もっとはっきりした返事をするべきところだ。でもそれなりの理由はある。俺はこんなふうに岩魚子の立場から状況を考えたことがなかった。"





label jp_L24b:



"必要以上に岩魚子の話題に触れたくはない。実際、このデートは俺とリリーのためのものだ。こんな時に俺の過去の関係のことを考えたくない。"



hi "いや、その時岩魚子に会ったのが最後だよ。それからは話もしてない"




label jp_L24c:


"沈黙の時間がしばらく流れ、そしてリリーが口を開く。"

show lilly basic_sad_che_close
with charachange



li "山久に移るのは久夫さんにとってとてもつらいことだったでしょうね。久夫さんに落ち度はないのに、友人だけでなく、恋人からも引き離されてしまうなんて"





hi "最悪な時期は入院している間に過ぎちゃったよ。周りにあるものが四方の白い壁と小さなテレビだけになったら、もう吹っ切れちゃうんだ"









hi "たぶん、ここも前の学校みたいなもんだな。なるべく過ぎたことにはくよくよせずに、先のことを考えるようにしてるよ"





hi "過去を振り返っても憂うつになるだけだし、やっと生活の調子が戻りつつあると思えるようになったのも、大部分はリリーのおかげだよ"


show lilly basic_veryemb_che_close
with charachange


li "それを聞けて……嬉しいです、久夫さん"



"リリーが物思いにふけるように少しうつむく。俺のおしゃべりが過ぎたせいで困らせてしまったみたいだ。"



hi "リリーだってやっぱり山久に入学した時、少しは俺と似たような経験をしてきたんじゃないか？　実際、ここの学校のほとんどの生徒は似たような経験をしたと思うんだ"



hi "前の学校にも友達がいたって言ってたよな。一緒に来てくれた人が多かったとは想像しにくいけど"


show lilly basic_displeased_che_close
with charachange


"リリーの深い笑みが失せ、予想外に暗い表情を浮かべる。両手さえ膝の上に引っ込めてしまったほどだ。"


"長い時間の後、リリーが口を開く。"

show lilly basic_reminisce_che_close
with charachange



li "久夫さん……誰にも話さないと約束してくれますか？　今から私が言うことを――"




hi "約束する"


"俺の真剣な声にリリーは少し驚いたようだったけど、すぐに気持ちを緩めて弱々しく微笑み、話を続ける。"

show lilly basic_weaksmile_che_close
with charachange


li "山久に移った時、前の学校の友人を失うことが私にはとても残念でした"

show lilly basic_reminisce_che_close
with charachange



li "だけど、一番残念だったのは、ある人に会えなくなること。私が英語を将来の進路にと考えたのは、彼が理由なんです"



"『彼』？　リリーが女子校出身だということを考えると、クラスメイトではありえない。それなら……"



li "彼のために、私は他の人たちから受けた告白を断り続けました。私の英語が上達するたびに彼がほめてくれるのが、私にとっては一番大切なご褒美だったんです"


show lilly basic_weaksmile_che_close
with charachange




li "おかしいですよね？　告白してきた人たちのことを自慢げに言う私のような人間が、家庭教師みたいな絶対に手の届かない人を好きになるなんて"







li "本当、最高に馬鹿げたこと……"



hi "その人には……？"




"リリーが首を素早く左右に振る。"

show lilly basic_displeased_che_close
with charachange



li "できませんでした。あの時だって、無理なのは分かっていたんです"



"沈黙がその場を支配する。"



"英語を教えるという進路にリリーが強い関心を寄せる理由も、これで説明がつく。でもリリーが打ち明けてくれた話のことを考えずにはいられない。"







"リリーはその人に想いを伝えることなく、その人を失ったんだ……そんなことが再び起こるのを恐れているんだろうか。でも、俺に対して？"







"どうとらえればいいのか、よくわからない。そういう関係のことは聞いたことがある。思春期と若さといったものから生まれるタブーだ。ただ、リリーが賢明にも一線を越えなかったことを心強く思う。"




show lilly basic_emb_che_close
with charachange



li "こんなことを言うのはおかしいって分かっています。だけど、お願いです……私のこと……"




hi "どうしてそのことで俺がリリーを見損なう必要があるんだ？"




hi "正直さ、もしリリーがその人をそんなに好きだったなら、きっとその人はすごくいい人だったに違いないと思うよ。それだけじゃなくて、リリーだって節度を持ってたんだし"


with Pause(1.0)

show lilly basic_arablush_che_close
with charachange



"リリーがしばらく呆然とした様子を見せる。だけど全く予想外なことに、リリーが次の瞬間笑い出す。その笑い声に虚を突かれる。含み笑いでも、控えめなくすくす笑いでもない、誠実な正真正銘の笑いだ。"






"俺は自分が微笑んでいるのに気づく。リリーが安心と喜びを見せているからだけじゃない。最も個人的な秘密まで俺に打ち明けるほど俺を信頼してくれているからだ。"


scene ev lilly_touch_cheong
with whiteout



"俺が気づかないうちに、リリーの手の平が俺の顔に触れる。それはいつもと同じように優しく、親指がゆっくりと俺の頬をなでている。"



li "優しいですね、久夫さん。心から愛しているわ"


"手の平で俺の顔を優しく愛撫するリリー。彼女の顔をこんなふうに見られるなんて……今夜はなんていい夜だろう。"



hi "俺たち２人とも、変わった過去を持ってるみたい、かな？"



li "ほとんどの人の基準から考えれば、私たちの現在も変わっていると思いますよ"





"俺は笑いながら頭を垂れる。リリーはいとも簡単に俺をやり込めてしまうことができる。それは間違いない。"




scene bg city_restaurant at right
with whiteout


"俺は客たちのひそやかな話し声が続いている部屋の中を見回す。"



hi "たぶんこの場所も『変わってる』部類に入るだろうな"


show lilly basic_weaksmile_che_close:
    center
    ypos 1.1
with charaenter



li "少し……分不相応ですね"



hi "そうそう、そういうこと"



"せわしなく動き回るウェイターが俺の目を引く。背は低く痩せこけていて、２０歳にもなってなさそうだ。何となく健二を思わせるけど、あいつみたいに真夏に冬の格好をしていたりはしない。"



show lilly basic_smileclosed_che_close
with charachange



"ウェイターがそっけなくおじぎをして皿を下げると、リリーは礼儀正しく静かに彼に会計を頼む。"




"ウェイターは熟練の調和した動作で、皿を手に持ったままテーブルを巧みにすり抜けて伝票を取りにいく。"




"間髪入れずウェイターがドアの向こうから再び現れ、優雅に差し出された会計をリリーが受け取り……"



show lilly basic_smile_che_close
with charachange


"……そして即座に俺に渡す。それを見たウェイターが眉を上げる。"



"俺はプリントアウトされた小さな伝票を読む。予想よりもかなり高い金額だ。"




show lilly basic_surprised_che_close
with charachange


li "久夫さん？"


hi "え……ああ……"

show lilly basic_smileclosed_che_close
with charachange



"俺が口ごもりながら金額を言うと、リリーはただうなずいてハンドバッグに手を伸ばす。"




"ウェイターはリリーからクレジットカードを受け取り、再びドアの向こうへと消える。"


hi "あれは……不釣り合いなほど高かったぞ"

show lilly basic_emb_che_close
with charachange



"今の一言は、リリーを少し気まずくさせたみたいだ。"


show lilly basic_weaksmile_che_close
with charachange



li "私の家族は、教育のために十分すぎるくらいお金を与えてくれるんです。姉さんにもですけど、姉さんはそのことを言われるのを嫌っています"


show lilly behind_cheerful_che_close
with charachange



li "と言っても、私も散財は嫌いです。だけど今回は例外にしてもいいと思っています。久夫さんのためだけに"




hi "デートの場所を選んでくれただけじゃなくて、食事代まで払ってくれるなんて……"


"俺は指で目元を押さえる。"



hi "信じられないくらい次のデートのハードルを上げてくれたよな"

show lilly basic_giggle_che_close
with charachange


"リリーがくすくすと笑う。"

show lilly basic_smileclosed_che_close
with charachange


li "楽しみにしていますよ、久夫さん"



"ウェイターがまるで魔法のように再び俺たちのそばに現れ、リリーにカードを返す。リリーが盲目であることに気づいているようで、たぶん不必要なくらいに念を入れて、しっかりと彼女の手にカードを握らせる。"




"俺がおかしな表情をしているにも関わらず、ウェイターはプロ精神を発揮して、無表情のまま去って行く。"





"俺は両手をポンと合わせると、今夜のデートをお開きにするために席から立ち上がる。"



hi "では、そろそろ参りましょうか、お嬢さま？"


stop music fadeout 2.0

scene black
with dissolve




label jp_L25:

scene black
with Dissolve(2.0)

scene bg school_dormhisao_ni
with vpunch


hi "ぎゃあ！"



"布団から飛び起き、背筋をまっすぐに伸ばしてベッドの上に座る。まるで電気ショックが体を駈けめぐったみたいだ。"




"素肌を伝わる汗のせいで夜の空気がひんやりとする。呼吸がぜえぜえと乱れて、まるで過呼吸寸前だ。"




"気持ちが落ち着かないまま、パニック状態の自分の体を落ち着けようと頭を手で押さえる。顔に押し付けている間もその手がぶるぶると震えていることにさえ、しばらく経つまで気づかなかった。"





"完全な静けさの中、時間が過ぎていく。ありがたいことに、心と体を落ち着かせようとする俺の必死の努力は、ゆっくりと功を奏し始める。"




"落ち着きを取り戻しながら、俺は自分の身に起こっている状況を把握し始める。まるでマラソンをした後みたいだ。全ての筋肉がこわばって、汗が文字通り滝のように流れている。"




"胸の鼓動に慎重に意識を向けて、そのリズムを頭の中で探る。確かに、俺の当てにならない心臓は、今回は正常に機能している。"



"ただ……あれは一体なんだったんだ？"


"心臓発作？　ひどい悪夢？　薬の副作用？　パニック発作ってのを聞いたことがある。たぶんそれが当てはまるような……"



"今はもう考えたくもない。あんなことの後では、ヘトヘトなのに完全に目が覚めてしまった。"





"ベッドの反対側を見る。静かにたたずむ人影の顔の青白さが、夜の部屋の闇に浮かび上がる。その光景だけで、俺の心が落ち着くには十分だ。"


scene ev lilly_sleeping_smile:
    truecenter
    zoom 1.0 subpixel True
    acdc_warp 20.0 zoom 1.05
with locationchange



"寝ているときでさえ、リリーの上品な振る舞いは失われることはない。その完璧に秩序だった息づかいと穏やかな顔からでは、リリーが今起きているのか本当に寝ているのか、判別するのは不可能だ。"




"誘惑にかられて、リリーの手を指先で丁寧になぞる。いつもそうであるように、その肌は柔らかな手触りで、それでいて寒い夜でも暖かい。"





"俺とリリーがお互いに最も近い存在のように感じて、それを静かに感謝するのは、こういう時なんだ。"



"リリーの手首の上で指を止め、それから手をそばのベッドに引き戻す。"





"なぜかはよくわからないけど、リリーとの距離が縮まるにつれて、俺たちの間で何かが大きくなっていく感じがしていた。それが何なのか、俺たちが恋に落ちる前から存在していたのかさえ、よく分からない。"





"あらゆることがこんなにも目まぐるしく移り変わっていく。俺は全く構わないけど、こうしてどんどん物事を推し進めるのはリリーらしくない気もする。"


scene bg school_dormhallway
with shorttimeskip

play music music_dreamy fadein 2.0



"幸い、朝のこの時間に廊下を歩き回っている生徒は１人もいない。そうじゃなかったら、あわてて制服を着込んだことがバレバレの俺がどうして２食分の朝食を部屋に運んでいるのかと質問攻めにあうだろう。"





"もちろん、そういうことが起こらないとは限らない。隣り合った寮部屋の間を１人の警備員が見回るからといって、そんなものは青春期のホルモンに比べたら微々たる力しか持たない。"




"考えてみれば、きっと月曜の朝だから助かってるんだろう。どうしてかはよく分からないけど、俺は他の大抵の人ほどには月曜が苦にならない。"



"少し独創的なやり方で手とひじを使って、ようやく自分の部屋のドアを開けることに成功する。"

scene bg school_dormhisao
show lilly basic_sleepy_paj at center
with locationchange


"部屋に入ると、ちょうどベッドから起き上がって眠そうに眼をこするリリーの姿が目に入る。俺が以前よく見てきたリリーの寝起き姿と同じく、ひどい様子だ。リリーは本当に朝型人間じゃないんだな。"


hi "ごめん、起こすつもりはなかったんだ"


show lilly basic_displeased_paj
with charachange



"リリーが頭をフラフラと振る。差し込む朝日の光が彼女を照らし、とても心地よい光景を作り出している。"


show lilly basic_weaksmile_paj
with charachange


li "いいんですよ、どうせ起きなければいけないのだし。何時ですか？"


"俺は自分の朝食を机の上に置くと、時計をこっちに向けて時間を確認する。"


hi "まだ早いな。登校時間まではまだたっぷり時間があるから、心配いらないよ"

show lilly basic_smileclosed_paj:
    ypos 1.2
with dissolvecharamove


"リリーはベッドの脇に座ると、クンクンと匂いを嗅ぎ始める。それを見て俺はすぐに朝食を彼女から引き離し、俺のそばの机の上に置く。"




hi "ああ、朝ごはんを持ってきた。だけど、シャワーと着替えが先だな"


scene ev lilly_kissing
with flash



"リリーが立って、あごをほんの少し突き出したまましばらくじっとしている。俺は喜んで従い、唇をリリーのそれに押し当て、その柔らかい感覚を味わってから唇を離す。"



scene bg school_dormhisao
with locationchange



"リリーはとても満足した様子で甘い微笑みを見せると、ゆっくりとシャワールームへ向かう。"



"俺はもう少し目をよく覚まそうと伸びをしてから、ちらりと湯気の立ち上る朝食を見る。ご飯、魚、みそ汁と野菜。ちょっと特別な日の、ごく普通の朝食だ。"



"机の上の瓶をつかんで、処方された１日分の薬を飲み始める。"


show pills:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)



"最初の発作以来襲ってきたもろもろのトラブルを考えると、こんなのが一体何の役に立ってるんだろうと時々疑問に思う。これまでの薬の副作用を考えたら、害にはならないと言うことさえできない。"






"まあ、とにかく。薬を飲めというのが医者の命令だ。それに、自分よりも医者の診断を信頼するほうが役に立つだろう、と俺の理性が告げている。"



show pills:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide pills
with None



"シャワーの音がやむのにそう長い時間はかからない。この状況なので、軽いシャワーを浴びるだけでもリリーには十分みたいだ。"






show lilly basic_smile_paj:
    center
    xpos 0.55
    easein 0.5 xpos 0.5
with charaenter



"シャワールームから出てきたリリーは落ち着くことができたようで、見るからにさっきよりもはっきり目が覚めている。"


show lilly basic_smile_paj_close at center
with characlose

show lilly basic_smileclosed_paj_close:
    ypos 1.1
with dissolvecharamove




"俺は何も言わずにリリーの手を優しく取って、机のほうへと導く。俺の部屋にはリリーの部屋のようなテーブルはないので、これで間に合わせるしかない。"





li "ありがとう、久夫さん。朝食のメニューは何ですか？"




hi "ご飯とおかずぐらいだよ。てっとり早いし"





show lilly basic_ara_paj_close
with charachange



"それを聞いてリリーが顔を輝かせる。"



show lilly basic_satisfied_paj_close
with charachange



li "それは豪勢な朝食ですね。普段からこうなんですか？"




"お世辞で言ってるだけだろうな。リリーの過去を考えたら、これが彼女の基準から見て高級料理とは言いがたいことはまず疑う余地がない。"




hi "朝食は三食の中で一番大事だからな。俺たちが学生だからって理由だけで朝食を軽く済ますわけにはいかないよ"



"とにかく、それが俺の信条だ。今までその話をした人々からのリアクションを考えると、俺は少数派なのかもしれない。"


show lilly basic_smileclosed_paj_close
with charachange



"俺はベッドの端に座り、リリーと朝食を食べ始める。ちょうどデートの時にやっていたのと同じように、リリーは野菜の輪郭をはしで軽くつついている。"


show lilly basic_smile_paj_close
with charachange


li "とてもおいしいです、久夫さん。こんなにお料理が上手だなんて知りませんでしたよ"




"今のはさっきよりも本心で言っているな。そのくらいはわかる。とはいっても、料理なんて全然特別なことじゃない。ちょっと練習すれば、シンプルな料理ならけっこう簡単に作れるんだ。"





hi "ほとんどは現代技術のおかげだよ。それでも、何年も自炊してるから、料理もうまくなってることを願うよ"



hi "両親が共働きで、仕事で家にいない時にインスタントラーメンや宅配ピザばっかり食べるのに飽きちゃったんだ。それで、独学で自炊を始めた。今でもコツをつかもうとがんばってるけど"


show lilly basic_cheerful_paj_close
with charachange



li "久夫さんもいつか、いい奥さんになれますよ"




"俺はご飯つぶを１つ取って親指に乗せ、よく狙ってからはじき飛ばす。"


show lilly basic_surprised_paj_close
with vpunch



"ご飯つぶはリリーの頬に当たり、リリーは驚いて少し跳ねる。狙い通りだ。"


show lilly basic_pout_paj_close
with charachange



"リリーをダシにしつつも、俺はくすくす笑わずにはいられない。リリーは眉をひそめて、懸命に真剣で厳しい表情を作ろうとしている。"






show lilly basic_sleepy_paj_close
with charachange


li "ああ、そうだ……"


hi "どうしたの？"

show lilly basic_concerned_paj_close
with charachange

$ renpy.music.set_volume(0.5, 1.0, channel="music")



li "昨夜寝ている間に、何かあったんですか？　休めていないようだったので"




"じゃあ、あの時リリーは起きてたのか。少なくとも半分は起きてたんだ。あれが心臓の不調だろうと、薬の副作用による悪夢のせいだろうと、俺にとって一番嫌なのはリリーにこれ以上心配をかけることだ。"





"リリーと付き合い始める前でさえ、何をするにしても自分の体は足手まといになっていると感じていた。この体は俺だけの重荷だ。だからリリーと一緒にいる限り、俺はできるだけ普段どおりに振る舞おう。"



hi "いや、特に何も"

show lilly basic_reminisce_paj_close
with charachange


li "そうですか……それならいいんです"

$ renpy.music.set_volume(1.0, 4.0, channel="music")



"幸い、リリーは俺の言葉を信じてくれているみたいだ。"


show lilly basic_weaksmile_paj_close
with charachange


li "そういえば、もう一つ聞きたいことがありました"


hi "え？"

show lilly basic_smileclosed_paj_close
with charachange


li "どう言えばいいのか……"

show lilly basic_smile_paj_close
with charachange


li "久夫さんが夢を見るとき……人やものは見えるんですか？"


hi "ああ、そりゃそうだよ……あ"



"真面目な返事ではあっても、口を滑らせてしまったことに俺は少なからずうろたえる。だけどリリーは気にしていないみたいだ。"


show lilly basic_smileclosed_paj_close
with charachange


li "でも、味わったり、感じたり、嗅いだりはしないでしょう？"



"それに答えようとするけど、考えをめぐらせる前に詰まってしまう。それを考えれば考えるほど、リリーの仮説が正しいと思わされてくる。"





hi "それは……そうだな、たぶん。そんなふうに考えたことなかったよ。リリーはそういう風に夢を見てるってこと？"


show lilly basic_smile_paj_close
with charachange



li "ほとんどの場合、夢の中では聞くだけですが、確かに時々触ったり嗅いだりすることもありますよ"


show lilly basic_planned_paj_close
with charachange


li "そのことを姉さんに話した時、姉さんはそれをとても変に思ったんです。だから聞いてみたくて。もし久夫さんもできないなら、きっとそれは私の盲目のおかげでしょうね"


hi "理にかなってるよ。リリーは俺よりも視覚以外の感覚に多く頼ってるから、きっと夢にもその影響が現れるんだ"


"人体の神秘、だろうな。"


"登校前の残りの時間、俺たちは目の前にある量たっぷりの食事を素早く平らげ、いつものように軽くおしゃべりを交わす。"

stop music fadeout 2.0

scene bg school_dormext_full
with shorttimeskip



"ドアの向こうを素早く覗き見て、誰も男子寮の入り口のほうを見ていないことを確認し、俺たちは人目に付くことなく外へと歩み出る。"


play music music_soothing fadein 4.0


hi "おっ、今日はいい天気だぞ"



"２人揃って外に出たところで、俺は伸びをする。明るい朝の日差しが俺たちを照らしている。"




"この時間になると、寮や正門から校舎へ向かう生徒たちの中にも、何人か俺と同じように伸びをしているのが見える。"



show lilly cane_smile_close at center
with charaenter


li "本当に快適で暖かいですね"


"俺とリリーは手をつなぎ、リリーは杖で地面をついている。俺たちは本格的に校舎へと向かい始め、周りでおしゃべりをしながら登校する生徒の集団に加わる。"

show lilly cane_smileclosed_close
with charachange


li "今日が試験の最終日、でしたね？"


hi "ああ。試験の出来はどう？"

show lilly cane_concerned_close
with charachange



li "全体的には、上出来ですよ。だけど久夫さんは試験のせいで少し疲れているみたいですね"




hi "そんなにはっきりわかる？"




hi "だけど、試験のことだけじゃないんだ。短い間にいろんなことが起きてるし、それに文系科目はあまり得意じゃないから"


show lilly cane_smileclosed_close
with charachange


li "でも、科学は得意なんですよね？"


hi "まあ、俺にとって科学は苦じゃないんだ。そういえば、リリーは科学と数学がそんなに得意じゃないって言ってなかったっけ？"

show lilly cane_oops_close
with charachange


"突然リリーがおどおどしたような表情を見せる。図星だな。彼女の誇り高さはまさに諸刃の剣だ。"



show lilly cane_smile_close
with charachange


li "まあ、そのことは置いておいて……久夫さんはその能力を何かに生かそうと考えたことがありますか？　使わないのはもったいないですよ"


hi "少しだけ、ほとんど武藤先生にせっつかれて"


hi "何にしろ、俺はたぶん何らかの形で科学に関わるような進路を選ぶだろうな"

show lilly cane_smileclosed_close
with charachange


li "それはいいですね、久夫さん"

scene bg school_gardens at bgleft
with locationchange

stop music fadeout 0.3
with vpunch


"庭園に入ると、頼んでもいないのに誰かが突然俺の背中を叩く。"


"緑の服に身を包んだその犯人が俺の前に躍り出る。そばのリリーのことは明らかに気にも留めていない。"

play music music_kenji fadein 0.5

show kenji neutral:
    center
    xpos 0.55
    easein 0.5 center
with charaenter


ke "よう、調子どうだ？　しばらく見なかったな"



hi "よう。ちょっと試験やなんかが忙しかったからさ"


show kenji tsun at center
with charachange



ke "試験、シケンか。本物のルネサンス教養人ってのは、勉強なんてしなくたってそんなもの楽勝なんだよ"




"出席記録はろくでもないし、労働倫理も欠如しているとはいえ、健二は学校の成績はいいタイプに見える。だから頭の良さを疑う理由もあまりない。"




"正直言うと、健二が少しうらやましい。試験勉強やリリーと一緒に過ごす時間のせいで、俺は自分の時間をほとんど取れていない。これは優子さんが感じていることに少し似ているのかも知れない。"


show kenji tsun at tworight
show bg school_gardens at center
with charamove

show lilly cane_smile_close at twoleft
with charaenter



li "おはようございます、瀬藤くん。お元気そうで、なによりです"




"リリーが形式ばった話し方をするのが、なんだか変な感じだ。俺に対してはこの数ヶ月でもっと気楽に話してくれるようになったけど、クラスメイトに対してはもっと堅い話し方をするのも時々目にしている。"





"絶対に変わらない人だっていると思うし。リリーの穏やかで丁寧なふるまいが悪いと言っているわけじゃない。実際それが最初にリリーと一緒にいると楽しいと思った理由の一つなんだから。"



"健二は俺のそばの人物が誰なのかをしばらく探っているようだ。たぶん俺とリリーが手をつないでいることも気づいていないだろう。健二のメガネって、実際役に立ってるんだろうか。"

show kenji neutral at tworight
with charachange


ke "おっ、よう、リリー。お前も試験がんばれよ"

show kenji tsun at tworight
with charachange


ke "じゃ、放課後にな"


"健二が少し語気を強めるのを聞いて、俺はそれが気軽な別れのあいさつというより命令の意味合いを持っているんだろうと考える。後でことを丸く収めないといけないだろうな。"


hi "ああ。じゃあな"



show kenji invis:
    xpos 0.6
with dissolvecharamove

hide kenji
with None


"健二がそっけなくうなずいて俺たちのそばを通り過ぎようとする。だけど、リリーのいる辺りをにらむのに気を取られ過ぎて彼女の杖に気づかない。"

show lilly cane_surprised_close at twoleft
with charachange


"俺が事態を防ごうと行動を起こす前に、健二が杖につまずいて思わず何かをつかもうと手を伸ばす。不運なことに、リリーの腕が、その何かの役割を担ってしまう。"

show lilly cane_surprised_close:
    easeout 0.3 ypos 1.2 alpha 0.0
with Pause(0.5)

play sound sfx_pillow
hide lilly
with vpunch


$ doublespeak(ke,li,"うおっ！", "きゃっ！")


"自分の無力さを感じている俺をよそに、２人が手足を投げ出して折り重なるように地面に倒れる。"


hi "あっ、くそっ。２人とも大丈夫か？"

show kenji invis:
    center
    ypos 1.2
with None

show kenji neutral:
    ypos 1.0
with dissolvecharamove


"健二はこのアクシデントに動じる様子もなく、素早く立ち上がる。"


ke "問題ねえ、問題ねえさ。何でもねえよ、俺の体はもっと酷い虐待にも耐えられるからな"


"リリーはうつむいて芝生の上に横たわっている。ケガはなさそうだけど、何よりも驚きが大きかったみたいだ。俺は彼女を助けようと手を差し出す。"



hi "リリー、大丈夫か？"

show kenji happy
with charachange


ke "ほらよ、砂藤？"



"健二も手を差し出し、リリーの手をためらいがちに触って自分の申し出を伝える。"





"健二は時々不愉快なことを言うけど、たぶん根は正真正銘いい奴なんだろう。俺がそう思ってると知ったら健二はけっこう気を悪くするだろうけど。"


stop music fadeout 2.0



"だけどリリーが何の前触れもなく自分のこぶしを何度も地面に叩き付け、俺も健二も驚いてしまう。"



play sound sfx_impact
with vpunch


li "ああっ、もうっ！"

show kenji tsun
with charachange


"怒りを爆発させるリリーにびっくりして健二が固まる。俺はただショックを受ける。リリーがこんな態度をみせたことは今まで一度もなかった。静音がいた時でさえも。"



ke "あー……"

show lilly invis_close:
    twoleft
    ypos 1.2
with None
show lilly cane_mad_close at twoleft

with dissolvecharamove



"周りに人がいることをたった今思い出したかのように、リリーがゆっくりと腰を上げる。その時の顔を見て俺は少しひるんでしまう。"


show lilly back_listen_close
show lillyprop back_cane_close at twoleft
with charachange



"リリーが背を向ける前にほんのちらっと彼女の表情を見るけど、それは簡単には忘れられないような印象を残す。"




"静音と衝突した時もいらついた態度をたくさん見せていたけど、今回の激怒ぶりはあの時とは違う。これは明らかに今のささいな事件だけのせいじゃない。"



hide lilly
hide lillyprop
with charaexit


"リリーはしばらく立ち尽くし、それからため息をついてむこうへと歩き出す。俺には原因がさっぱり分からない。"



hi "ええと……また後で話そう。それじゃ"



ke "おう、またな"

hide kenji
with charaexit



"健二は頭の後ろをかきながら何か言おうとしたあと、肩をすくめて距離を取るように立ち去る。"


show bg school_gardens at right
with charamove

show lilly back_listen at center
show lillyprop back_cane at center
with charaenter


"俺は素早くリリーに追いつく。リリーは少しだけ振り返って俺の存在を認識するけど、それ以外は何の態度も示さない。"



"こんなかんしゃくを起こしたことを叱るべきなのかもしれないけど、同時にあまりこのことで言い争いもしたくない。リリーはまだ明らかにひどくいらついている。"



"結局、俺は口を閉ざしたままリリーが冷静になるのを待つ。"

scene bg school_hallway3
with shorttimeskip



"２人とも黙ったまま歩き続け、ついに３階に続く階段の最上段へとたどり着く。俺たちがいつも別れている場所だ。"


show lilly cane_listen_close at center
with charaenter



"リリーが去る前に俺は彼女のほうを向く。普段俺たちが分かち合っている心地よく暖かい沈黙は確かに好きだけど、今のは全く違う。このままにしておくのは嫌だ。"



hi "なんか……最近普段より口数が減ってる気がするけど。どうかしたの？"


show lilly cane_displeased_close
with charachange



"俺が向けるどんな心配も全て払いのけるかのように、リリーがほとんど自動的に首を横に振る。"





li "試験で疲れているだけです。大丈夫ですから"




"それが理由だとは思えない。もう少しでそう言いかけるけど、やめておく。リリーが言いたくないのにそれを引き出そうとしても意味がない。こんなに不機嫌な時ならなおさらだ。"



hi "それならいいんだけど。じゃあ、また"

hide lilly
with charaexit



"自分の教室に向かうために廊下を折り返そうとすると、背後からリリーの柔らかい声がする。"



show lilly cane_concerned
with charaenter


li "久夫さん、あの……"


hi "ん？"


li "……"


li "ごめんなさい"

hide lilly
with charaexit





"そう言い残して、リリーは金属の手すりに手をはわせながら、足早に廊下の先にある自分の教室に向かっていく。"




"俺はその場に立ち尽くして、リリーが教室に入って視界から消えてしまうまで彼女を見送る。それから後ろ髪を引かれる思いで自分の教室に向かう。"


scene bg school_scienceroom at left
with locationchange

play music music_normal fadein 4.0




"いつも通り、まだ早い。何人かの生徒が固まってしゃべっているのを尻目に、武藤先生は今日一日に備えて机の上のファイルや紙をいじっている。"







"さっきのリリーに対する感情がまだ収まらない。収まるわけがない。だけどそれとは別に、彼女が俺の試験の出来について口にしたことで、俺も自分のとるべき進路について改めて考えさせられた。"




"そのことを考えるうちに、俺は職業として何らかの形で科学を探求していきたいと率直に思っていることを自覚する。その進路が一番簡単そうだからという理由じゃない。"




"だけど、俺は今までこの分野のどういう方向に進みたいのかよく分かっていなかった。『科学』だけじゃ仕事のカテゴリーが広すぎる。"




"リリーのさっきの言葉のおかげで、俺の考えも絞れてきた。以前からぼんやりとは思っていたけど、俺はその特定の進路に進むことをあまり真剣に考えてこなかったんだ。"


show bg school_scienceroom at right
with charamove



"武藤先生の机に歩み寄る。先生は授業の準備に夢中で俺が近寄っていることに気づかない。いつものことだ。"



hi "おはようございます"

show muto normal at center
with charaenter



"武藤先生は少し驚いたように顔を上げて、すぐにまたいつものぎこちない笑顔に戻る。"


show muto smile
with charachange


mu "おはよう、中井。どうした？"



hi "１つ質問してもいいですか？"




"俺にちゃんと向かい合うために、武藤先生は持っていた紙の束を置いて、少し苦労しながら立ち上がる。そして机の上に無造作に積まれた本を見下ろす。"



mu "なんせ私はそのためにここにいるんだ。何でも聞いてくれ"


hi "ちょっと思ったんですけど……武藤先生にとって、人にものを教える動機って何ですか？"


"俺に答える前に、武藤先生がしばらく考え込む。明らかに予想外の質問だったみたいだ。"

show muto normal
with charachange


mu "１０人の違う先生に同じ質問をしたら、たぶん１０の違う答えが返ってくるだろうな"




mu "自分自身の意見でしかないが、私が教えている理由は……ううむ……"



"武藤先生がまた深く考え込んで、どうやったら言いたいことが伝わるかを注意深く探っている。"

show muto smile
with charachange



mu "こう考えてみてくれ。中井が小さかったとき、水路とか水たまりのような流れる水の中で、棒切れや石を使って遊んだことがあるだろう？"




hi "ええ。子供の時にそうやって遊んだ人は多いと思います"



show muto normal
with charachange


mu "まあ、子供でなくともやる人はいくらかいるだろう。その遊びは別の形を取るだろうが。だけど私が言いたいのは、そういう遊びをやることで水の流れやその変化に対する好奇心が湧いてくるということだ"



mu "どんな人でも、小さな子供でさえも、自分を取り巻く世界の仕組みに大きな驚きと好奇心を抱いているんだ。その仕組みがどんなに小さなものであっても"




mu "私は今でも宇宙に対して、その驚きと好奇心を感じるんだ。新発見や古典的な実験のことを読むだけでも、遠い星から小さな水たまりに至るまで、森羅万象の素晴らしさに対する畏敬の念を新たにする"



show muto smile
with charachange



mu "私はただ、私の感じている驚きをどんなに少しでもいいから他の人々に伝えたいんだ。もしそれができるなら、それがたった１人に対してであっても、私は教師であることに喜びを感じると思う"



"自分の言ったことを思い返しているのか、武藤先生が頭をかく。"





"武藤先生のことが以前よりもっと理解できた気がする。たとえ周りの人間に対して不器用であっても、先生は彼らへの真剣な希望を持っていて、価値があると信じる自分の思いを彼らに提供しているんだ。"



"リリーが昨日俺に言った言葉が頭の中で鳴り響く。『久夫さんは他の人とうまくやっていると思います』か。リリーはいつも、俺が普通以上に好奇心旺盛だと言ってたな……"

show muto normal
with charachange


mu "話がそれてしまったのなら済まない。質問の答えになったか？"


hi "よく分かりました。ありがとうございます"



hi "実は、もう１つ質問があるんです"



mu "ほう？　それは何だ？"


hi "えっと……大学のパンフレットか案内はありますか？　そろそろ出願の準備を始める時期なので"



"武藤先生はうなずくと、机の中を覗き込むために腰をかがめる。その時、先生が心の底から笑っているのに気づく。先生が人前でこんな自然な態度を取るのは、俺も今まで見たことがない気がする。"




"たぶんそれは、教師としての武藤先生じゃなくて、１人の人間としての武藤先生なんだろう。"


show muto smile
with charachange


mu "これだ。他にもっと必要なら、遠慮なく言ってくれ"


"武藤先生が色やサイズの違うパンフレットと小冊子を６、７冊俺に手渡し、俺はそれを喜んで受け取る。"



"そう、これこそが俺自身の将来を創り出すために必要な情報なんだ。これまで時を過ごし、いろんなチャレンジをしてきて、今ついに自分のこれからの人生の全体像が見え始めてきたんだと思う。"





"俺の体はこの通りかもしれないけど、精神の方は今でも全く健全なんだ。"



hi "ありがとうございます"

stop music fadeout 2.0

scene black
with dissolve

$ suppress_window_after_timeskip = True



label jp_L26:

window hide None

scene black
with dissolve

nvl clear
nvl show dissolve


n "\n\n『変だ』"

play music music_pearly fadein 5.0

$ ksgallery_unlock("evul hisao_teacup")
show ev hisao_teacup:
    truecenter
    alpha 0.0 subpixel True
    linear 30.0 alpha 0.5
with None


n "\n\nここでの生活が始まって以来、この単純な思いが数えきれないくらい何度も俺の心を捕え続けてきた。"



n "それは、面倒な疑問を隅に追いやる簡単な方法に思える。まるで、その２文字のレッテルを貼ってしまえば俺の前から消えうせるか、さもなければそれ以上考える必要がなくなるかのように。"




n "発作が起こる前の生活を思い出そうとするたびに、それがぼやけていくみたいに感じる。だけど俺の心は、あれ以来突然俺の身に起こった全てのことに付いていこうと必死になっている。"




n "それは、現地の言葉をほとんど知らないような国に取り残された時の気持ちに似ている、とどこかで聞いた。"


n "考えてみると、確かに俺の身に起きたことはその例えにぴったりと当てはまるような気がする。"

nvl clear



n "\n\nだけどそんな状況下では、現地の言葉もすぐ身に付けることができるだろう。そうしなきゃ生きていけないんだ。言い換えれば、『おぼれるか泳ぐか』という二者択一の状況になる。"



n "\nここで時を過ごしてきた俺は、ちゃんと泳げているんだろうか。"




n "試験はついに終わりを迎えるけど、俺にとっては大きなストレスだった。だけど今もまだ武藤先生には気に入られているし、将来の進路もなんとなく見えてきている。"




n "なのに俺は、この馬鹿げた意味のないひと言をずっと使い続けている。"


n "\n\n『変だ』"

nvl clear



n "\n\n時にはひどくぞっとするような障害や症状を持つ人々に囲まれた環境にも、あっという間に慣れてしまうというのは本当に驚きだ。"




n "それなのに、こんなにも自分がよそ者みたいな気がしてしまうのはなぜだろう。"




n "\n社交性がないとか友人がいないってわけじゃない。ほとんどのクラスメイトとはとても仲良くなったし、他にも校内に何人か知り合いがいる。腕や脚がなくたって、ここの生徒は同世代の他の少年少女と何も変わらない。"





n "\n\n一度は迷ってしまい、絶対に覚えられないと思った学校の廊下も、理にかなった建物のレイアウトのおかげで今では簡単に移動できる。先生たちとは気さくな議論を交わすことができる。"


nvl clear
nvl hide dissolve

scene ev hisao_teacup:
    truecenter
    zoom 1.0 subpixel True alpha 1.0
    acdc_warp 20.0 zoom 0.8
with locationchange

window show


"俺がカップの中の紅茶を優しく揺らすと、中で動く液体に映る俺の顔がゆがみだす。"


"変だ……紅茶は嫌いだったのに。"


hi "きっと、考えすぎなんだ"

play sound sfx_teacup



"ティーカップがその下のソーサーに触れる、聞き慣れた陶器の音が聞こえてくる。"




li "どうしたんです？"


hi "いや、何でもない"

scene bg school_dormlilly
show hanagown normal:
    tworight
    ypos 1.15
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
with whiteout


"俺はそばにいる２人がそうするように、目の前の紅茶を長いあいだすする。"


"リリーの部屋で彼女や華子と一緒に紅茶をすすりながら過ごす、それだけの時間。親しみがあって、ノスタルジーさえ感じる。"


hi "それで、華子。新聞部の活動はどう？"

show lilly basic_satisfied_paj
with charachange


li "私も知りたいですよ。とても面白そうね"

show hanagown distant
with charachange



"俺とリリーの注目を浴びて華子がうつむく。だけどそれに反して、華子の笑顔からは、自分が俺たちの話題の中心になっていることへの素直な喜びがうかがえる。"



ha "うん……楽しい。だんだん慣れてきたと思う"



ha "直美さんと、直美さんのお友達がほとんどの仕事をやってる……記事を書いたりとか"


show hanagown smile
with charachange



ha "私はパソコン作業だけやってる。記事をまとめたりとか、印刷したりとか。た、楽しいよ。座って集中できるから"



"リリーの機械オンチは華子には当てはまらないみたいだ。部屋の中で座って他人の新聞記事を資料にまとめるなんて、そんなに外向的だとは思わないけど、それでも華子が交友関係を広げているのを見て胸が熱くなる。"





"ほんの小さな一歩、かもしれないな。華子にリリーのような社交的な人間性を求めるのはちょっと酷な話だろう。"


show lilly basic_oops_paj
with charachange



li "直美さんとはどう？　時々問題を起こす人だと聞いているけれど"




"そしてリリーが華子に対して保護者モードに入ってしまう。リリーも、華子を独り立ちさせることを考えてこなきゃいけなかったな。"


show hanagown worry
with charachange


"華子が頬をかきながら返事を考える。"

show hanagown smile
with charachange



ha "直美さんは……いい人だよ。たまにちょっと大声を出したり、一緒にいて疲れたりするけど……でもすごく助けてくれるし。直美さんのお友達もみんないい人"


show lilly basic_cheerful_paj
with charachange


li "それを聞けてよかったわ、華ちゃん。華ちゃんがそんな楽しみを見つけて、私も嬉しいですよ"



"リリーの笑顔は暖かな、心からのものだけど、そこにある種のもの寂しさも見え隠れする。華子はそれに全く気づいていないみたいだけど、俺には気のせいだとは全く思えない。"




"たぶん、俺がだんだんもっと自分の身の回りの出来事を意識するようになってきたからだろう。次々といろいろなことが起こっている中で、できるだけ注意していないとなにかを見過ごしてしまいそうな気がする。"





"試験、新たな恋愛生活、大学入試のための勉強努力、それから、腹が立つほど不規則にやって来ては俺の全てを台無しにしてしまう心臓の障害。最近俺の頭はパンクしそうになっている。"



"そんな感じだから、こういう稀有な静寂の時間は俺にとってありがたい。"



"人に囲まれるのを好むにもかかわらず、リリーが週ごとのコンビニ散歩や華子とのお茶会を楽しむようになったのも同じ理由だろう。それが混沌とした多忙な日々の中で、リリーに一時の平穏をもたらしていたんだ。"




hi "試験が終わってやれやれだな"

show lilly basic_giggle_paj
with charachange




"その言葉を聞いて、２人とも本心からくすくす笑う。試験の終わった先週から、誰もがひときわ幸福感にあふれているみたいだ。"






hi "それで華子、夏休みはどうするんだ？　あとたったの……"



"俺は頭の中で素早く日を数える。今日は月曜、学校は土曜日で終わるから……"



hi "……５日で始まるぞ"


show hanagown normal
with charachange


ha "旅行をしようかって……思って。ちょっと……だけ"

show hanagown smile
with charachange



ha "行きたい所がたくさんあるし……バスや電車のお金も足りると思うから。直美さんと新聞部の他の女の子も１人、いっしょに行くかもって"





"その様子から、華子が綿密に旅行のことを計画しているのがうかがえる。華子がこんなことを考えているなんて、ちょっと驚きだ。"



"どうやら華子は本気で前に進み出そうと決意したらしい。"

show lilly basic_smile_paj
with charachange



li "どこか行こうと思っている所はあるの？"


show hanagown distant_blush
with charachange


ha "京都がいい……かな、って。た、たぶん、他にも何ヶ所か行くと思う……けど"

show lilly basic_cheerful_paj
with charachange


"華子の旅行計画に満足して、リリーが同意するようにうなずく。"



"俺はリリーに目を向けるけど、同じ質問を彼女にするのは控える。リリーは自分自身の将来についての話をずっと避け続けている。でも俺からその話題を単独で持ち出すいいタイミングがまるでなかった。"





"会話の中でそのことが話題に上るたびに、リリー自身も確信がないか、あるいはその質問をはぐらかしているだけみたいに感じる。心配になってくる。"



hi "旅行中もたまに連絡するの忘れないでくれよ。俺の番号はもう教えたよな？"

show hanagown smile
with charachange



"華子が嬉しそうに笑いながら、素早くうなずく。"




"不思議なことに、目指すべきゴールを持った人はとても幸せに見える。優子さんも大学への志という話題になるといつも嬉しそうだし、今の華子も全く同じだ。"




"じゃあ、なんで俺はまだこんなに不安なんだ？　それにリリーまでも？"




"人間関係ってのは本当に時にイライラするほど面倒だな。"

show hanagown worry
with charachange


ha "あっ、えっと……い、今何時ですか？"


hi "ん？　ああ……"



"リリーの時計は目で見える情報は何も与えてくれない、と思い出すのに少し時間がかかる。何度もこの部屋に来ているんだから、いい加減覚えるべきだ。"





"とにかく、かばんから腕時計を取り出して素早く時間をチェックすると、華子が時間を聞いた理由もはっきりする。"



hi "１０時２０分くらい。もうすぐ門限だな"


show hanagown normal:
    ypos 1.0
with dissolvecharamove


"華子が立ち上がってほこりを払い、それから羽織っているガウンを整える。"

show hanagown smile
with charachange


ha "じゃあ……戻った方がいいかな。おやすみなさい、リリー、久夫くん"


stop music fadeout 5.0

show lilly basic_smileclosed_paj
with charachange



li "おやすみなさい、華ちゃん"



hi "また明日な"

hide hanagown
with dissolve



"そうして、華子はドアに向かって歩いていき、静かに部屋を出て行く。"


show lilly basic_smileclosed_paj:
    xpos 0.5
show bg school_dormlilly at bgright
with charamove


"……"


"静寂。"


"最近、リリーと俺のあいだにこういう間がよく起きるようになった気がする。数秒後、俺はようやく話題を見つける。"

play music music_another fadein 4.0


hi "ああそうだ。金曜日、武藤先生と話をしたんだ。ついに大学の情報と出願方法を調べたよ"

show lilly basic_smile_paj
with charachange



li "それはよかったです。大学に出願するということは、久夫さんも将来の進路について何か考えがあるんですね？"



hi "科学の教師になろうと思ってるんだ。大学に進学して教員の免許を取るのは時間がかかるだろうけど、その価値はあると思う"


show lilly basic_satisfied_paj
with charachange



"それを聞いて、リリーの顔がぱっと明るくなる。たぶん、自分も教師になりたいリリーにとって、俺が同じような進路に進むことが嬉しかったんだろう。"




li "では、教師になる道を選んだんですね……"


show lilly basic_smile_paj
with charachange



li "あなたにとってとてもふさわしい進路だと思いますよ、久夫さん"




"俺は笑顔でうなずく。俺のしぐさを見られなくても、リリーはそれを感じてくれている。今の俺にはそれが分かるんだ。"


show lilly basic_planned_paj
with charachange


li "武藤先生もそれを聞いて喜んだでしょうね？"



hi "そうとも言えるかもな"



hi "なあ、リリー？"

show lilly basic_smile_paj
with charachange


li "はい？"


hi "リリーが教師になりたいってのは知ってる。でも……"



"一瞬、頭に浮かんだ問いを本当にリリーにぶつけるべきか考える。でももう後の祭りだと気づいて、そんな懸念もすぐに吹っ飛んでしまう。"


show lilly basic_smileclosed_paj
with charachange



li "まさか久夫さん、私が目のことを言われたら気を悪くするなんて、まだ思っていたりはしませんよね"





"問い詰めるような口調に反して、リリーはこんな話題を持ち出しておどおどする俺を面白がって笑っている。こんなやり取りはいつも変わらないな。"






hi "まあ、そうかもな"




hi "俺はただ、リリーの教師になりたいっていう志とか、そういうものに対して、目が見えないことが妨げになるのかならないのか、って考えてたんだ"




show lilly basic_surprised_paj
with charachange



"リリーは少し驚いたような表情になって、それから考え込む。リリーがこの問題を今まで一度も考えたことがないとは到底思えない。"


show lilly basic_emb_paj
with charachange



li "そうですね……久夫さん、しばらく目を閉じてもらえますか？"



hi "いい……けど？"


"俺は眉を上げながら、リリーの言ったとおりにする。"



$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene black
with shuteye


"リリーが何を考えているのか、俺にはさっぱりわからない。片目で彼女を覗き見て、疑問はますます膨らむ。"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show bg school_dormlilly at bgright
show lilly basic_smileclosed_paj_close at center
with openeye



"リリーは、いつも髪を結んでいる黒いリボンをベッドのそばの衣装棚から取り出し、指をはわせて絡みついている髪の毛を取りながら、俺に近寄ってくる。"



$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene black
with softwipedown



"その黒い布切れが俺の顔に触れ、頭をぐるりとめぐって目の上に覆いかぶさった時、突然リリーが意図していることに思い至る。"



hi "ええと……これはどういうこと？"


li "ちょっとしたテストですよ、久夫さん。知りたがっているようだから、しばらく私と同じようにものを見てもらいます"


"はあ、つまり、そういうことか。"


"正直言うと、これは結構面白そうだ。傍から見たら子供っぽくてバカらしくさえ思えるだろうけど、別に誰も傷つかないちょっとしたバカ遊びだ。"



"俺はよいしょと立ち上がる。障害物がないか注意するために、すぐに両手を前に伸ばす。"




hi "いいよ。で、どうするの？"


li "では、私に触れてください"


hi "リリーがそう言うなら。それじゃ……"


"俺はゆっくりと前方に歩き出す。リリーの声がする方向だ。"




"歩く速さはすり足とさえ言えないだろう。今のこの経験すべてが俺にとっては異質に感じる。テーブルや無計画に積まれた本の山にうっかりつまずく危険を冒したくない。"




play sound sfx_rustling


"なにか柔らかい、それでいてしっかりしたものが俺の左足をかすめる。よく調べてみると、それはリリーのベッドだ。"



"俺は前に進んで、リリーの部屋がきちんと整理されていることのありがたさを身をもって知る。リリーが積んだ本の山もだいたいは壁際にあって、俺の行く手を阻んだりはしない。"


play sound sfx_pillow



"伸ばした手の先に固い壁を感じて、いらだった俺は眉間にしわを寄せる。"



hi "おい、リリー。どこにいるんだ？"


li "そんな所で何をしているんですか？　私はここですよ"



"部屋の反対側からリリーの声がする。さっきの場所からまるっきり離れていることは、未熟な俺の耳でも分かる。もし俺から逃れるためにそっち側に行ったのなら、これはリリーにとってただのゲームなのか？"





"……そりゃそうに決まってる。見るという概念さえもあいまいな人生に比べたら、数分間の目隠しなんて全くなんでもない。"



"リリーはこう言いたかったんだろう。彼女は部屋を自由自在に使いこなせる。それだけじゃなくて、俺には山久のどの生徒と比べても彼女がいかに独り立ちしているかということが分かった。"


"ふむ、もしこれがただのゲームであっても、やるからには真剣勝負だ。"



"俺はさっきよりもはるかに速いスピードでリリーの声のする方向に近寄る。部屋の真ん中にあるテーブルの位置を覚えているおかげで、俺はそれを手際よく避ける。"


hi "捕まえたぞ！"



"リリーがお茶目にくすくすと笑う。ちょうどリリーが俺のそばをすり抜けていることがわかる程度の短い笑い声だ。"



play sound sfx_impact2
with vpunch



"俺は素早く振り返ってそっちを向こうと――さっきはこんな所にテーブルなかったぞ！"



hi "いって……て……て……"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show bg school_dormlilly
with softwipeup


"俺はゆっくり起き上がってテーブルの横に座り、ズキズキする頭をさすりながら目隠しを上にずらす。"

play sound sfx_impact
with vpunch



"倒れた自分のすぐ目の前にあるテーブルにいらついて蹴りをお見舞いする。全く無意味な行動だけど、やらずにいられなかった。"



show lilly basic_oops_paj_close at center
with charaenter


li "久夫さん？"



"リリーは今も俺のすぐそばに立っている。俺の身に何が降りかかったのか、よく分かっていないのは明らかだ。"




hi "ごめん。ちょっとつまずいて"


show lilly basic_concerned_paj_close
with charachange


li "痛みますか？"


hi "頭が痛いけど、大丈夫だと思う。テーブルの奴が俺をひっくり返すために動いたんじゃないかな"

show lilly basic_giggle_paj_close:
    ypos 1.1
with dissolvecharamove



"リリーが歩み寄って俺のそばに座りながらくすくすと笑う。俺の手の上に彼女の手が重なる。"


show lilly basic_weaksmile_paj_close
with charachange



li "では、これでおしまいにしましょうか？"



hi "そうだな"



hi "だけど、言いたいことは分かったと思うよ。こんな痛い目にあわずに済めば良かったんだけど"


show lilly basic_surprised_paj_close
with charachange


"リリーが突然ぽかんとした表情をする。"



li "言いたいこと？"



"そして、俺は極端な無表情を返す。"


hi "ただのお遊びだったの？"

show lilly basic_reminisce_paj_close
with charachange



li "私はただ、こうすれば久夫さんがこの話をもう少し気楽に考えてくれるかもと思っただけです。だって、いつも腫れ物に触れるような様子だから"


show lilly basic_smileclosed_paj_close
with charachange



li "教えることに関して言えば、視覚はそれほど重要じゃないんです。全盲の教師が教えているクラスだってたくさんあるし、学ぶための資料も十二分にあります"


show lilly basic_smile_paj_close
with charachange



li "本当に、単純なことなんですよ"




"俺は肩を落とすと、鼻を鳴らして苦笑する。"




hi "ああ、分かったよ。じゃあ、俺たち２人ともそれぞれのゴールに向かってがんばらなきゃいけないな"


stop music fadeout 4.0

show lilly basic_cheerful_paj_close
with charachange



li "うーん……"



hi "どうした？"


"少しためらいながら、リリーがあごを突き出して目を閉じ、誤解しようのないしぐさを見せる。"

scene ev lilly_kissing
with whiteout

play music music_one fadein 1.0



"俺は喜んでそれを受け入れ、２人の唇が触れる。そうしている間、突然リリーの手が俺のシャツの下に滑り込み、胸をはい上がってくるのを感じる。素肌に触れるリリーの手の感触だけで、俺の心臓は急加速する。"




"これって、リリーはまたその気になってるのか？"



"まあ、俺に文句のあるはずもない。リリーは純粋にそういうことが好きなんだし、たくさんの薬を飲んでいてさえ、ありがたいことに俺のリビドーはまだ健在だ。"




"俺はより深くリリーに口づけをし、俺の胸の輪郭をなぞるリリーの手を感じながら、その手を固く握りしめる。"

scene bg school_dormlilly
show lilly basic_smileclosed_paj_close:
    center
    ypos 1.1
with whiteout


"そして俺たちは体を離す。部屋の中は俺たちの息づかいの他には何も聞こえない。"

show lilly basic_surprised_paj_close
with charachange


li "ねえ、久夫さん？"


hi "ん？"

show lilly basic_emb_paj_close
with charachange


li "もう一度……目隠しをしてくれたりはしませんよね？"


"そのためらいがちな提案を聞いて、俺は驚く。"



"リリーのセックス中の視界まで俺に体験させたいのか。それとも、目隠しに邪魔されている俺の行為中の様子を知りたがっているんだろうか。"


$ renpy.music.set_volume(0.5, 0.0, channel="music")


scene black
with softwipedown


"一抹の不安も好奇心には勝てず、俺はリリーの言うとおりに目隠しを降ろして目を覆う。再び世界が暗闇に包まれる。"



"リリーの手が俺の顔の側面を優しく撫でるのを感じて、それを全く予測できない俺はビクッと体をこわばらせる。"



"本当に、俺はこういう触れ合いにもっと慣れなきゃだめなんだ。付き合いだして何週間もたつのに、リリーと違って、俺はそれを自然なことと思えない。"



"……沈黙？"


hi "なあ、リリー……"



li "しーっ"



"俺は素直にリリーの指示に従って、静かに聞き耳を立てる。今何かが、何が、俺の周りで起こっているのか、それを知るために。"



"今は部屋の中の障害物に気を付けながら移動する必要もない。そのおかげで、さっきリリーを追いかけていた時に比べてはるかに聞くことに時間と集中力を向けられる。"




"しばらくかかったけど、俺はついにリリーのかすかな息づかいを、それを除けば静まり返った部屋にとらえる。"




"すう……はあ……すう……はあ……"



"自分の呼吸と聞き比べてみて、普段のリリーらしくないくらい、明らかに息づかいが荒くなっていることに気づく。"




"何か他の音も聞こえてくる。それが何の音なのかすぐには分からない。こんな音は聞いたことないと思うけど……"



"その音の出所に気づいて俺の胸は激しく高鳴り、思わずそこに向かって手を伸ばしてしまう。手が触れると、リリーの顔はいつもより柔らかく感じる。頬に触れた指に反応して、彼女がかすかにその向きに頭を回す。"




li "久夫さん……"



"俺はごくりと息をのんで、しばらく自分を落ち着ける。俺の今の状態では、周りの状況をちゃんと把握するには全意識を集中させないといけない。"




"何度か深呼吸をして、どうにか落ち着いた気がする。羽も動かさないような繊細なタッチで、俺は手をリリーの体の下方へと動かし始める。"





"……そして、自分がまた我を失っていくのがわかる。リリーの丸みを帯びた体に、薄いシルクのパジャマが完璧にフィットしているせいだ。"




"今の姿勢からすると、リリーはベッドにもたれかかって座り、俺の方を向いているはずだ。さあ、続けよう。"





"……よし、これは腰だな。ここから下にゆっくり移動すれば……"




label jp_L26h:



"俺の手がリリーの手に重なり、彼女がはっと息をのむ。俺はためらいがちに両足の間にある彼女の指をたどるけど、その先は下着の中に隠れてしまっている。"





"ほんのかすかな湿り気が指先に触れるけど、それだけでもリリーの行為を知るには十分だ。"




"突然、今俺の目の前でリリーがどんな格好をしているのか、その光景で頭の中がいっぱいになる。リリーがそんなことをするなんて今まで想像したこともなかった。それを見られないことが余計に俺を高ぶらせる。"



$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_dormlilly
with softwipeup



"俺は目隠しを上げて、リボンに引っかかっていた数本の髪の毛を目から払いのける。"




"どれくらいの時間なのか、しばらく俺の心が完全に空っぽになる。自由になった俺の目は眼前の光景に釘付けになり、それを凝視することしかできない。"


scene evh lilly_masturbate:
    truecenter
    subpixel True zoom 1.1
    acdc_warp 10.0 zoom 1.0
with flash



"想像していた通り、リリーは俺の前に座っている。"




"リリーは体を支えるように床に片手をついて、もう片方の手の指で紺色の下着に隠されている両足の根元を愛撫している。こんなにも官能的な光景を、俺は今まで見たことがない。"








"もう一度手を伸ばして、リリーの顔から髪を撫で上げる。リリーはあごを上げて、快感に包まれた体に新鮮な空気を満たす。"




hi "リリー……"



"名前を呼ぶ俺に微笑みかけるリリーが、おかしなくらいに可愛らしい。いつも思うけど、リリーが気を緩めきった瞬間こそが、彼女の一番興味深い感情が表に出てくる瞬間なんだ。"




"やがて、リリーが指を速く動かし始める。リリーの興奮が明らかに高まっていく。その場に満ちる彼女の汗の匂いがそれを裏付けている。"




"俺はリリーの前に座る。自分自身の興奮を抑えられない。リリーを押し倒したいという激しい衝動にかられながらも、なんとかリリーが自分でするがままにさせる。"



scene evh lilly_masturbate_come_face
with flash



"変だ……俺は最初、リリーの青く曇った目が落ち着かないと思っていた。どこにも焦点の合わない視線が不気味とさえ感じていた。今はそれがほとんど気にならない。"



"リリーがあえぎ声を漏らし、俺の注意がまた彼女に集中する。リリーの息づかいはさっきよりもどんどん激しさを増して、彼女の下半身が微妙に揺れ動く。"


scene evh lilly_masturbate_come
with flash



"激しい息づかいから、リリーがその間際まで来ていることがすぐにわかる。その目が固く閉じられて、全身の筋肉が収縮する。まぎれもなくリリーは絶頂を迎える。"




"数秒にも満たない間、リリーが固くこわばり、恍惚感に体を丸める。そして全身の力を緩めて、疲れ切ったような深いため息を唇から漏らす。"


scene bg school_dormlilly
with locationchange


"俺は……何を言えばいいのか分からない。リリーをただ見つめているあいだ、沈黙がその場を支配する。脱力して座り込むリリーの顔には髪が覆いかぶさっている。"

show lilly basic_emb_paj_close:
    center
    ypos 1.1
with charaenter


li "久夫さん……"


"リリーが俺の顔をなでようと俺に手を伸ばすその時、激しい衝動が俺の全てを支配する。俺はほとんど何も考えずに、リリーの体の上にのしかかる。"



"こんなのは、まともな精神状態じゃない。奇妙な力強さを感じながら、無表情なリリーの上で自分の体を支える。まるで、ずっと前に起きた発作以来初めて、自分の肉体が強くなったかのような気分だ。"




hi "リリーが……欲しい"

show lilly basic_weaksmile_paj_close
with charachange



"リリーが弱々しく笑って手を上に伸ばし、俺の顔の側面をさするので、俺は驚いてしまう。それはまるで物欲しさの表れだ。いつもならこんなしぐさは、俺から何かを得た後にしかすることはない。"



hi "リリー……してほしいの？"

show lilly basic_smileclosed_paj_close
with charachange



"リリーが微笑んだまま静かにうなずく。一度くらい、俺にリードを取らせるには効果的な方法だったのかもしれないな。"



$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene black
with softwipedown



"そして、再び驚くべきことに、リリーが俺の頭にかかったままのリボンをぐいっと下げる。俺はまたしても暗闇にとらわれる。"




li "言ったでしょう……そのままでって……ね？"




"そのからかうような、息づかいで途切れがちのリリーの声……こんな時でも、主導権を握る余裕を失うことはないんだな。"



"だけど、今回は……この時だけは……"



li "きゃっ、久夫さん！？　何を――？"




"リリーの体の下に手を回す。苦労しながらその体を優しく持ち上げると、柔らかなシルクと肌の感触が手に伝わってくる。"




"リリーが重いとは言わないけど……その長身のおかげで、持ち上げるのはかなり厄介だ。"




"注意深く数歩進むだけで、すぐに俺の脚がリリーのベッドの角に当たるのを感じる。俺は持ち上げた時と同じくらい優しく、リリーをシーツの上に降ろす。"



"さっきのゲームが役に立った。あれがなかったら、リリーのベッドまでの歩数と、それがどの方向にあるのかが分からなかったはずだ。"



hi "ベッドの方が、床の上よりも快適だろ？"



li "いつだって紳士的なんですね"



"俺はリリーのすらりとした長い脚へ自分の手を素早く滑らせる。その魅力は視覚で味わわなくても決して失われることはない。そしてリリーのパジャマのショートパンツと下着を足首から引き抜く。"





"それがどこに行ったのかはまったく分からないけど……"



"まあ、どうでもいいか。その辺にあるさ。"



"俺はパジャマのズボンと下着をたいした苦労もなく脱ぎ捨て、リリーの両脚の間に自分の身を置く。いや、少なくとも俺がリリーの両脚の間だと思う位置に。"



"ベッドの上に片手を突いて自分の体を支えながら、俺はゆっくりと右手を下に降ろす。"


"あっ、しまった。最初の接触で、俺の手の平が不器用にリリーの鼻先に当たる。"



"リリーが少し笑いながら顔を横に向ける。俺はカンを頼りに手で優しく彼女の頬を包み込むと、リリーが普段よく俺にやるみたいに、親指で顔の輪郭を感じ取る。"





"リリーが俺の手の中でじっとしてくれていたら、もっと簡単なんだ。だけど、リリーが俺の手に鼻をすり付けている、そんな感覚も悪くない。"





"俺は自分を落ち着かせるために唾を飲み込むと、ベッドから手を離して、その手でリリーの中に自分自身を導く。"






"俺がリリーのぬくもりを感じると同時に、自分がとてつもなく興奮していることに気づく。"




"視界がさえぎられた今、俺は触覚を含む他の感覚にものすごく集中することができる。この一連の経験は、これまでにないくらい鮮やかで強烈な感じがする。"




"俺はゆっくりと腰を前後に動かし始める。興奮のせいで心臓が激しく脈打つ。"




"固く閉じられたリリーの目を感じ取る。俺の親指の下にある彼女の頬の動きで、リリーの顔の側面を優しく包み込んでいることを思い出す。"




"完全に圧倒されてしまいそうになる。俺が一番大切にしている感覚以外のすべての感覚を通して経験する、こんなセックスがリリーにとっての普通だなんて、思いもよらないことだ。"





"頬から首へ、俺はリリーの体を感じ取るために手を下の方へと滑らせ始める。"




"リリーの鎖骨の輪郭……肌の上に浮かぶ小さな露……"





"リリーと俺の汗の臭いが空気に交じり、嗅覚を刺激する。俺の部屋のものとは明らかに違う周りの匂いさえも、俺の感情を高ぶらせる。"









"リリーのしなやかな胸へと手を動かすと、柔らかいあえぎ声が俺たちの行為が立てる音と一緒になって俺の耳を満たす。"




"俺の手の下の肌が俺の動きに合わせて前後する。目の前にいるリリーの肌もあらわな肢体への興奮が高まるにつれて、俺の手にもどんどん力がこもっていく。"



"手の平に当たるリリーの小さな乳首さえ感じ取れる。俺はさらに手を滑らせて、薄いシルクのパジャマ越しにそれをつまむ。"




"俺と同じ喜びに満たされて、リリーの上ずった声があえぎ声に変わる。俺の心臓が激しく脈打っているのが分かる。俺の手の下にある、リリーの心臓の鼓動も伝わってくる。"




"リリーが俺の手首をぎゅっとつかむ。快楽に飲み込まれて胸を跳ね上げながら、びっくりするほどきつくそれを握りしめる。"


label jp_L26x:

scene black
with dissolve


"もっと……もっとしたい……"

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show



"俺たち２人とも我を忘れて、死にもの狂いで体を前後させているその時、自分の胸が締め付けられるのを感じる。"



$ renpy.music.set_volume(0.4, 0.5, channel="music")

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show



"たいした……ことじゃない……ただ深呼吸をして、気を……落ち着かせれば……"


$ renpy.music.set_volume(0.3, 0.5, channel="music")

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

with Pause(0.7)

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show



"こんなの……いつもと同じだ……"


$ renpy.music.set_volume(0.2, 0.5, channel="music")

window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

with Pause(0.7)

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show


hi "ああ……うああああああああ……"

window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

with Pause(0.7)

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show


"違う……抑えられない……この痛みはひどすぎる……！"

window hide

play sound sfx_heartstop
show heartattack alpha
with Dissolve (0.1)

stop music fadeout 0.3

show heartattack residual
with Dissolve (0.8)

window show


hi "ぐあああああ！"

with vpunch



"俺はみっともなく焦りながらリリーから後ずさりすると、足の後ろを不器用にテーブルにぶつけて突然床の上に倒れ込む。"




"激しく呼吸しながら、仰向けになって死にもの狂いで目を覆うリボンをかきむしる。これを取らないと、今すぐ取らないと……"


scene white
with softwipeup

scene bg misc_ceiling
show heartattack residual
with locationchange



"一瞬、全てが空っぽになる。新たに見える光が俺の目になだれ込んでくるにつれて、過呼吸寸前だった俺の息もゆっくりになる。"



window hide

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_tragic fadein 4.0

hide heartattack
with Dissolve(3.0)

window show



"時間が過ぎていき、俺はありったけの集中力を使って、注意深く心拍のリズムを確認する。"




"心臓は……大丈夫だ。普段の動きに戻っている。"




"天井を見上げて床にぼーっと寝そべる俺の体は、奇怪そのものだ。さっきからのアドレナリンは今でも体中を駈けめぐっているのに、精神の方は完全に疲れ切ってしまっている。"





"リリーがベッドから降りてこちらに近づくのを聞きながら、俺は自分の体を持ち上げる。"


show bg misc_ceiling_blur as bg2:
    center
    alpha 0.0
    linear 1.0 alpha 1.0
show lilly superclose_shock:
    xalign 0.5 yanchor 0.5 ypos 0.15 alpha 0.0
    subpixel True rotate 180
    easein 1.0 alpha 1.0 ypos 0.3
with Pause(1.0)


li "久夫さん？　大丈夫？　久夫さん！？"


hi "大丈夫だ、リリー。大……丈夫"

show lilly superclose:
    xalign 0.5 yanchor 0.5 ypos 0.3 alpha 1.0
    subpixel True rotate 180
with charachange



"リリーが安堵のため息をついて、心配そうな表情をほころばせる。"




"その後に見せたリリーの表情、それは俺が絶対に見たくなかったものだった。もう何か月も前、俺が両親に初めて病院で会った時見るのが嫌でたまらなかった、あの表情。"



"同情。リリーが……俺に同情している。"

scene black
with shuteye


"俺はただ目を閉じて力なく顔を背ける。反吐が出そうだ。"

play sound sfx_rustling



"リリーがその場を離れて素早く身を整える音が聞こえる。リリーが着ていた衣類を、しばらくの探索の後、再び身につけていく音がかろうじて伝わってくる。"



hi "ごめん……"

scene bg school_dormlilly
show lilly basic_concerned_paj at center
with openeye


"リリーが上着のボタンをかけ終えながら首をゆっくりと横に振る。彼女のその優しい笑顔はとてもはかなげで繊細で、それが俺の気持ちを沈ませる。"

show lilly basic_concerned_paj_close
with characlose

show lilly basic_concerned_paj_close:
    ypos 1.1
with charamove





"リリーは俺に注意深く近寄り、ローテーブルの角の位置を感じ取ってから隣に座ると、俺の胸に腕を回す。"









li "ごめんなさい、久夫さん。あなたに欲望をぶつけるべきではなかったんです"


hi "謝ることはないよ。いつもは大丈夫なんだ。リリーも知ってるだろう"




hi "俺も無理しすぎたのがよくなかったな"




"まぶたが重く感じる。こうやってリリーの隣に落ち着いて座っていれば、たぶんアドレナリンが自然に抜けていって、気持ちをリラックスさせることができるだろう。"



show lilly basic_oops_paj_close
with charachange


li "だから……ずっと私に任せていたんですか……？"


hi "うん。リリーがそういうの好きでよかった、かな？"

show lilly basic_weaksmile_paj_close
with charachange



"その冗談でリリーの表情がほんの少し和らぐ。それを見て、頼りない自分自身に対する不安も軽くなる。"





"まばたきするたびに目を開けているのがつらくなってくる。俺の肩にリリーが頭を乗せる。もう完全にヘトヘトだ。"



li "大丈夫、久夫さん。何もかも大丈夫ですよ"

stop music fadeout 5.0



"そう言いながら、リリーが短く静かな曲を口ずさみ出す。何も考えられないほど疲れ切ってしまった俺は、その柔らかなハミングをじっと聴くことしかできない。"




"それは柔らかく、もの悲しいともいえる曲。聞いたことがある気がするのに、元の曲を思い出そうとすればするほど、集中力が失われていくように感じる。"





"俺の肩に優しくもたれかかるリリーの頭の感触、彼女の髪の匂い、俺に身を寄せる彼女の温かい体が心地よい。"
"その温もりが俺の体の緊張を緩めてくれるのと同じように、リリーの声が奏でる柔らかなハミングも、俺の心をリラックスさせてくれる。"





"このかけがえのない、静かな時間……あんな騒ぎを起こした後のこのひと時で、俺は自分がいかに疲れ切っているかを思い知らされる。まぶたが少しずつ、だんだんと重くなっていく。"





"さっきの大混乱を経験してなお、俺はこの時が永遠に続いてほしいと願う。"






"リリーと一緒に、かつて俺たちがそうしたように、ひとつひとつの出来事を共有して。"




"でも、もしそうなら……どうしてリリーが……以前よりもずっと遠くにいるような感じがするんだろう？"






scene black
with dissolve






label jp_L27:

scene bg school_library
with locationchange

play sound sfx_doorslam
play music music_happiness fadein 2.0




"本たちが返却口に投げ込まれる時にどさっと大きな音を立てて、図書室の沈黙が突然破られる。"




"少なくとも一週間に一度は図書室に顔を出すのが俺の習慣になっていた。それは読書自体のためだけじゃなく、華子やリリーと本について話したりするためでもある。"


show yuuko panic_up at center
with charaenter



"見るからに驚いた様子で、突然優子さんが音のした方へ振り向く。優子さんもここで働いてるんだから、今では本が投げ込まれることにも慣れてるだろうと思ったのに。"


show yuuko neutral_down
with charachange



yu "あっ、こんにちは、中井くん。また来たのね？"





"リリーが口ずさんでいた、聞き覚えのあるメロディーにまだ気を取られたままで、返事をするのにしばらく時間がかかる。それを聞きながら眠りに落ちて以来、あの旋律が数日間ずっと耳から離れていない。"




hi "えっ？　え、ええ。借りた本を返しに"


"優子さんが視線を落とす。たぶん本が投げ込まれた箱のほうへと。"

show yuuko closedhappy_down
with charachange


yu "中井くんって、ものすごい読書家よね？"


hi "もう今じゃ習慣になっちゃって。少なくとも時間は潰せますし"

show yuuko worried_up
with charachange


yu "わたしにも潰せるような自由な時間があればなあ……"


"ただのおしゃべりから意気消沈まで５秒もかからない。優子さんの新記録だろうな。今日の優子さんは普段と比べても全体的にちょっと落ち込んでるような気がする。"



"自活するために仕事を２つ掛け持ちしないといけないことを考えると、そのことがどれだけ優子さんの生活に負担をかけているかは想像がつく。"



"考えてみたら、ここでの仕事の給料はそんなに悪くないはずだ。こんな名門私立学校のスタッフが飢え苦しむなんて状況は、俺の直感にそぐわない。"



hi "２つの仕事を掛け持ちするなんて、大変でしょうね。俺にはできそうにないなあ"


show yuuko neutral_up
with charachange


yu "中井くんは学生でいられて幸運よ。大学には進学できそう？"



"進学のことを聞かれるということは、たぶんそれがこういう教育に望まれている結果なんだろう。ここみたいな私立学校に通うのだって安くはない。"




hi "たぶん……資金はあると思います"


hi "将来の計画があって、そのために大学に行かなきゃいけないんです。成績も十分だし。学費をどうやりくりするかの方が問題ですね"

show yuuko worried_down
with charachange



yu "大学の学費ってすごく高くて、私なんてそこに通うのに２つも仕事しなきゃいけないの……生活費だってバカにならないのよ"


show yuuko neutral_down
with charachange


yu "そんなにたくさん本を読んでるってことは、学校生活もうまくいってるってことよね？"



"面白い論理の飛躍だな。でも、全く的外れってわけでもない。"




hi "そう思います。どの試験もあまり難しくなかったし。１、２科目くらいは別としてですけど"



hi "優子さんが大学で何を専攻してるのか、聞いてもいいですか？"

show yuuko happy_up
with charachange


"その質問を聞いて、優子さんが心底喜んだ様子を見せる。"

show yuuko closedhappy_up
with charachange


yu "人類学よ。正確に言えば、古代アテネの文明と民主主義の歴史について学んでいるの"


"優子さん、本当に詳しそうだな。その情熱は尊敬に値する。優子さんが何かに対して純粋に興奮しているのを見られるのはいいことだ。"


"もし進むべき道筋が見えているなら、たとえ優子さんみたいな人であっても幸せでいられるんだろうな。"


hi "それを聞けて嬉しいですよ。もし優子さんが――{w=0.6}{nw}"

stop music fadeout 0.5
play sound sfx_phone

show yuuko panic_up
with vpunch



"突然俺のポケットから邪魔が入って、俺たちは２人とも飛び上がる。"


scene bg school_hallway3
with locationchange



"ペコペコと謝り、携帯を開きながら早足で廊下に向かうと、俺は携帯画面をちらりと見る。"




"……変だな。知らない番号だ。俺の携帯番号を知ってる人間なんて片手で数えられるほどしかいない。それを考えたら、この電話は俺の番号に運よく当たったテレアポか何かじゃないのか。"


scene bg school_hallway3_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)


hi "もしもし、中井久夫ですけど"


mystery "ったく、次はもっと早く出てくれよ。ところで、誰だと思う？"

play music music_comedy fadein 1.0


"はっきりとした低い、無愛想な声。俺はすぐにその声の主に気づく。"


hi "よう、ミーシャ。電話してくるなんて思わなかったぞ"


aki "はあ！？　あたしの声がミーシャに聞こえるってのか？"




hi "いいえ全然。でも晃さんに電話番号を教えた覚えがなかったから、ちょっとからかってやろうと思って"






aki "ああ、それ？　リリーから聞き出したのさ。簡単なこった"




"晃さんがたっぷりと誇らしげに言う。俺を自分のペースに引き込もうとしているのが見え見えだ。"




"だけど、リリーと晃さんの親密さを考えたら、別に２人が俺の番号を共有していても驚くようなことじゃないだろう。"


hi "それで、どうしたんです？"


aki "今、暇か？"


hi "たぶん……どうしてです？"



aki "町の公園で会えないかな？　ちょっと久夫と話したいことがあるんだ"



hi "それってデートの誘いですか？"



aki "は？　違うに決まって……"


stop music fadeout 5.0


"突然晃さんがしょげ返ったような声になり、さっきまでの人をからかうような態度があっという間に消えてしまう。晃さんらしくないな。"


hi "とにかく、断る理由もないですし。いつにします？"


aki "何ていうか……今。って感じで"


hi "ちょっと、今すぐですか？　でも、それは――"



"突然電話が完全に沈黙して、晃さんが黙って電話を切ったことを告げる。"


show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_hallway3
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None


"長いあいだその場に立ち尽くし、『通話終了』と表示された携帯画面を見つめる。俺の頭の中でさっきの会話が繰り返される。"


hi "晃さん、一体何なんだ？"

scene bg suburb_park_ss
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0


"道路の左右を軽く見やってから、俺は道を横切って公園の中へと入っていく。"




"こういう外出の時のペース配分はもうわきまえている。そのほとんどはリリーと町へ繰り出す時の彼女のスローペースのおかげだ。意識してゆっくり歩かないといけないからな。"





"ともあれ、俺が即刻やって来ると晃さんが期待してなければいいけど。"


$ ksgallery_unlock("evul akira_park")
scene ev akira_park:
    subpixel True xalign 1.0 yalign 0.0 zoom 1.0
    acdc_warp 15.0 zoom 0.8
with whiteout

play music music_night



"晃さんを見つけるのにそう時間はかからない。缶ビール片手にベンチに座って俺を待っている。"




"俺が近寄っても、晃さんは俺に気づくそぶりもなく、あいさつもしてこない。"




hi "何です、その態度？　別に来なくたってよかったんですよ"




aki "来るって分かってたよ。お前はそういう奴だからな"


scene bg suburb_park_ss
with locationchange

play sound sfx_can_clatter


"空き缶を捨てながらそう言う晃さんに、俺は眉をひそめる。俺が来るまでに空っぽになった缶が、カラカラと金属音を立てる。晃さんは古い木製のベンチに座り、俺もそれにならって腰を下ろす。"

play sound sfx_can



"晃さんは話し始める前に脇にあるもう１本の缶ビールを取り、それを開けるとぐいっとひと飲みする。本当にビール好きみたいだな。"




hi "何の話なのか、聞くまでもなさそうですね。いや、誰の話、と言ったほうがいいですか？"


show akira basic_resigned_close_ss at tworight
with charaenter


aki "リリーから聞いたよ。あたしたちの家族のことを尋ねたんだってな"



"リリーと晃さんが俺の携帯番号以上の情報を共有しているのは確かだ。今のが全く悪意のこもっていない声じゃなかったら、今ごろ激しい不安に襲われていただろう。むしろ物思いに沈んでいるように聞こえる声だ。"




hi "単なる好奇心ですよ、ほとんど"



hi "……晃さんとリリーがスコットランド人のハーフだなんて思いもよらなかったのは事実ですけど"


show akira basic_ending_close_ss
with charachange



"晃さんが皮肉っぽくニヤリと笑う。"


show akira basic_smile_close_ss
with charachange



aki "みんなそう言うよ。マジで"


show akira basic_distant_close_ss
with charachange


"晃さんの表情から小さな笑みが消えて、遠い目になる。"


"曲がりくねった小道をゆっくり歩く老夫婦がたまに交わす会話の声や、奇妙な古い車が立てる音を除けば、ここは心地いいほど静かだ。"


show akira basic_lost_close_ss
with charachange


aki "でも、リリーは全てを話したわけじゃない。だろ？"



hi "断片的にしか。両親がスコットランドに住んでいること、リリーが１２歳の時から両親に会っていないこと、それと彼女が両親と再会したがっていること"

show akira basic_annoyed_close_ss
with charachange



aki "リリーはうちの両親がほんとに好きだからな。いつも驚いてるよ。両親のあたしたちへの善行のたまものだな"



"その言葉には、まるで嘲笑的とも思える調子がこもっている。そんな感情を振り払うかのように、晃さんが小さなため息をつく。"

show akira basic_resigned_close_ss
with charachange



aki "久夫、両親が行っちまったのはどうしてだと思う？"




hi "どうしてご両親が行ったか、ですか？"




hi "リリーから聞いた話だと、仕事の都合だって。ご両親の暮らしぶりからすると、かなり高給な仕事だったんでしょうね"





hi "それでリリーは私立の学校に行った。だからあんな風に上流階級のお嬢様みたいな雰囲気を醸し出してる"




aki "ああ。インヴァネスでのビジネスが成功したんで、父親が現地に本社を移すことにしたんだ"


show akira basic_smile_close_ss
with charachange



aki "でもまあ、久夫ならそういう結論に達するだろうと思ったよ。全く、お人好しだよな"




hi "ご両親は仕事のためにここを去ったわけじゃないんですか？"


show akira basic_resigned_close_ss
with charachange



aki "こんなとこに座って、それをお前に愚痴ってるんだぜ。どう思う？"


show akira basic_lost_close_ss
with charachange


aki "山久学園。ずっと不気味な場所だと思ってたよ。『まっとうな社会』が見聞きしたくない連中を隔離するための場所、って感じでさ"

show akira basic_annoyed_close_ss
with charachange




aki "両親がここを発つとき、山久学園に放り込むにはリリーが若すぎたことを残念がってたに違いないぜ"




"晃さんが突然口にした両親と山久に対する激しい非難の後、長い沈黙が続く。"



"リリーの盲目という事実は、上流階級の家庭が体裁を保つうえで決して無視できない問題だ。ましてや絶好の仕事のチャンスが来ている時ならなおさらだ。"




"とうとう晃さんの感情が頂点に達して、嘲笑的に鼻を鳴らす。"




aki "新しいポストを得て、裕福な将来のために移住する。そんなの、あの時だってまるで信じられなかった"





"単なる晃さんの感情のはけ口になるのは嫌だ。俺はなるべく穏やかに話の方向を変えてみる。"




hi "じゃあ、それで晃さんはリリーと日本に残ることにしたんですか？"

show akira basic_resigned_close_ss
with charachange


aki "あたしがリリーと残るか、さもなきゃリリーは病弱な祖父母の所に預けられるところだったんだ"


hi "静音の家族の所はどうなんです？　もし従姉妹同士なら……"

show akira basic_annoyed_close_ss
with charachange



aki "父親同士がすごく仲が悪くてさ。まあ、あたしから『ふざけんな一緒に住めよ』って言ってやっても全然よかったんだけど、リリーはそういうのは望まなかっただろうし"


show akira basic_resigned_close_ss
with charachange



aki "その頃にはあたしにも仕事の誘いがあったから、リリーと２人でがんばって家の手入れはしてたし、両親がずっとここにいるのと変わらない生活を続けようとしてたんだ"




hi "じゃあ、２人っきりで暮らしてきたんですか？"


show akira basic_lost_close_ss
with charachange



aki "基本的にはね。リリーには学校があったし、あたしには仕事があったから、２人とも別にへこたれてはいなかったよ"




aki "でも、学校生活を送って、勉強して、あたしが働く間に家事をする、そんなリリーを見て、自分が役立たずだと思わずにはいられないよ。結局、リリーを助けようと思ってたのに、行き詰まっちゃったんだ"


show akira basic_annoyed_close_ss
with charachange


aki "……１９歳のガキが盲目の子供の母親になろうとしてさ。馬鹿な話だよ"






"そうか……リリーと晃さんは両親が去った後も２人っきりで暮らしてきたんだ。リリーは自分だけでほとんど何でもやってきた、だから山久の他の生徒に比べてあんなにも自立しているんだ。"







"俺だって両親が共働きだったからほとんど１人で暮らしてきたようなものだけど、でも、それとは……まるっきり違う話だ。"



show akira basic_resigned_close_ss
with charachange



aki "愚痴なんか聞かせちゃってごめんな、久夫"




hi "全然構いませんよ、でも……どうして俺にそんな話をするのか教えてくれませんか？"


show akira basic_smile_close_ss
with charachange



aki "ふむ。いつでも好奇心旺盛だな"


show akira basic_distant_close_ss
with charachange


aki "ことの成り行き、かな"



aki "人生はおとぎ話みたいにはいかないよ、久夫。それを思い知るはめになる人もいる"



"手に持った缶ビールをごくごくと飲むと、晃さんの表情がいっそう暗くなる。"

stop music fadeout 2.0

show akira basic_resigned_close_ss
with charachange



aki "数日前、彼氏と別れたんだ。あたしがここを去ったら、あたしと彼はもう２度と会えないだろうな"




aki "でも、それが人生ってもんさ。最初にお膳立てをして、それが永遠に続くなんてありえない。時には何かが起きて、それを受け入れざるを得ないこともある。それが自分自身や他人を傷つけることになってもな"





"晃さんは大きく息をつくと、明るいオレンジ色の空を見上げる。"


show akira basic_distant_close_ss
with charachange



aki "くそっ……あたしがタバコを吸ってたら、このタイミングでぐっと一服ふかして、かっこよくキメてただろうな"




"何か返事をしたい。どうにかして晃さんの助けになりたいけど、自分が全く役立たずに思える。俺はこんな状況に陥ったことは一度もない。意味のある慰めの言葉をかけられるほど俺は人生経験を積んでいない。"





"晃さんがこっちを見てそれに気づいたようで、とても恥ずかしくなる。"


show akira basic_lost_close_ss
with charachange



aki "あたし、今すごく情けなく見えるだろうな。ほとんど知らない人相手にこんなこと愚痴ったりしてさ"





hi "いいえ、全然。情けなく見えることに関しては俺はもうベテランですから"



show akira basic_ending_close_ss
with charachange


"晃さんがくすりと笑う。それを見て俺は個人的に勝ち誇った気分になる。"

show akira basic_smile_close_ss
with charachange



aki "お前はいい奴だよ、久夫。あたしが妹の付き合いを認めたのだって、ただの冗談や気遣いで言ったわけじゃなかったんだ"



show akira basic_smile_ss:
    tworight
    ypos 1.1
    ease 0.5 ypos 1.0
with charadistant

play sound sfx_can_clatter


"晃さんが歳に似つかわしくないうなり声を上げながらベンチから立ち上がる。そして缶ビールの最後の一口を飲み干すと、空になった缶をゴミ箱に投げ入れる。"

show akira basic_boo_ss at tworight
with charachange



aki "この世の中じゃ、そんなの大して意味がないってのが残念だよ、本当に"




show akira basic_resigned_ss
with charachange


aki "あたしがスコットランドに行くって決めたのは、あたしたちの会社の本社にいいポジションが用意されてたからさ"



aki "だけど、両親の所でそのことを聞かされた時、リリーもインヴァネスに呼び戻すって言い出したんだ。また家族で暮らすためにね"


play music music_sadness fadein 0.5


"まさか……"



"将来についての質問を避けるようなリリーの態度……俺たち２人の間にだんだん深まるぎこちなさ……あの時のリリーらしくない怒りの爆発……"



"突然、全てのことが腑に落ちる。"



"華子の誕生日パーティーの後でリリーが思い出にふけっていたあの家族。より良い場所を求めてリリーと晃さんを置き去りにして旅立っていったあの家族……"





"今となっては、リリーが何を思い悩んでいたのか問いたださなかった自分がバカみたいに思える。インヴァネスの家族を訪ねている間に何かがあった、なんてことすら考えもしなかった。"




"そして今、不安が胸いっぱいに広がってくる。もしリリーの家族がリリーをスコットランドへ、地球の反対側の地まで呼び戻しているのなら……"



hi "リリーはそれを……受け入れたんですか？"

show akira basic_lost_ss
with charachange



aki "リリーがどうするつもりなのかはまだ教えてもらってないんだ。どうやら久夫にも言ってないみたいだな"




aki "だからお前をここに呼んだんだ、久夫"



hi "ことの成り行き、ですか……"


"俺はベンチにもたれかかる。不安や不満の感情が俺の顔にありありと浮かんでいるに違いない。"

show akira basic_resigned_ss
with charachange



aki "久夫、リリーは強い子だ。だけど完全無欠ってわけじゃない"



aki "リリーの心配をするのは姉であるあたしの仕事だろうけど、久夫にもこのことを知っとく権利があると思ってさ"


hi "ええ、分かります"

show akira basic_lost_ss
with charachange


aki "大丈夫か？　落ち込んでるみたいだけど"


hi "いいえ、俺はただ……考えてるんです"

show akira basic_ending_ss
with charachange


aki "ならいいんだ。考えるってのはいいことだよ。早まったってどうにもならないしな"

show akira basic_boo_ss
with charachange


"晃さんが手首をほとんど動かさずに腕時計に目をやる。"

show akira basic_lost_ss
with charachange


aki "もう行かなきゃ。久夫、大丈夫か？"


hi "大丈夫です、心配しないでください。リリーと話をして、全てはっきりさせないと"

show akira basic_smile_ss
with charachange


"晃さんが笑顔を見せる。だけど、心の底から笑っているようにはとても見えない。"


"まったく、リリーが人生最大の決断を迫られ、しかも全ての重荷を自分で背負いこもうとしているのに、俺と晃さんがやっていることといったらそれを遠巻きに眺めているだけだ。"


"そして、その重荷には俺とリリーの関係も含まれているんだ。"

stop music fadeout 5.0
hide akira
with charaexit


"俺が目を上げると、晃さんはすでに手を上げながらここから歩き去ろうとしている。"



"ここにきてようやく、俺は答えを得た気がする。いや、たぶんそこまでは行ってない。だけど、少なくとも何を聞くべきかは分かる。"



"『行ってしまうの？　それともここに残るの？』"

stop ambient fadeout 2.0

scene black
with dissolve




label jp_L28:

scene bg suburb_roadcenter_rn
show rain normal
with locationchange

play ambient sfx_rain fadein 4.0


hi "急いで、リリー！"

show lilly basic_concerned_cas_close_rn behind rain at center
with charaenter


li "これが精一杯です！"


"激しい雨音のせいでリリーの声がほとんど聞こえない。彼女を引っぱりまわすのは嫌だけど、この状況では仕方がない。"



"俺は前を向くと、手を頭にかざして髪だけでも濡らすまいと無駄な努力を続ける。目に見えるのはまるでモノクロの世界だ。夏にしては本当に不愉快な、デートの日には一番ありがたくない天気だ。"





"つくづくいやになる。事前に天気予報を確認するなんて、普段の俺ならまずしないことまでしたっていうのに。日曜の午後は晴れだって言ってたんだぞ。"






"リリーのほうを見ると、今ではもう肩までぐっしょり濡れている。右手で俺の手を固く握りしめ、左手には縮められた杖を持っている。"



"俺とリリーが目的地と山久のちょうど中間にいるときに、このひどい夕立が降り出した。それで、来た道を引き返すよりも目的地へと急ぐことに決めたんだ。"




"こんな急ぎ足に全く慣れていないリリーは、足を滑らせないことだけにずっと意識を集中させている。"


show lilly basic_oops_cas_close_rn
with charachange


li "久夫さん、どこへ行くんですか！？"


"あのリリーでさえ風と雨の大きな音に負けないよう叫ぶ羽目になる。"


hi "しゃ――"


"俺の残りの声は激しさを増すとてつもない雨音にかき消されてしまう。"

show lilly basic_sad_cas_close_rn
with charachange


li "どこですって！？"


hi "上海だよ！"

show lilly basic_concerned_cas_close_rn
with charachange


li "ここからどのくらいですか！？"


hi "そんなに遠くないはずだ！"

show bg suburb_shanghaiext_rn
show lilly basic_concerned_cas_close_rn
with shorttimeskip


"それほど間を置かずに、俺はもう一度リリーに呼びかける。"


hi "どうやらもう安心だぞ、すぐそこだ！"



"見慣れた外装の前にリリーを引き入れる。外に吊るされている提灯が確かな輝きを放っている。リリーの息が整うのを待ってから、俺たちは中に入る。"



hi "レディーファーストで"

play sound sfx_storebell

show lilly basic_smileclosed_cas_close_rn at center
with charachange

with Pause(0.5)

hide lilly
with charaexit


"リリーのためにドアを開けると、中で小さなベルが音を立てる。彼女の笑顔と丁寧な会釈をご褒美として受け取って、俺も中へ入る。"

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
play music music_dreamy fadein 3.0

scene bg suburb_shanghaiint
show lilly basic_smileclosed_cas at center
with locationchange



"リリーに続いて中に入り足元を払う。店の中ががらんとしていることは一目見ただけでわかる。上海はあまり常連客が多くなさそうだけど、今日も例外じゃない。テーブルがほんの２、３埋まっているだけだ。"




"ベルの音に呼び寄せられるように、予想通りの人物が俺たちを出迎えにやって来る。"


show bg suburb_shanghaiint at bgleft
show lilly basic_smileclosed_cas at twoleft
with charamove

show yuukoshang happy_up at tworight
with charaenter


yu "いらっしゃいませ！"


"今日の優子さんは明るい気がする。機嫌がどうなのか想像するのはすごく難しいけど、普段からしたらいい変化だ。"

show lilly basic_smile_cas
with charachange


li "こんにちは、優子さん"


hi "どうも"

show yuukoshang closedhappy_down
with charachange



yu "こんにちは、２人とも"


show yuukoshang neutral_down:
    ypos 1.25
with Dissolvemove(0.2)

with Pause(0.2)

show yuukoshang neutral_down at tworight
with charamove


"優子さんが深くおじぎをする。それから再び顔を上げる時に少し後ずさりして、俺たちの姿をよく見る。"

show yuukoshang worried_down
with charachange



yu "いったいどうしたの？　２人とも……"



"優子さんが俺たちの後ろのドアガラスに目を移す。"

show yuukoshang panic_up
with charachange


yu "あら。あらまあ"



hi "少なくとも今は屋内にいますから。それが一番大事だと思うんです"


show lilly basic_weaksmile_cas
with charachange



li "快適で居心地がよくて。今日屋内で働いているのは運がいいですよ"


show yuukoshang smile_down
with charachange



yu "ずっと快適で静かよ。わたし、こういう日が好きなの"


show yuukoshang worried_down
with charachange


yu "あっ待って、ええと、ごめんなさい……ご注文は何にいたしましょう？"

show lilly basic_smile_cas
with charachange



li "フレンチバニラティーをお願いします"



hi "俺も同じものを"

show yuukoshang closedhappy_up
with charachange


yu "かしこまりました。すぐお持ちいたします"

hide yuukoshang
with charaexit



"優子さんが俺たちの注文を忘れないようにと固い表情を浮かべながら、小走りにその場を去る。他のことはともかく、優子さんは仕事は熱心にこなしている。"




show bg suburb_shanghaiint at center
show lilly basic_smileclosed_cas_close at center
with dissolvecharamove

show lilly basic_smileclosed_cas_close:
    ypos 1.1
with charamove



"俺はリリーを空いた席へと誘導して、２人で腰掛ける。いつもどおり、疲れ切ってどっかりと椅子に座り込む俺と違い、杖を脇に置いて椅子の上に体を滑らせるリリーの姿は繊細そのものだ。"





"しばらくの間、外で降る雨をぼーっと眺める。時々、少しでも濡れないようにと道を走っていく人が見える。その手にはだいたい雨にびっしょりと濡れた傘が固く握られている。"



"リリーは俺と同じように静かに座り、目を閉じて周囲で起こっている全てのことに耳を集中している。"



"俺とリリーの間に、落ち着きのあるリラックスした静けさがただよう。この数か月間、数えきれないくらい分かち合ってきた雰囲気だ。"


stop music fadeout 5.0


"少なくとも、リリーにとっては。"



"俺はといえば、さっきから晃さんの言葉を思い返さずにいられない。その言葉を時々、俺が山久に来てからリリーと一緒に過ごした時間や、俺たちが付き合い出してからの関係と比べたりしている。"




"どんなに努力しても、リリーのことがわからない。まるで、リリーの感情や彼女が下したであろう決定を勘ぐろうとするほどに、明確な結論がどんどん遠のいていってしまうような気がする。"




"そのせいで、リリーのことを本当に理解しているのかも自信がなくなってくる。結局、どんなにそうしたくないとしても、俺はそのことを問いただすしかないんだ。"



show lilly basic_smile_cas_close
with charachange


li "今日は静かなんですね、久夫さん"


hi "そう？"

show lilly basic_ara_cas_close
with charachange



li "あんなに熱心にデートに誘ってくれたのだから、私はてっきり久夫さんが何か特別にやりたいことがあるんだとばかり思っていました"



hi "いや、そんなことないよ。ただリリーと一緒の時間を過ごしたかったんだ"

show lilly basic_weaksmile_cas_close
with charachange



li "そうなんですか……"




hi "わかったよ、ひとつあった"


show lilly basic_cheerful_cas_close
with charachange



"俺に打ち勝ったことを十分に悟って、リリーの顔に笑みが浮かぶ。そのせいで、今から言おうとすることがますます言いづらくなる。"



hi "ただ……晃さんと話してたことなんだけど"

show lilly basic_surprised_cas_close
with charachange


li "あら？"


hi "なんでそんな声出すの？"

show lilly basic_weaksmile_cas_close
with charachange



li "２人とも、とても仲がいいみたいですね"




hi "まあ、晃さんは確かにかっこいい話し相手だと思ってるよ。うちの先生たちも、少しは晃さんみたいだったらいいのにな"


show lilly basic_sleepy_cas_close
with charachange




li "『かっこいい……』"






"リリーがどうしてそんな声を出したのかしばらく考える。その理由に気づいて、俺の口がにやける。"


hi "嫉妬なんかしてないよな？"

show lilly basic_pout_cas_close
with charachange


li "してません！"



"最初のデートで同じことをからかわれた身としては、今回逆の立場でリリーを少し笑ったって別に悪くはないだろう。"




"だけど再び落ち着きを取り戻してしまうと、こんなのは俺がリリーをここに連れて来た本当の理由から目を少し背けさせているだけだ。"




hi "心配しなくていいよ、大体は世間話だったから。だけど、晃さんが言ってた件で、ちょっとリリーと話がしたいんだ"




hi "この前リリーがインヴァネスの家族に会いに行った時のことだけどさ、晃さんが……"


show lilly basic_reminisce_cas_close
with charachange


li "姉さん、家族が私を呼び戻そうとしていることを話したんですね？"

play music music_drama fadein 2.0



"リリーの表情を何とか読み取ろうとして、刻一刻と時が過ぎる。奇妙に混ざり合った感情がその顔に浮かんでいる。いらついているようにも見えるし、困惑しているようにも見える。"


show bg suburb_shanghaiint at bgleft
show lilly basic_reminisce_cas_close:
    twoleft
    ypos 1.1
with charamove

show yuukoshang neutral_up at tworight
with charaenter


yu "あの……どうぞ……"


"優子さんがためらいがちに飲み物をテーブルに置く。その存在感は奇妙なほどに薄い。"

hide yuukoshang
with charaexit

show bg suburb_shanghaiint at center
show lilly basic_reminisce_cas_close:
    center
    ypos 1.1
with charamove



"優子さんが素早く丁寧にお辞儀をしてカウンターに戻っていく。俺はリリーと俺の間の空気の重苦しさに、そして２人とも何だか気難しい表情をしていることに気づく。"


show lilly basic_displeased_cas_close
with charachange



li "姉さんも、私には自分の人生を歩むべきだなんて言うくせに、一番タイミングの悪いときに横やりを入れてくるんですね……"



hi "晃さんを責めるべきじゃないと思う。ただリリーのためを思ってのことさ。俺だって晃さんのその気持ちはわからないわけじゃないさ"


show lilly basic_weaksmile_cas_close
with charachange



"いら立ちを隠せないリリーがぎこちなく自分の感情を押し殺そうとするけど、あまりうまくはいかない。リリーは個人的な話題で追い詰められると、それにほとんど対処できなくなってしまう。"




li "分かっています、でも……もう少し時間が欲しかったんです。いずれ久夫さんにもわかってしまうだろうと思っていました、だけど……"




hi "わざと俺に隠してたの？　いつからそうするつもりでいたんだ？"


show lilly basic_displeased_cas_close
with charachange



li "だから、ただじっくり考える時間が欲しかったんです。久夫さんに伝える前に私の決心に確信を持ちたくて"



hi "それで結局、どういう結論に達したの？"



"リリーに何と言ってほしいのか、俺はわかっている。でもひどく嫌な感覚が俺の腹の底から離れようとない。"




show lilly basic_sleepy_cas_close
with charachange



li "私の家族は、本当に私に戻ってきて欲しいと願っているんです。姉さんも一緒に行きますし。どこであっても教師にはなれるでしょうから"



hi "じゃあ……行っちゃうんだ"



hi "いつから知ってたの？　１ヶ月くらい前、リリーが最初にスコットランドに行ったときにその話を聞かされたって、俺ももう知ってるよ"


show lilly basic_concerned_cas_close
with charachange


li "しばらく……前から"




"俺のいら立ちはもう爆発寸前だ。リリーのこの仕打ちが必要以上に心にこたえる。"




"単にここを去るだけでなく、その計画を意図的に俺から隠していたなんて。こんなにも長い間しっかりと俺を支えてくれた、信頼できる人だと思っていたのに……"




"それはまるで、俺を支えてきたものが突然土台から動き出すような感覚だ。それが急激過ぎて俺は適応することができない。たぶん、これはいら立ちというより心の底からの不安なんだ。"



hi "リリー……"

show lilly basic_sad_cas_close
with charachange


li "ごめんなさい。私はただ……そのことをじっくり考えたかったんです。久夫さんをだますつもりはなくて、だからお願い――"


hi "分かってるよ、リリー。分かってるさ。ただ、ほんとに突然だったから"



hi "ということはつまり、リリーがここを去ったら、俺たちは別れるってことだよな？"



"リリーが完全に言葉を失う。彼女のこんな様子はめったに見たことがない。"



"その表情に驚きはない。去る決心をした時にそのことに思い至っていたからに違いないけど、むしろリリーも目の前の問題にどう対処したらいいのか考えあぐねているように見える。"


show lilly basic_oops_cas_close
with charachange


li "ち、長距離恋愛を続けてみましょう。最近はそういう関係もどんどん普通になってきていますし、だから……"



"リリーはそう言うけど、その声色を聞けば自分でも本気でそう信じているわけじゃないのは明らかだ。"


$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.05, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve



n "\n\n\n古風すぎる傾向のあるリリーが、実際に会えないような関係にうまく馴染めるはずがない。俺だってある程度はそうだ。お互いの触れ合いが地球の反対側から届く声だけになるなんて。"





n "結局、全てを満足させようとしても無理なんだ。今起こっていることから過去や未来をつなげようとしても、意識を集中すればするほどそれはより難しいことのように思えてくる。"





n "リリーとただ並んで歩いたあの静かなひと時、華子や晃さんと一緒に過ごした貴重な時間、昼食の時のなにげないおしゃべり、２人で愛し合った時間、お互いに思いを打ち明けたこと……"



n "\n\n\n全部無意味だったんだ。全部、青春のつかの間の出来事に過ぎなかったんだ。"

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show


hi "俺たちはただ背伸びした子どもに過ぎなかったってことだな"


show lilly basic_sad_cas_close
with charachange



"長い、長い沈黙だけが続く。他の常連客が立てる飲み物の音や話し声も、この状況をさらに奇妙で断絶したものに感じさせるだけだ。"



"リリーは相変わらずうつむき、落胆した様子で表情を曇らせている。"

stop music fadeout 4.0

show lilly basic_concerned_cas_close
with charachange


li "ごめんなさい、久夫さん"


"シンプルな謝罪の言葉、それだけだ。リリーはそれ以上何も付け加えようとはしない。"



"深いため息をついて、俺は気持ちを整理する。そして用意していた最後の質問をリリーに投げかける。"



hi "いつ発つの？"

show lilly basic_sad_cas_close
with charachange



li "姉さんと一緒に行きます。だから、あと１週間足らずで"



hi "夏休みの初めに？"

show lilly basic_sleepy_cas_close
with charachange


li "ええ、始まって少し後に"


"異様にゆっくりとした感情のこもらない声。口調では隠そうとしても、リリーの申し訳なさげに落ち込んだ思いは彼女の顔によりいっそう表れている。"





"結局、２人で一緒に七夕祭りに行く約束を守ることもできないってわけか。"


stop ambient fadeout 14.0
$ ksgallery_unlock("evul hisao_teacup")
show ev hisao_teacup:
    truecenter
    zoom 0.85 subpixel True
    acdc_warp 15.0 zoom 0.8
with locationchange



"俺はうつむいて、放っておかれたまま今ではすっかり生ぬるくなった、目の前の紅茶に写る自分の顔を見つめる。"




"こんな表情はもうとっくに捨て去ったものだと信じ込んでいた。"


"俺はしばらく静まり返った紅茶の表面を見下ろしながら、自分の気持ちを整理して、今であれこれからであれ自分が取るべき行動について考える。"


"だけど今までと同じように、そんな努力も無駄なんだ。"

hide ev
show lilly basic_reminisce_cas_close
with locationchange



"顔を上げて、リリーが文句も言わず穏やかに冷めた紅茶を口にしているのを見る。その顔はうつむき、肩はがっくりと落ちている。リリーも深く考え込んでいるらしい。"
"俺たちがそれぞれ考え込むあいだ、２人の間には奇妙な冷たい雰囲気が満ちる。"




"リリーのカップの中身は少しずつ減っていくけど、俺のはずっと手つかずのままだ。"



"長い時間が過ぎたあとでようやく、外の雨がすっかり止んでいて、他の常連客は店を出ていってしまっていることに気づく。"


scene bg school_dormhallway
with shorttimeskip

stop ambient
play music music_moonlight fadein 0.5



"急に暗さを増す夕方の寒気が、寮の廊下にも染み渡る。重い足取りで廊下を部屋に向かう俺は、眼の前のありがたくない動きに気づく。"


show kenji happy:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter



"思った通りだ。俺の部屋の反対側のドアが開いて、メガネ顔の健二の到来を告げる。"



ke "よう、調子は……"

show kenji tsun at center
with charachange



ke "おいおい、なんかひでえ顔してるな。大丈夫か？"




"全くこいつは、どんな状況でも好転させるコツを心得てるな。"




hi "俺……話したくないんだ。もう遅い時間だし"



show kenji neutral
with charachange


ke "おう。それがいいな"


ke "なんか話したくなったらよ、分かってんな、俺がいるぜ"



"俺はしばらく健二を見て、それから緊張した面持ちを解いて気まずそうに首の後ろをかく。こいつによそよそしい態度を取ってしまったことが恥ずかしくなる。"



hi "ありがとう、健二"

show kenji happy
with charachange



ke "いいってことよ。ダチってのはそういうもんだろ？"






hi "ああ、そうだな。じゃあ"

scene bg school_dormhisao_ni
with locationchange


"俺は自分の部屋のドアを開けると部屋に入り、軽く手を振る健二を尻目に背後のドアを閉める。"

play sound sfx_doorslam



"ドアがフレームに当たって立てる固くて鈍い音は、俺が山久に来て以来送ってきた生活に別れを告げる最後の合図のように聞こえる。"



"俺は暗闇の部屋の中に立ち尽くし、この先どうしたらいいのか探ろうとむなしい努力を続ける。"


"俺はどうすればいいんだ……?"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 2.0

scene black
with dissolve


label jp_L29:

scene bg school_scienceroom
with locationchange


"授業が終わって、俺はただ頬杖をついて時の過ぎるままにぼーっと窓の外を眺める。"

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_normal fadein 2.0

window hide
nvl clear
nvl show dissolve


n "\n\nリリーが彼女の計画を俺に打ち明けたのは数日前のことだ。あれ以来、日常だったリリーとつるむ昼食時間ともご無沙汰だ。そんなことはさして重要でもないけど。"



n "華子は新しく入部した新聞部の活動で忙しい。それどころか、時々直美と教室でおしゃべりまでし始めている。"



n "リリーですら、どんな時であれ俺と顔を合わせるのは気まずいんだろうという実情は別として、夏休みが近づくあいだ学級委員の仕事で忙しく駆けずり回っていた。"


n "そして今、とうとうここまで来た。今日のベルの音が終わるのを合図に、夏休みが始まる。"



n "\n\n\n俺のやることといったら、実家に帰って住み慣れた家で夏休み中ダラダラ過ごすだけだろう。俺の以前立てた計画が完全にねじ曲げられた今となってしまっては。"


nvl clear



n "\n\n一方で、晃さんとリリーはスコットランドに渡って、残りの人生をそこで過ごすんだろう。"




n "夏休みが始まってしまえば、俺の生活もまた以前のように戻るだろう。どんなにそう自分を納得させようとしても、どうしても納得することができない。"





n "誰もが自分の人生を進んでいく。リリーは再び家族と暮らし、晃さんは父親の会社で出世する。華子は新しい友人と趣味を得て、優子さんでさえ大学でやりたいことに向けてまい進している。"






n "俺だっていずれは前に進んでいくんだ。最初は山あり谷ありだったけど、今の山久での成績を考えれば、科学教師という職業への道はまっすぐ開けているように見える。"







n "\n\n少なくとも、それについては俺も喜ぶべきなんだろう。だけど、そんなのは慰めになりそうにない。"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

window show


mi "ひっちゃ～ん！"



"俺は即座に考えをめぐらすのを中断して、でき得る限り最高に上機嫌な表情を作ってから、そばにいる陽気な声の主のほうを振り返る。"


show misha hips_smile at twoleft
show shizu behind_smile at tworight
with charaenter


"思ったとおり、静音が声の主のそばに立っている。俺はひそかに、どうせ何か頼みごとがあるんだろうと勘ぐる。"


hi "よう、ミーシャに静音。どうした？"

show misha hips_grin
with charachange


mi "ええとぉ～……"

show misha perky_smile
with charachange


mi "しっちゃんと考えてたんだけどぉ～……"

show misha sign_smile
with charachange



mi "わたしたち哀れでか弱い女の子２人、夏休みが始まる前だっていうのに急に仕事ができちゃって、手伝ってくれる人が必要で～……"




hi "ああ、もちろん。手伝うよ"

show misha perky_sad
with charachange


mi "けどひっちゃん、ほんとに助けがい――"




stop music fadeout 0.2

show misha perky_confused
with charachange


mi "え？"



"どうやらミーシャを壊してしまったみたいだ。"


show shizu behind_blank
with charachange


"静音も、共犯者がわなわなと震えながら手話を中断している姿を見て眉をつり上げている。"

show misha hips_grin
with charachange



mi "じゃあ、手伝ってくれるの？　ひっちゃんが？"



hi "だから、手伝うって言っただろ？"



"他に用事があるわけでもないし。きっと、２人の仕事を手伝えば今の状況から気を紛らわせるのに役立つだろう。"




"ミーシャは俺の答えに心底陶酔しているようだけど、静音の表情は曇っていて、読み取りづらい。それが憐れみの表情のように見えて、俺はすぐに目を背けてしまう。いや、ただの気のせいに決まってる。"



scene bg school_council
with shorttimeskip

play music music_daily fadein 0.5


"生徒会室に来るのも何度目だろう。俺は本当に頻繁にここに足を運んでいる。それはリリーの学級委員の仕事を助けるためだったり、生徒会自体と雑用をするためだったり。"


"だけど今、ここは以前と様相が全く違う。"

show sc_comp:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"書類やファイルが部屋のテーブル全てにまき散らされ、その乱雑な机の上から小さな黒いノートパソコンだけがぽつんと顔をのぞかせている。"



"それは明らかに時代遅れのパソコンに見える。情報保存という職務を遂行するため、何年ものあいだ立派に働き続けてきたんだろう。"


show sc_comp:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide sc_comp
with None


hi "それで、何を手伝うんだ？　やることはいっぱいありそうだけど"

show misha hips_smile at twoleft
show shizu behind_frown at tworight
with charaenter


shi "……"


"静音が手話を伝えながら毅然とした表情になる。嫌な予感がするぞ。"

show misha hips_grin
with charachange



mi "全部だよ、ひっちゃん！"



"俺の予感は的中した。"


hi "全部……って言ったか？"

show shizu basic_normal
with charachange


shi "……"

show misha sign_smile
with charachange



mi "机の上にある物全部、これがやらなきゃいけないことだよ"


show misha perky_smile
with charachange



mi "これ全部、電子データにしたいの。そのためにノートパソコンがあるの"



hi "それで、俺にそれをやれと？"

show shizu behind_smile
with charachange


shi "……"

show misha hips_smile
with charachange


mi "この前ひっちゃんが図書室でパソコン使ってるの見たって、しっちゃんが言ってるよ。すごくパソコンが得意そうに見えたって～"


"パソコンが得意？　そりゃ、ブラインドタッチぐらいはできるだろうけど、買いかぶりすぎだろう。"



hi "ただ宿題を打ち込んでただけだぞ……"


hi "待てよ、静音はそれを見てたのか？"

show shizu adjust_smug
with charachange


shi "……"

show misha sign_smile
with charachange


mi "敵を知るにはまず味方から、ってね。当然よ～"


show misha cross_grin
with charachange


mi "へえ、あったまいいねぇ……"



"今度ばかりは、今のが誰の言葉なのか簡単に推測できる。"



"何はともあれ、言い争っていても意味はない。静音とミーシャの仕事の助けになるのなら、パソコンの前に座ってデータを打ち込むのも別に面倒なことじゃない。"

show shizu basic_normal
with charachange


shi "……"

show misha perky_smile
with charachange


mi "それに、気も少しは紛れるでしょ～"


hi "気が紛れる？　何から気を紛らわすんだよ？"

show misha perky_confused
with charachange


"ミーシャが静音に手話で伝えながらぽかんとした顔になる。だけど、静音の反応は短い手話の後でちらりと窓のほうに目をやるだけだ。"

show shizu behind_blank
with charachange


shi "……"

show misha sign_smile
with charachange

show shizu basic_normal2
with charachange


"ミーシャが俺に翻訳しながらすぐに笑顔に戻る。たぶんミーシャは困惑していたんだろう。でも、静音の気持ちをはっきり知るのはもっと難しい。"

show misha cross_smile
with charachange



mi "試験から気を紛らわしたいんじゃないかって思っただけなんだけど、決まってるでしょ～"



hi "どっちにしろ、早く始めるに越したことはないな。仰せのままに"

show misha hips_smile
with charachange


mi "そうこなくっちゃ、ひっちゃ～ん！"


hi "とは言っても、昼休み一回でこれを終えられるとはとても思えないな"

show misha hips_grin
with charachange



mi "ああ、それ？　わたしたち、次の授業は休みなんだ。これが終わったら家に帰って夏休みだよ～"



hi "最後の授業をサボるのか？　でも、生徒全員が机やいすを片付けるのを手伝う時間だぞ"

show misha sign_smile
with charachange

show shizu behind_smile
with charachange


"ミーシャが俺の言ったことを静音に翻訳すると、静音が勝ち誇ったような笑みを浮かべて胸を張る。静音、どれだけの権力を先生たちに対して持っているんだろう。"



"少しの罪悪感はあるけど、まあ俺たちだって何らかの仕事をしているわけだし。"

scene bg school_council
with shorttimeskip


"で、これが編集して保存した５枚目のスプレッドシートと。次は翌月の……"



"多少のドタバタはあったけど、俺たちの仕事も少しは手慣れてきたみたいだ。"



"静音は散らばった書類を集めて、ありがたいことに俺の隣に整とんして積み上げてくれる。一方、ミーシャは書類書きだ。女の子らしいピンク色のペンが、見落としようのない目印を次々と書き込んでいく。"





"いったん仕事が軌道に乗ってしまえば、こういうのも悪くない。静音とミーシャも乗りに乗ってるみたいだ。２人は無言で会話を交わしながら、熱意をもって仕事をしている。"




"俺はノートパソコンの横にある、生徒の住所録らしい紙に定期的に目をやり、そこに書かれている記録を忠実に入力していく。記録の内容はあまり意識していなかったけど、ページの中間あたりで俺の目が留まる。"




"羽加道……３年３組……へえ。実家は埼玉か。"


"俺の何気ない好奇心も、ドアから聞こえる３回の軽いノック音ですぐに終わりを告げる。"

show misha perky_smile:
    twoleft
    xpos 0.4
    easein 0.5 twoleft
with charaenter


"誰が来たのかチェックするためミーシャがすぐに駆け出す。そこに向かう途中で静音の肩を叩いて、何が起きているのか情報を共有する。"

show misha hips_grin at twoleft
with charachange


mi "あっ、来たんだ～"


hi "ん？　誰が？"



"静音のデータを他のデータと同じように入力するのをほんの少し中断して、俺は顔を上げてドアのそばにいる人物を確かめる。"


stop music fadeout 0.5

show lilly invis:
    left
    xpos -0.2
with None

show bg school_council at bgright
show misha hips_grin at center
show lilly basic_weaksmile_cas at left
with dissolvecharamove


"……リリー？"


"ミーシャに軽く会釈をした後、リリーは彼女らしいしぐさではっと頭を上げる。"

show lilly basic_surprised_cas
with charachange


li "久夫さん？"


"最近のリリーときたら、俺が発するほんの一言さえ聞きつける地獄耳を持ち合わせている。"


hi "ああ、俺だよ。ええと……やあ"

show lilly basic_reminisce_cas
with charachange



"リリーがおじぎをすると、場の雰囲気が少し気まずくなる。数時間後にリリーが去ってしまうという状況下で、どれくらい親しく振る舞えばいいのか２人ともよく分からない。"




"ありがたいことに、鈍感なミーシャも仕事に夢中な静音も、そんな事情を気にも留めていない。"



hi "それで……リリーもやることがあるの？"

show lilly basic_sleepy_cas
with charachange


li "ええ、残念ながら。できるだけ早く来たかったのですが、クラスメイトが私に秘密でお別れパーティーを用意してくれて。着替える時間もありましたし"


"俺はノートパソコンに表示されている時計に目を落とす。昼休みもほとんど終わりかけている。つまり、リリーもまんまと最後の授業を休む口実を得たってわけだ。"

show lilly basic_weaksmile_cas
with charachange



li "そこに静音もいるのね？"


play music music_shizune fadein 3.0

show shizu behind_blank at right
with charaenter


shi "……"

show misha cross_smile
with charachange


mi "もちろん！"

show shizu adjust_smug at right
with charachange


shi "……"

show misha sign_smile
with charachange



mi "昼休みもずっとここにいたんだからね！"




"最後の一言は必要ないだろ。静音がまたリリーを言い争いに引きずり込もうとしているのは見え見えだ。"


show lilly basic_displeased_cas
with charachange



li "静音、あなたのように勤勉でなくて、ごめんなさいね。私の仕事のためにもっと召使いを雇うよう、今後努力します。約束するわ"


"そしてリリーがそれに食いつき、論戦をエスカレートさせる。"

show shizu basic_frown
with charachange


shi "……"

show misha hips_frown
with charachange



mi "でも、いつもクラスメイトに仕事押しつけてるのはそっちじゃないの～？"


show lilly basic_listen_cas
with charachange




li "彼らは自主的に私を助けてくれているんです。あなたが自分のクラスを専政的に支配しているのとは違ってね"



show shizu behind_frown
with charachange


shi "……"

show misha cross_smile
with charachange




mi "専制支配上等よ～！　わたしたちのやり方は違ったけど、得られた結果は同じだった、でしょ～？"



show lilly basic_displeased_cas
with charachange



li "ここは学校です。警察国家ではありません。悪いけど、あなたがいつクラスの君主に選ばれたのか、教えてもらいましょうか"





show shizu cross_angry
with charachange


shi "……"

show misha cross_frown
with charachange



mi "権力は掌握しなきゃいけないの。与えられるだけじゃダメなのよ～！　リリーには理解できないかもしれないけどね、そうでしょ～？"


show shizu adjust_angry
with charachange


shi "……"

show misha hips_smile
with charachange



mi "こっちこそ、いつから君主が選挙で選ばれるようになったのか教えてほしいわね～"




"それを聞いて、リリーがあからさまに怒る。静音の２連コンボ攻撃でリリーは防御に回らざるをえない。"


show lilly basic_displeased_cas
with charachange


li "だけど、どんなに有り余る権力を振るっても、強制なしには人ひとりの助けさえ得られないわ"

show shizu behind_frustrated
with charachange


shi "……"

show misha sign_smile
with charachange


mi "でも、久夫は進んで助けてくれたわ～！　すごく働き者で、くだらない社交なんかよりこっちをやってくれてるの。ね～？"

show lilly basic_listen_cas
with charachange


li "久夫さん、そうなのですか？"


"ああ、こりゃまずい。まさに板挟みってやつじゃないか。"



"心苦しくはあるけど、少なくとも事実を伝えれば、この場で論戦を終わらせられる可能性はある。"



hi "いいんだよ、リリー。今回は強制されたりして来たわけじゃないんだ"


show lilly basic_displeased_cas
with charachange


"リリーが非難するようにしかめっ面をして、俺のいる辺りに向かって強い不快感を静かにまき散らす。"



"本気で怒った時のリリーはすごく怖いんだ。ありがたいことに、そういう機会は多くないけど。"


show shizu cross_angry
with charachange


shi "……"

show misha hips_frown
with charachange


mi "ひっちゃん、それって、いつもは強制だって言ってるように聞こえるんだけど～……"


hi "違うのか？"


hi "まあ何であれ、すべていい調子に片付くなら、それでいいじゃないか。この仕事もさっさとやっちゃって、家に帰ろうぜ"

hide shizu
with charaexit

hide lilly
with charaexit

hide misha
with charaexit


"静音はあざけるように鼻を鳴らすと、目の前にある書類を仕分ける作業に戻る。一方リリーはため息をついて、壁一面に並ぶファイル棚に手をはわせながら部屋に沿って目的の場所へ向かう。"



"これは俺がことを穏便に抑えるのに成功した唯一の機会、ってことになるんだろうな。だけど、お互いに脅威と敬意を残したままの不本意な停戦というのは、真の平和というよりはむしろ冷戦に近いかもしれない。"



"だけど、何も全て俺のおかげってわけでもない。リリーがここを去るということは静音にもある程度影響を及ぼしているはずだ。だからあんなに簡単に引き下がったんだ。"


show bg school_council at center
with charamove

show lilly basic_listen_cas at center
with charaenter



"仕事に戻ろうとするとき、俺はリリーが書類棚の上に手を伸ばして何か取っているのに気づく。手を貸そうかと言いかけたけど、長身のリリーにとってそれを安全に降ろすのは造作もない。"


show lilly basic_displeased_cas:
    ypos 1.15
with dissolvecharamove



"リリーはその異様な形をした機械を俺のそばの机に置くと、古い緑色のカバーを取って椅子に座る。その時俺は……何となくだけど……その正体に気づく。"


show brailler:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)



"一見すると古くて青い金属製のタイプライターみたいだけど、すぐに普通のタイプライターとは全然違うことに気づく。"




"思っていたよりもはるかにキーの数が少なくて、その表面には何も文字が書かれていない。ただ、小さな点字の点たちがキーに作る影が、この物体の使い道のヒントになる。"



hi "盲人用のタイプライター？"


show lilly basic_smile_cas
with None 

show brailler:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide brailler
with None


li "ああ、これですか？　そうですね、当たらずとも遠からず、ですよ"


li "一般にパーキンスブレーラーと呼ばれるものです。でも、そうですね、基本的には盲人用のタイプライターです。文字の代わりに点字を打つんです。それでキーの数が少ないんですよ"


hi "へえ……すごく洗練されてるな"

show lilly basic_cheerful_cas
with charachange



"俺の好奇心を知ってリリーが陽気な笑顔を見せる。その機械が俺の興味をかき立てていることは認めざるをえない。"


hide lilly
with charaexit



"俺たちはおしゃべりを切り上げて、それぞれ割り当てられた仕事へと戻る。すぐにリリーのブレーラーがガチガチと立てる大きな機械音と、ノートパソコンのくたびれたキーボードを叩く音が部屋中に満ちる。"




"とてもいい雰囲気だ。ここにいるみんなが自分のすべきことを分かっている。リリーと俺は隣同士で座って、仕事を続けながら時折言葉を交わす。"






"ノスタルジー。この言葉が今の雰囲気に当てはまる気がする。"


"心地いい。だけど、一緒の時間がもうすぐ終わりを告げると知っている俺の心には、ほんの少しの陰りがある。"

show lilly basic_smile_cas:
    center
    ypos 1.15
with charaenter



li "ミーシャ、ちょっといいかしら？"



show bg school_council at bgleft
show lilly basic_smile_cas:
    twoleft
    ypos 1.15
with charamove

show misha hips_smile at tworight
with charaenter



"リリーには見えないにもかかわらず、ミーシャはちゃんとリリーに話しかけるために、覗き込んでいた書類棚からすっとんで来る。変な行動だと一瞬思ったけど、俺もまったく同じようにしているのを思い出す。"



mi "どうしたの？"

show lilly basic_weaksmile_cas
with charachange



li "静音に３年２組の出席簿がどこにあるか聞いてもらえるかしら？　移動してしまっているみたいだから"


show misha hips_grin
with charachange



mi "がってんしょーち！"






hide misha
with charaexit

stop music fadeout 8.0


"その返事とともに、ミーシャは身をひるがえして俺たちの背後で仕事をしている静音のほうへ向かう。"


"リリーは生徒会室の勝手を分かっていて、仕事の効率もいい。そんな様子から俺は、リリーとミーシャと静音がかつて生徒会でずっと一緒に仕事をしていたことを思い出す。"



"きっとこれがリリーにお似合いな、山久での生活の幕引きなんだろう。彼女が愛する人や、少なくともかつては好きだった人、そんな面々に囲まれて、かつてと同じように仕事に打ち込みながら。"





"俺は目を上げると、ミーシャじゃなくて静音が棚の書類を調べているのを見て意表を突かれた気持ちになる。"


show shizu behind_blank at tworight
with charaenter



"思ったとおり、静音は表紙のかろうじて目に見える突起以外は何も書かれていないフォルダを引き出すと、それをリリーの前に差し出す。"




"リリーの手がその上をさっとなぞって内容をチェックする。指が点字を感じ取って、それがリリーの頼んだものだということを確認する。"


show lilly basic_smile_cas
with charachange



li "ありがとう、ミーシャ"




"返事はない。"

show shizu behind_smile
with charachange


"返事はない、というのは、静音の顔が変にニヤついて……いや……笑って……いる以外は、ってことだけど。"

show ev lilly_sheets:
    truecenter
    zoom 1.05 subpixel True
    easein 10.0 zoom 1.0
with whiteout


"数秒して、その人物が背後にいるミーシャでなく静音だということにリリーがはっと気づく。リリーはほんの一瞬驚いた様子で、それからはにかみがちな笑顔を見せる。"


"しばらくのあいだ、部屋の中に静寂と沈黙だけが満ちる。"


"だけど結局、静音は自分の持ち場へときびすを返し、リリーも再びタイピングを始める。"




"ほんの数秒の出来事だった。だけどその沈黙の瞬間、２人の間で何年分もの会話が交わされていたようにすら思える。"


scene bg school_council_ss at right
with shorttimeskip

play music music_tranquil fadein 3.0


hi "よし、終わったぞ"


"俺は頭を後ろに反らして疲れを和らげようと目をこする。小さくて貧弱なスクリーンを見続けるってのは結構こたえるな。"

show lilly basic_smile_cas_ss:
    center
    ypos 1.15
with charaenter



li "最高のタイミングですね。私も、これをファイルに綴じてしまえばすべての仕事が終わります"



hi "そっか。俺はその間にブレーラーを片付けておくよ"

show lilly basic_smileclosed_cas_ss
with charachange


li "ありがとう、久夫さん"


hi "ミーシャ、ミーシャと静音はまだ終わりそうにない？"



"ブレーラーにカバーを掛けながら辺りを見回して２人を探すと、ミーシャも静音もドアのそばで待っている。たぶん俺たちを待ってくれているに違いない。"


scene bg school_council_ss at left
show misha hips_smile_ss at center
show shizu behind_blank_ss at right
show lilly basic_smileclosed_cas_ss at left
with shorttimeskip



"最小限の時間で、俺とリリーは残りをファイルに綴じて片付けを終え、ミーシャたちに合流する。"




hi "待っててくれてありがとな、２人とも"


show misha hips_grin_ss
with charachange



mi "ひっちゃんを置いて帰ったりなんてできないでしょ。すごく助かったんだから！"





show shizu behind_smile_ss
with charachange


"静音も俺の努力に喜んで、満足げにうなずく。"



hi "じゃあ……これが学級委員としての最後の仕事ってことかな"


show lilly basic_smile_cas_ss
with charachange


li "そうですね"

show misha perky_sad_ss
with charachange



mi "寂しくなるね、リリー。一緒に仕事できて楽しかったと思うよ"


show lilly basic_weaksmile_cas_ss
with charachange



li "ありがとう、ミーシャ。一緒に仕事ができて良かったわ。あなたと……静音とも"



show shizu basic_normal_ss
with charachange


"静音がしばらくのあいだどう返答すべきかを考える。別に普段の静音が考えなしに会話してるってわけじゃない。むしろその逆だ。だけど、今回は普段よりももっと深く考え込んでいる。"

show shizu adjust_smug_ss
with charachange


shi "……"

show misha perky_confused_ss
with charachange


"そのメッセージを伝える前、ミーシャは少し驚いたみたいだ。"

show misha hips_smile_ss
with charachange



mi "しっちゃんが……むこうではこっちでやったよりももっとうまくやった方がいいわね、って"



show lilly basic_giggle_cas_ss
with charachange


"リリーはそれを悪口と捉えるどころか、口に手を当ててクスクスと笑っている。"

show lilly basic_smileclosed_cas_ss
with charachange



li "だったら、これからはここに残っている人たちにももう少し理解を示すようにって、静音に伝えてね"



"最後まで相変わらずだな。たぶん、結局静音もリリーも似た者同士なんだ。"



show shizu behind_smile_ss
with charachange


shi "……"

show misha hips_grin_ss
with charachange


mi "しっちゃんが、リリーがちゃんと約束したとおりの人生を送っているかチェックするから、って"


show lilly basic_cheerful_cas_ss
with charachange


li "ならば、そうしてくださいな"

show lilly basic_smile_cas_ss
with charachange



li "さて、もう行ったほうがいいわね。さようなら、静音。さようなら、ミーシャ"


show lilly basic_smileclosed_cas_close_ss
with characlose


li "久夫さん？"



"リリーが自分の腕を俺の腕に絡ませる。俺が導く時、彼女に杖は必要ない。２人に向かって別れの会釈をしながら、俺たちはドアをくぐって校庭に向かって歩き出す。"


"別れのために手を振ろうと振り返って、俺はリリーをじっと見つめている静音に気づく。お互いにうとましいこともあるだろうけど、一族のきずなはそう簡単には壊れないんだ。"

scene bg school_courtyard_ss
with locationskip


hi "それじゃ、書類はもう全部準備できたんだ？"


show lilly basic_smileclosed_cas_ss at center
with charaenter


li "はい。全て記入して提出済みです"


hi "いつもどおり用意周到、だな？"

show lilly basic_weaksmile_cas_ss
with charachange

stop music fadeout 4.0



"俺の褒め言葉でリリーが心底笑顔になる。だけど、リリーだっていかに多くのものを後に残していくか十分承知しているんだ。そんな事実の前では、彼女の幸せそうな笑顔も上っ面だけに思える。"




"俺と初めて会った時のリリーの様子を思い出す。いつも笑顔で、いつもほんの少しよそよそしくて、そしていつも誰からもほんの少しだけ距離を置いていた。"




"今だってリリーは、特に親しくない多くの他人の前ではそんな雰囲気を保っている。俺とリリーが一緒の時を過ごすことで彼女が変わってくれるよう、俺はずっと望んできたんだ。"


scene bg school_gardens_ss
with locationchange


"俺たちの歩くペースがゆっくりになり、ついにはがらんとした学校の中庭で立ち止まってしまう。"

show lilly basic_weaksmile_cas_ss at center
with charaenter


li "久夫さん？　どうかしたの……"

play music music_comfort

show lilly basic_surprised_cas_close_ss
with vpunch



"俺は振り返ってリリーの体に腕を回して固く抱きしめ、そのせいでリリーの言葉が遮られる。普段なら衝動的にこんなことをしたりはしない。だけど、ただリリーの近くにいたい。これが最後の機会だとしても。"




"他の生徒たちはもう学生寮の自分の部屋や家に帰ってしまっている。音を立てているのはそよ風に揺れる葉っぱのざわめきだけだ。"

show ev lilly_touch_cas
with charachange


"俺がリリーから離れると、注意深く保たれていた彼女の笑顔は消えている。"


"リリーの手が俺から離れることをためらい、俺に触れ続けることもためらう。"


"気丈に振る舞うリリー。だけど、ほんの少し震えている彼女を見れば本心は明らかだ。リリーの自制心はとても強いのに、彼女であっても今は落ち着きを保ってはいられない。"



"この人こそ、俺が愛するようになった女性だ。だけど彼女は、もうほんの少ししたらこの国を永遠に去ってしまうんだ。"



li "ごめんなさい、久夫さん"


hi "いいんだ。リリーはやっぱり自分自身の決めた人生を生きるべきなんだ"

scene bg school_girlsdormhall
with shorttimeskip



"俺とリリーは手をつないで女子寮の廊下を歩く。今では２人ともすっかり冷静さを取り戻している。にもかかわらず、俺たちはさっきよりもずっと固くお互いの手を握り合っている。"



"かすかなひそひそ声がリリーの部屋の中から聞こえてくる。その声の主は簡単に想像できる。"

scene bg school_dormlilly

show hanako invis at tworight
show lilly invis at twoleft
with locationchange

show lilly basic_weaksmile_cas at twoleft
show hanako emb_downsad:
    xpos 0.4 xanchor 0.5
with dissolvecharamove

show lilly basic_surprised_cas
with vpunch


"リリーがドアを開ける瞬間、華子がこっちに突進してきてリリーの体を抱きしめ、リリーが飛び上がって驚く。"




ha "リリー！　リリー！"

show lilly basic_oops_cas
with charachange


li "は、華ちゃん……？"

show hanako emb_downtimid
with charachange


ha "寂しくなるよ……リリー……"

show lilly basic_weaksmile_cas
with charachange


"思ったとおり、華子は今にも泣き出しそうだ。リリーはそれに応えるように華子の髪を優しくなでる。そして華子から離れると、暖かく力強い笑顔を見せる。"

show akira invis:
    right
    ypos 1.15
with None

show akira basic_lost at right
with dissolvecharamove


"華子越しに部屋の向こうを見ると、晃さんがリリーのベッドの脇で立ち上がって頭をかいている。"

show akira basic_smile
with charachange



"晃さんはリリーと華子から俺のほうに視線を移すと、こわばった顔で弱々しく笑う。俺はもう少し純粋に喜んでいるような笑顔を返そうとするけど、結果はたぶん同じだろう。"




show akira basic_boo
with charachange




aki "さて、準備できたか？　静音をぶっ殺すのは我慢できた？"




show lilly basic_giggle_cas
with charachange



"晃さんのその言葉を聞いて、リリーは愉快そうに笑う。"





li "ええ、全て計画通りに。それにちゃんと我慢もできましたよ。姉さんは必要なものは全部持ってきた？"




show akira basic_smile
with charachange



aki "ここにはバッグ２つ持ってきたけど、羽加道の家にもまだ荷物があるんだ。だけどまあ、明日の夜のフライトまであそこにいるから、そのあいだに荷物も引き取れるよ"




"晃さんが床に置かれた２つの大きな黒い旅行かばんをこつんと叩く。きっと晃さんは、リリーと一緒に出発する前に、荷造りと段取りの確認を手伝いに来たんだろう。"


show hanako cover_worry at center
with dissolvecharamove


ha "リリー……むこうで……大丈夫？"

show lilly basic_smileclosed_cas
with charachange



li "大丈夫よ、安心して。姉さんも私の面倒を見てくれるのだし。華ちゃんだって、姉さんは信頼できるって知っているでしょう"


show hanako basic_worry
with charachange


ha "でも……"

show lilly basic_smile_cas
with charachange


li "心配しないで、華ちゃん。電話番号だって知っているのだから、連絡もできるわ。姉さんの助けを借りれば、インターネットを使って何か送ったりもできるでしょうし"

show akira basic_boo
with charachange


aki "おい、パソコンを使えるようにならないからって、いちいちあたしを使うのやめてくれよ"

show lilly basic_giggle_cas
show hanako basic_smile
with charachange



"華子とリリーが２人で軽くクスクス笑って、ほんの少しだけ雰囲気が明るくなる。"


show lilly basic_smileclosed_cas
with charachange


li "久夫さん、あなたにも。スコットランドに着いたら連絡しますね。約束します"


hi "ああ、分かってる。楽しみにしてるよ"



"親切な申し出だろうけど、それは２人がバラバラになることを意味するんだと俺もリリーも知っている。俺たち２人とも長距離恋愛でうまくやっていけるなんて幻想は持ち合わせちゃいない。"




"誰が号令を発するわけでもなく、俺たち４人は長い道のりを学校の正門に向かって重々しい足取りで歩き出す。"

scene bg school_gate_ni at bgleft
with shorttimeskip


"山久の敷地内にあちこちに立っているたくさんの外灯も、深い暗闇の中でほんの点々とした光を照らし出しているだけだ。"


"校庭のすぐそばの道路に止められている車が視界に入ってくる。その黒光りの外装が山久の外灯のぼんやりとした光を反射している。重苦しいムードを少しでも和らげようと、俺は晃さんに話しかける。"


hi "あれが晃さんの車？　なんて車ですか？"

show akira basic_smile_ni at center
with charaenter


aki "車のことあんまり詳しくないんだな？　ランエボだよ。安定性もスピードも抜群さ"



"うーん、晃さんの俺の知識に対するコメントはあながち的外れってわけじゃない。あんまり車には興味を持ってこなかったからな。"


show akira basic_resigned_ni
with charachange


"晃さんが小さくため息をつく。"

show akira basic_lost_ni
with charachange



aki "いい車だったよ。明日お別れってのがつらいな。別荘もそうだけどさ。みんなはあの別荘の持ち主が変わる前の最後の客だった、ってわけ"



"無駄な努力に終わったおしゃべりをそらすように後ろを振り返ると、背後を歩いている華子とリリーの姿が目に入る。"

show akira basic_lost_ni at tworight
show bg school_gate_ni at center
with charamove

show hanako emb_downtimid_ni:
    xpos 0.4 xanchor 0.5
show lilly basic_weaksmile_cas_ni at twoleft
with charaenter



"本来なら華子がリリーをリードするはずだけど、リリーの腕をしっかりとつかんでいる華子を見ていると、２人の立場はむしろ完全に逆転している。"



"気が沈むような光景だ。"

show akira basic_resigned_ni
with charachange


aki "それじゃ……ここまでだな"

show lilly basic_reminisce_cas_ni
with charachange


li "そうですね"



"今こそ全員が別れを告げるべき瞬間が来ているのに、誰もその口火を切ろうとしたがらない。まるで、ずっと黙っていれば２人がここに残れる可能性が増すとでも思っているみたいに。"


show hanako emb_downsad_ni
with charachange


ha "リリー……どうしても行かなきゃダメなの？"

show lilly basic_concerned_cas_ni
with charachange


li "ごめんなさい、華ちゃん。だけど、ずっと離れ離れというわけではないわ。電話でお話もできるし、ここには久夫さんもいるのだから"


"俺はうなずく。だけど華子はリリーの腕をますます固くつかむ。"


"家族と呼べるような人がずっといなかった生い立ちを持つ華子にとって、彼女の人生の中で母親にも匹敵するような人物に別れを告げるのは、耐えがたいほどつらいことに違いない。"

show lilly basic_sad_cas_ni
with charachange


"リリーが深い悲しみの息を漏らす。晃さんと俺は無言のままそばに突っ立っていることしかできない。だって、この雰囲気を何とかできるのはリリーだけなんだ。"


"ついに、リリーがしがみつく華子から自分の腕を抜き、それから華子の両肩を優しく引き寄せる。それは、俺が見てきたどの華子の扱い方よりもはるかに断固たるやり方だ。"

show lilly basic_reminisce_cas_ni
with charachange


li "華ちゃん、最初に出会った時のこと、覚えているかしら？"

show lilly basic_weaksmile_cas_ni
with charachange





li "私が友達を慰めるのをたまたま聞いた後で、初めて私の部屋に来てくれた時、あなたは一晩中一言も口を利かなかったわね。私がお茶を出して話しかけても、あなたは静かに座って私の話を聞くだけだった"









li "あなたが心を開いてくれるようになるまで、本当にたくさん静かな時間を一緒に過ごしたわね。でも、あなたが変わり始めるにつれて、私は今まで感じたことのない幸せな瞬間を経験したの"


show lilly basic_sleepy_cas_ni
with charachange



li "あなたに同情したから友達になったわけではないの、華ちゃん。あなたが私だけじゃなくて、みんなから隠れているのがわかっていたから、あなたの友達になったのよ"




li "あなたの志、性格、興味、趣向……私も、他の誰も、華ちゃんのことを何も知らなかった"



show lilly basic_weaksmile_cas_ni
with charachange



li "だけど、華ちゃんが自分を見せてくれるようになって、あなたの人となりが分かり始めてきたの。そして確信したわ。私たちの出会いはとても特別な瞬間だったって"


show hanako emb_blushtimid_ni
with charachange


ha "でも、私……"


"リリーの手が華子の頭のほうへ伸び、華子の言葉が遮られる。リリーは華子の前髪を横へかき分けると、華子の額に唇を優しく押し当てる。"

show lilly basic_smile_cas_ni
with charachange


"リリーの頭が華子から離れると、華子はただ呆然としながら目を潤ませている。リリーが明るく笑いかける。"



li "華ちゃん、あなたはとても美しい子だと信じています。あなたはきっと、強くて自信に満ちあふれた女性になるわ"



li "華ちゃんは愛すべき私の大親友です。久夫さんと同じく、私は命ある限りあなたのことを決して忘れないわ"

show lilly basic_smileclosed_cas_ni
with charachange



li "私は去ってしまうけれど、あなたにはここでのあなた自身の人生があるのよ。私と同じように、華ちゃんにも友達や趣味や、卒業後の希望だってある。私がいなくなっても、それに一生懸命打ち込んでほしいの"



show lilly basic_smile_cas_ni
with charachange



li "だから華ちゃんは大丈夫だと思うの。華ちゃんは自分の人生を自分自身で生きているのだから。あなた自身がそれを私に証明してくれたわ"


show hanako emb_downtimid_ni
with charachange



"華子は恥ずかしそうにうつむきながらも、ついにはうなずく。"




ha "わ……分かった……"


ha "さよならを言わなきゃね……リリーは自分の道を歩んでいかなきゃいけないから……"

show hanako emb_smile_ni
with charachange


ha "でも……ありがとう、リリー。今までのこと、全部"

show lilly basic_reminisce_cas_ni
with charachange


li "ありがとう、華ちゃん。これから大丈夫？"



"数秒の沈黙の後、華子が返事をする。"

show hanako cover_smile_ni
with charachange


ha "うん、大丈夫"

show lilly basic_smile_cas_ni
with charachange


"リリーが笑顔になる。少なくともそれに安堵がこもっていることは間違いない。"

show lilly basic_smileclosed_cas_ni
with charachange


li "そう、とても嬉しいわ。さようなら"

show hanako basic_bashful_ni
with charachange


ha "さようなら……リリー"

show lilly basic_weaksmile_cas_ni
with charachange


li "久夫さんも、ごきげんよう"


hi "さようなら。寂しくなるな"

show lilly basic_weaksmile_cas_close_ni
with characlose


"しばらくためらった後、リリーが俺のほうに近寄る。彼女は右手を前方に伸ばし、俺の肩に手を乗せる。"


"リリーの左手はゆっくりと上品に俺の顔のほうへ伸び、その手の平で俺の頬を包む。"

show lilly basic_smile_cas_close_ni
with charachange


"しばらくのあいだ、リリーはただ俺の顔に触れ、ほんの少し指を動かして俺の顔の輪郭を感じ取っている。普段ならこうしている時の彼女の手は暖かいけど、夜の空気のせいか彼女の肌はひんやりしている。"


"どれくらいそうしているのか分からない。リリーは諦めきれないような、ほとんど遠くを見るような笑顔を浮かべて、曇った瞳で俺の瞳のすぐ下を見つめる。だけどついに、俺は自分の手で彼女の冷たい手を取る。"




"そうしたくはないけど、俺は小さなため息とともにリリーの手を優しく俺の頬から引き離す。"



hi "リリー、幸せな人生がずっと長く続くよう願ってる。どこにいてもな"


show lilly basic_weaksmile_cas_close_ni
with charachange


li "ありがとう。きっとそうします"


"震える息で大きくひと呼吸してから、リリーは晃さんのいるほうへと少しだけ体を向ける。"

show lilly back_sad_cas_close_ni at twoleft
with charachange


li "姉さん……"

show akira basic_lost_ni
with charachange


aki "オーケー"

show hanako basic_bashful_ni at left
show lilly back_sad_cas_ni at center
show bg school_gate_ni at right
with dissolvecharamove



"晃さんはうなずきながらリリーの手を取ると、リリーを連れて門の外に止めてある車のほうへ歩き出す。まるで前もって練習していたかのように、２人はゆっくりと慎重に歩く。"



"山久を去っていく誰かを見るのは、なんだか妙な気分だ。今感じている不安な感覚で俺は、あの黒塗りの鉄門を初めてくぐった時のことを思い出す。いつも学校の門にしては厳めしすぎるように見えたあの門を。"



"２人が去ることで、俺たちの人生が後戻りできないほどに変わってしまう。みんなそのことは百も承知だ。"
"人生をありのままに受け入れるしかないんだと、俺はずっと自分に言い聞かせてきた。だけど、全てのことがあまりにも急激に、唐突に変わりすぎている。"




"やっぱりリリーの存在は、華子と俺の両方にとってかけがえのない人生の一部なんだ。"


"晃さんがリリーのために助手席のドアを開ける音を聞いて、俺は我に返る。リリーが車に乗り込むと、晃さんが背後に向かって手を振る。"

show akira basic_smile_ni
with charachange



aki "じゃあな、２人とも！　元気でな！"


show lilly basic_weaksmile_cas_ni
with charachange


li "さようなら、華ちゃん、さようなら、久夫さん！"

show hanako cover_smile_ni
with charachange


"華子が素早く手を振り上げる。熱狂的な別れの言葉とともに華子の表情は輝きを増す。"


ha "さようなら、リリー！　さようなら！"



hi "じゃあね、晃さん、さようなら、リリー！"


hide lilly
hide akira
with charaexit


"俺たちが皆最高に幸せな別れの表情を見せる中、車のドアが閉まる。晃さんは車に乗り込むと、手早くエンジンを始動させる。"




"ちょうど、リリーがこちらに手を振っているのが色づいた車の窓越しに見える。俺も華子も手を大きく振る。"




"いつもそうだったみたいに、今回も、どうして俺が、いや華子も、決してそれを見ることのないリリーに向かって手を振っているのかよく分からない。でも、そんなことはどうだっていい。"


"黒光りする車が丘を下って暗闇の中に消えてしまっても俺たちは手を振り続け、晃さんとリリーを見送り続ける。"

stop music fadeout 5.0



"そして……２人は行ってしまった。"


show bg school_gate_ni at center
show hanako basic_normal_ni at center
with dissolvecharamove


"俺たちが手を降ろす頃には、奇妙な静けさがその場を支配している。"


"どう振る舞うべきか、どう感じるべきか、俺にはよく分からない。結局、俺たちはただ静かに立ちつくして車が視界から消えた方角を見つめ続ける。"


ha "さようなら……リリー"

show hanako basic_normal_close_ni
with characlose



"華子の静かで沈痛な別れの言葉に対して、俺はその肩に手を置くくらいのことしかできない。"


show hanako basic_distant_close_ni
with charachange


"華子は再び丘のほうに目をやるまでの少しのあいだ、俺の顔を見つめる。今も華子のそばには俺がいるということをしっかり確認しているんだ。"



"俺たちがこれからどうすべきか、全く見当がつかないわけじゃない。リリーも言っていたとおり、今では俺たちみんなにそれぞれの志があるんだ。"





"だけどそうであっても、俺と華子両方の人生から、ある何かが失われてしまったように感じる。かけがえのない何かが。"



window hide Dissolve(1.0)
$ suppress_window_before_timeskip = True

scene black
with Dissolve(2.0)



label jp_L30:



scene bg school_hallway2
with locationchange

play music music_daily fadein 1.0



"俺が携帯を折りたたむ時のパチンという音は、図書室の外の廊下にいても聞こえるぼんやりとした喧騒とは対照的だ。"



"夏休み初日。永遠の先にあるかのように思われたこの日がついにやってくる。それだけじゃなく、ここの生徒、いや、残っている生徒の少なさによって、夏休みだということを痛いほど実感させられる。"





"今ではほとんどの生徒が家族や親戚と過ごすために実家に帰ってしまっている。ここに残っている少数の生徒は、主に夏休み中に何をするかという話題でお互いに盛り上がっている。"





"夏休み最初の数日間開いている学校図書室を利用しようとする俺は、なんだか仲間外れにされているような気持ちになる。"




"借りた本をまだ返していない生徒のために、それから親が迎えに来るのを待っている生徒が時間を潰すために、というのが図書室が開いている表向きの理由だ。"




"今しがた、図書室の後ろのソファで寝ていた俺を乱暴に叩き起こした親からの長電話のおかげで、俺は今では後者に当てはまる。"





"今度は忘れずにマナーモードにしてから携帯をポケットの中に滑り込ませると、俺は静かで穏やかな雰囲気に満ちた部屋へと戻る。"


scene bg school_library_ss
with locationchange



"懐かしい光景だ。リリーが俺を初めて連れて来た時と同じように、部屋中が夕暮れのオレンジ色の光を浴び、華子はソファに座って読書にふけり、大わらわの優子さんがカウンターの後ろからほんの少しだけ見える。"





"とくに華子は昨日の出来事以来、明らかに普段よりも静かだ。無理もない。"



"ようは、あの人に頼っていたのは俺だけじゃなかった、ってことだ。"



"余計な物音を立てないよう念入りに注意しながら、俺は自分がさっきまで座っていた、華子の近くにあるソファに戻る。"


scene ev hana_library
with locationchange

show ev hana_library_read
with charachange


"俺が体重をかけるとソファがパフッという感じの音を立てて、華子がチラッとほんの一瞬だけこっちを見る。"



"リリーが去って悲しいというのは華子が静かにしている理由の一部でしかない気がする。"





"むしろ、俺が想像していたよりももっと慎重に考え込んでいるように見える。たぶん、リリーが去ってただ落ち込むよりも、それを乗り越えたいと望んでいるからだ。そんな華子のことを少し誇らしく思う。"





hi "なあ、華子？"

show ev hana_library
with charachange


ha "な、何？"


hi "旅行に行くって計画、今も進んでるのか？"


"華子が力強くうなずく。"




ha "明日か明後日には出発するつもり。直美さんも一緒に行くことに決めたって"





hi "へえ、早いんだな。最初はどこに行くつもり？"




ha "初めは北の方に行こうかなって……それから、Ｕターンして南向きに"




hi "じゃあ……最初は北海道に？"





"華子が、今度はさっきよりもためらいがちに、もう一度うなずく。俺たち２人とも、あの場所が持つ特別な意味を忘れてはいない。"




hi "旅行代とか宿泊場所とか、どう手配するかは分かってる？"





ha "うん、全部準備してあるから。たぶん大丈夫だと思う。直美さんも準備できてるって言ってくれてるし"





hi "なにかあったら電話してくれよな？　俺の電話番号は前に渡したし。何時でも大丈夫だから"



show ev hana_library_smile
with charachange



"華子が笑顔を見せる。それだけで俺は勝ち誇りたい気持ちになる。"





ha "分かってる"


ha "あ、ありがとう……久夫くん"




"リリーは正しかったのかもしれない。俺は華子のためならどんな手助けでもするだろう。でも華子にはそんな助けは必要ないことも、もう分かっている気がする。"



"華子、本当に成長したな。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve



n "\n\n\n華子の休み中の計画は、親に言われるがまま家族と過ごすことにしている俺のとはまるで正反対だ。"




n "だけど昔から、休みが来たからといって、他の人たちみたいに特別わくわくする気持ちを覚えることはなかった。つまり俺が元の俺に戻っただけなのかもしれない。"





n "\n心臓発作が起こる前の俺は何の目的もなく生活していたので、休日も普段の日常と大差なかった。"




n "放課後家に帰る前に少し街をぶらつき、大体は友達何人かともつるんでいて、家に帰ってからは両親のどちらか１人と夕食を食べる。親が２人ともそろうことはめったになかった。"




n "親も仕事が忙しくてそんなに家にいられなかったから、学校からまっすぐ家に帰っても退屈するだけだった。筋金入りの都会っ子だ。"


nvl clear



n "\n\n\nだけど山久に来てから、俺は根本的に生まれ変わったような気がする。その点について多少の不安はあったかもしれないけど、電話で両親と話した時には全部消え去ってしまった。"




n "１０代としてはごく一般的な水準――つまり大したことのないレベル――の自立性を発揮してはいたけど、俺が新たに身に付けた自活能力を耳にして、両親はすごく喜んでいた。"




n "親のいない生活で発生する、洗濯、自炊、掃除、その他もろもろの雑事……必要に迫られてやりかたを学んでいったけど、割と簡単なことだった。"




n "\nこうして考えてみると、たとえ親が家にずっといなくても、俺はいつも親に依存していたんだ。だけど山久の寮に入ってからは誰にも頼らずに生活してきたと言えば、それは嘘になる。"


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve
window show


yu "あの……ごめんなさい……"

stop music fadeout 3.0

scene bg school_library_ss
show yuuko worried_down_ss at center
with locationchange



"俺たち２人とも、目の前でばつが悪そうにもじもじしている人影を見上げる。ずっと変わらないものもあるんだな。"


show yuuko worried_up_ss
with charachange



yu "もうすぐ閉める時間だから、その、ええと……"




"ああ、そうか。休み中は図書室もいつもより早く閉まるのを忘れていた。"




"華子と俺は立ち上がってほこりを払うと、背後にある本棚にそれぞれ本を戻す。俺たちの読書の好みが少なからず重なっているということも、時々は役に立つ。"



"長い時間かかったことを優子さんにペコリと謝ると、華子は俺たちのもとを去っていく。"

show bg school_library_ss at bgleft
show yuuko worried_down_ss at twoleft
with dissolvecharamove

show hanako basic_normal_ss at tworight
with charaenter


ha "久夫くん、また明日"



hi "じゃあな"

hide hanako
with charaexit


"その言葉とともに、華子は図書室の入り口であることを誇示する木製の大きな古いドアから出ていく。"

play music music_happiness fadein 3.0

show bg school_library_ss at center
show yuuko neutral_down_ss at center
with dissolvecharamove



yu "華子ちゃんって大人しい子よね？"




"スタッフがそんな個人的な意見で俺に共感を求めることに驚くべきなんだろうけど、優子さんを知ってしばらく経った後では、それも予想の範囲内だ。俺にとって優子さんは偉い人というより、友達に近い存在なんだ。"






hi "ええ、それがあの子の性格なんだと思います"




hi "だけど最近はすごく自信を付けてきてますよ"


show yuuko smile_down_ss
with charachange



yu "中井くんほど華子ちゃんを知ってるわけじゃないけど、そうね。そう思う。ここで他の人たちと話してる華子ちゃんを見られて嬉しいわ。前はそんなことなかったもの"



hi "ねえ、優子さん……リリーがここを去ったことは知ってますよね？"

show yuuko worried_down_ss
with charachange



yu "何日か前に、本人から聞いたわ。あんなふうにみんなを残して去っていくって、つらいでしょうね"




"優子さんはそう言うと、俺に素早く視線を戻す。たぶん、前にリリーとの関係についてアドバイスを求めたことを思い出したんだろう。"


show yuuko worried_up_ss
with charachange


yu "中井くんはこれから大丈夫？"



"それは……難しい質問だ。もっと差し迫った問題があるので、今はあまりそのことを考えたくない。"




hi "この話、どうも何かがおかしいような、そんな感じがしませんか？"








"優子さんはしばらく考え込む様子を見せながら、上の空でいろんな斬新な形に顔にしわを寄せる。"





show yuuko worried_down_ss
with charachange


yu "そのことを判断できるほど私もリリーのことをよく知らないと思うの"




yu "ごめんね、役に立てなくて"



hi "いやいや、いいですよ。ちょっと口に出して考えてみたかっただけなんです"


"俺は大きくため息をつくと、いらつきながら頭をかく。"


hi "ただ、いろんなことがいっぺんに起こったから俺の手に余っちゃって……なんだか波にのまれてるような感じで"

show yuuko neutral_down_ss
with charachange



yu "きっと、誰だってそういう経験をするものだと思うわ"




yu "大切なのは、自分は何ができないかじゃなくて、自分に何ができるかを見据えることよ。少なくとも、私はそう思う"


show yuuko smile_down_ss
with charachange



yu "そうとでも考えない限り、私も今の人生は乗り切っていけないと思うし"




"笑顔の優子さんは明るい口調でそう言うけど、その言葉は冗談からはほど遠い。優子さんみたいにただでさえ２つの仕事を掛け持ちして、生活費どころか学費まで稼がなきゃいけないのはすごく大変に違いない。"



"優子さんから聞くと他の誰から聞くよりも説得力があるように思える理由は、たぶんそこにあるんだろう。"



hi "それもそうですね"



hi "またしてもアドバイスありがとうございます、優子さん"

show yuuko smile_down_ss:
    ease 0.5 ypos 1.2
with None

show yuuko closedhappy_down_ss:
    ease 0.5 ypos 1.2
with charachange

with Pause(0.2)

show yuuko closedhappy_down_ss:
    ease 0.5 ypos 1.0
    linear 0.5 alpha 0.0 
with charamove


"優子さんは深いおじぎをしてまた笑顔になると、いつも長い時間を過ごしているカウンターの後ろへと戻っていく。"

stop music fadeout 2.0

scene bg school_dormhisao_ni
with shorttimeskip




"部屋の薄明かりの中、かすかに見えるのは俺の手の中にある折り鶴の小さな翼だけだ。カーテンの向こう側やその縁のあたりから、月の光がほんの少しだけうかがい知れる。"





show origami_hand:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with None

show origami_hand:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
show bg school_dormhisao_blurred_ni
with Dissolve (1.0)

play music music_twinkle fadein 10.0


"俺は長いあいだ暗いベッドの中で静かに寝そべり、ぼーっと折り鶴を見上げ続けている。"


"リリーがこれを折ってからたくさんのことが起こったような気もするし、だけど同時にほとんど何も変わっていないような気もする。"



"他のみんなと比べると、俺はまた振り出しに戻ってしまった。人生の進路について新しいアイディアが浮かぶかもしれないけど、そんなもの今の俺にはほとんど影響を及ぼさない。"




"華子は変わった。それはよく分かる。それどころか、以前の彼女の状態を考えたらこんな状態でいる言い訳なんてできるはずがない。華子を見ているとそう思い知らされる。"




"だけど、リリーは……"


"俺は指で鶴の向きを変え、別の角度からそれを見つめる。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve



n "\n\n初めて会った時のリリーは他人行儀で、何だかよそよそしかったような気もする。いつも自分の行動は注意深く、慎重かつ正確で、神経の行き届いた冷静沈着な様子はいつも確かな自信と気品に満ちあふれていた。"






n "やがて、リリーも打ち解け始めた。ほんの少しだけ、でもそれで十分だった。俺に対する警戒を解き、ほんのちょっとだけど自分から心を開いてくれるリリーを見て、嬉しかった。まるで、本当のリリーの姿がだんだん鮮やかに、はっきりとしていくのを見ているようだった。"




n "\nだけど今、俺はそのことに疑いを持ち始めている。"



n "\n俺たち２人が事実上破局した後でそんな疑いが浮かぶのも、きっと分かり切っていたことなんだ。だけどそれは目新しくもないし、奇妙でもない。むしろ昔読んだ本を見つけてほこりを払っているような感じさえする。"




n "リリーと出会ってから、彼女が華子と接するように俺に接しているということにすぐに気がついた。助けや世話が必要な人間に対する接し方だ。初めは、俺はただ学校内の限られた時間に助け合う友達関係でいいと思っていた。"


nvl clear



n "\n\nだけどそのうち、俺にとってリリーとの時間がどんどん大切なものになっていった。静かな散歩の時間から昼食のおしゃべりに至るまで。リリーのいい所がどんどん見えてきて、それがどんどん愛おしくなっていった。"




n "リリーが遠く離れた家族や病気のおばに会いにスコットランドへと姿を消した時、自分がただリリーのそばにいたいと望む気持ちの強さを思い知らされた。リリーも同じように思っていただろうとその時は考えていた。"



n "\nだけど、きっとリリーにとってそれは俺たちの関係の全てじゃなかったんだ。"


n "\n日本に帰国しても、それはリリーにとって、ほんの短時間会うことができた家族を再び失う、ということに過ぎなかった。"



n "晃さんが働きづめだったこともあって、リリーは人生のほとんどを家族から離れて生きてきた。そうするしかなかったんだ。"


nvl clear


n "\n俺は、リリーの独立志向は素晴らしく賞賛に値するとずっと思っていた。心臓発作が起こる前の俺は、認めたくはなかったけど、両親に頼り切っていた。リリーはそんな俺とは大違いだ。"




n "だけどそれは、リリーが決して人を近づかせすぎなかったということでもある。"





n "リリーは、たぶん盲目のせいで家族を失い、同じ理由で慣れ親しんだ学校から転校し、晃さんや周りの人の重荷にならないようにと必死にがんばってきたんだ。"



n "\nそして今、晃さんはインヴァネスに発つ。ちょうどリリーが失ったと感じていた家族と同じように。"


n "葛藤を重ねながら、リリーは決して俺に計画を打ち明けることはなかった。"


n "リリーは誰の重荷にもなりたくなかったんだ。俺も含めて。"


n "\n……俺は、バカだ。"


nvl clear



n "\n疑いもしなかった。俺は、リリーのそばにいようともせず、リリーが望んでいることを聞いたりもしなかった。"





n "俺はただ自分の人生計画を立てて、ずっとその通りになると思っていただけだった。俺とリリーが末永く素晴らしい関係を築き、２人が将来に向けて一緒に歩んでいく、そんなふうに。"




n "\n俺の胸に、自分に対するいらだちと怒りがふつふつと湧き上がる。"





n "\n俺はただ事態を見守っていただけで、リリーを助ける努力すらしようともしなかった。"



n "\nリリーがいてくれるだけで十分だった。それが本当なら、俺はこれからもうまくやっていけると思っていた。"



n "だけど、決して十分じゃなかったんだ。そんなものは、相手の立場を理解しようとも助けようともしない、子供じみた他力本願に過ぎなかった。"



n "そのせいで、俺はリリーを失った。最愛の人を失ったんだ。彼女が俺を必要としていた時に、俺が彼女のそばにいてあげなかったからだ。"

stop music fadeout 5.0

nvl clear
nvl hide dissolve

show origami_hand:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

show origami_hand:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
show bg school_dormhisao_ni
with Dissolve (1.0)

hide origami_hand
with None

window show


"怒りが俺の中でどんどん大きくなっていき、俺は体を回転させると机の上の時計の横に折り鶴を戻す。そこは鶴が俺のために折られて以来ずっと暮らしている場所だ。"


"自分の重荷を自分だけで負う必要はない、そうリリーが言ってくれた、あの日以来。"


"目覚まし時計のどぎつい赤色の数字が、部屋の暗闇を通して俺の疲れた目に照りつける。"


"１０時。夜。門限が近い。"


hi "確か……"


"晃さんは今夜発つと言っていた。"



"飛行機の時間がいつなのか正確には分からない……でも、２人がまだ発っていないという可能性も、ほんの少しだけど、残っている。"





"可能性に突然目を見開いてベッドで上半身を起こすと、アドレナリンが体中を駈けめぐり始める。"





"２人がまだ出発していないという保証はどこにもない。いや、もう出てしまっている可能性が高い。でもまだチャンスはある、ほんの少しだけかもしれないけど。"



"今度こそは、もっと前にすべきだったことを……"

play sound sfx_switch

show bg school_dormhisao
with Dissolve(0.2)

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_friendship fadein 9.0



"俺は立ち上がると収納棚へ駆け寄り、できる限り速く服を引っ張り出すと、間髪入れずそれに袖を通す。"




"過ぎていく毎秒、それはもう２度と取り戻せない。その１秒が、リリーと晃さんに追いつくか、それとも２人を永遠に失うかを決定づけるかもしれない。"



"たとえダメだとしても、俺はやらなきゃいけないんだ。指をくわえたまま黙ってリリーを行かせることなんてできない。こんな時に彼女のそばにいてやらないなんて。"



"全部の服を身につけると、急いで机の上の電話をつかむ。ありがたいことに、地元のタクシー会社の電話番号が通話履歴にまだ残っている。"


show bg school_dormhisao_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)



"無愛想でやる気のない声が、部屋をうろうろする俺に会社の名前を告げる。ゆっくりと、電話越しでもはっきり通じるような声を保つのに苦労する。"


scene bg school_dormext_full_ni
with locationskip



"寮のドアを開けると、冷たい夜風が吹きつけてくる。だけど、それでも俺はきびきびとしたスピードで校門に向かって小走りに駈け続ける。"




"まだ門限にはほんの少し早いけど、もうギリギリだ。もし看守がここにいたら、いろいろ質問されたに違いない。でも看守がちょうど到着する直前か、間近に来たところで、ここを出ることができたみたいだ。"



scene bg school_gardens_ni
with locationchange



"学校の中庭を進みながら、俺のペースは上がっていく。校門に向かって走り始めたとたんに、夜の中庭が持つ魅力は完全に効果を失う。"


scene bg school_courtyard_ni
with locationchange




"中庭の外灯がいつもと同じように淡く光り、俺がつまずかずに走るには十分なくらいの明るさで道を照らす。校舎の方に目をやると、野暮ったい、古くさいとでも言うべき雰囲気をまとっている。"





"思い返すと、前はあの建物がどす黒く俺に迫ってくるように見えたのはおかしな感じがする。今となっては、その古さを除けばほかと同じような、ただの時代遅れ気味な校舎にしか見えない。"



scene bg school_gate_ni
with locationchange



"校門をくぐり抜け、タクシーのすぐそばで足を止める。ちょうど晃さんの車が止まっていたその場所で明るく派手に光るタクシーのサインは、静かな田舎の風景には似つかわしくない。"




"大慌てでタクシーの中に体を押し込むと、うまくいけばリリーと晃さんがいるはずの家の住所を運転手に告げる。"



scene bg shizu_houseext_ni
with shorttimeskip



"腹が立つほどゆったりとした速度で走るタクシーが目的地に到着すると、もう夜もすっかり更けてしまっている。"



"本当にすごい家だ。予想をはるかに超えて圧倒的に大きく、不気味な静けさがただよっている。最悪の事態を恐れ、俺は自分の努力が無駄になった時のためにタクシーの運転手に少し待ってくれるように頼む。"


"門の外にある装飾を凝らしたインターホンのボタンを一度押すと、電子音の短いメロディが静まり返った道路に響く。すぐに、いくらか低めで荒々しい声がインターホンから聞こえてくる。"


mystery "羽加道家だが。お名前と、なぜこんな夜遅くに我々を煩わせるのか、お聞かせ願おう"




"その声にこもるもっともな不快感に内心ビクビクしながら、それでも俺は自分を奮い立たせる。"



hi "中井久夫です。リリーさんと晃さんに会いたいんですが。もしまだこちらにいるなら"




"驚いたことに、俺はインターホンの向こう側の人物を黙らせてしまうほどの力強い声を出すことに成功する。"


show bg shizu_houseext_lights
with Dissolve(0.2)


"数秒が経過する。だけど、何が起きているのか聞くために俺が再びボタンを押そうとするちょうどその時、玄関のドアの明かりがつく。"


"俺は目を凝らして、誰が出てくるのかを知ろうとする。だけど、その人物が釣竿を後ろから飛び出させている大きな車のそばを通ってやって来ると、彼が誰なのかが明らかになる。"



"門までぶらぶらやって来るけど、例によって無表情で無感情だ。そんな態度にも関わらず、わざとらしい振る舞いはまだ子供っぽい。フェンスの後ろにあるいくつかのボタンが押されると、ゆっくりと門が開く。"



show hideaki surprise_ni at center
with charaenter



hh "久夫さん？　こんな所で何してるの？"





"その言葉は、俺が今まで聞いた秀明の声の中で一番感情がこもっているような気がする。今までが無感情すぎただけだけど。"






hi "晃さんが、フライトの前にリリーと一緒にこの家に泊まるって言ってたから"


hi "リリーと話がしたい。最後に少しだけでいいんだ。まだここにいるか？"

show hideaki sad_ni
with charachange


"秀明の表情がすべてを物語る。"



"ダメか。遅すぎたんだ。本当に急がなきゃいけない時だったのに、俺は……"


show hideaki serious_up_ni
with charachange



hh "実は……可能だよ……"



hi "何だって？　どういうことだ？"

show hideaki confused_ni
with charachange


"俺の熱心さに秀明が少したじろぐ。だけどこんな時に興奮せずになんかいられない。"



show hideaki normal_ni
with charachange


hh "ついさっきまでいたんだ。実際には、久夫さんが来るたった数分前までね。今から空港まですぐ追いかければ、もしかしたら……ちょっと、久夫さん！？"


"俺は待っているタクシーに駆け戻りながら、ポケットの中に残されたなけなしの金を握りしめる。"


hi "ありがとう、秀明！"


"そう言い残して俺は座席に座り、間髪入れず運転手に行き先を怒鳴る。"

scene bg city_street4_ni
show crowd_ni
with shorttimeskip

play ambient sfx_crowd_outdoors fadein 2.0


"街路を突進していく俺の胸が激しく鼓動する。そばを行き交う歩行者を避けるように、俺は自分の体をあちらこちらへよじらせる。"



"道路はタクシーや他の車でガッチリとふさがれていた。乗客を降ろしたり、待っている最中には客を乗せたりしていて、俺のタクシーは目的地のほとんど１ブロック手前で止まる羽目になってしまった。"




"だけど、そんなことはもうどうでもいい。今はリリーに追いつくこと、それだけだ。"



"片足が地面を蹴り、もう片足が条件反射的にそれに素早くならう。まるで俺の脚が自意識を持っていて、俺はただ前方の視界のみに意識を集中させているかのようだ。"



"ほんの一目でもいい、彼女のあの長い髪を。長く伸び、見わたす限り広がっていた小麦の穂と同じ色をした、あの金色の髪を。"



"結局、俺は華子と同じようにリリーに頼り切っていたんだ。付き合い始めてからも、リリーが俺のことを本当に頼っていたようには到底思えない。"



"ただ１回を除いては。俺とリリーがあの金色に輝く平原でお互いに固く抱きしめあった、あの瞬間。"


"あの時、リリーは他の人を失ったように俺まで失ってしまうことを恐れていたに違いない。だから、今度こそは……"



"夜の空気が俺を包み込み、俺の体温を全て残らず奪い去っていく。まるで今が夏の夜じゃなく真冬に感じられるほどに。"




"指、手、足……全てがどんどん冷たくなっていく。"




"行き交う群衆が立てる音はもう小さなざわつきにしか聞こえない。歩道を走る俺の足音が大きくこだましているのとは対照的だ。その一歩一歩が、追いつくべき人と俺との距離を縮めている。"




"夜の寒気のせいで胸が締め付けられ、思わず胸の上に手を置いてそれを落ち着かせようとする。"


window hide

scene bg hosp_ext_ni
show crowd_ni
with locationchange

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show



"だけど空港が見えてくる頃、この感触が以前感じたものと同じだということに気づく。"



"今はダメだ……こんな時に限って、頼むから今だけは。"



"俺は痛みをぐっとこらえると持てる力をふりしぼり、自分の体を行ける限り前に押し出す。"



"前へ進むたびに全身から汗が噴き出す。俺の肩が誰かの体にぶつかり、突然頭の中に感情や思い出があふれかえる。"



"俺は謝りもせずに進み続ける。進み続けなきゃいけないんだ。もし止まってしまったら、もう動けるかどうかも分からない。いや、動けたって、間に合わなかったら何もかもが無駄になるんだ。"

with vpunch


"他の人とぶつかり、またぶつかる。そのたびに俺の体が抵抗を受けて小さく跳ね飛ばされる。"



"足がしびれている。腕の感覚もなくなりかけている。胸の痛みのせいで無様に背中を丸める。胸がどんどん締め付けられる。"


window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show


"あの雪の午後……取り返しがつかないほど俺の人生が変わってしまったあの時……岩魚子の姿とあの忌まわしい手紙が俺の頭の中で何度もフラッシュバックする。こんな体のせいで失ってしまった俺の初恋。"


"あんな目にあうのはもう嫌だ。もう俺の身がどうなろうと構わない。最後に一度だけでも、リリーに会わなきゃいけないんだ。"


"……あそこだ！"

scene ev lilly_airport
with flash




"少し離れた道の先に、金色と白色がわずかに見える。空港の入り口を照らすライトで彼女の姿がくっきりと浮かび上がっている。"





hi "リリー！　リリー！"


hi "リリー！　待ってくれ、頼む！　リリー！"


"どうしたんだよリリー。俺知ってるぞ、リリーの耳が普通の人よりはるかにいい――"

scene bg hosp_ext_ni:
    xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
show crowd_ni:
    xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
with vpunch

play sound sfx_impact


hi "うぐっ！"




"突然俺の視界がコントロールを失ってぐるりと回転し、地面に落ちる。体が誰かにぶつかってよろめいた後、無造作に倒れ込んでいた。"


window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show



"受けたダメージを見極める間もなく、俺の体に信じられないような激痛が走る。頭の中が真っ白になり、体を丸めながら必死になって胸をかきむしる。"



mystery "おい、大丈夫か？　ひどい倒れ方だったぞ"



"この痛み……耐えられ……"



hi "ぐうっ……がああああああ！"

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show



"強い衝撃は命取り。体の酷使も同じ。今度だけは自分の限界を越えられると思っていた……"




mystery "この人、様子がおかしいぞ！"

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show


mystery "どうしたんだ、大……"

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

with Pause(0.7)

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show


"俺に群がる人たちの声がだんだんと大きな耳鳴りに変わっていく。今の俺はもう頭を動かすことができない。俺の目は群衆の口が音もなく動くのを見上げている。"

window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

with Pause(0.15)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

with Pause(0.05)

play sound sfx_heartstop
show heartattack alpha
with Dissolve (0.1)

stop ambient fadeout 0.3

show heartattack residual
with Dissolve (0.8)

window show



"自分の胸をつかんではいるけど、もう指も足も感覚が残っていないことに気づく。まるで体中のスイッチが手足からどんどん切れていくみたいだ。"


scene ev lilly_airport_end:
    truecenter
    zoom 1.2 rotate -8 subpixel True
    easein 12.0 zoom 1.0 rotate 0
with slowfade


"俺は最後のあがきで、道の先、俺に光を投げかけている空港入口のほうへと頭を向ける。"



"あそこにリリーがいる。人ごみの向こう側に。彼女が頭を傾ける。ほんの少しだけど。"

show passoutOP1
with None


"視界がぼやけていくのを感じる。俺は叫ぼうとして、だけどどんなにがんばっても口からは何も出てこない。ゆっくりと、だけど確実に、目の前の光景が暗くなっていく。"


"そう……これが結末だ。"




"ダメだったんだ。もう少しだった。ほんのもう少し、だけど最後の最後で、俺の病気が新しい人生へのチャンスを取り上げて、俺を引きずり戻してしまった。"





"これから俺は死ぬんだ。空港からほんの数メートルしか離れていない所で這いつくばり、ざわめく群衆に囲まれ、そしてリリーは俺の目と鼻の先でスコットランドへと去っていく。"



hi "リ……リー……"

stop music fadeout 4.0


"最後の力をふりしぼって発した最期の言葉。全身の力が抜けていき、世界が逃れられないほどの深い暗闇に覆われていく。"


"ごめんな、リリー。"


"俺、遅すぎたんだ。"

scene black
with dissolve



label jp_L31:

scene white
with dissolve



"……"


"…………"


"………………"


"何が……起こってるんだ……？"


"ゆっくりと目を開けると、明るい白色光が俺の網膜に差し込んでくる。"




"ただしばらくその場に横たわり、ゆっくり覚醒していく頭の中で断片的な考えが一つにまとまっていく間、俺はなんとなく前を見つめる。"


show bg hosp_ceiling:
    alpha 0.0
    linear 5.0 alpha 1.0
with None


"ゆっくりと、だけど確実に、俺の視界いっぱいに空間が広がり始め、見つめていた白色にも焦点が合い始める。"


"照明器具が視界に入った時に初めて、俺はそれが頭上にある天井だと思い当たる。"

scene bg hosp_room2
with locationchange



"ゆっくりと起き上がり、自分が今いる部屋の詳細へと全ての意識を静かに集中させる。"




"強い消毒液の臭いが立ち込めていて、普通の場所にしては清潔すぎるという印象をこの場に与えている。"





"当たり障りのない薄い桃色の壁は、ひび割れも汚れもむらもなく完全に塗装されている。額縁に入った１枚の絵が全く傾くことなく飾られている。壁と同じように、それはこれ以上ないくらい退屈で無害な代物だ。"




"俺の注意が視界を横切る半透明のカーテンへと引きつけられ、そのカーテンに覆われている開け放たれた窓が俺の目をとらえる。"



"窓の外を見るために右腕を動かして起き上がろうとした時、カテーテルがめり込んで不快感を覚える。その時初めて俺は、頬を伝い鼻の中に差し込まれているチューブの存在にも気づく。"



"いくらかバタバタしながら、俺は窓の端っこあたりが見えるくらいの位置に体を持っていく。"

scene ev lilly_hospitalwindow
with whiteout



"眼下では、いくつかの大木に茂るたくさんの葉の向こう側に、自然の風景が背後の平原まで続いている。街の郊外にある、お決まりな緑の孤島だ。"





"外に見える太陽から察するに、今は真昼だ。だけど、何日なのかはよく分からない。"


"じゃあ……俺はまた病院にいるってわけか。"



"俺は散らばった思考を集めようと、長い疲労の息を吐き出す。俺の心は同時にあっちこっちに飛び、たくさんの感情が俺の中を駆け回る。"



scene bg hosp_room2
with locationchange


"ゆっくりと再びベッドに体を横たえた後、俺はもう一度最初から始めてみることにする。なぜ俺はここにいるのか。"


"記憶をさかのぼるけど、何が起こったのかをスムーズに思い出すことができない。昨日の夜の出来事……いや、いつかわからないけど、夜……の、順序だった記憶というより、断片的な光景の連続が呼び戻される。"

scene bg school_dormhisao_ni_fb
show origami_fb at center
show noiseoverlay
with flash


"ベッドに寝そべって、折り鶴を見ている。"

scene bg shizu_houseext_lights_fb
show hideaki serious_up_fb at center
show noiseoverlay
with flash


"羽加道家の外で秀明と話をしている。"

scene bg hosp_ext_fb
show crowd_still1_fb at center
show noiseoverlay
with flash


"道を走り、歩行者とすれ違い、次々とその人たちにぶつかっている。"

scene bg hosp_ext_fb:
    xalign 0.5 yalign 0.52 rotate -6 zoom 1.2
show crowd_still2_fb:
    xalign 0.5 yalign 0.52 rotate -6 zoom 1.2
show noiseoverlay
with flash


"倒れる。"

scene ev lilly_airport_end_fb
show noiseoverlay
with flash


"焼けつくように明るい空港入口を見上げて、道路に這いつくばりながらリリーの背中を見ている……"


"……"

scene bg hosp_room2
with fade



"突然、俺は個室の静けさに圧倒される。"



play music music_rain fadein 2.0

window hide
nvl clear
nvl show dissolve



n "そうだ。俺は自分の過ちを取り返すチャンスを得て、そしてそれをふいにしてしまった。"





n "薬を飲むのをさぼり、無理をしないという言いつけを守らなかったのがいけなかったのか、それとも俺の体がこんなにすぐにへばったせいなのか、そんなことは今ではもうどうでもいい。"



n "重要なのは、俺はまた独りになったということ、それだけだ。"


n "再びベッドに体を戻すと、パステル色の青い枕がほとんど抵抗なく俺を受け入れる。パリッと糊の効いた枕カバーやシーツは全然快適じゃない。"



n "昨日の夜の出来事の真っ暗闇と比べたら、俺の周りに差し込むこの部屋の明るい光はとても鮮烈だ。だけどそれも、ここがいかに隔離された世界であるかを強調しているに過ぎない。"



n "\n不整脈。"



n "\n妙な言葉だ。耳慣れない、知らない言葉。お近づきにはなりたくない言葉。"


n "まれに起きる病気で、心臓の動きが不規則になり、ときには鼓動が極端に速くなる。場合によっては致命的だ。"

nvl clear


n "\n『今まで何の問題もなく過ごせていたのは奇跡的だ』と言われた。"



n "そして、それは起きた。俺の病気は、俺から全てを奪い去った。以前通っていた学校はもう重要な場所じゃなくなった。俺の家もはるかに遠のいてしまった。友達も初恋の人も、しばらくしたら来なくなった。"




n "俺はひがみっぽく怒りっぽい人間になった。よそよそしい、冷めた人間に。自己弁護するわけじゃないけど、誰だってこんなことが起こったらそうならないわけがない。ともかく、病院を退院した時の俺は完全に人が変わっていた。"




n "状況は変わった。華子、静音やミーシャと友達になった。寮を『我が家』と新たに感じるようになり、科学や身の回りの世界に対して新たな興味もわき、そして、今まで考えたこともなかった人生の進路も見つけた。"



n "\nだけど、他にも発見したものがあった。"




n "山久やその周囲の隔絶感は嫌いじゃなかった。その静けさのおかげで他では得られないような穏やかな気持ちになった。でも一方で、この一帯が人から追いやられているような、人目から遠ざけられているような気分にもさせられた。"



nvl clear


n "\n\n通りを行く人たちは時々いぶかしげにこちらを見たり、じろじろ見ている自分に気づいて慌ててそっぽを向いたりした。俺の病気は目には見えないけど、俺の制服はそれを表に示していたんだ。"



n "たとえそんなことがなかったとしても、それでも俺は以前とは違っていた。毎日、朝、昼、晩、１７錠の薬を飲んだ。俺の服の下に隠された傷跡は、ずっと消えることのない病気の証だった。そして何より、自分が本当に死ぬという可能性が現実のものになった。"



n "ひどい転倒。うっかり背中を強く打ち付ける。単純な短距離走でやりすぎる。俺の心臓はどんなきっかけでも止まっていたかもしれない。実際、細心の注意を払っているにも関わらず、俺は何度か死の淵に瀕した。"



n "\nでも大したことじゃなかった。そのくらいなら耐えられた。"




n "なぜなら、最後に見つけたものがあったから。いや、山久に転入してから再発見したと言ってもいい。"



n "\nそれは、俺の眼の前から再び奪い取られてしまったもの。"


nvl clear


n "\n俺が新たに見つけた幸せがいかに繊細なものだったのか、今になってようやく気づく。全て彼女に依存していたんだ。陰うつで、戸惑い、目的もない、そんな転校生だった俺が最初に山久に来てから、ずっと俺の人生のかなめだった彼女。"



n "砂藤リリー。彼女こそ、俺が他の誰よりも頼りにできた人、そして俺の抱いた愛情に報いてくれた人だった。だけど、俺は彼女を失った。それに気づくのがただ遅すぎた。"





n "俺はただ自分の人生の計画を立てて、いつまでもその通りに進んでいけると思っていた。でも現実はそんなに甘くはない。俺はようやくその言葉の意味を知った。でも気づくのが遅すぎたという事実を前にして打ちのめされるだけだった。"





n "……"




n "今いる環境は、あまりに見慣れたものだ。まるで山久はただの夢に過ぎず、まだ最初の深刻な心臓発作の治療が続いているかのように思える。"






n "こんなに疲れた感じがするのはそのせいかもしれない。たった数分の間に、自分の人生の最後の数ヶ月をまるごと生きてきたんじゃないかという気さえする。"



nvl hide dissolve
nvl clear

scene black
with shuteye

window show




"まぶたが重くて、目が閉じていく。身も心も疲れ切っている俺は、それに抵抗することができない。"


window hide
with Pause(1.0)
with shorttimeskip
with Pause(1.0)
window show


"ベッドの上からブツブツ聞こえてくる意味の分からない話し声が、俺を眠りから呼び覚ます。"




"目を閉じたまま意識を集中し、たぶん看護師であろう誰かが、医者に別れを告げているのを聞く。"



scene bg hosp_room2
with openeye



"目を開けると、視界の端でドアが閉まるのに気づく。"


"医者が立ったまま、手元のクリップボード上のメモを読み、慎重にカルテに目を通している。"


"明らかにすごく重要そうな書類を精読した後、その医者は顔を上げて俺の視線に気づく。その瞬間の医者の表情や態度にほんの少し妙な点があるような気がするけど、俺はその正体が何なのかはっきりとつかめない。"



"医師" "ああ、目が覚めたんですね……中井さん"





"医者がベッドの端をちらりと見て、俺の名前を確認する。つまりカルテには俺の名前が書かれていなかったってことだ。"




"医師" "ちょっと残念でしたね。ついさっき、寝ている間にご両親が来てたんですよ。もしよかったら、目を覚ましたとご両親にお伝えしますよ"




hi "ええと……どうも。そうしてもらえると"




"自分で何を言っているのかちゃんと考える前に、ちょっとぼんやりした返事をする。でもおそらく、彼が期待していただろう返事だ。"





"医師" "もちろん"




"医師" "もし聞きたいことがあったら、何でも聞いて下さい。でも休んでいたければそれでも構いません。あいにく、まだしばらく麻酔が効いていますからね"




"麻酔か……そりゃそうだ。最初に起きた時にすごく妙な気分だったのは、きっとそのせいだ。"



"チューブが外れたり、これ以上余計に気分が悪くなったりしないように気を付けながら、ゆっくりと頭を振る。それに応えるかのように、医者がクリップボードを丁寧に置く。"




hi "聞きたいことは……そうですね、実際何が起こったんですか？"




"医師" "簡単に言ってしまうと、残念ながらあなたはまた心臓発作を起こしたんです。最初のものほどひどくはなかったんですが、病院のすぐ近くで倒れたのは不幸中の幸いでした"



"医師" "容体が安定してから、手術室に移送して鍵穴手術を行い、一時的にペースメーカーを埋め込みました"




"医師" "かいつまんで言うと、発作は２日前に起きて、その後すぐに緊急処置が行われました。それからは、眠っている間ずっと経過を見守っていたというわけです"



hi "俺は大丈夫なんですか？　後遺症が残ったりするんですか？"



"医師" "最初の心臓発作の時に行われた一連の処置に比べたら、今回のは比較的軽いものでした"




"医師" "合併症が起きなければ、数日後にもう一度手術をしてペースメーカーを取り外すことになります。しかし後遺症が残ることはないでしょう"




"医者は話を続け、話題は不整脈と薬の処方に関する話に移っていく。もうほとんど知っていることの繰り返しだ。関心があるふりをしてうなずき始めるけど、俺の心は宙をさまよう。"




"医者の肩越しに見える壁上の無害な絵がどれだけ完璧に掛けられているか、医者自身さえも含んだ俺の周りがどれだけきちんとして無味乾燥か、そんなことを考え始める。"




"医師" "もし私の話が退屈だったら、遠慮なく言ってください、中井さん。どうも私は脱線してしまうところがあって"





"医者が自虐的な冗談を言って軽く笑う。思ったよりも悪く受け取られてしまった俺は決まり悪く顔をしかめる。"



"だけど考えてみると、その医者の笑い声は山久学園のナースのとは違っているように聞こえる。その理由を考えてみて、俺はなぜ目の前にいる人物が少し『遠い』ような気がするのかに気づく。"



"医者の笑顔は整然としていて、無味乾燥なんだ。完璧なタイミングでちょっとした冗談を持ち出し、それにお決まりの、当たり障りのない笑い声を加える。"





"まるで、名前がきちんと印刷された名札をつけた白衣の人物と話しているというよりも、全ての動きが事前に演出された、稽古ずみの台本を読んでいる役者と話しているだけのように感じる。"






"だけどきっと、医者としてはそうならざるをえないんだろう。"




"ガンが全身に広がっている少女とおしゃべりする時も、出産で命を落とそうとしている女性を安心させる時も、他のどんな末期患者や危篤状態の患者と接する時も、整然とした無味乾燥な笑いを保たないといけない。"




"こういうちょっとした距離を。こういうちょっとしたよそよそしさを。"



"俺は辛辣すぎたんだろうか。こんな態度を身につけるのはこうした職業の人たちだけでは決してない、と思えばなおさらだ。"









"俺が愛したあの人も、結局同じように他人から距離を置き続けていたんだ。"


"俺は再び医者を見上げ、自分がしばらくのあいだうつむきながら考え事をしていたことに気づく。"



"医師" "まだ疲れているでしょう。大変なことがあったし、さっきも言った通り、まだ麻酔が効いているでしょうから"




"医師" "もしよかったら、少し休んでください。目が覚めたことは私からご両親にお伝えしておきます"



hi "それが……いいですね。ありがとうございます"

stop music fadeout 6.0



"医者はそっけなくうなずいてクリップボードを手に取ると、部屋の隅にある白い大きなドアへと歩いていき、部屋を出て鈍い音とともにドアを閉める。"



"結局、俺はまた独りだ。"



"リリーは去った。晃さんも去った。華子は旅行中だろう。俺の両親さえ、もう病院を出た後だ。"




"四方を桃色の壁に囲まれ、頭上には白い天井。外の世界へと目を向けるために開け放たれた１枚の窓。"





"過去が自分の周りに押し迫っている。小ぎれいさや無味乾燥さや糊や消毒液の臭いにとらわれて閉所恐怖症になりそうだ。そんな時に、未来を考えることなんてできない。"





"何をすればいいのか、何に向かえばいいのか、分からない。俺は山久がそうだったのと同じく、この何もかもが全部夢だったかのように、眠って時を過ごすことにする。"

scene black
with dissolve


label jp_L32:

scene white
with dissolve


"白。"


"無味乾燥で清潔な部屋の、無味乾燥で清潔な白。"

$ renpy.music.set_volume(0.05, 0.0, channel="music")
play music music_musicbox fadein 10.0

show bg hosp_ceiling:
    alpha 0.0
    linear 5.0 alpha 1.0
with None



"俺は目を覚まし、ただしばらく天井を見つめている。天井に掛かったラック据え付けのテレビと同じ程度には、面白い。"





"事実、両親がここにいた間、テレビはつけっぱなしだった。両親が俺の意識回復を待つ間、ずっと音は消してあった。俺が最初に入院する羽目になった時とまるで同じ、新味のない行為だった。"





"さっき、部屋に来た看護師が心電図のスピーカーをオフにしようかと言ってくれた。俺はそれを断った。ただ単に、今の俺にとってその音の存在がごく自然なものだからだ。"



"それはある意味、快適ですらある。メトロノームのように規則的なリズムは、少なくともこんな場所でも時間が過ぎているという感覚をいくらかは与えてくれる。"



"だけど、完全に目が覚めてしばらくその電子音に耳を傾けていると、部屋の中に違う音が流れていることに気づく。"


$ renpy.music.set_volume(0.1, 5.0, channel="music")



"全ての意識を聞くことに集中させる。邪魔をするものもないので簡単だ。すると、小さな小さなメロディーが聞こえてくる。"



"軽快で静かで、その音楽は心電図のパルスにほとんどかき消されてしまうほどに繊細だ。"

scene bg hosp_room2
with locationchange



"体に取りつけられたセンサーやチューブ類が外れないようにほんの少しだけ頭を傾けて、その旋律の出所を見ようとする。そしてベッド横のナイトテーブルに小さな木箱が置かれているのに気づく。"


$ renpy.music.set_volume(1.0, 1.0, channel="music")

show musicbox open:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)




"箱の中で金色の小さな金属ドラムがゆっくり回るのを静かに見守りながら、俺はほんの少し口を開く。表面にあるいくつもの小さな突起が少しずつ動き、やがて視界の向こう側に消えていく。"





"このオルゴール……俺がプレゼントした……"

show musicbox open:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide musicbox
with None


"ドアの開く音がして、物思いにふける俺は我に返る。誰が入ってくるのか見ようと視線を向ける俺の頭と心臓は依然冷静なままで。"



"褐色のロングスカート……桃色のオフショルダーニット……青白い、まるで陶器のような肌……青い曇った目、そして長い金色の髪……"




show lilly basic_reminisce_cas at center
with charaenter



"リリーは壁に指を軽く滑らせて行く先を測りながら、ゆっくりと部屋の中に入ってくる。俺はその姿を見つめることしかできない。そして思考が打ち震えるように停止する。"



hi "リ……リリー……？"

show lilly basic_oops_cas
with charachange


"リリーが途中で歩みを止め、体中をこわばらせる。"


li "久夫さん？　久夫さんなの？"


"穏やかな憂いを帯びた声。それがリリーの感情を反映する。"


hi "俺、リリーはてっきり……"

show lilly basic_sad_cas
with charachange


"リリーが恐る恐る一歩を踏み出す。それからもう一歩。まるで彼女自身ためらっているかのように。"

show lilly basic_sad_cas_close
with characlose


"だけどその自制もむなしく、最後の抵抗が崩れ去り、ついにリリーは俺が横たわる場所へと駆け寄る。"

$ ksgallery_unlock("unlock_ev lilly_hospitalclosed")
scene ev lilly_hospitalclosed at l_hosp_out
with whiteout



"リリーが俺にしがみ付き、うずくまる彼女の頬に涙が伝い始める。俺は少し驚いてしまう。ほんの数分前までは、地球の反対側にいると思っていたのに。少しためらった後、俺はリリーの柔らかい肩に右手を乗せる。"





li "久夫さん！　久夫さん！"


"紺色のシーツに涙のしみを作りながら、リリーが体を震わせる。丹念に保たれている風貌を通して彼女の感情があふれ出す。"



"今ではより近くなったリリーの顔。窓から差し込む日の光を受けて青白く輝いているのがよりはっきり見える。俺は彼女の頬がいつもより赤く染まっているのに気づく。"



hi "大丈夫だよ、リリー。大丈夫だから。そんなに――"


$ ksgallery_unlock("unlock_ev lilly_hospital")
show ev lilly_hospital at l_hosp_out
with charachange



"リリーがすぐに体を起こす。悲しみと負けん気を潤んだ瞳に残したまま、ぐっと涙をこらえている。いつも一目置かれていた彼女のその気高い性質が、俺をたじろがせる。"



li "心配するな、なんて言わないで、久夫さん！"



li "今はただ……泣かせて……"



"俺は言葉を失う。返事を待っていたリリーは、だけど数秒もしないうちに再び冷静ではいられなくなる。"


show ev lilly_hospitalclosed at l_hosp_out
with charachange


"リリーがベッドの上で泣き続けるあいだ、俺はのどを激しく鳴らして気持ちを落ち着けようとする。安堵と憂うつが混ざった妙な気持ちがこみ上げてくる。"



"リリーが……ここにいる。本当にここにいるんだ。もし彼女の肌を手の中に感じていなかったら、自分の目だって信じられなかっただろう。"
"俺の努力は無駄じゃなかった。またしても俺の大切なものを奪おうとしたこの体の試みは、失敗に終わったんだ。"




"でも、今は……思っていたほど幸せな気分じゃない。"



"リリーがここにいて、こうやって俺のために泣いている……彼女を愛するようになってから、いや退院以来ずっと、こうなることだけは避けたいと思っていた。"



hi "ごめん、リリー。ここに入院したのは俺自身のせいなんだ。無理しすぎちゃいけなかったんだ"


"俺は自嘲気味に鼻を鳴らす。"



hi "誰にも心配かけないようにって、何か月も気をつけてきたのに、その後でこんなことをしでかして。俺ってほんとにバカだよな"




scene bg hosp_room2
show lilly basic_weaksmile_cas_close at center
with whiteout


"何度か鼻をすすって深呼吸をすると、リリーは自制を取り戻してほんの少し冷静になる。"


"赤い頬、潤んだ瞳や涙の跡は今でも見て取れるけど、リリーは細心の注意を払って弱々しい笑顔を作る。俺によく見せてくれた気がするあの笑顔を。"


li "自分を責めないで。私を追うために走っていて発作が起きた、と後で聞かされました。そうなんでしょう？"


hi "それでも……"


"リリーが手の甲で目を拭う。彼女の溢れ出る感情はだんだん落ち着き、いつものリリーに戻っていく。"

show lilly basic_reminisce_cas_close
with charachange


li "久夫さん、どうして私を追いかけたの？"

show lilly basic_concerned_cas_close
with charachange


"俺は答えようとして、こわばるリリーの表情に気づく。"


li "さよならを言った後なのに、そして私は山久学園を去ったのに……"



"リリーは一呼吸置いて、気持ちを落ち着かせる。また感情が爆発しそうだ。"



hi "俺はただ、謝りたかったんだ"

show lilly basic_surprised_cas_close
with charachange


li "謝る？"


hi "リリーが俺を必要としていた時、そばにいてあげられなかったから"


hi "今まで、俺はただリリーがそばにいてくれるだけで十分だった。ただ一日をいい気分で過ごすためだけに、リリーが俺の横にいてくれることを望んだんだ"


hi "俺の体はこんなだけど、リリー、俺は君の力になりたい。リリーが誰かを必要とする時、そばにいてあげたい"

show lilly basic_weaksmile_cas_close
with charachange


li "だけど、いつもそばにいてくれましたよ、久夫さんは……"


hi "リリー、どうしてスコットランドに行きたかったの？"

show lilly basic_sleepy_cas_close
with charachange



li "どうして……？　前にも言ったでしょう。姉さんも行くのだし、家族も私を呼びよせているから"



hi "どうして自分が行きたかったからって言わなかったんだ？"


show lilly basic_oops_cas_close
with charachange


li "私――"


hi "いつもの俺は強情じゃない。でも、今回だけはそうじゃなきゃいけないんだ。リリー、ここにいてほしい"


hi "俺はリリーに、リリーのよく知ってる人たちがいる場所、リリーの夢と希望がかなう場所にいてほしいんだ。もしここにいることを選んでくれるなら、俺はもう絶対リリーのそばを離れない。誰ひとり失わせやしない"


hi "俺が心臓発作に襲われた時、俺の知ってる全ての人、全ての場所が奪われたんだ。山久に来た俺に、リリーは新しい人生を見せてくれた。俺は過去を失ったけど、リリーは俺に未来を見せてくれた"



hi "確かに、いつもリリーのそばにいてあげられたわけじゃなかった。俺は頼りなくて、時々嘘だってついたし、自分自身のことだって理解してないのに、そのうちリリーを理解できるようになるって思い込んでた"




hi "とにかく、俺のほうからもリリーに未来をあげたいんだ。リリーのためにそばにいて、重荷も幸せも一緒に分かち合いたい。北海道で約束したみたいに"



hi "信じてほしい。俺が心臓発作を起こして知り合いをたくさん失った後、リリーのことをなかなか信用できなかったのは自覚してる。でもそのおかげで人を信用できないことがどれだけ惨めかが分かるんだ"



hi "だから俺は、リリーがこんなふうに全てを捨ててしまうのをただ見てることなんてできない。絶対に俺と同じ思いをしてほしくないんだ。それを止めるためなら俺は何だってするよ"


show lilly basic_weaksmile_cas_close
with charachange


li "久夫さんって、一度そうと決めたら本当に意固地なんですね？"


hi "言っただろ、いつもじゃないよ"



"だけど、俺の弱々しい笑顔も点滴針が少し腕に食い込んで消えてしまう。その不快さが、自分がこの病気に束縛されているという事実を思い出させる。"


show lilly basic_concerned_cas_close
with charachange



"俺が痛みに小さな声を上げると、リリーの表情がこわばる。それを見て即座に、自分がもっと我慢強ければ良かったのにと思う。俺は打ちひしがれてため息をつくことしかできない。"



hi "俺は退院してから、いつだって誰にも心配かけないように気を付けてきたのに、最愛の人が俺のために泣くことすら止められないんだな"



hi "やっと自分の思いを言葉にできたとしても、こんな体じゃ自分がほとんど役立たずに思えるよ"




hi "何かに近づこうとすると、それはいつも奪い去られてしまう。今だって、事態が好転したのはただ単に運が良かったってだけだ"




hi "たぶん、そのことについても謝らなきゃいけないな。俺はリリーに心配をかけることしかできない。今だって俺が満足な生活を送れる可能性はほとんどないだろうし"




"リリーの暖かく柔らかい手が俺の左頬を伝うのを感じて、俺は頭を上げる。彼女が俺に触れながら浮かべている笑顔は、優しくて温かい。"


show lilly basic_smileclosed_cas_close
with charachange



li "久夫さんがそう言ってしまうのも無理はないと思いますよ。久夫さんはいつだって真摯で、自分のことをよく考えていますからね"


show lilly basic_smile_cas_close
with charachange



li "それに控えめで温厚で、華ちゃんに対しても寛容すぎるくらい、それでいて何に対しても、誰に対しても好奇心旺盛で"



show lilly basic_weaksmile_cas_close
with charachange




li "家族と過ごしていた時、久夫さんがいなくて寂しいと言いましたけど、あれは冗談でも誇張でもなかったんですよ。あなたへの想いがずっと心の中にあって、それがあの時の励みになりました"



show lilly basic_reminisce_cas_close
with charachange



li "だから家族が私を呼び戻そうとした時、どうすればいいのか分からなかったんです。決心がついたと思った後でさえ、久夫さんが私の決心を変えるために全力を尽くそうとして"


show lilly basic_weaksmile_cas_close
with charachange



li "私が告白したのは同情心からではないし、本当のあなたは違うだろうと信じ込んだからでもありません。あなたを決して失いたくないから。どんなことがあっても、いつも私の人生の一部でいてほしいと思うから"



show lilly basic_smileclosed_cas_close
with charachange


li "久夫さん、あなたはとても美しい人。それは心臓がどうであっても何も変わりません。だからお願い、もうこれ以上あなた自身のことで謝らないで"



"長い間、沈黙が部屋の中を支配する。"



"俺の中で新しく生まれている感情。これが何なのか、俺にはよく分からない。でも、リリーのいつもどおりの温かくて優しい笑顔を黙って見ていると、そんなものはどうでもよくなってしまう。"


"リリーが俺の頬に親指を這わせ、一粒の涙を拭きとる。その時俺は気づく。これこそ、俺がずっと望んでいたものなんだ。"



"俺は生まれて初めてと思えるほどの、心の底からの満面の笑みを浮かべる。リリーは手の平でそれを感じ取ると、俺に笑顔を返してくる。"



"俺たちのどちらも口を開かないまま、時間が過ぎていく。俺たちのどちらも、自分の感情を言葉で相手に伝える必要はないんだ。"



hi "いつもリリーのそばにいるとか、永遠に一緒にいるとか、そんな約束できないのはわかってる"



"俺は少し苦労しながら自分の手を持ち上げ、リリーの青白い肩の上にそれを乗せる。"


hi "だけど……少なくとも来年の七夕祭りに連れて行くことはできると思う。今年の七夕祭りを逃した代わりにね"

show lilly basic_emb_cas_close
with charachange




"リリーは驚いたような表情を見せる。無理もないけど。"






li "覚えて……いてくれたの？"


hi "記憶力には自信があるんだ。たまにはね"

show lilly basic_giggle_cas_close
with charachange



"リリーは頭を少し上げると俺の頬から手を離し、小さく、おかしそうにクスクスと笑う。ほとんど女の子らしい軽快な笑いがいかに本気かを見て、俺はうっかり笑みをこぼす。"


show lilly basic_cheerful_cas
with charadistant


"温かい笑顔を保ったまま、リリーは落ち着きを取り戻し、俺の胸に手を当てながら背筋を伸ばす。"


"俺はリリーと初めて会っているような錯覚を覚える。ちょうど、彼女がお茶を飲んでいたあの部屋に俺が初めて入って行った時と同じように、リリーの背後で窓から差し込む日差しが輝く。"


show lilly basic_smile_cas
with charachange



li "大変結構です。では、来年の七夕祭りは一緒に行くという誓いを交わしましょうか？"



"俺は同意してうなずく。たとえリリーにはそれが見えないとしても。"


hi "誓います"

show lilly basic_smileclosed_cas
with charachange


li "誓います"

window hide

stop music fadeout 4.0



label jp_L33:

window hide None

play ambient sfx_parkambience fadein 6.0

scene bg lilly_hilltop
with Dissolve(3.0)

play music music_lilly fadein 5.0

window show




"晃さん、リリー、そして俺は、町を見下ろす草の生い茂る土手で静かに座っている。雲ひとつない青空を、そよ風が優しく吹き抜ける。"





"町から歩いてもたぶんほんの数分しかかからない、町のすぐそばにある丘。だけど、そこの景色は完全に想像以上だ。"


show lilly basic_smileclosed_cas_close:
    left
    ypos 1.1
with charaenter


"リリーは俺のそばに座って、目を閉じている。優しいそよ風が彼女の髪を揺らす。"


li "素敵な場所ですね"


hi "ああ。山久のそばにこんな場所があったなんて全然知らなかったよ"

show akira basic_ending_close:
    right
    ypos 1.1
with charaenter


aki "そしてもちろん、見つけたのはあたしだけどな"


"そう言う晃さんの笑顔は真摯なものだけど、声の調子がいつもの屈託のない晃さんと少し違う。"

show akira basic_smile_close
with charachange


aki "でもさ、退院できてよかったな、久夫"


hi "誰よりも俺自身が一番うれしいですよ。もう病院はこりごりです"



aki "それじゃ、２人とも明日学校に戻るんだな？"


$ doublespeak(hi, li, "ええ", "ええ")

show akira basic_ending_close
with charachange


"晃さんが愉快そうに声を上げて笑い、それから下方に広がる街へと視線を戻す。建物の間に立っている木々が風を受けて揺れる。"


hi "夏休みに一緒に北へ行けなかったのは残念だけど。それから七夕祭りも"

show lilly basic_weaksmile_cas_close
with charachange



li "心配しないで。また次の機会はあるから"



show akira basic_smile_close
with charachange


aki "次の夏休み前には２人とも卒業してるんだろ？"


hi "ええ。でもほら、その後も大学がありますから"


aki "同じ所に行くのかい？"

show lilly basic_smile_cas_close
with charachange



li "そうなるでしょうね。私たち２人とも、入学に必要な成績は十分満たしていますから"



hi "自信たっぷりだな……"

show lilly basic_cheerful_cas_close
with charachange


li "心配しないで。ほとんどの教科で久夫さんの方が成績がいいのだし"



hi "まあ、そのうち何とかするよ"


show akira basic_laugh_close
with charachange



aki "それでいいのさ。山久にいるうちは、ただ楽しみなよ"


show lilly basic_weaksmile_cas_close
with charachange


"晃さんが俺たち２人と隔てられてしまったことを悲しんで、リリーがため息を漏らす。"

show lilly basic_reminisce_cas_close
with charachange


li "やはりスコットランドに戻らなくてはならないの？"

show akira basic_resigned_close
with charachange



aki "ああ。今だってもう会社の連中があたしに復讐するつもりでいるよ"




hi "こんなに長くいる予定じゃなかったってことですか？"

show akira basic_ending_close
with charachange


"いつもの晃さんらしい大きな笑顔が浮かぶ。"


aki "彼氏のパスポートを用意するのに時間がかかってさ"



hi "彼氏さんも一緒に連れて行くんですか？"


show akira basic_smile_close
with charachange



aki "最初は少しの間だけな。びっくりするぐらい世渡り上手な奴だから、たぶん大丈夫だと思うよ"


show akira basic_lost_close
with charachange


"晃さんが愉快そうに鼻を鳴らす。"


aki "もしあたしたちの父親が分からず屋だったら、あたしもとっくにここを去ってただろうな"


show akira basic_laugh_close
with charachange




aki "だけどほんのもうちょっとの間、かわいい妹と一緒にいられる口実を利用しないわけにはいかなかったのさ"


show lilly basic_smileclosed_cas_close
with charachange


"晃さんが右に体を傾けて、ふざけた様子でリリーを固く抱きしめる。リリーにとってそれは大きな励ましだ。"




li "だけど、最後にまた姉さんと過ごせてよかったわ"




hi "別に興味ないかもしれませんけど、俺も全く同じ気持ちですよ"


show akira basic_smile_close
with charachange


aki "へえ、２人ともありがとな。そのうち帰ってくるようにするから、心配するなよ"


show lilly basic_reminisce_cas_close
with charachange


li "姉さんのお仕事がとても忙しくて、残念だわ"

show akira basic_lost_close
with charachange



aki "残念だけど、会社がひとりでに立ち行くってことはないのさ。それは向こうでも全く同じだと思うよ"



show akira basic_smile_close
with charachange


aki "それを考えたら、あたしもそろそろ行ったほうがいいな"


hi "晃さん、向こうでも楽しい生活を"

show akira basic_laugh_close
with charachange


aki "はは、そうだな"

show akira basic_smile_close at right
with dissolvecharamove


"わずかなうなり声とともに、晃さんが地面に手をついて立ち上がりながら体を払う。"


show akira basic_lost_close at right
with charachange


aki "さて、もう行ったほうがいいな。なんせ飛行機は待ってくれないから"



"晃さんの声色に後ろ髪を引かれているような思いがこもる。その視線は妹をしっかりと見据えている。"


show lilly basic_weaksmile_cas_close
with charachange



li "私は大丈夫よ、姉さん"


show akira basic_resigned_close
with charachange


aki "ああ、分かってる"

show lilly basic_smileclosed_cas_close
with charachange



li "まあまあ、それほど悪いことじゃないでしょ。すぐにまた会えるんだから"



"今回に限っては懐疑的な晃さんを元気づけているリリー。なんだか奇妙だ。リリー、本当に変わったな。"

show lilly basic_smile_cas_close
with charachange


li "さようなら、姉さん"


hi "さよなら"

show akira basic_smile_close
with charachange



"晃さんは少しの間俺たち２人を見下ろし、にっこりとほほ笑む。それはたぶん、俺が以前見たどの晃さんの笑顔よりももっとにこやかな笑みだろう。"


show akira basic_boo at tworight
with charadistant



"立ち去る前に、晃さんは震え気味な息を大きく吐いて自分を落ち着かせる。だけどついに、片手をポケットに突っ込んできびすを返す。"




"そして歩み去る。もう片手を宙に掲げたまま。"


show akira basic_ending
with charachange


aki "またな、２人とも！"

hide akira
with charaexit



"リズムもメロディーも方向性もないけど、最後の最後まで、ジャズの曲のような人だった。"



show bg lilly_hilltop at bgright
show lilly basic_smileclosed_cas_close at center
with dissolvecharamove


"しばらく静かに座り続けた後、リリーと俺は腰を上げて体を払う。"


"満面の笑みを浮かべながらリリーのほうに向き直り、俺は手を差し出す。"


hi "じゃあ、俺たちも行こうか？"


"優しくうなずきながら、リリーが俺の手を取る。今まで見た中で一番きれいで温かい笑顔とともに。"


show lilly basic_cheerful_cas_close
with charachange


li "そうしましょう、久夫さん"

scene unlock_ev lilly_goodend
show evbg lilly_goodend:
    truecenter
    zoom 3.0 subpixel True
    1.0
    linear 0.5 zoom 0.9
    easein 12.0 zoom 0.8
show evfg lilly_goodend:
    truecenter
    zoom 6.0 subpixel True
    1.0
    linear 0.5 zoom 1.2
    easein 12.0 zoom 0.8
with whiteout


"俺とリリーは学校に向かって歩き出し、あの素晴らしい笑顔は俺の記憶に刻み込まれる。俺たち両方が共有する、あの素晴らしい笑顔が。"



"俺たちの過去は散り散りで、時には悲しみに覆い隠されることもあっただろう。だけど、それは俺たちの消すことのできない人生や人格の一部でもある。"
"仮にそれを１つでも変えることができたとしても、そうはしないだろう。俺がここにいるのは自分の過去のおかげなのだから。"




"だからこそ、過去に俺たちの身に起きたこと、そしてこれから俺たちに起こるだろうこと、全部含めて……一緒に、俺たちは前へ歩き続けるんだ。"



"前へ……未来へ向かって。俺たちの未来へ。"

window hide Dissolve(1.0)

stop ambient fadeout 2.0
stop music fadeout 2.0

scene black
with Dissolve(1.0)

with Pause(1.0)

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
