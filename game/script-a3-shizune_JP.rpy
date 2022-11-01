label jp_S17:

window hide None

scene bg school_hallway3
with locationchange

nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_normal fadein 3.0


n "\n\nそれからというもの、日々は何事もなく、驚くような早さで過ぎていく。手話を勉強する意欲が再び湧いてきた。どうも俺には手話の才能があるみたいだ。勉強しなければその才能も無駄になる。それに授業に遅れるのはなおさら論外だ。"


n "もうすぐ夏休みだ。授業がだれてくるのにつれて、生徒会の仕事も減ってくると思っていたけど、そうはならない。来る日も来る日も、増え続ける無意味な仕事で多忙を極めている。"


n "どんなに話したくても、最近は静音と話す時間を一秒たりとも取ることができない。いつ見ても、静音は三重にチェックしないといけない、何かの台帳や書類の束に顔を埋めている。"


n "\n\n静音と話ができるのを期待して、今日は誰よりも早く学校に行くために早起きした。あいつはほかのどの生徒よりも先に着くように、いつも朝一番に教室に来る習慣があるから。でも残念なことに、こっちが先に来てしまったようだ。"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

play sound sfx_doorclose

window show


"俺の右側で生徒会室のドアが閉じるカチャリという音が聞こえて、そうでもなかったことがわかる。静音の方がほんの少し早かったみたいだ。"

play sound sfx_dooropen

scene bg school_council
with locationchange


"部屋に入り、静音の肩をぽんと叩いて注意を引く。"




show shizu behind_smile at center
with charaenter


"会話するのを期待しているのかも知れない。手に持っていたオレンジジュースのパックを置いたのはそのためか。"


ssh "おはよう"



his "相棒はどうした？"



show shizu adjust_frown
with charachange




ssh "私たちはそれぞれが一人の人間よ"






"考えてみれば、こんな言い方はしょっちゅう聞かされているにちがいない。今の答えが即座に出てくる理由はそれ以外に考えられない。"

show shizu basic_normal
with charachange


ssh "今日は早いわね。よかった。配布物の確認を手伝ってちょうだい。後で配るから"


his "今日は仕事抜きでお前に会えるようにわざわざ早く来たんだよ"

show shizu behind_smile
with charachange


ssh "ミーシャの話だと、あなたが早く来るのは珍しくないみたいだけど"


his "そっちだってそうだろ"

show shizu adjust_happy
with charachange


ssh "競争したいっていうの？"


"何食わぬ顔で静音は眼鏡を直す。でもその仕草の裏には、果てしなくどうでも良いことを真剣に競うことに対してうずうずしている気持ちが隠れている。ことが小さければ小さいほど静音は血が騒ぐのだと思う。"


his "競争じゃないよ。こんなのを勝負にしたいのか？　俺はいやだよ"


"最後の一言を付け加えるのを忘れそうになる。一番大事なところだ。"

show shizu behind_smile
with charachange


ssh "……まあ、それでもいいわ。三年の残り日数はあり余ってるし。どうせ途中で飽きちゃうから"


"そう言うと、静音はまたジュースを手にとって飲み干す。空き箱をゴミ箱に投げ入れるかと思ったけど、しない。俺ががっかりした表情になっているのを見て、怪訝な顔をしている。さっさと本題に入った方がいいな。"


his "話がしたかっただけなんだよ。言っとくけど、もうすぐ夏休みだろ"


his "そうでなくても、もっと一緒に過ごすべきだと思うんだよ。この夏ならそれができるって思ってたんだ"

show shizu adjust_blush
with charachange


"静音の顔が真っ赤に染まる。俺も同じくらい赤いに違いない。そしてあわてたように眼鏡を直し始める。万能ジェスチャーだな。考えるように指を軽くたたき、じっくりと次の言葉を選ぶ。"

show shizu basic_normal
with charachange


ssh "つまり、デートみたいな？"


his "二人でどこかに出かけるってだけで、それが即デートになるのか？"

show shizu behind_blank
with charachange


ssh "違うの？"

show shizu adjust_frown
with charachange


ssh "私はデートにしたい"


his "じゃあそうしよう"

show shizu basic_happy
with charachange


"静音は賛成するように一度手を叩くと、俺の言葉に付け加える。"

show shizu behind_blank
with charachange


ssh "でも今日はだめ"

show shizu basic_normal2
with charachange


ssh "家族に会いに、一週間出かけます"



"ずいぶん堅苦しい言い方だ。そのおかげで好奇心が刺激される。静音の家族はお上品で立派な、伝統的家族なのかもしれない。"
"大きな古めかしいお屋敷に住んでいて、鯉が泳いでいる池があったりして。家の人はみんないつも着物を着てるとか。"



"突飛な想像だけど、時にはそういうのも面白い。家族の人と一緒のときは、静音はリリーのような穏やかで落ち着いている良い娘を装うんだろうか。"


"俺には想像できないけど、そんな可能性が少しでもあるのなら、見逃すわけにはいかない。"


his "たった一週間？　じゃあそんなに遠くじゃないんだな"

show shizu behind_frustrated
with charachange


ssh "当たり前でしょ、みんな日本にはいるんだから"


his "そうなのか……"

show shizu adjust_happy
with charachange


ssh "一緒に行けるわけでもないんだし。もしかして、付いてきたいっていうの？"



his "どうしてだめなんだ？"

show shizu basic_normal2
with charachange


ssh "あなたが楽しめるとは思えないから"



his "そんなのわからないだろ。楽しいかもしれないじゃないか"


his "ああ、忘れるところだった。俺の質問に答えてない。一人で行くの？　それともミーシャも一緒？　家族の人は手話できるの？"

show shizu behind_blank
with charachange


ssh "ミーシャも一緒に行くわ"


"答えがなかった方の問いは、聞かなくてもおのずと明らかだ。"




"家族の人たちが静音と話ができないとしたら、静音の子供時代はどんな感じだったのだろうか。きっといつもメモ帳を持ち歩いて何もかも書いていたに違いない。今だって時々、どこからともなくメモ帳を取り出すし。"




"だいたい、それが出てくるのはミーシャも俺も近くにいないときだ。最後の手段みたいにメモ帳を出しているとき、ずっとしかめっ面をしているのが遠くからでもわかる。"


his "ミーシャが行くんだったら、俺だって行くよ"

show shizu basic_normal
with charachange


ssh "ミーシャが好きなの？"


his "それがものの道理だろ"


"もしかしたら静音は妬いているのかもしれない、という想像に少し心が躍る。でもきっとないだろう。静音はいつも感情をはっきり顔に出すし、俺の推理を裏付けるようなものは今のところ何も見あたらない。"



show shizu adjust_frown
with charachange


ssh "単に退屈してるだけだと思うけど"

show shizu behind_smile
with charachange


ssh "でもいいわ。よろしい、みんなで一緒に行きましょう。そもそも私もそうしたいって思ってたから"

show shizu adjust_smug
with charachange


ssh "急に行くのが決まったからって、生徒会の仕事をさぼって荷造り、なんてのは許さないわよ。そんなの言い訳にならないからね！"


his "大丈夫だよ。どうせ荷物なんてほとんど持ってないし"

show shizu basic_normal
with charachange


"静音は一瞬沈黙し、思慮深そうに指を重ねる。"

show shizu behind_blank
with charachange


ssh "あなたがこの学校に来ることになったのも、急に決まったことなんでしょうね"



label jp_S17a:


"静音がミーシャといっしょに急に俺の部屋に飛び込んできて、あの大量の薬を見かけたときのことを思い出したのかもしれない。あの気まずい瞬間は早く忘れてしまいたいし、思い出したくもない。"


"そうやって話を避けようとするのが、よけいに俺の居心地を悪くする。"


label jp_S17x:


his "確かにな。ほとんどその場で決まったようなものだった。思ってたよりもうまくいったと思うけど"


"静音がこれ以上追及しないでくれればと思う。実際にそれ以上は聞いてこなかったので、俺はほっとする。"

show shizu adjust_happy
with charachange


ssh "私の家は埼玉の中でも特別にきれいなところにあるの"


show shizu behind_smile
with charachange


ssh "朝早くに出かけるから、ちゃんと準備して。このことは後で話しましょう、いい？　とりあえず、この配布物は勝手にできあがったりはしないから。きっちり手伝ってもらうわよ"


stop music fadeout 3.0

hide shizu
with charaexit


"静音は俺を引きずり込んで作業に没頭する。俺が思うに、静音はこの旅行をそれほど楽しみにしていないんじゃないだろうか。"



scene black
with dissolve


label jp_S18:

scene bg school_dormhallway
with locationchange

play music music_daily fadein 0.5


"翌朝早くに静音とミーシャが迎えに来る。二人とも俺が見慣れた制服とは違う装いだ。"

show shizu behind_blank_cas at center
with charaenter



"休日なんだからそれもそのはずだけど、それでもどこか違和感がある。"
"静音の服は流行のお洒落なドレスで、山久のような落ち着いた場所にはちょっとやりすぎな気もする。七夕祭の時に着ていた浴衣を思い返すと、なんだか静音の服の傾向が見えてくる。"



"静音の服はどれも上品で大人びていて、念入りに考えられている。それなら当の本人がこんなに子供っぽいのはなぜだろう。"

show bg school_dormhallway at bgright
show shizu behind_blank_cas at tworight
with charamove

show misha perky_smile_cas at twoleft
with charaenter


"少なくともミーシャの服は、彼女の内面を表現しているな。"


show shizu adjust_frown_cas
with charachange


ssh "荷物、ずいぶん少ないのね"


hi "そう言っただろ。大して多くないって"

show shizu basic_frown_cas
with charachange



"静音はふくれ面をして、恥ずかしそうに足下にある結構な量の自分の荷物を足で揺らす。"
"ミーシャはスーツケース一つしか持ってきていないけど、下手をすると本人よりも大きなサイズだ。ミーシャもそのことは意識しているように見える。"



"まったく、小型の自動車なみに大きなスーツケースじゃないか。グリーンピースみたいな色も落ち着かない。死体の運搬にでも使いそうな代物だ。その見た目をネタに二人をからかってやりたくなる。"


hi "あーあ、二人とも残念だなあ？　そんなにでかいかばんを持ち歩かなきゃいけなくて。今度は荷物は減らせよ、俺みたいに。この小さなスーツケースに全部収まるんだから"

show misha hips_grin_cas
with charachange


mi "ジェームズ・ボンドみたいにね～！"


hi "そうだよ、それこそジェームズ・ボンドみたいに"

show shizu adjust_frown_cas
with charachange


shi "……"


"静音は意識を集中しながら、そっと眼鏡を持ち上げる。"

show shizu basic_normal_cas
with charachange


ssh "みんなで荷物を均等に分け合うべきよ"

show misha sign_smile_cas
with charachange


mi "わあ～！　すごくいいアイディアだよ、しっちゃん～！"


hi "は？　やだよ"

show shizu adjust_smug_cas
with charachange


ssh "私たち全員のためになるわ"

show misha cross_laugh_cas
with charachange


mi "そうだよ～！　わはは～！"


hi "俺はノーと言うしかないな"

show shizu cross_angry_cas
with charachange


ssh "多数決であなたの負けよ！"


"その手話を見せながら、前につんのめりそうになる。なんて恐ろしい。"


hi "あー、いや、冗談だって。一つや二つ余分に持つくらいなら大丈夫だよ。ちょっとからかったら面白いかなって思っただけで"


hi "ただし、その荷物全部俺に運ばせるつもりなら、そこのでっかい緑のスーツケースの上に乗って、そりみたいに山から滑り降りるつもりだったけどな"

show shizu adjust_smug_cas
with charachange


shi "……"



"今の一言が静音を笑わせたようで、手で口を覆って笑いを押し戻そうとしている。笑ってるのを隠しているみたいだ。"
"静音は笑えるんだろうか。笑えないなら、そのせいでこういう仕草をしているのかも知れない。なんだか悲しい気持ちになる。"


stop music fadeout 3.0

scene bg city_station
with locationskip


"荷物の件もけりが付いて、俺たちは駅に向かう。列車の旅は実に退屈だ。静音とミーシャはすぐに寝付いてしまうけど、俺はまるで眠れない。こんなことは初めてだ。薬のせいかもしれない。"

scene bg shizu_houseext
with shorttimeskip

play music music_soothing fadein 0.5


"静音の家に到着する。俺が想像していたよりもずっと大きい。巨大、と言ってもそれほど言い過ぎじゃないくらいだ。"


hi "お屋敷に住んでるのか？"

show shizu cross_angry_cas at center
with charaenter



"ミーシャが俺の言葉を通訳したのを見ると、静音は怒ってつま先立ちで俺に目線を合わせ、とてもきつい表情を見せる。まるで『皮肉でもそんなことを口にするなんて！』とでも言いたげだ。"




show shizu basic_frown_cas
with charachange


ssh "こんなのただの普通の家じゃない。お屋敷だなんて、そんな派手なものじゃないわ"


"だとしたら、その辺の言葉の定義が俺と静音とではずいぶん違うみたいだな。"

show bg shizu_houseext at bgright
show shizu basic_frown_cas at tworight
with charamove

show misha hips_grin_cas at twoleft
with charaenter


mi "わはは～、ひっちゃん、びっくりした？　ひっちゃんが泊まる場所、教えてほしい？"

show shizu behind_blank_cas
with charachange


ssh "ゲストルームがあると思うけど、二つあるかはわからない。確かめてくる"

show misha sign_smile_cas
with charachange


mi "ん～、でもだいじょうぶだよ、ひっちゃん～！　必要だったらしっちゃんとわたしは同じ部屋にするから。ただ～、しっちゃんの部屋がほかに使われてなければだけど"

hide shizu
with charaexit

hide misha
with charaexit

stop music fadeout 5.0


"『わからない』？　静音はあまり実家で暮らしたことがないんじゃないかと思い始める。そのことでジョークをかます間もなく、静音は家の中へと消える。ミーシャもそれに続くので、俺は一人で敷地内に取り残される。"


"まだ二人を追って中に入る気はしない。玄関の前に自分のかばんを置いて、その間に辺りを見回し、家の周りを一周する。"

show hideaki bored at center
with shorttimeskip



"たったの数分だったけど、戻ってみるとかばんがなくなっていて、代わりに小さな女の子がいることに気づく。静音によく似ているけど、静音は赤いショートパンツや星と月の柄が入ったストッキングなんて履かない。"



hi "こんにちは！　静音の妹さんですか？"

show hideaki normal
with charachange


hh "いいえ。弟です。秀明っていいます"

show hideaki thinking
with charachange


hh "はじめまして"

play music music_happiness fadein 2.0


"返ってきた声は単刀直入で、平板で、そして間違いなく男のものだ。駅までの道を忘れていなかったら、今すぐに背中を向けて帰ってしまいたいくらい恥ずかしくなる。"

show hideaki serious
with charachange


hh "姉がいっしょに連れてきた人の二人目ですか？"


hi "『いっしょに連れてきた』？　俺は荷物じゃないんだけど"



hi "とにかく、俺は久夫。荷物を中に入れてくれたの？"

show hideaki triangle
with charachange



hh "うん。自分のところで見つけたものは当然ぼくのものだからね"







hi "そんなわけないだろ。世の中そういう風にはなってない"


"こんなにお上品な子供でも、『拾ったもの勝ち』を信じているんだな。子供と言ってはいるけど、よく考えるとそれほど俺より年下には見えない。せいぜい二、三歳下ってくらいだろう。"

show hideaki normal
with charachange


hh "姉さんに渡しておいたよ。中にあるから。久夫さんも生徒会？"




hi "ああ。なんで知ってるんだ？　静音がよく話題にしてるのか？"


"『静音がよく話してるのか？』と言いそうになった。危ないところだった。"

show hideaki bored
with charachange



hh "うん、いつも。姉さんと仲良くしてるの？"





hi "仲良く？　変な質問だな。良くなかったら生徒会にはいないよ。君はどうなの。姉さんとはうまくやってる？"



"平板な声だけど、その表情は静音と同じくらい豊かで、自分の本当の気持ちを隠している。きっと家族の血だろう。理由はどうあれ、今の質問はありがたくないようだ。"

show hideaki thinking
with charachange


hh "ごめんなさい。二人の振る舞いがすごくよく似ているから、聞いただけなんです"


"理由はわからないけど、こいつにからかわれている気がしてくる。残念ながら効果はあった。俺は静音と比べられるのは好きじゃない。"



hi "君の方がずっと静音に近いけど、でもそれは当たり前だよな。静音の妹と間違えたくらいだし。そういう間違いをされたくないなら、着る服はちゃんと選んだ方がいいぞ"




show hideaki confused
with charachange


hh "よくわからないな。この服は季節に完璧に合ってるよ"


hi "そのストッキングは何だよ？"

show hideaki angry_up
with charachange


hh "かっこいいでしょ"

show hideaki disapproves
with charachange


hh "久夫さんは姉さんみたいなことを言うね。そのうち姉さんと間違えられるようになるよ"


"さっきの一言は思ったよりもこたえたようだ。こうしてやり返そうとしてくるのはそのせいだろう。"


hi "他人と比べられるのは嫌なんだけど"

show hideaki evil
with charachange


hh "姉さんも他の人と比べられるのはいやがるよ"



"秀明は静音よりも少し大人びていると思ったけど、負けず嫌いと他人を挑発する癖は同じだ。こうなったのは静音がいたからなのか、それとも別の理由だろうか。"




hi "それは君もだろ？　ああ、わかったよ。こういう揚げ足取りはいけないな"




show hideaki normal
with charachange

stop music fadeout 4.0


"小さい子供は特にそうだけど、秀明は今の言葉で俺が負けを認めたととったようだ。それを見逃すのはしゃくに触る。それでも引き下がれるうちに引かないといけない。"


scene bg shizu_living
with locationchange


"玄関に入った瞬間、ミーシャの笑い声が廊下にこだまするのが聞こえてくる。声の元をたどってリビングらしい部屋に入る。部屋には思っていたより人がたくさんいる。"

show lilly basic_displeased_cas:
    center
    ypos 1.17 xpos 0.55
show akira basic_boo:
    tworight
    ypos 1.15 xpos 0.72
show hideaki bored:
    center
    xpos 0.92
    easein 1.0 ypos 1.1
show shizu behind_blank_cas:
    twoleft
    ypos 1.11 xpos 0.27
show misha perky_smile_cas:
    center
    ypos 1.1 xpos 0.08
with charaenter

play music music_another fadein 4.0




"その中に、見覚えのある独特の金髪のポニーテールを見つける。ここにリリーがいることに驚いたけど、それ以上に混乱する。"
"静音も同じくらい驚いているようだ。リリーの方もこの偶然の出会いを喜んでいるようには見えない。"





"リリーの横に立っているのは、きちんとしたスーツを着込んだ、背の高くて中性的な女の人だ。リリーのお姉さんだろうと思うけど、早合点して間違えたくはない。"

show lilly basic_listen_cas
with charachange


li "こんなに早く到着するとは思っていませんでしたけど"


"俺に話しかけているのかと思ったら、静音に話しかけているのだった。リリーは俺がいることに気づいてもいないと思う。二人が話している最中に俺が入ってきたのは明らかだ。"
"リリーの意識は静音に向かっているので、俺が入ってくるのは聞こえなかったのだろう。"


show shizu basic_frown_cas
with charachange


ssh "あなたのために予定を全部立て直すべきだったわ"

show misha sign_smile_cas
with charachange


mi "しっちゃんは、あなたのために予定を全部立て直すべきだったって言ってるよ～！"

show lilly basic_displeased_cas
with charachange


li "そうしてもらえたら良かったのですけど。でもあなたがそういうことをするとは思えませんね"

show misha hips_smile_cas
with charachange


mi "あっ、こんちは、ひっちゃん～！　やっと来たね"


hi "ああ。こんにちは、リリー"

show lilly basic_surprised_cas
with charachange


li "えっ、久夫さん？　驚きました。姉さん、こちらは久夫さんです。同級生の。久夫さん、こちらは晃、私の姉です"

show akira basic_smile
with charachange


aki "よう"




"短く手を挙げて、とてもカジュアルな挨拶をする。じゃあやっぱりお姉さんだったんだ。"

show akira basic_boo
show lilly basic_weaksmile_cas
with charachange



aki "そっちの予定の邪魔にならなければいいんだけど。こっちはあと一日しかここにいないから、リリーもあたしといっしょに来ればいいんじゃないかって、二人で考えてたんだ"





"説明をする必要にかられたのか、晃さんがこっちを向く。ありがたく思う。"

show akira basic_ending
with charachange


aki "ここでのあたしの立場は、ベビーシッターっていうのが一番近いかな"

show hideaki disapproves
with charachange




"晃さんが秀明の髪をくしゃくしゃとかき回す。秀明は相変わらず不愉快そうな顔をしている。"




hh "屈辱的だ……"


show akira basic_smile
with charachange


aki "そうか？　あともう何歳か年取ったら、肩書き変えてやってもいいよ。それか背を何センチか伸ばすんだね"


"二人は面白いコンビだ。晃さんはベビーシッターと言うより弁護士に見えるけど。でも晃さんとリリーがここにいる理由はまだよくわからない。"


"部屋の中を見回すと、テニスのラケット、ゴルフクラブ、釣り竿と釣り具の箱などがあちこちに隠してある。"



"どの椅子の下にも、どの部屋の角にも、そしてテーブルの下にまで、なんらかのアウトドア系の用具が転がっている。釣り竿の一つを手にとり、もてあそんでみる。"



hi "ここ、いい家だな"


hi "静音、お父さんはいろんな趣味があるみたいだな"

show misha sign_smile_cas
with charachange

show misha perky_smile_cas
with charachange


"一瞬、自分の言葉を手話にするのを忘れてしまう。でもミーシャが俺の言葉をすでに通訳してくれている。こうやってミーシャが手話通訳を無意識にしていることに今でも驚かずにいられない。"

show hideaki normal
with charachange


hh "釣りはするの？"


hi "いや、やり方を知らないし。やってみたいとは思うけどさ。落ち着くって聞いたから"

show shizu behind_blank_cas
with charachange


ssh "少し車で行ったところに川があるわ。うちの家族はみんな釣りができるの。よかったらそのうちにみんなで行きましょう"

show akira basic_laugh
with charachange



aki "静音も秀明も釣りできるんだ？　その年で知ってるとは思わなかったよ。釣りって大体おっさんの趣味って感じがするじゃん"





show akira basic_ending
with charachange


aki "実はさ、リリーは料理がすごくうまいんだ。新鮮な魚が手に入れば……"


"晃さんの思考を読むのは難しくないな。"

show lilly basic_displeased_cas
with charachange


li "魚が食べたければ、魚屋さんに行けばいいじゃない"


"リリーの声は普段よりも少しだけ厳しい気がする。お姉さんとは違って、リリー自身はまるで釣りに行くことに乗り気でないみたいだ。"



show shizu basic_happy_cas
with charachange


shi "……"

show misha hips_grin_cas
with charachange


mi "魚釣りに行く方が楽しいよ。誰が一番大きな魚を釣れるか、勝負するのもいいね～！　それって面白そうだと思わない？　そうだよ～！　ひっちゃん、どう思う？　面白そうだよね、ね？"


hi "ああ、まちがいないな"

show akira basic_smile
with charachange


aki "良さげじゃん。あたしも釣りはしたことがないから、今回初チャレンジってのもありだね"


show akira basic_boo
with charachange


"晃さんの目がリリーの方を向くけど、何の反応もない。それを見て晃さんの笑顔も沈む。俺はというと、なぜそこまでリリーがかたくなになるのか不思議に思う。"


show hideaki normal
with charachange


hh "全員分の釣り具はないと思うよ"

show shizu behind_smile_cas
with charachange


ssh "交代でやればいいわ。チーム戦よ"

show hideaki confused
with charachange


hh "なんて言ってるの？"


hi "交代でやればいいって。あと競争にしたいって"

show akira basic_laugh
with charachange



aki "行こうよ、リリー。行ってみれば案外楽しめるかも知れないぜ"




show akira basic_boo
with charachange


aki "じゃあ、勝負は釣った魚の大きさで決めるの？　それとも釣った数？"

show shizu adjust_smug_cas
with charachange


ssh "お姉さんの方が話が早いみたいね、いつも通りに"

show shizu basic_normal_cas
with charachange


shi "……"

show misha sign_smile_cas
with charachange



mi "しっちゃんはね、リリーは魚屋さんに行く方がいいと思ってるんでしょ、て言ってるよ。そうでしょ～？　そっちのほうが楽だから、リリーならそうするのが当然だよね！"
mi "でも魚釣りに行く方が楽しいし、お金も節約できるよ。話が分かるね、晃さん～！"


show akira basic_smile
with charachange


"晃さんが愛想のいい、どちらかといえば気取った笑顔を見せる。まあ、静音にほめられるために釣りに行くわけじゃないしな。"

show lilly basic_sleepy_cas
with charachange


li "……"

show lilly basic_weaksmile_cas
with charachange


li "川は結構遠いんじゃないんですか？"

show akira basic_ending
with charachange


aki "そんなに遠くはないと思うよ。それに必要ならあたしが運転するし。魚が釣れるんだったら、そのくらいは構わないよ"


hi "これだけの人数、晃さんの車に入りますか？　釣り具だっていっぱいありますよ"

show akira basic_boo
with charachange




"晃さんは唇を結ぶと、わずかに指を動かして人数と荷物の量を数える。俺、静音、ミーシャ、リリー、晃さんと秀明を乗せるとなると……"



show akira basic_lost
with charachange


aki "６人か。ったく、あたしの車は５人しか乗れないよ"

show akira basic_ending
with charachange



aki "いや、秀明があたしのひざの上に乗れば――"


show hideaki angry_up
with charachange


hh "僕はひざ上なんてごめんだよ"

show akira basic_resigned
with charachange


aki "ちぇー"

show shizu adjust_happy_cas
with charachange


shi "……"

show misha hips_smile_cas
with charachange


mi "しっちゃんが、お父さんの車なら全員乗れるって"

show akira basic_lost
with charachange


aki "えっ、あのフーガ？　おじさんが使わせてくれるなら、ほかに選択肢はないなあ。あたしの車を見捨てるみたいでなんか嫌だけど。もうすぐ手放さなきゃいけないってのに"






"リリーのかたくなな態度や、そもそも夕食に魚を食べられない可能性を考えれば、先に食事をしたほうがいいんじゃないかという秀明の問いも、移動プランを決めた晃さんと静音の決意を変えることはできない。"




stop music fadeout 5.0

scene ev shizune_car
with shorttimeskip

play ambient sfx_businterior fadein 1.0


"田舎の地をのんびりとドライブする、という俺の期待は果たされた。晃さんの運転は車窓の風景と同じくらいスムーズで穏やかだ。車の中でミーシャが眠りこけてしまうほどだった。"






"今度の旅行は静音の好みよりもペースが遅すぎるんじゃないかと思っていた。でも当の本人は純粋に楽しんでいるみたいだ。ドアとの間で秀明が窮屈そうにしているのにも構わず、ずっと窓の外を見ながら微笑んでいる。"



stop ambient fadeout 0.5

scene bg shizu_fishing at left
with shorttimeskip

play ambient sfx_parkambience fadein 0.5


"川の周りはとてもきれいだ。晃さんと静音はあっという間に川辺に向かって行くので、俺たちもその後を追うしかない。でないと遅れをとってしまう。"

show lilly basic_weaksmile_cas at left
show hideaki bored at center
show misha hips_grin_cas at right
with charaenter




"秀明とリリーはどちらもお姉さんに調子を合わせているだけだというのが見て取れる。秀明よりはリリーの方がつまらなさそうだ。"
"でもミーシャはいつものように楽しそうにしている。静音と晃さんのやる気にうまく乗っかることができたらしい。"




"俺はどちらかと言えば今食事をしたいと思っているけど、リリーが料理してくれる取れたての魚を食べるというのも魅力的だ。"




"川は思っていたよりも幅広いけど、景色はとても良くて、流れも穏やかだ。魚釣りのためだけにあるような小さな桟橋をのぞけば、人の手が入った様子はない。ここ最近どれだけの自然を目にしているか実感する。"







show shizu invis at offscreenright
show akira invis:
    center
    xpos 1.5
with None

show bg shizu_fishing at right
show lilly invis at Position(xpos=-0.6)
show hideaki invis at offscreenleft
show misha perky_confused_cas at left
show shizu basic_happy_cas:
    center
    xpos 0.37
show akira basic_smile:
    center
    xpos 0.8
with Dissolvemove(1.5)



"晃さんに釣りのやり方を説明するために、静音がミーシャを引っ張り出す。リリーと秀明は二人でおしゃべりしているので、活気がある方の三人組に加わることにする。"


show akira basic_ending
with charachange


aki "うーん……それじゃあルアーはどれを使えばいい？　こっちのかわいいやつはどう？"

show shizu basic_frown_cas
show misha sign_smile_cas
with charachange


mi "まってまって～！　これは競争だから、先にチームを決めなきゃ！　しっちゃんとわたしはもちろん同じチームね。ひっちゃんもわたしたちのチームに入るよね、ね？　生徒会チームにしようよ～！"


hi "オッケー"

show akira basic_laugh
with charachange


aki "よし。じゃあもう一つのチームはあたしと秀明とリリーだな。リリー、チーム名は何がいい？"

stop music fadeout 2.0

play sound sfx_flash

show bg shizu_fishing at left
show lilly basic_sleepy_cas at twoleft
show hideaki bored at tworight
show misha invis at Position(xpos=0.85)
show shizu invis at offscreenright
show akira invis:
    center
    xpos 1.5
with Dissolvemove(0.5)



$ doublespeak (li, hh, "なんでもいいと思います", "なんでもいいと思うよ")




play sound sfx_flash

show bg shizu_fishing at right
show lilly invis at Position(xpos=-0.6)
show hideaki invis at offscreenleft
show misha perky_confused_cas at left
show shizu basic_angry_cas:
    center
    xpos 0.37
show akira basic_ending:
    center
    xpos 0.8
with Dissolvemove(0.5)

show akira basic_lost
with charachange


aki "じゃあ無気力チームってことで……"

play music music_comedy fadein 0.5


"またしても、晃さんの努力はそでにされてしまう。一方静音とミーシャには、活気の不足はまったく見られない。"

show misha hips_smile_cas
show shizu behind_frown_cas
with charachange


ssh "久夫！　チームリーダーになってちょうだい。とにかくがんばって、できるだけたくさん、さもなければ一番大きな魚を釣ってね"


hi "なんで俺？　まだ魚の釣り方だって誰からも教わってないぞ"

show misha hips_grin_cas
show shizu behind_blank_cas
with charachange


mi "今教えてあげるよ～"


"手短な説明の後、静音はすぐにこのタッグチーム釣り大会に勝利するための戦略会議に俺たちを引き込もうとする。"


"なんとなく、魚がミミズに食いついてくれるのを期待して何時間も座り込むスポーツに競争という概念はなじまない気がする。"

show shizu adjust_happy_cas
with charachange


ssh "秀明は予備の竿になっちゃったみたい。あれ、ただの竹竿に糸を結んだだけでしょ？　ということは、順番を決めるときはあなたが秀明と当たるようにすべきね"


hi "えっ、なんで俺？"

show misha sign_smile_cas
with charachange


mi "一番釣り経験が少ないでしょ、ひっちゃん～"


hi "へえ？　じゃあ一番うまいのは誰だよ？　静音か？　秀明は弟だし、たぶん同じくらいうまいんじゃないか。きっとしょっちゅう釣りしてると思うぞ。湖の近くに住んでるんだし。もしかしたら静音よりも上手かもな"

show akira basic_annoyed
with charachange


aki "お前ら見てると頭痛がしてくるよ。あたしがそっちの会話の２／３しか聞こえないってわかってるだろ？　何の話だよ？"


hi "順番決めです"


"晃さんが厄介そうな顔をする。だんだんいらだってきているようだ。無理もない。"

show shizu basic_sparkle_cas
with charachange


ssh "そっちがイライラしてるなら、その分私はもっとやる気が出てくるわ。もっとハードルを上げましょう"





show akira basic_lost
with charachange


aki "なんて言ってるの？"


hi "ハードルを上げたい、だそうです"

show akira basic_laugh
with charachange


aki "そう焦るなって。こっちのビギナーズラックはそっちの二倍だからな。海を丸ごと釣り上げるくらいじゃなきゃ、あたしたちには勝てないよ"

show shizu adjust_happy_cas
with charachange


shi "……"

show misha hips_grin_cas
with charachange


mi "ここは淡水域でしょ、大した海洋生物学者さんね～"



"平然としたまま、無邪気な陽気さで変てこな侮辱をする。晃さんは気にも留めていないようだ。それを笑い飛ばす一方、静音はいつものいたずら好きな様子に戻っている。二人が仲良くしていることに安心する。"



show akira basic_smile
with charachange


aki "で、結局チーム決めするの？　なんか腹減ってきたんだけど……"

show shizu basic_normal_cas
with charachange


ssh "久夫とミーシャと私は同じチーム。リリーと秀明とあなたでもう一チーム。違うの？"

show akira basic_ending
with charachange


aki "それが一番自然な分け方だと思うけどさ。でもちょっと混ぜた方が面白くなると思わないか？　どう？"

show misha perky_smile_cas
with charachange


mi "ん～、妹と一緒に釣りしたくないの？"

show akira basic_boo
with charachange


aki "いや、あたしたち二人とも釣りって知らないしさ。両方同じチームってのはちょっと……"


"なんかヤバい話を聞いた気がするぞ。静音の疑うような表情がそれ以上危険になる前に、話題を変えようとしてみる。"


hi "で、晃さんと静音はお互い知り合いなんですよね？"

show akira basic_smile
with charachange


aki "そりゃもう。昔からのつきあいさ"

show shizu basic_normal2_cas
with charachange


"静音に向かって、晃さんが物知り顔でニヤリと笑う。ミーシャが今の言葉を通訳し終わると、ようやく静音が嫌そうな表情を浮かべる。"



"晃さんは本当にリリーと大違いだ。外見はもちろん、晃さんはずっと砕けていて、おおらかだ。リリーの家族はみんな上品で改まっているとばかり思っていたので、驚いた。でも話しやすそうな人だという感じはする。"


show akira basic_laugh
with charachange


aki "魚釣りのことを話したいのは山々だけど、そろそろ本当に始めた方がいいんじゃないかな"

show shizu behind_blank_cas
with charachange


ssh "野球みたいにラインナップを決めた方がいい？　それとも総当たり戦とか、タッグ戦は？"

show shizu basic_sparkle_cas
with charachange



ssh "それぞれが好きな場所に座ってもいいことにする？　それともチームごとに固まるようにする？　釣る場所は事前に宣言する？　カウントする魚の大きさは？"


show akira basic_lost
with charachange


"律儀にミーシャが通訳するのを聞いて晃さんがうめき声を上げる。それを見て静音は眼鏡をこすり、声もなく笑う。"

show shizu adjust_happy_cas
with charachange

stop music fadeout 4.0


ssh "やっぱりいいわ。普通に釣りをしましょう"

show shizu behind_smile_cas
with charachange


ssh "個人戦ってことにしましょうか"

stop ambient fadeout 2.0

scene ev shizu_fishing_ah
with shorttimeskip

play music music_ease



"腰を下ろす。準備はばっちりだけど、あまり自信はない。晃さん以外のみんなもすでに座っている。晃さんは俺の隣に座り、スーツの上着を脱いで袖をまくると釣り糸を投げ始める。"




"桟橋には全員が座れる場所がなかったので、ミーシャと秀明は岸辺に座ることになり、二人でいっしょに釣っている。本音を言えば静音の隣に座りたかったけど、晃さんも十分親しみやすそうだ。"



aki "ちょっと気をつけろって、近すぎ。糸を絡ませるなよ？"



hi "それで、今まで一度も釣りしたことないんですか？"



aki "ないね、でもテレビで見たりしたことはあるから。顔に角みたいなのがついてる大きな魚、一度釣ってみたいと思ってたんだ。マカジキって言うんだっけ"




li "確か、その魚は海の魚じゃないかしら。海水魚です"


aki "わかってるよ。どうしてみんな、あたしが淡水魚と海水魚の違いがわからないってことにしたがるんだ？"


li "海水魚かどうかはともかく、気をつけないと魚が驚いて逃げちゃうわよ"




"静音をあおるのと同時に、リリーを気遣って話しかけている晃さんの声はちょっと大きめだ。リリーにも一理ある。俺の釣り針には何も引っかかる気配がないけど、それがどのくらい晃さんのせいなのかはわからない。"





"静音は日差しを受けてリラックスしようとしている風にうまく見せかけているけど、周りの話題がわからないことに少し不機嫌そうなのが俺にはわかる。近くにミーシャがいないというのは実に厄介だ。"



ssh "久夫、スコアはどう？　こっちが勝ってるの？　勝ってるといいけど、チームの成功はあなたに託されてるんですからね"


"釣り竿をうまい具合にホールドして、どうにかぎこちない手つきで静音に返事をする。たぶん話し言葉で言えばちんぷんかんぷんな手話になっていただろう。"


