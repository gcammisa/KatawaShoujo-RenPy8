
label jp_E16:

window hide None

scene bg school_scienceroom
with fade

nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_normal fadein 3.0


n "\n\n\n武藤先生の授業の間ずっと、俺の頭の中で様々な思いが渦巻いている。"




n "夕ご飯を食べに行くんだ。"



n "笑美と一緒に。"



n "間違いなく、俺の彼女になりたがってる。"


n "デートか……"



n "しかも向こうからキスしてきた。"




n "あのキス。そのことを考えずにはいられなくて、何度も何度も頭の中で繰り返している。"




n "あの瞬間の全てが、正に申し分のない様に感じられた。"





n "笑美への思いで頭が一杯になり、意識がふっと遠ざかってしまう。"



$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear
nvl hide dissolve
window show

show muto normal
with charaenter


mu "おい、中井？　聞いてるのか？"



"どうやら遠ざかりすぎていたみたいだ。"



hi "えっ？　何ですか？"




show muto irritated
with charachange



mu "まったく！　記憶喪失にでもかかったか！"






mu "おい、誰かナースを呼んで来い！"



"武藤先生の冗談で教室中からくすくすと笑い声が聞こえる。"


hi "すいません、先生"

show muto normal
with charachange


mu "ふむ。もうそういうことは二度とないようにしてくれよ。いいな？"




hi "もちろんです"


"それを聞き、先生の顔がかなり明るくなる。"


show muto smile
with charachange


mu "よし！　そう言ってくれて嬉しいぞ！"



mu "なんと言ったって、俺の優等生を怠けさせてしまいたくはないからな"



hide muto
with charaexit



"俺の成績は良い感じではあるけど、優等生と言われるほどじゃないと思うなあ。"





"はっきり言って、この科目は誰でも良い成績を取れる類のものだ。公式を暗記するだけなんだから。"





"自分の言葉通りに、俺は残りの時間、授業に集中することができた。"




stop music fadeout 2.0

show muto normal
with shorttimeskip

play sound sfx_normalbell


mu "中井、少し話があるんだがいいか？"



"もしかして、さっきのことで怒られるんだろうか？"







hi "あ、はい。もちろんです"


hi "何かまずい事になってますか？"

show muto irritated
with charachange


"一瞬、先生は素で戸惑っているような表情を見せる。"




mu "ん？　どういう事だ？"



"そう言うと先生は首をかしげて、しばらく考える。"





show muto smile
with charachange



mu "ああ、あのことか！　いやいや、何も問題はないさ"





mu "一つ聞きたいことがあってな"




hi "なんですか？"


show muto normal
with charachange


mu "別に悪い話じゃないんだが、お前が卒業後の進路について何か考えているのか気になっていたんだ"




play music music_another fadein 2.0


mu "大学に行くつもりか？"



hi "ええ、多分そうすると思います。行かない理由が見つからないというか"



mu "どんな分野を専攻するのか考えた事はあるか？"



hi "いえ、そこまでは。入学した時に何かやりたい事が見つかるんじゃないかと思ってます"

show muto smile
with charachange


"先生が笑い出す。"




mu "物事はあるがままに受け入れよ、か？"



mu "それには賛成できないが、俺自身も大学に行った時にはそうしていたよ"





mu "いや、そうでもないか"


mu "理系の道に進む事は分かっていたが、その中のどれにするかは決めていなかったな"


mu "その時は物理学に決めたが、もしかしたら天文学か何かの道に進む事もできたかもしれない"



show muto irritated
with charachange



mu "実際のところ、最初は化学を学んでいたんだが、まぁあれやこれやと色々あってな……"



"武藤先生は声を次第に小さくし、わずかに顔をしかめる。"


"彼の思考の流れが再び戻ってくるまでのしばらくの間、俺はじっと話の続きを待っている。"

show muto normal
with charachange


mu "まぁとにかくだ。物理も興味があったのでいろいろとやってみたが、それが俺自身にぴったりかどうかの確証が持てなかった"


show muto smile
with charachange


mu "だから化学へと戻ってきて、そのおかげでお前とここに一緒に居るわけだ。わかるか？"


show muto smile
with charachange


"まるで『そうですね、よく分かります』と俺が答えるのを待っているかのように俺に熱のこもった笑顔を向ける。"








"どういうわけか、武藤先生は最初からこういう話をするつもりでいたような気がする。それが本当かどうかは分かるはずもないけど。"








hi "すいません、どういう意味ですか？"



"先生は面食らった様子で、眉をひそめてあごをなでる。そして話の要点が何だったのかを思い出したかのように指を鳴らす。"





mu "そう！　そうだ！　お前だ！"




hi "俺……ですか？"



mu "そう！　科学系の科目に進むことを考えてみるべきだ！"




mu "お前は科学系がとても得意だからな"



mu "数学方面に行きたいというのでなければ、の話だが"


show muto irritated
with charachange


"先生は不機嫌そうな顔をする。"




mu "純粋な数学と言うものには興味があまりなくてね。数式の証明よりも実験をしていた方がいつも楽しかったな"




hi "つまり、俺に大学で科学を学べと言いたいわけですね？"




"俺の質問に先生は狼狽したように見える。"



show muto normal
with charachange



mu "うむ、まあそんなところだ"


show muto smile
with charachange


mu "あとはそうだな、科学部に入る事もできるぞ！"



mu "問題は、ここには科学部がないってことだ"




mu "でも作ることはできる！"




mu "むしろ創立メンバーになれるチャンスだ！"



mu "科学部の父になれるんだぞ！"



mu "もちろん、他の部員も探さないといけないがな"



show muto normal
with charachange


mu "まぁ、お前がよければの話だ"



mu "俺たち二人ですぐに始める事もできるぞ"



mu "そして、だな"

show muto smile
with charachange


mu "俺から何か読むものを渡して、それについて話し合うんだ"



mu "えー、それで、だ。大学進学の準備とか、そういうことも手伝ってやれるぞ"



show muto irritated
with charachange


mu "ちょっと待った！"


"先生はかばんの中を引っかき回すと、取り出した本を俺に投げてよこす。"



show muto smile
with charachange


mu "それを読んでみろ"


mu "もし面白いと感じたら、それについて一緒に話そうじゃないか"


"『ホーキング、宇宙を語る』？"





"本当にこの本を読みたいかよくわからないけど、武藤先生はこのアイディアに随分と夢中になっているようだ。"




hi "これはどんな内容なんですか？"

show muto normal
with charachange


mu "時間。そして空間。時空だ。ブラックホールやその類のものについてだ"



mu "しかも、それほど難しい話じゃない。お前がそういう話に興味があるかどうかを知りたいんだ"






mu "放課後にぶらぶらしたり、議論を交わしたり、研究室に行って爆発物の作り方を教えてやる事もできるぞ"




show muto smile
with charachange


"俺の戸惑った表情を見て先生が手を振る。"


mu "すまん。ほんの冗談だ"



mu "だがまあ、少々話が長引いてしまったようだな"




mu "科学方面の進路について考えておいてくれよ、中井。お前なら楽しめると思うぞ"





hi "ええと、分かりました。そうしますね。本、ありがとうございます"


stop music fadeout 14.0

scene bg school_hallway3
with locationchange



"教室を出て、時計を見上げる。笑美の練習が終わるまでにはまだまだ暇つぶしを続けなければいけないようだ。"



"そうだな、この本を読んでみようか。シャワーも浴びた方がいいだろうな。"



"デートの前にシャワーを浴びるのはちゃんとしてるよな？"





"そんな事を考えながら寮に戻る。"



scene bg school_dormhisao
with locationskip


"そういえば、どこで笑美と待ち合わせればいいんだろう。"




"笑美は『練習の後に』と言っていたけど、どこで会えばいいのかについては言っていなかった。"







"とにかく、競技場に立ち寄ってみるのが、たぶん一番いいだろう。"





"もし笑美もシャワーを浴びたいと言うなら、笑美の部屋かどこかで待っていればいい。"




"いや、通路でもいいか。それでも別に構わない。"



"すばやくシャワーを浴び、部屋に戻るとすぐにいつもの薬を飲む。"



"さて、あの本を読んでみようか。"

stop music

scene black
with dissolve


label jp_E17:

scene black
with None

scene bg school_dormhisao
with vpunch


"はっと飛び起きる。"


"しまった！　今何時だ？"


"ちらりと時計を見ると、１時間近くは眠っていたのが分かる。"



hi "ああ、よかった"



"笑美の練習はもうすぐ終わるだろう。"





"普段着に着替え、競技場へと向かう。"

scene bg school_track
with locationskip


"なんとなく、この夕食が洒落たものになるなんて事はないだろうな、という気がする。"


"笑美はあまり洒落た事が好きなタイプのやつだって感じがしないし。"




"と言っても、笑美には俺の知らない部分がまだまだ沢山あるだろうけど。"






"最近の親密さの割に、俺は彼女のことを知らなさすぎる気がしてならない。"








"でもまあ、それを解決していく時間はまだまだあるはずだ。"









"正直なところ、笑美のことをこれからもっと知っていくというのが楽しみだ。"




"そんな考えが頭を駆け巡っていて、自分がすでに競技場に着いていたことを見落としそうになる。"



"笑美の姿が見当たらない。"



"他の陸上部員の痕跡すらどこにも見えない。"



"こいつはやっちまったかな。"


"そう思いながら女子寮の方に顔を向ける俺の耳に大声が聞こえてくる。"



emi "やっほー！　ひさおー！"


play music music_emi fadein 1.0

show emicas smile at center
with charaenter


"振り返ると、体育かばんを肩から下げ、まっすぐこちらへ向かってくる笑美が見える。"




"彼女はショートパンツとオリーブグリーン色の服に着替えていて、普段よりも間違いなくカジュアルな格好だった。"





"いつもの競技用義足から、より本物の足に似せて作られた物に変わっていたけど、それに気づかない人はいないだろう。"








"笑美はそんな事を気にする風には全く見えなくて、それが俺には微笑ましい。"


show emicas happy
with charachange


emi "来てくれたんだ！"

show emicas closedsmile
with charachange




emi "というか、来るとは思っていたけど……でもやっぱり……"



show emicas closedsmile_up_close
with characlose




"気がつくと俺は、とても情熱的に抱きしめられていた。おかげで自分の顔に、きっと世界で一番大きいであろう笑顔が張り付くのをこらえきれなかった。"










hi "おいおい、来るに決まってるだろ！"




hi "来ないなんて頭おかしいだろ？"



"笑美は少しの間考え込む。"


show emicas grin_up_close
with charachange



emi "うん、ほんとだね"



show emicas wink_up_close
with charachange


emi "なんてったってあたし、ちょー可愛いもんね"



"俺は肩をすくめて応じる。"




hi "そりゃそうだ"




show emicas blush_up_close
with charachange



"それが何気ない一言だったせいで、その言葉に笑美が驚いたのを見て俺は驚く。"





show emicas smile_up_close
with charachange



"顔を赤らめると、優しく笑いながら唇にキスをしてくる。"



"今度は俺の方が驚かされる番だ。"



show emicas grin
with charadistant


"笑美は一歩後ろに下がると、そのまま後ろ足で体を支えながら満足そうな表情をしている。"






"気のきいた返事をさがそうと、頭を全力で働かせる。"


hi "……"



hi "これからはもっと褒めてあげなきゃいけないよな"


show emicas happy_up
with vpunch


"笑美は笑って小突いてくる。"






show emicas closedsmile
with charachange



emi "バカ"



show emicas weaksmile_up_close
with characlose




"俺が笑美の肩に腕を回すと、そうするのが世界で一番当たり前のことであるようにすぐさまもたれ掛かってくるのに満足感を覚える。"




hi "さて、どこに行く？"

show emicas awayfrown_up_close
with charachange


emi "じつは特に考えてないの"

show emicas neutral_up_close
with charachange



emi "この辺りでデートするとしたら、どこに行くんだろ？"




"すごくいい質問だ。"



hi "全然知らないな"



hi "とりあえずオーラマートに行って、なにかその辺で食べられる物でも買うのはどうだ？"



"その考えを聞いて笑美の顔が明るくなる。"


show emicas happy_up_close
with charachange


emi "ピクニックね！"

show emicas wink_up_close
with charachange



emi "いいアイディアだと思うよ"








scene bg school_gate
with locationskip


"笑美が俺の腰に腕をまわし、そのまま二人で校門の方へと歩き始める。"


"正直いうとこんな状況で俺がなにをすべきなのかはさっぱり分からないけど、少なくとも笑美も俺と同じくらい分かっていないようだ。"

scene bg suburb_roadcenter
with locationskip



"笑美と一緒にいると安心するけれど、まだ少し緊張してしまう。"






"もしなにか間違った事をしてしまったらどうしよう？"


"無様な真似をして失望されるのは嫌だな。"

scene bg suburb_konbiniext
with locationchange



"オーラマートに到着するまでの間、笑美は陸上部の練習の様子についてしゃべりつづけている。"




"俺はほとんどなにもしゃべらずに、笑美の近くに居られる心地良さをただ楽しんでいる。"




"通りすがりの人々がたまに奇妙な物でも見たかのような表情をするけれど、俺は気にしない。"




"結局、店でいくつかのパンと即席麺を買ったけれど、公園では即席麺を作る事ができないと気づいたときには後の祭りだった。"







show emicas weaksmile
with charaenter


emi "ありゃ。まぁいいか、そのうちお昼ごはんにでもしよっと"



hi "それもそうだな"


stop music fadeout 2.0
$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

scene bg suburb_park
with locationskip


"少し道に迷った後、ようやく公園を見つける。俺は迷ったのは笑美のせいだと言い張る。"







"いうまでもなく、笑美は俺のせいにする。"


show emicas smile:
    center
    easein 1.0 ypos 1.13
with charaenter


"木の下に良さそうな場所を見つける。木の幹に寄りかかる俺の向かい側に笑美が座る。"

play music music_ease fadein 3.0



hi "地面に敷く毛布かなにか、持ってくれば良かったな"


show emicas smile_up:
    ypos 1.13
with Dissolve(0.2)

show emicas smile
with charachange


"笑美が肩をすくめる。"

show emicas closedsmile
with charachange


emi "別に気にしないよ"



hi "まあ俺も構わないけど"


show emicas grin_up
with charachange


"笑美が渡してきたパンを受け取り、二人で食べ始める。"


"カレーパンか。これはなかなか……"



"どうやら俺は、店で買う物を選ぶときになにも考えていなかったらしい。"

show emicas wink_up
with charachange



emi "ねえ久夫。その今食べてるパン、辛いんじゃない？"








"俺は頭を振って男らしさを保とうとするけど、無駄な努力に終わる。"






hi "いやいや、全然辛くなんてないぞ"

show emicas closedsmile_up
with charachange


emi "そっかそっか。だから顔がまっかっかになってるんだね"




hi "うむ、その通り。辛さが足りなくてだな……頭に血が昇ってきたんだ"


hi "がっかりしてるせいだろうな"

show emicas happy
with charachange




"笑美は笑うと、自分が食べていたパンの最後のひとかけらを口に放り込む。"




show emicas wink
with charachange



emi "ねえ、もし辛すぎるんだったら、あたしが代わりに食べてあげるよ"



hi "おいおい、自分のをあっという間に平らげたからって俺のを分けてもらえると思うなよ"




show emicas pout
with charachange


"笑美がわざとらしく不満そうな顔をするのを見て俺はつい笑ってしまい、パンがのどにつまりそうになる。"



emi "もお！　いいじゃん久夫！"


show emicas awayfrown
with charachange




emi "あたしが食事を十分食べたかどうかを心配するのが筋ってもんでしょ？"





emi "言っとくけど、あたしたちデート中なんだよ！"


show emicas pout
with charachange


emi "と言っても……"


"突然笑美が困ったような顔を見せる。"

show emicas frown_up
with charachange


emi "いつもと違う感じがするかと言われたらそうでもないんだよね"




hi "うん？　どういう意味だ？"

show emicas awayfrown
with charachange



emi "これってどこがデートなのかな？"




emi "実際、普段やってることと同じじゃん"



emi "でも前は友達として一緒にお昼ご飯食べたりしてて、今はそれよりもっと深い関係になってるんだもの。なにか違う風に感じるのがあたりまえじゃない？"


hi "その台詞、琳っぽいぜ"

show emicas happy
with charachange



"笑い声が漏れだして、笑美がにやりとする。"





show emicas closedsmile_up
with charachange


emi "あはは、確かに影響されちゃってるかも"

show emicas closedsmile
with charachange


emi "こういう事、前に琳と話し合ったことがあるんだ"


hi "俺について？　マジで？"

show emicas grin
with charachange


emi "ううん、違うの。ただ……こういう事について、ね"

show emicas neutral
with charachange



emi "琳は、『友達』から『彼女』になるっていう役割の変化は、ほとんどの場合気まぐれに見えるって思ってるの"




emi "まるでその二つに実際の違いなんてないみたいに、ね"



hi "違うことなら、少なくともひとつは思いつくぜ"




hi "友達とこんなにいっぱいキスはしないだろ"





show emicas blush
with charachange


"笑美が顔を少し赤らめて笑うのは今日で二度目だ。"

show emicas closedsmile
with charachange



emi "うん、たしかにそうかも"



hi "だろ。俺はこういう事にかけてはいつも正しいんだぜ"

show emicas weaksmile_up
with charachange



"笑美は目を丸くすると、くすくす笑い出す。"




emi "あはは、じゃあ君はすっごく頭がいいんだね？"





"俺は同意してうなずく。"



hi "まぁな"


hi "武藤先生もそう言ってたしな。俺が卒業後に科学系の進路を選ぶべきだって思ってるみたいなんだ"

show emicas neutral
with charachange


"笑美が驚いたような顔をする。"



emi "へえ、ほんとに？"



hi "あぁ。俺もマジでそうするかもなって思ってるんだ"



"実際、それは考えれば考えるほど魅力的なアイディアだった。"



"後でもっとよく調べておこうと、そう俺は心の中で思った。"




hi "笑美は卒業後の進路はなにか考えてるのか？"


hi "走るのを続けるとか？"

show emicas awayfrown
with charachange


"なにかに少しためらっているかのように、笑美は肩をすくめる。"


show emicas frown
with charachange


emi "う～ん、どうだろ。もしあたしの実力が十分で、ぴったりなチームがあったらそれでもいいかも？"



hi "つまりはっきりとは決めてないんだな？"


show emicas neutral
with charachange


emi "ほんとの事いうと……あまり真剣に考えてないんだよね"


hi "そうなのか？"


hi "そろそろ考えておいた方がいいんじゃないか？　卒業までそこまで時間があるわけじゃないし"

show emicas awayfrown
with charachange


"笑美が少し神経質そうにもじもじする。"


emi "うん、そうなんだけど……でもまだ時間は十分にあるよね？"

show emicas neutral
with charachange


emi "それに、今はほかの事で頭がいっぱいなの"

show emicas grin_up_close
with vpunch



"笑美の目がいたずらっ子のように光り、俺は突然自分が背後の木に見事に押し付けられているのに気づく。"



show emicas smile_up_close
with charachange


emi "たとえば、これが本当のデートだってはっきりさせるとかね。どう？"

show emicas closedsmile_up_close
with charachange



emi "というか、キスもしなかったら、そんなのデートじゃないでしょ？"



hi "そうかも……むぐっ"




"いちごとカレーのミックス味。いい組み合わせとは言えないけど、俺には気にならない。"


show emicas grin
with charadistant



"笑美は俺の足の上に座り、またくすくすと笑う。"





emi "ほら。これなら科学的にも立証されるでしょ？"



"俺の頭に、武藤先生が神妙な顔をしてうなずきながらなにかのリストにチェックを入れているすごく変な光景が思い浮かぶ。"




"そのせいで俺はつい笑い出してしまう。"

show emicas neutral
with charachange


emi "むむ、キスの直後に笑われるのなんて見たのはこれが初めてだけど"





emi "これってバカにされたと思うべきかな？"


hi "へ？　あ、いや違うんだ"


hi "もちろん、科学的に証明されたさ"

show emicas happy_up
with charachange


"顔を輝かせる笑美に見つめられて、脳みそをまともに働かせるのがどんどんつらくなってくるのを感じる。"





emi "よかった！"


"教師たちがクリップボードを使っている想像で頭がいっぱいだった俺は、この時点で笑美にカレーパンの残りを盗まれているのにようやく気づく。"



hi "おい！"

show emicas blush
with charachange



"笑美は潔白だと言わんばかりの顔をするけど、俺のパンの最後の一片を口の中に詰め込んだばかりのこの状況では役に立っているとは言えない。"




emi "んふ？　ほめん、ふぁまんでふぃなふて"






hi "どろぼう！"

show emicas neutral
with charachange



"その言葉への笑美の反応は、単に肩をすくめるだけだ。"






hi "女の武器を使って俺を惑わしたな！"



"べつにそこまで空腹だったというわけではないけれど、それでもこの点は突っ込んでおくべきだと感じる。"


show emicas pout
with charachange


"笑美は『女の武器』という言葉に面食らったような顔をしていたけど、少しの間考え込むと納得のいったような表情になる。"


show emicas angry_up
with charachange


emi "全然そういうことじゃないでしょ！"

show emicas frown_up
with charachange




emi "君笑ってたじゃない！　女の武器なんて使ってたら笑いが起こったりしないはずだよ！"




"それに関してはなにも言い返せないな。"


hi "だからってお前が盗んだ事実は変わらないぞ"

show emicas happy
with charachange


"笑美は傷ついた風な俺の口調を聞いて笑い、冗談で小突いてくる。"






show emicas closedsmile
with charachange


emi "わかったわよ。じゃあこの即席麺をあげるね"


hi "冗談だろ？　あんなの糞まずいじゃないか！"


hi "言ってみれば、罰ゲームで食うようなもんだぞあれは！"




show emicas wink
with charachange



"俺の両脚の上に座る笑美がまた笑う。"




"……どっちも今ではすっかりしびれてしまっている。"


show expression im.Composite((295,1200), (0,0), "sprites/emicas/emicas_wink.png") as emicas:
    xalign 0.5 yanchor 0.5 ypos 1.13 subpixel True
    easeout 0.8 rotate -90
with None

show expression im.Composite((295,1200), (0,0), "sprites/emicas/emicas_blush.png") as emicas:
    xalign 0.5 yanchor 0.5 ypos 1.13 subpixel True
    easeout 0.8 rotate -90

with Dissolve(0.2)
with Pause(0.6)

hide emicas
with vpunch



"しびれをやわらげようとして足を引くと、思いもよらずその上にいた笑美をよろけさせてしまい、笑美は『わわっ』とびっくりしたような声と同時に横に転がり落ちる。"







hi "おっと！　わるいわるい"


hi "足がしびれちゃってさ"


"笑美は地面の上にころがったままでくすくす笑っている。"


"少しふらつきながら立ち上がると、足に感覚が戻ってくるのがわかる。"



"あたりの風景を見回していると、まだ立ち上がっていない笑美の姿に気づく。"


scene ev emi_parkback:
    xalign 0.5 yalign 0.5 zoom 1.1 subpixel True
    ease 10.0 zoom 1.0
with locationchange



"笑美の髪の毛は頭の周りに無造作に広がり、腕は左右に投げ出されて、口からは笑い声があふれ出てきている。"






"笑美の全てが、このひとつのイメージに凝縮されているかのようだ。"



"活力、精神、そして子供っぽいくすくす笑い。"





"一緒に芝生に寝転がりたいという衝動が心の底から意識の上へと湧き起ってくる。もちろん俺は、他になにをするよりもそうするのが楽しいだろうと確信している。"




"でも残念なことに日はすでに暮れていて、たぶんもう寮に戻らなくてはいけない時間だ。"




"笑美はここで夜通し過ごしたって大丈夫だろうけど、俺には耐えられる自信がない。"



"それに、宿題をしなくちゃいけない。"


"大学進学を考え始めた矢先に宿題をサボるなんて、矛盾してるだろう？"


"俺は笑美を引っ張り上げるために腕を伸ばす。"




hi "そろそろ帰らなきゃ"


show ev emi_parkback_frown
with charachange



"笑美が渋い顔をする。"




emi "そうだね"


scene bg suburb_park
with locationchange

show emicas weaksmile_close:
    center
    ypos 1.2
    easein 0.5 ypos 1.0
with charaenter



"笑美は俺が差し出した手をつかみ、俺はその手を引っ張り上げて笑美を抱き留める。"



"笑美を抱きしめていると、堪えきれず今度は俺のほうからキスをする。"



hi "帰らなきゃいけないのがほんとに残念だな"


show emicas closedsmile_close
with charachange



emi "うん、ほんとにね"


show emicas grin_up_close
with charachange



emi "でも早く学校に戻らないと、問題になっちゃうかもしれないからね"



"笑美がふざけてわき腹をつついてくる。"


show emicas wink_up_close
with charachange



emi "それに、宿題しなくちゃいけないんでしょ"




hi "残念だけど、まったくその通りだ"


hide emicas
with charaexit



"俺は笑美の肩に手を回し、学校へと戻り始める。歩く間に話題は次から次へと移り変わり、その度に笑いが起こる。"







"走る事から、学校の事、そして食堂の職員の奇妙な体臭の事まで、あらゆることを。"







stop ambient fadeout 2.0

scene bg school_dormext_full
with locationskip




"俺たちはあっという間に女子寮の建物の外に到着する。"




show emicas closedsmile at center
with charaenter


emi "じゃあ、もうそろそろいくね"




hi "ああ、そうだな"


show emicas grin_up
with charachange



"笑美がまた、あの茶目っ気を含んだ笑いを見せる。"





emi "あたしがいなくても生きていけそう？"



"俺は笑い出してしまう。"




hi "まあどうにかなるだろ"


show emicas pout_up
with charachange




emi "ひっどーい！　こういうときは『君とまた会えるのを今か今かと待っているよ』みたいなセリフを言わなきゃだめでしょ？"







hi "いや、全然そう思わないね"


show emicas closedsmile_close
with characlose

show emicas weaksmile
with charadistant


"笑美は俺を引っ張って軽くさよならのキスをし、一歩下がると意外なくらい照れくさそうな顔をする。"






emi "夕ご飯、ありがとね"


emi "ほんっとうに楽しかったよ"

show emicas closedsmile
with charadistant


emi "冗談じゃなくて、ほんとにさ"


hi "俺も楽しかったよ"


hi "またそのうち、一緒にどこか行こうぜ"

show emicas happy
with charadistant



"笑美が俺の無感情な話し方に笑い、そしてうなずく。"



emi "じゃあまた明日、朝早くに"

show emicas wink
with charadistant


emi "今日食べたあのパンの分を走らなくちゃだめだもんね"



hi "わかってるって。お前がそのパンほとんど食べちまったのは置いといてな"


show emicas smile_up
with charadistant



emi "うんうん、置いといて"


show emicas grin_up
with charadistant


emi "じゃあまたね、久夫！"

stop music fadeout 3.0

show emicas invis:
    xpos 0.6
with dissolvecharamove

hide emicas
with None


"笑美が寮内に戻ろうと振り返った時、俺はどこか変な事に気づく。"


"今まで気づかなかった事に自分自身驚くほど、それは妙だった。"




"笑美が左足を主に使いつつ、わずかに足を引きずって歩いている。"




play music music_pearly fadein 8.0


hi "おい、笑美！"

show emicas invis at tworight
with None

show bg school_dormext_full at bgleft
show emicas neutral at center
with dissolvecharamove


emi "うん？"


hi "足、大丈夫か？"

show emicas awayfrown
with charachange


"笑美が戸惑うような顔を見せる。もしくは、そう見せようとしているのか。"

show emicas frown
with charachange


emi "なにを言ってるの？"


hi "お前の右足だよ。引きずってるじゃないか"



show emicas blush
with charachange

show emicas frown
with charachange


"笑美の顔にほんの一瞬、なにかを懸念するような表情が浮かぶ。"


"俺に気づいて欲しくなかったのか、俺が気づくと思っていなかったのか……いや、笑美自身が気づかなかっただけだと思いたいけど。"

show emicas neutral_up
with charachange



emi "ああ、それね"



"笑美はなんでもないように肩をすくめる。"

show emicas awayfrown
with charachange


emi "ピクニックのあいだに義足の軸が少しずれちゃったみたいなの"


show emicas wink
with charachange


emi "なんでそうなっちゃったのかは、もちろん全然わからないんだけどね"




"俺の脳裏に木の下で押さえつけられた場面が浮かぶ。"



hi "あ～"


hi "そう言ってくれよ！　ちょっと立ち止まって直しておけばよかったのに"


"笑美が手をひらひらと振る。"

show emicas smile_up
with charachange


emi "ううん、そんな気にするような事じゃないよ"

show emicas weaksmile_up
with charachange


emi "心配しないで。ね、久夫？"

show emicas closedsmile_up
with charachange


emi "大丈夫だから"





label jp_choiceE17:
menu:
    with menueffect
    "俺だけでなく、笑美自身にも言い聞かせているように聞こえるのはなぜだろう？"
    "笑美にさらに聞いてみる":





        return m1
    "話を切り上げる":


        return m2


label jp_E17a:



hi "本当に大丈夫なのか？"


hi "階段を上る前に調整しなおしたほうが良いんじゃないか？"


hi "そうじゃないと、怪我しちゃうかもしれないだろ？"

show emicas awayfrown_up
with charachange


emi "だから大丈夫だって言ってるでしょ、久夫"

show emicas frown
with charachange


emi "ほんとにほんと。心配しないでも大丈夫だってば"

show emicas weaksmile
with charachange


emi "今までにこういう経験は何度もあったしね"


hi "まぁ、そうだろうけどさ"


"笑美が俺を安心させるようにと笑う。"




show emicas grin
with charachange



emi "正直、あたしの事を気にしてくれてうれしいよ、久夫。でもほんと、大丈夫だからね"


label jp_E17b:




"まあ、笑美は大丈夫なんだろう。"




"もしそれが大変な事なら、ちゃんと言ってくれると思うし。"




"それに、この話を持ち出し続けると嫌がるかもしれないしな。"



label jp_E17x:

show emicas smile
with charachange


emi "じゃあ今度こそ、そろそろ行くね"

show emicas wink_up
with charachange


emi "あたしを引きとめようって作戦は残念ながら大失敗でした！"


hi "はいはい、そうだな"


hi "さよならをいうのを少しでも遅らせたかったんだよな、きっと"


"笑美の顔からまた笑顔がこぼれる。"

show emicas happy_up
with charachange


emi "おやすみ、久夫"


hi "おやすみ"

hide emicas
with charaexit

stop music fadeout 5.0



"足をひきずりながら笑美が寮内へ入っていくのを見ながら、大丈夫だと言い張っていたにも関わらず、俺は笑美の無事を願っている自分に気づく。"





"まあ、この初デートは成功と言えるんじゃないか。"







"まったく、木に押し付けられて笑美にキスをされて終わった日を悪かったなんて言えるわけないだろ？"





"俺は通路で健二に待ち伏せを食う事なく部屋へと戻れた事に心の中で感謝すると、宿題を始める。"



scene black
with dissolve



label jp_E18:

scene bg school_dormhisao
with locationchange

play music music_night fadein 5.0


"朝が来るのがとてつもなく早く感じる。"



"昨日の夜なかなか眠れなかったなんてことは何の救いにもならない。"







"とにかく考えるべきことがたくさんありすぎた。思考がとどまることを知らなかった。"





"とどまるどころか、屋上、公園、その他もろもろの場面全てが何度も何度も記憶によみがえってきた。"






"今でも俺の心の片隅には、これがなにかの冗談じゃないかという猜疑心が残っている。"




"笑美と競技場で顔を合わせたら、昨日は何事もなかったかのような態度を取られるんじゃないかとか。"






"そんな考えを頭の片隅に追いやり、ランニング用の服に着替えてドアを開ける。"




scene bg school_track
show emi basic_grin_gym at center
with locationskip



"笑美はいつもの笑顔で俺を待っている。"


show emi basic_annoyed_gym
with charachange



emi "おっそーい！"


show emi basic_closedgrin_gym
with charachange


emi "というより、少なくとも今日は来るのが早くなかったね"

show emi excited_hesitant_gym
with charachange


emi "ちょっと疲れてる？"



"俺は自分が、何かに後悔したときのように、後頭部をさすっていることに気づく。"





hi "んー、まぁ多分そんな感じだな"



hi "いろいろと考えごとがあってさ"



show emi basic_closedgrin_gym
with charachange



"笑美が俺のちょっと控えめな表現に笑い出す。"





show emi basic_grin_gym
with charachange



emi "そうなんだ。あたしもよく眠れなくてさー"


show emi excited_proud_gym
with charachange



emi "ほんとは久夫が早く来てなくて良かったって思ったの。だってあたしも早く来てなかったからね"





"笑美も俺と同じような考え事で眠れなかったんだろうか？"



"眠りながら泣く笑美の顔が頭をよぎる。"






hi "なに考えてて眠れなかったんだ？"

show emi sad_shy_gym
with charachange


"笑美は口ごもるそぶりを見せるけど、俺がいぶかしんでいるのに気づくとすぐさま無理に笑顔を作る。"


show emi sad_grin_gym
with charachange


emi "別にたいしたことじゃないよ"



"どう見てもなにか隠している。"



"問題は、俺がそれに関してもっと切り込むべきなのか？　ということだ。"


"間違いなく、ここしばらく笑美を悩ませていることがなにかしらある。"



"俺は笑美の助けになりたいけど、単なるお節介だと思われてしまうんじゃないか？"



"とにかく、俺が笑美を気にかけていることは伝えなくちゃな。"


hi "本当にか？"


hi "もしなにか悩み事があれば、いつでも解決するのに手を貸すぜ"

show emi basic_closedhappy_gym
with charachange


"笑美はそれを聞いて笑うけど、いつもの笑い方ではない。冷酷とも見えるような、鋭さがそこにある。"

show emi sad_grin_gym
with charachange


emi "解決する？"


emi "久夫、あたしにはそれが解決できることなのかも分からないの"


"ぞっとするような笑顔が笑美の口にうかぶ。"


"それはまるで、諦めきったような笑顔だった。"

