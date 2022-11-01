label jp_S30:

window hide None

scene bg school_library
with locationchange

window show

play music music_happiness fadein 2.0











"その翌日、もう週末がやってくる。俺は重たい本の山を司書の机に降ろす。乱暴に置くつもりはなかったけど、あまりに重くて結局大きな音を立ててしまう。"




$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_impact

show yuuko panic_up:
    center
    ypos 1.2 alpha 0.0
    easein 0.25 ypos 1.0 alpha 1.0
with vpunch

show yuuko panic_up:
    center
    alpha 1.0
with None



"優子さんが椅子から飛び上がって、勢いで眼鏡がずれてしまう。かろうじて落とさずに済んだみたいだ。"




show yuuko neutral_up
with charachange



yu "あら、こんにちは"






hi "すみません。返さないといけない本があったんで、全部返却しに来ました"




show yuuko worried_down
with charachange



yu "それはよかったわ、でもできればもっと早く返却してほしかったな。どの本も蔵書が複数あれば問題なかったけど、そんなことないし……しかもそれを私のせいにしたりする人もいるから"






hi "誰がですか？"



show yuuko panic_down
with charachange



yu "ほかの生徒たちよ。その、結構強引な子もいるから……"





hi "すみませんでした。つい忘れちゃって。この数日間、結構大変だったんです"



show yuuko worried_down
with charachange



yu "そうなんだ……えっと、そのこと話したくはないよね……"




$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve



n "\n\n優子さんは静かに、俺が持ってきた本の返却処理を始める。司書というよりは爆弾処理の技術者のように、大変な丁寧さと正確さで本を扱っている。"







n "この数日間、俺はミーシャが口にしたある言葉のことを考え続けている。もちろんミーシャの言葉は一つ残らず考えていたけど、そのうちの一言が何度もよみがえってくる。誰かと別れたり、離ればなれになったりするのはもういやだ、とミーシャは言っていた。"






n "この言葉を思い出すたび、頬を叩かれたように思考が止まってしまう。あと数ヶ月で、俺たちは卒業する。ミーシャと静音は切っても切り離せない関係だけど、卒業後は二度と逢えないかもしれない。この考えが全てのきっかけになったのだろうか。"





n "もしミーシャが静音にこの事を話そうとしても、おそらく静音はまったく取り合わないだろう。悲しい気持ちになるとわかっているからこそ、その考えを遠ざけてしまう。静音のように、すぐに自分の悩みを抑えつけてしまう人には簡単なことだろう。"






nvl clear



n "\n\nミーシャは実際には見た目よりもずっと繊細だった。静音の態度に打ちひしがれてしまったのだろう。静音は結構冷たく応じることもあるから、なおさらだ。静音がどういう反応をしたかは知らないけど、たぶんそうだったのだろうし、俺にはその理由もわかる。"






n "ミーシャが自分の一部とも言えるくらい大切な人から遠ざかってしまうことに心を悩ませているのもわかる。俺もその瞬間まで卒業の事なんて考えもしなかった。"






n "すると『本当にまだ一年も経ってないのか？』なんてことを考え始めていた。今までに出会った人たちのことを考え始めた。それは優しい思い出だった。そして、彼らを失うことを想像した。突然、俺はミーシャの不安が理解できた。"






n "\n誰かにこのことを話せたらいいかもしれないな。"




$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show


hi "実は、話したいかな、って"




show yuuko worried_up
with charachange


yu "誰と？"



"その声から、あからさまに警戒しているのがわかる。"






hi "優子さんと"




show yuuko neurotic_up
with charachange



yu "あの……本当に？　本当にいいの？　な、何で私なの？"






hi "だって優子さん、大人だし"




show yuuko neurotic_down
with charachange


yu "それだけなの？　ああああの……それは……"







"渋い表情で、優子さんは椅子の上でもじもじと体を動かす。見た目はとても居心地悪そうだけど、姿勢を楽にしようとしている。つまり、これはオーケーということだろう。"







hi "大人でいることって、大変ですか？"




show yuuko cry_down
with charachange


yu "そうね"


show yuuko panic_down
with charachange



yu "私はそこまで年は取ってないと思うけど……今の生徒たち、た、たとえば静音ちゃんとかあなたが、香水やコロンなんてつけてるのはびっくりするな……私は全然使わなかったから。今でもしないし……"




show yuuko worried_up
with charachange



yu "あの、そういえば、今日はブドウのコロンつけてないね"






hi "ええ、俺には合わなかったんで"




show yuuko worried_down
with charachange



yu "あ、よかった。私もそう思ってたから……ごめんね"







"優子さんは本当に申し訳なさそうで、俺は罪悪感にかられる。思わず笑ってしまう。あんなちっぽけな嘘でも、こういう風に俺に返ってくるんだな。"







"ミーシャにとって、静音のためにあんなに長い間自分の気持ちを隠して笑顔を作り続けるというのは本当につらかったに違いない。"







hi "いずれ俺たちも卒業するって話を知り合いが持ち出したんです。それで、自分が今までそのことを全然考えてなかったって気がついて"







hi "これだけ時間が経ってるのに考えもしなかったなんて、バカみたいな気がします。今までいい人にたくさん出会えたけど、卒業して、もう二度と会えないかもしれない、そうなったときのことを全然考えてなくて"





show yuuko neutral_down
with charachange



yu "でも、連絡を取り合うことはできるじゃない……"







hi "まあ、そうですね。子供っぽいですよね、俺。きっとみんな同じような気持ちになってるんだと思います。優子さんもそういう話をいっぱい聞いてるんじゃないですか"




show yuuko worried_down
with charachange



yu "う、ううん……私ここに来てそんなに経ってないから……"



show yuuko worried_up
with charachange



yu "私も高校を卒業するときは、同じことで悩んでた。あの、この学校に通ってたわけじゃないけどね。友達と会えなくて寂しいって思う……ちゃんと連絡を取っていればよかったって。もっと努力するべきだったのよ"






"優子さんの話を聞いてもあまり心は晴れない。俺の顔からそれを読みとって、優子さんはすぐに口を閉ざしてしまう。"






hi "俺は過去を振り返って同じような後悔をしたくないんです"



hi "静音はそもそもこういうことは考えもしないんじゃないかって思うんです。あいつはときどき、一切悔いのない生き方をしたい、ってことを延々話し続けるから"




show yuuko panic_up
with charachange



yu "うわあ……そんなの無理だと思うよ、私は……"






"俺はうなずくけど、それには半分しか同意できない。"




show yuuko closedhappy_up
with charachange



yu "それでも……それってとても立派だとも思う……なんだか勇気があるよね。そう思わない？"






hi "『勇気がある』っていうのは斬新な表現ですね"




show yuuko neutral_down
with charachange



"優子さんはこだわるように首を振る。"






yu "でも、そうなのよ。それになんだか怖い感じもするけど……"





hi "マジですか。高校生相手におじけづいたりしたらだめですよ"




show yuuko worried_up
with charachange



yu "うん、努力はするわ……"




hide yuuko
with charaexit



"優子さんは背を向けて付箋紙を何度も折り始める。大学生にしてはずいぶん不毛なことをしているけど、そんなことより、俺は間違ったことを言ってしまったんじゃないか、と自問する。"






"静音と長い間一緒にいたおかげで、沈黙の一瞬一瞬からできる限りの意味を読みとらずにはいられなくなってしまっている。"







"もし優子さんが高校生におじけづいたりしない人だったら、たぶんこんなに気軽に話しかけることはできないだろう。"






"自分の悪い部分をなくしたいと思うことは簡単なことだ。皆のことを考えたとき、まさにその部分が自分は好きなんだ。"



show yuuko worried_up at center
with charaenter


yu "あの……"

show yuuko smile_down
with charachange



yu "私、そんなに後悔してないと思う。楽しかったときの思い出を覚えてさえいれば、それで十分だ、って思ったの"




show yuuko worried_down
with charachange



yu "よくわからないわ……ごめんなさい"







"生徒が何人か図書室に来始めているのに気づく。そろそろ潮時だな。"






hi "いえ、助かりましたよ"







hi "友達が二人でけんかしてるんです。卒業したらもう会えないかもしれないってことを、一人がすごく深刻に考えてるから。もう一人はたぶんそのことに関心がなくて、余計にまずいことになってて"







hi "こういう状況でどうすればいいのかわからないんです。最終的にどちらかの肩を持つような問題じゃないと思うけど、そうなってしまうかもしれないし、もしそうなったらどうすればいいのかさっぱりわからなくて"





show yuuko neutral_down
with charachange



yu "けんかはしちゃだめって言ってあげなきゃ"






hi "わかってます。けんかはよくないです"




hi "ところで、静音とミーシャのことじゃありませんよ"

show yuuko worried_up
with charachange



yu "わかったわ……あの、そう思ってたわけじゃないんだけど……"




"なんて恥ずかしい。こうなることはわかっていたのに、自分の頬が赤くなるのがわかる。それでも俺は見え見えのうそをついてしまった。ただ、時にはそれが正しいことだってあるかもしれないだろう。"





hi "難しい決断をしなければならない人についての本ってありますか？"



show yuuko happy_down
with charachange


yu "自己啓発本ならいっぱいあるけど……"


"それを聞いて驚いている自分がおかしい。ほんの数ヶ月前までは、驚いたりしなかっただろうから。"






hi "『そのための』じゃなくて、『それについて』ですよ。そんなにたくさんはないんですよね？"




show yuuko worried_down
with charachange



yu "ええ。その、多くはない、ってことね"




stop music fadeout 3.0



"少し不安はあるけど、静音と話したいと思う。そうすることに緊張を覚える理由がわからなくて、なんだかうんざりする。"




scene bg school_council
with locationskip



"おかげで、その場で、その瞬間に、静音を探そうという気持ちになる。とはいえ、それほど頑張って探すまでもない。静音はいつものように生徒会室にいる。"




play music music_pearly fadein 5.0

show shizu behind_blank at center
with charaenter



"ミーシャは一緒ではなくて、心配になる。静音が俺に気づいて顔を上げると、俺は真っ先にミーシャがどこにいるかたずねる。"




show shizu basic_normal2
with charachange



ssh "知らないわ"




"その答えはあまりにはっきりしなくて、そのまま受け流すようなことはできない。"






his "あいつ、学校さぼってるぞ。何日も"




show shizu adjust_happy
with charachange



ssh "あなたは出席警察のつもりなの？"





his "生徒会長がそういうことを言うってのは、ずいぶんおかしな話だな"




show shizu adjust_smug
with charachange



"静音は手で口を覆って笑顔を隠す。俺の心配は取り越し苦労なのかも、と思い始めていると、その笑顔が少しずつ真剣で沈痛な表情に変わる。"




show shizu basic_normal
with charachange



ssh "あなたの言うとおりだわ"


show shizu behind_blank
with charachange


ssh "昨日ね、"

show shizu adjust_happy
with charachange





"静音の言葉に俺は狼狽を隠し切れなくて、それを認めた静音の顔に抜け目のなさそうな笑みがかすかに浮かぶのに気づく。"
"いくらそうするまいと努力していても、静音は周りの人を驚かせることに、最後の最後まで満足感を覚えずにいられないんだ。"








"それでも、その笑顔がすぐに消えるのを見ると、静音がより大きな心配事を抱えているのがわかる。"




show shizu basic_angry
with charachange



ssh "……二人が私に気がつく前に、あなたが何か言っているのを見たわ。私だってバカじゃない"



show shizu behind_frown
with charachange




ssh "もし見てなかったとしても、戻ってる間にミーシャを見ていればお見通しよ。後でミーシャが私に話さなかったとしてもね。あの子は大したことじゃないように振る舞ってたけど、どう見たって私のせいよ。違う？"







his "ミーシャはなんて言ってたんだ？"




show shizu adjust_frown
with charachange



"その問いを覚悟していたのは明らかだったけど、それでも静音はたじろぐ。そして、とてももったいぶった手振りで返事をする。"




show shizu basic_normal2
with charachange


ssh "沢山"


show shizu adjust_frown
with charachange



ssh "例えば、私はわがままでわかりにくいことがある、とか。周りの人をかき集めるのに躍起になりすぎて、その後で遠ざけてしまうって"




show shizu basic_normal2
with charachange



ssh "どうすればいいのかわからなかった。ミーシャの言ったことはみんな正しいと思ったから、その通りだって返事したの。でも余計にひどいことになっちゃった"




show shizu behind_sad
with charachange



ssh "どうしてなのかわからない"






"眼鏡を直す静音は、本当に疲れているように見える。ミーシャをずっと避け続けていたことがその原因だとは思いたくないけど、この会話の流れを予想すると、可能性を考えずにはいられない。"




show shizu adjust_smug
with charachange




ssh "その通りなんだもの"
ssh "生徒会がこんなに少人数なのも、私たちがいつも仕事に追われているのも、私のせいだわ。私がそんな態度だったから、たくさんの人を追い払ってしまって、生徒会からも人がいなくなったのかもしれない"







"静音はおどけるように指を振り、『かもしれない』というのは控えめな言い方だと暗に示す。でもその疲れ切ったしぐさを見ると、その冗談は俺を安心させるために言ったもので、本音ではないのは明らかだ。"




show shizu basic_normal
with charachange



ssh "例えば、リリーとか。他のみんなが全員生徒会を辞めてからまた人を募集し始めたとき、リリーは一番最初に参加してくれたの。他の人は私に耐えられなかったんでしょうね"




show shizu adjust_happy
with charachange



ssh "みんなでどうにか去年の文化祭を開催することができて、最後にはいっしょに模擬店もやったの"




show shizu behind_frown
with charachange



ssh "でも私はリリーが嫌いだった。いつも自分の友達とのつきあいを優先して私たちを待たせて、学校全体に関わる仕事を私とミーシャだけに押しつける、わがままな人だと思ってた"




show shizu cross_angry
with charachange



ssh "リリーは何か困ったことにぶつかると、パニックを起こして、私たちのことはほったらかしにして、問題が解決するまでこっちに戻ってこないの"




show shizu adjust_angry
with charachange



ssh "自分の問題に１００パーセント集中してしまって、生徒会の仕事がまるっきり手つかずになるのよ！"




show shizu behind_frustrated
with charachange




ssh "私にとってはそれが最悪だった。あんなに愛想がいいのに、いろんな人が助けてくれるのを当然だと思ってることが。だったらどうして生徒会に参加したりするの？　すごく短絡的でわがままだと思わない？"





show shizu basic_normal2
with charachange



ssh "でも実際には、私自身がそういう人間だったのよ"




show shizu adjust_frown
with charachange



ssh "ミーシャが言っていた通りよ。いつも人を自分の近くに引き込もうとして、その後で追い払ってしまう"




show shizu behind_sad
with charachange




ssh "ミーシャにもそういう態度をとって、私はだめな友達だわ。あなたにもそういう接し方をした気がする。だからだめな彼女でもあるんでしょうね。ミーシャはあなたが自分の代わりになればいいって言っていたけど"





show shizu basic_normal2
with charachange



ssh "自分に腹が立つわ、こんなにめちゃくちゃになるくらい取り返しのつかないことをしてしまって。私はただ……"




stop music fadeout 3.0



"静音はふさわしい言葉を探すために静止し、指を重ねて集中する。"




show shizu behind_blank
with charachange



ssh "みんなを幸せにしたかっただけなのに"





show shizu adjust_happy
with charachange



ssh "なんだかこういうと単純に聞こえるけどね"




"頭を手の上に乗せると、静音の前髪がそっと両目にかかる。きれいに磨かれた眼鏡が、ごくかすかな光を反射している。"







"こんなことを考えるのは場違いかもしれないけど、静音は今、とても美しかった。より完璧な人のように。"






"静音からあふれ出る感情に応える初めてのチャンスのような気がする。ミーシャの代わりに静音の通訳になるだって？　ミーシャは冗談を言っているに違いない。"






"今の静音の手話は見たこともない手振りばかりで、それについていくのに俺はもう気力を使い果たしてしまっていた。"






"たぶん、それはミーシャからうつった習慣なんだろう。何年も一緒にいるうちにそれが発達していったんだ。こんなに静音に近しい人の代わりになることなんて、俺には絶対にできない。"






his "俺はお前が好きになったから好きなんだよ。お前にだまされてそうなったわけじゃない"







"相当だまそうと努力はしてたけどな。俺はそのまま、今までにないくらい真剣に静音の目を見つめ返す。"
"初めてその目を見たときは、ちょっと威嚇されているように見えた。捕食者の目のようだった。それは今でも変わっていなくて、安心する。"





show shizu basic_normal
with charachange



ssh "それでも、私はみんなを幸せにしたいの"





his "まずはミーシャからかな？"

play music music_shizune fadein 6.0

show shizu basic_frown
with charachange




"静音が他の誰かを優先する可能性をほのめかした俺に少しいらついたみたいだけど、静音は自信に満ちた笑顔を見せる。まるで親友の悲しみは実在する敵で、たやすく組み伏せて降参させられる相手だと言わんばかりだ。"







show shizu behind_frustrated
with charachange



ssh "もちろん、当然、当たり前よ"





show shizu adjust_noglasses
with charachange



"静音は眼鏡を外しながら、椅子に寄りかかり、ため息をつく。眼鏡を外した姿は初めて見るけど、じっくり見られる前にまたかけてしまう。"




show shizu behind_smile
with charachange



ssh "でも、今日はもう疲れちゃった。明日一番に始めるわ"




show shizu basic_normal
with charachange



ssh "手伝ってくれる？"





his "もちろん"


show shizu adjust_happy
with charachange


ssh "それと……その間に手伝ってほしい生徒会の仕事もあるんだけど"




"実際には、それほど大した仕事があるわけじゃなかった。"




stop music fadeout 2.0
$ suppress_window_after_timeskip = True

scene black
with dissolve





label jp_S31:

window hide None

scene black
with dissolve

with Pause(2.0)

play sound sfx_doorknock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show

play sound sfx_doorknock



"今日は学校がないので遅くまで寝られると期待していた。でも誰かが情け容赦なくドアを叩く音で、朝の８時に起こされてしまう。"




"最初は健二かと思ったけど、俺の不快感をあらわにした怒鳴り声に反応がないことから、それが静音だと気づく。"


play sound sfx_dooropen

scene bg school_dormhallway
show shizu adjust_happy_close at center
with locationchange

play music music_another fadein 0.5

show shizu behind_blank at center
with charadistant



"ドアを開けた瞬間静音は後ずさり、背中に何かを隠す。なんだか不吉だ。"




his "何だよそれ？　ドッキリか？　俺ドッキリは好きじゃないんだけど"


show shizu behind_frown
with charachange



"静音の不機嫌そうな表情が、つまらないけちをつけるなと言っている。でも背中に隠しているものをごそごそするのに手一杯で、手話で伝えることができない。"


show shizu adjust_smug
with charachange



"きっともどかしかったんだろう。その数秒後には隠していたものを誇らしげに、そしてちょっと危なっかしく放り出す。"


show shizu basic_happy
with charachange




ssh "じゃーん！　ピクニックバスケットよ。みんなで一緒にお昼を食べましょう、三人で"





"バスケットというよりはビニール袋に見える。ちらりと中身をのぞくと、ほとんどの食べ物は作ったものじゃなくて、店で買ったものみたいだ。まだ値札がついたままのものもある。"





"それでも品揃えはとても幅広い。小さなキャビアの缶まで入っている。だんだん俺はこの昼食のすごさに気づき始める。その中からブドウを取り出して口の中に放りこむ。"


show shizu adjust_frown
with charachange



ssh "つまみ食いしないで！　この最終兵器を仕上げるのに一晩中かかったんだから"


show shizu adjust_frown:
    ease 0.5 ypos 1.2
    ease 0.5 center
with Pause(0.5)

play sound sfx_pillow

show shizu basic_normal:
    ypos 1.2
    ease 0.5 center
with charachange



"静音は両手を空けるために袋を地面に置くと、すぐにサッカーボールのように気楽に足でつつき始める。どう考えても『最終兵器』と呼ぶようなものにすることじゃない。"


show shizu adjust_happy at center
with charachange



ssh "これも『ミーシャをこれ以上落ち込ませない』計画の一つよ。昨日徹夜して計画を練ったの"


show shizu behind_smile
with charachange




ssh "前に出前を取ろうとしたとき、ミーシャはほとんどなにも注文しないで、それを言い訳に早退したの。でも今度はそう簡単には逃がさない。食事はもう用意してあるし。これなら私たちと一緒に食べるしかないわ"



show shizu basic_happy
with charachange




ssh "完璧なエサよ。どれもすごくおいしそうだと思わない？　自分で料理しようとしたんだけど、おいしく見えるように作る方法なんて分からないから、結局全部買ってきちゃった。でも美味しそうでしょ？　当然よね"






"今日の静音ははつらつとしていて、ミーシャを元気づけようという思いであふれている。でもこんなに元気な姿を見ると違和感を覚える。昨日と同じくらい不安な気持ちでいるのを俺は知っている。"





"ただ一つ変わったところは、これを毎度のような自分自身への挑戦と受け取ることで、不安を棚上げして無謀なくらいに全力を尽くせる、ということだ。"




"今のところそれは静音にとってうまくいっている。これ以外の生き方を知らなかったとしても驚きじゃない。"



his "でも、まだ早すぎるんじゃないか……"

show shizu adjust_frown
with charachange


ssh "もう朝の８時よ、遅すぎるわ！　ミーシャだって８時か９時にはもう起きてる。あの子は夜の７時には寝ちゃうけど、それは重要じゃないし"





his "それすごく重要だと思うぞ"


show shizu basic_normal_close
with characlose



"静音は俺を無視して、ちゃんと反論をする代わりに強引に俺の手を取る。俺が期待していたよりも少しだけ長い間、静音がそばにいてくれたことにとても気分が安らぐ。"


show shizu adjust_happy_close
with charachange



ssh "大事なのは、ミーシャはもう起きていて、その辺をぶらぶらしてるってことよ。探しに行きましょう"


scene bg school_courtyard at bgleft
with locationskip



"静音はしびれを切らしたようにドアから飛び出す。意気揚々と俺を引きずり回しながらミーシャを探している様子に、共通の友達を捜しているというよりサファリでハンターについて行っているような気分になる。"





"探し出すのにそれほど苦労はしなかった。ショートになってもあのピンクの髪は人目につきやすい。しかも校庭をふらふらと歩いていたので、なおさら見つけるのは簡単だった。今度は俺がサファリハンターみたいだ。"



show shizu adjust_happy_close at tworight
with charaenter


shi "……！"


hi "ミーシャ！"

show mishashort hips_smile at twoleft behind shizu
with charaenter


mi "ん～？"




hi "探してたんだぞ"


show shizu behind_smile_close
with charachange



ssh "今日は絶好のピクニック日和よ。一緒に行きましょう。キャビアも用意したのよ。もちろんチョウザメのじゃないけど、おいしいわよ"


show mishashort perky_confused
with charachange



mi "キャビア？　チョウザメ？"




"長い説明を片手でするのはわずらわしいと気づいたのか、静音はすぐにあきらめる。"


show shizu adjust_frown_close
with charachange


ssh "魚の卵"

show mishashort sign_confused
with charachange


mi "え？"

show shizu behind_smile_close
with charachange



ssh "おいしいのよ"


show mishashort cross_smile
with charachange


mi "ごめんね、しっちゃん、今日はやめておくよ"

show shizu basic_angry_close
with charachange



"ミーシャが歩き去ろうとしたとき、静音がビニール袋を俺の方に差し出す。両手を空けるためには俺がそれを受け取らないといけなかった。"


hide shizu
with None

show shizu basic_angry_close at tworight behind mishashort
with None

show mishashort cross_smile:
    ease 1.0 center
show bg school_courtyard:
    ease 1.0 center
show shizu basic_angry_close:
    ease 1.0 xpos 0.75
with Pause(0.5)
show shizu behind_blank:
    tworight
    xpos 0.725
    ease 0.5 xpos 0.75
with charadistant

show mishashort perky_confused at Position(xpos=0.35)
show shizu behind_blank at Position(xpos=0.65)
show bg school_courtyard at Position(xpos=0.43)
with dissolvecharamove




"袋が手を離れた瞬間、静音はミーシャの目の前に駆け寄って行く手をさえぎる。"



show shizu adjust_happy
with charachange



ssh "でも、たくさん用意しちゃったの"


show mishashort perky_sad
with charachange


mi "ごめんね、でも今そんなにお腹すいてないんだ"

show shizu behind_blank
with charachange


shi "……"

show shizu behind_frown
with charachange


ssh "じゃあ、いつになったらお腹減るの？"

show mishashort hips_frown
with charachange



mi "しっちゃん、そんなのわからないよ～"



show shizu adjust_frown
with charachange



ssh "見当くらいつけられるでしょう"





"二人の間の緊張が静音を激怒させる。正面から突っ込んで状況を解決しようとしているけど、そんなやりかたでうまくいくわけがない。"





"ミーシャはもう立ち直っていると思っていた。そしてそう願っていた。でもミーシャが負った痛手は深すぎたのだろう。"




"だとすれば、もう誰の手にも負えない。静音もある程度は分かっていると思う。そうでなければ、疑いを抱いたりするはずがない。"




"ただ、静音が声を出せないからこそ、そのためらいに気づくことができるようになった。とてもよく分かる。叫んでいるのも同然だ。"


show mishashort sign_smile
with charachange

hide mishashort
with charaexit

stop music fadeout 5.0



"これ以上話を続けまいとミーシャは静音の目の前で手を振って、そそくさと立ち去る。逃がしたくはないのに引き留めるすべがなく、静音は無言で怒りをつのらせる。"





"ミーシャの背中が小さくなるのを見て、どこに向かっているのだろうと思う。静音も失意に唇を噛みながら同じことを考えているのだろうか？"





"安心させるため肩に手を置きたかったけど、そうすることが正しいのかどうか分からなくて、やめる。"





