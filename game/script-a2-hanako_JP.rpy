label jp_H2:

scene bg school_miyagi
show hanako emb_downsmile_close
with None

play sound sfx_doorknock2

show hanako emb_timid_close
with charachange


"俺たちが駒を並べていると、ドアが開く音がする。"

play sound sfx_dooropen

show bg school_miyagi at bgright
show hanako emb_timid_close at tworight
with charamove

show lilly basic_smileclosed at twoleft
with charaenter


li "こんにちは"

play music music_lilly fadein 4.0

show hanako emb_emb_close
with charachange


ha "リリー……"


hi "ああリリー、もう済んだのか？"

show lilly basic_smile at twoleft
with charachange




li "二人ともここにいるんですか？　良かった。何はともあれ、先生が手伝いの人を集めてきてくれたので、抜けてこられました。あれからずっとここに？"







hi "ほとんどね。ちょっとチェスをやっているところだよ"

show hanako emb_smile_close
with charachange


ha "こ……紅茶いる？"

show lilly basic_weaksmile at twoleft
with charachange


li "実は、ちょっと外に出かけてみるのもいいんじゃないかと思ったんですけど……"





show hanako def_worry_close
with charachange


"華子はなにも言わないけど、たちまちその表情が落ち込むのを見れば、リリーの誘いに反対なのは明らかだ。"







"リリーには見えないけど、華子の顔にはっきりと浮かんでいる感情を伝えなくては、という奇妙な衝動に駆られる。"







hi "あー……ここにいたほうがいいんじゃないかって思うな……"




show lilly basic_surprised at twoleft
with charachange


li "そうですか？　ここはとても混んでいるから、学校を出て近くの喫茶店に行った方がいいかと思っていたんです"




show hanako emb_blushtimid_close
with charachange


ha "し、上海のこと？"




show lilly basic_smileclosed
with charachange


li "はい、もちろん。町の人も山久の生徒も、みなさん学園祭に来ているのできっと空いていると思いますよ"






hi "喫茶店？"

show lilly basic_weaksmile
with charachange


li "あら、そうでした。たぶん久夫さんは知らないでしょうね"




show lilly basic_smile
with charachange


li "この近くに私たちが時々行く喫茶店があるんです"


hi "よさそうだな。華子、どう思う？"

show hanako defarms_shock_close
with Dissolve(0.2)

show hanako def_worry_close
with charachange



"話を振られて華子が少し飛び上がる。だけど少なくともさっきよりはうろたえていないようだ。"






show hanako cover_bashful_close
with charachange


ha "し……上海ならいいかな"

show lilly basic_planned
with charachange


li "では決まりですね。行きましょうか"

show hanako basic_bashful
with charadistant


"華子と俺はチェスをやめ、テーブルから立ち上がる。"


"俺がなにかしようとするまえに、華子が駒を小さな入れ物に流し込むように入れて、盤を片付けてしまう。"




hi "準備はできたな。じゃあ案内してよ"

stop music fadeout 8.0

scene bg school_hallway3
with locationchange

show hanako emb_smile at Transform(xanchor=0.5, xpos=0.58)
show lilly basic_smileclosed at Transform(xanchor=0.5, xpos=0.42)
with charaenter


"華子がリリーの隣に移動し、俺たちは廊下へと冒険の旅に漕ぎ出す。"





$ renpy.music.set_volume(0.2, 0.0, channel="ambient")

play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_gate_ss
with locationskip



"二人は見覚えのないいくつものドアを通って俺を先導し、学園祭が行われているグラウンドの反対側の建物の脇へと出た。"




"建物の重い石材に遮られ、人混みの喧騒はざわめき程度の大きさにしか聞こえない。"


hi "変だな、みんなもう帰り始めているだろうと思ったけど……"




show hanako emb_downtimid_ss at Transform(xanchor=0.5, xpos=0.58)
show lilly basic_smile_ss at Transform(xanchor=0.5, xpos=0.42)
with charaenter


li "あの方々はたぶん花火を見るためにここにいるんでしょう"



hi "花火？"

show lilly basic_weaksmile_ss
with charachange



li "はい、どうやら学校が盛大なショーをするらしいですよ。花火を見るためだけに、街から大勢の人が来るんです"








"リリーが学校を出ると決めた理由が今理解できた。町全体の人が学校になだれ込んでくれば、華子にとっては辛いことだろう。この場合『逆流してくる』が正しいかもしれないけど。"









stop ambient fadeout 7.0
play music music_tranquil fadein 3.0

scene bg school_road_ss
with locationchange



"リリーと一緒にこの道を下るのは山久に来てから２回目だ。"




"今になって絶え間ない学園祭の騒音がかすかに聞こえてきて、やっとその騒々しさに気がつく。昼間の音の攻撃から耳が回復してくるとともに、静かな夕方の空気の中で、わずかに耳なりが聞こえる。"





show hanako emb_emb_ss at Transform(xanchor=0.5, xpos=0.58)
show lilly basic_smileclosed_ss at Transform(xanchor=0.5, xpos=0.42)
with charaenter



"華子はリリーにぴったりとくっつきながらも道に従ってリリーのガイドを務めている。それに加えて歩行者からの好奇の視線を避けているうちに、彼女から活気がすっかり失われていく。"








"華子はめったに地面から顔を上げず、一言もしゃべらない。"





"一方でリリーはまさに学校にいるときのように礼儀正しく上品な外見を崩さないでいる。華子のように隠すのではなく、あえて自分の見た目を保つよう努めているのは明らかだ。"






"学校の外での二人の振る舞いがこんなに違うことに驚く。とはいっても、どちらの振る舞いも明らかに目に見えて変わっている。"






$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

window hide

nvl clear

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl show dissolve


n "\n\n\n山久学園ではみんなが『特別』で、それは『特別』であることの『特別さ』を打ち消している。"




n "だけど一度校門の外に踏み出せば、俺たちは『部外者』という身分に、ひとくくりにされるような肩書きに戻ってしまう。"









n "制服を着たままの時はなおさらだ。『どこが悪いか当ててみな』という看板を首にぶら下げているようなものだ。"




n "制服を着たままの生徒がこんなにたくさんいることに驚く。でも山久の生徒にとって杖や車椅子が珍しくないことを考えれば、制服くらい大したことではないのかもしれない。"







n "\nそれとも、これを不名誉な代物として見ているのはもしかして俺だけなのか？　しばらくすれば他の学校の制服のように慣れるのだろうか。"





nvl hide dissolve

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

scene bg suburb_shanghaiext_ss
with locationskip

window show


"案内された喫茶店は外から見る分には極めて普通のようだ。よくありがちな感じの看板で入口が装飾された平凡な建物である。"


"それは何の気なしに通り過ぎるであろう場所、どこにでもありそうな普通のカフェでしかない。"





"もし華子がリリーを入口の中へと導いていなければ、俺は建物の存在にすら気づかずに道を下っていただろう。"

play sound sfx_storebell

scene bg suburb_shanghaiint at Fullpan(5.0, dir="right")
with locationchange

stop music fadeout 6.0


"喫茶店の中は昔ながらな感じが漂っている。カウンターや座席から壁際の高い仕切りで仕切られた席まで、店の中にあるもの全てが同じ木材から作られているようだ。"






"だけどこの部屋の最も印象的な特徴は、人のいる感じがしないことだ。裏のほうでなにかが沸騰している音がかすかに聞こえる気がするけど、それ以外は無音だ。"




"どうするわけでもなく、俺たちは礼儀正しく『席に座らずにお待ちください』という看板に従いつつ入口付近でただ待つ。"


hi "あれ、やってないのかな？"

stop music
play sound sfx_impact2

show yuukoshang panic_up:
    xalign 0.5 yanchor 1.0 ypos 1.5 alpha 0.0
    easein 0.3 ypos 1.0 alpha 1.0
show bg suburb_shanghaiint at right
with vpunch


"椅子が倒れる音が誰もいない部屋に響き、仕切り席の中から頭が飛び出す。"


play music music_comedy fadein 0.5

show yuukoshang neurotic_up:
    ypos 1.0 alpha 1.0
with charachange


yu "ねっ寝てないですよ、いらっしゃいませ！"



"パステルカラーのエプロンを着てメニューを握りしめた優子さんが、もの凄い勢いで俺たちを出迎える。彼女のズレた眼鏡と乱れた髪の毛がさっきの言葉への疑いを呼び起こす。"







"しかし彼女が居眠りをしていたかどうか以上に気になることがある。"


hi "ここで働いているんですか？　図書室はどうしたんです？"


show yuukoshang smile_down
with charachange


yu "えっ？　リリー？　中井くん？"

show yuukoshang neurotic_up
with charachange


yu "ようこそ、上海へ！"

show yuukoshang noglasses_up at Transform(ypos=1.25)
with Dissolvemove(0.2)

play sound sfx_dropglasses

with Pause(0.3)

show yuukoshang noglasses_up at center
with charamove


"まだ半分寝ている優子さんが急に荒っぽいおじぎをすると、彼女の眼鏡が落っこちてしまう。"


yu "うひゃぁ！？　私の眼鏡……"


"俺が床から眼鏡を拾ってあげると、リリーが説明してくれる。"



show yuukoshang noglasses_up at tworight
show bg suburb_shanghaiint at center
with charamove

show lilly basic_weaksmile at twoleft
with charaenter


li "優子さんは図書室と同じようにここでアルバイトをされているんです。私たちがここに来るのが好きな理由の一つですね"



show yuukoshang neurotic_up
with charachange


"優子さんは俺から眼鏡を受け取り、おぼつかない手つきでかけ直す。"


yu "うん……そう……ありがとう……"



show yuukoshang neutral_down
with charachange


yu "テーブルまで案内しましょうか？"

show yuukoshang worried_up
with charachange


yu "他に誰もいないから、好きなところに座ってなんでも注文してね。私が作らないといけないから遅くなっちゃうかもしれないけど……"

show lilly basic_smile at twoleft
with charaenter


li "大丈夫です、優子さん。紅茶とサンドイッチでいいです"


show yuukoshang happy_down
with charachange


yu "それだわ！　すぐに作るね！"




hide yuukoshang
with charaexit

show lilly basic_smile at center
show bg suburb_shanghaiint at bgright
with charamove


"優子さんは入口に突っ立っている俺たちを残して厨房へと消えていく。"


"彼女は厨房のドアを開けたところで俺たちをまだ席へ案内していないことに気づく。"


yu "ごめん、ごめんね！　どこでも好きなところに座って！　すぐに戻ってくるから！"

stop music fadeout 3.0

hide lilly
with charaexit

show bg suburb_shanghaiint at bgleft
with charamove


"彼女に促され、俺はリリーを一番近い仕切り席へと連れて行き、それに華子も続く。"

show lilly basic_smileclosed:
    twoleft
    ease 1.0 ypos 1.2
show hanako basic_normal:
    tworight
    ease 1.0 ypos 1.17
with Dissolve(1.0)


"リリーの隣に腰を下ろすと、俺はこの場所がどれだけ華子に適しているかということを実感する。"


"背の高い仕切りを持つ仕切り席は、店の他の場所から完全に隔たっていて、加えてそんなに多くの客が入れるようにも見えない。"


"座席の上のクッションから調味料入れまで全ての家具が旧式に見えるけど、そこまで古臭い感じはしない。"


"リリーは華子を連れてくるためにあえてこのような場所を選ぶのだろうか？　彼女は華子の置かれた独特な苦境に合う条件を満たすためならどんな苦労もいとわない人間のようだ。"



play music music_another fadein 4.0

show lilly basic_weaksmile:
    ypos 1.2
with charachange


li "そういえば、久夫さん。あなたがチェスをやっていたなんて知りませんでした……"


hi "ああ、上手くはないけどね。やり方くらいは知ってるよ"

show lilly basic_smile
with charachange


li "ありきたりの質問でしょうけど……どちらが勝ったんですか？"


"リリーの無邪気な微笑みを見て、俺は口ごもってしまう。華子に勝ちを自慢するようには見られたくない。"

show hanako cover_bashful:
    ypos 1.17
with charachange


ha "ひ……久夫くん"



hi "うん……まあ、なんとかね……"





"なにやってんだ。声に出すと同時に俺は後悔の念に駆られる。"

show lilly basic_giggle
with charachange


li "やりましたね、久夫さん。あなたは私が未だにできないことを成し遂げてしまいました"




hi "えっと、ありがとう。長いあいだやってなかったから、またできてよかったよ"


show hanako basic_smile
with charachange


ha "う……うん……そうだね"


"華子は目を合わさずに髪をいじくりながら答える。しかしその顔にはわずかに笑みが浮かんでいる。"


"それは俺の予想をはるかに超えた反応だったけど、華子らしくてなんだかかわいいと思えてくる。"






show hanako defarms_shock at Transform(xpos=0.8)
show lilly basic_surprised at Transform(xpos=0.2)
with Dissolvemove(0.5)

show yuukoshang worried_up at center
with charaenter


"俺がそんな華子の反応に不意を打たれていると、大変動が起こるかのような優子さんの再登場によって会話へと引き戻される。"








hi "大丈夫ですか？　優子さん。手伝いましょうか？"

show yuukoshang neurotic_up
show hanako def_worry
with charachange


yu "大丈夫、大丈夫よっ大丈夫っっ……私の仕事なんだからちゃんと自分でやらないと……"






show yuukoshang worried_up
with charachange


"手に持っているトレイを睨みつける彼女の顔には、トレイの中身を凝視すれば中身はその場に留まるだろうというかのように集中している表情が浮かんでいる。"

show yuukoshang worried_up at centertremble
with charachange


"悲しいかな、そんな効果はあるはずもなく、カップとソーサーが時折互いにぶつかってカタカタと音を立てながらゆっくりと跳ね回る。"






show yuukoshang worried_up at Transform(ypos=1.1)
with ease

show yuukoshang worried_up at center
with ease


"細心の注意を払いながら、優子さんがほとんど音を立てずにトレイをテーブルに置く。"

show yuukoshang happy_down
with charachange



yu "ほら、できた！"




hi "えっと、よくできました……でいいのかな？"

show lilly basic_weaksmile
with charachange


li "ありがとうございます、優子さん"

show yuukoshang neutral_down at Transform(ypos=1.2)
with Dissolvemove(0.2)

with Pause(0.2)

show yuukoshang neutral_down at center
with ease


"優子さんは頭を思いっきり振りおろす特徴的なおじぎをしてから返事をする。"

show yuukoshang closedhappy_down
with charachange


yu "どういたしましてっ！！"






show lilly basic_smile
with charachange


li "よければ優子さんもご一緒にどうですか？　この前の発注について、他にも相談したいことがあるんですが……"






"ああ、そうだ。俺が初めて華子に会ったときにリリーと優子さんはたくさんの本について話し合っていたっけ。"



"点字の本のことでリリーが手伝う、とかなんとか……"






show yuukoshang neurotic_up
with charachange


yu "あー……うん。話す機会がなかったね"

show yuukoshang neurotic_up at Transform(ypos=1.17)
with charamove


"優子さんは慌てて華子の隣に座る。"


"どうやら優子さんの仕事熱心さは、集中力が残っている間しか続かないようだ。集中が途切れると、仕事も放り出してしまう。"







show yuukoshang smile_down
with charachange


yu "また話をするんだったら、明日の午後は図書室にいるけど……"





show lilly basic_cheerful
with charachange



li "ちょうどいいですね。授業が終わったら伺います"



show hanako emb_timid
with charachange


ha "あの……り、リリー……"

show lilly basic_oops
with charachange


li "あら、そうでした。明日は月曜日でしたね。どうして忘れてたんでしょう"


"なんだか会話に置いて行かれている気がしてくる。とはいっても、当たり前だ。ここに来てからまだ間もないのだから、全ての人の予定を知ることなんて不可能だ。"



show lilly basic_weaksmile
with charachange


li "そうですね、他の日に図書室に行くという選択肢もありますからね"


show lilly basic_smile
with charachange


li "優子さん、今週中は図書室にいますか？"


show yuukoshang worried_up
with charachange


yu "うーん……たぶん、でももう先延ばしにするのは厳しいかも……"

show hanako emb_downsad
with charachange


ha "わ、私も……どうしても必要なものが……あって……"



show lilly basic_listen
with charachange


li "これは困りましたね……"




"リリーは少しのあいだ考えを巡らせ、答えを見つける。"

show lilly basic_planned
with charachange


li "できたら、残りのお一方の助けを借りられないでしょうか？"






hi "えっ、何をするって？　ずいぶん前から話について行ってないんだけど……"





"状況がさっぱりわからない状態でなにか手伝わされる、というのはあまり気に入らない。"






"こっちはやっとのことで生徒会の魔の手と、あいつらの度重なる勧誘から逃れられたと思っていたのに。"




show lilly basic_smileclosed
with charachange



li "ああ、そうでした。先日、優子さんの手伝いで、図書室の点字本の整理をしていたんです"



show lilly basic_weaksmile
with charachange


li "でも華ちゃんと私は月曜日の午後はいつもお買いものに出かけるんです。そのほうが週末よりも混んでいないんですよ"