show emi sad_pout_gym
with charachange


emi "久夫があたしを助けるなんて、どうせ出来っこないよ"


"その言葉が心に突き刺さる。"


"俺が傷ついたなんて笑美に言いたくはないけど、心が痛いのは事実だ。"


"笑美が辛いときに一緒に居てあげたいと俺が思ってるのに気づかないのか？"



hi "じゃあ、この件はここまでにしとくよ"




hi "だけど、もし後で気が変わって話したくなったら、いつでも待ってるからな"




hi "話したら楽になるかもよ"


show emi sad_shy_gym
with charachange



"笑美の瞳の奥で葛藤が渦巻いているのが見て取れる。"



"なにかを俺に言いたいのに、言ってしまっていいのかどうかが分からないように見える。"







hi "まあ、ひとまずこの事は置いとこうか？"







hi "とりあえず走ろうぜ"




"ランニングの話を持ち出すと、笑美の手に余る話だったさっきとは違い、笑美はいつもの状態に戻る。"








show emi basic_closedhappy_gym
with charachange


emi "そうだね！"

show emi basic_grin_gym
with charachange


emi "はやく柔軟体操しちゃいなよ、久夫！"

show emi excited_proud_gym
with charachange


emi "ちゃっちゃと始めるよ！"

play ambient sfx_emipacing

hide emi
with easeoutleft

stop ambient fadeout 3.0


"今まで俺が慣れてきたのを遥かに越えるスピードで、笑美が弾丸のように走り出す。"

scene bg school_track_on
with locationchange

scene bg school_track_running
with Dissolve(2.0)


"それでも俺は笑美の後について行こうとしながら、向こう見ずに自分の限界に挑戦している。"



"そうしていると、俺の心臓がもはや何の問題でもないような自由な気持ちになる。"







"自分で限界と思い込んでいたレベルを超えて動ける喜びに満たされ、笑い出したい気分だ。"



"俺にやりすぎを禁止したナースの忠告が頭に浮かんでくるけど、そんなのはどうでもいい。"



"朝のランニングのような些細なことで心臓発作のリスクをあえて冒すような気分になるなんてのは、俺の性格からかけ離れている気がする。"




"でも本当にそうなのか？"




"というよりも、そうであるべきなんだろうか？"



"そりゃあ、俺は弱っちい心臓を抱えている。"


"俺の心臓が笑美の発揮できるようなスピードとスタミナに耐え切るなんてのは無理な話だ。"


"だけど、たとえ健康な心臓を俺が持っていたとしても笑美みたいに走れるようになるとは思えない。"

stop music fadeout 6.0


"最終コーナーを曲がるあたりで俺の足が抗議の悲鳴を上げ始めるけど、俺は初めてそれを無視する。"




"むしろ最後は全力疾走で終わらせようと加速し、笑美に追いつきそうになる。"


"もちろん、以前では起こりえなかったことだ。"


"それでいて俺の気分は驚くほどに良い。"


"そりゃ脚は火が付きそうなように感じるし、正しいフォームを続けるのが難しくなっている。"


"だけど、今日はなにかが変わったように感じるんだ。"



"そしてそれは全て、ゴールラインで俺を待つ、笑顔のこの少女のおかげなんだ。"

scene bg school_track_on
show emi basic_grin_gym at center
with locationchange

play music music_emi fadein 1.0


hi "いつもよりペースが少し早く感じたぜ"


"俺の言葉に、笑美は肩をすくめてニヤリとする。"




show emi excited_proud_gym
with charachange


emi "手加減してたと思われるわけにはいかないでしょ？"



show emi basic_closedgrin_gym
with charachange


emi "でもちゃんとついて来れたじゃない"



hi "あぁ、お前が居なかったらこんなことできなかっただろうな"


show emi basic_confused_gym_close
with characlose


"ランニングし終えてもまだ続く高揚と押し寄せる感謝の念に、俺は思わず笑美をぎゅっと抱きしめる。"




hi "ありがとう"


hi "いやマジでさ。ただ口先だけでじゃないぜ"


hi "笑美には借りができたな"

show emi basic_hes_gym_close
with charachange


"笑美は俺の言葉にあわてたようで、落ち着かなさそうにもじもじしている。"







emi "バカなこといわないでよ、久夫"


show emi basic_grin_gym_close
with charachange






emi "誰かが君をここまで引っ張ってこなくちゃならなかったでしょ？"





show emi basic_closedgrin_gym_close
with charachange



emi "それに、久夫があたしのためになにもしてないってわけじゃない。でしょ？"


show emi basic_grin_gym_close
with charachange


emi "あたしはランニングパートナーが必要だったんだよ。覚えてる？"

show emi basic_shock_gym_close
with charachange



"俺は笑美を離すことなくしっかりと抱きとめて頭を振る。もじもじするのを止め、頬をさっと赤く染めてこちらをまっすぐに見つめる笑美はいつもの様子と違っていた。"



hi "いや、その言葉は正しくないな"


hi "たしかにランニングパートナーが欲しかったかもしれない。けど、必要ではなかったんだ"



hi "もし俺が学園祭の後にまた来ることがなかったとしても、笑美は走り続けてただろ？"




hi "でも逆の立場だったら、そうはならなかった"


hi "学園祭の前にはほんの数回、どうにかやってみたけどさ"


hi "笑美が居なかったら、その後は一回も走ろうって気にはならなかっただろうな"

show emi basic_closedgrin_gym_close
with charachange


"笑美は笑顔を見せると、俺の胸を人指し指でつく。"

show emi excited_proud_gym_close
with charachange


emi "久夫のなまけもの～"



hi "おいおい、お前を褒めてんだぞ俺は！"

show emi sad_grin_gym_close
with charachange


emi "あはは……どういたしまして、なのかな"






hi "いつかこの恩は返すぜ"

show emi basic_hes_gym_close
with charachange


emi "あ～、うん。え～と……"

show emi basic_closedgrin_gym_close
with charachange



emi "ねえ、別にそんなのいいってば"


show emi basic_happyblush_gym_close
with charachange



emi "あたしは久夫のことが、まあ一応好きなんだし"


show emi sad_grin_gym_close
with charachange


emi "久夫と一緒に朝に走れるのはさ、あたしにとってもそんな悪い話じゃないし……"




"あんなにいっぱい賞賛されているにも関わらず、笑美は感謝されるのには慣れていないみたいだ。"






"それ以上言いたいことが見つからず、俺たちの間に静寂が訪れる。"




"笑美の息遣い、汗で湿った服、そして香りにふと気づく。"


"これが笑美じゃなかったら、単に臭いと感じるだけだろう。"



"でもこれが笑美の香りだと思うと、他のなによりも笑美らしく思える。"




"笑美の肌は汗でしっとりと冷え、一筋の風が通ると鳥肌が立ち始める。"


show emi excited_amused_gym_close
with charachange


"俺はほとんど無意識のうちに体を屈め、すでにこちらに顔を寄せていた笑美と口付けをかわす。"







"笑美の唇は柔らかく、キスしているとき嬉しそうに吐息をもらす振動が口から俺へと伝わってくる。"









"今この瞬間の全てが、驚くほど正しい。俺たちはお互いが完璧に調和している。"




show emi basic_grin_gym_close
with charachange



"キスを終え、俺はようやく笑美を抱きしめていた両腕を解き元の姿勢に戻る。"





show emi basic_closedgrin_gym_close
with charachange


"笑美は暖かい笑顔を俺に向け、そしてまたくすくすと笑い始める。"

show emi basic_closedhappy_gym
with charadistant



emi "ほら、行こうよ久夫。ナースくんに見てもらいに行かなきゃ"


stop music fadeout 1.0


"そしてそれは起こる。"




show emi basic_closedhappy_gym:
    ease 0.25 ypos 1.05
    ease 0.25 ypos 1.0
with None

show emi excited_sad_gym:
    ease 0.25 ypos 1.05
    ease 0.25 ypos 1.0
with Dissolve(0.25)


"振り返って歩き始めようとする笑美が、キャッと小さい悲鳴をあげて前につまずく。"


hi "笑美！"

play music music_rain fadein 2.0

show emi excited_sad_gym_close
with characlose



"笑美を支えようと急いで駆け寄ると、昨日と同じ足をかばっているのに気づき、心配になる。"





hi "お前の足……"

show emi basic_hes_gym
with charadistant


"笑美はパニックに陥ったかのように近づいた俺を押しやる。"




emi "大丈夫だってば！"


"それを聞いた俺の表情が傷ついたように見えたようで、笑美はすぐさま謝ってくる。"


show emi basic_shock_gym
with charachange


emi "ごめん！　ごめんね！"



emi "あんな風に突き放すつもりなんてなかったの！"

show emi basic_closedsweat_gym
with charachange


emi "あたしはただ……"


"笑美はなにかをいうべきかどうか躊躇っている。"

show emi sad_depressed_gym
with charachange


emi "本当になんでもないの"





hi "大丈夫だよ、そんなに気にするなって"




"すっかり取り乱した笑美を見て、俺は今の出来事全てを流そうと心に決める。"



"それでも腹の奥底にある冷たい感情は消えてくれそうにない。"






"俺が笑美を助けようと踏み込んだ時、笑美は俺を突き放したんだ。"



"しかし今は笑美のことに集中しようと、笑顔でそんな考えを頭の片隅に追いやる。"


hi "ただ笑美に怪我をして欲しくなかった。それだけさ"

show emi sad_pout_gym
with charachange


emi "あたしのことは心配しなくていいからね。ほんとに"

show emi sad_grin_gym
with charachange


emi "あたしは大丈夫だから！"



"ああ、お前はそう言うだろうけど、でも俺は信じてないよ。"


label jp_E18a:



"なんで問題があっても話してくれないんだ？"


"まるで俺が助けになろうとすることで笑美が不機嫌になるみたいだ。"


"それを俺はどう受け止めるべきなんだ？"



label jp_E18b:



"なにがあっても俺はお前を気にかけ続ける。昨晩なにも言わなかったことが、今日につながったのではないかという罪悪感を抱いてしまう。"





"少なくとも、どうしたのか尋ねておくべきだった。"




"そうしていたら笑美は昨晩も今日と同じような反応をみせていただろうか？"





"今となっては知るよしもない。"

label jp_E18x:

stop music fadeout 2.0

scene bg school_nursehall
with locationskip


"ナースの医務室の前に到着した時もまだ、俺は競技場でさっき起こったことを理解しようとし続けていた。"




"笑美はノックしようと腕を持ち上げ、ためらってから振り返り、気がとがめたような笑顔を俺に向ける。"





show emi sad_grin_gym:
    yalign 1.0 xanchor 0.5 xpos 0.47
    easein 0.5 center
with charaenter



emi "ねえ、ちょっとお願いしていい？"



hi "もちろん"

show emi excited_proud_gym at center
with charachange



emi "ナースくんに、後で行くからって伝えてもらえる？"


show emi basic_grin_gym
with charachange




emi "授業が始まる前にやらなきゃいけないことがあったって……今思い出したの"







show emi sad_grin_gym
with charachange


emi "だからホントにすぐ行かないといけないの"

show emi sad_shyblush_gym
with charachange



"俺が間近で見つめると、見つめられた笑美はそわそわする。"



"こりゃあ間違いなく、ナースを避けているだけだな。"


"あの足か……"



"まあいいか。助けになるって言ったんだし、そうしよう。"




"でも日が変わる前には絶対ナースのところに行かせるぞ。"








hi "ああ、わかった。そう伝えておくよ"


show emi excited_smile_gym
with charachange



"笑美はクリスマスにポニーでももらったかのような表情を見せる。"


show emi excited_joy_gym
with charachange


emi "ほんとにありがと！"

show emi excited_amused_gym
with charachange


emi "久夫ってばサイコー！"


show emi excited_amused_gym_close
with characlose




"笑美の嘘に加担したごほうびにキスをうける。それだけで報われた気分になる。というか自分にそう言い聞かせている。"




hide emi
with charaexit


"笑美が足を引きずらないようにとても気をつけながら建物から出て行き、俺は医務室のドアをノックする。"




nk "ああ、久夫くん。入りなさい"




play music music_nurse fadein 1.0

scene bg school_nurseoffice
show nurse neutral at center
with locationchange



nk "笑美ちゃんと一緒じゃないのかい"


show nurse fabulous
with charachange



nk "また病気になってたりしないだろうね？"




"口調からいって、ナースは俺が『はいそうです』と言うとは思ってないだろう。"




hi "えーと、用事があるのを忘れてたから、行かなくちゃいけないって言ってました。でもあとで会いに来るそうですよ"


show nurse concern
with charachange


"ナースが憤慨したようにため息をつく。"



nk "ほんとに、あの子は……"



hi "はい？"

show nurse neutral
with charachange



nk "このところ僕を避けてるんだ"



nk "昨日来た時は入ってきたと思ったら義足も脱がずにすぐ出ていったんだよ。そして今日はこれだ"


"つまり、少なくとも笑美が心配させたくないのは俺だけじゃないってことか。"


"それは……良かったのかな？"



"それはともかく、笑美の足のことは伝えておいた方がいい気がする。ナースに嘘をついておくとは言ったけど、笑美は本当にナースに診てもらわなきゃだめだ。"




hi "その件ですけど、今日の笑美はひどく足を引きずってたんです"




hi "昨日の夜もそうでした"


show nurse concern
with charachange



"『昨日の夜』という言葉にナースは眉をひそめる。"



nk "で、昨日の夜に君たち二人はいったい何をしてたんだ？"




hi "俺たち、その、デートしてました"


show nurse fabulous
with charachange


"驚いたかのようにナースの眉が持ち上がる。"


nk "本当かい？　それは興味深い"



hi "えっ？"

show nurse neutral
with charachange


nk "あ、いやなんでもないよ"


"ナースは考え込むような眼差しになり、そして俺に向かってニヤリと笑う。"

show nurse grin
with charachange



nk "久夫くんの彼氏としての魅力かなにかを使って、笑美ちゃんを今日中にここに来させることはできないかな？"




hi "もちろんできますよ！"


hi "もともとそのつもりでしたからね"


hi "本当は足を怪我しているのに、そうじゃないって振りをしてるだけだと思うんです"

show nurse neutral
with charachange



nk "ふむ、そうだね。あの子はそういうことをするから"




nk "残念だけど走るのはやめさせないといけないな"



hi "本気ですか？"

show nurse concern
with charachange



nk "僕だって言いたくはないけど、足を引きずるほど悪い状態ではね……"




nk "その判断をする前に、僕自身が直接診てみないといけないけど"



hi "なるほど"



"笑美が、走るのを禁じられる？　冗談じゃない。"





"走れない笑美なんて、生きていけるかどうかも怪しい。"




"調子が悪いのを一切認めたがらないのも無理はない。"




hi "そうですね、ちゃんと来させるようにします"





show nurse neutral
with charachange



nk "そうしてくれ。ああ、それと忘れる前に……"


show nurse grin
with charachange



"ナースは俺に再び笑顔を向けるけど、今度はどことなく脅しのように感じる。"




nk "僕が久夫くんの処方されている薬の種類を知ってること、忘れないでくれよ"



show nurse neutral
with charachange



nk "笑美ちゃんに下手な真似はしないこと。いいね？"




"おお。しかも真剣に見える。"



hi "わかりました"



hi "笑美は傷つけません。夢にも思いませんよ"


show nurse grin
with charachange


nk "よろしい！"

show nurse fabulous
with charachange


nk "君がいなくなるのはいやだからね"





hi "はい？"

show nurse grin
with charachange


nk "お亡くなりになるって意味さ"



show nurse concern
with charachange


"彼は不満げに眉を少しひそめる。"



nk "口に出すと微妙だったな……"


show nurse neutral
with charachange



nk "まあ、とにかくだ"


show nurse grin
with charachange



nk "１時間目に遅れる前にさっさと行きなさい！"




nk "やることがあるんだろ。しっしっ！"


stop music fadeout 6.0



"部屋を出る時、ナースが携帯電話を引っ張り出して番号を押しているのに気づく。"


show nurse concern
with charachange



nk "芽衣子、娘さんがまたやらかしたよ……"





"さっさと部屋に戻ったほうが良さそうだ。さもないと本当に遅刻してしまう。"




"まてよ、ナースに脈を測ってもらうんじゃなかったのか？"





label jp_E19:

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell


"お昼のチャイムが鳴り、午前の授業中に陥ったぼんやりとした感覚を振り払う。"




"昨日の夜にあまり眠れなかったのと、今朝のランニングでペースを上げていたのが合わさって、少し疲れが溜まっていた。"



$ renpy.music.set_volume(0.15, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

scene bg school_staircase1
with locationskip



"それをものともせず、俺は屋上への階段を一段飛ばしで駆け上がっている。"





"友人と一緒にお昼を食べる楽しみに加えて、今ではわくわくするような興奮も感じている。"



play sound sfx_door_creak
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene bg school_roof
with locationchange



"確かに笑美も琳も俺の友達だけど、でも今の笑美はそれ以上の存在になったのだから。"



"まるでずっとそこを動かなかったかのように、琳が屋上のいつもの場所に戻っている。"


scene ev rin_roof_boredom
show hisao rin_roof
with locationchange




hi "もう良くなったみたいだな？"



show ev rin_roof_surprised
with charachange



"俺の呼びかけに琳はただ眉を上げるだけだ。"



rin "良くなったって何と比べて？"

play music music_rin fadein 6.0



hi "いや、昨日よりは気分がましになったかって"


show ev rin_roof_nonchalant
with charachange



"俺の質問を聞いて、琳は真剣に考えこむ。"





rin "なんとも言えないな"




rin "昨日のいくらかは割といい気分だったかもしれない気がするけど、なにもかもぼんやりしてるんだ"





hi "風邪薬を飲み過ぎたか？"


show ev rin_roof_doubt
with charachange



rin "うーん、寝てた。それって普段ならすごくいいことなんだよ"


show ev rin_roof_boredom
with charachange


rin "だけど寝てるのがどんな感覚なのか思い出せないんだ。だってその間は意識を保ってないからね"




rin "ほんとにやっかいなんだ"


show ev rin_roof_nonchalant
with charachange



rin "でも、もし寝てる時の気持ちよさを知ってしまったら、もう眠らないかもしれない"






rin "でもそう努力し続けることで私は自分が疲れすぎないようにしているのかもね"




hi "永遠の謎のおかげで、夜も眠れ続けていられるってやつか？"


show ev rin_roof_boredom
with charachange




rin "謎というのとは違うかな。不可解、って言う方が近いかもしれない"





hi "なるほどな"





"いや、全然なるほどじゃない。琳が何を言っているのか見当もつかない。でもまあ、理解できることの方が少ないから別にいいか。"




show ev rin_roof_doubt
with charachange




rin "眠ってるときの感覚、思い出せる？"






rin "たとえば昨日、昨日寝てた間どんな風に感じてたか覚えてる？"





hi "あー、実は昨日あまり眠れなくてさ"


show ev rin_roof_nonchalant
with charachange


rin "ふむ"


rin "もしかしたら潜在意識のなかで記憶が残ってるからかもしれない"


hi "ホント言うと、笑美のことが心配だったからだと思うんだ"

show ev rin_roof_surprised
with charachange


rin "笑美は十分自分で自分の心配をしてるんじゃない？"




"考えたこともなかったけど、それを聞いて思案させられる。"




hi "たしかに。でも助けが必要になったとして、笑美は助けを求めるか？"


show ev rin_roof_doubt
with charachange



"琳が顔をしかめるのを見て、俺は眉を上げる。まともな答えが得られるのか？"




rin "多分しないね。なにか笑美が助けを求めなきゃいけないことでもあるの？"




hi "まずはそうだな、脚とかさ"



"この返答は琳の興味を引いたようだ。"

show ev rin_roof_disgust
with charachange



rin "脚？"


hi "怪我してるんだよ。だけどナースに見てもらおうとしないんだ"




"琳は否定するように頭を振る。"



show ev rin_roof_doubt
with charachange



rin "君がそうさせなきゃ"


show ev rin_roof_nonchalant
with charachange



rin "笑美が私を授業に行かせるようにね。それが笑美のためだから"






rin "そうでもしないとまた脚をなくしちゃう。そんなのおかしすぎるよ"




rin "二度も同じものをなくすなんて"


show ev rin_roof_doubt
with charachange


rin "しかも、そもそも取り戻すことなんてできないものだよ"




rin "義足を使うのが取り戻すと言えるなら話は別だけど"


show ev rin_roof_nonchalant
with charachange




rin "でもそっちの失うっていうのは意味が違うよね？"





hi "そうだろうな"

show ev rin_roof_boredom
with charachange



rin "うーん。不思議……"

stop music fadeout 0.5

show emi rin_roof
with charaenter



emi "なにが不思議なの？"


scene bg school_roof
show emi basic_grin at center
with locationchange



"笑美が俺たちにこっそり近づいていたみたいだ。でも琳は特別驚いたような素振りを見せない。それ自体特に驚くようなことじゃないんだろう。"


show bg school_roof at bgleft
show emi basic_grin at twoleft
with charamove

show rin basic_deadpannormal:
    tworight
    ypos 1.25
    easein 0.5 ypos 1.2
with charaenter


"慣れた様子で琳が上半身を前に投げ出し、その勢いでバランスを取りながら姿勢を正して座る。"

show rin basic_absent:
    ypos 1.2
with charachange



hi "脚、どんな調子？"


show emi sad_annoyed
show rin basic_awayabsent
with charachange



"呼びかけに対し、笑美は眉をひそめて少しにらみつけてくる。"





emi "大丈夫じゃん、たぶん"


show emi sad_shy
with charachange


emi "べつに心配するほどのことじゃないって"

show rin basic_absent
with charachange



hi "それはナースに言えよ"




hi "言っとくけど、かなりしつこく笑美に会いに来てもらいたがってるぞ"


show emi sad_pout
show rin basic_awayabsent
with charachange


"まるで俺から外出禁止を言い渡されたかのように笑美はふくれっつらをする。"



emi "ナースくんが心配しすぎなだけ"


show emi basic_grin
with charachange



emi "たいしたことないよ、ちょっと痛い感じがするだけで"





"怒りで空を仰ぎそうになるのを押しとどめようとする。"


show rin basic_absent
with charachange


hi "もしなんでもないんだったら、ナースに診てもらったってかまわないだろ？"


show emi basic_annoyed
show rin basic_awayabsent
with charachange


"笑美がいぶかしむように目を細める。"



emi "そう言えって頼まれたの？"


show rin basic_absent
with charachange



hi "ああ、まあ、ちょっとは"




hi "でも大事なのはそこじゃない。どっちにしてもナースに診てもらうように言ってたさ"




hi "笑美がひどい怪我をしてるのに何もせずにいるなんて、そんなひどい話があるかよ"




hi "そのままにしていたらもっと悪くなるし、俺は笑美が怪我してるところは見たくないんだ。わかるだろ？"





hi "笑うなら笑えばいいさ。だけど俺はまあ、笑美に幸せで健康でいてほしいんだぜ"




show emi sad_grin
show rin basic_awayabsent
with charachange



"俺が言葉を発するたび、笑美の嫌がるような表情はだんだん消え去り、最後には少し恥ずかしそうな笑顔に変わっていった。"



play music music_daily fadein 4.0




emi "久夫にそういう風に言われたら、ナースくんに会いに行くしかないな"




show emi excited_proud
with charachange



emi "そうじゃなきゃ久夫はずっと心配し続けるだろうし、同じ事を何度も何度も言われる。でしょ？"


show rin basic_absent
with charachange


hi "そのとおり。ずっとうるさく言い続けるし、そうなればデートだって楽しめなくなるかもしれないぞ"





"俺は一人芝居を始めて、自分の役と笑美の役を代わる代わる演じる。"






hi "『久夫、料理の味はどう？』『笑美、ナースに会いに行け』"





hi "『久夫、今日はどうだった？』『笑美、ナースに会いに行け』"





hi "『久夫、あたし行くところまで行――』『{b}笑美、ナースに会いに行け{/b}』"






hi "ほらな？　楽しくないだろ"


show emi basic_closedhappy
show rin basic_awayabsent
with charachange



"俺が裏声で笑美の声を真似るのを聞いて笑美はクスクス笑い始め、優しく小突いてくる。"




show emi excited_amused
with vpunch



emi "あたしの声はそんな高くないわよ、バカ"


show rin basic_deadpan
show emi excited_circle
with charachange



rin "私はけっこう似てると思った"


with Pause(3.0)



"二人で琳をしばらく見つめた後、俺は吹き出してしまう。"



show emi sad_annoyed
show rin basic_awayabsent
with charachange




"笑美は気分を悪くしたふりをして、腕を組んで鼻息を荒くする。"


show emi sad_angry
with charachange




emi "二人ともほんとバカ"


show rin basic_absent
with charachange



hi "なんて酷いことを言うんだい、お嬢さん"





hi "よりにもよって俺をバカ呼ばわりするだなんて、唖然とするね"






hi "正直……その……どう考えればいいかわからないな"



show emi basic_annoyed
show rin basic_awayabsent
with charachange


"笑美は俺に向かって舌を突き出してくる。"


emi "意地悪っ"


show emi basic_grin
with charachange


emi "ところでさ、琳。美術部は最近どんな感じ？"

show rin basic_surprised
with charachange


"突然の話題変更に俺と同じくらい琳も驚いたようで、答えるまでに少し間があく。"

show rin basic_lucid
with charachange



rin "まあまあだと思うよ"


show rin basic_deadpancontemplation
with charachange


rin "野宮先生が私にもっと頑張れって延々と言ってきてるけどね"

show rin relaxed_nonchalant
with charachange


rin "でも先生は私のやり方を理解してないんだと思う"

show emi sad_annoyed
with charachange



emi "あの先生ちょっとキモいって、前から思ってたよ"


show rin basic_lucid
with charachange



"琳がその発言に対ししばらく考えこむ。"



show rin basic_awayabsent
with charachange



rin "今までずっと気づかなかったよ"


show rin basic_deadpancontemplation
with charachange



rin "でも普段は先生のことはあまり意識してないから、多分そのせいなのかも"




hi "部活は週に何回あるんだ？"



show emi basic_closedgrin
with charachange



emi "なに久夫、美術部に入るつもり？"


show rin basic_absent
with charachange


hi "は？　いやいや、もう入る部活は決めてあるんだ"

show emi excited_happy
show rin basic_awayabsent
with charachange


emi "ほんとに？　どれどれ？"


show rin basic_absent
with charachange



hi "うーん、まあ実際の所、部活ってほどでもないんだけど……"


show emi excited_proud
show rin basic_awayabsent
with charachange




emi "ああ、あのお茶会クラブに入部したの？"



show rin basic_absent
with charachange


hi "そうじゃなくて、その……科学部に入った……と思う"

show emi basic_confused
show rin basic_awayabsent
with charachange



"笑美がとても困惑した表情を見せる。"



emi "科学部なんてあったっけ？"

show rin basic_absent
with charachange




hi "えーと、いやなんていうか。部員は俺だけなんだ"



show emi basic_closedhappy
show rin basic_awayabsent
with charachange


emi "それは部活動って呼ばないよ、久夫。ただ部屋で座って本読んでるだけじゃないの"


hi "違うんだ。俺と武藤先生だけって言えばよかったか"


hi "今のところ生徒では俺だけって意味だ"

show emi basic_confused
show rin basic_lucid
with charachange


emi "武藤先生が？　ほんとに？"



"笑美はなにかに思い当たったみたいだ。"


show emi basic_happy
with charachange


emi "あー、それってもしかして昨日話してたこと？　武藤先生との話し合いってやつ？"



hi "そうそう。あれが最初の活動なんだと思う"


show emi basic_closedgrin
with charachange


"笑美がクスクスと笑う。"

show emi basic_grin
with charachange


emi "オタクっぽい"



hi "おい、俺が賢いのは自分でもどうしようもないんだ"



show emi excited_proud
with charachange


emi "何年か前なら手伝ってもらいたかったことがあったんだけどなぁ"


emi "久夫はもっと早く心臓発作起こしておくべきだったよ"


"俺は笑い出すと同時に、今まで自分の発作を笑うことが滅多になかった事に気づく。"



hi "まあ過ぎたことだな……"


show emi sad_grin
with charachange



emi "そうだね……"


play sound sfx_warningbell



"昼休みの終わりを告げる鐘の音が俺たちの会話を終わらせる。"



hi "さて、もう行かないとな"

show emi basic_grin
with charachange


emi "うん、そうみたいね"

show emi excited_amused:
    xpos 0.45
with dissolvecharamove



emi "ほら、一緒に行くよ琳"


show rin basic_surprised
with vpunch


"明らかにうとうとし始めている琳を笑美がバシッと叩く。"



show rin basic_deadpanupset
with charachange


rin "もうすこしだったのに"

show emi basic_closedgrin
with charachange


emi "ごめんね、でも授業に行かないとだよ"

show rin relaxed_nonchalant at tworight
with dissolvecharamove


rin "そうは思わないな。でも授業中に昼寝をすれば今度はもしかしたらつかめるかもしれない"


show rin relaxed_boredom
with charachange


rin "こういうことは場所を変えてみると時々うまくいったりするからね"


"笑美も俺も、何のことを話しているのか聞いてみるつもりはない。"

stop music fadeout 3.0
stop ambient fadeout 2.0
scene bg school_hallway3
with locationskip



"俺の教室の前まで来ると笑美は俺に軽くキスをし、琳を連れて廊下をそのまま歩いていく。"



show shizu behind_blank:
    tworight
    xpos 0.8
    easein 0.5 tworight
show misha perky_smile:
    twoleft
    xpos 0.2
    easein 0.5 twoleft
with charaenter


"教室に入ろうと振り返ると、静音とミーシャの二人組がいることに気づく。"

play music music_shizune fadein 1.0

show shizu adjust_happy
with charachange


shi "……"



"怒鳴り散らすような静音の手話を翻訳する間、ミーシャは笑い出すまいと努力をしているけど、我慢できずにいるみたいだ。"



show misha hips_grin
with charachange




mi "あなたがうまく友人を作り、関係を深めていっているのを見て、私たちは喜びを、それどころか感動すら覚えます――しかもあんな可愛い子とね、ひっちゃん～ ……"





"最後の部分はおそらくミーシャの付け足しだろう。"

show shizu basic_normal
with charachange


shi "……"

show misha hips_frown
with charachange




mi "それでも、公共の場での親密な行為が固く禁じられている事をここで謹んでお知らせしなくてはなりません――ほんとに？　それはがっかりだよ、しっちゃん――これは生徒手帳の行動規範第８項に記されています"






show shizu adjust_smug
with charachange


shi "……"

show misha sign_smile
with charachange



mi "しかしながらこの場合、あなたたちは校則を知らなかったので、私たちは寛大な処置をとろうと考えています……"



show shizu behind_smile
with charachange


shi "……"

show misha hips_smile
with charachange




mi "……それに二人を処分するための事務作業は、たった二人の生徒会役員である私たちの前にすでに山のように積み上がった書類をさらに増やすだけなので――それに二人ともほんとに可愛いんだもの～！"





show shizu adjust_happy
with charachange


shi "……"

show misha hips_grin
with charachange




mi "以上の理由で、これは正式な警告として受け取っていただき、以後はあのような行動は慎んでください。すくなくともしっちゃんの目の届く範囲ではね、ひっちゃん～！"








"一連の流れがあまりにも馬鹿らしすぎて、俺は同じように大げさな言い回しで返答せずにはいられなかった。"




hi "これはこれは、わたくし目が覚めるような思いでございます"






hi "さきほどの無分別な行為に対し深く陳謝すると共に、おそれながら、かように不適切な公共の場での愛情表現へと駆り立てる恐れのあるわたくしめの下劣なる衝動を抑えるよう精進いたします"






hi "既に膨大な業務をお持ちの生徒会に対し、このような些細な件でご迷惑をおかけするのは意図する所ではなく、今後この件に関する日々の苦労を少しでも軽減するため最善を尽くす所存でございます"



hi "すくなくとも、静音の見てるところではな"


"最後の一言とともにウィンクを送ると、ついにミーシャは耐え切れずに吹き出す。"

show misha cross_laugh
with charachange


mi "わははは～！"

show misha cross_grin
with charachange


mi "まさにそのとおりだよ、ひっちゃん～！"


"自分でも笑いながら、俺たちは教室に入る。"

stop music fadeout 2.0
scene bg school_scienceroom
with shorttimeskip



"授業は特に何があったわけでもなく、終業のベルが鳴った後、またもや武藤先生と二人きりになっている。"


show muto smile at center
with charaenter



mu "どうやら科学部の第２回の活動に部員全員が集まったようだな"


play music music_another fadein 2.0
show muto normal
with charachange



mu "それとも１回目か？　昨日のを活動と呼ぶべきか否か、どう思う？"




hi "えーと、昨日は科学部を設立したんですよね？"





hi "それは部に関係ありますよね。だから昨日のあれを活動と呼んでも問題ないと思います"



show muto smile
with charachange




"武藤先生はいつもの通り不器用で硬い笑顔を見せる。もしかして自然に微笑むことができないのは、ただ単に顔の筋肉が正しい形をしていないからじゃないだろうか。"





mu "お前は本当にコツを心得ているのだと思うぞ。論理的思考法の事だ"





hi "そうかもしれないですね？"


show muto normal
with charachange


mu "科学者というものは権威を持って話すものだぞ、久夫。そしてここで言うべき答えは『はい、そうです』だ"




mu "世界がその仕組みを知りたいと思う時、我々はそれを伝える。たとえ我々が知っている事がよくできた仮説でしかないとしてもだ"


show muto smile
with charachange


mu "だが我々は確信しているがごとく話さなければならない。なぜなら我々はこの事象に関しての権威そのものだからだ。いいか？"



"下手な冗談と不器用な笑顔に続いて、静かに笑っている。俺は自分の顔をしかめない様に努力はしているが、とてもうまくいっているとは思っていない。"


show muto normal
with charachange


mu "もちろん、それは完全に誤りだ"




mu "我々は確かに色々な事を知っているが、誰も確信など持てないという事実だけからしても、この世の事象を知り尽くした者などいないと言える。確実性がなければ、熟練者は存在しえない"







mu "しかし時には、我々はそのフリをしたがるものだ"





hi "確信を持てるものだってある。ですよね？"





mu "そうだな……だが違うとも言える"



mu "例えば、我々は重力が存在しているのは知っている"


"例証するように、武藤先生はペンを持ち上げて落とす。"




mu "ほらな？　確かにここにある。だが折に触れて確認してみるのはいいことだ"





mu "だからこそ、今でも重力の研究に延々時間を費やす学者がいる"


show muto smile
with charachange



mu "それがどう働くかはよくわかっているが、我々の想定を超えるものがある可能性は常にあるのだからな"





mu "だから確認、確認、そしてまた確認だ。一言で言えば、それが科学なんだ、久夫"






"聞いてる間ずっと、俺は魔法をかけられていたような気がしていた。武藤先生は本当にこれらの事に情熱を持っているんだな……と思う。時々、怪しいと思うこともあるけど。"





"この世の理……"



"人体の仕組み。"


"大宇宙の論理。"




"答えられるべき全ての疑問。"






"そして今後どの道を進むかによっては、自分の心臓を治す方法を見つけることもできるかもしれない。と言っても、俺にとってはそれほど優先すべきことじゃないけど。"





"そのうえ、先生から昨日もらった本について話し合いを始めると、自分の心臓の状態よりもそちらの方がますます興味深く思えてくる。"


show muto normal
with shorttimeskip




"ふと気づくと、すでに１時間もたっていた。"





mu "ふむ、今回の活動はこれまでにしておこう。いいか？"



mu "次は……明日かもしくは……明後日あたりにしようか"


"武藤先生はそれについて少し考えこむ。"




mu "明後日にしよう。成績つけが沢山あるからな"



hi "わかりました。それではまた"

scene bg school_hallway3
with locationchange

stop music fadeout 5.0



"教室を出た所で、俺は今夜の予定が特に何もないことに気づく。"



"笑美とは特に何も計画してなかったからな……"



"じゃあ図書室にでも行こうか。部屋で宿題してるよりは少なくともマシだろう。"


scene black
with locationskip_in

label jp_E20:

play music music_happiness fadein 2.0
scene bg school_library
with locationskip_out



"図書室というのはいつも校舎内の他の場所に比べて涼しい気がする。"




"多分本が極度の暑さや湿気で傷まないようにするためだろう。"




"本は丈夫な物ではあるけれども、良い状態を保つには少しばかり気をつける必要がある。"




"使い古されて本の背からページがほとんど取れそうになっているものもいくつか持っている。"



"すでに使用不可能に見えても、気をつけて使えばなんとか……"


"貸し出し口まで歩いて行くと、そこに何か忙しそうにしている優子さんを見つける。"

show yuuko neutral_up at center
with charaenter


"中に入ると笑いながら手を振ってくる。"

show yuuko closedhappy_down
with charachange


yu "こんにちは、中井くん"

show yuuko happy_down
with charachange



yu "久しぶりね！　今度はどんなのを探してるの？"



hi "特にこれってのはないんです。なんとなく部屋に戻りたくないなって思ってるだけですよ"

show yuuko neutral_down
with charachange


"優子さんがうなずく。"

show yuuko smile_up
with charachange


yu "そうなの。もし用事がないなら、ちょっと私の探しものを手伝ってくれない？"


hi "いいですよ。なにが必要なんですか？"

stop music fadeout 5.0

show yuuko worried_up
with charachange


"優子さんは唇に指をあててこっそりと辺りを見回す。"



"誰かが聞き耳を立てていないか確認しているみたいだ。"



yu "もっと近くに来て"

show yuuko worried_up_close
with characlose



"かなり不安を感じつつ、俺はためらいながら数歩前に出る。"



"優子さんは声を低くし、秘密を打ち明けるようにささやく。"

show yuuko neutral_up_close
with charachange



yu "私ね、実は山久に出没するこそ泥の後を追ってるの"


play music music_tension fadein 0.5



hi "ええっ？"


show yuuko panic_up_close
with charachange



yu "しーっ！　壁に耳ありだよ、中井くん！"




yu "というかあるかもしれない、ね"



show yuuko worried_down_close
with charachange


yu "とにかく聞いて！　あの消えた本のこと、覚えてる？"




hi "ええと、まあ？"



show yuuko worried_up_close
with charachange



yu "それがね、実は消えたんじゃなかったの！　盗まれてたのよ！"




yu "間違いないんだから！"




hi "前にもそんな感じのことを言ってたと思いますけど、どうして分かったんですか？"



"優子さんは顔を近づけ、ささやく声をさらに可能な限り低くする。"

show yuuko closedhappy_down_close
with charachange


yu "なぜかってね、そいつの隠し場所を見つけたのよ！"



hi "なにを見つけたと？"



"優子さんが勝ち誇ったような顔をする。"



show yuuko happy_up_close
with charachange




yu "隠し場所を見つけたの！　男子寮にある吹き抜け階段の下よ"





yu "探していた本が、３冊全部そこにあったのよ！"


show yuuko closedhappy_up_close
with charachange



yu "泥棒かもって思ってた事は前にもあったけど、これで確定だわ！"



hi "じゃあその本は取り戻したんですか？"

show yuuko panic_up_close
with charachange


"優子さんはまるで今素っ裸で歩きまわっているのを俺に指摘されたような顔をする。"



yu "正気なの？"


show yuuko worried_down_close
with charachange


yu "私が探ってるってバレちゃうじゃない！　そしたら身を潜めて逃れようとするかも！"


hi "あぁ……なるほど。じゃあ俺にどんなことを手伝って欲しいんですか？"


"優子さんは再び視線を図書室中に巡らせると、顔を寄せてくる。"

show yuuko neutral_down_close
with charachange


yu "私のスパイになって欲しいの"


hi "スパイ？"


yu "そう。ほら、寮の中にいる時とかにさ"

show yuuko closedhappy_down_close
with charachange



yu "怪しい動きがないか目を光らせていてもらいたいの"



"いったいなにをもって怪しいか判断しろと？"



"健二はかなり怪しい奴だけど、あいつは授業にもろくに出てないだろうし、まして本を盗むために図書室に忍び込むなんてありえそうにない。"




"だけど頼みを引き受けて何か害があるわけでもないしな。少なくともこの奇妙な会話からは抜け出せるだろうし。"






hi "ええ、やりますよ。お安い御用です"



show yuuko closedhappy_down
with charadistant


"優子さんは背を伸ばし興奮したように手を叩く。"



yu "よかった！"

show yuuko worried_down
with charachange



yu "じゃあ急いで話題を変えなきゃ。誰かが入ってくるかもしれないしね！"


stop music fadeout 2.0

show yuuko happy_down
with charachange


yu "授業の調子はどう？"



hi "ええと、実際とてもいい感じですよ"



hi "朝にランニングしてるんですよね――"


show yuuko closedhappy_up
with charachange



yu "茨崎笑美ちゃんと、でしょ？"


play music music_comedy fadein 2.0


hi "う、はい"


hi "なんで知ってるんですか？"

show yuuko smile_down
with charachange


yu "カフェで二人に接客したじゃない。忘れたの？"

show yuuko closedhappy_down
with charachange


yu "もし中井くんが誰かと走るつもりなら、きっとあの子だろうなって思ったのよ"


"優子さんはどうやら自慢気なようだ。"


hi "凄いですね"


hi "とにかく、そうです。一緒に朝走ってるんですよ"



hi "あと、付き合ったりもしてたりして"


show yuuko closedhappy_up
with charachange


"優子さんが興奮したように手を合わせる。"


yu "本当に？　すごいすごい！"




yu "あなたたちふたり、絶対お似合いよ！"



show yuuko neutral_down
with charachange




yu "実はね、そんな風にお互いぴったりの相手を見つけた人たちを見るのって大好きなの"





yu "あなたたちが上海に入ってきたあの時、こんな風にも思ったの。『あの男の子があの女の子たちのどっちかと付き合う事になるんじゃないかな』って"





hi "……本当ですか？"


"俺が不気味に感じているのが口調ににじみ出てるのに気づいた様子もなく、肯定するようにうなずく。"


show yuuko closedhappy_down
with charachange



yu "そうよ！　あの子達の一人と付き合うだろうってわかってたんだからね"



show yuuko neutral_down
with charachange


yu "私にはそういうのが見えちゃうのよ"

show yuuko worried_down
with charachange


yu "といっても……"


"優子さんの表情がわずかに陰る。"


yu "私自身についてはてんで駄目なんだけど"


hi "いや、そんな事は絶対ないですよ"

show yuuko neutral_down
with charachange


yu "ううん、そんな事あるのよ"



yu "前にある男の人に出会ってね……"


show yuuko smile_down
with charachange


yu "一緒に居てすごく楽しかったの。でもその人は私より年下だってわかってね"

show yuuko neutral_up
with charachange


yu "ちょっと変だなって思ってたけど、耐えられないほどじゃなかったの"




yu "本当に変なのは、彼がある日突然いなくなったことよ。それから彼には一回も会ってないわ"







hi "へえ、それは確かに変ですね"



show yuuko worried_up
with charachange



yu "そうでしょ？"


show yuuko neurotic_down
with charachange



yu "私が何かしちゃったせいじゃなければ良いんだけど……"




"優子さんを安心させなくちゃ、という気分になる。"





hi "そんなことないですよ、きっと"


stop music fadeout 4.0

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_phone
show yuuko panic_up
with vpunch


"もう少し優子さんを落ち着けようとしていた所に突然ポケットから呼び出し音が鳴り響き、二人とも驚きのあまり飛び上がってしまう。"


show yuuko worried_down
with charachange



"優子さんは気持ちを落ち着かせるように息を吐き、俺はポケットから電話を取り出す。間接的にだけどびっくりさせてしまった事が少し恥ずかしい。"



scene bg school_library_yuuko_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)