"静音が脆く、弱く、悲しそうに見えたからじゃない。逆だ。しばらくした後、その顔から表情か消える。そこにあるのは思考だけだ。突然、静音がくるりとこちらを向く。"



play music music_dreamy fadein 4.0

show shizu basic_angry at center
show bg school_courtyard at right
with dissolvecharamove



ssh "これで用意した食べ物、全部無駄になっちゃったわね"



his "そうだな"


show shizu behind_sad
with charachange



ssh "ほんとに腹が立つわ"




"でも静音が怒っているより傷ついていることは簡単に分かった。俺の手にぶら下がっている袋が、まるで鉛が詰まっているように感じる。"



show shizu behind_blank
with charachange


$ doublespeak(ssh, his, "デートしましょう", "じゃあ役に立てようぜ")


show shizu adjust_blush
with charachange


shi "……"

show shizu basic_normal
with charachange


ssh "どこに行きたい？"



his "さあ"


show shizu behind_blank
with charachange


ssh "屋上"

show shizu adjust_happy
with charachange



ssh "私の好きな場所なの"





"苦笑いが静音の顔に浮かび、すぐに消える。"



play ambient sfx_rooftop fadein 1.0

scene bg school_roof
show shizu behind_frown_close at center
with shorttimeskip




"屋上に着くと、俺はすぐにキャビアの缶を開ける。静音の責めるような視線は気にも留めない。でもすぐに下に置くはめになる。"








his "三角トーストはないの？"




show shizu basic_normal2_close
with charachange



ssh "作らなかったわ。言ったでしょ、全部買ったものだって"



his "でもトーストはないんだな……"

show shizu adjust_frown_close
with charachange



ssh "何がそんなに大事なの？　とにかく、トーストだけなんてお店じゃ売ってないわよ。そんなのバカみたいじゃない"





his "絶対売ってるって"


show shizu behind_blank_close
with charachange


ssh "怠け者専用のお店なら売ってるかもしれないけど、ここでは売ってないわ。トルティーヤチップスでも使えば？"


his "トルティーヤチップスは同じじゃないよ"

show shizu basic_frown_close
with charachange



ssh "両方とも三角形でしょ。お姫様みたいなこと言うのはやめなさいよ。キャビアに正しい食べ方があるなんて知らなかったし、今初めて聞いたわ"



his "全然同じじゃないぞ"

show shizu adjust_smug_close
with charachange



"こんな不毛なことはいけない。大体、知らないなんておかしいだろう？　あんなに大きなお屋敷に住んでいるのに。そんなことを考えているすきに、静音が缶の中身の半分もすくいとってしまう。"



his "おい！"



"そんなふうに食べたら絶対おいしくないぞ。"


show shizu behind_smile_close
with charachange


shi "……"




"二人で食べるには量が多すぎる。食べている間はお互い会話ができないおかげで、俺たちはこれだけ手間をかけた計画の目的だったミーシャがここにいないという事実を無言で噛み締めるはめになる。"




show shizu basic_angry_close
with charachange



ssh "あの子がここに居ないのがしゃくだわ。これじゃ食事も満足に楽しめない"




"俺は静音の横にある、半分だけジュースが入った紙コップを見つめる。"




his "ここにある食べ物、無駄にしたくないんじゃなかったのか？"


show shizu adjust_frown_close
with charachange



ssh "ミーシャにもここにいて欲しかったのよ。それがそもそもの目的だったんだから。やりたかったことができなかった、だからおいしくないの"


show shizu behind_blank_close
with charachange



ssh "あなたが食べなさいよ。もっと食べて"




his "でも俺は揚げ物が欲しいんだ。おいしくないって言ってるけど、お前が全部食べてるんじゃないか"


show shizu basic_normal_close
with charachange



ssh "揚げ物はいつだっておいしいの。何にでも例外はあるわ"



his "太るぞ"



his "お前は強引すぎると思うんだけど"



show shizu behind_blank_close
with charachange



ssh "昨日言った通りよ、私はあの子を元気づけたいだけ"




his "そうなんだけど、軍事作戦でも計画しているみたいに見えるんだよ"


show shizu basic_normal2_close
with charachange


ssh "真剣にやろうとしてるだけよ"

show shizu behind_sad_close
with charachange



ssh "……それに、真剣にやる方法はこれしか知らないのよ"


show shizu basic_normal2_close
with charachange



ssh "自分が本当に無力だって思うわ。嫌になっちゃう。あの子に向かって怒鳴りたくても、怒鳴ることもできない。怒鳴るっていうのは真剣な場面ですることなんでしょう？"






his "そうだな"


show shizu adjust_frown_close
with charachange




ssh "私のかわりにあなたがミーシャに怒鳴るべきよ。ミーシャに落ち込むのをやめてほしいと私が言ってる、って。いくら悲しくて寂しい思いをしてるからって、いつまでも落ち込んでいる理由にはならないわ"





his "なんでお前から言わないんだ？"


show shizu basic_frown_close
with charachange



ssh "もう言ったわよ"


show shizu behind_blank_close
with charachange



ssh "サイコロでゲームをしながらね"


show shizu basic_happy_close
with charachange



ssh "正確に言うと、丁半ゲームで。勝ったのよ！　それも五回も！"






"運任せのゲームで勝つことにここまで得意になれるのはこの二人だけだろう。"



show shizu adjust_frown_close
with charachange




ssh "その後で話そうとしたんだけど、やっぱりダメだったわ、当たり前だけど"




his "まぁ、俺もだけど。やってみてダメだったよ"



show shizu basic_normal2_close
with charachange



ssh "いつだって私の目標はなんでもうまくやる、のはずなんだけどね"




his "そうだな、そうやって人に先んじようとする姿勢は本当にすごいよ"


show shizu behind_frustrated_close
with charachange


ssh "それでも失敗したわ……"

show shizu basic_normal2_close
with charachange


ssh "だからあなたの助けが欲しいの"

show shizu behind_sad_close
with charachange



ssh "もうこれ以上どうすればいいのか分からないわ"




"静音のように、あらゆる障害と正面からぶつかることでしか世界に関わってこなかった人には、それ以上の理解をすることはできないんだろう。"


$ renpy.music.set_volume(0.5, 2.0, channel="music")
$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

window hide

scene bg misc_sky at Fullpan(30.0)
with locationchange

nvl clear
nvl show dissolve



n "\n\n何も悩むことなんてないと言ってやりたい。お前は人を励ますのがとてもうまいんだ、だって俺がここに来た最初の週に、俺を励ますことができたじゃないか、と。"




n "振り返ってみると、ここに来たばかりの俺はいやな奴に見えたに違いない。転校早々、あんなにひねくれた態度でいたのだから。それが理不尽だったとは思わないけど。"




n "それを受け入れる時間が何ヶ月もあったとはいえ、俺のような形で心臓病があると知らされるのはつらいことだ。その上、突然山久に転校させられることについては、考える時間はずっと少なかった。"





n "\n\n文化祭を静音と過ごしたおかげで、マンネリな気分から抜け出すことができた。その間ずっと、静音に操られているような気がしていたことを忘れるくらい、楽しかった。あの時の俺は静音に操られてもいいと思っていたんだ、と今になって理解する。"



nvl clear



n "\n\n世界のどん底にいたような気分だったけど、今でも俺は普通の生活を取り戻したいと思っている。それは確かだ。俺は今の生活を楽しんでいるから。それは誰しも同じに違いない。ミーシャも含めて。みんな自分を苦しみの中から引き上げてくる人が欲しいんだ。"




n "ミーシャはずっと静音に引き上げてくれる人になって欲しいと思っていただけだ。でも二人はいつまでも一緒にはいられないから、静音の手を受け入れられないのだろう。そしてそれが静音をいらつかせる。でも俺みたいなよそ者を励ますことができたのだから、静音は全力でミーシャを励まそうとするだろう。"





n "\n静音の目を見ればわかる。落ち込んだミーシャを励ますのに、他の問題と同じようなやり方で臨もうとしているけど、今度ばかりはそうはいかない。静音の思考過程は全然違う。ある意味ではより慎重、ある意味ではもっと向こう見ずで熱狂的だ。そのくらいには気を使っているんだ。"





nvl clear



n "\n\n\n\n\n結局、俺は何も言わない。こうやって二人きりで隣に座っているのが心地よくて、質問でこのひとときを壊したくない、というのもあった。"





n "\n\n怖かったからでもある。実際はそうじゃないと思うけど、あの日の静音の行動は全て思いつき、まぐれ、もしくは偶然の連続だったのかもしれない。そうだったとしても何も変わらないけど、そう考えると居心地が悪くなる。"



$ renpy.music.set_volume(1.0, 2.0, channel="music")
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

nvl hide dissolve
nvl clear

scene bg school_roof
with locationchange

window show

stop music fadeout 5.0



"後ろのフェンスがわずかにきしむ。横を向いて、静音がフェンスに寄りかかったまま眠ってしまったからだと気づく。一晩中起きていたのを思えば、驚くことじゃない。"




"これだけのモチベーションはどこから来るのだろう？　ミーシャのことだけじゃない。俺はひねくれているので、そこまで人が強くなれる、というのは簡単には受け入れられない。"




"最初に思ったのは、静音は自分のことが嫌いだからかもしれない、ということだ。大いにあり得ることだ。"




"静音に寄りかかりながら、本当にそうなのかも、と思って悲しい気持ちになる。でももしかしたら、より良い人間になりたいと願っているという意味では、俺たちは似たもの同士なのかもしれない。"


stop ambient fadeout 2.0

scene black
with dissolve

$ suppress_window_after_timeskip = True



label jp_S32:

window hide None

scene black
with dissolve

scene bg school_dormhisao
with openeye

window show

play music music_daily fadein 8.0




"どうやら昨日は食べ過ぎてしまったみたいで、朝起きると気持ちが悪くてどうにも耐えがたい。"






"でも町へ買い物に行くのを先延ばしにはできない。また横になって気分が良くなるまで寝たい気持ちを抑えて、無理矢理体を起こして服を着る。"


scene bg suburb_roadcenter
with locationskip



"歯磨き粉と、他にいくつかの雑貨を買って歩いているうちに、気分は良くなっていた。すると腹が減ってくる。途中で朝食を食べた後、かなりの時間が過ぎていることに気がつく。"




"こんなに長い時間出かけているはずじゃなかった。部屋のドアの鍵を閉めたかどうかも分からない。そろそろ戻ったほうがいいな。"


scene bg school_dormhallway
show hideaki bored at center
with locationskip




"寮に帰ってくると、玄関から秀明がドアの前に立っているのが見える。俺が考えられるかぎり、これ以上予想外なことはあまりない。あまりの驚きで自分の心臓が止まるかと思わずにはいられなかった。"
"幸い、そうはならなかったけど。"



show hideaki normal
with charachange



"俺を見つけるとすぐ、秀明はいつも通りの気のなさそうな挨拶をしてくる。俺が返事をするのがやや遅れたので、また間髪入れずに同じ挨拶を繰り返す。"


show hideaki triangle
with charachange



hh "こんちは"


show hideaki normal
with charachange


hh "どうかしたの？"



hi "お前がここにいるのに驚いたんだ"




"秀明を他の誰かと間違えるなんてありえないから、それほど驚いたわけでもない。あの変な服装はどこにいても分かる。考えてみると、最近は本当に妙な格好の人に囲まれているな。"


show hideaki confused
with charachange




"秀明の頭があまりにあっけなく、かくんと片側に傾く。"






hh "どうして？　家族の人が生徒に会いに来るのは珍しいことなの？"




hi "まぁ……そうだな、実際には"


show hideaki surprise_up
with charachange

show hideaki bored
with charachange




"どうやら、秀明もそこまでロボットじみた奴じゃないみたいだ。それどころか、自分が不意をつかれたという事実に不意をつかれたみたいだった。でもすぐに気を取り直す。"






"どちらにしても、その瞬間だけ、秀明は年相応に見えた。その不安そうな一面が彼の素直な本性に見えて、もっと動揺させてやりたくなる。"







"と思ったけど、やっぱりやめる。そこまで熱心になれるのは静音ぐらいだろう。こんなに思考が脱線してしまうのは、静音に影響されている証拠だ。"






hi "なにか理由があるんだろうって、そう思っただけだよ"


show hideaki triangle
with charachange



hh "理由ならあるよ"




hi "ほらな？　とにかく、話でもしながら静音を探そうぜ。そのためにここに来たんだろ？"


show hideaki normal_up
with charachange



hh "姉さんは生徒会室にいる。僕が探してたのは久夫さんだよ。もうすぐ旅行に行くかもしれないんだ、家族旅行。姉さんもいっしょに来たいと思うかな？"





hi "さあ、分からないな。あいつは最近、色んなことで忙しそうだからさ。一度集中し始めると、そう簡単にやめないし……お前なら分かってるだろうけど"



show hideaki closed_up
with charachange



hh "うん"


scene bg school_courtyard
with locationskip



"校内を歩く秀明は、ここに来て間もない頃の俺自身よりもずっと落ち着いて見える。"





hi "ここに来るのは初めてじゃないんだな？"








"なんとなく質問を投げかける。もちろん、周りの環境を完全に無視するというのは羽加道家の血筋なのかもしれない。秀明が静音とこんなに違うことの説明にはなる。単に耳が聞こえないからというだけではないだろう。"




show hideaki bored at center
with charaenter




hh "そうだけど、こんなに歩き回れたのはこれが初めてだよ。ここはなんだか変なところだね。さっきぶつかった人に女性はこの寮に入れないって言われたよ"




show hideaki disapproves
with charachange



hh "僕は女じゃないって言ったら、紛らわしいって言われた。それと僕が暗殺者だっていちゃもんつけられたよ"


show hideaki normal
with charachange



hh "自分は無敵で、それどころかパンチ一発で建物を壊せるぐらい、少なくとも廊下にかかってる絵を倒せるぐらい強いってその人に脅されたよ。ちなみに、絵は壁にネジで止めてあったけどね"





hi "ああ、そいつは廊下の向かいのやつだ。あいつは大丈夫だよ"



show hideaki triangle
with charachange




hh "そうなんだ。あ、ドアの鍵がかかってなかったよ。僕が来たときには開いてた"






"秀明がそれを知っていたことに少しイラッとする。知っていたということは、実際にドアを開けたってことだ。でもその気持ちはすぐに収まる。"



hi "関係ないさ"


hi "隠すものも、盗むものもないし"

show hideaki happy_up
with charachange



hh "サッカーボールはすごくいいね"




hi "それはどうでもいい方のものだよ"


show hideaki serious
with charachange




hh "もし久夫さんがサッカーしてるんだったら、サッカーボールはすごく大事でしょ"






"そうかもしれない。その考えが、俺を少しだけ笑顔にさせる。"


show bg school_lobby
show hideaki closed_up at center
with locationskip



hh "僕がここに来たのは、父さんが新しい携帯を買ったんで、姉さんにそのことを伝えに来たから。姉さんが電話かけたいときにって。久夫さんにも知っててもらったほうがいいと思ったんだ。姉さんの彼氏なんでしょ？"




hi "ああ……"



hi "……なんで？"

show hideaki bored
with charachange



hh "なにかあったときとか、姉さんが欲しいものがあるときのために"




"そういう意味で言ったわけじゃないけど、話を合わせることにする。"





hi "仮に欲しいものがあっても、静音は電話しないと思うぞ"




show hideaki triangle
with charachange



hh "姉さんはそういう人だね"





hi "まあ、分かってるなら……でも、そんなことのためにわざわざここまで？　メールで伝えることもできたんじゃないか"





show hideaki closed_up
with charachange



hh "父さん、メール嫌いなんだ"




hi "ずいぶん時代遅れだな。今でも仕事を普通の手紙でやっているとか言わないでくれよ"


stop music fadeout 3.0



"沈黙。こんどは俺が気まずくなる番だ。秀明は言葉通りに受け取ってしまったのか、それとも俺が真実を言い当てたのか？"




"それはないか。本当のところは娘に会いたくて連絡を取り合いたい、それだけなんだろう。なんだかんだで二人は家族なんだ。お互い大げんかをしているように見えたとしても。"


scene bg school_council
show jigoro smug at tworight
show shizu basic_normal2 at twoleft
with locationskip

play music music_happiness fadein 2.0



"生徒会室のドアは開いていて、俺と秀明は怒鳴り散らしている最中の治五郎さんに出くわす。俺たちを一瞥するけど、静音に怒鳴るのを中断するまでもないと判断したようだ。さっき抱いた自信が激しく揺らぐ。"


show jigoro angry
with charachange




hx "わしが生徒会にいたときは、部屋はもっと狭かったぞ。それに寒かった。食肉冷凍庫の中で働いてるようだった。お前たちのような甘やかされたガキとは違う"
hx "なんという無駄だ。こんなでかい部屋に座って、油を売っているとは"



show shizu behind_frown
with charachange


shi "……"



hx "お前たち三人だけなのだろう？　こんな大量の机、愚劣なる退廃を無意味に露呈しているとしか見えん。ひどいものだ。必要な数の机だけ使え、それ以上はいらん。それがわしのやり方だ"




"こう考えるのはおかしいのかもしれないけど……会話の一方だけを聞いているというのは実に奇妙だ。あと、そのやり方ってのも大概だな。"




"俺が来たことで、治五郎さんは話題を変え、ここに来た理由を話し始める。"


show jigoro neutral
with charachange



hx "秀明と私とで旅行に出かけるのだ"


show shizu basic_normal2
with charachange


shi "……"

show jigoro angry
with charachange



hx "何をしている？　手話を使うやつはみんなブツブツ言いながら手を動かすのか？"





hi "違いますけど、俺はただのアマチュアなんで。考えやすくなるんです。癖みたいなものです"








hx "ただのアマチュアだと……信じられん……まあいい"






"静音がちょうど頭を横に振っているのが目に入るタイミングで、治五郎さんが振り向く。"


show jigoro neutral
with charachange



hx "本当に一緒に来ないのか？"


show shizu adjust_frown
with charachange



"静音はその仕草を繰り返す。"


show jigoro angry
with charachange



hx "そうか"


show jigoro neutral
with charachange



hx "もし何か必要なら電話をかけるようにと伝えてくれるか？"



hi "はい"



hi "でも、メールを送るほうがずっと簡単だったんじゃないかと思うんですけど"


show jigoro angry
with charachange



hx "わしは携帯でメールなど読まんのだ。静音が喋らないのなら、秀明にかければいい。もし私に用があるなら、お前がかけるか、もう一人の女子がかけるしかないな……ふむ。やはり三人とも秀明にかけるがいい"


hide jigoro
with charaexit

stop music fadeout 3.0



"かくして、治五郎さんはきびすを返してその場を去り、それに秀明がついて行く。五分しかかからない用事にしては遠出だったな。"




"どちらも感情を表現するのは上手じゃない。静音の場合、上手にできたとしてもそうするかは疑問だ。筋は通るけど、本人はこの現状にあまり不満はなさそうだ。それでも、実は思うところがあるんじゃないだろうか。"


play sound sfx_doorclose
with Pause(1.0)
show shizu basic_normal at center
show bg school_council at bgright
with dissolvecharamove

play music music_normal fadein 3.0



"二人の後ろでドアが閉まって、静音と俺だけが部屋に残されると、静音は無音の部屋に響きわたるような深い息をつく。"


show shizu behind_frown
with charachange




ssh "私を旅行に誘うなんてもうバカみたい。この上なく最悪なタイミングよ、だいいち生徒会選挙の時期とかぶってるし"
ssh "それにまだミーシャを元気づけてもいないし。それを考えれば、他に考えなきゃいけないことがあるってだけでイライラする"





his "そうだけど、今のお前はそういうこと全部にのめり込みすぎてるんじゃないかな"


show shizu adjust_frown
with charachange



"静音は手荒くメガネを直す。"


show shizu behind_frown
with charachange



ssh "全くもって、１００パーセントその通りね。ミーシャを励まそうって決めた瞬間から、他のことはみんな二の次になっちゃったんだと思う"




his "お父さんもいろいろ言ってるけど、本当は心配しているかもしれないぜ"




show shizu basic_normal
with charachange



ssh "わかってる"




his "だったら、いいアイディアかも――"


show shizu adjust_frown
with charachange


ssh "いいえ"



"そしてもう一度、きっぱりと、俺たち両方に向けているかのように繰り返す。"


show shizu cross_angry
with charachange


ssh "いいえ"

show shizu basic_frown
with charachange



ssh "ここまで来たら休むことなんてできないわ。休暇なんて不愉快よ。きっと別の人生に目覚めるみたいになるわ。昨日は私にとっての休暇みたいなものよ。だからこれからは全力で行かなきゃ"


show shizu behind_blank
with charachange



ssh "ごめんなさい、でもこれが私なの"




$ renpy.music.set_volume(0.5, 2.0, channel="music")

window hide
nvl clear
nvl show dissolve




n "\n\n優子さんが静音はある意味で勇気がある、と言っていたのを思い出す。今なら優子さんの言いたかったことが分かるし、それに同意せざるをえない。それは無謀さ、愚かさ、無意味な頑固さと呼べるかもしれないけど、『勇気』と言ってもいいのかもしれない。"





n "だけど、静音の考えには今まで気づかなかった致命的な欠点があることがわかる。"




n "\n自分がどこで間違えて、ミーシャとの関係をこんなにこじらせてしまったのか、静音は俺なんかよりもずっと長い間、根気強く考えていたはずだ。でも静音にありがちなことだけど、そのことを引け目に感じたりせず、すぐに問題を解決しようとする。"




n "これは問題の大きな部分を完全に無視している。つまりミーシャ本人だ。自己批判から離れて、ミーシャを目標の一部とすることで、当の本人が混乱の中に紛れてしまう。ここ数日、静音は色々なことを『言って』きたけど、ミーシャの気持ちについては何も触れなかった。"


nvl clear





n "\n\n静音のようなものの考え方は普通じゃない。たいていの普通の人なら、友達を拒絶したあとで、あっさり元の関係に戻れるなんて考えたりしない。でも静音はそう考えている。なぜなら静音は人生というのは、あえて簡単に言うと、切り分けて区分できるものと見ているからだ。"







n "ミーシャは他の普通の人々と同じように、人生を一つの体験として見ている。一度のつらい瞬間が永遠について回る、長くて果てのない旅路だ。"




n "静音にとって、出来事は出来事でしかなく、重なり合うものはほとんどない。人生は成功と失敗と決断に分けられていて、それぞれが一つの物語として独立している。だから旅行に行くという考えが邪魔に思えてくる。だから、その時々の他人の感情だけしか理解することができない。"




n "それはまさに、刹那に生きることに固執している人の考えることだ。"




n "同じように、静音はミーシャのことを友達して見ることはできても、それ以上のものと考えたことはつい最近までなかったんじゃないか。あるいはミーシャ自身のことを疑問に思ったことも。もしミーシャにとって信じられないぐらい息苦しくても、静音にとっては『ミーシャはミーシャ』というだけで十分なんだ。"


nvl clear




n "\n静音は自分自身にとっても静音でしかない。おそらく静音は、他人の人生を引っかき回している限り、自分の行動の長期的な影響なんて考えもしていない。でもミーシャにとってそれは英雄的に見えたのだろう。優子さんや俺が静音の勇敢さに感心したように。"






n "そしてそんな感情に対して、静音は他人の人生に触れられて良かったと考える。でもそこでおしまいだ。引きつけるのは簡単だけど、育てるのは難しい。そしてまた次へ。人生をほぼ完全に孤立した出来事の単位で考えていると、その人自身まで切り離してしまいかねない。"







n "静音は今それを直そうとはしているけど、問題は残る。静音にとってミーシャを傷つけてしまうことは避けようがなかった。ミーシャからの思いは静音には応じられないものだったから、応じなかったんだ。静音の性格も相まって、それは必然だった。"





n "知り合ってから数ヶ月、二人から断片的な話をいろいろと聞いて、大体のことはわかった。"




n "\n二人の違いについて考えている途中で、ある考えが頭の中で浮かび始める。"


$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl hide dissolve
nvl clear
window show



his "今、お前の計画のこと考えているのか？　この瞬間も？"







his "ミーシャを元気づけよう計画"




show shizu basic_happy
with charachange



ssh "もちろんよ。怒鳴られている間ずっと考えていたわ"


show shizu adjust_happy
with charachange




"妙に誇らしげな空気をまといながら、メガネを鼻筋に沿って持ち上げて、指でこめかみをコツコツと叩く。"



show shizu behind_smile
with charachange



ssh "マルチタスクよ！"


stop music fadeout 4.0




"本当か？　どちらかと言うと、聞こえないからそういうことに集中できるって話じゃないのか？　まあいい。静音に俺のアイディアをどう思うか聞いてみたら、俺たち二人とも同じようなことを考えていたのだった。"




scene black
with dissolve



label jp_S33:

scene bg school_scienceroom at bgleft
with locationchange

play music music_pearly fadein 5.0



"相手にしているのは人間なわけで、なんとなくイヤな気分になるけど、最初のステップはミーシャを追い詰めることだ。"




"刑事ドラマか何かに似すぎな気がする状況だけど、こうなってしまったのもミーシャに普通に話しかけるのはほとんど不可能だとわかったからだ。"




"でも俺たちは同じ授業を受けている。それも一日の最初の授業に。"


show shizu invis:
    center
    xpos 0.75
show mishashort invis_close:
    center
    xpos 0.15
with None

show shizu behind_blank at tworight
show mishashort perky_confused_close at twoleft
show bg school_scienceroom at center
with dissolvecharamove



"指示が出るまではしばらく時間があったけど、今日はグループで作業をすると聞いた瞬間、俺と静音はミーシャがいっしょのグループになるよう手を尽くす。"





hi "なあ、武藤先生ってやけにたくさんグループ課題と自習教材を出すよな、そう思わないか？"



