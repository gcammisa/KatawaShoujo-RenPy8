label jp_E3:



window hide None

scene black
with dissolve

$ renpy.music.set_volume(1.0,0.0, "ambient")
play sound sfx_alarmclock

window show


"目覚ましがピーッと鳴って早朝の静寂を破る。起きるためのモチベーションをどこから引き出すべきかと悩んでいる自分がいる。"



window hide

scene bg school_dormhisao
with openeye

window show


"授業にはまだかなり早いけど、笑美と一緒に朝練をする約束をしていたんだった。"






"実を言うと、趣味としてのランニングにはあまり興味がない。それどころか、俺の延命のためのトレーニングとしてさえも。"











"でも、昨日の笑美との約束を守る義務があると思って、気づいたらランニング用の短パンと軽いＴシャツに着替えていた。"





scene bg school_courtyard
with locationskip




"冷たい朝の空気が俺の顔を撫で、朝日の光が芝生の上の露にきらめいて、目がくらみそうになる。"





"競技場へ足を運んでいる間、ふと醜い考えが俺の心の中をかすめる。"


"もしこれが、笑美が俺をからかって言った冗談か何かだったらどうしようか？"


"いかにもありそうだよなあ？"




"ちくしょう、俺だって新入り相手なら同じことをするに違いない。"








"少なくとも、笑美と琳は、俺が実際に現れるかどうか賭けをしているに違いない。"







scene bg school_track
with locationchange


"陸上競技のトラックが見えてきて、俺は恐ろしくなってくる。"




show emi basic_annoyed_gym at center
with charaenter

play music music_emi fadein 1.0


emi "遅ーい！"





"笑美はもう来ていたみたいだ。安心したよ。"





hi "時計狂ってるんじゃないのか。むしろ俺たち二人とも早く来たんだ"





show emi basic_closedhappy_gym
with charachange


emi "ちぇっ。ばれちゃったか"





"笑美はランニング用の義足を付けて、幾分根気よく俺を待ちながら観覧席に座っている。"


hi "俺、笑美がここにいるのがマジで嬉しくてさ。冗談か何かだったんじゃないかと心配だったよ"

show emi basic_grin_gym
with charachange


emi "ううん、あたしは意味もなく誰かを早起きさせたりしないもん"

show emi excited_proud_gym
with charachange


emi "それに、琳には５００円の貸しができたからね。琳、久夫くんがここに来るって思ってなかったもん"






"やっぱりな！"





"まあ、少なくとも、笑美が俺を信用する側に賭けてくれたのはうれしい。"



show emi gymbounce_once
with Dissolve(0.1)


"笑美は観客席から飛び降りて、ストレッチ運動を始める。"



play sound sfx_gymbounce

show emi gymbounce
with Dissolve(0.05)


"笑美は本当にしなやかで、まるでダンサーみたいだ。"





"俺も同じようにストレッチをしようとするけど、きちんとしたストレッチ運動の方法を覚えてないことに気づく。"






"先週のランニングのときをのぞけば、もうずいぶん長い間ストレッチなんてやったことがない。"







"それにそのランニングのときだって、事前にストレッチなんてしなかったと思う。"








"入院時代の悪夢がまた脳裏に甦ってくる。"





"もっとも、入院する前は活動的だったとも言えないし、単に俺自身が落ち込んでいるだけなのかもしれない。"




show emi basic_closedgrin_gym at center
with charachange


"笑美は、俺が体を伸ばすのを見てクスクス笑う。"


show emi basic_grin_gym
with charachange



emi "そうじゃないよ久夫くん、もっと長く伸ばしてなきゃだめだよ！"





hi "やろうとしてるって！　ちょっと痛くてさ"




show emi excited_proud_gym
with charachange



emi "あはは、体がなまってるから痛むんだよ。もっと体を柔軟にしなきゃ、ほらこんな風に"



hide emi
with charamoveoutbottom



"お手本を見せつけるかのように笑美は手を伸ばして前屈し、頭を足の間に通す。"




"おいおいマジかよ笑美。"



hi "なるほど。俺もそのくらいできるように努力すべきってことか？"



show emi basic_closedgrin_gym
with charamoveinbottom



emi "もちろん！　柔軟さはランナーにとってすごく重要なんだよ。ストレッチすればするほど、早く走れるようになるよ"








"俺にはさっぱり理解できないけど、笑美はそう信じているみたいだ。"





"笑美の助けで、なんとかストレッチが形になる。"




show emi basic_grin_gym
with charachange



"笑美が説明のしかたを考えるときに集中のあまり口をくしゃくしゃにするのが、つい目に入ってしまう。"




"なんて可愛いんだ。"




show emi excited_proud_gym
with charachange


emi "悪くないよ、久夫くん。行こ、そろそろランニング始めないと"



show emi excited_happy_gym
with charachange




emi "じゃあ軽く１６００からいくよ。いい？"





show emi basic_happy_gym
with charachange



emi "トラックを４周だよ、わかった？"






hi "それでいいぞ"




show emi basic_happy_gym:
    center
    easeout 0.5 xpos 0.4 alpha 0.0 
with None

stop music fadeout 2.0



"そんなにきついってことはない、よな？"





scene bg school_track_on
with locationchange



"体育の授業で４周走ったときの、ぼんやりとした記憶が頭に浮かぶ。"






"そうだよな、そんなに酷いもんじゃなかった。"


play music music_running fadein 0.5

scene bg school_track_running
with Dissolve(2.0)

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

play ambient sfx_emijogging fadein 1.0



"笑美はかなり速いペースを保って走り、俺はその後ろを付いていく。"


$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi basic_grin_gym at left
with charamoveinleft




emi "がんばってついてきてね。いい？　久夫くん"





hi "了解"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with charamoveoutleft




"俺たちは無事に最初のコーナーを回るけど、早くも自分の心拍数が少しずつ上がってきているのを感じる。"






"２つ目のコーナーにさしかかった時には、もう口で息をし始めていた。"





"笑美は汗の一滴すらかいてるようには見えない。"



"自分の優位を見せびらかすように、笑美は振り返って後ろ向きに走り始める。"







$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi basic_closedgrin_gym at center
with charaenter



emi "今のところは順調？　久夫くん"





hi "ぜっこー……ちょー……だ"



show emi excited_proud_gym
with charachange


emi "本当？　じゃあもっとスピードあげちゃおうかな？"








hi "ああ……いや……おまえに……むちゃを……"




hi "……してほしく……ないから……やめて……おこう……"





"ぜえはあと荒い息のせいで、言葉に込めたかった説得力も薄れる。笑美はただにこっと笑って、また正面を向く。"






show emi excited_proud_gym at left
with charamove


emi "じゃあ久夫くんの言うとおりにしようかな。このペースを続けるね"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft


"なんとなく馬鹿にされているような気がする。"




"もしこんな体たらくじゃなければ、たぶん腹を立てていただろう。"






"３周目には、もう息も絶え絶えになっていた。"








"体も汗でびっしょりだ。気持ち悪い。"






"俺たちがコーナーを回り４周目に突入すると、笑美は振り返ってにやりと笑う。"






$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi basic_closedgrin_gym at left
with charamoveinleft


emi "行くよ！"

play ambient sfx_emisprinting

hide emi
with easeoutleft

$ renpy.music.set_volume(0.3, 0.5, channel="ambient")



"俺が頑なに遅いペースで留まる間に、笑美は目もくらむような速さで走り去っていく。"






"俺が最初のコーナーを回り始めるころには、笑美はもう２つ目に入っている。"









"俺がバックストレッチを抜けるのに苦労していると、ペースそのままの笑美が追いつく。"






play ambient sfx_emijogging

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi excited_proud_gym
with charamoveinright



emi "久夫くん、しっかり！　久夫くんならできるよ！"




$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with charamoveoutleft



"返事をしようにも、息を吸うのと足の筋肉が燃えそうなのを無視するのとでそれどころじゃない。"







"『{b}お前{/b}はできるかもしれないけど、こっちは今にも死にそうなんだよ』みたいなことを、心の一部が言いたがっている。"








"といっても、今の俺が実際にそれを言葉として発声できるかどうか。"






"笑美は第２コーナーを回ってゴールラインを踏むまで、俺とペースを合わせてくれる。"






stop ambient fadeout 1.5

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

stop music fadeout 5.0

show bg school_track_on
show emi basic_happy_gym
with locationchange



"笑美は全力疾走で汗ばんだみたいだ。"




"実際そのおかげで笑美のシャツが少し透けている。黒いスポーツブラを着けているようだ。"








"自分が女の子の胸を見つめるような奴だったことに漠然と罪悪感を覚えるけど、俺の足と胸はそれを気にしていられないほどひどく熱くなっていた。"







show emi excited_proud_gym
with charachange


emi "初めてにしては悪くなかったよ、久夫くん"

play music music_happiness fadein 0.5


hi "そりゃ……どうも……"



"笑美は、息を切らせてとは言わないまでも、少なくとも俺たちが走り始める前よりはちょっと息が荒いみたいだ。"








"間違いなくあの全力疾走のせいだ。"


show emi basic_grin_gym
with charachange



emi "ねえ、あたしもう少し全力で走んなきゃいけないんだ。トラックの周りを歩いてクールダウンした方がいいよ"






emi "その後ストレッチして、今日はおしまい。いい？"



hi "そうだな"



"足は火が付いたようだし、まだ息も上がったままだけど、驚いたことに心臓の方はこれまでの負担にも持ちこたえているようだ。"





"ここでも医学の勝利、かな。"




show emi basic_closedhappy_gym
with charachange


emi "頭の後ろに手を置いて。そしたらもっと呼吸がしやすくなるよ"


$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

play ambient sfx_emipacing

hide emi
with charamoveoutleft



"驚いたことに、笑美の言うとおりだ。呼吸がまた落ち着いてくるのはうれしく、俺はゆっくり歩いてトラックを回り始める。"





$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi blur at offscreenright
with None

show emi blur at offscreenleft
with move

$ renpy.music.set_volume(0.3, 0.5, channel="ambient")

hide emi
with None



"目にも止まらない速さで、笑美が俺の横を走り抜ける。"








"笑美の走りにはまったく惚れぼれする。"








"義足をつけているのも興味深いけど、それだけじゃない。"




show ev emi_run_face_zoomin
show ev emi_run_face as unlockstub behind ev
with dissolve



"本当に興味深いのは、その表情の変わりっぷりだ。"





"俺の横を走り抜ける一瞬の間しか見ることはできないけど、笑美の目はなんだか荒々しいまでの喜びで生き生きとして見える。"








"まるで、この世界に笑美とトラックしか存在しないかのようだ。"


stop ambient fadeout 0.5

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

scene bg school_track_on
with locationchange



"俺が最後の直線コースにさしかかったころには、笑美は全力疾走を終えていたようだ。"







"今は笑美も激しく息をしているけど、満足げな笑顔を浮かべている。俺が近づくと、笑美は嬉しそうに手を振る。"




show emi basic_grin_gym at center
with charaenter


emi "気分、よくなったでしょ？"





hi "ああ、ましになったよ"




show emi sad_grin_gym
with charachange



emi "あたしともう一周歩かない？　あたしもクールダウンしなくちゃなんないしさ"







"むしろ座り込んでじっとしていたいと思う部分はあるけど、多分そうしないほうがいいんだろうと感じる。"







"それに、もし座ってしまったら、もう二度と立ち上がれないかもしれない。"







hi "わかった、そうしようか"




"笑美は俺と同じように手を頭の後ろに回し、とてもリラックスしているように見える。"








"腕を上げているせいでシャツも上にほんの少しだけ引っぱられて、笑美のお腹の肌がちらっと見えてしまう。"








"俺は全力で紳士的になってそれを見ないようにするけど、笑美の素肌と赤いブルマのコントラストはむしろとても印象的だ。"







show emi basic_grin_gym
with charachange


emi "で、調子はどう？　久夫くん"




hi "すごくいい、ほんとに。体は痛いし疲れたけど……でもすごくいい"








"俺はそう言うとすぐに、それが本当であることに気づく。"




"もちろん俺の心の中にはすぐにでも寝転がって動きたくないという部分もあるけど、何かを達成したという満足感もある。"






"体の痛みにもかかわらず、満悦感に似た感覚が体中を駆け巡り続けているようだ。"





show emi excited_proud_gym
with charachange


emi "そう、ランナーズ・ハイってやつね"



hi "ランナーズ・ハイ？"

show emi basic_hes_gym
with charachange




emi "うん、確か……アドレナリンが関係してるんだっけ？"








"一緒に歩きながら、笑美は思い出そうとしてちょっと考え込む。"




show emi basic_closedgrin_gym
with charachange


"それから笑美は肩をすくめて、俺に微笑む。"

show emi basic_grin_gym
with charachange



emi "あは、思い出せないや。でも、それ気持ちいい感じだよね"





show emi basic_happy_gym
with charachange

stop music fadeout 0.5
play sound sfx_heartstop



emi "エッチより気持ちいい、でしょ？"






"俺は彼女が何を言ったのか理解する前に、返事をしようと口をあける。"



hi "……"



"笑美は少しの間俺の顔を見つめ、突然笑い出す。"



play music music_comedy fadein 1.0

show emi excited_laugh_gym
with charachange



emi "ごめん、ごめんね！　あたし我慢できなかったの！　久夫くんが単純すぎて！"








hi "お前とまた走るなんて約束しなければよかったよ……"








"笑美はますます大きく笑う。俺の腕をつかんで傾け、腕時計がよく見えるようにする。そして時間を確認するなり笑美の顔色が変わる。"






show emi basic_shock_gym
with charachange


emi "あーっ！　もう行かなくちゃ、久夫くん！"



show emi basic_closedsweat_gym
with charachange



emi "あと一時間で授業が始まっちゃう、シャワーも浴びなきゃ！"







hi "俺もそうしなきゃいけないんだけどな……"


show emi basic_hes_gym
with charachange




emi "ナースくんのところにも行かなきゃいけないし……もしかしたら、遅刻証明を書いてくれるかも！"









hi "なんでナースに会わなきゃなんないんだよ？"

show emi basic_closedgrin_gym
with charachange


"笑美は、それで全て説明がつく、とでも言いたげに自分の義足を指さす。"



show emi basic_grin_gym
with charachange



emi "炎症を起こしてないかチェックするのって大切なんだよ"





emi "ほら、汗とか摩擦とかそんなので起こったりするからさ"


show emi excited_amused_gym
with charachange




emi "いつもは練習の後だけ行けばいいんだけど、もしあたしたちが朝練続けるんなら、一日に二回行くことになるかなあ"








"待てよ、ってことは笑美は俺が来るようになってからこの朝練を始めたのか？"



hi "もし午後の練習で一緒に走る方が笑美にとって楽なら……"



show emi sad_grin_gym
with charachange




emi "バカなこと言わないでよ！　あたし、しばらく前から朝に走ろうと思ってたの"








emi "でもあたし一緒に走る相手がいないと、そういうの続きそうにないしさ"




show emi basic_grin_gym
with charachange



emi "誰かをがっかりさせちゃうって思うと約束を破る気にはなりにくいものでしょ？"




show emi basic_closedgrin_gym
with charachange


emi "だから久夫くんは、あたしの朝のランニングパートナーになるんだよ！"




show emi excited_proud_gym
with charachange




emi "二人とも運動が必要なんだし、それなら一挙両得、って思わない？"









hi "ああ、完璧だな"




"でも、それって俺じゃなきゃいけなかったのか？"



"まあ、それほど文句は言えないな。笑美と一緒にいるとすごく楽しいし。"









"それに笑美は正しい。俺は運動しなきゃいけない。医者からも指示されてるしな。"




show emi basic_happy_gym
with charachange


"笑美は俺にさっと手を振って別れを告げる。"





emi "うん、じゃ行くね！　お昼一緒に食べよう、いい？"







hi "なに？"



show emi basic_closedhappy_gym
with charachange



emi "ごはん！　ほら、食事だよ？　お昼の？　一緒に食べようよ！"








hi "どこで？"


show emi basic_grin_gym
with charachange



emi "屋上。琳がそこ好きなの"





hi "いつ？"


show emi basic_annoyed_gym
with charachange




emi "お昼休み以外にいつ食べるっていうの？　変なこと聞くね"







hi "ああ、でも完璧を期するには３つ全部聞いといたほうがいいと思って"






show emi excited_laugh_gym
with charachange




"笑美は声を上げて笑い、にっこりする。こんなにいっぱい笑う女の子は見たことがない。"






show emi excited_happy_gym
with charachange


emi "悪くないよ、久夫くん、またね！"




play ambient sfx_emisprinting

hide emi
with easeoutleft

stop ambient fadeout 2.0
stop music fadeout 8.0




"そう言いながら、笑美は校舎の方に弾丸のようにすっ飛んでいく。"







"まずナースに会いに行くんだろうな。"






scene bg school_dormbathroom
with locationskip




"俺は急いで部屋に戻ってシャワーに飛びつくけど、水が温まるのには時間がかかることがわかるだけだ。"







play ambient sfx_shower
with vpunch


"冷水のショックで俺は死にそうになる。"


show steam
with Dissolve(2.0)


"なんとか水が温まるのを待ち、筋肉がほぐれるのを感じながら至福の時を過ごす。"







"俺の心臓はあのランニングの後でもほとんど問題ない感じだ。驚いた。"







"たぶん、それはいいことなんだろう。自分がちょっと弱虫みたいな気分になるにしても。"







"心臓がおかしければ、少なくとも単に『体がなまってる』よりは立派な言い訳ができるんだし。"






"この朝練は続けなくちゃならないんだろうな、でなきゃ笑美にいつまでも文句を言われる。"










"服を着て授業に行くまでにあと１０分しか残っていないと気づいたのは、シャワーから出て体をふいた後だった。"







"くそ。"




label jp_E4:

scene bg school_dormbathroom
show steam
with None

stop ambient fadeout 1.0

scene bg school_scienceroom
with shorttimeskip

window show

play sound sfx_normalbell



"時計の針はようやく、楽しいたのしい授業の退屈さから今回も俺を自由にしてくれる。"






"自分の席から立ち上がるだけのことが、思ったより大問題だとわかる。"






"朝練から足が痛くてしょうがない。"




"結局、笑美との朝練はあまりいいアイディアではなかったのかもしれない。"







"それでも、朝練のせいで腹だけはやたらと減っている。"




play ambient sfx_crowd_indoors fadein 1.0

scene bg school_hallway3
show crowd
with locationchange



"食堂への廊下の途中で、俺は弁当を持ってきていたことを思い出す。"





"こっちに越してくる時に、うちの親がいくつか出来合いの食品を持たせてくれていた。ありがたいことだ。"





"廊下は、食堂に向かう学生でごった返している。"







"ここを引き返すのは流れに逆らって泳ぐようなものだ――けど、俺には屋上に行く約束がある。"




stop ambient fadeout 4.0

scene bg school_staircase1
with locationchange




"屋上への階段を探すのに時間がかかるけど、どうせまだ笑美と琳は屋上に行ってないだろう。"






"事実、廊下の人ごみの中で笑美が食堂に向かってたのを見たと思う。"


play sound sfx_door_creak
$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 0.5

scene bg school_roof at bgright
with locationchange



"俺はドアから屋上に出て深呼吸する。"




"新鮮な風が顔や体に吹いてきて、足の痛みも和らぐようだ。"



show rin basic_awayabsent at center
with charaenter


rin "さかさまになれば……"


$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_rin fadein 1.0



"琳がもう上がってきていたことに、心のどこかで驚いている自分がいる。"




hi "さかさまだったら何ができるんだ？"


show rin basic_deadpan
with charachange


rin "夢みたいないろんなこと"





hi "それって……普通に上向きじゃだめなのか？"






show rin basic_deadpanupset
with charachange


"琳は激怒に近い雰囲気であきれ顔をする。"





rin "それじゃ、あたらしい物の見方を得られないよ"






hi "さかさまってほんとにあたらしい物の見方なのか？"



show rin basic_delight
with charachange




"おっ！　今の質問は琳の不意を突いたみたいだ。琳は考えこんでいるように見える。"





rin "一理あるかもしれないね。横でもいいのかも"



hide rin
with charamoveoutbottom


"琳が空を見ようとベンチの上に横たわったので、俺は諦める。"


play sound sfx_impact2
with vpunch

show emi basic_closedgrin at center
with charaenter




"ちょうど運よく、笑美が袋を２つ抱えてドアから飛び出してくる。"







"もう少しでドアを外しそうな勢いだ。"




show emi basic_hes
with charachange




emi "ほんと遅くなってごめんね！　列にすごいたくさん人がいたの"




show emi basic_grin
with charachange

show emi basic_grin at twoleft
show bg school_roof at center
with charamove



"笑美は琳の前に袋をひとつ置いて、隣に腰掛ける。"



hi "いつも琳の昼飯を買いに行ってやるのか？"



show emi basic_closedgrin
with charachange




emi "ときどき、ね。お返しに琳にも行ってもらってもいいんだけど、どうやって持ってくるのかわかんないし"





show rin basic_deadpan at tworight
with charamoveinbottom





rin "それに、私は笑美の分は絶対買わないし"







"琳は笑美の言葉に怒ってるのかもしれないけど、表情には出していない。笑美は鼻であしらって言う。"


show emi basic_annoyed
with charachange



emi "ほんと恩知らずよね"






"二人は冗談を言い合ってるのか、それとも俺はキャットファイトの始まりを目の当たりにしてるのか、俺にはよくわからない。"





show emi basic_closedgrin
show rin basic_amused
with charachange



"二人が見つめ合って少しのあいだ緊張が走るけど、急に微笑みに変わる。"



show rin basic_awayabsent
with charachange



rin "ねえ笑美、さかさまになるのはあたらしい物の見方だと思う？"





"この話ってもうしなかったっけ？"


show emi basic_hes
with charachange


"笑美は考え込んでるように見える。どうも答えを考えているみたいだ。"



"深く重い沈黙の後、笑美は言う。"


show emi basic_closedsweat
with charachange



emi "わかんない"




"やれやれ、笑美も俺と同じくらいには見当つかないか。"



stop music fadeout 4.0

show emi excited_happy
with charachange


emi "ねえ久夫くん、今度の陸上競技会に来てくれるよね？"



"いきなりの質問に不意を突かれる。"




hi "うーん……まだわかんないけど？"


show rin basic_absent
show emi sad_annoyed
with charachange



emi "まったく、久夫くん、あたしは朝いっしょに走って久夫くんの面倒ぜーんぶ見てあげたのに、久夫くんはあたしの陸上競技会に来てもくれないんだ？"



show rin basic_awayabsent
with charachange


"一緒に走ってって頼んできたのは笑美のほうじゃなかったっけ？"







"実際、笑美は選択の余地なんてまったく与えてくれなかった。"






hi "待った、違う、そんなことは言ってなくて……"





play music music_ease fadein 3.0

show emi basic_closedgrin
show rin basic_absent
with charachange




"俺から１億円もらえることになったみたいに、ぱっと笑美の顔が晴れる。"





show emi basic_closedhappy
with charachange



emi "じゃあやっぱ来るんだ！　やった！"


"そんなことも言ってない！"



show rin basic_deadpan
with charachange



rin "笑美、私も行くから、久夫が必ず来るよう念押ししとく"




show emi basic_grin
show rin basic_absent
with charachange



emi "それいいね、琳！　終わったらご飯食べたりとかできるかも？"







"どうもハメられたような感じがする。でもこの二人にってわけじゃない。"






"むしろ何か外部からの力が、後戻りのできない運命へと俺を押しやっているかのような。"






"……いや、陰謀論の特集本なんかを読みすぎるのはやめたほうがいいのかもな。でないと健二みたいなことを言い始めるはめになりそうだ。"






"それでも、競技会には行かなきゃいけないと思い始めている。"





"笑美と琳の両方を失望させるなんて耐えられる気がしない。"





"永遠に恨み節を聞かされ続けるだろう。"





hi "競技会っていつだっけ？"




show emi basic_annoyed
with charachange



emi "もう、来週だよ！　あたし２、３日前に言ったはずだよ"





hi "言ってないよ"


show emi sad_shy
with charachange





emi "あたし言い忘れた？　うーん、でも競技会には忘れずに来てくれるでしょ、ね？"








hi "忘れないって！　カレンダーか何かにだって書いといてやるよ！"



show rin basic_lucid
with charachange



"琳はわけ知り顔でうなずく。"



show rin basic_deadpancontemplation
with charachange



rin "それはたぶんいい考えだね。時間がその流れを変えない限りは"



show emi basic_confused
with charachange


emi "そんなことあるの？"


show rin relaxed_nonchalant
with charachange


"琳はあいまいに肩をすくめる。"

show rin negative_spaciness
with charachange



rin "まだ起きたことはないけど、実際はわからないよ……"



show emi basic_closedgrin
with charachange


"今度は肩をすくめたのは笑美のほうだった。"


show emi basic_closedhappy
with charachange


emi "そんなことが起きたらどうしようもないよね"


show rin basic_deadpannormal
with charachange



rin "タイムトラベラーかなにかでもなければね"





hi "本気でそんなことがありうるなんて思ってないよな？"


show emi basic_confused
with charachange




emi "思ってない……よねえ？"


show rin relaxed_nonchalant
with charachange



"琳はまた肩をすくめる。こいつは何に対してもこういう反応をするみたいだな。"



show rin basic_deadpandelight
with charachange




rin "思ってないよ。でも意見を一瞬で変える権利は留保してるからね"








"琳にしては、不気味なくらい筋が通ったことを言う。"






"それに気づいたことが少し恐い。"




"笑美はいつもこんな気分を味わってるのかな。"


show emi basic_closedgrin
with charachange



"だとしても、笑美はそれを表に出してはいない。単にうなずくだけだ。"



show emi basic_grin
with charachange



emi "やっぱりね"


show rin basic_deadpanupset
with charachange



rin "どういうこと？"


show emi sad_grin
with charachange



"今度は、肩をすくめたのは笑美だった。"





"まるで琳の武器を当の琳自身に対して使ってるみたいだ。"



show emi excited_proud
with charachange



emi "琳の返事が思ったとおりだったってだけだよ"


show rin negative_worried
with charachange




rin "私、ほんとにそんなに予想できる感じかな？"





show emi basic_closedgrin
with charachange



"笑美は、ほくそ笑みに近い笑顔を浮かべているように見える。"






emi "ううん、予想できないとこが、予想できる、ってだけ"




show rin relaxed_nonchalant
with charachange



rin "ならいいや"



play sound sfx_warningbell



"予鈴が鳴って、俺は琳が本気かどうか確かめる機会がなくなる。"




"昼休みが終わりそうなことに全く気づかなかった。"


"二人と一緒に過ごすのが面白すぎたんだ。"


show emi basic_shock
with vpunch


"笑美は飛び上がり、驚いた表情になる。"



emi "いっけない！　あたし、次の授業で使うノートを部屋に置いてきたから行かなくちゃ！"


show rin basic_deadpandelight
with charachange



rin "今ならタイムマシンがあったらいいのにって思うでしょ？"






"琳はずいぶん得意そうな顔で言う。ちょうど今議論に勝ったみたいに。"






"笑美はそれを無視する。"



show emi basic_hes
with charachange



emi "ごめんね久夫くん、あたしたちのゴミ捨てといてくれる？"



show emi basic_closedsweat
with charachange



emi "いつもは自分で片づけるんだけど、急がなきゃなんないの！"





hi "もちろん、かまわないよ"

hide emi
with easeoutleft



"笑美があわただしく走り去るのもお約束に思えてきたな。"



hide rin
with charaexit



"琳になぜ手伝わないのかと聞いたりはしない。もう琳は何か他のものに夢中みたいで、どこかへ行ってしまう。"




"たぶん、笑美に片づけてもらうことに慣れているんだろう。それになぜか、笑美もそこに異議を唱えたことがあるとは思えない。"






"後片づけにはそんなに時間はかからず、ゴミを捨てて授業へ向かうのに十分な時間があった。"




stop ambient fadeout 1.0

scene bg school_scienceroom
with locationskip



"俺がドアを通ると、ミーシャが手を振りながらよこしまな笑顔で出迎える。"


show misha cross_grin at center
with charaenter


mi "食堂では見なかったね、ひっちゃん"




hi "ああ、あそこは混むからやめた"


show misha hips_grin
with charachange



"ミーシャのにやにやが広がる。"




mi "ホントにぃ～？　何かふ・じゅ・んな異性交遊とかしてなかったって断言できる～？"






hi "な……何だよ？　何言ってんだよお前？"

show misha sign_smile
with charachange




mi "屋上にいたよね？　琳と笑美といっしょだったよ絶対！　もう、この女ったらしってば～！"






hi "お……俺たちは昼飯食ってたんだ、それだけだよ！"





show misha cross_laugh
with charachange


"ミーシャが急に笑い出すと、何人かのクラスメートの注目の的になる。"



mi "わははは～！　そうやって赤くなるのすっごいかわいいね、ひっちゃん～！"


show misha cross_grin
with charachange


"ミーシャは俺に陰謀めいたウインクをする。"