hi "笑美か？　どうしたんだ？"



emi "ああよかったまだ電話したことなかったからこの番号であってるのかわからなかったし電話受けてくれるかもわからなかったし――"



$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play music music_pearly fadein 2.0


hi "おい笑美、ちょっと落ち着けよ"


hi "いったいどうしたんだ？"


"回線の向こうの声が止まり、笑美が落ち着こうと息を整えているのが聞こえる。"




"何かが笑美を酷く動揺させているようで、こっちまで落ち着かなくなってくる。"



emi "お願いだからちょっと……"


emi "部屋まで来てくれない？"




emi "ていうか今すぐ？　さもなきゃちょっと後とか？"





emi "ほんとにほんとに話さなくちゃいけない事があるの"




"笑美の最後の台詞には、今まで聞いたこともないような懇願する口調が含まれていた。"


hi "もちろん大丈夫だ。すぐ行く"


hi "だからじっとしててくれよ。いいか？"


"ますます心配が膨らみ、俺自身よくわからない事を言っているのは間違いない。"


emi "うん。いいよ"


hi "じゃあそっちで会おう"

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_library
show yuuko worried_down at center
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None

with charaexit



"俺は通話終了ボタンを押すとポケットに電話を滑りこませ、優子さんに突然の退席を謝るとすぐさま走りだす。"


scene bg school_girlsdormhall
with locationskip



"途中で、時間の事だったり、女子寮にこんな時間に入ろうとする男がいれば変に思われるだろうなんて事を考えて立ち止まっていたかもしれない。"




"だけど今はとにかく笑美に会って、なにが起こってて、どう俺が助けになれるかを考える事で頭がいっぱいだった。"



play sound sfx_doorknock2


"ドアをノックすると、感情を抑えているような声で『入って』と返事がある。"


scene bg school_dormemi at left
with locationchange


"目の前に広がる光景を見つめながら、何かとてつもなく悪い事が起こっているのが分かった。"


"もちろん笑美はそこにいる。"



"でも車椅子に座っている。"




"義足はない。部屋を見回すと端っこに放り投げられたように置いてある。"


show emiwheel weaksmile at center
with charaenter



"笑美は俺が入るのを見て、俺に会えた嬉しさと、そして完全に打ちひしがれた悲しみに口を歪めて笑う。"






emi "こんちは、久夫"





"泣いていたような跡が見えるけど、そうだったとしても今は泣き止んでいる。"


"ここに来るのに階段を一段とばしで登ってきたせいか、自分が少し息切れをしているのに気づく。"






"だけど心臓はそんな負担にもへこたれる様子はない。そんな嬉しい事実はしまいこんで、後で考えることにする。"










"俺の彼女が車椅子に座っているのを、ちょっと唖然としながら見つめているような状況じゃないときに。"








"笑美の挨拶にまだ答えていない事に気がついて、脳みそを急いで動かす。"




hi "笑美、いったいどうしたんだ？"

show emiwheel pout
with charachange



emi "やっぱり久夫のいうことを聞いておけば良かったみたいね"


show emiwheel sad
with charachange



emi "足が悪い感染症にかかっちゃった。最低数週間は義足つけて走ったらだめだって"




"笑美は苦い笑いを漏らすけど、笑美がそんな顔を見せるなんて耐えられない。"


show emiwheel frown
with charachange



emi "しかも、義足で歩くのだって禁止"



emi "松葉杖を使えば片足だけ付けてもいいらしいけど、それじゃなんの意味もないしね"


show emiwheel awayfrown
with charachange



emi "そうやって跳ねるなんて意味わかんないよ？　片足じゃ走れないんだから"


show emiwheel pout
with charachange




emi "少なくともこれなら、早く転がったりはできるしね。知らないけど"





hi "そ、そうだな。それっていいことだよな？"




"ぎこちなくも前向きに捉えようとする俺の努力を嬉しく思ってくれているようだけど、効果はあまりないようだ。"



"笑美はまた肩をすくめる。"


show emiwheel awayfrown
with charachange



emi "ただちょっと……不愉快だなあって"


show emiwheel frown
with charachange



emi "だってさ、もう屋上で一緒に食事もできないんだよ。車椅子じゃ行けないし"




hi "まあな、でも別に大問題ってわけじゃないだろ？"




hi "ほら、一緒に食べることはできるんだし。そこが大切なんだよ"


show emiwheel weaksmile
with charachange



"また歪んだ笑顔を見せる。そんな顔を見ていると心が痛い。"





emi "うん、まあそうかもね"



show emiwheel frown
with charachange



emi "でもさっきも言ったけど、不愉快なの"



show emiwheel awayfrown
with charachange




emi "というか車椅子なんてずっと使ってないからさ、もうかれこれ……"



stop music fadeout 10.0


"笑美は少しの間考えこむ。"

show emiwheel pout
with charachange



emi "７年くらい？　とにかく、だいたいそんな感じ"



emi "長い間だよ"

show emiwheel weaksmile
with charachange




emi "使い方、ちょっと忘れちゃってるみたい"




hi "まぁでも一時的な事でよかったよ。だろ？"


"笑美はうなずく。"

show emiwheel neutral
with charachange



emi "うん、そうだね、もちろん"




emi "もう二度と付けられないってわけじゃないし"


show emiwheel awayfrown
with charachange



emi "けど、やっぱりうんざりするのはおんなじだよ"



"俺は同情しながらうなずく。"



"どの道、それ以外に俺にできる事なんてないしな。"





"どうしろっていうんだ。『だから言っただろ』とでも言えばいいのか？"







"{b}確かに{/b}足を診てもらえとは言ったけど。"





"でも俺が気づいた時点ではもう遅すぎたんだ。"




hi "なにかやってほしい事でもあるか？"



hi "あー、いや、なにか俺に手伝える事はないか？"


show emiwheel closedsmile
with charachange


"頭を振る笑美の顔にはいつものような笑顔が戻りつつある。"



emi "ううん、自分の事は自分でなんとかできるよ"


show emiwheel grin
with charachange



emi "あ、でもベッドに運んでくれるっていうなら自分で転がっていかなくてすむから助かるかな"




"つい、俺は赤面してしまう。"





"笑美がくすくす笑う。"

play music music_heart fadein 0.5

show emiwheel wink
with charachange


emi "久夫ってばお堅いのね"



hi "そんなんじゃないさ！　笑美みたいな女の子の弱みにつけこむような真似はしたくないだけだ"



hi "紳士的じゃないだろ"

hide emiwheel
with charaexit

show bg school_dormemi at right
with charamove


"俺は車椅子をベッドに寄せ笑美を軽く持ち上げてそこに下ろすと、笑美はさっと姿勢を正して端っこに座る。"

show emi basic_grin:
    center
    ypos 1.0
    easein 0.5 ypos 1.1
with charaenter




"本音をいうと笑美は見た目より少し重かった。もちろん、そんな事を口に出したら失礼だけど。"





hi "うわ、お前重いんだな"


play sound sfx_pillow
show comic vfx2
show emi excited_amused:
    center
    ypos 1.1
with hpunch

with Pause(0.5)

show comic vfx2:
    truecenter
    easeout 0.5 yanchor 0.3 alpha 0.0
with Pause(0.5)


"笑美が投げた枕が当たる。"


show emi basic_closedgrin
with charachange


emi "最っ低"


hi "言ってみただけだ"


hi "走ってるからだろうな"

show emi sad_shy
with charachange


"走る事に触れると、笑美の笑顔が少し曇る。"


show emi sad_pout
with charachange



emi "ふん、まあしばらくはそんな心配しなくても良くなったもんね"


show emi sad_grin
with charachange


emi "体重もいくらか減るんじゃないかな"





hi "でも体重減らすときはそうするんだろ？　運動をやめるってのがさ？"






show emi basic_closedgrin
with charachange




emi "ナースくんがそう勧めてくるのは間違いないよね、きっと"



hi "そう、それについてなんだけどさ。まだ朝の時には来てくれるか？"


hi "一人で走るのは正直い――"


show emi sad_depressed
with charachange


emi "あぁちくしょう……"







"笑美の突然の言葉、乱暴な言葉使いというよりも不穏なうめき声に、俺はショックでちゃんと目を向けられなくなる。"








"笑美は前方に体を倒し、手で目を覆い泣いているのを隠そうとしている。"


"いうまでもなく、堪えるようにすすり泣く声で間違いなく泣いている事は明らかだ。"



hi "なあ、ごめんよ"



hi "今のは忘れてくれよ、な？"


show emi sad_depressed_close at center
with characlose


"俺はそっと笑美の体に腕を回して引き寄せる。"


"他に何を言ったら、したらいいかわからない。足を再び失った相手に何といって元気づけてやればいいんだ？"

show emi sad_pout_close
with charachange


"笑美も抱きしめるように腕を回し、そのまま少しじっとしている。"


hi "ごめんな"


hi "慰めるっての自体俺は下手くそなんだよな、多分"



emi "そんなこと言わないで"



emi "あたしは大丈夫だから。ほんとに"


"俺の胸に押し付けられてくぐもった声が聞こえる。安心させるように笑美の頭をぽんと叩く。"



hi "そうそう、その意気だ"


hi "笑美ならこれも乗り越えていけるさ。俺が保証する"


hi "それに、俺はいつだって助けになるぜ。そう言ったろ？"

show emi sad_shy_close
with charachange


"笑美は顔を上げ、涙ぐんだ目で俺をじっと見つめる。"

show emi sad_grin_close
with charachange


emi "助ける？　ほんとに助けてくれる？"



"歪んだ笑顔のその目には何かが閃いたような光が見える。"


"これは馬鹿にされてるんだろうか。"


hi "もちろん。そりゃあ確かに、笑美はちょっと重いけど――{w=0.5}{nw}"


play sound sfx_impact

show emi excited_amused_close
with vpunch



extend "むぐっ！"




"突然笑美に唇をふさがれて、俺の軽口が途切れる。予想していなかっただけに、勢いそのままで頭をベッド後ろの壁にぶつけてしまう。"



hi "いてっ"

show emi basic_hes
with charadistant


"笑美は身を引くと、笑い出しそうなのを抑えて心配しているように装おうとしている。"


emi "だいじょうぶ？"

show emi excited_proud
with charachange


emi "ゴメンね！"


"痛々しく頭を擦りながら、俺は笑美に笑い返す。"



hi "完全に隙を突かれたぜ"




hi "これからもいつもやるつもりか？　俺は静音とミーシャからもっとお説教を受けなくちゃいけないのか？"




"あの二人組を話題に上げると、笑美はくすくす笑う。"

show emi basic_closedgrin
with charachange



emi "まったく、あの二人は……"


show emi basic_grin
with charachange




emi "あたしが理由を知らなかったら、なんであんな偉そうな奴といつも一緒にいるのかほんとに不思議に思うだろうな"





hi "どっちのことを言ってるんだ？"


show emi basic_closedhappy
with charachange


emi "どっちかなんてわかってるでしょ、久夫。ミーシャは全然威張ってないじゃん"


hi "じゃあその理由ってのは何なんだ？"

show emi basic_confused
with charachange


emi "えっ？"


hi "ミーシャがいつも静音にくっついて回ってる理由だよ"

show emi basic_closedgrin
with charachange



"笑美は笑顔で俺の質問を受け流す。"





emi "し～らない"



hi "そうかい"

show emi basic_grin
with charachange



emi "とにかく、最初の質問を忘れちゃってるみたいだけど？"



hi "あぁ、そういえばそうだった"



hi "する前にちょっと一言いってくれてもいいだろ？"





hi "でないと脳震盪を起こす羽目になりそうだ"





"後頭部をなでて、その点を強調する。"



show emi excited_amused
with charachange


"笑美はたまらないように笑う。"



emi "ヘルメットかぶればいいじゃない"


show emi excited_proud
with charachange



emi "ここの子の何人かはそうしてるじゃん"



stop music fadeout 1.0


hi "それか今ここで復讐するかだ！"

play sound sfx_pillow

show emi excited_circle
with vpunch




"横に置いてあった枕をつかむと笑美の頭めがけて振り下ろす。"




show expression im.Composite((295,1200), (0,0), "sprites/emi/emi_excited_circle.png") as emi:
    xalign 0.5 yanchor 0.5 ypos 1.0 subpixel True
    easeout 0.8 ypos 1.25 rotate -90
with None

show expression im.Composite((295,1200), (0,0), "sprites/emi/emi_excited_sad.png") as emi:
    xalign 0.5 yanchor 0.5 ypos 1.0 subpixel True
    easeout 0.8 ypos 1.25 rotate -90

with Dissolve(0.5)
with Pause(0.3)

play sound sfx_impact

hide emi
with vpunch


"笑美がドスンと音をたててベッドから床に転げ落ちる。"

show emi sad_pout:
    center
    ypos 1.2
    ease 1.0 ypos 1.0
with Dissolve(1.0)


"するとまず腕がベッドに現れ、そして体全体を器用に引き上げる。"


"この小さな体のどこにこんな凄い力が隠れているんだろうか。"


"笑美はうつむきながら顔をこちらに向けず、もしかして怪我をさせてしまったんじゃないかと不安にさせる。"


hi "笑美、大丈夫か？"


hi "どこか怪我したりはして――{w=0.3}{nw}"


show emi excited_smile_close
with vpunch


"笑美の腕が急に持ち上がって俺の襟を掴む。ぐいと引っ張られ、不敵な笑顔が俺の目の前まで近づく。"



hi "おい笑美……？"

show emi excited_smile_close:
    subpixel True
    linear 0.1 ypos 1.7 zoom 2.0 
with None

scene white
with Dissolve(0.1)

play sound sfx_impact

scene black
with Dissolve(0.75)


"するどい頭突きをくらい、おでこがゴツンと大きな音をたてる。"

scene bg school_dormemi at right
show emi basic_closedgrin at center
with openeye


"後ずさりしながら痛む頭をさすっていると、笑美が勝ち誇ったようににやにやしているのが見える。"

show emi basic_grin
with charachange


emi "{b}こんな{/b}復讐はどう？"

play music music_running


hi "そりゃないぜ！"


hi "復讐の復讐、なんてのは駄目だろ！"



"足の大部分がないにしては、驚くほどにすばやく移動する。"


show emi basic_grin:
    center
    parallel:

        "emi basic_closedgrin" with Dissolve(0.2, alpha=True)
    parallel:
        easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None




"再び笑美めがけて振りかぶるけど、器用に転がって避けられて笑美の枕で反撃される。"







"いうまでもなくこれは笑美のほうが不利な状況だ。そもそも俺は立ち上がることができる。"




scene black
with vpunch


"うぉあ！"

window hide

show evh emi_grinding_victorytall:
    xalign 0.5 yalign 1.0 subpixel True
    easein 12.0 yalign 0.0

with Dissolve(1.0)

with Pause(6.0)

window show


"どうやらそうでもないらしい。笑美は上手に俺の足をからめ取ると、仰向けに倒れこんだ上にまたがって澄ました顔をしている。いったい何が起こってこうなったのかさっぱりだ。"



emi "あたしの勝ち！"




"笑美の目がいたずらっぽく輝く。完全に負けた。しかも体ははるかに小さいこの女の子にだ。"






"といっても、負けること自体そんなに悪いことじゃない。笑美が腰の上に乗っていると俺が、というか俺の体が、冷静でいられなくなってしまう。"





scene bg school_dormemi
with locationchange




"喋ろうとして口を開けるけど、一言も発せないうちに笑美がすぐに顔を寄せてくる。唇を合わせてくるのに何の抵抗もしない、しようとも思わない。"





"これは……なんだかいつもと違うぞ。"



"笑美の唇が俺の下唇をはさみながら引っ張り、再びねぶり始める。笑美の舌が口に進入し、中をまさぐる。鼓動が速くなり、体中に微熱が広がっていくのを感じる。"


"意識がぼんやりとし始め、自然に笑美のブラウスへと手が伸びる。胸に触れると笑美は息を呑み、クスクスと笑い始める。そして――"


scene evh emi_grinding_victory
with locationchange


"俺の見上げる前でその笑いはにやにや顔へと変わる。"



emi "ほら、言ったでしょ。これであたしの勝ち星２ね"




hi "なんだそれ？　こんなのノーカウントだろ。女の武器を使ったくせに"



show evh emi_grinding_wink
with charachange


emi "『恋愛と戦争では手段を選ばない』 でしょ？"



emi "あはは、顔がまっかっかだよ！　久夫がそんな恥ずかしがりやさんだって知らなかったな"




hi "お前の顔だって赤いだろ。そっちこそお堅いんじゃないか"




"今現在俺の上にまたがって、ついさっきまでディープキスしてた子にそんなことを言うのが馬鹿げてるのは、まあ良く分かってるけどさ。"



show evh emi_grinding_grin
with charachange


emi "あたしがお堅い？"



emi "あらそう。ならどっちが先に顔を赤くするかやってみよっか？"



"笑美の口調に怖がるべきなのか興奮すべきなのかは分からないけど、その質問に答えるまでもなく勝負は開始される。"

label jp_E20h:

show evh emi_grinding_half_undress
with charachange

show evh emi_grinding_half_grin
with charachange


"何という事もないように笑美はさっとブラウスを脱ぐと放り投げ、ブラとスカートも後に続いて床の上に舞い落ちる。"


emi "どうだっ！"


"顔が赤くなりそうな気持ちを押さえようとするけど、これがなかなか難しい。"



hi "盛り上がってきたな、おい"



show evh emi_grinding_off_yawn
with charachange



"こんな体勢をしているおかげで手間が掛かったけど、自分のシャツも同じように脱ぎ捨てる。笑美は待ちくたびれたようにあくびをするふりを見せる。"



emi "もうちょっと上手に出来るように頑張らないと――"


show evh emi_grinding_off_closesurprise
with charachange
stop music fadeout 3.0


emi "あんっ……！"



"俺の手が優しく素肌に触れると、笑美はピクンと震える。またもや何も考えずに手が自然に動き始めたようで、もしこんな体勢でなければとっくに笑美の下着を脱がしてただろう。"




"笑美の顔が赤くなり始めているのを言おうと思ったけど、すでにお互いの抑えがほとんど効かない時点まで一気に到達している。会話をする気も失せ、腕には力が入らない。"


play music music_one fadein 0.5



"この突然の感覚の高まりに対して、俺たち二人とも心の準備ができていない。"


show evh emi_grinding_off_closearoused
with charachange


"形容しがたいほどの熱が俺自身、そしておそらく笑美の体からも押し寄せ、体を駆け巡る。"



"俺の胸に片腕を置いて体を支え、体をこれ以上触られないようにもう片方で俺の腕を掴んでいる笑美はその状態をとても楽しんでいるようだ。"

show evh emi_grinding_off_aroused
with charachange


"しばらくのためらいの後、笑美が体を動かす。"


"また動かす。"


"さらにもう一度。"


"動かすたびに笑美の吐息は乱れる。俺の息も次第に早く、不規則になっていく。"


"笑美の体がぴくぴくと震えて、バランスを失い始めてるように感じる。確かに、足がない事を考えるとしっかりと体を支えるのは難しいに違いない。"


show evh emi_grinding_off_closesurprise
with charachange



"手を笑美の腰に回し、出来る限り安定させようとする。その体は硬く、張り詰めているような感触だ。"





"普段の運動量を考えてみれば当然だ。俺が触れるのに反応して、あの筋肉の中の秘められた力がそれ自体を収縮させている。"




"笑美を支えようとしたことで、その体をちょっと前にずらしてしまったのは計算外だけど、その……これはすごく気持ち良い。"



show evh emi_grinding_off_arousedclosed
with charachange


"笑美のパンツは俺のズボンの上で滑らかに動き続け、動作のリズムを掴むのにそこまでの時間は必要なかった。"



"しかし笑美は単調なリズムを続けるのが嫌なようで、早くしたり遅くしたり、時には止まったりと永遠とも思える時間をかけて動き続ける。"
"俺の反応を見て楽しんでいるのか、それとも笑美自身が気持ちいいのかは分からないけど、そんな事を気にするような意識はとっくに飛んでいる。"






"二人のあいだの熱は激しさを増し、俺は喘ぎ声を抑えることができない。その声に笑美まで追いつめられていくかのようだ。"





"体を動かして笑美の動きを一瞬止めると、それに合わせて控えめな胸が揺れる。そんな風に続けていると笑美の呼吸は次第に速くなっていき、俺自身の呼吸も同じように速まる。"




"目を閉じ、求めるように唇をすぼめる笑美を見て、俺は少しの間なんとか体を起こす。お互いの口を舐り合い、胸を重ねあい、汗が交じり合う。"



"再び体を横たえると、ズボンが汗まみれになっているのに気づく。今の行為を止めずに済むんだったら脱いでいただろうけど。"





"それに今の俺たちの行為を、脳みその裏側をくすぐるような、そしてますます押し寄せる快感を、止めたいとは思わない。"




"笑美は動きをさらに速め、息を荒くし、口から発する声はもはや意味を成していないようだ。それとは逆に、体の方は素直に反応を見せている。"


show evh emi_grinding_off_come
with charachange



"突然笑美の動きが少し不規則になって、俺自身の息がのどで止まる。その瞬間、最後の強烈な衝動が意識を端まで追いやり、今まで存在すら知らなかったほどの快感が迫りくる。"



scene white
with Dissolve(3.0)


"意識が飛び、視界は白み、絶頂の感覚に耐え切れない。数秒の間、笑美と俺が共に感じたこの素晴らしい快感以外の世界が全て消失したかの様に感じられる。"

show evh emi_grinding_off_end
with Dissolve(1.0)


"そして……その感覚が過ぎ去る。視界が戻り、俺は上にまたがる少女の目の中をただただ見つめるだけだ。"





"数分の間、どちらも口を開こうとしない。お互いの吐息の音が部屋を満たし、さきほどまでの快感の残滓が未だ息を整えさせてくれない。"




"笑美がようやくしぶしぶと俺の上から離れて壁に背を向けて座り、俺もそれにならう。"



label jp_E20x:

scene bg school_dormemi at right
with locationchange

show eminude smile_close
with charachange



emi "それで……あたしの顔赤くなってた？"




hi "気づかなかったな"



hi "俺は？"


show eminude neutral_close
with charachange



"まだ少し息を荒くしながら、笑美は肩をすくめる。"


show eminude weaksmile_close
with charachange


emi "あたしも気づかなかったよ"


hi "そうか、じゃあもう一回ため――"


play sound sfx_dooropen

stop music fadeout 0.3

show rin basic_deadpan behind eminude:
    center
    xpos 1.0 xanchor 0.0 alpha 0.0 subpixel True
    easein 0.5 right alpha 1.0
show eminude blush_close
with vpunch



rin "ちょっと窓使わせて"




"とっさに隠れようとするけど、この疲れ果てた体で、しかも隣に上半身裸の笑美がいることを思い出す。これはどのみち隠れようもないな。"


show rin basic_awayabsent:
    right alpha 1.0
with charachange

show rin basic_absent
with charachange

show rin basic_awayabsent
with charachange


"琳の視線が笑美から俺へ、そして窓へと移動する。"

show rin basic_deadpannormal
with charachange


rin "雲があったんだよ"

play music music_comedy fadein 0.5

show eminude neutral_close
with charachange


emi "雲？"

show rin basic_lucid
with charachange


"琳がうなずく。"

show rin relaxed_nonchalant
with charachange



rin "自分の窓からそれを見てたんだけど、じっとしててくれなかったから"


show rin negative_spaciness
with charachange



rin "だから笑美の窓を使わせてほしくて"


show eminude closedsmile_close
with charachange



"笑美が体の向きを変え、俺は自分の笑い顔が見えてしまうのをごまかすために咳払いをする。"



emi "どのくらい窓を使いたいの？"


emi "あたしたちさ、ほら"

show eminude wink_close
with charachange


emi "ちょっと取り込み中なの"



"ここで俺は耐え切れずに噴き出す。"


show rin negative_annoyed
with dissolvecharamove


"そんな俺たちを無視し、琳は窓から空を見つめている。"

show rin basic_deadpanupset
with charachange


"肩を落としているところを見ると、がっかりしているようだ。"



rin "うーん"




rin "別の形になっちゃった"




rin "残念"


show eminude grin_close
with charachange



"笑美は真面目な顔を保ち続けるのに苦労している。"



emi "あらら、それはとっても残念だね、琳"


show eminude pout_close
with charachange


emi "じゃあそろそろ、二人きりにさせてもらえないかな？"