li "先週は私が学園祭の準備で忙しかったので行けなかったんです。その後なら時間を作ることができたので日を改めようとしたのですが、先週中はそれ以降華ちゃんの予定が合わなくて"




hi "なるほど。俺は点字は読めないから、華子と買いものに行ってほしいってこと？"

show lilly basic_smile
show hanako emb_timid
with charachange


li "はい。先日はとても助かりましたし"


hi "俺は大丈夫だと思うよ。華子はどう？"




show hanako basic_smile
with charachange


ha "ひ、久夫くんが嫌じゃなければ……"




hi "もちろん嫌じゃないよ。俺はまだこの地域の店に詳しくないからいいアイディアだと思う"


show hanako basic_bashful
with charachange


ha "わ、わかった"

show lilly basic_smileclosed
with charachange


li "決まりですね。紅茶、飲みませんか？"


"先ほど出された紅茶が口をつけられないままで冷えてしまっていることに今気づく。"

show yuukoshang panic_up
with charachange


yu "私のせいだ！　もう一回入れさせて……"


"優子さんが手を小刻みに震わせながら伸ばしてくる。しかし俺はこれを遮る。今の彼女は熱い液体を扱える状態にあるようには見えない。"







hi "大丈夫ですよ、僕がやりますから。あなたは紅茶を入れてサンドイッチを作ってくれました。これでもうウェイトレスとしての義務は果たしたでしょう？　ね？"




show yuukoshang neurotic_up
with charachange


yu "そ……そうね"


"優子さんは少しは落ち着いたけど、俺が料理を各々に振り分けているあいだ、まだ熱心な眼差しを注いでくる。"

stop music fadeout 1.0
play ambient sfx_fireworks

show white
with Dissolve(0.1)

hide white
show fireshine
show hanako defarms_shock
show yuukoshang panic_up
show lilly basic_surprised
with charachange


"俺がサンドイッチにかぶりつこうとしたとき、低く大きなドーンという音が聞こえ、ほぼ同時に外から閃光が差し込む。"




show lilly basic_weaksmile
show yuukoshang smile_down
show hanako emb_timid
with charachange


li "あら、始まりましたね"



hide fireshine
show bg misc_sky_ni as front
show fireworks
with locationchange





"外を見てやっと気づいたけど、太陽はとっくに沈んでしまっていて、夕焼けの薄明かりだけが残っている。"









"閃光を放つ火の玉が花の形に爆発しようと天に昇っていく。"

hide fireworks
hide front
show fireshine
show yuukoshang happy_down
with locationchange


yu "見に行こうよ！"

show yuukoshang panic_up
with charachange


yu "あ……ごめんなさい、リリー……"

show lilly basic_ara
with charachange

show hanako_fw behind bg:
    truecenter zoom 1.05 subpixel True
    ease 22.0 zoom 1.0
show ev hanako_shanghaiwindow behind hanako_fw:
    truecenter zoom 1.05 subpixel True
    ease 22.0 zoom 1.0
with None


li "私にはかまわないで見てきてください。音を聞いた限り、ここは花火を見るには悪くない場所のようですね"




play music music_serene fadein 4.0

hide fireshine
hide bg
hide hanako
hide lilly
hide yuukoshang
with locationskip


"リリーを除いた三人は花火を見るために小さな喫茶店の窓に駆け寄る。"


"様々な色の光が華子と優子さんの笑顔のあちこちで揺れ動ているのを見て、少しのあいだ俺は窓の外を見ることを忘れてしまう。"


"こんなまったく新しい世界でも、変わらないものが少しはある。"




"それが山久学園が学園祭でこんなお祭り騒ぎを起こす理由なんだと思う。この笑顔のように誰にでも似通ったところがある、ということを示す機会なんだ。"




stop ambient fadeout 3.0

hide hanako_fw
with Dissolve(1.0)


"ショーはあっという間に終わってしまう。もっとも潤沢な予算がある学校にとっても、花火というのは高価なものなのだ。"





scene bg suburb_shanghaiint at bgright
with locationchange


"食事に戻るまえに華子がこちらを向く。"

show hanako emb_downsmile_close
with charaenter


ha "き、きょうはありがとう"

show hanako emb_smile_close
with charachange


ha "……それと、明日も……"




hi "いいって。俺もあの人混みには耐えられなかったと思うし"





hi "今日みたいにみんなから離れて過ごすのって落ち着くよな。そう思わない？"



show hanako basic_normal_close
with charachange


ha "う、うん"



hi "ところで、ずいぶんと紅茶をほったらかしてるし、戻ろうか"



show hanako basic_bashful_close
with charachange


ha "そ、そうだね"

stop music fadeout 6.0

hide hanako
with charaexit

show bg suburb_shanghaiint at bgleft
with charamove

show lilly basic_smileclosed:
    yanchor 1.0 xanchor 0.5 ypos 1.2 xpos 0.2
show yuukoshang neutral_down:
    yanchor 1.0 xanchor 0.5 ypos 1.17 xpos 0.5
with locationchange

show hanako basic_smile:
    yanchor 1.0 xanchor 0.5 ypos 1.0 xpos 0.8
    easein 1.0 ypos 1.17
with charaenter


"俺たちは席に戻り、食事を再開する。"



show lilly basic_smile
with charachange


li "あの音は印象的ですね。少なくとも去年よりも大きいです"




show yuukoshang happy_down
with charachange


yu "うん！　すごかったね！　こんなショー見たことないよ"






yu "年を重ねるごとに良くなってる！"

show lilly basic_weaksmile
with charachange


li "ですが、見ているあいだに紅茶がまた冷えてしまったみたいです"



show yuukoshang panic_up at center
with Dissolvemove(0.2)

play music music_ease fadein 0.5


yu "やだ！　もう一度作らせて！　私のせいだわ！"


hi "落ち着いてください、優子さん。誰のせいでもないですよ"


"俺はそれを証明するために自分のカップを一口すする。"


hi "とにかく、この紅茶、冷たくてもまあまあおいしいですから。アイスティーみたいで"





show yuukoshang worried_up
with charachange


yu "本当？"


hi "はい、本当です。砂糖を少し入れればいい感じですね"

show yuukoshang neurotic_up
with charachange


yu "本当に本当？"


hi "本当ですって。座って一緒に食べませんか？"

show yuukoshang smile_down
with charachange


yu "う、うん"

show yuukoshang smile_down at Transform(ypos=1.17)
with charamove


"優子さんは疑っているようだけど、とりあえず腰を下ろす。"



"彼女は注意深くティースプーン五杯分の砂糖を測り取り、紅茶に入れる。"


hi "あのー、俺は少しって言ったはずですけど……"

show yuukoshang neutral_down
with charachange


yu "わかってるよ。でも私は甘いほうが好きなの"


"興味をそそられて、優子さんのカップをのぞき込む。案の定、冷たい液体の中では砂糖はほとんど溶けていない。"





"彼女は二回ほどかき混ぜるとカップを傾け、溶け残っている砂糖まで一口で飲み干してしまう。"



show yuukoshang happy_down
with charachange


yu "本当だ！　すごくおいしいわ！"




hi "えっと……それは良かったですね"


"リリーと華子に視線を戻す。二人とも俺が優子さんの個性的な行動を見ているあいだに食事を終えてしまったようだ。"


"みんなを待たせたくないので、俺は優子さんと同じように紅茶の残りを一息に飲み干す。"





hi "さて、みんな食べ終わったみたいだな"




show lilly basic_smile
with charachange


li "帰りますか？　それともおかわりをいただきましょうか？"




show yuukoshang neurotic_up
with charachange


"優子さんの表情を見るに、間違いなくそれはやめておいたほうがよさそうだ。"





hi "すぐ帰るのが一番良いんじゃないかな"


hi "やっぱり、門限までには帰らないといけないし"

show lilly basic_smileclosed
with charachange


li "あ、それは大事ですね"

show lilly basic_smile
with charachange


li "また明日お会いしましょう、優子さん"

show yuukoshang neutral_down
with charachange


yu "うん待ってるね、リリー。じゃあね、みんな"

stop music fadeout 9.0

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_cicadas fadein 0.5

scene bg suburb_shanghaiext_ni
with locationchange


"俺たちは小さな喫茶店から出て夜の闇へと進んでいく。"

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")
scene bg suburb_roadcenter_ni
with locationchange


"リリーと華子はまた先頭に立つ。でも宵闇の中では、華子はここにくるときと比べてほんの少しだけ気が楽そうに見える。"







"時折、学校のグラウンドから出てきた人たちの集団に出会いながら進む。しかし華子は大規模な人混みを避けるために裏道を案内しているようだ。"

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_dormext_full_ni
with locationskip


"寮の前まで来ると、学校が昼間の喧騒に比べて奇妙なほど静まり返っているように感じられる。"


hi "さて、二人とも今日はありがとう。色々わかった気がするよ"

show hanako emb_timid_ni at Transform(xanchor=0.5, xpos=0.59)
show lilly basic_weaksmile_ni at Transform(xanchor=0.5, xpos=0.41)
with charaenter


li "どういたしまして。でももう帰らないと。今日は長い一日でしたから"





"そうだった。リリーは一日ずっと立ちっぱなしだったし、学校の外に出ることでとても疲れただろうことも想像がつく。"





"今朝十時ごろに起きた人間はたぶん自分だけだろうということを思い起こし、俺は罪悪感に駆られる。"


hi "確かに"


hi "じゃあ、また明日な。おやすみ"

show lilly basic_cheerful_ni
with charachange


li "おやすみなさい、久夫さん"


show hanako basic_smile_ni
with charachange


ha "お……おやすみ"

hide hanako
hide lilly
with charaexit


"二人は寮へと戻っていき、俺も自分の寮へと帰る。"


"……確かに、考えてみると今日は俺も疲れたな。"

stop ambient fadeout 2.0

scene black
with dissolve


label jp_H3:

window hide None

scene black
with dissolve

$ renpy.music.set_volume(0.0, 0.0, channel="ambient")
play sound sfx_alarmclock

with Pause(1.2)

play sound sfx_impact2

window show


"目覚ましの音が耳に鳴り響く。それを自分の拳で直ちに黙らせる。"




scene bg school_dormhisao
with openeye


"俺の体は自動運転に切り替わり、ぼやけた意識のままベッドから這い出すと、制服に着替える。"








"いつものように薬の瓶が机の上に鎮座し、俺が瓶を手に取り１日の服用量として決められている１７錠の錠剤を取り出すのを待っている。"








scene bg school_scienceroom at bgright
with locationskip


"気がつくと俺は３－３のドアを開けている。学園祭週間の疲れが残っている人間が自分だけではないということがわかり嬉しくなる。"







"教室の中にある顔はみんな寂しい感じだ。学園祭が終わって、まるで一生の夢を達成してしまったかのようだ。"



"学園祭という学校生活の中での生き甲斐がなくなり、生徒たちは授業に出るという本能だけを頼りに教室にやってきている。"





"ただの深読みかもしれないけどな。"



"俺はゆっくりと自分の席に向かうが、ようやくその時、なぜ教室がこんなに静かであるかがわかる。"





"ありがたいことに、俺の隣の席には誰も座っていない。世界で一番うるさい手話通訳者はまだお着きになっていないようだ。"




play sound sfx_doorslam
play music music_running

show misha hips_grin:
    yalign 1.0 xanchor 0.0 xpos 1.0
    easein 0.3 xanchor 1.0
with vpunch




"俺が腰を下ろそうとしたまさにそのとき、ドアが飛ぶような速度で開き、まばゆく輝くミーシャの姿が現れる。劇的な登場で髪のドリルをピョンピョンと縦に揺らし、両腕を天へと突き出しながら。"






show misha hips_laugh at right
with charachange



mi "いやっほーう！　終わったねー！"



"みんながみんな、学園祭の後の憂鬱に苦しんでいるわけではないみたいだ。"





"他の生徒全員がミーシャをにらみつける。明らかにみんな俺と同じことを考えているな。"



show misha sign_confused
with charachange


"いまだ腕を上へと伸ばした姿勢で教室の入り口で固まったままのミーシャが、心配そうに辺りを見回す。"





"このいやな雰囲気を感じ取っているのは間違いないけど、どうしていいのかわからないでいる。"




show misha sign_confused at center
with ease_decel


"突然、ミーシャが前へとつんのめる。"




show misha perky_sad
with charachange


mi "あっ！"



show shizu invis behind misha:
    yalign 1.0 xanchor 0.5 xpos 1.0
with None

show misha perky_sad at twoleft
show bg school_scienceroom at center
show shizu adjust_happy at tworight
with dissolvecharamove


"ミーシャが教室の中へとよろめき、静音の姿が現れる。その腕はミーシャを教室に押し込んだために伸ばされているままだ。"




show shizu basic_normal
with charachange


shi "……"


hi "余興をありがとう。でも、二人とも席に着いたほうがいいんじゃないのか？"





show shizu behind_frown
with charachange


shi "……"


"まだわずかに混乱しているミーシャは、一拍置いて自分が通訳しなければいけないことに気づく。"






show misha sign_smile
with charachange


mi "そうだよ！　先週ひっちゃんがばっくれたから怒ってる、ってしっちゃんが言ってるよ"





show misha cross_frown
with charachange


mi "本当に忙しかったんだから！"



hi "そうかよ。俺が二人のために資材を探してやったのはどうなったんだ？"








show shizu cross_angry
with charachange


shi "……"

show misha hips_grin
with charachange


mi "生徒会のメンバーじゃなきゃカウントしない、って言ってるよ。ひっちゃんは入会しなかったから、しっちゃんとは何の貸し借りもないの"




show misha hips_grin_close
with characlose



"ミーシャが俺に近寄ってきて、陰謀を告げるかのように俺に耳打ちしてくる。"





mi "本当はね、しっちゃんは学園祭でひっちゃんが一緒にいてあげなかったからちょっと不機嫌なだけだと思うよ"





show misha hips_smile_close
with charachange


mi "あんなこと言ってるけど、しっちゃんはひっちゃんが先週手伝ってくれたことに本当に感謝してるんだからね"

show shizu behind_frustrated
with charachange


"自分のことを言われていると気がついたのか、静音はミーシャが自分のほうに顔を向けるまで机を指で叩き続ける。"





show misha sign_smile
with charadistant

show shizu basic_angry
with charachange

show misha hips_grin
with charachange

show shizu adjust_blush
with charachange


"静音とミーシャのあいだで交わされているペースの速い手話は俺には理解できないけど、静音のわずかに恥ずかしがった表情とミーシャのこらえきれていない笑いからその内容は想像できる。"


stop music fadeout 8.0


"そうしている間にドアが再び開く。さっきに比べれば、開く速度はずっとまともだ。"






show hanako invis at offscreenright
with None

show bg school_scienceroom at bgleft
show shizu basic_normal at Transform(xpos=0.42)
show misha hips_smile at Transform(xpos=0.18)
show hanako emb_downtimid at right
with dissolvecharamove


"華子が静かに部屋に入ってきて、後ろ手でドアを閉める。"



show hanako emb_timid
with charachange


"華子は髪の下から素早く教室を見渡した。"




"俺と視線が合うと華子は身体をこわばらせる。そして瞳を閉じて深呼吸を一度してから、俺の机のほうへ歩いてくる。"



show hanako cover_distant
with charachange



ha "お……おはよう、久夫くん"





hi "おはよう華子。今日は少し遅いんだな"

show hanako basic_normal
with charachange


ha "り……リリーと話してたから"

show hanako basic_worry
with charachange


ha "き、今日のことで"


hi "ああ、じゃあもうリリーから買い物リストはもらってきたんだね？　それなら授業が終わったらまっすぐ行けるな"








show hanako emb_smile
with charachange


ha "そ、そうだね"



hi "楽しみにしてるよ"


"華子は恥ずかしそうな笑みを一瞬浮かべ、慌てて自分の席のほうへ行ってしまう。"

scene bg school_scienceroom at bgright
with shorttimeskip

play music music_normal fadein 3.0


"授業になって、学園祭の後に意気消沈しているのは生徒だけではないことがわかる。"


"武藤先生は教科書の課題をいくつか俺たちに出しただけで、教卓の後ろに座ってしまう。"





"あまりに一日が平凡なので、一瞬とはいえ短い昼休みのことまで完全に忘れてしまう。"





play sound sfx_normalbell


"退屈でつまらない一日が過ぎる。授業の終わりを告げるチャイムが鳴り、みんな驚いているようだ。"




show shizu basic_normal at tworight
show misha perky_smile at twoleft
with charaenter


"かばんに勉強道具を詰めていると、静音とミーシャが俺を両脇から捕まえる。"



show misha hips_grin
with charachange


mi "ねぇ、ひっちゃん。生徒会に入るの、今ならまだ遅くないよ。書かなきゃいけない学園祭の書類がたくさんあって……"


hi "あー悪いなミーシャ、その……今日はもう予定が…………"

show hanako invis at offscreenright
with None

show bg school_scienceroom at center
show shizu basic_normal at Transform(xpos=0.42)
show misha hips_grin at Transform(xpos=0.18)
show hanako cover_distant at right
with dissolvecharamove