show misha cross_smile
with charachange



mi "心配しなくていーよ、ひっちゃんの隠しごとはあたしの心にしまっておくから"




hi "隠しごとなんかねーよ！"


show misha perky_confused
with charachange


mi "えっ？"



"ミーシャはがっかりしたみたいだけど、すぐまた晴ればれとした顔になる。"



show misha hips_grin
with charachange



mi "そのうちわかるよね～！"





"お前は何を言っているんだ。けど幸い、先生が教室に入ってきて授業が始まる。"



stop music fadeout 2.0
label jp_E5:

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell



"ある日の授業もようやくながら終わった。"





"期待はしてなかったけど、丸一日起きていることができた。"






"これはちょっとした奇跡と言っていいな。"




"俺の足はしばらく立ち上がる気がないようだ。"




"たぶん、朝練でやられたんだろう。"


scene bg school_hallway3
with locationchange


"俺は廊下へ出て自室へと向かう。"

scene bg school_dormhisao
with locationskip



"机に向かって、気乗りしないまま宿題をしばらくちまちまと進める。まるでハゲタカがクソまずい死体をつつくように。"




"ハゲタカだって、食えると知ったところでこれをお持ち帰りにはしてもらわないよな。"





"これ以上耐えられるとは思えないけど、課題を済ませるのは重要なことなんだ。"






hi "さて……何を調べるんだったっけ？"







"負けるとわかっていても戦わなければならない時がある。"





"数学の宿題の途中で俺は鉛筆を置いた。"




"だめだ。気晴らしが必要だな。"






"あいにく、気晴らしになるような選択肢はほんのわずかしかない。"




"今は本を読む気分じゃない。"



"健二は今、珍しく外出している。"




"生徒会室に行ったら、結局は静音とミーシャの仕事を手伝うはめになるだろう。"






"そして他の奴らがどこにいるかは神のみぞ知るってとこだな、あいつ以外は……"





"そうだな、それもひとつの選択肢かもな。"






"俺は運動靴をひっつかんで競技場へ向かう。笑美がそこにいるだろう。"



play music music_tranquil fadein 3.0

scene bg school_track_ss
with locationskip





"競技場に着いたら、陸上部の練習が終わるところだった。"





"太陽が空の向こうに沈み始めている。"



"もうそんなに時間が経っていたのか？"


show emi basic_grin_gym_ss at center
with charaenter



emi "こんなとこで何してるの？　久夫くん"


show emi excited_proud_gym_ss
with charachange


emi "スパイしに来たんでしょ？"



"俺は肩をすくめる。正直、なぜここに来たのかわからない。"





hi "他にすることもないし"




"だいたい合ってるよな。"





"いま、会えると思えたのは笑美だけだし。"



show emi basic_annoyed_gym_ss
with charachange


emi "それで、あたしが最後の頼みの綱だってわけ？"

show emi sad_angry_gym_ss
with charachange




emi "他の人たちは微妙だし、じゃあ笑美にでも会いに行こう、なんて思ったの？"






"ほんとに怒ってるみたいだ。"





"からかってやるチャンスの発生だ。"





hi "実際そんなとこだろうね"



show emi sad_annoyed_gym_ss
with charachange




"笑美は口をとがらせ、子犬そっくりに目を見開く。"





hi "冗談！　冗談だよ！"


show emi basic_closedgrin_gym_ss
with charachange



emi "じゃああたしにつきまといに来たんだ！"




"待てよ、何だって？"




hi "そんなつもりで言ったんじゃない！"






hi "なんで俺が笑美につきまとわなきゃなんないんだよ？　つきまとってほしいわけじゃないんだろ"







hi "お前は寝ているか授業中とかじゃなければここに来るんだろ？"




"笑美はそれを聞いて笑う。"


show emi basic_happy_gym_ss
with charachange





emi "まあ、間違ってもいないと思うけど――でも久夫くん、食事のこと忘れてるよ。あたしだってそれくらいするし"






"俺はうなずく。そこはしょうがない。"


show emi sad_grin_gym_ss
with charachange




emi "それにあたし、ときどき琳とも遊ぶし……だからつきまとうのはちょっと大変かもしれないよ"





hi "いっしょに何するんだよ？　共通点があるようには見えないけど"



show emi basic_closedgrin_gym_ss
with charachange


"笑美は自分の手をお尻に当てて偉そうな態度をとる。"


show emi basic_grin_gym_ss
with charachange




emi "へえ、そう思うんだ。隠れた趣味ならあたしいろいろあるんだよ"






hi "ほんとに？　例えば？"



show emi sad_grin_gym_ss
with charachange




"笑美は、自分の自由時間にすることを思い出すように、頭を傾ける。"



show emi basic_closedgrin_gym_ss
with charachange



emi "そうね、琳とあたしでときどき外に買い物に行くよ"





"筋は通ってるな。なんだかんだ言っても笑美は女の子だし。でも琳は？"




hi "琳も一緒なのか？"

show emi basic_grin_gym_ss
with charachange





emi "あたしたち、いつも画材屋さんに寄り道するの"







emi "それと、琳はなんか変な楽器とか音楽とかいっぱい売ってる楽器屋も好きなの"



show emi basic_closedhappy_gym_ss
with charachange



emi "そういうのがあると集中できるんだって"




"それならまあわかる。"




hi "ふーん。で他に隠れた趣味は？"


show emi excited_proud_gym_ss
with charachange



"笑美は指を振る。"





emi "待ってよ、なんで全部ばらさなきゃなんないの？　あたしたちまだそんな知り合いじゃないじゃん！"




"なぜか、笑美は琳といることが趣味の全てなんじゃないかと思う。"




"でも、自分の疑問が解けたとは思わない。"





hi "趣味の２つや３つはあってもさ、なんでそんなに琳とぶらぶらするのか、俺にはわかんないよ"






hi "思うんだけど、琳って、どっちかって言うと変わってるよな？"




"その一言で笑美は大笑いする。"

show emi basic_closedhappy_gym_ss
with charachange



emi "あはは！　最高に控えめな言い方ね！"





hi "だからなんで琳？　っていうのは、笑美は人と話したりするの得意だから、いろんな人と仲いいんだろうなあって思ったら、琳といるとこしか見たことないしさ"


show emi sad_annoyed_gym_ss
with charachange


"笑美は珍しく受身の様子だ。"





emi "ちょっと、あたし琳じゃなくて他のみんなとも仲いいから！　久夫くんとはクラスが違うから、見たことないだけだよ"








hi "そうだな、でもそれじゃまだ琳と一緒にいることの説明になってないぞ"






"自分でもなんでこんなことを知りたいのかわからない。"




"今日のランチがあまりにも変だったからだろう。"


show emi basic_confused_gym_ss
with charachange



"笑美が肩をすくめて、一瞬、すごく琳っぽく見える。"

stop music fadeout 4.0





emi "あたしたちが似たような生き方をしてるからだよ"








"こんなに予想を裏切る答えもないと思う。"






hi "どういう意味？"




emi "例えば……"


play music music_emi fadein 1.0

show emi basic_grin_gym_ss
with charachange



emi "そうね、琳は絵を描いたりしてるよね？"



hi "そうだな……"




"この話はどこに行くんだろう。"



show emi basic_closedgrin_gym_ss
with charachange


emi "で、あたしは走る"


hi "で？"

show emi basic_happy_gym_ss
with charachange




emi "で……それがあたしたちが似てる理由"





hi "……"


hi "わけわかんねーよ"


show emi basic_annoyed_gym_ss
with charachange



"笑美はうまい答えを見つけようと顔をしかめる。"







emi "そうね、行動原理が同じなのかも"







hi "は？"



show emi sad_grin_gym_ss
with charachange



emi "んーとね、あたしたちは自分の情熱に従ってるの"


hi "それって笑美が走るのに熱心で、琳は芸術に熱心だってことか？"



emi "まあそんな感じ。えーっとね……"


show emi basic_closedgrin_gym_ss
with charachange



emi "そうそう、琳は前にあたしに話してくれたけど、自分でもどれだけ理解できたかわかんないの"





"べつに驚くことでもない。琳からなら、なにを説明されても誰だって混乱するだろう。"



show emi basic_grin_gym_ss
with charachange




emi "琳は、あたしたちは二人とも極端なものを追いかけてるって言うんだ"






emi "例えば、琳は特別な感覚かなにかを表現する新しい方法を探そうとしてるの"



show emi sad_grin_gym_ss
with charachange





emi "で、あたしは走ることで得られる特別な感覚のために走るの"







emi "それに、ぐずぐずさせられるのは二人とも嫌なの。あたしたちはそれでつながってるんだ"






hi "『ぐずぐずさせられる』って？"



show emi basic_confused_gym_ss
with charachange



"笑美は驚いたようで、自分の足を指さす。"






emi "だって、あたしはランナーだから。それに琳は腕がなくたって絵を描いてる"







emi "だからお互いにその決心を尊重してるの"



show emi basic_closedhappy_gym_ss
with charachange





emi "だからいっしょにいる"




show emi sad_grin_gym_ss
with charachange




emi "たぶんね"








"まあ、俺にその意味がわかったかどうか……でも、自信なさげな顔つきからすると、笑美もわからないようだ。"









emi "正直、そんなことあんまり考えないけどね"






emi "あたしたちはうまくいってる――それがすべてじゃないかなって"





"笑美は核心を突いたなと思う。"





"別の質問が浮かび上がってきて、他にすることもなかったから、尋ねてみる。"






hi "ところでさ、何がきっかけでそんなに笑美は走るようになったんだ？"




show emi basic_closedgrin_gym_ss
with charachange




emi "あー、ほんとにちっちゃいころから走ってるよ！"



show emi basic_grin_gym_ss
with charachange



emi "パパが陸上選手で、あたしが歩けるようになるとすぐに走り方を教え始めたの"



show emi sad_grin_gym_ss
with charachange




emi "それがあたしにとって、父親と娘の絆だったんだよね"




show emi sad_depressed_gym_ss
with charachange

stop music fadeout 10.0





emi "ふたりの共通の趣味"







"笑美の顔に影が差して、哀しそうに見えて……ショックだった。"





"笑美とお父さんの間に何かあったんだろうか？"


show emi basic_shock_gym_ss
with charachange




emi "ああもう、あんまり時間ないや"



show emi basic_closedsweat_gym_ss
with charachange




emi "ごめんね、ナースくんのところに行く前にもう少し走るから！"


play ambient sfx_emipacing

hide emi
with easeoutleft

$ renpy.music.set_volume(0.3, 1.0, channel="ambient")



"笑美は髪を風になびかせてトラックをひた走る。"




"今朝よりもかなり速く走っているように見える。"




"トラックを回っている笑美の顔を、俺はちらりと見る。"


scene ev emi_run_face_zoomout_ss
with locationchange




"今朝とほとんど同じだけど、その目つきは険しくなっているように見える。"





"笑美の言うとおりかもな。"




"俺はほんとうに、笑美のことをよく知らない。"


scene bg school_track_ss
with locationchange





"少し笑美の走りを見てから、部屋に戻るために立ち上がる。"




emi "ねえ！"




"笑美が帰る俺を見つけて、注意をひくように手を振る。"




emi "忘れないで！　また明日の朝の同じ時間にね？"


hi "もちろん"

stop ambient fadeout 2.0




"俺は部屋へと戻る。"




"宿題が俺を呼んでいる。"

label jp_E6:

scene bg school_track_ss
with None

scene bg school_dormhisao_ni
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")


"眠れない。"




"体は疲れていても頭は起きていて、俺は部屋のうつろな闇に浮かぶ天井を見つめている。"






"頭もくたくたになればいいのにと思って、必死で思考の脈絡をつけようとする。"






"俺が考えられるのは、何も考えられないということだけだ。"






"まったく生産的じゃない。"







"薬の副作用だろうか。でもそうだとしたら、出始めるのが妙に遅すぎる。"






"やっぱり、思うほど新しい環境に慣れていないだけかも。"




"わからないけど、でも理由はともかく、俺は、起きてちゃいけないのに起きている。"




"ばかばかしいな。"

play sound sfx_switch

scene bg school_dormhisao
with Dissolve(0.2)



"体の凝りは無視して、ベッドから出て時計を見る。"





"朝４時。最後に時計を確認したときはまだ１時だったから、少し寝たのかも。"




"わからないけど。"




"俺は服を引っかけて部屋を出る。"




"歩けば少しはましになるだろう。"


scene bg school_courtyard_ni
with locationskip




"日中の暖かさに比べて、外の空気がずいぶん寒いのに驚く。"





"構内を歩き回っていると自分の吐く息が見える。日が昇るのが先か俺が眠くなるのが先か。"





"現在のところ、どっちもありだけど。"




scene bg school_track_ni at left
with locationchange




"気がついたら競技場にいた――笑美が走っていない競技場を見るのは、初めてだ。"






"そりゃそうだろう。さすがに笑美でもこの時間じゃ早いよな。"





"屋外の観客席は冷たいけど、今の俺にはこの感覚がありがたい。"



show bg school_track as overlay:
    left
    alpha 0.0
    linear 15.0 alpha 0.5
with None





"太陽が地平線に顔をのぞかせ始めて、今からまた寝るのはもう無理だなと確信する。"







"徐々に強くなる陽の光が体を暖めるにつれ、地面の露もすこし湯気を立てはじめる。"





"心がほんの少し落ち着いてくる。"


stop music fadeout 2.0

scene black
with shuteye

window hide

with Pause(3.0)

play sound sfx_rustling

window show hpunch


"誰かが俺を揺さぶっている。"


emi "ちょっと、起きてよ！"


hi "あぁ？　どこだ？　ふぁ？"

scene bg school_track
show emi basic_shock_gym_close at center
with openeyefast



"結局寝ちゃったんだな。"

show emi basic_annoyed_gym_close
with charachange



emi "こんなとこで何してんの？　風邪とか引くよ！"

play music music_dreamy fadein 4.0





"俺は目をこすって、心配そうにのぞきこんでいる笑美と向かいあう。"






"俺はまだふらふらで、言葉もはっきりしない。"



hi "寝られなくってさ。日の出を見てたんだよ"

show emi basic_confused_gym_close
with charachange



emi "琳みたいなこと言うね"





"俺は肩をすくめる。２、３時間ベンチで寝たので、体が凝っている。"






hi "そうか？　知らないけど"



show emi basic_grin_gym_close
with charachange



"笑美は、俺の（多少めんどくさい）反応にちょっと笑う。"


show emi basic_closedgrin_gym_close
with charachange



emi "とりあえず、眠れなかったんでしょ？　なら当然、今日はきっちり走らなきゃ！"





"笑美のことは１週間くらいしか知らないけど、これはまったく笑美っぽい反応に見える。"





hi "おい、体は昨日のあれでほんとにボロボロなんだぞ！"






hi "気分が落ち着かなくてさ、それだけだって"




show emi basic_confused_gym_close
with charachange



emi "変わんないじゃん、きっちり走れば心だって疲れるよ"






"朝一でこんなことをする笑美の良識を俺は真剣に疑っている。"









"そうやって頭をへとへとに疲れさせたら、学業の方がどうなるか自信がない。"





show emi basic_closedgrin_gym_close
with charachange

with vpunch

show emi basic_closedgrin_gym
with charadistant



"笑美は、小さな体からは考えられないほどの力で、観客席の俺を引っぱる。"





emi "ほら行くよ、久夫くん！　走らなきゃ！"




"正直、今日は走るのに耐えられるかどうかわからない。"




"つまり明らかに睡眠不足だし……寝たのだって観客席だぞ！"







hi "どうすっかな……ほんとに走んなきゃだめか？"





show emi basic_annoyed_gym
with charachange



"笑美がにらんでくる。"



"ありゃりゃ。"


show emi sad_annoyed_gym
with charachange




emi "なに言ってんの？　走んなきゃだめに決まってるでしょ！"





emi "他にどうやったらすっきりするのよ？"


show emi basic_annoyed_gym
with charachange



emi "観客席で寝てたじゃない、まったく！"




emi "痛みを取るにはちょっと走るのが一番だよ"




emi "ほら観客席に隠れてないで出てきなさい！"





"議論の余地はない。言うとおりにしなかったら間違いなく殺されるだろう。"





"俺は立ち上がって、トラックに飛び降りる。"


scene bg school_track_on
with locationchange




"太陽がうまいこと辺りを暖めているな、と思う。"






"笑美と俺はストレッチを始めて、俺はまた、笑美をじっと見つめないでいるのが一苦労なことに気づく。"





"これで毎日起きられるなら、朝練にも慣れることができるかもしれない。"


show emi basic_annoyed_gym
with charachange



emi "ねえ久夫くん、失礼だよ、じろじろ見ちゃって"





hi "見ちゃってない！　誓って！"





"俺の反応を査定でもするみたいに、笑美は眉をつり上げてしばらく考える。"





"人生で一番恐ろしい間だ。"



show emi basic_closedhappy_gym
with charachange




"でも笑美はゆっくり首を振って微笑み、やがて笑い出す。"




show emi basic_grin_gym
with charachange



emi "そんなにむきになって否定しなくてもいいのに"



stop music fadeout 5.0



"返事のかわりに俺は手を叩いて、話題を変える。"




hi "さて！　ストレッチはもう十分だよな？"


show emi sad_grin_gym
with charachange



"笑美は軽く肩をすくめる。"





emi "伸ばせた感じしてる？　ちゃんと自分で判断するんだよ"









"もし走れるかどうかという意味だったら、大いに走れる気分だ。"





hi "そうだな、準備万端だ"

show emi basic_grin_gym
with charachange



emi "昨日と同じでいい？"




emi "ちょうどいいペースで１６００いくよ"



show emi basic_closedhappy_gym
with charachange




emi "速く走ることは考えなくていいから、ペースを保つことを考えて、いい？"






hi "そうするよ"



play music music_running fadein 0.5

show emi basic_grin_gym
with charachange

play ambient sfx_emijogging

hide emi
with charamoveoutleft

$ renpy.music.set_volume(0.5, 2.0, channel="ambient")



"笑美がまた笑って、俺たちはトラックを回り始める。"


scene bg school_track_running
with Dissolve(2.0)


"……"


"……"





"もう死にそうだ。"







"まだ１周目も終わっていないのに、足が燃えるように熱い。"





"呼吸も息切れでボロボロになってきている。"




"眉毛に汗が伝ってくるのを感じる。それでもやっとカーブを２つ回っただけだ。"


$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi basic_closedgrin_gym at left
with charamoveinleft




emi "ほら久夫くん！　あと３周あるよ！"



$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft



"無理だ……"




"無理。"




"むり！"





"吐きそうだ。"




"なんとか２周目に入った。笑美は汗ひとつかいていない。"




"なんでそんなに楽そうなんだ？"






"どういうわけか、俺はまだ走っている。"





"笑美はまるで機械だ。"





"３周目。２周目はどうなったんだ？"



$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi excited_proud_gym at left
with charamoveinleft


emi "あともう一息だよ、久夫くん！"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft




"嘘つけ！　まだ２周もあるだろ！"





"お手上げだ。"






hi "こ……こんな……の……むり……だろ"



$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi basic_annoyed_gym
with charamoveinleft



"笑美はくるっと回って後ろ向きに走り始める。"




"怒りの表情に驚く。"



show emi sad_angry_gym
with charachange




emi "そんなこと言わないで！"







emi "それ言ったら負けだよ"



show emi sad_angry_gym at left
with charamove




emi "走り続けて！　生きてるんなら、走れるのに！　バカ！"



$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft




"うわっ、なんて言い方だよ。俺たちはようやく４周目に入る。"






"笑美は本当に俺に走り続けてほしいみたいだ。"





"足よ動け。動け。動け。なんて重いんだ。"





"泥か糖蜜かタールの中にいるみたいだ。"




"足が続かない。"




"走り続ける。"


$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi basic_grin_gym at left
with charamoveinleft



emi "久夫くんラストまっすぐ！　全力で！"


$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft




"俺は、できる限り速く足を動かす。"





"両足は命令に従うのを拒否し続けている。"



"どうにか、俺は動き続ける。"


"なんとか、俺はゴールする。"


stop ambient fadeout 0.5

show emi excited_happy_gym at center
with charaenter

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")


emi "そうだよ、久夫くん！　やればできるじゃない！"



"１周前に見せた怒りは消え、誇らしげな顔になる。"





"自分が金メダルかなにかでも取ったみたいに晴れやかだ。"



scene bg school_track_on
show emi excited_happy_gym at center
with vpunch



"俺は止まろうとしてよろけて、手と膝からくずれ落ち、空気を求めてあえぐ。"





"こんなに動悸が激しいことになるのは本当に久しぶりだ。"



stop music fadeout 1.0

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)



"あれ以来こんなこと起きてなかったのに……"



play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)



"しまった。"


scene black
with shuteyefast

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)



"落ち着いてくれ、心臓。"


play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)




"ちょっと落ち着いてくれ。すこし止まってくれ。"




play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)




"咳払いをすると、なぜか、軽く笑ってしまう。"



play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)



"で、俺はこうやって死ぬのか？"


play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)



"健康でいようとして？"


play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)


"皮肉なもんだ。"

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)




"あきらめる準備ならもうできてるって。"



play sound sfx_heartslow
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.8)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.8)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)



"それでも、心臓が落ち着いてくるのを感じる。"





"二つの手が俺の腕の下をつかんで、引き上げる。"



scene bg school_track_on
show emi basic_confused_gym_close at center
with openeye



"見上げると、笑美が喜びと心配の入り交じった顔で覆いかぶさっている。"



emi "立って！"

show emi sad_grin_gym_close
with charachange



emi "さあ、そんなんじゃいつまでたっても息を整えられないよ"




"俺はなんとか立ち上がる。頭の上に腕を上げようとするけど、腕は鉛のようだ。"




"笑美がそばにつき、俺は歩いてトラックを回り始める。笑美は俺が倒れでもしないかと思ってるみたいだ。"






"当たらずも遠からず、かもな。"





"ものすごくつらくて、笑美にそう言った。"


show emi basic_closedhappy_gym_close
with charachange


"笑美は笑う。"

show emi basic_happy_gym_close
with charachange


emi "でもやり遂げたじゃない？"


show emi basic_grin_gym_close
with charachange



emi "久夫くんはできないって言ったけど、やり遂げたよ"




emi "それってすごいことじゃない？"




"すごいかどうかはわからないし、それを言うための息も続かない。"





"でも、さっき俺の顔に浮かんだ笑いは消えていない。"






"心臓が弱いからなんだっていうんだ？"








"それでも今朝は生き延びたんだ。"







"明日も生き延びるかもな。"



scene bg school_track
with shorttimeskip

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")

play ambient sfx_emisprinting





"俺がいきなりひっくり返ったりしないことがわかると、笑美はすぐ走り始める。"






"１キロ以上走った後でなんであんなにバカみたいに全力で走れるのか俺にはさっぱりわからない。でも笑美は俺よりずっと体調がいいんだろう。"






"またトラックを歩いてクールダウンするけど、やっぱり俺は笑美の走りを見ずにはいられない。"




scene ev emi_run_face_zoomin
with locationchange




"不思議だけど、がんばっているときの笑美は別人のようだ。"







"前に気がついたのは笑美の目だけど、今回は口だ。"





"笑美は、いつもの笑顔をしていない。"




"まだ微笑んではいるけど、緊張感がある。"





"まるで、勝ち目のない戦いをしているけど、そんなことを気にしていないような険しい表情だ。"







"昨日と同じように、笑美はもっときつい走り方をしているみたいだ。"





"顔から汗がしたたり始めても、笑美は走り続ける。"




"息を鼻から十分吸えなくなると、ついに口が開く。"




"笑美はもう一度俺を追い越す。激しく上下する足、合わせて振れる腕、わずかに離れた唇……"





"きれいだ。"



stop ambient fadeout 2.0

scene bg school_track
with shorttimeskip

play music music_normal fadein 3.0
$ renpy.music.set_volume(1.0, 0.0, channel="ambient")



"クールダウンするために二人でトラックを何周かしたあと、笑美はいつもの姿に戻る。"




"笑美の中に見た変化はもうない。"


show emi basic_happy_gym at center
with charaenter


emi "今日は悪くなかったよ、久夫くん"




"まるで褒めているみたいに聞こえる。"






hi "どういうことだよ？　笑美が俺に怒鳴らなかったらやめてたぜ"



show emi sad_shyblush_gym
with charachange



"笑美は少し赤くなる。さっきの爆発が気まずいみたいだ。"





emi "ごめんね、あたし……他の人があきらめるのを見るのは耐えられなくって"




emi "特に今みたいなことで"

show emi sad_grin_gym
with charachange




emi "言ってる間もできてるのに『できない』って言ってるのはおかしいよ"







emi "そういうこと"






hi "おかしなことを言うことがか？"




show emi basic_annoyed_gym
with charachange


"笑美は、俺に舌を出す。"




emi "ばか。生きてるって証の話よ"







"俺が生きてる証だって？　それがこんなに苦しいとは知らなかった。"




"にもかかわらず、気分はかなりいい。"


show emi excited_proud_gym
with charachange



emi "でもね、今日はいちばん厳しい日のひとつだよ"




hi "どういうこと？"



show emi basic_grin_gym
with charachange




emi "トレーニングを始めるときって、１日めはきついの。２日めはもっときつい。で、３日めはちょっと楽になるの"





emi "ほんとうに苦しい日はまだ続くけど、それがだんだん少なくなっていくの"





hi "で、結局は余裕でできるようになる、って？"



show emi basic_closedhappy_gym
with charachange


emi "そうね、もちろんよ"

show emi basic_closedgrin_gym
with charachange



emi "でもハードルは上げていかなきゃね、そうしないと伸びないもん"




emi "自己満足になっちゃうし、達成感もなくなるでしょ"




hi "ってことは俺は４周以上走らなきゃいけないんだな？"


show emi excited_proud_gym
with charachange



emi "うん！　でも当分は――慎重に、ね"





"なにかひらめいたようで、笑美の顔が輝く。"


show emi basic_closedhappy_gym
with charachange




emi "わかった！"




hi "何が？"

show emi basic_happy_gym
with charachange





emi "いっしょにナースくんのところに行こう！　それならもう倒れて死んだりしないよ！"





"なんて可愛いんだ。"



hi "んー……いつ？"


show emi basic_grin_gym
with charachange



emi "今すぐに決まってるじゃん！　シャワーとかもするんでしょ？　あんま時間ないよ、ほら！"




"笑美は俺の手をつかんで、引っぱっていく。"


stop music fadeout 2.0

label jp_E7:

scene bg school_nurseoffice
show nurse neutral at center
with shorttimeskip




nk "おやおや今日はずいぶん急ぎだね、笑美ちゃん？"



play music music_nurse fadein 2.0




"どうやってこんなに速く着いたのか全くわからないけど、俺たちは医務室にいる。"




show nurse neutral at twoleft
show bg school_nurseoffice at bgleft
with charamove

show emi basic_grin_gym at tworight
with charaenter



"ナースは笑美にニッと笑う。俺のことは完全に無視してるみたいだ。"


show nurse grin
with charachange





nk "シャワーして授業に出るまで、まだ時間はたっぷりあるんだけどね"



show nurse concern
with charachange



nk "そんなに廊下をばたばた走らなくてもいいだろう。遠くからでも丸聞こえだよ！"




"どうも、ナースは笑美を叱ってるようにはまったく見えない。"




"まるで二人の日常のひとコマみたいだ。"




"笑美はそこそこの演技で反省してみせる。"




show emi excited_sad_gym
with charachange



emi "すみません！　もう二度としません！"


show nurse grin
show emi basic_closedhappy_gym
with charachange




"なにかの内輪ネタみたいだけど、ナースと笑美は笑っている。"



show emi basic_grin_gym
show nurse neutral
with charachange



"突然、ナースが俺に気づいたみたいだ。"



show nurse fabulous
with charachange


nk "ああ、おはよう久夫くん"

show nurse neutral
with charachange


nk "何かあったかい？"



hi "そうですね、俺は――{w=.3}{nw}"


show emi basic_closedgrin_gym
with charachange




emi "久夫くんが正式に朝練に参加したの"







"俺は説明しはじめるけど、笑美が割って入る。"


show emi basic_happy_gym
with charachange




emi "だから死んだりしないようにここに来たほうがいいかなって"



show nurse fabulous
with charachange



"ナースは、大げさに怖がって眉を吊り上げる。"






nk "まったくだよ、そんなことがあったら僕はすぐにクビになっちゃうから。ねえ？"




show nurse neutral
show emi basic_grin_gym
with charachange




nk "それじゃあ久夫くん、診てみようか"





nk "シャツ上げてくれるかい？"




"突然、笑美が同じ部屋にいることをすごく意識してしまって、俺は思わず赤くなる。"






"ナースには俺の戸惑いがわかるみたいだけど、それはナースを面白がらせているだけのようだ。"





show nurse grin
with charachange



nk "ちょっと恥ずかしいよね？"




"ナースは笑美に申し訳なさそうなお辞儀をする。"





nk "すまないね笑美ちゃん、無料のショーをお見せできるかと思ったけど、だめだったみたいだ"