show rin relaxed_nonchalant
with charachange

with Pause(0.2)

show rin relaxed_nonchalant:
    easeout 1.0 xpos 1.0 alpha 0.0 xanchor 0.0 subpixel True 
with Pause(1.0)

play sound sfx_doorclose

hide rin
with None


"琳は『いいよ？』とでもいうように肩をすくめ、ドアに足をかけると開いて出て行き、後ろ向きにドアを閉める。"



show eminude happy_close
with charachange


"琳の異常なまでのタイミングでの登場に耐え切れず、二人でバカみたいに大笑いを始める。"



"笑いが止み、俺は笑美を見つめる。二人ともひどいありさまだ。"


stop music fadeout 5.0


hi "さて"

show eminude neutral_close
with charachange


"笑美が眉を上げる。"


emi "さてさて？"


hi "もう一回？"

show eminude wink_close
with charachange


"笑美は口をあけて笑い、そしてうなずく。"

show eminude grin_close
with charachange



emi "今度はちゃんと服を脱いでからしたほうがいいかもね"


$ suppress_window_after_timeskip = True

scene black
with dissolve

label jp_E21:



window hide None

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show


"目覚ましが朝の静けさを打ち砕く直前になって、日差しが窓を通り抜けて差し込んでくる。"

play music music_dreamy fadein 6.0



"体中が痛い。"



"前の晩の出来事が、とつぜん俺の意識のなかに押し入ってきて、赤くなっている自分に気づく。"



"目まぐるしい夜だった――背中の痛みの原因はまさにそれだ。"




"思い返してみるに、帰りは緊張したな。"



"ズボンが……その、汚れて、部屋に戻る前にシャワー室でそれを洗っていた。"


"ところが、前の方にも明らかな汚れがついていた。"



"幸運なことに、戻る途中で出会ったのは健二だけだった。"




"そして健二はなんにも気づいちゃいなかった。"




"まあ、俺がすぐそばにいるということ以外は。"





"もちろんその夜なにをしていたかとか、何か重要なことを突き止めたかとか、そんなことは聞いてきた。"




"自分が答えるために口を開いたかさえ覚えていない。それほど疲れていたんだ。"




"そして今朝、俺は疲れ果てていることを認めざるを得ない。"




"それでも、笑美とは運動場で会う約束をしているし、がっかりさせたくはない。"



scene bg school_track
show emiwheel weaksmile at center
with locationskip


"笑美はまさに俺が来るのを待っている。"



"車椅子に座っているにもかかわらず、笑美はできるだけ明るく振る舞おうとする。"




"俺は手を振って、ストレッチを始める。"



hi "早いな"

show emiwheel frown
with charachange


"笑美は顔をしかめて、頭を振る。"

show emiwheel angry
with charachange



emi "バカ言わないで"




emi "{b}そっちが{/b}遅いんだよ"


show emiwheel grin
with charachange


emi "寝坊したんでしょ、久夫？"

show emiwheel wink
with charachange


emi "くたくたになっちゃったのかな？"



"やれやれ、ようやく元の調子に戻ったみたいだ。"





"予想通り、笑美はこの前の……行為、に触れることに全く気後れする様子がない。"




hi "なあ、俺がちゃんとここに来れて良かっただろ"




hi "夕べはあんなに心臓を酷使したからな、あとでナースのところに行かなきゃいけないかと思ったぐらいなんだぞ"


show emiwheel wink
with charachange



"笑美が大声で笑うと、その顔がとつぜん心配そうな表情になる。"


show emiwheel blush
with charachange

stop music fadeout 8.0


emi "ねえ、それってなんか……"


emi "えっとね、君って……"



hi "いいよ、言えよ"


show emiwheel awayfrown
with charachange


emi "その……最中に発作が起きたりしたら、説明が難しいと思うんだけど"


hi "ああ"


hi "{b}ああ{/b}"



"言われてみれば、まさしく理にかなった心配事だ。"




"夕べの俺は確かにそんなこと考えもしなかった。もちろん……別の差し迫った問題があったからだ。"




hi "なあ、俺たちがその、{b}ナニを{/b}するにしても、朝のランニングより負担がかかることなんてないだろうし、その程度なら俺もぜんぜん問題ないからさ……"


show emiwheel frown
with charachange


"笑美はその点について考える。"

show emiwheel evil
with charachange


"その目に捻くれた光が宿る。"

play music music_emi fadein 2.0



emi "あのさ……"



hi "うん？"

show emiwheel grin
with charachange


"その光は消え去って、笑美は悲しげな笑みを浮かべる。"



"なんだか怪しいという気分がしてしかたない。"


show emiwheel happy
with charachange


emi "手袋、忘れちゃったみたい"


hi "手袋なんてなにに使うんだ？"

show emiwheel smile
with charachange



"笑美は座っている車椅子を指し示す。"



emi "これに決まってるじゃん！"

show emiwheel wink
with charachange



emi "そりゃ、手袋なしでも普段の移動には全然問題ないけど、でもきちんと運動したいからさ"



show emiwheel grin
with charachange



emi "そのくらいのスピードを出すとなると、手袋しなきゃ手に豆ができちゃう"





hi "それがなんだよ、ビビってるのか？　俺ひとりで走れってのか？"



show emiwheel awayfrown
with charachange



"笑美は少しのあいだ考える――か、考えるふりをする。"


show emiwheel closedsmile
with charachange



emi "うーん……たしか、予備の手袋が１つか２つ体育倉庫にあったかも"





"じゃあ笑美は本気で走りたいんだな。"




"でも、普通の制服でか？　こういうことだからてっきり体操服で来ると思ってたのに。"



hi "待った、どうしてあんなところに手袋があるんだ？"


show emiwheel frown
with charachange


"笑美は横目で俺を見る。"



emi "本気で言ってるの？　障害児向けの学校に陸上の用具が山ほど入ってる倉庫があるのに、そこにレース用の手袋がある理由も想像ができない？"




"なるほど、そう言われれば完全に納得できる。"





hi "おい、まだこの場所には慣れきってないんだ。勘弁してくれよな"



show emiwheel grin
with charachange


emi "ま、今回は大目に見てあげてもいいかな"

show emiwheel wink
with charachange


emi "じゃあ来て。手伝ってほしいんだ"



"なにを手伝うんだか想像がつかないけど、一方でレース用の手袋が倉庫にある理由もさっぱりわからないので、追及する気にはならない。"


scene bg school_sportsstoreext
with locationchange


"笑美は小声でぶつくさいいながらも、俺をいとも簡単に倉庫まで案内する。"



"実際、なんだか可愛らしいな。"





"俺は少し急いでドアに先にたどり着く。俺なら笑美よりも簡単に開けられるだろう。"




play sound sfx_door_creak

show emiwheel neutral:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter





"ドアを開いて、笑美は中に入っていくけど、戸口で突然止まる。"





"笑美が自分で乗り越えるには、段差がいくらか高すぎたみたいだ。"

show emiwheel awayfrown:
with charachange

show emiwheel awayfrown:
    center
    ease 0.4 xpos 0.45
    easeout 0.2 xpos 0.5
    ease 0.4 xpos 0.45
    easeout 0.2 xpos 0.5
    ease 0.4 xpos 0.45
    easeout 0.2 xpos 0.5
    ease 0.4 xpos 0.45
    ease 0.2 xpos 0.5
with Pause(1.0)


"障害物をじっとにらみつけて、何度か助走をつけてもうまくいかない。"


show emiwheel angry at center
with charaenter


emi "もう、ポンコツ車椅子"

show emiwheel frown
with charachange


emi "久夫、手伝ってくれない？"


hi "いいよ、もちろん"

scene bg school_sportsstoreroom
with locationchange



"俺なら笑美を少し押して、戸口の向こうにやるのは簡単なことだ。"


show emiwheel blush_close_ni at center
with charaenter


emi "ちょっと、気をつけてよ！"


hi "うわっ！　ごめん"


"このとき、俺は進んでいる先にマットがあることに気づかなかった。"

play sound sfx_impact

show expression im.Composite((425,1200), (0,0), night("sprites/emiwheel/close/emiwheel_blush_close.png")) as emiwheel:
    xalign 0.5 yanchor 0.5 ypos 1.0 subpixel True
    easeout 0.5 ypos 1.4 rotate 70

with vpunch

hide emiwheel
with None



"笑美は驚いて声をあげると、椅子から前のめりに転げ落ちてしまう。"




"この沈黙のさなか、自分のやらかしたことを恐る恐る見届けると、笑美は俺をにらんでいた。"



emi "久夫……"


hi "な、なんだ？"



emi "絶対に病院では働かないって約束して"





hi "ごめん！　わざとじゃないから！"




"笑美はくすくす笑うと、手を持ち上げる。"


emi "車椅子に戻してくださる、久夫さん？"

show emi basic_closedgrin_close_ni:
    center
    ypos 1.2
    easein 0.5 ypos 1.0
with charaenter



"屈みこんで笑美を抱え上げようとすると、笑美は勝ち誇ったように笑顔を見せて、俺を引っ張り寄せてキスをするものだから、俺たちは笑美を車椅子に戻すことなんてすぐに考えなくなる。"


play sound sfx_door_creak




"むしろ白状すると、俺はもっと快適な場所に移動しながら車椅子を外に押しやり、その勢いでドアがばたんと閉まる。"




play sound sfx_rustling

hide emi
show eminude smile_close_ni at center
with charachange



"さて、これで少なくとも邪魔は入らないな。良いことだ。俺の手は素早く笑美のブラウスとスカートを脱がしにかかる。"




"笑美がブラをつけ忘れているのを見てぎょっとする。計画してたっていうのか？"


show eminude blush_close_ni
with charachange



"笑美は腕を曲げて俺の肩に回す。俺は笑美の首筋へとキスを走らせながら、夕べの間に見つけた首と肩が出会う一点で一時停止し、そこに念入りに触れる。"



emi "き、君、すごく上手くなったよね……ひい！"



hi "努力はしてるよ"


show eminude frown_close_ni
with charachange


"笑美が強引に俺の胸に身を当ててくると、俺は戸惑った表情で後ずさりする。"



emi "あたし、言わなきゃいけないことがあるんだ"



hi "ん？"



"後ろへ下がった俺は、目標を変えて笑美の胸に触れることにする。"


show eminude blush_close_ni
with vpunch



"笑美はしゃべろうとするけど、その言葉は可愛すぎるくすくす笑いと混ざり合ってしまう。"


show eminude wink_close_ni
with charachange




emi "あたし、ほんと……くふふっ……本当は、ひ、ひゃあ！　手袋なんてしないんだ"






"俺の返答は、面と向かって諭すよりも、笑美の胸に向かってなにかボソボソ言っているみたいだ。"



hi "それを知ってればなあ……"


"言葉はすぐに無意味なものになった。"

show eminude closedsmile_close_ni
with vpunch



"笑美はまるで取り乱したような振る舞いをしている。今朝会ったときからずっとなにかを隠していて、そして今になってそれを吐き出そうとしているかのように。"




"シャツまで剥ぎ取られるような、優位に立とうとする笑美の積極さに、俺はもう少しで不意を突かれるところだった。"




"俺といえば、白状するともう笑美の態度に押されていて、胸を愛撫する間も転げまわったり、揉みあいながら反撃している。笑美も俺の肩に指を食い込ませて、俺は自分たちがどこにいるのかすっかり忘れている。"


show eminude blush_ni
with vpunch




"あまりに夢中になってしまい、俺はマットから転がり落ちて、なにか小さくて硬いものの上に落ちる。"






hi "いってえ！"


show eminude weaksmile_ni
with charachange


"まだ顔を赤らめて、荒い息をついている笑美は、俺をじっと見ていきなり笑いだす。"



emi "ごめんごめん。大丈夫？"




hi "ああ、たぶんな。何かの上に落ちたんだけど……"





"後ろに手を伸ばしてその物体を引っ張り出し、よく観察する。"


stop music fadeout 0.2





"『ローション　レモンの香り』。"






"待て、なんだって？"

play music music_running

show eminude happy_ni
with charachange


"笑美の目は上を向いて、さらに限界まで大きく笑いだす。"



hi "どうも、これは……陸上には関係なさそうだけど"

show eminude closedsmile_ni
with charachange




emi "ああもう、それ誰のか知ってるよ！"





hi "はあ？"


show eminude wink_ni
with charachange



emi "これ陸上部の部長のだよ！"





"ああ、俺のかつての天敵か。いや、そうでもないか。"







hi "どうして知ってるんだよ？"


show eminude awayfrown_ni
with charachange



"今のは馬鹿な質問だったみたいだ。少なくとも笑美はそう思ってる。"


show eminude frown_ni
with charachange




emi "だって、その人が体育倉庫はこういうことにピッタリの場所だって……なんて言ってたっけかなあ？"


show eminude pout_ni
with charachange



emi "『密会』"





hi "ん？　お前を誘ってたっていうのか？"



show eminude happy_ni
with charachange


"笑美はさらに大きく笑い出す。"



"正直、素っ裸の笑美が笑うさまは妙に綺麗だ。"





"突っ込んだ質問をしたのは俺だけど、会話を切り上げてもとの行為に戻りたいと切実に感じる。"



show eminude closedsmile_ni
with charachange


emi "久夫、その部長ってゲイなんだよ"



"そうかよ。"



hi "ほんとうか？　俺は最初、てっきりお前たちが付き合ってるんだと思ってたぞ"



show eminude awayfrown_ni
with charachange



emi "うーん……入部したときは確かに一目惚れしちゃったんだけど、向こうはそんな気なかったんだ"


show eminude frown_ni
with charachange



emi "当たり前だけど"


show eminude neutral_ni
with charachange


emi "でもいい友達になれたよ、たぶんね"

show eminude grin_ni
with charachange


emi "こういうことはみんなその人に教わったってわけ"


hi "あんまり聞きたくないんだけどさ、"




"掛け値なしの本音だ。それでも聞いてみる。"





hi "それで、なんでその人に、その……ローションがいるんだ？"



hi "つまり、その人は……えーと……"


"笑美はいったいどうやって顔が赤くなるのをおさえてるんだ？"

show eminude wink_ni
with charachange


emi "使ってるってことじゃないの、ほら"

show eminude evil_ni
with charachange



emi "アナルにさ"



"俺は鼻で笑うのをこらえようとする。"



"こらえきれない。"


show eminude happy_ni
with charachange


"笑美もくすくすと笑う。"



hi "で、{b}マジで{/b}お前にそういうことを話してるのか？"



show eminude awayfrown_ni
with charachange


"笑美は肩をすくめる。"

show eminude neutral_ni
with charachange


emi "うん、もちろん"

stop music fadeout 10.0

show eminude closedsmile_ni
with charachange



emi "そういうのが本当に好きみたいなんだ"




emi "何ものにも代えられない気分だってさ"



hi "ああ……そう"



"倉庫のなかの空気が最低な好奇心のようなもので満たされているみたいだ。"



hi "面白いな"



hi "その部長の言葉、信じるしかないよな"


show eminude neutral_ni
with charachange



emi "そうね……"



"表の鳥がさえずるのを止める。"


"風が止む。"


"どこかで、誰かがコーヒーを飲んでいる。そのカップがくちびるに触れたまま停止する。"

show eminude neutral_ni
with charachange


emi "大丈夫だよね……"


extend "たぶん……"

show eminude blush_ni
with charachange


emi "やってみよっか"

play music music_one fadein 5.0




"俺のあごが突然、無意識に外れ、そのまま床に落ちる。"




hi "な、なんだって？"


"笑美はしょげたように後ろ頭をこすりながら、ついに顔を赤らめる。"

show eminude pout_ni
with charachange



emi "えっとさ、昨日の夜にしたこと……今日はできないんだよね"




emi "ちょっとその……あぶない、っていうか？"


show eminude weaksmile_ni
with charachange



emi "ていうか、昨日の夜のあれもちょっとまずかったんだけどね"


show eminude closedsmile_ni
with charachange


emi "だからさ、試してもいいと思うんだ。その、これが……"


hi "いいのかどうか？"

show eminude weaksmile_ni
with charachange


emi "あー、うん。そうだね。そんな感じ"


hi "はあ"

label jp_E21h:

scene evh emi_shed_base1
show emi emi_shed_grin
show hisao emi_shed_neutral
show evh_l emi_shed_up
show evh_r emi_shed_down
with shorttimeskip



emi "気をつけてよね！"




hi "ほんとにやるのか？"




"俺は笑美の後ろに陣取っている。その笑美は肩越しに振り返りながら、なんだか赤くなっている。"




"ほんとうにやるって決めたのなら、もとのムードに戻さないとな。"




"そうして、俺たちはローションのボトルを空けて……"




"こうなっている。"


show emi emi_shed_hesitant
with charachange



emi "やるの！　早くしてよ、冷静になっていろいろ考えすぎちゃう前に"




"笑美の息づかいはまだ少し荒くて、返答ももう待ちきれないという感じだ。"




"それもそうだろうな。あともう少しだったのに、これはなんというか、お預けに近い。"




"俺たちは２人そろって、一時的におかしくなってるんだ。"





"少なくともこの件について、今後はそう主張する。"






"俺は自分が立ち入ろうとしている状況を詳しく考えまいと必死になっている。"




"こんなことがきれいに終わるはずがない。"


show evh emi_shed_base2
show hisao emi_shed_closed
with charachange



"笑美のためと同じくらい、自分のためにも深く息を吸って、ゆっくりと入っていく。"




"抵抗が強い。俺たちのどちらの体も気乗りがしていないかのようだ。"


show emi emi_shed_shock
with hpunch




"笑美の体全体が張り詰める。まだ途中までしか入っていないけど、驚くほど気持ちいい。変な感じもするけど。"






"それに対して、笑美は苦しそうだ。"





"その表情は滑稽でさえある。"



show hisao emi_shed_neutral
with charachange


hi "止めようか？"



"笑美の息がのどでもつれて、答えを返すのに数秒余計にかかってしまう。"


show emi emi_shed_closed
with charachange


emi "だ、だめ、続けて。変な感じがするだけ"


"笑美はくすりと笑う。"




"笑美を責めることはできない。俺自身がちゃんと話せたのだって驚きだ。"



show hisao emi_shed_closed
with charachange


"これは……アツいな。"


"ことさら妙な感じだけど。"



"ローションが不自然にぬらぬらと光る。"




"それを見ていると落ち着かなくなってくる。"




"俺は笑美のなかに入っていく行為に戻って、笑美の息に耳を傾けながらゆっくりと続ける。"


show evh emi_shed_base3
show emi emi_shed_hesitant
with charachange



"根元まで入った俺は停止する。笑美が下唇を噛みながら、また振り返る。"



emi "動いてみないの？　それともこのままぼーっとしてる？"

show hisao emi_shed_neutral
with charachange

hi "いや、慣れさせてやったほうがいいかと思って"



"こんなの無茶苦茶だ。"



"そもそもどうしてこんなことになったんだ？"

show emi emi_shed_grin
with charachange



emi "久夫、こんなの慣れようがないと思う"


show emi emi_shed_hesitant
with charachange



emi "動いてみてよ。そしたら気持ちよくなるかもよ？"



"笑美は疑わしげだけど、間違いなくここまで来て諦めるつもりはないみたいだ。"

show emi emi_shed_closed
with charachange



"ゆっくりと動き始める。笑美が目をつむって新しい刺激に意識を集中しようとしているのを見ると、お互いに上手くいっているみたいだ。"





"リズムに乗ろうとすると、昨日感じたような、意識が薄れていくような感覚を覚え始める。"



show hisao emi_shed_closed
with charachange




"俺も目を閉じて、その感覚の中に自分自身を溶けこませようとする。ただ……"





"なんだかおかしい。"




"笑美は音ひとつ立てない。"




"昨日のことから、笑美は自分が気持ちよくなっているときは、むしろ騒々しいくらいになることを早々に知った。"



show hisao emi_shed_neutral
with charachange


"目を開けると、笑美がこれに馴染もうとしているのが見えるけど、上手くいっているようには見えない。"




"笑美の目は閉じられていて、くちびるを噛んでいるけど、それは気持ちよさからというより我慢しているように見える。"





"『まあ、これは失敗だったけどすぐ終わるよね』という感じの表情だ。"





"俺も少々厄介な状況に陥っている。"






"本音をいうと、やめたくはない。"




"でも同時に、笑美はあまり盛り上がっているように見えないし――もしそうだとしても、俺よりもずっと反応が遅い。"





"申し訳ない気分だ。笑美にだって気持ちよくなって欲しい。"



show evh_r emi_shed_up
show emi emi_shed_shock
with charachange


"片腕を笑美の胸元に伸ばしていじくると、笑美はぎょっとする。"

show hisao emi_shed_sweat
with charachange


"それが笑美の体を強く収縮させ、不意に快感の波をもたらす。"

show evh emi_shed_base4
show hisao emi_shed_neutral
show emi emi_shed_closed
show evh_l emi_shed_down
with charachange




"俺のあえぎが笑美を面白がらせているけど、俺が何気なくもう片方の手を体の前側から下に降ろし、足のあいだの柔らかな毛を優しくなでると、笑美の笑顔もあえぎに変わる。"





"俺自身の腰の動きが早くなり、笑美の前側への愛撫がいつも聞き慣れたあえぎと悲鳴になって行く。"




show hisao emi_shed_sweat
with charachange


"俺は手の感触だけに意識を集中する。片方は滑らかに動き回り、もう片方は敏感でやわらかい、汗をかいて震える鳥肌のたった肌に当てられている。そして笑美は近づく絶頂に身をこわばらせる。"
"そしてとうとう俺ももう――"






"待ってくれ俺もう"


show hisao emi_shed_closed
with charachange


"やばいごめん笑美おれもう"



"俺は最後のひと突きを放つ。指が笑美の乳首をぐっとつまみ、脚と脚のあいだに潜り込む。"


window hide

play sound sfx_flash
with SilentWhiteout(0.1,0.0,0.1)
play sound sfx_flash
with SilentWhiteout(0.1,0.0,0.4)
with GenericWhiteout(0.5,1.0,4.0)

window show


"背中のけいれん、弓なりに跳ね上がる体、壁に反響する女の子らしい高い叫び声。そして俺も絶頂の波が体内のあらゆる感覚をなぎ払っていくのを感じる。"


show evh_l emi_shed_up
show evh_r emi_shed_down
with charachange



"腕が力つきて、笑美は前のめりに倒れこむ。かなり無理矢理に体が離れ、その際に俺の大事なものも引き抜かれる。"



label jp_E21x:

play sound sfx_impact

scene bg school_sportsstoreroom
with vpunch


"とつぜん快感が痛みに切り替わると、俺はバランスを崩して笑美に重なるように倒れこむ。"


stop music fadeout 2.0


emi "わっ！"


hi "おっと"



"俺は素早く笑美を転がして、自分の体を支えると、股間の痛みを無視するために深く息をつく。"






"笑美は転がされて小さく悲鳴をあげる。手持ちのティッシュを何枚かつまみあげると、再びパンティを履く前に後始末をし、壁にふらふらともたれかかる。"







"まだ激しく息をつきながら、俺も笑美の隣で壁に寄りかかって座ることにする。汗をかいた背中に冷たいコンクリートの感触が心地よい。"


show eminude sad_close_ni at center
with charaenter



emi "最後のアレ{b}痛かった{/b}よ！"




hi "そうだな、俺、その……"




hi "やっぱり、やめといたほうがよかったかな"



"笑美は体をよじらせて、俺の傍らであまり痛みを感じることなく座ろうとする。顔をしかめているのを見ると、どうも上手くいっていないようだ。"


show eminude pout_close_ni
with charachange



emi "あーあ、部長に言ってやらなきゃだね"


show eminude angry_close_ni
with charachange



emi "明らかに嘘ついてたんだし"


play music music_ease



"突然、絶対的におかしな状況に気づき、俺は笑いだす。"


show eminude happy_close_ni
with charachange


"笑美もかぶりを振ると、一緒になって笑いだす。"

show eminude grin_close_ni
with charachange


emi "ねえ、久夫"


hi "うん？"

show eminude pout_close_ni
with charachange



emi "もう絶対こんなことしないよね？"



hi "ああ。もう十分好奇心は満たされたからな"



"満足げに笑美はうなずく。"

show eminude closedsmile_close_ni
with charachange


emi "オッケ"

show eminude smile_close_ni
with charachange



emi "もっと基本に忠実に行くべきだと思うんだ、そう思わない？"


show eminude blush_close_ni
with charachange




emi "こういうのってほとんど知らないことばっかりだしさ"




hi "『ほとんど』って何だよ？"

show eminude grin_close_ni
with charachange


"笑美はいたずらっぽく笑う。"

show eminude closedsmile_close_ni
with charachange


emi "教えてあーげない"



"不愉快な考えが頭に浮かぶ。"





"さらに不愉快なのは、笑美にこんなことを聞かなくちゃならないということだ。"





"それでも、たった今やったことの後なら、ちょろいもんだ。"



hi "なあ、流し台ってあるか？"


hi "えーと、その、なんていうか"



hi "ちょっと洗いたいんだけど"


show eminude blush_close_ni
with charachange


"笑美のあごが落っこちる。"


emi "{b}流し台{/b}のなかで？"



hi "だって、他にできる場所なんてないだろ？"




hi "それにその……臭いをどうにかしたいし"



hi "ナースに気づかれるぜ"


"これまででいちばん無様な会話だ。"

show eminude closedsmile_close_ni
with charachange


emi "そうだね"

show eminude grin_close_ni
with charachange


emi "うん、それだったら、あの……裏のほうにあるよ"

show eminude smile_close_ni
with charachange


emi "石鹸もあったと思うよ"


hi "ありがとう"

hide eminude
with charaexit


"確かに小さな石鹸が転がっている。ないよりはましだ。"


"タオルはない。自然に乾かさないといけないのか。"

show eminude grin_ni at center
with charaenter


emi "終わった？"


hi "ああ、もう十分だ。ナースに会った後でシャワーぐらいは浴びたほうがよさそうだけど"

show eminude weaksmile_ni
with charachange


emi "よかった"

show eminude wink_ni
with charachange


emi "じゃあ、服探すの手伝ってよ。君、どっかに放り投げちゃったんだから"


hi "おいおい、お前も同罪だろ！　俺のシャツにあいた穴はどう説明するんだよ？"



show eminude closedsmile_ni
with charachange



emi "あらら、ごめん。さっきはちょっと興奮しすぎちゃったね"



scene bg school_sportsstoreroom
with shorttimeskip



"少し時間がかかったけど、なんとか俺たちはおおむね服を着た状態になる。"





"俺たちは笑美の車椅子がどこにいったか分からなくなって、てんやわんやしていたけど、ドアの向こうにあるのを思い出して、無事救出する。"



show emiwheel neutral_close_ni at center
with charaenter


emi "今度は気をつけてドアを通ってよ？"

show emiwheel awayfrown_close_ni
with charachange


emi "もうでこぼこなんて嫌い"



hi "無茶なことしてほんとごめん"


show emiwheel grin_close_ni
with charachange




"笑美は肩をすくめると、にっこりと笑う。"



show emiwheel wink_close_ni
with charachange


emi "まあ、試す価値はあったよ、ね？"

show emiwheel closedsmile_close_ni
with charachange


emi "それにさ、いい運動だったでしょ？"


"反論はできないな。"

scene bg school_nursehall
with shorttimeskip



"医務室に向かう間、笑美は不快そうに車椅子の上で動き回っている。"


show emiwheel awayfrown
with charachange



emi "ああもう、変な感じ"


show emiwheel neutral
with charachange


emi "車椅子でよかったね、久夫"


hi "なんでだよ？"

show emiwheel weaksmile
with charachange


emi "だってさ、ナースくんになんで変なカッコで歩いてるのか説明する必要ないじゃん"


hi "ああ"


hi "もうやらないからな"

scene bg school_nurseoffice
show nurse fabulous at center
with locationchange




"親切なナースは、少なくとも笑美の肩に残った痕についてはなにも言わなかった。"




"笑美がしきりに車椅子の上でもぞもぞと動いていることについてもだ。"



"気づいていないか、気づきたくなかったのか。"




"どちらにしろ、しばらくの間はナースが俺の薬に青酸を混ぜてないか確認しないとな。"




"念のためだ。"

stop music fadeout 4.0
scene bg school_dormhisao
with locationskip



"あのちょっとした『体験』から体をきれいにしておくために、いつもより長めにシャワーを浴びる。そしてベッドに崩れ落ちる。"





"授業までまだ２０分ある。一眠りできるだろう。"


scene black
with shuteye

label jp_E22:

scene black
with dissolve

with Pause(5.0)

play sound sfx_doorknock


"コンコン。"


"誰だよいったい？"

play sound sfx_doorknock


"コンコン。"


"いたずらじゃなさそうだ。"

play sound sfx_doorknock


"コンコン。"



"誰だって言ってるだろ！"



"それよりも、いまは何時だ？"


"というか、今日は何日だ……？"

scene bg school_dormhisao
with openeyefast



"ノックがまだ止んでいないことと、時刻がすでに昼を回っていることを受けて、俺は突然目覚めのなかに放り出される。"



"学校のある日だ。"



"完全に目が覚めると、どうして仮眠なんかしていたのかを思い出す。"



"武藤先生には言い訳しないほうがよさそうだ。"



"『授業に出なくてすみません、ガールフレンドと性的な実験をしていて疲れ切ってしまって』"






"ああ、バッチリだな。"


play sound sfx_doorknock


"このノックはいつまで続くのかと不思議に思う。"


"出たほうがいいってことかな。"

play sound sfx_dooropen

scene bg school_dormhallway
show kenji tsun at center
with locationchange



"ドアの向こう側の健二を見ても、妙なくらい驚かなかった。"





"ただ、健二のほうが俺に驚いているように見える。"



ke "おいおい、ここで何してやがるんだ？"

play music music_kenji fadein 0.5


hi "ああ、寝てたんだよ"

show kenji neutral
with charachange


"健二は納得したようにうなずく。"

show kenji happy
with charachange



ke "気絶させられたのか。なるほどな"


show kenji tsun
with charachange



ke "あの茨崎とかいうオンナには気をつけろって言ったろ"




ke "用心を怠るとこういうことになるんだ"



"健二は俺の頭の後ろをのぞこうとする。"


show kenji neutral
with charachange

ke "なにかで殴られたりしなかったか？"


ke "薬を盛られたとか？"


hi "さわるな"

with flash


"健二は懐中電灯を取り出すと、俺の目を照らす。"


ke "頭、くらくらしないか？"


hi "別に気絶なんかさせられてない！"

show kenji happy
with charachange



ke "覚えてないだけかもしれないぞ"



"こんな会話は続けても無駄だ。"



hi "いいや、朝から疲れてて眠っちまっただけだ"



show kenji tsun
with charachange



ke "なんでもいいさ"




ke "あくまで否定するっていうなら、止めはしない"




ke "だが、あの女には気をつけろよ。あいつは危険だ"



hi "なんだって？"

show kenji rage
with charachange




ke "一緒にいちゃ危険なんだ。もっともたちの悪いエージェントのひとりだ！"



ke "もっと用心しないと、なにが起こるかわかったもんじゃないぞ！"


ke "あいつはお前よりももっと強い男を打ち倒したんだ！"


hi "なんの話だよいったい？"




hi "あいつはエージェントでもなんでもない、俺を殴りつけてもいない、いいか？"




hi "その誰かを打ち倒したっていうのも嘘なんだろ"

show kenji tsun
with charachange


"健二は腹立たしげな様子だ。"


"なんでかはわからないけど。"


ke "俺を信じないのか？"



ke "そりゃ薄情だぜ、本当に薄情だ"





ke "お前のために目を光らせてるだけなのによ。友達ってそういうもんだろ"





"俺たちが友達？　知らなかったぞ。"



"そうはいっても、健二が友達であることがどういうことなのか知っているのには驚く。"


"そこに立っている健二が、なんだか哀れな気がしてくる。"



"もしかしたら、俺のために目を光らせていると本気で思ってるのかもな。"




hi "わかったわかった"


hi "悪かったよ。注意してくれてありがとな"


"俺は和解の印に手を差し伸べる。"

show kenji neutral_close
with characlose



"健二は慎重にそれを揺する。まるで俺の手に火が付いているかのように。"



"俺の手を揺すりつづけていることに健二が気づくまで、間の抜けた沈黙が少しのあいだ続く。"


show kenji happy_close
with charachange


ke "ところで、助けがいるんだ"



hi "どういう助けだ？　金ないんだけど……"




ke "いや、あるだろ。机の引き出しの下の黒いノートの下に隠してる。非常用に"




hi "俺の部屋を漁ったのか？"

show kenji neutral_close
with charachange


ke "そこは重要じゃない"



ke "それに金はいらないんだ"



"真面目な声色に切り替わる。"

show kenji tsun_close
with charachange


ke "重要な作戦に取り掛かるところなんだ"




ke "俺が正しければ、あの陰謀のすべてを白日の下にさらしてやれるんだ"





ke "だが危険なんだ。だから万が一俺が戻らなかったときのために、お前にやってもらいたいことがある"



hi "ああ、いいけど。なんでも"


"なにをしようっていうんだ？"


"誰かに知らせたほうがいいんだろうか？"

show kenji neutral_close
with charachange



ke "俺が行方不明になったら、３日待ってから俺の日記を新聞に投書するんだ"




ke "日記は俺の部屋の机の引き出しの、二重底の下にある"




hi "どうやってお前の部屋に入るんだよ？　鍵なんて持ってないぞ"


show kenji tsun_close
with charachange



"まるで俺が狂ってるかのように、健二は俺を見やがる。"




ke "じゃあ鍵を破れよ。やり方は知ってるだろ？"





ke "若いうちに知っておくべき重要スキルだろ！"






hi "あー、そうだな、もちろん知ってるよ"




hi "ちゃんとその、それをやればいいんだろ。お前が行方不明になったら"





"健二の日記なんざ読みたくないけど。"



"いずれにしても、健二は俺が協力するのを承諾したことに、かなり嬉しそうだ。"

show kenji happy_close
with charachange


ke "そうだ、そうこなくっちゃな"


