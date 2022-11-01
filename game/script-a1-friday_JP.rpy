label jp_A25:

window hide None
scene black
with dissolve

play sound sfx_alarmclock

scene bg school_dormhisao
with openeye

window show


"目覚ましが鳴り出し、しばらく意味もなくごそごそと体を揺らす。やがて、今朝もランニングに挑戦すると決めていたことを思い出す。"


"本当にいい考えなのかどうかはわからないけど、続けると決めたんだ。"


"結局、自分の健康のためなのだから。"


"確かに最近の俺は絶好調ってわけじゃないけど、生きるのがいやになるほどじゃない。健康でいるためにできることはなんだって試してみるさ。"


"それに、この病気を多少なりともコントロールできるようにするのが目的なんだろう？"


"この体をどうにかできれば、ああ、どんなことでもなんとかやれるさ。"


"せめて自分自身には、そう言い聞かせ続けている。"

scene bg school_track
with locationskip

play ambient sfx_emirunning fadein 0.3


"またしても、走るのは俺一人ではないらしい。"


"どうやら笑美はかなり前から運動場にいたようだ。"


"とっくにいい汗をかいているように見える。"


"というか笑美のやつ、いったい何時に運動場に来てるんだ？"

stop ambient fadeout 0.3

show emi basic_grin_gym at center
with charaenter

play music music_emi fadein 0.5


emi "あっ、久夫くんだぁ！"

show emi basic_closedgrin_gym
with charachange


emi "また久夫くんに会えたんで驚いちゃった！"


hi "なんで？"

show emi basic_grin_gym
with charachange


emi "まあ、実際にもう１回やってみようって来てくれる人は少ないってことね"

show emi basic_annoyed_gym
with charachange


"そんな考えに腹が立ったのか、笑美は眉をひそめる。"


emi "たとえば、他の陸上部の人たちとかねー"


emi "でも自由参加ってことになってたから、驚くことでもないの"


emi "そんで、かなり朝早いしねー"


"笑美は肩をすくめ、それでもう何を話していたか忘れたようだった。"

show emi basic_happy_gym
with charachange


"不満げな表情は完全に消え失せる。さっきからの話の続きにあっさりと意識を戻したようだ。"


emi "さて！　そんじゃ行こっか！"


hi "えっ？"

show emi excited_proud_gym
with charachange


emi "もっかい走りにここに来たんでしょ？"


hi "まぁ、そーだな"

show emi basic_closedhappy_gym
with charachange


emi "それじゃ、いこ！"

scene bg school_track_on
with locationchange


"俺はいきなり腕を引っ張られ、競技用トラックに引きずり込まれる。"

play ambient sfx_emijogging fadein 0.3

scene bg school_track_running
with locationchange


"昨日のランニングのリピートみたいだな。"


"つまり、俺は必死なのに、笑美は羨ましいほど余裕で走っているってことだ。"


"こんなにあっさりくたびれてしまうなんて、ひどく腹立たしい。"


"我慢して、地道に頑張らなきゃいけないってことはわかってる、けど……"


"前向きな気持ちを保つのは難しい。"


"俺たちはトラックを１周し、２周目に入る。"

play ambient sfx_emirunning


"笑美は俺のペースに合わせるのに飽きたのか、俺を引き離し始める。"


"俺は昨日、ここでへたばったんだ。"



label jp_choiceA25:
menu:
    with menueffect
    "これ以上やれるか？"
    "やるっきゃないな":




        return m1
    "無理しないでおこう":


        return m2

label jp_A25a:



stop music fadeout 10.0


"好きに走ればいいさ。笑美は容赦なく、すぐに半周差をつける。"


"別に腹は立たない。"


"というか、別に本気で勝負してるわけじゃないし。"


"かわりに、俺は一定のペースで走っている。本来はこうすべきだろ？"


"ここで自分の限界に挑戦する必要なんてない。"


"ちくしょう、こんなことして意味あるのかよ？"

scene bg school_track_on
with locationchange


"２周目を走り終えると同時に、俺はまた途中でやめる。"


"笑美はそのまま走り続けてるけど、なんだかがっかりしているようでもある。"


"いや、それはないな。"


"笑美に誇れるものなんて俺には何もない――考えてみれば、自分自身に誇れるものだって持ってないんだ。"


"別に俺はこのままでいいさ。"


"それに俺は陸上選手になるためにやってんじゃない。"


"こんなこと始めなければ良かったな。"


"かわりに何か他のことができるかもしれない。"


"それに、こんなに早く起きるのはイヤだ。健康を保つ方法は他にもあるはずだ。"


"ウォーキングなんていいかもな。快適な午後の散歩。"




"ああ、それが良さそうだ。ランニングは俺には合ってない。"

stop ambient fadeout 2.0

scene bg school_track
with locationchange


"俺は笑美に手を振り、自分の部屋に戻る。"


"後で別の方法でも考えるか。"





label jp_A25b:


"何やってんだよ、俺は？"


"ここでへこたれて、笑美に引き離されておしまいなんて、そんなんでいいのかよ？"

scene bg school_track_running
with locationchange


"俺はスピードを上げる。"


"２周目を速く走りきり、何も考えずに走り続ける。"


"振り返った笑美が、俺を見てニコッと笑う。"

show emi excited_proud_gym at twoleft
with charaenter


emi "まだやるの？"


hi "俺が……ハァ……不健康だとか……ハァ……思われたくないからね……ハァ……"

show emi excited_laugh_gym
with charachange

hide emi
with charamoveoutleft

play ambient sfx_emipacing


"笑美は笑い――なのに少しもペースを乱さず――さらにスピードを上げていく。"


"ふん、そっちがそのつもりなら……"


"俺もペースを上げる。"


"肺が熱くなるのを感じる。脚が自分のしていることに不平を言い始める。"


"乳酸が俺の筋肉の中で悲鳴を上げているけど、それには耳を貸さない。"


"倒れるわけにはいかない、それは負けだ。"


"いつからこれは勝負になったんだ、と穏やかな理性の声が頭の中で問う。"


"答えたいけど、今はまともにモノを考えることができない。"


"あいつ、{b}速すぎる{/b}。"


"どうやってあんな速度を保っ――{w=.5}{nw}"

stop music fadeout 0.2

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)


"胸をひもで縛られたような、すさまじい息苦しさと痛み。"


"『やばい』以外に何も考えられなくなる前に、自分の足元からトラックが消える。"

scene bg school_track_on:
    xalign 0.5 yalign 0.52 rotate 0 zoom 1.0
    linear 0.1 rotate -6 zoom 1.2
with vpunch


"地面に倒れる。片手で胸をつかみ、もう片方の手を地に突いて、顔から落ちそうになるのを避ける。"

stop ambient fadeout 0.2


"笑美が振り向き、目を丸くする。"


emi "久夫くん！"

play ambient sfx_emisprinting


"笑美は叫んで、トラックの反対側から走ってくる。"

show emi basic_shock_gym:
    xalign 0.5 yalign 0.7 rotate -6 zoom 1.2
with charamoveinright

stop ambient fadeout 0.1


emi "大丈夫？"


hi "ぐっ――なんでもない、ちょっと……"

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)


"呼吸を安定させるんだ。"


"落ち着け。慌てるな。"

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)


"慌てるな。"

show emi basic_shock_gym:
    parallel:
        linear 0.2 rotate -12 zoom 1.5
    parallel:

        "emi basic_hes_gym" with Dissolve(0.2, alpha=True)
with None


emi "ナースくん呼んだほうがいい？"

show black
with shuteyefast

scene black
with None


"外の世界を遮ろうと、俺は目を閉じる。"

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.3)

with Pause(1.0)

play sound sfx_heartslow
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.7)


"心臓がリズムを取り戻そうと必死にもがく。"


"徐々に、胸の痛みが和らいでくる。"


"すぐに、痛みは何事もなかったかのように治まる。"


"何事もなかった……？　そんなはずはない、何かが起きたんだ。"

play music music_rain fadein 2.0

scene bg school_track_on
show emi basic_hes_gym_close at center
with openeye


"目を開き、ちらりと笑美を見るととても心配そうにしている。"


hi "大丈夫だと思うけどな"


"俺の声は自分でも変に、奇妙なほど平坦に、無味乾燥に聞こえる。笑美はそれを聞いて眉をひそめる。"

show emi sad_annoyed_gym_close
with charachange


emi "そんなことないでしょ"


"笑美は何かを決心し、そしてうなずく。"

show emi basic_annoyed_gym_close
with charachange


emi "そうだ。あたしと一緒に行こう"


emi "ナースくんに診てもらわなきゃ"

with vpunch


"笑美は俺の手をつかんで引っ張り上げる。俺は少しだけよろめくけど、笑美が貸そうとした肩を拒む。"


"正直なところ、俺は自分の弱さが少し恥ずかしい。"


"笑美に心配をかけたくなかったけど、どうやら遅すぎたようだ。"



"くそっ、誰にも俺の病気のことを心配されたくないのに、今となっては、それも手遅れのようだ。"


"他人に迷惑をかけないで、なんでも自分でやっていけるようになりたい。"


"色んなことを願ってはいるけど、そもそもこんな病気にかかっていなければ、と思う。"

stop music fadeout 1.0

scene bg school_nurseoffice at bgleft
with locationskip

show emi basic_shock_gym at tworight
with easeinright


emi "ナースく―――ん！"


"笑美はノックもせずに医務室に押しかけるけど、ナースは少しも驚いた素振りを見せない。"

play music music_nurse fadein 0.5

show nurse grin at twoleft
with charaenter


nk "おはよう、ひまわりちゃん。どうしたのかな？"


"ひまわりちゃんだって？　落ち着いたふうにマグカップのコーヒーを一口飲むナースだが、笑美の視線をたどって、入り口にぬっと現れた俺の姿を確認すると、マグカップを置く。"

show nurse fabulous
with charachange


nk "久夫くんだね？　なんの用かな？"

show emi excited_sad_gym
with charachange


emi "一緒に走ってたら久夫くんが転んで、それから胸を押さえだしたからあたしナースくんを呼んでこようと思って、けど久夫くんが大丈夫だって言ってでもあたしはナースくんに見せたほうがいいと思ってそれで――{w=1.5}{nw}"

show nurse concern
with charachange


nk "大丈夫だよ、笑美ちゃん。落ち着いて"

show nurse neutral
with charachange


nk "久夫くん、何があったのかな？"


hi "わかりません。二人でランニングしてたら、以前みたいに胸が痛くなり始めたんだけど、ほんの数秒で治まりました"


hi "ただの粗動か何かですよ"

show nurse concern
with charachange


"ナースは、『ただの粗動』というのは矛盾しているぞと言い出しそうな、難しい顔をする。"


nk "少し運動をするようにとは言ったけど、こんなことになるまでやれと言ったつもりはないよ。もっと気をつけないと、久夫くん"


hi "注意はしてましたよ、俺はただ……"


"考えてみると、『俺はただ陸上部の部員と競争してたんです』なんてのは思ったほど筋が通ってない言い訳だ。"


nk "ただなんだい？"


hi "あ……あの時は……"


hi "笑美と競争してたんです"


nk "笑美ちゃん、それは本当かい？"

show emi basic_hes_gym
with charachange


"笑美はそわそわする。悔いるような表情がまたかわいい。"


emi "えっと、あの……"

show emi basic_closedsweat_gym
with charachange


"結局、笑美は言葉にすることができず、ただ単にうなずく。"


"ナースは、やれやれとため息をつくと、疲れたように自分の額を手でこする。"


nk "笑美ちゃん、他人の限度ってものにもっと気を遣わなきゃダメじゃないか！"


nk "久夫くんが君に話したか知らないけど、彼は心臓が悪いんだよ。競争に誘うなんてあまりに無責任だよ"


hi "あー、それ本当は俺が始めたんです"


"ナースは俺の発言に唖然となる。"


nk "なんだって？"


hi "僕ら、ランニングやってて、それで笑美に引き離され始めて、それで、あの、追いつこうとしてスピード上げたんです"


"ナースは天井をじっと見つめ、落ち着くために神様か何かに祈りの言葉をつぶやいてから、俺たち二人に視線を戻す。"


nk "じゃあ君らは{b}二人とも{/b}大バカだってことか"


nk "それがせめてもの救いだな"


nk "こっちにおいで、久夫くん。君の心臓が爆発とかしないか確認しないとね"

show bg school_nurseoffice at left
show nurse concern at center
show emi basic_closedsweat_gym at Alphaout(1.0), offscreenright
with charamove

hide emi
with None


"俺は律儀にナースの指示に従って、要は、卒倒して死んだりしないかどうかを確かめるために隣の部屋へとついて行く。"


nk "で、調子はどうだい？"


hi "わかりません。大したことはないです。疲れてますけど、さっきの運動のせいかも"


nk "少しの間ここで休んだほうがいい、後でまた様子を見よう"


"ここでナースに逆らうつもりはない。俺は医務室のベッドの上で横になる。"

stop music fadeout 2.0

scene bg school_nurseoffice at left
with shorttimeskip


"その後、隣の部屋でナースにお説教を食らってすっかり落ち込んだ笑美がやって来る。"


"閉じられたドア越しにナースが何を言ってるのか、俺には聞こえなかったけど、愉快な冗談じゃなかったってことは確かだ。"

show emi sad_depressed_gym at center
with charaenter

play music music_dreamy fadein 0.5


emi "ねえ、ホントに、ホントにごめんね"


emi "あたしがもっと気をつけてればよかったのに"


hi "どうして、君は知らなかったんだろ。君のせいじゃないよ"


"ひどく落ち込んで申し訳なさそうにしている彼女には、俺の元気づけの言葉は大した励ましにもならない。"


emi "埋め合わせさせてくれないかな"


"もう一度、決心して頷く。"

show emi sad_shy_gym
with charachange


emi "だからあたしと一緒にお昼食べようよ"


emi "あたしお昼持ってくるから、ね？　すっごくすっごくおいしいお弁当！"


"『いいよ、そんな……』と言いかけたけど、笑美の表情を見て俺は黙って頷く。"

show emi excited_proud_gym
with charachange


emi "よかったぁ！"

show emi basic_grin_gym
with charachange


emi "屋上で待ち合わせね"


hi "待ち合わせ？"

show emi basic_closedgrin_gym
with charachange


emi "そうだよ！　今なら天気も良いし、屋上はお昼食べるには絶好の場所なんだよ"