show emi basic_annoyed_gym
with charachange



"笑美はちょっとこわばって、ナースにいら立った視線を浴びせる。"





emi "うっさいバカ"



show emi excited_proud_gym
with charachange



"笑美は申し訳なさそうに俺にお辞儀をする。"



emi "外で待ってるね、いい、久夫くん？"


hide emi
with charaexit

show nurse grin at center
show bg school_nurseoffice at center
with charamove




"いやこんなのほんとうに大したことじゃないし別に出ていかなくてもいいから、と俺はしどろもどろで言いはじめたけど、笑美はとっくにドアの外で、ナースはそれを見て笑っている。"



show nurse fabulous
with charachange




nk "まだいけるな！　ハハハ！"





hi "よく分からないんですが"


show nurse grin
with charachange





"ナースはまた笑う。俺にわからない冗談でウケているかのようだ。"







nk "僕はまだ笑美ちゃんを振り回せるんだな。これは僕たちがしばらくやってる競争みたいなものだよ"





"それが俺にはすごく嫌な言い方に聞こえたことが、ナースにもわかったみたいだ。"



show nurse concern
with charachange






nk "えーと。今の言い方は実際よりもかなりひどすぎるね、そういえば"









hi "俺なにも言ってませんけど……"







nk "いや、いや、君は正しいよ。誤解しないように説明しなきゃね"



show nurse neutral
with charachange



nk "僕は、実はここではどちらかと言えば新人の方なんだよ。雇われたのは笑美ちゃんがここに通い始めた年でね"




nk "その前は、笑美ちゃんとは事故の後の初期のリハビリで一緒だったんだ"






"待った、何だって？"


show nurse concern
with charachange




nk "本当にひどい交通事故で、僕たちは彼女の足を切断しなきゃならなくなってね。危ない手術だったけど、うまくいった――"









"ナースは急に黙りこむ。俺は不意に知らされたこの事実に驚いている。"







nk "いや、僕から話せることじゃないな。とにかく、僕たちはけっこう前から知り合いなんだ"







nk "だから患者と看護師っていうより、もうちょっと親しい仲なんだよ"





"きまり悪そうに見える。なにか悪いことでもしたみたいだ。"





"ナースはそのことを本当に気にしてたんだと思う。俺は手を振って、大したことじゃないと伝える。"





hi "心配しないでください、先生。黙っておきますから"







"笑美が足を失った原因は気になっていた。今の話は俺も可能性のひとつとして考えていたものだった。"






"起こりうるパターンなんてそう多くはないにしても、実際に起こったことを聞くのは……やっぱり少しショックだ。"



show nurse neutral
with charachange


nk "いや、ありがとう。君はいい子だね、久夫くん"



nk "なんで笑美ちゃんが君と友達になったのかわかったよ"


show nurse fabulous
with charachange



nk "わかるかもしれないけど、笑美ちゃんは本当に負けん気が強い"




hi "どういう意味ですか？"






nk "あの子が歩く練習をするところは見てないよね。病院では他の誰よりもいっぱい練習してたんだ。頑としてやめなかった"







nk "普通は、また走るなんて考えられるようになるまで何年もかかる。それを笑美ちゃんは一年ぐらいで全部やったんだよ"





"ほとんど自慢してるみたいだ。まるでコンテストかなにかで優勝する娘を見る父親のように。"



show nurse neutral
with charachange




nk "まったく、もし僕たちが止めさせなかったらもっと早くやりとげただろうね"





hi "止めさせなかったら？　なぜですか？"


show nurse concern
with charachange

stop music fadeout 4.0




nk "長いあいだ頑張りすぎて、義肢が当たる部分から出血しはじめたんだ"







nk "実際、厄介な問題でね――だから毎日、走ったあとはここに来るんだよ"








nk "仮に足が傷ついて義肢が汚れていれば、感染症のリスクについては言うまでもない"



show nurse neutral
with charachange




nk "でもこの話はもういいね"



show nurse fabulous
with charachange

play music music_nurse fadein 2.0




nk "もし君をこのまま引き止めてたら、笑美ちゃんは僕らが何かを企んでると思うだろうし"




"ナースはそう言うと、ウインクをして俺の心臓の鼓動をチェックしはじめる。"


"聴診器があまりに冷たすぎる。"







"使う前に暖めるかなにかしておけばいいのに。"







"しばらくして、ナースは背を反らして、満足する。"



show nurse neutral
with charachange




nk "うん、だいぶいい感じに聞こえるね、久夫くん。走っている間、胸の痛みはなかったかい？"







hi "いいえ、あんまり。でも、呼吸がちょっと辛かったです――それと終わるころには動悸が速くなってました"




show nurse concern at center
with charachange



"俺がそう言うと、ナースは眉をひそめるけど、肩をすくめる。"



show nurse neutral at center
with charachange





nk "それは単に運動不足だからだろうね……けどもし良くならないなら、僕にちゃんと知らせなきゃだめだよ？"








nk "あまり無理をしないように――それと当然だけど胸に痛みを感じたら、すぐに僕のところに来ること、いいね？"





"俺はシャツを戻して、ナースは笑美を呼ぼうとドアから顔を出す。"


show nurse neutral at twoleft
show bg school_nurseoffice at bgleft
with charamove

show emi basic_annoyed_gym at tworight
with charaenter




emi "なんでそんなに時間かかるの？　あたし遅れちゃうじゃない！"



stop music fadeout 2.0

show nurse fabulous
with charachange


"ナースは俺に意味深な目線を送る。"

show nurse grin
with charachange



nk "久夫くんを誘惑してただけだよ"


play music music_comedy fadein 0.5

show emi sad_annoyed_gym
with charachange




emi "なにそれ！？　ちょっと、あたしの友達に変なことしないでって言ったでしょ？"






"笑美はショックを受けるかと思ったけど、ただうんざりしただけみたいで、クッキーを盗んだ子供でも叱るようにナースを叱っている。"






"こっちは、ナースが変なこと言うから顔を赤らめないように必死だ。"



show nurse fabulous
with charachange






nk "もうしないようにするよ。でもあいにく、若い久夫くんは永遠に女の子に興味をなくしちゃってるかもね！"






stop music fadeout 0.5



hi "そんなわけないだろ"


with Pause(3.0)

play music music_comedy fadein 0.5

show nurse grin
show emi excited_laugh_gym
with charachange




"大声で言うつもりはなかったけど、ナースも笑美も俺をちょっと見つめると、また爆笑し始める。"




show emi basic_happy_gym
with charachange



emi "ね、彼面白いって言ったでしょ！"






"へえ。笑美がナースにいろいろ話しているってのは本当なんだな。"




show nurse fabulous
show emi basic_grin_gym
with charachange




nk "ところで久夫くん、そろそろ行った方がいいんじゃないかな。授業に出る前にシャワー浴びなきゃならないだろう？"






"くそ！　ナースの言う通り、あと３０分しかないじゃないか！"








hi "ありがとうございました。あとでな、笑美！"




scene bg school_nursehall
with locationchange

stop music fadeout 5.0





"ナースが笑美の義足を外し始めたところで俺は医務室から飛び出す。"






"玄関へ向かう時、後ろからナースの声がかろうじて聞こえる。"





nk "笑美ちゃん、もっと気をつけないと……"


scene bg school_dormhisao
with locationskip



"俺は、記録的な速さで部屋に戻ってシャワーを浴びる。ふと、もう４時間も起きているのに授業はまだ始まってもいないことに気づく。"





"今日は本当に、ほんとうに長い一日になるだろう。"





"授業中に居眠りしなければいいけど。"



$ suppress_window_after_timeskip = True

scene black
with dissolve

label jp_E8:

window hide None

scene black
with dissolve

show bg school_dormhisao
with openeye

window show

play music music_pearly fadein 5.0




"目覚ましではなく、朝日の光が部屋の窓越しに俺を起こして、今日が日曜日だと気づく。"





"週末の朝練は、親切にも笑美が休みにしてくれた。"





"自分が昨日一度でも起きたのか、それともまる一日眠りっぱなしだったのか、よくわからない。"






"ベッドからやっと出ると、抗議するかのように脚がきしむ。"





"この朝練はほんとうに疲れる。"





"けど、笑美の言っていることは嘘じゃなかった。それは否定できない。"






"すこし楽になってきている。"






"毎朝これではイライラしてくるんじゃないかと心配していたけど、でも今のところはそれほど気になっていない。"







"まあ、まだほんの一週間だけだしな。"







"うっとうしい朝の目覚まし時計の音が鳴り出すまで、まだたっぷり時間があるだろう。"







"もっとも、今さらやめられるはずもないけど。"





"笑美が言ったように、他の人間がいるほうが、一度始めたことを続けやすい。"









"それに、言ってしまえば、がっかりした笑美を相手にする覚悟はできていない。"








"たぶん笑美はあの子犬みたいな目で俺を見つめてきて、俺はひどい自己嫌悪におそわれるだろう。"








"そういえば……俺は今日どこかに行くんじゃなかったっけ？"




$ renpy.music.set_volume(0.3,2.0,channel="music")

scene bg school_track_fb
show emi basic_closedhappy_gym_fb at center
show noiseoverlay
with flashback



emi "ねえ、日曜日の陸上競技会、来るんだよね？"

show emi basic_grin_gym_fb
with charachange



emi "何言ってるんだろあたし、来るに決まってるよね"


show emi sad_grin_gym_fb
with charachange


emi "そうだよね？"



"また子犬の目。"



hi "もちろん行くって！"


hi "笑美にはずいぶん世話になってるし、だろ？"

show emi excited_proud_gym_fb
with charachange



emi "そうよ！　だから忘れないで、いい？"


$ renpy.music.set_volume(1.0,2.0,channel="music")

scene bg school_dormhisao
with flashforward



"くそ、笑美の大会だ！"






"笑美が走るのを見逃したくないならさっさと行かないと。そもそも笑美がいなきゃ行く理由なんてないんだから。"







"笑美がいないんじゃ、行く目的がなくなってしまう。"




scene bg school_courtyard
show crowd
with shorttimeskip

play ambient sfx_crowd_outdoors fadein 3.0




"かくしてその直後、俺はうちの陸上部と他校のチームとの試合を見に来ている大勢の人に囲まれている。"



$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear

nvl show dissolve





n "白状すると、ここ以外にも同じような学校があるのを知って安心した。"







n "生徒……まあ、障害児だ、そういう生徒がたくさんいる学校が{b}２つ{/b}もあるなんて知ったら。"









n "……自分が不良品だという気がしなくなる。"









n "それに、自分が特別だという感覚もなくなる。普通ならそれは良くないことだけど、今回みたいな場合はマジで最高だ。"







n "それが山久学園の売りの一つなんだろうな。"









n "自分が特別ではないと知る――今自分が苦しんでいるものと取り替えられるなら、他人の障害を抱え込むこともいとわない、そんなやつが山ほどいることを思い知る、ってことだ。"












n "足がないとか心臓が悪いとかの理由でここにいるわけではない生徒もいる。"






n "中には、あと２年、運がよくても３年で死んでしまうからここに来ている生徒だっているかもしれない。"





n "そしてそれも正しいケアを受けられればの話だ。"







n "『まあ、少なくとも俺は大学卒業までは生き延びられそうだ』と言えてしまうのもなんだか苦々しい慰めだけれど、そういうことだ。"






$ renpy.music.set_volume(1.0, 2.0, channel="ambient")
$ renpy.music.set_volume(1.0, 2.0, channel="music")
nvl clear

nvl hide dissolve

window show

stop music fadeout 3.0



"観客席の入口近くに琳が現れて、俺は少々陰気な物思いから現実に引き戻された。"




show rin basic_deadpannormal at center
with charaenter




rin "来たんだ"





hi "当然。行くって言ったよな？"


show rin basic_deadpanamused
with charachange





rin "だからって、必ずそうしなきゃいけないとは限らないよ"




show rin basic_awayabsent
with charachange




rin "思ってもいないことを言う人、いっぱいいるから"






hi "いや、俺は言わないぞ"


play music music_soothing fadein 0.5

show rin relaxed_boredom
with charachange




"琳は肩をすくめる。話をするのに飽きたみたいで、きびすを返して観覧席のほうへ戻る。"






rin "笑美に借りができちゃった"




hi "なんでだよ？"

show rin basic_absent
with charachange




rin "来ると思わなかったから"




rin "笑美は思ってたけど"

show rin basic_awayabsent
with charachange




rin "で、笑美に５００円借りってわけ"






hi "お前ら、しょっちゅう賭けてないか？"







"腕のない連れは、また肩をすくめる。"



show rin basic_deadpan
with charachange



rin "そんなことないよ"


scene bg school_track
show crowd
show rin basic_deadpan
with locationchange



"観覧席に入ると、琳はあごで上のほうを指す。"


show rin negative_spaciness at center
with charaenter





rin "あそこ"



show rin basic_deadpancontemplation
with charachange



rin "私、君が来るかどうか確かめに来たんだよ"




"賭けのため、だろうな。"





"琳に連れられて、俺たちはほとんど空っぽのベンチに腰を下ろす。"



$ renpy.music.set_volume(0.3, 3.0, channel="ambient")

show rin basic_deadpancontemplation at tworight
show bg school_track at bgright
show crowd:
    linear 1.0 alpha 0.0
with charamove

hide crowd
show meiko smile at twoleft
with charaenter






"年上の女の人が琳の隣に座っている――誰かのお母さん、だろうな。"








"その人はいくぶん長い髪を三つ編みにまとめている。琳を見て、妙に見覚えのある感じで笑いかける。"



show meiko happy
with charachange



emm_ "まあ、驚いた"


show meiko wink
with charachange





emm_ "てっきりおやつでも探しに行ったのかと思ったら、男の子と帰ってくるなんて"





hi "え？"

show rin basic_surprised
with charachange




rin "おやつ？"



show rin relaxed_nonchalant
with charachange



rin "なんで下の方にいたのか不思議だったんだ"




show meiko happy
show rin basic_awayabsent
with charachange



"その人は笑う。またあの感じだ。"





"この人にどっかで会ったことあったかなあ？"



show meiko smile
with charachange





emm_ "そうねえ、あなたっていつもなにかを取ってくるって言って出かけて、別のものを持って帰ってくる子だから"






emm_ "って、やだ！　私、自己紹介もしてないじゃない"




emm_ "茨崎芽衣子です、笑美の母です"

show meiko happy
with charachange



emm "よろしくね"





"ああ、それでか。"







"芽衣子さんは、背が高くて年上でよりスタイルがいい笑美みたいな感じだ。"







"笑美よりも濃い色合いの髪を別にすれば、本当によく似ている。"



show rin basic_absent
show meiko smile
with charachange



hi "すみません、久夫です。中井久夫です"




hi "それと、自己紹介しなかったのを謝ることないですよ、茨崎さん"





hi "本当は琳が紹介するところ、ですよね？"



show meiko happy
show rin basic_awayabsent
with charachange


"笑美のお母さんが笑う。"




emm "琳ちゃんと知り合ってそんなに経ってないみたいね"



show meiko smile
with charachange



emm "琳ちゃんがそういうことを思い出すなんて期待しない方がいいわ"



show meiko wink
with charachange




emm "多分だけど、琳ちゃんはもっと他に考えることがあるのよ"



show rin basic_deadpannormal
with charachange




"琳はうなずく。この評価に喜んでいるみたいだ。"



show rin basic_deadpan
with charachange


rin "正解だね"

show rin basic_lucid
with charachange




rin "夕暮れについて考えてたんだ"



show meiko happy
show rin basic_awayabsent
with charachange




emm "ね？　自己紹介みたいなことは私たちでやるべきなのよ"




"他にいい反応もないので、とりあえずうなずく。"






"笑美のお母さんは、席の上ですこし体を反らして、眉を吊り上げる。"

$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

show meiko serious
with charachange

stop music fadeout 0.8



emm "それで、いつから２人はお付き合いしてるのかしら？"






"いきなり調子を狂わされて何も言えなくなる。でも、俺があわててべらべらと説明し始める前に、芽衣子さんはまたドッと笑い出す。"




play music music_soothing fadein 0.5
$ renpy.music.set_volume(0.3, 0.5, channel="ambient")

show meiko happy
with charachange



emm "あはは！　久夫くん、すぐ赤くなるほうなんだ？"





"この状況でどうやったら自分の尊厳を保てるのかわからなくて、とりあえずブツブツ言うことにする。"



show meiko smile
show rin basic_absent
with charachange 



hi "そうかも"


show rin basic_awayabsent
with charachange



emm "なら、新しいロマンスってことなのね？"


show rin basic_absent
with charachange



hi "待ってくださいよ、それは質問じゃなく――"




show meiko happy
show rin basic_awayabsent
with charachange





"また笑う。"






show meiko smile
with charachange




emm "わかってるわ。でもあなたがもじもじしてるところを見るの、面白くて"



show meiko wink
with charachange




emm "ごめんなさいね。おばさんの楽しみなの、許してちょうだい"





"おばさん？"



"ぜんぜんそうは見えないけどなあ。"





"笑美の元気なところは明らかにお母さんゆずりだ。"




show rin basic_absent
with charachange




hi "別に気にしてませんよ"



show meiko happy
show rin basic_awayabsent
with charachange




emm "ありがとう"



stop music fadeout 6.0

show rin basic_deadpan
with charachange



rin "始まるよ"


stop ambient fadeout 2.0

scene ev emitrack_blocks at Fullpan(12.0, dir="left", time_warp=_ease_in_time_warp)
with locationskip



"トラックに目をやると、選手たちが最初の短距離走に備えている。"




"４００メートル走みたいだな。"



"笑美を探す前に、ランナーたちを見渡す。"


scene ev emitrack_blocks_close
with flash


"笑美はほとんど自信過剰なくらいの笑顔を浮かべている。"


show insert startpistol at right
with easeinright




"スターターがピストルをかかげる。"



$ renpy.music.set_volume(0.5, 0.0, channel="ambient")

play sound sfx_startpistol
play ambient sfx_emisprinting

scene ev emitrack_running at Fullpan(1.0, dir="left", time_warp=_ease_in_time_warp)
with silentflash



"笑美はスターティングブロックから飛び出すと、残像を残してスタートラインから消える。"







"すごい。他の選手がレーンの内側ぎりぎりを走っているときでも、笑美は先頭へと躍り出る。"








"最後のコーナーを曲がるころになって、何人かのランナーが笑美に追いつく。"







"しかしその努力は無駄に終わる。笑美の爆発的なラストスパートで、他の選手は少なくとも０．５秒は離される。"




scene ev emitrack_finishtop:
    xalign 0.5 yalign 0.0 zoom 4.0 subpixel True
    0.2
    linear 0.3 zoom 1.05
    easein 8.0 zoom 1.0
with flash

stop ambient fadeout 1.0
play sound sfx_crowd_cheer



"芽衣子さんはきゃあきゃあ叫んで拍手喝采する。子供を応援する他の普通の親みたいに。"





"笑美はトラックから跳び出る。自分に満足したみたいだ。"



scene bg school_track at bgright
show meiko happy at twoleft
show rin basic_deadpandelight at tworight
with locationchange

play music music_daily fadein 2.0




"俺もみんなといっしょに喝采を続ける。"





"アナウンサー（どうもミーシャのように聞こえる）が大喜びで結果を伝える。"


show meiko smile
show rin basic_awayabsent
with charachange





emm "この前より速くなったと思うわ"




show rin basic_absent
with charachange



hi "すごかったですね"


show meiko happy
show rin basic_awayabsent
with charachange





"芽衣子さんは誇らしげに笑う。"






emm "笑美はすごいランナーなのよ"




show meiko smile
with charachange



"次の種目の準備が進むあいだ、俺たちは黙り込む。"






"笑美がまたトラックに大股で入っていくのを見て驚く。"




show rin basic_absent
with charachange




hi "え、いま走ったばっかりですよね？"







"芽衣子さんがうなずく。"


show rin basic_awayabsent
with charachange




emm "ええ、でも笑美はほかの種目も走るの。特に短距離走ね"



show meiko happy
with charachange



emm "いっぱい走ることになるけど、でもあの子なら大丈夫よ"





"様子を見てると、どうもその通りみたいだ。"






"笑美に疲れの気配は見えない。まるで前の競技にそもそも出ていなかったかのようだ。"







"もしシャツが汗ばんでいるのが見えなければ、気づきようもないだろう。"




show rin basic_absent
with charachange


hi "今度の競技は？"

show meiko smile
show rin basic_awayabsent
with charachange



emm "２００メートル走ね"





emm "あと１００メートル走とリレーもやることになってるの"




show rin basic_absent
with charachange




hi "へえ"



show rin negative_spaciness
with charachange

play sound sfx_startpistol
play ambient sfx_emisprinting




"ピストルがもう一度鳴り響くと、笑美ももう一度スターティングブロックから飛び出す。"







"ドシンという音が俺の意識をレースから引き離す。"





"琳の足だ。"




"琳はすっかりレースに夢中みたいだ。"


show meiko happy
with charachange

stop ambient fadeout 1.0
play sound sfx_crowd_cheer





"芽衣子さんがまた声を上げ始めて、レースが終わったんだなと思う。"







"短距離走はそんなに長いこと走らないだろうし。"





hi "お前の足"



show rin relaxed_surprised
show meiko smile
with charachange



rin "んー？"





hi "お前の足、席の上で跳ねてたぞ"



show rin basic_deadpan
with charachange



rin "ああ"




hi "なんだかのめり込んでるみたいだな。驚いたよ"


show rin basic_deadpansurprised
with charachange


"琳はいぶかしげに俺を見る。"


rin "そんなに変？"


hi "別に。お前はスポーツなんかには興味がないと思ってたからさ"

show rin relaxed_nonchalant
with charachange



rin "うーん、君の言う通りだね"




rin "そんなに面白くはないよ"


show rin basic_deadpannormal
with charachange



rin "でも私は笑美を見てるから、競技じゃなくて"





hi "なんだそれ"



show rin basic_lucid
with charachange



rin "笑美は走ってるときがいちばん笑美なんだ"





rin "笑美が最笑美状態なのを見られるチャンスはそうそうないよ"



show rin basic_deadpanamused
with charachange



rin "でもここなら見えるよ。ほらね？"




"琳は俺の注意をもう一度、１００メートル走が始まろうとしているトラックのほうに向ける。"



stop music fadeout 6.0
stop sound fadeout 2.0

scene ev emitrack_blocks_close
with locationskip


"俺は笑美をしっかりと見る。"



"スターティングブロックに乗りかかって、体全体がリラックスしているように見えるけど、それは見せかけのリラックス状態だ。"




"笑美の体が本当にバネのように見える。"


scene ev emitrack_blocks_close_grin
with locationchange



"スターターが位置につくよう声をかけると、頭がピシッと上がり、目はほんの少し細くなる。"




"口が上向きに曲がり、笑いとも唸りともとれそうな形になる。"


play sound sfx_startpistol
play ambient sfx_emisprinting

scene ev emi_run_face_zoomin
with locationskip







"ピストルが鳴り響いたとき、笑美は檻から解き放たれたかのように、常にこんな目にも止まらぬ速さで動いていたかのように走り出す。"
"でも、すべてが静止していたかのような錯覚をスターターのピストルが吹き飛ばすまで、俺たちにはそれがわからなかった。"




"それは数秒で終わったけど、その数秒のあいだに、俺はすごく個人的ななにかを笑美に見た気がする。"



stop ambient fadeout 1.0
play sound sfx_crowd_cheer





"笑美がゴールラインを横切るやいなや、険しい表情がいつもの笑顔へと戻る。"







"一仕事終えて、普段の姿に戻ったみたいだ。"







hi "すごいです"






hi "ほんとにすごい。あんなに速く走る人は見たことないですよ"




scene bg school_track at bgright
show meiko smile at twoleft
show rin basic_deadpanamused at tworight
with locationchange


emm "あら、私を見られてもなあ。私はあんなに速く走るにはのんびりしすぎてるから"

show meiko worry
show rin basic_awayabsent
with charachange



emm "ううん、笑美の才能はみんな父親から受け継いだんだと思う"





"笑美の父親の話になると、芽衣子さんは寂しげな、悲しそうな顔をする。"






emm "彼が笑美にランニングを教え込んだのよね"


show rin basic_absent
with charachange




hi "ええ、笑美がそう言ってました"





"笑美の父親についてたずねるのが失礼にあたるかどうか、俺は判断しきれない。"


"でも、数日前の笑美の顔を見たあとだと、聞かざるを得ない感じがする。"



hi "聞いてもよければですけど、お父さんはいまどちらに？"





"明らかに質問に答える気はないけど同時に失礼になるのも避けたいようで、芽衣子さんは口ごもる。"


show meiko serious
show rin basic_awayabsent
with charachange


emm "お父さんは……もういないの"




hi "すみません、嫌なことを思い出させるつもりはなかったんですけど"


show rin basic_absent
with charachange



hi "前に笑美がお父さんのことを話してたとき、なんだか悲しそうにしてたから"



show meiko worry
show rin basic_awayabsent
with charachange




emm "そうね、そうでしょうね"





hi "え？"


emm "とっても仲がよかったから"

show rin basic_absent
with charachange





hi "そうですか"



play sound sfx_cellphone



"とつぜん芽衣子さんのポケットから電子音が鳴り響いた。芽衣子さんはポケットに手を突っ込むと、携帯電話を取りだして見る。"


show meiko serious
show rin basic_awayabsent
with charachange




emm "……メールだなんて、何考えてるのよ？"








emm "高校生じゃあるまいし、もう"






hi "え？"

show meiko smile
with charachange


emm "ううん、なんでも"

show meiko wink
with charachange



emm "友達と会わなきゃいけなくなっちゃったの"


show meiko happy
with charachange





emm "笑美に、母さんがよくやったわって言ってたって、それと夜になったら電話するって、伝えてもらえるかしら？"




show rin basic_absent
with charachange


hi "ええ、もちろん"

hide meiko
with charaexit

show rin basic_absent at center
show bg school_track at center
with charamove

show rin basic_awayabsent
with shorttimeskip

play music music_tranquil fadein 2.0


"しばらくぼうっとしてたみたいだ。"




"もうすぐリレーが始まるのを見逃すところだった。でも、トラックを見ても笑美の姿が見つからない。"






hi "笑美、リレーにも出るんだと思ってたけど"


show rin basic_deadpan
with charachange



rin "笑美はアンカーだよ"


show rin basic_deadpannormal
with charachange


rin "だからまだしばらくは走らないよ"


hi "ああ"

show rin basic_deadpandelight
with charachange



rin "見た？"



hi "ん？"



rin "最笑美な笑美"




hi "かもな"



show rin basic_deadpanupset
with charachange




rin "ふーん。次はきっと見られるよ"



play sound sfx_startpistol




"レースが始まって、笑美のチームメイトがバトンを渡されるたびに俺は声を張り上げる。"




play ambient sfx_emisprinting

scene ev emitrack_running:
    truecenter zoom 1.0 subpixel True
    ease 20.0 zoom 1.05 xalign 0.0 yalign 0.0
with locationskip




"いよいよ、最後のバトンを繋ぐ笑美がトラックを走るのが見える。"





"またも、笑美が走るときの優雅な姿に心を奪われる。"




"本当にきれいだ。"




"決意を固めた、なにものをも恐れないような表情が、ただただその美しさを高めていく。"





"最笑美状態、なんだろうな。"



stop ambient fadeout 1.0
play sound sfx_crowd_cheer

show ev emitrack_finish
with locationskip




"でもその時、笑美がゴールラインを横切る瞬間、少しよろめくのが見える。"



"ほんの少しだけど、でも確かによろめく。"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

scene bg school_track
show rin negative_worried at center
with locationskip


"琳は鋭く息を吸い込むと、一瞬、本当に心配したような様子を見せる。"


rin "あれ、笑美……"



hi "どこか痛めたんじゃないのか？"


show rin basic_surprised
with charachange


rin "君も気づいた？"

show rin negative_confused
with charachange



rin "あれはまずいよ"



show rin negative_annoyed
with charachange


"次にどうするかを決めているかのように、琳は眉をひそめる。"


"結局はそれにうんざりして、琳はまた肩をすくめる。"

show rin basic_deadpanupset
with charachange


rin "それじゃ、降りようか"




rin "勝者に冠を授与しないとね"


show rin basic_deadpanamused
with charachange



rin "月桂樹の枝、探してきてよ"



hi "そりゃ簡単にはいかないぞ"

show rin basic_deadpannormal
with charachange


"琳は肩をすくめる。"



show rin basic_deadpan
with charachange



rin "少なくとも探そうとはしたよ"



"まあ、それほど真面目にはやらなかったけど。"



"というより全然。でも、どうでもいいか。"


stop music fadeout 5.0
stop sound fadeout 5.0
play ambient sfx_crowd_outdoors fadein 2.0

scene bg school_track_on
show crowd
show rin basic_awayabsent at center
with locationskip



"笑美はチームメイトに囲まれている。みんな笑美の走りを祝っている。"




"琳は、自分が来ていることに笑美が気づくのを待っているみたいだ。"