hi "すぐ隣にいるんだからさ。見りゃわかるだろ？"


ssh "がっかりね。あなたは集中力が足りないのよ。もっと集中しなきゃ"




hi "はいはい、そうだな。どっちにしても０対０だから"



"晃さんがクスクス笑う。でも今ので晃さんの勢いもなくなったのは明らかだ。"


hi "釣った数だけで勝負するのか、それとも大きさもカウントするのか、どっちだ？"



ssh "両方よ。魚のランクも考慮するから"






hi "そのランクは誰が決めるんだ？　魚の判定資格なんて持ってるのか？"



"静音が首を振り、持っていないことを示す。"


ssh "……でもそんなに難しいようには見えないけど。ミーシャにああやって腕を振り回しちゃだめって伝えて。魚がみんな驚いて逃げちゃう。あと秀明にどうしてまだ糸も垂らしてないのかって聞いて"


"二人の方に目を向けて、静音の言ったことを大声で伝える。"


mi "しっちゃん、予備の竿しか使えないから秀明くんがすねちゃってるみたいだよ～！"


"今のミーシャは意味の通る手話をできる状態ではないので、静音からは怪訝な表情しか返ってこない。俺が通訳すると、静音はため息をつくだけだ。"


aki "おーい、嫌な気分かもしれないけど、いいからやってみなよ。もしかしたら、本当にでかいのが釣れるかもしれないだろ。でもやってみなきゃ何も釣れないんだぞ！"




"そう晃さんが励ます理由の半分は、もし秀明が『でかいの』を釣ったらご相伴に預かりたいと思っているから、という気がする。参加者が六人いる方が、五人しかいないよりは釣れる可能性が上がるわけだし。"




"静音と話すために始終手をまごつかせるはめになり、静音自身もそわそわし始めている。そろそろ静音に竿を渡してもいい頃合いだ。"


hi "みんな、そろそろ交代しないか？"


aki "いいよ。リリーは？"


li "いえ、いえ、大丈夫。魚釣りのやり方なんて全然わからないし"


"俺が静音の通訳の立場をミーシャから引き取ったような状態なので、二人の会話を手話に訳す。"


ssh "ご立派ね、リリー"


"ほんとにもう、また始まった。またけんかが始まるのはごめんなので、今のをわざわざ通訳はしない。"


hi "静音が、少なくともチャレンジしてみるべきだって。やってみたら意外とおもしろいかもよ"


li "わかりました。姉さん、これはどう使うの？"


aki "結構簡単なんだ……"


"こうやって静音の言葉をわざと完全に言い替えてしまうのは、倫理的にどうなんだろう。少なくとも役には立ったわけだけど。"

scene ev shizu_fishing_sl
with shorttimeskip


li "……わかった気がするわ。どの餌を使うのが一番いいかしら？　魚があまり傷つかないものを使いたいんだけど"


aki "魚の口に針を通すんだし、餌がそれ以上傷を増やすってことはないと思うよ"


hi "それでリリースするの……？　いやいや、それはだめだよ"


li "でも大きな魚じゃなかったら、殺す意味があまりないんじゃ……"


"手が自由になって、みんなの会話を通訳するのがずっと楽になった。今度は静音が両手がふさがって苦労する番だけど、楽々とこなしているように見える。"



ssh "なんなの、その傲岸不遜は。わかった、じゃあこれからは大きな魚だけ釣り上げるから"



aki "なんて言ってる？"


"通訳すると、晃さんはただため息をつく。"


aki "いや、その『だけ』ってのはやめようぜ。魚は魚なんだからさ、釣ったものを自分のものにすればいいだろ"


"でもあいにく静音には聞こえていないし、リリーもちゃんと聞いてはいなさそうだ。"


"リリーはすんなり魚釣りに入り込んでいる。やっぱり、とてもゆったりした活動だからだろう。ほどなく二人とも魚を釣り上げる。意外だけど、リリーも静音と同じくらい魚の大きさを気にしている。"

stop music fadeout 3.0


"時間が経つにつれ、みんな本当に楽しみ始めているようだ。"

scene bg shizu_fishing_ss
with shorttimeskip

play ambient sfx_parkambience fadein 4.0
play music music_tranquil fadein 3.0



"日が暮れる頃には、何匹かいい具合の大きさの魚がとれた。秀明とミーシャも一匹ずつ釣っている。釣った数を競っている、なんて話は誰も持ち出さない。もうそんなことは誰も気にしていないと思う。"



show akira basic_smile_ss at center
with charaenter



"静音とミーシャは少し離れたところで二人きりで話し合っている。リリーと秀明も同じだ。俺もこの静かな瞬間に乗じて、晃さんと話すことにする。"



hi "リリーと静音、今日は仲良くしてましたね。普段学校であの二人がぶつかり合うのを見てるから、こんなふうになるとは思ってませんでした"

show akira basic_boo_ss
with charachange


"晃さんがおもしろそうに大声で笑う。俺が気にしているほどには、二人のいがみ合いを深刻にはとらえていないようだ。"


aki "あいつらなりの理由があるのさ。リリーとあたしは明日から遠くに出かけるから、ちょっと顔出していこうと思ったんだ"

show akira basic_ending_ss
with charachange


aki "終わってみれば、来て良かったって思うよ"



"短い沈黙の後、晃さんは大声を出しながら体を伸ばすと、手を叩いてみんなの注意を引く。"


show akira basic_smile_ss
with charachange


aki "さて、ちゃんと全員食べられるくらい釣れたかな。そろそろ帰ろうぜ"

show bg shizu_fishing_ss at bgright
show akira basic_smile_ss at tworight
with charamove

show lilly basic_weaksmile_cas_ss at twoleft
with charaenter



"リリーはうなずくけど、その後ためらいを見せる。少し表情を曇らせてはいても、今朝よりは機嫌が良くなっているようだ。"
"晃さんは本当にリリーの扱い方を心得ているんだろう。静音に対する反感を見事に解きほぐすことができたのだから。"


show akira basic_ending_ss
with charachange


aki "今日釣った魚、すごくおいしそうだな。醤油持ってくれば良かったなあ、そうすればこの場で食べられたのに"

show lilly basic_surprised_cas_ss
with charachange



li "私に料理してほしかったんじゃ……"



show akira basic_laugh_ss
with charachange


aki "生で食べるのっていいと思わない？"



"晃さんの提案なのか冗談なのかわからないけど、それはともかく料理してから食べようということに決める。"


stop ambient fadeout 2.0

scene bg shizu_houseext_lights
with shorttimeskip

stop music fadeout 3.0



"外出しているうちに遅くなってしまっていた。静音の家に戻る頃には、ちょうど夕食の時間になっている。"


scene black
with dissolve



label jp_S19:




scene bg shizu_guesthisao
with locationchange

play music music_pearly fadein 5.0


"持ってきた薬がかばんの底いっぱいにこぼれてしまっていた。昨日の夜、寝床に着こうとする直前まで気づいていなかった。かばんの中から薬を全部拾い出すのに、とんでもなく時間がかかった。"



"起きたときには、早くも寝付きの悪さと遅寝からくる偏頭痛に襲われている。"

scene bg shizu_living
show hideaki normal_up at center
with locationchange


"居間に立ち入ると秀明がいて、朝ごはんを食べ終えるところだった。フォークを口まで持ち上げる途中で、食べ続けるべきか俺に挨拶すべきか迷っているようだ。部屋から出た方がいいのかな。"

show hideaki triangle
with charachange


hh "おはようございます"


hi "おはよう"

show hideaki thinking
with charachange


hh "朝ごはん、何を食べるのがいいと思う？"



hi "『思う』って、そっちは今食べてる最中じゃないの？"


show hideaki normal
with charachange


hh "そうだよ。他の人はみんな食べ終わってる"


"にもかかわらず、秀明は同じ質問を繰り返す。気を使っているだけなんだろう。表し方は独特だけど、それでもありがたい。それに結構腹も減っている。"


"朝ごはんを取りに行く間、沈黙を埋めるために秀明と少し話そうとしてみる。"


hi "昨日の魚釣り、楽しかったね。羽加道家と砂藤家はいつもあんなふうに仲良しなの？"

show hideaki bored
with charachange


hh "良くないよ"


hi "そうなんだ"



"とは言うものの、俺には理解できない。短い沈黙の後、秀明が親切にも説明してくれる。"

show hideaki thinking
with charachange


hh "家どうしの問題があって。両家の父親が兄弟で、お互いに仲が悪いんだ"


"それを聞いて、考えるネタが山ほど出てくる。それが静音とリリーがお互いにああいう態度を取る背景なんだ。二人に関わるのがよけいに心配になってくる。"


hi "ああ、時にはそういうのって厄介だよな"

show hideaki normal
with charachange



"秀明はただうなずく。俺は朝ごはんを持って席に着く。もう少し話しやすいやつだったらなあ。"



"食べている間、ミーシャがいる割には家の中がずいぶん静かなことに気づく。静音とミーシャがもう朝ごはんを食べ終わっているなら、まだ寝ているというのはありえない。秀明に二人がどこにいるのか聞いてみる。"

show hideaki bored
with charachange


hh "姉さんとミーシャさんは父さんのお使いで出かけたよ。地元の商売相手がミーシャさんと話すのが大好きで、父さんがぜひ行ってくれって"





hi "まあ、あいつはいい子だし、陽気だからね。その人たちに気に入られるのもわかるよ。ミーシャに個人授業してもらうといいんじゃない。そうしたら仕事の人脈も増やせるかもよ"

show hideaki confused
with charachange


hh "本当ですか？"


"真剣そうだ。こんな小さい子がどういう人脈を必要としているのか、見当がつかないけど。学校バザーのために史上最強の資金調達者を手配したいとか。"




"秀明の計画がどんなものなのか知る前に、ここから帰らないといけないのが残念だ。"




"アウトドア派っぽいという以外に、静音のお父さんがどういう人なのか、また興味が湧いてくる。今のところわかっているのは、自分の商売相手や娘の友達に頼みごとをする、ということだ。"


"ものすごく恥ずかしがりか、ものすごく怠け者かのどちらかだと思う。この時点で決めつけるのは失礼かもしれないけど、そうであれば静音の性格の大部分は説明が付く。"

show hideaki triangle
with charachange


hh "どっか出かけたいですか？"


hi "いや、あんまり。なんで、出かけたいの？"

show hideaki normal
with charachange


hh "どこか行きたいところがあるんじゃないかなって思ったから。観光したり、どこかのレストランで食事したいとか思ってないんですか？"


hi "どうだろう。ここには一度も来たことがないしさ"

show hideaki thinking
with charachange


hh "なるほど"


"小さい頃の静音はどんな感じだったのか、と聞こうと思っていたところだった。でもたった一つの質問ではぐらかされてしまう。今の会話は秀明にとっても、俺と同じくらい気まずいんじゃないか。"


hi "今日は熱心におもてなししてくれるね。なんでそんなに気を使ってくれるの？　お姉さんがいないから、隠していた心優しい自分を見せてくれてるとか？"


show hideaki bored
with charachange


hh "まあ割と合ってます。久夫さんが退屈しないようお世話しろって姉さんに言われたから"





"秀明に面倒をかけたくはないので、それをわかってもらおうとするけど、彼は静音と同じくらい頑固で、それが自分の義務か何かだと思っている。それに、俺に良くしようと真剣に努力しているのがわかる。"



"秀明が楽しいと感じるのは釣り、カメラ収集、それと難解なダジャレだった、と急いで頭の中で思い出す。"
"魚釣りはおもしろいけど、俺としてはそれを話題に話すよりは実際に手を動かしたい。カメラも同じだ。集めるよりは実際に使ってみたい。"



"俺の物思いに秀明が感づく。"




show hideaki normal_up
with charachange


hh "退屈ですか？"


hi "全然退屈なんてしてないよ"



"その言葉といっしょにあくびが出そうになるので、秀明にはまるっきり無視される。"


show hideaki sad
with charachange


hh "退屈なんだね。姉さんには楽しんでもらいなさいって言われたけど、どうすればいいかわからないよ"


hi "俺は楽しんでるよ"

show hideaki serious
with charachange


hh "楽しそうに聞こえないです"


hi "楽しんでるって！"

show hideaki normal
with charachange


hh "どうして大声出すんですか？　姉さんの周りでそんなに怒鳴ったりしてないですよね"



"冗談なのかどうか判断がつかない。どっちにしても少し驚かされる。その話は流して、話題を変えようとしてみる。"


hi "カメラは集めてるだけなの、それとも写真も撮ったりする？"

show hideaki bored
with charachange


hh "撮ってないです。撮ってたら、家の中は今よりも写真がたくさんあるでしょ。撮るものなんてどこにあるんですか？"


hi "さあ。鳥とか？　建物とか？　さっき言ってたレストランとか？　ここの町にはいけてるものが山ほどあると思ってたけど。ここならできることが本当にいっぱいあるのに、何もすることがないってどういうこと？"

show hideaki triangle
with charachange



hh "何をすればいいのかわからなかったんじゃないんですか。でもさっきから突然アイディアがぽんぽん出てきて、久夫さんは娯楽の権威ですね。役所の観光課みたいに。鳥や建物を見に行きたいんですか？"



hi "わかった、わかったよ。そんなに怒るなよ"

show hideaki normal
with charachange


hh "……怒ってないです。ただ、そんなにこだわるんだったら、遊園地に行けばいいんじゃないかって"


hi "どうして？"

show hideaki confused
with charachange




hh "久夫さんが退屈せずにすむから。遊園地で遊ぶのは楽しいですよ"







"こいつはジェットコースターやフリーフォールに乗っている間も、この無表情でつまらなさそうな顔をし続けるんだろうか？　それじゃこっちの楽しさも急降下だ。わざわざ行くだけの価値があるとは思えない。"





hi "それもちょっとな、前から遊園地って、実際に乗り物に乗るよりも列に並ぶ時間の方がずっと長いって思ってたから。並ぶのを避けるだけのために、今よりも早い時間に出なきゃいけないとかさ"

show hideaki normal
with charachange


hh "今まで遊園地に行ったことありますか？"



hi "ないけど、そういう感じに思えるな"


show hideaki bored
with charachange


hh "……じゃあいいです。普通の公園はどうですか？　近くに姉さんが気に入ってる公園があります。もしかしたらそこにいるかもしれないし。そしたら姉さんに丸投げします"




hi "『丸投げ』って何だよ？　俺は荷物じゃないぞ"

show hideaki triangle
with charachange


hh "遊園地にも行きたくないんでしょ。じゃあどうしろっていうのさ"


"まるで一緒に行くのを断ったから傷ついているみたいだ。早くも俺の頭は言い訳を考え始めている。列に並ぶのが嫌だ。これじゃデート同然だ。どうせなら静音と行きたい。きっとひどく気疲れする。"


hi "別にお前が嫌いとか、そういうわけじゃないから。ただ、静音に町を案内してもらう方がいいなあって思ってただけで"

stop music fadeout 2.0


"それに今の体調からすると、遊園地はあまりいいアイディアじゃないだろう。"

scene bg shizu_park
with locationskip

play music music_soothing fadein 0.5


"静音の家の敷地がその一部じゃないかと思えるくらい、公園は近いところにあった。公園と静音宅の裏庭はほとんど同じに見える。公園の方はベンチがあってもっと人が多いという違いはあるけど。"


"でも、とてもいい場所だ。犬の散歩をしている人もいるし、凧をあげている子供もいる。遠くで凧が木々の上でのんびりと前後に漂っている。こういうゆったりした景色のいい場所なら、いつまでだって座っていられる。"

show hideaki bored at center
with charaenter


"一方、秀明は非常に退屈しているようだ。突っついて生きているかどうか確かめたくなる。でも生きているかどうかに関係なく、こいつは反応するだろうか？"


hi "退屈してる？"

show hideaki normal
with charachange




hh "してないです。久夫さんはほかの人たちみたいに、ジョギングとか犬とフリスビーとかしたりするんですか？　公園に来る人ってそういうことするの？"




hi "あのさ、人は自然に戻って雰囲気を楽しむために公園に来るんだよ。だからどっかの歩道とかじゃなくて公園でジョギングするんだ。ジョギングなんてどこでだってできるよ"




hi "なんで俺こんなこと言ってるんだろう。そんなことも知らないってどういうことだよ？　なんて話題だよ本当に、おかしすぎるだろ。『子どもは大人の前でみだりに尋ねてはいけない』って言葉、聞いたことないか？"








show hideaki bored
with charachange


hh "あるよ"

show hideaki triangle
with charachange


hh "さっきは嘘ついた。退屈してる。ゲームしない？"


"やりたくないという意志が伝わるよう、聞こえるくらいの大きさでうめき声を上げる。秀明は気にもとめない。というか、すでにトランプの束をもてあそんでいる。"

show hideaki serious
with charachange


hh "なんでイライラしてるの？　そのためにここに来たんでしょ"


hi "ここに来たのは静音を探すためだろ"

show hideaki happy
with charachange


hh "そうだよ。だからゲームしようって言ってるの。静音トラップだよ。人だって何だって罠にかけられるんだ"

show hideaki thinking
with charachange




hh "スポーツマンらしく競争心を燃やしながらお互いに争っていれば、姉さんがそれにつられてやってきて、勝った方に戦いを挑んでくるってわけ。サメみたいに"
hh "そしたら、僕がサファリハンターみたいにやっつけて、表彰式の写真を撮るんだ"





"サメは道場破りよろしく、そこら中の人にゲームで勝負を挑んで回ったりはしないだろ。"



hi "いつの間にそのカメラ出したんだ？　とにかくやだよ。ゲームならお前の姉さんといやになるくらいしょっちゅうやってるからな"

show hideaki normal
with charachange



hh "いいから、やろうよ。面白いから。チェスもあるよ"




hi "頼むから勘弁してくれ。それに公園でチェスなんておじいちゃんのすることだろ、釣りみたいに。そうやって老人趣味してたら、あっという間に年寄りになっちまうぞ"



show hideaki darkside
with charachange



"俺がいきなり外国語をしゃべり出したかのように秀明が凍り付く。また怒らせてしまったんだろうか。もしかしたら秀明は実は５０歳だけど、とんでもなく童顔なのかも。静音の弟っていうのは作り話だったりして。"


show hideaki disapproves
with charachange



hh "じゃあチェッカーとか、囲碁は？　バックギャモンだっていいよ、あんまり好きじゃないけど。ボードゲームがつまらないなら、トランプでも。七並べ以外ならなんだっていい。あれは弱虫のやるゲームだから"


show hideaki evil
with charachange


hh "負けるのが怖いの？　僕に勝ったら飴あげるよ"


hi "秀明、お前本当に静音みたいだな。今までのは全部ゲームをするための前振りか？"

show hideaki thinking
with charachange


hh "違うよ。それは違う"


hi "違わないだろ！　そういう勝負好きなところも遺伝だろうな。科学者に売り払ってやる"

show hideaki normal
with charachange


hh "何人も他の人を所有することはできないんだよ"


hi "代わりに、俺がお前に手話を教えてやるってのはどうだ？"



hi "静音が俺をここに誘ってくれたとき少し話をしたんだ。お前とお父さんは手話がわからないんだろうって思った。ただの推測だけど、でもお前が知らないなら少しは教えてやれる。俺もそんなに上手じゃないけどな"



hi "それに、お前も少しは腕を動かした方がいいだろうし"


"秀明はほとんど腕を動かさない。たいてい、ただ体の横にだらんと垂れ下がっているだけだ。実に落ち着かない。"




"静音の一家が誰も手話を知らないというのも妙な感じだ。ミーシャに会うまではどうしていたんだろう。手話通訳でも雇ったのか？　あのいつも持ち歩いているメモ帳に全部書いていたのか？"



"メモ帳が一番ありそうだ。携帯に打ち込んだっていい。それならメモ帳を使うのをあれだけいやがるのも説明が付く。それは悲しいことだけど、秀明やお父さんがわざわざ手話を学ばなかった理由もわかる気がする。"




"そのときは手話を学ぶのが大変すぎたんだろう。想像するのはたやすい。ただ今まで見てきた限り、二人ともそのことでお互いを責めたりしないし、悪影響を受けているようにも見えない。考えすぎかもな。"




hi "やってみようぜ。正直言うと、俺もまだ手話を勉強してる最中なんだけど。忘れたりしないように教科書とか全部ここに持ってきてるんだぜ？　それでも５０音くらいなら教えられるから。簡単だよ。これが『凧』"



"おそろしく格好悪い気分だ。学ぶという概念そのものが理解不能とでも言いたげに、秀明がぽかんとした目で見つめ返してくるので、よけいにその気分が強まる。"

show hideaki bored
with charachange


hh "姉さんはここで凧を飛ばすのも好きだったよ"


"今のは、彼なりに会話を取り繕おうとしているのだろう。喜んでそれにつきあう。"


hi "魚釣りの次は凧揚げか？　ほんとに静音はそういうのんびりした趣味が好きなのか？"

show hideaki thinking
with charachange



hh "凧同志で戦うんだ。実は姉さんは――{w=0.5}{nw}"


stop music fadeout 0.3

show misha cross_grin_cas behind hideaki:
    center
    ypos 1.1 alpha 0.0
    linear 0.2 ypos 1.0 alpha 1.0
show hideaki ohshit
with vpunch


"後ろから現れたミーシャに手で目隠しをされて、秀明が体をこわばらせる。"

play music music_comedy fadein 0.5


mi "こんちはこんちは～！　だーれだ！"


"秀明もようやく緊張がゆるんだみたいだ。"


hi "ようミーシャ。静音も一緒か？"


mi "ひっちゃん、ネタばらし禁止！　禁止だからね、せっかくのドッキリをだいなしにしないの、い～い？"

show hideaki thinking
with charachange


hh "ミーシャさん"

show bg shizu_park at bgright
show hideaki normal at tworight
show misha perky_confused_cas at twoleft
with dissolvecharamove


mi "あったりー！　そうだよ！　でも～、今のはわかりやすすぎたね、なんだか"


"『なんだか』ってのはどういう意味なのかわからない。"

show misha hips_frown_cas
with charachange


mi "みーんなわたしだってわかっちゃうんだもん！　たまにはびっくりさせたいよ！　秀明くんなら絶対引っかかると思ったのに～。どうしてわかったのかな、ん～？"

show hideaki bored
with charachange


hh "こんなことするのはミーシャさんしかいないから。ミーシャさんと誘拐犯だけ"

show misha cross_laugh_cas
with charachange


mi "ほんとに？　わはは～！"

show hideaki serious
with charachange


hh "何がおかしいの？"

show shizu invis:
    center
    xpos 0.1
with None

show bg shizu_park at left
show misha cross_laugh_cas at Position(xpos=0.4)
show hideaki serious at Position(xpos=0.8)
show shizu basic_angry_cas at Position(xpos=0.2)
with dissolvecharamove


ssh "久夫を困らせてるんじゃないでしょうね？　公園よりは面白みのある場所に連れて行くと思ってたけど。家からだってそんなに離れてないじゃない。ほんとに怠け者ね"

show misha hips_frown_cas
with charachange


mi "秀明くん、ひっちゃんを困らせてるの？　もっと面白いとこに連れてかなきゃだめだよ！　公園は家にだって近すぎるし、しっちゃんがこの怠け者って言ってるよ～"

show hideaki bored
with charachange


hh "久夫さんが来たいって言ったんだよ。どうしてそんなに突っかかるの？"

show shizu behind_frown_cas
with charachange


ssh "弟をきちんとしつけないといけないからね"



show hideaki triangle
with charachange


hh "なんて言ってるの？"


hi "しつけだってさ"

show hideaki serious
with charachange


hh "マジで……"




"いつでも相手ののど元につかみかかる準備ができてるってことか。でも姉弟げんかというのはそんなに珍しくないと聞いたこともある。"
"そしてけんかしているということ自体が、二人の間である程度のコミュニケーションがあるという証だ。だったら、二人がうまくやっているのはいいことだ。"




scene bg shizu_houseext
with locationskip

stop music fadeout 4.0


"家に帰り着くまで二人は言い争いを続ける。静音にはミーシャが、秀明には俺が通訳する。"
"だからミーシャと俺が言い争っているように見えるけど、実際にはそうでもない。ミーシャの話し方を聞いてそんなことを信じる人はいないだろう。"



"少なくとも、最後には面白い一日になったな。"

$ suppress_window_after_timeskip = True

scene black
with dissolve



label jp_S20:



window hide None

scene black
with dissolve

show bg shizu_guesthisao
with openeye

window show


"まだここに来て二日しか経っていないのに、ずっと長い間滞在しているような感じがする。目が覚めてもすっきりしたというより、疲れた感じがする。こっちに来てからずっと動き回ってばかりだからかもしれない。"


"理由がなんであれ、おかげで毎日おかしなくらい遅くまで寝てしまっている。朝寝坊は好きだけど、くせになってしまったら厄介だ。"



"遠くで男性が大声で叫ぶ太い声が聞こえる。静音の父さんに違いない。このお屋敷の大きさを考えたら借金取りかもしれないけど。聞く限りでは怒っている感じではなく単に声が大きいだけなので、それはないだろう。"


scene bg shizu_living
show hideaki normal:
    center
    xpos 0.5
show misha perky_smile_cas:
    center
    xpos 0.3
show shizu basic_normal_cas:
    center
    xpos 0.08
show jigoro smug:
    center
    xpos 0.87
with charaenter

play music music_another fadein 0.5



"居間に座っている静音、ミーシャ、秀明が、脚の上に載せたお皿から食事を食べるのと、剣を振り回すのを交互に繰り返す、熊のような大男に一方的に話しかけられている。"










"静音と秀明の見た目からして二人の父親はとても控えめで上品な、場合によっては中性的な人物だろうと思っていた俺は、その人が話しかけてくるまで度肝を抜かれていた。"





show jigoro laugh
with charachange


hx_ "おう！　静音のもう一人の友達だな。昨日はよく眠れたか？　ゲストルームはあまり物がないからな、必要な物があったらいつでもわしに言うようにな"





hi "どうも。静音のお父さんですね。はじめまして。同級生の中井久夫です"

show jigoro neutral
with charachange


hx_ "こちらこそよろしく。会いたいと思っていたのだよ、我が家に来客が一人増えると聞いた後ではな。予想外だ。そんなことを聞いたら、それがどんな人物か知りたくなるのは当然というものだ。名刺は欲しいかね？"



$ renpy.music.set_volume(0.5, 1.0, channel="music")

show jigorocard:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)



"名刺の詰まったケースを手にとって見せる。名前が治五郎であること、営業時間が８時から６時であることが読みとれる。それと職業は『コンサルタント』だ。"
"用意のいい人だな。自宅の中でも名刺ケースを持ち歩いているなんて。"


$ renpy.music.set_volume(1.0, 1.0, channel="music")

show jigorocard:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide jigorocard
with None

show jigoro smug
with charachange


hx "ちょっと遅めの昼食をとっているところだ。ちょうどいいところに来たな。よろしい。席に座りたまえ。皿を取ってこよう。熊の肝臓が嫌いでなければいいが"


"熊の肝臓は毒じゃなかったっけ。とにかく、周りの人にその経験を吹いて回れるという以外に、熊の肝臓を食べることには魅力を感じない。まあ食べたところで死にはしないだろうけど。でも静音の父さんは笑うだけだ。"

show jigoro laugh
with charachange


hx "ただの冗談だ。とはいえ、熊の肝臓をお前たちに料理してやるのは悪い考えではないかもしれんな。強くなれるぞ"

show jigoro neutral
with charachange


hx "本当はオムレツを食べておる。今作ってやろう。君は昼飯にオムレツというのは珍しいか？"

show hideaki triangle
with charachange


hh "とても珍しいね"


hi "いえ、全然そんなことないです"

hide jigoro
with charaexit


"治五郎さんはキッチンがあるとおぼしい場所へ消える。こんな場所に住んでいるのに、お父さんが俺の食事を作らないといけないという事実に驚く。料理が好きなだけかもしれないけど。"

show jigoro smug:
    center
    xpos 0.87
with shorttimeskip


"湯気の立つ料理があっという間に運ばれてくる。とてもいい匂いだ。"


hx "お前も静音と同じで、生徒会に入っているのか？　生徒会というのは、静音がどこに行くにも友達を引き回さないといけないくらい忙しいものなのか？"

show shizu behind_blank_cas at Position(xpos=0.12)
with charachange



ssh "今回は文字通り旅行よ。そういうときもあるわ"




hi "生徒会のところは合ってますよ。でもここに来てるのは純粋に遊びです"

show jigoro neutral
with charachange



hx "なるほど。そうなのか？　わしが若い頃は、生徒会は余りに仕事が多くて、旅行に行くなど考えられなかったがな。そんなに自由な時間があるとはすばらしいな。将来のことを考える時間がたっぷりとれるだろう"



"話が怪しい方向に向かっている。俺はうまくかわす方法を考え始める。"



hx "考えてもみたか？　将来のことについて"



hi "いえ、最近はあんまり。聞いてよければ、おじさんはどんなお仕事をしてるんですか？　こんなお屋敷に住めるんだから、きっとすごい仕事だと思いますけど"

show jigoro angry
with charachange


hx "なぜそんなことを聞く？　子供というのは商売に興味など持たんのだ。わしの仕事がお前に何の関係がある？　怪しいぞ。まさか税務署の回し者か、小僧？"


"質問を聞かれるのはマジで好きじゃないみたいだな。"

show misha hips_grin_cas
with charachange


mi "ひっちゃんは税務署の人の子供じゃないと思うよ～。ひっちゃん、ご両親はなにしてるの？　一度も聞いたことないよ～！"


hx "何だお前は、黙らんか。話の邪魔をするな。邪魔をされるのは実に好かん。失礼な"

show misha perky_sad_cas
with charachange


mi "あ～……"

show shizu basic_normal2_cas at Position(xpos=0.08)
with charachange


"静音もこの展開には不愉快そうだ。ミーシャが状況を手話で伝えられなくても、この雰囲気を読みとるのはたやすい。治五郎さんががなり立てているうちに、静音の視線がどんどん険しくなっていく。"


hx "それにだ。わしの釣り道具だがな。家に帰ってみれば、部屋の隅でぐちゃぐちゃの山になっておった。釣り具の上に竿がでたらめに積み重なっているだけだ"

show hideaki thinking
with charachange


hh "あ、それ僕"


"秀明だったかどうか、良く思い出せない。違うのなら、俺たちのために泥かぶりを買って出てくれるのはありがたい。でも治五郎さんには一瞬も省みられずに無視されてしまい、それも徒労に終わる。"


show jigoro smug
with charachange



hx "うむ。とにかくだ。娘のご友人のお楽しみにわしの釣具が大いに役立ったというのは喜ばしい。使いたいという断りの一言もなかったな。あれは値の張る、特注の竿なのだぞ。好事家の素人にはもったいない代物だ"



"突然、オムレツの中に卵の殻のかけらが入っているのに気づく。治五郎さんの料理が下手なだけなのか？　カルシウムのために食べてるのか？　俺の居心地を悪くするためにわざと入れたっていうのか？"



"混乱はしているけど、今の自分は思ったよりも落ち着いている。だって俺の人生は最近変なことばかり続いているし、様々な人物に出会ったりもしている。もう何があっても驚かない。"


show jigoro angry
with charachange


hx "使った後でちゃんと洗いもしないとは。最悪だな"



hx "そもそも釣りのやり方など知っとるのか？　知らんに決まっとるな"
hx "大体全員分の竿もない。数が合わんじゃないか。交代で使ったのか？　一人が餌を針にかけて、もう一人が投げるのか？　糸を引くときも二人がかりか？　ど素人め"





hi "まあ、六人で行ったんで、みんなで一度にはできませんでしたけど。最初は僕と晃さんと、秀明くんとミーシャで"


hx "黙らんか。あまりの汚さに言葉もないわ。その汚い口の聞き方、我慢ならん。なんという下品な。そのような恥ずかしくなるほどぞんざいな言葉遣いは二度と許さん。わかったな"



hi "何ですって……?"


hx "『何ですって』だと？　無礼千万な。これは驚きだ。不良というのはみんなこうなのか？　その服装も目上の者に対する生意気さ、敬意のなさの表れだな。セーターベストだと。はしたない……"


hi "不良？　俺は生徒会に入ってるんですよ"


"セーターベストのことを悪く言われて俺は傷つく。こんな悪趣味なシャツを着たおっさんに言われたらなおさらだ。でも何も言い返せそうにない。相手は剣を持っているし。熊を殺してるかもしれないし。"

stop music fadeout 0.3
play sound sfx_impact
with vpunch


"ミーシャが大きな音を立ててお皿をテーブルに置く。"

show misha hips_smile_cas
with charachange



mi "おいしかった～！　しっちゃんとわたしはごちそうさまだよ。ひっちゃんもだよね、ね～？　そろそろ行かなきゃ！"



"なんて単純かつ効果的な脱出方法だ。"

scene bg shizu_houseext
with locationchange


"お皿をちゃんと置く間もなく、二人が俺を引っ張り上げて居間から連れ出し、屋外へ出る。"

show shizu behind_frustrated_cas at tworight
show misha perky_confused_cas at twoleft
with charaenter


shi "……"

show misha sign_confused_cas
with charachange


mi "信じられない～！　尋問の現場を見てるみたい～！　警察ドラマじゃないんだから～！　そりゃあ客にだって責任はあるけど、寛大な宿主になるってこと、考えたこともないの～？　ほんとに～！"



"ミーシャは精いっぱい手を振り回して、静音の怒りをいい加減ながらも再現しようと試みる。表情は控えめだし、声の調子も相変わらずなので、元の表現をうまく伝えるのに必要な怒りの感情がすっぽり抜けている。"




show misha hips_smile_cas
with charachange


mi "わはは～。あんまり気にしちゃだめだよ、ひっちゃん～！　しっちゃんのお父さん、誰にでもああなんだから。ジョークみたいなものだと思うよ～"


hi "今までで一番アグレッシブなジョークだったよ"


"こんなに急いで脱出したことを考えれば、あれが冗談だったと言われてもまるで信じられない。でも今は、静音の父さんが実はクソ親父かもしれないなんてことを話している場合じゃない。"

play music music_shizune fadein 4.0

show misha sign_smile_cas
with charachange


mi "ひっちゃん、ショッピング行こうよ！"

show shizu adjust_happy_cas
with charachange


ssh "まだ町には行ったことないんでしょう？　楽しいわよ。いろいろ見物もできるし、遊園地にも行けるし。いいレストランで食事もいいわね"


hi "昼飯食べたばっかりだろ"


"俺はあまり食べてないけど。"

show shizu behind_smile_cas
with charachange


ssh "大丈夫よ。それなら今日は気づいたときには夕食の時間になってるくらい、思い切りいっぱい遊んでくればいいから"

show misha cross_grin_cas
with charachange


mi "ばっちりだね～！　いこ、ひっちゃん～！"

show shizu behind_smile_cas_close at closeright
show misha cross_smile_cas_close at closeleft
with characlose



"二人がすぐに俺の左右について腕を絡めてくる。静音が片方、ミーシャがもう片方。最初はお互いにつまずきそうになる。静音はとても歩くペースが速くて、ミーシャは妙にはずむような動き回り方をする。"


scene bg shizu_park
with locationchange


"すぐに感じがつかめてきて、俺たちは公園を通り抜けて町に向かっていることに気づく。近道には見えないので、これは景色のいいルートなんだろう。"


"こういう歩き方をしていると、お互いにコミュニケーションを取るのが大いに妨げられる。静音とは全く話せないし、静音とミーシャは片手のジェスチャーしかできない。でも気分はいいので、あまり気にはしない。"


"そのことをミーシャに伝えると、ちょっと混乱した様子で答えてくる。"


show misha perky_confused_cas_close at closeleft
with charaenter


mi "ひっちゃん、ほんとに～？　んー……ほんとにしっちゃんに気づいて欲しいなら、わたしに言ってくれたら、かわりにしっちゃんの肩叩いてあげるよ"


hi "俺を離してくれればいいだろ。そしたら自分でやるよ。どうやってそっちから静音の肩を叩くってんだ？"

show misha hips_grin_cas_close
with charachange


mi "こうやってだよ～！"

with vpunch

show shizu behind_frustrated_cas_close behind misha at closeright
with charachange


"ミーシャが強引に足を止めて、背中から俺の肩を越えて静音の気を引こうとする。確かにうまくいったけど、それはミーシャが立ち止まったときに俺も止まったからだ。さもなければみんなで転んでいた。"

show misha hips_laugh_cas_close
with charachange

show shizu adjust_blush_cas_close
with charachange



"もちろん静音も急停止するはめになっていた。それを見てミーシャがいつもの笑い声を上げて、よけいに俺たちもぐらぐらと揺さぶられる。"
"静音が空いている方の手でミーシャを止めようとするけど、よけいに笑い声が激しくなるだけだ。"



"静音がそんなにあわてふためくのを見るのはとてもおかしくて、俺も笑い出してしまう。"

stop music fadeout 2.0

scene black
with dissolve



label jp_S21:



scene bg shizu_guesthisao
with locationchange

play music music_dreamy fadein 2.0