show mishashort perky_smile_close
with charachange



mi "ん～、でも簡単だから大丈夫だよ、でしょ～？"




hi "そうか？　最近他にも色々考えてることもあるんだ、そっちは大丈夫じゃないかも知れないんだけど"





"ミーシャは一つ一つの言葉が終わるたびにうなずき、そして全部聞き流す。"




show mishashort sign_confused_close
with charachange




mi "わたしもそのことは考えたよ、だけど～……ひっちゃんやしっちゃんと一緒にいると、十分勉強できないんだよ！　だから今日はもっとがんばってみる"
mi "だから～！　邪魔しないでね、ひっちゃん～。集中しなきゃいけないから～"





show shizu behind_frustrated
with charachange



"腹が立つくらいあからさまな避け方だな。ミーシャが今の会話を一切手話にせず、代わりに手でペンを回していたので、静音も不機嫌そうだ。"




"その危なっかしい回し方からして、不用意に手話を使わないようにするためだったに違いない。"




"落ち着きのない、不安そうなミーシャの様子を見ると、悪意があって静音を蚊帳の外に置こうとしているわけではなさそうだ。それでも、静音を自分から遠ざける手段なのは明らかだけど。"




hi "静音がお前と話したいってさ"


show mishashort perky_sad_close
with charachange


mi "……"

show mishashort perky_confused_close
with charachange



mi "あとじゃだめなの、ひっちゃん？"


show shizu basic_angry
with charachange



ssh "だめ"




hi "今じゃだめなのか？"


show mishashort sign_confused_close
with charachange



mi "まだ授業中だし～……"






"今度は両手でペンを回している。ミーシャの手話は神経性の癖か何かに変わってしまったんじゃないか。代わりの動作としては微妙だな。でも両手でのペン回しは結構すごい。"






hi "じゃあ、授業のあとで"


scene bg school_scienceroom at bgleft
with shorttimeskip



"授業の後、一秒たりとも無駄にせずに話を蒸し返す。"


show shizu invis:
    center
    xpos 0.75
show mishashort invis_close:
    center
    xpos 0.15
with None

show shizu behind_frown at tworight
show mishashort perky_sad_close at twoleft
show bg school_scienceroom at center
with dissolvecharamove




"他のみんなが教室を出て、俺たち三人だけが残る中で、ミーシャが正面以外を見つめる時間がますます長くなる。"






hi "なにか食べ物でも買いに行く？"


show mishashort hips_frown_close
with charachange



mi "どうしてひっちゃんもしっちゃんも、いつもわたしが何か食べたいか聞いてくるのかな～？　ねえ、ひっちゃん～？"




hi "みんな食堂に向かってるし、もうずっと三人でいっしょに食事してないからさ。ダメか？"


show mishashort perky_confused_close
with charachange



mi "生徒会のことなのかな？"


show shizu behind_blank
with charachange



shi "……"


show mishashort perky_sad_close
with charachange



"静音が答えないのを同意と取り、ミーシャはため息をつく。"


show mishashort hips_frown_close
with charachange



mi "しっちゃん、それしか考えることないの？"


stop music fadeout 5.0

hide mishashort
with charaexit



"静音が答えるまえに、ミーシャは立ち去ってしまう。正直に言うと、今の出来事の後では俺も自信が揺らぐ。"


show shizu behind_blank at center
show bg school_scienceroom at bgleft
with charamove



"二人ともうまくいくとは思ってなかったけど、もしそうだったらどんなに良かったか。"


show shizu adjust_frown
with charachange




"俺の考えを察して、静音はしばらくメガネの周りに指を絡めてから手話を始める。"




show shizu basic_angry
with charachange



ssh "あなたの考えてることは分かるけど、でも違うの。ミーシャに一歩譲った方がいいと思ったからじゃないわ。そう簡単には諦めないって言ったでしょ"





his "うん、まあ、実はもう手遅れなんじゃないかと思い始めてる"




show shizu behind_frown
with charachange



ssh "怖じ気づいたの？"


show shizu adjust_frown
with charachange



ssh "言っとくけど、私はそうは思わないわ。それじゃミーシャを諦めるのと同じことよ"




show shizu behind_blank
with charachange




ssh "誰かを助けることとダメにすることの差は紙一重よ。でも私はミーシャにちゃんと立ち直ってほしいし、あんなおかしな態度をとるのをやめてほしいの"





show shizu basic_normal
with charachange




ssh "ミーシャならできるわ。でももしそうしたいと思っても、人は一晩では変わらない。もしそんなことができるなら、世界はもっと楽な場所になってるわ"





his "わかったよ、お前の言うとおりだ"








his "ここは二手に別れてミーシャを探す場面かな"




"でも本当は、俺が一人で見つけなきゃいけないんだけど。"



show shizu adjust_happy
with charachange

play music music_tranquil fadein 3.0



ssh "もし私が最初に見つけたら、携帯に電話するわ"




"笑顔のまま静音は携帯を取り出し、電源を入れる。俺はものすごい数の未読のメールに気がつく。その表情から察するに、静音も気がついたみたいだ。ストラップで携帯をくるくる回しながら、しかめっ面を見せる。"


show shizu behind_frown
with charachange



ssh "私これ使うの嫌いなの"


show shizu basic_angry
with charachange



ssh "なんで指を鳴らすだけじゃだめなのかしら？"




his "そしたらどうするんだ？　俺は犬じゃないぞ。それに電波よりも遠くに飛ばないし"


show shizu behind_smile
with charachange



his "この状況、結構楽しんでないか、お前？"




"首を横に振りながら、静音は続ける。"


show shizu adjust_happy
with charachange



ssh "ミーシャがどこに行くかなんて決まっているわ。学校の敷地内じゃ見つからない。できるだけ遠くに行きたいはずよ"


show shizu behind_blank
with charachange



ssh "喫茶店をチェックする？　こんな早くなら空いてるわ。ミーシャはサボりたい気分のときはあそこに行くのが大好きなの、あとあそこのパフェもね"






"『ほんとにあいつのこと色々知ってるんだな』。でも静音は考えすぎて、実際よりずっと皮肉に取ってしまうだろう。だからただうなずいてその場を去ることにする。静音が俺の袖をつかんでいるのに気がつくまでは。"






show shizu basic_normal_close
with characlose



hi "どうした？"




"静音には聞こえないことも忘れて、無意識に口に出してしまう。"


show shizu behind_smile_close
with charachange



ssh "もう自分一人で何もかもやらなくてもいいって、いい気分ね、だってあなたは信じられるから。本当にうれしい"




"俺もそれを聞いて嬉しくなる。でもどう反応すればいいか分からなくて、結局またうなずいただけだった。"


play ambient sfx_crowd_indoors fadein 2.0

scene bg school_lobby
show mishashort perky_confused:
    center
    xpos 0.6
    ypos 1.05
show crowd
with locationskip



"外に向かうと、他の女子の向こうにわずかにピンクの髪が見える。そっちに向かいながら、それが学校を出るために通る道じゃないことに気がつく。"




"生徒会室へ向かう道だ。俺がもし静音を避けるとしたら、そっちには向かわない。"




"だったらミーシャがそっちの方に行くのはおかしい。もしかしたら静音と話をつけたいのかもしれない。"




"もしそうだったら、成り行きに任すのも悪い考えでないのかもしれない。良い方向に行きそうなら、なおさらだ。"


show mishashort invis as mishafront:
    center
    xpos 0.6
    ypos 1.05
with None

show mishashort invis at center
show mishashort hips_smile as mishafront at center
with Dissolvemove(0.7)

hide mishashort
hide mishafront
with None

show mishashort hips_smile at center
with None



"突然、ミーシャは立ち止まって振り返り、俺は不意を突かれる。"


show mishashort hips_grin
with charachange





mi "ひっちゃ～ん、びっくりした～？　わたしを探してたの？　そんな気がしたんだ～！"







"『よう、お前のこと探してたんだぞ』と言うつもりだったけど、もうその手は使えないな。"



show mishashort hips_grin:
    easeout 0.7 xpos 1.0 alpha 0.0
with Pause(0.7)





"自分の言葉も言い終わらないうちに、ミーシャは俺の横をすり抜けて出口へと走り去る。ミーシャが予想より腹が立つくらいに鋭くなっているのを認めざるをえない。それと、驚くほど素早くなった。"




stop ambient fadeout 2.0

scene bg school_courtyard
with locationskip




"自分で思っている許容範囲を越えて体を動かしてる気がするけど、なんとか校門を出かかっているところでミーシャに追いつく。"






hi "お前今、世界で一番いやな女になってるぞ"




hi "ちょっとでいいから逃げるのをやめてくれないか？　お前と話がしたいんだよ"


show mishashort cross_smile at center
with charaenter



"ミーシャは少し愉快そうな表情できびすを返し、話を続けろと言わんばかりに両手を上げる。彼女の注意を引けたのはいいけど、正しい言葉を考えつくのが難しい。"




hi "これからどこにいくんだ？"


show mishashort sign_smile
with charachange



mi "上海だよ～"




hi "じゃあ、俺も一緒に行っていいか？"


show mishashort perky_confused
with charachange



"ミーシャの返答を待つのが永遠のように感じられる。自分の腕時計が一秒を刻む音まで聞こえてくるようだ。"


show mishashort hips_smile
with charachange



mi "いいよ、ひっちゃん"


stop music fadeout 3.0



"ミーシャが同意したのは、単に今日はもうこれ以上口論したくないからじゃないかという気がする。"


scene bg suburb_shanghaiint
show mishashort perky_smile:
    center
    ypos 1.02
with shorttimeskip

with Pause(0.2)

play sound sfx_storebell
show mishashort perky_confused:
    ease 0.1 ypos 1.0
    ease 0.2 ypos 1.02
with Pause(0.3)



"俺たちが着いたあと、カップルが入ってきて、ミーシャはその音に驚く。"


show mishashort perky_smile_close at Position(ypos=1.1)
with dissolvecharamove




"静音ではないと確認した後、また緊張を解いて、ほぼいつも通りの笑顔で優子さんにパフェを頼み、一番近くの席に滑り込む。"






hi "お前走るの早すぎるよ。せめて静音が何を言うのかわかるまで待ってもよかったんじゃないか"


show mishashort hips_frown_close
with charachange



"ミーシャの怒ったような反応を見ると、静音の言葉を恐れていたのかもしれないと思う。"




mi "どうして二人ともこんなことするの、ひっちゃん？"




hi "静音がまだ友達でいたいと思ってるからさ。多分あいつにとって、これは潜水艦から核ミサイルを発射するようなものなんだ。鍵が二つないといけないっていう"


show mishashort perky_confused_close
with charachange


mi "……"



hi "でも、あいつには他にどうしようもないだろ？"






"ミーシャはもう自分が聞いたり話したりすることを自動的に手話にしない。静音ともめていたのはそのせいだろう。"







hi "あいつがお前に話しかけようとしても、お前は話を聞かないじゃないか"


show mishashort perky_sad_close
with charachange

play music music_night fadein 6.0




"ミーシャの後ろめたそうな表情を見ると、どうやら図星みたいだ。"





hi "本当に静音のことがそんなに嫌いなのか？"


show mishashort sign_confused_close
with charachange



mi "違うよ、ひっちゃん。言ったでしょ"


show mishashort perky_confused_close
with charachange



"スプーンをもてあそびながら、たじろぎもせずに返事をする。"




hi "ああ。分かってる"





hi "あいつも分かってると思うよ。でも本当に嫌ってる方が話が楽な気がするぞ"







hi "静音は先週からずっと、お前を元気づけることだけを考えてる。静音はまだお前を頼りにしてるからだ。でも昨日は、自分を嫌いになってくれる方がお前にとってはいいんじゃないかって言ってた"





hi "お前は静音に嫌いだとは言わなかったから、あいつはまだお前と友達でいられると思ってる。あいつはそういうやつだよ。考え方がいつも極端なんだ"




"ミーシャのパフェは溶け始め、中身が小さな川のように混ざり合う。それを見ていて、低速度撮影で写した成長する木の根の映像を思い出す。"


show mishashort cross_frown_close
with charachange



mi "バカだよ、そんなの。しっちゃんはそんなにバカじゃないよ、ひっちゃん。おかしなこと言わないで～"




hi "頭がいいかどうかは関係ないよ。頭のいい人だってバカなことはやるさ。それに、本当の事だろう？　先週話したときはヒヤヒヤしたけど、最後にはまた元に戻りそうだったから安心したんだ"




hi "その直後に二人でけんかするとは思ってなかったけどな"


show mishashort perky_confused_close
with charachange



mi "けんかなんかじゃないよ、ひっちゃん。ただわたしが怒鳴ってただけだよ"





"ミーシャの声のトーンはほとんど変わらず、声の大きさだけが変わっていることに気づく。やましさのせいでその声はあまりに小さくて、それがミーシャの声とはまるで信じられない。"





hi "どっちにしても、俺はうれしかったんだ。お前とあいつはまだ友達でいられると思ったからさ。あいつにはお前が必要なんだ"


show mishashort sign_confused_close
with charachange



mi "ん～。必要じゃないよ、ひっちゃん"




hi "だからなんだよ？　なんでそんなこと分かるんだ？　静音にはいろいろ……"









"声に出せないことがある？　喋れない、話さないことが？　もし言い方を間違えたら、雰囲気を壊してしまう。やっとミーシャと話ができたのに、ここで台無しにはしたくない。"
"ミーシャと腹を割って話すのはもしかしたらこれが初めてだろうか。"






hi "あいつがお前にそう言わなかったからって、お前のことが嫌いってわけじゃないよ"


show mishashort hips_frown_close
with charachange



mi "わけわかんないよ……"




hi "いや、わかるだろ。そうじゃなきゃ、あいつは反論してくるさ"


show mishashort hips_grin_close
with charachange



mi "わはは～"




hi "そう思わないか？　あいつは誰にでもけんかを売る、ならお前が相手でもそうじゃないかな？　そりゃそうだろ、だってお前は友達で、あいつはお前のことが大事だから。それに静音は傷ついてる"




hi "あいつは自分の気持ちを見せるのが本当に下手なんだ。しかも大体やりかたを間違えてる。それでもまだお前のことが好きなんだよ"


show mishashort perky_confused_close
with charachange




mi "ひっちゃん、わたしがしっちゃんを嫌いたくも、怒らせたくもないって言ったの覚えてる？　本当のこと言うと～、両方ともやっちゃったんだよね"
mi "今じゃなんていうか、その、二人の間に違和感みたいなのがあるんだよね。説明しにくいんだけど"





hi "二人ともほんとに頑固だな。お前は静音と離ればなれになりたくないってずっと言ってたじゃないか、でもこのままそうなるのを黙って見過ごそうとしてる"






hi "それに静音も同罪だ。お前と友達でいたいのに、お前に気を使いすぎてるから、他の人を相手にするときのように積極的にはなれないんだ"






"そして静音の気遣いを、ミーシャは思いやりのなさと解釈するに違いない。"


show mishashort perky_sad_close
with charachange




mi "わたしはもう失敗しちゃったんだよ、ひっちゃん。また同じことになるよ～、絶対。そんなふうに考えちゃうと、わたしどうすればいいのか分からないよ。何をしたって、もっとひどいことになっちゃう気がする"
mi "だったら、何もしない方がいいかも、だよね～？"





hi "おかしなこと言うなよ。そもそもなんでそんな風に考えるんだ？　もっとポジティブになれよ"




"『お前なら簡単だろ』と言いたかったけど、それは出しゃばり過ぎだろう。"


show mishashort hips_smile_close
with charachange



mi "ひっちゃん～、そんなに楽観的だったなんて知らなかったよ。予想もできなかったよ"




hi "……"


show mishashort perky_smile_close
with charachange



mi "わたしがひっちゃんを驚かそうとするときは、いつも暗そうな感じなんだもん"




hi "いや、それは最近のことさ。本当だって。今の俺は、人が簡単に諦めるのがいやなだけさ"


show mishashort cross_grin_close
with charachange



mi "はは～"


show mishashort perky_smile_close
with charachange



mi "『今』、ね～……？"




hi "人が諦めるのを見ると腹が立つんだ。諦めるのはある意味逃げだって考えてた、だってみんなそう表現するから。でも今考えると、それはなにかを捨てることに近いって思うんだ"




hi "なにかから逃げても、それそのものはまだそこにある。だから、俺が病院にいた時、ただ問題から逃げたいと思ったんじゃなくて、二度とそのことを考えたくないって思ったんだ"




"ミーシャがどろどろに溶けて灰色になったアイスクリームをスプーンで口に運ぶ。たった今そこにあるのを思い出したのか、それともそういう状態のほうが好きなんだろうか？"




hi "とにかく、俺が言いたいのは、そんなことはできないってことだ。人は思い出をそうやって捨てるには感情的すぎるよ"




hi "不可能なんだ。静音は人生を勝ち負けでしか考えられない。静音は負けた時の記憶を覚えていたくないと願っている、って思わないか？"






hi "でもそんな選り好みはできないんだ。それは泡の中で生きたいって思うことと同じだよ。最悪なのは、お前の考え方は無駄が多すぎるってことだ。そのせいで悲観的になりすぎて、何もかもが怖くなってるんだ"





stop music fadeout 4.0



hi "行こう"





"俺はミーシャの手を取ると、会計をするために空いている手で優子さんに手を振る。"



show mishashort sign_confused_close
with charachange



mi "こんどはどこへ行くの？"




hi "昼休みが終わる前に学校へ、でもその前に寄っておきたい場所があるんだ"




scene bg school_gate:
    right
    subpixel True
    linear 30 left
with locationskip

play music music_comfort



"せいぜい軽いジョギング程度の運動しかしていないのにもかかわらず疲れを覚え始めていたけど、ミーシャと俺は十分くらいの余裕を残して校門にたどり着く。"




hi "本当の所、この学校には来たくもなかったんだぜ。選択の余地なんてなかった。俺がこの校門に着いたとき、きっと『なんて気が滅入る場所なんだろう』と心の中で考えてたと思う"




hi "でも全然そんな場所には見えないんだ。まあ、それでも俺には何もかも分かってるって思ってたけど。自分がほとんど別人みたいに感じてた"




hi "もしできるなら、過去に戻って自分に言ってやりたいんだ。一瞬で何もかも忘れられるとか、自分の人生は終わったとか、もう二度と楽しい気分にはなれないなんて考えるのはやめろって"



scene bg school_gardens:
    right
    subpixel True
    linear 30 left
with locationskip




"校庭にはまだ結構人が散らばっている。昼休みなので、いつものことだ。"






hi "ここはお前と静音に二度のお祭りを手伝わされた場所だ。とんだ重労働だと思ったよ。『こんな事してる時間なんてない』って"




hi "でも今振り返ると、大した仕事はしてなかった。それに他にすることなんてなかった。多分一人きりで過ごしてただろう"


scene bg school_scienceroom:
    right
    subpixel True
    linear 30 left
with locationskip




"次に俺はミーシャを３－３の教室に連れて行く。中には授業前にサンドイッチを食べようとする武藤先生しかいない。"





hi "お前たちの事を思い出すたび、俺は放っておいて欲しいって思ってた。それはここだったり、さもなければ……"


scene bg school_lobby
with locationskip



"武藤先生を残し、近くの自販機へ向かって、あと五分しか飲む時間がないけどソーダを買う。俺は昼休みの間ずっとミーシャと過ごしていた。この数日間、静音と俺の両方がミーシャと話せた時間よりも長い。"




hi "……食堂まで俺をつけて来る時とか、いろんな授業が終わった後で俺を追い詰めてくるときとか"




hi "実際には四回ぐらいしか話してなかったって、自分では全然気づかなかった。そう思い込んでただけなんだ。今やっと気がついたよ"


show mishashort hips_smile at center
with charaenter



mi "わたしも覚えてるよ、ひっちゃん。でも～、そういうことがあった場所はわたしも全部知ってるよ～"





hi "待った、まずこのツアーを最後まで終えさせてくれ。時間もそろそろなくなってきてるし。それはそうと、ソーダ飲むか？"



scene bg school_staircase2
with locationchange



"階段の方に向かいながら、これ以上ミーシャの手を引かなくてもいいということに安心する。"





hi "階段に来ると目を回す、だよな？"



show mishashort perky_sad_close at twoleft
with charaenter



mi "そうだよ～"




hi "だったら、ここでちょうどいいか"


show mishashort perky_sad_close:
    ease 1.0 ypos 1.2
with Pause(1.0)



"俺は壁に寄りかかり、ミーシャは俺の向かいで階段に腰かける。"




hi "小学校とか、中学校の時に一緒にいた人のことを懐かしいと思ったことはある？"


show mishashort perky_confused_close
with charachange



mi "ううん"




"即答だな。考えるまでもないということだ。俺は反射的にたじろいでしまう。"




hi "俺、前の学校ではもっと友達がいたんだ。でも今はもう話もしない。なんだか自分の前世のときのことみたいに感じる。本当、寂しいよ"




hi "時々、また話したいって思うこともあるけど、無理だとわかってるんだ。怖いとか、恥ずかしいとか、そんな感じで。会いに行くのにも遠すぎるしね。電話しようとも思うけど、番号はほとんど知らないし"




hi "それに別れ方も不本意だった。向こうだって俺に会いたいと思う理由もないよな？"




hi "もう忘れた方がいいって気になるけど、やっぱり今でも考えてしまうし、連絡を取り合うようもっと努力しなかったことを後悔してるんだ"




hi "それで、忘れた方がいいなんて考えが間違っているのかもしれないって思い始めたんだ。それは一緒にいて楽しかった人たちに対する侮辱だし、いろんな楽しかった時間を無駄にすることだ"





hi "前にも言ったけど、悪い時もあるかもしれない、でも振り返ったときに幸せな記憶として思い出せれば大丈夫なんだよ"







hi "でもその時はそんなこと考えもしなかった。だから、ある日目が覚めたら友達がいないことに気づいたような感覚だった。俺は何もしないまま友達を失ったんだ"

hi "最悪だった。お前と静音には同じようなことになってほしくない。それだけなんだ"




show mishashort perky_sad_close
with charachange



mi "『それだけ～』"




hi "お前が俺と同じように友達を遠ざけると思うと悲しくなるんだ。お前は静音に近いからなおさらさ。っていうか、同じ寮に住んでるんだぜ"




mi "友達、ね～……"


show mishashort perky_confused_close
with charachange



mi "あなたも友達じゃないの、ひっちゃん？"




hi "そうだよ"




hi "お前はずっと寝てたけど、あのとき、学園祭の花火はすごくきれいだった"




hi "あんなふうに花火を見たのは初めてだった。それに空を見たのも久しぶりだった。それまで星を見上げた事もなかったしね"




"ただ入院中に星に関する本はざっと読んでいて、知識は結構あったけど。"




"例えば星はただ燃えてるだけじゃなくて、むしろ休みなく爆発が続いている、とか。とても遠くにあるので今見ている星は何千年も前に燃え尽きてたりする、とか。"




"星の光はそれだけ経ってやっと地球に届く。地球と俺たちの太陽の大きさ、それと他の恒星の大きさを比較した写真を見たことがある。その本に載っていた小さな地球の上には日本なんて見えもしなかった。"




hi "今まで気づきもしなかったことがあるんだ、何だと思う？"


show mishashort perky_smile_close
with charachange



"ミーシャは期待に満ちた顔で俺を見る。"




hi "星ってものすごく明るいんだ"


show mishashort hips_grin_close
with charachange



mi "あははは～"




hi "本当さ"


show mishashort perky_confused_close
with charachange



mi "どうしてこんなことするの、ひっちゃん？"




hi "なにを？"


show mishashort cross_frown_close
with charachange



mi "わたしだってバカじゃないんだよ"






hi "さあな。色々さ。お前が静音の友達だから？　２人が仲良しなのがいいから？　みんな短所はあるけど、諦めるのはバカらしいって言いたいのかもな。どっちにしろ、苦労する価値はありそうだし"





show mishashort sign_smile_close
with charachange



mi "理由はそれだけ？"




hi "あと、お前は友達だから"


show mishashort hips_smile_close
with charachange



mi "それだけ？"




hi "理由がなかったら何かしちゃだめなのか？"


show mishashort hips_grin_close
with charachange



mi "わはは～。いいよ、いいよ～、でも知りたいんだよ"




hi "じゃあ、他に何が聞きたい？"


play sound sfx_warningbell
stop music fadeout 3.0



"答える前に予鈴が鳴ったので、ミーシャは笑顔を見せるだけだった。"




scene black
with dissolve




label jp_S34:

scene black
with dissolve



"その後数日、ミーシャの姿を見る機会が減った。でも心配はしていない。目にすることがあるたびに、だんだん昔のミーシャに戻っているように見えたからだ。"




"自分の考えが甘いせいで勘違いをしているんじゃないか、と恐れる必要がないことが十分はっきりすると、俺はまた安心し始める。"


window hide

with Pause(1.0)

scene bg school_dormhisao
with openeye

window show



"朝早くに目が覚めて気持ちが悪い日曜日。それに、昨日の夜は寝るのが早すぎた。カーテンの様子も何かがおかしくて、きちんと閉まらない。"




"おかげで寝直すこともできない。眠ろうとするたびに太陽の光が目に入ってくる。こんなに朝早く目が覚めてしまったのも、たぶんそのせいだろう。"


play sound sfx_doorknock



"これだけの具合の悪さと疲労は不快感を煽る。ドアがノックされた時は思わず喜びそうになる。"


scene bg school_dormhallway
show kenji neutral at center
with locationchange

play music music_kenji fadein 0.5



"ほぼ完食済みのリンゴを手にした、おなじみの人物がそこにいる。最後の一口をかじると、それを部屋の中のゴミ箱めがけて投げ込もうとするけど完全に外れ、二メートル上の壁にぶつかってバラバラに砕け散る。"