hi "なるほど"

show emi sad_shy_gym
with charachange


emi "来てくれるでしょ？"


emi "あたしに埋め合わせさせてくれるよね？"


hi "当然だろ"

show emi excited_joy_gym
with charachange


emi "よかった！　じゃあまた屋上でね！"

hide emi
with charaexit

with shorttimeskip


"俺は完全に疲れ果て、眠りと目覚めの間をふわふわと漂い続ける。"


"体だけじゃなく俺の全部が――意識をのぞいて――ぐったりとなって麻痺している。"


"俺はなんとか唾を飲み込み、ベッドに横になったままできるだけ体を動かさないようにする。今の俺の状態ならそんなに難しいことじゃない。"


"俺のために引いたカーテンの向こう側で、ナースはすり足で歩き回る。太陽の光の中で影が動くのが見える。"


"ナースが医務室の窓を開けていた。外は風が強い。"


"綺麗な白いカーテンが、重くのろのろとした調子で、さざ波のようにそよ風にパタパタとはためく。陽の光は自らの半分をカーテンの布地に吸い込まれながらも、ゆっくりとその篩を通り抜けてくる。"

stop music fadeout 5.0

scene darkgrey
with shuteye


"俺は目を閉じる。顔に当たるそよ風がカーテンの柔らかい布のようだ。"


"ナースがパソコンのキーボードを打つ音や、自分の荒い息づかいを遮断しながら、自分の心臓の鼓動に耳を集中させる。"


"規則的だな。"



"ちきしょう、まだ１週間も経ってないってのにまたこんなことになっちまった。今回のはマジで大失敗だ。"
"半端なスポーツ選手ごっこなんてやるんじゃなかった。それも本物の選手を前にして。"


"どうして粗動が大したことじゃないなんて、かっこつけようとしたんだ。明らかに大問題じゃないか。"


"反射的な行動だったんだ。現実から目を背けて、隠しておこうとするための。"


"こんなこと起きて欲しくなかった。"


"笑美に見られたくなかった。"


"あぁぁぁ……"


"馬鹿だ馬鹿だ馬鹿だ。"


"もっと気をつけなきゃ。そうじゃなきゃ、また病院に逆戻りだ。さもなきゃ、もっとひどいことに。"


"……"


"疲労感に音を上げる前の、最後の思考だった。"

scene black
with Dissolve(1.0)

window hide Dissolve(2.0)

with Pause(2.0)

scene bg school_nurseoffice at left
with openeye

window show

play music music_daily fadein 6.0


"眠っていた。どのくらい寝た？　今何時なんだ？"


"少し頭がクラクラして、耐えられずまばたきを繰り返す。"

show bg school_nurseoffice at center
with charamove


"カーテンを脇によせ、窓から直接降り注いでくる光に目を細める。キャンバス布の手触りは、前に感じた風とは似ても似つかない。"


"さっきと全く同じ場所に座っていたナースが、机から顔を上げる。"

show nurse fabulous at center
with charaenter


nk "調子はどうかな？"


"自分でもよくわからなかったので、何も答えない。こんな変な時間に寝てしまったので、意識がぼんやりしている。変な風に見えないといいんだけど。"


hi "何時ですか？"


"状況を把握しようと、しゃがれ声で尋ねる。ナースは質問に答える前に腕時計を見る。"


"スローモーションみたいに感じる。"

show nurse neutral
with charachange


nk "１０時１５分"


"それが何を意味するのか少し考えるけど、よくわからない。"

show nurse concern
with charachange


nk "僕の質問に答えてないよ、久夫くん"


hi "ああ、大丈夫です"

show nurse neutral
with charachange


nk "じゃあベッドから降りて、様子を見よう。でもあまり……"

$ renpy.music.set_volume(0.5, 0.2, channel="music")

show bg school_nurseoffice as dizzy_bg behind nurse:
    xalign 0.5 yalign 0.5 rotate 0 zoom 1.0 alpha 0.0
    ease 0.4 rotate 6 zoom 1.05 alpha 0.5

show nurse neutral as dizzy_fg:
    xalign 0.5 yalign 0.5 rotate 0 zoom 1.0 alpha 0.0
    ease 0.4 rotate -4 zoom 1.05 alpha 0.5
with Pause(0.4)

show bg school_nurseoffice as dizzy_bg behind nurse:
    ease 1.0 rotate 0 zoom 1.0 alpha 0.0

show nurse neutral as dizzy_fg:
    ease 1.0 rotate 0 zoom 1.0 alpha 0.0


"言われた通りにしようとするけど、早く動きすぎて、ただフラフラと倒れこんでしまう。ナースが俺の腕を取って支え、ため息をつく。"

show nurse concern
hide dizzy_bg
hide dizzy_fg
with charachange


nk "……あまり急いで起きなくていい、って言おうとしたんだよ。そこに座って、確認のために血圧を測るからね"

$ renpy.music.set_volume(1.0, 2.0, channel="music")



"俺のやることはずっと裏目に出続けている。ナースが古めかしい血圧計と俺の腕を取って忙しくしている間、きまりの悪さを感じながら黙る。"
"数分後、ナースは血圧計をしまう。その表情は不満そうでも満足そうでもない。"

show nurse neutral
with charachange


nk "問題はなさそうだ。頭のふらつきは治まったかい？"


hi "ええ"


nk "よし。じゃあ中身のほうはどうだい？"

show nurse concern
with charachange


nk "君の行動は軽率だったね、久夫くん"


"反論しそうになったけど、その言葉を飲み込む。俺だってそう思っていた。でも同じことを他人から聞かされると言い返したくなる。"


"ナースの言っていることは不愉快だ。それでも正しいことには変わりない。"


hi "はい"

show nurse neutral
with charachange


"彼は頷く。相変わらずよくわからない表情。"


"もし『言わんこっちゃない』とか言ってくれたら、俺だって簡単に怒れる。でもナースはそんなことは言わない。"


nk "僕は君の健康を維持する手助けはできる。でも最後に責任を持つのは君なんだよ。これに懲りて、そのことを覚えていてくれるといいんだけどね"

show nurse fabulous
with charachange


nk "ほら、先生に渡すメモだ。質問責めに会わないためのね"


"俺はナースがくれた紙切れを受け取り、そのまま医務室を後にする。言うことなんて何も思いつかなかったし、そもそも何も言いたくなかった。"

show nurse neutral
with charachange


nk "面倒ごとは避けるんだよ、聞いてるかい？　今回は怖い目にあったくらいで済んだけど、次は違うかもしれないからね"


"聞いてますよ。"

scene bg school_nursehall
with locationchange

stop music fadeout 4.0


"副校舎から本校舎にまっすぐ向かう方法があるそうだけど、そんなに見つけたいとも思わないし、迷う可能性だってあるから、確実に出られるとわかっている出入口から外に出る。"

scene bg school_courtyard
with locationchange


"副校舎の階段で足を止め、教科書などを取りに寮に立ち寄るか、速攻で学校に向かうかを考える。"


"太陽の光が目にしみるので、俺は寮へと向かう。"




label jp_A26:

window hide None
scene black
with dissolve

scene bg school_dormhisao
with openeye

with Pause(0.2)

scene bg school_dormbathroom
with locationskip

window show


"起床後、熱いシャワーを浴びる。"

label jp_A26a:

scene bg school_dormhisao
with locationskip


"部屋に戻ると、最初に目に入るのはおなじみ机の上の薬瓶の列。いつものことだけど憂鬱になる。"


"不愉快だ。大丈夫だと思っていた。もう折り合いをつけたつもりだった。乗り越えたつもりだった。"


"でも実際は……自分が病気を抱えているということから逃避していただけだ。ここにいると現実を思い知らされる。現実と戦うのが辛くて仕方ない。"


"くよくよ悩んでいたって解決しない。前もそうだった。何ヶ月も。もう立ち直る時だろう。"


"他の人のようにはまず長生きできないという事実から逃避していても、何も得られない。"


"俺の人生は、他の人とは違うかもしれない。でもこの人生は現在進行中なんだ。"


"そう思って納得しよう。"


"この突然沸きあがったつまらない気分を追い出すように、いつもと同じ一握りの錠剤を飲む。早めに家を出るよう準備する。これもいつも通り。"

scene bg school_dormhallway
with locationchange


"廊下に出ると、廊下の角からこちらへ歩いてくる健二を発見する。大きなかばんを抱えて忍ぶように部屋に向かっている。景色に溶け込む忍者のように音もなく俺の横を通り過ぎようとするそいつに、俺は声をかける。"


hi "よう"

show kenji neutral at center
with charaenter

play music music_kenji fadein 0.5


"俺の声に飛び上がる健二。"


ke "ああ……なんだよ、気づかなかったよ。マジ疲れてるんだ"


"見えなかったと言ったほうが正しいんじゃないだろうか？　ってそんなことよりも、"


hi "こんな早くからどこ行ってたんだ？　買い物？"

show kenji tsun
with charachange


ke "いや、買い物じゃねえよ。時々……数学教師に会いに行かないといけないんだ。ああ、次の試験日を聞いておくのもいいと思ったし。あいつは聞けば事前に教えてくれるからな"


hi "じゃあ、そのかばんの中には何が？"

show kenji neutral
with charachange


ke "外に出たついでに買い物しようと思ってな。フェミニストの巨大な陰謀と戦い続けるには、物資が必要なんだよ"


hi "ああ……そうか"


hi "お前、外には出ないんじゃなかったのか"

show kenji happy
with charachange


ke "帽子をかぶるようにしたからな"


"帽子なんて見当たらないけど放っておこう。"


"俺たちの間に気まずい沈黙が漂う。健二がゆっくりと部屋のドアを開くと、ギイギイと音がして余計に気まずくなる。健二はかばんを中に置いてドアを閉める。"


hi "わざわざテストの日程を調べに行くとは驚いたよ。前もって予習しておくなんて、けっこう真面目なんだな"

show kenji tsun
with charachange


ke "勉強なんかしねえよ"


hi "はあ……"

show kenji neutral
with charachange


ke "次のテストの日が知りたかっただけだ。それでもテストは受けるんだぜ。当たり前だろ。授業をサボれない日を知る為に聞きにいったんだ"
ke "あいつはあのクソテストの日程を電話で伝えてくるんだ。だから外に出て調べないといけなかったんだよ"


hi "なんで外に行かないといけないんだ、電話で済むのに？"

show kenji tsun
with charachange


ke "俺、電話は持ち歩かないんだ"


hi "持ち歩かないって？　部屋に置いてるってこと？"

show kenji neutral
with charachange


ke "ちげえよ、俺は電話は使わないんだ。持ってないんだよ、電話。一つも持ってない"


hi "なんで持ってないんだ？　電話持ってないなんて、そんなわけあるかよ？　一つもないのか？　電話なしか？"

show kenji tsun
with charachange


ke "電話は嫌いなんだよ。なんか怖いし。上手く説明できないけど。抑圧されたトラウマってやつかもな"


ke "まあ要するに、電話の音を聞くと不安になるんだ。俺の一番の秘密な"

show kenji neutral
with charachange


ke "原因は二つ考えられる。誰からともなく、俺の人生を変えるような、不気味な悪夢の電話がかかってくるのを恐れているのか"
ke "さもなきゃ昔電話で殴られたことがあるか、だ。思い出せないくらいひどく殴られたんだろうな"


hi "頭を叩かれたんだろうな"

show kenji tsun
with charachange


ke "他にどこ叩かれたら思い出せなくなるっていうんだよ。ケツ？"


"意外なほど論理的な答えが返ってくる。なんかすごく気が滅入る。会話も終わりだと判断して、健二はまたドアを開けて中に入ろうとする。"

show kenji neutral
with charachange


ke "さて寝るとするか。お前もがんばれよ"


hi "あと２０分ぐらいで授業始まるんだが"

show kenji tsun
with charachange


ke "もう今日は頑張ったからな。くたくたで学校行けない"

show kenji happy_close
with characlose


ke "そうだ、リップクリームいらないか？　単三電池をバラ売りし始めたのかと思って間違って二つも買っちまったんだ"


hi "どーも、でもいらない"



label jp_A26b:

scene bg school_dormhallway
show kenji happy_close at center
with None

stop music fadeout 0.3

play sound sfx_doorslam

show kenji tsun_close
with vpunch


"廊下の先にあるドアが勢いよく開かれて、壁にぶつかってばぐんと大きな音を立てる。続いて陽気な大笑いがこっちまで響いてくる。声の主は一発でわかる。"

play music music_comedy fadein 0.3

show misha perky_smile at center behind kenji
show shizu basic_normal2 at center behind kenji
with zoomin


show shizu basic_normal2:
    easein 1.0 tworight
show misha perky_smile:
    easein 1.0 twoleft
show kenji tsun_close:
    0.25
    easeout 0.5 offscreenleft alpha 0.0
with Pause(1.0)

hide kenji
with None

play sound sfx_impact2


"音を聞いたとたん、健二は忍者のように自分の部屋へと消える。ドアがぴしゃりと閉まるのと同時に、静音とミーシャがやってくる。"
"静音はきびきびと素早い足取りで、一方ミーシャはほとんど壁の間を跳ね回っているみたいだ。"

show misha hips_smile_close at twoleft
with characlose


"健二を見習って部屋に逃げようとするけど、遅かった。ドアを閉められないようミーシャが足を突っ込んできたので、二人を中に入れるしかなくなる。"

scene bg school_dormhisao
with locationskip

show shizu behind_smile at center
with charaenter


shi "……"

show shizu behind_smile at tworight
with charamove

show misha hips_grin at twoleft
with charaenter


mi "おはよ、ひっちゃん～！　おはよ～おはよ～！"


hi "よう"


hi "二人ともこんなところで何してる？"


"邪険に聞こえないよう、言葉の間にはじゅうぶん間を空けたつもりだけど。"

show shizu basic_normal
with charachange


shi "……"

show misha hips_frown
with charachange


mi "ひっちゃん失礼だよ～！　わたしたち迎えに来てあげたんだよ！"

show misha hips_smile
with charachange


mi "ひっちゃんが逃げるかもしれないから、逃げないように捕まえておこうとしてると思ったの？　そんなわけないじゃ～ん！"


hi "ちょっと待てよ、それがお前らの目的だなんて言ってないだろ"


"でもそれが二人の目的だってことはもう明らかだ。"