"しばらく手話の勉強をさぼっていたので、少し手話に時間を割かないといけない気がする。でも今までの見よう見まねだけで、かなりいい線行っているんじゃないかと思う。"
"我ながらとても満足しているけど、自慢しないよう気をつけないといけないな。"




"旅行に持ってきた本のほとんどは、手話の入門書とかではなく、さまざまな手話の『方言』についての研究書だ。静音がミーシャとの間だけで通じる秘密の合図を使っていることには、俺も気づいている。"




"そういう合図をいくつか見かけてから、学校の図書室でこの本が目に入った。"


"あいつらにちょっかいをだすために、自分の手話にもそういう実例を取り入れるのがいいかもしれない。俺が手話を学び始めてから、そういう暗号を使うことが増えたのは確かだからだ。あいつらに思い知らせてやる。"




"休憩がてらに短いシャワーを浴びてから、ゲストルームの鏡に向き合って手話の練習に戻る。昨日はかなり強く指同士をぶつけてしまった。今でも痛みでうずいているし、同じことを繰り返したくはない。"

play sound sfx_doorknock2

show hideaki normal at center
with charaenter


"背後でドアのノックが聞こえて、振り返ってみるとドアの内側に秀明が立って、こっちを見つめている。わざわざノックしてくれるとはご丁寧に。でも普通はドアを開ける前にノックだろう。"

show hideaki triangle
with charachange


hh "何してるの？"


hi "手話の練習だよ。いつからそこに立ってた？"

show hideaki thinking
with charachange


hh "僕、何も見てないよ"


"そういう問題じゃないだろ。大体それどういう意味だ。人に見られて恥ずかしいようなことをしてたわけじゃないんだから。"



"とはいえ、普通の人には手話は変てこに見えるに違いない。俺が違和感を覚えないのは、静音やミーシャと一緒に長い間過ごしていたからというだけだ。"



hi "手話を復習してるし、参考書も読んでる。手話の歴史とかね。授業でもやってはいるけど"

show hideaki normal
with charachange


hh "山久には手話の授業があるの？"


hi "ああ。そういう授業はあまり一般的じゃないってことは最初に教わったよ。山久はすごくインターナショナルというか、そういう感じなんだろうな"






show hideaki serious
with charachange



hh "面白そう"



hi "いや、面白いとは言わないけどな"

show hideaki bored
with charachange


hh "面白くないんだったら、わざわざ姉さんと話をするだけのためにずいぶん大変なことをしてるんだね"




hi "なんでみんなそう言うんだ？"



show hideaki happy
with charachange


"秀明の口が今にも笑い出しそうにひきつるけど、こらえる。そういえばこいつ、会ってから一度も笑うのを見たことがないな。ここで笑い出さないのは気遣いともとれるけど、こいつの笑顔は見てみたいな。"


hi "笑えよ"

show hideaki thinking
with charachange

stop music fadeout 4.0


hh "……"

show hideaki bored
with charachange


hh "どうして？"


"直接言うのが一番手っ取り早いと思ったからだよ。"



show hideaki normal_up
with charachange


hh "手話を教えてくれる？"



"何の気なしに言うけど、身振りからは緊張が伝わってくる。"
"こういう頼みごとをするのに慣れていないのが明らかだ。やっぱりお姉さんのことが好きなんだな。でもミーシャの方がよほど近づきやすいだろうし、どうしてあいつに頼まなかったんだろう。"




"密かに心の中で『やりい！』と叫ぶ。秀明には手話を覚えてほしいと思っていたし、それを話題にしたりもしたけど、こいつは巧みに話を避けてきた。"
"やっぱり俺は正しかったんだ。どうしてこんなにうれしい気分になるのかよくわからない。"



hi "もちろん"


"でもよく考えると、俺は手話の先生じゃない。どこから始めればいいのか見当もつかない。授業では一週間かけてゆっくり学ぶ。秀明はたった一日の集中コースで俺が役に立つ手話を教えられると思っているんだろうか？"

show hideaki normal
with shorttimeskip

play music music_normal fadein 3.0


"俺の手話の先生は、手話の歴史だけで二、三日かけて教えた。俺もそこから始めることにする。それで時間を稼ぐ間に、うまく実技につなげる方法を考えよう。五分たった後、秀明が手を挙げる。"


show hideaki serious_up
with charachange


hh "何をやってるのかわからないよ"


hi "あー……その、いきなり手話を教えるのは無理があるんだよ。こういうのは徐々に入らないと。泳ぐ時みたいにさ、どっかの映画みたいにいきなり湖に飛び込んだりはしないだろ"

show hideaki triangle
with charachange


hh "僕、泳がないし"


"どっかの科学者が小さな子供から活発さや腹立たしい、子供っぽい性質を全部吸い出して父親に植え付ける方法を発明したかのようだ。結果として怒り狂うクソ親父が生み出され、後に秀明が残ったんだ。"




"閉所恐怖症にかかった気がしてくる。ゲストルームは俺の寮の部屋より三倍広いし、部屋の中には俺たち二人しかいないのに。考えすぎなだけだ。わかってるし、どうでもいい。"
"それでもそれを口実に、レッスンを外で続けることにする。"


scene bg shizu_garden
with locationskip


"ここならずっと集中しやすい。外に出るまでのわずかな時間でさえ、考えをまとめるのに役立った。その間に質問はなかった。秀明は歩きながら話すということができないらしい。"



"でもそのうちに、満足に何かを教えるなら授業をどんどん先に進めないといけないことに気づく。一秒でも間が空けば、秀明は質問をしてくる。その質問が別の質問につながる。きりがない。"




"この手の動きはどうしてその意味なのかという二度目の質問を受け、俺は勉強し始めてせいぜい一ヶ月くらいでしかない手話の、知りもしない語源について記憶を掘り返す羽目になる。そろそろ逃げ出したくなってくる。"






hi "秀明、ちょっと休憩しよう"

show hideaki bored
with charachange


hh "うん"

show hideaki serious
with charachange


hh "久夫さんの学校ってどんな感じ？"





"まるで小さなレポーターだな。でもこの年の子が好奇心旺盛なのは自然なことだし、こういう質問なら聞かれても答えられる。"






hi "どんな感じって？　まともに考えたことなかったな。山の上にあるから、ときどき隔離されてて寂しいって思うことはあるな。そのおかげで景色がすごくいいってのはあるけど"


hi "生徒は面白い奴らだよ。ほんとのこというと、最初は嫌だったんだけど。山久がどういう学校かは知ってるだろ？"



show hideaki normal
with charachange


hh "うん"



hi "嫌だっていうのは、山久には行きたくなかったんだ。あのときどういう気持ちだったのかはもう思い出せない"
hi "たぶん、障害児のための学校なんて気が滅入るに違いない、なんて思ってたんだろうな。そこに放り込まれて忘れ去られてしまえ、って言われてる気がした"



hi "そしたら、みんな自分なりの人生を普通に過ごしてるんだ。大体は。だから余計に嫌な気分になった。その人生は他の人と何も違わなくて、自分がひどい奴に思えてさ"




hi "学校で最初に出会ったのが静音だったんだ。ほとんどの授業は一緒に受けてる。ミーシャもだな。あの二人はいつも一緒にいる。山久はあいつらをできるだけ組ませるくらいに融通を利かせてるんだろうな"
hi "華子って女の子もいる。気の毒だなって思うんだけど。体をやけどしててさ。そのことでコンプレックスを抱いてる。でもきれいな子だと思うんだ。かわいい子だよ。あとリリーとも仲がいいし"




hi "リリーは知ってるだろ？　華子のことは話したりする？"


show hideaki thinking
with charachange


hh "うん、ときどき"


hi "ほかに誰か面白い奴がいたかな。義足をつけてる、ちっちゃな陸上部のエースがいるな"



hi "あと琳っていう女の子がいて、そいつは腕がないんだけどものすごく絵がうまい。琳の描く絵はこう、荒々しくて生き生きしてる。山久に行ったことはある？　何枚かあいつの絵がかかってるのを見てると思うぞ"



hi "ちょっと変なところもあるけど、芸術家とかクリエイター的な人はそういうものだってよく聞くし。そういえば、寮で向かいの部屋に住んでる奴もすごい変な奴なんだ。そいつもまあ、時々は面白い奴だけどな"

show hideaki normal
with charachange


hh "久夫さんも面白いよ"


hi "悪いかよ？　なんだよその言い方は？　大体どういう意味だ？　俺が変だって言いたいのか、秀明？"

show hideaki triangle
with charachange


hh "いっぱいしゃべるんだね"


"本能的に守りに入ろうという衝動がわく。でも考えてみればみるほど、秀明の言うとおりだ。"



hi "そうだな、確かにいっぱいしゃべってるな。前はそうでもなかったと思うけど"




hi "たぶん……静音やミーシャとずっと一緒につるんでるからじゃないか。あの二人と話してると、あいつらの堂々巡りの話し方とか、物事の進め方全部に巻き込まれて圧倒されるっていうか、置いて行かれる気分になる"



show hideaki confused
with charachange


hh "姉さんは久夫さんを圧倒できるの？"



hi "本当に言い負かされてるわけじゃないぞ、当たり前だけど。説明しづらいな"
hi "あいつらは俺よりも活気があるんだ。アグレッシブさみたいな。別に張り合う必要は感じないけど、張り合いたいって思うんだ。静音は周りの人にそういう影響を与えてるのかもな"


show hideaki thinking
with charachange


hh "……"


hi "お姉さんのこと、尊敬してるか？"

show hideaki normal_up
with charachange


"無表情な顔で俺を見つめる。俺の質問にどう答えるべきか思案するように、困惑と緊張が浮かぶ。"

show hideaki angry_up
with charachange

stop music fadeout 5.0



hh "僕は姉さんよりもすごくなるよ"




hi "どうすごくなるんだ？"

show hideaki angry
with charachange


hh "どうって……なにもかもだよ"


hi "たとえば？"

show hideaki triangle
with charachange


hh "僕、マジックできるよ"


hi "それって、観客の鼻を盗んだって脅かすとか、ケツからウサギを取り出すとか、そういうマジックのことか？"



"不愉快そうな顔だ。いつの日か、こいつの笑い顔を拝んでやる。必要とあらばくすぐってやってもいい。"

play sound sfx_doorslam

show hideaki surprise
with vpunch

show hideaki thinking at twoleft
show bg shizu_garden at bgleft
with dissolvecharamove

show jigoro neutral at tworight
with charaenter



"裏口のドアがバンと開き、治五郎さんが飛び出してくる。背筋はまっすぐで、幅広でゆっくりとした、堂々たる歩みだ。その姿は王様か、さもなければお山の大将だろう。"






"俺の目に見えなければ向こうにも見えないだろうという思考が働き、俺は背を向けようとする。そんなわけもなく、しかも治五郎さんがものすごい早さで近寄ってくるので、肩越しに突然姿を現したような状態になる。"


show jigoro laugh
with charachange

play music music_happiness fadein 2.0


hx "ほほう、なんだこれは？　こんなところで手を振り回して、二人とも何をしている？　女子のまねをしてあやとりか？"


hi "秀明くんに手話を教えてるんです。おじさんこそどうしたんですか？"



show jigoro angry
with charachange


"怪しむように目を細める。まるで礼儀正しくされるのに慣れていないかのようだ。"


hx "自分の人生と時代について自伝を書いておるのだ。『書く』と言うのは、伝記作家に口述で書かせておる。あいにく作家どのは遅刻しているがな。不真面目きわまりない"






show jigoro smug
with charachange


hx "今年の後半には出版されるから、読んでみるといい。予約者リストに入れておいてやるぞ。お前の人生に欠けている道徳的な指針というものが得られるかもしれないぞ。己の未熟さを脱するきっかけになるだろう"



"あらゆる人に向かってこんなに平然と侮辱をまきちらしていて、人生が成り立つはずがない。"
"でも秀明は無関心すぎて気づきもしないだろうし、静音には聞こえていないし、ミーシャにはほとんど理解できていないだろう。晃さんならきっと思うところがあるに違いない。"




"気にするな。俺を参らせようとしているのだとしたら、冷静さを失ってはいけない。さもなければあっちの勝ちだ。とにかく、絶対に、この親父に勝ちを与えてはだめだ。きっと静音の気持ちもこれと同じなんだろう。"





hi "おじさんは、今何歳ですか？"

show jigoro neutral
with charachange


hx "４６だ"




hi "自伝を書くような年齢には思えないですね。というか、そもそも年寄りとも言えないじゃないですか。普通はもっと年取ってから回想録とか書くものじゃないんですか？"

show jigoro angry
with charachange


hx "黙れ小僧。一つ忠告してやる。年長の者相手に年齢の話をしてはならん。お前はわしの半分の年もない。お前に老いを語る資格などないわ。わしにはお前の年よりも古い胃潰瘍があるのだぞ"


"それは医者に診てもらえよ。でもそこはその通りで、治五郎さんは確かに俺よりも年上だ。"

show jigoro laugh
with charachange


hx "……ともかく、同い年だったとしても、わしのことを説明する必要などないな。セーターベスト君"


hi "うぇ"

show jigoro angry
with charachange



hx "なぜそのような妙な音を立てる？　気でも違ったか？　まあ聞くまでもないな。よかろう。そのセーターは最悪だし、お前にはその最悪ぶりを悔やんでほしいものだ。この胸焼けからすると、効いているようだな"




hi "このセーターは気に入ってるんですよ"

show jigoro smug
with charachange




hx "おおかたシンナーなど吸ったりしておるのだろう。そんなことでそのセーターが正当化されはしないぞ"






hi "シンナーなんて吸いませんよ。どこからそんな発想が出てくるんですか？"

show hideaki normal
with charachange


hh "それは中傷だよ"


"どこで中傷の意味を知ったんだろうか。治五郎さんは弁護士なのかもしれない。わからなくもないけど、ここまで悪役じみた弁護士はテレビにしか出てこないと思っていた。この機会に職業も聞いてみるべきだろうか。"


hi "そうですよ。中傷です。おじさんは弁護士ですか？"

show jigoro neutral
with charachange



hx "今のは推測だ。お前がバカだという事実に基づいた推測だ。今お前が、わしが弁護士だろうと仮定したようなものだ"
hx "ただお前にはそう仮定する理由は何もない。わしの仕事がそんなに知りたいなら、わしの自伝を予約したらどうだ？"


show jigoro angry
with charachange



hx "お前はわしの本を、ひいてはわしの人生そのものを侮辱しているぞ。何の権利があってそんなまねをする？　無礼者めが"
hx "わしは自分の苦闘をお前にわからせる方法を考えているのだ。殴れば伝わるかもしれん。わしの自伝でな"





hx "わしの指導で貴重な教訓を得て帰るが良いぞ。たとえば物事を決めつけない、などとな"



show hideaki bored
with charachange


hh "傷害罪だ……"


"でもそっちだって俺がシンナー吸ってるって決めつけてるじゃないか。その露骨な偽善を突っ込んでやりたいけど、やったって無駄だろう。どうせ『黙れ小僧』の一言でかわされるだけだ。"

show jigoro smug
with charachange



hx "わしの若い頃は、子供というのは無駄口を叩かずに黙っていたものだ。大人になるというのは幾多の苦難を経験するということだった"
hx "一目見るだけで人となりというのはすぐにわかったのだ。子供時代は人間を成熟した大人へと鍛えるための存在にすぎなかった"



hx "わしを見れば、わしが経験してきたあらゆることを一目で見て取れるはずだがな？"


hi "ええと……そうかもしれません。剣闘士だったとか？"


"それとハワイ出身で、狼人間だったりして。"




hi "待ってくださいよ、勝手に推測するなってさっき言いませんでしたか？　でも今は推測しろって言ってる"
hi "しかも自分が俺くらいの年だったときはみんなそうしてたって。そんなのせいぜい８０年代ですよね。たいして昔でもないじゃないですか！"




"通学するときは雪の中を石炭を運ぶ列車に乗るために３０キロ歩いたとか、自分で石炭をくべたとか、そのあと山に登って怪物と戦ったとか、そう言わんばかりの話しぶりにそろそろ反撃をかましてやる時だ。"





"でもようやくやりかえしてやろうと思ったところで、治五郎さんはことがうまく進んだのに満足して、自分の世代がいかに苦労して育ったかを延々話しているだけだ。"
"その間バトンのように剣を振り回したり、ときどきあくびをしたり時間を確かめたりしている。"






"今も自伝作家の人が遅れているのが一番気になっているようだ。つまり今まで延々俺のことを侮辱し続けていたのは、ただの暇つぶしだったんだろう。治五郎さんの時計がとても上等なのが、余計に不愉快だ。"

show jigoro angry
with charachange



hx "……わしがお前くらいの年の時は、子供にも責任感というものがあった。今とは大違いだ"
hx "反吐が出る。誰も自分の行動の結果を考えることもしない。若いから誰にも責任を問われないと思って、ただやりたいことをやっているにすぎん"



"変だな。その説明は静音とミーシャに当てはまる気がする。昨日も似たようなことを考えたけど。でもほんのちょっとしか当てはまらないな。"


hx "お前自身はどうだ。道徳心のない、目標もない、不良のシンナー吸い、礼儀もまるでなっていない、服のセンスも皆無だ。お前が日本の明日なのだぞ。実にふがいない。これがかつての大国の未来だというのか？"



hi "おじさんと馬が合いそうな奴が知り合いにいますよ"



hx "話の邪魔をするな！　お前の友達か？　そんなろくでもない若者など話す気も起きん。人の話を聞いていないのか？　なぜそう無礼なのだ、小僧？　そのような態度では友達も少なかろう"


hi "いいかげんそのご忠告をやめてもらえませんか"





"少なくとも、自分で従うつもりがある忠告だけにしてほしいんだけど。"




show jigoro neutral
with charachange


hx "どこに行っていた？"


hi "は？"

show jigoro angry
with charachange

stop music fadeout 3.0


hx "お前ではない、馬鹿者"

show jigoro angry at Position(xpos=0.85)
show hideaki normal at Position(xpos=0.45)
show bg shizu_garden at center
with dissolvecharamove

show shizu behind_blank_cas behind hideaki:
    twoleft
    xpos 0.2
with charaenter


shi "……"


hi "悪い。いたの気づかなかった"

show shizu adjust_happy_cas
with charachange


"静音が笑顔を見せ、短く手を振る。静音が来たおかげで治五郎さんの話が止まったので、そのことだけでも静音の姿を見られたのがありがたい。"

show shizu basic_normal2_cas
with charachange


ssh "ミーシャと二人でまた町に行くことにしたの。久夫、昨日お店の前で服を見てたでしょう。だからもう一回行って何着か買ってきてあげようって思って。本当はサプライズにするつもりだったんだけど"




"サプライズにならなくて不機嫌そうだ。ばらしたのは本人だけど。"

show shizu behind_blank_cas
with charachange


ssh "どうぞ！"


hi "ありがとう"

show shizu basic_normal_cas
with charachange


ssh "ミーシャが髪を切るって言ってたの。やめたらって言ったんだけど、夏には暑すぎるんだって言って"


hi "ほんとか？　どうだろうな。もっともだと思うけど。あの髪の中はオーブンみたいになってるんじゃないか。見てみたいな。ミーシャはどこだよ？"


mi "ここだよ～！　こんちはひっちゃん～！　こんちはしっちゃんのお父さん～！　こんちは秀明くん～！"

show jigoro smug
with charachange


hx "……"

play music music_running

show mishashort hips_grin_cas behind shizu at offscreenleft
with charamoveinright

hide mishashort
with None

show mishashort hips_grin_cas at offscreenleft
with None

show shizu basic_normal_cas:
    xpos 0.3
show jigoro smug:
    xpos 0.95
show hideaki normal:
    xpos 0.55
show mishashort hips_grin_cas:
    center
    xpos 0.1
show bg shizu_garden:
    xpos 0.55
with dissolvecharamove


"ミーシャは俺たち全員の周りを走って一回りしてから、静音の隣で立ち止まる。"



"初めてミーシャが俺に目隠しをしてこなかったけど、両手に袋を持っているのを見ると、やりたくてもできなかったんだろう。でもきっとやろうとはしていたに違いない。"


"念入りに形作られた巻き髪はなくなっていて、ずっと短くてさっぱりした髪型になっている。ミーシャも普段より楽しそうな雰囲気だ。たぶん、毎朝早起きしてあの髪型をセットする必要がなくなったからだろう。"

show jigoro angry
with charachange


hx "なんだその髪型は？　実習生みたいじゃないか。前の髪型はピンク色の裁判官のかつらのように見えたものだが。裁判官から実習生では大幅降格だ"



show shizu behind_frown_cas
with charachange


ssh "久夫、父さんが失礼なこと言ってるんじゃない？　友達を侮辱するなって言ってやって！"


hi "友達を侮辱するのはやめてください"


hx "今しゃべったのはどっちだ？"


hi "両方です。俺も静音と同意見です"

show mishashort hips_smile_cas
with charachange


mi "へへへ～！　どう思う、ひっちゃん？"

show shizu adjust_frown_cas
with charachange


ssh "前の髪型の方がよかったのに"

show mishashort perky_sad_cas
with charachange


mi "えぇ～……ひっちゃん、なんだかがっかりしてるみたい。ひっちゃんも気に入らないの？"


hi "まあ、そうだな、確かに前の髪型のほうが良かったなって思うけど、でもその髪もいいと思うよ。よく似合ってる"

show mishashort hips_grin_cas
with charachange


mi "わあ、ありがと、ひっちゃん～！"


hx "いじらしいな。そんなにその髪型が好きなら交換すればよかろう"


hi "髪型は交換なんてできませんよ"


hx "それは残念だな。その子の前の髪型でも、お前の今の怠け者じみた髪よりはよほどましだ。まったくひどいものだ。こっちはといえば……"



show jigoro laugh
with charachange


hx "ふむ……前の髪型にくらべれば、よほど派手派手しさがなくなっているな。気に入ったぞ"



show mishashort cross_laugh_cas
with charachange



mi "あはははは～！　ほんとですか？　ありがとうございます、静音パパさん～！"




show jigoro angry
with charachange


hx "羽加道だ。まともに話さんか"

show mishashort perky_smile_cas
with charachange


mi "ん～？　よくわかんないです～！　おっけおっけおっけ～！　じゃあ羽加道のおじさんにしますね！"



hx "ええい、スライドホイッスルに話しているみたいだ。これはかなわん。作家はまだか？　秀明！"



show jigoro invis
show shizu basic_normal_cas
show hideaki bored
with charaexit



"治五郎さんは静かに独り言をつぶやきながら歩き去る。ああいう偏屈気取りの年寄りは、女の子を怒鳴りつけるのは少なくとも抵抗はあるんだろうな。"
"と思っていると、最後に一言言わずにいられなかったのか、突然引き返してくる。"




show jigoro angry
with charaenter


hx "あともう一つ。そんな大声を出すんじゃない。目の前で大声を出されるのはわしは好かん"

show mishashort hips_grin_cas
with charachange


mi "えっ？　大声ですか～？　大声なんて出してないですよ～！"



"派手さがどうこういうとか、大声をたしなめるとか、そういう口をきくのにこれ以上不適切な人を思いつくことができない。偽善が行列をなしていて、延々と続いているようなものだ。"






"珍しい反応が起きているみたいだ。ミーシャは治五郎さんのことが面白いらしく、何か言うたびに笑い声をあげている。そのせいで余計に治五郎さんの怒鳴り声も激しくなる。こういうのを悪循環って言うんだろう。"




"ミーシャの声は四方八方から聞こえてきて、ときどき爆発的な笑い声で中断される。一方、治五郎さんの声はとどろくような低い声で、大砲みたいに狙い澄まされている。ともかく、双方信じがたいくらいの大声だ。"



"二人が話せば話すほど、お互いの声に反応して音量が大きくなっていく。"

show mishashort perky_sad_cas
with charachange


mi "あ～！　耳痛い～！"


hx "{b}なにを叫んでいるのだ！？{/b}"



hide shizu
with charaexit

show black
with hands_in


"静音の手が後ろから俺の目を隠す。ミーシャにやられるのには慣れているけど、当のミーシャは目の前にいるのだから、今度は掛け値なしに混乱する。"


show shizu adjust_happy_cas_close at center behind black
show hideaki bored at center
with None

hide black
with hands_out


"静音は手を離すと、指を唇に当てる。"

show shizu behind_smile_cas_close
with charachange


ssh "こっちに気づいてない。ちょうどいいわ！　今がチャンスよ。こっそり抜け出しましょう"


his "どうしてこっそり抜け出すんだ？　普通に歩いて移動すればいいだろ"

show shizu adjust_smug_cas_close
with charachange


ssh "それじゃ面白くないでしょ"

show shizu basic_happy_cas_close
with charachange


ssh "じゃあ決定ね。シークレットミッションよ。気づかれないように脱出するの。秀明を救出したらボーナス得点"

hide shizu
with charaexit

stop music fadeout 3.0


"すでに状況をゲーム扱いしてしまっている。静音は静かに現場から身を引いて、家の方にじりじりと近寄っていく。俺は普通に歩く。"




label jp_S22:

scene bg shizu_living
with locationskip


"最初は静音の姿が見えなかったけど、やがてグラスに入った氷水に口をつけながら、片手に眼鏡をぶらぶらさせつつ母屋の方に入ってくる。すると俺を見るなりあわてて眼鏡をかける。"

show shizu basic_normal2_cas at center
with charaenter

play music music_ease fadein 4.0



ssh "秀明を救出しなかったわね。つまりボーナス点はなし。スタイリッシュさも評価対象だったら、あんな超超超退屈な脱出は減点間違いなしよ"








his "お前が俺に話したいみたいだったし、スタイリッシュにしなきゃいけないなんて知らなかったよ。ところで、本当にスタイリッシュな人ってのは、無理して自分をかっこよく見せたりしないって言うぜ"


show shizu cross_wut_cas
with charachange



ssh "あなたってほんとにかっこいいわよ"





"俺が静音の皮肉をたやすく理解できるってのはどういうことなんだろう。それと、耳の聞こえない静音は皮肉という概念を理解するのにどれほど苦労したんだろう。想像もつかない。"


his "機嫌良さそうだな"


"本当に機嫌がいいというわけではなさそうだけど。どっちかといえば、とても興奮しているように見える。"

show shizu behind_frown_cas
with charachange



ssh "良くなんかないわよ"





show shizu basic_normal2_cas at Position(ypos=1.1)
with dissolvecharamove


"グラスを置くと、静音はソファに座る。"

show shizu behind_frown_cas
with charachange


ssh "ミーシャの前の髪型の方がずっと好きだったのに。とてもかわいかった。洗練されてて、すごく手が込んでた。今の髪型はさっぱりしすぎてて、おてんば娘みたい"






his "ミーシャが洗練されてて手が込んでるってのはちょっと違うんじゃないか。お前の方が当てはまりそうだぞ。やってみればいいじゃん。髪伸ばしてドリルみたいにすれば"





his "ふむ……案外、お前に似合ってるかもしれないな"

show shizu adjust_frown_cas
with charachange


"静音は眼鏡のフレームを乱暴にこする。今の言葉の言外の意味に憤慨しているようだ。別に構わない。まさにそういうことをほのめかしたのだから。俺が座ると、静音は少し俺に近寄る。"

show shizu basic_angry_cas
with charachange


ssh "私がおてんばですって？"






his "いや、お前をおてんば呼ばわりする人はいないと思うぞ……見た目だけなら"



"静音がすごい目つきでにらむ。不愉快そうだ。笑いをこらえるのに苦労する。"



his "やっぱり、二人で髪型交換した方がよかったんじゃないか"


shi "……"

show shizu behind_frown_cas
with charachange


ssh "まるで父さんみたいな話し方ね"

show shizu adjust_smug_cas at center
with Dissolvemove(0.2)



"本当だ。それを自覚して腹を立てる俺を見て、静音は声を立てずに笑う。勢いよく立ち上がると、左手の見えない剣をくるくると回し、兵隊のようにまっすぐに立ってしかめ面をする。おそろしく正確な物まねだ。"


show shizu basic_frown_cas
with charachange


ssh "とにかく、私は青いセーターに茶色のズボンなんて格好の人の指図は受けないからね。その色のセンスはなんなの？　最悪ね"



show shizu adjust_smug_cas
with charachange


ssh "……でも髪型を変えるのは面白いかも。そうじゃない？　周りの人がどんな反応をするか、見てみたいな"


his "本当に人をおもちゃにするのが好きなんだな。時々やりすぎじゃないかって思うぞ"

show shizu adjust_frown_cas
with charachange


"答えはない。眉根を寄せながら眼鏡をいじる様子を見ると、答えられないのだという気がする。"

show shizu behind_blank_cas
with charachange


ssh "楽しいんだもの"


"すると、さらに俺の近くに寄りながら、もっと自信たっぷりに――"

show shizu basic_happy_cas
with charachange


ssh "たくさんの人をどんどん自分の人生に引っ張り込むのが楽しいの"


his "ああ、なるほど"


"俺もその中に入ってるのかな。聞いてみたいけど、どう聞けばいいのかさえわからない。"

show shizu adjust_happy_cas
with charachange


"そんな質問には答えない、と先手を打つように静音が指を振る。"

stop music fadeout 0.5

show shizu adjust_blush_cas_close
with vpunch


"静音がグラスに手を伸ばす。でもさっきから距離が離れてしまっていたことに気づいていない。無様に転びそうになって俺の体をつかもうとしたはずみに、俺の方が静音の上に倒れ込んでしまう。"

scene ev shizu_couch
with vpunch

play music music_serene fadein 9.0


"静音にもたれかかると、その体が発している熱が感じられて、お互いの近さを自覚する。静音の柔らかな息と、わずかに身をよじらせたときの布ずれの音が聞こえる。"




"静音の頬がじわじわと赤らんでいく。でもその深い色の瞳は、まばたきもせずに俺の目をまっすぐ見つめている。"


"初めて静音に会ったときと同じ目つきだ。貫くように鋭く、はっきりした感情は何も読みとれない。猫の目のように、これから起きる出来事だけを待ちかまえている。そんな目つきで見られると不安になってくる。"


"こんなに長い間、こんなに近くに居続けるのは初めてだ。雰囲気も変わってしまった。ミーシャと組んでいつものゲームをしているときに軽く手が触れるような状況とはわけが違う。"



"おずおずと静音が両手の指を重ねる。でも手話を見せる様子はない。その目線も、最初に思っていたようなうつろなものじゃなかった。それは期待に近い。"
"もしかして、俺は今までずっと静音の期待の糸をたどり続けていたんだろうか。"


scene bg shizu_living
with vpunch

show shizu behind_blank_cas_close
with charaenter


"静音の手が俺の肩をつかんで、そっと、でも力強く俺を押し返す。俺は柔らかなソファに転がって、少し離れたところで体を起こす。俺にとっては１０メートルくらい投げ飛ばされたような感覚だ。"


"考えてみれば、これは手話の最大の難点かもしれない。手話で言葉を伝えるときは、その言葉を表に出す前に必ず頭の中で考える時間が生まれる、と静音も言っていた。"



"でも逆に言えば、単なる気まずい沈黙がとうてい乗り越えられない壁にだってなりうるということだ。できることなら、とにかく何でもいいから言葉にして、この緊張した空気を払いのけたいけど、俺には無理だ。"



"普通ならここで謝ってこの場を立ち去るものだろう。でも今は、そんな対応が正しいのかどうかも怪しい。そんなことをしてダメ野郎と思われることには耐えられない。こそこそ逃げ出すのと同じことじゃないか。"




"もちろん、何事もなかったかのようにやりすごせるわけでもない。それじゃお互いにとって失礼だ。"
"決してそうしたいわけではないけど、俺は素早く謝罪の言葉を口にする。素早すぎて手話にするのも忘れてしまう。そして自分の部屋に戻る。"


window hide None

scene bg shizu_guesthisao_ss
with locationskip

play sound sfx_pillow
with vpunch

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show black
with shuteye

window show


"どっと息を吐きながら、ベッドに仰向けに倒れ込む。今すぐ眠りにつけたらいいのに、と思う。でも目はぱっちりと覚めたままだ。"

play sound sfx_doorclose
$ renpy.music.set_volume(1.0, 3.0, channel="music")

with Pause(3.0)

show shizu basic_normal2_cas_close
hide black
with openeye



"ドアが閉じる音を耳にして目を開けると、目の前の椅子に静音が座っていて、俺は体を起こす。"




show shizu behind_blank_cas_close
with charachange


shi "……"



"静音が何か質問するけど、不意をつかれた俺には全く理解できない。"
"自分の驚きを隠すのは得意じゃないし、静音も驚かせる気はなかったのだろう。何を言っていたのかはわからないけど、静音は一歩身を引くと、しばらく手話を見せない。"


show shizu adjust_happy_cas_close
with charachange


ssh "久夫の部屋に入るの、初めて"


"静音は指を重ねると、大げさそうに恥じらい、おしとやかなふりをする。笑えない冗談だ。静音がここにいるってだけで、こっちは落ち着かないというのに。"


his "バカいうなよ。そもそも俺の部屋じゃないだろ。お前の家のゲストルームじゃないか"


label jp_S22a:


his "それに、ミーシャと一緒に俺の部屋に突入したことだってあるだろ"

show shizu behind_blank_cas_close
with charachange



"俺がもっと話すのを期待しているみたいだ。部屋に入られたとき、ひどくうろたえたのを思い出す。壁際に並ぶ薬の瓶を見てどんな突拍子もない想像をされるかびくびくしていた。静音は覚えていないだろうけど。"


show shizu basic_normal_cas_close
with charachange



ssh "あのときは動揺してたわね"




label jp_S22b:



ssh "私が入ったときもまだ動揺してるみたいだったわよ"



label jp_S22c:


"図星を突くような言い方が心に刺さる。"



his "動揺してるのにはいろいろ理由があるんだよ"



his "その中にはお前だって入ってるんだぞ"

show shizu behind_blank_cas_close
with charachange


shi "……？"


his "お前は、なんでもそうだけどさ……自分のやることに他人を巻き込むのに熱心すぎるんだよ。生徒会に人を入れるとか、休憩するのだって。相手の気持ちなんてお構いなしだ"

show shizu basic_angry_cas_close
with charachange


shi "……"

show shizu adjust_happy_cas_close
with charachange


shi "…… …… …… ……"

show shizu basic_normal2_cas_close
with charachange


shi "…… ……"


"静音はのろのろと手を動かし、手話の途中で何度も手を止めるので、俺が意味を読みとろうとし始める前にその言葉は立ち消えてしまう。そのことを表に出すまいと努力する。"



"効き目はあったようだけど、静音は少し悲しそうにしている。"
"奇妙なくらい憂いに満ちた、心ここにあらずという表情の静音を、一発で元気づけられる言葉を持ち合わせていないことが残念でならない。俺にできるのは静音が立ち直るのを待つことだけだ。"


show shizu behind_sad_cas_close
with charachange


ssh "久夫の言うとおりね。私はみんなを自分の人生に引っ張り込みたいと思ってる。でも最近は、それが本当に正しいことなのか、自信がなくなってるの"


his "このまえ気に入ってるレストランに連れて行ってくれたときは、楽しかったぜ"

show shizu basic_normal_cas_close
with charachange


ssh "別に気に入ってたわけじゃない……ほかにも好きな店はあるわ。数字で順位付けできるかも"


his "ほんとかよ……"

show shizu adjust_frown_cas_close
with charachange


ssh "この椅子固すぎるわ。ベッドに座りたい"


"静音を促すと、俺は静音が椅子から立ち上がってベッドに腰掛けるのを待つ。別に面白がらせるつもりではなかったのに、向こうはその様子が面白いと思ったようだ。"

show shizu behind_smile_cas_close
with charachange

stop music fadeout 5.0


ssh "目を閉じて"


his "どうして？"

show shizu adjust_smug_cas_close
with charachange


ssh "ひみつ"

show black
with shuteye



"静音に合わせることにして、俺は目を閉じる。静音が俺によりかかってくるのを感じる。"
"そして突然、何か柔らかくて湿ったものが唇に触れる。驚きで全身がこわばるけど、あまり気まずいリアクションにはならなかったのは幸いだ。"





"ただの軽い触れ合い、それで終わりだろうと思いかけていると、静音がまた口づけてくる。今度はもっと深く。静音の手が俺の肩をなで、首へと登り、そしてまた下がる。次は肩を越えて、腕へと降りていく。"




"足に静音の体重を感じる。この状況のいやらしさは十分に伝わっている。ほんの少しだけ目を開けてみようかという気になっていたけど、それを待ちかまえていたかのように、静音は俺のまぶたに指を重ねる。"



play sound sfx_rustling


"数秒後、両手が手首で縛り付けられてしまい、状況を理解できない俺は恐怖に陥る。静音に何を考えているのか問いただそうと真っ先に考える。俺の声が聞こえなくたって、言いたいことは伝わるに違いない。"


"静音は俺の手を離さず、その指で手のひらから、手の甲を越えて手首までなぞっていく。"





scene evh shizune_hcg_tied_stare:
    yalign 0.0 xalign 1.0 subpixel True
    easein 6.0 xalign 0.5 zoom 0.5
    truecenter
    zoom 1.0

    "evh shizune_hcg_tied_stare_small"