"ああそうか、琳は笑美に手を振ってやることができないんだ。"




"それに、もし腕があっても、そんなことをしたかどうか。"





"誰かの注意を引く、というのは琳の流儀じゃないように思う。肩をすくめる以上の感情表現もそうだけど。"





"どっちにしろ待ってやるつもりはない。俺が手を振ると、笑美は顔を上げて俺に、いや、俺たちに微笑みかける。"


show bg school_track_on at bgright
show crowd at bgright
show rin basic_awayabsent at tworight
with charamove

play music music_emi fadein 1.0

show emi basic_closedhappy_gym at twoleft
with charaenter


emi "来てくれたんだ！"

show emi excited_proud_gym
with charachange



emi "これで琳には貸しができたよね？"


show rin basic_deadpanupset
with charachange



rin "月桂樹の冠をあげようとしたんだけど、久夫が探してくれなくってさ"


show emi basic_grin_gym
with charachange



hi "おい、お前もだろ"


show rin basic_deadpan
with charachange


rin "探すのは私の役目じゃないよ"


hi "いつそんなこと決めたんだよ？"

show rin basic_deadpannormal
with charachange




rin "『月桂樹の枝、探してきてよ』って言ったとき"



show rin basic_deadpandelight
with charachange


rin "ちゃんと聞いてなよ"


"俺は肩をすくめる。琳のくせがうつったみたいだ。"



hi "やっぱり俺のせいみたいだ、笑美"


show emi basic_closedhappy_gym
show rin basic_awayabsent
with charachange


"笑美は俺と琳を笑う。"

show emi basic_happy_gym
with charachange




emi "大丈夫だよ、きっとほかのことで埋め合わせしてくれるよね"



show rin basic_absent
with charachange


hi "あー、もちろん"

show rin basic_awayabsent
show emi excited_amused_gym
with charachange



emi "よし！　で、あたし、どうだった？"


show rin basic_absent
with charachange




"俺は『きれいだ』とか『すげえ』なんてことを口走らないようにして、もっと差し障りのない『すごく良かった』という表現に落ち着く。"



show emi basic_closedgrin_gym
with charachange



"笑美はこの評価に喜んだみたいだ。"




"脚がないおかげで、その走りがはるかにカッコよく見えたことには触れないでおく。笑美にはもうわかってるはずだ。"





"それに、どうもそれを言うのは笑美の努力をだいなしにしてしまうような気がする。"


show emi basic_grin_gym
show rin basic_awayabsent
with charachange




emi "よかった！　リレーで少し遅くなっちゃったかなって心配したけど、あたし頑張ったでしょ、ね？"



show rin basic_absent
with charachange



hi "あのさ、俺、気づいたんだけど――{w=.4}{nw}"

play sound sfx_impact

show rin basic_deadpanupset
with vpunch



"言い終わる前に、琳が俺を蹴飛ばして制止する。"

show emi basic_confused_gym
with charachange


emi "なんのこと？"

show rin basic_deadpancontemplation
with charachange


rin "気づいたんだって。終わりのとこ"

show emi basic_annoyed_gym
with charachange


emi "ああ、それは良くないなあ"

show emi sad_grin_gym
with charachange


emi "あとでナースくんが診てくれるよ、きっと"

show emi sad_grit_gym
with Dissolve(0.2)

show emi sad_grin_gym
with charachange



"なんでもないような気の抜けた声色だけど、俺はすぐにわずかな顔のけいれんに気づく。"



"本当は痛いのを隠そうとしているみたいだ。"




"それに息づかいが浅いことにも気づく。"




"本当に痛いんだな。"




"笑美はスキップしてこちらに近寄り、気さくな感じで肩を叩く。俺が心配しているのに気づいているんだろう。"


show emi basic_closedgrin_gym_close
show rin basic_deadpannormal
with characlose



emi "ねえ、なんか心配そうだね！"


show emi basic_grin_gym_close
with charachange



emi "平気だよ、ほんとに！"




emi "走りっぱなしで疲れちゃって、それだけ"



show emi excited_proud_gym_close
with charachange



emi "それにほら、ちょっと痛いぐらいじゃあたしは止まらないよ"


hi "本当かよ？"

show emi basic_closedgrin_gym_close
with charachange




"笑美はにこりと笑うと、一瞬、短距離走のときのように、荒々しく誰にも打ち負かされないような様子を見せる。"





"言いかたを変えれば、ほんとにきれいだ。"

show emi basic_grin_gym_close
with charachange


emi "まだまだだよ"


hi "まあそれなら、心配ない、だな？"

show emi basic_closedhappy_gym_close
with charachange



emi "そういうこと！　あたしは茨崎笑美、地上最速の足なきもの！　どんな時でも止まらない！"



hi "すげえや"

show emi basic_closedgrin_gym_close
with charachange


"笑美はくすくす笑うと、なにかを思い出したみたいだ。"

show emi basic_grin_gym_close
with charachange


emi "そうだ、忘れないうちに……"





emi "次の日曜日に琳とあたしとで、競技会の後のお祝いに何かしようと思ってるんだ！"




show emi excited_proud_gym_close
with charachange




emi "久夫くんもおいでよ！"



show emi sad_grin_gym_close
with charachange




emi "いつもなら次の日にやるんだけどね、でも今日は日曜日でしょ。宿題とか、授業とか、やることがたくさんなの"



show emi basic_closedgrin_gym_close
with charachange


emi "プラス、朝練もね"




hi "そうだな、もちろん"



hi "あ、そうだ。お前のお母さんがよくやったって伝えてくれってさ"




hi "今晩電話するって"



show emi basic_happy_gym_close
with charachange


emi "たしか客席にいるの、見たよ！"

show emi basic_closedhappy_gym_close
with charachange


emi "来てくれてよかった！"

show emi sad_grin_gym_close
with charachange



emi "競技会にはいつもパパが来てくれてたんだけど、ママがうまくバトンタッチしてくれたんだ"


show emi sad_shy_gym_close at Transform(function=tf_lefttremble)
with Dissolve(0.1)



"笑美が少し震えて、俺は笑美がまだ汗をかいているのに気づく。"




"軽く風も吹きはじめている。"



"俺はぜんぜん寒くないし、上着があるので、黙って笑美の肩に上着をかけてやる。"


play sound sfx_rustling

show emi basic_shock_gym_close at twoleft
with vpunch

with Pause(0.5)

show emi basic_grin_gym_close
with charachange




"笑美は少し驚いて、そして俺に笑いかける。"



show emi basic_closedhappy_gym_close
with charachange


emi "ありがと！"

show emi sad_grin_gym_close
with charachange



emi "ちょっと寒くなってきたかな"



hi "ああ、みたいだな"


"笑美に上着を貸してやったのは間違いだったんじゃないかと思いはじめると同時に、陸上のユニフォームを着た男子が近づいてくる。"






"チームメイト" "おーい、笑美！　表彰式遅れちゃうぞ！"




show emi basic_closedgrin_gym_close
with charachange



emi "あ、そうだった！　ありがと！"

show emi basic_grin_gym
show rin basic_awayabsent
with charadistant



"笑美は琳と俺に向きなおる。"






emi "終わるまで待ってなくてもいいからね。すごく長くなるから"



show emi basic_closedgrin_gym
with charachange




emi "それに、夜更かししたくなかったら、宿題は今すぐやっつけないとだめだよ、久夫くん"


show emi excited_proud_gym
with charachange




emi "明日は朝練！　忘れないでね！"


show rin basic_absent
with charachange




hi "どうやって忘れるんだ？"


show emi basic_closedhappy_gym
show rin basic_awayabsent
with charachange





emi "それもそうか。というか、結局{b}あたしと{/b}一緒に時間を過ごすってわけだしね"



play sound sfx_emirunning

hide emi
with easeoutleft

stop sound fadeout 3.0

show bg school_track_on at center
show crowd at center
show rin basic_awayabsent at center
with charamove



"笑美はそう言いながら素早く手を振って、メダルを、あるいはメダルとして扱われているものを受け取りに走っていった。"



scene bg school_courtyard
show crowd
show rin relaxed_nonchalant at center
with locationskip

stop music fadeout 7.0



"俺と琳はトラックを離れる。寮に戻ってくるまで、琳はほとんどずっとなにか深い考えごとをしている。"




"俺が見送ると、琳は口を開く。"

show rin basic_deadpan
with charachange


rin "上着、返してもらってなかったと思うけど"


hi "もちろん、そのうち返してもらうよ"

show rin basic_deadpannormal
with charachange



rin "いいね。出たとこ勝負ってわけだ"


show rin basic_deadpandelight
with charachange





rin "すごく笑美的だね"


hide rin
with charaexit


"この奇妙な言葉とともに、琳は振り向いて建物に向かう。"




"正直、そんなに大したことか？"






"笑美は寒がっていたし、俺が間違ってなければ、痛みもあったはずだ。"





"そのうちの一つぐらいを解決してやるのは当然の反応だろう。"





"もっとも、笑美が返すのを忘れてれば、上着を失くす可能性はあるけど。"



"琳はいいところをついてくる。"


"それでも、なにからなにまで心配するわけにもいかない。"



"だって、最近は暖かくなってきてるし。"





"上着はなくてもいい。"




"変だな。前は自分のことはもう少しちゃんとしてたと思うけど。"





"『笑美的』だって？"










"悪くないかもな。"



stop ambient fadeout 2.0

scene black
with dissolve

label jp_E9:







scene bg school_nurseoffice
show nurse concern at center
with locationchange




nk "ここのところ薬は飲み忘れてないだろうね？"





play music music_nurse fadein 0.5




nk "少し雑音が聞こえる"







nk "数日は無理をしないほうがいいね"






"ナースの言葉が朝練の疲労なんかよりずっと深く胸に刺さる。"







"数日は無理をしないほうがいい？"





"やっぱり黙っておけばよかった。"









"俺は床を見つめる。本当にバカみたいな気分だ。"





"薬を飲むのなんて忘れてたに決まってるじゃないか。"







"笑美より先に競技場に着くために、俺は毎朝大急ぎで部屋を出るようになっていた。"









"数日前の競技会が終わって、俺は……すごく刺激を受けた。"









"それで俺は、笑美が来る前に何周か走ってウォーミングアップをしている。"







"でも今日いっしょに走っていたとき、胸に小さな痛みを感じた。"





"本当に小さかったし、ほんの一瞬だけだったので、ナースにそれを伝えた。"








hi "ほんとに、ひどくはなかったです"








hi "というか、走れてたし走り終わっても問題なくて、だからほんとにぜんぜんひどくはなくて……"






"ナースに言い訳をしているような気がするのはどうしてだ？"








"さらに、なんで俺は痛いにも関わらず走り続けるのを正当化しなきゃいけないと思ってるんだろうか？"










"結局、俺は笑美を心配させたくないんだってことになる。とっくに心配してるみたいだけど。"









"なんで笑美が異常に気づいたのかわからないけど、俺が軽くよろけたと言っていた。"








"ナースにそれを伝えろと言い張ったのも笑美で、その笑美を結局は不安にさせてしまっていることが嫌だ。"








"医務室の外で笑美がうろうろしている間に、ナースは残念そうに首を振る。"







nk "久夫くん、新しい習慣を身につけるのが難しいのはわかるけど、あれこれ面倒なことになるのがいやならもっと努力しないとだめだよ"







nk "薬を飲むのも忘れちゃいけないし、頑張りすぎるのもいけない"








hi "でも頑張らなかったら、どうやって上達するんですか？"





"どこからこんな言葉が出てきたのか、自分でもわからない。"







"ナースは見当がついているみたいだ。"




show nurse fabulous
with charachange




nk "あれ、どこかで聞いたような台詞だね？"






show nurse grin
with charachange




"ナースは笑って俺の肩を叩く。"








nk "はは！　あの子の性格がうつってるんだろうね"






show nurse concern
with charachange



"ナースの表情がまた変わり、真剣な様子に戻る。"







nk "いいかい、べつに頑張るなと言ってるわけじゃないんだよ"









nk "でもそれは薬を飲むなという意味じゃないし、胸が痛み始めてもやめるなという意味でもない"






nk "僕がここのスタッフとして働いている間は、一人たりとも死人を出したくないと思ってるんだ"



show nurse neutral
with charachange



nk "確かにちょっと大変な目標だけど、いつも努力はしているよ"






"認めるのはしゃくだけど、ナースの言うとおりだと思う。"







"薬を飲むのは忘れないようにしなきゃだめだ。"








hi "そうですね。心配させてすみません"





show nurse fabulous
with charachange




nk "誰が？　君は賢いから大丈夫、だよね？"





show nurse neutral
with charachange




nk "君ならちゃんとやれるはずだよ、久夫くん。君みたいな状況なら、早くそれを学ばないとね"







hi "わかってますって"




"ナースの表情が急にうさんくさくなる。"




show nurse fabulous
with charachange




nk "じゃあ、笑美ちゃんとの練習が楽しくなってきてるってことかな？"







hi "ええ、自分にとっても本当にためになってますから"






hi "その、今日までは今までよりずっと健康になった感じがしてたんです"






hi "それに笑美の走りは見ていてすごいと思うんです。陸上競技会の時の笑美、見ましたか？"






hi "本当にすごかったんですよ！"




show nurse grin
with charachange




"ナースはうなずきながらずっと笑っている。"








nk "まったくだね、久夫くん。用事があって最初の数レースしか見られなかったけど、あとで本人が全部教えてくれたよ"





show nurse fabulous
with charachange




nk "親切に上着も貸してあげたんだってね、そういえば"







hi "え？　ああ、いえ別に大したことじゃ"






"本当にすっかり忘れていた。まだ返してもらっていない。"




show nurse neutral
with charachange




"ナースが微笑むので、からかわれているような気分になる。"






nk "君にはそうじゃなくても、笑美ちゃんはとても感謝していたよ"





nk "それと君が毎朝一緒に走ってくれていることも、だね"








"不意打ちを受けた気分だ。確かに、朝練を続けるには誰かと一緒のほうが楽だとは言っていたけど、俺は親切で何かしているなんて気持ちは全くなかった。"







hi "笑美の方が、僕が医者の指示に従うのを手助けしてくれてるんだと思ってましたよ"





nk "あの子はね、君がいると頑張るんだよ"






nk "一緒に走ってくれる人がいたら、もっと頑張る"






nk "そして君と一緒にいるときは、もっともっと頑張るんだ。君だから、だよ"






hi "それは一体どういう意味ですか？"

show nurse grin
with charachange




nk "お、知りたそうだねえ？"






"ナースは心底意地悪そうに笑った。"




show nurse neutral
with charachange




nk "いや、まじめな話、君があの子の友達だからさ"







nk "手塚さんと走っても、同じように頑張るだろうと思うよ"




nk "まあ、多分だけど"







nk "でも大事なのはそこじゃないんだ"






nk "君は笑美ちゃんの助けになっているんだよ、そう思っていなくてもね"


show nurse fabulous
with charachange



nk "そして、笑美ちゃんはそのことに感謝している。何も言わないとしてもね"






hi "『何も言わないとしても』ってどういうことです？"





show nurse neutral
with charachange



nk "あの子は多くを語らないけど、僕は長い付き合いだから言わなくてもだいたいわかるんだ"





"なるほど、ナースが何を言っているのかまったくわからないな。"






"笑美はいつもおしゃべりなタイプに見えるけど。"





hi "そうなんですか"



"話がそれていることに突然気づいて、ナースは口をつぐむ。ちょっと決まり悪そうだ。"




show nurse fabulous
with charachange


nk "いずれにせよ、別に朝練をやめる必要はないよ"

show nurse neutral
with charachange


nk "ただし、数日は走らずに歩くこと。まずは落ち着かせよう"


show nurse concern
with charachange




nk "あと、薬は飲めよ！"





scene bg school_nursehall
with locationchange

stop music fadeout 0.3
play sound sfx_impact

show emi basic_confused_gym_close
with vpunch



"俺は笑いながら医務室を出て、そのまま笑美にぶつかる。"




show emi basic_confused_gym
with charadistant


hi "おっと、ごめん"

show emi basic_hes_gym
with charachange



emi "大丈夫だった？　ナースくんはなんて？"






emi "病院に行かなきゃいけないの？"



show emi basic_shock_gym
with charachange



emi "どうしよう、あたしのせいだ、そうでしょ？"




show emi basic_closedsweat_gym
with charachange




emi "無理させすぎちゃってたんだね、させてなかった？"




show emi excited_sad_gym
with charachange




emi "あたしって、ほんとバカ！"








"せきを切ったように言葉があふれる。とても動揺している。"






"正直にいって、こんなに俺のことを心配しているとは思わなかった。"




"笑美を落ち着かせないと……でもいったい、どうすればいいんだ？"







"頭に浮かんだ唯一の行動を取る。"



show emi basic_shock_gym_close
with characlose

play music music_serene fadein 6.0




"俺は笑美を抱きしめる。笑美が少しこわばったので、安心させようと頭をなでる。"







hi "おい、落ち着けって！"







hi "大丈夫だからさ。心配ないよ"




show emi basic_hes_gym_close
with charachange



"大丈夫だと言い続けているうちに、笑美の体がリラックスしていくのを感じる。"






"笑美が腕を背中に回してくる。俺が今すぐ倒れて死んでしまわないことを確認するかのように。"







"髪の香りが鼻をくすぐる。汗のような、でもこれがアドレナリンの匂いなんだろうか。活発さの匂いだ。"








"そして、ほのかなイチゴの香り。たぶんシャンプーだろうな。"





hi "薬を飲み忘れないように言われただけだ"



hi "心配しなくていい、笑美のせいじゃない"

show emi sad_depressed_gym_close
with charachange


emi "本当に？"


"俺の胸に顔を押し付けてきたせいか、彼女の声がくぐもって聞こえる。"



hi "本当だって、ただ数日間は激しい運動ができないだけだ"



"突然、俺たち二人の距離がとても近いことに気づく。"






"その近さがとても心地よいことにも気づく。"






"笑美の鼓動が落ち着いていくのを感じる。そして、俺は彼女の頭にあごを乗せたいのを我慢しなければいけなかった。"


show emi sad_grin_gym_close
with charachange




emi "よかったあ"








emi "もう本当に心配だったんだよ、久夫くん"




stop music fadeout 1.5

show nurse concern behind emi:
    center
    xpos 0.0 xanchor 0.3
    easein 0.5 xanchor 0.2
with Dissolve(0.5)



nk "笑美ちゃん、まだ入ってこないの？"




show nurse grin
with charachange




nk "……ああ、ごめん。お邪魔だったかな？"



show emi basic_shock_gym
with vpunch




"お互い火でもついたみたいに、俺たちはとっさに体を離す。"




show emi basic_hes_gym
with charachange



"笑美はそわそわと髪をなでつけ、笑う。"




play music music_emi fadein 1.0



emi "んなわけないでしょ！"




show emi sad_shy_gym
show nurse fabulous
with charachange


emi "えーっと、その、またね？"

show emi basic_closedgrin_gym
with charachange



emi "あ、あと久夫くん？"






hi "んー？"



show emi basic_annoyed_gym_close
with characlose

with hpunch




emi "薬は飲めよ！"






"最後の一言は肩へのパンチ付きだ。"




hi "わかった、わかった。覚えてるって"


hi "じゃあ、またな"

show nurse grin
with charachange





"俺には分からない冗談でウケているかのようにナースは再び笑い、俺に手を振る。部屋へと戻りながら、頬が熱くなるのを感じる。"






stop music fadeout 8.0

scene bg school_dormhisao
with locationskip




"シャワーを浴びないと。"








"冷たいのをだ。いま俺の頭を駆けめぐっている思考がなにかの兆しだとしたら。"





"笑美、とても柔らかかったな。"





"部屋に入ると薬が待ちかまえている。"








"何も考えずに、それを飲み込む。"







"練習が終わってから飲むことをなんで考えつかなかったんだろう。なぜか、起きたときに飲むか、ぜんぜん飲まないか、だと思い込んでいた。"





"でも違う、２４時間ごとに飲みさえすればいいんだ。一日のどの時間かは関係ない。"








"廊下での抱擁に考えがふらふらと戻る。"








"変だな、運動した後の人なんて臭いはずなのに、どういうわけか、笑美の香りは……似合ってた。かすかな汗の匂いはぴったりだった。"








"ほんとに、シャワーでも浴びなきゃな。"




scene black
with dissolve

$ suppress_window_after_timeskip = True

label jp_E10:

window hide None

scene bg school_roof
with locationchange

nvl clear

nvl show dissolve

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0


n "\n\n最近、屋上に上がるのがごく自然なことと思うようになっている。妙な感じだ。"




n "前の学校だったらそんなことは絶対にしなかっただろう。"







n "あのころは一人で食べる方が好きだった……いや、それは少し違う。一人でいるのも好きだったけど、人を観察するのも好きだったんだ。"





n "ずっと自分はそういう人間なんだと思ってきたけど、それは間違いだったみたいだ。"




n "とはいえ、自分はまともな心臓の持ち主だとも思っていたわけで、結果はご覧のとおりだ。"



n "自分のこと、あんまりわかってないんだな。"


n "今じゃ、俺は二人の連れと昼飯を食べるために屋上に来ている。"


n "しかも二人とも女子、というのがなおさら妙な感じだ。"



n "変な話だけど、前の学校の誰よりも、笑美と琳の方に親しみを感じる。"




n "もし俺が入院するはめになったら、少なくともお見舞いには来てくれるだろう、という気がなんとなくする。"


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

nvl hide dissolve

nvl clear

window show


"そんな思考を頭から追い出して、屋上からの眺めに集中する。"


"そよ風が吹き、太陽は空高く輝いている。"



"空は深い青色で、雲はほとんど見当たらない。暖かさが心地よく、俺は笑美たちが来るのを座って待ちながら、目を閉じて陽光が皮膚に染み込む感覚を味わう。"



$ renpy.music.set_volume(0.1, 2.0, channel="ambient")

window hide

scene black
with shuteye

with Pause(4.0)

window show



"意識の端に声が割り込んでくる。"




emi "――寝ちゃってるみたいだよ、琳"




rin "寝たふりかもね、私たちを油断させようとして"




emi "どうしてわざわざそんなことするのよ？"


rin "さあ"


emi "でも、いいとこ気づいたね"



emi "蹴っとばすかなにかして、ほんとに寝てるのか確かめたほうがいいね"



stop music fadeout 1.0


hi "えっ？　なに？"

$ renpy.music.set_volume(0.5, 5.0, channel="ambient")

scene bg school_roof
show rin basic_absent at tworight
show emi excited_happy_close at twoleft
with openeye

play music music_ease fadein 3.0


"笑美が背の低い女の子にしかできない姿勢で俺の頭上を覆う。真剣にこっちをのぞき込んでいる。"

show emi basic_closedgrin_close
with charachange



emi "あ、起きてる。じゃあ蹴っとばさなくてもよさそうだね"



show rin basic_deadpan
with charachange



rin "それも君の大計画の一部だったの？"



hi "いったい何の話だよ？"

show emi basic_grin_close
with charachange



"笑美は肩をすくめ、その動きでツインテールが跳ねる。"


show emi basic_closedhappy_close
with charachange


emi "あたしもよくわかんない"

show emi sad_grin_close
with charachange


emi "こんなところで居眠りしちゃうなんて、よっぽど疲れてたんだね"

show emi basic_closedgrin_close
with charachange



emi "まあ、確かにすごく気持ちよさそうだけど"



show emi basic_closedgrin_close:
    yanchor 0.9
with ease
with vpunch


"笑美は俺のとなりにどすんと腰を下ろして食べ始める。"

show rin basic_absent
with charachange

show rin basic_absent:
    yanchor 0.77
with charamove



"琳は俺と笑美に向かい合って座る。おかげで俺の隣にいる笑美の存在を余計に意識してしまう。"





"琳のことをよく知らなければ、きっとわざとやっていると思っただろう。"




"俺は自分の食事に集中して、琳と笑美の会話をできるだけ頭に入れないようにする。"




"しかし必死の努力にもかかわらず、笑美が口を開くと俺の目はついそちらに向かってしまう。"


show emi basic_grin_close
with charachange



"笑美が考えごとをするとき、口をすぼめて目をちょっと細めるのに気づく。そうすると思考が深まるとでもいうように。"



show rin basic_deadpan
with charachange

show emi basic_grin_close at Transform(function=tf_leftrock)
with None

show emi basic_closedhappy_close at Transform(function=tf_leftrock)
with charachange



"琳がなにか言って笑美が笑うと、たぶん初めてだけど、笑美は全身を前後に揺らして笑うということに気づく。頭は後ろに投げ出して、ほとんどひっくり返りそうなくらいだ。"





"今の俺はそうとう気持ち悪く見えるだろうな。"



show emi basic_confused_close
with charachange



"このあたりで、笑美が俺の方を見ているのに気づく。声がちょっと高くなっていたので、たぶん質問をしただけだろう。"



hi "えっ？　ごめん、ちょっと今ぼんやりしてた"

show rin basic_deadpannormal
show emi basic_annoyed_close
with charachange



"笑美はあきれた顔をする。一方の琳はただ怪訝そうに眉を上げるだけで、それが関心を示しているという唯一のしるしだ。"



emi "久夫くんもクラスで進路調査票もらった？　って聞いたの！"



show emi basic_grin_close
with charachange


emi "ほら、あの『卒業後はどんな進路を希望しますか？』ってやつ？"



hi "ない……と思う。明日もらうのかも"


show emi excited_happy_close
with charachange


emi "なんて書くつもり？"


"とてもいい質問だ。"


"俺はずっと、高校を出たら大学に行くものだと思っていた。でも大学に入ってから何をするかなんて全然考えてない。"


"心臓発作やらなにやらで、俺はずっと長期的な計画なんて立てず、やってくる毎日を過ごすだけで精一杯だった。"





"もうそろそろ、また先のことを考え始めても大丈夫な気がする。"






"あいまいでもいいから将来のプランは持ちたい、といつも思っていた。だからプランを立て直すのはいいことだろうな。"



"もちろん、だからといって今の俺にはまるっきり……"


hi "……わからない"



hi "大学に行ってから考えるんだろうなって思ってた。それかサラリーマンにでもなるか。普通だろ"



"でも、俺は本当にそうしたいのか？　難しい質問だ。"



"たぶん、本当のところは何もしたくないんだろう。"


show emi basic_closedhappy_close
with charachange


emi "あんまり乗り気じゃなさそうな言い方だね"

show emi basic_closedhappy_close at Transform(function=tf_leftrock)
with None


"言いながら笑美は笑う。俺はまたその笑い声にとらわれてしまう。"




"すごく……女の子っぽくて。くすくすと高い声は、なんというか……ありきたりな表現だけど……小川のせせらぎ、みたいだ。"




"さらさらと笑美から流れ出てくるんだ。お腹から始まって、のどの方まで。"


"俺も笑い出してしまうのを止められない。伝染性だな、これは。"


hi "そうだな、俺もサラリーマンはないなって思う"


hi "でも正直言うと、最近は将来のことはあんまり考えてないな"


hi "最近は、一日一日をどう過ごすかってことに集中してるんだと思う"

show emi basic_grin_close
with charachange


"笑美はしばらく考えて、にっと笑う。"


emi "すごくいい考えだね、久夫くん！"

show emi excited_proud_close
with charachange


emi "あたしは『海賊』としか書いてないよ"



"俺は一瞬あぜんとした。そして笑い出す。"





"なんとか笑うのを止めて、息も絶え絶えに質問する。"




hi "おま……お前さ、それ、本気じゃない、よな？"

show emi sad_annoyed_close
with charachange


"笑美はすねたふりをする。"


emi "だって、足ならもう準備できてるし、だからいいかなって思って……"

show rin basic_amused
with charachange


"その一言に、あの琳まで面白がっている。"

show emi basic_annoyed_close
with charachange


emi "見てなさいよ、あたしは大海原の脅威になってやるんだから！"


emi "みんな首を洗って待ってろー！"

show emi basic_closedhappy_close
with charachange


emi "海賊声の練習だってしてるんだよ！"

show emi basic_closedhappy_close at offscreenleft
with ease

hide emi
with None

show emi basic_closedhappy at offscreenleft behind rin
with None

show emi basic_annoyed at left
with ease


"笑美は突然立ち上がり、命令をがなり立てながら威張った態度で屋上を歩き回る。"

show emi basic_annoyed at center
with ease


emi "おらぁ野郎ども、やつらに大砲ぶち込んでやれ！"


show emi basic_annoyed at twoleft
with ease


emi "やつらのはらわたを引きずり出してガーターにしてやるぞ！"



show rin basic_deadpanamused
with charachange


rin "それ意味わかって言ってるの？"

show emi basic_confused
with charachange


"琳が不意に割り込んだので、笑美はその場で止まってしまう。"

show emi sad_shy
with charachange



emi "あんまり"


show emi basic_closedgrin
with charachange


emi "でもこういうのは言い方が大事なの！"

play sound sfx_warningbell

show emi basic_hes
show rin basic_awayabsent
with charachange