"そんな合図の意味を理解するかのように、小さなかばんを持った華子が俺の後ろで外界の誰とも目を合わせないようにしながら立っている。"



show misha cross_laugh
with charachange


"ミーシャは目を大きく見開き、どっと笑いだす。"


mi "ぶわっはっは！　行動がお早いようで、ねぇひっちゃん～？　デートの邪魔なんていたしませんよ！　ぶわっはっはっは！"



show shizu behind_blank
with charachange


"爆笑しているミーシャの後ろで、静音が全く興味なさげにしている。俺の思い違いかもしれないけど、静音はわざと俺を無視しているように感じる。"

show hanako emb_downtimid_close
with characlose


"シャツが控えめに引っ張られるのを感じ、俺は床に視線をしっかりと固定したままの華子の目を見るために振り返る。"


show hanako emb_timid_close
with charachange


ha "い……いこう……"


hi "わかった。静音、ミーシャ、またな"


hi "それから、やっぱり生徒会には興味ないから"



show misha cross_grin
with charachange


mi "つまんないの"

stop music fadeout 2.0

hide misha
hide shizu
with charaexit

show bg school_scienceroom at bgleft
show hanako emb_timid_close at center
with charamove


"ミーシャと静音は楽しそうに手話を交わしながら廊下へ出ていく。"




hi "忘れ物はないな？　じゃあ行くか"



play music music_soothing fadein 4.0

scene bg school_gate
with locationskip


"生徒たちの大群が校門をくぐり、町へと向かう道へ流れ出ていく。"


"ちょっと変な感じだ。この光景は他の高校とほとんど変わらない。しかしときたま目に映る車椅子や手足を欠損した生徒がそんな幻想をかき消す。"




"１つ気づいたのは、誰一人として一人きりの人間がいないことだ。"





scene bg school_road
with locationchange

show hanako emb_downsad_close at center
with charaenter


"そして華子と一緒に校門をくぐったとき、華子が俺との距離を縮めていることに気づく。"


"『近づいている』と言えるほどその距離が縮まっているとは思わないけど、いつものちょっと身を引いた距離と違うのは確かだ。"


"華子がリリーと親密なほどには、俺と華子の仲は親しくなっていないんだろう。"







"でも、華子が物理的に俺に少し近づいたとしたら、精神的には１キロ近づいているようなものだろう。"







"かばんの革紐をつかむ華子の手は、真っ白になるほど強く握られていて、頭も下を向いて口を閉じたままだ。"







"まるで初めて校長室に行かされているかのように見える。"






"俺はこんな考えに吹き出してしまいそうになるのをこらえようとするが、その努力は無駄になった。"




show hanako emb_timid_close
with charachange


ha "ど、どうかしたの……？"



"隠してもしかたないか……"




hi "ごめんごめん。ちょっと叱られに行く子どもみたいに見えたからさ"




show hanako defarms_strain_close
with charachange


ha "ど、ど、どういうこと？"


hi "もう少しリラックスしたほうがいいと思うんだよね。そんなに遠くに行くわけじゃないんだし、周りには山久の生徒しかいないんだからさ。な？"



show hanako def_worry_close
with charachange


ha "そ、そうだね"


"こんなに華子が取り乱しているのを見ると、ちょっと心配になる。"





hi "毎週こうして買いものに行っているんだってな"

show hanako basic_worry_close
with charachange


ha "う、うん。リリーと"


"そうだった。『リリーと』だった。華子はリリーの付き添いなしで学校から出たことはあるんだろうか？"




"一見しただけでは大したことはなさそうだけど、華子のリリーへの依存は途方もなく大きい。"





"もしリリーがいないと学校の外にさえ出られないのだとしたら、リリーと出会っていなかったらどうやって生きてこられたのだろうか？"




"しがみつく人間を他に見つけていただろうか？　そして、華子をリリーに引き寄せたものはなんだろう？"



"目が見えなかったことか？　それともリリーが色々手を貸してくれる親切な人間だったからか？"


"この条件に当てはまる人間は他にいないんじゃないか？"





hi "その、なんだ。今日は俺がいるし。それに遠くに行くわけじゃないんだから、気づいたら終わってるって"


show hanako emb_downsmile_close
with charachange


"華子の拳が徐々にその色を取り戻すのと同時に、彼女は小さな微笑みを隠そうとする。だけどその努力がこれ以上会話が続くことを妨げているように感じられる。"





"俺たちは町へと続く曲がりくねった道を並んで下っていく。歩道を進んでいくと生徒の集団が小さくなっていく。"


"足の速い生徒たちが前へとどんどん突き進み、ゆっくり進む生徒を追い抜いて行くことで集団は分散していき、やがて『集団』とは呼べなくなる。"


scene bg suburb_konbiniext
with locationskip


"俺たちがコンビニに着くころにはほとんど二人だけになる。"

scene bg suburb_konbiniint
with locationchange


"華子は俺を店員とのあいだを隔てる壁にして、カゴに商品を入れながら細い通路を進んでいく。"





"パン、牛乳、紅茶……タイム？"


"ハーブを売ってるコンビニって、なんだそれ。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear

nvl show dissolve


n "\n\nとはいったものの、思い返してみるとこの町に『普通な』ところなどないようだけど、それは悪い意味のものじゃない。"



n "あらゆるものがあまりに違っていて落ち着かない。だからそんなことをくよくよ考えているのはあまりいい選択肢じゃない。"






n "なんて思考をめぐらせていると、華子のことが頭に浮かぶ。"



n "どうしたって華子の傷跡からは逃げることはできない。俺も目に入るとまだ気を取られてしまう。"



n "認めたくないけど、俺は彼女の傷を無理やり無視しようとしているのだと思う。"





n "かといって、俺だって傷なしっていうわけじゃない。胸の上にギザギザに走る手術跡が完全になくなることは決してない。"




n "だけど俺の場合は簡単にそれを隠すことができる。華子に比べると贅沢なことだ。"



n "\nでもある意味では、俺と華子の傷跡は俺たちがみんな理由があってこの場所にいるんだということを思い出させてくれる。"






$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

window show


"……"


"華子は買い物リストに残った最後の一品をカゴへ入れ、数枚のお札と一緒におずおずと俺に差し出す。"





show hanako emb_downtimid_close at center
with charaenter


ha "あ、あ、あの、これ、お願い……"





"華子が言いたいことを理解するのに少し時間がかかる。"


hi "ああ、会計してほしいってことか？"

show hanako emb_downsad_close
with charachange



"華子はうなずくけど、顔を上げない。"



"いつもならこれはリリーの役目なんだな。"


hi "もちろんいいよ。ちょっとだけ待ってて、俺もまだ少し買うから……"






"自分用に生活必需品を急いで数個つかむと、後ろに華子を連れてレジへと向かう。"





"店員は無関心な会釈をして、品物をスキャンする。"








"俺たちを無視するというのは、山久の特殊さに対処する１つの方法なんだろう。学校に一番近い店だし、たくさんの生徒が来店するに違いない。"






"ここの店員は皆それぞれが、生徒に対処するその人なりの方法を持っているに違いない。いや、そんなことはないのかもしれない。俺が独特な学友たちについて意識し過ぎているのかもしれないな。"






stop music fadeout 2.0

scene bg suburb_konbiniext_ss
with locationchange


"会計が終わり、華子と俺は元来た道へと戻る。"

scene bg school_road_ss
with locationskip

play music music_tranquil fadein 10.0


"道路は今、人々に見捨てられたように閑散としている。学校から出てきた生徒たちは既に帰ってしまって、今は学校に向かう人間はいない。"



"さらにこの先には学校しかないので周りには誰もいない。"

show hanako def_worry_close_ss at center
with charaenter



"そんな人の気配のなさは明らかに華子の立ち居振る舞いに反映される。両腕を体の横に伸ばして袋とかばんを持ち、頭はきちんと前を向き、背中はまっすぐに伸びている……"








"まるで散歩を楽しんでいるかのようだ。"




hi "で、どうしてそんな変わったものばかり買ったんだ？　スパイスミックス？　そんなの学校で必要か？"

show hanako basic_normal_close_ss
with charachange


ha "と……ときどきだけど……料理するのが好きで……"


hi "ああ、俺もだよ。だけど……スパイスミックスってどういうことだ？"


hi "ちょっと上級者向けじゃないのか？"




show hanako emb_blushing_close_ss
with charachange


ha "そ、そんなことないよ"


hi "ふむ、それはいいな。いつか俺にも教えてよ"





show hanako emb_smile_close_ss
with charachange


ha "も、もちろん"


"『もちろん』というほどには見えないけど、そこを突っ込むのは賢明ではないだろう。"




"控えめに言っても、華子は道を下って来たときに比べるととても楽しそうに見える。"



"それだけで俺も少し楽しくなる。"

scene bg school_dormext_full_ss
with shorttimeskip

show hanako basic_normal_close_ss at center
with charaenter



"女子寮の前で、華子と俺はコンビニの袋を各々が買った品物ごとに分類する。"




"並べてみると俺の買ったものがとても地味に見える。"




hi "なんだかさ、俺が買ったものが普通すぎて恥ずかしくなってくるな……"



show hanako defarms_shock_close_ss
with charachange


ha "ち、ちがうよ……私はただ……"



hi "冗談だって"

show hanako def_worry_close_ss
with charachange


hi "先週休んじゃったから宿題が溜まってるんだよね。だから今日は帰らないと"






hi "部屋まで運べる？"

show hanako cover_bashful_close_ss
with charachange


ha "う、うん"


hi "そうか？　わかった、じゃあまた明日な"

show hanako basic_smile_close_ss
with charachange


ha "じゃ、じゃあ"

hide hanako
with charaexit

stop music fadeout 7.0


"華子と別れ、俺は自分の部屋へと戻る。"

scene bg school_dormhisao_ss
with locationskip


"宿題の紙の山が机の上で『早く終わらせてくれ』と俺に語りかけてくる。先週の騒ぎのおかげでほとんどやる暇がなかった。"





"俺は入院していたあいだの勉強の遅れを取り戻そうとしたけど、その課題には前に通っていた学校でも一度も見たこともないものがある。"




"俺は完全に見切り発車状態で、缶ジュースのフタを開け作業に取りかかる。"




scene black
with dissolve
label jp_H4:

scene black
with None

play music music_daily fadein 6.0

scene bg school_dormhisao
with locationchange


"この所本当に暑くなり始めている。"


"今朝目が覚めると、俺の体は汗にまみれていた。"



"生徒たちが朝食と朝の日課を済ませに寮を出るころには太陽はパワー全開になってしまうけど、おかしなことに、それが俺のやる気を奮い立たせる。"



"まだ８時にもなっていないのに、もう今日が静かで暖かく心地よい一日になるだろうと感じる。"



"『授業を休むこと＝生命の危機に瀕しているサイン』と受け取られる学校に通っていなかったら、全部サボって一日中校庭でくつろいでいるところなんだけど。"




"ああ、今日は本当にのんびりとした一日になりそうだ。"




"俺は少しのあいだ途中で動きを止め、ナースに運動について注意されていたことを思い出す。朝のランニング、続けるべきだったかもしれないな。"





"笑美みたいな子と一緒に走るのはちょっときつかったかもしれないけど、もし俺が自分のペースで走っていたら……"





"いやいや、何言ってるんだ。なんのモチベーションもないのに、そんなのやり通せるわけがないだろう。"




"俺だって一日中座っているわけじゃない。コンビニまで行き来するのだって運動のうちだよな？　特にこの高台まで登って帰ってくるときとか……"


"うん。気にしないでもいいさ。何か月も病院のベッドで寝ていたのと比べれば、俺は豊富な運動をしているし。"

scene bg school_scienceroom
with shorttimeskip



"さっき俺が今日という日へ下した評価は、どうやら自分だけが思っているわけではないようだ。"




"クラスのほぼ全員が窓の外の誘うような空を眺めている。"



"しっかりものの静音でさえ、いつも勉強に向けている熱心さを失っているようだ。"


"相変わらずあつかましいミーシャはシャツの第一ボタンさえも外してしまい、ノートであおいでいる。"



"俺はミーシャをジロジロ見ていたに違いない。それに気がついたミーシャがこちらを向いて舌を出している。"




"だけどその行為を止める素振りは見せないし、その事実を隠そうともしない。"


play sound sfx_normalbell


"昼休みの開始を告げる鐘にみんな驚いたようだ。そしていつもに比べてとてもゆっくりと人が、はけていく。"



"この暑さがみんなから急ぐ必要性を吸い取っているようだ。"

stop music fadeout 8.0



"まあ、そうでもない人もいるけど。"


show hanako emb_emb
with charaenter



ha "ひ……久夫くん？"




hi "やあ華子、今日はどうしたの？"





"華子はもう弁当袋を手に持っている。"





"探偵にならなくたって、これがどういうことかはわかる。"



show hanako emb_smile
with charaenter



ha "あの……もしよければ、またお昼ご飯一緒に食べない？"


show hanako basic_bashful
with charaenter


ha "み……みんなの分……持ってきたから……"


hi "おお、すごいな。でもそんなに緊張する必要ないからな"

show hanako basic_normal
with charaenter


ha "あ……うん"



hi "あの紅茶の部屋に行くってことでいいのかな？"


show hanako cover_worry
with charaenter


ha "そ……それでよければ"

show hanako basic_normal
with charaenter


ha "リリーはそこで落ち合おうって言ってたから、その……い……一緒に……"


hi "一緒に？"

show hanako emb_smile at center
with charaenter


ha "…………一緒に行ったほうがいいんじゃないかな……"


hi "うん、それがいい。この暑さでかなり腹が減ってるんだよね"


"華子は安堵の息をつき、俺は勉強道具をまとめる。"

scene bg school_miyagi
with locationskip

play music music_happiness fadein 1.0



"いつものように紅茶部屋の雰囲気はさわやかで、他の世界から隔離されているように感じる。"




"だけど今日はいつもより校内が少し静かな気がする。おおかた、この暑さからくる疲れで引き起こされている倦怠感のせいだろう。"




"華子はまるで雑念を振り払うかのように、小さな動き全てに一心不乱に集中しながら、ゆっくりと昼食をテーブルに広げる。"




"大したことじゃないけど、そんな彼女の振る舞いから華子はこの上ない注意を払って全ての準備をしたのだと感じられる。"



hi "リリーはまだ来ないみたいだな。先に俺たち二人で始めたほうがいいかな？"

show hanako emb_timid:
    center
    ypos 1.17
with charaenter


ha "す、すぐ来るよ……"

show hanako emb_downtimid
with charachange


"華子はご飯が入った入れ物のフタと格闘している。"




hi "ほら、貸してみて……"


"俺は華子の手からその入れ物を受け取ると、フタを開けようと力を入れてみる。"


"いくらやっても、フタは金具で留められているかのようだ。"


hi "あのさ、ご飯がまだ熱いうちにフタを閉めなかった？"

show hanako emb_sad
with charachange


ha "う、うん。急いでて……"


"俺は二人で挟んだテーブルに入れ物を置く。"


hi "だと思ったよ。金具で留まってるみたいにぴったり閉まってる。開けるには熱いお湯がいるね"


hi "でもここじゃ大変そうだな。水ならどこでも手に入るけど"



li "なるほど。では、本日のお昼ご飯に私が貢献するというのはいかがでしょうか？"


show lilly invis at left
with None

show hanako emb_smile:
    tworight
    ypos 1.17
show bg school_miyagi at bgright
show lilly basic_cheerful at twoleft
with dissolvecharamove



"ドアのところでリリーが色々なパンが入った袋を手にぶら下げて微笑んでいる。俺もつられてつい微笑みかえしてしまう。"


show lilly basic_smileclosed
with charachange


li "先日は私のせいでお二人の予定が狂ってしまったので、なにか持っていこうと思っていたんですよ"



hi "ありがとう、リリー。ほら、それ俺が持つよ……"


show lilly basic_smileclosed at Transform(ypos=1.2)
with charamove



"少しの手助けとともに、リリーが持ってきた様々なパンが、華子のご飯抜きの昼食盛り合わせに加わる。俺はこの光景を完成させるために急いで紅茶を入れる。"




hi "よし、これを楽しみにしていたんだよね"

show hanako emb_downtimid
with charachange



"一口目を口にしたとき、華子が俺を注視している素振りを見せないように、懸命の努力をしていることに気づく。"





"特別おいしいってわけじゃないけど、考えてみると文句を言うことはできない。自炊するとなると、俺はかなり無精だからな。"



hi "悪くないな、昨日買った材料で作ったのか？"

show hanako emb_blushtimid
with charachange


ha "う、うん"


"華子の目が感想を求めてこちらを凝視する。"



hi "うん、それだけの価値はあったな。ありがとう、華子"

show hanako cover_bashful
with charachange



ha "あ……これを見せたかったの……昨日話してたから……"





hi "大丈夫だよ。華子が買った材料にちょっと驚いただけだから"





show lilly basic_weaksmile
with charachange


li "華ちゃんは食べ物のことになるといつも実験したがるんです。大概は……良い結果だと思いますよ……"