"公平のために言うと、破片の大半は一応ゴミ箱の中に落ちた。でもわざわざこんなことをするほど厚かましい人間は絶対にいないと思う。"


show kenji happy
with charachange



ke "ナイスショット！"


show kenji neutral
with charachange



ke "よう、同居人？"




hi "俺はお前の同居人じゃない、同じ部屋に住んでないだろ"


show kenji tsun
with charachange



ke "関係ないさ"




hi "関係ある、最低でも同じ建物に住むのと同じ部屋に住むことの違いぐらいわかれよ"


show kenji neutral
with charachange



ke "部屋を使わせてくれ"




hi "なんのために？"




"失敗した、『絶対にダメだ』と言うべきだった。"


show kenji tsun
with charachange



ke "生徒会がいつまでも手紙を届けるのをやめないんだ、俺がロッカーかどこかに置いといてくれって言ってるのに"





ke "でもあいつらは手紙をドアの下に置いて行って、俺に気づかれないように配達していくんだ。だから今日は、その瞬間をとらえるために待ち伏せをするんだ……探偵とか、ハンターみたいに"




show kenji neutral
with charachange




ke "お前の部屋に居座ってその小さなのぞき穴からのぞいてなくちゃ、現場を押さえられないんだ。あと、多分明日もな"



show kenji happy
with charachange




ke "めちゃくちゃ楽しいぞ。今日も明日も、ピザを注文しようぜ。それとも一日はピザにして、次の日は別のものにするか？　でも何がいい？　それにどっちの日がピザの日だ？"






hi "今日はない。絶対にない。あのな、俺は生徒会に入ってるんだ。なんで俺に聞かなかったんだ？"





"もし聞いていたら俺は簡単に事態に気づいただろうし、健二を部屋に入れることもなかった。ウィン・ウィンの状況だ。健二が俺のおごりでピザを食えなくなる以外は。もしかしたらそれが健二の目的なのかもしれない。"





"でも……いや、それはないな。こいつにはそんな凝った計画は立てられないだろう。"



show kenji tsun
with charachange



ke "知ってるのか？"






hi "いつ手紙を配達に来るか？　いや、知らない。いつもなら、俺の手紙は俺が生徒会へ行くときに手渡してくる"
hi "要するに、俺が聞けば分かるってこと。そしたらお前に教えられる。そうやって人は何かを調べるんだよ、他人に聞いて"





show kenji neutral
with charachange





ke "原始人はそうじゃないってか。ああそうだな、今のにはノーリアクションなんだろ？　はいはいわかったよ"








hi "……自分ののぞき穴使えよ"



show kenji tsun
with charachange



ke "奴らに見られたらどうするんだよ？"




hi "見えないよ、のぞき穴はそういう作りなんだ。マジックミラーみたいな"


show kenji happy
with charachange



ke "本当なのか？　じゃあ……そんなわけあるか。どっちみち、奴らは俺が中にいると予想してるはずだ。俺の気配を察知して俺がいるって分かるはずだ。実は廊下の向かいの部屋にいるとは思いもしないだろうさ"




hi "俺が生徒会室に行ってお前の手紙を取って来てやる、今すぐに"


show kenji tsun
with charachange



ke "だったらお前をここから出すわけにはいかないな"




hi "アホか。俺がトイレに行きたい時はどうするんだ？"


show kenji neutral
with charachange



ke "お前の小細工は俺には効かないぞ"


scene bg school_dormhisao
with locationchange



"俺は机に座り、週末に備えて宿題をやり始める。"




hi "あのな、どうせお前はそのうち出て行くことになるんだから、ここにいつまでも居座ったり、俺を閉じ込めたりはできないんだぞ。というか、元々俺の部屋だし"


show kenji neutral at tworight
with charaenter




ke "ああ、俺もそうは思わない。手紙が届くのはいつぐらいだ？"





hi "今"


show kenji tsun
with charachange



ke "なんで女ってやつはこんなに遅いんだ？"




hi "なんでそんなに手紙が気になるんだ？　何か届くのを待ってるのか？"


show kenji neutral
with charachange



ke "俺はいつも何かを待ってるさ……でも今日は違う"




hi "何かを送って欲しいのか？　そもそも手紙を送る事なんてあるのか？"


show kenji tsun
with charachange



ke "送らねえよ！　奴らはそうやって俺たちを捕捉するんだ。俺は８歳のとき以来郵便なんて使ったことがない。その時はレゴの会社にドラゴンボールのレゴを作ってくれって手紙を送ったんだ"


show kenji happy
with charachange



ke "奴らは版権が取れなかったと言って、割引券をくれたんだ。おおいに価値はあったぜ、でもそれ以来ずっと見つからないようにしてる"


show kenji neutral
with charachange



ke "お前は郵便は使ってないよな？"




hi "先週両親に手紙を書いたよ"


show kenji tsun
with charachange



ke "でも奴らはそれでお前を捕まえるんだぞ！"





hi "ああ、わかっているべきだったな。だからその次の日に、奴らにあのマイクロチップを埋め込まれたのかもしれないな"



show kenji neutral
with charachange



ke "そうか……噂は本当だったのか"





"その噂の出所はいったいどこのどいつだ。"






hi "冗談だ。ジョークだよ"


show kenji tsun
with charachange




ke "ジョーク？　くそっ。お前、ジョークだと？　こういう気持ちになるんだな……冗談を言われるっていうのは。まさか自分にそんな事が起きるなんて思わなかった"
ke "これは重大問題なんだぞ。まったく、俺のジレンマの深さを理解してないだろう"





ke "これはたくさんの手順が必要なんだ。大勢の人が関わる、複雑な手順だ。すげえ難しいんだぞ、分かるか？　これが終わったら俺は魚をまるごと食うんだ、記念に"
ke "ああああ、ちくしょう。俺はピザが欲しかったんだ。今でも欲しい。ピザに魚は乗せられるのか？ 今はそんなことしてくれるのか？"





hi "お前が払えよな。まだ俺に金返してもらってないし、そもそも腹減ってないし"


show kenji neutral
with charachange



ke "ピザ食う気分じゃないだと？　そんなのありえないだろ、坊や"


show kenji tsun
with charachange





ke "どっちにしろ、ピザじゃないといけないんだ。俺は今人生のピザ期にいる。前はアイスクリーム期だったけど、彼女が俺のナポリ風アイスのイチゴの部分ばかり食べ続けてたんだ。そのうち同じ目に遭うぞ、お前もな"







"毎度こいつが本気なのか判断がつけにくい。ドアに顔を押しつけてないときしか、健二の表情を見ることができない。"





hi "それはないな。なあ、お前俺に彼女がいるって知ってるだろ？　岩魚子でもないぞ。生徒会長、なんだけどさ"



show kenji neutral
with charachange



ke "とっくに知ってるさ"




hi "え？　マジで？"


show kenji happy
with charachange



ke "俺にも情報源はある"



show kenji tsun
with charachange




ke "とにかく……アイスの食べ過ぎで太ったことに気づいてな。突然目が覚めたよ。まるでビーチで寝ていたら波にうたれて砂の城が壊れたみたいな"




show kenji neutral
with charachange



ke "俺は走り始めた。痩せなきゃいけかったからな。だがしかし……本当は自分から逃げていただけなのかもしれない"


play sound sfx_doorknock
stop music
show kenji rage:
    tworight
    ease 0.3 twoleft
with vpunch



"突然ノックの音が立て続けに鳴り、健二は後ろに跳びすさって反対側の壁にぶつかる。そのすきに俺は歩み寄ってドアを開ける。"


play sound sfx_dooropen

scene bg school_dormhallway
show shizu behind_blank
with locationchange



ssh "おはよう。元気？"




ke "出入り口に塩を置いておけば、招待されない限りは中に入れないって聞くぜ"


play music music_comedy fadein 4.0

scene bg school_dormhisao
show kenji neutral at center
with whip_left




hi "俺は出入り口に塩なんて置かないぞ"




show kenji happy
with charachange



ke "しかし……考慮はしていると。よし"


scene bg school_dormhallway
show shizu behind_blank
with whip_right



hi "おはよう。郵便を届けにきたのか？"


show shizu adjust_happy
with charachange



"うなずきながら、静音は俺の顔との間に封筒を数枚ちらつかせる。俺がそれを受け取ると、静音の両手が空いて会話ができるようになる。"


show shizu basic_normal2
with charachange



ssh "どうして分かったの、どうして分かったの？"




hi "お前が非常に分かりやすく背中に隠してたから"




ke "何を隠してたって？"


scene bg school_dormhisao
show kenji tsun at center
with whip_left



hi "手紙"


scene bg school_dormhallway
show shizu basic_normal2
with whip_right

with Pause(0.2)

show shizu adjust_smug
with charachange



ssh "いいの、そもそもそんなに隠す気なんてなかったから"




hi "お前らしくないな。『やる価値があることは何でも全力でやる』タイプなのに"





ke "女子が主導権を握る？　そうしたら俺はどうなる？　俺はその台詞をもう何年も使ってるんだ。こっちのお楽しみはどこに行っちまうんだよ、ええ？"








ke "俺が吐き出した金言をお前ら女は気軽にパクって、一枚買うともう一枚サービスのサンドレスみたいに使い捨てやがる"
ke "お前らみんな、俺のカークに比べりゃピカードみたいなもんだ。いや、それどころかジェインウェイだ"






show shizu behind_frown
with charachange



ssh "いつもそんなんじゃないわ。バカにしてるの？"


show shizu adjust_happy
with charachange



"ようやく健二に気づき、静音は手を振る。"


scene bg school_dormhisao
show kenji tsun at center
with whip_left



hi "よう、健二、生徒会長がおはようだってさ"


show kenji neutral
with charachange



ke "おはよう"


scene bg school_dormhallway
show shizu behind_blank at center
with whip_right



ssh "紹介して。彼がなんて言ってたかは全く分からないけど、自信ありげに見えたわ"




"まったくだ、あんな話を自信を持って言うことに関して、あいつの右に出るものはいない。"




hi "もうしたよ。役職も紹介した。こいつは健二、廊下の向かいに住んでる。お前のすぐ後ろの部屋さ。それはそれとして、こいつ宛の手紙もあるのか？"


show shizu adjust_happy
with charachange



ssh "そこにあったからあなたの手紙だけ持ってきたわ。私は他の人より早く受け取れるの！　全てはどこに何があるかよ。生徒会の特典ってとこね"




"なんだか不公平な話だ。静音はおおいに職権を乱用しているな。少なくとも小さいものは。"



label jp_S34a:



ssh "今まであなたの部屋に入った事はなかったわ。興味深いわね"



label jp_S34b:



ssh "あなたの部屋をじっくり見られるのはこれが初めてね"




"これは明らかな嘘か、手話が早すぎたかのどちらかだ。静音はこれが初めてじゃないことを絶対に覚えてるはずだ。"



label jp_S34c:

show shizu basic_frown
with charachange



ssh "なんで彼はあなたの部屋を見られて私はだめなの？　男の子同士の何かなの？"




hi "男であることは別に秘密クラブでもなんでもないぞ"




ke "そうあるべきさ。指輪付きでな。バカでっかい刻印付きの指輪だ。あと金でできてる！"


show shizu adjust_smug
with charachange



ssh "本当に？　本当に本当？　私ずっと男同士の秘密結社があるって思ってたわ"




ke "なんでそいつは俺を無視するんだ？　そいつに漢クラブのことを話させてくれ。あと、その手信号みたいのはなんだよ？　俺に呪いかなにかをかけようとしてるのか？"


scene bg school_dormhisao
show kenji tsun at center
with whip_left




hi "違う、お前は引っ込んでろ。お前の言ってること全部静音に通訳するはめになるし、そんなの俺にできるかどうかわからない"
hi "それに静音はたぶん誤解するし、お前もその返事を誤解して、俺はお前の反論を通訳することになる"



show kenji happy
with charachange



ke "はんこ？　なんではんこが要るんだよ？　俺そんなの持ってないぞ"









scene bg school_dormhallway
show shizu behind_frustrated at center
with whip_right



ssh "なんて言ってるの？"




hi "反論はないって言ってる"


show shizu basic_normal
with charachange



ssh "なんの反論よ？　まだ議論も何も始めてないのに"





"静音の言い方がひっかかる。どうやら議論をふっかけたいみたいだ。でも何について？　関係ないか、どうせいい終わり方はしないだろうし。"






hi "理由もないのにけんかを売るなって"


show shizu adjust_frown
with charachange



ssh "私、あなたの友達に会ったことないわ。どうしてだめなの？　彼もなんていうか……乗り気に見えるわ"




"健二がああやって腕を振り回しているのを見て、静音がそういう理解をしないと思わない方がどうかしているな。どちらにしても、話題を変えた方が良さそうだ。"





"それが通用するとは思わないけど、静音が手紙を届ける以外の理由でここに来たのは間違いない。"





"もしそんなささいな用事なら、わざわざドアをノックすることもなかったはずだ。"





hi "俺に手紙を届けるとか、俺の友達とダベるだけのためにここに来たわけじゃないよな？"




play sound sfx_snap



"静音が不満そうなふりをして指を鳴らす。今までになく大きい音で、身がすくんでしまう。"


show shizu basic_normal
with charachange



ssh "その通りよ"


show shizu behind_smile
with charachange



ssh "またどこかへ行きましょう"




hi "もう行きたい場所は決まってるのか？"


show shizu adjust_smug
with charachange



ssh "また正解ね。いつもの所へ行きましょう"





"丁寧に包まれた弁当箱がいくつか入ったビニール袋を、ドア枠の外からさっと取り出す。多分食べ物で満杯なんだろう。それに今回は店で買ったものじゃなさそうだ。それを足下に置きながら、静音は続ける。"




show shizu behind_smile
with charachange


$ doublespeak (ke, ssh, "それ、俺にか？", "こっちが本当のサプライズ。どう？")



show shizu adjust_smug
with charachange



ssh "結局、私は誰よりも上でないと気が済まないのね"





"お、おう……"





show kenji invis:
    center
    xpos 0.0
with None

show shizu behind_smile at tworight
show kenji tsun at twoleft
show bg school_dormhallway at bgright
with dissolvecharamove



ke "ふん、上等だ、お前ら二人して俺を無視するんなら、出て行ってやるよ。なんてひどい奴らだ。後悔するぞ！"


stop music fadeout 2.0

hide kenji
with charaexit

scene ev shizu_roof at shizu_roof_in
with shorttimeskip

play ambient sfx_rooftop fadein 1.0
play music music_soothing fadein 0.5



"それからちょっとして、俺たちは学校の屋上にいた。"





"こんな週末の、晴れた日のこんな時間はこんな閑散としているのだろうか？　いや、そんなことはもちろんない。静音のしわざだろう。もちろん屋上の人払いにはドアの張り紙くらいしか必要ないだろうけど。"





"静音が用意した食事が入っていた、空の弁当箱が俺の横に置かれている。またしても静かな食事だった。箸を持っているとあまり会話ができないからだ。"




"問題になるほどではないけど、今日は風が強い日だ。空の弁当箱の下に敷いたビニール袋が風に吹かれて飛び、しばらく飛び回ったあと俺の足の上を転がって、静音の靴のつま先に引っ掛かる。"


show ev shizu_roof_towardsangry at shizu_roof_in
with charachange



"その瞬間、静音はそれをつかんで手話で話し始める。俺が笑っているのが不服そうだ。自分でも笑いを堪えているというのに。でもビニール袋が邪魔で、結局話を続けるためにはそれをお尻に敷かないといけなかった。"




ssh "面白くないわよ"


show ev shizu_roof_towardsnormal at shizu_roof_in
with charachange



ssh "どうだった？"


show ev shizu_roof2_towardsnormal at shizu_roof_in
with charachange



his "食事か？　なじみのある味だったよ"


show ev shizu_roof2_towardsangry at shizu_roof_in
with charachange



ssh "それはまずかったって意味ね"


show ev shizu_roof_towardsangry at shizu_roof_in
with charachange



his "違う、違う。まったく同じものを食べた覚えがあるからさ、お前が作った時の"




"まったく同じというわけじゃない。海老フライは新しかった。"




ssh "作り方を知っているのはそれだけだったの、でも上達はしてるはずよ"




his "いままで何回ぐらい作ったことがあるんだ？"


show ev shizu_roof_towardsnormal at shizu_roof_in
with charachange



ssh "これで二回目よ"




his "この料理を作るのが？"


show ev shizu_roof at shizu_roof_in
with charachange



ssh "料理自体が"


show ev shizu_roof_smile at shizu_roof_in
with charachange



ssh "今度は、あなたが挑戦する番ね"


show ev shizu_roof_towardsangry at shizu_roof_in
with charachange



"静音がビニール袋の角をいじっているのが気になる。そうしている理由は分かるような気がする。"


show ev shizu_roof2_towardsangry at shizu_roof_in
with charachange



his "それ、そんなに気になるのか？"


show ev shizu_roof2_towardsnormal at shizu_roof_in
with charachange



ssh "きちんと畳みたいのよ"


show ev shizu_roof_towardsnormal at shizu_roof_in
with charachange



his "いいよ、俺がやっておくから"





"ビニール袋を拾いながら、これだけの弁当箱をいっぱいにするために相当な量の食事を静音が用意したんだろうと気づく。"
"俺はそんなに食べなかった。あれだけのものを全部平らげたのだから、静音の代謝は相当なものに違いない。"



stop music fadeout 1.0
play sound sfx_impact

scene black
with vpunch





"立ち上がったばかりだったのに、間抜けにも自分の足につまずいてしまう。かろうじて転ぶのは避けられたけど、四つん這いになって静音の膝のとなりに着地していた。"





scene bg school_roof
with locationchange

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.7)




"体を起こし、恐る恐る胸に手を当てながら、俺は膝の痛みと、自分が下手をすれば死んでいたかもしれないということしか考えられなかった。気分が悪くなってくる。"






"静音が肩を押して、立ち上がるのを助けてくれるけど、妙な目つきで俺を見ているのに気づく。残念だけど、軽く押されるだけでも俺を驚かせるには十分だ。"



show shizu basic_normal2_close:
    center
    ypos 1.1
with charaenter



ssh "大丈夫？"




"俺はうなずくけど、元通りに隣に座ることはしない。静音といるときは必然的にいつもとても静かだけど、俺は今始めてそのことに気づく。気まずい状況の典型的な兆しだ。そしてまたしても静音が緊張を破る。"


show shizu behind_smile_close
with charachange




ssh "なにかいやらしいことをするんだと思ってた"





hi "……"


show shizu behind_sad_close
with charachange




"また雰囲気が妙な感じに戻る。"





his "ミーシャはどうしてる？"


show shizu basic_normal_close
with charachange

play music music_twinkle fadein 6.0




ssh "ミーシャは機嫌が良くなったみたい。昔のミーシャに戻った感じ。そのお祝いにこうするのがのがいいと思ったの、それとあの子を助けてくれたお礼に"





"最後の言葉で、静音の手は少しもたつく。"





his "考え方が事務的すぎると思うぞ"




show shizu behind_blank_close
with charachange



ssh "どうにもできないわ、そういうふうにするように教えられてきたんだもの"


show shizu adjust_happy_close
with charachange



ssh "あなたがミーシャのことを聞いてくれてうれしいわ。あの子は『本当の自分に戻った』っていうほうが正確ね。あなたにとっては以前のミーシャに戻っただけだろうけど"




show shizu basic_normal_close
with charachange



ssh "あなたが知っているミーシャは私の思い浮かべるミーシャとは全然違うわ、最初に会ったときを考えるとね。元気でいつも笑顔のあの子のほうがいいって思うけど、それは普段のミーシャじゃないの"


show shizu behind_blank_close
with charachange



ssh "もしかして、あなたもそうなのかしら？"




"俺は答えない。"





his "まあ、ミーシャが幸せなら、いいじゃないか、最終的にうまく行ったのなら。お前のプランは成功したってことさ"






his "お前が言った通りお前はミーシャの事をわかってた。あいつが話すことが全部わかってた。でもお前の計画が、俺がお前の代わりにミーシャと話すってだけなら、俺はただの駒じゃないか？　なら俺は何もしてないよ"





show shizu cross_angry_close
with charachange



ssh "違うわ。元々はあなたのアイディアよ"




show shizu basic_frown_close
with charachange




ssh "私は間違ってた。今考えてみると、私の物の見方はすごく問題があるわ。あなたも分かってると思う。時々、私はどんなことも他人との競争みたいに考えてしまうの。それが全然ふさわしくないときでも"





"時々？"


show shizu behind_blank_close
with charachange




ssh "手話でしか会話できない人がどんなに無視されやすいか、私にはよく分かってる。誰かに助けを求めるべきだったの"
ssh "でも私なら全部一人でできるって信じきってた。あなたがしたことは本当は勇敢だったわ。自分ではそう思っていなくてもね"



show shizu basic_normal_close
with charachange



ssh "それとは別に、あなたは本当になんだか立派になったわ"






"ここまで褒めてくれている間、静音の表情が全く変わっていないのは妙な感じだ。"


show shizu adjust_frown_close
with charachange



ssh "でも！"


show shizu basic_happy_close
with charachange




ssh "『人はそんな簡単に変わらない』。あなたによればね。でしょ？"






"静音はウィンクをする。明らかに楽しんでいるな。"




his "ミーシャは全部お前に話したのか？"


show shizu behind_blank_close
with charachange



ssh "大体全部ね"




his "そのことについては俺が間違っていた、って言うつもりなんだろ？"


show shizu basic_normal2_close
with charachange



ssh "それはイエスでもノーでもあるわね"


show shizu adjust_frown_close
with charachange



ssh "私がミーシャにそう言ったの、誰よりも先にね。でもあの子はそれを真に受けすぎて、意味を取り違えてしまった。もちろん簡単なことじゃないけど、あの子はまるで不可能みたいに振る舞うの"



show shizu basic_normal_close
with charachange



ssh "ちゃんとできるのよ、少しずつやっていけば。私、対抗意識をもう少し控えめにしようと思ってるの"




his "お前はそういうのを楽しんでるんだと思ってたけど"


show shizu behind_smile_close
with charachange




ssh "もしかしたらほんの少しだけね。だからあえて『控えめに』って言ったのよ"







"静音はフェンスに寄りかかる。言いたいことがあるけど、なぜか今はその時ではなさそうだ。そんな気がする。静音はまだ話し終わっていないのがわかる。"




show shizu basic_normal2_close
with charachange



ssh "私が頑張りすぎているって、いろんな人が思ってる"


show shizu adjust_happy_close
with charachange




ssh "まあ……私はいつもちょうどいいくらいに頑張ろうと努力しているつもりだったけど"






"静音が寄りかかるたびにフェンスが軋む音と、袖のボタンが金具に当たる繊細な音が、不思議と心地よい。後ろから吹いてくる柔らかい風もだ。下から生徒たちの喧噪が聞こえる。"


show shizu basic_normal_close
with charachange



"静音の目も下を見つめている。自分が何かから取り残されていないかと考えているのだろうか。彼女が人の気を引くために指を鳴らすのは、他の人が音をどう認識しているかを理解している証拠だ。"


show shizu invis_close at center
with dissolvecharamove

hide shizu
with None





"そこまで分かっていながら、それを自分で体験できないというのは、妙な感じに違いない。静音は袖のボタンでフェンスを撫でながら、ゆっくりと屋上の外周を歩き始める。"
"全然リズミカルじゃないけど、あえてそうしているわけじゃない。"







show shizu invis_close at twoleft
with None

show shizu basic_normal_close at center
with dissolvecharamove



"そうしている間に俺はぼんやりしてしまって、一周して戻ってきた静音に肩を叩かれてはっとする。"


show shizu behind_blank_close
with charachange



ssh "私たちが話していたこと、覚えてる？"




his "いつ？　今？　もちろん、ついさっきの事だろ"


show shizu basic_angry_close
with charachange



ssh "もう１０分くらい経ってるわよ"


show shizu adjust_frown_close
with charachange




ssh "初めてあなたに会ったとき、自分を哀れむ気持ちにすごくとらわれてるように見えたわ"






"その言葉が刺さる。事実だけど、それでも。"



show shizu behind_smile_close
with charachange



ssh "ごめん、ごめん"


show shizu basic_normal_close
with charachange



ssh "初めて見たその時から、あなたを元気づけたいって気持ちになった。でも無駄になるかもしれなかったから、怖いとも思ってた。あなたの考えを改めるのは難しそうだって思わずにはいられなかった"


show shizu behind_smile_close
with charachange



ssh "でもあなたは変わったわ。それでとても驚いたし、感化されやすい人なのかもって思った。でも、驚いたの。いろんな認識を改めたわ。例えば……結局全部、やってみて良かったんだって"




his "全部？"


show shizu adjust_happy_close
with charachange

stop music fadeout 4.0



ssh "――だからあなたの事が好きなのよ"




his "なるほど"




"やっとそれが分かって良かったよ。"


stop ambient fadeout 2.0

scene black
with dissolve


label jp_S35:

scene bg school_council_ss at right
show mishashort hips_smile_close_ss at closeleft
show shizu behind_blank_close_ss at closeright
with locationchange

play music music_ease



hi "……あと覚えていて欲しいんだけど、この仕事は真剣にやって欲しいんだ。サボっていても大丈夫とか、大して重要じゃないって思っている人は山ほどいる。そういう考え方は危ないんだ"




show mishashort cross_frown_close_ss
with charachange





mi "そうだよ～。真剣にやるに越したことはないよ～！　いつでも大きく、ポジティブに考えてないと、それにちょっとでも弱みを見せたりすると、みんなに役立たずだって思われちゃうんだよね～"




show mishashort sign_confused_close_ss
with charachange



mi "そしたら自分の権力がちょっとずつ他の人に委任されて、最後には何も残らなくなるから、自分は何もできなくなっちゃうんだよね。前回はそんなことが起きたんだよ～"