with whiteout

play music music_heart fadein 5.0


hi "おい、何してるんだ？　なんだよこれは？"


"当たり前だけど、両手を後ろに縛られていては、猿ぐつわをかまされているのと同じことだ。心のどこかで、それが静音の狙いだったんだと思わずにはいられない。"

scene evh shizune_hcg_tied_smile_small
with charachange



"心を読んだかのように、いたずらっぽい表情が静音の顔にぱっと広がるけど、頬の赤みが引くことはない。むしろ、俺と目が合った瞬間に赤みはさらに増す。"




"恥じらいながら、静音はさらにもたれ掛かってきて、深く俺を抱きしめる。"
"俺の肩と首に自分の顔を埋めて、表情を隠す。静音の髪の毛は柔らかくてくすぐったくなり、俺は笑い声を漏らしてしまう。どうせ静音には聞こえないので、怒られることもない。"



label jp_S22h:

scene evh shizune_hcg_tied_blush_small
with charachange




"静音の手が、スカートに覆われているズボンのジッパーへと下がる。"
"その手が見えなくなるけど、勃起している俺のものに触れたとたんに引っ込んでしまう。静音は緊張で俺の上から転がり落ちそうになる。まるでそこにそんなものがあるなんて思っていなかったかのようだ。"







"ここまではあんなに積極的だったのに、急にうぶな様子を見せるのが強烈に対照的で、面白い。静音が突然子供っぽくなったように見える。女子高生がもっとアグレッシブな女性の役を演じているようなものだ。"








scene evh shizune_hcg_tied_blush:
    yalign 0.0 xalign 0.8
show evh_hi shizune_hcg_tied_hisao2:
    yalign 0.0 xalign 0.8
with flash


"興味深そうに人差し指で俺のペニスをつつきながら、残りの指を裏側に滑らせると、静音の顔がさらに赤らんでいく。恥ずかしそうなその表情とは裏腹に、手は穏やかに、探るように動く。"

show evh shizune_hcg_tied_stare
hide evh_hi
with charachange


"静音も俺と同じくらい緊張しているんだろう。検査みたいにつつき回すのをやめてくれて、俺は少しほっとする。でも次は何がくるのかと考えてしまう。"



"シャツのボタンを外そうとするだろうか。胸の傷を見たら何を言われるか。俺自身まだ気にしているし、傷を見た静音が浮かべる心配そうな表情、物思いに沈むときのあの指を重ねる仕草が想像できる。"




"幸い、このポジションではセーターを脱がすことはできない。破けば別だけど。さっきの恐れも薄らぐ。これで俺が今感じているのは、奇妙かつやっかいな具合に混じり合った期待と緊張だけになった。"

show evh shizune_hcg_tied_blush
with charachange



"膝にかかっている重みが急に軽くなって、現実に引き戻されると、静音がつま先立ちになって下着を太股から滑り落としているのが見える。俺に見られているのに気づくと、静音はこっちの両目を片手で隠そうとする。"







"俺はいつの時点から静音に惹かれ始めたんだろう。肉体的にだけじゃなく、惹きつけられるようになったのは。どうしてだろう。静音はかわいいけど、とても好戦的だ。好きでそうしている節がある。"






scene evh shizune_hcg_tied_blush_small
with charachange


"でも今、あるいはほかの時々に静音が見せる振る舞いは、そのイメージにはあまり合っていない。俺の手を縛ったのは、分かり切った理由以外にも何かあるのかもしれない、という気がしてくる。"



"それでも、名刺でも見せるかのような気軽さで静音が振り回すあのアグレッシブさは本物だ。ああいう態度は危険と見なして良いものかどうか、俺にはわからない。"
"もし危険なら、俺はどういう人間ということになるんだろう。"




hi "ここに来て最初の週のことだったかな。考えてみれば一週間ってそんなに長い気がしないけどさ、そのときはそう思えたんだ"
hi "あのとき、俺の人生はもう残り少ないって思ってたのに、日が経つのがものすごく遅いって感じがした"







"静音に聞こえなくても、話すことが俺にとっては落ち着く。"




hi "別に不満があるわけじゃない、って実感がわき始めたんだ。ただそれでも……"


hi "あー、まあいいや"

scene evh shizune_hcg_tied_stare_small
with charachange


"静音が俺を見る。俺がしゃべっているから、という以外にそうする理由がない。俺が何を言ったかわからないせいで、静音はどんどんあわてふためくけど、返事の手話を見せることはしない。"

scene evh shizune_hcg_tied_close_small
show evh_hi shizune_hcg_tied_hisao2_small
with charachange


"俺のペニスに向けて体を降ろすと、静音は鋭く息をのみ、俺の上でぐらつく体をまっすぐに保とうとする。"





"ドレスのスカートが俺たち二人の秘部を覆っていて、テントのように体の熱を閉じこめる。その下では耐え難いくらい暑くて、静音の手が俺のものを導こうとしているのがさらに暑さを増すばかりだ。"

show evh shizune_hcg_tied_kinky3_small
with flash


"静音の中に入った瞬間、静音は苦しげな表情を浮かべて、俺の上に倒れ込みそうになる。突然の感覚で精神が麻痺しそうだ。端から端まで、いくつもの快感の波が俺の体を突き抜けていく。"


"俺の下半身全体が、静音の肉体の暖かさと湿り気に包み込まれたかのようだ。静音が動き始めると、その痙攣と震えが全部俺に伝わってくる。"

show evh shizune_hcg_tied_kinky2_small
with charachange


"静音はお尻を前後に揺らし始める。最初はゆっくりだけど、抜ける寸前まで腰を持ち上げ、最後の最後でズンと降ろす、ということを繰り返しているうちに、そのテンポはだんだん速まっていく。"




scene evh shizune_hcg_tied_kinky2:
    zoom 1.0 yalign 0.1 xalign 0.7
    acdc_warp 6.0 xalign 0.9
with flash


"こんなに近くにいると、静音の肌に浮かぶ玉のような汗や、眼鏡が鼻からずり落ちて口の近くにかかり、かけ直す前にレンズが曇ってしまう様子も見える。"


"静音の指先が両肩に食い込んでくる。体を安定させようと俺をつかみ、体を離すために押し返し、また下へと体を押し戻すときに俺の腕を滑り降りて手首や手を握る。"



scene evh shizune_hcg_tied_close_small
with flash



"こんな体さばきは困難きわまりない。静音は両足で自分自身を上げ下げしながら、俺を抱き寄せようとする。俺は俺で静音にキスしてみるけど、お互いの額を触れ合わせるだけに終わる。"



"ドアに鍵はかかってるだろうか、という考えが一瞬頭をよぎる。今あのドアが開いたら、俺は文字通り心臓発作を起こすだろう。それにドアを開けるのは誰か、という問題もある。"


"その危機感は静音の動きを余計に苦しいものにするだけだった。もっと速くしてくれたらと思うけど、このポジションではそんなことはできそうにない。"

show evh shizune_hcg_tied_kinky1_small
show evh_hi shizune_hcg_tied_hisao2_small
with charachange


"もっと深く静音の中に入ろうと、俺も静音のリズムに合わせて腰を上げるようにする。その動きで木製の椅子が揺れて、板張りの床にぶつかってがたがた音を立てるけど、もう関係ない。"

$ ksgallery_unlock("evhul shizune_hcg_tied_hisao2_small")
show evh shizune_hcg_tied_kinky3_small
with charachange


shi "……んん……！"


"静音の息づかいがだんだん大きくなり、口からはくぐもったうめき声のような音まで漏れ始める。我慢しようとしているのは明らかだけど、それでもドアの外に立っている人には十分聞こえてしまう音量だ。"


"俺は静音を突き上げるのをやめる。静音自身がますます行為に入り込んでしまって速度を上げてくるので、下にいる俺には追いつけなくなってきた。"


window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.4)

window show




"こめかみに流れる血液の音が聞こえそうなほど心臓の鼓動が激しくなる。それよりも心配なのは、胸のあたりに感じる鈍い痙攣だ。たった一瞬だけど、太腿の間の締め付けるような感覚が意識から離れる。"





$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene white
with whiteout



"でもその一瞬で十分だ。静音が俺のものをきつく締め付ける感覚と、こすれ合う肌の触感が合わさって、俺は体をこわばらせ、静音の中に解き放つ。力がみなぎる感覚と浮き上がるような気持ちが一瞬で通り抜ける。"



label jp_S22x:

$ renpy.music.set_volume(1.0, 2.0, channel="music")
$ renpy.music.play(music_heart, fadein=2.0, if_changed=True)

scene evh shizune_hcg_tied_close:
    yalign 0.1 xalign 0.8
show evh_hi shizune_hcg_tied_hisao2:
    yalign 0.1 xalign 0.8
with Dissolve(2.0)


"行為が終わった後、自分の心臓が速度をゆるめ、もとのリズムに戻るまで、鼓動の音に耳を澄ませる。その間に静音の息づかいも聞き続ける。"

hide evh_hi
with charachange


"眼鏡が少しだけ傾いていて、静音がそれをいじろうとしないところは初めて見る。かわりに直してやりたいと思うけど、やろうとしたとたんにそれができないことを思い出す。静音も忘れているようだ。"

stop music fadeout 7.0

scene evh shizune_hcg_tied_close_small:
    truecenter
    subpixel True zoom 1.2
    easein 10.0 zoom 1.0
with Dissolve(2.0)



"立ち上がるかわりに、静音は椅子に縛られたままの俺に体を押しつけて手を伸ばそうとする。その位置からでないと俺の手をほどけないというかのように。静音が手首を解き放つのを感じながら、そんなことを考える。"




"でも静音は俺の上から離れない。指をそっと俺の指に這わせながら、ときどき指を曲げて俺の手のひらをなぞる。おかしな話だけど、こんな単純な行為だけでも、今までよりもっと静音とつながっている気がする。"



"しばらく静音はそうやって体を押しつけている。ちょっと居心地は悪いけど、俺は幸福な気分だった。このまま何時間でもこうしていられるくらいに。"

scene black
with dissolve
label jp_S23:

scene bg shizu_guesthisao
with locationchange

play music music_daily fadein 0.5



"それからの日々は、指の間から水がこぼれ落ちるようにあっという間に過ぎ去っていく。一緒に話そうと思っても、静音はいつも用事で出かけていたり、ミーシャと一緒にいたりする。俺は避けられているんじゃないか。"




"無理もない。そりゃあ気にはなるけど、静音がああいう態度を取るのは自然なことだと思う。とはいえ、今までこんな状況を経験したことなんてないし。"




scene bg shizu_living at left
show mishashort perky_smile_cas at center
with locationskip



"静音を見つけられないときは結局ミーシャにばったり出会い、手話の勉強を手伝ってほしいと頼むんだけど、いつも逃げられてしまう。明日にはここを出発するんだから、今日は逃がさないぞと心に決める。"



"学校に戻ったら、二学期の準備も重なって生徒会の仕事はずっと忙しくなるだろう。たった一日であっても、それまでにできるだけ手話の勉強をしておきたい。"


hi "頼むよ、ちょっと手話で雑談するだけじゃないか！　お前だっていつもやってるだろ。というか今まさにやってるじゃないか"

show mishashort cross_laugh_cas
with charachange


mi "わはは～、ほんと、ひっちゃん？　おかしいね！"




"ミーシャは無意識にしている手話を中断して、顔の前で手を振って否定する。でもすぐにまた、俺たち二人の会話を誰にあてるでもなく手話に通訳し始めてしまう。"







show mishashort sign_confused_cas
with charachange



mi "ひっちゃんって、ほんとに根気強いよね。急にまた手話に興味持ったりして……もしかして、将来手話の仕事がしたいの？　ずるいよそんなの、もともとはわたしのアイディアだったのに～！"


show mishashort cross_frown_cas
with charachange



mi "気をつけなきゃダメだよ、ひっちゃん。時代が変わるのは早いんだからね～……"

mi "わたしが手話通訳者になろうって決めた頃には、携帯電話で段落丸ごと打ち込めるようになってるんだもん。すごいよね～！　わたしは困っちゃうけどね！"





"これ以上話をはぐらかすのは無理だと悟ったのか、ミーシャはすぐに申し訳なさそうな声色に切り替える。"



show mishashort perky_sad_cas
with charachange



mi "ごめんね、ひっちゃん、わたしすっご～く疲れちゃったの～！"
mi "特にここ最近は、しっちゃんと一緒なのは楽しいけど、しっちゃんはわたしよりずっと元気だから！　その上手話まで教えるのって大変すぎるよ～。わたしそんなにスタミナないし！　ごめんね～！"




"いつもの陽気さと勢いで叫んでいるのを見ると、そんなに疲れているようには思えない。でもこれ以上しつこく食い下がるのも良くない。"

show mishashort sign_smile_cas
with charachange


mi "実はね～、しっちゃんと一緒にショッピングにいく予定だったんだ！　おみやげ買うなら今日しかないからね"


hi "おみやげかあ。夏休みでここに来てるってこと、忘れそうになってたよ"


hi "言ってることはわかるよ。教えることって、そんなに簡単そうじゃないよな。秀明にも手話を教えてくれって頼まれたんだけど、教えてる間は自分でも信じられないくらいわけが分からなくなってたし"


hi "まあ、お前が手話の先生になったらどうなるのかは見てみたいな。お前ならそう簡単には疲れたりしないだろ"

show mishashort perky_confused_cas
with charachange


mi "うんうん、そうだね～！　だといいな！"

show mishashort hips_smile_cas
with charachange


mi "でもひっちゃん、なんだか心配になってきたよ。でも～、おみやげ！　だから～！　また今度ね、ひっちゃん。あはははは～。ひっちゃんにも何か買ってきてあげようか？"


"理解するとは言ったけど、教えてほしくないわけじゃない。でもこれ以上しつこく言うのは無理そうだ。ただのわがままに見られそうなのも気分が悪い。あきらめることにする。"


hi "いやいいから。何も買ってくるなよ。本気だぞ。変なシャツだかなんだかで驚かそうとするなよ。いいな？"

show mishashort cross_grin_cas
with charachange


mi "へへへ～"


"嫌な笑い方をするなあ。"

hide misha
with charaexit




"靴を履くと、ミーシャは俺を除けば無人の家に向かって行ってきますと叫び、ドアを開けて出かけていく。涼しい新鮮な空気が廊下を吹き抜ける。"
"ドアの枠から濃い色の髪がはみだしているのを見て、静音が外で待っているのだと気づく。"





hi "おはよう"

show mishashort invis:
    center
    xpos 0.8
show shizu invis:
    center
    xpos 1.0
with None

show bg shizu_living at right
show shizu adjust_happy_cas at tworight
show mishashort perky_smile_cas at center
with Dissolvemove(2.0)


"ドアの向こうからミーシャが通訳してくれる。静音は振り向いて小さく手を振る。"


"いつもの無造作な挨拶とはほとんど違いはないけど、それでもそこには紛れもないためらいがある。漠然とした空虚さと距離感が残る。"

show shizu behind_blank_cas
with charachange


shi "……"

show mishashort hips_grin_cas
with charachange


mi "ひっちゃん、朝早いんだね～！　お話の邪魔だったかな？"



hi "ミーシャにお前と話す方法を教えてもらおうとしてたんだけどさ、ちょっと急ぎすぎてたかもな。後でいいよ。二人とも今日は買い物にいく予定だったんだろ"






"ミーシャがいると自分の言葉を手話でも伝えることを忘れてしまう。あいにく静音がドア口に立っているので、ミーシャがその陰になる。この一瞬の位置関係のおかげで、今の俺の言葉は静音に全く伝わらない。"


show shizu basic_angry_cas
with charachange


ssh "全然わからない"



"言いたいことはいろいろあるけど、静音にわかるように伝えることができない。静音にだって、俺に伝えたいけど俺には理解できないことがいっぱいあるはずだ。そういう状態はもうすぐ終わるということを伝えたい。"


hide shizu
hide mishashort
with charaexit


"そのかわりに、俺はただ『なんでもない』と答える。二人にいってらっしゃいと言い、手を振って見送る。"


"今日はみんな一日出かけているようなので、俺は本を手に取ると、居間で一番大きくて座り心地の良さそうないすに座る。手話の本じゃなくて、転校した最初の週に図書室で借りた小説だ。"


"ずいぶん前のことだ。あの借りた本の山、そろそろ崩すか、さもなければ返すかしないと。"

stop music fadeout 2.0

show jigoro neutral at center
with charaenter


"１６ページ読み進めたところで、治五郎さんが部屋に入ってくる。片手には紙束を持ち、もう一方の手で刀をバトンのようにむやみに振り回している。浴びたばかりのシャワーで濡れた髪を振って、水滴を飛び散らせる。"

show jigoro angry
with charachange

show jigoro angry at Position(ypos=1.15)
with charamove


"そんな行儀の悪いところを目撃されて、治五郎さんはヘッドライトに照らされた鹿のように硬直すると、数メートル先のソファに座り、徐々に強烈な、でも何の根拠もない怒りをくすぶらせ始める。"


"まだこの人には三回しか会っていないのに、すでに見ただけで吐き気を催しはじめている。これも一種のカリスマといえるかもしれない。"



"こっちは一言も口にしていないけど、向こうはもう不機嫌になりつつある。彼を挑発するのは利口とはいえないし、話しかけるだけでも挑発と取られそうだ。でもそれ以外に取り得る展開を想像せずにはいられない。"






"俺が一切口を開かずにここを立ち去って、本を読みに自分の部屋に戻るか、外に出るとする。間違いなく、許し難い侮辱と受け取られるだろう。たぶんそこへ直れと言われて叩きのめされる。"
"それにどっちを選ぶにしても、あまり礼儀正しい行動とは言えない。"



hi "何を読んでいるんですか？"

show jigoro smug
with charachange

play music music_another fadein 6.0


hx "わしの自伝の草稿だ。男が目を覚ますと、招かれざる客が居間にいて、自分の椅子に座って底の浅い安物の小説を読んでいる、という筋書きだ"


"まだほとんど読み始めたばかりだし、感想なんて持ち合わせていない。早くもこの会話の行き着く先が目に浮かぶ。せめて話の流れを変える努力をしてみよう。"


hi "秀明はどこです？"

show jigoro angry
with charachange


hx "お前は質問の仕方も失礼だな。破廉恥な。それはさておき、なぜそんな愚かな質問をわしに聞くのだ？　わしが知っているとでもいうのか？　わしは息子の番人か？"


"『まあ、一応おじさんは父親ですし、秀明もここに住んでるみたいだから、それで……』とはさすがに言えないよな。言ってみたいけど。"



"お手上げだ。治五郎さんと雑談しようとしたけど、もう失敗した。自分のことを嫌っているレンガの壁と会話しようとするようなものだ。"
"この場を離れて、映画を見に行くのにお金が足りるかどうか財布の中身を確かめるには、いいタイミングだ。"



"立ち上がろうとした瞬間、俺は考え直す。ただ逃げ続けることで、厄介な状況をうやむやにして切り抜けるのにはいい加減うんざりしているんだ。"



"俺自身が自分のガールフレンドから逃げているというのに、ミーシャがのらりくらりと俺を避けるのに腹を立てるのは偽善というものだ。治五郎さんが俺を引き留めようとしたとき、俺は喜んだと言ってもいい。"
"もう立ち去る気はなくなっていたけど。"


show jigoro neutral
with charachange


hx "待て"


"ただの思いつきで命令を下すかのように、威厳のほかには何の中身もない声で言う。こんな言い方で他人を引き留められるのは、よほど権力のある人か、よほど傲慢な人だけだ。ある意味感心する。"



show jigoro smug
with charachange


hx "お前は静音と一緒に生徒会に所属しているのだったな？　どのような役職に就いている？"



hi "生徒会長以外には、決まった役というのはないと思います。静音はいつもあっちこっちから手伝ってくれる人を集めてます"
hi "たいてい来てくれるのは一人くらいですけど、ほかに誰もいないときは俺たち三人で何でもこなしてます"





"初めて静音に出会った頃に何度か頭をよぎったのは、人を不安にさせる静音の見定めるような視線は、耳が聞こえないせいじゃないか、ということだった。でもそれは家族全員に共通の特徴だということが分かる。"





show jigoro neutral
with charachange


hx "お前はそれでいいのか？"



hi "何か問題ありますか？"




show jigoro laugh
with charachange


hx "お前と静音と、あのピンクの髪の子か？　本当に生徒会はそれで全員なのか？"

show jigoro smug
with charachange


hx "そんな小さな生徒会では、選挙を行うまでもあるまい。当ててやろう。お前は自分から生徒会に入ったのではなくて、静音に引っ張り込まれたのだろう。お前は自分の役職もよく知らないと言っていたからな"


hx "筋は通るな。選挙で選ばれてもいないのだから、知っているわけがない。つまるところ、選挙を経ていない者は何者でもないのだ"



show jigoro laugh
with charachange




hx "誰がそのような生徒会を尊重する。選挙の洗礼も受けていない三人組が臨時の助っ人をかき集めるだと？　茶会にうつつを抜かす子供の三人組が何でも問題を解決できるというなら、よほどお粗末な学校に違いない"






hi "人数が少ないことの何が悪いっていうんですか？　生徒会がやるべきことをやっているなら、それで十分じゃないんですか？"



hi "それにこれはゲームじゃありません。一度あなたも学校に来るべきだと思います。タイミングが良ければ、静音にどれだけのことができるのか、見ることができるかもしれませんよ"


show jigoro angry
with charachange


hx "あんなど田舎にぶらりと立ち寄って、自分の娘が権力を誇示するのを見物するような時間が、このわしにあると思うか？　これほど気分が悪くなったのは人生で初めてだぞ"



hi "あなたは山久に生徒会なんてなくてもいいと言っている。でも現実には生徒会はあるんです"
hi "それに静音はちゃんと生徒会長に選ばれたし、静音にとっては意味のない役職なんかじゃありません。実際、静音はものすごくがんばってます"


show jigoro laugh
with charachange


hx "お前は静音に票を入れたように聞こえるな"


hi "入れていません。選挙の時には学校にいませんでした"

show jigoro neutral
with charachange


hx "ふん。静音に投票もしていないではないか。まあそれはともかく――秀明にも聞いてみたらどうだ？"

show jigoro smug
with charachange


hx "静音は中学の頃から、高校の生徒会長になりたがっていた。スピーチの草稿を秀明に読ませて、あいつの時間を浪費しておったな。どういうわけだ？"


"この会話の間ずっと、治五郎さんは自伝の草稿に目を通しながら、一度も顔を上げていない。どんどん腹が立ってくる。"


hi "生徒会はゲームじゃないからですよ。俺たちは学校を運営はしていないけど、遊び感覚でやってるわけじゃないし、真剣にやってないわけでもありません"


"純粋主義でないことはそんなに間違ったことだろうか。"

show jigoro angry
with charachange


hx "学校に行ったことはある。まったく……あそこの生徒は……"


"この人の言いそうなことが百万通りも思い浮かび、そのどれを聞いても意気消沈する覚悟をする。おかしなことだ。以前だったら自分がそういうことを考えていただろうに。"


hx "掃除当番もないのだからな"


"今のは完全に予想外だった。それに間違ってる。"


hi "ありますよ。俺は生徒会に入ってて当番は免除されてるから、当然知ってます"


show jigoro neutral
with charachange


"間違いを犯したという事実に治五郎さんは困惑する。この機会に反撃をするべきだ。単なる会話なのにこんな考えをしているなんて、ひどく奇妙な感じがする。"


hi "あなたが山久に行ったのはずいぶん昔みたいですね"


hi "のんびり回想録なんて書く暇があるんだったら、静音と話をしたらいいんじゃないですか。静音にだって誇りにしていることくらいあるって思いませんか？"


hi "若者ってのはそういうものなんですよ。誇りにしていることがあるんです。あなただって自伝を書いているなら、わかるはずでしょう"



"絶好の機会だったのに、台無しにしてしまった。どういう反応を期待していたのかよくわからない。自分に対してなのかもしれないけど、治五郎さんは見る間に怒り出す。"
"でもその一方で、落ち着きを取り戻しつつあるようにも見える。自信と自制を取り戻しているかのようだ。"


show jigoro angry
with charachange


hx "わしの人生がそんなに気楽だと決めつけるとは、お前は何様だ？　わしの自伝を読んでもいないお前が、娘との関係だの、諸々の問題をどう解決すべきか指図できるというのか。お前には決してわかるまい"



hx "わしが今このソファから立ち上がり、お前の正面に立ち、わしの人生の物語の要約版が刻み込まれたブラスナックルでその額を殴りつけ、その面にわしの自伝を刻み込んでやったとしても、お前にはわからんだろう"




hx "あらゆる種類の家庭教師や通訳を何人も雇って、静音を普通にしてやろうと努力した。だが１２年もの間、静音はわしに話しかけることすらしなかったのだ。お前が思っているほどことは単純ではないのだ"


show jigoro smug
with charachange


hx "静音がわしと関わりたくないというなら、それはかまわん。それ自体は変わったことではない。お前が最後にご両親と話をしたのはいつだ？"




"ずいぶん前のことだ。俺は恥ずかしく思う。親元に電話するなり、メールや手紙を書くなんてたやすいことをしなかったことより、治五郎さんにそれを気づかれたことの方が恥ずかしい。"
"そしてそう感じていること自体がなおさら恥ずかしいと思う。"





show jigoro laugh
with charachange


hx "やはりな"


hi "親に会いたくたって俺は会えないんです。それは話が違います。あなたはそんな遠くに住んでいるわけでもないでしょう。電車一本じゃないですか！"



show jigoro neutral
with charachange


hx "もういい。いらんといったらいらんのだ。実に頑固な奴だな。有意義なことに対してそうであればよかったのだが。そのことと口答えの仕方以外に、お前が静音から何を学んだのか皆目分からん。違うか？"


stop music fadeout 10.0



"答えはイエスだ。静音とミーシャに会うまでは、こんなに頑固でも理屈っぽくもなかった。大体、二人に会う前に俺は死にかけたばかりだったんだから。そもそも生徒会に入るのを拒んだ理由がよくわからない。"





label jp_S23a:



"転校したあの日、クラスで自己紹介するだけでも途方もない労力が必要だった。何が理由で誰についていったとしても不思議はない。生徒会があまりに魅力がなくて、俺が抵抗したというのもただの偶然かもしれない。"




label jp_S23x:



"たぶん、あの二人のしつこすぎる勧誘から逃れようとしているうちに、自分のエネルギーを取り戻すことができたんだろう。気の利いた話だ。"






"自分がここにいる理由をもう一度考える。治五郎さんと言い争っていても意味がないけど、俺はどこかでそれを心待ちにしていたと思う。"
"それに治五郎さんは正しい。俺にはこの人が理解できない。理解したとしてもこの人は気にもしない。俺はクジラの上を這い回る一匹のシラミだ。全く取るに足らない存在なんだ。"





"俺にはない自信をこの人は持っている。静音もだ。俺がここにいるのは、それが理由なのかもしれない。静音の父親と怒鳴り合いに近い言い争いをしているのは、静音の大胆さが多少でも俺に移ったからだ。"
"でもそれを続ける理由は何もない。"




"それでも、この人は大嫌いだ。どうすればいいのかわからない。数ヶ月前だったらそのまま殴りつけて、後のことは成り行きに任せていただろう。でも今はその危険は犯せない。この人にやり返されたらきっと殺される。"




"結局、俺にできる唯一のことは、言い返す言葉もなく、彼を嫌っていて、敗北感にまみれていることを自覚しながら、無言で治五郎さんをにらみ返すことだけだ。妙なことに、治五郎さんはそれを反抗と取ったらしい。"

show jigoro angry
with charachange


hx "ふん。そうか。なら好きにしろ"

show jigoro invis at center
with dissolvecharamove




"治五郎さんは剣を手にとって地面に突きながら立ち上がると、部屋からぶらぶらと出ていく。手元の本を投げつけてやりたくなる。もう本を読む気分ではなくなっていたとしても、ようやく一人になれたのはありがたい。"


scene black
with dissolve

label jp_S24:

scene bg city_station
with locationchange


"学校への帰りの旅は何かにつけて遅れてしまう。静音とミーシャが戻ってくるのが遅すぎて、家を出るのが間に合わなくなってしまったので、結局もう一日滞在するはめになる。"



"翌朝、一分差で電車に乗り遅れたと思ったら、次の二本は駅に止まらなかった。俺がふらふら飲み物を買いに行っていたせいで、四本目の電車も乗り過ごしてしまう。おかげで静音はかなり不機嫌だった。"




scene bg school_dormhisao
with shorttimeskip

play music music_dreamy fadein 2.0




"ようやく自分の部屋にたどり着いたころには、もうくたくただった。電車の中ではほとんど寝てばかりだったというのに。今日一日だけの疲れとは言えないだろう。"
"旅行に行ったときにはよくあることだ。これが初めてってわけじゃない。"



$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

scene black
with shuteye

window show


"他にやった人が誰もいなければ、これで論文が書けるかもしれない。医学会誌に載ったりするかも。『旅行帰り症候群』。あまりぱっとしないな。もっといい名前を考えつく前に、俺は眠りに落ちる。"

window hide

play sound sfx_doorknock
with Pause(1.0)

scene bg school_dormhisao
with openeye

$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show


"寝入ってから数時間後、大きな音でドアをノックされて目が覚める。夢の真っ最中にたたき起こされたのでむっとする。もう思い出せないけど、きっといい夢だったに違いないのに。"


"一瞬誰だろうと考えるけど、そうそう客が来るわけでもないし、健二に違いない。歓迎会をしに来てくれただけで、金をせびりに来たわけじゃないと思いたい。もしそうだったらたぶん感動するだろう。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene black
with shuteye


"でも寝返りを打って二度寝する衝動に打ち勝つほどではなかった。"

stop music fadeout 5.0

window hide

with Pause(4.0)

scene bg school_dormhisao
with openeye

window show


"その数時間後、俺はまた目を覚まし、すぐに床の上の封筒に気づく。"


"俺がいない間に届いた郵便に違いない。郵便は静音とミーシャの担当だから、届けるためにわざわざ来てくれたんだろうか。それとも二人の代理で誰かが届けに来て、俺に渡すよう健二に頼んだのか……"

show letter_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_rain fadein 4.0


"それを拾い上げたとき、体内に残っていた眠気が一瞬で吹き飛ぶ。"


"送り主の名前がなかったとしても、封筒を見るだけで気づいたに違いない。見覚えがある理由に思い当たる。その手書きの住所の繊細な筆跡だ。"



"岩魚子からだ。最初は信じられなかった。でも本気でそうしようと思えば、俺の居場所を突き止めるのはそれほど難しくはないはずだ。"


"もちろん、岩魚子にそうしたい気持ちがあるとは俺も思っていなかった。岩魚子が俺の彼女であった時間はせいぜい五秒くらいだ。その後は、ほとんど言葉も交わさなかった。"



show letter_insert:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide letter_insert
with None



"この手紙をどこかにしまいこんで忘れてしまうのは簡単だ。そうしたいと思う自分がいる。さもなければ、読まずに捨ててしまうか。"
"どうしてそうしたいと思うのかはわからない。そのほうが簡単だからだろう。手紙を読むよりは。"


scene ev hisao_letter_open
with locationchange


"ペンの先端で封筒を開くと、俺は出てきた手紙の長さに驚く。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide



$ written_note("久夫くん、\n\nお元気ですか？　新しい学校で、元気に楽しくすごしているといいな。みんな寂しがってます。２年のクラスのほとんど全員が３年になって３－１にクラス分けされたので、最初からみんなとても気楽にしています。きっと久夫くんもこのクラスに入ってたんじゃないかな。")

$ written_note("３年生になって、みんな卒業試験のことで頭がいっぱいになっています。まだずっと先の話なのにね。先生たちはいつもその話を持ち出してます――おじいちゃんの橘先生まで。そうそう、橘先生は今年の担任です。信じられる？　私たちが２年生から上がったら絶対に定年退職すると思ってたけど、結局残っていて、みんなに試験のことを口うるさく言ってるんだよ。\n")


$ written_note("そういうことがあるので、３年の雰囲気がすごくピリピリしているんだろうなって思います。正直に言うと、試験でいつもそれなりにいい成績を取ってはいるけど、私もなんだか自分に自信がなくなってきています。\n\n\n\n\n")

$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show



"こんな他愛ない会話が、懐かしい気持ちをかき立てる。病院に戻ったかのような気分になる。"
"折に触れ岩魚子が立ち寄って、クラスの出来事をかいつまんで教えてくれた。その当時でさえ、もう二度とそこには戻れないだろうという予感はあった。"


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

$ written_note("私たちがもう最高学年だっていうのが、とても変な感じだと思わない？　月日は本当にあっという間に過ぎてしまった。どこに行っちゃったんだろう。新しく入ってきた１年生はとっても初々しくて、なんだかすごく純真に見えます。私も１年の時はあんな風だったのかな、なんていつも考えてます。１学期の間ずっと、そんなノスタルジックな気持ちを抱いてました。\n\n\n")

show ev hisao_letter_open:
    "ev hisao_letter_open_2" with locationchange
with None

$ written_note("他にも言いたいことがあります。冬のあの時から、言わなくちゃいけなかったことがあると思って、こうして手紙を書いています。直接伝えることができなかったのを、本当に後悔しています。言い訳のしようもありません。\n\n\n\n\n")

$ written_note("本当のことを言うと、病院にお見舞いに行くたびに、久夫くんのことが心配になりました。あなたの健康のことじゃありません。あなたはずっと遠ざかって、希望をなくしたように見えました。もちろん、あんなことがあった後では当然だと思います。でもなんだか、あなたはなにかをあきらめたような気がしました。もしかしたら、あきらめたのは「幸せ」だったのかも？\n")

$ written_note("なんとかして自分の気持ちを伝えたいと思ったけど、それにふさわしい言葉は見つけられませんでした。あなたを慰める言葉を、私は何も言えませんでした。あなたのことがこんなに好きだったのに、一番大事なときに支えることができなくて、本当にごめんなさい。でも少なくとも今は、やっと、もっと自分に正直になれます。\n\n\n\n")

$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show


"ずいぶん都合良く誠実さを取り戻してくれたもんだ。そう思う一方で、岩魚子が正しいというのもわかっている。『遠ざかって、希望をなくした』というのはいい表現だな。俺もあきらめてしまっていたのかもしれない。"





"病院でベッドに横たわって、ついに岩魚子が姿を現さなくなったときの苦い気持ちを思い返すと、心が重くなる。"
"驚きはなかったし、俺に驚く資格なんてなかった。岩魚子が来なくなることしか俺は望んでいなかったのに、それでも来続けることなんてどうしてできるだろう？"




"岩魚子が見舞いに来たのは、あの出来事からたったの六週間後までだった。俺が岩魚子から遠ざかったのだとすれば、それは彼女が顔を出した瞬間から、向こうが距離を置き始めているのが感じ取れたからだ。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

$ written_note("２月と３月の、あの静かな日々に戻れるなら、自分をあきらめないで、とあなたに伝えると思います。きっとそう言います。なんでもいいからあなたに話しかけてさえいれば、こんなに遠くへ行ってしまうこともなかったかもしれません。あなたが自分の力で立ち直れているといいな、と思います。\n\n\n\n")


$ written_note("今の私たちは物理的にも遠く離れてしまっていて、それがなんだかずっと決定的なように感じます。もう一度会うことはできるのかな。もしかしたら、会わないほうがいいのかも？　でも、もし連絡を取りたいと思ったら、ぜひお返事ください。あなたの新しい学校のこととか、今どんな風に過ごしているかとか、とても聞いてみたいです。元気でね。\n\nかしこ、\n岩魚子")

$ renpy.music.set_volume(1.0, 1.0, channel="music")

window show


"おかしな感じだ。岩魚子からまた連絡が来ることなんて絶対ないのはわかりきっている。"


"本当に連絡を取り合いたいなら、郵便なんて手段を使ったりはしないだろう。俺の住所を知ることができたなら、メールアドレスや電話番号を知るのだってたいした手間じゃないはずだ。これはただのお別れでしかない。"


stop music fadeout 4.0


"手紙を読んでいる間、呼吸をするのも忘れていたことにたった今気づいて、俺は息を吐く。これで遠ざかったのはどっちだよ、岩魚子？　でも確かに、これが一番いいのかもしれないな。"



"岩魚子がわざわざペンを取ってこの手紙を書くとすれば、それは俺たちがあんな終わり方をしたのを後ろめたいと思っていたから、という以外にありえない。"
"俺たちが漂うようにお互いの人生から離れていったことに、岩魚子は心を痛めていた。そのことに俺は痛々しい幸福感を覚える。"



"もう少しで感謝の気持ちを抱きそうになる。岩魚子も返事を求めていないとわかっているから、そう思わないだけだ。"

play sound sfx_doorknock

scene bg school_dormhisao
with locationchange


"ドアがノックされ、その一ミリ秒ほど後に構わずドアが開く。鍵をかけるのを忘れていた。俺のバカ。"


ke "よう、元気か？　なんでドア開いてるんだ？"