"リリーは笑顔を崩さないけど、わずかな声色の変化から、過去には芳しくない結果もあったことが伝わってくる。"




"それに、華子の料理を試食するような人がそうそういるわけでもないし……"


stop music fadeout 7.0



"待てよ……リリーは俺が最初に食べるのを待ってたんじゃないか？　俺が大丈夫と言うまで食べなかったよな……"




"リリーの小生意気な笑いを見てこれが彼女による計画的犯行だったことがわかる。いつか今日の仕返しに、どうにかして一本取ってやらなきゃならないな。"





hi "まあ、おいしかったし。それが一番大事だよな？"


show hanako basic_smile
with charachange


ha "そ、そうだね"

show lilly basic_smileclosed
with charachange



"リリーは華子の『創作』の最初の毒味役にならずに済んだことに満足して、目の前の食事を食べ始める。"






"リリーは器用に食べ物を箸で持ち上げるとき、箸をそっと皿に当て、先端で慎重につついたりなぞったりして、素早く食べ物の位置を把握している。俺はその様子に知らず目を奪われていることに気づく。"





"こんな状況でなければ、リリーは食べ物を弄ぶ子供と思われていただろう。ただこれだけ慎重に、そして無頓着に行っているのを見れば、普段からこういう食べ方だというのは明らかだ。"




"機会を逃す前に俺も空腹を満たす作業に入る。"

show hanako emb_downsmile
with charachange




"華子は俺たちとはまた違うアプローチを取る。リリーと俺が手をどけるのを見計らって、素早く自分の分を取り分ける。"






show hanako emb_smile
with shorttimeskip

play music music_dreamy fadein 4.0


"間もなく入れ物は空になる。……閉じたままのご飯のケースを除いて。"

show lilly basic_smile
with charachange


li "ありがとう、華ちゃん。お腹いっぱいです"

show hanako basic_smile
with charachange


ha "こ、こっちこそ……パンありがと……"



hi "うん、あれがなかったらひどいことになってただろうしね"


show lilly basic_planned
with charachange


li "どういたしまして"

show lilly basic_weaksmile
with charachange


li "でも私はもう戻らなくてはならないんです。ここで食事をした後はとても遅刻しやすいんですよ"






hi "ああ、言いたいことはよくわかるよ。俺たちは片付けてから戻るよ"




show lilly basic_smileclosed at twoleft
with dissolvecharamove


li "では、ごきげんよう"

hide lilly
with charaexit

show hanako basic_smile:
    center
    ypos 1.17
show bg school_miyagi at center
with charamove


"リリーが去っていき、彼女の杖が床を叩く音が静かな廊下を下っていく。"


"華子と俺は素早く片付けをすると腰を下ろして鐘が鳴るのを待つ。"


$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene bg misc_sky at Fullpan(20.0)
with locationchange


"俺たちは二人で窓の外の終わりなき紺碧の空を見つめる。"

play sound sfx_warningbell


"もし鐘が鳴らなかったら、時が止まったと断言するんだけどなあ。"


"次の授業をサボってしまえという衝動が俺の本能から湧き上がる。"


"俺と同様、動く素振りを見せない華子に視線を飛ばす。"





ha "まだ、もう少しだけ……"


$ renpy.music.set_volume(1.0, 3.0, channel="music")

scene bg school_miyagi
show hanako basic_smile:
    center
    ypos 1.17
with shorttimeskipsilent


"昼休みの終わりを告げる鐘と予鈴のあいだの時間は瞬く間に過ぎる。"



hi "もう行かないと……もし俺たちがサボったらみんなおかしな想像して、捜索が始まるぞ……"

show hanako basic_distant
with charachange


"華子がため息をつく。"

show hanako basic_normal
with charachange


ha "そうだね"

show hanako basic_normal at center
with charamove


"華子がゆっくりと立ち上がり、俺も後に続く。"

scene bg school_staircase2
with locationskip


"俺たちは無言で３階へ続く古い階段を上り、自分たちの教室に向かう。"


scene bg school_hallway3
with locationchange

play sound sfx_dooropen



"ドアの前で俺は先頭に立って、先手を打って謝るためにあらかじめ頭を下げたまま、華子よりも先にドアを開ける。"


scene bg school_scienceroom at center
with locationchange

stop music fadeout 5.0


hi "遅れてすいません、先生"

play sound sfx_doorclose


"俺は厳しい言葉でも、席に着けという怒った命令でもなく、ただの静寂に出迎えられる。１５人ほどの生徒が笑いをこらえている。"


"武藤先生はいつもの例に漏れずまだ来ていない。しかし華子と俺が一緒に教室に戻ってきたという事実は揺るがない。"

show misha hips_grin at center
with charaenter


mi "プククッ……プフファ……"



"訂正。こらえてるのは１４人くらいで、１人はこらえきれてない。"




play music music_comedy

show misha cross_laugh
with charachange


mi "ぷふっ……ぶぁっははは！　カップルのおかえりで～す！"

show misha hips_laugh
with charachange


mi "わははは～"



hi "どーも。そろそろ落ち着けよ"


hide misha
show hanako invis_close:
    center
    xpos 1.0
with charaexit

show bg school_scienceroom at bgleft
show hanako emb_downsad_close:
    xpos 0.8
with dissolvecharamove


"俺はドアをくぐったところで、華子がクラスの連中から身を隠すように俺の背中にぴったりとくっついているのに気がつく。"

show hanako invis_close:
    xpos 0.7
with dissolvecharamove



"俺が自分の机に近づくと華子は俺から離れてぎこちなく自分の席へと歩いていく。彼女の顔には、みんなの存在を自分の心から精神的に遮断しようという努力がはっきりくっきり書かれている。"


scene bg school_scienceroom at bgright
with charamove


"先生が来ないかサッと確認してから、俺は華子の机まで行き、耳元でささやく。"


hi "ミーシャのことは気にしないでいいから。あいつはいつもこんな感じだし。今日は楽しかった。心配するなよ、オーケー？"


"華子は抱え込んだ腕の中でうなずくけど顔は見せない。"

play sound sfx_dooropen

show muto invis at tworight
with None

show muto normal at center
show bg school_scienceroom at center
with dissolvecharamove


"俺はもう少しここで華子を慰めていたいんだけど、タイミング悪く武藤先生が教室に入ってきてしまう。廊下から授業を始めたかのように、既に話半ばだ。"

show muto smile at center
with charaenter


mu "……もちろんこれは電荷に比例するが距離の２乗に反比例しており……"

hide muto
with charaexit

play sound sfx_doorclose


"先生は俺が華子の机から自分の席までこっそり戻っているのにも気づかないほど熱心にしゃべっている。"


"武藤先生のとりとめもない話が続くなか、ミーシャがこちらへ体を傾けてくる。"

show misha invis at offscreenleft
with None

show misha perky_smile_close:
    xanchor 0.5 xpos 0.16
with dissolvecharamove



mi "先生はひっちゃんの遅刻に気づいていないかもしれないけど、わたしはそうはいかないよ"




"さっきの一幕を見ればそんなことはわかるっての。"

show misha hips_grin_close
with charachange


mi "今日はひっちゃんを助けてあげるように言われてるんだけどね、一つだけ条件があるの"


hi "ええ？　なんだよ？"

show misha sign_smile_close
with charachange



mi "今日の午後はわたしたちの手伝いをすること～！"



"俺はミーシャの肩越しから向こうを見るために首を伸ばす。"


"都合よく静音はこちらを見ていない。"


hi "わかった、今日だけだぞ"


hi "生徒会には入らないって前に言ったからな、覚えてるだろ？"

show misha hips_grin_close
with charachange


mi "もちろん！　それじゃあ……それじゃあ……"

show misha perky_confused_close
with charachange


"ミーシャはノートに目を落とす。明らかにそこに書いてあるものの中から次にどう返したらいいのかを探している。"

show misha hips_grin_close
with charachange


mi "……それじゃあ脅迫だもんね、法律違反になっちゃうよ"



hi "今更法律を気にするなんて、お前らしくないな"


show misha sign_smile_close
with charachange



mi "物事はルールに従ってやらなきゃだめなの！"


show misha perky_smile_close
with charachange



mi "ただ、全ての状況に合わせてルールが書かれてるわけじゃないの。だから無視していいときもあるんだよ"





hi "これでお前ら２人とも、みんなが生徒会に入りたがらない理由がわからないっていうんだからな……"



stop music fadeout 3.0

show misha hips_frown_close
with charachange

with Pause(0.3)

show misha invis at offscreenleft
with dissolvecharamove

hide misha
with None



"ミーシャは俺に向かって舌を出した後課題に戻り、俺たちは午後の授業を切り抜けるのに悪戦苦闘する。"



with shorttimeskip

play sound sfx_normalbell

show shizu invis_close at offscreenright
show misha invis_close at offscreenleft
with None

show misha hips_smile_close at twoleft
show shizu behind_blank_close at tworight
with Dissolvemove(0.5, time_warp=_ease_in_time_warp)


"俺が立ち上がることさえできないうちに、ミーシャと静音がそれぞれの手で俺の両肩を掴んでしまう。"



hi "おい、手伝うって言ったろ、ったく……"


play music music_shizune fadein 1.0

show misha hips_grin_close
with charachange


mi "ひっちゃん、これはただの保険だよ、保険～！"

show hanako invis behind shizu at offscreenright
with None

show misha hips_smile_close at Transform(xpos=0.17)
show shizu behind_blank_close at Transform(xpos=0.5)
show bg school_scienceroom at bgleft
show hanako emb_timid:
    xanchor 0.5 xpos 0.9
with dissolvecharamove



ha "ひ、久夫くん？"




"華子が恐る恐る俺たちの周りをまわって教室から出ようとする。これはミーシャたちから逃げるチャンスじゃないかとひらめく。"





hi "ああ、華子。どうかしたか？"

show shizu basic_angry_close
with charachange


shi "……"

show misha hips_frown_close
with charachange



mi "ちょっと、おしゃべりしてる時間なんてあると思ってるの？"





hi "落ち着けよ、すぐ済むから……ごめん華子、どうしたんだ？"





show hanako emb_downtimid
with charachange


ha "と……図書室に行こうと思っていたんだけど、その……それで……"


"華子は手を組んで親指を互いにくるくる回し、視線は部屋中にチラチラと動いている。だけど俺たちを見ることはない。"


show misha sign_smile_close
with charachange



mi "ごめんねー華子、ひっちゃんはわたしたちと一緒に来ないといけないの。やらなきゃならない仕事があるんだよ"


show shizu behind_smile_close
with charachange


shi "……"

show misha hips_grin_close
with charachange


mi "あ！　でも華子が手伝いたいって言うならそうしてくれていいよ"

show hanako cover_worry
with charachange


ha "あう……"

label jp_choiceH4:
menu:
    with menueffect
    mi "ね、これでどう？　ひっちゃん"
    "どうする？　華子":




        return m1
    "俺はもう十分生徒会の仕事に貢献したよ":


        return m2

label jp_H5_1:




show bg school_scienceroom at bgleft
show hanako cover_worry:
    xanchor 0.5 xpos 0.9
show shizu behind_smile_close at Transform(xanchor=0.5, xpos=0.5)
show misha hips_grin_close at Transform(xanchor=0.5, xpos=0.17)
with None


hi "どうだ？　華子。みんなでやればすぐ終わるぞ"

show hanako emb_timid
with charachange


"華子がなにか言う前からそわそわしているのが俺の質問への答えだ。"

show hanako emb_downtimid
with charachange


ha "ほ……本当に行かないといけなくて……"



"うむ、予想通りだった。また生徒会女子２人と俺の３人か。"



"狭い生徒会室で、華子を交えて作業をすることは諦めることにしよう。"



hi "あとで行くからさ、な？"

show hanako emb_smile
with charachange


ha "わ、わかった"

stop music fadeout 3.0

show misha hips_grin_close at twoleft
show shizu behind_smile_close at tworight
show hanako invis at offscreenright
show bg school_scienceroom at center
with dissolvecharamove

show misha hips_smile_close at twoleft
hide hanako
with charachange



mi "よし！　お別れは済んだわね、お仕事おしごと～！"


scene bg school_hallway3
with locationchange




"ミーシャと静音は俺の肩をずっとつかんだまま、無理やり生徒会室へと連れて行く。"





"こんな形で華子を置いていくのは少し悪い気がするけど、これが華子からミーシャを引っぺがすための対価なら、しかたないか。"


scene bg school_council
with locationchange


hi "それで、今日はなにをするんだ？"

show misha sign_smile at center
with charaenter

play music music_ease fadein 8.0


mi "ほうこく！"



hi "は？　普通は何かしたあとに報告するもんだろ？"


show misha hips_grin
with charachange


mi "うん！　しっちゃんが先生に報告できるように学園祭の情報を全部整理しなきゃいけないんだよ"

show misha hips_grin at twoleft
show bg school_council at bgleft
with charamove

show shizu adjust_happy at tworight
with charaenter


"静音は俺の前に巨大な書類の山を置いて短く笑う。"

show misha hips_smile
with charachange


mi "これを２つの山に分類してほしいの"

show misha sign_smile
with charachange



mi "１つはお金関係ね、レシートとか。次は意見書。その次は前向きな意見書、それと来年問題になりそうな意見書があったらそれも別にして。あと１つ、改善できそうにない問題点の意見書……"



hi "全然２つなんかじゃないじゃないか……"

show misha perky_confused
with charachange


mi "はれ？　あ、そだね。２つだけだと思ってた。ごめんごめん"


hi "わかった。で、俺がこれをやってる間、２人はなにしてるんだ？"

show misha hips_grin
show shizu adjust_smug
with charachange



mi "うーん、報告書を回収してたらお昼食べそびれちゃったから、何か食べてくるつもり！"




"なんで回収するついでに分類しなかったんだよ……"




"俺の自己防衛機能が作動したおかげで、口を開いてこれ以上事態を悪化させるのを防ぐことができた。"






show misha perky_confused
with charachange


mi "んー？！"

show misha perky_sad
with charachange




mi "そんなの不公平じゃない？"



show shizu behind_blank
with charachange


shi "……"


"俺は不平等な作業分担にうんざりしていて、静音がずっと手話を続けていたことに全く気づかなかった。"



"もしミーシャが思わず漏らした言葉がなければ、たぶん全く気づいていなかっただろう。"




show shizu adjust_smug
with charachange

show shizu basic_normal
with charachange

show shizu behind_blank
with charachange


"静音はミーシャにかなり長々と指示を出しているようだけど、その中に楽しそうなものはなさそうだ。"


show misha sign_sad
with charachange

show misha perky_sad
with charachange

show misha perky_sad at Transform(ypos=1.15)
with charamove


"指示が終わるとミーシャが静音に短く手話を返し、俺の隣にある机に座る。"


show shizu adjust_happy
with charachange

hide shizu
with charaexit

show misha perky_sad at Transform(xpos=0.5)
show bg school_council at center
with charamove



"静音は俺とミーシャに手を振ってから、ドアの外に消えていく。"





hi "一体なんだったんだ？"

show misha perky_confused
with charachange




mi "しっちゃんはひっちゃんが監督なしだと作業をまるっきり間違えちゃうんじゃないかって心配だったんだよ"



show misha perky_sad
with charachange



mi "で、しっちゃんはひっちゃんにどこが間違ってるって言えないからわたしを残したの。あーあ……もー、わたしもしっちゃんと一緒に行きたかったよー！"


show misha cross_smile
with charachange


mi "でもしっちゃんは食べ物持ってきてくれるって～！"

show misha cross_grin
with charachange


mi "やったね！"



"ミーシャの軽快さはもはやこの世のものとは思えない。食べ物の話題くらいで憂鬱の底から世界のてっぺんまで昇り切ってしまう。"







"他の人がこのレベルに達することができるとは思い難い。"


hi "ああ、不幸中の幸いだよ"


hi "で、なにすればいいんだっけ？"

show misha sign_smile
with charachange


mi "分類"



hi "それはわかったよ"


show misha hips_smile
with charachange



mi "うん、じゃあ書類の分類を始めよっか。分けた書類の山の意味は後から考えるから"



hi "そうだな……"

show misha perky_smile
with charachange


"俺たちは書類を次第に込み入ってくるいくつもの山に分け始める。"



"最初は大きなカテゴリーに分けていく。収支、意見書、事故の報告……"


"そしてそれらを良い報告と悪い報告に分け、ついには机の上に書類を投げているように見えてくる。"



hi "絶望的だな"


show misha perky_confused
with charachange    


mi "へ？　なんで？　言われたことはちゃんとやってるよね？"


hi "ああ、だけど俺たち散らかしてるようにしか見えないぞ"

show misha hips_grin
with charachange 



mi "ううん。たくさんやったと思うよ。これなら、残りはしっちゃんでもできるでしょ"



show misha cross_grin
with charachange 


mi "だから一旦このへんで作業を止めてもいいかな"



"ミーシャの中の常識は静音といっしょにこの部屋から出て行ってしまったようだ。"




"だけどミーシャの提案に異議を唱える意味なんてこれっぽっちもない。"