show mishashort hips_grin_close_ss
with charachange




mi "だから～！　覚えててね～、簡単そうな仕事に見えるかもしれないけど、この部屋の中では沢山の血が流れるかもしれないんだよ。あはは～"
mi "あと～、部屋の外でもね。学校の職員と関わるときもだよ！　クラス委員から予算報告をもらうのだって死闘になるかもしれないよ～、時々ね"







hi "……ああ。殺るか殺られるかだ。闘技場の中では友達はいないし、捕虜は取らない。……これ本当にいいのか？　大丈夫なのか？"




show shizu basic_angry_close_ss
with charachange




ssh "なんだか熱意があるって感じに見えないわ、ちゃんと伝わるようにしてもらわないと。もう一回、今度は気持ちを込めて！"





show aoi_keiko:
    yalign 1.0 xanchor 0.5 xpos 0.0 alpha 0.0
with None

play sound sfx_flash

show bg school_council_ss at left
show mishashort invis_close at Position(xpos=1.1)
show shizu invis_close at Position(xpos=1.6)
show aoi_keiko:
    center
    alpha 1.0
with Dissolvemove(0.5)





"静音は両手を指揮者のようにひねって力説し、目の前にいる二人の女子を見るからに引かせている。全ての事の発端は、二人のうちの片方が静音が仕事に対して真剣すぎるんじゃないかと尋ねたことだったと思う。"






ssh "わかった！？"





hi "二人とも分かった？　俺に怒鳴られてるふりしてくれるかな"






"葵" "分かった、分かりました！　ああもう！　この生徒会おかしすぎ！"




"恵子" "イエス、サー"




hi "『サー』？　そもそも、二人ともどっちに向かって話してるんだ？"


play sound sfx_flash

show bg school_council_ss at right
show mishashort hips_smile_close_ss at closeleft
show shizu adjust_frown_close_ss at closeright
show aoi_keiko:
    yalign 1.0 xanchor 0.5 xpos 0.0 alpha 0.0
with Dissolvemove(0.5)





ssh "おかしくありません！　これは仕事ととらえてもらわないと困るわ。なんだったら、このすばらしい生徒会室を使う権利が報酬だと思ってくれればいいわ"




play sound sfx_flash

show bg school_council_ss at left
show mishashort invis_close at Position(xpos=1.1)
show shizu invis_close at Position(xpos=1.6)
show aoi_keiko:
    center
    alpha 1.0
with Dissolvemove(0.5)



hi "レクチャーはまだ必要？"




"葵" "いいですぅ……"




ssh "もう行っていいわよ"


stop music fadeout 5.0

scene bg school_council_ss
show mishashort perky_smile_ss:
    twoleft
    ypos 1.1
with shorttimeskip




"かくもあっけなく、一時間にもおよぶ生徒会のオリエンテーションが終わる。個人的には５０分くらい長すぎたと思う。俺たちがずっと通っている学校のツアーも込みというのがおかしかったけど、無駄でもないか。"





"今日の静音は一日中ピリピリしていたので、席にどっと腰を下ろすだろうと予想していたけど、そうはしない。落ち着きなく部屋をうろうろと歩き回る。"


show shizu invis:
    center
    xpos 1.0
with None

play music music_shizune fadein 1.0

show shizu adjust_frown_ss at tworight
with dissolvecharamove



ssh "あの子たちは全然まだまだね！　今のところは使い物にならないわ"


show mishashort sign_confused_ss:
    twoleft
    ypos 1.1
with charachange



mi "え？"




hi "なんだって？"


show shizu behind_frustrated_ss
with charachange



ssh "本当に新しい生徒会になれると思っているのかしら？　全然集中できてないし。経験不足が目に見えて分かるわ。今年は最高の年だったけど、あの二人には私たちの後を継ぐための資質が欠けてると思う"


show shizu basic_frown_ss
with charachange




ssh "それにあの二人以外にもいっぱいいるのに、その人達は一体どこにいるの？"
ssh "そういう人はみんな、低予算だけど評判の高い隠れた名作映画のあとにできた、お金もいっぱいかけて宣伝しまくったくせに平凡な中身で酷評される続編みたいなものよ"



show mishashort perky_confused_ss
show shizu behind_blank_ss:
    ypos 1.1
with dissolvecharamove



"やがて、静音は足を止めて座る。"




hi "寂しくなると思うか？"


show shizu basic_normal_ss
with charachange



ssh "それはそうよ"




show mishashort perky_sad_ss
with charachange



mi "んん～……わたしもここを離れなくて済むのならそのほうがいいよ"




show mishashort hips_smile_ss
with charachange



mi "わたし、生徒会にいるのが好きなの、時には疲れることもあるかもしれないけど、それでも"




hi "ああ、本当に疲れるよな"


show mishashort hips_grin_ss
with charachange



mi "しっちゃんがいつも、必要以上に物事をやろうとするからだけどね～"


show shizu adjust_frown_ss
with charachange




ssh "もし私が最低限の仕事しかしなかったら、私たちはビラ配りとアンケートの回収と、次の生徒会が一年間何もせずに済むように生徒会選挙の準備をするほかは何もしなくなるのよ。そのことを忘れてるんじゃないの"



show shizu behind_frown_ss
with charachange



ssh "私にそんなことを見逃せっていうの？　冗談じゃない。そんな生徒会だったらそもそも乱用できるような権力も持てやしないわ"


show shizu adjust_happy_ss
with charachange



ssh "もっと厳しく鍛える必要はあるけど、あの二人は悪くないわ。それで十分満足よ。まだまだだけど、これならきっと新生徒会は安泰よ"




hi "なんで分かるんだ？"


show shizu behind_smile_ss
with charachange




ssh "文化祭のあと、ハロウィンのイベントをやってくれないかって聞いてきたのよ、お化け屋敷とかそんな感じの。他にも色んなアイディアを持ってたわ"



show shizu adjust_smug_ss
with charachange



ssh "もちろん私の返答は『却下』よ。そんなにやりたかったら、自分たちでやりなさいってミーシャに言ってもらったの。二人とも怒ってたわ、なぜかは分からないけど"


show mishashort cross_laugh_ss
with charachange



mi "あはは～"




hi "そんなこと言ったら怒るに決まってるだろ"





"それに、ミーシャに伝えさせたっていうのもだめだろう。"




show mishashort cross_smile_ss
show shizu behind_blank_ss
with charachange



ssh "私も怒ったわよ"


show shizu basic_frown_ss
with charachange





ssh "急に多くを欲しがって。お化け屋敷とか、昔風な喫茶店とか、海に遠足とか、そんなありきたりなことがやりたければ、どうして今まで自分たちで計画しなかったの？　私をいいように利用しているみたいだったわ"




show shizu behind_frown_ss
with charachange




ssh "私は文化祭の準備ですごく頑張った。そのお返しに、あの二人は私に『とっても良かったです、でも次はこれをやってくれませんか？　これはどうですか？　すごくやって欲しいんです』なんて言ってくるのよ"



show mishashort sign_smile_ss
with charachange



mi "でも、しっちゃんは間違ってたんだよね～"


show shizu basic_happy_ss
with charachange



ssh "そう。あの子たちはそれを実現したくて生徒会に入ろうとしてた。私はあの子たちを嫉妬させて煽ったのよ。それもある意味、モチベーションにはなるわ"


show shizu adjust_happy_ss
with charachange



ssh "なにか大きい事をやろうとする意志って、広がるものなのよ。それが私を乗り越えるためだとしてもね。それでも彼女たちは私を相手に挑戦することにしたわけ"


show shizu behind_blank_ss
with charachange



ssh "感心だわ。まあ、今のところはね。はっきりするまでには、もう少し様子を見ないといけないけど"


play sound sfx_snap

show shizu adjust_happy_ss
show mishashort perky_confused_ss:
    ease 0.1 ypos 1.05
    ease 0.1 ypos 1.1
with vpunch




"突然静音が指を鳴らし、ミーシャが席から飛び上がりそうになる。面白いな、どうやらこれに慣れるのは無理みたいだ。"



show shizu basic_happy_ss
with charachange



ssh "そうよ！　そういえば、無事生徒会を引き継げたお祝いにパーティーをやるんだったのよね？　せっかくだから今やらない？　でなければ今予定を立てて、明日やるとか"




hi "でもあの二人は引き継いでもないじゃないか。というか、お前が真っ先に言った言葉が『あなたたちはまだ役に就いてないから』だぞ。早すぎるんじゃないか"



show shizu adjust_frown_ss
with charachange



shi "……"


show shizu behind_blank_ss
with charachange



ssh "ミーシャ、どう思う？"


show mishashort hips_smile_ss
with charachange




mi "んん～、わたしも賛成、まだ早すぎるよ。それに～、どっちみちわたしは行けなさそうだし。ごめんね～！　っていうか、わたしもう出るところだったし"





ssh "どうして？"


show mishashort hips_grin_ss
with charachange



mi "ノ～コメント～！"


show shizu adjust_frown_ss
with charachange



ssh "いいじゃない、教えてよ"


show mishashort perky_confused_ss
with charachange



mi "うーん……おっけ～！"




"ほんとプレッシャーに弱いよな、ミーシャ。"


show mishashort sign_confused_ss
with charachange



mi "考えてたんだけど～……もし行きたくなくても、昔なら行くって言ったと思うよ～！　いつもならね～。わたしってそういう人だから。もうそういうことはやめなきゃいけないし、今がいい機会だって、そう思うんだ"


show mishashort perky_sad_ss
with charachange



mi "さよならを言うためのお祝いなら、わたしそんなのいらない。悲しすぎるよ～。かわりに何か別のことをしたいな。それに、ひっちゃんとしっちゃんは明日もまだここに居るじゃん。なんか違うと思うの"


show mishashort hips_grin_ss
with charachange



mi "あと、今日は他に学校でやらなきゃいけないことがあるしね～！　軽々しくサボるわけにはいかないの"


show shizu adjust_frown_ss
with charachange



ssh "延期にしてもいいのよ"


show mishashort hips_frown_ss
with charachange



mi "ううん。早すぎるさよならはいやだよ～！"




"そう答えるミーシャはとても毅然としている。"








hi "でも、今から行くんじゃないの？"


show mishashort hips_grin_ss
with charachange



mi "ん～？　あ、そうだった～！　わはは～！"


show mishashort perky_smile_ss at twoleft
with Dissolvemove(0.7)

show mishashort sign_smile_ss
with charachange



mi "おっけー、今以外は、早すぎるさよならはなし、いい？"


show shizu behind_blank_ss
with charachange



ssh "わかったわ"


show mishashort hips_grin_ss
with charachange



mi "うん、じゃああとでね～！"


stop music fadeout 4.0

hide mishashort
with charaexit

show bg school_council_ss:
    subpixel True
    center
    parallel:

        "bg school_council_ni" with Dissolve(5.0)
    parallel:
        ease 5.0 bgleft
show shizu behind_blank_ss:
    subpixel True
    parallel:

        "shizu behind_blank" with Dissolve(5.0, alpha=True)
    parallel:
        ease 5.0 xpos 0.5
with None



"そうして、俺と静音だけが二人きりで生徒会室に残される。"


play music music_dreamy fadein 4.0

with Pause(2.0)



"静けさの中に座りながら、夕暮れがゆっくりと夜に変わっていく。二人とも話す言葉を探している。"


show bg school_council_ni at bgleft
show shizu adjust_frown:
    center
    subpixel False ypos 1.1
with Dissolvemove(0.5)



ssh "本当にそんなにダメなのかな？"




his "そうだな。そんなふうに考えたことはなかったけど、やっぱりミーシャが正しいよ。パーティーは雰囲気を作るものだし、悲しいものになっちゃうよ。悲しいパーティーってのはあまり楽しそうじゃないからな"


show shizu basic_angry
with charachange



ssh "どうして悲しくなるの？"




"引っかけ問題か？　そうに違いない。答えを待ち構える静音の、超然とした分析者の視線が俺の目を貫く。しばらく見なかった視線だけど、それでも見慣れた感じがする。"




"俺は用心深く答えを考えながら、静音にとってその質問が持つ意味も同時に考える。"




"静音も憂鬱に感じているのかもしれない。あるいは、人がそのことを憂鬱に感じる理由が理解できないのかもしれない。両方とも同じくらいありそうだ。"




his "俺、お前が卒業したら、もうそれっきりなんだろうって思ってた。それが生徒会の終わりだって。お前もそんなふうに考えているのかなって思って"


show shizu behind_frown
with charachange



ssh "バカなこと言わないで。私は楽しみにしてるのよ。これでもう生徒じゃなくなるんだから、期待ってものが全然変わってくるわ。他の人から私への期待と、私から他のすべてのものへの期待が。とっても楽しそう！"


show shizu adjust_frown
with charachange



ssh "生徒会の事なら、十分よくできた人たちに引き継げるはずよ。何も悲しむことなんてないわ"




his "それ、本音じゃないだろ。たった何週間か前までは、生徒会を手放すのが嫌そうだったじゃないか。新入りたちに任せるのが嫌なんじゃなくて、とにかく生徒会の仕事をやめるのが嫌だったんだろ"


show shizu behind_smile
with charachange



"予想に反して、静音は微笑む。"




his "否定しないんだな"




his "それじゃ意味が分からない。どうしてそれでパーティーをしたいなんて思うんだ？"


show shizu basic_normal
with charachange



ssh "私は乗り越えようとしてるの。それに……お別れの会はとても大切なのよ。最初の第一歩が一番大事ってよく言うけど、最後までやり通してきれいに終わらせるのも大事なことよ、そうでしょ？"




his "そうかもな"


show shizu adjust_smug
with charachange




ssh "とにかく、私はお別れだなんて思っていないわ。でもイベントには違いない。やっぱりお約束はきちんと踏まえないとね"




show shizu behind_blank
with charachange

stop music fadeout 4.0



ssh "あなたはしないの？"




his "しないって、何を？"


show shizu basic_normal
with charachange



ssh "キスよ、もちろん"





his "それが『お約束』か？"



show shizu behind_blank
with charachange



ssh "そうするのが普通でしょ、違う？　自然なことよ"




"思い切って行動するときだ。さもなければ心臓が爆発してしまうに違いない。"


show shizu adjust_blush_close
with charachange



"すぐに静音にキスをする。速すぎて楽しむ時間もないくらいに。静音も心の準備はできていたとはいえ、その顔は真っ赤に染まる。俺も同じような熱が首と頬に上がってくるのを感じる。"


play music music_one fadein 4.0

scene evh shizu_undressing_clothed_stare
with whiteout



"もう一度キスしようと静音に近づく。でもその動きに合わせて静音は後ろに下がり、いたずらっぽく背後のキャビネットに飛び乗る。二人きりで、完全に無音の部屋の中、俺たちはしばらくお互いをただ見つめ合う。"


show evh shizu_undressing_clothed_kiss
with charachange




"今度は静音にもっと深く口づける。その唇は薄く、乾いていて、少しだけ開いている。静音が無理矢理キスを返してくるので、その感覚を味わうことができたのは一瞬だけだった。"






"さらにキスを深くすると、静音の前髪が俺の閉じたまぶたにかかる。服越しに身体の輪郭が感じられて、俺はよけいに静音を強く抱きしめる。"



show evh shizu_undressing_clothed_blush
with charachange



"お互い体を離すのに少し努力が必要だった。さっきのキスとこれから起きることへの想像で、二人とも顔が赤くなっている。息づかいが少し荒くなっているのは決して俺だけじゃない。"




"静音が俺のネクタイをゆるめると同時に、俺は静音のブラウスを脱がし始める。脱がし方を理解するのに少し時間がかかる。制服のブラウスの構造なんて今まで考えた事がなかった。"






"静音のブラウスは少し小さいらしく、腕の所でひっかかってしまう。どうにか脱がしていったけど、静音も同時に服を脱ごうともぞもぞ体を動かすので、少し難しい。なんだか笑える光景だ。"




play sound sfx_rustling

show evh shizu_undressing_unclothed_closed
with charachange




"腕が自由になり、静音はシャツをするりと脱ぎ去る。留め具を外して膝に落ちたスカートを足から外す。もうその体を覆っているのは下着だけだ。"






"静音の身体は豊かで張りがあって、肌の健康的な色合いは黒い下着と対照をなしている。美しい姿だ。窓から入る月明かりを背にするとなおさらそれが際だつ。"




show evh shizu_undressing_unclothed_blush
with charachange




"静音は俺の胸に目をやると、俺のシャツのボタンを一つずつ外し始める。静音の太ももを俺の手が上下に撫でていたので、その行為はひどく遅くなる。こうやって静音にいたずらができるのがちょっと楽しい。"



show evh shizu_undressing_unclothed_kiss
with charachange



"やがて、そしてついに、俺のシャツは床に落ちる。静音が突然俺をぐいと引き寄せてディープキスをしてきたので驚かされるけど、こっちもすぐにやり返す。"


show evh shizu_undressing_unclothed_talk
with charachange



ssh "なんで今日は屋上にいるときよりも大胆なのよ？"




ssh "それかあなたの部屋にいる時よりも？"





"いい答えを考えようとするけど、簡単じゃない。仮に答えられたとしても、俺はどう応じればいいんだ？　お役所仕事をしているとそういう気分になるんだ、というのでもなければ答えようがない。"





"シャツを取り去ったので、静音は俺のベルトに手をかける。俺は質問に答えるかわりにそれを手伝う事にした。今の時点では答えたところであまり足しにはならないだろう。"


scene bg school_council_ni
with locationchange




"ベルトは簡単に外れ、金属音を立てて床に落ちる。もう一度キスをしようと近づいて、静音の横腹をなで上げる。でも静音は急に手前に体を傾け、俺は後ろにつまずいてしまう。"





"自分の後ろにある机の固い角のことは、それが腰に食い込むまで考えもしなかった。そこにそんなものがあることさえ気が付かなかった。机の上に二人で倒れこみながら、俺は静音を少し強めにつかむはめになる。"


label jp_S35h:

show evh shizu_pushdown
with charachange



"静音は俺の上で勝ち誇り、俺はため息を押し殺す。また静音の勝ちだ。"




"気が散ってしまうけど、それも静音のブラがまるで空から降ってきたかのように俺の上に落ちてくるまでのことだった。必死に笑うのを我慢したけど、結局俺は笑いだしてしまい、その笑いは静音にも伝染する。"




"シャツ越しに見ても目立つ大きさだったけど、ブラから解き放たれた静音の胸は想像以上に大きかった。静音はブラを指でつまんで放り投げ、俺はその体に手をのばす。"





"机に膝立ちになって俺にまたがりながら、静音は下着を脱ぎ捨てる。それを手伝うように俺の手は無意識にその尻へと動いている。"
"腕の時計がちらりと見える。まだ数分しかたっていない、でもずっと長い時間が過ぎたように感じる。"





"静音はゆっくりと体を下ろしていく。だんだんと近づいて、お互いのあらわな胸が直接触れ合うまで。俺の胸の傷跡に静音の乳房が当たるのは妙な感覚だ。"


window hide

show evh shizu_straddle_open
with whiteout

with Pause(7.0)

window show




"静音が身体を起こすと、その胸が俺の胴から持ち上がるのと同時に、下腹にゆっくりと包まれて、ぬるりと中に入っていく感触がする。二正面攻撃か、と俺は状況を冷ややかに考える。実に静音らしい。"



show evh shizu_straddle_tease
with charachange





ssh "このまま動かないで、ずっと焦らしっぱなしにしてあげようかな"







"そう言うと静音は体を俺にこすりつけ、突然おそってきた快感に俺は思わず目を閉じる。言ってくれるぜ、静音。俺はすぐに無我夢中になってしまう。"


show evh shizu_straddle_closed
with charachange



shi "……っっ"






"静音は声を抑えようと唇を噛む。出したくない声。ここまで聞こえたのはこれが初めてで、声を漏らしていることに気が付いた静音は顔を赤らめる。"




"それを隠そうと、静音はさらに身体を強く打ち付ける。おかげで俺の身体も静音に向かって跳ね上がり、勃起したものが静音のさらに奥深くへとねじ込まれる。"




"その急な動きが引き起こした感覚に、俺は腰を静音にぐっと押しつける。静音もそれにあらがって、俺の身体を下に押し戻そうとする。その間に俺は両腕をなんとか体の下から引き抜く。"


show evh shizu_straddle_smile
with charachange



"その瞬間、静音が腰をさらに強く打ち付けて反撃する。"




"静音の柔らかく、押し殺したようなあえぎ声が、腰が俺に当たるたびに上下に動く豊かな胸が、生徒会室の静寂の中で時間とともに欲情をかき立てていく。"




shi "ん、ふうっ……"




shi "……んん……"




"もうこれ以上は耐えられそうにない。快感が足の間から湧き上がって、静音の体の重みでそれがさらに増幅されて、考えるのも難しくなる。腰が勝手に動き始める。"





"静音の手が俺の手を机に押さえつける。何をするにしても、静音の行動は押せ押せだ。"






"二人分の体重を受けて、下の机が音を立てる。壊れたりすることはないと思うけど、この音はかなりのものだ。"


show evh shizu_straddle_come
with charachange




"でも静音は気づいてもいない。ペースはどんどん上がって行き、その勢いで机から押し出されてしまいそうだ。前触れもなく、静音の動きが最後の頂点に達する。"




scene bg school_council_ni
with locationchange
with vpunch



"突然静音は動きを止め、そのまま落ちたら二人とも失神してしまいそうな勢いでこちらに倒れ込む。もし二人とも気絶している間に誰かが中に入ってきたら、これ以上最悪なシチュエーションはない。"





"驚いたけど、自分たちが裸であることと、突然痛い目にあって行為が中断したことを忘れるほどじゃない。"







"どうしてこんなことになってしまうんだ？　俺をずっと焦らしっぱなしにするためにわざとやったのか？　静音はおずおずと息をついて、俺と同時にそのことに気づく。"






show shizu behind_blank_nak
with charaenter



ssh "ごめんなさい、転んじゃったというか、滑っちゃったというか、そんな感じ"






his "そういえば、ドアの鍵がかかってないんじゃないか？"


hide shizu
with charaexit



"静音は急いで机から降りるとドアに駆け寄って確認し、鍵を閉め、また開けて、そして閉め、念のためにドアノブを引く。ようやく確認し終えると、両手で場違いな身振りをする。"




show shizu behind_smile_nak
with charaenter



ssh "セーフ！"





his "お前がそうやって物事を軽々しく扱ってくれて嬉しいよ"


show shizu behind_frown_nak
with charachange



ssh "わざとやったんじゃないわ。だったら、あなたがリードしたらどう？"


show shizu behind_smilelow_nak
with charachange



ssh "ほら"




hide shizu
with charaexit



"俺は静音の肩をつかんでテーブルの上に寝かせようとする。俺の時と同じようにテーブルの角が背中に食い込み、その眉間に不快そうなしわが寄る。結局自分からテーブルの上に横になる。"


scene evh shizu_table_smile
with dissolve




"静音が裸のまま横たわっているのを見るのもこれが初めてだ。鎖骨と胸の輪郭がとても綺麗で、そのまま俺の目線は均整の取れた尻へと下がっていく。繊細な砂時計のような姿だ。"





"身体のラインに沿って、肩から下るように手を這わせる。"





"俺はゆっくりと根元まで静音の中に挿入する。強烈な火照りと締め付けにすぐに包み込まれて、俺はさっきの続きをするために抽送を始めた。"






"俺の腰が静音に当たるたびに、そしてお互いに身体を支えている部分で、肌に触れる静音がとても熱い。体熱でやけどをしてしまいそうだ。"




"その上、俺はさっきよりずっと敏感になっていて、それを埋め合わせるように静音により強く突き入れている自分に気づく。"


scene evh shizu_table_normal
with charachange





"静音の太ももの曲線を撫でまわしながら、じっくりと丁寧に刺激を与える。静音が激しく反応して、腰が跳ね上がって俺の股間にぶつかる。バランスを失いかけて危うく二人とも床に落ちそうになる。"







"手を上へと動かし、静音の張り出した乳房をつかむと、今までずっとそうしたかった通りにもてあそぶ。それは見た目よりさらに大きく感じられて、俺の手にも余る。柔らかくて形も完璧だ。"





"乳首を指で弾くと静音は俺の下で身体をくねらせる。お返しとばかりに俺の腕に自分の腕を回し、指を握って俺を引き寄せてくる。まるでレスリングをしているみたいだ。この極め技からは逃げられない。"







"初めて二人の手が触れたときから、俺たちは繋がっていたのだろう。"




"生徒会の行事に次から次へと引っ張り回されたときでも、恋人として手を繋ぐときでも、静音が俺の手を取るときに伝わってくる強い自信はずっと同じだったと思う。"




"静音の手が机の上でのたうち、そして机の端につかまる、その両脚を俺の背中に回して、俺たちの身体をさらに押しつけあう。俺とのつながりはもっと深くなり、俺は静音の中にとらえられていく。"




show evh shizu_table_comeopen
with charachange



"静音の中はあまりに熱くてきつく、しかも下から俺を押し返してくるので摩擦は増すばかりで、俺は頂点へと追いこまれていく。"


show evh shizu_table_comeclosed
with whiteout

stop music fadeout 4.0



"あっけなく、その感触は終わる。直後の俺は、机をつかんで静音に挿入したままでいるしかなかった。力が入らないのと、静音の脚がまだ俺を離さなかったからだ。静音はというと、まるで夢見心地のような笑顔だ。"




"それを見て俺も笑顔になる。静音の両脚がゆっくりと外れ、俺はようやく引き抜くことができた。"


label jp_S35x:

scene bg school_council_ni
with locationchange



"疲れ果てた俺は、背中を机に預けて、服を着る前に息を整えようとする。"




"シャツのボタンをはめていると、胸の中に鈍くて熱い動悸を感じる。今までに起きた諸々の最後に、いやな後味が残ってしまった。"