show misha sign_smile
with charachange


mi "ほらほら、生徒会の仕事する時間だよ～！"

show misha hips_grin
with charachange


mi "ひっちゃん、ついに学校全体のお手伝いができるんだよ～！　うれしいでしょ～？　ヒーローみたいだよ～！　今日という日はきっと子々孫々の代まで語り継がれるよ！"


"おもしろいな。生徒会に入るのがヘラクレスなみに英雄的な行為だとは思わなかった。"


hi "いやまあ……確かに約束はしたけどさ……"

show shizu adjust_happy
with charachange

stop music fadeout 7.0


"ほったらかしにしていた静音が、俺の視野の端に入ってくる。あいつは俺の肩越しに部屋の中を見渡している。あの分析するような目で、じろじろ視線を移しながら……"


"人の部屋に勝手に入って何してるんだ。裸を見られたような感覚にタマがむずむずする。幸い、脱いだ服やらなんやらが床に散らかっていたりはしないけど。"

show shizu behind_smile
with charachange


shi "……"

show misha perky_confused
with charachange


mi "ん～？　どしたの、しっちゃん？"

show misha hips_smile
with charachange


mi "そうだよ、ここはひっちゃんの部屋～！　そういえば今まで来たことなかったよね！"

show misha hips_grin
with charachange


mi "なんだか地味だけど、ひっちゃんまだ飾り付けする時間がなかったんだよね～？"

show misha sign_smile
with charachange


mi "それな～に？"

"ミーシャはナイトテーブルの上に並んだ、薬瓶の数々を指さす。"



label jp_choiceA26:
menu:
    with menueffect
    "二人にこのことはあまり話したくない。"
    "話をはぐらかす":




        return m1
    "二人を追い出す":


        return m2


label jp_A26c:


hi "なんでもないよ"

show shizu basic_normal2
with charachange


"俺は素早く二人の前に立って、薬を背中で隠そうとする。静音は怪訝そうな表情で一歩退く。でもその表情には心配も混じっている。"


"このまま話題を避ければ、詮索されたくないということが静音に伝わるんじゃないかと期待する。"

show shizu behind_blank
with charachange


shi "……"

show misha perky_confused
with charachange


mi "ほんとに？　なに隠してるの、ひっちゃん～？"


hi "なんでもない"

show shizu basic_normal
with charachange


shi "……"

show misha sign_confused
with charachange


mi "そうかなあ～？"


"こんなやりかたじゃ話題を変えるのは無理だと気づく。もともと二人とも詮索好きなんだし、隠したって好奇心をかき立てるだけだ。"


hi "わかったよもう、確かになんでもなくはないよ。でもこのことはあまり話したくないんだ……まだ"


hi "今は触れないでおいてくれないか？"

show misha perky_smile
with charachange

"ミーシャが通訳すると、静音はいつも以上に見透かすような目つきでこちらを見据える。眼鏡の縁越しに、好奇心に満ちた視線で見つめられる。"


"熟慮するように両手を合わせる。俺の意志を無視する失礼なことだとしても、このまま問いただす価値があるのか考えているようだ。"


"ようやく静音は表情を和らげてかすかに笑い、ミーシャに何事か手話で伝える。"

play music music_dreamy fadein 2.0

show shizu adjust_happy
with charachange


shi "……"

show misha hips_smile
with charachange


mi "おっけ～！　じゃあ、わたしたち待つよ。これからずっとずっと仲良くなって、ひっちゃんが話したくなったら、そのときはわたしたちに教えてね！"


"二人ともにっこりと笑う。俺はショックだった。こんな態度をとった自分がなんだかバカみたいだと思う。"


"この二人はバカじゃない。俺の事情だって半分は見当がついているはずだ。それに……"


"こんなに無邪気で、優しい言葉。二人が全く気にしないでくれたことに心が軽くなる。"
"俺のこんな態度を見ても、俺が山久の他のみんなと同じでなくても、俺自身がそれを受け入れられていなくても。"


"憎たらしい、いたずらじみたことをするけど、本当はとても優しくていい子たちなんだ。俺はそう思う。"


hi "ありがとう"


hi "で、俺になんか手伝って欲しいんだろ？　もう俺もお前らの仲間ってわけだし"

show misha hips_grin
with charachange


mi "うん！"


hi "放課後？"

show misha sign_smile
with charachange


mi "ちがうちが～う！　今すぐだよ！"


hi "今？　って、授業はどうすんだよ？　またさぼる気か？"

show shizu adjust_smug
with charachange


shi "……"

show misha cross_laugh
with charachange


mi "ははは～！　これは公共の利益のためなのよ、だから数学の授業には犠牲になってもらうの。もしかしたら、社会もね～！"


hi "そっか。まあ、俺は構わないけど"

show shizu behind_smile
with charachange


shi "……"

show misha sign_smile
with charachange


mi "そうこなくっちゃ、ひっちゃん～！　今自分で言ったよね？　忘れちゃだめよ！　『俺は手伝っても構わないけど』って、そういうことだよね、ね～？"


hi "ああ"


"その声の調子……俺は突然自分の言葉を後悔する。"

show shizu basic_normal2
with charachange


shi "……"

show misha hips_grin
with charachange


mi "おっけ～！　じゃあ用意はいい？　生徒会室に一緒にいこ～！"


hi "いや待て。俺に荷物全部持たせるとか、何か仕掛ける気だろ"

show shizu adjust_happy
with charachange


shi "……"

show misha perky_smile
with charachange


mi "何バカなこと言ってるの、ひっちゃん"

show misha hips_smile
with charachange


mi "わたしたち、一度も一緒に登校したことなかったじゃん、ひっちゃん～"


"なぜ一緒に登校しなきゃいけないのか、という問いがのどまで出かかる。でもふと俺は気づく。"
"二人とも俺を友達だと思ってくれているんだ。さっきミーシャが言ったように。そしてもっと仲良くなりたいんだ、と。"


"妙な感じだ。二人のことを、いや今週会った人たちの誰であれ、そんな風に考えたことなんてなかった。そんなにあっさりと打ち解けるものなんだろうか？"


"いとも簡単に……"


hi "わかった。じゃあ行くか"

show shizu behind_smile
with charachange


"静音は何か企んでいるような笑顔を浮かべると、両手を背中にまわす。"

show misha hips_grin
with charachange


mi "ははは～！　ありがと、ひっちゃん～！　おっけおっけ、でもその前に～！　今のすごくいいアイディアだね、しっちゃんも気に入ってるよ……なので～！　今からゲームしよう！"


hi "おいマジかよ"

show misha hips_smile
with charachange


mi "しっちゃんは片手に千円札を持ってるよ～！　どっちの手か当てられたら、ひっちゃんが千円ゲット～！　はずしたら……"

show misha hips_grin
with charachange


mi "わたしたちの荷物、全部学校まで持っていってね～！　だよね、しっちゃん～？　ね～！"




"ミーシャと静音はうなずきあう。"

show misha sign_smile
with charachange


mi "おっけー、ひっちゃん～！　覚悟してね～！"

stop music fadeout 7.0

scene bg school_courtyard
with shorttimeskip


"かばん一つじゃなくて、かばん三つ。俺は今日これからのことを思う。俺たち三人の。"


"中庭を生徒が行き交うのが見える。自分のところの企画の準備だろう。"


"学園祭はもう始まったようなものだ。つまり、俺の手伝いが必要な理由は二つしかない。"


"もうほとんど仕事なんて残ってなくて、単調な最終チェックを片付けるのを手伝ってほしいだけか。"


"実はまだ仕事が山ほど残っていて、先延ばし続けて積み上がった作業が土石流みたいに俺たち全員を飲み込もうとしているのに、静音は平気なふりをしているだけか。"



label jp_A26d:

play music music_rain fadein 4.0


"とうとう、こいつらは最後の一線を越えた。邪魔くさい奴らだ。いちいち首をつっこみやがって。"


hi "なんでもない"

show misha perky_smile
with charachange


mi "ほんとに～、ひっちゃん？　なんでもないようには見えないけど"

show shizu adjust_smug
with charachange


shi "……"

show misha hips_smile
with charachange


mi "ビンがたくさんだよね～？　ね～！　そんなにいっぱいなんなの、ひっちゃん？"


hi "ちょっとな"

show shizu basic_normal2
with charachange


shi "……"

show misha perky_confused
with charachange


mi "『ちょっと』っていうには多すぎるんじゃないかな……"


"二人がそうやって詮索するのを責めることはできない。ミーシャは静音のかわりにしゃべってるだけだし、静音はもとから好奇心が強い。"
"それでも俺はこれ以上二人にかぎ回られたくないし、そろそろ察して欲しい。でもミーシャは気づかないし、静音は気づくことができない。"


"だから二人は詮索をやめない。"


hi "お前らには関係ないだろ"


hi "そろそろ出たらどうなんだ？　人の部屋なんだから。プライベートだろ"


"静音はそれを挑戦と受け取ったようだ。"

show shizu behind_frown
with charachange


shi "……"

show misha hips_frown
with charachange


mi "それどういう意味、ひっちゃん？　興味を引くものを見かけたら、それが何か聞くのは本能ってものよ。当たり前じゃない。何が悪いっていうの？"


hi "さっきも言っただろ。見るものなんて何もないんだよ"

show misha perky_confused
with charachange


mi "ひっちゃん、しっちゃんは心配してるだけだと思うよ"


hi "俺の部屋にあるものはお前らには関係ない。それだけだ"

show misha sign_confused
with charachange


mi "でも……"


hi "ちくしょう！　お前らふざけるのもいいかげんにしろよ。それが面白くないときだってあるんだよ。そのくらいわかるだろ？"


"思っていたより強く言いすぎてしまい、ほとんどミーシャの顔に向けて怒鳴りつけていた。ミーシャは驚いて手話の途中で止まってしまう。聞こえないはずの静音まで反応している。"

stop music fadeout 6.0


"俺の怒りの表情から、言いたいことは全部伝わったようだ。"

show misha perky_sad
show shizu behind_blank
with charachange


"ミーシャがゆっくりと訳し終えると、二人は悔やむようにお互いを見あう。"

show shizu behind_sad
with charachange


shi "……"


mi "わかったよ、ひっちゃん。わたしたち行くね"


"俺は初めて、あの陽気で上がり下がりの激しい調子抜きでミーシャが話すのを耳にする。ひどく奇妙な感じがする。俺は謝りたかったけど、二人はもう背を向けて部屋を出ている。"


"静寂が訪れるとともに、俺はますます今の言葉を後悔する。"

hide shizu
hide misha
with charaexit


"二人は静かに部屋を出て行く。俺はしばらく立ちつくしていたけど、服を着てその後に続く。"



label jp_A26e:

show kenji tsun_close
with charachange


ke "はいはいそうかよ"

stop music fadeout 2.0

hide kenji
with charaexit


"健二がそそくさと自分の部屋へ戻ったので、俺もようやく学校へ向かえる。"



label jp_A27:

scene bg school_hallway3
with shorttimeskip


"廊下は中庭と同じように静かだ。みんな授業に出ているから当たり前だけど。３年３組のドアを軽くノックして、武藤先生が呼び入れるのを聞いてドアを開く。"

scene bg school_scienceroom
with locationchange


hi "遅れてすみません"


"１５組の目が俺のほうを向く。"

show muto irritated at center
with charaenter


mu "おはよう、中井"


"武藤先生は俺が遅れて入ってきたせいで面食らっているようだ。何か授業の流れを邪魔してしまったんだろうか。"


"いつもとりとめのない授業をしていることを考えれば、それが正解なのかもしれない。"


"ナースにもらったメモを先生に渡す。先生はうなずいてそれに素早く目を通す。"

show muto normal
with charachange


"先生は眉を上げると険しい目で俺を見る。でも何も言わず、ただもう一度重々しくうなずく。"


"俺は肩をすくめる。先生に席に着けと無言で促され、俺はそのまま従う。"


label jp_A27a:

scene bg school_scienceroom
show muto normal at center
with None


hide muto
with charaexit


"俺が席に着く間、２組の視線だけが俺をしっかりと捕らえつづける。"


"席に着いてから１５秒ほど後、ミーシャの爪が俺のシャツをつつくのを感じる。俺は驚きもしない。"

show misha perky_smile_close at offscreenleft
with None

show bg school_scienceroom at bgright
show misha perky_smile_close at Transform(xalign=-0.3) 
with charamove

play music music_another fadein 2.0


mi "ねえねえ！　どこに行ってたの？"


hi "お前には関係ない"


"これが一番まずい答え方なのはわかっている。これじゃ二人の好奇心をかき立てるだけだ。でも手の込んだ作り話を思いつくような気力は今の俺にはない。"

show misha perky_confused_close
with charachange

show bg school_scienceroom at center
show misha perky_confused_close at offscreenleft
with charamove


"でもミーシャは引き下がる。今日はずいぶんあっさりあきらめるな。"


"……"


"でもすぐに、ミーシャがまた指でつついてくる。"

show misha hips_grin_close
with None

show bg school_scienceroom at bgright
show misha hips_grin_close at Transform(xalign=-0.3) 
with charamove


mi "いいじゃん、教えてよ！　しっちゃんもすごく知りたいって！"


"俺が甘かった。ミーシャは静音に話していただけだったんだ。どうやって俺に吐かせようかと相談していたんだろう。"


hi "だめだ"

show misha perky_sad_close
with charachange

show bg school_scienceroom at center
show misha perky_sad_close at offscreenleft
with charamove


"ミーシャはまた引っこんで相談する。"

show misha sign_smile_close
with None

show bg school_scienceroom at bgright
show misha sign_smile_close at Transform(xalign=-0.3) 
with charamove

label jp_choiceA27:
menu:
    with menueffect
    mi "生徒会の一員として、授業をさぼった理由は正直に話さなきゃダメだよ！　それがお楽しみだったらなおさらね～！"
    "そうだな、医務室で大いにお楽しみしてきたぜ……":





        return m1
    "話したくないって言ってるだろ？":



        return m2

label jp_A27b:

stop music fadeout 4.0


"ちくしょう。いい加減にしろってんだ。"


hi "ああそうかよ。わかった。教えてやる。すげえ楽しかったさ"


hi "今日朝イチで心臓発作起こして、何時間もナースと一緒にお楽しみだったんだよ"


hi "人生最高の朝だぜ。マジで"