show misha sign_smile
with charachange


mi "とにかく……"

show misha cross_smile
with charachange



mi "ひっちゃんと華子はどうなってるわけ？"



hi "どうって？"

show misha hips_smile
with charachange 



mi "ひっちゃん、今日華子と一緒にいたよね～？"


show misha hips_grin
with charachange 




mi "何か二人の仲に進展でもあったの？　ひっちゃん、わたしに言ってない噂があるよね～？"






hi "俺が自分の状況をお前に話したら、それはもう噂じゃないだろ？"


show misha perky_confused
with charachange



mi "まあ、たしかに……"





hi "華子とはただの友達だと思ってるよ"


hi "なんでそんなに興味があるんだ？　お前と静音は華子のことが好きじゃなかったんじゃ……"

show misha cross_frown
with charachange



mi "ほんとはそういうのじゃないんだよ。しっちゃんとリリーの仲が悪いのは知ってるでしょ"




mi "そんでもって華子をリリーから引き離すことなんて実際できないから、わたしたちは華子とほとんど話さないんだよ"


show misha sign_smile
with charachange



mi "でもだからといって、わたしが華子を心配できないというのとは違うんだよ"



hi "何の心配だよ？"

show misha perky_sad
with charachange



mi "うーんと、華子は他の人と絶対に付き合わないんだよね？　そんなの良くないよ、ひっちゃん！"





"もし静音とリリーが『性格の違い』から互いを毛嫌いしているのなら、ミーシャと華子の関係がどうなるかなんて考えたくもない。"


show misha perky_confused
with charachange



mi "ていうか、どっちみちわたしたちはみんな同じ環境にいるわけじゃない。そうでしょ～？"






hi "まあ、そうだろうな"


show misha sign_smile
with charachange



mi "前に一度、華子が授業の途中で廊下に出て行っちゃったときに、しっちゃんが先生の所に行って、華子の扱いはどうなるのかって聞いたの"


show misha sign_confused
with charachange



mi "先生は『ここの生徒は皆、それぞれに特別な事情がある。しっちゃんはそういうことを気にかけなくていい』って言ってた"


show misha perky_confused
with charachange


mi "華子はまだ一度も共同作業をしたことがないんだよ、そうなると逃げちゃうから"


mi "これが心配しないでいられる？"



hi "お前の言ってることは正しいと思うよ。俺たちが話してるとき、今でも華子はほとんどしゃべらないし"


show misha perky_sad
with charachange


mi "むむむ、わたしはそこまでできなかったよ。初めて出会った時にしっちゃんとわたしも華子と話そうとしたけど、華子、怖がって逃げちゃったんだよね"



"俺も最初は同じだったとミーシャに言おうかと思ったけど、どうやら彼女は考えることに夢中なようだ。"


"静音の影響がない状態のミーシャと話すのは……面白い。"

show misha cross_frown
with charachange




mi "わたし思うの。華子はここの人たちは見た目なんて気にしないこと、わたしたちを信用していいってことに気づかなきゃだめだって"



show misha cross_smile
with charachange



mi "もしそれができたら、わたしの華子に対する印象もぐっと良くなるんだけどな"






"こんなに長い間手話を使っていないミーシャを見るのは初めてだ。"



"静音と一緒にいるとき、まわりの状況を静音に説明するためにミーシャは絶えず手を動かしているからな。"


"あれほどの頑張りは、たぶん回転の速い頭でさえその負担になるはずだ。"


"そして正直言って、ミーシャは世界一頭がいいわけでもない。"




hi "ああ、ミーシャのためにも華子のことを注意して見ていくつもりだよ"



hi "でも早めに華子に謝っといたほうがいいぞ。華子はその手の冗談には向いてないと思うし"

show misha perky_confused
with charachange


mi "え？　あ～！"

show misha perky_sad
with charachange


mi "気づきもしなかったよ。ごめん"


hi "その言葉は俺じゃなくて華子に言ってやれよ"

show misha perky_smile
with charachange


mi "そうだね。まずは明日話してみるよ"


hi "それがいいよ"

play sound sfx_doorslam
with vpunch


"ドアから不協和音が響き、静音が戻ってきたことを告げる。"



"今どれだけの雑音を出したか、静音自身は気づいていないんだろうな。"



show misha hips_grin
with charachange


mi "あ、しっちゃん！　おかえり！"

show shizu invis at Transform(xanchor=0.5, xpos=1.0)
with None

show misha hips_grin at Transform(xpos=0.3)
show shizu behind_blank at tworight
show bg school_council at bgleft
with dissolvecharamove




"コンビニの食料品を山ほど持った静音が現れる。"




show shizu basic_normal2
with charachange


shi "……"

show misha sign_smile
with charachange


mi "学園祭の予算に余りがあったんだ。これはれっきとした学園祭の仕事なんだから、少しぜいたくさせてもらったの"


show misha hips_grin
with charachange


mi "ナイスアイディアだね。しっちゃん、１０点！"




hi "本当にいいのかよ？　それ"

show shizu cross_angry
with charachange


shi "……"

show misha cross_frown
with charachange


mi "生徒会に入ることを嫌がる割には、ひっちゃんは生徒会の政治問題に不健全な興味を持つようね"


show misha cross_grin
show shizu adjust_smug at tworight
with charachange


mi "無礼の罰としてひっちゃんの分減らしちゃおうか"



hi "へいへい、わかったわかった"

show misha perky_smile
show shizu adjust_happy at Transform(ypos=1.15)
with dissolvecharamove



"静音が次々とテーブルの上に広げていく大量の食べ物を置く空間を作るために、ミーシャは分けた書類の山を机の一端にまとめる。"





"俺がやっていたキツい上に見当違いの作業が水泡に帰すのを見て、道理でこの２人が手伝いを必要としているわけだと気づく。"




"コンビニの食べ物は特別おいしいってわけではないけど、少なくとも腹は満たされる。"

show shizu behind_smile
with charachange


shi "……"

show misha sign_smile
with charachange


mi "今日は手伝ってくれてありがと。ほとんど先生に出す報告書を書いてただけだったね"

show misha perky_smile
with charachange


mi "今年は少なくとも何件かは報告書にきちんとした表題がつけられるよ"




hi "これで腐敗組織じゃないって自称してるんだからびっくりだな？"




show misha hips_grin
with charachange



mi "違うよ、全然違うよ！　わたしたちは規則に従ってる。その規則にあいまいなところがあるのはわたしたちのせいじゃないよ"



hi "そういうのが腐敗の定義だと思ったんだけど……"


show misha hips_smile
with charachange


mi "考え過ぎだよ～！"



hi "奇遇だな、俺もそう思うよ"




hi "とにかく、俺はもう行かないと……"


hi "……その、行ってもいいなら"

show shizu adjust_smug
with charachange


shi "……"

show misha hips_grin
with charachange



mi "十分な働きだったわ。行ってよろしい"



hi "そうか、サンクス"



hi "あのさ、『果てしない仕事』よりも『タダ飯』の方を強調してれば、手伝いに来る人ももっと増えると思うぜ"


stop music fadeout 6.0

show misha sign_smile
with charachange

show shizu behind_blank
with charachange


mi "それは一理あるかもしれないね"


hi "うん、考えてみろよ"


hi "それとさっき話したこともさ……別に言いたくないんだったら静音に言わなくたっていいんだから"

show misha perky_confused
with charachange



mi "えっ？　あー、そうだった。明日華子と会ってみるよ"


show misha perky_smile
with charachange


mi "じゃあね、ひっちゃん"


hi "またな、ミーシャ、静音"

scene black
with dissolve



label jp_H5_2:

show bg school_scienceroom at bgleft
show hanako cover_worry:
    xanchor 0.5 xpos 0.9
show shizu behind_smile_close at Transform(xanchor=0.5, xpos=0.5)
show misha hips_grin_close at Transform(xanchor=0.5, xpos=0.17)
with None




hi "なあ静音。手を貸すって言ったけど、前々からの予定があったのを忘れてたよ。それに先週は俺の役目以上に手伝っただろ？"




hi "また今度埋め合わせするって約束するからさ"

show misha sign_confused_close
with charachange

show shizu basic_frown_close
with charachange

show misha perky_smile_close
with charachange

show shizu behind_blank_close
with charachange


"静音とミーシャは手を俺から離し、長く深い、そして無音の会話を交わす。"

show misha sign_smile_close
with charachange



mi "まあ、ひっちゃんの言うことにも一理あるね。実は余った予算でケーキ買おうかって思ってたんだ"


show misha cross_laugh_close
with charachange


mi "だからひっちゃんがいなければ好都合だね。ケーキたくさん食べれるもん。わははは～！"

stop music fadeout 6.0

show shizu invis at offscreenleft
with dissolvecharamove

show misha invis at offscreenleft
with dissolvecharamove

hide shizu
hide misha
with None


"静音は回れ右するとドアの外へと出て行き、ミーシャもそれに続く。"


hi "あれ、思ってたよりもずっと簡単だったな。あいつら、先週は警察犬みたいだったのに。それか刑務官って言ったほうがいいか"




hi "それとも警察犬の『刑務官種』かもしれないな……"



"自分がそんなことを考えるなんて信じられない。ましてやはっきりと口に出すなんて。健二から離れる必要があるな。"



hi "……忘れてくれ。とにかく、図書室へ行かなきゃならないんだろ？"

show hanako basic_smile
with charachange


ha "そ、そう"

play ambient sfx_crowd_indoors fadein 0.5

scene bg school_hallway3
show crowd
with locationchange


"華子は図書室へ続くまだ人の多い廊下を、俺の陰に身を隠しながらついてくる。"


stop ambient fadeout 0.5
play music music_happiness fadein 2.0

scene bg school_library
show hanako invis at offscreenright
show yuuko neutral_down at center
with locationchange

show hanako basic_worry at tworight
with dissolvecharamove


"ドアをくぐるとすぐに、華子は優子さんが本を積み上げているカウンターへと走っていく。"

show hanako emb_emb
with charachange



"俺が追いつく前に、華子は何かを優子さんに耳打ちした。"


show yuuko neurotic_up
with charachange


yu "うーん、それならノンフィクションの棚にあると思うけど、正確にどこにあるかはわからないわ。よかったら調べるけど……"


show hanako emb_downsad
with charachange


ha "だ、大丈夫"


hi "やあ優子さん、何の話？"

show yuuko neutral_down
with charachange


yu "あっ、中井くん……華子ちゃんが本を探してて……分野は――――"


show hanako emb_blushing
with charachange


ha "な、何でもない……"


hi "何でもない本？　ノンフィクション？"




show hanako def_strain
with charachange


ha "わ……私はただ……"

show yuuko neurotic_up
with charachange


"優子さんに目をやると、先ほどの華子の頼みを秘密にするということのプレッシャーから今にも逃げ出しそうだ。"



hi "優子さん、いったい何を……"

show yuuko happy_down
with charachange


yu "チェス！　華子ちゃんはチェスの本を探してるの！"




"優子さんにはどんな重要な情報も決して委ねない、と俺は心にとめる。"


show hanako defarms_shock
with charachange


ha "ゆ、優子さん……"

show yuuko panic_up
with charachange


yu "ごめんね、華子ちゃん……口が滑っちゃった……"



hi "まあ、これで秘密じゃなくなったな。行こう、手伝うよ。俺も腕を磨くべきだしな"


show hanako def_worry
with charachange


ha "わ……わかった"

hide yuuko
with charaexit

show hanako def_worry at center
show bg school_library at bgleft
with charamove


"華子と俺はノンフィクションの書架エリアの奥へと歩みを進めると、優子さんは恥ずかしそうにカウンターの裏へと消えていく。"




"これらの本を分類するやり方があるということは知ってるけど、自分の半生をその分類法の研究に費やした人でもなければ、それを読み解ける人がいるとは思えない。"





"たぶんそれが、俺が知っている司書がみんな神経質であることの理由なんだろう。"








"通路の終わりに向かって並んでる本のなか、手品と子供向けゲームの本のあいだに『チェス王者への戦略』という本がある。"



show hanako basic_bashful
with charachange


"俺が手に取る前に、華子はその本を手に取って、胸に抱えこむ。"



hi "さて、無事に手に入ったな。そうだ、読み終わったら借りてもいいかな？"


show hanako cover_worry
with charachange


ha "も、もちろん。わ……私今までリリー以外の人と対戦したことなかったから……だからその……"


"やばい、本気で勝ちに行っていたわけではさらさらなかったんだけど、華子はそう受け取ったみたいだ。"





"でも、これは少なくとも華子は俺ともう一度チェスをやりたいってことだ。それはいいこと……だよな？"




hi "はは、俺は上級者でもなんでもないぞ。だってほんの少ししかやったことなかったし……"




"華子に俺の境遇を言っていなかったことが頭に浮かぶ。俺は一瞬口ごもり、自分の過去については黙っておくことに決める。それはまた今度にしよう。"




hi "……ここに来るまでは"

stop music fadeout 6.0

show hanako cover_distant
with charachange





ha "だ……大丈夫？"




hi "ああ、ちょっと思い出したことがあって……"




"考えてみると、俺は華子に入院中の生活とか体の状態について話すことを恐れるべきじゃなかった。華子の傷跡から察するに、たぶんかなりの時間を病院のベッドの上で過ごしたはずだし。"





"だけど、どういうわけか、言い出すことができない。少なくとも今日はだめだし、突然言うのもなしだ。"



"この会話を中断したくてたまらず、本棚から適当に本を抜き取る。"







"世界で最速のジェットコースターの本……"



"……１９８２年出版。うーむ、そんなに新しくないけど、少なくとも面白いはずだ。"




hi "さて、二人とも読む本は決まったし、座らないか？"



show hanako cover_bashful
with charachange


"華子は俺の虚勢を真に受けてくれたようで、俺たちは図書室の後ろの方にある人目につかない読書コーナーへと足を進める。"



hide hanako
with charaexit



"二人とも言葉を発さず、ただ本を開き、読書を始める。"




"俺も本を読もうとするけど、その本によると１９８２年のジェットコースターは２０年以上経った今のものに比べると小さいようだ。"





"本に載っているもののほとんどが木製だ。それがどうも俺には安全に見えない。"





"もし危険かもしれない乗り物に乗るのなら、俺は鋼鉄製か、『チタン』や『ルテニウム』という、小難しい単語が入った最新式の合金製がいい。"





"俺はすぐに興味を無くすと、読書コーナーの中に視線を漂わせ、華子へと向ける。"

show ev hana_library_read_std:
    truecenter zoom 1.0 subpixel True
    easein 20.0 zoom 1.05
with locationskip



"華子は夢中になっているようで、自分がたった今読んだ内容を確認するかのように、前後にペラペラとページをめくっている。"



"あれで本当に効果があるのだろうか？　それとも単に理解が追い付いていないだけなのか。"


"華子が無意識に顔から前髪を払う。その瞬間、傷跡の皮膚組織が露わになる。"



"俺はまだ山久での礼儀を完璧にわかっているわけじゃない。華子の傷跡について尋ねるのは正しいことなのか？　華子の過去のことは？　入院していた期間は？　まだ医者には行っているのか？"




"どの質問も、転校してきたばかりの生徒にするような質問に見える。しかも方言で。"





"でも、今までそんなことを俺に面と向かって聞いてきた人は一人としていなかった。まあ、琳は除くけど。あいつを正しい人付き合いの手本にするべきだとは思わないし。"






"さしあたりは黙っていよう。もし知ってほしいのなら、誰だって自分から言うだろう。無理やり言わせるようなことをしたら、華子はまた心を閉ざしてしまうかもしれない。"





scene bg school_library_ss
show yuuko worried_up_ss at center
with shorttimeskip


yu "あのぉ……お邪魔して悪いんだけど、もうここ閉めないといけないのよ"

play music music_tranquil fadein 3.0


hi "もうそんな時間？"


"俺は時計を確認する。どうやら、俺が思いにふけっている間に２時間近く経ってしまったようだ。"

show yuuko smile_down_ss
with charachange


yu "その本借りてく？　帰る途中に手続きできるけど……"

show hanako invis:
    xpos 0.9 xanchor 0.5 ypos 1.17 yanchor 1.0
with None

show hanako basic_worry_ss:
    xpos 0.7
show bg school_library_ss at bgleft
show yuuko smile_down_ss at twoleft
with dissolvecharamove


ha "お、お願いします"



hi "俺はいいです。戻る途中に棚に戻しておきます。最初に思ったよりも面白くなかったんで"



show hanako emb_timid_ss at tworight
with dissolvecharamove


"華子は紙をしおりにして本に挟み、立ち上がる。優子さんと華子はカウンターへ向かい、俺は元あったと思う本棚に本を戻す。"


show yuuko neurotic_up_ss
with charachange



"優子さんは手慣れた正確さで華子の本をスキャンするけど、それでもまた手を滑らせる。"


show yuuko neutral_down_ss
with charachange



yu "ふぅ……はい、できた。三度目の正直よ。ノンフィクションは１週間しか借りられないからね"


show hanako basic_smile_ss
with charachange


ha "だ、大丈夫です"