"たった数十センチ先にある、ドア一枚で隔てられているだけの薬の山を健二が目にしないよう、俺はおそらく自分の体調にとって安全な速度よりも素早くドアに駆け寄る。"


"と思うと、手には例の手紙を握ったままだ。そのことを問いただされたら、たぶん満足な言い訳は思いつけないだろう。"


"健二から５０センチの距離で、こいつはあまりに目が悪いから、そもそも気にするまでもなかったことに気づく。もう少しで俺がタックルをかまして部屋から押し出す勢いだったのに、健二は気づきもしなかったし。"

scene bg school_dormhallway
show kenji tsun_close at center
with locationchange

play music music_kenji fadein 0.5


ke "おい、なんなんだよ？"


hi "お前何言ってんだ？　自分の部屋には百万個くらい鍵かけておいて、他人の部屋にはむりやり入ってくるのかよ"


hi "ノックしてドアを開けるまで一秒も待たなかったじゃないか。というか同時だったぞ。ノックしたときにはお前はもうドアを開けてたんだよ"

show kenji happy_close
with charachange



ke "ほらな？　だからこそこんなにたくさん鍵をかけてるんだよ。外の世界は非情で冷淡だ。押し入ってくる客だらけの世界だ。これでわかっただろ"




show kenji neutral_close
with charachange


ke "今貴重な教訓を教えてやったんだぞ、お前。知識は力だぜ。なに怒鳴ってんだよ？　こっちは英雄なんだぞ"

show kenji tsun_close
with charachange



ke "自分を見てみろ……ドアに鍵もかけてなかったじゃねえか。普通の女だったらもうお前は１０億回は殺されて、あげく本物と見分けのつかない女のクローンに差し替えられてたところだぞ。俺もやられそうになった"




"わけがわからないので後半は無視するけど、こんなことを健二が言うってのは笑えるな。自分が頭からタックルされるのは止められなかったくせに、女の人が俺を１０億回も殺せるっていうのか。"
"こいつが英雄だったら俺たちはみんなおしまいだよ。"


show kenji happy_close
with charachange


ke "それ、何持ってるんだ？"


"どういうわけか、俺が手に持っている手紙は見えているようだ。さんざん振り回していたから不思議ではないけど。素早く折り畳むけど、わざわざ背中に隠すとか、そういうことはしない。そこまでしたら怪しすぎる。"


"どうやら岩魚子が手紙を送ってきたことに、俺は思っていたより動揺しているみたいだ。"


hi "手紙をもらったんだ"

show kenji neutral_close
with charachange


ke "ああ、そうだ、俺がそこに置いたんだ。寝てたんだけど、爆発音が聞こえて目が覚めてさ"


ke "ヘルメットかぶって、外で何が起きているかのぞいてみたんだ。でも生徒会の女がお前の部屋のドアをバンバン叩いてるだけだった。髪がピンクじゃない方だったぜ"

show kenji tsun_close
with charachange



ke "ものすごい音を立ててたから殺意に満ちてるのは明らかだったな。お前への殺意だ。そしたらなぜかこっちに気がついて、俺も逃げようとしたんだけど間に合わなかった。そいつは俺を捕まえてドアを指さしたんだ"



"俺は口を開いて、静音は耳が聞こえないと言おうとしたけど、やめる。いろいろな理由で。"


ke "何が言いたいのかわからなかったんで、向こうも余計腹を立ててさ。年取ったおっさんがスマホを使おうとしてるみたいに"


show kenji happy_close
with charachange


ke "殺されるところだった。そいつに殺されて、女の俺に置き換えられるところだった。でも俺の眼鏡に太陽の光が当たって、そいつの目をくらませたから、俺は助かったんだ"

show kenji neutral_close
with charachange



ke "見よ、オプティックブラスト！　みたいに。眼鏡かけた人が眼鏡で傷つくってのはよくわからんけどな。向こうだって眼鏡かけてるんだから、眼鏡の殺人ビームは効果がないはずなのに"


ke "……とにかく。そいつはお前宛の封筒を俺に渡して、そのまま帰って行った。明らかにそいつは血に飢えていた"

show kenji happy_close
with charachange



ke "だからお前は外出してるってうそをついたんだ。ていうか外出してたんだろ？　俺の宿題を手伝う気はないかって、一週間くらい聞こうとしてたのに、全然返事なかったからさ……よく帰ってきたな！"



hi "ありがとよ"

show kenji neutral_close
with charachange



ke "ああ、それで封筒を渡されて、お前の名前が書いてある。自分で持ってるのもいやだったからさ。もし爆弾だったらどうするよ？　だからそいつがいなくなった後に、お前の部屋のドアの下に突っ込んでおいたわけ"



ke "言うつもりだったんだけど、俺が言う前にお前が戻ってきたからさ。少なくとも爆弾じゃなかったしな"


hi "そっか、ありがとう。でもお前の数学の宿題は手伝わないぜ。数学の教科書が爆弾だったらどうするんだよ？"

show kenji tsun_close
with charachange


"ショックを受けているようだ。ついでに、本当に教科書が爆弾である可能性も考えているように見える。ないとは言えないだろうな。みんな教科書なんてほとんど使ってないし。"

scene bg school_dormhisao
with locationchange



"俺は背後のドレッサーに手紙を放り投げて踵を返すと、後ろ手にドアを振って閉じる。"
"ドアは健二の靴のつま先にぶつかってそのまま跳ね返るように開き、健二は実際に感じているはずの痛みよりも大げさにぴょんぴょん跳ねている。"


show kenji neutral at center
with charaenter


"あっという間に健二は部屋の中に入っていた。健二が手紙を手に取るのを、俺は止めることができない。それを囲んでいる薬瓶の山にはなぜか気づいていないけど。"


hi "他人の手紙を読むんじゃないよ"

show kenji happy
with charachange



ke "いいだろ、なんなんだよ？　彼女からのラブレターか？　写真同封か？　エロい写真は？"


play sound sfx_dropstuff
stop music fadeout 4.0


"ドレッサーによりかかって、上に乗っていた薬瓶が床にちらばるのを気にもとめず、健二は岩魚子の手紙を静かに読み進める。"


"読み終えるまで果てしない時間がかかるかのようだった。顔に思い切り手紙を近づけているので、まるで手紙を食べようとしているみたいだ。"

show kenji tsun
with charachange


ke "『岩魚子』って誰だ？"


hi "俺の元カノだよ"

play music music_night fadein 4.0

show kenji neutral
with charachange


ke "へえ、元カノか？　じゃあこれは別れの手紙ってわけだ。こんなの伝説だと思ってたぜ"




hi "伝説じゃないさ。まあそうなんだろうけど、でも実際、その子と別れたのはかなり前だから。もう立ち直ったよ"



"健二はサムズアップで答える。俺が話を気まずい方向に持って行かなかったことに明らかに安心している。そうしてやりたい気持ちもあるけど。手紙を読むなと言ったのに読んだし。"



show kenji happy
with charachange


ke "そうだな、いい心構えだ。どうってことないさ、俺だってきつい別れ話は経験あるからな。でもそれで気落ちしちゃだめだ。というかさ、俺を見ろよ"


hi "ええええ……"


ke "でもさ、お前、向こうは手紙書いてくれたんだぞ。もしかしたらよりを戻したいのかもしれないじゃん、な？　ここに書いてあるだろ、返事してって。返事してやれよ。その子かわいいか？"


"フェミニストがあらゆる男を奴隷にしようとしていると信じている奴にしては、ずいぶんかわいい女の子にご執心じゃないか。"


hi "彼女ならもういるよ。それに文脈をちゃんと読めよ。俺に返事してほしいなんて思ってないよ。そう書いてあるからって、本当にそう思ってるわけじゃないんだよ"

show kenji neutral
with charachange


ke "でもそう書いてあるじゃないか。この岩で魚で子供のお姉ちゃんはまだお前に気があるんだよ。わざわざここに書いてるだろ"




hi "読んだよ。何が書いてあるかもわかってるよ。だから言ってるだろ、文脈を考えろって。俺が岩魚子から離れてしまったって書いてある。そこの一字一句が、向こうがそれを受け入れたってことを示してるんだよ"


hi "たぶん、岩魚子が手紙を書いたのは、ただいい雰囲気で別れたかったからでしかないんだよ。でも俺たちは終わったんだ。あいつはよりを戻したいとか、お前が思ってるようなことは考えてない"


"考えれば考えるほど、自分がただのいいわけをしているだけのように聞こえてくる。こんなのは不毛だ。"


"岩魚子が俺の返事を求めていないのははっきりしている。それには耐えられる。もし俺が返事を書いて、期待していたよりも厳しい返事が来たら、それとも返事がなかったら、俺はたぶんつぶれてしまう。"





"その恐怖があるから、俺は自分の決断を正当化しようとしているのかもしれない。可能性はあるけど、考えたくはない。ひどく不愉快な考えだ。"


hi "だいたい、どうしてそこまでお前がこだわるんだよ？"

show kenji happy
with charachange


ke "お前は返事をするべきだからさ。向こうはそれを望んでる。俺はその返事を見てみたい"


show kenji neutral
with charachange


ke "ったく、別にいい返事じゃなくたっていいんだよ。それでもいいけど、でもお前が怒りの手紙を書いて呼び出したっていい。俺の新しい攻撃戦略だぜ、とりあえず女を呼び出すんだ。やってみろよ"


hi "手紙を書いてきたとしても、その意味を考えなきゃだめなんだよ。今の時代、人に手紙を書くことの意味が違うんだ。普通にやるようなことじゃない。今みたいな状況では違うんだよ"


hi "電話を使えば一瞬で世界中の誰にでもかけられて、隣にその人がいるのとほとんど同じ感じで話ができるだろ。それともメールを送ったっていい。一瞬でメールが来たってわかって、手軽に返事ができる"


hi "手紙だって親しい内容のこともあるけど、でも岩魚子は俺と距離を置いておきたいと思ったんだ。ひょいと向こうに行って会ったりできるわけじゃない"


hi "電話番号を知っていれば電話したよ。メールアドレスを知っていればメールも出した。本当に返事が欲しいと思ってるなら、番号なりアドレスなりを手紙に書いておいてもいいじゃないか"


"俺が岩魚子の手紙に動揺していないとひたすら自分に言い聞かせているのがバカみたいに思えてくる。これじゃどう見ても動揺しているじゃないか。"

show kenji tsun
with charachange


ke "向こうは徐々に進めていきたいってことなんじゃないの。電話をするにはまだ恥ずかしい、とかな。そういえば俺の彼女なんてすごくシャイでさ、いつもメールばかり送ってくるんだ。すげえウザかったけどな"




ke "電話なんてどうでも良かったから一つも持ってなかったんだ。しかも実はメール一通受信するたびに金がかかるんだぜ。でも電話嫌いだったから、こっちから電話かけて送ってくるなって言うこともできなかった"



show kenji neutral
with charachange


ke "結局伝えたけどな。呼び出したんだ。電話も使ったんだぜ。文字通りお呼び出しだよ"


hi "そうだろうな"


"健二が正しかったとしても、それは岩魚子がまだ俺と距離を置いておきたいということだ。俺と気楽におしゃべりする『心の準備ができていない』ってことだ。"


"どうして？　俺は変人か何かだって言うのか？　だとしたら、岩魚子の行動では何も安心できない。考えすぎかもしれないけど、とにかくまるでわからない。"


"健二はそれ以上何も言葉を続けられず、その後の沈黙が余りに気まずくて重たかったので、俺は健二が適当な理由を作って部屋から出ていくまでの秒数を数え始める。"

show kenji tsun
with charachange


ke "また会いたいなあ……"


hi "元カノに？"


ke "ああ。あいつ頭はおかしかったけど、一緒にいるのは楽しかったからな"



ke "背中が痛むんだ。あいつがいれば、マッサージしてくれって頼むこともできた。オーブンの使い方も俺はわからなくてさ。焼いた食い物も恋しいなあ"
ke "それと、時々廊下でボーリングしてたんだ。あれも懐かしいな。この前の学園祭じゃ、一人きりでやるはめになったし"



hi "廊下でボーリングするのか？　人にぶつかるだろ"


ke "あいつも、いつも同じこと言ってたよ……"



"健二は懐かしそうにため息をつく。人がボーリングのピンで足を滑らせてひどいけがをする可能性をまるで考えていない。一緒に遊んでいたってことは、健二の彼女も考えてなかったんだろう。"
"実に奇妙な愛情のあり方だけど、でも大したものだ。"



hi "お前こそ彼女に手紙書けばいいんじゃないの。返事が返ってきたら結婚できるぜ"

stop music fadeout 0.3

show kenji rage
with charachange


ke "結婚！？　いや。いやいやいや。それはないな"


hi "わかったよ。でもどうして？　お前どう見てもその人のこと好きなんだろ。女は憎んでるくせに"

show kenji tsun
with charachange

play music music_kenji fadein 2.0



ke "フェミニスト！　女じゃない、フェミニストだ。違うんだよ。ったく、お前の区別のしかたは信じられないな。相関関係と因果関係は違う"
ke "頭がおかしい女だからといって、そいつがフェミニストで頭のおかしい女だとは限らないんだ"



show kenji neutral
with charachange


ke "証拠がないことが、存在しないことの証拠にならないのと同じだ。それが本当なら、相対的特性によって、証拠の存在が存在の証拠とイコールにならなくなる"





hi "いやイコールだと思うぞ。あと相対的特性とは言わないんじゃないか"

show kenji tsun
with charachange


ke "うるさい黙れ、数学だ！　数学が間違ってるっていうのか？"


"お前が間違ってると思う。"


"この健二にも好きな人がいたんだな。元カノと別れた理由とか、その他諸々について根ほり葉ほり聞いてみたくなるけど、やめておこう。立ち入りすぎているし、同じ質問を返されるかもしれない。"

stop music fadeout 8.0


"話しているうちに静音のことを思い起こす。でも頭に浮かぶ思考はちらかっていて、かすんでいる。疑問ばかりだ。"


"そもそも俺に岩魚子を愛するチャンスなんてあったんだろうか。この岩魚子とのいきさつ全てが、まだ俺には痛い。後味の悪さが心の奥に残っている。"


"静音の方がずっと好きだ。でも俺は静音の後を追いかけている気がする。今でも。追いかけるのは苦にならないけど、俺は二人の距離をもっと縮めたい。"


"岩魚子の手紙もその理由ではあるけど、前からそういう気持ちは抱いていた。近づきはしたけど、これじゃ足りない。もう一度やってみたい。今すぐに。"

hide kenji
with charaexit


"着替えたいので部屋を出ろと健二に伝え、俺は生徒会室に向かう。"

scene bg school_courtyard
with locationskip


"今日のグラウンドはほとんど無人だ。残念だな、今日はすごくいい天気なのに。"

scene bg school_hallway3
with locationskip

play sound sfx_doorknock2


"ノックをしたけど、誰も返事をしない。そのまま入ろうとするけど、ドアに鍵がかかっている。ドアノブから手を離すと、ほこりまみれになっている。俺たちが出かけてから、誰もここには来ていないようだ。"


"もうここまで出てきて服も着替えているので、町まで食事しに行くか。財布は部屋に置いてきてしまったけど。"

scene ev misha_sad:
    truecenter
    subpixel True zoom 1.05
    easein 10.0 zoom 1.0
with locationskip


"部屋に戻る途中、本校舎の裏で座っているミーシャを見つける。"


"眠っているのか、目は閉じていて、とても安らかに見える。今まで、ぴょんぴょん跳ねまわったり、落ち着きなさそうにつま先立ちで飛び回ったりしていないミーシャを想像するのはとても難しかった。"


"本能的に、声をかけて静音を見ていないかと尋ねるか、いっしょに町に行かないかと誘おうとしたけど、このミーシャの姿を見て邪魔をする気にはなれなかったので、そっとしておく。"


scene black
with dissolve

$ suppress_window_after_timeskip = True

label jp_S25:

window hide None

scene bg school_council_bw
with locationchange

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_pearly

nvl clear
nvl show dissolve


n "\n\n\n戻ってから数日の間、自分が生徒会員であることを忘れそうだった。休みの終わりくらいになると生徒会の仕事がとても忙しくなるという話はあちこちで聞いていたけど、そうとも限らなかったみたいだ。"


n "静音かミーシャを捕まえられたことはほとんどなくて、あっても手助けが必要かと聞くこともできないほど急いでいた。急いでいないときでも、捕まるのはミーシャだけだ。"


n "\n静音からは決まって、仕事はあってもまるで大したことのない量だから、ミーシャや俺が関わっても退屈するだけだ、と言っていた。"


n "\n\nしばらくして、少し自由な時間を過ごそうという気持ちがだんだん強くなってきた。ひまが多すぎると感じる時期はまだあったけど。"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_council
show shizu basic_normal2 at center
with locationchange

window show


"でもようやく自由な時間の多さに慣れ始めてきたころ、また状況が変わる。俺はまた生徒会室に戻っていて、ティッシュの箱は投票箱にふさわしいかどうかについて静音と言い争っている。"


hi "だから言ってるだろ、細長いやつじゃなくて正方形のが手に入れば、絶対いけるって"


hi "ミーシャ、今の静音に伝えてくれないか？　今ちょっと手がいっぱいで……あー、やっぱいいや"


"ミーシャは投票用紙を切るのに忙しい。ちょっと手を滑らせたら、ハサミを人の頭に投げつけてしまいそうだ。"


"抱えていたポスターカラーの箱を、生徒会室にある自分用の小さな机の上に置くと、舞い上がったほこりが顔にかかって俺はせき込む。ほんとに間が空いてしまったな。"

show shizu behind_blank
with charachange


ssh "投票用紙の大きさを変えた方がいいと思う？"

show bg school_council at bgright
show shizu behind_blank at tworight
with charamove

show mishashort sign_confused at twoleft
with charaenter


mi "え～？　でもしっちゃん、もうこんなにいっぱい切っちゃったよ……"

show shizu basic_normal
with charachange


ssh "もっと小さくするのはどうかしら。それならもっと能率的になるわ。字を小さくすればいいだけだし。ひと箱に用紙が入る数も多くなる。そうすれば必要な紙の量も半分になるわ"

show shizu behind_smile
with charachange


ssh "投票の仕方も変えたらいいわね。もっと本物の選挙に近づけて。そうすれば買う箱の数も減らせるかもしれない"

show shizu adjust_happy
with charachange


ssh "余ったお金でピザが頼める。それとも中華とか、ケーキとか、新しいラーメン３杯とか。食べてみたいのがあるのよ"


"経費を１円の半分でも節約する手段を次々と考えつきながら、静音は意気込みたっぷりに眼鏡の縁を指でこする。"


"そもそも生徒会の予算額を知っているのは静音以外にいないと思うので、この選挙をするための予算がどれだけ少ないのか聞くのが怖くなる。"


hi "もうミーシャがこんなに用紙を切ってるんだけど。これどうするんだよ？"

show shizu basic_happy
with charachange


ssh "大丈夫、大丈夫。それで私がメモ帳を作って、購買で売るから"

show mishashort perky_confused
with charachange


mi "でもしっちゃん、これあんまり見た目がかわいくないよ～……"

show shizu adjust_frown
with charachange



"静音はそうは思っていないようで、今度はミーシャと言い争っているけど、その実態は『かわいい』と『かわいくない』を延々お互いに向かって手話で言い合っているだけだ。"
"やがて二人とも疲れ切ってしまって交互に相手のことを命令するように指さすだけになる。"




"変な感じがする。なんだかばかばかしく見えるというのもあるけど、この二人が意見を違えるのは今まで見たことがないからだ。"


"とはいえ、この数日は二人ともすごくくたびれているみたいだった。"


"実施はまだ数ヶ月先だというのに、このところ静音は生徒会選挙の話にますます没頭している。政権交代が目前に迫って、自分の時代が終わることを自覚した政治家はこういう風に振る舞うんだろうな、と思う。"


"数週間先まで掲示もされない張り紙のために習字の練習をしている今でさえ、俺は生徒会の活動に真剣になりきれずにいる。でも静音が真剣になる理由はわかる。"




"やっぱり、三年間も生徒会長を勤め上げてきたわけだしな。もっと前から生徒会長になりたがっていたとお父さんが言っていた。満足な気持ちで職を離れるには、三年という期間は短すぎるんだろうな。"


hi "先代の生徒会は、引き継ぎをスムーズにやるのにこれだけの手間暇をかけてたのか？"



show shizu behind_frustrated
with charachange


"静音は腹立たしげな顔になる。まったく役に立っていなかったというのが伝わってくる。"


hi "じゃあ、立派な前例を作るためにこれだけのことをしてるってわけだな？"

show shizu basic_frown
with charachange


shi "……"

show mishashort hips_frown
with charachange



mi "それは前例から少しでも教訓を学んでればの話だよ、ひっちゃん～！　そうじゃなかったら、わたし超怒っちゃうよ～！　もし後を継ぐ人が頼りなかったら、絶対しごいてやるから～"



"ミーシャが言うとあんまり恐ろしそうに聞こえないな。"


hi "じゃあ、もうその人たちには会ったのか？"

show shizu adjust_smug
with charachange


shi "……"

show mishashort hips_grin
with charachange


mi "あはは～。ひっちゃん、まだ立候補者はいないんだよ～！"


hi "え？　一人も？"

show shizu behind_smile
show mishashort hips_smile
with charachange



ssh "生徒会長の候補だっていないわ。だから私がこうしてこの役職への関心を喚起してるの。どう思う？"



"静音は誇らしげに、自ら作っていたポスターを手に掲げる。実に、その、ミリタリー系な感じだ。"




hi "もしかしたら、ちょっと入れ込みすぎかもしれないぜ"



show shizu adjust_frown
with charachange


"機嫌を損ねた静音は、顔をしかめて眼鏡をいじる。"


ssh "それって変？"


hi "変だよ"

show shizu behind_smile
with charachange


"俺が同意しなかったことに、静音は妙に嬉しそうだ。もし静音が今取りかかっていることに集中していなければ、おもしろそうだからというだけの理由で俺に議論を仕掛けてきただろう。"

show shizu basic_normal
with charachange


ssh "それの何が変なの？"

show shizu adjust_smug
with charachange


"結局議論はしかけてくるのか。と思うと、静音は素っ気なく手を振る。まるで空中に浮かぶ言葉を捕まえて削除するかのように。そのかわりに、静音は未来の後継者をすごい勢いで罵倒し始める。"


hi "まあ、ひとつ変なところを言えば、前の学校だと生徒会選挙があるのは半年先だよ。３月に卒業するわけだからさ。こんなに早くから考え始めるってのは結構変な感じだぜ"

show shizu behind_blank
with charachange


ssh "ここではちょっと事情が違うの"

show shizu adjust_frown
with charachange


shi "……"

show mishashort sign_smile
with charachange


mi "ひっちゃん、わたしが引退するのに後任がいなかったらがっかりしちゃうよ～！　ってしっちゃんが言ってる"

show mishashort hips_grin
with charachange


mi "でも～！　別に生徒会がなくても学校の運営が止まるわけじゃないから。プリントを配るのは大変になるだろうけどね～！"

show mishashort cross_laugh
with charachange


mi "ははは～"

show shizu basic_normal2
show mishashort cross_smile
with charachange


"でも静音は笑っていない。ミーシャの冗談で、静音は針で刺されたかのようにたじろぐ。そういうつもりで言ったわけではなかったとしても、ミーシャの皮肉には無神経な残酷さがあった。"

show shizu adjust_frown
with charachange


ssh "ふん。立候補者を増やそうと努力してるのに、みんな怠けてばかり。まだ締め切りがないからのんびりしてても大丈夫だと思ってる。怠け者だわ。先手必勝って言葉を知らないのかしら"


show shizu cross_angry
with charachange


ssh "『まだ』半年先ですって？　今すぐ行動しないんだったら、投票される資格なんてないわ！"

show mishashort sign_smile
with charachange


mi "生徒会長なんて、最後の最後で駆け込んですんなり就任できるような楽な仕事だって、みんなほんとにそう思ってるのかな～？　バカにしてるよね～！　ほんと～、ほんと～！"

show mishashort hips_frown
with charachange


mi "このちっちゃな机に座って、どれだけ仕事があるか見ただけで、踊り食いにされちゃうよ～！"


show shizu behind_frustrated
with charachange



ssh "これが本物の選挙だったら、みんな大変なことになるわよ。この前、公職選挙法について読んでいたの。どういうわけか、悪いのばっかりだけど"





hi "どういうわけか、ねえ"


"一瞬、静音がお父さんみたいに『話して』いて、しかもミーシャの口からその言葉が流れていた。気味が悪い。"


hi "まあ、第一にだな、影の将軍さんよ、それを決めるのはお前じゃない。選挙で選ばれるんだ。２つ目に、たかが学校の選挙だぜ。市議会とか国会議員を選ぶわけじゃない。公職選挙法は適用されないと思うぞ"



"そして３つ目、言いたくはないけど、静音があまりにこの選挙やら投票やらにやる気たっぷりなので、俺は心配になっている。"


"静音のお父さんによれば、そもそも選挙で生徒会長に当選したわけでもないらしい。考えてみると、静音自身が選ばれたという話を本人から聞いたことは一度もない。"


"じゃあ静音は生徒会に勧誘されて今の役職について、組織が崩壊して自分が最後の一人になるまで続けたってことか？　その可能性は考えたことがなかった。"


"そのことをどう受け止めればいいのかわからないけど、驚きはしない。今だって総勢三名でしかないんだし。"



"静音が生徒会長になったいきさつがそんなに悲しいものだったなら、そもそも投票なんてできないんじゃないか。関心もそのくらい低いか、下手をすれば全くないかもしれない。"
"あれだけの静音のエネルギーも、それでは無駄になってしまう。"



"俺は作業をしていたポスターの端に、無造作に感嘆符を書き付ける。ちょっと平凡だったので、ひとつ付け加えるくらいいいだろう。というか、まだ平凡かもしれない。感嘆符のサイズを倍にする。"


hi "やっぱりもう少しペースを下げた方がいいよ。これがあと何ヵ月も先にならないと意義がないことなら、ちょっと頑張りすぎじゃないか。俺はそう思う。心配しすぎだよ"


"俺は『意義』という単語の手話を知らなかった。試しにやってみても、あらぬところにポスターカラーで長い線を引いてしまうだけだった。こんなのもう直しようがない。"


hi "ミーシャ、静音に聞いてみてくれないか？"

show mishashort sign_smile
with charachange

show shizu adjust_happy
with charachange


"静音は静かにくすくすと笑う。音が漏れないようにわざわざ歯を食いしばっている。"

show shizu behind_blank
with charachange


ssh "だって、心配事はたくさんあるんだもの"


hi "たとえばどんな？"

show shizu basic_normal
with charachange


ssh "たとえば……投票箱はたいてい、とてもかわいらしい見た目になるから、みんな持って行ってしまうの。それに備えておかないとね"

show mishashort hips_grin
with charachange


mi "わはは～！　じゃあ今度はへんてこな見た目にしないとね。そしたら誰も持っていかないよ！　どうかな、しっちゃん～？"


hi "箱に変な顔なんか描くのもいいかもな。それとも、一つ一つの箱に静音の小さな絵を貼り付けるとか。『盗んではいけません』ってせりふつきでさ"

show shizu behind_frown
with charachange


ssh "だめ。笑い事じゃないのよ！　それに問題はそれだけじゃないの。もちろん投票率の話だってあるし……"

show shizu basic_normal2
with charachange


ssh "……最悪の事態は、立候補者が一人も現れないってことね"



"冗談で言っているみたいだけど、手話をするときの笑い方を見ていると、そういう風には受け取れない。"


show mishashort cross_laugh
with charachange


"ミーシャでさえその可能性が高いことはわかっている。雰囲気を変えようと、静音の言葉を笑い声で強調してみるけど、効果はない。"

show shizu behind_frustrated
with charachange


shi "……"

show shizu basic_angry
with charachange


ssh "二人ともどうしちゃったの？"

show shizu adjust_frown
with charachange


ssh "今のはただの冗談よ。今年は本当に関心が出てきてるの。もし何もなかったら、わざわざこれだけの仕事をしてると思う？　私だってバカじゃないんだから"



show shizu behind_smile
with charachange


ssh "選挙が終わったら、みんなに夕食をおごってあげる。もうプランも立ててるの"


hi "次の生徒会メンバーにもか？"

show shizu adjust_smug
with charachange


ssh "いいえ、そっちは自分たちで祝勝ディナーをすればいいの。こっちは今の生徒会メンバーだけ。感謝もされない仕事を延々続けてるのにけりがついたら、私も楽しい気持ちになれるわ"

show mishashort hips_grin
with charachange



mi "わたしたちだけの夕ごはん～？　やったあ～！　ちっちゃなパーティみたいだね、しっちゃん～！"


stop music fadeout 3.0


"無理をして陽気に振る舞っているのは明らかだけど、俺は何も言わない。その時限が終わるまで、幸いそれは短い間だったけど、俺たちは静かに作業をする。"

scene bg school_hallway3
with shorttimeskip

play music music_daily fadein 0.5


"授業の後、生徒会室のドアに鍵がかかっているのに気づく。おかしい。さっきまで静音はあんなに忙しそうにしていたから、放課後も仕事をしていると思っていたのに。普段の静音ならそうしている。"


"俺のアドバイスを聞き入れて、休みを入れることにしたのかもしれない。そんなに単純な話だったらいいけど。"

scene bg school_courtyard_ss
with locationskip



"少し落ち着かない気分のまま、俺は学校の周りを散歩する。でも半分は上の空だ。"
"いつ自分で足を動かし始めたか思い出せないのに、もうさんざん敷地内を歩き回って足がくたびれていた。それに何の意味があるわけでもないけど。"



"ちょっと校庭を散歩したくらいで、もうへとへとだなんて。本当にひどいもんだ。"

scene bg school_hallway3
with locationskip


"あっという間に、生徒会室の前に戻ってきてしまった。しかも今度は別の誰かがいる。"

show mishashort hips_smile at center
with charaenter


mi "こんちは、ひっちゃ～ん！"


hi "そこ鍵かかってるだろ"


"ミーシャがレモネードの缶を手に持っているのを見て、俺は反射的に近くの自動販売機を探している。のどが渇いて仕方ない。"

show mishashort sign_smile
with charachange


mi "そんなのわかってるよ、ひっちゃん～！　しっちゃんはどっか行っちゃってるんだろうね、たぶん～！"


hi "変だよな"

show mishashort hips_grin
with charachange



mi "あははは～。わたしたちはいつも一緒ってわけじゃないんだよ、ひっちゃん～"






"ミーシャはぐいっとレモネードを飲み、やがて缶を逆さにして、最後の一滴まで口に流し込む。なんかバカにされているような気になる。"

show mishashort perky_smile
with charachange


mi "ひっちゃんもほしい～？"




hi "いや、いいよ。他の人が飲んだのは受け取れないよ。失礼だろ。それにお前、俺のことからかってないか？　たった今全部飲み干したじゃないか"


show mishashort sign_smile
with charachange



mi "かばんの中にもう一つあるんだよ～！　準備してたんだよ、ほらねほらね～？　わたしってしっちゃんみたいだよね～！"



hi "静音は準備が良すぎるけどな。まあ、多少でもそれがお前に移ってるのはいいことだよ。何年だっけ、二年経って、ようやくか？"

show mishashort cross_laugh
with charachange


mi "わはは～！"


"俺が飲む間、ミーシャがこっちを見つめてくる視線がちょっと変な感じだ。でもあまりにありがたくて、俺は気にとめない。"


hi "お前と静音は、いつも俺になんかおごってくれるよな。だんだん恥ずかしくなってくるよ"

show mishashort hips_smile
with charachange


mi "ほんとに～、ひっちゃん？　あはは～。じゃあたまにはわたしにもお昼おごってよ、ね～？　そしたら～！　貸し借りなしだよ"


hi "まあ、お前がそういうこと言うのはおかしな話だな。俺も町まで食事しに行かないかって誘おうと思ってたんだ……"

show mishashort hips_grin
with charachange


mi "いいね～いいね～！　わたし、今日すっごくおなかすいてるんだ！　ありがと！"

show mishashort invis at tworight
with dissolvecharamove

stop music fadeout 3.0



"……昨日は。昨日は誘おうと思ってたんだ。俺が言い切る前にミーシャが話を切る。それを正す間を見つけられないまま、ミーシャは笑いながら、興奮して腕をばたばたと羽ばたかせ、俺の周りを勢いよく駆け回る。"


scene bg suburb_roadcenter_ss
with locationskip

play music music_dreamy fadein 2.0



"もう財布は持っているから、そのまま町に向かって歩き始める。ミーシャは俺の後ろについてきていて、暇そうに自分の手をもてあそびながら、どこで食べるのがいいかと大声で独り言を言っている。"
"少なくとも俺にはそう思える。俺に聞いているのかもしれないけど。"



hi "どこか行きたいところ、あるか？"

show mishashort hips_smile_ss at center
with charaenter


mi "ん～～～～、お茶屋さんに行きたいな。あそこはすっごく大きなパフェがあるんだよ"


hi "前に行ったときもパフェ食べてたよな。あれすごく大きそうだったけど"

show mishashort hips_grin_ss
with charachange


mi "ちがうちがうちがう～！　今度のはすっごく、すっご～く大きいの！　それにとっても高いんだよ～！"


hi "すっごく、すっご～く高い？"

show mishashort cross_laugh_ss
with charachange


mi "ははは～！　ちょっとだけ～……"


hi "ったく。まあ、お前と静音は何度も俺にメシおごってくれてるからな、いいよ"

show mishashort perky_confused_ss
with charachange


mi "ひっちゃん、わたしは一度もおごってないと思うよ～。しっちゃんだけだったんじゃないの？"


hi "ただで食事できるってのにマジで文句言ってるのか？　心配するなって"

scene bg suburb_shanghaiint
with locationskip


"俺たちは上海に行き、驚いたことに優子さんではないウェイトレスに席まで案内される。"


"ミーシャは例のパフェを食べる気で満々だ。店に入るが早いか、大声で注文をする。品が届いてみると、確かにとても大きなサイズで、しかも高そうな見た目だ。"

show mishashort perky_confused_close at center
with charaenter


mi "ひっちゃんは何も頼まないの～？　おなか空いてるなら、食べていいよ"


hi "いや、俺パフェ好きじゃないんだ。あの砂糖がかかったアーモンドが苦手でさ"




show mishashort sign_smile_close
with charachange


mi "どければいいじゃん～！"


hi "アーモンドだけどけるなんて無理だよ。バカなこと言うな"

show mishashort perky_smile_close
with charachange


"できたとしても、ミーシャはパフェをぐちゃぐちゃに混ぜていて、もうどけることなんて不可能だ。しかもなんだか見た目も気持ち悪い。"


"あれだけの味がちゃんと良く混ざるのか、疑問に思う。ミーシャはほんとにこのドロドロを味わうことができるんだろうか？　食べている様子はとてもおいしそうだけど。"

show mishashort hips_grin_close
with charachange


mi "んん～、パフェ最高～、わたし歯が知覚過敏だから、アイスクリームはだめなんだ～。でもケーキは柔らかすぎるし、アイシングが多すぎると飽きちゃうの。パフェっておもしろいんだよ"

show mishashort perky_smile_close
with charachange


mi "この町の喫茶店で、パフェを出すお店は何件あるでしょう～？　１０件はあると思うよ！　全部試したことがあるけど、これが一番好き。小さなフランがついてるんだよ～！"


hi "デザートの専門家みたいなこと言ってるな"

show mishashort hips_smile_close
with charachange


mi "デザートだけじゃないよ～！　わたしはいろんなおいしいものが食べたいの～"

show mishashort hips_grin_close
with charachange


mi "将来、松坂牛を２キロ買えるくらいのお金を貯めるんだ～！"


hi "それって１０万円以上するんじゃないか……じゃあそういう退廃的な食べ物がお前の趣味ってわけか？"



"ある人のことを知るのに数ヶ月もかけたりするのは趣味とは言わないだろう。考えてみると、すごく失礼だったな。それにずいぶんお金の掛かりそうな趣味だ。"




show mishashort perky_confused_close
with charachange



mi "そうだね～！　……たいはいてき～？"



hi "ああ"

show mishashort hips_grin_close
with charachange



"ミーシャは手を顔に持って行きながら、ケラケラと笑う。アイスクリームが鼻についてしまったみたいだ。ミーシャは気づかない。俺は気づいてしまう。自分で拭いてくれればいいのに。"
"そのことを伝えようとすると、突然ミーシャが口を開く。"


show mishashort perky_confused_close
with charachange


mi "それ、なんて意味かわかんないよ"


hi "そっか。まあ、どっちみちいい意味の言葉じゃないよ。言外の意味があるんだ。美食のほうがいいな。おいしいものを食べるのを楽しむ人、って意味。でもこれじゃ形容詞か。美食家っていうのが正解だな"

show mishashort cross_laugh_close
with charachange


mi "わはは～！"

show mishashort cross_grin_close
with charachange


mi "ひっちゃん、話がくどすぎるよ"


hi "悪い"

show mishashort perky_smile_close
with charachange


mi "ははは～。ひっちゃんのそういうところが、しっちゃんは好きなんだと思うよ"