"ミーシャのバカみたいに陽気な口調を真似してみるけど、周りに聞こえないよう小さな声でしゃべる。その言葉ははき出すような調子になる。"

show misha perky_confused_close
with charachange


mi "なにそれ、ひっちゃん？　本当なの？"


hi "これ以上聞くなよ。聞こえただろ"

show misha perky_sad_close
with charachange


mi "でもひっちゃん、これ大事なことでしょ！"


hi "だめだ。いいからほっとけよ。それに今は授業中だろ"

show misha sign_sad_close
with charachange


mi "でもひっちゃん！"


"ミーシャは心配してるようだ。パニック状態かもしれない。そうやって首突っ込まれるのが嫌なんだってこと、気づいてないのか？"


"……"


"しばらく自分がしでかしたことを思い知らせてから、俺は答えてやる。静音には伝わらないだろうけど、知ったことか。"


hi "お前ウザいんだよ"


hi "静音にもそう言ってやれ"


"そう口にした直後に後悔するけど、でも言ったことはもう取り消せない。"

show misha perky_sad_close
with charachange

show bg school_scienceroom at center
show misha perky_sad_close at offscreenleft
with charamove

hide misha
with None


"ミーシャは本当に口をつぐんだので、俺は少し驚く。でも静音に通訳したかどうかは確かめない。してもしなくても関係ない。"


"武藤先生は二日後の学園祭についてどうでもいい話をして、授業を終える。"





label jp_A27c:


hi "あきらめろよ。絶対言わないからな"

show misha hips_grin_close
with charachange


mi "そーなの～？"


hi "そうだよ"

show misha perky_confused_close
with charachange


"ミーシャはしばらく考える。"

show misha hips_frown_close
with charachange


mi "けちだよ、ひっちゃん～！"


"不機嫌さが声ににじみ出ている。いかにも失望したって感じだ。"

show bg school_scienceroom at center
show misha hips_frown_close at offscreenleft
with charamove


"またしばらく引き下がって、パワフルコンビの頭のいいほうに相談してから戻ってくる。"

show misha hips_smile_close
with None

show bg school_scienceroom at bgright
show misha hips_smile_close at Transform(xalign=-0.3) 
with charamove


mi "一緒にお昼食べながら話を聞きましょうか……ってしっちゃんが言ってる"

show misha hips_grin_close
with charachange


mi "わたしたちのおごりだよ"

show misha sign_smile_close
with charachange


mi "それに、今朝わたしたちが手伝ってほしかったのにひっちゃんはいなかったんだから、埋め合わせしてもらわなくちゃね～！"


"他の生徒たちがこっちを見はじめてる。ミーシャが机から思い切り身を乗り出して、俺に頭をこすりつけてきてるからだろう。ミーシャの巻き毛が俺の首筋に触れる。"


"シャンプーと、髪をセットするために使っているんだろう、何かの香りがする。"


"前の席の女子が聞き耳を立ててるようだ。誰も勘違いしてくれなきゃいいけど、でもこんな状況で勘違いせずにいてくれる人がいるか、自信がない。"


"幸運なことに武藤先生は気づいていない。あるいはミーシャをわざと無視しているのか。今のところは。"


"これは逃げるのは無理だよ、なあ？"



label jp_choice2A27:
menu:
    with menueffect
    "笑美とも昼を食べるって約束してしまった。でも同時に二つの場所にはいられない。"
    "笑美とその友達と一緒に昼を食べる":




        return m1
    "静音に付き合う。俺も今は生徒会員だし":


        return m2


label jp_A27h:



hi "悪い、行けないんだ。もう他の人と昼を食べるって約束してて"

show misha perky_confused_close
with charachange


mi "ええぇ？　誰なの？　女の子～？"


hi "ああ……"

show misha hips_grin_close
with charachange


"ミーシャのくすくす笑いに、勘違いされないようあわててフォローを入れる。"


hi "そういうのじゃないぞ！　ちょっと……複雑な事情なんだよ"

show misha perky_smile_close
with charachange


"複雑……そうだ、それが俺の人生だ。もう学校生活という日常に落ち着き始めてはいても。"


"この第二の人生、すべてを新しい角度で見ないとダメだ。これからの俺の視点から見直した価値観で。"


"心臓のぶっ壊れた、この俺の。"


hi "あと、やっぱり生徒会には顔出せないかもしれない"


hi "少なくとも今は。他に集中しなきゃいけないことがあるんだ"


"そうだ。何をして何をしないか、俺は優先順位を考え直さないと。ナースに説教されてから、そのことがずっと頭の中でぐるぐる回っていた。自分が病気じゃないふりをするなんて、そんな余裕は俺にはない。"


"こんなに自分が分析的に考えられることに、自分でも驚く。でも今はこの流れに身を任せることにする。"


hi "後でちゃんと説明するって、約束する。でも今は待ってくれ、な？　がっかりさせてごめんって静音にも伝えてほしい"

show misha perky_confused_close
with charachange


mi "うん、わかったよ、ひっちゃん"


"ミーシャは驚いたようだ。そして真剣だった。今までこんな話し方をするのは聞いたことがない。"

show bg school_scienceroom at center
show misha perky_confused_close at offscreenleft
with charamove

hide misha
with None

stop music fadeout 3.0


"幸い、ミーシャは俺が真剣だと理解してくれた。ミーシャにすらちゃんと俺の意図が伝わった、というのは思いがけない幸運だ。そのまま引き下がり、ミーシャは静音に話の内容を通訳する。"


"その後は二人とも俺には話しかけてこない。"



label jp_A27i:


hi "わかった、一緒に行くよ。でも授業が終わるまでは離れててくれないか？"

show misha hips_grin_close
with charachange


mi "いいよ、ひっちゃん～！"

stop music fadeout 2.0

show bg school_scienceroom at center
show misha hips_grin_close at offscreenleft
with charamove

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell

with Pause(7.0)

play ambient sfx_crowd_indoors fadein 0.3

scene bg school_hallway3
show crowd
with locationchange


"生徒会室に行く途中、廊下を行き交う生徒をたくさん見かける。たぶん自分の企画の準備をしているんだろう。"


"学園祭はもう始まったようなものだ。つまり、俺の手伝いが必要な理由は二つしかない。"


"もうほとんど仕事なんて残ってなくて、単調な最終チェックを片付けるのを手伝ってほしいだけか。"


"実はまだ仕事が山ほど残っていて、先延ばし続けて積み上がった作業が土石流みたいに俺たち全員を飲み込もうとしているのに、静音は平気なふりをしているだけか。"

stop ambient fadeout 1.0


label jp_A27d:



scene bg school_scienceroom
with locationskip


"昨日までと違って、俺は教室に入るのが遅いほうだった。"


"逆に、ほとんどクラスの全員がすでに来ているみたいだ。もうクラスメイトの顔はほとんど見分けが付く。名前はまだ覚えてないけど。"



label jp_A27e:



scene bg school_scienceroom
with shorttimeskip

play music music_normal fadein 3.0


"だらだらと授業は進む。この学校のリズムにだんだん巻き込まれていく気がする。"


"もうノートをとるとか授業に集中するとか、そういうことも気にしなくなった。最初の数日はかなり緊張していたからな。"


"武藤先生が電気に関する授業を早めに切り上げるが、間髪入れずに学園祭について話し始める。"

show muto normal at center
with charaenter


mu "さて、知っての通り明後日は学園祭だ。お前たちの企画もうまくいくといいな"

show muto smile
with charachange


mu "当日の日曜は存分に楽しんでくれ。ただし忘れないで欲しいのは学園祭の意義、つまり……"


mi "ゲームと揚げ物！"


"俺もみんなも大笑いする。"

show muto irritated
with charachange


mu "そうだな、御門"

show muto normal
with charachange


mu "だが私が言いたいのはもっと――{w=.5}{nw}"

play sound sfx_normalbell


"その言葉の続きはお昼のチャイムに埋もれてしまい、みんな荷物を片付け始める。"


"先生はしばらく考え込むけど、もう誰も聞いていないので、あきらめて席に座る。"

stop music fadeout 2.0

scene bg school_hallway3
show crowd
with locationchange

play ambient sfx_crowd_indoors fadein 0.3


"廊下は人でいっぱいだ……つまりこの学校にしては人でいっぱいだ。ほとんどの生徒は食堂に向かっているようだ。"






label jp_A27f:

scene bg school_scienceroom
with shorttimeskip

stop music fadeout 2.0    


"ミーシャも静音も、午前中ずっと俺にちょっかいを出してこない。"

play sound sfx_normalbell


"チャイムが鳴ると、俺は二人のほうを見もせずに教室を出て行く。"

scene bg school_hallway3
show crowd
with locationchange

play ambient sfx_crowd_indoors fadein 0.3


"廊下は人でいっぱい……つまり、この学校にしては人でいっぱいだ。ほとんどの生徒は食堂に向かっているようだ。"





label jp_A28:

scene bg school_council
with locationchange

show misha perky_smile at twoleft
show shizu behind_smile at tworight
with charaenter


"生徒会室に入って中を見渡すと、誰もいなかった。"


hi "あんまり仕事は残ってないみたいだな？　ほかに誰もいないみたいだし"

show misha sign_smile
with charachange


mi "ここはいつもこんな感じだよ、ひっちゃん～！"


"前から思っていたけど、今まではっきりとは確かめられなかったことが今はっきりした。静音とミーシャこそが生徒会なんだ。これで全部、他には誰もいないんだ。"


hi "くっそ、やっぱりそうだったんだな。生徒会には本当にお前ら二人しかいないんだ"

play music music_ease fadein 4.0

show misha hips_grin
show shizu cross_wut
with charachange


"静音は恥じるべきか怒りで爆発するべきか迷っているように見える。ミーシャも笑おうか静音を止めようかと、同じくらい迷っているようだ。"

show shizu behind_frustrated
with charachange


shi "……"

show misha sign_smile
with charachange


mi "じゃあひっちゃん、喜んでちょうだい。わたしたち三人しかいないんだから、やることはいっぱいあるのよ！"
mi "いっぱい～！　いっぱい～いっぱい～いっぱい～……"


hi "全然嬉しくないぞ"

show shizu adjust_happy
with charachange


"でも静音は大いに嬉しそうだ。"

show misha cross_laugh
with charachange


mi "わはは～！"

show misha hips_grin
with charachange


mi "冗談だよ！"

label jp_A28a:


scene bg school_council
with shorttimeskip



"仕事というのは書類の仕分けと再チェックだった。学園祭のような大きなイベントに必要な書類の量は、膨大なものだ。"



"事務の仕事ってのは気が遠くなるな。"

play sound sfx_normalbell


"それでも、昼のチャイムが鳴る前になんとか片づける。"

show misha hips_grin at twoleft
show shizu adjust_happy at tworight
with charaenter


mi "おっけ～、仕事も済んだし、少し休めるよ！　でもあんまりゆっくりはできないよ、午後にはもっとたくさんあるからね～！"

label jp_A28b:

$ renpy.music.play(music_ease, fadein=4.0, if_changed=True)

show shizu behind_smile
with charachange


shi "……"

show misha sign_smile
with charachange


mi "ほんとはそんなにいっぱいでもないよ、ひっちゃん～。だから～、先にお昼食べる時間はあるよ"

show misha cross_laugh
with charachange


mi "ははは～！"


"どこからともなく、二人はプラスチックの容器を一式取り出す。"

show misha hips_grin
with charachange


mi "ふむふむ～……チキンカツと、つけあわせにトマトともやしだよ～！　もう聞いただけでおいしそうだよね、ひっちゃん！"


mi "今朝作ったばっかりだし、まだ温かいから、食べて食べて食べて～！"


"俺は容器を一つ取り上げて開いてみる。見た目もいいし、おいしそうな匂いがする。とても腹が減っているので、余計にそう感じる。"


hi "おー、すごくおいしそうだな。どこで買ってきたんだ？"

show shizu basic_normal
with charachange


shi "……"

show misha hips_smile
with charachange


mi "そんなのどうでもいいでしょ、ひっちゃん！"

show misha sign_smile
with charachange


mi "お弁当の屋台を出すはずだったんだけど、担当の子が急にできないって言いだしたの。しっちゃんは『ひっちゃんをだましてこれ作らせるのにすごく苦労したのに、無駄になっちゃった～』って――"


hi "おい、なんだって……"

show misha hips_grin
with charachange


mi "……それで～！　しっちゃんは自分でできるか試してみたけど、結局やめることにしたの。ね、しっちゃん～？"

show shizu basic_angry
with charachange


"静音は腹立たしげにすねてしまい、ミーシャを不満そうににらみつける。今の話は俺が聞いたらまずかったんじゃないか。"


hi "この弁当は実験ってことか？"

show shizu behind_frown
with charachange


shi "……"

show misha sign_smile
with charachange


mi "わたしも食べるよ、ひっちゃん～！"

show misha hips_grin
with charachange


mi "しっちゃんもね～！"


"答えになってないだろ！"


"それでも、俺は静音がくれた箸を割ってチキンカツを一切れつまみ、口に放り込む。"


hi "すごくおいしいじゃん。驚いたよ。静音がこんなに料理が上手だなんて思わなかった"

show shizu basic_frown
with charachange


"静音が箸をおいて、そっけなくミーシャに手話する。ミーシャは通訳しようとして、食べていたチキンカツをとても難儀そうに飲みこむ。"

show misha sign_smile
with charachange


mi "ひっちゃん～！　口に食べ物を入れたまましゃべらないの～！"


hi "別に好きでやってるわけじゃないぞ。ていうか、母親みたいなこと言うよな……"

show shizu behind_frown
with charachange


shi "……"

show misha hips_frown
with charachange


mi "あなたは食事もまともにできないってことよ、ひっちゃん～！　それだけ～！"

show misha perky_sad
with charachange


"膠着状態だ。俺は静音と話そうとすれば食事ができないし、静音は俺の食べ方が行儀悪いとガミガミ叱るので食事ができない。"
"間に挟まれたミーシャも同じ状態で、ことの成り行きに一番がっかりしているようだ。"

show shizu behind_blank
show misha perky_smile
with charachange


"どちらにしても、もともと熱々だったわけでもない食事はどんどん冷めていく。結論はともかく、そのことに気づいた俺たちはさっさと話をやめにして、食事にありつく。"

play sound sfx_warningbell


"しばらくしてチャイムが鳴る。でもミーシャは静音に伝えようともしない。また授業をさぼって一日ここで過ごす気なんだろう。間違いない。"