scene bg school_hallway2
with locationchange


"優子さんは図書室のパソコンをシャットダウンし、俺たちを外に出るように促す。"

show yuuko panic_up at twoleft
show hanako def_worry at tworight
with charaenter



yu "あー！　もうこんなに遅くなってたなんて思わなかった！"




hi "でもさっき自分でもう閉めなきゃって言ってたじゃないですか……"


show yuuko worried_up
with charachange


yu "そうだけど、わかってたけど、時計は見てなかったの！"

show yuuko neurotic_up
with charachange


yu "またねっ！"

hide yuuko
with easeoutleft


"優子さんはハンドバッグを不格好な吹流しのように後ろにたなびかせながら、廊下を駆けていく。"


show hanako def_worry at center
show bg school_hallway2 at bgleft
with dissolvecharamove


hi "司書ってみんな本当に神経質だよな"

show hanako emb_timid
with charachange


ha "へ？"


hi "あ、いや、何でもない。どんなに本に詳しくても、時間を計画的に使える司書を見たことがないなって思ってただけだよ"


show hanako basic_smile
with charachange



ha "うん……い、言いたいことはわかるよ……"




"華子はおかしそうに微笑む。冗談で言ったわけじゃなかったんだけど、別の司書の人か何かを思い出させてしまったみたいだ……"


show hanako cover_worry
with charachange


ha "わ……私、帰らないと"


hi "そうだな、俺もだ。こんなに遅くなってるなんて気がつかなかったよ。付き合わせてくれてありがとう"

show hanako basic_bashful
with charachange


ha "き、気にしないで"


hi "どっちみち俺も寮に帰るから、よければ一緒に行かないか？"


show hanako emb_blushing
with charachange


ha "う、うん、いいよ"

hide hanako
with charaexit


"華子は俺の前を歩きだす。俺は小走りして華子の隣に並ぶ。"


scene bg school_dormext_full_ss
with locationchange

show hanako def_worry_ss at center
with charaenter



"学校の庭を通って、そのうち寮の前に到着する。"




hi "おいおい、歩くの速いな。サッカー部だった俺より早いよ"

stop music fadeout 6.0

show hanako emb_downsmile_ss at center
with charaenter




"俺は自分の言葉に後悔する。それは華子のペースが速いという以上に、俺の病状が運動能力をかなり悪化させたということだ。"






"華子の反応は妙だ。てっきり自らの歩く速さを卑下しようとするいつもの不器用な反応が返ってくるものだと思っていたけど、実際には笑みを浮かべながら足下に視線を落として、ただ顔を赤らめるだけだ。"








"二人の間の空気に沈黙が流れる。華子と一緒にいるとこんなことはよく起きるけど、今回はいつもと少し違うように感じる。数秒後、俺は沈黙を破る。"




hi "さてと、また明日、教室で……かな？"

show hanako emb_smile_ss
with charachange


ha "う、うん"

hide hanako
with charaexit


"華子は短く手を振ると寮のドアを押しあけて、中へ入っていく。俺は少しの間、突っ立ってその様子を見送ってから、自室へと足を進める。"

scene black
with dissolve



label jp_H6:

scene bg school_dormhisao
with locationchange


"鳥たちがチュンチュンと鳴いている。"


"普通ならば、自然の美しさに思いを馳せるいい機会だろう。"



"でも……今は朝の６時だ。"

play sound sfx_pillow

scene black
with Dissolve(0.2)


"俺は枕で頭を覆って、衝撃で夢の世界へと戻れたらいいのにと思いながらマットレスに顔面をぶつける。"



"無駄だった。"



"俺は寝返りを打つけれど、眠りはまったくと言っていいほど戻ってくる気配がない。"


play music music_daily fadein 10.0

scene bg school_dormhisao
with locationchange


"自然の欲求には敵わない。お前の勝ちだ。わかるか？　へいへい、今起きますよ……"



"睡眠不足で俺のテンションはダダ下がりだ。うまい朝飯をたくさん食べる、テンションを上げるにはこれしかないな。"


$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_cafeteria
with locationchange


"一番乗りに出て行くのもいいだろうな。"



"湯気が上がるようなできたての料理に一番にありつくために、好きな席に座るために……"


"…………だとよかったんだけどな。"



"俺が自分の中ではとてつもなく早起きしたのにもかかわらず、いわゆる学校で一番勤勉な生徒たちはもうすでに来てしまっている。"




"あれやこれやの理由で、ここには朝が早い奴がかなりたくさんいるみたいだ。"




"体操着を着た生徒たちが、テーブルのまわりで時折食べ物を吸い込むようなスピードでパクつきながら、熱心に試合の作戦会議をしている。"





"広間には寝ぼけ眼の生徒もけっこう見られる。たぶん俺と同じ、そう、あのやかましい鳥どもに苦しんでいるのだろう。"



"もちろん、かばんを教科書や終わった宿題やらでいっぱいにして、本当に早起きを楽しんでいる人もいる。"


"そういう人たちを嫌がるなと言われても、それは無理な注文だ。ましてや疲れてるときは尚更だ。"



"まばらな人混みの中、知っている顔を探しつつ、俺は一番近くのテーブルに向かう。"



"リリーが一人で座って、卵がのった小さな皿の縁をフォークで上品に確かめている。"





"その動きは機械のように正確で、声をかけることもはばかられる。"







"目の見えない人が何かに夢中になるとこうなるのだろうか？　長年繰り返して身についた、決まり切った動作をしているだけだ。目の見える人が新聞を読みながら食事をするように。"





hi "おはよう、リリー。こんなに早くからいるとは思わなかったよ"

show lilly basic_surprised:
    center
    ypos 1.2
with charaenter


li "あら久夫さん、びっくりしました。こんなに早い時間に朝ごはんを食べていたんですね、知りませんでした"


hi "いや、今日はたまたまだよ。普段なら朝飯のために早起きするより学校に遅刻する方を全力で選ぶよ"

show lilly basic_weaksmile
with charachange


"俺が食事を始めると、リリーは俺が遅刻体質であることを自覚していることに小さなため息をつく。"


"まもなくしてリリーはさっきまでの無意識の食事に戻る。"


"このリリーの一連の動作にはエネルギーが欠けていて、普段の雑務をこなすときに周りをキョロキョロ見回してしまうことに似ているなと感じる。"



"しかし、食べ物を見つけては食べ、見つけては食べ、を数回繰り返した後、リリーはフォークを置き、ナプキンで口を拭う。"

stop music fadeout 6.0
stop ambient fadeout 6.0

show lilly basic_concerned
with charachange


li "久夫さん、一つ質問してもいいでしょうか？"


"ちくしょう。俺が欲しいのは少しの食事と４時間ほどの睡眠だ。そして残念なことに、簡単な質問をするときに『質問してもいいですか』なんて言う人間は誰一人としていない。"


hi "ああ"

show lilly basic_listen
with charachange


li "華ちゃんを友達だと思いますか？"


"あれ、なんか誘導尋問みたいだぞ。"


hi "うん……そうだと思う。なんでそんなことを？"

show lilly basic_weaksmile
with charachange


li "特に意味はないです"

show lilly basic_displeased
with charachange

play music music_serene fadein 8.0



li "ただ、もう一つ質問があります。どうして華ちゃんを友達だと思うんですか？"




"さっぱりわからない。リリーは俺に何を期待しているんだ？"






hi "俺にもよくわからないよ。華子は人との接し方が少し違うからだと思う……"






show lilly basic_reminisce
with charachange


li "……私と出会ってから、華ちゃんは本当に私以外の誰とも、関わりを持っていないんです"

show lilly basic_concerned
with charachange



li "華ちゃんは他人に興味がないみたいなんです。それに華ちゃんの見た目をみんな少し怖がっていると思うんです"





hi "マジで？　ここではそういうことは、その、しないものだと思ってたよ。差別とかさ"


show lilly basic_listen
with charachange



li "うーん、言わせていただけるのなら……"




"リリーが考え込んで眉間にしわを作る。それを見て、リリーが何を言い出すのか少し心配になる。"



show lilly basic_weaksmile
with charachange



li "久夫さんは少しウブなんじゃないかと思いますね"





"ウブ？　リリーの顔にシニカルな微笑が浮かんでいなかったら、俺はこの言葉を侮辱と受け取っただろう。"



hi "な……なるほど"

show lilly basic_reminisce
with charachange



li "山久は他の学校に比べて強い共同体意識を持っている反面、人同士の衝突がないとは到底言えないのです"


show lilly basic_displeased
with charachange


li "規則は人間の本質までは取り除けません。結局ただ抑え込むだけなんです"


"確かにそれは俺も気づいていたことだ。"




"それは人や仲間グループが廊下でどうやって他の人とすれ違うかといったような、ほんの小さなことだ。俺がいた学校となにも変わらない。"







"リリーと静音でさえ、一見するとかなり心が広そうだけど、犬猿の仲だと言えるだろう。"




"まあ、少なくともミーシャを通して見る静音は寛容そうだ。ミーシャは静音の指の動きと眼鏡の向こうの目つきの本当の意味を理解しているからな。"




hi "リリーの言っていることは正しいだろうけどさ、俺が初めてここに来たとき、何もかもがちょっとした衝撃だったんだ"






hi "俺はずっと間違ったことばかりしてた。そうでなくても、少なくとも自分が間違ったことをしてると思い続けてた。俺たちが初めて会ったとき、君に『見たことあるよ』って言ったみたいにね"









hi "俺はそれが失礼なことかどうかわからなかったから、とにかく心の奥にしまっておくことにしたんだ。人を特別扱いするとか、そういうことを"








hi "だから俺は特別扱いしなかった。華子とリリー、それに他のみんなは『普通』なんだって自分に言い聞かせて、わかりきっていることにも気づかないふりをしようとしたんだ"



hi "だから俺は華子に他の人と同じように話しかけたし、友達にもなった"



hi "少なくとも、俺はそういうことだと思ってる"





hi "だけどさ、こういうことを口に出して言うだけで悪い気がするんだ。まるで華子やリリーや他のみんなを『普通』の人間だって考えるために特別な努力が必要だって言ってるみたいで。そんなのおかしいと思う"



show lilly basic_smileclosed
with charachange


li "久夫さん、やっぱりあなたはウブだと思います。でもあなたはいい人なんだとも思います。たぶんこれは、久夫さんの良いところの一つなんでしょうね"


hi "そう言ってもらえると……ありがたいけど……"

show lilly basic_smile
with charachange


li "お聞きしますが、今夜の予定は空いていますか？"



hi "宿題を除けば、そよ風のように自由の身だよ"


show lilly basic_cheerful
with charachange


li "それでは、私と華ちゃんと３人でお茶でもしませんか？"


hi "うーん、今そんなにお金持ってなくてさ、店に行くのはちょっと……"


show lilly basic_smile
with charachange



li "あら、学校の外に行くつもりはありませんよ。今夜ここでやるんです"



hi "この学校は夕方に教室に入れるのか？"

show lilly basic_giggle
with charachange



li "いえ、そうではなくて、華ちゃんと私はよく私の部屋で一緒にお茶会をやるんですよ。夕方になったらぜひいらしてください"



hi "わかった。それは大丈夫だけど、部屋番号は何番？"

show lilly basic_smileclosed
with charachange


li "２２５号室、２階の２５号室です"


hi "オッケー、了解"

show lilly basic_weaksmile
with charachange


li "ではもう行きますね。やらなくてはならない学級委員の仕事があるんですよ"

show lilly basic_cheerful at center
with dissolvecharamove


li "また今夜、久夫さん"


hi "ああ、また後でな"

hide lilly
with charaexit

stop music fadeout 8.0


"ちょっと待て……俺は放課後に女の子の部屋に招かれたんだよな？　これって大丈夫なのか？"




"ここには門限はあるけど、寮の部屋に誰かを呼ぶことについての規則はまだ聞いたことがないぞ。"




"それでもなお、このお誘いは睡眠不足の脳を活性化させるには充分すぎる。"





"ぬるくなった朝食に、とんでもない刺激が加わった。"


scene bg school_scienceroom
with locationskip




"俺はしぶしぶ教室へ向かうけど、規則を破る可能性に今も少しドキドキしている。"





"なんか、子どもが夜に窓から外へ抜け出す計画を立てたときの感じに少し似てるな。"



"まあそれは少し行き過ぎかもしれないけど、お茶会へのご招待と６時間ほどの授業を比べたとき、どっちがいいものかくらい俺にもわかる。"






"ミーシャと静音はどちらも俺の退屈を紛らわしてはくれない。今日に限って、武藤先生が出した課題をちゃんと終わらせようとしている。"





scene bg school_scienceroom_ss
with shorttimeskip

play sound sfx_normalbell



"とはいうものの、やがて一日は終わりに向かう。"


scene bg school_dormhisao_ss
with locationskip


"俺は部屋に急いで戻り、顔を洗って髪をとかす。ありがたいことに健二には出くわさない。"


scene bg school_dormext_full_ss
with locationchange


"少しして俺は男子寮を後にした。"



label jp_H7:

scene bg school_girlsdormhall
with locationskip

play sound sfx_doorknock2


"俺は時計をもう一度確認しつつ、恐る恐る『２２５』と書かれたドアをノックする。"



li "久夫さんですか？　開いていますから、お入りください"



"ドアの中から聞こえてくるリリーの陽気な声が、俺の緊張を和らげる。"



"日が暮れてから女の子の部屋に招かれるのは初めてだ。"


"たとえこの招待に隠された意味などないのだとわかっていても、その可能性に俺の心は暴れまわるのをやめない。"



"一人の男。二人の女。寮の部屋。ティーセットと共に。"


"こう言うとちょっとアブナく聞こえるな。"


"小さく息をついて心を落ち着かせたあと、この上なく慎重にドアノブを回して扉を開け、部屋の中に頭を突っ込む。"

play sound sfx_dooropen

window hide

scene white
with dissolve

with Pause(0.1)

play music music_one fadein 10.0

scene ev lilly_bedroom:
    truecenter
    zoom 1.1 subpixel True
    ease 15.0 zoom 1.0
with Dissolve(4.0)

window show


"ドアが完全に開くと、俺の目に初めて見るリリーの部屋の様子が飛び込んでくる。"



"家具のほとんどがアンティーク風だけど、むきだしの壁と平面は全くと言っていいほど装飾されていない。部屋の中央にローテーブルが鎮座し、小さなティーセットが静かに乗っている。"






"この部屋の中にある全てのものには決まった置き場所があるようだ。例外を言えば壁際に積みあがっているいくつかの本の山くらいか。"



"刺激を受けているのは視覚だけではない。何かはわからないが、ほのかな香りが漂っているのがわかる。マニキュア、香水、化粧品……『女の子の部屋の匂い』という言葉以外では形容し難い。"


"部屋を一通り見渡すと、俺は二人の女の子に目を向ける。"

scene ev lilly_bedroom_large:
    xpos -130 ypos -400 subpixel True
    acdc_warp 4.0 ypos -600
with flash




"リリーはダークブルーのパジャマを身につけて、先ほどの小さなテーブルの隣に座っている。パジャマの下はショートパンツで、魅力的な白い足をたっぷりと見せつけている。"




show ev lilly_bedroom_large:
    ease 1.0 ypos -300 xpos -830
    acdc_warp 12.0 ypos 0 xpos -830
with None


"リリーの反対側には、控えめな淡いピンクのガウンを着た華子が座っている。"



"両手は足の間にしっかり固定し、背を丸めてうつむいている。まるでガウンの中に隠れようとしているみたいだ。"





"ガウンは華子のサイズより二回りほど大きく見えるし、やろうと思えば簡単だろう。"


"華子の体の上でフランネルの生地が波打って、子どもが親の服を着て遊んでいるように見える。"





"華子が俺の存在を確認するために顔を上げ、わずかな笑みを浮かべかけるけど、本当に笑ったのかわからないほどすぐにそれは消えてしまう。"





show ev lilly_bedroom_large:
    ease 1.0 xpos -130 ypos -400
with None



li "ドアの前に立っていても仕方ありませんよ、久夫さん"


scene bg school_dormlilly
show lilly basic_smile_paj:
    twoleft
    ypos 1.2
show hanagown distant:
    tworight
    ypos 1.17
with locationchange

play sound sfx_doorclose
stop music fadeout 10.0


"俺は後ろ手でドアを閉めつつ、部屋の中に数歩踏み込む。"

show lilly basic_weaksmile_paj
with charachange



li "あらあら、この部屋、三人だと狭いですね。座りませんか？"



"俺は部屋を荒らさないように最大限の努力をしながらゆっくりとテーブルへと歩みを進め、腰を降ろす。"



"あと、腰を降ろす時にリリーの上半身をちらりと見ずにはいられない。"





"視覚を奪われるというのは本当に恐ろしい悲劇だろう。"


show lilly basic_smileclosed_paj
with charachange


li "さて、お茶にしましょうか。華ちゃん、注いでもらえますか？"



show hanagown normal_blush
with charachange



ha "う……うん。ひ……さ……くん、こ……"


show hanagown distant_blush
with charachange


ha "……こう……"