"なおも実演を続けようとする笑美だけど、鳴り響くベルがその邪魔をする。"

hide emi
with easeoutleft


"笑美はすぐに走り去ってしまい、琳と俺だけが屋上に残される。"

show rin basic_awayabsent:
    xpos 0.5
show bg school_roof at bgleft
with charamove

show rin basic_deadpancontemplation
with charachange


"琳はしばらく俺をじっと見つめている。"


hi "どうか……したのか？"

show rin basic_lucid
with charachange


"琳はしばらくその質問を真剣に考える。"


"そして長い沈黙の後、首を左右に振る。"

show rin basic_deadpannormal
with charachange


rin "ううん"


hi "ああ、そっか……"


extend "じゃあ、どうしてじっと見てたんだ？"

show rin basic_awayabsent
with charachange


"琳はまた首を振る。"




rin "ううん、わからないね"





hi "何が？"

show rin basic_deadpan
with charachange




rin "見つめてるの。君と笑美はそうしてるみたいだけど、私は見つめられてない"







"まいった。俺が笑美を見てるのを見られてたんだ。恐らく、もう俺のことを変態か何かだと思ってる。"




"いや、そうでもないか。なにせ琳のことだからな。"


"でも自己弁護はしておく必要がある気がする。"


hi "見つめてたんじゃないよ。疲れてただけだ"

show rin basic_deadpancontemplation
with charachange




"琳は文字通り鼻で笑うけど、でも何も言わない。"





hi "いや、ほんとだから！　ただ……気が散ってたんだよ、それだけだから"

show rin basic_lucid
with charachange


rin "んー"

stop music fadeout 4.0


"さっさとこの会話を終わらせたくて、俺は教室に戻る。"

stop ambient fadeout 2.0

scene bg school_scienceroom
show misha cross_grin at twoleft
show shizu behind_blank at tworight
with locationskip


"静音とミーシャ、二人の化け物に出迎えられる。俺に用がありそうな感じだ。"



"まあ、どっちみち、静音はなにか用がありそうな見た目だけど。"




"ミーシャは、もう本当に今すぐにでも笑い出しそうな様子だ。"


play music music_shizune fadein 3.0

show misha perky_smile
with charachange


mi "まーた屋上行ってたの、ひっちゃん？"

show misha hips_frown
with charachange


mi "屋上は危ないんだよ、知ってるでしょ～？"

show shizu basic_angry
with charachange


shi "……"

show misha sign_smile
with charachange


mi "そうだよ～！"

show misha hips_smile
with charachange


mi "あそこで何かけがをしても、学校は責任取れないんだからね！"

show misha cross_frown
with charachange


mi "それに、校則違反で言いつけたっていいんだよ～！"

show misha cross_frown_close
with characlose


"ミーシャは身を乗り出して、いわくありげにひそひそとささやく。"

show misha sign_smile_close
show shizu behind_smile
with charachange


mi "でもそんなことしないよ、ひっちゃん！"

show misha hips_grin_close
with charachange



mi "三人いっしょにいるひっちゃんたち、かわいすぎるよ～！"

show misha cross_laugh
with charadistant


"急に顔を赤くした俺を見ると、ミーシャはまた体を起こして笑い出す。"


mi "わははは～！"

show misha cross_grin
with charachange


mi "ほんとにからかいやすいね、ひっちゃんってば～！"


hi "おい、勘弁してくれよ"


hi "こっちはまだ来て日が浅いんだぜ、一応"


hi "新入りをそんな風にいじめるのは意地が悪いんじゃないか？"

show misha hips_grin
with charachange


mi "いいえ～！"

show misha sign_smile
with charachange



mi "ひっちゃんが新しい環境になじめるように手伝ってあげてるの！"



hi "ああ、なるほどな"


hi "だったら……そこまで熱心になる必要はあるのか？"

show misha hips_grin
with charachange



mi "うんっ！"


show misha hips_smile
with charachange


mi "あ！　それはともかく、ひっちゃん、今朝探してたんだけど、部屋にいなかったよね！"



hi "そりゃいないよ。朝練に行ってたか、教室に来てたか、どっちにしても朝早かったんだよ"



hi "お前とは違って"

show shizu basic_angry
show misha hips_frown
with charachange


"静音は怒ったみたいだ。そこから一拍おいてミーシャも続く。まあ、怒ったふりかもしれないけど。"


mi "生徒会の仕事があったからよ！　ひっちゃんのためにわたしたちががんばって仕事してることに感謝しなさいよ～！"



hi "あー、してるしてる。それで俺に用事って何だったんだ？"


"またこいつらが俺を汚れ仕事に引っ張り込もうとしてるんじゃなければいいけど。"

show misha sign_smile
with charachange



mi "渡さないといけないものがあったんだけど～、ひっちゃんが見つからなかったから、部屋に置いてきたんだよ！"




hi "もの？　どんな？"


show misha hips_grin
with charachange


mi "あー、部屋に戻ったらわかるよ、ひっちゃん～！　わははは～！"

hide misha
hide shizu
with charaexit


"武藤先生が入ってきて俺たちの会話は終わり、みんな自分の席に戻る。"

stop music fadeout 10.0





"なにか変だと気がついたのは、俺も自分の席に着いて先生がなにやら話を始めたころだ。"








"琳が言ってた『君と笑美はそうしてるみたい』って、どういう意味だ？"




"笑美も何かを見つめてたのか？"



"一瞬、俺が笑美を見つめていたように、笑美も俺を見つめていたという可能性を考える。"



"そんなバカな。あるわけない。"



"ただ、もしそうだとしても俺は構わない、という気持ちはある。"


"でもその可能性は考えない方がいい。期待をしすぎる必要はない。"


"考えてみれば、いつから俺はそんな期待をするようになったんだ？"


"頭を振ってそんな思考を追い払い、授業に集中する。"

scene bg school_dormhallway
with shorttimeskip


"放課後、俺は寮の部屋へと向かう。今日は武藤先生が山のような宿題を出してきたからな。"

play sound sfx_impact2

show kenji tsun at left
with vpunch


"でも部屋のドアを開ける前に、突然健二が自分の部屋から紙切れをまき散らしながら飛び出してきて、邪魔されてしまう。"



ke "おい、話がある"

play music music_kenji fadein 1.0



ke "お前が屋上で会ってるふざけた連中のことだよ"



ke "奴らと会うのはやめるんだ"


hi "なに？"


ke "あの腕なし脚なしのビックリ人間どもと屋上で走り回ってるじゃねえか！"





ke "女だぞ、お前！　あんなのと走り回ってたら殺されちまうぞ！"



hi "話が見えないんだけど"

show kenji neutral
with charachange



"どうやら、自分の言いたいことを辛抱強く説明するつもりらしく、健二は溜息をついて眼鏡を直す。"




ke "なあ、俺たちは友達だ、だからお前のために言ってやってるんだぞ"



ke "だがもし俺が人を殺すとしたら、そいつを屋上から放り投げて事故に見せかける"

show kenji tsun
with charachange



ke "もし俺に思いつけるなら、奴らだって同じことを思いつけるのはわかるだろ"




ke "あいつらは狡猾だ――ほとんど、俺と同じくらいにな"




hi "なるほど"

show kenji happy
with charachange


ke "わかってくれたか！"




ke "話ができてよかったぜ"


show kenji neutral
with charachange


ke "５００円貸してくれ"



hi "……悪い、なんだって？"


show kenji tsun
with charachange



ke "飲み物買いたいんだよ！"



ke "俺は一日引きこもってたんだ。水道水はもう奴らの手で汚染されてる。知ってるよな"



ke "だから缶入りの飲み物を買いだめしないといけないんだ、いいか？　でもそのためには５００円いるんだ"

show kenji neutral
with charachange



ke "それにお前は俺のタイミングばっちりのアドバイスで命拾いしたんだからな、５００円くらい恵んでくれたっていいだろ"



"なんというか、こいつがどっかに行ってくれるなら、５００円なんて安いもんだ。"

stop music fadeout 6.0

show kenji happy
with charachange

show kenji happy:
    easeout 0.5 alpha 0.0 xanchor 0.2
with None



"俺が金を渡すと、健二はうなずいて感謝の意を示し、廊下の先へと走り去る。でもドアの鍵はかけ忘れたままだ。"



"なんて疲れるやつなんだ。あいつの気が変わる前に戻った方がいいな。"

scene bg school_dormhisao
with locationchange



"ん？"



"ドアを閉じると、床に落ちていたものにかかとが触れる。"


"明るい色の、長方形の紙切れだ。ああ、これがミーシャがさっき言ってた『渡さないといけないもの』か。"


"たぶん、ドアの下から滑り込ませた生徒会のプリントだろう。"


"でもそれを拾い上げたとき、その予想はとんでもない間違いだったと思い知る。"


"誰かが俺に昔ながらの手書きの手紙を送っていたんだ。"




"この時代にわざわざ手紙を書いてよこす人なんているのか？　でも、手紙を受け取る可能性がどんなにありそうになかろうと、俺が手にしているのは間違いなく手紙だ。"






"宿題を終わらせて、夕食を食べて、明日の朝のランニングのために寝るつもりだった。"



"でも当たり前だけど、手紙は俺の関心をつかんでいた。俺は机に座り、よく見てみることにする。"

scene ev hisao_letter_closed:
    xalign 0.5 yalign 0.5 zoom 1.1 subpixel True
    acdc_warp 10.0 zoom 1.0
with locationchange

play music music_rain fadein 5.0


"山久で受け取る初めての手紙だ。だから仮にそれが手書きの手紙なんてレアな代物でなかったとしても、特別な気持ちになったことだろう。"


"封筒の裏に丁寧な字で書かれた送り主の名前、それを見て俺はさらに戦慄する。"


"『岩魚子』。"




"どうして俺に手紙なんて書いたのか、見当もつかない。転校して以来、前の学校の連中とは全く連絡を取っていない。そして岩魚子が俺に手紙を書く気になるなんて、最もありえそうにないことだった。"




$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve



n "\n\n\n\n\n最後に岩魚子と会ったときは、ひどく気まずかった。恥ずかしくなるくらいに。彼女は俺の病室に来て、義理っぽくリンゴをむいてくれて、その後は３０分間お互いに一言も話さなかった。"





n "岩魚子は『さよなら』と言って、俺の目を見ないままドアを閉じた。"





n "あの一連の見舞いは、恐らくお互いにとってとてもつらいものだった。あれが自然な終わり方だったのかもしれない。"



n "岩魚子が見舞いに来てくれるたびに、話しかけたいと思った。でもそのたびに何かが俺を引き留めた。"



n "毎回俺は話すことができなくて、それで次はもっと話しづらくなった。"


nvl clear



n "\n\n\n\n岩魚子はあまりに後ろめたそうに見えて、俺は気分を悪くさせるようなことを言いたくなかった。どんなことを言えばよかったのか、俺にはさっぱり分からなかった。"




n "岩魚子は俺の心臓発作が自分のせいだと思ってたんだろう。そんなことはあるはずがないけど、でもそれを知っているのとそう信じこんでしまうのは全く別のことだ。"






n "あれは岩魚子のせいじゃないんだ、と俺は言って、彼女はうなずいた。あの時ああならなくても遅かれ早かれ別の原因で俺の心臓はやられていた、それをわかってくれたんだと、俺は本当にそう思っている。"





n "でも病室のドアを開けて中に入ってくるときは毎回、岩魚子はどうしようもなく悲しそうに見えた。"


n "だから俺は言いたかったことを一度も言えなかった。結局、それが岩魚子を余計に傷つけていたのかもしれない。"

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl hide dissolve
nvl clear

scene ev hisao_letter_open
with locationchange

window show



"注意深く、俺は封筒を開いて、折りたたまれた手紙を取り出す。"


window hide


$ written_note("久夫くん、\n\nお元気ですか？　新しい学校で、元気に楽しくすごしているといいな。みんな寂しがってます。２年のクラスのほとんど全員が３年になって３－１にクラス分けされたので、最初からみんなとても気楽にしています。きっと久夫くんもこのクラスに入ってたんじゃないかな。")



$ written_note("３年生になって、みんな卒業試験のことで頭がいっぱいになっています。まだずっと先の話なのにね。先生たちはいつもその話を持ち出してます――おじいちゃんの橘先生まで。そうそう、橘先生は今年の担任です。信じられる？　私たちが２年生から上がったら絶対に定年退職すると思ってたけど、結局残っていて、みんなに試験のことを口うるさく言ってるんだよ。\n")




$ written_note("そういうことがあるので、３年の雰囲気がすごくピリピリしているんだろうなって思います。正直に言うと、試験でいつもそれなりにいい成績を取ってはいるけど、私もなんだか自分に自信がなくなってきています。\n\n\n\n\n")


$ written_note("私たちがもう最高学年だっていうのが、とても変な感じだと思わない？　月日は本当にあっという間に過ぎてしまった。どこに行っちゃったんだろう。新しく入ってきた１年生はとっても初々しくて、なんだかすごく純真に見えます。私も１年の時はあんな風だったのかな、なんていつも考えてます。１学期の間ずっと、そんなノスタルジックな気持ちを抱いてました。\n\n\n")


$ written_note("他にも言いたいことがあります。冬のあの時から、言わなくちゃいけなかったことがあると思って、こうして手紙を書いています。直接伝えることができなかったのを、本当に後悔しています。言い訳のしようもありません……\n\n\n\n\n")

window show


"ああ、もうたくさんだ。"

scene bg school_dormhisao
with locationchange


"手紙をくしゃくしゃに丸めて部屋の向こうに放り投げる。狙いが悪かったので、ゴミ箱を外れてナイトスタンドの下に転がり込んでしまう。"





"あれは俺を捨てたことへの謝罪だった。でも、今の俺にそれがまだ本当に必要か、よくわからない。"








"入院していたころのことは大昔のように思えるし、ここでは、そして今では、他に大事なことがある。"



stop music fadeout 8.0



"笑美だってそうだし。"





"入院中に捨てられることでいい気分はしなかったけど、それはもう気にするようなことではない。"





"事実、この手紙が来るまでは、入院中のことなんてずっと前から考えもしていなかった。手紙を受け取ること自体がうっとうしいとさえ思えてくる。"





"俺にだって、勉強しなきゃいけない試験がある。過去を振り返ってる時間はない。"




"さて、宿題しなきゃ……"

scene black
with dissolve

label jp_E11a:

scene black
with None


hi "で、今日の予定はどうするんだ？"

play music music_daily fadein 1.0

scene bg school_girlsdormhall
with dissolve


"女子寮の中、笑美と琳の部屋のすぐ外の廊下で、俺は辛抱強く待っている。"


"どうやら笑美は琳の着替えを手伝っている。"



"まったく合理的だと思う。笑美の手伝いなしに琳がどうやって服を着るのか想像もつかない。"





emi "ピクニック！"



hi "ピクニック？"


emi "そのとおり！"


hi "なかなか楽しそうだな"


emi "うん、でしょー？"




"琳がこのときを見はからって所見を述べる。"





rin "今日は空が怪しいよ"


"実はこっちに来るとき、俺も気づいていた。早朝は日が差していたのに、午後になるとうってかわって空が薄暗くなっている。"


"空気もなんだか重い。暴風雨の前触れだ。"



"傘を持ってきた方がよかったかな……"



hi "琳の言うとおりだな"


hi "笑美、雨に降られるかもしれないけど、本当にいいのか？"



"なんでわざわざこんなこと聞いてるんだろう。"

show emi basic_shock:
    center
    xpos 0.9
    easein 0.5 xpos 0.7
with charaenter



"琳の部屋から笑美が廊下に飛び出してくる。止めようなんて口にすることさえ信じられない、といった顔だ。"





emi "当たり前でしょ！"

show emi basic_annoyed
with charachange





emi "なに、雨が降りそうってくらいであたしがやめるとでも思ってるの？"






"笑美のけんか腰の態度に思わず顔がにやけてしまう。降るなら降ってみろと言わんばかりだ。"


"大自然がその辺を歩いていたら、笑美はたぶん取っ組み合いのけんかを始めているだろう。"




"少なくとも競走で勝負を挑むだろうな。"






"実際、今日の笑美はほとんど攻撃的なくらい元気だ。"



show rin basic_absent:
    center
    xpos 0.9 alpha 0.0
    ease 1.0 xpos 0.7 alpha 1.0
show emi basic_annoyed at twoleft
show bg school_girlsdormhall at bgleft
with charamove



"琳はふらふら廊下に出てくる。いつも通りの見た目だ。"



hi "さて、じゃあみんな準備はいいか？"

show emi basic_closedhappy
with charachange


emi "いいよ！"

show rin basic_deadpannormal:
    tworight alpha 1.0
with charachange


"琳はうなずき、一言つぶやく。"

show rin basic_deadpan
with charachange


rin "バスケット"


hi "なに？"

show rin basic_deadpannormal
with charachange



rin "バスケット。笑美の部屋の。久夫が持って"


show emi basic_hes
with charachange



"笑美はきまり悪そうに口の前で手を合わせる。"


show emi basic_closedsweat
with charachange


emi "あっちゃー！　忘れるところだった！　助かったよ、琳！"

show emi basic_closedsweat at offscreenleft
with ease

with Pause(0.3)

show emi basic_closedgrin at twoleft
with ease


"笑美は自分の部屋に飛び込むと、たっぷり荷物が詰まったピクニック用のバスケットらしきものを持って出てくる。"

with vpunch


"手渡されたバスケットはずっしりと重い。なんだこりゃ、どれだけ食べ物を詰め込んだんだ？"



"……それよりも、どうやってこれだけの物を買うお金を手に入れたんだ？"



hi "じゃあ、もう大丈夫だな？"

show emi basic_grin
with charachange


emi "うん！"

show rin basic_awayabsent
with charachange



"琳はまたうなずいて、俺たちは寮を出る。"


scene bg school_courtyard_rn
with locationskip


"１０分ほど中にいた間に、空はあっという間に灰色になっていて、俺はつい顔をしかめる。"




"それでも、笑美は空の色なんてささいなことを心配しているようには見えない。俺たちが歩くそばで、笑美はまさにスキップしている。"




"それで思い出した……"


hi "どこに行くんだ？"



"その問いに笑美は急に立ち止まって、俺にきまり悪そうな目を向ける。"


show emi sad_shy_rn at center
with charaenter


emi "えっと、実はあんまり考えてなかったんだよね"


emi "久夫くん、どこか行きたいところある？"


"そうだな、学園祭の時に食事をしたところが浮かぶけど、せっかくだし学校から出るのもいいかもな。でも町中にちょうどいい場所があるかどうかはわからない。"



"口を開こうとしたちょうどそのとき、予想外にも琳が割り込んで意見を述べる。"


show emi sad_shy_rn at twoleft
show bg school_courtyard_rn at bgleft
with charamove

show rin basic_deadpan_rn at tworight
with charaenter


rin "町の画材屋の近くに公園があるよ"

show emi basic_closedhappy_rn
with charachange


emi "ナイスアイディア、琳！　あそこのこと完全に忘れてたよ！"


"ピンチは避けられたな。"


hi "行き方は知ってるのか、琳？"

show rin basic_deadpannormal_rn
with charachange


"琳は肩をすくめる。"

show rin basic_awayabsent_rn
with charachange


rin "たぶん"

show emi excited_amused_rn
with charachange


emi "それで十分！"


"ちゃんと知ってる方がありがたかったけど……でもまあ、いいか。"



hi "案内頼むよ、琳"


scene bg school_gate_rn
with locationchange


"俺たち３人はさっさと校門を出て、町へと向かう道を下る。"


scene bg school_road_rn
with locationchange



"バスケットがちょっと重い。公園が近くだといいけど。"


scene bg suburb_roadcenter_rn
with locationchange


"画材屋の前を通り過ぎる。琳の足取りが少しばかり遅くなる。"



"笑美がそれに気づいて立ち止まる。"


show emi basic_grin_rn at twoleft
show rin relaxed_nonchalant_rn at tworight
with charaenter


emi "見ていきたいの、琳？"

show rin basic_awayabsent_rn
with charachange


"琳は肩をすくめる。"

show rin basic_deadpan_rn
with charachange


rin "いるもの、何もないし"

show emi excited_proud_rn
with charachange


emi "ほんとにいぃぃ？"

show rin basic_delight_rn
with charachange

show rin basic_deadpandelight_rn
with charachange




"琳の顔にほんのかすかな笑みが浮かんで、すぐにいつも通りの表情に戻る。"



show rin basic_deadpan_rn
with charachange




rin "人生って気まぐれだけど、少なくともこれはほんとのほんとだよ"



show rin basic_deadpanamused_rn
with charachange



rin "ご提案ありがと"



show emi basic_closedhappy_rn
with charachange


emi "まあ、あたしがバスケット運んでるわけじゃないしね"

show emi basic_grin_rn
with charachange


emi "でも久夫くんなら気にしないと思うよ、ね？"


hi "おう、当たり前だろ。こんなの全然重くないし"


"腕を曲げて強調してやる。"

show emi excited_laugh_rn
with charachange


"笑美は笑いそうになるのをこらえて、突然たどり着いた公園の方を指さす。"

$ renpy.music.set_volume(0.02, 0.0, channel="ambient")
play ambient sfx_rain fadein 15.0

scene bg suburb_park_rn at bgright
with locationchange


emi "あっ、あたしここ覚えてる！"

show emi basic_closedhappy_rn
with charachange


emi "あのとき琳にぶつかったんだっけ、違う？"

show emi basic_closedhappy_rn at twoleft
show bg suburb_park_rn
with charamove

show rin basic_deadpannormal_rn at tworight
with charaenter


"琳の眉が少しだけ持ち上がる。"

show rin basic_deadpan_rn
with charachange


rin "そうかもね"

show rin relaxed_boredom_rn
with charachange


rin "どっちにしても、断定する気はないけど"

show rin relaxed_nonchalant_rn
with charachange


rin "記憶ってのは、油断のならない代物なんだよ"


"へえ。結局全員無事にたどり着いたじゃないか。"


"太陽は今もまったく姿が見えない。でも笑美も琳も気にしていないようだ。"

scene ev picnic_normal:
    yalign 1.0 subpixel True
    easein 8.0 yalign 0.0 
with whiteout









"俺たちは芝生の上に座れる場所を見つける。バスケットをようやく下ろせるのもありがたい。"





"びっくりするほどの量の食べ物が用意してある。笑美のチームメイトか誰かも呼んであったんじゃないだろうな？"






emi "あたし、おなかペコペコ！　みんな食べよ！"


"もう何年間も食べ物を口にしていなかったかのように、笑美はすごい勢いで食べ始める。"

stop music fadeout 2.0

play sound sfx_thunder

show ev picnic_rain:
    yalign 0.0
with charachange





$ renpy.music.set_volume(0.2, 0.5, channel="ambient")

show rain light
with dissolve


"俺が食べ物に手を伸ばそうとしたそのとき、最初の雨粒が手の甲に落ちるのを感じる。"


hi "ありゃ"


hi "やっぱり天気は俺たちに味方してくれないみたいだな"

hide ev
show bg suburb_park_rn behind rain
show emi sad_grit_rn behind rain:
    twoleft
    ypos 1.15
show rin basic_absent_rn behind rain:
    tworight
    ypos 1.2
with flash


"笑美は、それだけで雨が引っ込むと言わんばかりに空をにらみつける。"


"本当に笑美ならやってのけるんじゃないか、と思いそうになる。ものすごい目つきだ。"

show emi basic_annoyed_rn
with charachange


emi "味方しなかったらただじゃおかないんだから"


show emi sad_angry_rn
with charachange


emi "聞いてるの、空？　今すぐ雨降らせるの止めなさい！"



"堂々とした口ぶりだったけど、空は笑美の言うことを聞く気はなさそうだ。"


$ renpy.music.set_volume(0.5, 4.0, channel="ambient")

show rain medium
with dissolve


"それどころか雨足は強くなっていく。琳はことの成り行きを嫌って鼻にしわを寄せる。"


show rin basic_deadpan_rn
with charachange


rin "残念"

show emi basic_confused_rn
with charachange


emi "どういうこと？"

show rin basic_deadpannormal_rn
with charachange


"琳は肩をすくめる。"

show rin relaxed_nonchalant_rn
with charachange



rin "ここに出てこなければ、絵に描けたのに。できなくて残念、ってこと"



"怒っているとか、いらだっているとか、そういう風には見えない。ただちょっと残念そうなだけだ。"

show emi basic_closedhappy_rn
with charachange


"笑美は琳の言葉を聞いて笑い出す。"

show emi basic_grin_rn
with charachange



emi "やっぱり、あそこの画材屋に寄った方がよかったみたいだね？"

$ renpy.music.set_volume(1.0, 6.0, channel="ambient")

show rain normal
with dissolve



"俺たちがさっさと逃げないことに怒っているかのように、雨はさらに強くなる。"




"今までは暖かい気温に恵まれていたけど、雨はけっこう冷たい。傘を持ってくればよかったな。"


hi "なあ、どこか中に入った方がいいんじゃないか。濡れちゃうぞ"

show emi basic_confused_rn
show rin basic_absent_rn
with charachange


emi "もうみんなびしょ濡れじゃん、久夫くん"



hi "そうだけど、中に入れば乾かせるし、雨が止むのも待てるかも。風邪だのなんだのは嫌だろ？"


show emi basic_annoyed_rn
with charachange


"笑美はしばらく考えている。この天気にもめげずに、雨に降られてもいいから外に出ていたい気持ちがあるんだろうな。"


"笑美には残念だけど、天気は俺たちの都合なんてまるで考えてはくれない。"

show emi basic_closedgrin_rn
with charachange


emi "確かにそうかもね"

show emi sad_grin_rn
with charachange


emi "どこに行けばいいと思う？"



"俺は答えられない。この辺のことはまだ詳しく知らないし。"




"学校そのものには徐々になじんできてはいると思うけど、その周囲の街はまだまだわからないことばかりだ。"


"知っているのはあの画材屋だけ、それもさっき前を通り過ぎたからというだけだ。"

show emi basic_closedgrin_rn
with charachange


"幸い、笑美はすぐに勝ち誇った様子で指を鳴らす。"

show emi basic_happy_rn
with charachange


emi "そうだ！　この近くに喫茶店があるよ！"



emi "お茶飲んで体も乾かせるよ。ばっちり！"


"悪くない話だな。"


hi "いいじゃん！　場所はわかるか？"

show emi basic_grin_rn
with charachange



"わりと自信ありそうに笑美はうなずく。"


show emi basic_closedgrin_rn
with charachange


emi "もちろん！"

show emi basic_hes_rn
with charachange


emi "たぶん"

show emi excited_laugh_rn
with charachange


emi "でもどっちにしても、冒険にはなるよね？"


hi "冒険だって？　まあ、ちょっとくらいは冒険があってもいいかもな"


"この雨をしのげれば、俺は文句はない。"

show emi basic_grin_rn at twoleft
show rin basic_absent_rn at tworight
with dissolvecharamove


"少なくとも、ピクニックのバスケットは少しは軽くなっている。"


hi "案内頼むぜ！"

show bg suburb_roadcenter_rn
hide rin
hide emi
with locationchange



"自信に似た何かを漂わせて道を抜けていく笑美に、琳と俺は付いていく。"



show emi basic_confused_rn at center behind rain
with charaenter


emi "あとはここを左に……"

show emi excited_joy_rn
with charachange


emi "あった！　上海！"


"喫茶店を指さして、笑美は得意そうににっと笑う。"

show bg suburb_shanghaiext_rn
hide emi
with locationchange



label jp_E11x:


"そういえばここには前にも来たことがある。中はけっこう混んでいる。急に降り出した雨のせいに違いない。"

play sound sfx_storebell
stop ambient fadeout 0.5
play music music_jazz fadein 2.0

scene bg suburb_shanghaiint
with locationchange

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

with Pause(1.0)

show yuukoshang neutral_down at center
with charaenter



yu "いらっしゃいませ！　何名様――"



show yuukoshang happy_down
with charachange


yu "あら、笑美ちゃん"



"優子さんは笑美のことを知ってるみたいだ。"

show yuukoshang happy_down at tworight
show bg suburb_shanghaiint at bgright
with charamove

show emi basic_closedhappy at twoleft
with charaenter


"覚えていてもらえたことに喜んで、笑美は輝くようににっと笑う。"

show emi basic_grin
with charachange


emi "こんちは、優子さん！　席空いてる？"

show yuukoshang neutral_down
with charachange



label jp_E11y:


"中はけっこう混んでいる。急に降り出した雨のせいに違いない。"

play sound sfx_storebell
stop ambient fadeout 0.5
play music music_jazz fadein 2.0

scene bg suburb_shanghaiint
with locationchange

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

with Pause(1.0)

show yuukoshang neutral_down at center
with charaenter



yu "いらっしゃいませ！　何名様――"




"ウェイトレスが他ならぬ優子さんだったので、びっくりする。"



"制服姿の優子さんは、どこからどうみてもウェイトレスだ。これが学校の司書の人と同一人物だとはとても信じられない。"


"仕事を掛け持ちしているのか？　多分そうなんだろう。"

show yuukoshang happy_down
with charachange