hi "おれがくどいから？　じゃあ類語辞典を買っておかないとな"

show mishashort hips_grin_close
with charachange



mi "わはは～！　違うよ、そういう意味じゃないよ、ひっちゃん～！"



"やっぱりコーヒーを頼むことにする。でもウェイトレスが気づくまで時間がかかる。コーヒーが出てくるまで同じくらい時間がかかるだろう、と思う。"



"店内が客で埋まりつつある。ミーシャがデザートをつついているうちに、もう一時間はここに居座っているのだから、それも当然だ。"
"俺はコーヒーをテイクアウトにしてくれと頼むけど、ミーシャもコーヒーを頼んだので、思ったよりも長居をすることになりそうだ。"



hi "本当、そんなに簡単だったらいいのにって思うぜ。最近静音に話しかけるのが大変なんだ"

show mishashort sign_smile_close
with charachange


mi "しっちゃんはずっと選挙の準備で忙しいんだよ～！"




hi "楽しいことばかりやってるわけにはいかない、ってのはわかるよ。ただ、静音に言いたいことがいっぱいある。でもここぞって時にいつも失敗するんだけどな。しかも今はそうする時間さえない。選挙の準備で"






hi "ずっと先の話だっていうのにさ"

show mishashort hips_frown_close
with charachange


mi "ひっちゃん、しっちゃんがひっちゃんのこと避けてるって思ってる？"



"ミーシャは怒っているように聞こえる。そういう反応は予想していたけど、俺はそんなことは全く思っていない。"



hi "いいや"

show mishashort perky_sad_close
with charachange


mi "そっか～……"


"その夢見心地のような答え方を聞くと、ミーシャは俺の答えにがっかりしているんじゃないかと思えてくる。だったら、それはミーシャ自身の考えなのかもしれない。"
"そんな質問をするのは落ち着きが悪いけど、ミーシャなら正直に答えてくれると信じている。さもなければこんなことは夢にも思わないだろう。"



hi "お前はそう思うか？"

show mishashort hips_smile_close
with charachange



mi "もちろん違うよ、ひっちゃん～！　でも～！　……ときどき、イライラすることはあるよ～。しっちゃんはすごくエネルギーがあって、いろんな人が自分と同じくらい物事に熱心になるよう努力してるよ～"


show mishashort perky_sad_close
with charachange



mi "でも、みんなが本当に熱心になったとき、しっちゃんはどうすればいいのかわからないみたい"
mi "それとも～！　しっちゃんは絶対に間違いが起きないようにしようとしてるんだと思う。わたしが手伝おうとすると、しっちゃんはいっつもわたしを追い払うの"



mi "それってイライラするよ"



show mishashort hips_grin_close
with charachange


mi "たぶん、考えすぎなだけだよね～！　そうでしょ～？"


"ミーシャはカップに入ったコーヒーをごくりと飲むと、舌を突き出す。"

show mishashort hips_laugh_close
with charachange


mi "ふえ～！　あちゃちゃちゃ～……もう冷めたころだと思ってたのに～！"


hi "そんなに時間たってたか？"


"腕時計をみる。時間は全然たっていない。でも外を見ると、もう日が沈もうとしている。"


hi "そうでもないな。あー、でも今日はけっこう日が沈むのが早かったな。お前がそう思ったのもわかるよ"

show mishashort perky_sad_close
with charachange


"俺がそう言ったとたん、ミーシャは外を見てすぐにあくびをする。眠そうだ。変だな、だって……"


hi "お前眠いのか？　たった今までバッチリ目が覚めてたじゃないか"


show mishashort sign_sad_close
with charachange


mi "暗くなると疲れちゃうんだよ、ひっちゃん～"


hi "そんな一瞬でか？　鳥かよ？"

show mishashort perky_smile_close
with charachange


mi "あははは～"


"俺は自分のコーヒーを手にとって一口飲む。全然熱くないけど、とてもおいしい。俺も早く寮の部屋に戻りたかったので、できるだけ早く飲み干す。ミーシャも俺に続こうとするけど、まだ熱すぎるみたいだ。"


"ミーシャが飲み終わるのを待つ間、静音が俺のどういうところが好きか、というさっきのミーシャの話の意味を考える。急に俺も知りたくなった。でもいまさらその話題を蒸し返すのは余計なことのように感じる。"

show mishashort hips_grin_close
play sound sfx_impact
with vpunch


"どうしようかともう一度考えたけど、ミーシャが大きな音を立てて空の紙コップを机に叩きつけたので、その思考も中断する。"

show mishashort cross_grin_close
with charachange


mi "ごちそうさま～！"



"とても満足しているようで、ミーシャは短い笑い声を漏らす。幼児みたいだ。小さいときもあのドリルみたいな髪型だったのかな、と思う。それとも最近のスタイルにもっと近いのか？　そのほうが筋は通っているな。"



hi "じゃあそろそろ戻った方がいいな。ウェイトレスが見つからないけど。サンデーの会計してくるから、ばったり眠ったりするなよ、いいな？"

show mishashort sign_smile_close
with charachange


mi "サンデーじゃないよ、パフェだよ、ひっちゃん"

show mishashort cross_laugh_close
with charachange


mi "わはは～"


hi "鼻にアイスついてるぞ"

stop music fadeout 2.0

scene black
with dissolve


label jp_S26:

scene bg school_scienceroom at right
with locationchange

play sound sfx_paper
play music music_normal fadein 3.0



"翌日の午後、数学の授業で記号論理学のプリントを２問目まで進めたところで、畳んだ紙切れが俺の頭に当たる。犯人が誰かは分かりきっているけど、念のために急いで教室をぐるりと見回す。"


show shizu invis at left
with None

show bg school_scienceroom at left
show shizu behind_blank at center
with dissolvecharamove


"この教室には何も起きていないふりをするのが下手なやつしかいない。紙切れを投げたのが誰か、みんな気づいている。しかも当の犯人が静音なのはバレバレだ。自分の行為を恥じる素振りすら見せていない。"


"田舎ってのはほんとに違うな。前の学校だったら、誰がやったのかなんて絶対にわからないだろう。"


"紙切れを開くと、こう書いてある。"

window hide


$ written_note("ミーシャが休みなの！　放課後手伝って！")

window show


hi "なんでわざわざメモ帳使うのかわかんねえよ。どうして手話で言わないんだ？"



"俺が学んだ手話のほとんどは、ミーシャがしゃべりながら手話も同時にするというスタイルをまねることで身につけていた。おかげで今の言葉も手話と同時に、うっかり口に出してしまう。"
"小さな笑い声が教室に広がる。かっこ悪すぎる。"



his "あまり仕事が多くないなら手伝うよ"

show shizu basic_angry
with charachange


ssh "バカ言ってないで。ミーシャがいないんだから、あなたは二人分手伝わなきゃいけないの。当たり前でしょ"


"今のにどれほどの意味があるのかわからない。大体、昨日ミーシャは静音が手伝わせてくれないと愚痴っていたし。それじゃ俺だって大してできることもないだろう。"


"少し考えるふりをしてから、手伝うことにするとメモを書いて返す。実際、手伝いを頼まれたことは嬉しい。かなり前から静音と話をしたいと思ってたし。"


"これはいい機会だけど、表向きだけでも、多少は反抗の気持ちがあるように見せておかないといけない気がする。"

hide shizu
with charaexit



"俺はプリントに戻って、すぐに３問目でつまずく。どうにかしようとしたあと、何気なく静音にメモを投げてよこす。"


window hide


$ written_note("どうしてミーシャは休んでるんだ？　あと３問目の答えは？")

show shizu behind_blank at center
with charaenter

window show



ssh "気分が悪くておなかが痛いって言ってた。ミーシャはよく腹痛を起こすんだけど、今日休むのは勘弁してほしかったわ"




show shizu basic_normal2
with charachange


ssh "手話使いなさい"


"腹痛なのは、昨日自分の頭よりも大きなパフェを一気に平らげたからだと思うけどな。"


"でもそんなにしょっちゅう腹をこわしているなら、ただの偶然か、それとも苦しくなるほどたくさん食べ過ぎるのが習慣になっているか、どちらかだろう。"



"先生が険しい目で俺たちをにらんでいるのに気づく。ごもっともだ。俺たちは授業中に手話で『おしゃべり』しているわけで、やたら目立つ上に授業の邪魔になっている。"
"会話を終わらせたくて咳払いをするけど、静音にはヒントが通じない。"



"そりゃそうだよな。今度は手を使って意志を伝えようとするけど、静音は気づいていて、単に気にしていないだけだというのがわかる。"

show shizu adjust_smug
with charachange


ssh "３問目の答え、まだ知りたい？　教えてあげてもいいけど、かわりに２５問目の答えを教えて"



his "おい、こっちは手話を知らない先生が、下手したら俺たちが手話ができるのを悪用してカンニングしてると疑うかもしれないって考えてたんだぞ。お前がほんとに実行するなんて信じられないぜ！"
his "あと、俺はまだ２５問目まで行ってない"


show shizu behind_frown
with charachange


ssh "３問目の答えが知りたかったのはそっちでしょ。あなたが先に聞いたのよ。この偽善者"


his "お前は生徒会長だろ、そういうずるはしちゃだめなんだよ"




"こんなことをしている暇はないし、先生の忍耐力の限界を試している気がする。目の前の数学の問題を解きながら静音に手当たり次第に議論を仕掛けてやりたいけど、それには少なくとも腕がもう二本は必要だ。"



show shizu basic_normal
with charachange


"静音はちょっと工夫をきかせて、片言に近い単純な言葉をたくさんつなげることで、この状況を切り抜ける。俺は長ったらしい数式にめまいを覚えながら、合間に頭の中で何度かメモを取る。"




show shizu adjust_smug
with charachange

play sound sfx_impact2
with vpunch



"チャイムが鳴る直前、静音はペンにキャップをかぶせると勝ち誇るように机に叩きつける。大きすぎる音に教室中がびっくりするけど、みんな音の出所よりも昼ご飯のほうが気になっていたので、すぐに忘れ去られる。"


stop music fadeout 6.0

show shizu basic_normal_close at twoleft
with characlose


"何度か軽く伸びをした後、静音は立ち上がって俺の左肩あたりでうろうろする。"

show shizu behind_frown_close
with charachange


ssh "まだ終わってないの？　こっちが立ってる間に、ついでにあなたのも提出してあげようかって言うつもりだったのに"


his "誰かさんに邪魔されたからな。先生に頭下げて、今から問題が解けるまで９分時間くれって頼むはめになったんだ。言っとくけどな、人と話をしながら片手でこの問題解くのは大変なんだぞ"





"先生も俺と同じくらい早く出て行きたかったので、俺の頼みにいい顔はしていなかった。"


"あと１問でおしまいというところだったので、静音はあまり信じていないようだ。プリントを提出した瞬間、俺は静音に生徒会室まで引きずられている。"

scene bg school_council
with locationskip

play music music_happiness fadein 2.0


"不気味なほど、そして腹立たしいまでにきれいになっている。昨日まで作業していたものがどこにあるのか見つけられない。"


his "何もかもどこにあるんだよ？"

show shizu behind_blank at center
with charaenter


ssh "ちょっと片づけをしたの"


his "それじゃ何の説明にもなってないだろ。自分がしまったものがどこにあるのか忘れるようなもんだぞ。まあいいか、見つからないんだったら俺は帰るかな"

show shizu basic_normal2
with charachange


ssh "そこの引き出しにあるわ"






"俺は作業していたポスターを取り出して少しシャッフルする。静音は元々色別に重ねていたので、それを見て不機嫌になる。"
"別に静音をからかっているわけじゃない。俺には俺のやり方があるってだけだ。静音に言っても信じるとは思えないけど。"






his "俺は少し散らかってる方がいいんだよ。そのほうが自然だろ。それに時間も節約できる。前に置いておいた場所が一番いいんだ。昨日まで作業してたものを探すのにいちいち棚の中を探さなくてもいいしさ"

show shizu adjust_frown
with charachange


ssh "怠け者"


his "そうじゃない。俺は怠けてないよ、お前がいつもみたいにやりすぎてるだけだろ"



"ちらりと静音の机を見る。"
"角にはメモ帳がきちんと置かれていて、その後ろには小さなデスクカレンダー。一つ一つの日付には、丁寧だけど豆粒のように小さな字でメモが書き込まれている。右には青、黒、赤と３つのペンの箱がある。"



his "見てみろよ。毎日仕事が終わるとペンまでいちいち同じ色の元の箱に戻してるじゃないか。こんなの整理マニアどころじゃすまないぜ"



show shizu behind_frown
with charachange


ssh "あなたはどうしてるの。机の上のマグカップに投げ込んでるの？"


his "なんだよ、十分整理してると思うけどな"

show shizu basic_frown
with charachange


ssh "ほんとに整理整頓ができてないのね。自分の髪の毛だってきちんと整えられてないじゃない"


his "それは傷つくぞ……"


"やってないわけじゃない。ただ平らにならないってだけだ。俺はペンの箱を開いて、静音が中のペンを全部同じ向きに入れているんじゃないかと確かめる。俺の意図に気づいたみたいで、静音は不機嫌な顔をする。"

play sound sfx_dropstuff


"箱の底がきちんと閉まっていなかったようで、俺が持ち上げた瞬間にペンが滝のように流れ落ちる。"


his "悪い。大丈夫、ちゃんと拾うから"

stop music fadeout 4.0
play sound sfx_impact

show shizu adjust_blush_close
with vpunch



"俺はペンを拾うためにかがむけど、静音がペンの方に注意を向けていれば、俺の手話に気づくはずもないということを忘れていた。"
"静音の頭が俺の胸にぶつかる。それほど強くではないけど、俺はバランスを失って転んでしまう。"


show shizu adjust_blush
with charadistant


"俺は笑って流す。静音もそうするだろうと思う。でも静音が体をこわばらせて身を引くのを見て、不安が全身に這い上がってくる。"



"今のは妙な反応だ。なぜそんな反応をしたのかと考える。そりゃそうだ。心臓が悪い人に向かってヘッドバットをかましたんだから。"






label jp_S26a:



"静音は俺の心臓のことを知っているだろう。ドレッサーの端にずらりと並ぶ薬を見たのだから。少なくとも、見ただけではわからないけど、あれだけの薬が必要なくらい深刻な病気だというのはわかったはずだ。"




label jp_S26b:


"静音は俺の心臓のことを知っているだろう。生徒会の仕事をしていれば、そういう情報も目にしているかもしれない。少なくとも、経過観察が必要なくらい深刻な病状だってことはわかっているはずだ。"


label jp_S26c:


"で、俺がガラスでできているような扱いをするわけだ。静音にとっては自然な反応だ。転校初日に笑美が俺を突き倒したとき、静音がパニックを起こしたことを忘れてはいない。さっきのだってそれと同じってことだ。"

show shizu basic_normal
with charachange


"今、静音はあのときのことを思い出しているに違いない。自分自身に怒っているように見える。"


"静音が俺の薬を目にしたときのことを説明する、いい機会だ。話を蒸し返すのはいやだけど、悪いことじゃない。これで雰囲気を変えられるだろう。"




"それでも俺は怖くて、何も言うことができない。"
"床に向いている静音の関心をこっちに向けさせて、自分がどういう障害者であるかということをひとつひとつ手話で説明することを想像しているうちにどんどん気が滅入ってしまったということもある。"






hide shizu
with charaexit



"いすに座り、俺は気を紛らわせるためにこのポスターを完成させることにする。作った覚えのないポスターがいくつかある。紙面を埋め尽くす文章と、ものすごくきれいな手書き文字からして、静音が作ったに違いない。"




"つまり、残りはミーシャが作ったってことだ。そっちはずっと視覚に訴える作りで、俺たちのかわいらしいイラストが小さく描かれている。"
"自分がマスコットとして使われるのは何とも言えない感じがするけど、あまり面白いとは思えない。"


scene bg school_council_ss
with shorttimeskip

play music music_tranquil fadein 3.0



"少し時間がたつ。日が暮れ始めるには十分長い時間だ。静音がペンを置いて、一本ずつ丁寧に指を鳴らす音が聞こえる。その音は静かな部屋に大きく響き、静音が俺の注意を引こうとしているのかと思って頭を上げる。"


show shizu behind_blank_ss
with charaenter


"そういう意図はなかったものの、俺が頭を上げるのに気づいて、静音は間髪入れずに手話を始める。"

show shizu basic_normal_ss
with charachange


ssh "休憩しましょう"


his "お前がそう言うってのは驚くな"

show shizu adjust_happy_ss
with charachange


ssh "いいの。私はもうすぐ終わるし。それにおなか減っちゃった。あなたは減ってないの？"


his "ちょっとな"

show shizu basic_normal2_ss
with charachange


ssh "私はすごく減ってる"


his "なんか注文するか"

show shizu behind_smile_ss
with charachange


ssh "あなたのことを気にしてたのよ。私はもう食べ物があるから"


his "どこに？"

show shizu adjust_smug_ss
with charachange


"静音は机の下からシナモンパンを取り出すと、頭の高さまでゆっくりと持ち上げる。石を上昇させる魔法使いのようだ。"

show shizu behind_smile_ss
with charachange


ssh "ただし！"

show shizu basic_sparkle_ss
with charachange


ssh "ひとつしかないの。二人分には足りないわ"



"ああ、なんてドラマチックな。その意味が理解できる。一瞬、既視感が脳裏をよぎる。"




his "半分こすればいいだろ"

show shizu adjust_frown_ss
with charachange


ssh "そんなの。おもしろく。ない。つまらなすぎ。将棋で勝負しましょう"


"もう将棋盤を用意している。あの机には何でも入っているに違いない。"


his "チェスじゃないのか？"

show shizu behind_smile_ss
with charachange


ssh "チェスの成りはつまらないんだもの。こっちのほうがいいわ"


his "それはよくわからないけどな。まあ、俺はけっこう将棋は得意だから、これでもいいぜ"

show shizu basic_happy_ss
with charachange


ssh "そうなの？　いいわ、じゃあもう少し面白くしましょうか。３０秒以内に手を指すこと。そっちもルールを足していいわよ"


his "やめとくよ。どんなルールを追加したって、俺には有利よりも不利の方が大きくなるから。３０秒制限だって俺にはきつすぎるよ"



his "お前のおかげで、少しくらい自慢しても大丈夫だと思ったのを後悔してるよ"



scene bg school_council_ss
show shizu basic_normal_close_ss at center
with shorttimeskip


"コイントスで静音が先攻をとると、すぐに全ての駒を最速で成らせるように手を指し始める。とても基本的な指し方のようだ。何かの罠じゃないかという気がしてならない。"



"でもそうではなかった。この進め方のポイントは、自分の駒を成らせて俺の駒を取るというところにあるようだった。"
"静音はとてもうまく進めるけど、その分だけ指し方がわかりやすくなる。俺は思っていたよりも少しだけうまくやることができた。"



"それでも３０秒制限はとてもきつい。勝負は引き分けに終わる。再試合をするか、駒を数えて勝負をつけるか、どちらかにすべきところだろう。"


"静音は時間がないので再試合はしたくないけど、判定勝ちは明らかに不満のようだ。"

show shizu adjust_frown_close_ss
with charachange

stop music fadeout 4.0


"静音は座ったまま、銀を端から端へと動かし、二つの選択肢のどちらを取るべきか考えている。あまりに長いので、賭けのことを忘れたんじゃないかと思ってしまう。"


"やがて、静音は駒をもてあそぶのをやめ、下に置く。"

show shizu behind_blank_close_ss
with charachange


ssh "ミーシャは私のことを怒ってるの？"


"ずいぶんいきなりだな。"

play music music_pearly fadein 5.0



"静音の率直さに俺は戸惑う。静音が単刀直入な話をするのは、それがきわめて真剣であることの現れだ。戯れのような笑みはその顔には浮かんでいない。"
"かわりに、いつもの沈着冷静な表情で、俺が真実を話そうとしているのかどうか見極めようとしている。俺が真実以外の何かを話すかもしれないと静音が考えていることが腹立たしい。"


"でもたぶん、静音とミーシャは俺の知らないところでけんかをしている。二人がお互いのことをこんなに気にかけていることを知って、心が暖かくなる。"



his "いや。それはないと思う"


his "ミーシャはお前が怒ってると思ってるって、知ってたか？"

show shizu behind_sad_close_ss
with charachange


"静音はゆっくりと、居心地悪そうにうなずく。"

show shizu basic_normal2_close_ss
with charachange


ssh "ええ"


his "ミーシャはお前よりももっと回りくどい聞き方をしてた。ちょっと驚いたよ。お前の方がそういう駆け引きが好きだと思ってたから"

show shizu behind_blank_close_ss
with charachange


ssh "いつもってわけじゃない"


"……"


his "二人でけんかでもしてるのか？"

show shizu adjust_frown_close_ss
with charachange


ssh "違うわ"


"すぐさま否定する。しかもそのことを快く思ってはいない。地雷を踏んだ気分だ。"

show shizu behind_sad_close_ss
with charachange


ssh "ごめん。本当はけんかしてる。ほんのささいなことよ"

show shizu behind_blank_close_ss
with charachange



ssh "ミーシャが生徒会に何の関心もないのはわかってる。私がいるから入っただけだって。でも私は感謝してる。ミーシャが私の友達でいてくれて、本当に嬉しい。でも今は、ミーシャが何に怒ってるのかわからない"



his "聞けばいいだろ？"

show shizu basic_normal2_close_ss
with charachange


ssh "教えてくれないの。だから答えは自分で見つける。耳が聞こえなくたって、私はとても察しがいいと思ってた。バカみたいよね。今ごろ気づいたわ"

show shizu behind_sad_close_ss
with charachange


ssh "たぶん、私がしたことが悪かったんだと思う"

stop music fadeout 8.0


"それが何なのかについて、静音はそれ以上説明しない。静音自身も状況を完全には理解していないからだろう。"


"いつもあらゆることに自信満々な静音が、友達とのささいな言い争いで怖じ気づくというのは妙な感じだ。でもよく考えると、それも筋が通っている。"



"二人は普通の友人関係よりもずっと近い距離にいる。そして静音はある意味、他の人からはとても浮いている。耳が聞こえないこともそれに大きく関わっている。"



"でも俺には、静音が仕方なくというより自分の意志で、ミーシャを周りの人との緩衝帯として使っているように思える。静音は例のメモ帳で問題なく意志疎通ができる。ただそれが大嫌いなだけだ。"


"別の人を通じて話をするのをあんまり長い間続けていると、だんだん話し方を忘れてしまうんだろう。それは避けがたいことのように見える。自分が人付き合いが下手だと感じるのも、それほど見当違いとは言えない。"

hide shizu
with charaexit


"時間が経つほどにあのシナモンパンが食べたくなってきて、俺は作業に戻る。でも静音の机に転がったままの駒の数を数えると、静音の勝ちは明らかだ。"


"それにもし再戦となると、腹が減りすぎていて集中できそうにない。とっとと終わらせて何か食べたいという気持ちに動かされて、俺は最後のポスターを仕上げにかかる。"


his "終わった。これだけあれば十分だろう。あまり多くてもまずいかもしれないしな"

play music music_shizune fadein 3.0

show shizu behind_blank_ss at center
with charaenter


ssh "オーケー"


his "それだけかよ？　『オーケー』だけか？"

show shizu adjust_frown_ss
with charachange


shi "……？"

show shizu behind_blank_ss
with charachange


ssh "……私も自分で少し作るわ。投票用紙の書式を決めてから"


his "っだあああああ。ポスターは多すぎてもよくないんだよ。過飽和って聞いたことないのか？"



his "ほんと、お前はがんばりすぎてると思うぞ"

show shizu basic_normal_ss
with charachange


"指を重ね合わせる静音は、もう少しでそれを認めるかのように見える。"

show shizu behind_blank_ss
with charachange


ssh "そうかもね"


his "ミーシャだってそう思ってるんだぞ"

show shizu basic_normal2_ss
with charachange


"ミニチュアの綱引きのように、静音の指が落ち着かなげに互いに巻き付いたり、引っ張り合ったりするのを、俺は見守っている。"


his "俺はいいよ、でも今日いくつかクラスを回って聞いてみたけど、あまり関心は高くなかった。お前が言ったとおりだよ。だから……"

show shizu adjust_frown_ss
with charachange


ssh "だから間違ってるっていうの？"



his "そうじゃないよ。でも……なんか空回りしてると思う"




show shizu basic_angry_ss
with charachange



ssh "そんなことない"



"そうかよ、でも誰にとって？　静音だって本気でそう信じてるとは思えない。"

show shizu behind_frustrated_ss
with charachange


ssh "私のわがままだけでわざわざこんなことをしているわけじゃないのよ"


his "そういう意味で言ったんじゃないよ"


"久しぶりに二人きりになれるチャンスだったというのに、もう台無しになってしまった。でも静音は怒っているようには見えない。"


"むしろ、自分の思いをはっきりと伝えられないことにいらだっているように見える。でも静音は手話の達人なのだし、それが理由だとは思えない。"


"もし静音が話すことができたら、どれだけその恩恵を受けることができるだろう。静音はそんなことを考えたことがあるだろうか。"

show shizu basic_frown_ss
with charachange


ssh "私の仕事の一つってだけよ。学園祭と同じように。ちゃんとやってみせるわ、自分の仕事なんだから。ただ、生徒会選挙は学園祭ほど楽しくはないから、誰も気にしないってだけ"




"『でも、もしかしたら……』とでも言うかのように、静音は一瞬だけ指先を触れ合わせる。それは分からないでもない。でもそこまで軽薄な言葉でまとめられてしまうようなことを、静音は口にしようとしない。"




show shizu behind_frown_ss
with charachange


ssh "でも私は気にしてないわ。私はみんなを盛り上げていきたいけど、でもそれは私とは関係ない。私はいっさい関わりたくないの"


his "どういう意味だ？　だってお前、学園祭には毎回出てるじゃないか"

show shizu adjust_frown_ss
with charachange


"静音は怒ったふりをして手を振る。"

show shizu behind_blank_ss
with charachange


ssh "そうね……私自身も楽しまないといけないわ。でもね、それとこれとは別なの"


"静音の気分は多少良くなったみたいだ。冗談を飛ばせるくらいだから。"

show shizu basic_normal2_ss
with charachange


ssh "誰かがわざわざ私を関わらせる、なんていうのは嫌なの。そんなの面倒だし。私はそんな責任は負いたくない"

show shizu adjust_frown_ss
with charachange



ssh "今でだって、状況はややこしくなりすぎてるの。選挙の関心をもっとかき立てようとするほど、私がもっと関わらないといけなくなる"

ssh "誰もまだ自分から動こうと思ってない。私の仕事はもうとっくに終わってないといけないのに、まだ終わってる気がしないの"



show shizu behind_frustrated_ss
with charachange


"腕を組んで後ろにもたれると、静音はいらだちで歯ぎしりする。"

show shizu cross_angry_ss
with charachange




ssh "みんなほんとに怠け者なんだから。何かさせたくても、何も任せられやしない"

ssh "他の所ならどこでも、選挙は面白いイベントなのに。理屈に合わないわ。どうしてみんなこんなに違ってないといけないの？　あいつらを処罰できる手さえあれば……"



show shizu adjust_angry_ss
with charachange


ssh "……鎖で生徒を机に拘束するとか。投票は義務よ。投票しなければむち打ち刑"


"なんて恐ろしい。じゃあ俺が投票日にベッドにこもってたら、どれくらいの偽善になるんだろう。インフルエンザで。風邪で。のどの感染症で。それと足首の捻挫で。"


his "自分をこれに載せてみるといいんじゃないか"


his "罰としてじゃないぞ。勘違いするなよ"


"俺はミーシャのポスターを一枚掲げる。"


his "こんな風にさ。いいアイディアだろ。ミーシャは何かを思いついてたんだ。文字だけよりはずっとかわいらしいし。お前も気に入ると思う。かわいいマスコットがいれば、関心も盛り上がるだろ"

show shizu basic_normal_ss
with charachange


ssh "ミーシャだけならそうかもね"


his "何で俺はだめなんだよ？　誰かから、この学校は男子よりも女子の数が少し多いって聞いたぞ……その人口統計に対応する必要はあるだろ"

show shizu adjust_blush_ss
with charachange


"静音はくすくすと笑う。今度は俺にも聞こえるくらいに。驚いた。こっちを見る静音も驚いている。声が漏れたことを恥ずかしがって、その顔がさっとピンク色に染まる。控えめに言っても、この光景には混乱する。"



his "どうして自分のイラストを載せないんだ？"


"静音は手を振って、俺の質問をはねつける。"

show shizu basic_angry_ss
with charachange


ssh "面倒だから"


his "面倒って、どういうことだよ？　お前が生徒会にいるって、この学校の生徒なら誰でも知ってるぞ"


"俺の腹がぐるぐると鳴って、思っていたよりも腹が減っていたことに気づかされる。静音はそれを機に俺の質問を跳ね返して、話題を変える。"

show shizu behind_blank_ss
with charachange


ssh "どうかしたの？"


his "いや。俺の腹が鳴った"

show shizu basic_normal_ss
with charachange


ssh "そう"


"静音は机の上の忘れ去られたパンを見ると、二人分には足りないことに気づいて顔をしかめる。"

show shizu adjust_happy_ss
with charachange


ssh "そんなにおなかが空いているなら、上海に行きましょう。こんなに遅い時間だと混んでるかもしれないけど、今日は優子さんが働いているから。絶対席は取れるわ"


"その笑顔の裏にたくらみを感じ取って、俺は不安になる。"


his "やめとくよ。今週はもう二日連続であそこに行ってるし"


show shizu basic_frown_ss
with charachange


"静音は不機嫌そうな顔をすると、抗議するように机にもたれかかってうずくまる。"


his "なんだよ？"

show shizu adjust_frown_ss
with charachange


ssh "断られてがっかりしてるのよ"


his "そりゃあ、何もかも同意見ってわけにはいかないよ"

show shizu behind_frown_ss
with charachange



ssh "あなたはいつも自分の意見を言わなさすぎるのよ。私にとってはすごく楽だけど、でもあまり面白くない、そうでしょ？　だったら、時には久夫は私の決断に反対しないといけない。あなたにはその義務があるわ"



his "反対しなきゃいけない決断って、そんなのどうやってわかるんだよ"

show shizu basic_normal_ss
with charachange


ssh "簡単よ"


his "簡単なもんか。お前が本気か冗談で言っているのかだって、時には見分けるのが難しいんだ"

stop music fadeout 9.0


"それでも、静音は全てのコミュニケーションを手話で行うから、それは一目瞭然だろう。そのことが全てだとは言わないけど。"




"俺が心臓発作を起こしたときのことを思い出す。最初、岩魚子は話をするのをやめなかった。やがて、俺はいい加減黙ってくれないかと願い始めた。"
"さもなければ自分が黙った。もう誰が見舞いに来ても嬉しくなくなっていたから。俺はだんだん感謝の気持ちを持てなくなった。"







"二人で話していたとき、それは礼儀正しさをやりとりするための儀式でしかないと思った。岩魚子は自分の気持ちを表に出さないようにものすごく努力していた。俺はもうどうしようもない、という気持ちを。"
"やがて、岩魚子の表向きの態度は内側の感情と一致した。"




"そのせいで、岩魚子が見舞いにこなくなったことを受け入れることができた。それが起きた頃には、俺はもう驚かなかった。岩魚子は自分の気持ちを隠せる名人だと思っていたようだけど、それでも俺は驚かなかった。"



"将棋やチェスのようなゲームは、人のいろんな性質を教えてくれると聞いた。静音が俺とプレーしていてどんな性質を読みとったのか、知りたいもんだ。"



"撤退することでしか静音とつながることができないなら、俺は自分が望んでいたよりも、岩魚子に近いのかもしれない。俺は出前を取ろうと提案する。"




scene black
with dissolve




label jp_S27:

scene bg school_hallway2
with locationchange


"翌日の昼食時、いつもの自販機に立ち寄ったらお気に入りのドリンクが売り切れている。物置部屋と図書室に挟まれて、ほとんどの教室からは遠く離れているのに。こんな場所に自販機があるなんて誰も知らないはずだ。"



"これだけ図書室に近い自販機なら大繁盛していると思っていたけど、図書室だってたいてい人がいないし、図書室に用がある人はレポートの行数を稼ぐための資料を探している人だけだ。"





"必要以上に長居する人は一人もいない。この一ヶ月の間、俺にとっては好都合なことだった。ただ、この誰も存在を知らない自販機には、全然補充がされないという罠があったんだ。"



play sound sfx_can


"オレンジソーダの缶で妥協して、食堂に持って行くのではなく、この場で飲もうと思っていると、俺の隣で図書室のドアが開く。"

show yuuko worried_down at center
with charaenter


yu "あ……"

show yuuko worried_up
with charachange


yu "ずっと探してたのよ！"

play music music_happiness fadein 2.0


"今日の優子さんは普段よりもずいぶん自己主張がはっきりしている。でも勢いが足りなかったみたいで、すぐにむにゃむにゃとつぶやくだけになってしまう。"

show yuuko worried_down
with charachange


yu "お、お願いだから、本返してちょうだい。その……図書室の本ね。あなたが借りた本、ずっと前から延滞してるでしょう。貸し出し予約が入ってる本もあるし……"


hi "しまった。忘れてました。新しい本を借りてばっかりで、借りた本を返すのをいつも忘れちゃうんですよね"

show yuuko neurotic_up
with charachange


yu "私も大学の図書館でいつもそれやっちゃうんだ、すごく恥ずかしい"


hi "返却させるように人をよこしたりするんですか？"



show yuuko worried_up
with charachange


yu "ううん……大学の図書館はもっと大きいから、ちょっとくらい延滞しても気づかないし。おかげで助かるけどね、あまり長い間延滞すると罰則が……すごく厳しいから。ここよりも……"




"自分でたった今言った言葉に反して、優子さんが本を期限までに返さないことを気にしていないのがいいなと思う。俺よりよほど長く延滞しているのにあんなに勝ち誇っているのがちょっと偽善っぽく見える。"
"蛇の道は蛇ってことか。"








"俺と同じくらいのタイミングで自分が言ったことの意味に気づくと、優子さんは口をつぐんで怒ったように態度を豹変させる。"

show yuuko panic_up
with charachange


yu "……あの……ええと……それとこれとは……話が別なの！　全然違うんだから……"


"優子さんは自分の爪をじっと見つめる。ものすごく爪を噛みたいのに、人目が気になりすぎてできないかのようだ。"

show yuuko worried_down
with charachange




yu "たとえば、どれだけ前に……中井くん、何ヶ月も前から借りっぱなしの本だってあるのよ。ごめんね……ただ、他にもその本を読みたい人がいるってだけなの。もし読むのが遅いのなら、それはかまわないけど……"




hi "いや、俺が全面的に悪いです。正直言うと、まだ読んでない本だってあるし。読んでないのに新しく本を借り続けるのは良くないですよね"


yu "それは良くないわ……"


hi "ええ、ほんとに……"


"今度は俺が優子さんの語尾を濁す話し方をまねし始めている。優子さんのぎこちなさは、どういうわけかとても移りやすい。"


"でも、驚いた。今日の優子さんはまるで普通に見える。ただ時々、ウェイトレスをしているときのような神経質なくせが飛び出してくるけど。"



"考えてみれば、初めて会ったとき優子さんはこんな振る舞いはしなかった。おっちょこちょいで過敏ではあったけど、ここまでひどくはなかった。静音とミーシャと俺が上海に行ったときに、ばったり出会うまでは。"



"自分がウェイトレスの仕事をしているところを学校の生徒に見られることに、コンプレックスを持っているのかもな。"


"だとしたら、学校から一番近い喫茶店をバイト先に選ぶのはちょっと変な話だと思う。あんなに客の少ない店だったのは運が良かったとも言える。"


hi "まあ、わかりました。放課後になったらすぐに返します"

show yuuko smile_up
with charachange


yu "なるべく早く、お願いね"

show yuuko worried_up
with charachange


yu "あ……ちょっと待って、もう一つお願いしてもいい？"


hi "もちろんですよ、何ですか？"

show yuuko worried_down
with charachange



yu "わた……私、ちょっと出かけなきゃいけないの、でも図書室を空にするわけにはいかなくて……"
yu "悪いんだけど、かわりに番をしてくれない？　ほんの少しだけ、できるだけ早く帰ってくるから！　あなたも生徒会だし、代理をしてもきっと大丈夫だと思うの"



hi "わかりました、やりますよ。心配し――"

show yuuko closedhappy_up
with charachange


yu "ありがとう！"

show yuuko neurotic_up
with vpunch


"優子さんは前のめりになって、まるで感謝のあまり俺を抱きしめるかのように見えたけど、二センチ手前で踏みとどまる。おかげでものすごくまぎらわしいしぐさに見えてしまう。"


"ちょっとドジっぽい優子さんが、自分の動きをこれだけコントロールできることにも驚いた。"

hide yuuko
with charaexit

stop music fadeout 6.0


"俺が『どういたしまして』と言う間もなく、約束の時間に遅れているかのように、優子さんは走り去っている。"