show hanagown worry_blush
with charachange



ha "……こうちゃ……"



hi "もらうよ。手伝おうか？"

show hanagown normal_blush
with charachange


ha "う……ううん、大丈夫"

show hanagown smile
with charachange


ha "ありがとう……"

play music music_dreamy fadein 2.0

show lilly basic_giggle_paj
with charachange




"華子の緊張ぶりを見て、リリーが微笑みをこらえきれずにいる。無理もないなと俺も思う。"



show hanagown distant
with charachange


hi "今日は疲れる日だったのか？"

show hanagown smile
with charachange


ha "う……うん"

show lilly basic_smileclosed_paj
with charachange



"俺はたんすの対面に自分の居場所を確保すると、緊張を解く。"



"左に青を纏ったリリーが、そして右側にはピンクの華子が座っている。"

show teaset:
    xalign 0.5 yanchor 0.5 ypos 0.6 alpha 1.0
    easein 0.5 ypos 0.5
with charaenter


"テーブルの上のティーセットは実用的でありながら、赤に花のモチーフをあしらえたかわいい見た目をしている。"




"それは質素だけど洗練された作りのリリーの家具と比べると奇妙に映る。もしかしたら華子が選んだのかもしれないな。"




"華子が紅茶を注いでいると、わざとではないんだろうけど、ティーポットがカップにぶつかって『カチャ』という音が聞こえてくる。"


show hanagown worry
show lilly basic_displeased_paj
with None

show teaset:
    easeout 0.5 alpha 0.0 ypos 0.6
with Pause(0.5)

hide teaset
with None




"華子がはっと息をのむ。本当に緊張しているに違いない。そんなに心配することでもないのに。"





show hanagown worry_blush
with charachange



"自分の不手際に華子はわななく。"




show lilly basic_weaksmile_paj
with charachange



li "いいのよ、華ちゃん。緊張しなくても大丈夫だから"


show hanagown normal
with charachange




"リリーの安心感のある柔らかな言葉で華子は少し自信をつけたようで、残る２つのカップに手際よく紅茶を注ぐ。"



show hanagown normal_blush
with charachange



ha "どうぞ、久夫くん……リリー"





"華子が俺とリリーの前にカップとソーサーを注意深く置く。こんなサービスも悪くないな。"



show lilly basic_smile_paj
with charachange


li "ありがとう、華ちゃん"


hi "ああ、サンキュー"

show hanagown smile
with charachange


ha "ど、どういたしまして"

show lilly basic_smileclosed_paj
with charachange


"リリーは手探りで自分のカップを探し、上品に口をつける。"


"俺も同じように紅茶を飲む。俺たちがいつも学校で飲んでいるものより、いくらか良い味だ。"



hi "おいしいな、今までに飲んだ紅茶とはまるで違う……"



show lilly basic_ara_paj
show hanagown normal_blush
with charachange



li "いいのを選んだみたいですね、華ちゃん"


show lilly basic_smileclosed_paj
with charachange




li "よくやりましたね。大胆だったかも知れませんけど"





show hanagown smile
with charachange



"華子の顔に笑顔が二倍になって戻ってくる。"




"やけどの跡が残っているにもかかわらず、華子のはにかんだ笑みは『かわいい』以外の言葉で言い表すことができない。"



show hanagown distant_blush
with charachange


ha "気に入ってもらえて嬉しい……な"


"華子も緊張がとけたようで、カップから紅茶をすすりはじめる。"


label jp_H7a:

$ renpy.music.set_volume(0.5, 1.0, channel="music")
window hide
nvl clear
nvl show dissolve


n "先日のミーシャとの会話を思い出してみる。"



n "華子の振る舞いは心配すべきことなのか、それとも単にシャイなだけか？"



n "今度は今朝のリリーとの会話を思い出す。"


n "二人の華子に対する心配は心からのものだと思うし、俺よりも華子を取り巻く状況をよく知っている。"



n "でも実際、俺にどんな手助けができるっていうんだ？"





n "俺は形成外科医じゃないんだから、華子の外見をどうにかするなんて無理だ。華子をもっと社交的にしてやれるような心理学者でもない。"





n "じゃあリリーとミーシャは一体全体俺にどうしてほしいって言うんだ。"




n "考えると心が折れそうになる。華子とはお互いの意思で、それも速いスピードで友達としての仲を深めているし、そのせいでみんな俺に華子の抱えている問題をすべて解決することを望んでくるみたいだ。"





n "で、俺にはどうすればいいか全くわからない。"




n "この学校の誰も、俺の心臓を治すことはできない、リリーの目も、ここに居る誰のことも。"







n "でも華子と友情を深めていくことは嫌じゃない。今は華子が俺に好意的になってくれているので、俺も華子と一緒に過ごす時間を楽しんでいる。"

$ renpy.music.set_volume(1.0, 1.0, channel="music")
nvl clear
nvl hide dissolve
window show



label jp_H7b:


$ renpy.music.set_volume(0.5, 1.0, channel="music")
window hide
nvl clear
nvl show dissolve



n "\n\n\n\nここまで考えて、俺は朝食の時にリリーから投げかけられた質問を思い出す。"





n "どうして俺は華子の友達なんだろう？"





n "リリーは華子の幸せを心から気にかけているけど、実際俺に華子の手助けができるわけじゃない。"




n "俺が見る限りでは、華子の傷跡は彼女の身体に不具合をもたらすものではないし、今までに出会ったどの人も、それぞれある程度は自分の障害を克服している。"





n "俺は何か魂胆があって華子と一緒にいるわけじゃない。ただ単に趣味が近いってだけだ。"






n "\nそれで十分じゃないのか？"

$ renpy.music.set_volume(1.0, 1.0, channel="music")
nvl clear
nvl hide dissolve
window show




label jp_H7c:

show lilly basic_smile_paj
with charachange


li "久夫さん、楽しんでいますか？"



"リリーの言葉で、俺は物思いから現実に引き戻される。自分がどこにいるのかを認識するのに数秒かかる。"




"寝間着を着た二人の女の子と一緒に部屋の中にいるんだ。楽しまなくてどうする。"



hi "ああ、リラックスしてるよ。もう学校の中じゃないみたいだよ。こういうのはちょくちょくやってるのか？"


show lilly basic_weaksmile_paj
with charachange


li "ええ、頻繁に。さすがに学校でお茶を飲む頻度には劣りますが"


"ほぼ毎日学校でお茶会を開いている二人を見れば、驚くことじゃない。"



"俺はもう一口飲もうとカップを覗き込むけど、残念なことに、空になってしまっていた。"



hi "おいしかったよ。ありがとう、華子、リリー"

show hanagown smile
with charachange


ha "どういたしまして"

show lilly basic_smile_paj
with charachange


li "はい、どういたしまして、久夫さん。三人目のメンバーが増えて嬉しいです"



hi "えーと、その席を埋める人が必要になったら、いつでも呼んでくれよ。いつでもだ"



"こういう状況だ、大事なことはちゃんと念押ししておかないとな。"


stop music fadeout 8.0
show lilly basic_sleepy_paj
with charachange



"リリーがあくびを漏らす。手で口を覆うけど隠し切れていない。"


show lilly basic_weaksmile_paj
with charachange



li "ごめんなさい、少し疲れているみたいです"


show hanagown distant
with charachange


ha "みんなそうだと思う……"

show lilly basic_ara_paj
with charachange



li "あらあら、今夜は良く気がつくのね、華ちゃん"



show lilly basic_weaksmile_paj
with charachange


li "本当に寝たほうがいいですね、明日も授業がありますし"


hi "うん……そうする"

show lilly basic_smile_paj
with charachange


li "いらしてくれてありがとうございました、久夫さん"

show hanagown normal
with charachange


ha "あ……ありがと。また来てくれる？"



hi "万難を排して参上するよ"




show lilly basic_cheerful_paj
with charachange


li "その決意に感動しました。久夫さん"



hi "どっちにしろ、リリーの言うとおりだ。もう帰ったほうがいいな"



"俺は立ち上がると、ドアのほうへ向かう。"

show hanagown normal at tworight
with dissolvecharamove


"華子が俺の後ろで慎重に立ち上がる。"


"俺は立ち止まり、華子に顔を向ける。"


hi "一緒に来るのか？"

play music music_comedy fadein 0.5

show hanagown normal_blush
with charachange


"華子が途端に真っ赤になる。"

show hanagown distant_blush
with charachange


ha "ちが……私……違う……この部屋……じゃなくて……"


hi "わかってるよ、ただの冗談だ"

show hanagown smile
with charachange


ha "あぅ……うん……おやすみ……"

show lilly basic_smileclosed_paj
with charachange


li "おやすみなさい、華ちゃん。久夫さんも"


hi "おやすみ"


"そうして、お茶会はお開きとなった。"

scene bg school_girlsdormhall
with locationchange



"俺はまだ、リリーが俺に華子のために何をしてほしいのかがわからないでいる。でもリリーを失望させたくはない。"



"ドアが後ろで閉まるのを待ってから、俺は華子へと向き直る。"

show hanagown distant_blush
with charaenter


hi "なあ華子、前に言ったろ？　俺と一緒にいるときには気を張る必要なんかないって"


hi "つまりだな、俺たちは友達じゃないか。な？"

show hanagown normal_blush
with charachange


ha "う、うん。友達……だね"



hi "もし遊んだりしたくなったら、俺に言ってくれよ。チェスの再戦だってしなきゃいけないだろ？"


show hanagown distant
with charachange


ha "う、うん……"

show hanagown normal
with charaenter



ha "で、でも、久夫くん……勝てないと思うけど……"



hi "簡単に勝てちゃったらつまらないだろ"

show hanagown smile
with charachange




"華子は抑えた声で笑ったように見えたけど、単に息を吐いただけかもしれない。"







ha "お、おやすみ、久夫くん……"


show hanagown invis at tworight
with Dissolvemove(0.5, time_warp=_ease_out_time_warp)

hide hanako
with None

stop music fadeout 5.0


"そういうと華子は急いでリリーの部屋の隣にある自分の部屋に戻る。"



"俺も自分の寮へと歩き始めるけど、歩くという単純な行為さえ俺の体力を奪っていくように感じる。"



scene bg school_dormhisao
with locationskip



"かろうじて自分の部屋にたどり着くと、疲労感の波が押し寄せてくる。"


play sound sfx_switch

scene bg school_dormhisao_ni
with Dissolve(0.2)



"靴を脱ぎ、ベッドに倒れこむ。枕に頭が触れる頃には、もう夢の世界へと旅立っていた。"


scene black
with dissolve


label jp_H8:

scene bg school_dormhallway
with locationchange



"自室を出てドアを閉める。今日の授業の準備は万端だ。"




show kenji invis at twoleft
with None

show kenji neutral_close at center
with Dissolvemove(0.5, time_warp=_ease_in_time_warp)


ke "よく寝てるか？"

play music music_kenji fadein 0.5


"健二がいきなり現れたので俺は飛び上がってしまう。かろうじて健二と頭同士をぶつけそうになるのを回避する。"





"健二の視力はとても悪い。でももう俺のことはわかっている。だったらこんな近くに立っている必要はあるのか？"






show kenji neutral
with charadistant


hi "ああ、うん。赤ちゃんみたいにな"

show kenji tsun
with charachange


ke "ふん、なんでみんなそう言うんだ？　寝ている赤ん坊を知らないのか？"




ke "奴らは泣き叫ぶんだ。一晩中。毎晩だぞ。赤ん坊がよく眠ることなんてないんだよ、決してな"




"あーあ、俺の安息はどこかに行っちまった。二度と健二に比喩表現を使わないようにしないとな。"



hi "あーわかった、わかったから。もののたとえだよ"

show kenji neutral
with charachange



ke "ああ、まあ、なんでもいいや。昨日の夜はどこに行ってたんだ？　頼みごとがあったのに、どこにもいなかったじゃねえか"





"一瞬、華子とリリーと一緒にいたという真実を言おうかと考える。"




"ありがたいことに、その一瞬はその名の通り瞬く間に過ぎ行く。"


hi "出かけてただけだよ。このあたりを散策してたんだ。ほら、『偵察』だ"


show kenji happy
with charachange



ke "上出来だ、よくやったぞ。やっぱりお前は計画性のある奴だったな……"



hi "ところで、頼みごとってなんだったんだ？"

show kenji neutral
with charachange


ke "食い物をテイクアウトしようと思ってな、金が必要だったんだ"



hi "待て、なんだって？　お前、先週貸した金もまだ返してないじゃないか！"


show kenji tsun
with charachange


ke "チッ、お前はいいやつだと思い始めていたのに"



"健二はポケットをまさぐり、財布を取り出す。"



"健二が俺に借金している４００円を数えて出す時に、財布の中に少なくとも１万円札が２枚あるのが見える。"




hi "おい、どういうことだ？　なんでそんなに金があるのに返さないんだよ"



"金を持っていることを見とがめられて、健二は不満そうに小さく『シッ』と舌を鳴らす。"






ke "お前には関係ねえだろ。額面の半分以下の買い物をするのにデカい札を崩すのは縁起が悪いんだ。それが資本家のルールだ"




ke "昨日の夕飯のおかげで俺は７年不運になるんだ。７年だぞ！"



show kenji happy
with charachange



ke "誰かを助ける理由には十分だと思わないのか？　そのブツをただ盗んだとしても、そっちの刑のほうがまだ短いんだぞ"



"俺の中の常識が健二に何か言い返せと叫ぶけれど、ありがたいことに俺はそれを抑え込む。"



"この類のことを健二と議論しても、余計に会話がこんがらがるだけだ。"



hi "ああ、まあそうかもな。金については、もう少しよく計画を立てたほうがいいんじゃないか？"


show kenji neutral
with charachange




ke "ああ、わかってる。でもやることがあまりに多くてな、大変なんだ。それに最近お前が全然いないから、俺一人でやるしかないんだよ"





ke "俺たちは同志の中の同志だろ？　覚えてるか？"


hi "ああ、うん、わかってるよ。世界的陰謀とかなんとか。噂には敏感であろうと思ってるよ"

show kenji neutral_close
with charachange



"健二はニンニクが腐ったような息の臭いがはっきり感じられるほど近くに近づいてくる。"



show kenji tsun_close
with charachange




ke "まったくだぞ、お前。最近留守にしてばっかりじゃねえか。これは奴らが最初にやる手口だぞ"




ke "奴らは俺たちを分裂させようとするだろう。分裂させて征服せよ。孫子の言葉だ"


hi "オーケー、よくわかった。さて、もう行かないと。授業があるからな。お前は行くのか？"

show kenji neutral_close
with charachange



ke "いや、疲れたし。あの札を崩しても何も起こらないことを確かめるのに徹夜してたからな"



hi "了解。相変わらず合理的なことで"

show kenji tsun_close
with charachange



ke "まあな。おやすみ"


stop music fadeout 3.0

show kenji invis at twoleft
with Dissolvemove(0.5, time_warp=_ease_out_time_warp)



"健二は急ぎ足で自室に戻る。俺が廊下を下っていると、奴が鍵をかける音が聞こえてきた。"




label jp_H9:

scene bg school_dormhallway
with None

scene bg school_scienceroom
show muto smile at center
with shorttimeskip

play music music_daily fadein 4.0


mu "……そのようなことから巻き舌ができない人がいたり、その人たちの足の人差し指が親指より長かったりするわけだ"


"武藤先生が自信たっぷりに劣性遺伝子の説明をしながら微笑みを向けてくる。"


"でも先生が俺たちを定義する科学にいくら感動したところで、教室内は昏睡状態のようだ。"



"世界で一番面白いことであっても、説明が下手くそだと何の価値もないように見えてしまうのはどうしてだろう？"




show muto irritated
with charachange



"先生がここ３０分で自分が話したことが全く伝わっていないことに気がついて肩を落とすのが見える。"


$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 4.0


"コソコソ話が始まり静寂を破ると、雪崩のようにその音量が大きくなっていく。"

show muto normal
with charachange



"心が折られた先生は教科書から問題をいくつか指定すると黒板を消し始める。"


hide muto
with charaexit



"皆が談笑を始めるころには、ほとんど予定していたかのように華子は荷物をまとめて教室を出て行く。"






"初めてこんな露骨に授業をサボるのを見たときの衝撃は薄れてしまったけど、今でも驚きがないわけではない。"




"華子は話しかけられたくないから教室を出て行くのか？　それとも単に周りの人間の考え方が彼女の平穏を壊すのか？"


play sound sfx_normalbell
$ renpy.music.set_volume(1.0, 4.0, channel="ambient")




"それ以上考える前に、昼休みの鐘が鳴る。華子は単にこの機会を利用して早退しただけなのだろうか。"








"生徒たちが教科書と昼飯を入れ替えるいつもの喧騒が教室内に反響し、ミーシャの気がそれている間に、俺は昼飯を手にしてドアの外へ向かう。"


stop ambient fadeout 1.0

scene bg school_miyagi
show lilly basic_smileclosed:
    center
    ypos 1.2
with locationskip



"既にリリーがいつもの紅茶の部屋で一人で昼飯を広げて席についている。"