show shizu adjust_smug
with charachange


shi "……"

show misha sign_smile
with charachange


mi "ひっちゃん、学園祭は何か予定ある？"


hi "いや、特にはないよ。もともと転校して一週間しかたってないんだし、そんなにすぐに予定なんて立てられるわけないし"

show misha cross_laugh
with charachange


mi "わはは～！　ひっちゃん、いっぱい手伝ってくれたじゃない。あんまり自分を安売りしちゃだめだよ！"


hi "わかったよ"

show shizu basic_angry
with charachange


shi "……"

show misha hips_frown
with charachange


mi "本気で言ってるんだから～！"


hi "わかったってば！"


"二人とも、ほんとにおかしなことに怒りだすな。"

show shizu adjust_happy
with charachange


shi "……"

show misha hips_smile
with charachange


mi "学園祭には行くんだよね、ひっちゃん？　少なくともわたしたちが、どれだけのことをじょう……じゅ……？　したのか、見ておくべきよ"
mi "誰だって、自分の仕事の成果を見て、それをちゃんと理解するべきよ！　それがわたしの信念なの～！　ひっちゃんも例外じゃないわよ！"

show misha perky_smile
with charachange


mi "ひっちゃん、絶対行ったほうがいいよ～！　ほかに予定がないなら、わたしたちも一緒につきあってもいいよ～！"

show shizu adjust_blush
with charachange


hi "ほかに何か手伝うことはないか？　助けがいるなら、しばらくここにいても構わないけど"


"さっきよりもずっと気分が楽になっている。心配ごとや恐れもとっくになくなっている。静音と楽しく過ごしていたら、今朝のトラブルのことも今のいままですっかり忘れていた。"


"静音と楽しく……いまいちしっくりこない考え方だ。でも思い返せば、この数日間静音とミーシャと一緒に過ごした時間は本当に楽しかった。まあそうでないこともあったけど、それでも。"


"一緒に学園祭に行くんだったら、もう少しここにいたっていいか。授業に行くよりはよっぽどいいだろう。"

show shizu behind_blank
with charachange


shi "……"

show misha hips_smile
with charachange


mi "ほんとに、ひっちゃん？　おっけ～！　じゃあその分でお弁当のおごりのお返しってことにしておくね～！"

show misha cross_laugh
with charachange


mi "いいね、すごくいいね、すっごくすっごくいいね～！　どっちみちしっちゃんは後で仕事頼むつもりだったんだけどね！　あははは～！　わははははは～！"


"それはおごりとは全然言わないだろう。普段なら俺は怒るか、少なくともちょっとは動揺したと思う。でも今までよりは気分が良くなっているので、俺は突っ込まないことにする。"


"手伝いというのは、書類にはんこを押したり、５０種類の予算計画書をそれぞれ１００００部コピーするような仕事がほとんどだった。"


"難しくはないけど非常に退屈だ。しかもミーシャによれば、二人の仕事の中でも一番単純なほうらしい。"


"どんどん疲労がたまっていき、同時に授業に戻る意欲が失われていく。さぼっている時間が長引くほど、立ち上がって教室に戻るのが難しくなるわけで、これは実にまずい。"


"こいつら、本当にろくでもないお手本だな。悪い影響を与えまくりだ。別に俺が心配してるってわけじゃないし、生徒から尊敬されてるとも思えないけど、世の中って往々にしてそんなものか……"

show shizu adjust_happy
with charachange


shi "……"

show misha hips_grin
with charachange


mi "おわり～！"


hi "お、ずいぶん早いじゃん。こっちは次の授業が始まるまでには終わると思う"

show misha sign_smile
with charachange


mi "ちがうちがう、ひっちゃん、もう全部片づいたの。だからひっちゃんもおつかれさま～！"


hi "全然訳わからないぞ。じゃあ仕事ってのは全部適当で、ただ意味もなく俺を引き留めてたってことか？"

show misha hips_grin
with charachange


mi "ちがうよ～……"

show shizu basic_normal
with charachange


shi "……"

show misha perky_smile
with charachange


mi "でも長く引き留め過ぎちゃったね～！　もう授業に戻ったほうがいいわ、ひっちゃん～！　今ならまだ、残りの授業に十分間に合うよ！"


hi "お前らはどうするんだ？"

show shizu behind_blank
with charachange


shi "……"

show misha hips_smile
with charachange


mi "もちろん行くわよもちろん。すぐについていくから！"

stop music fadeout 6.0

scene bg school_hallway3
with locationchange


"安心して、俺は教室に戻ろうとする。でも授業はだいたい半分くらい過ぎていたし、あまり戻る意味もない気がしてくる。なので、廊下でジュースを飲みながら次の授業まで暇をつぶすことにする。"


"生徒会室のドアをしばらく眺めてみるけど、ドアは開かない。どうしてこんなに時間がかかるんだ？　俺がやっていた作業を仕上げるのに忙しいのか？"
"まあ、それならそんなに時間がかかるはずはない。まだ仕事が残っていて、単に俺に出て行ってほしかった、ということでなければ。"


"考えれば考えるほど、そんな気がしてくる。"


"静音は……まあ、バカではないけど、でも不器用なところがあるよな。明らかに。"


"話ができないから、そういうのが難しい、ということなのかもしれない。静音にはミーシャがいるけど、それがどんなに簡単そうに見えても、通訳のいらない会話と手話の間にはやっぱり違いはある。"

play sound sfx_normalbell


"戻って二人の様子を確かめてみようか、と考える。でもチャイムが鳴ってしまったので、俺は教室に戻らないといけない。"

scene bg school_scienceroom
with locationchange


"数分後に、二人とも教室に入ってくる。さっきの考えごとも、平凡な学校生活にまぎれてすっかり忘れてしまう。"

with shorttimeskip


"ふと気がつけば、とっくに一日の授業は終わっていた。疲れはてた俺は部屋に戻って、宿題をやって寝るくらいしかできない。"

$ suppress_window_after_timeskip = True

scene black
with Dissolve(3.0)




label jp_A29:

scene bg school_hallway3
show crowd
with None

play ambient sfx_crowd_indoors fadein 0.3
play music music_emi fadein 0.3

show emi basic_happy at center
with charaenter


emi "久夫く――ん！"

show emi excited_proud
with charachange


emi "あたし、今回限りの超スーパースペシャルランチを久夫くんにごちそうしちゃいます！"

show emi excited_laugh
with charachange


emi "笑美ちゃんお手製のお弁当に、超セクシーな美少女二人が一緒にいてくれるオマケつきなの！"


"笑美の大げさで軽薄な売り込みが廊下に響き渡り、多くの生徒の注目の的になる。"

show emi basic_closedgrin
with charachange


"おかしな誘いをさらにプッシュするように、笑美は自信満々にポーズを取り、とっても控えめな胸を張ってＶサインをきめる。"


hi "そりゃおいしそうだ。俺がご招待にあずかる理由は何かあるのかな？"

show emi excited_proud
with charachange


emi "久夫くん、マジで途方に暮れてて悲しそうに突っ立ってたから、それで一緒にどうかなって思って"


"そいつは考えうる限り、もっとも憂鬱な理由だ。"

show emi basic_closedgrin
with charachange


emi "どうするの？　来ないなら久夫くん、きっと寂しく一人ぼっちで食堂のヒドいご飯を食べることになっちゃうよ"


hi "ええっ……"

show emi excited_proud
with charachange


emi "冗談、冗談だよ！"


hi "わかった、じゃあその話乗るよ。喜んで"

show emi basic_happy
with charachange


emi "んじゃ、屋上行こ！"


hi "屋上？"


hi "なんで屋上なんだ？"

show emi basic_closedgrin
with charachange


emi "そこでお昼食べるからに決まってるじゃん！"


emi "それに行かないと、あの子どっかにふらふら行っちゃうし。あの子絶対お弁当持ってこないから、お腹空かせちゃうってわかってるし！"


hi "あの子？　誰だよ？"

show emi basic_closedhappy
with charachange


emi "ほら、行くよ！"


"質問に答えず、俺の返事も待たずに、笑美は俺の腕を取って廊下を引っ張って行く。"


"途中、何とか話をしようと試みる。"


hi "どうして余分に弁当なんて持ってるんだ？"

show emi sad_grin
with charachange


"笑美は気まずそうに微笑む。"


emi "ホントはね、これ昨日のお弁当なの"


emi "お昼休みに走ってて、食べるの忘れちゃったの"


"ふーん。"




label jp_A29x:


"笑美の表情が可笑しくて、声を出して笑うところだった。"


"笑美はクスクス笑う。思い出し笑いだったり、誰かのことを笑ったり、何の理由もなかったり、そんな笑い声が俺は好きになる。"


"笑美の陽気で生き生きした性格のおかげで、静音やミーシャとけんかした時から続く、頭を締め付けるような感覚が楽になる。"


"俺はそのことを心から追い出し、今日初めて笑う。"



label jp_A29a:


scene bg school_hallway3
show crowd
with None

play ambient sfx_crowd_indoors fadein 0.3


"いつもなら人の流れに乗って食堂に行き、一人でさっさと昼飯を食べるところだけど、今日は違う。"


"今日は屋上でのランチに招待されている。"


"おかしな場所だけど、行けと言われたしな。"


"幸い、教室のドアの陰に隠れて、どっと出て行く人ごみをかわすことができた。"

stop ambient fadeout 1.0

hide crowd
with Dissolve(2.0)


"そのうち喧騒も落ち着き、俺はためらいつつ廊下へと踏み出す。"


"すると、笑美がいる。弾丸のように廊下を突っ切ってこっちに来る。"

play music music_emi fadein 0.3

show emi basic_happy at center
with charaenter


emi "あっ！　ハーイ、久夫くん！　丁度よかったぁ！"

show emi excited_proud
with charachange


emi "スーパースペシャルランチ、ちゃんと持ってきたよ、約束通り！　屋上行こうよ！"



label jp_A29b:



stop music fadeout 2.0
stop ambient fadeout 1.0

scene bg school_staircase1
with locationchange


"屋上への階段は少しおんぼろだけど、明らかに最近使われた跡がある。"


"階段の最上段にあるドアは、南京錠がなくなっている。"


"鍵を取り外した怖いもの知らずなやつは誰なんだろう？"

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 2.0

scene bg school_roof at bgright
show emi basic_closedgrin at center
with Fade(0.5,0.3,1.0,color="#FFF")


"笑美はドアを強く押し開け、太陽の光が降り注ぐ中へ笑顔で足を踏み入れる。"

show rin silhouette at offscreenright
with None

show bg school_roof at center
show emi basic_closedgrin at left
show rin silhouette at tworight
with ease

show emi basic_shock
with vpunch


"突然、背の高い人影が俺たちの前に姿を現し、堂々と立ちふさがる。たじろいだ笑美は、階段から転げ落ちそうになる。"

$ doublespeak (emi, rin_, "キャーッ！", "こんちは")

show emi basic_hes
with charachange

show emi basic_hes at twoleft
with charamove


emi "わぁ！　ビックリしたじゃない、琳！"


"ちょっと待てよ、こいつは……"

show rin relaxed_surprised
with charachange

play music music_rin fadein 2.0


rin "こんちは"


"琳が俺に話しかけていると気づき、不思議そうに笑美がこちらを見つめる。"

show emi basic_confused
with charachange


emi "二人とも知り合い？"


"俺はわけが判らなくなって笑美を見る。"


hi "こいつがさっき言ってた友達？"

show rin relaxed_nonchalant
with charachange


"琳は学校の真上を流れる雲へ目を向ける。"


rin "笑美、この人と知り合いだったんだ。知らなかったよ"

stop music fadeout 2.0


"……"


"気まずい沈黙が流れる。でも笑美がこの偶然に肩をすくめ、小さくクスクス笑いだすと、それもすぐに途絶える。"

show emi basic_closedgrin
with charachange


emi "あたしが久夫くんをお昼に誘ったの。琳が久夫くんのこと知ってるなら、ちょうどいいわ"

show rin basic_deadpan
with charachange


rin "あれ。じゃあ私は昼ご飯なしってこと？　それともお弁当はないけど久夫をお昼に誘ったの？"

show emi basic_grin
with charachange


emi "うーん、どっちもはずれ。三人分用意してるの"

show rin basic_deadpanamused
with charachange


rin "さすがだね"

hide rin
hide emi
with charaexit


"笑美たちはお喋りしながら屋上のむこう端へと歩いていく。俺は時計台の辺りで少し立ち止まり、この状況を理解しようとする。"

play music music_soothing fadein 0.5


"屋上には俺たち以外誰もいない。ここの屋上は、他の学校ほどには人気のある場所じゃないらしい。"


"屋上の端には、古びたベンチとテーブルが点々と置かれている。ここのわびしい雰囲気を少しでもマシにしようとしたんだろう。"


"俺たちの足元で、屋上を覆う小さな石ころがガラガラと音を立てる。"


"金網フェンスを通して、学校のグラウンドやその彼方が垣間見える。"


"生徒たちは二人組やグループになって、中庭や食堂をぶらついている。"


"何台か運送トラックが学校の前を通り過ぎ、近所のコンビニのほうへ向かっている。"


"どこかで番犬が通行人に向かって吠えている。"


"街の中心のほうを眺めていると、どうしてなのか、このちっぽけな町の雰囲気に俺の胸が震える。触れたら判りそうなくらいに。"


"ここだと、大都市での忙しい生活がとても遠く、異質なもののように感じられる。誰もバスに必死で駆け込んだりしないし、ネオンの光や渋滞にくらくらすることもない。"


"俺の新しい居場所を見渡しながら、ここでの新生活に対してかなり楽観的になる。それがたった一年の間だとしても。"


"病気が見つかったこととか、家を出たりしたことが、何もかも急に起きたおかげで、そのことを自分自身でどう思っているのか、振り返る時間がなかった。"


"時計台の影から広々とした場所に一歩踏み出すと、背中に温もりを感じる。"


"澄み切った青空に太陽が輝いている。"


"冷たい風が屋上を通り過ぎ、ほんのわずかだけど体が震える。"


"風が木や草花の匂いを運んでくる。ほんの数週間前は、風が運んでくるのはスモッグや車の排ガスだけだったのに。"


"笑美は琳を従えてベンチに腰掛け、大きな弁当箱１つと小さな弁当箱２つをかばんから取り出す。"