show shizu behind_smile_nak
with charaenter



ssh "ミーシャが来られなくてラッキーだったわ、そう思わない？"




his "今日は珍しく冗談を言う気分なんだな"




his "あいつ、どんな用事だったんだろうな"


show shizu behind_blank_nak
with charachange



"静音は指で何もない空間を気だるげにたどり、ドアに向ける。"




ssh "自分で見にいってくれば"




his "教えてくれればいいだろ？"


show shizu behind_smile_nak
with charachange



ssh "自分の目で見たほうが面白いわよ。百聞は一見にしかずってね"





his "そうか。さえてるな。じゃあそうしてみるか。お前はどうするんだ、ずっとここにいるつもりか？　もう時間遅いぞ"




show shizu behind_blank_nak
with charachange



ssh "今日が生徒会長でいられる最後の日って感じがするから、ここで寝ようかしら。机の上で寝られるのも最後かもしれないしね。仕事を間に合わせるのに頑張った締切日の後みたいに"




his "そんなの変だぞ"




his "俺はベッドで寝るよ"




ssh "座りながら寝るのも技能のうちよ。とても役に立つわ"




his "そうだな"


scene bg school_lobby_ni
with locationchange



"部屋を出てしばらくした後、実際にミーシャが何をしているか見に行こうとする。静音の言い方がまるでタイムマシンでも作っているみたいに秘密っぽく聞こえたから、というだけの理由で。でもやっぱりやめておく。"






label jp_S36:

scene bg school_courtyard_ni
with locationskip


"この季節は夜の空気が心地よい。さわやかで少し湿気があるけど、ちょっと外にいても居心地が悪くなるほど寒くはない。中庭からほとんど人がいなくなる程度には遅い時間でもある。"


"静音と別れの言葉を交わしあってから、寮の部屋へと戻る。でも部屋にたどり着く前に、余計なことを考えてしまう。"


"ミーシャが何を企んでいるのか確かめてみるのも悪くなさそうだ。他にやることもないし。宿題はない。読みたい本も切らしてしまった。それに、単に知りたいというのもある。"

scene bg school_lobby_ni
with locationchange


"放課後に本校舎に立ち入るのはこれが初めてじゃないけど、それは普段なら静音やミーシャと生徒会室で長い一日を過ごした帰りに通るからだ。一人で立ち入ることはない。"



"雰囲気は静かだ。いつもの廊下を表現するのにこんな言葉は使わない。ちょっと気味が悪い。正面で照明がちらつき始める。ホラー映画みたいなシチュエーションが起きる前触れみたいだ。"



play sound sfx_rustling
with vpunch


"肩に手が置かれるのを感じて、反射的に体がこわばる。"



"ミーシャではないだろう。もしそうなら両手で俺の目を覆って『だーれだ』と歌うように言ってくるはずだ。"
"じゃあこれは誰だ？　健二ではないといいけど。せめて知っている人であってほしい。でなければ妙な話になってしまう。"


show shizu invis_close at tworight
with None

show shizu behind_blank_close_ni at center
with dissolvecharamove

play music music_happiness fadein 4.0


"その人物はするりと俺の前に現れる。静音だ。"


hi "こんなところで何してるんだ？"


"安心しきってしまい、俺は手話をすることも忘れる。"

show shizu adjust_frown_close_ni
with charachange


"静音は唇に指を当てる。耳が聞こえないとはいえ、音の大きさについては多少わかっていて、俺の表情から今のは声が大きいとわかったんだろう。どう考えても、今ここで大声を出すのはまずい。"


"でもそれじゃあ、どうしてミーシャは静音の通訳をしてるんだ？"


his "なんだよそりゃ。お前ここで何してるんだ？"




show shizu basic_normal_close_ni
with charachange


ssh "あなたが見に来るのを待ってたのよ。絶対来るって思ってたから。少し時間がかかったみたいだけど"


his "ここでずっと待ってたのか？"

show shizu behind_blank_close_ni
with charachange


ssh "そうよ、でもそれはどうでもいいわ。ミーシャに気づかれたくなければ、こっそりいかないと。もし私のこっそりさが足りてなかったら教えて。いい？"




show shizu basic_normal_close_ni
with charachange



"そう言って、静音は廊下のど真ん中をゆっくりとつま先立ちで歩き出す。俺は静音の肩を叩いて注意を引く。"




his "それはこっそりしてない"


his "なんでこそこそしなきゃいけないんだよ？"

show shizu behind_frustrated_close_ni
with charachange


"静音は答えようとしない。たぶん手話と忍び歩きを同時にやるのは難しいんだろう。"

scene bg school_hallway3_ni
with locationskip



"あっという間に俺たちの教室の前にたどり着く。"


stop music fadeout 0.5
play sound sfx_snap
with vpunch


"突然、むちを打つような音が空気を切り裂く。それに続いて、聞き覚えのあるいらだった声。"


"今みたいな音は間違いなく心臓に悪い。言うまでもないけど、こんなに静かな状態ではどんな音も普段の百万倍は大きく聞こえる。音は部屋の中から聞こえてくる。俺は横歩きで静音に近づき、中をのぞく。"

scene ev misha_nightclass:
    center
    xpos 0.4
show ovl misha_nightclass_aperture at left
with silentwhiteout

play music music_comedy fadein 0.5


mu "頼むから鉛筆を投げるのはやめてもらえないか？　いったい何をどうしたら鉛筆でそんなでかい音を立てられるんだ？"


ssh "すごくびっくりしてるみたい"


"控えめな言い方にもほどがある。武藤先生に同情を禁じ得ない。教室の壁と分厚いドア越しでも、ミーシャの鉛筆が音速の壁を越えるのが聞き取れた。先生の鼓膜は破れて、壁に痕が残ったに違いない。"

show ev misha_nightclass:
    ease 1.0 xpos 0.23 xanchor 0.0
show ovl misha_nightclass_aperture:
    ease 1.0 right
with None


mi "投げてないですよ～、緊張すると鉛筆回ししたくなるんですけど～、でも手に持ってることを忘れちゃって、それで――"


mu "そんなことはどうでもいい、とにかく鉛筆があちこち飛び回ったりするのは困る。そんなものは普段の授業だけで十分だ。放課後は勘弁してくれよ"





mi "そ、そうですね～！　ごめんなさい"


mu "いいから、とにかく物を投げたり手放したり落としたりするのはやめてくれ。頼むから。教師にも仕事ってものがあるんだよ"

scene bg school_hallway3_ni
show shizu behind_blank_close_ni at center
with locationchange


"静音が俺と同じ光景を見ているのに気づく。武藤先生はあらん限りの声でどやしつけていて、一方ミーシャはいつも通りのミーシャだ。"


"先生の声はドア越しでもよく聞こえる。でも当たり前だけど、静音には何も聞こえない。この光景を見てどう感じているんだろう、と気になる。"




"俺にも見てほしいと言っている以上、静音にも状況はわかっているはずだ。でも静音は目に見ている状況を理解するために人よりも必死に努力しないといけない。自分が何かを見逃していると感じたことはないのかな。"



show shizu basic_normal_close_ni
with charachange


ssh "ミーシャが補習を受けてるみたいね。違う？"


his "そうだな"


"ただの言葉のあやと知りつつ、俺は答える。"


show shizu behind_smile_close_ni
with charachange


ssh "ミーシャは将来、本気で手話の先生になりたいって言ってた。推薦がもらえれば海外で勉強ができるんだって。だからあんなにがんばってる。ミーシャの成績は普段からあまり良くなかったから"


his "なんか俺まで後ろめたくなってきたよ。俺だって自分の進路はまだ決めてないのに"

show shizu adjust_smug_close_ni
with charachange


ssh "私もよ！"


"陽気そうな手話のしぐさはとても静音らしくなくて、ついでにいえば明らかに嘘だ。"

show shizu basic_normal2_close_ni
with charachange


ssh "戻りましょう。姿を見られたくないし。こんなところでバカみたいに突っ立ってるのを見られたらまずいことになるわ"


his "どこに？　生徒会室か？"

show shizu adjust_happy_close_ni
with charachange

stop music fadeout 3.0

show shizu invis_close at tworight
with dissolvecharamove


"頭を振ると、静音は廊下をはさんで反対側の教室に忍び込む。"

scene bg school_room34_ni
with locationchange


his "たいした隠れ場所だな"



show shizu behind_blank_ni at center
with charaenter



ssh "最近、やけに皮肉が多いじゃない。ドアは閉まってるし、十分いい隠れ場所よ。それにさっきのは面白くなかった？"




his "面白かったけど、そんなに驚きはしないよ"

play sound sfx_doorclose


show shizu adjust_smug_ni at Position(ypos=1.1)
with dissolvecharamove


"俺が背にしたドアを閉めると、静音は声もなく笑い、椅子に腰掛ける。一瞬、俺は気落ちする。静音の本当の笑い声を聞きたいと思う。"

show shizu behind_smile_ni
with charachange

play music music_innocence fadein 10.0



ssh "私は驚いた。ミーシャのこと、ずっと見下してたから。目標なんて何もない子だと思ってた。でも間違ってた。軽はずみな思いこみだった。ミーシャは私と同じくらい無計画と思ってたの。バカだったわ。私の負けよ"


show shizu basic_normal_close_ni
with charachange




"静音は動きを止めて指の関節を鳴らすと、手を重ね合わせて椅子に座ったまま体を前に倒す。異常なまでの静けさの中で、ドア二枚と廊下をへだててなお、武藤先生がまたミーシャを怒鳴りつけるのが聞こえてくる。"





"静音の目は俺の目をしっかりと捉えている。きらりと光る眼鏡の後ろから、瞬きもせずに今の言葉に対する俺の反応をうかがう。"


"これはテストなんだ。静音は質問への答えで他人を評価することはほとんどない。本当に大事なのは、発言に対してどう反応するかだ。"



"よくよく考えれば筋が通っている。喋ることができないということ、それに静音の性格そのものからすれば、何かを『言う』ことはそれだけで静音にとって重大なことなんだ。すべてにおいて。"





"そのせいで、静音が何の思惑もなく話をすることなんてあり得ないんじゃないか、と疑ってしまうこともある。"






"被害妄想が過ぎるような気もする。健二だってそう思うだろう。"
"そんなことで頭がいっぱいになって、静音に返事をし損ねてしまう。静音は答えはないと受け取ったようだ。このテストには目に見えない、そして普通よりも短い時間制限があった。"


show shizu adjust_smug_close_ni
with charachange


ssh "やっぱり"


his "何がだよ？"

show shizu behind_blank_close_ni
with charachange


ssh "そうは思わないんでしょ？"


his "まあな、そういう意味じゃなくて。ただ俺には分からない"

show shizu basic_normal2_close_ni
with charachange


ssh "私は他の人たちに自分の考えを押しつけたいの"


"さわやかなくらい正直だな。"

show shizu behind_frown_close_ni
with charachange


ssh "そんな変な目で見ないでよ。いつでもそう思ってるってわけじゃないんだから"

show shizu basic_normal_close_ni
with charachange


ssh "最初は、退屈してただけだった。他の人が何かに情熱を注ぐのを見たかったの。そしたら、私がその人に勝つことができる。他人の能力や信念を試したいと思ってたのよ"

show shizu adjust_frown_close_ni
with charachange


ssh "でも無理だった。この学校の生徒は何かに賭ける情熱なんて、何も持ってないんだもの。みんな引きこもりたいだけなのよ"

show shizu behind_frustrated_close_ni
with charachange


ssh "信じられない。そんなのつまらなくてしょうがないじゃない。こんな活気のない人たちが現実にいるなんてあり得ないって思った。平穏に過ごしたいどころの話じゃないわ"

show shizu adjust_angry_close_ni
with charachange


ssh "興味のあることが絶対あるはずだと思った。みんな何かを隠してるんだと思った。それを暴いて、あらわにして、引っ張り出したかった"

show shizu behind_blank_close_ni
with charachange


ssh "誰かの心を開いて、しかも元気づける一番うまいやり方はね、自分自身のことを話して、相手に向けて自分を開くことよ。そうやって、相手が自分の話をしやすくなるように仕向けるわけ"

show shizu adjust_happy_close_ni
with charachange


ssh "ギブアンドテイクみたいのものね。でも相手を誘導するようなところもあって、そこが面白いんだけど"

show shizu behind_blank_close_ni
with charachange



ssh "私にはそれができない。私が自分のために、ミーシャに私のことを話させようと思ったら、傲慢だと思われてしまう"
ssh "メッセージは伝令役を通じてしか伝えられない。私はミーシャの隣にいて、自分のことを他の人に説明しろって命令してるのよ"


show shizu adjust_frown_close_ni
with charachange


ssh "そんなことは手話が分からなくたって理解できるわ。自分がそんな状況に押し込められたら、私だって自分が傲慢だって感じると思う"

show shizu basic_angry_close_ni
with charachange


ssh "すごく悩んでた。ミーシャ以外の人とどうやって話をすればいいのか分からなかったんだもの。誰も私には心を開かなかった"

show shizu behind_frown_close_ni
with charachange



ssh "それで私は人に信頼とか、信用してもらうことはできないんだ、っていう結論に達したの。だから何かを作って、それをみんなに見せて、喜んでくれることを期待するしかなかった"
ssh "さもなければ、もっと自分が強引になって、それが他の人に伝染するとかね"



"それって俺のことなんだろうな。すこし気が滅入る。"

show shizu basic_normal_close_ni
with charachange


ssh "いつからか、私はミーシャを無視するように、見下すようになった気がする。ミーシャがいるのが当たり前だって思ってた。それが一番適切な説明だと思う。あの子は自分の延長でしかないって、そういう感じだった"





show shizu behind_sad_close_ni
with charachange


ssh "でもミーシャはずっとそばにいて、私に心を開いてくれていた。いつでも自分の１００パーセントを私に与えてくれていた。そのことを忘れてたのよ"

show shizu basic_angry_close_ni at center
with Dissolvemove(0.7)



ssh "自分の探していたものを見つけられなかったの。それはもう目の前にあったから"
ssh "私ってなんてバカなんだろう。本当に傲慢になっちゃったんだ。だから私は負けたのよ。昔よりももっと先が見えなくなってる。逆向きに進んじゃってる"



"前後に体を揺らしている。ほとんどふさぎ込むようにしているのに、それでも静音はエネルギーで満ちていて、動きを止めることができずにいる。"


"今の静音に電線の両端を持たせたら、電球を光らせることができるに違いない。これだけ真剣な静音の前で、こんなのんきなことを考えられる自分が奇妙に思える。"

show shizu adjust_frown_close_ni
with charachange


ssh "それなのに、ミーシャは私が自分にとって刺激になってるって言うのよ。おかしいと思わない？　私なんかが他の人にとって刺激になるわけがないのに"




show shizu behind_blank_close_ni
with charachange


ssh "自分が刺激を受けた人に欠点があるとしても、それはそれよ。考えたことはあるの。偽善だって、場合によっては受け入れられることもあるしね"




show shizu basic_normal2_close_ni
with charachange



ssh "たとえば……あるスポーツ選手を尊敬していて、その人がスポーツマンらしくない行動をしたとして、人としての短所はあっても、その能力だけでその人は尊敬に値するかもしれない"




play sound sfx_snap
show shizu adjust_angry_close_ni
with charachange


ssh "ただし、"


"静音が小気味よく指を鳴らす。無人の部屋の中で、その音は雷鳴のように響き、静音は数秒かけて指を伸ばす。考えてみれば、こんなに長く静音が手話をするのは初めてだ。"



show shizu cross_angry_close_ni
with charachange


ssh "私みたいな人間が目的を持っていないとしたら、そんなのは絶対に許されないわ。最悪の偽善よ。それに偽善者は一切責任を負うことなんてできない。自分自身を律することさえできないんだから"


"びっくりするような悲観主義だ。考えるだけで腹が立ってくる。"


"たった数ヶ月前の自分も、俺は嫌うだろう。あの時の俺は、他の人たちからはこんな風に見えてたんだな。"


"そして、おかしな話だけど、そんな俺を引き留めてくれたのも静音とミーシャだった。二人がいなければ、きっと状況は違うものになっていた。いい方向には向かわなかっただろう。"


"最近、俺たちはお互いを支え合っているのと同じくらい、自分の辛さや苦しさを二人でたらい回しにしている気がする。でもそれは結局、友達でいること、誰かに寄り添うことの範囲内なんだろうな。"





his "まあ、リーダーはお前だからな"

show shizu behind_frown_close_ni
with charachange


ssh "それは他に誰もなりたい人がいないからってだけよ"



his "つまり、お前はまだリーダーってことだろ。そういう形でみんながお前を信任してるんだから。というか、そっちのほうがもっと大事なことじゃないか？"






his "どっちにしても、お前はリーダー、刺激を与える人物、好きな呼び方をすればいいさ。お前が支配しているものに、お前は責任を負ってるんだ"



his "何かの本で読んだんだけどな"

show shizu basic_normal_close_ni
with charachange


ssh "気が利いてるわね"


"静音はそうしたいと思ったときにしか自分の気持ちを顔に出さないタイプに見える。でも今のは皮肉ではなさそうだ。"

show shizu adjust_frown_close_ni
with charachange


ssh "私は誰も『支配』はしたくないんだけど"


his "じゃあリーダーであること、尊敬されること、でどうだ。同じことだろ"

show shizu behind_frustrated_close_ni
with charachange


ssh "リーダーになんて一度もなりたくなかった。結果としてそうなっちゃうのよ"


his "そうは思わないな。お前、次から次へと責任を背負い込んでばっかりじゃないか"

show shizu adjust_frown_close_ni
with charachange




ssh "待って、待って。楽しくないって言うつもりはなかったの。リーダーなんてどうでもいいけど、なるのは構わないの。ベストかどうかもどうでもいいけど、それでも構わない"
ssh "ただ、私が責任を好き好んで背負い込んでるって言うのは確かにその通りよ"






show shizu basic_happy_close_ni
with charachange



ssh "もっと責任を負いたいって、そんなの当たり前じゃない。責任を負うことで生き返ったような気分になるの。だから生徒会に入った。プレッシャーがないと耐えられないのよ"




show shizu behind_blank_close_ni
with charachange


ssh "それでも、今は私がリーダーなのよね。リーダーっていうのは指示するのが仕事だとずっと思ってたけど、実際にはそれだけじゃなかった"

show shizu adjust_frown_close_ni
with charachange


ssh "目標を持つのがリーダーの本質だったのよ。私自身に目標がなければ何の意味もない。それじゃあ私のお楽しみにみんなが付き合わされてるだけになる。そんなのはわがままよ"


"他人に勝つのが好きでしょうがないような人物にしては、おかしなくらい良心的なものの見方だな。"

show shizu basic_normal2_close_ni
with charachange


"重ねた指にあごを乗せ、一生懸命に自分の悩みを考える静音は、無防備なくらい子供っぽく見える。その表情はちょっと滑稽だ。あまりにわかりやすくて、そのせいでとても静音らしくない。"


his "それは仕事についてくるものだよ。お前はリーダーにならなきゃいけないと思う。それ以外のものじゃお前は満足しないだろ。飽きちゃうだけさ"

show shizu basic_frown_close_ni
with charachange


"静音は答えない。でもそのムッとした表情を見ると、俺の予想は当たってたようだ。"




his "最近、俺もちょっと進路のことを相談したいなって思ってたんだ"





show shizu adjust_happy_close_ni
with charachange


ssh "社会貢献は大事だって言われたの？"


"なんてへんてこな反応だ。あまりに唐突でどう返していいかわからない。それに理由は分からないけど困惑する。静音から出てくるような話題には思えないからだろう。"



"これは静音自身の考えではないんじゃないか、と思う。こんなことを吹き込んだのは誰だろう。まあ、多分静音の父さんだろうな。でも自分で思いついたという可能性もある。"
"だとしたら、自分の耳が聞こえないからなんだろうか？"



his "どうしてそんな話になるんだ？"

show shizu behind_blank_close_ni
with charachange


ssh "別に"


his "嘘つけ"



his "でもまあ、そういうことなんだろうな"


show shizu basic_normal_close_ni
with charachange


ssh "なるほどね"

show shizu adjust_frown_close_ni
with charachange





ssh "私にとってはそうなのかどうかわからない。それがすごく嫌"






"誰しも、目的を持ちたいと思ってるんだろう。振り返れば、静音に目的がないって言うのは筋が通る。さもなければあれだけのエネルギーは何か別のものに向かっていたはずだ。"






"エネルギーをつなげる先がどこにもなくて、静音はあらゆる方向にそれをぶちまけた。嵐の中で切れた電線が暴れ回るのを連想する。怒りに燃えて、白熱していて、でも何の当てもなくて危険で。まるで静音みたいだ。"




"だから静音はあらゆるものを競争にしたがるんだ、と言ってやりたい。でも……それが静音なんだろうな。そのエネルギーを注ぐ目標を持つのは、すぐ次の段階でしかない。"

show shizu behind_blank_close_ni
with charachange


ssh "こういうのはどう？　起業するの。私の家族は人脈が多いから、難しくはないはずよ……なんだか今の、倫理に欠けるというか、縁故主義みたいに聞こえた？"


his "ちょっとな"

show shizu adjust_frown_close_ni
with charachange


ssh "でも楽をするつもりはないわよ。一生懸命働くわ。本当の頂点に立つまで"


ssh "使い道が考えつかないくらい、思いっきりお金を稼いだら、次のステップに進むの。もちろん、おとぎ話のドラゴンみたいに、しばらくお金の上にどっしり座ってからね"


his "で、何になりたいんだ……？"

show shizu basic_happy_close_ni
with charachange


ssh "慈善家よ！"


hi "……"

show shizu adjust_smug_close_ni
with charachange


ssh "ちっちっち。なんだと思ったの？　守銭奴になりたいって？"

show shizu behind_blank_close_ni
with charachange


ssh "まあ、確かにそうよ、それもプランの一部。でも私を見くびってもらっちゃ困るわ"




stop music fadeout 8.0


"静音はまだ不安そうだ。それはそうだろう。自分の悩みをあっさり解決したように見えても、不安をそんなに早く乗り越えられる人はいない。誰だってそんなに簡単に悩みを解決できたりはしない。"


"大事なのは、やってみようという決心をしたように見える、ということだ。静音の意欲が良いところから来ているのか、それとも悪いところか、見極めるのはいまだに難しい。"


"でも静音には確たる目標ができた。俺には心底からそう思える。俺もうれしい。同時に、少し寒々とした気持ちになる。今度は俺が遅れている。今、目的がないのは俺だけだ。"

$ suppress_window_after_timeskip = True

scene black
with dissolve



label jp_S37:

window hide None
nvl clear

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_daily fadein 0.5

scene bg school_dormhisao_bw
with dissolve

nvl show dissolve


n "\n\n\n\n\n\n\n\n\nあの週からは何の混乱も起きていない。"

nvl clear


n "\nもちろん、そう思ったのはその前の週のことだ。そして静音とミーシャが突然悟りを開いたことに、俺は少しとまどいと嫉妬を覚えていた。その時は、自分が安心していられるわけがないと思っていた。"






n "でも幸いに、その心配は無用だった。気づいてみると学校の出来事が山ほどありすぎて、そのことは頭の中からきれいに忘れてしまっていた。それでも何もかもが順調だった。"


n "俺は間違っていた。注意深く隠されていた、静音とミーシャの弱さを俺は目にしていたけど、それは今でも根強く残っていた。"


n "そして俺たちはもうすぐ卒業だ。ここでの生活にあまりに慣れ親しんだおかげで、そのことが徐々に俺にしのびより始めていた。すると俺は悲しくなって、考えたくないと思った。だから考えなかった。つい最近までは。"


n "一週間ほど前、卒業前に別れの挨拶をする人のリストを作り始めた。自分に課した一つ目のルールは、たとえば一番縁遠い人から一番大事な人まで、みたいに順番をつけて並べたりしないということだった。"


n "でもどういうわけか、結局そういう並びになってしまった。それと、思っていたよりも短いリストになった。健二は真ん中のどこかにおさまった。"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_dormhisao
show kenji neutral at center
with locationchange

window show


ke "俺ももうすぐ卒業だって言われたんだ。奴らに見せつけてやったぜ。俺は十分長い間、家賃も払わずにここで住み通した。地価の上昇を計算に入れれば、最終的には俺の勝ちと言えるだろうな"

show kenji happy
with charachange


ke "いや、待て。こりゃ確かに俺の勝ちだ。歴史は俺を勝者として認めるぞ"


hi "何の勝者だよ？"


ke "人目から逃れて、隙間をすり抜けることに成功したんだ。俺はシステムに勝利したんだ"


hi "その言い方だと、お前が単にシステムから逃げただけみたいに聞こえるな"


ke "時には逃亡は最高の勝利の形なんだよ。オリンピックみたいにな"


"こいつと議論するのはもう飽き飽きだ。どういう冗談だよ？　大体、オリンピックで一番の競技は砲丸投げに決まってるだろ。"





hi "じゃあ、お前が言いたいのは、寂しくなんかないってことか？"

show kenji neutral
with charachange


ke "何が寂しいって？"


hi "卒業がだよ、バカ"




show kenji tsun
with charachange


ke "それはない。言っただろ、この学校はフェミニストだらけだ。もう救いようがない。でも少なくとも、臨界を迎える前に俺はここを出られるからな。遠い未来になって、俺を称える彫像が建ったときに帰ってくるさ"


hi "１０年後に同窓会とかするのかな？"

show kenji neutral
with charachange


ke "俺が知るかよ。多分な。まあいいや。俺、荷造りしないと。お前も気をつけてな"


hi "一週間前には荷造りを終わらせとけよ。俺みたいに"


"大して荷物もなかったけどな。"

show kenji tsun
with charachange