ke "じゃあまたな。まだやることがあるんだ"

stop music fadeout 5.0

show kenji happy_close:
    easeout 0.5 xpos 0.7 alpha 0.0
with Pause(0.5)

hide kenji
with None


"健二は駆け足で廊下を下っていってしまう。"



"これが最期といわんばかりだ。"



"あいつの最後の望みを叶えてやる羽目にならなきゃいいけど。"

scene bg school_dormhisao
with locationchange

play sound sfx_doorclose


"頭を振って、ドアを閉めると俺はベッドに戻る。"



"午後の分しか出られないとしても、授業には行かなきゃいけないんだろうけど。"



"今になってのこのこ行くのもなあ……"




"それに、武藤先生から借りたホーキングの本も実際もっと読みたかったし……"





"先生なら分かってくれるだろ。"

with shorttimeskip

play sound sfx_hammer


"コンコン。"


"雑音が俺の意識を本から遠ざける。"



"寝起きのときとあまり変わらないな。"




hi "誰ですか？"




emi "あたしだよ！　嬉しくないの？"


play music music_emi fadein 4.0


"ドア越しのくぐもった声だけど、紛れもなく笑美の声だ。"

play sound sfx_dooropen

scene bg school_dormhallway
show emiwheel smile at center
with locationchange



"俺は飛び起きてドアを開ける。満面の笑みで。"



hi "よお！　また会えて嬉しいぜ！"

show emiwheel grin
with charachange


"笑美も車椅子の上から俺を見上げながら、微笑み返す。"

show emiwheel closedsmile
with charachange


emi "うん。もっと早く会えたかもしれなかったけど、おバカなエレベーターが動かなくって"

show emiwheel pout
with charachange


emi "直るまで待たされちゃったの"

show emiwheel awayfrown
with charachange


emi "ちゃんと整備しておいてくれればよかったんだけど、そうもいかないみたい……"



"俺は笑美の困り顔を、軽く、くすくすと笑うと、部屋に招き入れる。"


scene bg school_dormhisao
with locationchange


"笑美は簡単に車椅子を乗り入れると、俺の手を借りてベッドの上に飛び移る。"

show emi basic_closedgrin:
    center
    ypos 1.0
    easein 0.5 ypos 1.1
with charaenter


emi "ほら。この馬鹿車椅子よりよっぽど快適だよ"


show emi basic_grin:
    ypos 1.1
with charachange



"満足げなため息が宙を舞うと、俺たちは少しのあいだ、お互いを見つめあう。"




"このとき、俺は笑美の目の下のくまに気づく。"



"それほど暗いものじゃないけど、明らかに以前は見られなかったものだ。"



"俺がそれについて聞く前に、笑美はいたずらっぽい目つきを俺に向ける。"

show emi excited_happy
with charachange




emi "それで、今日のお昼のとき君がいないのに気づいちゃってさ"





emi "実際、君のこと一度も見てないしね"

show emi excited_proud
with charachange


emi "なにかあったの、ねえ？"



hi "眠かったんだ"


hi "昼になるまでずっと起きられなくて、やっと健二のやつに起こされたんだ"


show emi excited_amused
with charachange


emi "なににそんなに疲れちゃったのかなあ？"



hi "朝っぱらから激しい運動してね。ちょっとばかり違和感もあったし"



show emi basic_closedhappy
with charachange



"笑美は半分笑って、半分恥ずかしがって、咳払いをする。"



show emi basic_happy
with charachange


emi "あんなのもうゴメンだね"



hi "それでいいさ。正直、俺もあれはなんだか微妙だったし"




hi "これからはああいうことはやめとこう"



hi "なあ、まだ、えーと、痛むのか？"

show emi basic_confused
with charachange


"笑美は信じられないというふうに俺を見る。"


hi "なんだよ？　普通そう思うだろ！"


show emi sad_grin
with charachange




emi "絶対聞かれるなんて思ったこともない系の質問だよ、それ"





hi "まあ、俺だってこんなこと聞かなきゃいけないはめになるなんて思わなかったから、これで引き分けだ"


show emi basic_closedhappy
with charachange


"それを聞いて笑美は笑う。"



emi "あたしも同感、かな？"


stop music fadeout 5.0

show emi sad_shy
with charachange



emi "まあ、聞かれたから答えると、そうかな。まだちょっと痛いや"


show emi sad_pout
with charachange


emi "もうあんなことはやらないよね"


hi "異議なしだ"



"あくびが笑美の口から出ると、俺は眉を吊り上げる。"


hi "疲れたか？"

show emi sad_grin
with charachange


"笑美は眠そうにうなずく。"

play music music_serene fadein 8.0

show emi sad_depressed
with charachange


emi "よく眠れなくってさ"


"よく眠れなかっただって？"


"笑美が、嘘がバレて急いで二の句を継ごうとするみたいにハッとするのを見ると、言葉通りの意味じゃないってことが分かる。"


show emi basic_closedgrin
with charachange


emi "大したことじゃないよ"


hi "どうかしたのか？"

show emi basic_grin
with charachange



"笑美は肩をすくめて説明するのを拒む。"



hi "テストで疲れたんだろ？"


"また肩をすくめるけど、今度はそのまま停止して、おずおずとうなずく。"

show emi sad_shy
with charachange


emi "あー、うん。たぶんね"



emi "それでここに寄ったの"




"笑美の表情がどんどん落ち込んでいく。"





"もちろん気づかれないようにはしている。でも笑美はひざに目を落として、そわそわしている。声も小さい。"




show emi sad_pout
with charachange




emi "あたしたちって、えーと、あんまり一緒にいないほうがいいかもしれない"




hi "はあ？　なんでだよ？"


"笑美は練習していたかのように深く息をつく。"

show emi sad_shy
with charachange


emi "君といると楽しすぎるんだもん"


emi "君の近くにいると集中できないんだ"



emi "テストも近いんだし、あたし……気が散るようなことは避けないと"


show emi sad_depressed
with charachange


emi "でないと、成績下がっちゃう。やばいよ"


hi "勉強なら見てやるぜ……"

show emi sad_grin
with charachange


"笑美は俺に微笑みかける。明らかにこの状況に不満げなようだ。"



emi "できるならぜひそうしてほしいけど、あたしたち二人一緒にいると、実際勉強にならないでしょ？"



show emi sad_shy
with charachange


emi "今だって君としゃべってはいるけど、本当いったら……"


show emi sad_shyblush
with charachange



emi "話す以外のことがしたいし"




hi "ああ"


hi "俺の武骨な男らしさにはうんざりだってか。わかったよ"


show emi basic_grin
with charachange



"少なくとも、その言葉で、笑美を笑顔にはさせられる。"



"笑美は頭を振る。"

show emi basic_closedgrin
with charachange


emi "お馬鹿さん。君は君でしょ"


hi "ふーん。俺ってそんなに魅力的か"

show emi sad_shyblush
with charachange



emi "えーと、まあ多少は。たぶん"


show emi sad_grin
with charachange


emi "ま、そんなところかな、久夫"


emi "君といると本当に楽しいんだ。だからテスト勉強するなら一人でいないと"


hi "ああ、それならいいんだ"



"本当にそのことが気になってたみたいだな。"




"だいいち、まだ２週間しかたってない。それに俺たちはまだ毎日朝と昼には顔を合わせてる。"




hi "学校のなかで会えばいいさ。問題ないよ"




hi "でもってテストが終わったら、お祝いにデートしよう、いいな？"


show emi basic_closedgrin
with charachange


"この提案に喜んで、笑美は微笑む。"

show emi basic_happy
with charachange


emi "もっちろん！　楽しそう！"

show emi excited_amused_close at center
with characlose


"会話を終える合図であるかのように、笑美は俺に寄りかかってキスをする。"


"その日の残りの夜はテストの心配をすることなく過ごした。"


stop music fadeout 2.0

scene black
with dissolve


label jp_E23:

window hide None

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_night fadein 4.0

scene bg school_library_bw
with locationchange

nvl clear
nvl show dissolve



n "\n授業が終わったあとも、笑美と俺がこうも簡単に顔を合わせずにいられることがおかしい。"






n "実のところ、思い切って言ってしまうと、ちょっと不安になる。"







n "付き合い始めるのも簡単だったみたいに、なにごともなく別れてしまったかのようだ。"





n "まあ、実際はそうじゃないのかもしれない。"




n "俺たちはあの夕べ以来、２人揃って落ち込んでいる。"





n "それに、毎朝走る時には顔を合わせている（付け加えるなら、走るときだけだ）。"




n "昼時もだ。特に、昼飯を一緒に食べるのは楽しみにしている。"



n "学校の外では色々なことを話す時間がたっぷりある一方で、朝のランニングはどんどん事務的になっていっている。"




n "体育倉庫で馬鹿をやらかしたことについて、笑美が埋め合わせをしたいからなんだと思う。"





n "でも、どんなに昼飯時に冗談を言い合っているとしても、笑美のことが気がかりになる気持ちを抑えられない。"


nvl clear



n "\n\n笑美は普段よりも気を取られることが多くなったように見える。気が立ったようにそわそわしている様子を一度ならず目撃している。"





n "笑美がそこまでテストのことを深刻に考えるような子だとは思っていなかったけど、間違いなく負担にはなっているみたいだ。"



n "まだ始まってもいないのにな。"



n "これはまだ助走だ。本番前の深呼吸に過ぎない。"




n "明日になれば本当の試練が始まる。"



n "あるいは本当のテストか。"




n "俺はといえば、テストのことはまったく気になっていない。"





n "どうしてかは分からない。いや、試験は大事さ。その成績でいい大学に入れるかどうかが決まるんだから。"





n "まったく、こんな時に天狗になってたら、学歴もふいになりかねないぞ。"




n "でも今のところは、うまく切り抜けられる自信がある。"



nvl clear




n "\n\n\n\n\n\n武藤先生はどのみち俺の科学のテストは万全だと思ってる。"








n "『俺のテストに手こずることはまずないだろう、久夫。お前の実力なら楽勝だ』なんて言っていたし。"





n "とはいえ、武藤先生のことだしな。"






n "先生の褒め言葉は、満点以外は認めないような、妙な含みがある気がして、おかげで必要以上にテストに対して不安になってしまう。"





$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene bg school_library
with locationchange

window show



"そんなわけで俺は放課後の図書室で、じっくりと教科書を読んでいる。"




"ざっと見ればシンプルなものだ。速度を求める公式、摩擦抵抗の話……"



"さんざんだった英語のテストに比べれば簡単だ。外国語はどうもだめだ……"


"もう一度ノートをめくると、俺の意識はさまよい始める。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\n\nテストさえ終われば、肩の荷も降りるだろうな。"


n "そして、俺たちは卒業する。"


n "うまくいけば、大学へ。"



n "笑美が高校を出たあとどうするのかを聞き出そうとしたけど、うまくいかなかったことを思い出す。"





n "うーん、考えてみると、あのときの笑美は巧みにこの話題を避けていたな。"






n "ちぇ。俺が無理に関わろうとすると、笑美はいつも話をごまかしてるな。"







n "それか、俺の気をそらそうとする……他の手段を使って。"






n "何日か前の昼、琳がいなかったときみたいに……"



n "はあ。"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide None
window show None

stop music fadeout 0.2

show yuuko happy_up
with vpunch


yu "ついにやったわ！"



"優子さんの勝利の雄叫びに、俺はうたた寝から叩き起こされる。"



hi "うわっ！"

show yuuko panic_up
with charachange


"俺の驚きに、優子さんは恥ずかしげだ。"

play music music_happiness fadein 2.0


yu "ああ、私ったら！"

show yuuko panic_down
with charachange



yu "ごめんなさい！　私、その――そういうつもりじゃなくて――その、だから――"




"優子さんがどもる間に、俺は優子さんが動揺しすぎないようすぐになだめにかかる。"



hi "まあまあ、ちょっと"


"どうも俺の言葉は届いていないみたいだ。"



"優子さんは取り乱すばかりで、完全にテンパっている。"


show yuuko panic_up
with charachange


yu "ここは図書室だから、私も――"



hi "ちょっと待って、落ち着いてください"



show yuuko cry_down
with charachange


yu "本当に悪い見本だわ、こんなこともできないんじゃ私、クビに――"


hi "優子さん！"

show yuuko worried_up
with charachange



"一喝したのが効いたみたいだ。おかげで勉強している他の何人かの生徒から怒りの矛先を向けられたけど。"



"優子さんはまるで上官に命令を下された兵士のように、ハッとして姿勢を正す。"

show yuuko neurotic_up
with charachange


yu "ごめんなさい！　ごめんなさい！"


hi "大丈夫ですから、落ち着いて"


hi "ちょっと驚いただけですよ、勉強もしないでぼんやりしてたもんだから"




hi "だからおかげで勉強に戻れたんですよ、本当に"




"これは真っ赤な嘘だ。でも効き目はあった。"

show yuuko worried_down
with charachange


"優子さんは大きく息をつくと、少しは落ち着いたようだ。"


"とても親しみのある、怯えたようなオーラを発しながら動き回ってはいるけど。"




hi "それで、何にそんなに興奮してたんです？"

show yuuko neutral_up_close
with characlose



yu "山久に出没するこそ泥！"




"優子さんはとてつもなく嬉しそうだけど、ちゃんと遠慮してひそひそ声で伝えることができた。"



show yuuko closedhappy_up_close
with charachange



yu "犯人の目星が付いたの！"


show yuuko happy_down_close
with charachange



yu "それを知らせる匿名のたれこみがあったのよ！"




yu "それで張り込みをしたんだけど、情報どおりだったみたい！"



hi "本当に？　それで、その、泥棒は誰だったんです？"

show yuuko worried_down_close
with charachange


"優子さんはしっかと頭を振りながら、口を閉じてしまう。"


yu "だめ。君には教えられない"



hi "どうしてです？"


show yuuko worried_up_close
with charachange


yu "これは私と泥棒の問題よ"




yu "私がそいつを追っていることを、君が知らせてしまうかもしれないでしょ"






yu "そいつは早めに手じまいして、高飛びするかもしれない"





yu "そうなったら犯人（ホシ）を確保できなくなっちゃうわ"




"いつからそんなハードボイルド刑事みたいなしゃべり方になったんだ？"



hi "なにもしゃべったりしませんよ！　どうして俺が？"

show yuuko neutral_down
with charadistant


yu "それを聞かなきゃいけないということは、君が知る必要はないってことよ"


hi "よくわからないけど、まあいいです"


hi "おめでとうってことですね？"

show yuuko closedhappy_down
with charachange


yu "ありがとう！"

show yuuko worried_up
with charachange


yu "えーと、なにが？"


hi "え、だから、泥棒？　ですよ"

show yuuko smile_down
with charachange


"優子さんはうなずいて、納得したように微笑む。"



yu "さて！　テスト勉強してる？"






hi "まあ、そのつもりでした。あんまりうまくいってないですけどね"



show yuuko worried_down
with charachange


yu "そうなの？　お探しの本が見つからないとか？"

show yuuko panic_up
with charachange


yu "ごめんなさい！"




yu "もう何週間も本棚の整理をしようと思ってたのに、いつも別のことに気を取られちゃうの！"




yu "本当にごめんなさい！"


hi "ちょっと待ってください"


hi "そういうわけじゃないです。俺の本はここにありますよ"




"それを証明するためと、優子さんを落ち着けるために、俺は教科書を取り出す。"




hi "ぼんやりしてただけ、それだけです"


show yuuko worried_up
with charachange



yu "この騒音のせいかしら？"



yu "もっと騒音には厳しくしようと思ってるんだけど、人を怒鳴りつけるわけにもいかないし……"

show yuuko worried_down
with charachange



yu "というか、私が偉そうにしなくたって、みんな十分大変な思いをして生きてるんじゃないかしら？"




hi "いいえ、騒音も関係ないです。ほんとに"


hi "俺はただ……"


"くそ、どういえばいいんだ。"


"笑美のことを心配していた。"


"俺たちのことを。"


"卒業した後、俺たちになにが起こるのかを。"


hi "最近、笑美のやつが変なんです"

show yuuko worried_up
with charachange


yu "どういうこと？"




hi "なんていうか、俺たちがどんな付き合いをしてるかって知ってます？"





hi "あれで本当に、なんていうか……"




hi "カップルなのかなって。少なくとも友達以上の関係なのかなと"



"そりゃあ友達っていうのは、俺たちのやったようなことはしないけど。"



"肉体的には付き合ってるな。"





"突き合いはしてる、少なくとも。"






hi "笑美のこととか、笑美が将来どういうことをやりたいのか聞こうとすると、決まってはぐらかされるんです"




hi "この前の日も、昼ごはんのときに、俺がいくつか調べた学校のことを話してたんです"





hi "それで俺、聞いたんです。『なにか進学先のことは調べてるのか』って"




hi "そうしたら肩をすくめて、調べてないっていうもんだから、俺がなんで調べてないのか聞くと、『そんな先のことは考えてない』って言うんです"





hi "どうしてそんな考え方してるんだって聞いたら、あいつ……"




"俺はとつぜん、自分が何を言おうとしているのかに気づき、賢明にも口を閉じる。"


show yuuko neutral_up
with charachange


yu "それで？"


hi "えーと、話題を逸らすんです"


hi "それで、それについては話さない"

show yuuko neutral_down
with charachange


yu "なにかあの子が嫌がるような話題だったんじゃないの？"


yu "説明がいるとは思わなかったとか"


hi "ええ、でもそれだけじゃないんです"



hi "なにをそう悩んでるのかと聞こうとするたびに、やっぱり話を逸らしちゃうんです"



hi "俺と一緒にいるのはよくても、あまり近づきたくはないみたいで"







"声に出してみると、さらにいやな気分になる。"




"優子さんがこの断片的な情報を取りまとめる。"

show yuuko worried_down
with charachange




yu "つまりさ、君がその子以上に真剣に考えすぎてるんじゃないかな"





"胃がもつれるように痛むのを感じる。"



"その通りだ。"


"俺はまさにそんなふうだった。"


hi "でも、本当にそうなんでしょうか？　俺……"

show yuuko panic_up
with charachange




yu "ごめんなさい！　わけのわからないこと言っちゃった！"




yu "今のは気にしないで、君も私のこと全然知らないでしょ！"


show yuuko cry_down
with charachange



yu "私はただの司書で、独り身だから、ご想像の通り自分でも何を言ってるのか分かってないの！"




hi "いえ、俺は……"


hi "的を射てると思いますよ"



"それを考えるだけでも傷つくけどな。"




"優子さんはどうにかして、今の言葉のダメージを和らげようとする。"


show yuuko neutral_down
with charachange


yu "えっと、ほら"

show yuuko smile_down
with charachange




yu "たぶん私が間違ってると思うけど、それが明らかな間違いだってことを確認したいなら、とにかくその子と話をするべきかもね？"




yu "２人きりになって、そのことを聞くの"

show yuuko closedhappy_down
with charachange


yu "それから、話題を変えさせないこと！"



hi "ええ、それがよさそうですね"


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve




n "\n\nあるいは、今あるものを楽しんでいるべきなのかもしれない。"





n "なんだかんだで、だらだらと一緒に過ごすのを俺たちは楽しんでる。"



n "走るのもいい。他になにかするのもいい。笑美と話すのはいい……"


n "笑美とこれ以上近しくなる必要なんてあるか？　今のままだって十分いいじゃないか。"


n "でも、それも馬鹿げてるな。"


n "俺は笑美ともっと親しくなりたいんだ。"


n "笑美を悩ませているものが何であろうと、笑美を手助けしてやれるようにもなりたい。"



n "だけど……テストが終わるまでは待つべきかもな。"



n "一旦ストレスから解放されれば、笑美も明るくなるさ。"


n "そうすれば、俺も心配する必要はなくなる。"


n "でも、もしそうならなかったら。"


n "やるときはやってやるさ。"

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl hide dissolve
nvl clear
window show

stop music fadeout 5.0


"優子さんのアドバイスに感謝して、俺は部屋に戻る。"

scene bg school_hallway2
with locationchange


"あそこならもっと勉強にも集中できるだろう。"

scene black
with dissolve


label jp_E24:

scene bg school_hallway3
with locationskip
play music music_tranquil fadein 3.0



"最後のテストを終えると、俺は教室を後にして、ほっと息をつく。"




"願っていた通り、テストはそれほど悪くなかった。どれも難なくこなすことができた。最後の英語を除けば、だけど。"




"でもそれだってまあまあの出来だった。"




"笑美はどうだったのか、気になる。"




"それよりも、笑美の今の調子が気になる。昼飯時に見かけたときはひどい顔をしていたし。"





"いや、車椅子を降りることができたのは大いに喜んでいたけど、でも笑美は疲れ切っていた。"





"何かが笑美を参らせている。その原因がテストだけなのか、俺はいよいよ疑い始めている。"




"そのことについて笑美を問い詰めるべきだろうか？"




"肩を叩かれて、そんな物思いを遮られる。"


show muto smile at center
with charaenter


mu "なあ、久夫"

label jp_choiceE24:
menu:
    with menueffect
    mu "ちょっといいかな？"
    "まあ少しだけなら":




        return m1
    "すみません、他に心配なことがあるので":


        return m2

label jp_E24a:







hi "ええ、時間ならあります。別に急ぎの用とかもないですし"



show muto normal
with charachange



"先生は俺の言葉を疑うかのように眉を吊り上げると、教室に戻るよう合図する。"


hide muto
with charaexit

scene bg school_scienceroom
with locationchange

show muto normal at center
with charaenter


mu "もしよかったら、少し意見を聞きたくてな"



mu "この授業がお前の実力に合ってないのは分かってるんだが……"






hi "平気です。科学部の活動が十二分に埋め合わせになりましたから"



show muto smile
with charachange




mu "ほう、そうか？"



show muto normal
with charachange




mu "まあ実は、ちょうどその件で話がしたくてな"






mu "意味のある活動だったと思うか？　参考までに聞かせてくれ"





hi "まあそうですね。授業でやったことをもっと掘り下げるには有効でした。十分価値がありましたよ"


show muto smile
with charachange


"武藤先生は俺の返答に喜んだようだ。"




mu "それはよかった！　まさにそういうことを期待していたんだ"







mu "なあ、久夫。お前がここに来てくれてよかった。自分の担当科目に深い関心を持ってくれる生徒をもつのはいつだっていいものだ"







mu "ある意味、ほかの生徒を教えるのももう少し耐えられるようになった"






mu "それにお前は頭もいい。アヒルが水に入るみたいに、どんどん吸収していった。他の例え方もあるが"



hi "はあ、どうも"


hi "先生にも随分助けられました。特に大学関係のことは"

show muto normal
with charachange



mu "もう一つあるぞ、久夫"



mu "ちょっとしたアドバイスだ。一人の科学者からもう一人の科学者へ"



hi "なんですか、それ？"


mu "科学者というものはなにをする？"


hi "身の回りの世界を観察します"

show muto smile
with charachange


mu "その通り。いいぞ"

show muto normal
with charachange




mu "簡単な質問だが、ほとんどの人が答えられないような問いでもある。それこそが科学者の本質なんだ、久夫"






mu "そこにあるものを観察し、解明していく"




mu "しかし解き明かせないものがあったら？"




mu "観察できないものがあったとき、科学者はどうするか？"






mu "例えば、誰も実際に見たことがないクォークについてどうやって話せる？　あるいは、直接観察することが不可能なブラックホールのことは？"







hi "うーん、今の機材は技術的に進んでるから…"


show muto irritated
with charachange


"先生はいら立たしげに俺の返答を却下する。"


mu "違う、そういうことじゃないんだ"



mu "それは手段の話だ、俺はお前に考え方を教えたいんだ"


show muto normal
with charachange


mu "考えるんだ。あるものを直に見られないのなら、どうすればそれを観察できる？"


hi "予測するとか？"


mu "どうやってだ？　どうやってクォークの動きを想像できる？　なにを基準にして考える？"



"そりゃそうだ。"



"もっと早く思いつくべきだった。"






hi "それが影響を与えるもので"




show muto smile
with charachange



"先生は興奮したように手を叩いて、感嘆する。"




mu "そう、その通りだ。いいぞ"



mu "それを忘れるなよ"

show muto normal
with charachange




mu "なにかを直接検証できないのは、見方が間違っているからだ"





mu "真実を紐解きたければ、見方を変えることだ。それもままならなければ、それが残したものを見るんだ"




mu "それが科学者たることの本質なんだ。答えを捜し求めるのをやめてはいけない。何も当然と思ってはいけない"



mu "観察し、経験する。そしてさらになにかを観察する"


mu "理解の及ばないことなどたくさんあるんだ、久夫。それを理解できるようにするのがお前の役目だ"




mu "他のことはともかく、それをここで学んでくれたのなら幸いだ"




hi "覚えておきます"

show muto smile
with charachange


"武藤先生は満足げに微笑む。"


mu "よろしい。それでは休暇を楽しんできてくれ。努力の見返りだ"

stop music fadeout 8.0

scene bg school_hallway3
with locationchange


"俺は少しの混乱とともに教室を出る。"


"いったいなんだったんだ？"


"そうはいっても……"



"笑美との件は間違った方向に進んでしまっているのか？"




"笑美が何も言わなかったら、別の手段を使うことができるだろうか？"




label jp_E24b:


hi "すみません、他にやることがあるので……"

show muto normal
with charachange


mu "ん？　そうなのか"


mu "科学部について少し意見を募ろうかと思ったんだがな。まあそれは後になってからでもいい"


mu "休みを満喫するんだ、いいな？"


hi "ありがとうございます"



"ぜひ先生と立ち話をしたいところだけど、いまは別のことが気にかかっている。"



"はっきりいえば、笑美とどうするかということがだ。"


"本当に笑美と向き合えるだろうか？"



label jp_E24c:

scene bg school_dormhisao
with locationskip



"部屋に戻ってからも、その疑問が頭の中をめぐり続ける。"


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\nもし笑美を怒らせてしまったらどうしよう？"




n "それに、全然大したことじゃなかったらどうする？"





n "なにに困っているか話してくれるまで帰らないなんて言ったら、しつこくないだろうか。"





n "こういうことでけんかだの何だのをおっぱじめることは避けたい。"




n "この件は一度引っ込めて、明日また笑美の様子を見てみるまで何もしない方がいいのかも。"







n "そのまま放っておくのはそんなにまずいだろうか？"







n "一緒にいるのが楽しくないってわけじゃないし。"





n "でも、変な話だけど俺は……本当に、笑美を助けてやりたい。"





n "笑美が何の助けを必要としているのか、そもそも助けが必要なことがあるのかさえ、俺にはわからない。"





n "でも助けたいんだ。"


$ renpy.music.set_volume(1.0, 2.0, channel="music")

play sound sfx_doorknock

stop music fadeout 2.0

nvl clear
nvl hide dissolve

window show


"とつぜん、ドアをノックする音に俺は目を覚ます。"

play sound sfx_dooropen

scene bg school_dormhallway
show kenji neutral at center
with locationchange


"ドアを開けると健二の姿が見える。"


hi "なんだ、お前か"

play music music_kenji

show kenji tsun
with charachange



ke "俺かって？　それだけかよ？"




ke "俺がどんな目に遭ってたか、なにを成し遂げたのか少しでもわかってたら、もっと喜んでしかるべきだぞ、お前"




ke "そりゃあもう壮絶だった。『もう二度と出会えない』的なアレだぜ？"




ke "なのにお前ときたら、俺がスーパーで牛乳でも買ってきたみたいなツラしやがって"


show kenji happy
with charachange



ke "お前は冷酷だな、久夫。本気で尊敬するぜ"





hi "あー、まあ、ありがとよ"


show kenji neutral
with charachange



ke "慎重なのはいいことだからな、感情は一切見せたらだめだ"





ke "切り札は最後まで隠しておけよ"






ke "カードを見せるそのときまで、さもなきゃよほど引きが悪いときまではな"





ke "そしてゲームを降りるか、勝ち分を回収するんだ"


show kenji happy
with charachange


ke "わかったか？"


hi "ああ、よーく分かったよ"


hi "おかげで、えーと、任務はうまくいったんだろ？"

show kenji tsun
with charachange


ke "ほほう、ずいぶんと首を突っ込むんだな？"



ke "そんなおおっぴらな言い方したらだめだろうが！　ことは細心の注意を要するんだ！"




ke "ひとつ間違えばドカンだ！　もう侵攻は止められない！"



hi "その陰謀を白日の下にさらしに行くんじゃなかったのか？"



ke "想像以上に大ごとになってる。計画を立て直さないとな"


ke "はべらせておく協力者も少し入れ替えないといけないか"

show kenji happy
with charachange



ke "手伝わねえか？　ウィスキーがあるんだ……出所は秘密だぞ"



ke "調査して分かったことはすべて俺に聞かせてくれよ"


hi "いや、やめとくよ。俺は、ああ……あいつに会うことになっててさ"


hi "もう行かないと。疑われるようなことはしたくないしな"

show kenji neutral
with charachange



"健二は同意するようにうなずく。"





ke "まだ手札は隠すってか？　いいだろう、好きにしな"






ke "グッドラック"



hi "あ、ああ。ありがとな"

hide kenji
with charaexit

stop music fadeout 4.0



"自分の正気を保つために、健二は笑美と話しにいく俺の幸運を願ったんだということにする。"




"ふと考えれば、健二の言っていたカードの例えはどれも当たっている。"



"今こそカードをテーブルに広げるときだ。"





"むしろ笑美にも同じようにさせられるか、だな。"






"なにか決意のような気持ちを持って、俺は笑美の部屋に向かう。"


scene bg school_girlsdormhall
with locationskip

play sound sfx_doorknock2


"階段を力強く登っていき、笑美の部屋のドアをノックする。"


emi "だ、誰？"

play music music_drama fadein 8.0



"ん？　変だな。なんだか息の詰まったような声だ。"




hi "よお、俺だよ。ちょっと立ち寄ったんだ"



emi "久夫？"


emi "入って！"



"俺は手を伸ばしてドアを開けようとするけど、鍵がかかっているのが分かっただけだ。"




"ますます気になるな。"



hi "なあ、鍵かかってるぜ"



emi "あ、うん。ごめん。ちょっと待ってて"

show emi basic_grin:
    tworight
    xpos 0.8
    easein 0.5 tworight
with charaenter


"数分のうちに、笑美はドアを開けてにこやかな笑顔を見せる。"



emi "ごめんごめん。脚を着けなきゃいけなかったから。昼寝してたんだ"




"その笑顔をもってしても、やはりどこかおかしい。"


"笑美の目はわずかに赤い。まるで泣いていたみたいだ。"


hi "いや、大丈夫だよ"


hi "なあ、大丈夫か？"

show emi sad_shy at tworight
with charachange


emi "へ？　もちろん、元気だよ！"


hi "なんだか泣いてたみたいに見えるけど……"



"まったく、久夫。最高の切り出し方だな。"


show emi sad_grin at tworight
with charachange


emi "ええ？　まさか、元気だよ。君に会えて嬉しいぐらいなんだから"

scene ev emi_firstkiss
with flash


"笑美は俺たちの後ろでドアが閉まっても続くような、長いキスで話を中断させる。"




"笑美がこうしたいのは分かるし、俺もそうしたくてたまらないという気持ちを痛いほど自覚してる。だけど……"



scene bg school_dormemi at left
show emi excited_amused_close at center
with locationchange



"今にも俺を殺しにかかりそうな自制心に苛まれながら、俺はくちびるを離す。"



hi "なあ、待ってくれ"

show emi basic_confused_close
with charachange



"困惑で笑美の目元にしわが寄る。"


emi "なに、なにを待つの？"


hi "話がしたいんだ"

show emi sad_grin_close
with charachange


emi "それはこっちの台詞じゃない？"

show emi sad_shy_close
with charachange





emi "それにその台詞言って、いいことあった試しなんてないよね？"





"確かにそのとおりだ。"



"この台詞はふつう別れを告げる前置きで使うんだ。"






"あるいはけんかの前触れだ。"







hi "今回はいいことあるかも知れないぜ"




hi "まあ、願わくば、だけど"

show emi sad_shyblush_close
with charachange



emi "あー……そう"


show emi basic_grin_close
with charachange



emi "せめてベッドの上にしない？　義足つけ始めたばかりだし、まだカンを取り戻してる途中なの"



show emi basic_closedgrin_close
with charachange



emi "それに、ナースくんが義足をつける回数をもっと減らせって。走ってると負担がかかりすぎるから"




hi "異論はないかな"



"これは罠だ。俺たちは２人ともそれを分かってるし、気にもしない。"




"しかし、恋の相手とベッドの上に一緒にいると怒るのがとても難しくなる。そういう腹づもりもあるのかもしれない。"





hide emi
with charaexit

show bg school_dormemi at right
with charamove

show emi basic_grin_close:
    center
    ypos 1.0
    easein 0.5 ypos 1.1
with charaenter


"笑美の義足を横にどけて彼女の隣に座り、腕を肩に回す。"



"俺たちは黙ったまま、しばらくのあいだまたこうして体を寄せあえるようになったことを楽しむ。"




"そしてもちろん、口を開いてそれをぶち壊さないといけない。"



hi "なあ、ここんとこずっと大変だったんだろ、わかるよ"



hi "俺も助けになりたいんだ"





hi "単にテストの事だけだと思ってたけど、部屋に来たら笑美が泣いてたなんて、気になって死にそうだよ"





hi "でも、お前が話してくれなきゃ俺だって手助けできない"


show emi basic_closedgrin_close:
    ypos 1.1
with charachange



emi "言ったでしょ、大丈夫だって"





hi "いいや、大丈夫じゃないね。明らかに何かで悩んでるだろ"







hi "話してくれたっていいんだぜ"





"笑美の声がほんのわずかに張り詰める。"


show emi sad_shy_close
with charachange



emi "あたしが大丈夫って言ってるのに、それじゃ足りないの？"


show emi sad_annoyed_close
with charachange


emi "心配してくれてるんだよね、わかるよ。それはいいの"


emi "でもね、本当に大丈夫なの。君が心配することなんてなにもないんだよ"


hi "寝てもいないで、琳以上にぼーっとしてるのが『大丈夫』とは思えないな"