"実際その可能性はあるけど、そう決めつけるのも早計だと思う。なにせ優子さんのことだし、あの人はどんなことにもそういう態度で臨むような人に見える。"

scene bg school_library
with locationchange




"で、図書室にいるわけだけど、なんだかバカみたいな気分になる。実際何をすればいいのかわからない。普段どおりに座って本でも読んでいればいいのか？"
"それでも多分問題なさそうだけど、優子さんの勤勉な仕事ぶりには釣り合わないだろう。"




"司書のデスクに座って、入ってくる人をいちいち厳しい視線で品定めしていればいいんだろうか。手始めに静音の目つきを真似して、ペンの表面を鏡代わりに何度か練習する。"


"けっこう良さそうだ。でもムカつくことに誰も入ってこないので、さっさとその線はあきらめて、代わりに華子を捜すことにする。"



"中は人っ子一人いない。誰かいるように見えるけど、瞬きをした瞬間にそいつはいなくなってしまう。デスクに戻って面白そうな本を開くと、見覚えのある人物が落ちてくる振り子のようにふらりと姿を見せる。"


show kenji invis:
    center
    xpos 0.4
with None

show kenji tsun at center
with dissolvecharamove

play music music_kenji fadein 0.5



ke "よう司書の人、あんたのこと１０分くらい探してたんだぜ。はあ！？　お前かよ？　ったく、どこにでも現れるやつだな。それとも生徒会にそうさせられてるのか。あのビッチどもめ！　なんてことをさせるんだ！"


show kenji rage
with charachange



ke "奴隷使いどもめ！"





"大げさに言っているんだろう。俺が図書室全体をゆっくり巡回するのに、３０秒もかからなかったし。その考えも、健二に会ったという驚きで上書きされてしまう。"


hi "どこから入ったんだよ？　ここで何してる？"

show kenji tsun
with charachange



ke "なんだよ、男子は図書室に入っちゃいけないってのか？　お前みたいな若造に尋問されないと図書室にも行っちゃいけないのか"
ke "その辺の女子がしょっちゅうここに来てるけど、そいつが何してるか聞かれたことなんて一度もないぞ"



ke "どうしてだよ、そいつは本を読むけど、俺は読まないからか？"



"華子のことを言っているに違いない。二人とも人を避けているんだろうけど、普通は図書室では読書をするものだと言ってやりたい。"
"じゃあ健二が本を読んでいないなら、何をしているにせよ、華子よりはよほど怪しそうに見えるはずだ。"



"でも結論を言えば、俺はこいつがどこからともなく現れたことに心底驚かされている。"


hi "その――それはお前がここで何をしてるかっていう質問の答えになってないぞ"

show kenji neutral
with charachange


ke "俺はお前がいるからここに来たんだ"


"その答えに俺は困惑する。もしかしたら俺は眠ってしまっていて、何もかもただの変な夢で、この健二は現実ではなくて俺の潜在意識なのかも。次は意味深だけどわかりにくい言葉でアドバイスをし始めるんだろうか？"


show kenji tsun
with charachange


ke "お前のおかげで、俺はフェミニストどもに寮から追い出されたんだ。それでこの図書室をさすらってるんだ。祖国を失った兵士か、幽霊のように。いろいろ台無しにしてくれたお前にとりついてやらなきゃな"


"残念。面白そうな夢になると思ったのに、どうやらこれは現実らしい。"



ke "そうだろ、お前が女と一緒に仕事し始めたおかげで、そいつらが俺の所に来たんだ。覚えてるか？　忘れたとは言わせないぞ、お前もいたんだからな。その日以来、俺は狙われてたに違いない"
ke "自分の勘を信じるべきだったぜ。でも俺は若くてバカだった"



hi "まだ一週間も経ってないじゃないか"


ke "そしたら、親父が電話してきて、俺の手紙が一通配達されてないって言うんだ。郵便局がなくすはずがないから、途中で盗まれたに違いない。情報戦争だ！"

show kenji neutral
with charachange



ke "それで自分の秘密の隠れ家がバレたと確信したんだ。今の俺は逃亡中だ、脱走者みたいに。非常警報発令だぜ"





hi "寮の部屋は秘密でも何でもないだろ。廊下に堂々と名前と番号の入った表札を出してるじゃないか"

show kenji rage
with charachange



ke "わかってる、それは見た。極悪非道だぜ。あんなものを出すんだったら、西部劇みたいな指名手配ポスターでも貼っときゃいいんだ！　『お尋ね者：生死問わず』ってな！"
ke "生きてる方がいいだろうな、それで俺のクローンを作るか、バッタに変身させるんだろ"


show kenji tsun at Position(ypos=1.15)
with Dissolvemove(0.5)



"断りもせずに俺の向かいにある椅子におさまると、健二はタバコを一本取り出して指の間でくるくる回し始める。こいつがタバコを吸うのは見たことがないから、ただのかっこつけだろう。"




ke "俺はもう自分の住みたい場所に住むこともできないんだ。ここが全ての始まりなんだ"


ke "目を見張る戦術だ……というか、あいつらに一歩家に立ち入られたら、もうおしまいなんだぜ。シロアリみたいに。フェミニストの侵略計画が家{b}から{/b}始まるんだったら、俺たちはいったいどこに行きゃいいんだよ？"


show kenji happy
with charachange



ke "唯一の疑問は、女は生まれつき木に近寄れないのに、どうやってシロアリ計画の本を参考にしたかだな"





hi "『二度と家には戻れない』って書いてあるのか？"


show kenji neutral
with charachange



ke "いや、二度とってのはよくわからないけど。俺はそこにいただけだから。他にどこでシャワー浴びたり、着替えを出したりすればいいかなんてわからないし"
ke "それに食事も、トイレも。テレビも。ニュースだって見てなきゃいけないんだよ。情報収集のために"





"寮の部屋を追放されて逃亡中の身にしては、一日に何度も部屋に戻って長い間過ごすのは全く平気らしい。"


"でも今の健二はゆっくりと向こうを向いて、回転する殺人ミステリー本のラックに話しかけている。わざわざ邪魔することもないだろう。"

play sound sfx_can_clatter


"俺はソーダを飲み終え、空き缶をドアのそばにあるゴミ箱に投げ込む。缶は縁に当たるけど、無事中に入る。俺は無言でガッツポーズを取る。"

show kenji neutral at center
with dissolvecharamove


"健二はそそくさと立ち上がり、ドアに向かって歩き出す。よく注意していなかった。今のガッツポーズはタイミングがまずかったかな。"


hi "どこ行くんだ？"

show kenji tsun
with charachange


ke "お前ずっとそのジュースぐびぐび飲んでただろ"


hi "それがどうした？　大体ジュースじゃなくてソーダだよ。それにもう空だし。あと『ぐびぐび』って何だよ？　二口飲んだだけだぞ"


ke "あーはいはい。５００万口くらい飲んでるんだろ"


hi "不可能だろそんなの"

show kenji neutral
with charachange


ke "お前には無理かもな。でも俺は常に不可能を超越するんだ。ああ、まあいい、俺ものど乾いてきた。ジュース買ってくる。すぐ戻るからな"

show kenji invis at Position(xpos=0.4)
with dissolvecharamove

with Pause(0.5)

show kenji neutral at center
with dissolvecharamove


"本当にすぐに戻ってきた。あまりに早かったので、俺の秘密の自販機を知っているんじゃないかと疑う。"


ke "お前にも買ってきたぞ。グレープジュースでよければいいけど。これでピザの借りは返したぜ"


hi "ありがとよ"

show kenji neutral at Position(ypos=1.15)
with charamove



"俺が貸した金はグレープジュース一缶分の十倍はあると言ってやりたい。でもそんなことを言ったらけちと思われるかもしれない。"
"反論されなかったので、健二は腰を下ろすとブドウに恨みでもあるかのようにすごい勢いでジュースを飲み始める。"


show kenji happy
with charachange


ke "なあ、ここでお前にばったり会えて、俺は運がよかったぜ。ちょっと頼みたいことがあるんだ"



"皮肉なことだけど、こいつはその頼みごとをするために俺にジュースを買ってきてくれたのかと考える。"
"だとしたら実にわかりやすいし、間が悪い。健二がそこまで深く物事を考えるとも思えないけど。率直に言ってくる方がよほど健二らしい。"



ke "俺に本を紹介してほしいんだ"


hi "でもお前、本は読まないんじゃなかったのか"

show kenji neutral
with charachange


ke "どうして知ってるんだ？"


hi "お前が言ったんだろ。自分が本を読まないから、そのせいで人に差別されてると思ってるって言ったじゃないか"

show kenji happy
with charachange


ke "まあ、その通りだ。それに本だって読むぞ。オーディオブックを読むんだ。それが未来のあり方だからな"



show kenji neutral
with charachange


ke "でも文学の授業で、月に一冊は本を読まないといけないんだ。それでこの学校じゃ、『上級暗号理論』みたいな古典は認められないんだと。山ほど本を読まないと、俺は落第しちまう"

show kenji tsun
with charachange



ke "文学は落とせないんだよ……そしたら俺は文盲ってことになっちまう。俺の母ちゃんは正しかったってことになる。母ちゃんが正しいなんてあるわけがない。俺はとにかく、文学を勉強しまくらなきゃいけないんだ"



hi "何か別の課題で単位を稼ぐってのは？"




ke "そりゃ勘弁。こんなバカみたいなものを持ち運ばなきゃいけないだけでも最悪なのに"


"健二は辞書を手に取り、ぱらぱらとめくって、後ろにある殺人ミステリーのラックに置く。"



ke "俺たちの祖先が、ポルノを見るのにこんな媒体を使ってたなんて信じられないぜ"





"俺は手元の本の上に飲んでいたジュースを吹き出してしまい、本は修復のしようもないくらいに台無しになる。あわてて裏表紙を確かめると、定価７９００円と書いてある。心臓発作を起こしそうだ。"




show kenji happy
with charachange



ke "うわ、ぐちゃぐちゃだ。でも今のはまずかったな。設備とか壊したらめちゃくちゃ厳しいからな、この学校。むち打ち刑だぜ"






"健二は嬉しそうに笑うと、缶ジュースを長々と音を立ててすする。"


hi "壊したんじゃない。わざとじゃないぞ。お前のせいだぞ、お前が変なこと言うから"


hi "それにむち打ちってどういう意味だよ？　むち打ちなんてやだよ"

show kenji neutral
with charachange


ke "まあ、落ち着けよ。本当にむちで打たれるって意味で言ったんじゃない。ただ弁償させられるってだけだ。それにむっちゃくちゃ怒鳴られる。ケツを食いちぎられるかと思ったぜ。でも大したことないけどな"


hi "もののたとえかどうかなんて知らねえよ。むち打ちも嫌だし、ケツを食いちぎられるのも嫌だし、とにかく罰なんて受けたくないんだよ、この……この大バカ野郎"


hi "どうすりゃいいんだよ？　ここには俺しかいない。優子さんが知ってる人は、ってことだけど。ゴミ箱に捨てるわけにも行かないし。どうせ見つけられる。そしたら優子さんにもバレる"

show kenji tsun
with charachange


ke "なんだよ、お前、ちょっとおかしいぞ"


hi "罰金取られたくないって思うのはおかしいのか？"


ke "ったく、興奮するなっての"


hi "興奮なんてしてない、金を減らしたくないんだよ"


ke "せこいやつだな"

show kenji invis at center
with Dissolvemove(0.5)

hide kenji
with None

stop music fadeout 1.0


"健二の首を絞めようと思ったそのとき、ミーシャの『わはは』声が廊下から聞こえてくる。健二にも聞こえたんだろう、そのタイミングで素早く自伝の棚のあたりに姿を消す。風のように。"

show mishashort hips_grin at center
with charaenter

play music music_comedy fadein 0.5


mi "こんちは、ひっちゃん～！"

show bg school_library at bgleft
show mishashort hips_grin at twoleft
with charamove

show yuuko neurotic_down at tworight
with charaenter


"ミーシャは生き生きと叫ぶ。後ろには決まりの悪そうな優子さんを引っ張っている。"

show mishashort sign_confused
with charachange


mi "ひっちゃん～！　ひとりごと言ってたの？"


"そうだと言ったら俺は頭がおかしいと思われそうだ。でも健二の居場所をばらしたら、健二のタガが外れて、俺も一緒に頭がおかしいと思われるかもしれない。"


hi "そうだよ"

show mishashort cross_grin
with charachange



mi "あはは～！　大丈夫だよ～！　恥ずかしがらないの、ひっちゃん。わたしもときどきやるから、一人きりのときにね！　ら～ら～ら～"


show yuuko worried_up
with charachange


yu "あの……私がいない間、何も起きなかった？"


hi "まったく何も"

show yuuko worried_down
with charachange


yu "何だか……ブドウの匂いがするわ"


hi "俺、ブドウのオーデコロンをつけてるんです"



"露骨かつ厚かましい嘘をつく。優子さんの反応からすると、嘘だとバレているか、オーデコロンのセンスが破滅的にひどいと思われたか、どちらかだと思うことにする。"


"俺が飲んでいたグレープジュースの缶はすぐそこにあるので、たぶん前者だろう。幸い、優子さんはそれ以上質問をしてこない。"


hi "二人一緒で何してるんですか？"

show mishashort sign_smile
with charachange


mi "一緒にランチ食べてたんだよ～！　まじめな話なんだよ、ビジネスランチだよ～！"


"スーツを着込んだミーシャが、誰かとビジネスランチをしている様子を想像してみる。どういうわけか、まるで頭に浮かんでこない。"


hi "どういう仕事？"

show yuuko panic_up
with charachange


yu "知らないの？"

show mishashort hips_grin
with charachange


mi "あはは～！　大丈夫～、大丈夫だよ～。生徒会のメンバーが他のメンバーの仕事を知らないのは普通だから～！"


hi "おい、そういうことを『大丈夫、大丈夫』でスルーするなよ。全然普通じゃないだろ。というかまずいだろ。俺たち三人しかいないんだぞ"

show yuuko neurotic_up
with charachange


"優子さんが不安そうに笑う。きっと震え上がっているに違いない。"

show yuuko worried_down
with charachange




yu "ミーシャちゃんが、あなたが図書室にポスターを貼りたいと言ってるって聞いたの……選挙のために"
yu "その……まだかなり先の話ではあるけど、たぶん大丈夫よ。私が自分でそういうことを決めたりできるとは思わなかったから……"



show mishashort cross_laugh
with charachange


mi "できるよ～！　すごいよね～？　あはは～！　ハッピーでしょ？　やった～やった～！"

show yuuko panic_up
with vpunch


"ミーシャは優子さんの両手をつかむと、無理矢理嬉しそうな風にその両手を叩かせる。自分がこれまで思っていたよりも多くの責任と権限を持っていると知って、優子さんはあまりいい気分ではなさそうだ。"

show mishashort sign_smile
with charachange


mi "ひっちゃん～！　せっかくここにいるから、ポスターを張り出すのを手伝ってよ！"


"かばんから巨大なポスターの束を取り出すと、ミーシャはトランプのカードのようにそれを半分に切り、少しつぶれた方を俺に渡す。"

show mishashort hips_smile
with charachange



mi "しっちゃんがすごくいいアイディアを思いついたんだよ～！　本の中にもチラシを挟むの～！　そしたら、みんながわたしたちを無視したくてもできないんだよ！　バネ仕掛けで飛び出すようにもできるよ！"




"ミーシャはがんばって静音が話したときの口調を伝えようとする。その調子は本人にかなり似ていて、そして少し危うさを感じる。"



hi "たぶん冗談で言ってたんだと思うぞ"

show mishashort perky_confused
with charachange



mi "わたしはいいアイディアだと思ったよ～"


show yuuko cry_up
with charachange


yu "だ、だめ……お願い……それはだめ……"

show mishashort cross_smile
with charachange


mi "スーパーウルトラアグレッシブな電撃マーケティングだよ～！　しかも全部の部屋も訪問するよ～！"


hi "それはひどいアイディアだな"

show mishashort cross_frown
with charachange


"ミーシャがふくれっ面を見せる。今までで一番静音に似ている感じだ。不愉快そうに指先を高速で突き合わせている。"


mi "ひっちゃん～！　どんなアイディアでも全部だめ出ししてるじゃない……"


hi "ああ、でもそのアイディアはひどすぎる。ひどすぎてスルーできない。それは飲めないよ"

show mishashort hips_smile
with charachange



mi "わはは～！　ひっちゃん、それって挑戦されてるみたいだね。反乱～、反乱だ～！"


show yuuko cry_down
with charachange


yu "は、反乱はだめよ……けんかはしないで"

show mishashort hips_grin
with charachange


mi "わはは～！　ただの冗談だよ～！"

show yuuko worried_down
with charachange


yu "そうなんだ……"

show yuuko worried_up
with charachange


yu "けんかはだめ"

show mishashort cross_laugh
with charachange


mi "あは～は～は～"


"有無を言わせない調子の優子さんの話し方は、保育園の先生をほうふつとさせる。優子さん独自のやりかただけど、すごく説得力を感じさせるな。"

hide mishashort
hide yuuko
with charaexit

stop music fadeout 5.0



"ポスターの掲示は驚くほど大変だ。理由は単純で、図書室の中はすでに掲示板や張り紙が数メートルごとに張り巡らされているからだ。ものによっては思いもよらないところにあって、今まで一度も気づかなかった。"


play sound sfx_warningbell


"単純な作業なのに、どれをはがして俺たちのポスターを張り出すかを決めるところで大いに時間をとられる。昼休みの終わりを告げるベルが鳴るころ、ミーシャと俺はまだかなりの数のポスターを残していた。"


"図書室を出るとき、ドアのそばに一」枚張り出していくことにする。それはミーシャが作ったものに違いない。下の方に静音の小さなイラストがある。"

scene black
with dissolve


label jp_S28:

scene bg school_scienceroom
with locationchange


"数日後、静音は一人で昼御飯を食べに行って戻ってこない。生徒会の仕事で本当にいっぱいいっぱいなんだろう。でも仕事の大半は自分が考えついたことだろうけど。"

scene bg school_hallway3
with shorttimeskip


"生徒会室に行ってみると、ドアの鍵がかかっていない。ドアを開ける前に一呼吸おいて、ミーシャの笑い声が聞こえてこないか確かめる。何も聞こえない。"


"中に誰もいないと思いそうになるけど、それなら静音が鍵をかけ忘れるはずがない。"

play sound sfx_dooropen

scene bg school_council
with locationchange



"静音はまだデスクにいる。胸の前で腕を組んで、椅子に座って眠っている。"
"なんて堅苦しい姿勢だろう。目が閉じているからわかるけど、さもなければ寝ているかどうかなんて見分けがつかない。実際、本当に寝ているかどうかだって確信が持てない。"





"普通なら机を軽く叩いて相手を起こすところだけど、静音が相手ではうまくいかない。寝ているならどんないたずらを仕掛けようかと、すぐに考えを巡らせる。自分の考えがそういう方向に向かってしまうのが残念だ。"



show shizu basic_normal at center
with charaenter


ssh "はーい。こんにちは"



play music music_shizune fadein 3.0


"静音は両手で別々に挨拶の手話をする。とてもまぎらわしい。"


his "おい、何してたんだよ？　こっそりサボってたのか？"

show shizu behind_smile
with charachange



"静音は笑うけど、頭を下げて隠そうとして、ついでにどうにか機嫌を損ねたような表情を作る。"




show shizu adjust_frown
with charachange


ssh "そんなところに突っ立ってないで。こっちが座っててあなたが立ったままだと落ち着かないでしょ"



"近くのいすに腰を下ろすと、静音は動きを止めて眼鏡を鼻の上で調整する。ちょうど楽器を調律するような感じだ。"



show shizu adjust_angry
with charachange


ssh "どうしてそんな遠くに座ってるの？"


his "それも落ち着かないのか？"


"静音は唇をきっと閉じる。からかわれるのは面白くないようだ。"


his "ちょっと暇ができたから、顔を出してまだ忙しいのかどうか見ていこうと思ってさ"

show shizu behind_blank
with charachange


ssh "手伝いたいの？"


his "ああ"

show shizu adjust_smug
with charachange


ssh "残念ね"

show shizu behind_smile
with charachange


ssh "ありがたいけど、もう必要ないの。最後の仕事も終わらせたから、もうやるべきことは全部終わっちゃった"


his "なんだよ、水くさいな。ミーシャも昨日は同じくらいビジネスライクだったぞ。二人とも生徒会の仕事に真剣になってるのか？"



show shizu basic_normal2
with charachange


ssh "私はいつだって真剣よ。生徒会役員の立候補者が誰だって真剣であるべきようにね"




"即答だな。こっちは足を休める間もないのに、生徒会にも入ってない未来の同僚をいきなり批判し始めるんだから。"



show shizu behind_frown
with charachange


ssh "少なくとも生徒会長はそうよ。生徒会長には指導力がないと。それなら他のみんなを動かせるか、少なくとも力づくで引っ張れるかもしれない。でもあんなに人数がいるのに、みんな気迫が足りないんだもの"

show shizu basic_angry
with charachange



ssh "副会長の立候補が一人もいないの。みんな大きな獲物が欲しいけど、ちゃんとした意欲を持ってる人は一人もいないってこと。それに会計も全然当てにならないし。だから私の権限で会計職を廃止することにしたわ"



his "おい、ちょっと待ってくれよ。そんなこと、できるのか？　物事はそういう風には進まないんじゃないか？"

show shizu adjust_frown
with charachange


ssh "そうなっているのよ"


"と言うと、静音は険しい顔で遠くを見つめて、眼鏡の縁をこする。答えになってないだろ、未来の独裁者め。"

show shizu behind_frown
with charachange


ssh "がっかりした。自分がその仕事をやりたいか、少なくとも私が生徒会長なのが気に入らないなら、みんなさっさと私を追い出したいって思わなきゃいけないのに"
ssh "どっちか一方の理由でも生徒会に入りたがる人を動員できないのなら、私のやってきたことは全部徒労よ"



show shizu adjust_angry
with charachange


ssh "あまりぐずぐずしてるんだったら、私ができるだけ長い間生徒会長に居座ってやるわ！"

play sound sfx_snap


"その一文を強調するために静音は指を鳴らし、銃声のような音が響く。どれだけ大きな音がするか、静音はわかっているんだろうか。"


"間違いなく周りの注意は引く。だから聾者にとっては貴重なんだろうとしか言えない。静音はそのために練習したのかもな。"


his "『全部』か？　そりゃずいぶん厳しいじゃないか"

show shizu behind_blank
with charachange


ssh "私はこれが実地テストだといつも考えてるわ。いつまでも消えない印象を残すのは大事なの。だから私は砂のお城は作らない。自分が去るときには壊れてしまうから"



his "かもな。でも、ものすごくよくできた砂のお城なら、それでも俺はすごいなって思うぜ。俺だったらすごいなって言うよ"



his "お前のこと、ある意味尊敬してるんだよ。だから俺にとっては、それは無意味じゃない"

show shizu adjust_happy
with charachange


"静音は眼鏡を外そうとしているかのように引っ張り、皮肉っぽく笑う。"

show shizu basic_normal
with charachange


ssh "ごめん"

show shizu behind_blank
with charachange


ssh "不注意だったわ。わがままがつい出ちゃった"

show shizu basic_normal
with charachange


ssh "私、いつもトップに立ちたいって思ってた。それが何かはどうでも良かった。私が一番で、それを完全に理解してて、自分のものにしている限りは"

show shizu adjust_happy
with charachange


ssh "歌を聴いて音楽家になる夢を持つとか、飛行機を見てパイロットになりたいって思うとか。そんな夢を持ったことはある？"


his "ああ"



"初めてサッカーをしたとき、世界をあっと言わせるくらい上達できるだろうかと考えたりもした。"
"でもそれはただの妄想だった。自分と、本当に才能ある人たちの間にあるギャップを見た瞬間、俺はその夢を過去に置いていった。"



"まあ、この心臓だし、もうサッカーはできないけどな。"


his "お前はまだそういう夢があるのか？"

show shizu basic_normal2
with charachange


ssh "いいえ。非現実的じゃない、そんなの。すぐに気づいたわ。世の中には必ず、自分よりもできる人がいるんだから"


"郷愁がその表情に浮かぶ。今の静音はやけに大人びて見える。頂点を目指して他人と熾烈な争いを繰り広げていた日々が、まるで遠い過去であるかのように。"



"もちろん、それが事実からかけ離れていることも俺にはわかっている。つい先週だって、静音は一枚のガムで誰が一番大きな風船を膨らませられるか競争しようとした。"
"小さい頃の静音は今よりもずっとひどかったのかもしれない。その考えに俺はぞっとする。"



show shizu behind_smile
with charachange


ssh "そのことがいいなって思ってた。自分よりも優れた人が必ずいるってことが。そういう人が現れたら、すごく興奮した。その人たちに挑んでみたいって思った"

show shizu adjust_frown
with charachange


ssh "でも最後には、たいていその人たちの方が本当に優れているってことを思い知って、 愕然とするの。まるでレベルの違う人っていうのが、いたりするものなのよ"
ssh "しばらくして、私は嫉妬してた。自分にもそういう何かが欲しくなった"



his "生徒会はお前にとっての、自分だけの何かっていうことか？"

show shizu basic_normal
with charachange


ssh "違う違う。時々そう感じることもあるけど、そのために始めたんじゃないわ。それは全然別の話"

show shizu adjust_happy
with charachange


ssh "でも……生徒会長であることは気に入ってるわ。仕事が大変で、いつも背伸びしてるとしても、だからこそこの仕事は面白いのよ。大体、トップに立つ人がいつでも楽ができるなんておかしいでしょ"



his "農民みたいなこと言うな"




"似合わないとは思うけど、つなぎの服と麦わら帽子姿の静音はかわいいだろうな。"


his "じゃあ、それが理由じゃないなら、どうして立候補したんだ？"

show shizu behind_frown
with charachange


ssh "してないわ。でも結局、やりつづけることにしたの。私が生徒会長になりたかったのは、前の生徒会がバカだったからよ"

show shizu basic_normal
with charachange


ssh "それと、私はみんなに発奮してほしい。それでみんなが『あれは面白かったな。今日は面白かったな』って言えるようになってほしい。そういうことよ。思い出に残る経験ってやつ"

show shizu behind_smile
with charachange


ssh "私は幸せよ。だって私たち、成功したんだもの。私と、ミーシャと、あなたが"

show shizu basic_normal2
with charachange


ssh "でも私にもわがままな望みはあるわ。最初は棚ぼた程度のおまけだと思ってたけど、私も欲張りになっちゃった"

show shizu behind_blank
with charachange


ssh "だから、選挙がスムーズに進むのが私はうれしいの。それが私の願いがかなう唯一の道だから"


his "じゃあ何だよ、それは？"

show shizu adjust_blush
with charachange


ssh "ひみつ"



"そんな思わせぶりな言い方では俺は納得しないと察したのか、静音は恥ずかしそうに頬を染めながら、すぐに手を振ってそれ以上の追求を拒む。あまりに他愛ないので、自分だけの秘密にしておきたいんだろう。"




"ふと空腹を感じて、腕時計を見る。思ったよりは早い。夕食には早すぎる。"



his "机の中に何か食べる物ないか？"

show shizu cross_wut
with charachange


"一瞬、静音はその質問に戸惑ったようだけど、すぐに立ち直る。"

show shizu behind_frustrated
with charachange


ssh "机には資材を入れるものよ"




his "食べ物は資材だろ"


show shizu basic_normal
with charachange


ssh "お昼を食べておけば良かったでしょ"


his "食べなくても大丈夫だろうと思ったんだよ。仕事をしていれば考えなくても済むって。忙しすぎて腹が減ったって感じるひまもないだろうから"

show shizu adjust_happy
with charachange


"笑うのを隠そうと静音は手を口に当てるけど、あまりうまく隠せていない。その手で眼鏡を鼻柱の上に上げるふりをして、さらに無理矢理隠そうとする。"


his "お前は腹減ってないんだろうな。もう食べたんだし"


"そのものずばりの言葉を伝えられるほど手話に詳しいわけではないので、かわりにゴミ箱の中に積み重なって、崩れそうになっている中華料理の容器を指さす。"

show shizu basic_normal
with charachange


ssh "それは昨日のよ"


his "じゃあ二人とも腹が減ってるってことだな。何か食べようぜ"


his "食堂のメシはなしだぞ。昼もろくなものがなかったから、今行ってもいいものは何も残ってないと思う。出前でも取るか？"

show shizu behind_frown
with charachange


ssh "二日連続で出前は不自然よ。緊急の時以外はだめ。私の個人的なポリシーなの"



"だったら机の中にお菓子の一つや二つくらい入れておけばいいのに。こういう『緊急事態』をやり過ごすのだって楽なはずだ。"
"そう言ってやりたいけど、五回も腹が減ったと手話をしていたら、そんな偉そうな真似をするには疲れすぎてしまった。"



"そうしたいという誘惑はものすごく大きいけどな。"


mi "やっほ～！　こんちは、こんちは！"


"ミーシャ独特の抑揚のついた声が、ドアを挟んで聞こえてくる。その一秒後に本人が突入する。"

show shizu behind_blank at tworight
show bg school_council at bgright
with dissolvecharamove

show mishashort perky_confused at twoleft
with charaenter


mi "……"

show mishashort perky_smile
with charachange


mi "ひっちゃん～！　ひっちゃんもいるじゃん～！"


hi "『も』？　どうして他の人もいるって知ってたんだ？"

show mishashort sign_smile
with charachange


mi "ドアが開くなら、誰かがいるってことだよ～"

show mishashort cross_laugh
with charachange


mi "わはは～！"

show mishashort hips_grin
with charachange


mi "おじゃましちゃったかな～？"

show shizu basic_normal
with charachange


"静音は首を振る。"

show mishashort hips_smile
with charachange


mi "よかった～！　すごくよかったよ～！　絶対邪魔してるって思っちゃった。休憩中なの？"


hi "俺もそう思ってたんだけどな、でも生徒会がらみの仕事はもう全部おしまいなんだって。今のところは。お前もそのことで来たのか？"

show mishashort perky_smile
with charachange


mi "わはは～！　うん！　そうだよ、ひっちゃん！"


ssh "がっかりさせちゃってごめんね。夕食に出前を頼もうかって話をしていたの"

show mishashort hips_grin
with charachange


mi "それ、楽しそうだね～"


hi "静音はあまり楽しくないけどな。二日連続で出前はだめなんだと。お前も腹減ってるか？　もしそうなら、俺たち二人で静音に多数決で勝てるからさ"

show mishashort hips_smile
with charachange


mi "う～ん、う～ん、それ楽しそうだよ、ひっちゃん！　それに、わたしもちょっとおなか減ってるし……"


hi "お前なら、そんなの裏切りみたいだって言うと思ったけどな"

show shizu adjust_frown
with charachange



"静音は眼鏡の縁をつまむ。明らかにこれが裏切りみたいだと思ってるようだ。"
"でも争う余地もなく二対一で少数派になった静音にはどうすることもできない。ミーシャはもう携帯を取り出している。ものすごく派手にデコレーションされている。"



show mishashort sign_smile
with charachange


mi "しっちゃん、わたしたちだけで生徒会パーティするって約束したでしょ、ね～？　そうだよ、そうだよ～！　今からそうしようよ～！"

show shizu behind_frown
with charachange


"静音は頭を振るだけだ。山久の生徒会長として参加できる最後のパーティという機会は、静音にとってとても大切なものだ。こんな行き当たりばったりの夕食はその題目にはふさわしくない。"

stop music fadeout 3.0


"ただ、もしその時が来たら、それは今と全く同じような感じになるに違いない。俺たち三人で。"

scene bg school_dormext_full_ss
with shorttimeskip


"夕食を食べ終わって片づけたあと、二人に別れの挨拶をして寮の部屋に戻る。特に疲れているわけではないけど、今夜はさっさと寝ようと思う。"



"これが自分の家だったら、食べてすぐ寝るんじゃないと母さんにガミガミ言われるだろう。でも知らぬが仏ってやつだ。"




scene bg school_dormhisao_ss
with locationskip


"部屋に入ってすぐ時計を見る。思ったよりもかなり遅い時間だ。"


"携帯と腕時計を持っているのに、わざわざ壁の時計を見るのはおかしな感じだ。俺は腕時計を外して片手に持ち、もう片方の手で携帯を持つ。なんだか自分が強くなった気がする。そしてバカみたいな気がする。"


play sound sfx_doorknock


"寝ようとするけど、寝付けない。ほんの数分後にドアがノックされて、邪魔が入ったのをありがたいと思う。健二に違いないと思っていたのに、現れたのはミーシャだったのでびっくりする。"

play sound sfx_dooropen

scene bg school_dormhallway
show mishashort hips_smile at center
with locationchange


mi "こんちは、ひっちゃん～！"

show mishashort perky_sad
with charachange


mi "わたしに会うの、うれしくなさそうだね～……"


hi "いや、ちょっとびっくりしただけだよ。静音が何か、俺に頼む仕事があるのを思い出したのか？"


hi "もう夜遅いけど……まあいいや。着替えてなくてちょうど良かったな"

show mishashort sign_smile
with charachange


mi "ちがうよ～。ただひっちゃんについて行こうって思ったんだ～！"


hi "面白半分でか？"


"違う。そんなわけがない。話があるからに決まってる。大事なことに違いない。静音に知られたくないことだ。"


hi "入るか？"

show mishashort hips_grin
with charachange


mi "うん、ありがと～、ひっちゃん！"

scene bg school_dormhisao_ss
show mishashort invis at center
with locationchange

show mishashort perky_smile_ss at Position(ypos=1.13)
with dissolvecharamove

play sound sfx_doorclose


"中に入ると、ミーシャはすぐにいすに座る。何もおかしくはないけど、ベッドに腰掛けるんだろうと思ってたのに。"

show mishashort cross_frown_ss
with charachange


mi "ひっちゃん……"


"ミーシャは胸の前で腕を組むと、すごい形相で俺をにらむ。厳しい尋問者気取りのようだ。あとは口ひげと、天井からつり下がっている切れかけた裸電球があれば完璧だな。"



mi "しっちゃんを悲しませるようなこと、した？"

play music music_drama fadein 6.0


hi "どういうことだよ？"

show mishashort hips_frown_ss
with charachange




mi "今日生徒会室に行ったとき、しっちゃんはわたしが入ってくるのが聞こえなかった。それで～、ドアを開けたら、しっちゃんがすごく困ったような顔をしてた"
mi "嬉しそうだけど悲しそうだった。それがどうしてか知りたかったの"




hi "まあ、俺のせいじゃないぞ。俺はそんなの見てもいないし"


hi "あと何ヶ月もすれば生徒会長じゃなくなるってことに気落ちしてるんだと思うぜ"

show mishashort perky_confused_ss
with charachange


mi "う～ん……わたしがしっちゃんに聞いたときは、大丈夫だって言ってたよ～！"


hi "そんなの意味ないよ。静音ならそう言うだろうけど、あいつがそんな簡単にあきらめるって思う方がおかしいだろ"


hi "というか、一つしかないリンゴとか、さもなきゃチョコレートミルクとか、なんでもいいけど、そういうのを巡って俺と争うことはあるよ。でもそれは大事でも何でもないことだろ"

show mishashort hips_frown_ss
with charachange


mi "チョコレートミルクは大事だよ"


hi "わかったよ。怒るなって。でもあいつにとっての生徒会ほどじゃない。あいつはそう簡単に流したりはしないよ"



show mishashort hips_grin_ss
with charachange


mi "わはは～。そうだね～"


"これは尋問のはずだと思ってたけど、ミーシャはもう忘れてしまっているようだ。"

show mishashort sign_smile_ss
with charachange


mi "でも～！　わたしが気落ちしないようにしっちゃんがうそをつくなんてやだよ"

show mishashort hips_grin_ss
with charachange


mi "ははは～！　みんなしっちゃんがどれだけ真剣か知らないんだよ。ただかっこつけてるだけだって思ってるんだ。ひっちゃんはしっちゃんのことをきちんとわかっててくれて、うれしいよ"


hi "見ればわかるさ。今日あいつが話すのを聞いたから、なおさらな"


"ミーシャは頭を手のひらに乗せて、興味深そうにこちらに身を乗り出してくる。"

show mishashort cross_smile_ss
with charachange


mi "ほんとに～？　なんて言ってたの？"


"静音とは十分に親しいことだし、ミーシャが詮索するのも気にしたりはしない。"



hi "生徒会に入った理由のことさ。大体は。それを話し始めたけど、黙っておいた方がいいこともあるって考えた。で、『秘密』って手話をした。だから秘密ってことなんだろうな"

show mishashort sign_smile_ss
with charachange


mi "えっと～、誰かが秘密があるって言っているときは、それ自体がある意味秘密だって言えるんじゃないかな、ひっちゃん～！"


hi "いつかお前が言ってた、幸運も実力のうちってのと同じようなものか？"

show mishashort hips_grin_ss
with charachange


mi "そうかもね！"

show mishashort cross_laugh_ss
with charachange


mi "わはは～！"


hi "気をつけろよ、声でかいよ"

show mishashort perky_confused_ss
with charachange