show rin basic_deadpannormal at tworight
show emi basic_happy at twoleft
with charaenter


emi "おいでよ、久夫くん！　早く早く！"


"笑美はすでにギュウギュウ詰めのベンチに場所を作り、手招きする。"

hide emi
hide rin
show bg school_roof at bgleft
with charamoveoutleft

show emi basic_happy_close at closeleft
show rin basic_deadpannormal_close at closeright
show bg school_roof at center
with charamoveinleft



"俺はできるだけ場所を取らないようにベンチの隅に座る。かなり窮屈だけど、なんとか３人収まった。"


hi "素敵な眺めだな"

show emi basic_closedhappy_close
with charachange


"笑美はクスクス笑いをこらえて琳の前に弁当箱を置き、もう一つを俺に手渡す。"

show emi excited_proud_close
with charachange


emi "はいどうぞ！　お約束どおりのお弁当だよ！"


"まさしく笑美の手作りだ。すごいもんだな。"


hi "すげぇ。こりゃマジで美味そうだな"

show emi excited_amused_close
with charachange


emi "ありがと！　あたし、作れるときは自分でお弁当作るんだ"


"俺が弁当を食べるのに忙しくなると、会話が途切れる。"

show rin basic_awayabsent_close
with charachange


"弁当を何口か食べ、チラッと顔を上げると、琳が足だけで器用に弁当箱を開け、フォークでご飯をすくってポイッと口に入れるのに気づく。"


"以前にも見たけれど、琳の器用さに感心せずにはいられない。"


"そして、自分が今いる場所のことも思い出す。"


"こんな光景に慣れることができるのだろうか。"


"慣れることがいいことなのか悪いことなのかも、俺には判断できない。"


"この場所に慣れるってことは、俺が『普通の人間』であることをあきらめるってことなのか？"


"それとも、周りにいる人たちのことをもっと思いやれるようになっているだけなのか？"


"笑美が先祖の仇と戦うかのように弁当をがつがつ食べるのを見て、俺の気が逸れる。"

show rin basic_absent_close
with charachange


hi "なんかかなり腹ペコみたいだけど"

show emi basic_grin_close
with charachange


"笑美は顔を上げ、口に入ったままの食べ物を飲み込んでうなずく。"


emi "朝練でいっつも食欲が増すの"

show emi basic_closedhappy_close
with charachange


emi "それっていいことなのよ。だってお昼ご飯もすぐに燃えちゃうから"

show emi excited_proud_close
with charachange


emi "そのおかげで女の子らしいスタイルを保ててるの"

show rin basic_deadpan_close
with charachange


rin "女の子っぽいスタイルがなくなるとどうなるの？　男になっちゃうとか？"


"笑いをこらえようとして、昼飯が危うくのどに詰まりそうになる。"

show emi basic_annoyed_close
with charachange


emi "言葉のあやよ"

show rin basic_deadpandelight_close
with charachange


rin "スタイルも朝走らないといけないの？"


hi "お前ら、いっつもそんな風に話してんのか？"

show rin relaxed_surprised_close
show emi basic_confused_close
with charachange

$ doublespeak(emi, rin, "どんな風に？", "どんな風に？")


"ああ、今のでよくわかった。"


hi "あぁ、気にすんなって"


hi "そうだな、うーん……"


"何か世間話をしようと考えてみるけど、今さらの質問に落ち着く。"


hi "二人はどうやって知り合ったんだ？"

show rin basic_awayabsent_close
with charachange


"琳は、質問を笑美に答えさせようとしているらしい。"

show emi basic_grin_close
with charachange


emi "部屋を決める人が、あたしたち互いを補えるだろうって思ったの。だから隣同士の部屋になったってわけ"


hi "互いを補う？"

show rin basic_deadpannormal_close
with charachange


rin "靴と服の関係みたいなもんかな"


hi "はぁ？"

show emi basic_closedgrin_close
with charachange


"笑美は俺が混乱してるのを見てクスクス笑う。"


emi "一緒にすると、手足が揃うの。わかった？"


hi "あぁ"

show emi basic_happy_close
with charachange


emi "それであたし、琳の朝の支度を手伝うことにしたの。そういうこと！"

show emi basic_grin_close
with charachange


emi "だってさ、毎朝着替えを手伝ってて、仲良くならないわけないでしょ？"


hi "確かにな"


"このタイミングを見計らって琳が言葉を差し挟む。"

show rin basic_deadpan_close
with charachange


rin "私、シャツ着るの大変なの"


hi "そうだな、そりゃ……見ればわかるよ……"

show rin basic_surprised_close
with charachange


rin "ホントに？"


hi "なんとなくだけど……"


"フォローになってない。とはいえ、笑美はこのやり取りを面白がっているようだ。"


"琳が純粋に好奇心から聞いているってこともあり、気持ちは軽くなるものの、まだ俺は困惑している。"


hi "だってほら、ないじゃないか、腕"


hi "そんで、えーと、シャツを着たりするのが……難しそうだなって"


"よし。俺もう話すのやめる。"


"長い目で見れば、そのほうがずっと厄介ごとが少なくて済むだろうさ。"


"琳は頷く。たぶん思慮深そうな態度のつもりなんだろうけど。"

show rin basic_lucid_close
with charachange


rin "なるほど"

show rin basic_absent_close
with charachange


"俺が弁当に意識を戻すと、また会話がとぎれる。"


"本当に美味しかった。"


"笑美が最初に弁当を食べ終え、満腹の声を上げる。"

show emi excited_laugh_close
with charachange


emi "あー、おいしかった"


"笑美が忙しく弁当の片付けをしてると、琳が声を上げる。"

show rin basic_deadpan_close
with charachange


rin "のど渇いた"

show emi basic_shock_close
with charachange


emi "あーっ！　すっかり忘れてた！　ゴメンね！"

show emi basic_closedgrin_close
with charachange


"見せびらかすように、笑美はかばんからジュースのパックを３本取り出す。"


"俺にクランベリージュースの入ったパックを放り、琳には苺ミルクのようなピンク色のやつを渡し、自分は同じピンクのフルーツパンチらしいパックを取る。"

show rin basic_awayabsent_close
with charachange


"琳は器用にストローをパックの上に突き刺して飲み始める。"


"琳の適応力にまたもや感心してしまうけれど、今回は心の中にしまっておこう。"


"どういうわけか、笑美や琳が、それぞれの障害とどう付き合っていくかをじっくり考えたりするタイプだとは思えない。"


"特に琳はそうだ。"


"実際、琳からは腕が無いことにまるで気づいてない、そんな印象を受ける。"


"意識してそうしているかいないかはまた別問題だ。"


"正直なところわからない。"

show emi basic_grin_close
with charachange


emi "久夫くん、ここの屋上どうだった？"

show rin basic_absent_close
with charachange


hi "んん？"


hi "マジで良かったよ。俺、高い所からの眺めって好きでさ"


hi "屋上に誘ってくれてありがとな"


hi "あと昼飯もな。美味しかったよ"

show emi excited_amused_close
with charachange


"笑美は１０００ワットの笑顔でニッコリと微笑む。俺の反応に喜んだから、だと思う。"


emi "どういたしまして！"

show emi excited_proud_close
with charachange


emi "またいつでも一緒に食べに来てよ、ね？"


emi "久夫くんのお弁当は作らないけど、自分のを持ってくればいいから"


hi "お弁当はナシかよ？　どうしようかな……"

show emi basic_annoyed_close
with charachange


"笑美は拗ねたふりをする。"


emi "あたしの親切に乗っかろうとしてるんだ？"


emi "ずうずうしいんだから！"

show emi basic_closedgrin_close
with charachange


"笑美がクスクス笑う。"

show emi sad_depressed_close
with charachange


emi "そうね、それが久夫くんの答えなら、あたし、ずっと琳と二人だけでお昼食べるから……"


"ふくれっ面をした笑美の、今までで一番にキュートな子犬みたいな瞳が俺に不意打ちを食らわす。"


hi "冗談！　冗談だってば！"


hi "もちろんまたここで昼飯を食べるよ"


hi "眺めもいいし、メンバーも悪くないしな"

show emi basic_grin_close
with charachange


"笑美は『悪くない』って言い方にちょっとまゆを寄せたけど、俺が誘いを受けてくれたことはとても嬉しいみたいだ。"


"これで、俺たちは友達なのかな。"


"少なくとも知り合いかな。"

play sound sfx_warningbell


"昼休みの終わりのベルが鳴る。階下に戻る時間だ。"

show emi basic_hes_close
with charachange


emi "ちょっと琳、またご飯残してる！"

show rin basic_deadpan_close
with charachange


rin "私、そこまでお腹すいてなかったんだ"

show emi basic_annoyed_close
with charachange


emi "もう、ちゃんと食べなきゃ、そのうち消えてなくなっちゃうよ！"

show rin relaxed_boredom_close
with charachange


"琳は肩をすくめる。それでも構わないと言わんばかりに。"

stop music fadeout 4.0


hi "ほら、もう行かないとだぜ"

stop ambient fadeout 2.0

scene bg school_staircase1
with locationchange


"三人揃って階段を下りる。"

scene bg school_scienceroom
with shorttimeskip


"午後の授業は過ぎていく。またしても放課後の予定がないことに気づき、読み終えた本を何冊か返しに図書室へ向かうことにする。"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

scene bg school_library
with locationskip


"図書室の中を歩くと、火曜日と同じぐらいしか生徒がいないことがわかる。部屋全体を包む、せき一つない静寂からもそのことは明らかだ。"

play sound sfx_impact2
with vpunch

show yuuko panic_up at center
with easeinbottom

play music music_happiness fadein 2.0


"借りた本をカウンターの返却口に放り込むと、優子さんが突然その後ろから飛び出す。本が彼女の隣にあるトレイに当たって立てたバンという音で驚いたらしい。"


hi "あ、すみません、優子さん。驚かすつもりじゃなかったんです"

show yuuko worried_up
with charachange


yu "ううん、いいの。大丈夫だから。こんなことは……しょっちゅうあるの。もう慣れちゃったから"

show yuuko neurotic_up
with charachange


yu "あ、何か手伝おうか？"


hi "大丈夫ですよ。どこに何があるかはわかってますから。ありがとうございます"

hide yuuko
with charaexit


"１、２冊本を借りていこうか。そんなにすることもないし、病院に入院してる間にたくさん本を読んだせいで、本を読まずにはいられなくなってしまっている。"

stop music fadeout 5.0


"何か目ぼしい本がないか探しながら小説の区画辺りをぶらつき、図書室の奥へと向かう。"


"そうしながらも、以前華子に出会った本棚の角のあたりを見渡す。何かを期待していたわけじゃない。"

scene ev hana_library_read_std
with locationskip


"……けど、意外にも華子がいて、すっかり分厚い本に夢中になっている。邪魔するのはやめようと思い、本を探しに戻る。"

scene bg school_library_ss
with shorttimeskip

play music music_tranquil fadein 6.0


"それからどれくらい経っただろうか、通路の本棚全部に目を通し、ようやく俺は２冊の本を取り出す。"


"寄り道せずに素早くカウンターへ向かって本を借り、かばんへ入れつつ図書室を出る。"

scene bg school_courtyard_ss
with locationskip


"本校舎を離れるころには、日暮れが近くなっていた。残ってる生徒たちがポツポツと出てくるけど、大半の生徒はとっくに校舎からいなくなっている。たぶん自宅か寮に戻ってるんだろう。"



label jp_A29c:

scene bg school_dormhisao_ss
with locationskip


"俺はすっかり疲れた気分になって、借りた本を読もうと自室へ戻る。もう十分過ぎるくらいの運動と興奮のあった一日だし。"


"まずは『不思議の国のアリス』だな。もちろんこの話は知ってるけど、原本を読んだことは一度もない。"


"いかれた登場人物やナンセンスな筋書き、覚えていた通り、奇抜な物語だ。"


"俺は自分のことをアリスのように考え始める。不運にもウサギの穴から転がり落ちて、たどり着いたのは『かたわの国』。"


"……いや、今のはひどい言い方だ。それでもこの孤立した立地と、なにもかもをありのまま受け入れるこの学校のやり方は落ち着かない。ここは全くの別世界みたいだ。"


"どうして、自分がアリスみたいによそ者だという感覚を振り落とすことができないんだろう。ここの人々のほとんどはとても親切で友好的なのに。"


"ページをめくりながら、俺の意識はさらに本から離れていく。心臓の鼓動がシャツの布地に打ち付ける音が聞こえそうなくらい静かだ。"


"どういうわけか、岩魚子に森で会ったあの時のように、マジで心地が悪くなる。気持ち悪くて恐ろしい何かと、一緒の檻に閉じ込められたみたいだ。"

stop music fadeout 5.0

scene bg school_dormhisao_ni
with Dissolve(3.0)


"しばらく本を置き、天井を見つめ、ゆっくりと嫌な気持ちを振り払う。"


"２００ページを過ぎたあたりで、俺は眠りに落ちる。"

scene black
with shuteye




label jp_A30:

scene bg school_courtyard_ss
with None

$ renpy.music.play(music_tranquil, fadein=3.0, if_changed=True)


"何か食べ物を買ってこないとな。ここにいる間、ずっと学食や外食だけで食いつなぐわけにはいかない。"

scene bg school_gate_ss
with locationchange


"門に向かいながら、この一週間の疲れを払いのけるように何度か大きく伸びをする。"

scene bg school_road_ss
show lilly back_smileclosed_ss at center
show lillyprop back_cane_ss at center
with locationchange




"門を抜けて角を曲がると、小さな町へと続く下り坂を一人きりで歩く人影が見える。あの髪の色と、杖を突く音は間違えようがない。"

show lilly cane_surprised_ss
hide lillyprop
with charachange


"早足で追いつく。声をかけるまでもなく、こちらに気づいたようだ。"


hi "よう、リリー"

show lilly cane_weaksmile_ss
with charachange


"リリーは口を開くまでに少し間を置き、俺の声がしたほうへとわずかに顔を向ける。"



show lilly cane_smile_ss
with charachange


li "……久夫さん？"


hi "うん、俺だよ"


"リリーは声を聞き分けるのが得意みたいだ。ちゃんと覚えてくれていたことに驚いた。なんだか嬉しくなる。"


li "こんばんは。どうしてこちらに？"

show lilly cane_weaksmile_ss
with charachange