hi "俺はただ……助けになりたいんだ"



emi "ふーん、そうなの"


hi "ああ、そんなふうになってるお前は見たくないからさ"



hi "もっと元気でいてほしいんだ、わかるだろ？"

show emi basic_annoyed_close
with charachange



"今のはまずかった気がしてくる。なぜなら、笑美は冷たい視線を俺に突き刺してきたから。"




emi "それで、あたしのことを治したいっていうの、久夫？"



"これは間違いなく怒ってるな。"

show emi sad_grit_close
with charachange



emi "白馬の上からあたしを抱え上げて助け出そうってわけ？"





emi "悪夢や幻肢痛も直してくれるの？"



show emi sad_angry_close
with charachange




emi "なくなったものを取り戻してくれるの？"



show emi sad_depressed_close
with charachange


"笑美が言葉を飲み込むと、涙が落ち始める。"


emi "ね、そんなこと{b}できない{/b}の"

show emi sad_pout_close
with charachange


emi "誰にもできない"



emi "誰もそんなことしてくれないよ"



"とつぜんの言葉の抵抗に、俺は固まって言葉を失う。"




"しばらくのあいだ、俺たちはなにも言えずにいる。"


"笑美が俺を押しのけずに、より強く俺を握ってくるのに驚く。"


"笑美は深く息をついたところで、また話しはじめる。"

show emi sad_shy_close
with charachange


emi "あの、ごめんね"

show emi sad_depressed_close
with charachange



emi "あたしね……悪い夢を見るの"



emi "事故のことをね"



"ああ。事故。そうだった。"




"笑美が足を失った事故。もちろん決して話題には上がらないけど。"


show emi sad_pout_close
with charachange



emi "いつもならそのこととは上手く向き合えたの。走れたから"



emi "走ってると、頭のなかが空っぽになっていくみたいだった"


emi "走ってれば、ほかのことを心配する必要なんてなかったんだ"


emi "ただリズムを整えて、呼吸に集中するだけでね"



emi "そのほうが楽だったし。そうやってうまくやってきたの"


show emi sad_shy_close
with charachange



emi "前に進むだけ、わかる？　他のことなんて関係ない、次のコーナーを曲がるだけ"







emi "そしてまた次のカーブ。次も、その次も。もう進めなくなるまで、それ以上考えられなくなるまで、スピードを落として歩いて、また呼吸が落ち着くまで"






emi "そんなことをしてれば、他のことはもうどうでもいいの"


show emi basic_annoyed_close
with charachange



emi "でも、もうずっとこのバカみたいな車椅子から降りられなかったから。ストレス溜まっちゃってさ"


show emi sad_shy_close
with charachange


emi "それで今日は、ちょっとキレちゃったの"




hi "俺に話すこともできたんじゃないのか？"





hi "一人で悩む必要なんてなかったんだよ"

show emi sad_grin_close
with charachange



"笑美は泣きわめく子供を諭すような、悲しげな笑顔を見せる。"





emi "うん、そうだね。確かにそうだよ"





hi "どうしてだ？"


hi "どうして一人で悩まなきゃいけなかったんだ？"


hi "どうして俺をもっと信用して助けさせてくれなかったんだ？"


"また笑顔を見せる。"

show emi excited_amused_close
with charachange

show emi sad_grin_close
with charachange


"笑美は俺にもたれかかって頬にキスをする。母親のような仕草で。"




"告白するかのように、笑美は俺の耳もとに口を近づける。"




show emi sad_shy_close
with charachange



emi "それはね、久夫"






emi "あたしは一度、自分が知っていたもの全部から引き離されちゃったの"




show emi sad_depressed_close
with charachange



emi "またそんなことになったら、どうしたらいいかわかんない"



"話を続けるべきかどうか分からないかのように、笑美は静止する。"


"はらわたに、猛烈な動揺を感じる。"


"笑美は続ける。"

show emi sad_shy_close
with charachange



emi "だから君のことは頼りにできないの"


emi "ナースくんも"


emi "他の誰も"

show emi sad_pout_close
with charachange



emi "あたしだけ"




emi "そうじゃなきゃだめなの"





"この短い告白を終えると、笑美はうつむいて口を手の甲で覆う。"





"これでこの会話は終わりだ。何か言うべきことを探すけど、俺はなにも考えられない。"



hi "俺……"


hi "とりあえず、もう行くよ"


hi "ちょっと……野暮用でさ"


"笑美は顔を上げない。"



"疲れたか、あるいは安心したような声で言う。"



"どっちかは分からない。"




emi "分かった"



emi "その野暮用、済ませてきなよ"



emi "また明日ね"

hide emi
with charaexit

with Pause(0.2)

show bg school_dormemi at left
with charamove


"俺はベッドから降りると、戸口で一旦静止する。"


hi "なあ、笑美……"

show emi sad_shy at tworight
with charaenter


emi "なに？"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve




n "\n\n言いたいことはごまんとある。"





n "でもあまりに混乱していて、どれも口に出せない。"




n "俺を近づける気がないのを笑美が認めたあとで、俺は{b}自分の{/b}世界が俺から引き離されてしまったような気分になる。"





n "事故のときになにが起きたっていうんだ？"




n "足を失くしたのは知っているけど、それを気に病む様子は一度も見ていない。"




n "なにがあったんだ？"




n "好きな人からの助けさえ受け入れられないほど、笑美を怯えさせるものとは一体なんだ？　"




n "俺にはわからない。"


n "\nそれでも知りたい。"



n "答えを拒否されたことが、はらわたにナイフを突き立てられるように感じるくらい、俺は知りたいんだ。"


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve
window show


emi "久夫？"


emi "どうかしたの？"



"俺はまだ戸口で突っ立っている。"



hi "いや、なんでも"


hi "気にしないでくれ"

scene bg school_girlsdormhall
with locationchange

play sound sfx_doorclose
stop music fadeout 6.0


"俺はドアを閉める。"


"廊下を下っている。"


"階段を下りて。"

scene bg school_dormext_full_ni
with locationskip


"ドアを開けて。"


"暗闇のなかへ。"

scene bg school_dormhisao_ni
with locationskip

play music music_night fadein 1.0


"どういうわけか俺は自分の部屋に戻ってくる。脳が猛烈なスピードで、目的もなくはたらいている。"

window hide
nvl clear
nvl show dissolve



n "\n\nどうすればいいのかわからない。"



n "前に進むことはいいことだと思っていた。"



n "変えようのない過去にはあまりこだわらない。今を生きて、未来を見据える。"





n "\n\n今度の……笑美のことの後では、もう自信が持てない。"




n "笑美は本当のことを言っていた。通り過ぎた道のことは忘れて、次のカーブに目を向けるのは簡単だって。"



n "後ろにいる競争相手のことは心配しない。客席にいる観客のことも気にしない。"


n "そして不運にも、遅れをとったチームメイトに注意する暇もない。"

nvl clear
nvl hide dissolve
window show



"俺はベッドに身を投げて、求めている答えがそこに書いてあるかのように天井の角を見つめる。"



"もちろん、そんなはずはない。"

window hide
nvl clear
nvl show dissolve




n "\n\n\n\n\n笑美は文字通りなにかから逃げている――けど俺は笑美と同じように、入院生活のことをどうにかして忘れ去ろうとしてきたんじゃなかったのか？"





n "俺は良くなってるけど、魔法のようにひとりでに病気が治るわけもない。"





n "\n笑美の苦労は俺みたいに心臓じゃなくて２つの足だけど、それだって魔法のように勝手に治ったりはしない。"








n "\nもしかしたら、俺たち二人の仲はここまでしか直らないのかもしれない。"




nvl clear
nvl hide dissolve
window show



"部屋はどんどん暗くなっていき、俺はもはやその角を見ているのかどうかあまりわからなくなっていく。"






label jp_E25:

scene bg school_dormhisao
with shorttimeskip


"朝があっという間にやってくる。まったく眠れなかった。"



"最近の笑美もこうして朝を迎えていたんだろうか？"



"壁を、天井を見つめる。浮かんでくる考えを押し止めようとしながら。"


"笑美のことを考えずにいられない。"



"はらわたを締め付けられるような感覚がまだ残っている。"


window hide
nvl clear
nvl show dissolve



n "\n\n『だから君のことは頼りにできないの』"








n "\nあまりにあっけない言葉。"





n "まるで俺をからかっているかのように、あるいは地球は平らだと主張したことをとがめるかのように。"





n "\n『そうじゃなきゃだめなの』"





n "\nそんなのひどすぎるじゃないか。"



n "自分がみじめすぎて朝のランニングをサボりそうになる。"



n "そんなのは馬鹿げているけど。俺がランニングをしないといけないのは笑美に会うためだけじゃないはずだ。"



n "確かに、最初は笑美に会うためだったかもしれないけど、今はそれだけじゃない。"

nvl clear


n "\n\n\n\nランニングそのものが楽しみになってきている。"





n "血行をよくする方法としては、ましな部類だろうし。"







n "俺がこんなことを言うなんて、あの最初の一週間ちょっとの後では考えもしなかったけど――"




n "\nランニングを終えたときはとても気持ちがいい。その日他に何もできなかったとしても、少なくともそれだけはやり遂げたことになる。"


n "目覚めもすっきりする。笑美も走ってると頭がすっきりすると言ってたけど、俺の頭もすっきりするかもしれない。"



n "\nそう願いたい。"

nvl clear
nvl hide dissolve

scene bg school_track
with locationskip

window show




"朝の空気は少し湿度があるけど、冷たくて澄み渡っている。夏が近づいているみたいだ。"





"トラックにたどり着くと笑美はもうストレッチをしていて、笑顔で手を振って俺を出迎える。"

show emi basic_closedgrin_gym at center
with charaenter


emi "おはよ、久夫！"


"元気の良い笑美を見て、急所を蹴られたような気分になる。"


"昨日のことがあったのになんでそんなに明るくしてられるんだ？"

show emi excited_amused_gym_close
with characlose


"軽く手を振ると、笑美が俺を抱きしめてきて驚いてしまう。"


show emi sad_shy_gym_close
with charachange


emi "ねえ、昨日のことなんだけどさ"


"ほらきた。"

stop music fadeout 1.0

show emi basic_grin_gym_close
with charachange


emi "お礼を言いたかったの"

show emi excited_happy_gym_close
with charachange


emi "実はあたし久しぶりにちゃんと眠れてさ、久夫との話のおかげだと思うから"

show emi basic_closedgrin_gym_close
with charachange


emi "だから、ありがと"

play music music_rain fadein 4.0



"あんな会話のあとでどうすればよく眠れるっていうんだ？"



"昨日笑美がしたのは要するに、俺との距離を縮めるつもりはないという宣言だった。"


"そのおかげでよく眠れた？"


"一体全体何を言ってるのかわからないんですが。"


"笑美は俺の困惑に気づいていないのか、そういう振りをしているのか。"


"もう笑美のことがまったくわからなくなった。"


hi "そっか。役に立ててよかったよ"


"声音に毒が混じりそうだけど、今のところは我慢できている。でも馬鹿なことをしてしまわないうちにさっさと走りはじめたほうがよさそうだ。"

scene bg school_track_on
with locationchange



"笑美も俺と同じくらい走り始めたそうに見えたので、俺たちはすぐにトラックを走り始める。"



"笑美が前よりリラックスして落ち着いているのがわかる。"

scene ev emi_run_face:
    truecenter
    zoom 1.0 subpixel True
    acdc_warp 20.0 zoom 1.1
with flash


"笑美の走りは俺が初めて見たときのように、優雅な動きを取り戻している。"


"ここ数日の乱暴な走りとはあからさまに違う。"


"昨日の会話は本当に効果があったらしい。"


"俺には何の効果もないのが残念だ。"



"俺はランニングのリズムに入り込んでいく。息を落ち着けて足を動かし続けることしか考えられなかったあの頃を思い出す。"




"あの日々はもう過去のものってことかな。"




"少なくとも最初の２周のうちは。"



scene bg school_track_running
with Dissolve(2.0)



"頭を空っぽにできないことにいら立って、俺はペースを上げる。"




"ああ、脚が燃えるような感覚がくる。"



"息はぎこちなくなり、心臓が跳ねる。それは今でも気をつけないといけない症状だ。"


"でも俺の体は強くなっているようだ。血が身体中を駆け巡るのを感じる。"



"鼓動の音が耳を打つ。だけどパニックになったあの雪の日とは違って、俺は高揚感で満たされている。"



"よし、効果は出てる！　俺の心臓は――俺をここに連れてきた欠陥品は、良くなってるんだ。"




"まだ走り続けることができている。そしていつかは、今みたいに色々と心配せずにすむようになるかもしれない。"



"これから笑美とどうしていけばいいのかさっぱり分からないけど、今はどうでもいい。"


"俺の腕と脚がリズムを合わせて動き続ける、それだけが大事なことだ。"


"他のことはどうでもいい。"

show bg school_track_on
with locationchange



"最後の直線に入って俺は気づく。ランニングは確かに役に立ったけど、期待したほどじゃない。"



"確かに気分は良くなったけど、何周か歩いてクールダウンしているうちに俺は昨日の夜のことを思い出し始める。今朝よりは少しだけ冷静に。"




"笑美は俺に距離を置いてほしいと思っている。"




"俺にはそんなの無理だ。"


"別の方法があるはずだ。なにかしら妥協点が。"


"それがなにかはわからない、けど。"



"くそ、なんだよそのおめでたい考えは。"


show emi excited_joy_gym at center
with charaenter


emi "お疲れ様、久夫！　走るのほんとに上手くなったね！"


"お疲れ様。今の俺が望めるのはそれっぽっちだ。違うか？"


"おめでとう、俺。お前はだめなやつだ。"


"俺も態度を変える必要がある。"


hi "ああ、まあな。俺はすごいんだよ"


"だというのに、俺は本音と違うことを言い続けている。"



"すぐに俺も笑美と同じくらい自分の抱えている問題を隠すのが上手になるだろうな。"



show emi basic_closedgrin_gym
with charachange


emi "だといいわね"


"どうして笑美はこんなことをしてくるんだ？　どうしてそんな風に本当に優しい声音で言葉をかけて、俺の心をはずませるんだ？"


"笑美はきっと本気でやってるわけじゃないんだ。本気なわけがない。"


"俺は自分で思ったよりも心を隠すのが下手だったようだ。笑美がじっと俺を見つめてくる。"

show emi basic_confused_gym
with charachange


emi "ねえ、大丈夫？"

show emi basic_hes_gym
with charachange


emi "ナースくんのところに行ったほうがいいんじゃ？"


hi "そうだな、笑美の上に倒れこむのは嫌だし"


"そう言う俺の悲痛な声音に笑美は少しショックを受けたような顔をする。"

show emi basic_shock_gym
with charachange


emi "そんなこと言わないの！"

show emi sad_shy_gym
with charachange


emi "前にも一度倒れてるんだから"


"どうしてそんなに優しく振る舞うんだ？"


"俺のことなんかどうでもいいはずだ。笑美はそれをはっきりさせたんじゃないのか？"


"そんなことを考えるけど、俺は謝っていた。そんな必要はないのだとしても。おそらく笑美は演技をしているだけだとしても。"



hi "悪い悪い、はは"



hi "さあ、ナースのところに行こう"


"ずっと落ち着かないままにナースのところへ向かう。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\n\n\n昨日の夜のことを乗り越えたと思うたびに、笑美が優しげなことを言ったりしたりして、俺は振り出しにもどる。"


n "会話を終わらせようとする笑美の姿がまとわりついて離れない。"



n "笑美と俺はもっと近い関係になれるんじゃないかという希望を奪われたような気分になる、とどめのナイフの一突きのようなやり取りだった。"



n "今の俺たちはどういう関係なんだ？　たまたま体の関係を持った、わずかに友達以上のなにか。"


n "実際のところ、笑美と一緒に過ごすのが楽しくないってわけじゃない。それは前にも言った。"


n "そもそも笑美と何かを育んできたってことすらない。ただ飛び乗って、成り行きに任せただけじゃないか？"

stop music fadeout 2.0

nvl clear
nvl hide dissolve

scene bg school_nursehall
with shorttimeskip

window show



"そんなことを考えているうちに、俺は医務室の前に着いている。ナースが笑美を診察している間も、まだ考え続けている。"




"笑美が跳ねるようにして医務室から出てくると、俺にキスをしてから、どこかへ走り去っていく。きっとシャワーだろう。"



"それに対して、ナースは俺に入るように手招きする。いつもの体のチェックだ。"


$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_nurse fadein 0.5

scene bg school_nurseoffice
show nurse neutral at center
with locationchange


nk "今日はなにかあったかい？"


hi "いいえ。むしろ今までよりちょっと頑張ったくらいですよ。それでも大丈夫そうでした"


show nurse grin
with charachange


nk "そんなに無鉄砲なことをするなんて君らしくないねえ、久夫くん"


nk "笑美ちゃんと長く一緒にいすぎたみたいだね。性格がうつっちゃってるよ。必ずしも良いとはいえないところがね"


"笑美の名前が出て、俺は我慢しきれずついつい不機嫌そうに顔をしかめてしまう。"

show nurse fabulous
with charachange


nk "おや。これは新しいね"

show nurse neutral
with charachange


nk "前まではいつも、笑美ちゃんの名前を出して返ってくるのは笑顔ばかりでしかめっ面じゃなかったんだけど"


show nurse concern
with charachange


nk "本当に何があったんだい？　笑美ちゃんはそんなことなさそうだから気になるんだけど"

show nurse neutral
with charachange


nk "笑美ちゃんは笑美ちゃんでここ何週間かで一番落ち着いた顔をしてるしね。この時期にしては珍しいよ"


hi "それ、どういう意味ですか？"

show nurse fabulous
with charachange


nk "それって？"




hi "『この時期』ってやつです。笑美が一体何に悩んでるのかずっと確かめようとしてるんですが、その話題を持ち出すと途端に口をつぐむんですよ"




hi "昨日なんか、あいつ――"

show nurse neutral
with charachange




nk "当ててあげようか。君のことを信頼するわけにはいかないから、教えないっていうんだろ"





nk "そして君は傷ついた。なぜなら自分たちは笑美ちゃんが考えてるように見える以上の関係だと思っていたから。違うかい？"




hi "まあ、遠からず"


hi "ってなんでわかるんです？"

show nurse grin
with charachange



nk "久夫くん、僕はナースだよ。こういうことを把握するのが仕事さ"


show nurse neutral
with charachange



nk "それに、そういうことをするだろうなとわかるくらいには笑美ちゃんとの付き合いは長いよ。あの子らしい行動なのさ"





"そう言うナースの声音は愛情といら立ちが入り混じったようで、唇からタバコでもぶら下げていたほうが似合いそうだ。"



"そうじゃなくても、ボールペンで同じ事をしそうではある。"

show nurse fabulous
with charachange

label jp_choiceE25:
menu:
    with menueffect
    nk "どうだい、よかったらアドバイスをあげようか？"
    "もちろんですよ":




        return m1
    "いえ、これは俺の問題です":



        return m2


label jp_E25a:







"武藤先生は昨日なんて言っていた？"





"対象そのものを観察できないなら、その周りのものを観察しろ？"


"試してみる価値はある。"


"きっとナースは俺より笑美のことをよく知っているだろう。"


hi "ええ、ぜひ聞きたいですね"


hi "正直、途方に暮れてるっていうか"


hi "どうしていいのかまったくわからないんですよね"

show nurse grin
with charachange


nk "それは思ってもみなかったな"


"そう言いながらナースはニヤリとする。本気で言ってるわけじゃなさそうだ。"

show nurse neutral
with charachange



nk "つまりこういうことだ。笑美ちゃんは……頑固なんだよ"


show nurse grin
with charachange


nk "もう気づいてるはずだけどね。そうじゃなけりゃあまりにも観察力がなさすぎさ。だけどここは疑わしきは罰せず、良いように考えてあげよう"



hi "そりゃどうも"


show nurse neutral
with charachange



nk "ともかく、笑美ちゃんが過去のことを話さないって決意してるんだとしたら、これからもそのことは話さないってことだよ"




nk "笑美ちゃんが何に苛まれてるのか口にしたことがあるかい？　ただのヒントすら聞けたかな？"


hi "事故の悪夢を見てるってことは話してくれましたね……"

show nurse fabulous
with charachange


nk "本当かい？　それは大きな一歩だ。朗報だよ"

show nurse neutral
with charachange


nk "ふむ、笑美ちゃんが馬鹿なことを考えてるんだとしたら、事故について君にちょっと教えるくらいは僕の厳しい不干渉主義にも反さないかな"


show nurse concern
with charachange


nk "もうすぐ笑美ちゃんが事故にあった日がやってくるのさ"


nk "この時期は笑美ちゃんはいつも落ち込むんだ。笑美ちゃんが失ったものを考えれば、トラウマになるような出来事だったんだからね"


hi "それだけじゃないですよ。足をなくしただけだとは思えないんです。何があったんですか？"

show nurse fabulous
with charachange


nk "おっと！　ダメだよ、そこまでは言わない。他の誰かに聞くんだね。そこは複雑な問題だから僕からは言えないよ"

show nurse neutral
with charachange



nk "もし笑美ちゃんが君に知ってほしいと思ってるなら、本人に心の準備ができたら教えてくれるよ"




nk "君は辛抱強く待ってればいいのさ"




hi "でもどうしてわざわざこんな助言をするんですか？"


show nurse grin
with charachange


nk "笑美ちゃんには君がぴったりだからさ。久夫くんはそう思ってないかもしれないけど、笑美ちゃんは君のことを信頼してるよ"


nk "それに、君は今この学校のどの生徒よりもこの時期の笑美ちゃんの助けになってあげられる可能性が高いからね"


show nurse neutral
with charachange


nk "笑美ちゃんは僕が助けようとしても受け入れないだろうけど、久夫くんならヘマをしなければ受け入れてくれるかもしれない"

show nurse fabulous
with charachange


nk "だからしくじるなよ、いいね？"



label jp_E25b:


"アドバイス？　何の？　俺にできることなんて何もないだろう。"


hi "いえ、いいです。何か言ってもらってもどうしようもないと思いますし"

show nurse neutral
with charachange


nk "それはわからないよ"


hi "いえ、俺にもいい考えがあるんです"



hi "笑美はただちょっと意固地になってるだけで、そのことで俺も悩んでるんですけど、まあ乗り越えてみせますよ"


hi "心配しないでください"

show nurse concern
with charachange


"ナースは信じていないようだったけど、肩をすくめる。"


nk "好きにしなよ、久夫くん"



label jp_E25c:

$ renpy.music.set_volume(0.3, 0.0, channel="sound")
play sound sfx_hammer


"返事をしようと口を開くけど、その前にドアを叩く音が聞こえてくる。"


emi "もしもし、まだいるのー？"

show nurse grin
with charachange


nk "ちょっと待っててね"


nk "僕も久夫くんもズボンを履かないといけないから"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorslam

show emi invis:
    tworight
    xpos 1.0
with None

show bg school_nurseoffice at bgleft
show nurse grin at twoleft
show emi basic_annoyed_gym at tworight
with dissolvecharamove


"ドアが勢い良く開くと、入ってきた笑美が刃物のような眼光をナースに向ける。"


emi "どあほっ変態っ"

show nurse fabulous
with charachange


nk "期待させるつもりはなかったんだけどね"


hi "あのー……これから知らない人のふりしていいですかね？"


hi "ところで、どうしたんだ笑美？　何か忘れた？"


"元気な声音に聞こえるように努力する。"


"笑美を怒らせる必要はない。『何事もなかったゲーム』は俺にだってできる。"

show emi sad_grin_gym at tworight
with charachange


emi "実は、久夫に聞き忘れたことがあって"


hi "え？　なんだよ？"

show emi basic_happy_gym
with charachange


emi "一緒にあたしの家にこない？"

show emi basic_closedgrin_gym
with charachange


emi "ママがご馳走を作ってるから、よかったら一緒にどうかなって"

show nurse grin
with charachange


nk "そりゃあ、もちろん行かせてもらうよ"

show emi basic_closedgrin_gym:
    parallel:

        "emi excited_proud_gym" with Dissolve(0.2, alpha=True)
    parallel:
        ease 0.2 xpos 0.6
        ease 0.2 tworight
with Pause(0.5)


"笑美がナースの腕を軽く小突く。"




emi "そっちじゃないわよ、ばか。ナースくんは先週来たでしょ"


show emi sad_grin_gym at tworight
with charachange


emi "久夫に言ってるのよ"

show nurse neutral
with charachange



nk "へえ？　こりゃ面白い！　親御さんにご挨拶かあ！"



hi "絶対行くよ。ありがとう"

show nurse fabulous
with charachange


"ナースは眉を吊り上げるけど、何も言わない。"


emi "よかった！　それじゃあたしは自分の部屋に戻るから、シャワーを浴びて綺麗な服に着替えたら寄ってね。バスで行きましょ"


hi "わかった。んじゃすぐにまた！"

stop music fadeout 2.0

show emi excited_amused_gym_close
with characlose


"今度は俺の番だった。屈みこんで笑美にすばやくキスをしてから、自分の部屋へと駆け出していく。"


scene bg school_dormhisao
with locationskip


"なんて展開だろう。"


"ひょっとしたら結局、俺たちの関係は深まっているのかもしれない。"


"ひょっとしたら笑美は少しだけ心を開いてくれる気になったのかもしれない。"


"それともひょっとしたらこれはただの親切で、食事に招待することで昨日の夜の埋め合わせをするということかもしれない。"



"やれやれ。もはや興奮していいのか、緊張していいのか、落ち込んでいいのかもわからない。"



"俺はその３つが入り混じった気分のまま、シャワー室に駆け込む。"

scene black
with dissolve

$ suppress_window_after_timeskip = True

label jp_E26:

window hide None

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_businterior fadein 2.0

scene ev busride
with locationchange

nvl clear
nvl show dissolve


n "\n\n\n俺はバスに乗るのは好きじゃないほうだと思う。"



n "事実としてそう断言してしまっても問題はない。"



n "よく揺れるし、変な臭いがするし、道路の凸凹が伝わってくる。"



n "とてもじゃないけど楽しめない。"




n "\nついでに笑美の足がガチャガチャという音を立てて、他の乗客たちに注目されてしまっている。"



n "笑美はまたショートパンツを履いている。長い靴下を履いて一目ですぐに義足とわからないようにしているのも前といっしょだ。"


n "だけどそれでも、義足同士がぶつかりあって聞こえるほどの音を立てたときに好奇の目を向けられることは避けられない。"

nvl clear


n "\n\n\n俺がそわそわと席での座り方を変えていると、笑美はいぶかしげに片眉を上げる。"



n "笑美は視線を受けても気にしていないようだ。あるいは、じろじろ見られていることに気づいてすらいないようだ。"





n "笑美は小さいころから好奇の視線に十分すぎるほど晒されてきただろう。そんな時間をしばらく過ごせば、もう気づくこともなくなるのだろう。"






n "\n\n聞いたとしても教えてくれることはないだろうけど。"





n "そしてもう一つ、居心地が悪いのはバスのせいだけじゃない。"




n "笑美は俺を遠ざけようとする一方で、同時に俺を近くに置こうとしている。どうにもその事実に折り合いをつけられない。"



nvl clear



label jp_E26a:


n "\n\n\nそうは見えないかもしれないけど、笑美は俺のことを信頼しているとナースは言った。"



n "だけど俺がナースのことを信頼していいのかどうか、確信が持てない。"



n "ナースも俺と同じように、笑美の味方をしたがる。俺がもし誰かに笑美のことを聞かれたら、俺は笑美がよく思われるように話すはずだ。"


n "\nナースもそうしているだけかもしれない。"



n "\nだけど、さっきのナースは笑美が俺を招待したことに純粋に驚いているようだった。あの表情には何かがあった……"



n "俺が思っている以上に昨日の夜の会話には効果があったということかもしれないけど、俺の心配は消えない。"


label jp_E26b:

stop ambient fadeout 12.0

nvl clear



n "\n\n\n親御さんに会うなんて、大ごとだろ？"



n "笑美のお母さんと会うのが初めてってわけじゃないけど、あれはただの知り合いとしてだった。"


n "でも今度は笑美の彼氏として会う。"



n "心臓が高鳴るのがわかる。雪に包まれたあの日の夕方と同じように。それははるか昔のことに感じられて、まったく別の人生のようだ。"



n "だけどあの時の俺は、何が起きているのかわかっていなかった。みるみるうちに手に負えない事態になるのを抑えるための薬も持っていなかった。"


n "体の健康はずいぶんと回復した。俺はもう普通に生きられるんじゃないかと、少なくとも可能な限り普通に暮らしていくことはできると感じるのは今日これで二回目だ。"



n "\nあとは心臓と同じように笑美との関係さえなんとかできれば、俺は絶好調と言えるだろう。"


stop ambient fadeout 1.5

window hide None

nvl clear
nvl hide dissolve

scene bg city_street4
show emicas smile_close at center
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

window show


emi "よし、ついたよ"

play music music_soothing fadein 2.0



"バスを降りるなり笑美が手をつないでくる。そしてそのまますぐに歩き始める。"


show emicas wink_up_close
with charachange


emi "ほらほら、うちまではもうちょっと歩くよ"


hi "ん？　ああ、わかった"

scene bg city_alley
with locationchange

stop ambient fadeout 12.0


"俺は笑美の堂々とした足取りを眺めながら、その後を追いかける。"


"散歩というにはなんだか速いペースで歩く。"


"早く家に着きたくてたまらないのかもしれない。"


hi "笑美のお母さんはよくこういうことをするのか？"

show emicas neutral_close at center
with charaenter


emi "ううん、あんまり。昔から人を招待したがることってあんまりなかったよ"


hi "そうなのか？"

show emicas awayfrown_close
with charachange


emi "うん、いつも人を呼ぼうって言い出すのはパパだったから"


"急に自分からお父さんに言及する笑美に、俺は不意をつかれる。"



"笑美の表情からは、お父さんに言及するつもりがあったのかはよくわからない。笑美がお父さんについて話すところは一度しか見たことがなかったはずだ。"




"笑美のお母さんが、もうお父さんはいないと教えてくれたことだけは覚えている。"



hi "へえ？　笑美のお母さんは孤独を愛する感じなのか？"

show emicas happy_up_close
with charachange


"笑美が笑い出す。お父さんについて聞かれなかったという安心からか、それとも俺の発言が本当に面白かったのか。"



emi "ぜんっぜん！　あたしが外向的なのは母親似なの"


show emicas closedsmile_close
with charachange


emi "ママはただ人を迎えるより自分から訪ねていくほうが好きなだけよ。そのほうが気楽だから、って言ってる"


hi "自分の彼女のお母さんに会いに行ったことがないからそんなことが言えるんだよ"


"笑美はまた笑うと、からかうような声音で話し始める。"

show emicas wink_close
with charachange


emi "緊張してるの？"

show emicas smile_close
with charachange


emi "そんな必要ないんだからね！　そんな大したことじゃないよ！　ただうちで食事するだけ！"



hi "そうだけど、今までに彼氏を家に連れて行ったことはあるのか？"



"そう言いつつどこかで答えを聞くのを怖がっている自分がいることは認めざるをえない。"



"俺は笑美に昔どんな付き合いがあったのかはほとんど知らない――昔付き合ってた人がいるのかどうかさえも。"


show emicas awayfrown_close
with charachange


emi "ううん、ないはず"

show emicas frown_close
with charachange



emi "あっれえ、これって実は大したことなのかも……"




hi "そりゃよかった、さっきの二倍緊張してきたよ"



"本当のことを言うと、自分が最初だって聞かされてかなり嬉しい。"


"やっぱり俺たちは特別な関係になれたのかもしれない。"

stop ambient
stop music fadeout 10.0

scene bg emi_houseext
with locationchange

play sound sfx_hammer



"さっきの話に元気づけられて、笑美が自宅のドアをノックするころには相当落ち着くことができていた。"


show emicas grin_up at center
with charaenter


emi "ママ、開けて！　連れてきたよ！"

show bg emi_houseext at bgleft
show emicas grin_up at twoleft
with charamove

show meiko smile at tworight
with charaenter


"ドアが開くと、笑美のお母さんは自分の娘にニヤリとした顔を向ける。その表情は驚くほど笑美にそっくりだ。"



"これに慣れるのは絶対無理な気がする。"


show meiko wink
with charachange



emm "あのねえ、普通は大声をあげて呼ぶ前にちょっとくらいは待つものよ"


show emicas pout_up
with charachange


emi "普通のお母さんは娘をすぐに叱るんじゃなくて挨拶くらいするものよ"

show meiko happy
with charachange


emm "ああ、そうね。おかえりなさい、笑美。会いたかったわ"

play music music_another fadein 0.5

scene bg emi_kitchen
with locationchange


"愛に満ちた抱擁のあと、俺たちは中に入る。そうしてようやく笑美のお母さんは俺がいることを思い出したようだ。"

show meiko smile at center
with charaenter


emm "久夫くんもこんにちは。元気にしてた？"



hi "ええ、おかげさまで。しばらく学校のことを心配しなくてよくて、気が楽です"


show meiko happy
with charachange


emm "ああ、試験は終わったのよね？　二人とも肩の荷が下りたでしょう"


hi "はい、ホッとしましたよほんとに"

show bg emi_kitchen at bgright
show meiko happy at tworight
with charamove

show emicas happy at twoleft
with charaenter



emi "あたしも！　それだけで昨日は何週間かぶりに良く寝られたわ"



"そのニュースがもし驚くことだったとしても、笑美のお母さんは驚いたそぶりを見せない。それでも、返事をするその声は興味を隠しきれていない。"


show meiko smile
with charachange



emm "そうなの？　それならよかったわ。あなたがずっと……その、試験のことでピリピリしてたから心配したのよ"




"やはり笑美のお母さんは俺が知らないことを知っている。いやむしろ、笑美が俺に悪夢の件について話したってことを知らないのか。"



"笑美のお母さんが笑美をどうかばうかを観察していると興味深い。笑美が俺に話したくないことは教えないようにするという保護本能がある。"


label jp_E26e:


"今まで気づかなかったけど、笑美はなんだかクォークと似ているなと思う。"



"速く動き、直接観測することでは理解できなくて、でも出会うものみんなに影響を与える。"



label jp_E26f:


"笑美のお母さんは俺が笑美の悪夢については知っていると気づくだろうか？　それともただ誰に対してもすべてを秘密にするだけなんだろうか？"

show emicas weaksmile
with charachange


emi "うん、今年はいつもほどじゃないんだよ。久夫もあたしが集中できるように助けてくれたんだ"



"うん、それは嘘だ。試験期間中は放課後に顔を合わせることさえ一切しなかったじゃないか！"




"だけど……昼間は俺と会っていたのも確かだ。笑美は試験期間中は朝のランニングだけが楽しみだと何度も言っていたし、そんなに嘘というわけでもないかもしれない。"


"どちらにせよ、俺が近くにいたことでわずかでも役に立ったと言われたらちょっとは嬉しく感じる。"



"笑美のお母さんはこの発言に眉をひそめる。笑美の言うことを信じていないのか、それとも俺と同じように驚いているのか。"


show meiko happy
with charachange


emm "そう、あなたたち二人が仲良くなったのは良いことだったみたいね"

show meiko smile
with charachange


emm "久夫くん、うちの子をよろしくねって言うつもりだったけど、もうそうしてくれてるみたいね"


show emicas closedsmile
with charachange


"笑美はその言葉にニヤリとする。俺がこうも簡単に笑美のお母さんに気に入られたことに鼻が高いようだ。"


hi "実は、むしろ面倒を見てくれたのは笑美のほうなんですよ。俺をランニングに連れ出してくれて"


hi "笑美に会ってからずっと活動的になれたと思います。それこそ前よりも……"


"そういうことを考えたこともあまりなかったし、その面白さもわかっていなかった。"


"心臓発作の前はあまり活動的じゃなかった。成り行きでやることがあったサッカーはそんなに頻繁じゃなかったし数のうちに入らない。"


"そして今自分の心臓が弱いことがはっきりとわかって、{b}そうなってから{/b}俺は毎日ランニングをし、薬に助けられながら無理をしている。"


"俺は静かに笑って、自分がしゃべり終えていないことに気づく。"


hi "ええと、心臓発作を起こしてこの学校に入る前よりも、です"


"その言葉はするりと出てきた。自分の欠陥を口にする前にくよくよと考えていた頃もあったのに。"


"だけど今はどうだ？　そんなことを気にするのは馬鹿みたいに思える。特に笑美とそのお母さんの目の前でなんてなおさらだ。"


"笑美が自分の障害のことに無頓着でいられるのなら、俺だってそうできるはずだ。"



"陸上競技会のことを思い返す。笑美は自分のことを足がない人の中で最速だと断言していた。"



"明らかな欠損に、笑美が悩んでいるように見えることはなかった。少なくとも人前では。"




"確かに車椅子を使うことを強いられていたときの笑美はイライラしていた。だけどそれも笑美が自分自身でなんとかしてしまった。俺の努力なんて関係なく。"



show meiko happy
with charachange


emm "この子には他人の活発な面を引き出す力があるのよね。どうやっているのかはさっぱりわからないけど"



"まず笑美にはこの子犬みたいな目があるからな。"


show meiko smile
with charachange


emm "いつものランニングに引っ張りこんだくらいなら驚かないわ"



emm "もし琳ちゃんがあんなに頑固じゃなかったら、笑美はきっとあの子も連れ出して一緒に走らせてたはずよ"



show emicas happy
with charachange


emi "あっ、そうだ！　琳がママによろしく伝えといてってさ"

scene bg emi_dining
with locationchange



"みんなで食事のためダイニングへと移動するうちに、俺はまた会話の中心から外れていく。"



"美味しそうな匂いがする。笑美のお母さんが作ったというスプレッドも素晴らしい。"

show meiko smile at tworight
show emicas happy_up at twoleft
with charaenter


emi "うわっ、作りすぎでしょ！　食堂でも開くの！？"

show meiko happy
with charachange


emm "多すぎたかしら？　まあ、残ったら帰るときに持って帰ってくれていいのよ"


hi "嬉しいです！　しばらく学校の食堂でしか食べてなかったんですよ。家庭料理はちょうど食べたかったんです"

show emicas smile
with charachange



emi "右に同じ。ありがと、ママ"



"香りと同じくらい味も良い。みんな食事をはじめたことで、しばらく会話は小休止となる。"


"笑美はいつものようにおいしそうに皿の上の料理を片付けていく。俺自身もかなりのペースで食べていることは認めざるをえない。"

show meiko wink
with charachange


emm "それで久夫くん、うちの子とずいぶん親しくしてくれてるそうじゃない？"


"『それほどでもないですよ』と言いたい衝動に駆られて口を開くけど、自制しなおす。"


"俺たちが親しいってことは隠せることじゃない。だって、俺をここに連れてきたのは笑美だろう？"


"幸いにも、笑美も笑美のお母さんも俺のその反応を、俺がひどいことを言いかけていたなどとは思わずに俺が不意をつかれたせいだと解釈してくれたようだ。"


hi "まあ、そうですね。それもこれも朝のランニングのせいなんですよ"

show emicas pout_up
with charachange


emi "まるで悪いことみたいに言うのね"

show meiko smile
with charachange


emm "そう、私としては安心したわ"


hi "どうしてですか？"

show meiko worry
with charachange


emm "この子はいつも人気者ではあったけれど、親しい友達はあまり作ったことがなかったから"


"初耳だ。いつも廊下でクラスメートと話している笑美を見てきた。"


"陸上部のみんなだって笑美のことが大好きなようだ。だけど笑美が昼食のときは必ず俺と琳とだけ一緒にいることを選んでいることも確かだ。"



"確かに人気者のすることじゃない。とはいえ俺自身、周囲との距離を縮めたくないという笑美の拒絶を直接経験しているわけだし、そんなに驚きはしない。"


show meiko serious
with charachange



emm "心配し始めてたところだったのよ"


show emicas awayfrown_up
with charachange


"笑美は呆れたように目を回して天井を見つめると、よく聞き取れないことをぶつぶつと口にする。"

stop music fadeout 1.0


hi "え？"

show emicas neutral_up
with charachange


emi "何？"


hi "さっき何て言ったんだ？"

show emicas blush
with charachange


emi "なんでもないよ"

show meiko happy
with charachange


"笑美のお母さんが笑って、飲み物にむせる。"

play music music_comedy fadein 0.5


emm "ナースくんと長く一緒にいすぎたわね、笑美"


emm "私の大事な娘を堕落させた件について話し合いに行く必要があるわ"


hi "なぜでしょう、あまり効果がある気がしないですね"

show emicas evil
with charachange


emi "そもそもほとんどママから教えられたことだよ。ナースくんじゃなくて"

show meiko smile
with charachange


emm "耳を貸しちゃダメよ、久夫くん。うちの子は天性の嘘つきなの"

show emicas awayfrown
with charachange


emi "ふん。はいはいそうですよ"


hi "うーん、わかんないけど、笑美のお母さんの言うとおりかも"

show emicas angry_up
with charachange



emi "何それ？　この裏切り者！　ここはあたしの味方をするところでしょ！"




hi "そうだけどお前、競技会のあとの足の件だって実際嘘を――{w=0.3}{nw}"


with vpunch



extend "いってえ！"



"間違いなく義足から繰り出された蹴りが俺のすねに入って、言葉を遮られる。だけど笑美のお母さんはもうすでに眉をひそめている。"


show meiko serious
with charachange


emm "足がどうしたの？"

show emicas awayfrown
with charachange


emi "大したことじゃないよ……あたしはただ、あー、えっと車椅子だったのよちょっとだけ"


"笑美が最後にモゴモゴと呟いた言葉を、笑美のお母さんはすぐさま解読する――こういうことが前にもあったのかもしれない――そして笑美のお母さんの顔に心配の色が浮かぶ。"

show meiko worry
with charachange


emm "だからナースくんが私の電話を避けつづけてたのね……"


emm "なんてこと……あなた車椅子大嫌いだものね"


emm "気分も落ち込むわけだわ！"

show emicas frown
with charachange


hi "ですよね、車椅子を降りただけではるかに幸せそうっていうか"

show meiko serious
show emicas awayfrown
with charachange


emm "それはそうよ！　車椅子は事故のあとに十分乗ったもの"

show emicas frown
with charachange


hi "義足はすぐには手に入らなかったんですか？"

show meiko worry
show emicas awayfrown
with charachange


emm "ええ。義足に適応するためのセラピーを受けるためにはまず身体が癒えないとだめだったのよ"


emm "特にこの子は歩くだけじゃなくて走りたがってたしね"

show emicas frown
with charachange


hi "知りませんでした"

show emicas weaksmile_up
with charachange


emi "うん、あのときは最悪だったよ。あ、そういえば学園祭のとき琳の壁画は見た？"


"笑美が急に話題を変えたことで、俺と笑美のお母さんが話している間ずっと笑美がそわそわとしていたことに今さら気づく。"


"事故の話になると笑美が少し臆病になることをちゃんと考えるべきだった。たとえ笑美のお母さんの前であってもだ。"


show meiko serious
with charachange


emm "見てないのよ、学園祭には行けなかったから。覚えてないの？"

show meiko happy
with charachange


emm "競技会のときにちらっと見たけどね。なんか奇妙な感じだったわ"

show emicas closedsmile
with charachange


emi "それが琳の狙いみたいなものなんだと思うよ。夢の中みたいな絵にするとか、夢の中みたいな絵にしたいとかたくさん言ってたから"

show meiko smile
with charachange


emm "私に琳ちゃんの絵を理解できる日はこない気がするわ"

show emicas wink
with charachange


emi "そりゃそうだよね。琳自身も人に理解してもらおうと思ってなさそうだしね"

show emicas grin
with charachange


emi "琳は前に、絵っていうのは他の方法じゃ理解できなかったはずのことを理解させてくれるものだって言ってた。だけどそう上手くはいかないとも思ってるみたい"


"それだけの話とはいえ、笑美が琳の意見をちゃんと聞けるくらいに琳と深く話していたということに、俺は驚く。"





"ただ琳が仮にその気になったとして、笑美の意見について同じように話ができるかというと、そうは思えない。"






"もちろん、笑美がわざと俺に何も教えないようにしているんじゃない限りは。ありうることだけど、そんなことは考えたくない。"



"そうしてしばらく不愉快な考えにとらわれているうちに、俺は会話の流れがわからなくなる。"

show meiko serious
with charachange


emm "あのね、ずっと聞こうと思ってたんだけど……"

show emicas neutral
with charachange


emi "うん？"

show meiko worry
with charachange


emm "今年もお父さんに会いに行くの？"

stop music fadeout 3.0



"まるで天気の話でもしているみたいな口振りだ。だけど笑美の反応を見ると、明らかに天気の話なんかじゃない。"


show emicas awayfrown
with charachange


"笑美はたじろいで、頭がぴくっと少し後ろに揺れる。まるで顔でもはたかれたかのように。"

show emicas sad
with charachange


emi "またあとでいい？"


"そういう笑美の声は脆く、張り詰めている。お母さんからの質問にひどく動揺しているかのようにみえる。"


"どうやら笑美のお母さんは俺たちの親密さを見誤ったらしい。"




"俺の前では避けた方がいい話題があるらしい。笑美のお父さんの件もそのひとつだ。"




"笑美が足を失った事故もそうかもしれない。俺が笑美のお母さんとさっき話していたときの笑美の反応に意味があるのだとしたら。"



"笑美のお母さんが自分の失敗を悟るまでに長くはかからなかった。"

show meiko happy
with charachange


emm "もちろんよ。余計なことを言ってごめんね、予定を立てられたらと思って聞いちゃったの"

show emicas neutral
with charachange


emi "いいよ。気にしないで"




"笑美はそわそわしている。まるで自分の反応自体に恥じ入っているかのように。正直笑美の反応は理解に苦しむ。"





"今朝、お父さんのことを話題にしたばかりじゃないか！　まだ何時間も経ってないのに！"



"いつお父さんに会いに行くかというだけの単純な質問に、どうしてそんなに激しい反応をしなければいけないんだ？"


"笑美が昨晩の会話のおかげで得られたと主張していた平穏が、たった今いきなりかき消えたとでもいうのでなければありえない。"



"さもなければあの会話が、笑美が思っていたほどには、あるいは本人が言っていたほどには、役に立たなかったか。"


show emicas weaksmile
with charachange


emi "ちょっと、えっと、席を外すね。おトイレ"

hide emicas
with charaexit

show bg emi_dining at bgleft
show meiko smile at center
with dissolvecharamove


"笑美は急に立ち上がると去っていく。俺と笑美のお母さんだけが残される。"


"俺は少し葛藤する。笑美を追いかけるべきだろうか、それともここに残るべきだろうか？"


"トイレに行きたくて席を立ったんじゃないことは明らかだ。笑美は何かに悩んでいる。俺はそれが何なのかを知る必要がある。"



label jp_choiceE26:
menu:
    with menueffect
    "どうしよう？"
    "追いかける":




        return m1
    "笑美のお母さんと話す":


        return m2

label jp_E26c:




"真相を突き止めるためには、大元に行くしかない。そしてその大元は現在トイレに行かないといけないかのようなふりをしている。"


scene bg emi_kitchen
with locationchange


"俺は断りを入れて中座し、笑美の去った方へ向かう。笑美の姿はトイレではなく、リビングルームのすぐ隣にあるキッチンで見つかる。"

show emicas sad
with charaenter


"笑美はドアを開けっ放しにしていて、近づいてみると笑美がテーブルにしがみついて落ち着きを取り戻そうとしているのがわかる。しかし俺が口を開いた瞬間、笑美の試みは失敗した。"



hi "そんなに急ぎのトイレじゃなかったみたいだな"


show emicas angry
with charachange



"笑美は飛び上がって俺をにらみつける。"


show emicas angry_up
with charachange



emi "ここで何してるの？　あたしは一人になるためにここにきたのに"



hi "笑美の助けになりたいだけさ。すごく悩んでるように見えたから"

show emicas awayfrown
with charachange



emi "なんでもないって言わなかった？　それに、久夫があたしの助けにはなれないってことはハッキリさせたはずでしょ"



hi "いいや、俺たちがハッキリさせたのはお前が頑固だってことだけだ"

show emicas angry
with charachange


emi "久夫がそんなこと言えるの？　あたしをつけてきた人が"


hi "それは別の話だ！　助けになりたいんだ……その問題がなんであれ"

show emicas awayfrown
with charachange




emi "面白いこと言うのね、だって{b}あたしは{/b}ただそっとしておいてほしいだけなのに"





hi "でもどうしてなんだ？　どうして俺を信頼してくれない？"

with charachange



emi "その話ならもうしたでしょ、久夫。あたしは自分でこの問題をなんとかしないといけないの"



hi "そんなの認めるかよ！　笑美は俺の助けが必要なのに、意地でも受け取ろうとしないだけだ！"


"俺の言葉の選び方はどうもおかしくなっている。"

show emicas angry
with charachange


emi "必要？　あたしが久夫の助けなんて{b}必要{/b}だっていうの？"

play music music_tragic fadein 0.5

show emicas angry_up
with charachange


emi "うん、あたしたち会えてよかったよね？　そうじゃなかったらあたしはただの壊れた人間だったんだもんね？"



emi "ううん、最高のことだよね。久夫が現れてあたしの危機を救ってくれたんだからね？　神様はあたしが自分で解決できないって知ってるんだもんね？"



emi "あたしはただのかわいそうな、情緒不安定な壊れた足のない女の子だよね？"



hi "笑美、俺がそんなこと思ってるわけ――"

show emicas angry
with charachange


emi "本当に？　もしそんなこと思ってないんだとしたらあたしが久夫の助けが必要だなんて言いながらここに押しかけてくるはずないと思うけど"


emi "あたしは久夫がいなくても普通の人間として長い間ずっと生きてきたの"



hi "で、俺たちが一緒に過ごした時間は全部どうでもよかったっていうのか？　俺はただたまたま一緒いるだけの男なのか？"


show emicas awayfrown
with charachange



emi "久夫はあたしの彼氏、救世主様じゃない"




hi "ああ、そんなのわかりきってるよ。俺が助けになれるかもしれないって可能性を、お前は考えもしないんだろ？"



hi "笑美はただ問題に蓋をして、ランニングが自分の問題を解決してくれることを祈るだけ。それか俺のところにきて気分が良くなるまで一緒に遊びまわるだけだ"


hi "そんなのは健全じゃないよ、笑美。恋愛関係っていうのはそういうもんじゃない"

show emicas frown
with charachange


emi "でも今のあたしにとってはそれが恋愛関係なの"

show emicas sad
with charachange


emi "あたしだってもし――"


"そこまで言って、笑美は発言を考えなおす。苦しみと疑念が笑美の顔をよぎる。一瞬泣き出すのかと思ってしまう。"

show emicas frown
with charachange


"しかしその一瞬が過ぎると、笑美はふたたび平静を取り戻す。『もし』何なのかは、語られることはないだろう。"


emi "あのね、あたしはただ……今は無理なの"




hi "真剣に話すことが？　俺の話をちゃんと聞くことが？　正直になるのが？　自分と自分の悩み以外のことを少しでも考えることがか？"



show emicas angry_up
with charachange



emi "久夫にあたしの何がわかるっていうの？　何もわからないでしょ！　あたしがどんな苦労をしたか知らないんだから、知ってるふりするのはやめてよ"




hi "笑美が悪夢にうなされてることと、お父さんがいなくなったってことは知ってる。お父さんに何があったんだ？"


show emicas sad_up
with charachange


"まるで顔をはたかれたかのように、笑美の頭がぴくっと後ろに揺れる。笑美の声にもろさのようなものが戻ってくる。"

show emicas sad
with charachange


emi "もういいわ"


"馬鹿げてる。この会話は全部、笑美が俺を拒絶する色んなパターンの寄せ集めでしかなかった。"




hi "なんだよ、質問にも答えてくれないのか？　わかった、じゃあ秘密にしとけよ。俺に言わせりゃ、墓にでも埋めておけばいいさ"



show emicas blush
with charachange


"笑美の瞳がショックで見開かれる。笑美が再び口を開くと、低く恐ろしげな声が出てくる。"

show emicas grit
with charachange


emi "久夫、うちから出ていって"


"急に変わった笑美の声音が、俺の独善的な怒りに冷水を浴びせる。俺は自分が言ってしまったことに気づいて、恐怖がわいてくる。"


hi "笑美、俺はそんなつもりじゃ――"

stop music fadeout 2.0

show emicas angry
with charachange



emi "あたしは{b}出て行け{/b}って言ったのよ"




emi "ママには料理はおいしかったけどうっかり先約があったのを忘れてましたって言って出ていきなさい"




"笑美は身震いしている。怒りに、悲しみに、あるいは決意に打ち震えている。笑美の声は今も低く、抑えられていて、まるで動物のうなり声のようだ。"



"言い過ぎたことを謝ろうと笑美の肩に手を伸ばすけど、笑美は俺の手からサッと離れる。"

show emicas angry_up
with charachange


emi "出ていって"

show bg emi_dining at bgleft
show meiko serious at center
with locationchange



"もうどうしようもない。俺はキッチンを出てリビングルームへ歩いて行くと、笑美のお母さんに謝ってから外に出る。"


$ suppress_window_after_timeskip = True

scene black
with dissolve





label jp_E26d:


"笑美が走り去ってから、テーブルに気まずい沈黙が流れる。何も言うことが思い浮かばない。"

show meiko serious
with charachange


"笑美のお母さんがため息をついて、沈黙が破られる。"

play music music_moonlight fadein 5.0


emm "ごめんなさいね。あの子にもデリケートな話題があるってことをどうしても時々忘れちゃって"


emm "車椅子のことも話しちゃったし……"


hi "追いかけたほうがいいですか？"

show meiko worry
with charachange


emm "絶対にダメよ！　会話を続けたくないから席を外したんだもの"


hi "でも笑美が困ってるなら、誰かが助けないといけないんじゃないですか？"

show meiko serious
with charachange


emm "それが笑美じゃなければ、そのとおりだわ。でもあの子はとことん頑固なの。一人になりたいならそっとしておいてあげるのが一番よ"


emm "そうしないとあの子はきっとあとで後悔するようなことを言ってしまう。あなたもあとで後悔するようなことを言い返してしまうかもしれない"
emm "せっかくの食事会を、誰かが家を飛び出していく形で終わりにしたくはないもの"


show meiko happy
with charachange



emm "こちらからご招待しておいて、そんなことになったら最悪でしょう？　ただでさえ今日はもう恥ずかしいところを見せちゃってるっていうのに"




hi "気にしないでください、俺も車椅子の話を持ち出すべきじゃなかったんです"


show meiko serious
with charachange



"笑美のお母さんは眉をしかめる。さっきの口振り以上に、笑美が怪我のことを自分に黙っていたことを気にしているようだ。"




emm "こういう事はしないでくれたらいいんだけどね。ますます心配になるもの"


hi "よくあることなんですか？"

show meiko smile
with charachange


emm "よくあるって、トイレに走り去ること？　そんなことないわ。それとも怪我を隠すこと？　まあ、それならちょっとは"


emm "嘘をついてることがばれるたびに、笑美は私を安心させようと大したことじゃないから言わなかっただけだって言うのよ"



hi "こんなことが慰めになるかはわかりませんが、俺が怪我を知ってたのは毎日会ってるからってだけですよ"


show meiko happy
with charachange


"そういうと乾いた笑いがテーブルの向こうから聞こえてくる。笑美のお母さんは少し悲しそうにため息をつく。"

show meiko smile
with charachange



emm "人と親しくなることを今でも怖がってるのね？　乗り越えてくれたらとずっと思ってるんだけど"




emm "おかしいわよね。あの子は色んな意味で事故から見事に回復したのに……"


show meiko serious
with charachange


emm "それでも絶対に消えてくれないものはあるのね"



"その表情からして、その事故は笑美のお母さんをもいまだに苦しめ続けているのだろう。"



"でもそばに笑美がいる時よりも事故について話してくれる気はありそうだ。"



hi "質問があるんですけど、よかったら聞いてもいいですか"


show meiko smile
with charachange


emm "あら？"



hi "笑美は事故でほかに何をなくしたんですか？　ナースは毎年事故の日が近づくと笑美がこうなるって言ってましたけど、笑美は話してくれなくて……"


show meiko happy
with charachange


emm "私が教えてあげられると思ったわけね？"


hi "あー、はい。できればですけど"

show meiko serious
with charachange


emm "そのお願いに応えるには問題があるのよ"


hi "ひょっとしてこういうことですか。笑美が知られたくないことは誰にも話さないって約束していて、笑美が俺に知ってほしいかどうかはわからないから教えられない？"



emm "そんなところね。誰かに詳しい話をするのはあの子の口からだけって約束してるから"





hi "でもそれって大事なことじゃないんですか？　事故から長い時間が経ってもこんな状態のままだなんて、明らかに大きな影響を残してますよ"



show meiko worry
with charachange


emm "それはそう。本当に長いあいだ影響が残ってるわ。中にはきっとあの子がずっと完全には克服できないこともあるでしょう"


"一瞬笑美のお母さんは古傷でも疼くかのように、信じられないほど悲しげな顔をする。"



emm "私にだってそういうことはあるけどね……"


show meiko happy
with charachange


"笑美のお母さんはまたしても乾いた笑いを飛ばし、頭を振って回想を払いのける。"

show meiko smile
with charachange


emm "あのね、笑美が事故をどう考えてるかについて絶対に理解しておかないといけないことがあるの"


hi "何ですか？"


emm "あれは大したことじゃなかった"

stop music fadeout 1.0




"どうにか俺は自分の口が驚きでぽかんと開くのをこらえるけど、それなりの努力を要する。"






"こんなに馬鹿げたことは今まで聞いたことがない。"



hi "い、今なんて？"

play music music_sadness fadein 3.0

show meiko serious
with charachange




emm "そうね、そんなに単純ではないかもしれないけど、要約としてはかなり正確なのよ。あの子は、自分は事故に縛り付けられはしないし、事故で失ったものにも縛られないと信じているの"






emm "あの子は『足のない女の子』じゃない。『足がないものの中で最も速いもの』なの。あの子に関する限り、あの楽観主義とエネルギーは事故のあとでも傷一つつかなかったわ"




hi "でもそれどころの問題じゃないんじゃないですか？　だって昨日の夜、笑美は俺を失うのが怖いから俺に頼ることはできないって言ったんですよ"


show meiko smile
with charachange


emm "それほどでもないわ。あなたは笑美が事故のことについて聞いても教えてくれなかったと言ったわよね"


emm "たずねても笑美があなたに事故のことを教えないのは、笑美にとって、それがどうしてもあなたが知る必要があることじゃないからなの"
emm "たとえ他人と親密になりすぎることを恐れたりしてなかったとしても、あの子が事故のことについて語ることはないと思うわ"




hi "俺と親密になりすぎることを恐れてる？"

show meiko happy
with charachange


emm "ああしまった、ええそうよ。事故の後も無傷で残ったものという話はしたけれど、同時にあの子はどんなものも失うときにはいきなり失ってしまうということを強く心に刻み込んでしまったの"

show meiko smile
with charachange



emm "だからあの子は誰かと特別親しくなることは避けようとするし、この件は自分一人では乗り越えられないなんて言いたげな言葉には本気で怒るでしょうね"





hi "だけど笑美一人じゃ{b}無理{/b}だと思います"


show meiko serious
with charachange


emm "そんなことないわよ？　あなた、笑美と勘違いして他の子と付き合ってたんじゃないわよね。私を信じてほしいわ。あの子は自分で乗り越えられます"



hi "でも笑美は何度も悪夢を見てるし、夜もよく眠れないんですよ、それに――"

show meiko smile
with charachange




emm "それにあの子は毎年こうなるのよ。ねえ、あの子が自分一人で乗り越えられないんだとしたら、どうして今も生きてるのかしら？　メロドラマみたいに自殺したり馬鹿げたことをしてしまうと思わない？"





hi "だったら何なんです、笑美の助けになろうとしたらいけないんですか？"

show meiko serious
with charachange


emm "そんなことは言ってないわ！　あの子がこんな風にしているところは見たくないし、あの子が頼れる人がいるとわかったら私も安心できるわ"




emm "ただ、あの子にとって人の助けを受け入れることはあの子の自意識や世界観に完全に反しているってことは理解してほしいの"






emm "それでもあの子を助けたいのなら、あとは久夫くんが決めることよ。正直言うと、そうしてくれたらいいなと思ってる。だけどそれが簡単じゃないってことを伝えないのもどうかしてるからね"


show meiko smile
with charachange


emm "気長にやれば大丈夫よ。あなたはもう山久の誰よりもあの子との距離が近いんだから"


hi "ううん、あまりそんな感じがしないんですが"

show bg emi_dining at center
show meiko serious at tworight
with dissolvecharamove

show emicas evil at twoleft
with charaenter

stop music fadeout 0.3


emi "そう、じゃあ話が簡単になるわね"



"その笑美の声に心臓発作を起こしそうになる。"



hi "うわ！　戻ってきてるのわからなかったぞ"

show emicas angry
with charachange


emi "それはちょうどよかったわ"



hi "おい待てよ、盗み聞きしてたのか？"


show emicas angry_up
with charachange



emi "いーえ。たまたまタイミングよく戻ってきたっていうかね"


show meiko worry
with charachange


emm "笑美、久夫くんはただ――"


"笑美は指を立ててお母さんの言葉を遮る。"

show emicas grit
with charachange



emi "帰るところだった？　うん、知ってる"



"笑美は裏切られたような雰囲気を漂わせながら、怒りに打ち震えている。"



emm "笑美、バカな真似はやめて、私たちはただ――"


show emicas angry_up
with charachange


emi "{b}約束{/b}したでしょ！"

play music music_rain fadein 0.5


"その言葉には、聞いている俺にも耐えがたいほどの痛みが含まれていた。俺が笑美をここまで傷つけてしまうことがありうるという考えに、胃袋を殴られたような気分になる。"



"笑美のお母さんも同じように痛みを感じているようだ。"



emm "約束なら守ったわ！　ねえ聞いて、急に人を追い出していい理由なんてないの"



"笑美のお母さんは感情を爆発させた笑美に怒ると同時に、俺がその光景を見てしまったことを恥ずかしく思っているようだ。"



"解決策は１つしかないな。"



hi "いいんです。帰りますから"


emm "そんな、そこまでする必要はないわよ……"


hi "大丈夫ですから。料理、ごちそうさまでした。アドバイスもありがとうございました"

show meiko serious
with charachange



emm "どういたしまして。デザートをお出しできなくてごめんなさいね"



hi "いえいえ。俺も食べるものには制限があったりしますから"


hi "おやすみなさい、芽衣子さん、笑美"


"形式張った会話をして、俺が帰る用意を始めたことで、笑美の怒りが急速に冷える。"

show emicas frown
with charachange



emi "あ、待って。ごめんなさい。さっきはあたし……あと昨日の夜のあと考えたことが……久夫、帰らなくていいの、取り消すから、帰らなくていいから――"





"俺はついつい少し笑みをこぼす。はっきり言えてないにしても謝ってくれたし、俺もまだここにいたい……"




"だけど今は無理だ。芽衣子さんが言ったこと、そしてこれから俺たちの関係をどうするかを考えなくてはいけない。"


"それに今の笑美の状態で、うっかり笑美をまた怒らせてしまう危険も冒したくはない。"


hi "いや、帰ったほうがよさそうだ。笑美もまだ気が動転してるだろうし、俺もまた助けになりたいとか言いだしちゃうよ。それは嫌だろ？　だから今日のところは帰るよ"

show emicas sad
with charachange


emi "でも――"



hi "おいおい、大したことないって。白馬の王子様はいらないんだろ？　だから１つだけ約束してくれ"


show emicas frown
with charachange


emi "なに？"



hi "お母さんのこと、怒るなよ？　俺にちょっとアドバイスをしてくれてただけなんだから"


show emicas sad
with charachange



"笑美はおずおずとうなずく。まるでこの発言しかすがれるものがないみたいだ。ひどく不安定そうだけど、今の俺にはどうしようもない。"



emi "わかった"


hi "また明日な。朝のランニングで。忘れるなよ！"



"こうして帰ることで笑美を傷つけてしまったのはわかってる。だけど今のままでは笑美にしてやれることは何もない。笑美だって俺に居残って欲しいと自分から認められるほど素直な子じゃないんだ。"



"さっきまでの出来事を消化しようとする笑美の顔にいくつもの表情が浮かぶ。"

show emicas weaksmile
with charachange


"昨日の夜のように、すぐにまた落ち着いた表情があらわれ、必死に何でもないふりをした声が聞こえてくる。"



emi "もちろん。またね"



"今は俺も笑美も、自分の感情を認めたがっていない。俺も強がり続けるのが限界にきていたので、踵を返してドアを出る。"

stop music fadeout 7.0

scene bg emi_houseext
with locationskip



"俺は後ろ手にゆっくりとドアを閉めると、掛け金が閉まるまでドアノブに手をかけたまま少し動きを止める。"





"俺の選択は正しかったのだろうか？　帰らずに残ってことの解決を目指すべきだったのか？"




"いや、それは違う。あんな風に笑美のお母さんの前でやることじゃない。何よりまず昨日の夜に笑美が見せたような怒りを、笑美のお母さんに見せたくはない。"



"どうせ笑美のお母さんはそれくらいのことには慣れているかもしれないけど、笑美には陽気な女の子というイメージのままでいて欲しいと、俺の保護本能が語りかけてくる。"


"自分の手がノブにかかったままになっていることに気づいてはっとする。俺は手をどけてポケットに突っ込むと、ゆっくりと暗さを増していく道を歩き始める。"

scene bg school_dormhisao
with shorttimeskip

play music music_pearly fadein 1.0


"大きく息をつく。"


"朝が来るまでの時間は手強そうだ。"



"どうなるにせよ、笑美になんて言うかは考えないといけない。謝らないといけないし、なんとかして笑美にわかってもらわないといけない。"



"だからこそ、この部屋までの帰り道でずっと気になっていたことがある。"


"岩魚子からの謝罪の手紙。"


"あの手紙を受け取ったときの俺は自分の生活のことで手一杯で、まともに読もうともしなかった。"


"だけどこうして自分が同じような立場にたってみると、好奇心が蘇った。岩魚子が俺にああしてまで伝えたかったこととは何だろうか？"


"少なくとも、岩魚子の考えを読めば自分の考えを整理する助けになるだろう。"


"どこかに投げ捨てたことは覚えている。くそ、どこに投げた？"


"机の下を調べるけど、何も出てこない。仕方がないから手の届きにくい、可能性の低そうな場所を探していく。"


"……"


"うん、片方なくなってた靴下が見つかったぞ。"


"でもまだ手紙は見つからない。"


"ナイトテーブルの下で手を動かそうとして、カサカサとしたものが壁とテーブルの間に挟まっていることに気づく。"


"取りにくさにぶつぶつと文句を言いながら、目的のものに手を伸ばして灯りの下に持ってくる。"


"ビンゴ。"

play sound sfx_paper


scene ev hisao_letter_open_2
with locationchange


"机に座ってくしゃくしゃの紙を広げていく。パチリと机の明かりをつける。"


"意味のない社交辞令は読み飛ばして、前に読むのをやめたところを探す。ああ、あった。"

window hide


$ written_note("他にも言いたいことがあります。冬のあの時から、言わなくちゃいけなかったことがあると思って、こうして手紙を書いています。直接伝えることができなかったのを、本当に後悔しています。言い訳のしようもありません。\n\n\n\n\n")


$ written_note("本当のことを言うと、病院にお見舞いに行くたびに、久夫くんのことが心配になりました。あなたの健康のことじゃありません。あなたはずっと遠ざかって、希望をなくしたように見えました。もちろん、あんなことがあった後では当然だと思います。でもなんだか、あなたはなにかをあきらめたような気がしました。もしかしたら、あきらめたのは「幸せ」だったのかも？\n")

window show


"幸せをあきらめる……"