ke "そうはいかないんだよ。物事ってのは何でも時間ぎりぎりになってやらなきゃだめなんだ"
ke "男はどんなこともぎりぎりの時のほうがよくできるんだよ。その方が、たとえば一週間前なんかよりてきぱきできるんだ。そうすればクソ面倒なこともうまくいく"


show kenji neutral
with charachange


ke "けっ、お前には俺たちの男らしいやり方は絶対わかんねえよ"


hi "お前も元気でな"

show kenji happy
with charachange

show kenji invis at right
with dissolvecharamove

play sound sfx_doorslam

hide kenji
with vpunch


"会釈をすると、健二はドアを駆け抜けて、後ろ手でバンと閉じる。思い切り力を入れたので、寮全体に音が響いただろう。そういえばここではドアを乱暴に閉める人が多い。この地方の習慣なのかもな。"




"『気をつけてな』だって。あいつがそんなことを言うのを聞いたのは初めてだ。普段なら『あばよ』とか『今度返すからさ』なんて言葉で会話を終わらせるのに。"
"まあ、時にはちょっとうるさいやつだったけど、寂しくなるな。心の中で健二の名をリストから消す。"




"もうリストはかなり短くなった。もう一度、順番がどうこうという考えを振り払う。前も言ったけど、そんなつもりは最初から一切ない。"

scene bg school_dormhallway
with locationchange


"というわけで、静音とミーシャを探しに出る。いそうな場所は一カ所しか思いつかない。もちろん生徒会室だ。"

play ambient sfx_crowd_indoors fadein 2.0

scene bg school_lobby
show crowd
with locationskip


"角を曲がると、数人の生徒の群れにぶつかりそうになる。一瞬、苦い記憶が蘇る。場合によっては命に関わっていたかもしれないから。"


"新しい生徒会のメンバーだ。人数は少ないけど、三人よりはよっぽど多い。つまりそれぞれが自分の肩書きを持てるわけで、それは良いことだ。"


"自分の名前と肩書きの入った飾り板を机に置けたらかっこよかっただろうな。今も昔もそんなことはしていないだろうけど。残念なことに。"


"考え事をしている間に、新生徒会が俺を取り囲んでいる。遠くからこの様子を見ている人がいたら、きっと相当危なそうな光景に見えただろう。"



"ずっとこいつらのことを『新生徒会』って呼んでたから、ついに仕返しに来たんだろうか。俺は静音の通訳をしてただけなんだけど。でも横着せずにもっと気を使うべきだったのかもな。後悔はしていない。"



"『俺のしたこと全て』について、俺はお礼を言われている。"


"お礼を言われている。今まで何度も、生徒会は報われない仕事だと思ったことを考えれば、いい気分になってしかるべきだ。確かにうれしいけど、完全には喜べない。"



$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve


n "\n\n俺たちの生徒会が、これから引き継ごうとしている新生徒会と同じくらいに大きくなっていたら、どうなっていただろう。"


n "たった二、三人多いだけとはいえ、役割分担ができるくらいの人数はある。静音は会長っぽかったけど、それ以外には何もなかった俺たちとは違う。"


n "新生徒会にお礼を言われていることに、奇妙な感覚を覚える。家に戻ったら、何年も前に世話をした木が大きく育っていた、というような。でも世話をきちんとしていなかった気がする。他に何ができただろう。"


n "こういう形で生徒会でやってきたこととの距離を感じるとか、仕事が不十分だったとほのめかしたら、静音は激怒するだろう。でもそうなんだ。俺は静音を追いかけていただけだ。"


n "\nだからある意味、俺もその同じ木を遠くから見ているような気分になっている。通り過ぎる列車の窓から見ているかのように。"

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
stop music fadeout 4.0

nvl hide dissolve
nvl clear
window show


"考えに浸りすぎていた。ふと気づくと、新生徒会の奴らに囲まれたまま、俺はずっと立ちつくしている。自分にできるただ一つのことをする。ぼんやりしていたことを謝り、お礼を返す。"

stop ambient fadeout 0.5

scene bg school_council
with locationchange

play music music_normal fadein 3.0


"新生徒会が去ると、俺は生徒会室に入る。中はずっと散らかっているけど、どうやらパソコンを手に入れたようだ。"




"筋は通ってる。そういえばクリップボードを持っていた子の一人が、静音のやっている退屈なデータ入力をもっと楽にするためにパソコンを使う、という話をしていた。"


"ただ、誰が言ったのかは思い出せない。葵は意欲的な方に見えるけど、一方恵子はもっと真剣そうだ。まあ今は関係ないか。"




"部屋にいたのは俺一人ではなかったけど、いるだろうと思っていた静音ではなく、ミーシャだけだ。静音が普段そうしているように静音の机の上に座って、足をぶらぶらと前後に揺らしている。"


show mishashort invis:
    center
    ypos 1.2
with None

show mishashort hips_grin at center
with Dissolvemove(0.5)


"俺と目が合うとミーシャは飛び降りて、どういうわけかスーパーヒーローのようなポーズを取る。"


mi "こんちは、ひっちゃん～！　ここで会うなんて驚いたよ～！"


hi "何してるんだ？"

show mishashort cross_smile
with charachange


mi "そっちからどうぞ～"


hi "静音を探してたんだ"

show mishashort cross_grin
with charachange


mi "わたしもだよ～！　ここにいると思ったんだけど、代わりにひっちゃんを見つけたよ～！"


hi "おお、ありがとよ"

show mishashort sign_smile
with charachange


mi "わはは！　まあ～、よかったよ。ほんとほんと～。ひっちゃんにも話がしたかったしね～"


hi "何の話だ？"



"しばらく、部屋の中をよく見回す。ホットプレートがある。新生徒会の奴ら、本当に贅沢な暮らしぶりだな。"




show mishashort perky_sad
with charachange


mi "謝りたかったんだよ～、当たり前でしょ～、ひっちゃんとしっちゃんにあんなに迷惑かけたんだから"



hi "『迷惑』だなんて言うなよ"


show mishashort sign_confused
with charachange


mi "そうだね～、そうだね～"


hi "静音に謝ったりするなよ"

show mishashort hips_smile
with charachange


mi "あはは～。そうだね～、そうだね～。でもそのためにここに来たんじゃないよ、ひっちゃん。しっちゃんには謝らないね。せっかくここにいるから、聞きたいことがあるの"

show mishashort perky_confused
with charachange


mi "ひっちゃん、何をどうすればしっちゃんは幸せな気持ちになると思う？"



hi "そんなの世界征服に決まってるだろ"

show mishashort cross_laugh
with charachange


mi "わはは～！"

show mishashort hips_smile
with charachange


mi "冗談だとしても、ひっちゃん……ううん、世界征服できたとしても、しっちゃんは幸せにならないと思うよ。なってもほんの一瞬だけ"

show mishashort sign_smile
with charachange



mi "ひっちゃん、絵を描いたそばからビリビリに破いちゃうアーティストの話、聞いたことある？　そういう人って本当に世の中にいるんだよね～！"


show mishashort perky_smile
with charachange



mi "突然思い出したんだ。考えてみると、まるでしっちゃんみたい。しっちゃんが何かに挑戦してやり遂げると、それで身につけた腕前はもう意味がない、みたいになるの"




show mishashort perky_confused
with charachange


mi "どうしてだろうね～、永遠に続くものは何も作れないから、かな？"

show mishashort perky_sad
with charachange



mi "そのアーティストと同じだよ。後に残る芸術作品を～、しかもとってもすごいものを作りたいけど～、それができないっていう"
mi "後から考えるとすごく当たり前なんだけど～、でも～、今まではわからなかったんだ。今はわたし、怖くて。しっちゃんはもう幸せになれないんじゃないかって"



hi "いや、そうは思わない。あいつが幸せだったことがない、ってことじゃなくて。お前は間違ってると思う。静音は実際、俺が思ってたよりもしょっちゅう幸せな気分になってるぞ"


hi "実際、すごいことだと思うよ。普通の人は中年とか死ぬ間際にならないとそんなこと考えないからな。そしたら『何かを後に残したい』とか『みんなの記憶に残りたい』って考え出すんだ"


"俺みたいに。"


"俺はちょっと先を飛ばしただけだけど。俺の人生は短かった。心臓発作の後は、余計に短くなったように思える。"



"自分が後に残すものについて、俺は考えていなかった。ざっと思いついた限り、残すものなんてほとんどなかったからだ。残ったのは自業自得の苦しみだけだ。"





hi "もう静音はどこかに自分の存在を残したいって思ってるんだ。ただし、人を助けることでそうしたいと思ってる。だからあいつにとってお祝いが大切なんだ。慈善家になりたいとまで思ってるんだぜ"


hi "一番いい生き方だと思うな。他の人に与えることで生き続けるっていうのは。それがわがままな理由だったとしても、それでもいいさ"


hi "静音はもう幸せなんだよ。だって何かがうまくいけば、かならずそれを見て記憶にとどめる人がいるんだから。そのことがあいつを幸せにするんだ"


"ミーシャはため息をつく。腕は体の側でこわばり、手はそっと空を叩いている。"




show mishashort sign_sad
with charachange


mi "前はさ、まだ……う～ん……しっちゃんを幸せにできるかもって、そうできる立場にいるって、そう思ってたんだ。わたしはしっちゃんの通訳だったから、いつでも側にいられたし。たぶん……"



show mishashort perky_confused
with charachange


mi "それで～、そうしようと思ったの……しっちゃんの影になることで"

show mishashort perky_sad
with charachange



mi "ふられた後も、ずっと続けたんだ"
mi "身動きができなくなって、しっちゃんがどんどん先に進んで、背中が小さくなっていくのを見ることしかできない、そんな気持ちになった。受け入れなきゃいけなかったんだけど、それでも怖かったの"




mi "つらいよ。しっちゃんを理解することはできたかもしれないのに～"




show mishashort cross_smile
with charachange


mi "でも、結局わたしがまるっきり間違ってたみたいだね～……全然わかってなかった、考えたこともなかった……しっちゃんなら完敗って言うだろうな"

show mishashort cross_frown
with charachange


mi "おっけ～、おわり。おしまいだよ、ひっちゃん～。でも～！　しっちゃんを一番よく知ってる人なんだから、しっちゃんを泣かせたらだめだよ。さもないと怒るからね～！"

show mishashort hips_smile
with charachange


mi "卒業したら海外に行くんだ。推薦状ももらったんだよ。でなければ普通だったら海外なんて行けないと思うよ～！　あっちで勉強して手話の先生になるかも？　どうだろうね～！"

show mishashort hips_grin
with charachange


mi "つまり～！　ひっちゃんがしっちゃんの面倒を見るの。いい？"

stop music fadeout 8.0


"ミーシャの笑顔は本当に心からのものだ。でも明らかにミーシャは変わった。そのまなざしはずっと思慮深い女の子のものだ。困難が英知を生む、というのは本当みたいだ。静音の視線を思い起こさせる。"



"静音はああいう性格になるのにどんな経験を積み重ねたんだろう。想像することはできる。最初からああだったのかもしれない。静音に会いたい気持ちがどんどん強まり、いっしょに探しに行こうとミーシャを誘う。"



"もちろん、それは友達ともっと過ごすための口実だ。いつもの生徒会の仕事で最後に三人一緒に過ごしたときから大して日が経っていないのに、おかしなことだ。でもずっと昔のような感じがする。"


"将来のことを考えていると、過去のことにそういうレンズが被さったような感じになる。"


"レンズと言えば……"

scene bg school_courtyard at bgleft
show yuuko neutral_up at center
with locationskip

play music music_ease fadein 8.0



"外では優子さんが所在なげに立っていて、小さくて新しそうなカメラを手でいじっている。メタリックな表面に太陽の光が反射しなければ気づかなかっただろう。"
"ミーシャが優子さんを呼ぶ。俺たち静音を探してたんじゃなかったのか。"


show yuuko neutral_up at tworight
show bg school_courtyard at center
with charamove

show mishashort hips_grin at twoleft
with charaenter


mi "こんちは～、こんちは～！"

show mishashort cross_smile
with charachange


mi "なにしてるの～？"

show yuuko closedhappy_down
with charachange


yu "みんなの写真を撮ってるだけよ"

show mishashort hips_grin
with charachange


mi "見れば分かるよ～！"




"気まずいなあ。ミーシャ、山ほど秘密を持っている人でも、圧倒的に気遣い不足でいられるって思い知らせてくれたこと、絶対忘れないぞ。"






hi "俺の写真はありますか？"


show yuuko worried_up
with charachange


yu "あ、あなたも一枚欲しいの？　その……どうしよう。まあ……誰にも言わないって約束してね、でないとみんな欲しがっちゃうから"

show mishashort cross_smile
with charachange


mi "わたしも小学校の時、そういうことあったよ、そのときはアメだったけどね～！"

show yuuko smile_up
with charachange


yu "オーケー……じゃあ今から写真撮るね……"




hi "あっ、待って、まだ準備できてないです。冗談ですよ"

show mishashort sign_smile
with charachange


mi "ひっちゃん、ピースしてよ～！"


hi "俺はそういうことはしないの"

play sound sfx_camera
with cameraflash


"カメラのフラッシュが閃き、目がくらむ。"

show mishashort perky_confused
show yuuko worried_down
with charachange


"優子さんが目を覆い、いらだったようなうめき声を上げる。屋外ではフラッシュ炊かなくてもいいのに。"

show yuuko invis at right
with dissolvecharamove


"優子さんはしなくてもいいのに謝りだして、静かにその場から抜け出そうとする。"


hi "あっ、待って"

show yuuko worried_up at tworight
with dissolvecharamove


yu "なに？"

show mishashort sign_smile
with charachange


mi "この辺でしっちゃん見なかった～？"

show yuuko neutral_up
with charachange


yu "うん……門の前で"


hi "どうも"


"ミーシャを追いかける寸前、かろうじて口に出す。"

play ambient sfx_crowd_outdoors fadein 3.0

scene bg school_gate
show crowd at center
show shizu behind_blank at center
with locationskip


"幸い、ミーシャの追跡はすぐに終わる。ここから門までは一分もかからない。俺にとってはきついこともある距離だけど。静音が新生徒会の連中と一緒にいるのが見える。静音にもお礼を言っているんだろう。"

$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

show shizu adjust_frown
with charachange

hide crowd
with charaexit


"俺たちを目にするが早いか、静音は周りの連中を追い払う。それ自体はたやすいことだった。みんな手話を理解したり使ったりできるとは思えないので、その場を離れてもあまり悲しまないだろうし。"


"逆にどうして手話が使える人と一緒にお礼をしに来ないのかが不思議だけど、こういうのは気持ちが大事だからな。"

show mishashort invis at twoleft behind shizu
with None

show mishashort hips_grin:
    xpos 0.36
show shizu adjust_blush
with Dissolvemove(0.4)

show bg school_gate at bgright
show mishashort perky_smile at twoleft
show shizu behind_smile at tworight
with dissolvecharamove



"ミーシャはすぐに静音をハグすると、静音の隣の門にもたれかかる。一方俺は少し身を引いて、二人が話をするに任せる。ミーシャはずっと静音と話をしたがってたし。俺は後でもいい。"




show bg school_gate at right
show shizu invis:
    xpos 0.4
show mishashort invis:
    xpos 0.0
with dissolvecharamove


"二人の会話を『盗み聞き』しないよう、二人から顔を背けることまでしてしまう。"



"おかげで時間が経つのを忘れていた。"



"時計を見ると、もう１０分も経っている。もう話は終わったのかと思い、後ろにいる二人を探そうと振り返る。"

show bg school_gate at bgright
show mishashort perky_smile at twoleft
show shizu behind_blank at tworight
with dissolvecharamove


ssh "何を考え事してるの？"


hi "話したくもない、つまんない哲学的な話。大丈夫、そんなに真剣に考えてるわけじゃないから"

show shizu adjust_smug
with charachange


ssh "よかった。こんな時にわざわざ哲学的になるなんて最悪よ"


hi "ああ。ちょっとここで突っ立っていたかったんだ。リラックスできるし"

show mishashort hips_grin
with charachange


mi "わはは～！　今週は～いそがしかったね"


hi "いや、俺はそうでもなかった"

$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve


n "\n\n\n\nこの二人が忙しかっただろうっていうのはわかってる。でも俺はもう自分のやりたいことを見いだした。それに気づいたときも、特に興奮や不安は感じなかった。"


n "その逆だ。ずいぶん久しぶりに、俺は穏やかな気持ちになっている。その感覚をもう少しの間味わっていたい。"


n "\nここで教師になりたい、と思う。"


n "\nそれに思い至ったとき、曲がりくねった長い道が頭の中に現れた。ここに戻ってくる、はっきりしない道だ。"

nvl clear


n "\n\n\n\n将来、俺みたいな誰かに会うことができるだろうか。苦しみに満ちあふれた誰かに。"


n "自分自身に話しかけることはできないから、俺はその人に話しかけたい。人生は短すぎると伝えたい。俺がそれを教わることはなかった。見せつけられることしかできなかった。同情したりせずにそうしたい。"





n "俺が同情されていたら、俺はもう少しだけ枯れていたに違いない。最初の週のことを思うと、今でもそれがどれほど順調だったかを考えてしまう。それは優しさの結果としか呼べないくらい順調すぎた。他の人たちに同じ優しさを見せてあげたい。"



n "\nそれと、静音を追いかけ続けたい。"

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

nvl hide dissolve
nvl clear

show mishashort perky_smile
with charachange

window show


mi "新生徒会の子達、なんて言ってたの、しっちゃん～？"


"ミーシャの声と付き合っていると、空想にふけるのは難しい。"


hi "手話ができるやつがいるとは知らなかったけどな"

show shizu behind_smile
with charachange


ssh "いないわ。たぶん、ただのお別れの挨拶だと思う。だから感謝したの。あの子達には伝えられなかったけど"

show shizu basic_normal
with charachange


ssh "どうして私がここにいるって分かったの？"



hi "それって秘密だったのか？　とにかく、優子さんに聞いただけだよ。優子さん、お前の写真も撮ったのか？"


show shizu behind_blank
with charachange



ssh "ええ、私に撮ってもいいか聞く前にね。でも優子さんがその場の勢いで何かするのは珍しいから、何も言わなかったけど"




play sound sfx_snap
show shizu basic_sparkle
with charachange


"静音が指を鳴らす。何かにひらめいたというより、たぶんやりたくてやったんだろうと思う。"

show shizu behind_smile
with charachange


ssh "私たち三人の写真を撮らなきゃ"


show shizu adjust_happy
with charachange



ssh "まだ生徒会の写真を撮ってないもの。今が絶好のチャンスよ"


show shizu basic_normal
with charachange


ssh "でも、この写真を一年後に見たとき、自分をにらみ返してるっていうのは嫌ね"


mi "ん～？　それどういうこと、しっちゃん？"

show shizu adjust_frown
with charachange


ssh "写真はその瞬間をとらえるものよ、そうでしょう？　間違いないわ。肖像画とは違う。ただ立ってるだけなんて堅苦しいわ。そんなんじゃ私の今の気持ちもとらえられない"

show shizu behind_smile
with charachange


ssh "私たち、また会える気がするの。だから今はそんなに改まった写真を撮る時じゃない。『また会おうね』って感じの写真じゃないと。大したことじゃなくて。もっと……お祝いみたいであるべきよ"


hi "なんてこった"

show shizu basic_happy
with charachange


ssh "こんな感じ。私に続いて"

show shizu adjust_smug
with charachange

show shizu behind_smile
with charachange


"静音は銃士のようなポーズを取る。あまりに素早いので、静音だってばかばかしいと思ってるに違いない。"

show mishashort cross_laugh
with charachange


mi "あははは～！"


hi "マジでその……ダサいポーズしないといけないのか？"




show shizu adjust_happy
with charachange


ssh "これ以上いいポーズなんて思いつかないわ。ミーシャ、優子さんを探してきて！"

show mishashort sign_smile
with charachange


mi "わたしもこのポーズ好きじゃないけど、なんだかいいと思うよ～"


hi "そんなのわけがわからないぞ"

show mishashort invis:
    xpos 0.0
with dissolvecharamove


"ミーシャはもう行ってしまい、優子さんを引っ張って戻ってくる。"

show yuuko invis:
    center
    xpos -0.2
with None

show bg school_gate at left
show shizu behind_smile_close:
    xpos 0.83
show mishashort hips_grin at center
show yuuko neutral_up at left
with dissolvecharamove


"フラッシュはオフだ。優子さんがボタンを押してから、赤いＬＥＤが三回点滅する。タイミングをしっかり合わせるように、静音は俺たち二人をちらりと見る。息を合わせる。みんなでジャンプする。"



play sound sfx_camera
$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

scene ev shizu_goodend
with cameraflashlong


ssh "今のはばっちりね"


ssh "オーケー……"


mi "じゃあ、優子さんも一緒に撮ろうよ～！"


yu "だ、だめよ、お願い……"


hi "そういうのはナシですよ"




"俺もこの写真が一枚欲しい。"

show ev shizu_goodend_pan
with None



"俺はたぶん普通の人よりは早く死ぬだろう。いつ自分の命が燃え尽きるかわからない。だったら無駄にできる時間なんてない。できる限り生き続けたい。そして、俺が成し遂げたことで他の人が笑ってくれるのを見たい。"



"他人の幸せを代償として生き続けるのは悪くなさそうだ。他人の幸せを通して喜びを覚えるのは悪い話じゃない。俺自身の人生を生きる道としては一番簡単そうだし、際だつだろうと思う。"


"静音が自分自身に見いだした意味というのはこれなのかもな。あくまで俺の想像だけど。生きてる間に自分がひとりぼっちで、目標を見失ってることに気づくのはよくあることだ。"


"ただし、幸せな瞬間に逃げ込むことはできる。それは鉄道の地図にある駅のように人生に印をつけることもある。あるいは長い旅路の途中に置かれた、記憶の中継点のように。"



"考えてみると、こうした個々の瞬間は、人生に充足感を与えられるのだろう。友達全員、お祭り、楽しい集まり。そして楽しい別れ。"



"俺が正しいのかどうか、静音に尋ねられるようになりたい。今自分が持っている時間を静音と過ごしたい。最後に、静音が自分自身のために笑えるようになってほしい。"

$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

scene bg school_gate at left

show mishashort perky_smile at twoleft 
show shizu behind_smile_close at tworight 


with locationchange


hi "愛してる"


"俺は言葉を切る。静音が困惑して俺を見て、どうして突然そんなことを言うのかと聞き返されるだろうかと思いながら。でも静音は聞かない。"


hi "この学校じゃ同窓会ってやるのか？"

show shizu adjust_happy_close
with charachange


ssh "もちろんよ"

show mishashort sign_smile
with charachange


mi "生徒会のメンバーなら知ってなきゃダメだよ～！"

show shizu behind_smile_close
with charachange


ssh "でもそれよりは前に、ね？"

show shizu adjust_happy_close
with charachange


ssh "二人ともよ"

show mishashort hips_grin
with charachange


mi "そうだね～！"


hi "ああ"

show shizu basic_happy_close
with charachange


ssh "優子さん！　一緒にポーズとって！"

show shizu adjust_happy_close
with charachange


ssh "終わったらお茶しに行きましょ"



"静音が笑う。この世に心配事などないかのように。まるでそれが自分の声であるかのように、ミーシャもやすやすとその笑い声に加わる。俺たちはきっとまた会える。"


stop ambient fadeout 2.0
stop music fadeout 2.0







label jp_S38:

play music music_pearly

scene bg school_scienceroom
with locationchange


"翌日、ミーシャは教室に姿を見せる。まだかなり気落ちしているようだけど。魔法のように機嫌を直してくれることを期待していたわけじゃない。昨日の出来事を考えれば、不可能を求めるようなものだ。"


"今度は静音が教室にいない。片方が出席すると突然もう片方がいなくなるというのに笑いそうになる。でも決して笑い事じゃない。というか、そのおかげで授業に集中することができない自分に気づく。"




"単に体調が悪いだけかもしれない。それともただのさぼりか。もっと深刻なことかもしれない。ミーシャに知っているかどうか聞いてみたくなるけど、結局何の行動も起こさない。"





"昨日、ミーシャが何か軽はずみなことをするんじゃないかと恐れて取った行動を、俺は後悔していない。"



play sound sfx_normalbell


"でも今では、ミーシャをそっとしておいてやるべきじゃないかと思っている。やがてベルが鳴り、ミーシャは他の生徒と一緒に昼ご飯を食べに行く。俺は人のいない教室で昼を食べることにする……でもここはいやだ。"




scene bg school_hallway3
with locationchange


"残念ながら、同じ気持ちでいる生徒は他にも大勢いて、落ち着けそうな無人の教室はそれほど多くない。もうあきらめかけたとき、廊下の端に暗い教室を見つける。"

scene bg school_miyagi
show lilly back_surprise:
    center
    ypos 1.15
with locationchange


"でも明かりをつけてみると、ここも無人ではなかったことに気づく。リリーの頭がこちらの方向を向き、俺はひどく驚くけど、多分スイッチを入れた音に気づいたんだろうと思い至る。"

show lilly basic_listen
with charachange


li "こんにちは"


hi "ああ、リリー。他に人がいるとは思わなかったよ"

show lilly basic_weaksmile
with charachange


li "久夫さんですか？"


hi "ああ、でももう気づいてると思ったよ"


"立ち去ろうと振り向くと、リリーが間髪入れずに口を開く。"

show lilly basic_smile
with charachange


li "そんなにすぐ出て行かなくてもいいんですよ。二人で同じ部屋でお昼を食べてもいいじゃありませんか。実は私、他の人と一緒に食べる方が好きなんです"



"どうして俺が昼飯を食べにここに来たって知っているのかと聞きたくなるけど、置いておく。ただの推測だろう。それに俺がすぐ感心するタイプだとは思われたくない。"




show lilly basic_smile_close:
    center
    ypos 1.1
with characlose