"またも礼儀正しくおじぎをしてくれる。必要ないんだと気づく前に、俺もまた礼で応じてしまう。"


hi "町に行こうとしてたんだ。君は？"

show lilly cane_ara_ss
with charachange


li "あらあら、なんて偶然なんでしょう"


hi "同じことしようとしてた？"

show lilly cane_smile_ss
with charachange


li "ええ。いつも金曜日はお買い物に出かけるんですよ"

show lilly cane_surprised_ss
with charachange


"リリーはふと立ち止まる。まるで、少し道に迷ったかのように。"


li "ですけど、いつもは華ちゃんが一緒に町に行ってくれるんです……"


"ああ、華子を心配してたのか。確かに、二人はお互いをかなり気にかけてるみたいだし。こんなふうに華子がリリーのことを忘れるなんて、ちょっと意外だ。"


hi "そうだ、華子は図書室で本を読んでたよ。きっと夢中になってるだけじゃないかな"

show lilly cane_weaksmile_ss
with charachange


"リリーは胸を撫で下ろす。"


li "そうでしたか。あの子はよくそういうことをするんですよ"


hi "本の虫ってこと？"

show lilly cane_smile_ss
with charachange


li "そうなんですよ。華ちゃんは人ごみが苦手で。みんなから離れて読書しているほうが安心するんです"


"リリーにそんなつもりはなかったんだろうけど、俺は華子と初めて出会った時のことを思い出し、苦い顔をしてしまう。"

show lilly cane_smileclosed_ss
with charachange


"そのことにはあまり触れたくなくて、俺はそのまま黙りこむ。静かな道を、二人はただ静かに歩き続ける。"


"コツ、コツ。コツ、コツ。"


"道路に車はいないし、山久の生徒たちは遥か後ろだ。聞こえるのは木々のかすかなざわめきと、リリーが白杖で地面を叩くリズミカルな音だけ。"


"なんだかいいな。俺が住んでた所の喧噪と比べると、特に。"


"気が抜けていたのか、思わず大きなあくびがでてしまう。"

show lilly cane_giggle_ss
with charachange


li "疲れましたか？"


hi "まあね、ここ数日はボロボロになってたから"


"正直、これでも控えめな言い方だ。普通は転校するだけでも大変なのに、これだもんな……"

show lilly cane_smile_ss
with charachange


li "まあ。何もかもうまく落ち着くといいですね。学園祭で皆さんが大わらわな中に、あなたは放り込まれてしまったわけですから"


"少しの間、俺はためらう。でもリリーなら、本音を言ってもうまく受け止めてくれるだろう。洗いざらい話してみることにする。"


hi "そうかもね。でも山久って、何かが違うんだ。ほら、なにもかも堅苦しいところとか、人里離れた環境とか……一番の違いは言うまでもないけどね"


hi "なんていうか、物の見方がまるっきり違うみたいなんだ。そのうち俺も慣れると思うけどね"

show lilly cane_smileclosed_ss
with charachange


"リリーはその通りだと言いたげにうなずく。どうやら俺の答えがお気に召したらしい。なんだか、リリーの率いる３－２の生徒たちと華子の仲間にされたような気分だ。"


"まあ、悪い気はしない。なんにしたって胸の内を打ち明けられて良かった。"

show lilly cane_smile_ss
with charachange


li "前向きに見れば、新しいスタートのチャンスじゃありませんか。新しい友達を作る、というのは素晴らしいことですよ"


"楽天的な考え方だな。とはいえ、前向きな態度でいるのは良いことなんだろう。"


hi "そう思ったほうがいいんだろうね"

scene bg suburb_roadcenter_ss
show lilly cane_reminisce_ss at center
with shorttimeskip

stop music fadeout 6.0


"道を歩いているうちに、リリーがなんだかそわそわし始める。どうしたのか聞く前に、彼女は気を取り直したように別の話を始める。"

show lilly cane_weaksmile_ss
with charachange


li "それで、町のどちらに行くつもりなんですか？"


"とてもいい質問だ。食べ物を買いに来たつもりだけど、町のどこに何があるのか、まだ全然わかっていない。"


"ただ適当にぶらついて何か見つかればと思っていたけど、すでに日は沈みかけていて、夜ももうすぐだし、それはあまり賢明ではなさそうだ。"


"リリーに道を尋ねるしかなさそうだ。またしても。"


hi "何か食べ物を買いに行くところだったんだけど……そう言われてみると俺、どこに行けばいいかよくわからないや"

show lilly cane_planned_ss
with charachange


li "あら、それはちょうど良かったです。私、コンビニに行くところだったんですよ"


hi "じゃあ、またお世話になるみたいだね。ありがとう"


"目的の店まで一緒に歩く。リリーの横にいられるように、俺は注意深くペースを落とす。俺が普段歩く速さに比べると、リリーはかなり遅い。もちろん、理由はあるんだけど。"

scene bg suburb_konbiniext_ss
with shorttimeskip

play music music_daily fadein 2.0


"何分かたって、目的地が見えてくる。この町は本当に狭い。"

scene bg suburb_konbiniint
with locationchange


"あとはこともなく、俺たちは中に入る。レジカウンターからいらっしゃいませと声がかかる。"

show lilly cane_weaksmile at center
with charaenter


li "あなたについて行っても良いでしょうか？　いつもは華ちゃんが私を手助けしてくれるんですけど、いないので……"


"その意味がわかるまで少し時間が掛かる。"


"ラベルを読めないということもあるし、リリーにとって助けなしに買い物をするのはかなり辛いことなんだろう。"


"とはいえ、俺がここに行くと言ったときから、リリーはこうするつもりだったんじゃないか、という気がしてならない。"


hi "もちろんかまわないよ"


"入り口の横に低く積まれた、使い古された赤いカゴを二つ掴み、一つをリリーに手渡す。"

show lilly cane_weaksmile at Transform(ypos=800)
with charamove

show lilly basic_smileclosed at Transform(ypos=800)
with charachange

show lilly basic_smileclosed at center
with charamove


"リリーはそれを地面に降ろして通学かばんを入れ、白杖を縮めてカゴの取っ手に通し、また右手で持ち上げる。"


"待てよ、リリーが杖を使わないということは……"

show lilly basic_smileclosed at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with None

show lilly basic_smileclosed_close at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with Dissolve(1.0)


"考えがまとまる前に、リリーは俺のそばに寄り、か細い指で俺の制服の袖をつまむ。"

show lilly basic_concerned_close at twoleft
with characlose


li "いいですか？"


hi "あー、もちろん"

show lilly basic_smileclosed_close
with characlose


"拒む理由はない。やむを得ないとはいえ、かわいい子が俺にすがりついてくるのは悪い話じゃない。"


"俺たちは店内を進んでいく。時折すれ違う他の客は、顔色一つ変えない。"


"山久からの近さを思うと、学園の生徒を目にすること自体は、地元の人からすればまるで普通のことなんだろう。"


"各コーナーに行くごとに、手早くリリーに確認して必要なものを聞く。俺が探しているものも一緒に取って、それぞれのカゴに商品を入れる。"


"これがリリーと華子の、金曜日の日課なのだろう。"


hi "よし、あとはパンだけだ。これで俺の買い物は済んだと思うよ。リリー、他に何かいるものはある？"

show lilly basic_smile_close
with characlose


li "いいえ、これで全部ですよ"


hi "じゃあ行こうか"

show lilly basic_smileclosed_close
with characlose


"パンのコーナーにちょっと立ち寄ってから、俺たちはレジへと向かう。"


"ありがたいことに、レジで待っている人はほとんどいない。俺たちはすぐに会計を済ませ、店を出る。"

scene bg misc_sky_ni at Fullpan(15.0)
with locationchange


"リリーは白杖を取り出して、元通りに伸ばす。俺は２人分の買い物袋を持ちながら、少しの間夜空を見上げて時間をつぶす。"


"つかの間、白い息を吐こうとしてみるけど、この夏の熱気では無理がある。"


"やがてリリーは立ち上がり、さっと伸びをして自分の袋を手に取る。俺の分は袋二つだ。"

scene bg suburb_konbiniext_ni
show lilly cane_listen_ni at center
with locationchange


hi "リリーも疲れてる？"

show lilly cane_sleepy_ni
with charachange


li "学園祭の準備が本当に忙しかったものですから。羽加道さんにうるさくつきまとわれても、状況はあまり変わらないんですけどね"


hi "まあ、あいつは物事を進めようとしてただけだよ。善は急げ、だろ？"

show lilly cane_weaksmile_ni
with charachange


li "そうかもしれません。とにかく明日は町で気晴らしをするつもりです"


"学園祭の準備で、二人とも気が立っているんだろうな。"

scene bg suburb_roadcenter_ni at bgright
with locationchange


"コンビニ袋を手に、二人で話をしながら、俺たちはひっそりした通りへと差し掛かる。"


"……待て。あれはなんだ？"


"街灯の光に浮かび上がった、とても独特な人影が俺たちに向かってくるのに気づく。"


"一瞬、俺のクラスの男子かと思う。けど彼、いや、彼女が近づいてくるにつれ、すぐに誰だか見分けがつく。"

show bg suburb_roadcenter_ni at center
show rin relaxed_nonchalant_ni at right
with charamoveinright

stop music fadeout 8.0


hi "琳か？　こんな遅くにここで何やってんだよ？"

show lilly cane_surprised_ni at center
with charaenter


li "りんさん？"


"リリーは頭をぴんと上げ、周りの音を聞き逃すまいと集中しているようだ。俺が状況を説明してあげないと、と気づく。"


hi "琳だよ……名字は手塚だったと思う。ほら、俺たちの学園の"

show lilly cane_weaksmile_ni
with charachange


"リリーはその名前を聞いて硬くなり、複雑な表情を浮かべる。作り笑いと、苦々しいしかめ面を無理矢理混ぜ合わせたような。"


li "ああ。わかりました"


"リリーも琳を知ってるみたいだ。"

show rin basic_awayabsent_ni
with charachange

show bg suburb_roadcenter_ni at bgleft
show rin basic_awayabsent_ni at tworight
show lilly cane_weaksmile_ni at twoleft
with charamove


"琳はとてもぼんやりした様子でこちらを向く。俺たちに気づいていないのか、気づいてはいても、俺たちが誰だかわかっていないのか。どうにも確信が持てない。"


"ゾンビみたいだ。銅像かな。いや、ゾンビの銅像か。"


"しかし徐々に、状況を理解したような兆しが暗い瞳にきらめく。私はこれに何か反応しなくてはいけないのだ、と。"

show rin basic_lucid_ni
with charachange

show rin basic_awayabsent_ni
with charachange


"琳は瞬きをひとつする。とてもじっくりと。"

show rin basic_absent_ni
with charachange


rin "やあ"


"……"


"気まずい沈黙だ。みんな誰かが何か言うのを待っている。"


hi "こんな遅くに、ここで何してるんだ？"


"……"


rin "私……"

show rin basic_deadpan_ni
with charachange


rin "自分でも考えてたんだ、そのこと。たった今"

play music music_rin fadein 0.5

show rin basic_deadpannormal_ni
with charachange


rin "さっきも何人かの人がそう聞いていったよ。みんな同じように不思議がってた"


rin "私は知らなかった。その人たちも知らなかった。聞いてみたんだ。だから私も不思議に思ってるの"


rin "大体そんなとこ。殺人事件の推理みたいだね。人は死んでないけど"


"……"

show rin negative_spaciness_ni
with charachange


rin "その人たちならあっちに行ったよ"

show rin basic_absent_ni
with charachange


"まるで大事なことのように、琳は他の人が行った方向を指し示して右を向く。そして、時計仕掛けの凝ったカラクリ人形みたいにこっちに向き直る。"


"おとなしそうな印象を与えるタイプの割には、琳は手短に済むことについても長々と喋る。"


"琳が話し終わったのかがわからず、俺は何も言わない。今のところ、リリーも言葉が出ないようだ。"


"本当のところ、うっかり琳を刺激して、また喋り出されることが二人とも怖いんだと思う。"


"俺たちは呆然として反応できずにいるけど、琳は全くうろたえない。こっちを期待に満ちた目で見続けている。無表情な顔に浮かぶ感情らしいものはそれだけだ。"


"琳はそういう人間らしい。いつもそうやってのんきにしていて。"


"血のかわりにオス象用の鎮静剤が血管の中に流れているみたいだ。"

show lilly cane_concerned_ni
with charachange


li "健忘症なんですか？　でも琳さん、そういう症状をお持ちでしたっけ……"


hi "いや、そうじゃないと思うぞ"


hi "まあ、通りがかった人たちは心配しただけだろう。本気で迷子になったように見えるよ。そうやって道のど真ん中で立ってたりしたら"

show rin basic_deadpan_ni
with charachange


rin "ああ、なるほど"

show rin relaxed_nonchalant_ni
with charachange


rin "だったら、もっと別のポーズで立ってたほうが良かったかもね"


"このことをさらに深追いするべきか、俺の正気を保つために見切りをつけてしまおうか、しばらく頭を悩ませる。"


"俺は後者に決める。"


"大抵の場合、琳の無駄口は深読みしない方がいいらしい。"


"琳と話していると、チェスの定石を馬鹿にするように滅茶苦茶に駒を動かす、スーパーコンピューターと勝負をしているみたいだ。人間だけど。"


"そして、たとえ勝っても負けたような気分になるんだ。"


"くそ、まさしく健二が言ってた通りじゃないか。俺が勝ったとしても、俺の負け。これが、山久学園の女子のパワーか？"


"……"


"この先を考えると危険すぎるので、頭の隅に押しやる。たぶん、まいっているせいで、健二の反女性プロパガンダが心に入り込んできたんだな。"


hi "そうだな、ポーズを変えれば役には立ったかもな"


hi "それはそうと、本当にここで何をしてるかわからないのか？"

show rin negative_annoyed_ni
with charachange


"琳は眉をひそめる。俺の質問、この会話の流れ、自分が言おうとしている答え、そのどれかが非常に気に入らないようだ。"


rin "わかってるよ。少しは。それがなんなのかはうまく説明できないけど"

show lilly cane_smile_ni
with charachange


li "あら、それなら一歩前進じゃないですか"


"何かまともな会話の糸口を見つけたような話しぶりだ。俺はリリーほど楽観的な気持ちにはなれない。"