yu "あら、笑美ちゃん"


"優子さんは笑美のことを知っているようだ。"

show yuukoshang happy_down at tworight
show bg suburb_shanghaiint at bgright
with charamove

show emi basic_closedhappy at twoleft
with charaenter


"覚えていてもらえたことに喜んで、笑美は輝くようににっと笑う。"

show emi basic_grin
with charachange


emi "こんちは、優子さん！"


hi "こんにちは、優子さん。ここでも働いてるなんて知りませんでしたよ"

show yuukoshang worried_down
with charachange


yu "あの、どこかでお会いしましたか？"

show yuukoshang worried_up
with charachange


yu "すごく見覚えがあるんですけど、でもここでお会いしたことは一度もないと思うんです"


hi "えっと、もう一つの仕事の方で会ってますよね。山久の図書室で。覚えてませんか？"

show yuukoshang happy_up
with charachange


"記憶が呼び覚まされて、優子さんの目が大きく広がる。"

show yuukoshang closedhappy_down
with charachange


yu "そうそう、そうよ！　また会ったね……"

show yuukoshang panic_down
with charachange


yu "大変、どうしよう！"

show yuukoshang panic_up
with charachange


yu "お客様の顔は覚えていなきゃだめじゃない！　ごめんなさい……本当に申し訳ありません！"


"不手際に気づいた優子さんは一瞬でパニックに陥り、何度も高速でおじぎを繰り返す。俺はヘッドバットを食らいそうになるのを危ういところで避ける。"



hi "いや、ちょっと、落ち着いてください！"


hi "いいですか、初めて会ったときは、俺は客じゃなかったんですから。というか上海に来たことだってなかったんです。だから気にしないでください"


"あまり出来のいい説明とは言えないけど、少しは優子さんも落ち着いたようだ。"

show yuukoshang worried_down
with charachange


yu "ほんとにそう思う？"


hi "その、ええ、もちろんです。１００パー。だよな、二人とも？"

show emi basic_closedgrin
with charachange


"目の前で展開するこのささやかなドラマに、笑美はかなり戸惑っている。"

show emi excited_proud
with charachange


emi "うん、そうだよ！"

show yuukoshang neutral_up
with charachange


yu "そ、そうなんだ……"

show emi basic_happy
with charachange


emi "で、優子さん、空いてる席はある？"

show yuukoshang neutral_down
with charachange



label jp_E11z:

$ renpy.music.set_volume(0.3, 3.0, channel="ambient")


"優子さんはうなずいて俺たちを角の席に案内すると、注文を聞く前に小さなタオルを渡してくれる。"


show yuukoshang happy_down
with charachange


yu "ご注文は？"

show emi basic_closedhappy
with charachange


emi "ケーキ！　あと紅茶も、かな"

show yuukoshang neutral_down
with charachange


yu "どのケーキにしますか？"

show emi excited_proud
with charachange


emi "おまかせで！"


show yuukoshang worried_up
with charachange


"優子さんは何かを任されるというだけで不安そうになるけど、うなずいてから琳に向き直る。"

show rin invis:
    yalign 1.0 xpos 1.0 xanchor 0.6
with None

show yuukoshang neutral_down:
    xpos 0.55 
show emi basic_grin at left
show rin basic_absent at right
show bg suburb_shanghaiint at center
with dissolvecharamove


yu "ご注文は？"


show rin negative_spaciness:
    right alpha 1.0
with charachange


rin "ストローください。足が濡れちゃったから"

show yuukoshang worried_up
with charachange


yu "えっ？"

show rin basic_awayabsent
with charachange


rin "飲むストロー。一つください"

show yuukoshang worried_down
with charachange


"優子さんは明らかに、琳の言葉をどう解釈すればいいのか分からずにいる。泣きそうな表情でしばらくペンと伝票をいじり回すと、俺の方を向く。"


show yuukoshang neutral_down
with charachange


yu "お客様は？"


hi "じゃあ、紅茶だけで"


"ケーキなんて頼んだら笑美に怒鳴られるだろうな。"

show emi sad_depressed
with charachange



emi "えー、ちょっと久夫くん！　あたしだけ食べさせないでよ、ブタになったみたいじゃない！"



hi "健康な食生活を実践してるだけだよ"


hi "そもそも、お前の言いつけだしな"

show emi basic_closedgrin
with charachange


emi "じゃあ……今日は久夫くんのオフ日！　明日から健康になればいいじゃん！"


hi "そういうことなら、やっぱりケーキもらおうかな"

show yuukoshang neurotic_up
with charachange


"優子さんは俺が注文を変えたことに少しいらだっているようだ。"


yu "どのケーキにしますか？"


"俺は笑美を見て、にやりと笑う。"


hi "おまかせで"

show yuukoshang smile_down
with charachange


"優子さんはため息をつき、うなずく。"


yu "かしこまりました。すぐにご注文をお持ちします"

show emi basic_grin at left
show yuukoshang neutral_down
show rin basic_awayabsent
with shorttimeskip



"混雑している割には、頼んだ品はその通りすぐに運ばれてくる。"


show emi excited_joy
with charachange


emi "ありがと、優子さん！"


"優子さんはうなずいてお礼を返す。"


stop music fadeout 4.0

show yuukoshang happy_down
with charachange



yu "こちら、いつもの彼じゃないわよね？"





"はあ？　違う彼？"


show emi basic_hes
with charachange


"笑美も俺の困惑に気づいているに違いない。ちょっと決まり悪そうにしているのがその証拠だ。"


emi "えっ、な、なに？　ああ、そういえばそうかも"

show emi sad_grin
with charachange


emi "友達の久夫くんだよ"




hi "前にお会いしてますよ"



show yuukoshang smile_down
with charachange



yu "はあ。世の中って狭いわね"


show yuukoshang neutral_down
with charachange


yu "じゃあ、他に欲しいものがあったら言ってね"

hide yuukoshang
with charaexit

show emi sad_grin at twoleft
show rin basic_awayabsent at tworight
with charamove


"そして、優子さんは弾丸のように飛び出して他のテーブルへと向かう。残された俺は優子さんの今の言葉を反芻する。"



"違う彼だって？　不思議じゃあないよな。笑美はかなりの人気者だし。というかそう聞いてるし。"



"陸上部の男子だろうな。"


"バカみたいだ。直接笑美に聞けばいいじゃないか。"

show rin basic_absent
with charachange

play music music_comedy fadein 0.5



hi "で、その彼って誰だよ？　秘密の恋人でもいたりするわけ？"


show emi basic_closedhappy
show rin basic_awayabsent
with charachange


"また笑美が笑うけど、それは緊張しているからじゃないかという気がしてならない。"


show emi basic_grin
with charachange


emi "陸上部の部長だよ。この店がお気に入りで、練習の後に時々来るの"

show emi basic_closedgrin
with charachange



emi "だから、話し合うことがあるときはあたしもついて行くってわけ"



"うーん、ものすごく怪しいんだけど……"

show rin basic_absent
with charachange


hi "へえ、そうなんだ"


"そこで話を終わらせることもできたけど、せめてもう一歩踏み込みたいという気持ちを抑えきれない。"


hi "じゃあ{b}やっぱり{/b}秘密の恋人じゃないか！"


hi "案の定だよ！"

show rin basic_deadpanamused
with charachange



"なんだか楽しんでいる様子で、琳が俺たちの猿芝居を見ている。何かつぶやいたみたいだけど、俺にはよく聞き取れない。"



rin "……とにかくさ"

show emi basic_confused
with charachange

$ doublespeak(emi,hi,"えっ？", "なに？")

show rin basic_surprised
with charachange


"どこか自分の意識が漂い出た先から、琳は突然戻ってくる。"



rin "へ？"


hi "今なんて言ったんだ？"

show rin basic_deadpan
with charachange


rin "へ"


hi "いや、その前"

show rin relaxed_nonchalant
with charachange


rin "さあ"


hi "まあ、いいか"


hi "わかったよ"

show emi basic_grin
show rin basic_deadpannormal
with charachange



"それ以上の追及はしないけど、琳が会話をさえぎったことで笑美が安心した様子なのが気になってしょうがない。"




"ちょっと深入りしすぎたかな……"


"笑美と俺はケーキを食べるのに夢中になり、しばらく会話が途切れる。"


"俺のはストロベリーだ。びっくりするほどおいしい。"

play sound sfx_slide2

show emi excited_happy_close
with characlose

show emi basic_closedgrin
with charadistant


"笑美もそう思ったようで、突然フォークを伸ばして俺のケーキをすくい取る。"


hi "どろぼう！"

show emi excited_proud
with charadistant


emi "海賊よ。泥棒とは違うの"



hi "ここは海の上じゃないだろ！"

show emi basic_closedgrin
with charadistant


emi "まあ違うけど。でも水なら外にたくさんあるじゃん。だからいいの。でしょ？"

show emi sad_grin
with charadistant


emi "それに、久夫くんもあたしの少し食べていいよ。クランベリーか何かだと思う"

show emi sad_depressed
with charadistant


emi "あたしもストロベリーにしとけばよかったな。ストロベリー好きなんだ"


hi "じゃあ好きなだけ俺の食べなよ、どうしてもっていうなら"


"どういう理由か、一言付け加えずにはいられない。"


hi "どうせもう、一回食われちゃってるしな"


show emi basic_closedgrin
with charadistant


"笑美は俺に舌を突き出すけど、俺のケーキのつまみ食いを止めることはしない。俺も笑美のケーキを少しいただく。"


"ラズベリーだ。なかなかうまい。"

show rin relaxed_boredom
with charachange


rin "雨、上がったよ"


"どうやら琳の言う通りだ。"


"タイミングもいい。俺は食べ終わったし、笑美も終わったみたいだ。"



hi "じゃあ会計して出ようか、また降り始める前に"


stop ambient fadeout 1.0

scene bg suburb_shanghaiext_rn
with locationchange


"優子さんの注意を引くのに数分かかったけど、会計を終えて俺たちはすぐに店を出る。"

show emi basic_grin_rn at center
with charaenter


emi "さて、公園に戻ってみる？"


"俺は開いた口がふさがらない。"


hi "冗談だろ？　またすぐに雨が降り出すぞ！"


"実際、雨粒が落ちるのを感じた気がする。"



show emi sad_grin_rn
with charachange


emi "うーん……そうかもね"

show emi basic_closedgrin_rn
with charachange



emi "しかたないね、今日のところは許してあげる。だから今度あたしをピクニックに連れて行くこと。わかった？"




"俺に言ってるのか、琳になのか、二人にか、よくわからない。"




hi "はい、はい"


show emi excited_proud_rn
with charachange


emi "ほら急いで！　トラックで何周か走ろうと思ってたの。雨が降らないうちに走る方がいいでしょ"


hi "今日はお前のオフじゃなかったのか！？"




$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 6.0

show emi sad_depressed_rn
with charachange


emi "それは……"




"笑美は急に説明するのをためらい始める。"



show emi sad_grin_rn
with charachange


emi "練習しないとだめなの"

show emi basic_grin_rn
with charachange


emi "それにどっちみち、今日食べたケーキは燃やさなきゃいけないし"



"なにか大事なことを省略しているような気がするのはなぜだろう？"




hi "本当か？　あんなの大した量じゃ……"

show emi basic_closedgrin_rn
with charachange


emi "そりゃ、{b}久夫くんが{/b}食べた分は大したことないわよ。あたしがほとんど全部食べたんだもん"


"それもそうだ。"




label jp_choiceE11:
menu:
    with menueffect
    "それでも、俺は笑美と一緒に走ると申し出るべきなんじゃないか……"
    "一緒に走ると言う":






        return m1
    "黙っておく":


        return m2



label jp_E11b:



hi "なあ、俺も一緒に走るよ"


hi "その方がいいだろ？"

show emi basic_annoyed_rn
with charachange


"笑美はきっぱりと首を振る。"



emi "だめだよ、久夫くん。休養は大事でしょ、忘れたの？"



emi "無理をするのは禁止だよ"


"笑美はアドバイスを受けるよりは与える方が得意みたいだ。"



hi "笑美がそういうなら"




"これ以上は踏み込まないほうがよさそうだ。"




label jp_E11c:





"そういえば、今の笑美はむしろ一人になりたそうに見える。"



"付いていくのは止めることにする。"



label jp_E11d:



stop music fadeout 12.0

scene bg school_dormext_full_rn
with locationskip


play ambient sfx_rain fadein 2.0
show rain normal
with Dissolve(2.0)



"女子寮に近づくころには、雨がまた降り出している。"


show emi sad_annoyed_rn at center behind rain
with charaenter


"笑美の顔が少し不機嫌そうになる。"


emi "えー、まじで……"


emi "いやな雨"


hi "気にするなよ、すぐに止むって。そしたら走りに行けるだろ、な？"

show emi basic_grin_rn
with charachange



"おもしろがるように笑美が鼻を鳴らす。"


show emi excited_proud_rn
with charachange


emi "あたしが雨の中で走ったりしないって思ってるでしょ"



hi "おい止めたほうがいいって！　風邪ひくぞ！"



show emi basic_grin_rn
with charachange



"笑美は陽気に手を振る。"




emi "んなわけないでしょ！　あたしは風邪なんてひかないの"



show emi basic_closedgrin_rn
with charachange


emi "あたしの免疫力なら風邪なんて引くわけないんだから"





"俺は笑い出さずにはいられない。"


hi "わかった、じゃあまた明日な？"

show emi basic_happy_rn
with charachange


emi "うん！"

show emi basic_grin_rn
with charachange


emi "来てくれてありがと！　あっ、バスケット持ってくれたのもね！"

show emi excited_amused_rn
with charachange


emi "明日のお昼にまた持ってくるからね。屋上でピクニックしよう！"



hi "いいね。じゃあまたな！"


hide emi
with charaexit



"笑美は俺からバスケットを受け取ると、ドアを抜けて部屋に飛び込んでいく。"




"琳は半分うなずくようなしぐさをして、同じくふらりと中へ戻る。"




"くそ、このへん濡れてるじゃないか。"



"部屋に戻って乾いた服に着替えないと。"

stop ambient fadeout 2.0

scene bg school_dormhallway
with locationskip



"やがて自室の前に着いたけど、突然現れた健二に邪魔される。本を山ほど抱えているみたいだ。"


show kenji neutral at center
with charaenter


ke "おう、ちょっと手伝ってくれよ、な？"


hi "はあ？"

play music music_kenji fadein 0.5

with vpunch



"その本がいきなり俺の腕に積まれて、健二は自分の部屋の鍵をごそごそと手探りする。"



show kenji happy
with charachange



ke "わりいな、助かったぜ"




ke "お前がいなかったらドアの鍵を開けっぱなしにしないといけなかったし、そんなことしてもトラブルを呼ぶだけだからな"



show kenji tsun
with charachange



ke "待ち伏せを仕掛けるには絶好のチャンスだ、手を汚したくないやつなら爆弾だって仕込めるかも"





ke "奴らは恐らく手を汚したくないのさ"




ke "いざ俺を刺すとなったら、爪とか割れるのをいやがるんだ"


ke "これだから女は"


"たった今解き放たれた、この言葉の洪水を認識するべきかどうかと俺の精神は考えるけど、やっぱり無視することに決める。その方が楽だし。"



hi "あー……そう"

show kenji happy
with charachange 


ke "まあいいや、どこ行ってたんだお前？"

show kenji neutral
with charachange 



ke "これを図書室から持って帰るのを手伝ってくれりゃ良かったのに！"


ke "部屋をノックしたけどいなかったし"


hi "ああ、悪い"


"とは特に思ってない。俺は荷物運びのラバかよ。"


hi "笑美と琳と出かけてた"

show kenji rage
with charachange



"健二はショックで後ろによろめく。"




"俺が健二の犬を射殺でもしたみたいな感じだ。もし犬を飼ってたとしたら、だけど。"



ke "またあの腕なし足なしレディースどもか？"

show kenji tsun
with charachange


ke "今度は何をやらかした？"



hi "いや、いろいろあって上海に――"



"突然、絶望的な叫び声が響いて俺はそれ以上続けることができない。"

show kenji rage
with vpunch


ke "上海？"



ke "なんで上海なんだ？"



ke "だめだだめだだめだだめだ、お前、よりによって上海なんかに行くやつがあるか！"


ke "あれはこの町で一番危険な場所なんだぞ！"


ke "奴らの最強のエージェントたちが集まる真の牙城だ！"



ke "知ってるんだよ！　俺は会ったんだ！"




ke "奴らは手を尽くして俺たちをなだめすかして偽りの安心感に浸らせておいて、そしたらバン！　だ"


play sound sfx_impact2
with vpunch


"健二は自室のドアを叩いて強調する。"



ke "財布をやられた。バスの定期？　やられたよ。学生証？　{b}やられちまったよ{/b}、ちくしょう！"


show kenji tsun
with charachange


ke "二度とあんなところに行かないと約束しろ！"


"健二は上海という概念そのものに激しく反発しているようなので、部屋に戻りたい俺は少しばかり嘘をついてもいいかという気になる。"



hi "いいよ、あそこにはもう行かない"




"というか少なくとも、また行ったってことは絶対お前には言わない。"




"その返事に、健二は落ち着きを取り戻す。"

show kenji neutral
with charachange


ke "よし、よし"

show kenji happy
with charachange



ke "うるさいこと言って悪かったな。でも俺は、あの場所の危険さをよく知ってるんだ。あんなライオンの巣にお前が迷い込むのを放っておけなくてさ"




ke "一度は生きて戻れたかもしれないが、二度はないぞ"



hi "ああ。じゃあ俺着替えとか、その、宿題とかしないといけないから……またな"

show kenji tsun
with charachange


ke "はあ？"

show kenji neutral
with charachange


ke "ああ、そうか。じゃあな"


"突然、自分がまだ健二の本を抱えていることを思い出す。"



hi "これ持っていけよ"



"そのうち一冊の題名が目に入る。暗号学がどうとか。"


"なんて変なやつだ。"

stop music fadeout 6.0

show kenji neutral:
    center
    easeout 0.5 xpos 0.3 alpha 0.0
with None



"健二は大切な荷物を俺から奪い取り、自分の部屋へと消える。"


$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0

scene bg school_dormhisao
with locationchange


"俺は自分の部屋のドアを開いて中に入る。ようやく濡れた服を脱げるのがありがたい。"




"雨が強くなってくる。笑美がこんな天気に外で走ったりしてなければいいけど、と願っている自分に気づく。一人で走ることにひどくこだわっているみたいだった。まだ足が不調なのかとつい勘ぐってしまう。"





"今日の笑美が少しでも足を引きずっていたかどうか思い出そうとするけど、思い出せない。俺もきっと楽しむことに夢中になりすぎていたんだろう、雨に降られたとはいえ。"




"今日のできごとを思い返していると、すぐに思考が俺のランニングパートナーに戻ってきてしまう。"



"雨に予定を邪魔されるのを徹底的に拒否する笑美は、信じられないくらいかわいかった。"


"でもそこには他にも何かがあった。"


"やってくる一日を楽しむことについて、なんというか、取り乱さない、落ち着いた態度。"




"あの性格はすごく好きだ。"



"俺も少し見習わないとな。"


stop ambient fadeout 2.0
scene black
with dissolve

$ suppress_window_after_timeskip = True

label jp_E12a:

window hide None

scene black
with dissolve

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show



"アラームの音が、海賊やその他よく思い出せない夢から俺を覚ます。"


scene bg school_track
with locationskip

play music music_pearly

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")



"目が少しぼやけていて、着替えて競技場に来るまで普段より時間がかかった気がする。"





"時計をちらっと見ると、自分が正しかったことがわかる。確かに少し遅刻している。"






"問題は……"



"笑美がいないことだ。"



"おかしいな。もういるはずなのに。"





"絶対いるはずだろう。"





"というか、俺は{b}遅刻{/b}したんだし。"




"今朝起きるのに手間取ったのは俺だけじゃなかったということだろう。"




"まったく止まなかった昨日の雨のことが脳裏をよぎる。それでも笑美は走ったんだろうか？"




label jp_E12b:






"あいつならやりそうだ。笑美にはすごいところがいろいろあるけど、慎重ではない。たぶん笑美は雨が止まないと思ったんだろう、だから一人で走ることにあそこまでこだわったんだ。"




"けど、俺はたとえ雨の中でも、喜んで笑美と一緒に走っただろうと思う。"






"ちくしょう、それならそれで雨が本当にひどくなったときは建物に入るように説得できたのに。もちろん、それが分かっていたから笑美も付いてきてほしくなかったんだろうけど。"







label jp_E12c:




"笑美と一緒に走ると言うべきだった。"




"そしたら俺は笑美を説得できていたか、でなければ少なくとも笑美が無事だったことくらいは知っていられたのに。もし笑美が雷に打たれたりしていたらどうしよう？"




"俺は決して自分を許せないだろう。"


"……"






"いや、今のはちょっと馬鹿らしいな。"






"笑美は機転がきく。雷雨の中、ずっと屋外に出ているとは思えない。"





"少なくとも、そのへんの判断は信じる。"




label jp_E12d:





"それにしても、笑美がどこにいるか知りたくてしょうがない。"




"……まあ、しかたない。ストレッチをして走ったほうがいいだろう。笑美が笑って現れて言い訳をしてくれることを願おう。"




scene bg school_track_running
with shorttimeskip

show bg school_track_on
with Dissolve(3.0)




"クールダウンの１周で、俺は笑美が現れないことを認めざるを得なくなった。"






"そのうえ、俺には笑美がどこにいるのかわからない。不安が俺を蝕むのと同時に、どうしてこんなに笑美のことが心配になったのか不思議になる。"






"走っていればそのことはしばらく忘れていられたけど、今は走り終えて心配に逆戻りだ。"



$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear

nvl show dissolve




n "\n\n笑美がここにいないのは変な感じだった。"





n "ひどく落ち着かない。"





n "突然、俺は気づく。俺が走っているのは健康維持のためと同時に、笑美と一緒にいるためなんだと――たぶん笑美の方が大事なんだろうな、考えてみれば。"






n "そんなことはまるっきり明らかなのに、どういうわけか全く気づかなかった。"






n "笑美はほんとうに、一緒にいて楽しい人だ。"






n "別にそれほど重大なことが明らかになったわけではない。"




n "それでも、少しだけ驚いている自分もいる。"




n "いつからこんなことになったんだろう？"




n "まあ、今はそれを考えている暇はない――この新しい変化をじっくり考えてはみたいけど、それより笑美に何が起こったのか調べたいという欲求のほうが大きい。"





n "ナースに会いに行ったら聞いてみよう。"



$ renpy.music.set_volume(1.0, 2.0, channel="music")
stop music fadeout 2.0

nvl clear

nvl hide dissolve

scene bg school_nurseoffice
show nurse neutral at center
with shorttimeskip



nk "ふむ、調子はいいみたいだね、久夫くん"




hi "それはよかったです"




"いつも通り、俺はシャツを戻して出ていこうと立ち上がる。"



"ただし出ていく代わりに、俺は質問をする。"




hi "あの、笑美はどこですか？　今朝は来なかったんです"




hi "大丈夫なんですか？"


show nurse concern
with charachange



"声の不安をちゃんと押し隠そうとしてみても、俺が哀れにも失敗していたことはナースの表情でわかる。"





nk "笑美ちゃんは君に言ってなかったんだね？"



nk "笑美ちゃんなら病気で寝てるよ"



hi "えっ？　病気？"


show nurse neutral
with charachange


"ナースは肩をすくめる。"



nk "ああ、けさ早く熱が出て医務室に来たんだ"




nk "正直に言うと、ここにたどり着けたのは驚きだね"

show nurse concern
with charachange



nk "来たときはひどい熱だったんだよ"





nk "笑美ちゃんは君に知らせるつもりでいたんだと思うけど、僕から伝えてくれって頼まれ――ああしまった！"



stop music fadeout 2.0

show nurse neutral
with charachange



"ナースは俺に恥ずかしそうな笑顔を見せる。少なくとも、ある程度は本気みたいだ。"





nk "僕が言ったんだった、笑美ちゃんが忘れたときは僕が競技場に寄って君に知らせるって。ごめんよ"



play music music_nurse fadein 1.0

show nurse fabulous
with charachange


nk "でも僕が忘れたってことを笑美ちゃんに伝える必要はないよね？"



"俺はナースの笑みに意地悪く笑顔を返す。"



hi "ええ、もちろんですよ"


hi "これはいい強請りのネタですからね"



hi "あなたに頼み事をしたいときのためにとっておきます"


show nurse grin
with charachange


"ナースは笑う。"



nk "まあ僕の落ち度だし、しかたないね"





nk "でも言っておくけど、僕は君が気づいてもいない強請りのネタを大量に持っているんだよ"


show nurse fabulous
with charachange



nk "だから調子には乗るなよ、いいね？"




"俺の表情を見て、ナースはまた笑う。"


show nurse grin
with charachange


nk "ただの冗談だよ、久夫くん"

show nurse concern
with charachange



nk "でも冗談抜きに――僕が忘れたことは笑美ちゃんには言うなよ？"




hi "秘密は守りますよ"


show nurse neutral
with charachange




nk "ああよかった。さあ、もう行っていいよ"




hi "すみません、もう一つ質問が"

show nurse fabulous
with charachange


nk "どうぞ"



hi "笑美はよくなるんですか？"


show nurse grin
with charachange 



nk "ああもちろん、なるとも"


show nurse neutral
with charachange 



nk "熱は高かったけど、医務室に来たときにはもう下がり始めていたよ"




nk "もちろんお昼にはもう一度診るつもりだけど、たとえ僕が何を言っても、笑美ちゃんは夕方にはもう起き上がって動き回っているだろうね"




hi "うーん、放課後に見舞いに行ったほうがいいかも"



"少しの間をおいて、俺は自分が声に出して喋っていたことに気がつく。"

show nurse fabulous
with charachange




"ナースは眉を上げて、一瞬、ちらっと俺に探るような眼差しを向ける。"





nk "ふーむ……"


show nurse neutral
with charachange 


nk "そうだね、それも悪くないかもしれないな"




nk "もし笑美ちゃんの具合がもっと悪くなっていたら、僕に伝えてもらえるし"



show nurse concern
with charachange




nk "でも怪しいことはするなよ、いいね？　君が使ってる薬は知ってるんだからね"






"今のは俺の命に対する脅しのような気がするけど、確信は持てない。"





stop music fadeout 7.0

scene bg school_nursehall
with locationchange




"ともかく、よこしまな意図はないんだとナースにはっきり伝えて、俺は医務室を出る。"






"ナースが俺のことを、笑美の彼氏候補のように見ているのはおもしろい。"







"もっとおもしろいのは、おかげで俺はすごく喜んでいるってことだ。"




"シャワーを浴びる必要があるな。"


scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell



"昼休みのベルが鳴り、俺は屋上に上がろうとはあまり思っていないことに気づく。"





"どうせ、琳は笑美のいる場所を知っているはずで、そんなときでも琳はわざわざ屋上に上がっているのだろうか。"








"もっと言えば、仮に琳がいたとしても、二人で気のきいた会話ができるとは考えにくい。たぶん琳は一人きりでいたいだろう。俺の不注意で自分の考え事やらなにやらを邪魔されないように。"







"あいにく、食堂に向かう気もまったくない。"



"代わりに図書室にでも行こうか。"




"昨日寝る前に残りの一冊を読み終わったので、どっちにしろ新しい本は必要だ。同じ作者の本がもっと見つかるかもしれない。"


scene bg school_library
with locationskip

play music music_happiness fadein 2.0



"図書室は大好きだ。"



"埃と紙とインクみたいな匂いがする。"



"あらゆる物語や事実や考え方が一カ所にぎっしり詰め込まれて、活気を秘めた雰囲気になっている。"







"ずっと自分が持ちこんだ本ばかり読んでいたおかげで、図書室の本の並びがまだよく分からないので、手伝いを頼める司書の人を探す。"






"……"



"うーん。優子さんはどうもこのへんにはいな――{w=0.5}{nw}"


show yuuko smile_down:
    center
    xpos 0.4
    easein 0.5 center
with charaenter



yu "……信じられない"




"優子さんが突然、ずいぶん取り乱した様子で、たくさんある通路の１つから現れる。"



hi "あの、すみません"

show yuuko neutral_down
with charachange


yu "あら、何かご用？"


hi "実は、本を探していたんですが……"

show yuuko panic_up
with charachange



yu "私もよ！"


show yuuko smile_down
with charachange



yu "『上級暗号学』。仕入れたばかりなのに、もうなくなってるの"



show yuuko worried_up
with charachange




yu "私、本当に、ほんとうにあの本が読みたかったのに！"




hi "暗号学？"

show yuuko neurotic_up
with charachange



yu "ええ。わたしの……えーっと、そのお……"






yu "わたしの知り合いだった人。知り合い。うん"







yu "どう説明したらいいのかしら……"


hi "要点だけ言ってください"

show yuuko smile_down
with charachange





yu "彼のせいで暗号学に興味を持ったのに本がなくなっちゃって、盗まれたんだと思うの！"