"リリーの前の席の椅子を後ろ向きにして座る。人間の意識は自分が認識しているものの大部分を、一度目にした光景や自分の予想で補っていると聞いたことがある。"






"それは効率のためだろう。個別に目に入るものをいちいち全部処理せずに済むように。"


"リリーはどんな物音がしても、立ち止まって不思議に思ったりすることはまずない。それはリリーの意識が毎回状況を補っているからなのか？　それともいちいち気にしたりせず、そういうものだと受け入れているのか？"


"リリーの机の上には、数枚のクッキーとお茶の入った水筒しかない。昼ご飯は軽く済ませる方なんだろう。俺はサンドイッチをかじる。具が後ろの方からこぼれ落ちる。"

show lilly basic_ara_close
with charachange


li "最後にお話ししてからかなり経っていますけど、私の名前はまだ覚えていたんですね。驚きました"


hi "ふぉうふぁい？"




show lilly basic_smileclosed_close
with charachange


li "生徒会はとても忙しいんでしょうね"


hi "週によって違うよ。すごく暇な週もあるし、病欠したくなる週もあるし"



"ちょっと待ってリリー、さっきのサンドイッチを飲み込んで一息つかないと。"


show lilly basic_smile_close
with charachange


li "最近はいかがですか？"


hi "予測不可能だね"

play sound sfx_snap

show lilly basic_oops_close
with vpunch


"俺は指を鳴らす。リリーの表情を見ると、大いに機嫌を損ねている。"

show lilly basic_reminisce_close
with charachange


li "久夫さんはあの二人と長く付き合いすぎていると思いますよ"


hi "静音のトレードマークの一つってところかな。俺は好きだよ"

show lilly basic_displeased_close
with charachange


li "私は無視しています"


"声の調子は少しも変わらないけど、リリーは明らかに気を悪くしている。"


hi "そうするのは簡単じゃなさそうだけどね。静音がどうやってあんなに大きな音を出せるのか、自分でも試してるんだけど、手を怪我しそうだよ"

show lilly behind_displeased_close
with charachange


li "窓が割れるほど大きな音でも、私は無視します。私は訓練されたアザラシじゃありませんから。そのくらいの余裕はあります"


hi "さっきのこと、まだ怒ってるのかな？"


"できる限り注意深く、そつのない尋ね方をする。でも結局は自分の好奇心を満たすために聞いているだけだ。"

show lilly basic_weaksmile_close
with charachange


li "いえ、そんなことはないです。静音のことは好きではないですけど"

show lilly basic_reminisce_close
with charachange


li "短い間ですけど、生徒会に一緒にいたことがあるんです"


hi "俺も聞いたよ"

show lilly basic_sleepy_close
with charachange



li "あんなにすぐ入会しなくてもよかったのに、と思います"




show lilly basic_listen_close
with charachange



li "静音の生徒会運営の仕方は、私は好きではありません。旧生徒会のメンバーを彼女が脅かして追い払ったって、知っていますか？　だから静音は自分に反対しない人を周りに置こうとしている、そう思うんです"


show lilly basic_reminisce_close
with charachange



li "実際、反対はありません。まるでお追従ですね"





"リリーの言っていることには、静音も気づいているだろう。何度か静音がはっきり否定していたのを覚えている。俺も毎回変だなと思っていた。"



"否定の仕方が具体的であればあるほど、その指摘は正しいという。今回の場合、俺はそうは思わない。静音の意見は決して客観的とは言えないからな。"




hi "静音には直接言ったの？"

show lilly basic_displeased_close
with charachange


li "いつも言っていますよ"


"リリーは言葉を切って紅茶を飲み干す。俺も食べるのが遅れていたので、その瞬間を利用してできる限り食べる。"

show lilly basic_sleepy_close
with charachange


li "静音の友人はみんな生徒会関係なんです。ミーシャのように"


li "静音とミーシャの仲が微妙なことになっていると聞きました。けんかをしたんですか？"


hi "そういうわけじゃないよ"

show lilly basic_surprised_close
with charachange


li "そうですか？"

show lilly basic_reminisce_close
with charachange



li "いずれにしても、無理矢理仲直りさせるのは無駄ですよ。いつも正面から立ち向かうのが静音のやり方ですけど、現実にはそれではうまくいきません。度が過ぎればそれは勇気や善意ではなく、ただ頑固なだけです"



hi "それは一般論だよね、そう思わない？"

show lilly basic_smileclosed_close
with charachange


li "まあ、そうかもしれませんね"



show lilly basic_weaksmile_close
with charachange



li "紅茶には何が一番合うと思いますか？　クッキー、それともスコーン？それぞれ違うけど、私はどちらも好きです。選ぶことなんてできません"


show lilly basic_displeased_close
with charachange


li "いつも私にどちらの味方につくのか選ぶよう強いる人、どんなことでも勝負にしてしまうような人は好きではありません"


li "生徒会に入ったとき、それは単にいろいろなことを円滑に進める手助けをする、人助けをする、それだけだと思っていました。クラス委員の時と同じように"

show lilly basic_reminisce_close
with charachange


li "実際には、静音が我が物顔で歩き回って、ミーシャを拡声器代わりにして、前の生徒会を越えるとか、もっとたくさんイベントをやるとか、イベントを大きくするとか、毎日そんなことばかり言っていました"



hi "でもリリーも静音も、目指してるものは同じだよ。そういういろんなものが物事を盛り上げるんだ"
hi "俺も最初は分からなかったけど、わがままで企画をしてるわけじゃない。花火も、そばの模擬店も、りんご飴も、おめかしする日も、それ以外もみんな好きなんだよ"



hi "生徒会が仕事をこなすほど、学校ももっと責任を与えてくれる。仕事は増えるけど、ある意味それは自由が増すことでもあるんだ"


hi "大きなお祭りを運営するだけの実力があれば、学校側もこいつらなら十分やりとげられるって思ってくれるよ。その場で却下するんじゃなくてね"






hi "それはとにかく、今では俺もそうしたいと思うんだ。確かに無駄な雑用はあるけど、最後にはその労力が報われる時が来る。俺にもやるべきことを与えてくれる。ただ学校に行って帰るだけじゃ、俺は爆発しちゃうよ"





show lilly basic_weaksmile_close
with charachange


li "私は、山久は他よりもおおらかな学校だと思うんです"


"山久は他の学校とは違うけどな。"




"俺は別の、なじみのある心理状態に陥りはじめる。ある意味では、山久はおおらかすぎるとも言えるだろう。"





"俺が今のような自分でなかったら、あまりのおおらかさに息苦しさを覚えただろう。でもここ以外の学校なら、そんな気楽さも正常な暮らしの一部でしかない。"





"でもここでの平穏さは作られたものだ。何かが違うと感じる。それは俺が普通の人間じゃないからなのだろう。"





"こめかみで血管が脈打つのを聞くたびに、そのことを思い出す。劣っている、弱っているという気分になり、苦しみはつのるばかりだ。"


hi "ああ、そうだね"


hi "何が言いたいかっていうと、今の俺にはその意味が分かる気がするんだ。リリーは静音につらく当たりすぎていると思うよ"

show lilly basic_sleepy_close
with charachange


li "そうかも知れませんけど、静音の個人個人への接し方を見ていると、あまり上手ではありませんね"


"残念だけど、そっちはちょっと反論しづらい。"

show lilly basic_smile_close
with charachange


li "時間、わかりますか？　授業の１０分前には教室に着いておきたくて"


hi "じゃあ、今出ればちょうどいい時間だよ"

show lilly invis_close at center
with dissolvecharamove

stop music fadeout 4.0


"挨拶をすると、リリーは部屋を去る。俺は座ったまま、リリーの杖が床を叩く音が、他の教室や廊下にいる生徒達の話し声に埋もれていくのを聞く。"


"疲れ切った俺は、静音と話したいと思っていたことも完全に忘れてしまう。"

scene black
with dissolve




label jp_S39:

scene bg school_hallway3
with locationchange


"翌日の放課後、俺は静音と話すため、すぐに生徒会室に向かう。"


"静音は授業には出ていたけど、ドアの近くや廊下で捕まえて話をするというのはちょっと邪魔になりそうだった。"

scene bg school_lobby
with locationchange


"生徒会室で落ち合うほうがいい。俺は途中の自販機で飲み物を買いつつ、ゆっくりと向かう。"


"それと、言いたいことを頭の中で練習する。大して重要なことじゃない。これからのイベントについていくつか聞きたいことがあるだけだ。"

scene bg school_council
with locationchange

play music music_rain fadein 8.0



"着いてみるとドアは鍵がかかっていない。机の上に乗っている静音のかばんと、その向こう側にのぞく本人の頭が見えなければ、室内も無人だと思っただろう。小さな砦を築いたかのようだ。"



show shizu basic_normal at center
with charaenter


"静音はかばんの向こうから手を振ると、指でそれを拾い上げて脇にどける。"


"でもその後は、すぐにペンで机をつつきながらチェックリストを凝視する作業に戻る。まるでそれに人生の意義が込められているかのように。"

show shizu adjust_frown
with charachange


ssh "どうかしたの？"


his "何か手伝えることがないかと思って。そこにあるものとか。あれはなんだ？"


"静音の横に積み重なった中くらいのフォルダーの束を指さすけど、静音は素っ気なく手を振る。"

show shizu behind_blank
with charachange


ssh "一人でできるから"


his "じゃあ選挙はどうなんだ？"


his "それとミーシャはどこだ？"

show shizu behind_sad
with charachange


shi "……"

show shizu basic_normal2
with charachange


ssh "問題なく進んでる。それと、ミーシャにはわたしが全部片づけるからって言っておいた"


his "どうして？"


"一切れの布の間に針が通っていくように、静音は手の中でゆっくりとペンを回し、それぞれの指の間を通していく。"

show shizu behind_blank
with charachange


ssh "別に"


his "本当に？"

show shizu adjust_frown
with charachange


ssh "別に"


"強調するように、そしてなにか裏があるのかという考えを封じるために、同じ手話を二度する。でもそこには何かがある。間違いなく今の静音の振る舞いは普通じゃない。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve



n "\n\n\n\n『何を黙ってるんだよ？』。とても冗談を言っている場合ではないけど、そんな言葉がすぐに頭に浮かぶ。今の俺の気持ちではある。俺たちは普通に会話をすることはできないから、そうできるわずかな手段だけでも俺にはありがたい。こんな風に拒絶されると傷つく。"







n "静音の事情がどうあれ、明らかに今日は静音と話すのは無理そうだ。意地っ張りを通り越して、静音は気落ちしているようだ。でも会話の流れがこうなってしまった今、その理由を聞き出すことはできそうにない。"



n "\nなぜか、そのせいで余計に理由が知りたくなる。つまりミーシャに聞かないといけないということだ。問題は、俺はミーシャが暇な時間に何をしているかを知らない。"


$ renpy.music.set_volume(1.0, 1.0, channel="music")
stop music fadeout 3.0

nvl hide dissolve
nvl clear

scene bg school_lobby
with shorttimeskip

window show


"明るいピンク色の髪の子を見かけなかったかと必要以上に多くの人に聞いて回り、思っていた以上に知らないと答えられた後、ようやくミーシャを見かけたという二人連れに巡り会う。"

scene bg school_cafeteria
show mishashort perky_smile at center
with locationchange

play music music_moonlight fadein 8.0


"それまでずっとミーシャがいたらしい食堂に着いた頃には、俺はもう学校全体をまるまる二周していて、疲れ果てている。ミーシャのそばを通り過ぎていたけど、柱の後ろにいたので見えなかったのだと気づく。"


hi "俺はお前を探すのが下手だけど、どうしてお前は俺を探すのが上手いんだ？"

show mishashort hips_smile
with charachange


mi "わたしのこと探してたの、ひっちゃん？"

show mishashort hips_grin
with charachange


mi "う～ん……知らないよ～？　ただの偶然じゃないかな"



hi "あのさ、そんなにしょっちゅう起きることは偶然とは言わないだろ"




show mishashort cross_laugh
with charachange


mi "ははは～"


hi "すごく遅い昼飯か？"

show mishashort sign_smile
with charachange


mi "お昼の時間に食べられなかったから、そうだね～！　でも～、あんまりたくさんじゃないよ、夕ご飯もちゃんと食べられるようにね"

show mishashort perky_smile
with charachange


mi "わたしと何か話したいことあったの、ひっちゃん？"


"俺はすぐに本題に入る。"


hi "ああ。ここに来た理由は……今日の静音がなんだか不機嫌そうなの、気づいたか？"

show mishashort perky_confused
with charachange


mi "わたしも同じこと聞きたかったんだよ、ひっちゃん～"

show mishashort perky_sad
with charachange


mi "ただ～、その、しっちゃんは何日か前からあんななんだ"


hi "そうか"

show mishashort sign_confused
with charachange


mi "ひっちゃん、わたしが何かしたせいだと思う？　前みたいに、わたしがしっちゃんを怒らせちゃったのかな？"


hi "いや。俺の方にもっと腹を立ててるみたいだし"




"嘘はついていない。本当にだ。でも残念だけど、ミーシャを安心させるという俺の試みはあまりうまくいっていない。ミーシャもミーシャなりに結構強情だ。"



scene bg school_dormhisao_ss
with locationskip


"結局俺は寮に戻ってしまう。ここ数日はイライラするようなことばかりが続いていて、おかげで俺は疲れ果てている。あまりにくたびれたので少し眠ることにする。それでいい案が思いつくことを願いながら。"

stop music fadeout 3.0

window hide

scene black
with shuteye

with Pause(1.0)
with shorttimeskip
with Pause(1.0)

scene bg school_dormhisao_ni
with openeye

window show

play music music_night fadein 1.0


"目覚めてみると、気分はよくなったけど、やっぱりいい考えは浮かばない。変わったことと言えば外が暗くなったことだけだ。"


"少し窓を開けると、外の天気がまだ快適だとわかる。夜の分の薬を水なしで飲み込むと、軽い散歩がてらに自動販売機に向かう。"

scene bg school_lobby_ni
with locationskip


"いつも買っている飲み物は全部売り切れだったので、何か品物が出てくるまで片っ端からボタンを叩いていく。"

scene bg school_courtyard_ni
with locationchange



"生徒会室も含めて、本校舎の明かりは消えている。特に意味のない観察だけど。"



play sound sfx_rustling



"一人で考えていると、背後で物音が聞こえる。そんな映画を見た覚えがある。一人きりで夜中に聞こえる音としてはとても不吉な音だ。"


show kenji happy_ni at center
with charaenter


"幸い、それは健二だった。妙に陽気な様子で茂みからふらりと姿を現す。"


ke "よう"



hi "なんなんだよ？　お前はいつも夜中に人のそばに忍び寄って気安く『よう』なんて言ってるのか？"


show kenji neutral_ni
with charachange



ke "いや、そんなの変だろ。お前だって分かってたからさ。夜目がすっげぇきくんだ。俺って超人だからかもな"





hi "じゃあここで何してるんだよ？"

show kenji tsun_ni
with charachange



ke "こっちも同じこと聞いたっていいんだぜ。{b}お前こそ{/b}ここで何してるんだ？"





"本当のことを言おうかと考えるけど、すぐに打ち消す。説明するには長すぎる話だ。"


hi "月に向かって吠えてるんだ"

show kenji neutral_ni
with charachange


ke "俺もそれやるぜ、時々。今夜は月は出てないけどな"


"俺はほとんど聞いてもいない。邪魔をされたのがちょっと腹が立つ。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve



n "\n\n俺は口先だけで、何も問題ないなんて白々しい嘘を静音についた。いや、正確には手で嘘をついた、か。それと全く同時に、まるで違うことをミーシャと話していた。"





n "もちろん、あの会話は静音を怒らせるだろう。でもあいつに聞こえるはずがない。普段は自分の考えを全部手話にするミーシャの手も、あのときは全く動いていなかった。そうでなかったとしても、俺が正面に立っていて、静音には見えなくなっていたはずだ。"


n "静音があの会話を盗み聞きできる唯一の手段があるとすれば、読唇術しかない。俺が手話の授業を取ったとき、最初に聞いたのが読唇術のことだった。あくまで興味本位でだったけど。簡単ではないし、完全でもない……だから今まで一度も考えつかなかった。"


n "\nつじつまは合う。唇を読むときに読み間違える可能性はあるけど、何の足しにもなりはしない。"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show



ke "……で、夜の闇に紛れて牛乳を買いに行けると気づいたわけだ。普段は雨の時か、自転車乗りや旅行者の群れに隠れられるときしか外出しないからな。こっちの方がよほど筋が通ってる"
ke "……今じゃ牛乳買うのに金をかけすぎてるけどな"


show kenji happy_ni
with charachange



ke "お前なんか落ち込んでるか、元気ないみたいだな。あんまり考えすぎるなよ、男ってのは行動が全てだからな！　一日中考え続けてもいいけど、行動を起こして状況を変えるのが一番だぞ"




ke "俺なんかいつだって何も考えずに行動するからな。だから中学では『問題を多々引き起こす者』って呼ばれてたんだ。それがかっこいいって思ってた。インディアンの名前みたいだろ"




hi "今ちょっとそういう気分じゃないんだ"

show kenji neutral_ni
with charachange


ke "嫌なことでもあったか？"


hi "ああ、よくわかんないや。今はなんか気が散ってるんだよ"

stop music fadeout 7.0

hide kenji
with dissolve


"あまりに気が散っていて、健二が立ち去るまであいつのアドバイスが実は正しいということに気づかなかった。静音も同じような忠告をしただろう。でももうちゃんとした礼を言うには遅すぎる。"


"俺はこれ以上ないくらいに失礼な声で返事をしてしまっている。本当に最低な気分だ。"



"思い返せば、この数日間俺はやることなすこと全て後悔している。最悪なのは、くよくよ思い悩んで、そこから教訓を得る時間もなかった。その帰結はいずれ――今までもだけど――さらなる後悔を生むだけだ。"




scene black
with dissolve



label jp_S40:

play music music_dreamy fadein 2.0

scene bg school_dormhisao
with locationchange

play sound sfx_doorknock2


"翌朝、服を着ているとドアをノックする音が聞こえる。急いで残りの服を身につけて、その向こうに誰がいるのかと立ち止まって考えることもなくドアを開く。"

scene bg school_dormhallway
show shizu basic_normal
with locationchange


"静音がいる。"

show shizu behind_blank
with charachange


ssh "ミーシャから私のことを探してるって聞いたから"


"『おはよう』の挨拶もないことに少し傷つくけど、大したことじゃない。"


his "探してたけどな"

show shizu basic_normal2
with charachange


ssh "でも昨日は見つけたじゃない"


"静音の指が壁のひび割れをなぞる。努めて他人行儀な態度を保とうとしているかのようだ。"

show shizu adjust_smug
with charachange


ssh "まあ、そう簡単には見つからないつもりだったけどね、どうだった？"





his "別に"


show shizu behind_blank
with charachange


ssh "だからここに来たの。今日は話ができるわ。ただ……できれば別のところに行きたい"


his "授業はどうするんだ？"

show shizu adjust_smug
with charachange


ssh "いいの、いいの"

show shizu basic_normal2
with charachange


ssh "学校の周りを散歩しない？　本校舎以外の場所はどこも人がいなくなるし。もう一時間目のベルが鳴ってるはずよ"


"ちらりと自分の時計を見る。静音の言うとおりだ。"


his "わかった"

stop music fadeout 6.0

show shizu basic_angry
with charachange


shi "……"


his "何かあったのか？"

show shizu behind_blank
with charachange


ssh "どうして何かあったって思うの？"



his "見るからに機嫌悪そうだからさ。わかるんだよ"





his "そのことで話がしたかったんだ"

show shizu basic_normal2
with charachange


"俺が手話をする間に、静音が素早く指を鳴らす。"

show shizu behind_blank
with charachange


ssh "どうやら、私は自分が思っていたより気持ちが表に出やすいみたいね。とてもがんばって隠していたのに。私が今何を考えてるか、わかる？"




hide shizu
with charaexit


"俺は答えず、静音はドアに向かう。俺がついてくることを期待しているとわかる程度にゆっくりと。両手は背中で重ねられていて、その背中は今にもこちら側を向くかのように反っている。"




scene bg school_courtyard
with locationchange


"外に出ると、静音は正しかったことがわかる。校内は完全に人の気配がない。学校のこういう光景を見るのは初めてではないけど、なんだか気味が悪い。"

scene bg school_backexit at right
with locationchange



"静音はまるで俺がそこにいないかのように振る舞う。自動販売機を眺め、曲がりくねったゆるい坂道を進み、やがて本校舎の裏にたどり着く。"




show shizu invis_close at tworight
with None

show shizu basic_normal_close:
    ypos 1.05
with dissolvecharamove


"ようやく、静音は壁により掛かって俺に向き合う。でも俺は会話の始め方を忘れてしまったみたいだ。"

play music music_sadness fadein 8.0

show shizu behind_blank_close
with charachange



ssh "こんな格言があるわ。『実際に失敗するまで、自分がどれだけひどい失敗をしていたかはわからない』"





his "誰の言葉だよ？"

show shizu basic_normal2_close
with charachange


ssh "私かもね"

show shizu basic_angry_close
with charachange


"自分の一連の思考を考え直して、静音はいらだったように手を振る。"

show shizu behind_blank_close
with charachange


ssh "ちょっと待って、言い方を変えるわ"

show shizu basic_normal_close
with charachange


ssh "私が小さかったとき、学校で『地球の日』のポスターを作ることになったの。私のクラスには学校で一番絵がうまいってみんなが思っている女の子がいた"

show shizu behind_blank_close
with charachange


ssh "それは他のみんなより絵を描くのがうまいからじゃなくて、一枚の絵にとてもたくさん描き込むことができるからだった"

show shizu adjust_frown_close
with charachange



ssh "私はその子よりもうまくなりたいって思った。だから一番いいポスターができあがるまで、何枚も何枚もポスターを描いたの。自分のポスターが最高で一番じゃなきゃだめだった"
ssh "結果として、みんな私のポスターを気に入ってくれた。先生だって"


show shizu basic_normal_close
with charachange


ssh "一週間たったら、そんなの何の意味もなかった。ポスターはゴミ箱に捨てたわ"

show shizu behind_blank_close
with charachange


ssh "前にもこんなことを言ったような気がする"


his "そうだな"

show shizu basic_angry_close
with charachange


ssh "何かが終わったって思ったとき、私は何もかも始めからやり直したいって思うの。成功したか失敗したかは関係ない。ミーシャにはいっぱい迷惑をかけたし、あなたまで引きずり込んでしまった"

show shizu adjust_frown_close
with charachange


ssh "こんなバカな状況を解決できた瞬間、そもそもこうなるのを防ぐことができたはずの瞬間を、何度も思い出してしまうの"

show shizu behind_sad_close
with charachange


ssh "最悪な気分だわ。正しいことを何一つできなくて、何もかも間違えたような気分の時には、なおさらよ。最近みたいに。最悪の失敗ね。自分があらゆる意味で出来損ないのような気がする"

show shizu basic_normal2_close
with charachange


ssh "自分がやったことを全部白紙に戻して、一人きりになりたい。私がやったことといえば、二年間もミーシャに迷惑をかけ続けただけ。そして自分勝手な理由であなたを引きずり回しただけよ"


his "別にいいよ"

show shizu adjust_frown_close
with charachange



ssh "よくないわ。あなたはわかってない。考えてたのよ。自分が何をするときでも、他人を打ち負かさないといけないような気がするって。他人どころか、あらゆる人を"
ssh "もしそうだとしたら、私と他の人との関係ってなんなの？　どっちもほとんど同じに思えるの"




"話の結末が見えたよ。"




show shizu behind_sad_close
with charachange


ssh "要は、私自身の身勝手のせいで、あまりにたくさんの人に迷惑をかけてしまったってことよ。だから今は他の人からしばらく距離を置きたいの"


his "俺ともか？"


"言葉が途切れる。"

show shizu basic_normal_close
with charachange


ssh "そうよ"


"さらに長い沈黙が続く。今度は俺の番だ。"


his "そうか"


his "それこそ一番自分勝手な行動じゃないか"




his "またお前が自分一人で決めてるだけだろ"

show shizu basic_normal2_close
with charachange


shi "……"


"その瞬間、静音は一番いい返事を考えているように見える。でも結局は単にうなずくだけだ。どっちにしても、それが一番いい答え方だろう。"


"とても静音らしい。こんな時でさえ回りくどいけど、最終的には言い訳なんてしない。"



"あらゆる感情が俺の中で爆発しそうだ。目の前にお湯の沸き立っているやかんが見える。あまりに近くて、手で触れることも、その発熱を感じることもできるくらいだ。"
"気分がそれたことに感謝する。もう頼れるものも交渉の余地もないとわかっているから。"


show shizu adjust_frown_close
with charachange


ssh "あなたは何も問題はないって言ったけど、でもそれは正しくなかった。そうでしょう？"

show shizu behind_sad_close
with charachange


ssh "だったら、もう二度と信じられない"


hi "わかった"

show bg school_backexit at center
show shizu invis_close:
    xpos 0.85
with dissolvecharamove


"わざわざ手話にすることもせず、俺は立ち上がる。両手はポケットの中で小銭をもてあそんでいる。朝の空気が顔に冷たい。"

scene ev shizu_badend:
    xalign 0.0 yalign 0.5 zoom 1.1 subpixel True
    acdc_warp 10.0 zoom 1.0
with locationchange



"静音を振り返ると、とても寂しそうに見える。自分のことを思い出す。俺もあんな表情をしていた。今の俺の顔もああなっているかもしれない。あれほど孤独な女の子のイメージは、永遠に俺の心から離れないだろう。"







"この状況を避けるか、解決することができたはずのすべての瞬間が頭に浮かぶ。その記憶に笑みが浮かぶけど、そこには何の喜びもない。"




stop music fadeout 4.0

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