hi "あれ、華子はいないのか？"

show lilly basic_smile
with charachange



li "あら久夫さん、こんにちは。あいにく、華ちゃんとは今朝以来会っていないんですよ"



"そうだ、華子とリリーは部屋が隣同士だった。"



"同じ『朝の会話』なのに、リリーたちのそれは健二の散漫な演説に比べてもう少し落ち着いたものだと感じるのはなんでだろう。"



hi "おかしいな。先に授業を抜けていったから、ここに来てるものだと思っていたんだけどな"

show lilly basic_displeased
with charachange


li "やっぱりまだ早抜けしているんですか……"


hi "へ？　ああ。今までに何回か見たな"

show lilly basic_sad
with charachange

stop music fadeout 7.0


"リリーが少し頭を垂れる。その声のトーンは明らかに下がっている。その様子は『またですか』と言わんばかりだ。"



li "久夫さんと友達になってしまえば華ちゃんは早抜けをやめるだろうと私は確信していたんです"

show lilly basic_weaksmile
with charachange



li "まあ、人には皆、自分のペースがありますよね"




hi "ああ、俺も今日、ちょうどそのことが気になってたんだ。華子が早抜けする具体的な理由はなんなんだ？"

show lilly basic_reminisce
with charachange



li "確信があるわけではないんですが、華ちゃんは誰かの質問に答えなくてはならない状況に居たくないのでは、と個人的には思いますね"







"初めて華子と出会った時のことがフラッシュバックする。あのとき俺は華子が追いつめられた動物のように見えていた。その考えは完全に間違いってわけじゃなかったのかもしれないな。"





hi "でもリリーと話しているときは大丈夫そうじゃないか。俺とのときも……ほんの少しだけは……"

show lilly basic_displeased
with charachange




li "それほど単純ではないんです。たいていの人は、華ちゃんにまず傷跡のこと、そして何があったのかを尋ねるだろうと思います"








li "華ちゃんは私に傷跡の話をほとんどしませんが、そのとき起こったことを思い出したくないのだということはわかります"


show lilly basic_reminisce
with charachange


li "授業の早抜けや話し合いから逃げ出すのは言うなれば、先手を打っているようなものなんです"



hi "うーん……じゃあ俺と話してることはどう説明すればいいんだ？"

show lilly basic_weaksmile
with charachange


li "久夫さん自身が昨日の朝食の時に言っていたじゃないですか。華ちゃんの傷跡に気づかないようにした、と。華ちゃんは久夫さんが傷跡のことを何も聞こうとしなかったのを見て、心を開いたんです"



hi "ふむ、リリーの言う通りかもね。たぶん。わからないや。リリーのほうが華子のことをよく知ってるし、リリーの言うことを信じるよ"


play music music_normal fadein 3.0

show lilly basic_giggle
with charachange


li "それについては心配していませんよ。きっとじきに私と同じくらい華ちゃんのことがわかるようになりますから"

show lilly basic_smileclosed
with charachange



li "華ちゃんが新しい友達を持つことは大歓迎です。二人ともとてもよく似た趣味を持ってますし……"




hi "まあ、読書はチームでやるもののうちには入らないと思うよ。ただ仲間がいるっていうのはいいもんだね"




show lilly basic_smile
with charachange



li "それです。華ちゃんは実際にはまだ普通の子なんです。時にはそういう仲間が欲しいはずです"




hi "うーん、わかった。そうだな。正直言って二人には今でもちょっと戸惑うことがあるよ"


show lilly basic_smileclosed
with charachange



li "当たり前ですよ、久夫さん。私たちは知り合ってまだほんのわずかですから。私たちが久夫さんのことを理解できないのと同じで、久夫さんが私たちのことを理解してくれると期待するのには無理があります"


show lilly basic_weaksmile
with charachange


li "だけど、それも友達になることの楽しみのうちですよね？"


hi "ああ、そうだね"

show lilly basic_giggle
with charachange


li "とはいえ……私たちが異性であることの問題もあると思います。本当に、男性と女性はいつも互いを惑わせるみたいです"




"ちょっとした人生のおかしさに慰みを見いだしたのか、リリーは軽く笑いながら言う。"





show lilly basic_cheerful
with charachange



li "もし差し支えなければ、私はお昼を食べますけど"




hi "ああ、どうぞどうぞ。俺も食べるとするかな。午後の授業が始まる前に図書室に返したい本があるから、急がないと"


show lilly basic_smileclosed
with charachange



li "たぶん華ちゃんもそこで見つかると思います。もし見かけたら、今夜私の部屋に来るように言っておいていただけないでしょうか？　華ちゃんとお話がしたいので"



hi "リリーは図書室に来ないのか？"


show lilly basic_weaksmile
with charachange


li "残念ですがこのあと学級委員の会議があるんですよ。なので、食べ終わったらすぐにそちらに行かなくてはなりません"





hi "了解。じゃあもし図書室で華子を見なかったら教室で言っておくよ。華子も昼休みが終わったら教室に戻ってると思うし"


"俺たちは食事を再開し、部屋の中には沈黙が落ちる。俺は今の会話について少しのあいだ思いをめぐらす。"



"俺はいつも、華子の内気な性格は彼女がその傷跡を気にし過ぎているせいでそうなっているのだと思ってきた。"


"だけど、それは華子に対する極めて表面的な見方だ。"



"リリーと華子の心の霧の向こう側を見ることができたと思ったまさにそのとき、俺は最初よりもさらにわからなくなっていることに気がつく。"




"リリーは会議を強く意識して手早く昼食を食べ終え、俺もそれを咎めない。"





"間違いなく静音も会議に出ているだろう。リリーがまた静音に議論を仕掛けられることを望んでいるとは思えない。"




show lilly basic_smile
with charachange



li "もう行かないといけません。明日もこの時間に？"




hi "同じ時間に、チャンネルもそのままさ。俺もそろそろ行ったほうがいいな、遅刻するのは避けたいし"


show lilly cane_smileclosed
with charachange

show lilly cane_smileclosed at center
with charamove

stop music fadeout 4.0


"リリーは優しく微笑むと、杖を手に取り廊下へと出て行く。"




label jp_H10:

scene bg school_hallway2
with locationchange




"俺はリリーに背を向け互いに反対方向へと向かう。どういうわけか、リリーがまた静音とけんかをしなければいいけどと願っている自分に気づく。"





"リリーは大切な友人だと思っているけど、静音とミーシャも俺が山久に慣れるのを大いに手助けしてくれている。たとえ会話の半分が見え透いた生徒会への勧誘だったとしてもだ。"






"でも、俺はリリーのことも静音のこともほとんど知らない。もしかしたら二人は以前なにかの秘密結社の指導者で、でもお互いへの愛が二人を引き裂いてしまって……"






"まったく、安っぽいフィクションを読むのはやめなきゃだめだな。脳が腐る。そうでなければ、健二とあいつが及ぼす悪影響から距離を置かないと。"



"もはやこの２つを区別できないのが悲しい。"

scene bg school_library at right
with locationskip

play music music_happiness fadein 2.0



"借りた本を返却ポストへ入れると、中のカートにぶつかって小気味いい音を立てる。"


play sound sfx_impact2

show yuuko panic_up
with vpunch



"しかし優子さんは俺と同じようには感じなかったみたいだ。"





yu "な、中井くん！　脅かさないで！"



hi "すいません、慣れてるものだと思って。それとも山久の生徒の読解力が低すぎるせいで誰も本を借りないとか？"

show yuuko worried_up
with charachange



yu "へ？　ここの生徒はみんな字は読めると思うけど……"



hi "ああ……忘れてください"




"勝ち目がない戦いというものがある。冗談を説明するのはそのひとつだ。そのことは自分の父親に思い知らされた。"





hi "ところで、優子さん。華子を見ませんでしたか？　授業を早抜けしてたんですけど、いつもの隠れ家に居なかったから"


show yuuko closedhappy_down
with charachange



yu "昼休み前にこっそり入ってくるのを見たと思うんだけど……"



show yuuko panic_up
with charachange



yu "あっ！　でもそんなこと人に言っちゃいけないんだった！"






hi "俺はただ『華子が出て行くのを見た』って言っただけです。そんなに慌てなくても大丈夫ですよ……"








show yuuko smile_down
with charachange



yu "あ……そうだね。華子ちゃんならたぶん奥の方にいると思うわ"



hi "ありがとうございます。最近新しい本は入りましたか？"

show yuuko worried_up
with charachange



yu "ううん、ごめんね。でも、もし新しいものが入ったら教えるから"



hi "はい、お願いします"





"俺が司書について知っていることが１つあるとすれば、その人がバイトであれ何であれ、自分たちの仕事に心から興味を持っている人間を理解してくれるということだ。"





hide yuuko
with charaexit

show bg school_library at Fullpan(10.0, dir="left")
with None



"華子が読書をしている部屋の隅へと続く、今では見慣れた道のりを進む。途中で本を何冊か選び出す。"





"本棚から面白そうな本を見つけるのが大変だと感じることがある。著者名と２語くらいの題名じゃ、似たような単語ばかり並んでいる中ではあまり意味がない。"






"だから俺は時々過去に読んだことのある本を読み直す。初顔よりもお気に入りの馬に賭けたほうがいいってことだ。"




"よく知っている著者だけど、まだ読んだことのないタイトルの本の背表紙が目にとまり、俺はそれを本棚から引き出す。"





"まあ、古い本を読み直すわけじゃないしな。"





scene ev hana_library_read_std
with locationskip



"予想通り、華子はいつものクッションに座り、『ダンス・ダンス・ダンス』という本に頭をつっこむようにして読書にのめりこんでいる。"




hi "よう華子。調子はどうだ？"




"俺はなんで授業を早抜けしたのかを聞きたくなる衝動を抑える。もしリリーの予想が正しければ、逆効果になる可能性がある。"




"さしあたりこのことには触れないでおくのがベストだ。『何も聞かない』というのが、ときには誰かから答えを聞き出すための最善の方法になることもある。"


show ev hana_library_smile_std
with charachange



ha "こんにちは、ひ、久夫くん。元気だよ"





"なんだか違和感を感じて、数秒後にその正体に気づく。華子が微笑んでいる。"



"華子は俺に会えたことに喜んでいるように見える。いつもの本能で怯えているような反応から考えると良い変化だし、俺もお互いをもっと知るためにこれからもその笑顔が見れればいいなと思う。"


hi "そりゃよかった。その本はどんな感じだ？　旅をする物語だってのは聞いたことがあるけど"


ha "お、おもしろいと……思うよ"


ha "よ、読み始めたばかりだから、全部は、わ、わからないけど"


hi "いいよいいよ。読み終わったらどうだったか教えてくれよ。後で俺も借りるかもしれないからさ"


ha "も、もちろん"


"昼休みは１５分残っている。本当に本にのめりこむには少々短いけど、何もしないでいるのは手持ち無沙汰だ。"


show ev hana_library_read_std
with charachange



"華子は既に読書を再開していて、あまり会話をすることは期待できそうにない。"




"まあいいか、俺は俺でくつろぐとしよう。"


play sound sfx_pillow


"俺はソファに座って前かがみになり、自分の持ってきた本を開く。"



"作者のいつも通りの執筆スタイルが１行目から目に飛び込んで来る。文、段落と読み進めるうちに俺は徐々にリラックスしてくる。"


stop music fadeout 8.0



"だけどどう頑張っても、本の雰囲気に浸ることはできそうにない。"



"時間が無いせいでもあるけど、俺の気を散らすより大きな原因は華子だ。"

show ev hana_library_std
with charachange

show ev hana_library_read_std
with charachange




"１０秒かそこらおきに華子が本の上越しにこちらを見てくるのだけど、俺と目が合うと瞬時にカバーの後ろに隠れてしまう。"





"やっぱり華子は俺と何か話したいんじゃないのか。"

scene bg school_library
with locationskip



hi "どうした？　見張り中のプレーリードッグみたいだぞ"


show hanako emb_blushing:
    center
    ypos 1.17
with charaenter


ha "な……なんでもない"


hi "前に言ったよな？　そうやって華子が『なんでもない』って言うときは『なにかある』って"

show hanako cover_worry
with charachange



"体勢を変えることで探している言葉が見つかるのを望むかのように、華子はクッションの中で小さく身じろぎする。"



show hanako emb_downsad
with charachange


ha "じ……事故に遭ったの"


hi "事故？　それって今？　元気じゃないか"

show hanako emb_sad
with charachange


"華子は首を振り、その髪が青白く暗い肌を下地にして、紫色の束となって肩の周りに広がる。"

show hanako emb_downsad
with charachange


ha "う、ううん。ち、小さいときに"

play music music_hanako



"華子が言おうとしていることの意味が、俺の頭にセミトレーラーのごとく殺到する。"




ha "私……私は昔……"


hi "大丈夫だ華子。言いたくないことは言わなくていいんだぞ"


"華子はもう一度首を振る。"

show hanako emb_sad
with charachange



ha "ち、違うの。言いたい、言わなくちゃだめなの"


scene ev hanako_crayon1:
    truecenter zoom 1.0 subpixel True
    linear 20.0 zoom 1.05
with locationskip


ha "私が小さかったとき……火事に遭ったの"


ha "い、家は全焼して、私ももう少しで……もう少しで助からなかった"

show ev hanako_crayon2:
    linear 8.0 zoom 1.05
with charachange


ha "その後……私は一人になって……"

scene bg school_library
show hanako emb_downsad_close:
    center
    ypos 1.1
with locationskip


"華子の瞳が薄暗い図書室の光にきらめいたのを見て、俺はその手を掴もうと手を伸ばす。"



hi "いいんだ華子。無理しなくていいから"


show hanako emb_sad_close
with charachange


ha "で、でも……言わないと……"



hi "なんでだよ？　どうしてそこまでするんだ？"


show hanako cover_distant_close
with charachange



ha "き、昨日の夜、リリーが久夫くんの心臓のこと、話してくれて……"


show hanako cover_worry_close
with charachange


ha "そ、それで私……それじゃ、こ、公平じゃないって思って"


hi "公平？"

show hanako emb_blushing_close
with charachange



ha "私は、ひ、久夫くんのこと知ってる、のに、久夫くんは私のこと知らない……"




"華子の手を少し強く握る。"




hi "ばかなこと言うなよ。だけどそうだな、俺は心臓の病気を持ってる"





"俺は華子のほうに少し体を乗り出す。"



hi "そのことだけど、リリーに言わなかったことがあるんだ。初めて病状が出たのって女の子に告白されたときだったんだよね"



"俺は二人の間の緊張をほぐすために微笑む。"

show hanako cover_worry_close
with charachange


ha "ほ、本当に？"


hi "ああ本当だ。でもそれから音沙汰が無いから、終わったんだと思う"



"間違いなく終わっている。岩魚子と最後に会ったときの出来事は、それ以外に解釈のしようがない。それ以来連絡がなかったことは、ある意味で俺にとってあの日々から先に進む助けになっていた。"





hi "さて、お互いに少しは知ってることが増えたな。でも言いたくないことは言わなくていいんだぞ"




"実際、俺だってこれまであった出来事全てを思い出すと少々気分が悪くなる。鼻の裏側を燃やすような病院の消毒の臭いがフラッシュバックしてくるかのようだ。"




"華子も今同じものを感じているだろう。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\n俺は入院していたとき一度、火傷患者の病棟に行ったことがある。本当に一度だけだけど。退屈を紛らわせるために、全ての病棟を歩き回っていたんだ。"



n "腫瘍病棟を通り抜けたときは、耐えられると思ったけど、火傷病棟にたどり着いたとき、俺は回れ右をして自分のベッドに戻った。"




n "ただれた皮膚と強い消毒と殺菌の臭いだけが漂う、そんな場所で華子が何か月も過ごしていたのだろうと思うと。"



n "本当に深刻なケースだと、外部から何も中に入らない隔離カプセルのようなものに入れられ続けることもある。つまり読書はできないってことだ。"




n "\nもし入院中に本がなかったら、俺は気が狂っていただろう。"



n "そして華子は『一人だった』と言っていた……"


n "親は亡くなったのだろうか？　今度リリーに聞いておこう。じゃないと意図せず何かバカなことを口走って地雷を踏むのが目に見える。"

stop music fadeout 2.0

nvl clear
nvl hide dissolve

show hanako emb_timid_close
with charachange

window show


ha "あ、ありがと、久夫くん"


show hanako emb_downtimid_close
with charachange


ha "こ……このこと、ほとんど人に言ったことないんだ"



hi "正直言うと、俺も自分の……体のこと、ほとんど話したことないんだよね"


show hanako cover_smile_close
with charachange


ha "そ、それなら、私も誰にも言わない"



hi "じゃあ約束だ"


play sound sfx_warningbell


"俺が華子の手を握る手を握手の形に変えたと同時に、窓の外から予鈴が聞こえてくる。"


hi "よし、そろそろ教室に戻ったほうがいいな、大丈夫か？"

show hanako basic_bashful_close
with charachange


ha "う、うん"
$ renpy.music.set_volume(1.0, 0.0, channel="music")

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