hi "それはちょっとひどいですね"


show yuuko worried_up
with charachange





yu "ほんとよ、そのおかげで図書室ぜんぶ探さなくちゃいけないんだから！"






yu "たぶんないだろうとは思うんだけど！"



hi "優子さん……忙しそうですね"

show yuuko neurotic_up
with charachange


yu "ちょっとね"

show yuuko neurotic_up:
    center
    easeout 0.5 alpha 0.0 xpos 0.6
with None





"優子さんは他の通路に走り去って、俺は観念して自分で自分の本を探す。"





"うーん、どれにしようか。"

stop music fadeout 2.0

hide yuuko
with shorttimeskip


"いや、ちょっとまて。いつの間に俺は迷子になったんだ？"



"これは印刷された本ですらないじゃないか！　全部点字になっている。"





"こんな学校なら納得できるけど、正直なところ、俺にはちょっとうっとうしい。"






li "すみません、どなたかいらっしゃるんですか？"






"自習用に設けられたブースの１つから軽やかな声が流れてくる。"




show lilly basic_displeased at center
with charaenter



"近づくと、俺が通路でどたばたやっていた間もリリーがそこで本を読んでいたことに気づく。"





hi "ああもう、謝らないと。あんなに音を立てるつもりじゃなかったんだ"



show lilly basic_ara
with charachange



li "あら、久夫さんですか？"


show lilly basic_smile
with charachange



li "ずいぶんごぶさたでしたね"



show lilly basic_pout
with charachange



li "もう私のことなんて全部忘れてしまっているんだろうと思い始めていたんです"



hi "あー、ごめん"

play music music_lilly fadein 4.0

show lilly basic_giggle
with charachange



"リリーは洗練された振る舞いで笑い、首を振る。"



show lilly basic_smile
with charachange


li "からかっただけですよ、久夫さん"




li "聞いたところでは、忙しかったみたいですし"


show lilly basic_cheerful
with charachange



li "茨崎笑美さんとの早朝ランニング{b}と{/b}屋上での昼食、ですよね。私が間違っていなければですけど"



hi "へ、ああ"




hi "話が広まるのは早いもんだな"



show lilly basic_weaksmile
with charachange




li "それに、おかげでかわいそうな華ちゃんを屋上でなだめることができなくなりました"



show lilly basic_displeased
with charachange




li "あなたがた３人がいつも屋上にいて、あの場所を独り占めしているんですから"






"リリーはやんわりとたしなめるけど、今度もからかっているのは明らかだ。"





"でも、どうも謝らなきゃいけないような気分になる。"





hi "ごめん、もし本当にまずいのなら俺たちはどこか別の場所で――"




show lilly basic_ara
with charachange



li "いえいえ、それは気にしていませんよ"


show lilly basic_smile
with charachange




li "華ちゃんも私も、お昼にはいろいろとすることがありますし"





li "見てのとおり、例えば図書室で読書をしたり"



hi "あれ、華子もいるんだ？　見なかったけど"


show lilly basic_smileclosed
with charachange



"リリーは少し謎めいた微笑みを浮かべる。"



li "あら、どこかそのあたりにいますよ"

show lilly basic_smile
with charachange



li "でも驚きましたよ、久夫さん。あなたがここにいるんですもの、屋上ではなくて"




li "どうして図書室に？"





hi "その、笑美が病気でさ、だから屋上でのランチもなしってわけで……"


show lilly basic_giggle
with charachange



"リリーは俺の言葉に眉を上げて、また含み笑いをする。"




li "まあ。かわいそうな手塚さんは、のけ者にされたと思っているでしょうね"




hi "そんなんじゃないよ！"


show lilly basic_weaksmile
with charachange




li "ええ、私も違うと思います。笑美ちゃんはどのグループにいても活気の源になるような子ですからね"



show lilly basic_sad
with charachange





li "笑美ちゃんが病気というのはお気の毒です。大丈夫なんですか？"






"どうもただ礼儀として聞いているような感じが少しするけど、とにかく俺は返事をする。"





hi "ナースはそう思ってるよ。俺、放課後に笑美がどうしているか見に寄っていくつもり"



show lilly basic_smileclosed
with charachange


"また眉を上げる。"




li "まあ。とても紳士的なんですね、久夫さん"





hi "たいしたことじゃないよ、本当に。ただ友達の様子を見るだけだ"



show lilly basic_planned
with charachange



li "あら、ただの友達なんですか？　がっかりです"




"顔が赤くなる。リリーには見えなくてよかった。"

show lilly basic_giggle
with charachange



"でもどういうわけか、俺がリリーの言葉でうろたえていることがわかるようで、リリーは笑う。"





li "ごめんなさい、久夫さん。またからかってしまいました"



show lilly basic_smile
with charachange



li "おだいじにと笑美ちゃんに伝えてもらえませんか？"





"腕時計をちらっと見ると、本を探す時間はほとんどないことがわかる。"



hi "もちろん"


hi "その、昼休みが終わる前に本を見つけたいんだ。だからもう行かないと"


hi "また見かけたら声をかけるよ"




"今のは、リリーに言うのにはベストな言葉ではなかっただろうな。"







"けどリリーは俺の失言をうまく受け流す。"


show lilly basic_weaksmile
with charachange

stop music fadeout 3.0



li "また会いましょうね、久夫さん"



scene bg school_hallway2
with shorttimeskip





"探していた本はぜんぜん見つからないけど、代わりに見つけたものを持って図書室を出る。"






"腹が軽く鳴って、昼食に何か食べたほうがいいと俺に教えてくれる。"



"ああ、そうだ。"



"あとで笑美のところへ行く前に、ちょっと何か食べよう。"



label jp_E13:

scene bg school_hallway2
with None

scene bg school_scienceroom
with shorttimeskip

play music music_normal fadein 3.0





"時間がまるで俺にひどい嫌がらせをするというはっきりとした目的を持って遅く進むことにしたみたいだ。"







"授業がずるずる延々と続くように感じる。"





"心配事で頭がいっぱいになっていることも関係があるんだろうな、とは思う。"



play sound sfx_normalbell




"幸いなことにベルが鳴って、俺は教室から飛び出す。眉をつり上げる人が何人かいたに違いない。"




scene bg school_hallway3
with locationchange




"今日ほぼ一日、やきもきする気持ちをできるだけ表に出さないようにして過ごした。"





"笑美ならすっかり大丈夫だとナースは言っていたけど、自分の目で確かめたい。"



stop music fadeout 14.0

scene bg school_girlsdormhall
with locationskip


"女子寮に入って笑美の部屋まで行くのには時間がかからない。"



"部屋の前に立って、俺は突然ためらう。もし笑美が寝ていたら？"





"起こすのはいやだ。まだ具合が悪いなら、なおさらだ。"







"だけど、もし一日中寝ているとしたら笑美の睡眠サイクルを狂わせてしまうかもしれない。"






"でも病気の時は休息が大切、じゃないのか？"



"どうするか決めかねて、俺は馬鹿みたいにドアの前に突っ立っていることになった。"



"するとドア越しに笑美の声が聞こえてくる。"




emi "心配してくれてありがとう、でも本当に大丈夫"




"俺に話しているんだろうか？"



emi "それじゃまた明日練習で！"


"違うみたいだ。"




"それでも、笑美が寝てないのは確かだ。だからノックは気兼ねなくできる。"





"ならこの内臓が掴まれてるみたいな感じはなぜだ？　前に来たときは緊張してなかったのに、なんで今日は？"





"笑美の健康状態に関心を持つという、自分の新たな気持ちをちゃんと検討する時間はまだ取れていないけど、それにしてもだ。"





"もちろんこういう経験はそんなにないけど、ただの友情なんて思いを越えそうなのは間違いない。"





"でも次のステップを踏めるだろうか？　俺は今あるものを失うリスクを負うことができるだろうか？"




"つまり笑美とは友達でも十分、じゃないか？"





"どっちにしろ、ドアを開けて笑美がどうしているか見るくらいはするべきじゃないか？　そのために来たんだ……よな？"



stop music fadeout 1.5



"でももしまだ服を着ていなかったら？"


play ambient sfx_heartslow

with Fade (0.05, 0.0, 0.3, color="#ffc0cb")



"頭にちらつくイメージが、文字どおり心臓をドキッとさせる。"


stop ambient fadeout 3.0




"もうこんなことを考えるのはやめたほうがいい。心臓発作を避けるためにも。"





"俺は突然、まだ自分が馬鹿みたいに廊下の真ん中で突っ立っていることに気がつく。"



play sound sfx_doorknock2



"笑美はまだ会話の途中みたいだけど、気にせずノックする。邪魔をしても気にしないでくれるだろう。"




emi "心配しすぎ――どうぞ！　鍵あいてるよ"







"そういうことだ。俺はドアを開けて中に入り、その時点で俺の思考には急ブレーキがかかってしまう。"





play music music_serene fadein 4.0

scene ev emi_sleepy_face:
    subpixel True
    center
    zoom 1.05
    ease 15.0 zoom 1.0
with whiteout



"笑美がベッドで起き上がっていて、髪は一日中寝ていたからかボサボサだった。あのいつものビーズの髪留めをしていないところを見るのは初めてだと思う。"





"体操服とブルマは、俺が入る前に急いで身につけたのだろう。しまうときにきちんと畳まれていなかったのか、しわくちゃになっている。"



scene ev emi_sleepy_legs at Fullpan(8.0)
with flash



"脚がむき出しでシーツの上に横たわっている。"





"義足をつけていない笑美を見たことはなかった。でも笑美はここにいる。膝のすぐ下で切れて終わっている細い脚で。"







"でもその光景と同じくらい奇妙なことだけど、自分が笑美の腰から上の部分にもっと気を引かれていることに気づく。"



scene ev emi_sleepy:
    subpixel True
    center
    zoom 1.05
    ease 15.0 zoom 1.0
with flash



"どうやら笑美は誰かとの電話の会話を終えたようで、今は片方の寝ぼけ眼をこすりながらもう片方の目で俺の反応をじっと見ている。"







"彼女の表情は、恥じらいから遠く離れていて、やたらと大きいあくびを見せた。こんな小さい口にはぴったりかもしれない。"





"俺を視界に入れるときに口の端で一瞬見せた笑いは、俺を誘っているように見えた。"






"俺はなにもできずに、恐怖と混乱と、少なからぬ欲望の中に取り残される。"







"笑美はあわてて髪の毛を目から払い、元の位置に戻してから俺に話しかける。"



scene bg school_dormemi
show emi sad_grin_gym at center
with locationchange




emi "ちょっと油断してたみたいね、久夫くん"







"笑美の満面の笑いがうつって、自分も笑いながら頭をかいてしまっていることに気づく。"





hi "ごめん、俺はただ……"



"だらしない様子がこんなに魅力的な人なんて見たことがなかったんだ。"




"義足のない君を見たこともなかったんだ。"





"君がすごく……"





hi "その、ごめん"

show emi basic_closedgrin_gym
with charachange




"笑美はまたくすくす笑って、ちょっと座りなおす。"






"シャツの動きが気になって、我を失いそうだ。"


show emi basic_grin_gym
with charachange




emi "久夫くんならどんな反応するかなって思ってたの"




show emi basic_closedhappy_gym
with charachange




emi "あのね、ナースくんから電話があって、久夫くんが来るって言ってたから"




show emi basic_grin_gym
with charachange




emi "それに、久夫くんが見たことないの知ってるし、あたしの……えっと、ほら"




show emi sad_grin_gym
with charachange



emi "足がないとき"




"俺は軽く驚いたように返す。"





hi "あ、付けてなかったんだ？　わからなかったよ"





"ほぼ本音だ。ほとんど気づかなかった。"






"人当たりをよくしようとか、そんなのじゃないんだ。なんだか、笑美はそういうことをされたら怒るような気がする。"



stop music fadeout 0.5
play sound sfx_pillow
show emi basic_annoyed_gym
with vpunch



"かわりに、笑美は舌を出して枕を俺の頭に投げてくる。"




emi "バーカ"



"俺はその枕をうまく受け止めて、慎重に狙ってから投げる。"


play music music_running

show emi basic_annoyed_gym:
    center
    parallel:
        ease 0.5 xpos 0.7
    parallel:

        "emi basic_closedhappy_gym" with Dissolve(0.5, alpha=True)



"笑美が笑いながら転がって枕を避ける。ずれたシャツに気を取られて、次の枕が俺の眉間を直撃する。"



play sound sfx_pillow


hi "おぅふ！" with hpunch




"もちろん、反撃する。"





"そして二回も反撃すれば、まあ、遅かれ早かれ戦争になるに決まってる。"





"それに、笑美は狙うのが俺よりずっとうまいみたいで、だから……"



"捨て身の攻撃を強いられるようになるのは時間の問題だった。"


show bg school_dormemi:
    center
    ease 0.5 bgleft

show emi basic_closedhappy_gym:
    ease 0.5 center

with None

show emi basic_closedhappy_gym_close:
    ease 0.5 center

with characlose



hi "つかまえた！"


show emi basic_hes_gym_close
with charachange



emi "きゃあ！"


window hide None

play sound sfx_pillow

show comic vfx1
show emi basic_closedsweat_gym_close
with vpunch

with Pause(0.5)

play sound sfx_pillow

show comic vfx2
with hpunch

with Pause(0.5)

play sound sfx_pillow

show comic vfx3
with vpunch

with Pause(0.5)

show comic vfx3:
    truecenter
    easeout 0.5 yanchor 0.3 alpha 0.0
with Pause(0.5)









stop music fadeout 3.0

scene black
with dissolve

window show



"そして一度捨て身の攻撃が成功したら、まあ、枕を取り上げるのに取っ組み合いすることになるのは当然で。"





"そんなふうにやりあってれば、しまいにはこんな体勢になっちゃうのも当然だ。"


window hide

play music music_twinkle fadein 2.0

scene ev emi_bed_full:
    xalign 0.5 yalign 1.0 subpixel True
    easein 15.0 yalign 0.0

with Dissolve(1.0)

with Pause(3.0)

window show



"そうして俺は、自分が笑美に乗りかかって見下ろしているのに気づく。"





"笑美は笑っていて、目はおかしそうにきらきらしている。今のじゃれあいでちょっと汗ばんでいるかも。"




"笑美の胸が上下に動き、空気を吸っている。"





"いまのところはこの光景や匂いにとらわれていない俺の頭のほんの一部分が、笑美はまだ調子悪いな、と分析する。笑美のスタミナはこんなものじゃないはずだ。"



"俺たちはしばらくそのままでいた。"




"どれくらい長い間かわからない。すべてがぼやけているみたいだ。笑美以外のすべてが、だけど。"





"笑美と目が合って、その奥にはかすかな……なんだろう、恐れ？　愛しさ？"






"希望？"



hi "笑美……？"


stop music fadeout 0.5

show ev emi_bed_unsure at center
with vpunch



"咳が突然笑美の体を震わせる。俺はいろいろ謝ろうとして、ほとんど転げ落ちるような勢いで笑美から離れる。"


play music music_emi fadein 3.0



hi "ごめん、こんなことはしちゃ……"


show ev emi_bed_happy
with charachange



emi "平気、へいき"




"笑美は安心させるように俺の肩をたたく。"



show ev emi_bed_normal
with charachange



emi "で……なんでここに来たの？"





"笑美はまだ荒い息をしていて、そのせいで声が少し震えている。"





hi "ええと、枕でいきなりやられる前は、笑美がどうしてるか見に来たんだけど"





window hide None

play sound sfx_pillow

show comic vfx4
show ev emi_bed_frown
with vpunch

with Pause(0.5)

show comic vfx4:
    truecenter
    easeout 0.5 yanchor 0.3 alpha 0.0
with Pause(0.5)

window show




"俺はもう一度突き飛ばされて、笑美のベッドから落ちかける。"



show ev emi_bed_normal
hide comic
with charachange




"笑美の目がまた輝き始める。それがこんなに魅力的なことに、どうして今まで気づかなかったんだろう。"




show ev emi_bed_smile
with charachange



emi "心配でたまらなかったんでしょ？"





"馬鹿にしているような、えらそうな調子だ。からかってるな。"




"笑美は芝居がかったしぐさで額に腕を置いて、その下からはっきりと笑顔を見せる。"



show ev emi_bed_unsure
with charachange




emi "あたしが病気で死にそうになって寝込んでいるなんて思うと耐えられなかった？"






"俺たち二人でさっきの格闘戦から回復する間、笑美は俺をからかうことにしたようだ。"





hi "まあ、心配でたまらなかったとは言わないけど、今朝、笑美が弱虫みたいに出てこなかった後ではね……"



show ev emi_bed_frown
with charachange



"笑美は拗ねる。不機嫌そうに腕を組んで下唇を突き出している。"




emi "あたしのせいじゃないもん"




emi "ナースくんがだめだって"




hi "そうだろうさ。笑美を信じるよ"




"笑美はまた舌を出す。"





emi "久夫くん、最っ低"






hi "で、今日はどうだった？　さぼりを満喫したか？"


show ev emi_bed_normal
with charachange



emi "そうでもないよ、電話でけっこう早く起こされちゃったし"



hi "電話？"



emi "そう、陸上部の部長が大丈夫かって電話してきたの"



emi "あと練習休んでいいって"



"よかった、少なくとも一日中ひとりじゃなかったんだ。誰かが確認をしたんだな。"




"でも、そうすべきなのは俺だったという考えが止まらない。"




hi "ああ、それはよかった"





hi "笑美のこと本当に気にしてるんだな？"




show ev emi_bed_smile
with charachange



"笑美は肩をすくめる。"





emi "それが仕事だもん"






emi "メンバーが学校にいないときにどこにいるかを知っておくのも、部長の役目の一つだから"






emi "でも、電話くれたのって親切だよね？"




hi "うん。そうだな"





"笑美はあくびをしながら少し楽な姿勢になった。"



show ev emi_bed_normal
with charachange



emi "で、久夫くん今日はどうだった？"




hi "まあ平凡なもんだったね"




hi "ひとりで行って自分で走って、笑美がどうしてるかナースと話して……"



stop music fadeout 2.0

scene bg school_dormemi_ni
with shorttimeskip



"特に面白くもない今日のできごとを、だらだらとあれこれ話す。"





"ふと気づくと笑美の腕が俺の腰にあって、話が止まってしまう。"




"話している間に寝てしまったみたいなので、毛布を引っぱって二人いっしょにかける。"


play music music_comfort fadein 9.0

scene ev emi_sleep_unsure
with locationchange




"笑美が寝返りを打つと、片足が俺の足の上に投げ出され、ほぼ身動きがとれなくなってしまう。"




hi "おい"




"起こすのも気の毒だけど、しなきゃいけないことがあるしな。"




play sound sfx_rustling




"俺はそっと笑美を揺さぶるけど、もっと強く抱きしめられて、ちょっとため息をつかれただけだ。"







"俺の抵抗はずいぶんあっさり砕け散った。"




"笑美がゆっくりと息をしているのを感じるのは、落ち着くと同時に、信じられないほど刺激的だ。"





"自分の呼吸も静まりたいんだか早まりたいんだかわからない。"





"結局安心感が勝ち、俺は笑美に腕を回していた。"


scene ev emi_sleep_normal
with dissolve



hi "好きかも"





"漏れた言葉が、気づかれないまま宙に漂う。"





"少なくとも今のは気づかれないまま消えてほしい。"



scene ev emi_sleep_weep
with dissolve



"笑美は夢の中で弱々しく涙ぐんで、またぎゅっと抱きしめてくる。"



"笑美に会ってから初めて、笑美の顔に涙が流れるのを見た。"




"心臓が壊れてしまいそうな気がする。"





"俺は思わず抱きしめ返して、落ちつかせるように笑美の髪をなでる。"




"こんな状況では意味のない慰めの言葉が、頭に浮かぶ。"




"起こしたほうがいいのかも。悪い夢を見ている人って起こすものなんだっけ？"




"どうしてもそれが思い出せない。"





"笑美が突然叫んで目を覚ましたのに驚いて、それどころではなくなる。"



scene ev emi_sleep_cry
with dissolve



emi "パパ！"







"これは……俺が聞いたことを笑美が知らないままにできる話じゃないと思う。俺はさっと起き上がって、笑美をちゃんと起こすように肩を優しく揺さぶる。"




scene bg school_dormemi_ni
with locationchange


hi "おい、大丈夫か？"



"なんともまぬけな質問だ。"


show emi basic_shock_gym_close_ni at tworight
with charaenter


emi "へ？　なに？"

show emi basic_hes_gym_close_ni
with charachange



emi "久夫くん？"




"笑美は何かを払いのけるように頭を振って、さっと涙をぬぐった。"





hi "悪い夢でも見たんだよ。たぶん"


show emi sad_shy_gym_close_ni
with charachange




"笑美はまた震えて、少し怖がった様子でちらっと俺を見上げる。自分が本当に起きているのかどうかわからないみたいに。"




emi "う、うん。そうみたいだね"



hi "話してみる？"




emi "んー？"




"頭の中でめまぐるしく行われているらしい議論が、肩をすくめることで終わる。"


show emi basic_hes_gym_close_ni
with charachange



emi "いいよ、あんまり覚えてないし"




"嘘をついているのは見え見えだけど、なぜか、深入りはしないほうがいいと思った。"



show emi sad_shyblush_gym_close_ni
with charachange



"笑美はまた震えてこっちを見る。少し恥ずかしそうな顔だ。"




emi "あんなふうに寝ちゃってごめんね"



"俺はできるだけ安心させるような声のまま言う。"





hi "いや、気にするなよ。病み上がりだし"




emi "うん、あの風邪薬で少し眠くなっちゃったみたい"



hi "みたいだな"



"笑美はあんなにあっという間に寝るようなタイプには見えない。"




"琳ならそうなるのかもしれないけど、笑美は活発すぎる。"



show emi basic_grin_gym_close_ni
with charachange




"笑美は俺の返事に半笑いを浮かべて、そしてあっけなく元の笑美に戻る。"



show emi basic_closedgrin_gym_close_ni
with charachange



emi "じゃあ、久夫くんはちゃんと明日に備えること！"


show emi excited_proud_gym_close_ni
with charachange



emi "二人とも今日の分を取り戻すために二倍がんばらなきゃいけないからね！"






hi "俺は今朝走りに行ったぞ！"


show emi basic_annoyed_gym_close_ni
with charachange



emi "言いわけしない！"




hi "わかったよ、覚悟しておくよ！"


show emi basic_grin_gym_close_ni
with charachange




"笑美は満足げにうなずく。"





emi "よし"




"それを、ここを出るきっかけにする。"






hi "じゃ、俺はもう行ったほうがいいな。明日のためによく寝ておこうっていうなら、なおさらな"





show emi basic_grin_gym_ni
with vpunch




"俺はベッドから飛び降りてドアへ向かう。"




show emi sad_shy_gym_ni
with charachange



emi "ねえ、久夫くん……"



hi "うん？"




"俺はきれいに回れ右して笑美のほうを向く。"




show emi basic_hes_gym_ni
with charachange



"笑美は何かを言いかけて口を開き、それをもう一度繰り返す。少しためらっているのがわかる。"





"口を閉じて、また開く。"


show emi sad_grin_gym_ni
with charachange


emi "……ありがとう"




emi "その、来てくれて"





emi "琳以外で部屋に来てくれたのは久夫くんが初めてなんだ"




"これには驚いた。笑美なら誰かがいつも来ているものだと思っていた。"






"笑美は人気者のはず、だと思っていた。いつも廊下で誰かと話している。"




show emi sad_shy_gym_ni
with charachange



"笑美はまた躊躇する。"





emi "あと、あの後もいてくれてありがとね、あたしが……えっと"




show emi sad_depressed_gym_ni
with charachange



"表情に痛みがよぎる。"



emi "その"

show emi sad_grin_gym_ni
with charachange


emi "たすかった"


show emi basic_closedgrin_gym_ni
with charachange



"笑美はまた明るい表情に戻って元気に手を振る。"



emi "また明日ね！"



hi "ああ、またな"





"部屋から出ようとしたけど、何かが俺をまた振り向かせる。"





hi "なあ、笑美"


show emi basic_grin_gym_ni
with charachange



emi "ん？"




hi "もし何か話したいことがあったら、言ってくれよ、な？"


show emi sad_shy_gym_ni
with charachange




"この言葉に笑美はびっくりしたみたいだ。"



show emi basic_closedgrin_gym_ni
with charachange




"笑美の笑い顔がさらに広がる。"






emi "わかったよ、久夫くん"


show emi basic_grin_gym_ni
with charachange


emi "また明日の朝にね！"

scene bg school_girlsdormhall_ni
with locationchange



"頭が混乱したまま笑美の部屋を出る。"




"ほんとうに出てくるべきだったのか？"





"ほんとうに笑美は大丈夫なんだろうか？"





"引き返して廊下を戻って、ドアを開けて、笑美に……"


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear

nvl show dissolve



n "\n\n好きだと伝えたい、きれいだと思っていると伝えたい、必要な時はそばにいると伝えたい。"






n "いっしょにいたい、笑美がまた眠るまでそばで抱きしめていたい。"




n "笑美はどれだけの夜をあんなふうに過ごしたんだろう？"




n "目が覚めても誰もいないと気づくだけで。"




n "そんなことがあったとき、いっしょにいられる人になりたい。"




n "ばかげた考えなのは、知っている。"




n "まだそんなにお互いのことを知らないのに？"





n "それらの考えが、気分をうわつかせるけど、不安にもさせる。"








n "心配、なのかもしれない。踏み込みすぎじゃないのかって。"









n "さらにやっかいなことに、笑美はもう他の誰かに興味を持っているように思える。"



nvl clear




n "\n\n\n\n\n\n笑美の健康状態にやけにご執心の、例の陸上部の部長。"






n "確かに、そいつが笑美と二人でいるのを見たことは数回しかないけど、二人がお似合いっぽいことに変わりはない。"






n "それについては何もできることはない。"




n "どうにかしてこの状況から気をそらさないといけない。"


$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear

nvl hide dissolve

window show



"宿題やんなきゃな。"




"それで気も紛れるかも。"



stop music fadeout 2.0

$ suppress_window_after_timeskip = True

scene black
with dissolve

label jp_E14:

window hide None

scene black
with dissolve

scene bg school_dormhisao
with openeye

window show



"眠れない夜のせいで今朝はけっこうふらふらだ。"


play music music_drama fadein 8.0




"前日のできごとが頭の中に割り込み続けている。"






"俺によりかかる、笑美の感触の記憶。"





"俺と笑美の取っ組み合いの記憶。"




"そしていちばんやっかいな、笑美の悪夢の記憶。"




"笑美はとても苦しんでいた。"




"目が覚めても誰もいないなんてどんな感じなんだろうと思わずにはいられない。"


scene bg school_dormbathroom
show steam
with locationskip

play ambient sfx_shower fadein 1.0


"シャワーの熱いお湯で目が覚める。目は覚めたけど、心配だ。"

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl show dissolve

nvl clear



n "\n今日は何が起こるのだろう？"




n "全部普段どおりに戻るだけなのか？"




n "あの話はあれで終わって、今までどおりに？"







n "昨日はつながりがあった。二人の関係を、それまでのただの友情という一線から押し出しそうになった何かが。"





n "それはそんなに悪いことだったのだろうか？"






n "枕投げの後で見た笑美の目を思い出す。あれはまるで、もっと踏み込むよう俺を挑発しているように見えた。"







n "たぶん。"





n "でも確信はない。"







n "とにかく、笑美が一番お気に入りなのは陸上部の部長なんだろう。"






n "そう思いながらも、俺の意識はあざけるように鼻を鳴らしている。自分は言いわけを探しているだけだ。とにかくうまくいかない理由を。"






n "挑戦しない理由を。"


nvl clear



n "\n\n\n\n部活の練習の時以外に二人でいるところを見たわけでもない。"





n "そして彼が笑美のところに行ったことがないのは明らかだ。笑美自身が言っていた。もし仲が良かったら、訪ねているはずだ。"







n "ほんとに臆病者だな、俺は。"





n "とにかくやってみりゃいいんだ、結末なんて知ったことか。"






n "笑美ならやるだろう、と思う。そうだ、笑美なら{b}絶対に{/b}やるに決まってる。"








n "笑美が俺に興味がないと確信する理由の一つがそれだ。笑美だって何も行動を起こしていない。"







n "それは陸上部の部長のせいなのかもしれない。報われない片思いの恋みたいな状態なのかもしれない。"


nvl clear


n "\n\n\n\n\n\nでも誰があの二人の関係をはっきりとさせられるんだろう？"




n "笑美には聞けるわけがない。たぶん笑美はただ笑って、どうして知りたいのかと聞いてくるだけだ……そして答える準備はできていない。"







n "琳……琳ならたぶん謎めいた返事かなにかをするだけだろう。それに下手をすると、琳は直接笑美に聞いて、笑美はなぜ俺がそんなことを知りたいのか聞いてくるんだ。これについてはもう検討済みだ。"






n "もしかしたら……"

nvl clear