mi "どうして、ひっちゃん？"



hi "建物中のみんなが目を覚ましちゃうだろ。それに寮は男女別なんだから"




show mishashort hips_frown_ss
with charachange


mi "ひっちゃん、なんかエッチなこと考えてる？"


hi "変なこと言うんじゃない"

show mishashort hips_grin_ss
with charachange


mi "あははは～"

show mishashort hips_smile_ss
with charachange


mi "ひっちゃんだったら、いいよ、わたしは"



"それを聞いて、今までずっとミーシャと気兼ねなく話せていたことに、これからも用心なんていらないはずだと思っていたことに気がついた。俺がミーシャに警戒心を抱いたのはこれが初めてだ。"


show mishashort perky_sad_ss
with charachange


mi "わたし悲しいよ、ひっちゃん"



mi "おかしいよね、しっちゃんが喜べば喜ぶほど、わたしはどんどんつらい気持ちになるの。わたしもしっちゃんのことを喜んであげなきゃいけないはずなのに"
mi "今もつらいんだ……でも～、わたしの悩みをしっちゃんに話すなんてできないよ"



hi "どうして？"

show mishashort sign_sad_ss
with charachange




mi "しっちゃんが自分の悩みをわたしに話せないのと同じだよ。同じことなんだよ、ひっちゃん。もしわたしたちが二人ともそういう悩みを抱えてるんだとしたら、もうどうすればいいのかわからない"
mi "もしかしたら……わたし、だめな友達なのかな"









show mishashort perky_sad_close_ss at center
with characlose

stop music fadeout 2.0



"ミーシャは立ち上がると、素早くベッドに腰掛ける。俺との距離は数センチしかない。その直後に頭を前に出して、俺に軽く口づける。唇からは外れたけど、俺のせいというよりはミーシャの狙いがまずかったせいだ。"



hi "何してるんだよ？"


"あえて聞きはしたけど、これで何をしようとしているかわからないほど俺はバカじゃない。ただ、自分がこの事態に正面から向き合わずにすむ方法があればいいのにと考えているなんて、おかしすぎる話だとは思う。"


show mishashort hips_grin_close_ss
with charachange


"今度は恥ずかしがるそぶりを見せ、困ったように笑う。"


mi "……"

show mishashort perky_smile_close_ss
with charachange


mi "ひっちゃん、わたしのこと好き？"


hi "ああ"


"ミーシャの頭が俺の胸に埋まる。ミーシャが俺の傷に向かって話しかけているみたいだ。頬に傷が当たるのを感じているかもしれない。"


"二人からそのことを必死で隠そうとしたことがあった。今思えば、あんなに不安がったのは本当にバカみたいだったと思う。"

show mishashort perky_sad_close_ss
with charachange



label jp_choiceS28:
menu:
    with menueffect
    mi "お願い、なぐさめて、ひっちゃん。今日だけでいいから"
    "ミーシャを慰める":





        return m1
    "拒む":


        return m2


label jp_S28a:

play music music_moonlight fadein 4.0



"文句を言うふりはしていても、俺はこうなるまで事態を成り行きに任せてしまっていた。これがミーシャの狙いだったなんて、言われるまでもなくとっくに分かっていたというのに。"




"少なくとも、俺はこうなっても構わないと思っていた。まだミーシャを拒んでいないのが何よりの証拠だ。"



"拒否しようと思えばいつだってできた。早くそうしなかったのは俺の過ちだった。でもこの時点で拒否しないのは、単なる不注意を通り越している。"

show mishashort perky_sad_close_ss:
    linear 0.2 alpha 0 ypos 1.1
with vpunch

hide mishashort
with None




"ミーシャは俺が黙っているのを合意と受け取って、ぎゅっと自分の体を押しつけてくる。まるで俺の服の中に入り込もうとしているみたいだ。"
"腕がミーシャの柔らかな肌と、暖かい体に包まれる。俺は反射的に身を返して、ミーシャに覆い被さる形になる。"





"俺がリードするのを期待するような目で、ミーシャが俺を見つめる。でも俺が見つめ返した途端にあわてて目を閉じる。仕方なく、まごまごとした手つきでミーシャの服を脱がし始める。初めての経験だ。"

label jp_S28h:

scene evh misha_naked:
    xalign 1.0 ypos 0.0 subpixel True
    easein 12.0 xalign 0.0
with whiteout



"まだ一回しかセックスをしたことがないし、しかもその時は椅子に縛り付けられていた。今回は俺が主導権を握っている。"
"あの時もそうだったら良かったのに。でも今になってみると、恐ろしい感じがする。手始めにブラウスのボタンを外して、肩からすっと脱がせる。"



"思っていたよりもミーシャの体つきはくびれていて、かわいらしい表情によく似合っている。"


"ブラのホックは背中にあって、外すのに苦労する。ミーシャが胸を見せるのを恥ずかしがって、まだ外し終わっていないのに半ば無意識に隠してしまうので、余計に大変だ。"


"スカートの留め具を外してパンティを下ろそうとすると、弱々しい、形だけの抵抗がだんだん増えてくる。それはただの儀式でしかない。"


"そういう儀式がミーシャにとってとても大事なのだと気づく。だからミーシャは誰彼問わず必ずうれしそうにあいさつをするんだ、たとえ相手に会うのがうれしくないとしても。"





"ミーシャはまた目を開いていて、俺は手をその内股に滑らせる。ミーシャは笑い声を上げそうになりながら足を閉じるので、危うく手がつぶれるところだった。演技ではない、かわいらしい反応だ。"




"経験のなさをごまかすのは静音のほうが上手だった。あいつも同じくらい恥ずかしがっていたけど。"


hi "いいか？"


"俺を見ることもせず、ミーシャはうなずく。"

scene evh misha_sex_aside:
    truecenter
    subpixel True zoom 1.05
    easein 6.0 zoom 1.0
with locationchange



"中に押し入ると緊張でミーシャが体をこわばらせるのが伝わってくる。そして俺自身が中で押し返されるのを感じて、自分まで緊張してくる。あまりに体が固まってしまい、動くたびに痛いくらい機械的になっている。"





"静音がやったときのように、もっと早く動くべきなのか。でも静音はずっとやる気に満ちていた。今は状況が違う。こんなことになって、俺は後悔している。"
"ゆっくりと、俺は挿入していく。ミーシャが痛みに顔をゆがめる。"




mi "お願い、早く……"




scene evh misha_sex_closed:
    zoom 1.0
with locationchange


mi "いたっ……"


"俺は動きを止める。"

scene evh misha_sex_aside
with locationchange


mi "いいよ、大丈夫"


"そして、竿の部分まで、さらに奥深く押し進める。ミーシャの手が俺の腕をしっかりと握り、さらに上の方に伸びていくのを感じる。俺の体をよじ登ろうとしているかのようだ。"



"俺の肩をぎゅっとつかむと、ミーシャは体を起こし、さらにきつく体を重ね合わせる。俺には押し返すことしかできない。"


scene evh misha_sex_closed
with locationchange


mi "あ～……あはああっ……"


"ミーシャの喘ぐ声を聞きながら、俺は速度を上げ、リズムをつかむ。ミーシャの両手が俺の背中で合わさって、俺が一突きするたびに、ミーシャのひじが俺の肋骨の下の隙間に食い込むのを感じる。"


"打ち鳴らされるドラムのように、耳の中でどくどくと血の流れる音がする。もうミーシャの声もほとんど聞こえてこない。"


mi "っふ……んん～……"

scene evh misha_sex_aside
with locationchange


mi "男の人とするの、初めてだよ。おかしな感じ"



"頼むから喋らないでくれ。ミーシャの声はあまりに静かで、息づかいも混じっていて、聞き取るのが一苦労だ。でもにじみ出るような悲しげな声の調子は間違いようがない。そのことが余計にやましい気持ちにさせる。"




"ミーシャを慰めているはずなのに、慰めているのは肉体でしかない。仮にこれで少しでも慰めを得ていたとしても、ミーシャはそれを表に出していない。"
"それを見て、本当にこの決断は正しかったのかと疑問を抱く。俺は真剣に疑い始めている。"


scene evh misha_sex_closed
with locationchange



"それでも、ミーシャが柔らかくのどを鳴らす声が耳に伝わり、俺はそのまま動き続ける。俺のモノの周りにまとわりつく、なめらかな締め付けも。"
"やがてミーシャの足が俺の足にからみつく。オーガスムに全身がこわばり、すべすべした首筋が俺の頬に押しつけられる。"


scene evh misha_naked
with whiteout

stop music fadeout 6.0


"一分ほどして、ミーシャは俺から体を離す。その時、ミーシャの全身を見ることができた。ピンク色の肌が明るい朱に染まり、汗まみれになっている。俺は寒気を覚える。"


mi "……ひっちゃん？"


"時計の針の音と、自分の息づかい以外、俺には何も聞こえない。"


mi "……なんでもない"


"自分の手でミーシャの手を探し出し、そっと撫でる。こんなにしっかり俺の手首を握っているというのに、その手はあまりにも軽くて繊細そうに見える。この感触を俺は知っている。"




scene black
with dissolve




label jp_S28b:

show mishashort perky_sad_close_ss:
    linear 0.2 alpha 0 ypos 1.1
with vpunch

hide mishashort
with None

play sound sfx_pillow


"俺が答える前に、ミーシャは全体重を俺に預けてくる。俺はバランスを崩して、ミーシャもろともベッドに倒れ込む。早く答えないと、状況はどんどん危険になる。"



"こうなる前になんとかしなくてはいけなかったんだ。それはわかっている。"





"なので、あまり気の利いたやり方ではないけど、俺はミーシャを押し返す。ミーシャは後ろ向きにシーツに倒れ込む。でもそっと倒れたので、落ちたようにはまるで見えない。"
"目を閉じたまま、しばらくそのままの姿勢でじっとしていたけど、やがて虚ろな笑いとともに起き上がる。"


show mishashort invis:
    center
    ypos 1.2
with None

show mishashort perky_sad_ss at center
with dissolvecharamove

play music music_moonlight fadein 6.0


mi "そうだよね、ひっちゃん。ごめんね"

scene black
with shuteye



"自分の気持ちがよく分からない。"
"少しの後悔。俺は後悔だけはしたくないと思っていたのに。いろいろな理由があるけど、悲しみ。それと少し怒っている。ミーシャと自分の両方に。そしてある意味、何も感じていないようにさえ思える。"



hi "謝るなよ"


mi "いいの、ひっちゃん。大丈夫だよ～。大丈夫だから、ほんとほんと～"



mi "でも……わたしにとっては、聞くだけで十分だったんだ、って思うの"




mi "ダメって言ってくれて、うれしかったよ"





hi "そうなのか？　まあ、そりゃよかった"


mi "うん、そうだよ～。ありがとね、ひっちゃん"



"ミーシャは体を起こすと、壁により掛かる。少なくともそうしているんだろうと思う。頭があまりに痛くて、おれは目を開けることもしない。"
"ただベッドに横になって、自分の髪がシーツにこすれる音と、外で草が風になびく音を聞いている。"



"もっとミーシャを安心させるようなことを言うべきなんだろう。でもどんなことを言えばいいのか。何も言わないほうがいいかもしれない。わからないけど、でもこういうときは唯一正解なんてありはしないんだろう。"


mi "おやすみ、ひっちゃん"

play sound sfx_doorclose

stop music fadeout 4.0


"そう言ってミーシャは立ち去り、後ろめたいささやきのように、ドアがかちりと音を立てて閉まる。"


"今夜のことを早く忘れたいと思っているからかもしれないけど、ミーシャがいなくなった後、寝つきがずっと良くなった。俺はあっという間に眠りにつく。"

scene black
with dissolve





label jp_S29:

scene bg school_dormhisao
with locationchange

play music music_night fadein 4.0


"翌朝に目を覚ましながら、今日はとにかく静音とミーシャを避けながら過ごすことになるんだろうな、と考える。"


"昨日のことが気になって今も落ち着かない。一晩寝れば気も晴れるだろうと思っていた。そう簡単にすむと思っていた自分がバカみたいだ。"


"ミーシャも同じような気持ちでいるのかな。だとしたら、今日は学校には来ないだろう。俺も休もうかと考えたけど、相当怪しまれるだろうし、怖がって一日中部屋にこもるなんてごめんだ。俺はそんな臆病者じゃない。"


scene bg school_scienceroom
with locationskip


"思った通り、ミーシャは教室にいない。静音はいるけど今日は普段よりも忙しくて、授業の内容に集中している。つまり俺とおしゃべりを始めるような空き時間はないってことだ。"


label jp_S29a:



"今まで静音と話したいと思って必死になっていたのに、今頃になってそのことから逃げようとしているのはおかしな気分だ。"
"でもそれ以外にどんな気持ちになればいいっていうんだ。俺は静音の一番の親友と寝てしまったというのに。"







"自分がこんな気持ちなら、ミーシャはどうなんだろう。同じくらい後悔しているのか？　俺に誘いをかけてきたとき、あいつは色っぽかったというより落ち込んでいた。"
"今のあいつがどれだけ辛い思いをしているかは、想像することしかできない。"






"そうやって考えていると、ミーシャにまた会いたくなってくる。でもその気持ちは半分でしかない。残りの半分はまだ恐怖で震え上がっている。認めたくはないけど。"



"情けない気持ちになる。でも今の自分を説明できる言葉はそれしかない。いやな気分だ。"


label jp_S29b:


"静音とミーシャと一緒にいることに慣れきってしまって、最近はあまり一緒ではないということに昨日まで気づかなかった。"


"ひどい話だ。隣の席が空いていることが、二人で一組という事実を思い出させる。昨日のことは墓場まで持って行くしかない。"





"自分がこんな気持ちなら、ミーシャはどうなんだろう。同じくらい後悔しているのか？　そもそもミーシャが俺のところに来たとき、あいつは色っぽかったというより落ち込んでいた。"
"今のあいつの気持ちは想像することしかできない。"




"そうやって考えていると、ミーシャにまた会いたくなってくる。でもその気持ちは半分でしかない。残りの半分はまだ恐怖で震え上がっている。認めたくはないけど。"



"情けない気持ちになる。でも今の自分を説明できる言葉はそれしかない。"



label jp_S29x:

scene bg school_library
with shorttimeskip


"一日ずっと授業に出続ける気分でもなく、といって寮まで戻る気にもなれず、次の数時限は図書室で過ごす。"

show shizu invis at center
with None

show shizu behind_frown at Position(ypos=1.14)
with dissolvecharamove


"面白くもない歴史小説のページをだらだらとめくっていると、俺の正面のいすに静音がどっかと座る。不機嫌そうだ。"

show shizu adjust_frown
with charachange


ssh "学校に来て授業は全部さぼってるんじゃ、来る意味ないと思うけど"


his "悪かったな"

show shizu behind_frustrated
with charachange


ssh "せめて病欠だってみんなに言っておけばいいじゃない"




his "今日は気分がのらないだけだよ。昨日は全然問題なかったんだし。明日になればよくなるって。週のど真ん中で病欠なんて怪しすぎるだろ。そんな『一日風邪』にかかった、みたいな言い訳は通らないよ"





show shizu adjust_frown
with charachange


ssh "怪しくなんかない"



his "怪しいだろ"


show shizu basic_angry
with charachange


"俺は本に意識を戻すけど、静音がそっと本を下げる。その動きと裏腹に、表情は心配と怒りの間を行き来している。"

show shizu behind_blank
with charachange


ssh "何かあったの？"


his "は？"

show shizu basic_normal2
with charachange


ssh "何か気になることがあるの？　だって今日は何だか様子がおかしいから。違う意味で"

show shizu behind_blank
with charachange


ssh "もしあるんだったら教えて。さもないと怒るからね。人の気持ちを読むのは得意じゃないの"


"めちゃくちゃなことを言う。俺の気分にはあっさり気がついたくせに。"


"半分冗談だろうけど、事実でもある。確かに声の調子は静音には聞こえないし、他の人とコミュニケーションを取るには気持ちを読むしかない。"


"電子メールでしか他人と会話ができないようなものだ。それは苦労するだろう。"



"他人をすごくじっと見つめるのもそのせいだろう。相手の反応を見極めるためだ。他人をぐいぐい追いつめるのもそれが理由なのかも。そうやってリアクションを引き出すんだろう。"




"前にも考えたことはあるけど、それが何であれ、静音の動機というのをはっきりと言い当てるのは難しすぎる。"



"なので、今のはどこまで冗談だったのか、と考えてしまう。時にはわかりやすいけど、今度のはわからない。冗談じゃなかったとしても、静音には言えない。"
"手話を使っているおかげで、落ち着いてうまくうそをつく余裕がとれた。"



his "何もないよ"

show shizu cross_wut
with charachange


shi "……"


his "最近、生徒会の将来のことをいろいろ考えてたってだけさ。ミーシャも同じだと思う……まあ、あいつなりに"

show shizu behind_frustrated
with charachange


ssh "私だってそうよ。でもミーシャは今日休んでるから。ミーシャも教えてくれればいいのに。今日は手伝いが必要になるかもしれないから。あなたもね。忙しくなければだけど"


his "俺は別に……"

show shizu basic_normal
with charachange


ssh "ありがと"

show shizu behind_sad
with charachange



ssh "最近、親しかった人たちをいっぱい失っていってる気がするの"





"いい返事の仕方が思いつかない。安心できるようなこと、心配しなくていいということを。『俺がいるから、俺はそんな連中とは違う』って。"


"じゃあ、それは誰なんだ？　それにいかにも無理やりに聞こえる。俺はどうにか手を振るけど、そうしたとたんにものすごく無神経な仕草に見えてしまう。"



his "そういうこと考えるのはやめろよ"



show shizu basic_normal2
with charachange


shi "……"


his "ちょっと気分が悪くて、わざわざ表沙汰にするような気力がないってだけさ。俺はそのほうが楽ってだけだよ"

show shizu behind_frown
with charachange


ssh "それは間違ってる"


"楽じゃないやり方と正しいやり方は、たいてい同じやり方だと聞いたことがある。だからその逆が成り立つというのも拡大解釈とは言えないだろう。"

show shizu basic_normal
with charachange


ssh "まあ、いいわ。あなたが大丈夫だって言うなら、それで十分"


his "待てよ"

show shizu behind_blank
with charachange


shi "……？"


his "お前から聞いたんだし、今度はこっちから聞くぞ。お前は大丈夫なのか？"

show shizu basic_normal2
with charachange


ssh "ええ"

stop music fadeout 3.0


"一瞬のためらいもなく、手話で返す。そして俺がそれ以上追及するのを待ちかまえる。"

show shizu invis at center
with dissolvecharamove

hide shizu
with None


"俺は何も言わず、静音は立ち去る。突っ込まなかった自分がバカみたいだ。その方がよかったとは思うけど、それでも。"


"図書室にかなり長居してしまった。気分を変えようと屋上に行くことにする。"

play sound sfx_door_creak
play ambient sfx_rooftop fadein 1.0

scene bg school_roof_ss
with locationskip


"ドアを開けると、さわやかな風が俺に吹き付ける。ここは学校の中でも特にお気に入りの場所だと思う。すると先客がいることに気づく。目の前にピンク色の髪の女の子がいる。"



"俺に背を向けてはいるけど、顔を見なくたって誰なのかはわかる。あんな髪の持ち主は世界でもミーシャ一人だろう。"




"まずいタイミングでばったり会ってしまった気がする。一人になりたくてここにいるのは明らかだ。俺のことにはまだ気づいていないだろうか。"
"だとしたら今すぐに立ち去るところだ。でもミーシャは気づいてしまい、振り向いて俺を見る。"


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene ev misha_roof_normal:
    yalign 1.0 xalign 0.5 subpixel True
    easein 12.0 yalign 0.0
with whiteout

play music music_sadness fadein 8.0


mi "ああ、ひっちゃん。誰か後ろにいるって思ったけど、ひっちゃんだとは思わなかった。今度はひっちゃんにびっくりさせられちゃったね"


"後ろに忍び寄って『誰だ』ってやる、あれのことを言っているんだとしたら……あんなのでびっくりしたことなんて一度もないぞ。"


hi "俺も驚いたよ。でもよかった。お前と話したいこともあったしな"


mi "……"


hi "そっちのことじゃないぞ……"




hi "お前と静音、何かあったのか？　静音は教えてくれないから、お前に聞くけどさ"



"『お前の方が答えを引き出しやすいから。手話なら俺もうそをつくのが楽だけど、静音にとっても俺の質問が受け止めやすく、はねつけやすくなるから』。ミーシャがためらうと、俺はさらに詰め寄る。"




hi "正直に言ってくれ。頼む"



mi "ややこしいんだよ、ひっちゃん……ずっと昔の出来事が原因なの。忘れられると思ってたんだけど、でも～……すごくつらいんだよ"
mi "だから～、それともうすぐ卒業っていうのもあって、もっとしっちゃんと一緒に過ごしたかったんだよ～！"


scene ev misha_roof_sad
with charachange


mi "でも最近、しっちゃんはずっと忙しいし。だから～！　わたしたちけんかしてるの。でももうけんかするのもいやになってきたの"


mi "だって～……しっちゃんのことが好きだから"


hi "俺だってそうだよ"

scene ev misha_roof_normal
with charachange


mi "わはは～。ちがうちがう～、ひっちゃんがしっちゃんのこと好きなのは知ってるよ。わたしも同じようにしっちゃんのことが好きだってこと"

scene ev misha_roof_closed
with charachange


mi "しっちゃんと恋人同士になりたいの"


"ミーシャは目を閉じる。処刑人の前で最後の罪を自白する死刑囚のように。よけいに返事を考えるのが難しくなる。何か言わなければいけないのはわかっているのに。"


hi "そうだったのか。全然気づかなかった"

scene ev misha_roof_normal
with charachange



mi "この学校にだって来たくなかったんだよ、ひっちゃん～。でも面白そうだなって思ったから"
mi "それにみんながわたしのこと嫌ってても、少なくとも放っておいてくれるって思ったんだ。わたし手話を勉強してたけど、あまり上達してなかったから～"



mi "しっちゃんは生徒会に人を勧誘してたんだ、自分とリリーしかいなかったから。そしたらわたしのところに来たの。何言ってるのかぜんぜんわからなかったよ～"

scene ev misha_roof_angry
with charachange




mi "でも～！　しっちゃんはペンと紙なんて使わないし。わたしが手話のクラスにいるの知ってたの。手話なんて全然知らないのに、すぐばらされちゃって～"
mi "……そしたらよけいに誘ってくるの。しっちゃんのこと嫌いになった。わたしをからかってるんだって思った"




scene ev misha_roof_normal
with charachange


mi "でもそうじゃなかったんだ～……"





mi "それで～！　だんだんしっちゃんのことが好きになって……好きだって伝えたの"

scene ev shizu_flashback:
    truecenter
    zoom 1.15 subpixel True
    easein 30.0 zoom 1.0
with whiteout


mi "生徒会室にいたときだった。わたしたち二人きりで"


mi "しっちゃんが生徒会室に一人でいて、いろんな仕事を全部自分でやってる姿をいつも想像してた。それがとっても寂しそうで、悲しいって思ったんだ～。そうであってほしいって思ってたんだ～"



mi "そしたら、しっちゃんの手助けができるし、もしかしたらしっちゃんもわたしを好きになってくれるかもしれない"
mi "そう考える理由なんてなかったけど、そう思った。そうなってほしかったから、わかっていたけど、そう信じることにしたの"




mi "それにその日はね、すっごくすっごく～、きれいだったんだよ、ひっちゃん～。仕事が終わって、窓の外を見てたの。窓越しでも光がとっても暖かくて～……ずっとそうしていたかった。しっちゃんの隣で"




mi "でも～！　それでしっちゃんを見ると、窓に背中を向けてまだ仕事を続けてたの。ほかのことは全部意識から追い出して。光がしっちゃんの肩にかかってた。ちっちゃいときのわたしが、肩に毛布をかけてたみたいに"




"想像の中の静音のイメージを手放すまいとするかのように、ミーシャは一瞬だけ言葉を切る。"


mi "その時のしっちゃんは……ん～……なんていうか、一緒にいたいっていう気持ちになるような、そんな姿だったの……でもそれが現実になるのは難しいだろうなって感じはしてた"


mi "わはは～。でもそれって、すっご～く昔の話だよ。わたしの髪型も違ったんだよ。ちょっとボサボサっていうか～？　しっちゃんがいつもそのことを言うから、切っちゃったんだ"



mi "とにかく～！　しっちゃんに言ったの。その時、その場で。告白したんだ～"




scene ev misha_roof_sad
with whiteout


mi "でもふられちゃった～"




mi "だから～、それでおしまいだと思ったんだよ、ひっちゃん"
mi "でもしっちゃんはいつもわたしのことを探すから、またしっちゃんのことが嫌いになった。どうしてそんなことするのって聞いたら、わたしは友達だから、って"




"ミーシャの頬にはわずかに赤みがさしている。ミーシャはどれだけ泣いたことがあるんだろう、と思う。こんなに涙を流すことを我慢できるなんて。"
"目をぬぐうために言葉を止めていなければ、俺は気づきもしなかったかもしれない。"



scene ev misha_roof_closed
with charachange


mi "しっちゃんがそう言ってくれたのはうれしかったけど、悲しくもあった。傷つけるつもりで言ったんじゃないのはわかってるけど、それでもつらいんだよ。今だって……"



mi "しっちゃんって、人を自分の思い通りにするくせがあるんだよ、ひっちゃん。そうしたくてすることもあるし、そうでなくても自然とそうなっちゃうこともあるし～"
mi "それでときどき……どっちなのかわからなくなるの。だから疑っちゃって……"




mi "しっちゃんがひっちゃんじゃなくて、わたしのことを好きになってくれたらよかった。それで、ほんのちょっとだけど……自分がひっちゃんやしっちゃんのことを嫌いになってるんじゃないかって思って"
mi "わたし……そんなのいやだった"



hi "じゃあ、俺がそもそもここにいない方がよかったんじゃないかって、そう思ってたってことか？"

scene ev misha_roof_normal
with charachange


"戸惑っているようだ。そんなことは思いもしなかったんだろう。"


mi "そうじゃないよ、ひっちゃん"

scene ev misha_roof_sad
with charachange



mi "この何日か、いっぱい考えたんだよ。わたしは誰のことも嫌いになりたくない。ひっちゃんも、しっちゃんも"
mi "そんな気持ちになるなんて、わたしほんとにバカだよ。そうじゃない、ひっちゃん？　もうこんなこと二度と考えたくないよ"



mi "人と別れるのも、離ればなれになっちゃうのもいや。耐えられないよ。そんなこと、もう考えたくない"




mi "でももう考えちゃったんだけどね。だから～！　……わたしって最悪な人間なんだよ。ひっちゃんがこの学校に来なければ、なんて思ってなかった。わたしは……わたしが死んじゃった方がいいんじゃないかな？"



label jp_S29xa:


scene ev misha_roof_closed
with charachange


mi "それに、わたしは本当にひどいことをしちゃったから。絶対に許されないことを"


"ミーシャは背中をぐっとフェンスに押しつける。そのまますり抜けてしまおうとするかのように。"


hi "バカなこと言うな"


"自分の声の調子に驚く。"


hi "悪い"


hi "俺は後悔したまま取り残されるのが嫌いなんだ。それが何であっても。そう気づいたんだ。それでも何かを後悔せずに済むなんてことはありえない"


hi "昨日はバカなことをしたよ。たぶん、そのこともあって俺はここにいる。もしかしたら……どうにかしてそれを埋め合わせる方法が見つかるんじゃないかって"




hi "そう思ったことってないか？　ひどいことをしたって自分でも言ったよな。それを埋め合わせることだってできるじゃないか"




scene ev misha_roof_normal
with charachange


mi "ひっちゃん～、それって……"


"俺がミーシャのためというより、自分のために言っていると思われている。そんなのはわかってる。"


hi "ちがう。そうじゃない"


hi "自殺すれば、これ以上ないくらい大きな後悔をするはめになる。それだけさ"




mi "……"


mi "ひっちゃんって、ほんとドラマチックだよね"

scene ev misha_roof_closed
with charachange


"本気で言っているのかどうか、俺にはわかりようがない。そのことを詮索はしない。ミーシャがため息をついて、眠りに落ちるかのように目を閉じると、その周りにあった危険な雰囲気は去っていったのを俺は感じる。"



label jp_S29xb:

stop music fadeout 0.5
$ renpy.music.set_volume(0.0, 0.5, channel="ambient")


"ミーシャは背中をぐっとフェンスに押しつける。そのまますり抜けてしまおうとするかのように。"


scene bg school_roof_ss
show mishashort perky_confused_close_ss at center
with vpunch

$ renpy.music.set_volume(1.0, 6.0, channel="ambient")


"深く考えずに、ミーシャの手をつかむ。反射神経が鈍すぎて、つかめたのは何本かの指だけだった。でもそんなことはどうでもいい。"

play music music_rain fadein 6.0


hi "悪い。今、すごく変なこと言ったから"

show mishashort perky_sad_close_ss
with charachange


mi "ははは～。そうだね～、そうかもね、ひっちゃん"


hi "そうだろ"


hi "俺の思ってること、聞きたいか？"



hi "静音は自分のやりかたを受け入れないやつは誰も自分に近づけない。そういうやつだ。イライラすることもあるし、ほんとに腹が立つことだってある"



hi "俺もイライラしたと思う。病院にいたとき、俺をシャットアウトした人がいた。その人は俺にとって死んだのと同じだった。今の今まで完全に忘れてたけど、最近手紙をもらってさ。そのことが延々書いてあった"




hi "腹が立ったよ。『俺が周りのみんなから閉じこもってあきらめたって、どうしてお前に責められなきゃいけないんだ？』"
hi "『それをしたのはお前らの方じゃないか？　ほかにどうすればよかったって言うんだ？　どうしろってんだよ？』ってさ"



hi "そうさ、今だって、そのせいでそうなったって思ってるけど、でも……その人も正しかったんだ。確かに俺は閉じこもってた"


hi "だから決めたんだ。二度とそんなことは起こさせないって。絶対に"

show mishashort perky_confused_close_ss
with charachange


label jp_S29xba:


mi "病院？　ひっちゃん……あの薬はそのせいだったの？"


label jp_S29xbb:


mi "病院？　ひっちゃん……何を言って……"


label jp_S29xbc:


hi "いいから聞いてくれ。頼む"


hi "静音は俺のまるっきり反対だった。あいつはいつも自分のそばに人を引き寄せようとする。最初に俺に興味を持った理由もそれだけだと思う。で、俺はそんなことはさせないと決心してたんだ。ある意味では"


"その意味を完全に理解して、ミーシャは目を伏せる。"


hi "それがこんなに厄介だったとは思わなかったけどな"


hi "今は、その恩を返そうと思うんだ。二倍の時間がかかるとしても。ここまで来るために、もう二つ目の言語も覚えたしな"


hi "思ったほど難しくはなかったけど、やっぱり難しかった。時々、痛むのに素手で山を登ってるような気分になるよ"


hi "お前も同じことをしたんだ。それは同じ理由だったんだろ？　それってすごいよ。だからお前がそんなバカなことを言うなんて、俺は悲しいし、ちょっと怒ってる"



mi "……"


hi "まあ、俺はそう信じてるって話さ"

show mishashort perky_sad_close_ss
with charachange


"すべての力を失ったかのように、ミーシャは肩を落とし、床にずり落ちそうになる。"


mi "ひっちゃんってば、ドラマチックすぎるよ"



"そう言って向こうを向く。校庭の方を見ようと首を回すけど、実際に見えるほどには回さない。"



mi "わはは～"



label jp_S29y:

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_roof_ss
show mishashort perky_confused_close_ss at center
with locationchange

stop music fadeout 0.5
$ renpy.music.set_volume(0.2, 0.0, channel="sound")
play sound sfx_door_creak


"俺たちの後ろでドアが開く。柔らかな風越しにその音がかろうじて聞き取れる。"

scene bg school_roof_ss at bgleft
show mishashort perky_confused_close_ss at closeleft
with charamove

show shizu behind_blank_ss at tworight
with charaenter


ssh "学校中探したのよ。秘密の打ち合わせか何か？"


"静音はこちらに歩いてくると、呼吸を整えるかのようにミーシャの隣でフェンスに寄りかかり、体を起こしてから話を続ける。"

show shizu basic_normal_ss
with charachange


ssh "二人とも顔を出さないのに、毎日生徒会室で座ってたから飽きちゃった。ちょっとくらい休憩するのはいいけど、これは行き過ぎよ"


"普通ならミーシャと俺が冗談めかして言い訳をするタイミングだ。でも今回は沈黙しかない。いつも抵抗があるのを待ちかまえている静音は、何もないことに意表を突かれる。"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_snap
show shizu adjust_happy_ss
with Dissolve(0.3)


"落ち着かない沈黙が数秒間続いたあと、静音が指を鳴らすけたたましい音でそれが破れる。『エウレカ！』とでも言いたげな笑顔を浮かべている。"


show shizu basic_happy_ss
with charachange


ssh "一緒に何かしましょう"


hi "何をだよ？"

show shizu behind_smile_ss
with charachange


ssh "何でもよ！　まずは生徒会室に行って、そこで考えましょう"


hi "俺たちに仕事させる罠に見えるけどな"

show shizu basic_normal2_ss
with charachange


ssh "バカ言わないの"



label jp_S29ya:

show shizu behind_smile_ss
with charachange


ssh "うそじゃないから。約束する。きっと楽しいわよ"

show mishashort perky_sad_close_ss
with charachange

play music music_rain fadein 4.0


"静音の穏やかな笑顔とは対照的に、ミーシャの表情は寂しげだ。"


"俺が静音を奪ったことでミーシャが本当に嫉妬しているなら、俺たち三人が一緒にいても事態は悪くなるだけだ。開いた傷口に塩を擦り込むようなものだ。なので、二人で一緒に過ごしてもらうことにする。"


"たった一日一緒に過ごすだけで何もかも解決すると考えるほど理想主義ではないけど、何かの足しにはなるかもしれない。一緒に行くよりはましな選択に思える。俺がいたって何の役にも立たないに決まっている。"


hi "二人で楽しんできなよ。俺は早いけど寝るから"


show shizu basic_normal_ss
with charachange


ssh "本気？　まだ昼になったばっかりよ"


hi "言っただろ、今日は調子悪いんだよ。病気にかかりかけてるみたいだ"

show shizu adjust_frown_ss
with charachange


ssh "そういう言い訳はきかないって言ったのはそっちだったと思うけど"


"今のはやられたな。"

show shizu basic_normal2_ss
with charachange


ssh "いいわ。でも人の招待を断るのは失礼よ。こんど埋め合わせてもらうから"

show shizu adjust_happy_ss
with charachange


"静音は振り向いてミーシャに笑いかけ、手話を始めるけど俺には見えない。『私たち二人だけみたいね』とか、そういう内容だろう。"

stop music fadeout 3.0


"よかった。"


stop ambient fadeout 2.0

window hide



label jp_S29yb:

show mishashort hips_grin_close_ss
with charachange

play music music_comfort fadein 5.0



"ミーシャが『わはは』と抑えた笑い声をかろうじて漏らす。今のが静音の目に入らなくてよかった。ミーシャのためというだけじゃなく、ほんとうに。"





show shizu behind_smile_ss
with charachange



ssh "実は考えて欲しいことがあったのよ。ほかに何があるのか。外に食べには行けないし。出前は昨日取っちゃったし、それだけでもルール違反だし。三日連続なんて許されないわ"


show mishashort perky_smile_close_ss
with charachange


mi "でも～！　それは出前でしょ、しっちゃん～！　外に食べに行くのは違うよ"


hi "そうだよ、全然違うぞ"

show shizu adjust_frown_ss
with charachange


ssh "二人とも調子いいんだから"



show shizu basic_normal_close_ss at closeright
with characlose


"俺が答える前に、静音に手をつかまれてしまい、返事ができなくなる。選択肢が大きく狭まった俺は、顔をしかめるくらいしかできることがない。お返しに静音もしかめ面を返すと、ミーシャにも手を伸ばす。"


"ミーシャはその手を取るのをためらうけど、俺は静音と手をつないだままで、できる限り歩み寄って、自分でミーシャの手をとる。"

show mishashort hips_smile_close_ss
with charachange


mi "……ははは"


"笑顔を見せた一秒後、静音はしびれを切らしたように俺たちをドアまで引っ張っていく。人間の鎖のように、手をつないだままで。"

stop ambient fadeout 1.0

scene ev shizu_hands
with locationskip


"危ないけど、校舎の中を進み、ドアを抜けて、校庭を横切る間、誰一人として手を離すことを考えもしない。"


"懐かしい感じがする。前もこうやって歩いたことがあるかのようだ。三人で、手に手を取って。もちろん、その時の雰囲気は今よりもずっと楽しかったけど。"




"悲しみが二人の表情に跡を残しているのが見える。実際、何も変わってなんかいないんじゃないか、と思う。これはただの気晴らしなんじゃないかって。"
"でも、それはこの雰囲気のせいで俺がまたひねくれているだけだと思う。これは始まりなんだ。"





stop music fadeout 3.0

window hide
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