rin "そう、少しはわかってる。残りはこれから浮かんでくるよ"

show rin basic_deadpanupset_ni
show lilly cane_weaksmile_ni
with charachange


rin "うん、きっとそうだ。私にはいつも……理由がある"


"その後に続く沈黙が、リリーの期待を完膚無きまでに打ち消してしまう。あっという間だったな。"


"琳の――どうやら根拠のない――確信はともかく……どうすりゃいいんだ？"


"琳の目的がなんであれ、好きにさせて放っておくこともできる……でも、もう夜も遅いし、琳が夜中にここで突っ立っているのが見つかっても、それはそれでまずい。"


"そもそもここで何をしていたのか思い出さない限り、きっと琳はここから動かないだろう。"


"何を思って琳がこの冒険に乗り出そうとしたかを言い当てるとして、正解する確率は宝くじの一等を当てるのと同じくらいだろう。"


"何回も連続で、だ。"


"リリーは妙に静かだ。もし俺より琳のことに詳しいんだったら、少しは助け船を出してくれるとありがたいんだけど。"


"まあ、しょうがない。琳をよく知っているからこそ、リリーはおとなしくしているんだろう。"


hi "それじゃあ、どこかに行こうとしてたんじゃないのか。学校に戻ろうとしてたわけじゃなさそうだし……どこか心当たりは？"

show rin relaxed_surprised_ni
show lilly cane_surprised_ni
with charachange


"琳は何だかわざとらしくのけ反って、目を丸くする。そのせいで、こんな時のために演技を練習していたかのように見えてしまう。"


rin "君ってばエスパーなの？　それが君の障害？　すごいや！"


hi "ちが……何？　どこからそんな考えが出てくるんだ？"

show rin relaxed_disgust_ni
show lilly cane_listen_ni
with charachange


rin "私が何をしていたのか、知ってたじゃん"

show lilly cane_displeased_ni
with charachange


hi "えっとな、ただの常識に基づいた推測だ。俺たちはコンビニに行くために、さっき同じ道を反対から来たんだから"


hi "もし学校に向かってたなら、俺たちは途中で会ってたはずだろ"

show rin basic_deadpanupset_ni
with charachange


rin "ああ……"


"琳は少しがっかりしたみたいだ。"


"健二みたいに、琳はすぐ訳のわからない結論に飛躍するらしい。"


"ここの水には何か混ざってるのかもな。ジュースを買いだめしておこう、と心に刻む。"


hi "なあ、俺がエスパーかどうか聞いた人間は今週で二人目だぜ"


hi "俺、本当にそんな感じに見えるのか？"

show rin basic_deadpannormal_ni
with charachange


"琳は肩をすくめる。どっちなんだ。"


hi "あのな――{w=0.3}{nw}"

show lilly cane_smile_ni
with charachange


li "琳さんも、私たちと一緒に学校に戻ったほうがいいんじゃありませんか？"


"俺がエスパー云々という誤解をきちんと解こうとしたところで、リリーが口を挟む。心配しているような口ぶりで、見え透いた笑顔はそのことをまったく隠せていない。"


"リリーは俺と同じ結論に達したのかもしれない。みんなのために、エスパーネタはこれでやめよう。どうせ意味なんてないんだし。"


hi "ああ、リリーの言うとおりだ。何も覚えてないんだったら、ここに居続ける必要はないだろ"

show rin basic_awayabsent_ni
with charachange


"琳はしばらくの間、このどちらかといえば簡単な理論を検討し、うなずく。"

show rin basic_absent_ni
with charachange

stop music fadeout 2.0


rin "わかった"

scene bg school_road_ni
with shorttimeskip

$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_cicadas
play music music_dreamy fadein 2.0


"俺たちは再び学校に向かって歩き出す。こんなことで必要以上に時間を無駄にしてしまった。"

show rin basic_awayabsent_ni at tworight
show lilly cane_smileclosed_ni at twoleft
with charaenter


"琳は歩道の端に沿ってふらふらと歩く。夢遊病者と綱渡り芸人が合わさったようだ。リリーは俺の肩に手をかけたまま、杖で地面を叩いている。"


"カツン、コツコツ、カツンカツン、コツコツコツ。"


"その音と、とぎれとぎれの会話を除いては、あたりは静かだ。ただ、町の落ち着ける静けさとは全く別物だ。"


hi "それで、壁画はうまくいってる？"

show rin basic_deadpan_ni
with charachange


rin "縁起悪いなあ。完成前の作品のことは絶対話しちゃダメなんだよ"

show lilly cane_weaksmile_ni
with charachange


li "きっとすばらしいものになると思いますよ"

show rin basic_deadpannormal_ni
with charachange


rin "縁起悪い"


"カツン、コツ、カツン、コツ。その話をしようともしない。はじめて、リリーの礼儀正しさが場違いな気がした。コツコツコツ。"


"学園がたたずむ丘は驚くほど急だ。俺たちはペースを落とすけど、それでも自分の脈が上がり、息が辛くなっていくのを感じる。"


"あと少しだ。もう門は見えている。"


"それに気を取られていても、肩に置かれたリリーの手が少しこわばるのがわかる。何かを聞きたがっているしぐさなのだと判断し、はっきりと言う。"


hi "リリー、どうかした？"


"『そこの旅の仲間は別にしてだよ？』と、言ってしまいたい衝動をかろうじて抑える。"


"一瞬、彼女は言い出そうか迷っているように見えた。けど、結局それを口にする。"

show lilly cane_concerned_ni
with charachange


li "大丈夫……ですか？"


hi "大丈夫？　どういう意味？"


"あまりに遠回しで、わけがわからない。質問の意味が俺に伝わらなかったことで、リリーはわずかにたじろぐ。"


li "いえ、ただ……ひどく疲れているようで"


"そう言われて、自分の息がやけに荒くなっていることに気づく。上り坂にはほんとうにやられた。"


label jp_choiceA30:
menu:
    with menueffect
    "リリーはそのことに気づいたんだ。あまりに早すぎる……"
    "ごめん、俺、ほんとは調子良くないんだ":




        return m1
    "このことはあまり話したくない":


        return m2

label jp_A30a:

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
stop music fadeout 5.0


hi "だ……大丈夫だよ"


hi "心配することなんてないよ。この丘がびっくりするほど急なだけで。そう思わないか？"


hi "いったいなんでこんな高い所に学校を建てたのかな？　車椅子の生徒とかいるのに"

show lilly cane_sad_ni
with charachange


li "そうですね"

show lilly cane_concerned_ni
with charachange


"リリーの額に気遣いがしわになって浮かぶ。俺のことでリリーにこんな表情なんてして欲しくなかった。俺たちはほとんど知りあってもいないじゃないか。"


hi "な、そう思うだろ。こういう場所はどこにでもあるわけじゃないのにさ。なんでわざわざここを選んだのか不思議だよ"


"俺の声は軽薄なまでに穏やかだ。俺自身の耳にも奇妙に響くし、しゃべるのが早口すぎる。リリーは人の声を聞くだけで、どれだけのことを感じ取れるんだろう、と思う。"


li "でも……"


hi "さ、行こう。もうすぐ山久だ"

hide lilly
hide rin
with charaexit


"学校までの道のりの間、俺たちは三人ともずっと無言のままだった。"


stop ambient fadeout 3.0

scene black
with Dissolve(3.0)


label jp_A30b:

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")


hi "ちょっと一休みすれば大丈夫だから。最近、体調が良くなくて"

show lilly cane_oops_ni
with charachange


li "まあ"


li "それは……ここに転校して来たことと何か関係があるんですか？　つまり……"

show lilly cane_concerned_ni
with charachange


"リリーは不意に言葉を切る。たぶん、少し踏み込みすぎたと気づいたんだ。それにしても彼女の勘は鋭い。俺はこのことを話したくはないけど、わざわざ嘘をつくほどでもない。"


"リリーになら、俺は気にしない。"


hi "最近、ちょっと体が弱っててさ。それだけだよ"

show lilly cane_oops_ni
with charachange


li "華ちゃんが、久夫さんは割と……健康そうに見えると言っていたので、私もそうなのかと思って……"

show lilly cane_sad_ni
with charachange


"心配そうな口調のまま、リリーの言葉はまたしても尻すぼみになる。"


"眉をよせたリリーの不安そうな表情を見て、気持ちが焦る。せめて何か気を楽にしてやれることを言わないと。"


"リリーの目の障害に対する率直な姿勢を考えると、この狼狽ぶりは驚きだ。みんながリリーと同じように障害と向き合えるわけじゃないってことはわかっているはずなのに。"


hi "いや、いいんだ"


hi "俺、心臓が……壊れてる、っていうのが一番近いかな。不整脈なんだ"


hi "そのせいで、しばらく前にきつい心臓の発作があったんだよ。春の間はほとんど病院で過ごして、医者の指示で山久学園に、ってわけさ"


"リリーはそれを聞いて、静かにうなずく。"


"でも、俺の答えにリリーはますます眉を寄せる。そこまで互いを知っているわけではないから、どう反応していいのかわからないんだろう。"


"俺の立場だって全く同じだ。リリーを責めることはできない。"


label jp_A30c:


"驚いたことに、リリーはすぐに何かに思い当たったような表情を浮かべる。"

show lilly cane_oops_ni
with charachange


li "待ってください……その、笑美さんと廊下でぶつかった時も……？"


"俺はわずかに顔をしかめる。次から次へと点を結ぶリリーの能力は思ってもみないほど素早かった。"


hi "ああ、廊下で走ってはいけないっていう校則がある理由のわかりやすいお手本だな"

show lilly cane_sad_ni
with charachange


"思ったよりはるかにそっけない言い方だ。明らかにリリーはこの話を続けることをためらっている。"


label jp_A30d:


"リリーの心配を和らげてあげたいが、この話題を続けたくもない。"


hi "気にすんなって"

show lilly cane_weaksmile_ni
with charachange


"笑顔を見せて元気づけようとするけど、意味がないと気づく。そうとも知らずに、リリーは俺を元気づけようと微笑みかけてくる。ただ、それ以上は何も言わない。"

$ renpy.music.set_volume(0.5, 5.0, channel="ambient")
stop music fadeout 2.0

scene bg school_dormext_half_ni
show rin relaxed_surprised_ni at tworight
show lilly cane_weaksmile_ni at twoleft
with shorttimeskip


"寮に到着すると、琳は自分の壁画の前で雷に打たれたように立ち止まる。帰り道ではほとんど黙っていたから、琳がここにいたことをもう少しで忘れるところだった。"

show rin relaxed_disgust_ni
with charachange


rin "今日って金曜だったよね？"

show lilly cane_smile_ni
with charachange


li "ええ……金曜ですよ。６月８日の"

show rin basic_upset_ni
with charachange

play music music_rin fadein 0.5


rin "大変だ"

show lilly cane_surprised_ni
with charachange


li "大変？　どうしてですか？"

show rin negative_annoyed_ni
with charachange


rin "今すぐ膝を抱えて吐きそう。順番はもしかしたら逆だけど"

show lilly cane_concerned_ni
with charachange


li "何か問題でも？"

show rin negative_confused_ni
with charachange


rin "いや、問題はないよ。今日は金曜だから、まだ問題ない。この絵、日曜までに完成させなきゃいけないの。だから何も問題ない"

show rin negative_worried_ni
with charachange


rin "クスリでも持ってない？　あるいはタイムマシーンとか？"

show rin negative_confused_ni
with charachange


rin "これはまずい。まずいよ"


"ということは、琳の予定は遅れているのか。数日前、のんきな態度の琳に静音が激怒していたのを思うと、どうなっているのやら。"


"なんであれ、日曜の朝までにやるべき作業を終えることができなければ、琳は『だから言ったでしょ』となじられる運命にあるわけだ。"


"琳は壁画を屈辱的に見つめ続ける。"

show rin negative_annoyed_ni
with charachange


rin "先に行って。少しでも進めなきゃ"


"俺はちらりとリリーを見る。俺と同じようにあきれ顔をしているだろうかと期待したけど、考えてみればリリーはそういうことをする子じゃない。"

show rin negative_angry_ni
with charachange


rin "行って"

stop music fadeout 2.0

hide rin
with charaexit

show lilly cane_concerned_ni at center
show bg school_dormext_half_ni at bgright
with charamove


"もちろん、俺たちはそうする。これ以上琳を刺激したくない。"


"腹の中をかき回されるような、嫌な予感がする。琳には間違いなく人を不安にさせる才能がある。"


"琳を野放しにしてはいけないんじゃないだろうか。"


hi "誰かを呼んだほうがいいのかな？　ショック症か何か起こしそうだし"

show lilly cane_oops_ni
with charachange


li "大丈夫だと思いますよ。彼女はその……ええと……何て言っていいか……"


"リリーは頭を少し傾け、琳がおかしいということを、『おかしい』という言葉を使わず礼儀正しく表現しようとしている。"


hi "ユニークってこと？"

show lilly cane_weaksmile_ni
with charachange


li "ええ、とてもユニークな人なんです"


hi "それは言えてると思うよ"

show lilly cane_giggle_ni
with charachange


"リリーはその意見にクスクスと笑い、納得してうなずく。"

show lilly cane_weaksmile_ni
with charachange


li "あなたが琳さんと話している間、知らないふりをしてすみません。私……彼女のことは本当にわからないので、距離を置くようにしているんです"


"思ったとおりだ。琳を敬遠してしまった自分の短所を謝るように、リリーは申し訳なさそうな笑顔をわずかに見せる。"


"決してリリーを責めることはできない。"


"リリーは深く息をもらす。きっと欠伸をごまかしたんだろう。俺と同じように、今日の出来事に疲れたんだと思う。"

show lilly cane_cheerful_ni
with charachange


li "華ちゃんにこれを渡さないといけないので、私はもう行きますね。一緒にいてくれてありがとう、久夫さん"


"リリーは俺に愛らしく微笑む。いつもと違った感じがする。彼女はよく微笑んでいるのに。"


"その違いがなんなのかなんてわからない。ただ違っていたんだ。"


"ゆったりしていた、とでも言えばいいのか。でもそれは、単に琳から逃れた開放感のせいだろう。たぶん。"


hi "うん……おやすみ。華子によろしく言っておいて"

show lilly cane_smile_ni
with charachange


li "ええ。おやすみなさい"

hide lilly

stop ambient fadeout 2.7

scene black
with Dissolve(3.0)

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