n "\n\n\n\n\nナースに聞けばどうにかなるか？　笑美をとても気遣っているように見える。もしなにかあったら知っているはず……"



n "それに笑美が病気だったことを俺に伝えなかったという貸しがあるから、黙っているだろう。"


n "でも、もしなぜ俺が知りたがっているかを聞いてきたらどうする？"



n "なんとかごまかせるな。友達として気になると言うだけだ。それで納得するだろう、するよな？"





n "するだろ！"




n "じゃあ、これで解決だ。"



n "走った後で、笑美が医務室の外で待っている間に話そう。"


stop ambient fadeout 2.0

nvl clear

nvl hide dissolve

scene bg school_track
with locationskip

nvl show dissolve




n "\n\n\n\n俺がトラックに来ても笑美がいる様子はない。まだ具合が悪いんだろうか？"





n "十分ほど待つことにする。"




n "俺は早めに着いているし、笑美は昨日風邪を引いていたので、ここに来るのに時間が掛かっても不思議じゃない。"





n "でも、時間を無駄にするのも嫌で、結局ストレッチをしたり不安でうろうろしたりする。"




n "もし昨日自分がやり過ぎていたらどうしよう？"




n "もし笑美が恥ずかしがって来なかったらどうしよう？"



n "もし……"

$ renpy.music.set_volume(1.0, 2.0, channel="music")
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

nvl clear

stop music fadeout 2.0

nvl hide dissolve

window show

show emi basic_closedgrin_gym at center
with charaenter



emi "今日も早いね、久夫くん！"


show emi excited_proud_gym
with charachange



emi "感心感心！"




"あっけなく、身体から緊張がいくらか抜けていくのを感じる。"





"笑美はいつもどおり明るく元気そうで、昨日まで寝込んでいたそぶりも見せないどころか、眠れぬ夜を過ごしたなんてこともなさそうだ。"





"でも、聞かなきゃいけない。"




hi "昨日はよく眠れたか？"


play music music_serene



"ただの、その場だけの質問だ。雑談だ。"




"喫茶店で朝のコーヒーを注文していたら知り合いにばったり会ったようなときにするようなものだ。"




"でも俺たちの間では違う。少なくとも、俺にとっては。"





"笑美が昨日よく寝られたかを俺が本気で心配していることに気づいたかはわからないけど、その質問で笑美は一瞬止まった。"



show emi basic_grin_gym
with charachange



"しばらくしっかりと考え込んだように思えるような間の後、笑美はうなずく。"



show emi basic_closedhappy_gym
with charachange


emi "うん！　もちろん！"


"俺のおかげか？"




"俺は本当に助けになったのか？"





"それとも俺の質問をやめさせるためにそう言っているだけなのか？"



hi "そりゃよかった"

show emi basic_closedgrin_gym
with charachange



"笑美は笑って準備運動を始めた。"


show emi basic_grin_gym
with charachange


emi "それで、始める準備はいい？"




hi "ふっ、準備はいいかって？　もちろんいいよ！　生まれたときからＯＫさ！"



show emi basic_closedhappy_gym
with charachange



"笑美は俺の見栄に笑って、二人で走り始める。"


scene bg school_track_running
with shorttimeskip


"俺はずっと一定のペースで走り、一定のペースで呼吸をする。"

scene bg school_track_on
with Dissolve(2.0)





"走り終えたら死んだような気分にはなるけど、水から上がった魚みたいに息を切らす事はもうなくなった。"





show emi basic_happy_gym:
    center
    xpos 0.6
    easein 0.5 center
with charaenter



"今日の笑美は走り終わってからとても晴れやかな顔をしている。"



emi "よくやったね、久夫くん！　進歩してるよ！"



show emi basic_closedgrin_gym
with charachange



emi "もうすぐあたしの半分ぐらいの速さになれるよ！"





"最後の台詞は俺もすっかり慣れてしまった、からかうような笑顔で言った。"





hi "ああ、それは楽しみだな"


play ambient sfx_emisprinting

$ renpy.music.set_volume(0.3,1.0,channel="ambient")

hide emi
with easeoutleft



"俺がクールダウンするあいだに、笑美は全力で走り始めた。"



"今日はやけに頑張っている。"

stop ambient fadeout 1.0

scene bg school_track
with shorttimeskip

$ renpy.music.set_volume(1.0,0.0,channel="ambient")



"俺がクールダウンを終えると、笑美は疲れ切ったみたいにベンチで横になっている。"




hi "おいおい、今日はちょっと頑張りすぎてないか？"





hi "風邪ひいてたんだぞ、覚えてるだろ"


show emi basic_annoyed_gym at center
with charaenter


"笑美は鼻を鳴らして起き上がる。"



emi "ふん！　遅れた分を取り返そうとしてるだけだもん"




show emi excited_happy_gym
with charachange



emi "今日はいつもの二倍がんばったんだよ"


show emi excited_laugh_gym
with charachange




emi "いい走りをするとすっきりするんだよ"




show emi basic_closedgrin_gym
with charachange



emi "頭もはっきりするし、ね"




hi "ほう？"




show emi excited_happy_gym
with charachange




"笑美は元気よくうなずく。"




show emi excited_amused_gym
with charachange



emi "うん！　そういうのを解消するには最高なんだ"




"笑美はそれ以上説明しないし、俺も聞かない。"





"笑美が今日はあんなにがむしゃらになった本当の理由を知っている気がする。"






"風邪だったことは関係ない。何かが気になっているんだ。"



"もしかしたらあの悪夢なのかもしれない。もしかしたら他のことかもしれない。"




"でもそれは俺が首を突っ込むところじゃない。"





"もし知ってほしいなら向こうから言ってくるはずだ。"




hi "そりゃ便利だな"


show emi basic_grin_gym
with charachange



emi "久夫くんにはわからないよ"




"その声の正直さが俺の疑いを裏付ける。"





"ここで問題がひとつ……"




"俺に知ってほしかったら笑美が話すだろうけど、それでも俺は知りたい。"




hi "じゃあ、なにか悩みでもあるのか？"



"笑美は俺の質問に驚いた様子はない。"


show emi basic_closedgrin_gym
with charachange



"かわりに、肩をすくめる。"


show emi sad_grin_gym
with charachange



emi "んーん、心配するようなことじゃないよ"





"まるで、俺への説得と同じくらい、自分にも納得させようとしているみたいだ。"




"そんな気持ちになるのは昨日のことのせいなのかと聞こうと思って俺は口を開きかけるけど、考え直してやめる。"





"その質問を笑美が変なほうに受け取るリスクが高すぎる。"





"それに、自分でも昨日のことをどう考えたらいいのかわからない。"





"隣で寝ている笑美の感触を思い出そうとすると脳がシャットダウンしてしまうのが本当のところだ。"





"汗まみれのまま顔をしかめてこっちを見ている笑美を前にすると、考えるのが難しくなる。"





hi "ああ、そうか"





show emi basic_hes_gym
with charachange



emi "急いでナースくんのところに行ったほうがいいね。時間もなくなっちゃってるし"



hi "いつもそうじゃないか？"

show emi basic_grin_gym
with charachange



"笑美が笑う。一番笑美らしくない乾いた笑いだ。"

show emi sad_grin_gym
with charachange



emi "ほんと、そうね"





"ほんの一瞬、笑美は古傷で衰えてしまったかのように、老いて見えた。"






"でも昨日のように、重荷を背負って、か細くても真っすぐに立っているように思える。"





"そして笑美はいつも通りに戻る。"


show emi excited_proud_gym
with charachange



emi "じゃ行くよ、久夫くん。競走しよ！"



play ambient sfx_emisprinting

hide emi
with easeoutleft

stop ambient fadeout 2.0



"笑美はいきなり笑って、駆け出す。"




hi "っておい！　ずるいぞ！"





"俺は笑美を追って駆け出す。捕まらないだろうけど知ったことか。"




"勝算なんかなくても、笑美を追いかけて走る。"



stop music fadeout 2.0

scene bg school_nursehall
show emi basic_grin_gym at center
with locationskip



"俺が到着すると笑美がドアのところで待っている。"



show emi basic_closedhappy_gym
with charachange




emi "あれあれ、ビリはだーれだ！"





hi "はい、はい"


hi "今のうちに勝ち誇ってればいいさ"

show emi basic_closedgrin_gym
with charachange




"笑美がにやにやしているとドアからナースが頭を出す。"




show nurse neutral:
    center
    xpos 0.0 xanchor 0.5
    easein 0.5 xpos 0.1
with charaenter



nk "ああ、そこにいたのか"




nk "入ってくれ、久夫くん"


play music music_nurse fadein 1.0

scene bg school_nurseoffice
show nurse neutral at center
with locationchange



"俺にもすっかり習慣になった手順で、ナースが血圧と心拍数を計る。"


show nurse fabulous
with charachange



nk "今日はちょっと速いんじゃないか？"






hi "ええまあ、ちょっとここまで笑美と競走したっていうか"



show nurse grin
with charachange



"ナースは笑う。"




nk "それはよくないな！"


show nurse neutral_close
with characlose



"ナースは俺のほうにかがんで内緒話をするようにささやく。"


show nurse fabulous_close
with characlose



nk "もう聞いてるかどうか……でも笑美ちゃんは陸上ではちょっとしたスターなんだよ"



show nurse fabulous
with vpunch



"俺は驚いたふりをしてのけぞる。"




hi "そうなんですか？　そんなこと一言も言ってなかったですよ！"


show nurse grin
with charachange



"二人で笑う。"


show nurse neutral
with charachange



nk "今日の笑美ちゃんは大丈夫だったかい？"





nk "風邪の影響はなかったかな？"



hi "どうして自分で聞かないんですか？"

show nurse concern
with charachange




"ナースはあきれたように空を仰ぐ。"






nk "そりゃもちろん笑美ちゃんにも聞くよ。でも全然問題ないって答えるさ、問題があってもなくてもね"




show nurse fabulous
with charachange



nk "それで君に聞いてるんだ。君は笑美ちゃんの友達だし、笑美ちゃんに何かあったら僕に話してくれるだろうからさ"






"ナースがそう言うと、すごく納得できる。"




hi "今日はずいぶん調子よさそうでしたよ、普段よりちょっと疲れてたかもですけど"





hi "昨日行ってみた時はもう大丈夫だったから、驚きはしないですけど"



show nurse neutral
with charachange




"ナースはうなずくけど、俺が昨日お見舞いに行ったことを話す時ちょっと緊張するのに気づく。"





nk "まあ、それならよかった"





nk "あれは一日あれば治る程度のものだとみていたんだ。笑美ちゃんは風邪みたいなことの治りはいい方だし"





hi "そういえば、笑美の話なんですけど……"





hi "笑美と陸上部の部長って……？　その、ほら"



show nurse fabulous
with charachange



"疑惑の表情が顔を横切る。"



nk "どうしてそんなこと聞くんだい？"



hi "その、仲よさそうに見えるし、ただの好奇心なんですけどね"






hi "それに俺から本人には聞けないですよ、なんか恥ずかしくて"




"ここまでは、大丈夫だ。もう一押ししよう。"


hi "それに、二人だったらお似合いだと思いますし"

show nurse grin
with charachange



"ナースは笑う。"



nk "まあ、そう思うのは君が初めてじゃないだろうね"






nk "でも、わりと確信を持って言えるけど、二人は絶対そんなことにはならないと思うよ"








hi "確信？"


show nurse neutral
with charachange



nk "ああ"


show nurse fabulous
with charachange




nk "もちろん、僕が言えることじゃないけどね。守秘義務やら何やらでさ"






hi "よく言いますよ、俺に隠しごとするのが好きなだけでしょ"



show nurse grin
with charachange


nk "それもあるかな"

show nurse neutral
with charachange



nk "よし。もう行っていいよ。なんたって、僕は忙しい男だからね"


stop music fadeout 2.0

scene bg school_nursehall
show emi basic_grin_gym at center
with locationchange



"最後の台詞にあきれながらドアを出て、部屋に入るよう笑美に合図する。"


show emi basic_grin_gym:
    center
    easeout 0.5 xpos 0.4 alpha 0.0
with Pause(0.5)

hide emi
with None



"その間、踊りだしそうになるのをこらえるので必死だった。"


window hide

play music music_running




centered "二人は絶対そんなことにはならないよ"


window show


"それこそが俺が聞きたかったことだ。"



"今すぐに笑美に何らかのアプローチをかけようと思ったけど、多分ナースは反対するだろう。"




"それに、まだ笑美が俺のことをどう思っているかがよくわからない。"






"友達として大事にしてくれてるのは当たり前だけど、それ以上はどうだ？　確かなことは言えない。"




"それでも、期待できると思わずにはいられない。あとは俺がどう思っているかを笑美に伝えるいいタイミングを見つけるだけだ。"



"少なくとも、このパズルは一日中頭から離れないだろう。"

stop music fadeout 6.0

label jp_E15:

scene bg school_nursehall
with None

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

scene bg school_roof
with shorttimeskip


"屋上は完全に無人状態だった。"



"普通なら俺より先に琳が上がってきていると思っていたけど、妙なことにいなかった。"





"今回だけは笑美と一緒に食堂に行くことにしたんだろうか。そんなことはなさそうだけど、今はそれぐらいしか思いつかない。"






"琳を探しに行きたいと思うけど、この日だまりの感触を味わっていたいという思いのほうが大きかった。"




"俺は笑美と琳が来るのを待ちながらぼんやりと昼飯を食べる。"





"誰かが階段を上がってくる音が聞こえるまでそんなに時間はかからなかった。"



$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_door_creak





"俺は扉が開き始めると口を開く。"






hi "ずいぶん時間かかったな"




hi "待たせておいて、まったく"





hi "二人とも……"




hi "え？"




"おかしいぞ。"



show emi basic_confused at center
with charaenter



"そこに立っているのは笑美だけで、少しとまどっているみたいだ。"





emi "『え？』ってなによ？"



show emi basic_grin
with charachange



emi "あたしよ！　ほら、笑美だよ！　今朝一緒に走ったよね"





"笑美が笑う。それを見て俺は心臓が少し跳ねるのを胸に感じる。"






hi "ああ、それは知ってたけど。その、ちょっと混乱してて……"





hi "……琳はどこだ？"


show emi sad_depressed
with charachange



"笑美の笑顔は悪いことをしてしまったような表情に変わる。"




emi "ああ、そのことなんだけど……"



emi "その……なんていうか……"

show emi sad_shy
with charachange



emi "風邪うつしちゃったみたい"



play music music_another fadein 0.5
$ renpy.music.set_volume(1.0, 0.0, channel="sound")



hi "ありゃ"



hi "俺も危ないかな？"



"ありそうなことだ。笑美と俺は先日ぴったりくっついていたし……"





"じゃあ笑美と琳が何をしたせいで琳が風邪になったんだ？"



"……"





"とりあえず、落ち着け。それ以上はいけない。"





"たぶん琳は俺より免疫力が弱かったんだろう。"



show emi basic_shock
with charachange



"笑美は俺の発言にショックを受けたようだ。まるでそんなこと考えもしなかったみたいに。"




emi "そんな！"

show emi excited_sad
with charachange



emi "もしあたしのせいで久夫くんが風邪ひいちゃったらいやだよ！"






hi "ああ、なんだか風邪で気分が悪く……"


show emi sad_annoyed
with charachange



"笑美はぞっとしたみたいだけど、すぐに怒った顔に変わる。"




emi "久夫くん！"



emi "今すぐ風邪になるのをやめて！"

show emi basic_annoyed
with charachange



emi "そんなの認めない！"


show emi basic_annoyed_close
with vpunch



"笑美は衝動的に俺の襟をつかむ。"






emi "聞いてる、久夫くんの抗体たち？"



show emi sad_angry_close
with charachange



emi "さっさと働きなさい！"





"俺はパッと敬礼する。"





hi "了解です、隊長"


show emi basic_grin
with charadistant



"笑美は後ろに下がって、満足げにうなずく。"



show emi basic_closedgrin
with charadistant


emi "よし"

show emi basic_happy
with charadistant



emi "もうこれ以上朝のランニングさぼるの禁止だから"





hi "でも笑美は一回さぼったじゃないか！"


show emi sad_annoyed
with charachange



"笑美は腕組みをして横柄に俺をにらむ。"







emi "そうだよ、でもそれは特例。あたしだったから、久夫くんじゃなくて"






hi "それ全然説明になってないぞ"


show emi basic_confused
with charachange



"笑美はぽかんとしている。"





emi "冗談、だよね？"


show emi basic_annoyed
with charachange



emi "その説明で完璧にわかるじゃない！"




hi "全然だろ！　あからさまなダブルスタンダードだ！"




show emi sad_annoyed
with charachange



emi "それがなんの関係があるのか全然わかんない"





hi "ああ、もういいよ"



show emi basic_closedgrin
with charachange


"笑美は自分の勝利に満足げだ。"


hi "どっちにしろ、琳は大丈夫なのか？　そんなにひどい風邪じゃないんだろ？"

show emi basic_grin
with charachange



"笑美は首を振る。"




emi "うん！　大丈夫そう"


show emi excited_proud
with charachange



emi "よく効く風邪薬あげたから"


show emi basic_hes
with charachange




emi "でもいっぺんに全部飲まないように確認しておけばよかったかも……"





show emi basic_grin
with charachange


emi "その、前にやったことあるから"






"なぜか、それを聞いてもそれほど驚かない。"






"琳が薬の用量用法みたいなことを気にするかどうか怪しいもんだ。"





hi "だったら、あとで確認したほうがいいと思うぞ。念のために"


show emi sad_grin
with charachange




"笑美は肩をすくめる。"






emi "練習が終わったら寄ってみるね。それまでは大丈夫でしょ"





"この話題が終わったことを察して、俺はうなずく。"






"問題は、他に何を話せばいいかわからないことだ。"



hi "それで……"



hi "この先も陸上の試合とかってあるのか？"


window hide

nvl clear

nvl show dissolve



n "\n\n\n\n\n\n\n\n週末の予定が空いているか確認するにしては、ひどく遠回りな方法だ。"




n "もし暇なら、デートに誘えるかもしれない。"



n "まあ、うまい具合に言葉を探せればの話だけど。"


nvl clear

nvl hide dissolve

window show

show emi basic_grin
with charachange



"笑美は首を振る。"


show emi basic_closedgrin
with charachange



emi "んーん、あと何週間かはないと思うよ。そろそろ落ち着いてくる時期だし"





"そうか。俺は学期のど真ん中にやってきたんだったよな？"





"ということはもうすぐ試験なんだろうか？　それも頭に入れておこう。"





hi "試合がない週末は何してるんだ？"



show emi excited_proud
with charachange



"笑美の眉が上がって、からかうような表情になる。"





emi "久夫くん、今日はやけに知りたがりだね？"






"俺は冷静に見えるように願いながら肩をすくめる。"




hi "会話をしようとしてるだけさ"



hi "やっぱり、陸上のスターでいるのってどんな感じかわからないし"



show emi basic_closedgrin
with charachange



emi "ふふ、お世辞ね"




"笑美は手をぶらぶらと振る。"


show emi basic_grin
with charachange




emi "ほんとはそんなすごくないんだよ"



show emi basic_closedhappy
with charachange



emi "久夫くんはたまたま調子のいいときに見に来ただけだもん"





hi "うそつけ"



show emi sad_grin
with charachange

stop music fadeout 6.0



emi "あはは、そうね"




emi "でも謙虚なのはいいアスリートの条件だよ"


show emi sad_depressed
with charachange





emi "少なくとも、パパはよくそう言ってた"







"笑美は肩をすくめる。顔に浮かんだ暗い気持ちを隠そうとするけど、うまくいっていない。"




hi "なあ、どうしたんだ？　なにか悩みでもあるみたいに見えるぞ"




"笑美は否定し始めるけど、くじけたようにため息をつく。"





"病み上がりで疲れていて、いつものように否定する元気がないんだろうか。"





"それとも、大事なことを打ち明けられるくらい本当に信頼してくれているんだろうか。"


show emi sad_shy
with charachange

play music music_comfort fadein 9.0



emi "あのね、昨日の夜のこと覚えてる？"




"もちろんだ。でも、とりあえずうなずくだけにしておく。"


show emi sad_depressed
with charachange



emi "あたしがああなったのは初めてじゃないんだ"





emi "っていうより、あれは……"






"笑美は言葉を切る。自分がいま何をしているか突然気づいたように。"





"まるで、自分で作ったルールを破っているみたいだ。"



"でもまた、慎重に言葉を選んで話し始める。"





emi "まあ、よくあるわけじゃないんだけど、でも……"



show emi sad_shy
with charachange



emi "ときどきね"



emi "それがたまたま起きたときだったの"

show emi sad_depressed
with charachange



"笑美からため息が漏れる。まるでひどく打ち負かされたみたいだ。"


show emi sad_shy_close
with characlose




"俺は笑美に近づいて抱きしめる。前の時とは違って、笑美はそれほど驚いていないみたいだ。"




"というより、俺の腕の中で安心しているように見える。"



"俺たちはしばらくそのままでいる。"




hi "なあ、昨日言ったことは本気なんだ"





hi "もし何か悩みがあるなら話してくれていいんだ。そういうのは一人でどうこうするのは大変だしな"


show emi sad_grin_close
with charachange



"笑美は笑って、抱いた腕をほどく。でも俺の肩に寄りかかったままだ。"




emi "ありがと、久夫くん"


show emi basic_grin_close
with charachange




emi "大丈夫だよ、たぶん"






"笑美が早くも自分を立て直して、また全てを封じ込めようとしているのがわかる。"





"この話は終わったみたいだな。"



hi "ところでさ、進路調査のこと何か考えたか？"

show emi basic_closedgrin_close
with charachange



emi "そうとは言えないかな"


show emi basic_grin_close
with charachange



emi "あたし、あまり先のことまで計画したりしないから"





emi "でもそろそろ大学のことを調べるくらいはしてみてもいいのかもね？"





"俺は肩をすくめる。"



hi "かもな、例の海賊のこと本気じゃなければだけど"



hi "前に確認したら、海賊は大卒でなくてもよさそうだし"





hi "世間のどっかに海賊の大学みたいなのがあったら、話は別だけど"




show emi basic_closedgrin_close
with charachange



"笑美はくすくす笑いながら元の自分に戻っていく。でもその表情には新しい要素が加わっている。"




"いたずらっぽさ、だな。"





"笑美は、いたずらっぽく、俺の肩に頭をあずけたままこっちを見上げる。"


show emi sad_grin_close
with charachange



emi "もしあたしが海賊になったら一緒に来てくれる？"






hi "もちろん行くよ！"




hi "正気の人間で笑美と一緒に海賊になれるチャンスを逃すやつなんかいないだろ？"



show emi basic_grin_close
with charachange



emi "まあ、そんなふうに言われると、どうだかわからないけど"



show emi basic_closedgrin_close
with charachange



"また笑美は笑う。"




"自分の心臓が速くなった様子に気がつく。たぶん笑美が近づいてきたのが原因だろう。"






"また、あの微かなイチゴの香り。"




"笑美を見下ろす。どうしても笑顔になってしまう。"




"笑美はまた元気になったみたいだ。"


show emi sad_shy_close
with charachange



emi "ねえ、久夫くん"



hi "ん？"

show emi sad_grin_close
with charachange





emi "もしキスするつもりなら、早くしたほうがいいよ。もう昼休みのベル鳴るだろうし"





stop music fadeout 1.0



"俺の思考が緊急停止する。"




"口は確実にショックで開いたままなんだろう。"




"かろうじてできたのは、息が詰まったような『は？』という声を出すことだけだった。"



show emi basic_closedgrin_close
with charachange



"それで笑美はもっと面白がる。"


show emi excited_proud_close
with charachange




emi "そう思ってたんでしょ？"





"笑美は座りなおして、俺と同じ高さまで顔を上げてくる。"


show emi basic_grin_close
with charachange



emi "あたしもきっとうれしいし。ね？"



show emi sad_grin_close
with charachange



emi "久夫くん、本当に……"


show emi sad_shy_close
with charachange


emi "……その"




"笑美は、なにか大切なことを言いかけているみたいに、少しの間自分を落ちつかせる。"




show emi sad_grin_close
with charachange



emi "もし気がついてないとしたらだけど、あたし、久夫くんのこと本気で好きになっちゃったみたい"



show emi basic_grin_close
with charachange



emi "どうにかしてくれるんだよね"




"その笑顔で今度は大事な思考プロセスのいくつかがショートする。"




"いつの間にか俺は笑美のほうを向いていて、いつの間にか笑美の腕は俺の首に回っていた。"




"そして、俺の腕が笑美の腰を包んでいた。"





"いつのまにそうなっていたのか、自分でもわからない。"





"その瞬間、頭の中はキスをしろという声でいっぱいだったからだ。"




"俺は笑美の目を見つめる。"




"あの感じだ。"




"昨日ベッドで見たのと同じ。またあの感じだ。"





"それで突然、笑美は俺が拒絶するのを怖がっていることに気づく。"



stop ambient fadeout 1.5



"なんておかしな心配だろう。"


window hide

play music music_romance fadein 0.5

scene white
show ev emi_firstkiss:
    truecenter
    zoom 4.0 rotate 20 subpixel True
    0.7
    linear 0.3 zoom 1.1 rotate 0
    easein 12.0 zoom 1.0
with GenericWhiteout(0.5, 0.2, 2.0)

with Pause (5.0)

nvl clear
nvl show dissolve



n "\n\n\n\n笑美の唇は微かにイチゴの味がした。"




n "笑美はキスで俺に寄りかかって、腕を俺の頭の後ろにきつく回している。俺が身体を引き剥がさないように。"




n "そんなことをするはずがない。"




n "身体の中がかき回される感じだ。"




n "世界が崩れる。"




n "ここにあるのは俺と、笑美と、このベンチだけだ。"




n "抱く腕を強めて笑美の腰を引き寄せると、笑美の感触に自分を忘れた。"





n "笑美の香りを吸い込んで、俺の意識は笑美の味も、匂いも、感触も、そのすべてを記憶しようと必死になる。"



play sound sfx_warningbell
play ambient sfx_rooftop fadein 4.0

nvl clear

nvl hide dissolve

scene bg school_roof
show bg school_roof_blurred as overlay:
    center
    linear 6.0 alpha 0.0
show emi sad_shyblush_close
with silentflash

window show



"ベルの音が俺たちを現実に引き戻し、俺たちは唇を離した。"




"笑美は頬が少しだけ赤くなって、息を整えているみたいだ。笑美の名誉のために言うと、俺もだ。"




"今したことを頭の中で整理しようとして、俺たちはしばらくそのままでいた。"




"沈黙を最初に破ったのは笑美だった。"

show emi sad_grin_close
hide overlay
with charachange


emi "それで……"

show emi basic_closedgrin_close
with charachange



emi "……練習終わったら一緒に晩ご飯食べよっか？"




hi "偶然だな"



hi "俺も同じこと聞こうとしてた"




"まあ、実際には週末かそのくらいにちゃんとしたデートっぽいことをするんだろうけど、今夜のことも聞こうと思った、と思う。"



with vpunch



"笑美はふざけて俺を押す。"


show emi basic_happy_close
with charachange


emi "嘘つき"


show emi basic_closedhappy_close
with charachange



emi "まだそっちはあたしのキスがすごかったことに驚いてたじゃない"



"俺たちはそれぞれの教室に向かうために階段を降り始める。"


stop ambient fadeout 2.0

scene bg school_hallway3
show emi sad_grin at center
with locationskip


hi "おい、そっちだってしばらく喋らなかったじゃないか"



show emi basic_closedgrin
with charachange



emi "わざとだもん"




show emi basic_closedhappy
with charachange



emi "じゃ、練習のあとでね、久夫くん"


show emi basic_closedgrin_close
with charachange

show emi basic_closedgrin_close:
    center
    easeout 0.5 xpos 0.6 alpha 0.0
with None



"笑美はすっと俺にもたれて廊下の真ん中で素早くキスしてきて、俺はまたしばらく呆然とさせられる。"


scene bg school_scienceroom
with locationchange



"自分の教室に向かうと、ミーシャが笑って出迎える。"


show misha hips_grin at center
with charaenter




mi "ひっちゃんたら～、ロマンチックなんだから～、この～！"




mi "屋上で告白してたんでしょ？　でしょ～？"



hi "えと、実はその逆だったっていうか"


show misha cross_laugh
with charachange



"この発言にミーシャはまた笑いの発作を起こす。"


show misha hips_grin
with charachange



mi "若い子の恋愛はほんと何があるかわかんないよね～？"




"ミーシャのことだから、からかわれるのを予想するべきだったかもしれない。"



hi "かもな……"

show misha hips_grin:
    center
    easeout 0.5 xpos 0.4 alpha 0.0
with None




"なにか言い返せる前に武藤先生が教室に入ってきて、ミーシャはずっと笑いながら自分の席に戻る。"






"笑美が廊下のど真ん中でキスしてきたことを考えると、この先こんな感じの会話が増えるんだろう。"




"でもとにかく、そんなことはどうでもいい。"


$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 5.0



"ここに来てから初めて、心が軽く感じる。"


window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