"不愉快になるくらい聞き覚えがある言葉だ。"


window hide


$ written_note("なんとかして自分の気持ちを伝えたいと思ったけど、それにふさわしい言葉は見つけられませんでした。あなたを慰める言葉を、私は何も言えませんでした。あなたのことがこんなに好きだったのに、一番大事なときに支えることができなくて、本当にごめんなさい。でも少なくとも今は、やっと、もっと自分に正直になれます。\n\n\n\n")


$ written_note("２月と３月の、あの静かな日々に戻れるなら、自分をあきらめないで、とあなたに伝えると思います。きっとそう言います。なんでもいいからあなたに話しかけてさえいれば、こんなに遠くへ行ってしまうこともなかったかもしれません。あなたが自分の力で立ち直れているといいな、と思います。\n\n\n\n")



$ written_note("今の私たちは物理的にも遠く離れてしまっていて、それがなんだかずっと決定的なように感じます。もう一度会うことはできるのかな。もしかしたら、会わないほうがいいのかも？　でも、もし連絡を取りたいと思ったら、ぜひお返事ください。あなたの新しい学校のこととか、今どんな風に過ごしているかとか、とても聞いてみたいです。元気でね。\n\nかしこ、\n岩魚子")



window show


"手紙を読み終わった俺は、丁寧にしわを取ってからそれを机の傍らに置く。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve



n "\n\n\n岩魚子、ありがとう。あの冬の雪の日、俺はお前の告白に『はい』と答えを返すつもりだった。そうはならなかったけれど。"



n "俺たちが再び会うころには、もう手遅れになっていたな。"


n "俺がそう思っていただけかもしれないけど。あの陰気な無菌の病室で、俺がもっと違った振る舞いをしてたらどうなってたんだろうな？"


n "悪い。こんなことを考えてももう何の意味もないな。だけど忘れようとするのも同じように意味がない。"


n "俺が俺なのは、今まで俺に降りかかったすべての出来事があったからだ。これから楽しみにしているすべての出来事があるからだ。現在、未来、過去。"

stop music fadeout 2.0


n "\n\nそしてその過去は俺に大切なことを教えてくれたのかもしれない。"

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear
nvl hide dissolve




label jp_E27:

window hide None

scene black
with dissolve

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show


"目覚まし時計の音が鳴り響き、俺は寝返りを打ってアラームを止める。俺はかすんだ目を開いて天井を見つめる。"

play music music_night fadein 1.0

window hide
nvl clear
nvl show dissolve


n "\n\nこれからどうしよう？　ベッドから起き上がって、校庭に行って、何事もなかったふりをする？"



n "そもそも笑美は来るのか？　昨日のことを考えると、来ない気がする。"




n "それに笑美が来たとして、俺はどうするんだ？　このけんかを乗り越えたとして、次にまた笑美がなにかに悩まされたら同じ事を繰り返すのか？"



n "昨日話し合いを急ぎすぎたことはわかってる。特に笑美のお父さんをだしに使おうとしたのは良くなかった。"



n "でも俺の言ったことはそんなに的はずれだったか？　笑美は絶対に俺を踏み込ませようとせず、そして一人で苦しむはめになる。"




n "俺が何をしようと、何を言おうと、それは変わらない。笑美は変わろうとしない。笑美は俺と距離を取るとすでに心に決めてしまっている。"




n "\n俺は本当に笑美に会いに行くことができるのか？　この状況から前進することができないとわかっていても？"



nvl clear
nvl hide dissolve

scene black
with shuteye

window show


"できない。本当に無理だ。今日はだめだ。俺は寝返りを打って眠りに戻る。"



"どうせ笑美も来ないだろう。"


scene bg school_cafeteria
with shorttimeskip



"昼食の段になっても、同じような内心の葛藤が繰り返されて、俺は一人食堂で食べることにする。"



"笑美に会いたくない。そのことを考えていると気持ちが悪くなる。"

scene bg school_track_ni
with shorttimeskip


"夜、俺はランニングに出る。一人で走るのは競技会のあと笑美が体調を崩したとき以来だ。"


"ナースに見てもらうのはやめる。笑美のことを聞かれるかもしれない。"


"誰かと笑美について話すのもいやだ。"

scene bg school_hallway3
with shorttimeskip


"次の日も、俺は同じことをする。目覚ましは切る。ベッドから出ない。一人で食べて、一人で走る。"


"いつも笑美と過ごしていた時間を埋めるために、本を読む量を増やす。"


"それで驚くほど上手くいっていた。授業の合間に廊下を歩く笑美の姿を見つけて急いでトイレに身を隠すまでは。"



"笑美が俺に気づいても、そんなそぶりは見せない。そもそも笑美が何か変化を見せるとは思わないけど。"



"笑美に元気よく話しかけるクラスの女の子たちに見せるわけがない。"


"陸上部の仲間にも見せるわけがない。"


"特に俺になんて見せるわけがない。"


"目覚ましは切る。ベッドから出ない。"

scene bg school_scienceroom
show muto normal at center
with shorttimeskip


"武藤先生とひも理論が妥当である可能性について長々と話す。個人的には信じられないけど。"



"４次元以上の多次元空間は、納得できる。だけど原子より小さい振動するひもの塊？　それを信じろというのはちょっと無茶だ。"




"だけどそういう風に考えるのは俺だけではないらしい。かつては有力な理論だったけど、今はそれほどではないようだ。"



"武藤先生は、それは単にデータの正しい見方をまだ誰も発見できていないからだと言う。"

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_rooftop

scene bg school_roof
with shorttimeskip


"一人で食べる。"


"今日は屋上には誰もいない。一瞬笑美と琳はどこにいるのかと思ったけど、すぐに忘れる。大事なのはあの二人がここにいないということだ。話さなくて済むんだから。"


"話し相手がいないから、読む本は持ってきてある。"


"ちょっと暑いかもしれないけど、天気は良くなっている。"


"夕方には今より涼しくなるだろう。吹いてきた冷たい風が俺の考えを裏付けてくれるようだ。"

stop ambient fadeout 2.0

scene bg school_track_on_ni
with shorttimeskip


"一人で走る。"



"実際、校庭のほうが涼しい。笑美の姿は見えない。俺としても都合がいい。"



"俺はストレッチをするといつものように走り始める。目の前を走るパートナーがいないことを懸命に考えないようにしながら。"


"ふと余計なことを考えている自分に気づく。あの女の子っぽい笑い方、変わることのない笑顔、丸くて人懐っこい目、引き締まった体――"

scene bg school_track_running_ni
with Dissolve(1.0)


"俺は頭を空っぽにするためにペースを上げる。自分とコーナーの間の距離を一気に食いつぶして、自分の足とそこにある熱以外のことを考えられなくなる速度を求める。"


"最後のコーナーを曲がりながら時計を見やると、今までより速いタイムが出ていることに気づく。"

show bg school_track_on_ni
with Dissolve(2.0)


"鼓動がいつもより少し早いようなので、念のためクールダウンを何周か余分にする。"



"わざわざナースに伝える必要はない。大丈夫だろう。笑美みたいな考え方をしているなと認めざるをえない。"




"いつかは笑美のことばかりこんなに考えるのもやめられると願うしかない。"


scene bg school_dormhisao
with shorttimeskip


"寝る前にまた１つ本を読み終わる。明日は図書室に寄らないといけないな。"

play sound sfx_switch

show bg school_dormhisao_ni
with Dissolve(0.2)

with Pause(0.5)

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 3.5

scene black
with shuteye

window hide

with Pause(2.0)
play sound sfx_alarmclock
scene bg school_dormhisao
with openeye

window show



"自分がどうしてまだ目覚まし時計を早朝にセットし続けているのかわからない。次の朝も同じようにアラームに起こされる。今日も目覚ましをオフにして二度寝する。"


scene bg school_scienceroom
show misha perky_smile at center
with shorttimeskip

play music music_pearly fadein 1.0


"午後、また今日も一人で食堂に向かおうとしていると（古代ペルシアの二人の詐欺師を扱った新しい本を手に入れた。読むのが楽しみでワクワクしている）いきなり誰かに声をかけられる。ミーシャと……"



"なんだ。ミーシャだけか。"


show misha hips_smile
with charachange


mi "また一人で食事するの、ひっちゃん～？"

show misha sign_smile
with charachange



mi "わたしたち、気づいてるんだよ～！"



hi "私たち？"

show misha hips_grin
with charachange


mi "うんうん！　しっちゃんとわたしはひっちゃんが一人で過ごしてる時間が増えたことに気づいたのだ～！"

show misha hips_smile
with charachange


mi "しっちゃんは理由が知りたそうだったから、わたしが聞いてくるよって言ったの！"


hi "静音が自分で聞きにこなかったことに驚いたよ"

show misha perky_smile
with charachange



mi "なにもなければ来たと思うけど、しっちゃんは今のうちに書類仕事を始めておきたかったの。学期末が近づいてるから、仕事がいっぱいあるんだよ～！"




hi "でもなんでいきなり俺の生活に興味がわいたのさ？"

show misha sign_smile
with charachange



mi "あ～、しっちゃんはね～『生徒たちの心の健康を把握するのも生徒会の義務である！　うつ病に陥っちゃう、ゆうけ――有権者を見過ごすのは許されない怠慢なのだ』って言ってたよ"




hi "ああ、なら話は簡単だな。俺は落ち込んでないよ"



show misha perky_confused
with charachange



mi "でもずっと一人で食事してるし、ひっちゃんと笑美が一緒にいるのを見た人はだーれもいないんだよ！　何かあったんじゃないの、ひっちゃん～？"



"ミーシャの声音がわずかに厳しさを増す。だけど言葉の言い終わりにはなぜかいつもの聞き慣れた陽気さがある。"



label jp_choiceE27:
menu:
    with menueffect
    "どう返事したものかわからずに俺は口をすぼめる。"
    "大した問題じゃないと言う":




        return m1
    "降参してミーシャに教える":


        return m2







label jp_E27a:

"個人的な問題を生徒会にさらけだすっていうのは好ましいことじゃない気がする。"



hi "大したことじゃないよ"


show misha cross_frown
with charachange


mi "ひっちゃん、嘘をつくのはよくないよ～！"


"ミーシャは信じようとしない。"



"しかたない、少しは教えてやろう。でも教えすぎないように。"




hi "けんかしたんだ。まだ仲直りしてない"



show misha perky_confused
with charachange


mi "ええ？　どうして？"



hi "それは――なあ、こんなこと話さなくてもいいだろ？"



hi "大したことじゃないんだよ。な？　大丈夫だからさ"

show misha perky_sad
with charachange


mi "じゃあ笑美は？　笑美も大丈夫なの、ひっちゃん？"

stop music fadeout 4.0



"ミーシャの声が明らかに真剣みを帯びる。やってられない。"




hi "知らないよ、そんなこと。聞いてないし。今は事情がややこしいんだよ"


show misha hips_frown
with charachange



mi "なんなのそれ？　ちょっと状況が大変になったからってそこから逃げるっていうの？"


play music music_rain fadein 4.0


"ミーシャからのいきなりの反撃に俺は完全に面食らう。"

show misha cross_frown
with charachange



mi "しっちゃんなら臆病者ってゆーでしょうね、わたしもそう思うよ！"



mi "二人とも仲良かったじゃない！　一緒にいて幸せそうだったじゃない！　ひっちゃんは戦わずに降参しちゃうの？"



mi "自分の彼女のためなら戦わなきゃだめだよ、久夫！"




"ミーシャに静音が乗り移っているようだった。静音が俺の回答に応じて読み上げるための原稿を渡していたと言われても俺は驚かない。"



"ミーシャは腕を横柄に教室のドアに向ける。"

show misha sign_smile
with charachange


mi "今すぐ教室から出て行って仲直りしてきなさい！"


hi "あの、まだ午後の授業があるんだけど……"



"こんな言葉じゃミーシャは納得しそうにない。"


show misha hips_smile
with charachange




mi "じゃあ授業のあと！　でないとひどいことになるよ、ひっちゃん！　そうやってほったらかしにしたらだめなんだから！"




hi "どうして？"

show misha cross_frown
with charachange


"ミーシャは動物のふんを見るような目で俺を見る。"




mi "久夫、笑美のこと大切だと思ってたんでしょ？　それって大事なことじゃないの？"



"やれやれ。そのとおりだ。"



"思ってた……今でもそう思ってる。"



"そうだろ？"


hi "わかったよ。授業が終わったら会いに行く"

show misha hips_grin
with charachange


mi "それでいいのよ～！　しっちゃんにも大丈夫だって伝えておくね～！"


"ミーシャの陽気さが戻ってくる。もう俺に怒ってはいないということなんだろう。"

hide misha
with charaexit


"ミーシャが手を振って廊下を歩いて行き、俺は昼食を取る。"

scene bg school_scienceroom
with shorttimeskip


"午後の授業が終わりに近づき、俺はこの先に待ち構えている仕事に備える。"


"俺は笑美に会わないといけない。少なくともそこはミーシャが正しかった。笑美と俺の問題を未解決のままにしておいてもどうにもならない。"


"少なくとも、俺は自分の発言について謝らないといけない。"


"笑美の部屋に行くことも考えてみるけど、笑美はきっとまだ運動場にいるだろう。"

scene bg school_courtyard
with locationskip


"本校舎から出て運動場へ向かうにつれて、自分の命運が尽きているような気がしてくる。"



"何もかもが間違った方向に行ってしまうんじゃないかと、自分は何も成し得ないんじゃないかという、ねじくれたひどい予感を腹に感じる。"





"昔の俺たちが持っていたものが入っている棺桶に最後の釘を打ち込むくらいのことはできるかもしれないけど。"



stop music fadeout 2.0

scene bg school_track
with locationskip


"笑美はやはりいた。他の奴らがみんなシャワーやご飯のために帰ったあとも、トラックを走り続けている。"


"俺は手を振ることはせず、笑美に気づいてもらおうとすることすらしない。観客席に座って、笑美が走るのをただ眺める。"

show emi basic_confused_gym:
    center
    xpos 0.6
    easein 0.5 xpos 0.5
with charaenter


"トラックを何周かしたころ、笑美はようやく俺に気づく。横滑りで足を止めて、驚きで目を見開く。"

show emi basic_annoyed_gym at center
with charachange

show emi basic_grin_gym
with charachange


"驚きはすぐに怒りで覆い尽くされる。しかしそれもまたすぐに俺がよく知っている頑強な仮面の奥へと消えていく。"


emi "何してるのよ？"


"待ち望んでいた反応ではない。だけどもう俺に選択肢はない。"


hi "このまえ言ったことを謝りたくて"

show emi basic_confused_gym
with charachange


emi "このまえ？"

show emi basic_closedgrin_gym
with charachange



"笑美は笑い出す。信じられないものを見たような驚きを、ぶっきらぼうに伝えてくる。"


play music music_sadness fadein 0.5

show emi basic_grin_gym
with charachange



emi "もう１週間近く経ってるんだけど、久夫"



hi "そうだな、でも……何もしないよりましだろ？"

show emi sad_annoyed_gym
with charachange


"笑美は腕を組んで冷ややかに見つめてくる。まるで俺を品定めするかのように。やがて笑美がうなずく。"

show emi sad_grin_gym
with charachange


emi "ふん。それもそうね。じゃあ水に流しましょう。許すわ"

show emi basic_grin_gym
with charachange


emi "それだけ？"

show emi basic_grin_gym:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None


"そのせっかちとも言える質問に俺が不意を突かれているうちに笑美は競技トラックへと足を進めていて、俺はあわてて声をかける。"


hi "待ってくれ！"

show emi basic_annoyed_gym:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter


"笑美は足を止めると、踵を返してこちらへ戻ってくる。息は少し荒く、俺が呼び止めたことに怒っているような顔をしている。"


emi "何よ？"


"さて、なんとかして決着をつけないといけない。自分の立場を見誤ったらいけないし、あわよくば仲直りしないといけない。"


hi "せめて座ろうか？"

show emi sad_annoyed_gym at center
with charachange


emi "このまま話せばいいと思うけど"



hi "ああ、うん。それで、俺たちのことだけど……"



"俺は一息ついて、自分の言いたいことにうまい言い方がないかと考える。"


"しかし俺がもう一度チャンスをくれと必死に乞い始めるその前に、笑美はもう口を開いていた。"

show emi sad_shy_gym
with charachange


emi "『俺たち』なんてもうないのよ、久夫"


hi "どういうことだよ？"

show emi sad_pout_gym
with charachange


emi "あたしたちは合わないの"


"笑美はそんなとんでもないことを、俺と目を合わせようともせずに口にする。"



hi "そんなわけないだろ！　俺たちはお互いぴったりだよ！"


show emi basic_annoyed_gym
with charachange


emi "『先週は家から追い出されてごめんなさい』なんて謝ってる人がそんなことを言うのね"



hi "あれはけんかだっただろ！　俺は本当に信じられないくらい馬鹿なことを言っちまったからそのことを謝ったんだ！"


show emi sad_angry_gym
with charachange



emi "じゃあそのけんかを始める原因になった話、あたしたちはどれだけ繰り返してるの？　あたしがこの一線を超えるつもりはないって何度言って、久夫がそれを何度超えてこようとしたと思ってるの？"




hi "お前のその一線が馬鹿げてたからだよ！"


show emi sad_annoyed_gym
with charachange



"笑美は呆れたように目を回すと、胸の前で腕組みをして、首を横にかしげる。"



emi "久夫、わかる？　だからあたしたちは合わないって言ってるのよ！"



"笑美の声が少しやわらかくなる。笑美が手を伸ばしてきたかと思うと、俺の頬をなでる。"

show emi sad_grin_gym_close
with characlose



emi "君はいい人だよ。でもあたしたちじゃ上手くいかないの"



"雷に打たれたように、笑美はこの一連の流れを練習していたんだと気づく。ひょっとすれば俺が笑美の家から去ったときから毎日。"



"あの頬を撫でる動きさえ、まるで映画の一場面のごとく前もって練習していたかのようだ。"



"笑美には俺にもう一度チャンスを与えるつもりなんてなかったんだ。"


"くそっ、あのまま俺と二度と会うことがなかったとしても平気だったんだろう。"



hi "じゃあ終わりなんだな？　『あー、あの時は楽しかったよ、でもさよならな』だけで終わりで、他に言うことは何もないんだな？"


show emi basic_closedgrin_gym_close
with charachange


"俺のその返事は、俺が意図したよりはるかに笑美を面白がらせたようだ。笑美は病的な笑い声をこぼす。"


emi "あたしはそうやって生きてきたの。久夫ももう知ってるはずでしょ"

show emi sad_grin_gym_close
with charachange


emi "楽しかったよ"


"悲しい笑顔だ。笑美がかすかに震えて、笑顔が消える。"

show emi sad_shy_gym_close
with charachange


emi "でもそれは終わり。これで良かったんだよ"


"叫び出したい。笑美を怒鳴りつけて、こんなのは馬鹿げていると、何もかも馬鹿げているとわからせたい。お前は俺を怖がっているだけだ、誰かとの距離を縮めることを恐れているだけだと。"


"俺はお前のことを愛していると、お前をすぐに諦めることなんてできないと伝えたい。"


"だけど……それは意味がない。笑美はもう心を決めてしまっている。俺たちはおしまいなんだ。"


hi "わかった"

show emi sad_grin_gym_close
with charachange


"笑美が満足したようにうなずく。俺は物に当たりたくなる。"


emi "よかった"

show emi basic_grin_gym_close
with charachange


"笑美は顔を明るくして空元気を作る。"


emi "またね、久夫"



hi "うそだな。もう俺と顔を合わせる気もないだろ"


show emi basic_grin_gym_close:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None



"『好きにすれば』とでも言うかのように笑美は肩をすくめて、再び俺に背を向けると、見る見るうちに加速してトラックのカーブを曲がっていく。"



"何も感じない。終わってしまった。ここが何なのかはともかく、俺たちの道はここで途絶えている。少なくとも、ここから先は通行止めだ。"


"笑美は俺にもう一度目をくれることもなく、トラックで周回を重ねている。その走りはさっきよりはるかに早く、初めて一緒に走った時のことを思い出さずにいられない。"


"自分が思っているほど弱くはないのだと証明しようと、必死にお前に追いつこうと走った。だけど結果はひどいものだったよな？"



"そして今、お前はまた俺に追いつけないほどの早さで走っている。俺にもまた、お前の後を追いかけるという選択肢がある。"


"でもそうはしないよ。今度はそうはしない。お前は俺に追いつかせてくれやしないだろうから。"

stop music fadeout 6.0

scene bg school_dormhisao
with shorttimeskip


"何も意識しないままに、運動場から立ち去り、自分の部屋へと戻り、かばんから読むための本を取り出す。"



"そしてベッドの前で、目覚ましの時間を変える。俺たちの最後の逢瀬は終わった。"


scene black
with shuteye



"それきり、俺たちは二度と話さなかった。"






label jp_E27b:



"まあ、他に俺の問題を知っているやつがいても損はないだろう。ミーシャがアドバイスをくれることだってあるかもしれない。"



hi "笑美の家でけんかをしてさ"





hi "俺は笑美との距離をもっと縮めようとしてるんだけど、笑美はそうさせてくれなくて、それで……"





hi "俺は馬鹿なことを言っちまって、笑美に家から放り出されたんだ"


show misha perky_sad
with charachange



mi "それから笑美とは話したの？"



"ミーシャは純粋に心配してくれているように見える。驚きだ。どういう問題かわかったらミーシャはすぐにこの話題をやめるだろうとほとんど確信していたのに。"



"もっと驚きなのは、自分がこうもあっさりミーシャに全部を話してしまっていることだけど。"



hi "いや、まだ話してない。どうしてもあれから笑美と会う踏ん切りがつかなくて"



hi "俺は本当に恥ずかしいことをしたし、どうせ笑美ももう俺のことを嫌いになってるだろうから。あれからずっと会ってないし、なおさらさ"


show misha sign_smile
with charachange



mi "ひっちゃんって、すっっごく鈍感だね"


stop music fadeout 4.0



"今のはアドバイスには聞こえないけど。"



hi "え？"

show misha hips_frown
with charachange



"ミーシャは腰に手を当てると、静音が喋っていたほうが似合いそうな話を始める。"




mi "答えは単純！　笑美に会って謝らなきゃだめ！　こんな風に何もしないでいたら事態は悪くなるだけだよ！"




mi "本人から聞かない限り、笑美がひっちゃんのことを嫌いかどうかなんてわからないでしょ！　ひっちゃんが怖がってることには根拠がないの！"





mi "それに本当に笑美のことが大切だと思ってるなら、こんなことになって笑美がどういう気持ちか心配しないといけないんじゃないの？"


play music music_innocence fadein 1.0


"その通りだ、とハッとする。心のどこかで笑美と一緒に走りたいと思っていたからこそ、朝の目覚ましをセットし続けていたんだ。"



"健康にしていないと笑美が心配することがわかっていたからこそランニングを続けていた。"



"昨日屋上に行った時も、笑美がそこにいるんじゃないかとどこかで期待していたし、いないとわかってがっかりした。"



hi "馬鹿だな、俺"


show misha hips_grin
with charachange


mi "かもね、ひっちゃん～！"

show misha sign_smile
with charachange




mi "だから～！　できるだけ早く謝りに行くの。わかった～？"




"俺は今すぐそうするよと言おうと口を開くけど、昼休みの予鈴が鳴って、まだ午後の授業が残っていることに気づく。"


hi "授業が終わったら一番に会いに行くよ。約束する"


hi "それと、あー、アドバイスありがとうな"

show misha hips_grin
with charachange


"ミーシャは俺に、まるでひらがなを覚えたばかりの子供に向けるような笑顔を見せる。"


mi "うんうん！　しっちゃんにも大丈夫だって伝えておくね～！"


hi "あ、ああ。たのむよ"

hide misha
with charaexit


"ミーシャは手を振って（そして自分とは逆にクラスに戻ってきている生徒達のことはまったく気にせずに）教室を出て行く。"


"ミーシャと静音はまた生徒会の仕事があるんだろう。"

scene bg school_scienceroom
with shorttimeskip



"午後が過ぎていくうちに、授業が終わるのが待ちきれなくなる。今すぐ笑美に会わないといけないんだ。"




"過ちをたださないといけない。もう笑美が俺のことを嫌いになっていたとしても、せめて謝らないといけない。"



"それくらいの借りはあるんだ。"




"笑美の部屋で会うべきだろうか？　いや、それじゃ遅すぎる。俺の予想通りなら、笑美は陸上トラックにいるだろう。"





"そこで笑美になんて言うべきかはまだわからないけど、笑美だってこんなことにどうするかなんて考えちゃいないのはわかっている。それだけは安心できる。"



"アドリブでいいんだ。心配するのはやめて、陸上トラックに行こう。後のことはついてから考えろ。"

scene bg school_track
with shorttimeskip



"前方にトラックが見え始めると、また心が揺らぎはじめる。Ｕターンして立ち去りたくなる衝動を必死に抑えると、それどころか予想通りに笑美がまだ走っていることに気づいて満足する。"



"すぐには自分がいることを知らせない。観客席に腰掛けて笑美が走るのを眺めながら、今まで笑美と過ごした時間に思いを馳せる。"

show emi basic_confused_gym:
    center
    xpos 0.6
    easein 0.5 xpos 0.5
with charaenter



"何度か周を重ねたころ、笑美は俺に気づいて横滑りに止まる。驚きをあらわにしたその表情は、いつ怒りに塗り変わってもおかしくないものだ。"


show emi basic_annoyed_gym at center
with charachange


emi "何してるのよ？"


"待ち望んでいた反応ではない。だけどもう俺に選択肢はない。"


hi "このまえ言ったことを謝りたくて"

show emi basic_confused_gym
with charachange


emi "このまえ？"

show emi basic_closedgrin_gym
with charachange



"笑美は笑い出す。信じられないものを見たような驚きを、ぶっきらぼうに伝えてくる。"


show emi basic_grin_gym
with charachange



emi "もう１週間近く経ってるんだけど、久夫"



hi "そうだな、でも……何もしないよりましだろ？"

show emi sad_annoyed_gym
with charachange


"笑美は腕を組んで冷ややかに見つめてくる。まるで俺を品定めするかのように。やがて笑美がうなずく。"

show emi sad_grin_gym
with charachange


emi "ふん。それもそうね。じゃあ水に流しましょう。許すわ"

show emi basic_grin_gym
with charachange


emi "それだけ？"

show emi basic_grin_gym:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None


"そのせっかちとも言える質問に俺が不意を突かれているうちに笑美は競技トラックへと足を進めていて、俺はあわてて声をかける。"


hi "待ってくれ！"

scene bg school_track_on
with locationchange



"俺の言葉が聞こえたようには見えない――それとも聞きたくもないのだろうか――なら追いかける。運動するための服装じゃないけど、そんなの関係ない。"


scene bg school_track_running
with Dissolve(2.0)


"足が痛いし、シャツの襟はまるで首を絞める縄のようだけど、それでも俺は追いかける。チャンスを失いたくはないから。"



"笑美のスピードはまだあまり上がっていない。俺が笑美に追いついて肩に手を伸ばすことができたのはそのおかげだろう。俺の足は革靴で走ることを諦め、つまずいて止まってしまう寸前だった。"



scene bg school_track_on
with Dissolve(2.0)



"驚くべきことに（幸運にも？）今までのランニングが役に立っていたらしい。確かに息こそ切れてるけど、少なくとも俺の心臓は自分であばらから飛び出しそうなくらい暴れまわってはいない。"


show emi basic_confused_gym_close at center
with charaenter


"俺が肩に触れたことで笑美は足を止めていた。息を落ち着けようとしている俺を見るその顔には心配の色が浮かんでいるけど、笑美も俺の能力はよく理解しているようだ。"


"その心配は長く続かない。"

show emi basic_annoyed_gym_close
with charachange


emi "何？"


"俺がまだいることに笑美がこんなにもいら立っているということにおじけづきそうになるけど、おじけづくのはもう十分だ。"



hi "説明させてくれ。どうして俺がただこのままじゃいられないのかを"


show emi sad_annoyed_gym_close
with charachange


"笑美は腕を組んで、義足のバネを地面にはずませる。イライラして足で地面をコツコツするのと同じようなものだろう。笑美は怒っているし、俺は緊張でガチガチだけど、それでも笑美は綺麗だ。"



emi "わかった。説明して"





hi "事故のことやお父さんのことが、笑美にとって本当にデリケートな話題なのはわかるよ"




"俺たちを隔て続けてきた、少なくとも俺にそう感じさせてきた２つの事柄へ言及すると、笑美の顔がひきつるのがわかる。"



hi "だけどだからこそその事を知りたいんだ"


hi "そのことでどれだけ笑美が心を痛めているかが分かるから、いつでも慰めてあげられるようにしたいんだよ"


hi "笑美が眠れずに過ごしてるのとか落ち込んでるのを見るとつらくてしょうがないんだ――そんなことないフリなんてするなよ？　わかってるんだから"



hi "あの夜を思い出すよ。一緒に寝て、悪い夢を見て、目を覚ました時に俺がそばにいたことを喜んでくれた"



hi "あんな風に、必要なときはいつでもそばにいられたら嬉しい"

show emi sad_depressed_gym_close
with charachange


"厳しい顔が、少し揺らぐ。俺が話し続けようとする前に、笑美が口をはさむ。"



emi "もう……いいからやめてよ。あたしたちもう会っちゃいけないの、わかった？"


show emi sad_pout_gym_close
with charachange


"笑美は話を急いでいる。俺と目を合わせようとしない。走り去らないのが驚きだ、俺じゃ追いつけないことはわかってるだろうに……"


emi "あたしたちは……あたしたちは合わないのよ"



hi "そんなことない。わかってるだろ"


show emi sad_shy_gym_close
with charachange



emi "そんなことあるのよ。だいだい久夫は――"




hi "わかってる。笑美の過去のことを知りたがって、厚かましかったよな"



hi "俺にまだ話せないっていうんなら、理由はわからなくていいからせめてそばにいさせてくれよ"



hi "それでいい、約束する。どうしてなのかは聞かない、いくらでも慰めてやる"


show emi sad_depressed_gym_close
with charachange


"笑美は首を振る。瞳の隅には涙が押し寄せてきている。"


emi "やめてよ！！"



hi "どうして？　俺の話に乗っちゃいそうで怖いから？"

show emi sad_pout_gym_close
with charachange


emi "こわくなんかない！"


"俺は穏やかな声音を保てなくなりながら返事をする。"


hi "いいや、怖がってるよ。自分で俺にそう教えてくれたよな？　別にそれでいいんだよ、本当に"



hi "だけどな、お前みたいに大事故を生き延びたあとでも明るくて元気に溢れてるような子なら、その恐怖に立ち向かうくらいの覚悟があるんじゃないかと俺は思うよ"


show emi sad_angry_gym_close
with charachange


emi "覚悟？　久夫に覚悟って言葉の何がわかるっていうの？"



hi "見ず知らずの他人の面倒を見てやるって覚悟を決めて、学園祭でそいつの食い物まで没収する女の子を俺は知ってるよ"




hi "俺の障害のことで手助けするって覚悟を決めて、食事と運動の計画をびっしり書き上げてくる女の子を俺は知ってる。しかも一緒にそれをやってくれるんだ。自分が走れないときまで"




hi "それが正しいと思ったことなら、自分が苦しい思いをしているあいだもずっと俺と距離を置き続けようとする、強い覚悟の持ち主だ"





hi "だけどな、その覚悟ある女の子にも想定外だったことが１つある。俺だってその女の子を傷つけさせないことに同じような覚悟を持ってるかもしれないってことだ"



hi "俺はお前が好きだよ。俺を失うことが怖いからってこの恋を捨てられるのはまっぴらごめんだね"

show emi excited_sad_gym_close
with charachange


"笑美が辛うじて保っていた自制が破れる。気がつくと俺は泣きわめく笑美に抱きしめられている。"



emi "どうしてこんなことするの？　どうしてそっとしておいてくれないの？"


show ev emi_forehead
with dissolve


"俺は笑美を近くに抱き寄せると、頭の上にキスをする。"



hi "ごめんな、笑美。俺が最初ここにきたとき、笑美は俺のことを助けてくれた。今度は俺が助けないと。でなきゃ不公平だろ"



emi "久夫ってどうしようもない人だよね。わかってる？"


"しゃくりあげながら言う笑美は少し震えている。"


hi "お前にも同じ事が言えそうだけどな"


emi "ねえ久夫、お願いしていい？"


hi "何なりと"

scene bg school_track_on
show emi sad_shy_gym_close at center
with charachange


emi "もう行ってくれない？"


"胸をナイフで突き刺されたような気分になる。"


hi "行くって？"

show emi sad_pout_gym_close
with charachange


emi "考える……時間が欲しいの。いい？"


emi "まだ全部は話せないよ。まだ怖いし、久夫がそばにいると、上手く考えられないの"


emi "でも代わりにもう１つお願い"


hi "もう１つ？"

show emi sad_grin_gym_close
with charachange


emi "明日の朝はここにきてね？"


"俺は微笑む。こんなに良い気分はもう１週間は味わっていない。"


hi "当たり前だろ。絶対くるよ"

show emi sad_grin_gym
with charadistant



"笑美はまるでためらうように、ゆっくりと後ろへ下がる。それから小さく鼻をすすって俺に笑いかける。笑美の本当の笑顔が、弱まった夕暮れの光よりもはるかに強くトラックを照らす。"


show emi basic_grin_gym
with charachange


emi "また明日ね、久夫"


hi "ああ"

show emi excited_amused_gym_close
with characlose

show emi basic_grin_gym
with charadistant


"笑美は急にこちらに足を進めると、俺にやさしく唇を重ねる。そして恥ずかしそうに後ずさる。"

show emi basic_grin_gym:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None


"笑美は後ろ足を軸に回転すると、再び駆け出していく。これで会話は終わりだ。"


"さっきの短いキスのぬくもりに昔交わしたキスを思い出し、唇がうずいている。"


"俺は弾むような足取りで自分の部屋に戻る。"


"明日の目覚ましには必ず起きよう。"

stop music fadeout 2.0

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
