label jp_A19:

window hide None
scene black
with dissolve

play sound sfx_alarmclock
stop ambient

show bg school_dormhisao
with openeye

play music music_dreamy fadein 2.0

window show


"俺は目覚ましの音でうつろなまどろみから引きずりだされ、不愉快な気分で目を覚ます。"


"誰にともなく言い訳をしながら、しばらく布団にもぐったまま起きあがる気力を溜める。"


"正直なところ、丸一日ここにいろと言われてもかまわない。長期入院の後で学校に通うのは驚くほど疲れるし、思うに、カルチャーショックはまだ薄れていないんだろう。"


"この学校で授業をサボるのは簡単そうな印象だけど、そう楽はさせてくれないだろうとも思う。"


"それにナースだって運動のことで口やかましく言ってくるはずだ。"


"ようやく俺は起きあがり、朝の薬を飲んで、昔のサッカーユニフォームに着替える。"


"病気のおかげで俺は山久学園での体育の授業を免除されたので、体操着一式をもらえなかった。"


"こういう事態に備えていくつか注文してもいいけど、こうして昔のユニフォームを着ているのもこれはこれでなんだか懐かしい気分になる。"


"もうこれを着てサッカーをすることはできない。このユニフォームはジョギング用として新しい生を歩むのかもな。ちょっと俺みたいだ。"

label jp_A19a:




"何にせよ、自分で自分の体の面倒を見るなら、サボっている余裕はない。まずはランニングから始めるか。"


"ランニングは俺が心臓を強くするためにできる数少ない方法なのに加え、体の他の部分も快調に保ってくれる。"


"ひょっとしたら普通に近い生活へ戻れるかもしれない。少なくともいつの間にか倒れて死ぬなんて可能性は低くなるだろう。"

stop music fadeout 2.0


label jp_A19b:



"まったく、ちょっと馬鹿らしいとは思うが。"


"でもこうすれば、少なくともナースに俺は健康管理をしてるぞと正直に話せる。"


"そもそも俺は走るのがあまり得意じゃなかったけど。"


"やってみるのも悪くはないだろう。"

stop music fadeout 2.0


label jp_A19c:


show bg school_track
with locationskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_emijogging fadein 0.1


"運動場のトラックにいるのが自分だけじゃないことに驚いた。"


"しかも、以前に見たことのある顔だ。"


"昨日廊下で俺にぶつかってきた義足の少女が、半身機械のカモシカのように、競技用トラックをしなやかに走っている。"


"あの子の名前、何だったっけ？　短い名前だったけど、思い出せない。"


"義足でトラックの硬い地面にカタッとリズミカルに音を立てながら、彼女は大きなストライドでゆったりと走っているようだ。"


"なぜ彼女がこんな早朝から走ってるのか不思議に思う。俺と似たような理由かも知れない。俺がされてるように、ナースに走れと強要されているのかもしれない。かわいそうに。"


"ナースの勧めや、この病気さえなければ、俺はここにいなかったに違いない。"


"そもそもそんな仮定をしなくても、ただこれを早く終わらせたくてやってきただけだ。"


"誰にも見られずに健康のための惨めな努力ができるつもりだったけど、それは虫が良すぎたようだ。"


"俺はこの場から立ち去ろうとしたけど、かつての加害者が、最後の周回でこちらに気づいたみたいだ。"


"彼女は元気よく手を振って、こっちに駆け寄ってくる。"

show emi basic_grin_gym at Slide(0.7,0.5,0.5,0.5,1.0,_ease_in_time_warp)
with charaenter

stop ambient


emi_ "おはよう！　久夫くん、だよね？"

play music music_emi fadein 2.0


"にっこりと笑う。俺の名前を思い出せて喜んでいるようだ。"

show emi basic_closedgrin_gym at center
with charachange


emi_ "あたしのことは覚えてないかもしれないけど"

show emi basic_grin_gym
with charachange


emi_ "笑美だよ？　昨日廊下であなたにぶつかったんだよ"

label jp_A19i:

show emi excited_circle_gym
with charachange


emi "『い・ば・ら・ざ・き・さん？』"


"笑美は『静音の真似をするミーシャ』の真似をするが、あの陽気さを押し殺した感じを、彼女の高い声では再現しきれていない。"



label jp_A19j:


hi "あんな、ええと、乱暴な自己紹介を忘れるわけないだろ？"

show emi sad_shy_gym
with charachange


"笑美はけらけらと笑う前に、なんとなく申し訳なさそうな顔をするくらいの礼儀はわきまえている。"

show emi sad_grin_gym
with charachange


emi "そうそう、あの時は本当にごめんね"


hi "ん、そうだな、あれを癖にしないなら、俺はいいけど"

show emi basic_happy_gym
with charachange


emi "よかった！"


"俺が冗談を言ったことに気づいているのやら。"


hi "ってことはだ、ナースが言ってた『スパイ兼相談役』って……本当に君なのか？"

show emi basic_closedgrin_gym
with charachange


emi "そうだよ！"


hi "へぇ"


hi "正直、俺は看護スタッフの誰かかと思ってたぞ"

show emi basic_confused_gym
with charachange


emi "なぁに、あたしじゃスパイになんかなれそうにないっていうの？"


hi "違うって、むしろ安心したんだよ。俺、ひょっとしてナースが俺の行動を誰かに逐一監視させてるんじゃないかって心配だったからさ"


hi "君がそのためにここにいるっていうんじゃなければだけど"

show emi excited_laugh_gym
with charachange


emi "違うよ、あたしは自分なりに理由があってここに来てるの。ナースくんには『途方に暮れてるように見える髪の毛ボサボサの転校生』をトラックの近くで見かけなかったか、って聞かれただけ"


hi "じゃあ君はどうしてこんなところにいるんだ？"


"笑美は大げさなポーズをきめる。"

show emi basic_happy_gym
with charachange


emi "朝練だよ！"


hi "何の？"

show emi basic_closedhappy_gym
with charachange


emi "陸上の！"


hi "ああ、わかったよ。君、陸上部に所属してんだよな？"


"笑美は熱烈にうなずく。"

show emi excited_proud_gym
with charachange


emi "そうなの！　しかも、走るのは速いほうなんだよ！"


"おまけに謙虚でもある。"

show emi basic_grin_gym
with charachange


emi "ねえ、一緒に走ろうよ！"


emi "いい運動になるでしょ"


"そんなに激しい運動はたぶん論外だろう。"


hi "いやあ、俺は自分が走るの好きかどうかすらわからないんだ"


hi "それに本当に俺、みんなでスポーツとか苦手なんだよ"


"これは本当だ。俺はサッカーにすらたいして入れ込んだことがない。"


"そりゃ、昔は友達とかと走り回っていたけど、それはただ一緒に遊ぶためだった。"


"サッカー場で手に入れる栄光のためなんかじゃなかったことは確かだ。"


"笑美は俺の真意を理解しているようだ。"

show emi basic_confused_gym
with charachange


emi "うん、うん。グループでやるとかがそんなに好きじゃないのね"

show emi excited_proud_gym
with charachange


emi "でも今ここにいるってことは、一緒に走ろうかなって思ってんでしょ？"


hi "何だって？　あぁ、そうだよ。そう思ってるよ"


"笑美は嬉しそうだ。"

show emi excited_joy_gym
with charachange


emi "じゃあ準備運動でもする？"


hi "真の男は準備運動なんてしないんだ"

show emi basic_annoyed_gym
with charachange


emi "ダメだよ、準備運動ぐらいしなきゃ！　久夫くん悪い子だなぁ！"

show emi excited_proud_gym_close
with characlose


"笑美は猛烈に叱るけど、その後すぐに微笑んで、俺のほうへ身を乗り出す。"


emi "あたしも準備運動嫌いなの"

show emi excited_laugh_gym_close
with charachange


"笑美が突然笑い出す。"


emi "しかも、脚のストレッチなんて必要ないし！"

play sound sfx_gymbounce

show emi gymbounce
with charadistant


"まるで自分の言葉を確かめるように、笑美は飛んだり跳ねたりを繰り返す。一瞬まるで２本のバネの上に立っているかのように見えた。彼女の義足はなかなか弾力性があるようだ。"


emi "いこ！"

stop music fadeout 1.0

play ambient sfx_emijogging fadein 0.3

scene bg school_track_running
with locationchange


"一緒にトラックを駆け出すと、走るのは得意という笑美の言葉は嘘じゃなかったことがわかる。"


"笑美はまるで川の中に飛び込んだみたいに、流れるように気ままに走る。"


"俺は、もっとフォームに気をつけて走ろうとしている自分に気づく。"




label jp_A19d:


"手は広げるんだよな？"


"あと、かかとじゃなくて親指の付け根で着地とかなんとか……"


"俺は自分の歩幅を笑美に合わせようとするが、かなり難しい。"


"俺は走るのにはあまり向いてないようだ。"


"あとで笑美にアドバイスしてもらおう。"



label jp_A19e:




"正直にいうと、ランニングにこれというフォームがあるのかどうか思い出せないが、どうにも自分の走り方が間違っているように感じてしまう。"


"走りが乱れる様子が全くない笑美と比べてしまい、俺は無様な気分になる。"


"……"


"もうこれ以上続ける気になれない。"



label jp_A19f:


"俺は２、３周が限界だと感じ、すぐに速度を落として歩き始める。"

scene bg school_track_on
with Dissolve(4.0)


"笑美は走り続け、２回俺を抜き去ってようやく俺が足を止めていたことに気づいたようだ。"

stop ambient


"笑美は落ち着いた呼吸で、素早く横滑りして停止する。俺のどちらかといえばあえぐような呼吸とは対照的だ。"

play music music_emi fadein 2.0

show emi basic_confused_gym at center
with charamoveinleft


emi "もうおしまい？"


"俺はしょんぼりと頭を下げる。"


hi "はぁ、まぁね"


hi "今はあまり調子よくない"

show emi basic_grin_gym
with charachange


"笑美は相槌を打つと、すぐにもう一度俺にニコッと笑う。"


"よく笑う子だな。"


emi "そうね、久夫くんが運動し始めたのが、一番大事なことなんだよ？"

show emi excited_amused_gym
with charachange


emi "次は、今のをもっと長く辛抱できるようになればいいんだよ。その次はもっと長く、その次はさらに長く、そしたらいつかすごくよくなるよ！"


hi "覚えとくよ"


hi "けど今は授業の準備をしないと"


hi "君は準備しなくていいの？"


"笑美は関係ないねというふうに肩をすくめる。"

show emi basic_grin_gym
with charachange


emi "いーえ、あたしは時間いっぱいあるもん"


"俺は、笑美が腕時計をしていないことに気づいた。"


hi "マジかよ？"


"無意識にまた肩をすくめる。"


emi "いっぱいってほどじゃないけど……朝練終わらせなきゃ！"

show emi basic_closedgrin_gym
with charachange


emi "じゃあまたね、久夫くん！"


hi "ああ、またな"

stop music fadeout 5.0
play ambient sfx_emisprinting

hide emi
with easeoutleft

stop ambient fadeout 2.0


label jp_A19g:



"今朝の運動が成功なのか失敗なのかはわからないけど、運動場に行ってみたのは少しは良かったと思う。それは認める。"


"で、笑美の言うように、ひたすら続けていけば走りもうまくなる、そうだよな？"


"継続は力なり、とかなんとか。"


"少なくとも、自分の体調管理みたいなものをできてる感覚ってのはいいものだ。"


"続けないとな。"

scene black
with locationskip_in

label jp_A19h:



"やる前より疲れただけで、今日は何も成してないなと思う。"


"あまりにも不健康すぎる自分が恥ずかしい。"


"すべてが時間の無駄だったかもしれない。他の方法を探すことにしよう。"

scene black
with locationskip_in




label jp_A20:

scene bg school_dormext_half
with locationskip_out


"汗を流すために寮に戻る。制服にも着替えないと。熱いシャワーを長々と浴びたいところだけど、我慢する。"


"さっきの運動がこたえているからゆっくりしたいけど、せっかく朝混雑する前に登校する習慣がつき始めているのを無駄にしたくない。"

scene bg school_dormbathroom
show steam
show steam2
with shorttimeskip


"結局長々とシャワーを浴びてしまった。体を拭いて、服を着るためにシャワールームの個室から出る。"

show kenji silhouette_naked at center behind steam
with charaenter


"と、湯けむりの中に突然影があらわれる。邪悪な意思をまき散らしながら、ゆらゆらと揺れている。その影が湯気の中から飛び出してくる。"

play music music_kenji fadein 0.3

hide steam
hide steam2
show kenji neutral_naked
show steam as newsteam behind kenji
show steam2 as newsteam2 behind kenji
with charachange


ke "どうした？"


hi "お前何してんだよ？　驚いただろ！　なんだってんだよ！？"

show kenji tsun_naked
with charachange


ke "こっちが聞きたいね。あちこち探してたんだぞ、まったく"


hi "『あちこち』ってどういう意味だ？"


"そのあからさまな猥褻物陳列罪で俺を探し回ってたのかと聞きたかったが、こらえる。"


"俺もまだ裸だったとようやく気づく。急いでシャツで隠すけど、健二はなにも気づいてないみたいだ。"


"あ、こいつの眼鏡曇ってる。というかなぜ拭かないんだ？　普段から視界に霧がかかってるぐらい目が悪いのか？"


ke "そりゃ、お前の部屋だろ、それから……あー、それだけだ。ていうか、俺だって起きなきゃいけなかったんだからな。まあそんなことはどうだっていい。金貸してくれるか？"

show kenji neutral_naked
with charachange


"健二は純朴そうな顔をつくって目を逸らし、懸命にさりげなく振る舞う。その甲斐もなく、健二の魂胆は簡単に見透かせた。お前がつけてる窓ガラスみたいにでかい眼鏡並だよ。"


"こうやって淡々と──それも裸で──話していると気まずい。"


"どうしたことか、裸なのが見えないやつの前で裸でいるのは余計に気まずいものらしい。もちろん健二も裸なんだけど。"


"この嫌な気分を振り落とそうとするけど、うまくいかない。"


hi "金？　もちろん"

show kenji happy_naked
hide newsteam
with charachange


ke "おお、助かる"


hi "待った、なんで金が必要なんだ？"

show kenji tsun_naked
with charachange


ke "えええ……"

show kenji neutral_naked
with charachange


ke "黙ってただ金を貸せないのか？　お前がシャワーを浴びてる間にポケットを漁る事もできたのにやめておいた俺の善意を買わないのか？"
ke "しようと思えばできたけど、俺は自制したんだぞ。それに結局、大事なのは気持ちだろ？　なあ、友達だろ"


"意味がわからない。大事なのは気持ちだっていうなら、金は渡さないほうがいいな。こいつの考えは明らかに不純だし、使い道も言えないってことはなおさら悪質な意図があるんだろう。そう健二に告げる。"

show kenji tsun_naked
with charachange


ke "ムカつくな。でもそっちがそのつもりなら仕方ない。いいだろう、答えてやる。ピザを注文したいんだ。代金のほとんどは既に用意してある。残りを払ってくれればいいんだ"


hi "俺もピザをもらえるんだな？"


ke "いいや"


hi "本気で言ってんの？"

show kenji neutral_naked
with charachange


ke "ああ。別にあげてもいいんだけどな、お前授業あるだろ。食べる時間ないよな"


hi "お前はどうなんだよ！？"


ke "俺は授業出ないし。ピザが届くの待って宅配の人に金払わないと。そして食す。簡単なことじゃないぞ。隠密にピザを入手しなくてはならない"
ke "そうしないと、みんなに姿を見られる。ピザも見られる。奴らは一切れよこせと言い出す"

show kenji tsun_naked
with charachange


ke "一歩外に出れば厳しい世界が広がってる。誰もが一切れ欲しがる。そしてこの容赦ない世界にピザなしで放り出されるんだ。前にそういう事があったからわかる"


ke "俺は毎日、復讐を計画してるんだよ。俺をないがしろにしたやつらがピザを頼んだら、その場にいられるように。油断はない！"


"健二は大袈裟なポーズを決める。やつは１００パー真剣だ。"

show kenji neutral_naked
with charachange


ke "だけどまあ、ほんの４００円ぐらいあればいいんだよ。頼む！　お前だけが頼りなんだ！　外に出てピザを買いに行くなんて無理なんだ、遠すぎて！"


ke "本当に必要なとき以外、外には行かないことにしてるんだ。聞いてくれ、前回俺が不用意に外に出かけたとき何があったかを"


ke "外に出かけてた。何をやってたかは覚えてない。何かしてた。立ってた？　どうやってそこにたどり着いたのか考えてたのかもしれない"

show kenji tsun_naked
with charachange


ke "そして、唐突にそれは起こったんだ"


ke "一陣の雷が空を裂くように、サンドイッチを食べやすく半分に裂くように、俺の頭に鳥がクソしやがったんだよ"


ke "人生で二番目に衝撃的な出来事だったな"


hi "一番目は？"


"健二は答えずに続ける。体を掴んで揺すってやりたい。話の勢いを保とうとしてるだけなのか？　まあそれならいい、ただ単に俺の話を聞いていないだけという可能性のほうが高そうだけど。"



ke "こう何かのアニメのオープニングみたいにほら、必ず主人公がライバルキャラと戦うシーンとかあって、お互いに飛びかかって剣がぶつかり合って、色のついたすげえオーラとか爆音とか出てさあ？"

show kenji neutral_naked
with charachange


ke "さっき言ったのもそんな感じ。まあフンでやっちまっただけで"


hi "そうか"

show kenji happy_naked
with charachange


ke "だからさ、金がいるんだよ。いいだろ？　見捨てないでくれよ、なあ。ほんの１０００円くらいなんだ"


hi "４００円だと思ったけど"


ke "いいよ"


hi "は？"


ke "借りたら返すよ、ほんとに"


hi "当たり前だ。人から物借りるっていうのはそういうことだぞ"

show kenji neutral_naked
with charachange


ke "いつ返せるかわからないけどね"


hi "１週間で返せ"

show kenji tsun_naked
with charachange


ke "あああああああああああああああああああああああああぁぁあ……"


"健二は顔をゆがませて、まるで死にゆく牛のような声を出す。その下でゆらゆら好き勝手に指揮を取っている健二の『指揮棒』に、心穏やかではいられない。"


ke "お前、戦友に向かってケチくさいこと言うんじゃねえよ。既に男側の状況は悪いんだ。ＡＶ男優はＡＶ女優の半分しか稼げないって知ってたか？"


hi "そんなのお前がＡＶ男優じゃなけりゃまったく関係ない話だろ"


ke "ＡＶ男優のバイトしてるかもしれないだろ！　フェミニストの陰謀と戦いながら生活費を稼ごうと奮闘してるかもしれない俺に、お前はパンくずすらあげられないのか。バカ野郎。誰もわかってくれない。誰もだ"


"そもそもフェミニストってポルノ作品には反対してなかったっけ？"


hi "またフェミニストの陰謀云々かよ？"


ke "これは大事なことなんだ。お前が気にも留めてないことは分かる。でもこれは真剣な話なんだ"
ke "フェミニスト……やつらは危険な敵だ。間違いないんだよ。甘く見てると、朝目を覚ました時には背中にナイフが刺さってるだろうな。ドスッ！　前触れもなく！"


hi "寝てる間に刺されてどうやって起きるんだよ？"

show kenji happy_naked
with charachange


ke "女が人をまともに刺せるわけないじゃん"


hi "お前、やつらを甘く見るなって言わなかったか"

show kenji neutral_naked
with charachange


ke "それはもっと重大事についての話だ。やつらは個人個人を見れば脅威じゃない。だがもし戦争みたいな事が起きたら、男とフェミニスト軍の大戦が起きたら、厄介なことになる"

show kenji tsun_naked
with charachange


ke "そしていつかはフェミニストどもが国際フェミニスト軍秘密総司令部から出てきて『覚悟しな、このマザーファッカーどもめ！』という日がやってくる"


hi "ばかげてるよ。そんな本部なんてないだろ。どこに隠すんだよ？　相当巨大な建物になるはずだけど、そんなの地球のどこにも隠せないだろ。女だけしかいないクソデカい建物なんてすぐに誰か気づくって"

show kenji happy_naked
with charachange


ke "誰が地球にあるって言った？"


"俺は健二から顔をそらし、鏡に向かって顔をしかめる練習をする。俺の気持ちがもっとも良く表せる表情を探すために。どうせこの距離なら健二には見えないしな。"


"つまりその間は、残念ながら健二はお構いなしに支離滅裂なことをわめき散らし続けるというわけだ。"

show kenji tsun_naked
with charachange


ke "ああ、戦争が起こっているんだ。知っている奴は少ないが、大きな戦争だ。いずれ手がつけられなくなって、全世界を巻き込むことになる"
ke "俺たちはどちら側につくか選ばなくてはならなくなる。立場を示さないといけなくなる。今まさに戦争は起きているんだ"


ke "想像してみろ、血にまみれた戦場を。終わりなき凄惨な争いを"


ke "俺も諦めかけたことがあった。戦争の原因が馬鹿らしく思えたとき……望みのない戦いに疲れ果てたとき……停電をフェミニストの急襲と勘違いしてもう終わりだと思ったとき……"


ke "だが俺は気づいてしまった。俺が諦めてしまえば、すべてが終わってしまうと。俺は『うおお』と叫び、本気を出さないといけないと悟った。俺は最後に残った正気の人間だから。これは義務だ"


hi "さぞかしひっどい結果になるだろうな。シャワールームで裸で俺にまくし立ててるやつに全てが託されているなんて"

show kenji neutral_naked
with charachange


ke "で、金は貸してくれるのか"


"健二は出口をふさいでいる。ずっと裸で寒くなってきたし、さっさと学校にも行きたい。仕方なく金を貸すと約束する。"

show kenji happy_naked
with charachange


ke "やった。助かったぜ。今度一緒にボウリング行こうな"


hi "ボウリング？"


ke "ああ、究極のスポーツだ。最高に男らしいスポーツでもある。女のボウラーなんてほとんどいないからな"


ke "ピンクのボウリングシャツとそれにぴったりの靴でいくか、それともパステルグリーンの花柄がいいかな？"


hi "ボウリング用の服なんてあるのか"

show kenji neutral_naked
with charachange


ke "あるかもしれない"


hi "なんにしてもちゃんと返せよな"


ke "物で返していいよな？"


"どういう意味か詳しく聞いてる時間がない。"


hi "知るかよ。学校行かないと。お前さ、邪魔になってるんだけど"

show kenji tsun_naked
with charachange


ke "ああ、悪いな。そりゃ俺も時間取らせたくないし、それに俺だってやる事がある。時は満ちた"


hi "何の時だよ？"

show kenji happy_naked
with charachange


ke "これ言うのが好きなんだよ"


ke "よし、本当にもう時間がきた"


hi "何の？"

show kenji tsun_naked
with charachange


ke "シャワー使う。出てけ"


hi "今出るところだろ！　てかどういう意味だよ？　ここ広いじゃねえか"


ke "だから？　俺は一人じゃないとダメ。圧迫感……"


hi "わかったよ。でも他のやつが入ってきたら？"


ke "……"


ke "何か考えるさ"


"練習しておいたしかめっ面を披露するけど、健二の眼鏡に映ったそれはバカっぽかった。当の健二は気づいてないのか見えてないのか……"
"ともかく俺は服を着て部屋へと急ぐ。起きてからとても長い時間が経っているような感じがする。"

stop music fadeout 2.0

scene bg school_dormhisao
with locationskip


"二度と取り戻せない時間だ。健二め……覚えてろよ。"


"でも今は、とにかく学校へ急がないと。"





label jp_A21:

scene bg school_scienceroom
with locationskip

play music music_normal fadein 2.0


"今日は教室に一番乗りなんだけど、ちょっと早すぎたかもしれない。とはいえ、ここに一人で座って２０分過ごすほうが、健二に同じ時間つきあうよりずっとマシだ。"


"体の疲労、苛立ち、退屈さが組み合わさって、とてもくたびれた気分になる。"


"一瞬だけ意識が途切れて、机に頭をぶつけて目を覚ます。今日はともかく、明日からこんなに早く来るのはやめようと額をさすりながら心に決める。"


"しばらくすると廊下からコツコツと音が聞こえてきて、リリーの背の高い姿が入り口に現れる。リリーはこのクラスじゃないから、何か用事があるんだろう。華子を探しているんだろうか。"


"リリーはドアの所で立ち止まって、招かれないと入ることができない吸血鬼のようにためらっている。その心細そうな姿に、声をかけようとする。"

"でも、結局リリーは自分から教室に入ってくる。入る前に、身なりを整えるのが大切な場面であるかのようにスカートとブラウスの襟を正してから。"


show lilly cane_concerned at left
with charamoveinleft


li "あの、すみません"


"静かな教室に、繊細で探るような声で呼びかける。目が見えない彼女にとって、沈黙は不安なものかもしれない。そう思い、声をかける。"


hi "おはよう、リリー"

show lilly cane_surprised at left
with charachange

show lilly cane_surprised at center
show bg school_scienceroom at bgright
with charamove


li "久夫さん？　おはようございます。いつ入ってきたんですか？"


"リリーが姿を見せてから、ずっと何も言わなかったことを疑っているのかもしれない。きっとそうだ。ここで下手な嘘をつくと、まずいことになる。"


hi "いやあ、ずっといたんだけどさ、今の今まで眠ってたんだ"

show lilly cane_listen
with charachange


li "そうなんですか。ひょっとして、今日、華ちゃんを見てませんか？"


hi "見てないなあ。華子が来るのはチャイムの直前……か後だと思うから。何か伝言でもある？"

show lilly cane_weaksmile
with charachange


li "いえ、大丈夫です。変な話ですけど、今は校舎に私たち二人しかいないような気がします。ここに来る途中、誰の声も聞こえませんでしたから"


hi "なら、今日早起きするんじゃなかったな"

show lilly cane_smile
with charachange


li "自分を責めてるんですか？　他の方もすべきことなんですから。時間を守るのは良いことですよ。私はそう思います"

show lilly cane_concerned
with charachange


li "今朝はとても忙しいんですよ。もうすぐ学園祭ですから、今日は催し物の登録とか、予算申請とか、すべての書類の締め切り日なんです"

show lilly cane_weaksmile
with charachange


li "みなさん、ぎりぎりになって必要な書類を仕上げているのかもしれませんね。だから今日はとても静かなんでしょう"

play sound sfx_doorslam

show lilly cane_surprised
with vpunch


mi "おはよ～！　おはよ～！"

show shizu behind_blank at offscreenright
show misha hips_grin at offscreenright
with None

show lilly cane_surprised at left
show misha hips_grin at center
show shizu behind_blank at right
show bg school_scienceroom at bgleft
with charamove

hide misha
show misha hips_grin behind shizu
with None


"ミーシャと静音が、タイミングを計ったかのごとく同時に部屋に飛び込んでくる。あまりに大きな声で叫ぶので、リリーは明らかにたじろいでいる。"

show misha hips_smile
with charachange


mi "おはよ、ひっちゃん～！"


hi "よお"

show shizu behind_smile
with charachange


shi "……"

show misha hips_grin
with charachange


mi "あっ見て、学級委員だよ～！　こんちは～！"

show lilly cane_smile
with charachange


"リリーが笑みを見せる。ミーシャ──静音かもしれない──の、『見て』という言い方がおかしいんだろう。"

show lilly cane_smile
with charachange


li "おはようございます"

show shizu adjust_smug
with charachange


shi "……"

show misha cross_smile
with charachange


mi "もちろんこのクラスのじゃないけどね、ね～？"

show lilly cane_weaksmile
with charachange


li "そうですね"


"その静音への返事には、この前、俺と初めて会った時よりも警戒の色が見える。きっと二人は相性が悪いんだろう。"


"それとも、リリーは静音がいるかどうかわからなくて、探っているんだろうか。自分が誰と話しているのか知るために。"


"リリーがわかるのは、ミーシャと話しているということだけ。でも、ミーシャと静音が二人で一人同然なのも知っているはずだ。実際に『話して』いるのは静音だと思っているかもしれない。"


"ったく、どれだけややこしいんだよ。俺はリリーを助けることにする。何よりも、これじゃ俺の気持ちが落ち着かない。"


hi "朝早いんだな、静音"

show shizu basic_angry
with charachange


shi "……"

show misha hips_frown
with charachange



mi "わたしたちより早かったくせに！"



"ミーシャは怒って頬を膨らませる。何で怒ってるんだ？　静音の代わりに感情まで感じとってるのか？"


"静音が俺の一言に腹を立てるのはそれほど変じゃない。確かに二人より早く来ていたわけだし、あんなことを言ったらどう誤解されてもしょうがない。"


"口調を聞いて意図を判断できない静音には、特に誤解されやすそうだ。"


"謝るべきか迷っているうちに、とっくに静音の話題は変わっていた。"

show shizu adjust_smug
with charachange


shi "……"

show misha hips_smile
with charachange


mi "学級委員～！　ちょうどよかった～！　お話があるの"

show shizu behind_frown
with charachange


shi "……"

show misha hips_grin
with charachange


mi "学園祭まであと３日よね？　他のクラスは全部、企画の予算申請書を提出してるのよ！　一年生だって！　あなただけ未提出よ～！"

show misha cross_laugh
with charachange


mi "わはは～！"

show lilly cane_surprised
with charachange


li "提出までにまだ時間はあるでしょう？　違いますか？"

stop music fadeout 2.0

show shizu cross_angry
with charachange


shi "……"

show misha cross_frown
with charachange


mi "今日よ！　締め切りは今日！　ずいぶん時間かかってるんじゃない？"
mi "私がやっていれば、必要な書類はとっくに全部集まってたはずなのに、誰かさんが～！　『締め切り延ばしてください、お願いします』なんて言うから～！"

show lilly cane_displeased
with charachange


li "ええ、確かにそう言いました。こんなに大がかりなことを計画するのは簡単じゃありません。これだけ複雑な仕事をクラス全員がこなすには、一週間では短すぎます"

show shizu adjust_angry
with charachange


shi "……"

show misha hips_frown
with charachange


mi "一つのクラスに予算配分するより大変なことがあるのよ。なんだかわかる？"


mi "全部のクラスに同じことをしてから、あとで個別にやり直すことよ～！　その仕事をするのはわたしなのよ！"


"ミーシャは腰に手を当てて大見得を切る。おおっと、役に入り込んでる。だけど、リリーは面白くないみたいだ。"


hi "おい、静音、お前ちょっとリリーに厳しくないか？　まだ丸一日あるんだからさ"

show lilly cane_weaksmile
with charachange


li "いいんです、久夫さん。大丈夫ですから"


"リリーは俺が味方していることに満足なようだ。でも、自分の面倒も見られないと思われているのでは、と葛藤しているようにも見える。"

show lilly cane_listen
with charachange


li "予算のことでしたら、私が忘れていたと思われるのは心外です。予算申請書が大事だということくらいわかっていますよ"

show shizu behind_frustrated
with charachange


shi "……"

show misha hips_grin
with charachange


mi "だったら～！　いますぐ提出してくれる？"


hi "静音、きっと今は持ってないよ"

show lilly cane_displeased
with charachange


li "今は手元にはありません。他の生徒さんにお願いしていますから。私のクラスのね"


"リリーが最後の一言を強調したことに驚く。静音とミーシャが俺を生徒会に引き込もうとしていると知っているのか？"


"噂が広まったんだろう。それでリリーは俺を静音への反撃のネタに使っているわけだ。これで収集がつけばいいけど……"

show shizu cross_angry
with charachange


shi "……"

show misha hips_frown
with charachange


mi "予算申請書を書くのはあなたの責任でしょう～！　他の人に丸投げしていいような仕事じゃないのよ！"
mi "全体の進捗を把握するのが学級委員の責務！　そうやってしかるべき手順を軽視するのって最悪です～！"

show lilly cane_listen
with charachange


li "その二人は書類作りくらいできますし、もう出来上がってます。でも最近体調を崩して学校を休んでいるので、私に渡すことができなかったんです"
li "お望みであれば、二人が体調を崩したことについては代わりにお詫びしますよ"

show misha hips_grin
with charachange


mi "おっけ～！"


"ミーシャにはリリーの軽い皮肉が全く通じていないけど、静音には伝わっている。リリーの大胆さに腹を立てるか、勝負を仕掛けられたことを喜ぶか、迷っているようだ。"

show shizu behind_frown
with charachange


shi "……"

show misha hips_smile
with charachange


mi "リリー、その生徒は寮にいるんじゃないの？　歩いて５分なんですけど～"


mi "自分たちのクラスの楽しみにかかわる大事な書類なんだから……いくら忙しくたって、持ってくるのにたったの５分もかけられない理由って何？"

show shizu adjust_angry
with charachange


"リリーは何か言おうと口を開くけど、静音が間髪いれずにすごい勢いで手話を始め、オーケストラの指揮者のように手を振り回している。"


"ミーシャはその熱意を伝えようとベストを尽くしているけど、いつもの陽気なトーンのままだ。おかげでちょっとシュールで面白いことになっている。"


shi "……"

show misha cross_frown
with charachange


mi "それに何なの、その態度は～？　丸投げしていいような仕事じゃないって言ったでしょう。あなた学級委員でしょ、違うの？"

show misha hips_frown
with charachange


mi "その二人の名前を教えて。こんな簡単なことも自分でできないんだったら、そっちがあなたの代わりに仕事をしたほうがいいわ"

show lilly cane_displeased
with charachange


li "私の仕事は書類一枚だけではありませんよ"


"リリーの口調がだんだん苛立ち始めているけど、静音に自分の不快感を見せないようによくやっている。手の内は見せないってことだ。"


"一方で、静音は機嫌よく眼鏡のふちに指を添えている。自分がどれくらい興奮しているか、リリーには聞くことも見ることもできないと分かっているんだ。"

show shizu adjust_smug
with charachange


shi "……"

show misha hips_grin
with charachange


mi "それはそうよね、お仕事多いもんね、学級委員さん～！　あなたにはとっても大変でしょうね～！"

show lilly cane_listen
with charachange


"ミーシャの口調からは、そこにあったはずの皮肉が全く伝わってこない。それでもリリーはその意図をはっきりと理解し、唇をきっと結ぶ。"


"静音とリリーが互いを気に入らないのはわかるけど、これはちょっとやりすぎだ。我慢の限界に達したらしいリリーが反撃に出る。"

play music music_tension

$ wdt_off(False)

scene black
with Dissolve(0.2)

show showdown_lilly_slice at Transform(xanchor=0.0, xpos=1.0, yalign=0.0)
show showdown_shizu_slice at Transform(xanchor=1.0, xpos=0.0, yalign=1.0)
with None

play sound sfx_draw
show showdown_lilly_slice at Transform(xalign=0.0, yalign=0.0)
with slice_in

with Pause(0.2)

play sound sfx_draw
show showdown_shizu_slice at Transform(xalign=1.0, yalign=1.0)
with slice_in

with Pause(0.2)

play sound sfx_thunder
scene ev showdown
with Fade(0.2, 0.0, 3.0, color="#FFF")


play sound sfx_slide2
show ev showdown_large:
    size (800,600) crop (0, 0, 2400, 1800) subpixel True
    easeout 0.2 crop (280, 100, 800, 600)
with None

window show



li "ちょうどあなたが来る前に、予算申請書の話をしてきたところですよ"
li "生徒会の仕事をあっと言う間に終わらせて、わざわざ私が仕事を忘れないように追い回す暇があるくらいですから、あなたはさぞかしご優秀なんでしょうね"

play sound sfx_slide
show ev showdown_large:
    ease 0.2 crop (1400,160, 800, 600)
with None


mi "わたしが怠けてるっていうの？　自分のことと間違えてるんじゃない～！？"

play sound sfx_slide2
show ev showdown_large:
    ease 0.2 crop (280,100, 800, 600)
with None


li "そんなことはありませんよ。あなたと私を比べるなんて、とてもできません"


play sound sfx_slide2
show ev showdown_large:
    ease 0.2 crop (1400,160, 800, 600)
with None


mi "本当、わたしたち二人は天国と地獄くらい違いますからね"

play sound sfx_slide
show ev showdown_large:
    ease 0.2 crop (280,100, 800, 600)
with None


li "あなたがそのどちらなのかは、想像に難くないですね"

$ _window = False

play sound sfx_thunder
scene ev showdown
with Fade(0.2, 0.0, 1.5, color="#FFF")

window show


"二人の間の空気が波立つ。いや、文字通りってわけではないけど。でもこれはもう隠しようもない。ミーシャでさえこの会話の意味に気づき始めている。"

stop music fadeout 5.0

scene bg school_scienceroom
show lilly cane_listen at left
show misha perky_confused at center
show shizu basic_angry at right
with flash


shi "……"

show misha sign_confused
with charachange


mi "ひっちゃん～！　あなたも怠けてるんじゃないの！"


hi "何の話だよ？"

show shizu basic_frown
with charachange


shi "……"

show misha hips_smile
with charachange


mi "ひっちゃんだって学園祭の手伝いをしてるんでしょう？　そうでしょ、違うの？　だったら～！　学園祭が滞りなく開けるように、こっちの人よりたくさん仕事してくれるんでしょうね～！"

label jp_choiceA21:
menu:
    with menueffect
    "何で静音は突然俺に怒りだしたんだ。"
    "俺を巻き込むなよ！　自分のやれることはやった！":




        return m1
    "なあ、頼むから。リリーを勘弁してやれよ……":


        return m2

label jp_A21a:


hi "なんでまたこんな事に巻き込まれるんだ？　俺は十分やったと思うぞ"


hi "リリーに怒ってるんだったら、俺には関係ないだろ"

show lilly cane_reminisce
with charachange


li "あの、ちょっと待ってください……生徒会長が私を叱責するのは良くて、自分に矛先が向かうのはおかしいとでも言うんですか？"


"しまった、今の言い方はまずかった。"


hi "いや、そうじゃなくてさ、ほら……ええっと、つまり……"

show shizu behind_frown
with charachange


shi "……"

show misha perky_confused
with charachange


mi "何を言ってるの、ひっちゃん？"


hi "お前のその言い方はフェアだと思えないってだけさ。俺だってお前達に協力したんだから"


"雰囲気が変わった。ガンマン同士の決闘みたいだ。まあ、さっきからそんな感じだけど。でも、今の静音の標的は俺だ。"


"それに、黙ってはいるけど、リリーの標的も変わった。そんなつもりじゃなかったのに、リリーを怒らせてしまったようだ。"

show shizu cross_angry
with charachange


shi "……"

show misha hips_frown
with charachange


mi "わたしが間違ってるっていうの？"


"一触即発だな。"


hi "お前と言い合うにはまだ早いよ……そうだ、お前が俺を責めるのはフェアじゃないと思う"

show shizu behind_frustrated
with charachange


shi "……"

show misha hips_smile
with charachange


mi "ひっちゃんは欲張りすぎ～！　でも～！　それももっともだね。おっけー、おっけおっけ～！　ひっちゃんはさぼってないね"

show misha hips_laugh
with charachange


mi "ははは～！"


"静音は満足そうにメガネを親指で押し上げる。"

show shizu adjust_happy
with charachange


shi "……"

show misha perky_smile
with charachange


mi "よろしい！　自分が役立たずじゃないなら、他の人にもそんなことを言わせちゃだめ～！"
mi "でも次にわたしがそう言うときは、ひっちゃんがわたしの期待を裏切ったってことだからね。この学級委員さんみたいに。だからあんまり調子に乗らないようにね！"

show lilly cane_displeased
with charachange


"リリーは敵意に満ちた顔つきを崩さず、黙って静音の皮肉に耐える。"

show misha hips_smile
with charachange


mi "学級委員～！　しっちゃんが『申請書は忘れないでください』だって～！"


li "忘れませんよ"

show lilly cane_listen
with charachange


li "お話はこれで終わりですか？"

show misha hips_grin
with charachange


mi "は～い！"


li "ではごきげんよう、みなさん"


"もしリリーの声が刃物だったら、教室の空気は真っ二つになっていただろう。"

hide lilly
with charaexit


"リリーが不機嫌なのも無理はない。それでも、いつも通りの落ち着きと穏やかさを保ったまま教室を出ていく。"

show misha hips_grin at twoleft
show shizu adjust_happy at tworight
show bg school_scienceroom at bgleft
with charamove


hi "静音、今日はちょっとやりすぎだぞ"

show misha perky_smile
with charachange


mi "そうだよ、しっちゃん。ちょっとだけ～"


"俺の言い分をいやいやでも認めるんじゃないかと期待していたけど、甘かったようだ。静音は答えない。"

show shizu basic_normal2
with charachange


shi "……"

show misha cross_laugh
with charachange


mi "ははは～！　しっちゃんは余計なお世話だって言ってるよ"

show misha hips_smile
with charachange


mi "ひっちゃん、授業の前にわたしたちやらなきゃいけないことがあるの～！　遅れちゃうかもしれないから～！　わたしたちのノートもお願いしていい？"


hi "ああ"

show misha cross_grin
with charachange


mi "最高～！　やったぁ～！　おっけ～！　ありがと、ひっちゃん！"

hide misha
hide shizu
with charaexit


"二人は外に出ていく。授業開始のベルが鳴るまであと１０分しかないのに。"



label jp_A21b:


hi "おい、俺は転校したばっかだってこと、憶えてるか？"


hi "いくら手伝いたくたって、大したことができるわけないだろ"

show lilly cane_displeased
with charachange


li "その通りです。転校生が一週目からすぐ仕事に取りかかれると思うのは間違っていますよ"


"リリーが味方をしてくれると、なんだか心強い。俺もリリーの肩を持つことにしよう。"


hi "そうだよ。俺たち両方に無茶を言ってるぞ、二人とも"

show shizu behind_frustrated
with charachange


shi "……"

show misha hips_frown
with charachange


mi "はいはい、言い訳言い訳。学級委員さんは今までいくらでも申請書を書く時間があったはずよ"


mi "それにひっちゃん、あなたはこっちから何度も生徒会の仕事をしないかって誘ったのに断ったわね。学園祭の成功に貢献するチャンスだったのに"


hi "あのさ、前も言ったけど、そんなことできるかどうか……"


"今はこんなことしてる場合じゃない。どうせ俺が何をしたって、静音との対立に引きずり込まれるだけだし、それが静音のねらいなんだ。"


hi "もういいよ。何でもない"


label jp_A21c:


"俺は彼女たちに背を向ける。"

hide shizu
hide misha
with charaexit

show lilly cane_displeased at center
show bg school_scienceroom at bgright
with charamove


hi "リリー、授業がもうすぐ始まるからまた後で話そう。リリーが探してたって華子に伝えとくよ"


"静音が固まるのが見なくてもわかる。たぶん、こんなあからさまに無視されたのは初めてなんだろう。"

show lilly cane_smile
with charachange


li "ありがとう、久夫さん。私、戻りますね"


"今まで見たことのない優しい笑顔を俺に向けると、リリーはきびすを返して教室を出ていく。"

hide lilly
with charaexit


"リリーが教室を出て行くと、静音の方に振り向くことを急にためらってしまう。"


"静音の視線を背中にジリジリと感じ、目を合わせることができない。きっとご立腹に違いない。"
"ミーシャが何か場を和ませることを言ってくれないかと期待してしまう。でも、それこそ期待のしすぎだ。"


"結局自分の席に戻り、静音が部屋からどかどかと出る足音を聞く。静音は授業の数分前まで戻ってこない。"



label jp_A21d:

hide shizu
hide misha
hide lilly
with charaexit


"俺は彼女たちに背を向ける。"


"自分の席に戻り、リリーと静音の山場を迎えた言い争いに耳を塞ぐ。"


"結局、俺に何も言わずにリリーは教室を出て行き、静音とミーシャの二人は席に着く。"


"静音の視線を背中にジリジリと感じる。あいつはたぶん俺に怒ってるんだろうけど、俺だって同じくらい静音に怒っているんだ。"


"何で俺が口げんかに巻き込まれないといけないんだよ。"





label jp_A22:

scene bg school_scienceroom at bgleft
with shorttimeskip

play music music_daily fadein 0.5


"華子は全く朝の授業に顔を出さない。教室の後ろに残された彼女の席は、からっぽで寂しく見える。"


"後で見かけたら、リリーが探していたって伝えないと。"


"今朝のあの出来事にくらべれば、授業はとても退屈だ。俺はだらだらと教科書のページをめくる。"


"授業の進む早さは毎日同じなので、先のページを読めば明日の授業の内容はだいたいわかる。"


"教室正面にかかった時計の音がうるさくてたまらない。先生はもう７分ほど一言も話していない。かわりに、延々と続く数式を教科書から黒板に丸写ししている。"


"チョークが黒板にぶつかる規則的な音が、時計の秒針の音に完全に同調しているような気がする。"

show misha cross_smile_close at offscreenleft
with None

show misha cross_smile_close at Transform(xpos=0.1, xanchor=0.5)
show bg school_scienceroom at center
with charamove


"暇つぶしにその数式をノートに取り始める。するとミーシャがいつの間にか俺の肩越しにのぞき込んできて、俺に覆い被さりそうになる。"


hi "何してるんだよ、お前？"


"ミーシャに聞こえるけど、周りの注目は引かない程度の、微妙な声の大きさを保とうとする。"

show misha cross_grin_close
with charachange

show misha cross_grin_close at twoleft
show bg school_scienceroom at bgright
with charamove


mi "ひっちゃんこそ、何してるの～？"


"ミーシャがいつものでかい声で話し始めるので、俺はパニックに陥る。目立たないようにしようと言う俺の努力は全くの無駄に終わったけど、それでもあわてて小声のまま返事をする。"


hi "ノート取ってるんだよ、お前こそ何だよ？　何でそんな大声出すんだよ？"

show misha perky_confused_close
with charachange


mi "なんだぁ～、そうなの？　でも、あれ全部教科書に載ってるのに……だから誰もノートなんて取ってないんだよ～！"


hi "んなことはわかってるよ、声がでかいっての！"

show misha hips_grin_close
with charachange


mi "なんでそんなに小声なの、ひっちゃん？　よく聞こえないんだけど"


"俺とミーシャのおしゃべりが気づかれていないか、周りを見渡してみる。明らかに気づかれてる。先生にまで。"

show shizu behind_smile at right
with charamoveinright


"静音が恥ずかしげな笑顔を浮かべている。まさか、ミーシャがこんなまねをしてるのはあいつの差し金じゃないだろうな。"


"さっきのリリーとの出来事があったからか？"


"俺は中立を保って自分の筋を通しただけなのに、こんな目に会わなきゃいけないのか？　静音はあまりに高慢すぎる。もっとも、それくらいとっくにわかっているべきことだけど。"


hi "どうしてこんな真似するんだよ？"

show misha perky_confused_close
with charachange


mi "へ？"


"先生が俺たちに向けるとげとげしい視線を気にもせず、ミーシャは指一本で教科書を持ち上げるのに夢中になっている。"
"やばいことになりそうな気配が一瞬漂ったが、先生は無言でそっぽを向く。わざわざ面倒を起こすまでもない、とでも言うように。"


"ありがたいことだ。安堵した俺はいすにもたれかかる。"

scene bg school_scienceroom at bgright
with shorttimeskip


"その日の残りの授業は何事もなく過ぎていき、俺はそうして過ごせることに感謝する。"

play sound sfx_normalbell


"ベルが鳴るけど、特に急いでいるわけではないので、俺はしばらく教室に残ってその日の授業内容を復習する。もともと最後に教室を出るのが好きだった。そのほうが廊下の人混みを避けられるし。"


"静音とミーシャも残っているのに気づく。他のクラスの誰かと話しているようだ。"


"静音の手話があまりに早いので、手を動かす際に剣で空気を切っているような音がする。"


"ミーシャが必死に追いつこうとしているけど、理解するだけでも精一杯なのが見ていてもわかる。"


"俺はうなだれる。何を話しているのか知らないけど、真剣な話みたいだ。俺なんかには理解できないような。"
"それだけじゃなく、静音は怒っているように見える。いつもの気性の激しさのせいでそう見えるだけかもしれないけど。"


"手話の勢いが激しすぎて、静音の手首がぱきんと鳴る。ミーシャはそれを言葉にして伝えようと悪戦苦闘している。"


"ときどき、早口言葉を噛んだときのように言い間違える。その上、他の女子の話も静音に訳さないといけない。"


"大変そうだなあ。"


"見るからにミーシャは疲れている。今にも倒れそうだ。"


"幸いなことに話はすぐに終わり、静音とミーシャはまた自分の席に戻る。"

show shizu behind_blank at tworight
show misha perky_sad at twoleft
with charaenter


mi "うわああぁ！　つかれたよー！"


"ミーシャは疲れきった様子で、ぐったりと机に突っ伏す。"


hi "学園祭の準備、大変なんだな"


"確かに、この学校の生徒たちは学園祭にとても真剣に取り組んでいるようだ。授業の合間にその辺をぶらついている生徒を見ても、いつも自分の関わっている企画の話をしている。"


"みんながこれだけ熱心になっているというのはすごいな、と思う。"


"何もやることがない、というのはたぶん俺だけだろう。"

show shizu basic_normal
show misha perky_confused
with charachange


"静音が俺に手話し始める。ミーシャはそれを見て起きあがり、静音の手を少し焦点のぼけた目で追う。"

show shizu behind_frown
with charachange


shi "……"


"厳しく、重々しく、芝居ががった調子で静音は手を動かす。"


"ミーシャがその手話を言葉に訳してくれる。"


"ミーシャの訳し方は本当にうまい。静音が実際にしゃべっていて、考えていることを直接ミーシャを通じて伝えているかのようだ。"

show misha cross_frown
with charachange


mi "まあ、わたしたちは生徒会なわけですから。結構忙しいのよ"


hi "皮肉か？"

show misha perky_confused
with charachange


mi "へ？"


"静音の動き方を見ていると、軽蔑したように『話して』いる気がする。でもミーシャは普通に通訳するので、その言葉の裏の意図が何であれ、ミーシャの陽気な調子に置き変わってしまう。"
"今でもこれは混乱する。たぶん一生慣れることはないんじゃないか、と思う。"


hi "なんでもない"


hi "一日に最低２回は、お前らが生徒会に入れって勧誘してくるんだから。忘れるわけないだろ"

show misha cross_laugh
with charachange


mi "ははは～！　でもね、ひっちゃん、仕事は確かに多すぎるのよ"

show shizu basic_normal2
with charachange

show misha perky_sad
with charachange


mi "生徒のみんなが生徒会にもっと協力するとか、学園祭に向けてすごくがんばってる人たちに少しは感謝するとか、してくれるといいんだけどね"

show shizu behind_frown
with charachange

show misha perky_smile
with charachange


mi "たとえば、ちょっとした手助けね。そのくらいはいいでしょ？　そう～！　お手伝いは大歓迎！　ひっちゃんみたいな生徒のね～！"

show shizu adjust_angry
with charachange

show misha hips_frown
with charachange


mi "生徒のみんなが熱心さと愛校精神を示して、ちょっと手助けしてくれれば……あーでも、別に助けが必要ってわけじゃないけど……"

show shizu behind_smile
with charachange

show misha hips_smile
with charachange


mi "でも手助けがいらないってわけじゃないの……なので～！　手伝ってもらえると……"

stop music fadeout 2.0

show shizu adjust_blush
show misha perky_confused
with charachange


mi "おや？　こんちは～！"

show shizu adjust_blush at offscreenleft
show misha perky_confused at Transform(xanchor=0.5, xpos=-0.45)
show bg school_scienceroom at bgleft
with charamove

show hanako emb_timid at Transform(xanchor=0.5, xpos=0.93)
with charamoveinright

play music music_pearly fadein 1.0


"肩越しに見ると、華子が扉から顔だけを出して、恐る恐る教室の中をのぞいている。"

show misha perky_smile at Transform(xanchor=0.5, xpos=0.15)
with charamove


mi "なーに？　また不良ごっこ？"

show hanako emb_blushtimid
with charachange


"ちょっとからかっただけかもしれないけど、ミーシャの単刀直入な当てこすりに華子の顔が真っ赤に染まる。"

show shizu basic_angry at Transform(xanchor=0.5, xpos=0.35)
with charamove


shi "……"

show hanako emb_downsad
with charachange

show hanako emb_downsad at Transform(xanchor=0.5, xpos=0.97)
with charamove


"静音に探るようににらみつけられて、華子はうつむいてじりじりと後ずさる。もう神経質そうにドアの端をつかんでいるその指先しか、こちらからは見えない。"


"リリーを嫌っている関係で、華子もまとめて毛嫌いしているのだろうか。"


"たぶんそうなんだろう。それは華子にもわかっているはずだ。"


"俺を捕まえておこうと説得していたことも、静音とミーシャは失念してしまったようだ。"


hi "どうした、華子？"

show hanako emb_timid
with charachange


ha "あ……あの、リリー、来てませんでしたか？"


mi "悪いけど、砂藤さんならいないよ。あー……朝には来てたけど"

show hanako emb_downtimid
with charachange


"華子は落ちつかなげに静音を見つめ続ける。静音もいつもの観察眼で華子をにらみ返す。あいつはいったい何がしたいんだ？"


"もちろん静音は目をそらしたりしない。それにあいつ自身がそもそも威圧的だ。華子がどれだけおびえているか、想像するに余りある。"


"それでも、普段どおりの静音に対する華子の反応はちょっとおかしくはあるけど。両極端の二人が出会うとこうなる、ということなのかも。"

show hanako emb_timid
with charachange


ha "ど……どこにいるか、知りませんか？"

show shizu behind_frown
with charachange


shi "……"

show misha hips_frown
with charachange


mi "ちょっとでも常識があるんだったら、自分の教室で学園祭の仕事をしてると思うけど。でもどこかで油を売ってるとしても、知りませんけどね"



label jp_A22a:

show misha hips_grin at Transform(xanchor=0.5, xpos=0.15)
with charachange


mi "ひっちゃんみたいに、どこかでサボってるのかもね～！　わはは～！"


"ちくしょう。静音のやつ、何考えてるんだ？　わざわざそんな当てこすりをして。"



label jp_A22b:

scene bg school_scienceroom at bgleft
show shizu behind_frown at Transform(xanchor=0.5, xpos=0.35)
show misha hips_frown at Transform(xanchor=0.5, xpos=0.15)
show hanako emb_timid at Transform(xanchor=0.5, xpos=0.97)
with None



mi "どこかでサボってるのかもね～！　役立たずだよね～！"

show hanako emb_downtimid
with charachange

hide hanako
with easeoutright


"華子はすばやくうなずいて、そそくさと引っ込んでいく。一刻も早く静音から離れたかったんだろう。あいにくなことに、これで二人の関心が一気に俺に向かうことになる。"

stop music fadeout 2.0

show shizu behind_frown at tworight
show misha hips_frown at twoleft
show bg school_scienceroom at bgright
with charamove

show misha hips_grin
show shizu behind_smile
with charachange


mi "でもひっちゃんは役立たずじゃないよね、ね？　自分でそういったもんね～！　わはは～！"


"この後の展開は想像がつく。昨日あんな目に合わされたのに、これ以上それに付き合うのはまっぴらごめんだ。"


hi "まあ、準備がんばってくれよ……"


"俺は荷物をまとめて、出口に逃げようとする。"


"あいにく、出口は俺から見て教室の反対側だ。"


"扉までの短い距離が、今は広大な不毛の荒野に見える。"

show misha perky_smile
show shizu behind_blank
with charachange

play music music_shizune fadein 4.0

show bg school_scienceroom at bgleft
show shizu behind_blank at center
show misha perky_smile at Transform(xalign=-0.15)
with charamove

show bg school_scienceroom at center
show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charamove


"静音とミーシャがゆっくりと俺の前に歩き始めて、不気味なくらい注意深く脱出ルートをふさぐ。その動きを見て、俺は戦艦同士の戦いを思い起こす。"

show misha hips_grin
with charachange


mi "ひっちゃんも手伝いなさい、ってしっちゃんは言ってるみたいだよ～！"


hi "へええ、そうだったんだあ。静音の話はわかりにくいからなあ"

show misha perky_confused
with charachange



mi "でも～！　そういうことなの。だから、ね？　もうわたしも限界なんだよ。学園祭の屋台を作らなきゃいけないの。ほとんど全部わたしたちだけで。信じられる？"


show misha perky_sad
with charachange


mi "何枚も何枚も、板を打ち付けるのを何時間も続けるんだよ。すごい大変なんだから！"


mi "ずっとやり続けてたから、授業中でも思わず腕が釘を打ってるんだよ！"


"かなづちで釘を打つときみたいに、ミーシャが机をバンバンとたたく。"


mi "ずーっと繰り返しで、もう耐えられないの！　昨日なんか、ベニヤ板を全部一枚にまとめて釘打っちゃって……"


mi "ただの板をまとめて釘でとめただけで、それ全部はずしてやり直さなきゃいけなかったんだよ。わたし、怒鳴られて大笑いされたんだよ～！"


hi "あー……"

show misha perky_smile
with charachange


mi "なので……"

show misha hips_grin_close
with characlose


"ミーシャは俺の肩に両手を置いてにやりと笑い、いたずらっぽく舌を出して自分の歯をなぞる。"


mi "今日は予定はあるのかな、ひっちゃん？"


mi "どうでしょうねえ～"


hi "あるに決まってるだろ……"

show misha perky_confused_close
with characlose


mi "ほんとに～？"


mi "わたしたちを手伝ってくれるんでしょ、ね？"


"ミーシャの手がずっと動き続けていることに気づく。"


"静音が理解できるように、俺たち二人の会話をずっと手話で伝えているんだ。"


"今日の静音は普段よりも静かだ。まだ怒ってるのか？　まあ、少しは怒ってるだろう。目を見ればわかる。でもこれだって、またしても俺をはめて手伝わせるための仕掛けにすぎないんじゃないか。"


"どうにかしてこの罠から抜け出さないと。"


hi "なあ、俺用事があるんだよ。図書室に。宿題とかさ……"


hi "行ったほうがいいって思わないか？　ちゃんと勉強しないといけないだろ、転校生なんだし。ほかにもいろいろあって、いい第一印象を作らなきゃいけないんだよ、な？　そうだよ……"


hi "じゃあまた後でな！"

show misha perky_confused_close at offscreenleft
show shizu behind_blank at twoleft
show bg school_scienceroom at bgleft
with ease

hide misha
show misha perky_confused_close behind shizu at offscreenleft

show shizu basic_normal2 at offscreenright
show bg school_scienceroom at center
with ease_accel

show shizu cross_angry_close at tworight
show bg school_scienceroom at bgright
with ease_decel


"俺は振り向いてドアにダッシュする。でも腕を組んだ、厳しい顔つきの静音が俺の目の前に立ちはだかる。"

show shizu basic_angry_close
with charadistant


"あざけるように指を振ると、部下の兵士に指示を出す隊長のような調子でミーシャに手話し始める。"

show shizu basic_angry
with charadistant

show misha perky_smile at twoleft
with charamove


mi "急いで図書室に行きたいようには見えなかったけどね、ひっちゃん～！"

show misha hips_grin
with charachange


mi "そうだよね、しっちゃん～、たぶんあとは一日ダラダラ過ごすだけだったんじゃないかな"

show misha hips_laugh
with charachange


mi "ははは～！　わはは～！　きみは包囲されている～！"

show shizu behind_frown
with charachange


shi "……"

show misha hips_smile
with charachange


mi "生徒会室に行きましょう～！"


"ミーシャは笑いをこらえていたが、結局大笑いする。"

show misha cross_laugh
with charachange


mi "ごめんね、ひっちゃん。わたしも悪いと思うけど、でもこれはみんなのためなの。ね？"

show shizu basic_normal2
with charachange


shi "……"

show misha sign_smile
with charachange


mi "そうだね、しっちゃん！　うん、それも大事だよ"

show shizu behind_blank
with charachange


shi "……"

show misha hips_smile
with charachange


mi "そう、これはみんなのためなのよ。私たちの問題も全部解決するわ"

show shizu basic_frown
with charachange


shi "……"

show misha hips_frown
with charachange



mi "そうだそうだ～！　わたしもひっちゃんはもっとわたしたちの努力に感謝してくれると思ってたよ"


show misha hips_frown_close
show shizu basic_frown_close
with characlose


"二人はじりじりと距離を詰める。今にもとびかかってきそうだ。"


hi "なあ二人とも、二対一ってのはちょっと不公平じゃないか？"

show shizu behind_blank_close
with charachange


shi "……"


"静音は平然とした目つきでまっすぐにこっちを見つめ、そして悪魔のような笑顔を見せる。"

show shizu basic_sparkle_close
show misha hips_grin_close
with characlose


mi "ほら行こうよ、やることはたくさんあるよ！　生徒会室に行きましょう～！"


hi "いやあ、それはちょっとなあ……"

show misha cross_laugh_close
with characlose


"ミーシャは笑う。"

show misha hips_grin_close
with characlose


mi "デジャヴかな～？"


"くすくす笑いの後、またしても大笑いする。"

show misha cross_laugh_close
with characlose


mi "ははは、実はね、星占いで今日はいいことがある日だって言ってたんだよ"

show misha perky_smile_close
with characlose


mi "じゃあひっちゃんが手伝ってくれるってことで――{w=.5}{nw}"

show shizu adjust_smug_close
with charachange


"静音が素早くミーシャに向け手話をおくる。"

show misha hips_grin_close
with charachange


mi "そうだね～！　それに、ひっちゃんは自分の考えでわたしたちを手伝うって決めたわけだから……"
mi "わたしはゆっくりできるってわけ！　ラッキーだよね～、ね？"




"俺は何か言おうと口を開くが、何の意味もないことに気づく。"


"この状況から抜け出す手を考えることに集中する。いや、こいつらの行動は明らかにわざとだ。理屈で攻めるのは全くの無駄だ。"


"狂人には理屈は通じない。俺はしかめ面をするが、二人は俺の不満に気づきもしない。いよいよもって怪しい。"


"二人ともかなり落ち着いて見える。もう勝ったと思って、油断してるんだろう。"

stop music fadeout 2.5


"ちょっと思い上がりじゃないか。"


"二人は俺の前を通って、ドアから外に出る。"

hide shizu
hide misha
with charaexit


"そのまま廊下に出て階段に向かうのを見つつ、俺はこっそりと教室側に逆戻りする。"


"安堵のため息をつくと、この場から脱出するために急いで荷物をまとめる。"

play sound sfx_doorslam


"教室のドアがバタンと閉じる。"

play music music_running fadein 0.5

show shizu cross_angry at offscreenright with None
show misha cross_frown at offscreenleft with None
show shizu cross_angry at tworight
show misha cross_frown at twoleft
with ease


shi "……"


mi "今のはいただけないわね。ははは、でもひっちゃん、意外とやるじゃん。そう思わない、しっちゃん？"

show shizu behind_frown
with charachange


shi "……"

show misha hips_grin
with charachange


mi "うんうん、そうだよね……ははは！"

show misha cross_frown
with charachange


mi "今のはどういうつもり？　手伝ってくれるって言ったじゃない！"


mi "それなのに逃げ出すような真似して！　それで許されるって思ってたんだよね、そうでしょ！"

show misha cross_laugh
with charachange


"怒った表情が消え失せ、ミーシャはげらげらと笑いだして止まらなくなる。静音のいらだった視線を受けて、ようやく落ち着く。"

show misha cross_grin
with charachange


mi "ぜー、はー……いや～、ほんとに逃げられると思ってたんだね！　でも、犯人は必ず犯行現場に戻ってくるものだよね！"


"俺はそもそも教室から出てないぞ。いや待て、それ以前に手伝うなんて言ってもいないじゃないか。"

show misha perky_smile
with charachange


mi "あまり頭は良くないみたいね、犯罪者さん。そんなふうに仕事をさぼろうとして……卑劣だよ、ひっちゃん～！"


hi "俺は犯罪者かよ？　俺が何をしたって言うんだ？　容疑は何だよ？　何か悪いことしたか？"

show misha hips_grin
with charachange


mi "それは裁判所が決めることよ、犯罪者さん！　そんなことは言うまでもありません！"

show misha perky_smile
with charachange


mi "それに犯人なら、自分がやったことくらいわかってるんじゃないの～！"


hi "お前、カフカの『審判』って読んだことあるか？"

show misha hips_grin
with charachange


mi "んーん、何それ、ひっちゃん～？　それとこれと何の関係があるの？"


hi "何ヶ月か前に読んだんだ。ごく普通に暮らしていた人が、でたらめな裁判にかけられるんだ。裁判する人たちはとにかくその人を陥れようとするけど、その人は権力に逆らえない"

show shizu basic_frown
with charachange


shi "……"

show shizu behind_frown
with charachange


shi "……"

show misha hips_smile
with charachange


mi "ひっちゃん、その話がいったいどんな関係があるの？"

show misha sign_confused
with charachange


mi "ちょっと～！　今のどういう意味？"


"静音と長いこと手話でやりとりしたあげく、ミーシャは俺に向き直る。"

show misha hips_frown
with charachange


mi "わたしたち、あなたにはちょっと失望したわ。わたしたちの期待を裏切ったのよ、久夫"

show shizu basic_frown
with charachange


shi "……"


mi "大失敗をして"

show shizu behind_frown
with charachange


shi "……"


mi "わたしたちをほったらかしにして。無視したし～"

show shizu cross_angry
with charachange


shi "……"

show misha sign_smile
with charachange


mi "自分の責任から逃げ出して、仲間を置き去りにするなんて、どういう態度なの？"

show misha hips_frown
with charachange


mi "あなたにはわたしたちとの約束を守る義務があると思うの"


hi "なんだと？　俺は何も約束してないじゃないか……っ！"


"自分の息にむせ返って、しばらく呼吸できなくなる。"

show shizu basic_frown
with charachange


shi "……"

show misha cross_smile
with charachange


mi "そんなことはないわ、ひっちゃん！　自分は役立たずじゃないって、間違いなく言ったよね。そう、絶対言った言った言った～！"

show misha hips_grin
with charachange


mi "言ったからには証明してもらうよ～！　自分が役立たずじゃないってところ、見せてもらおうじゃないの！"


mi "これでばっくれたら、ひっちゃんの名誉に永久に土が付きっぱなしだよ～！"



mi "というわけで、今日一日はわたしたち３人だけで、一緒にがんばって仕事するよ！"


show shizu behind_frown
with charachange


shi "……"

show misha hips_smile
with charachange


mi "もうだまされないからね！"


mi "この学校のために偉大な貢献ができることを喜ぶべきよ。学校があなたに何ができるか問うのではなく……"


mi "あなたが学校に何ができるか問いなさい！"

show misha cross_laugh
with charachange


mi "ははは！"


mi "ははははははは！"


"なんて気の滅入る……"

show misha cross_grin
with charachange


mi "ほら、元気出してよ、ひっちゃん！"


"ミーシャが思い切り俺の背中をぶっ叩く。肺から空気が押し出されてしまい、俺は息を切らして喘ぐ。"


mi "それに、こんなにかわいい女の子二人といっしょにいられるのに、うれしいと思わないの？"

show misha hips_laugh
with charachange


mi "はははは！"


"そうかも知れない。確かにそのことは口を滑らせてしまった。"

stop music fadeout 3.0


"自分の運命を受け入れて、俺は二人とともに生徒会室に向かい……"

scene bg school_council_ss
with shorttimeskip

play sound sfx_hammer
play music music_tranquil fadein 3.0


"……最後の釘を屋台に打ちつける。昼からずっとかかりっきりで、夕食の時間ももうすぐ過ぎてしまう。でもこれで完成だ。"

show shizu basic_normal_ss at center
with charaenter


"静音は巻き尺と小さな水準器をとりだし、念入りに検査する。"

show shizu behind_smile_ss
with charachange


"満足そうに笑うと、ミーシャを手招きする。"

show shizu adjust_happy_ss
with charachange


shi "……"

show shizu adjust_happy_ss at tworight
show bg school_council_ss at bgright
with charamove

show misha perky_smile_ss at twoleft behind shizu
with charaenter


mi "とってもよくできてるって。実はひっちゃん、才能があるのかもしれないね"

show misha hips_smile_ss
with charachange


mi "わたしも驚いたよ。しかも早いし。前にもやったことあるの？"


hi "いや。一度もない"


hi "全然ない"


hi "もう二度とやらねえ"

show shizu behind_smile_ss
with charachange


shi "……"


mi "でも、今日のノルマは屋台６つだから。もうすぐわたしとしっちゃんも一つ作り終わるよ"

show misha hips_grin_ss
with charachange


mi "つまり～……残り４つだね！"

show misha sign_smile_ss
with charachange


mi "しっちゃんが、予定より早いって～！"

show misha hips_grin_ss
with charachange


mi "すっごい楽しいね、そうでしょ？"


hi "なんだと？"


"これ以外にやりたいことは山ほど思いつくけど、学園祭の準備は俺も含めてみんなで分担しなきゃいけないことなんだろう。"


hi "お前らな、俺が手伝ってやってるのは運がいいと思えよ。別にやりたくてやってるわけじゃないし、逃げようと思えば逃げられたんだぞ"

show shizu basic_normal2_ss
with charachange


shi "……"

show misha perky_smile_ss
with charachange


mi "ほんとに、ひっちゃん？"

show shizu adjust_smug_ss
with charachange


shi "……"

show misha cross_laugh_ss
with charachange


mi "わはは～！　しっちゃんが、そんなの口先だけでしょ、だって！　日本人は逃げたり反抗したりしないんでしょ、ひっちゃん～！"


"ごまかすように静音は指を組む。"

show shizu basic_happy_ss
with charachange


shi "……"

show misha hips_grin_ss
with charachange


mi "絶対そう～！　ぜったいぜったい～！　ほんとに逃げ出したかったら、すぐに逃げてたはずよ～！　疑問も後悔もない、真剣な人はそうするものよ！"

show shizu basic_normal_ss
with charachange


shi "……"

show misha sign_smile_ss
with charachange


mi "今のは黙ってたほうがよかったかもね。ひっちゃんに知恵をつけることになっちゃうから～"


"でもわざわざ俺に言っているということは、俺がそんな行動に移れるはずがないと踏んでいることの証拠だ。"


"そう考えると余計に逃げ出してやりたくなる。そのチャンスが生まれることを期待しさえする。でも仮にチャンスがあっても、静音はまた俺を捕まえるかもしれない。"

show shizu behind_smile_ss
with charachange


shi "……"

show misha perky_smile_ss
with charachange


mi "しっちゃんは満足だって"

stop music fadeout 1.5

scene bg school_council_ni
with shorttimeskip

play music music_dreamy fadein 0.5


"さらに夜遅く、俺たちの前には６つの完成した屋台が並ぶ。"


"仕事をやりとげた誇らしさとともに、俺たちは座り込んで労働の成果に見とれる。一言も言葉を交わさない。ただ見とれ続ける。"


"俺はひどくのどが渇いていることに気づく。"


hi "なあ、廊下に自動販売機があったよな？　あれ、２４時間動いてるだろ？"

show misha hips_smile at center
with charaenter


mi "うん、それにすごく安いよ。今日みたいな日はあそこで飲み物買うんだ"


"ポケットを探ると、百円玉が一枚見つかる。"


hi "これで足りる？　俺ちょっとのど渇いたよ"

show misha hips_grin
with charachange


mi "百円？　それだけあればどれでも買えるよ"


hi "よかった。そりゃありがたい"

show misha hips_grin at twoleft
show bg school_council_ni at bgleft
with charamove

show shizu adjust_happy at tworight
with charaenter


shi "……"

show misha sign_smile
with charachange


mi "あ、ちょっと待って"

show misha hips_grin
with charachange


mi "んー？　なあに、しっちゃん？　自分の分も買ってきてほしいって？　ははは！"

show shizu behind_smile
with charachange


shi "……"

show misha perky_smile
with charachange


mi "ひっちゃん、今日はよく手伝ってくれたから、わたしが――わたしじゃなくてしっちゃんね――おごってあげる"

show misha perky_confused
with charachange


mi "ちょっと、わたしは？"

show shizu adjust_smug
with charachange


shi "……"

show misha perky_smile
with charachange


mi "何がほしい？　わたしものどがかわいてるんだ？"

show misha perky_confused
with charachange


mi "わたしもだよ！"


hi "うーん、どうだろう。何でもいいよ。メロンソーダとか"

show shizu behind_smile
with charachange


shi "……"

show misha perky_sad
with charachange


mi "ちょっと待ってよ、しっちゃん！　わたしも飲み物ほしい！"

hide shizu
with charaexit

show misha perky_sad at center
show bg school_council_ni at center
with charamove


mi "あーあ……！"

show misha perky_confused
with charachange


mi "なんか、こういうときって単にからかわれてるんじゃないかって気がするんだよね"


hi "まあそうなんだろうな。ちゃんとお前にも買ってきてくれると思うよ。そうだろ？"


mi "うん、いつもは買ってきてくれるけど……わかんないよね……"


hi "ふーん"

show misha perky_confused at twoleft
show bg school_council_ni at bgleft
with charamove

show shizu basic_normal2 at tworight behind misha
with charaenter


"静音はメロンソーダ二つと、フルーツジュースを持って戻ってくる。"


"メロンソーダを一つ俺に、もう一つをミーシャに渡す。"

show misha hips_grin
with charachange



mi "ありがと、しっちゃん～！　わたしにも買ってきてくれるって信じてたよ、やっぱ頼りになるね！　わははは！"


show misha perky_confused
with charachange


mi "でもどうしてわたしが欲しかったのがわかったの？　いつもは違うのを買ってるのに"

show shizu behind_smile
with charachange


shi "……"

show misha hips_grin
with charachange


mi "なに？　試しに飲みたいと思ってると思った？　それにこういう子供っぽいのが好きだろうって？　はははは！"

show misha hips_laugh
with charachange


mi "はははは！"


"俺は手振りで静音に感謝の気持ちを伝える。静音は笑顔でうなずく。"

show shizu adjust_happy
with charachange


shi "……"

stop music fadeout 4.0

show misha sign_smile
with charachange


mi "ねえ、ひっちゃん……"


hi "ん？"

show shizu behind_smile
with charachange


shi "……"

show misha perky_smile
with charachange


mi "わたしたち、長いこと一緒に過ごしたよね。初めて会ってからほんの少ししか経ってないけど、すごくいろんなことをやりとげてきた"


mi "お互い、そろそろ率直に話すべきだと思う。何が言いたいかっていうと、"


"なんだか今にも告白してきそうな口ぶりだけど、まさかそんなはずはないだろう。それでも俺の心臓は削岩機のようにバクバクいっている。くそ、あのときのことを思い出すじゃないか。"


"何か言おうと思うけど、それ以上話すなと言うべきか、そのまま続けろと言うべきか、俺の頭では決められない。"


"耳まで真っ赤になるのが自分でもわかる。"

show shizu adjust_smug
with charachange


shi "……"

show misha hips_smile
with charachange


mi "何が言いたいかっていうと……"

show misha hips_grin
with charachange

play music music_ease


mi "生徒会に入る気はない？"


hi "何だよ、つまらないな"

show misha cross_laugh
show shizu adjust_blush
with charachange


mi "ははは！　はははは！　ははははは！　わはは！　はははは！"


mi "しっちゃんに告白されると思ってたの、ひっちゃん？"


mi "はははは！　ははは！　ははは！　はははは！"


mi "はははははははは！"


"俺は今、とても恥ずかしい。顔がさらに赤くなるのを感じる。"


"ミーシャの翻訳を見て、静音も赤面するのを隠そうとしている。そして数枚の紙を俺の前に差し出す。"

show shizu behind_frustrated
with charachange


shi "……"

show misha cross_grin
with charachange


mi "で、どうなの？　書類は全部用意してあるわ"

show misha cross_smile
with charachange


mi "あなたもちょうど席に着いてるし、くつろいでるみたいだし。飲み物とかいろいろね～！"



show shizu basic_normal
with charachange


shi "……"

show misha hips_grin
with charachange


mi "どう？"


"ミーシャはしばらく黙り込み、もう少し真剣な調子で聞き直す。"

show misha cross_smile
with charachange


mi "ひっちゃん、どうなの？"

show misha sign_smile
with charachange


mi "そこまでイヤだってわけでもないんでしょ？"




"急な態度の変わりぶりにとても驚く。どう反応すればいいのか、正直よくわからない。"


"まず、いつものような遠慮なしの騒がしい叫び声じゃない。"


"今までは、ミーシャは俺が断るのをわかっていてやっていたと思う。"


"今度はどうやら本当に真剣みたいだ。"

show misha perky_smile
with charachange


mi "わたしは、ひっちゃんは生徒会に入るべきだと思ってる。手伝ってもらえると助かるからってだけじゃなくて、その、どっちみちわたしたちと一緒に過ごしてるわけだし"


mi "ひっちゃんが生徒会に入ってくれたら、しっちゃんも喜ぶと思う。わたしたちのこと、嫌いってわけじゃないんでしょ、ね？"

show misha perky_sad
with charachange


mi "入ってもひっちゃんには何の損もないよ。それに、わたしも入ってくれたらうれしいよ"


"ミーシャはなんだかしゃべりにくそうにしている。普段はあんなにおしゃべりなのに、妙な感じだ。"


"どういうわけか、俺は心配にさえなってくる。"

show shizu behind_blank
with charachange


"視線を静音のほうに向けると、静音は上の空で爪をいじりながら、ためらいがちに俺を見つめ返す。"

show misha perky_smile
with charachange


mi "入りたくないなら、もう二度と誘わないって約束する。でも入ってくれたら、わたしたちすごく嬉しいな"


"静音もミーシャも、俺をまっすぐに見られないようだ。"


"白状すれば、俺もこんなにかわいい子二人といっしょに過ごせるチャンスを逃すことはできなかった。"


"こんな大変な仕事を毎日こなすのは願い下げだけど、学園祭が終われば仕事の量も減るはずだ。"


"少なくともそう願いたい。"


hi "わかったよ、損にはならないだろうし、やってみる"

show shizu adjust_happy
with charachange


shi "……"

show misha hips_grin
with charachange


mi "すごい、最高だよ！　あははは～！"


"静音は満足そうに手を合わせる。"

show shizu basic_happy
with charachange


shi "……"

show misha perky_smile
with charachange


mi "書類はしっちゃんが用意してくれるよ、ひっちゃん。おめでとう、これでたった今から正式に生徒会のメンバーだよ！"


hi "そりゃよかった。あまり仕事が多くないといいけどな"


hi "正直言うと、今まで生徒会の活動ってものに一度も関わったことがないんだ"


hi "でもまあ、いい経験にはなるのかな？"


"ミーシャはいつものように元気いっぱいに笑いながら、拍手を始める。"

show misha hips_laugh
with charachange


mi "おめでとう、ひっちゃん！"

show shizu adjust_smug
with charachange


shi "……"


mi "おめでとう！"

show shizu behind_smile
with charachange


shi "……"


mi "おめでとう！"

show shizu adjust_happy
with charachange


shi "……"


mi "おめでとう！"


hi "もうわかったよ"


"子供みたいにかわいらしい振る舞いに、俺は笑いを抑えられない。"

show misha hips_grin
with charachange


mi "あのね、生徒会はいつも忙しいんだよ！　でも今日のところはおしまい。また明日ね、ひっちゃん！"

show misha hips_smile
with charachange


mi "まだ仕事はあるんだから、よろしくね！"

stop music fadeout 4.0

scene bg school_hallway3
with locationchange


"完全に疲れ切った俺は部屋を出る。運動場は人っ子一人いない。こう遅くなると、学校は不気味な場所に見える。まだ明かりがついているのは生徒会室の窓だけだ。"


"生徒会ってのはこういうものなのか？　これじゃ俺の体はもたないかもしれない。"





label jp_A23:

scene bg school_scienceroom at bgleft
with shorttimeskip

play music music_tranquil fadein 3.0


"華子は全く朝の授業に顔を出さない。教室の後ろに残された彼女の席は、からっぽで寂しく見える。"


"後で見かけたら、リリーが探していたって伝えないと。"


"今朝のあの出来事にくらべれば、授業はとても退屈だ。俺はだらだらと教科書のページをめくる。"


"病院でも勉強が遅れないように努力はしていたけど、それでも追いつかなくて結構やることが多い。べつに、特別にやる気があるってわけじゃないけど。"


"教室正面にかかった時計の音がうるさくてたまらない。先生はもう７分ほど一言も話していない。かわりに、延々と続く数式を教科書から黒板に丸写ししている。"


"チョークが黒板にぶつかる規則的な音が、時計の秒針の音に完全に同調しているような気がする。"


"暇つぶしにその数式をノートに取り始める。といっても、全部教科書に載っているんだけど。"

scene bg school_scienceroom at bgright
with shorttimeskip

play sound sfx_normalbell


"ベルが鳴るけど、特に急いでいるわけではないので、俺はしばらく教室に残ってその日の授業内容を復習する。もともと最後に教室を出るのが好きだった。そのほうが廊下の人混みを避けられるし。"


"静音とミーシャも残っているのに気づく。他のクラスの誰かと話しているようだ。"


"静音の手話があまりに早いので、手を動かす際に剣で空気を切っているような音がする。"


"押し殺した怒りがこもっているのかもしれない。"


"ミーシャが必死に追いつこうとしているけど、理解するだけでも精一杯なのが見ていてもわかる。"


"俺はうなだれる。何を話しているのか知らないけど、真剣な話みたいだ。"


"手話の勢いが激しすぎて、静音の手首がぱきんと鳴る。ミーシャはそれを言葉にして伝えようと悪戦苦闘している。"


"ときどき、早口言葉を噛んだときのように言い間違える。その上、他の女子の話も静音に訳さないといけない。"


"大変そうだなあ。"


"見るからにミーシャは疲れている。今にも倒れそうだ。"


"幸いなことに話はすぐに終わり、静音とミーシャはまた自分の席に戻る。"

show shizu behind_blank at tworight
show misha perky_sad at twoleft
with charaenter


mi "うわああぁ！　つかれたよー！"


"ミーシャは疲れきった様子で、ぐったりと机に突っ伏す。"


"今なら生徒会に引きずり込まれることなく、少しは静音と仲直りできるチャンスだ。まあ、生徒会に入れる可能性はもうないだろうけど。"


hi "学園祭の準備、大変なんだな"


"確かに、この学校の生徒たちは学園祭にとても真剣に取り組んでいるようだ。授業の合間にその辺をぶらついている生徒を見ても、いつも自分の関わっている企画の話をしている。"


"みんながこれだけ熱心になっているというのはすごいな、と思う。"


"何もやることがない、というのはたぶん俺だけだろう。"

show shizu basic_angry
with charachange


"静音は鼻で笑う。俺を無視するか冷笑するか考えていたのだろうか。でも結局そのどちらもせず、手話を始める。"

show misha perky_confused
with charachange


"ミーシャはそれを見て起きあがり、静音の手を少し焦点のぼけた目で追う。"

show shizu behind_frown
with charachange


shi "……"


"厳しく、重々しく、芝居ががった調子で静音は手を動かす。"


"ミーシャがその手話を言葉に訳してくれる。"


"ミーシャの訳し方は本当にうまい。静音が実際にしゃべっていて、考えていることを直接ミーシャを通じて伝えているかのようだ。"


"きっとがんばって練習したんだろうな。"

show misha cross_frown
with charachange


mi "そりゃもちろん、わたしたちは生徒会なわけですから。結構忙しいのよ"

show shizu basic_frown
with charachange


shi "……"

show misha sign_smile
with charachange


mi "全力を尽くして、学園祭を確実に成功させるのが、わたしたちの大事な務めなの"

show shizu behind_frown
with charachange


shi "……"

show misha hips_frown
with charachange


mi "もし学園祭が失敗に終わったら、過去の生徒会の先輩たちの目の前で恥をかくことになるわ"

show shizu adjust_angry
with charachange


shi "……"

show misha sign_smile
with charachange


mi "だから学園祭を不完全なものにしてしまうような間違い、じゃなくて、ええと……今のは『妨げ』だと思う……はいっさいあってはいけないの"


"静音の情熱的な演説と、ミーシャの実演は本当にお似合いだ。奇妙なくらいに。"

stop music fadeout 2.0

show shizu adjust_blush
show misha perky_confused
with charachange


mi "おや？　こんちは～！"

show shizu adjust_blush at offscreenleft
show misha perky_confused at Transform(xanchor=0.5, xpos=-0.45)
show bg school_scienceroom at bgleft
with charamove

show hanako emb_timid at Transform(xanchor=0.5, xpos=0.93)
with charamoveinright

play music music_pearly fadein 1.0


"肩越しに見ると、華子が扉から顔だけを出して、恐る恐る教室の中をのぞいている。"

show misha perky_smile at Transform(xanchor=0.5, xpos=0.15)
with charamove


mi "なーに？　また不良ごっこ？"

show hanako emb_blushtimid
with charachange


"ちょっとからかっただけかもしれないけど、ミーシャの単刀直入な当てこすりに華子の顔が真っ赤に染まる。"

show shizu basic_angry at Transform(xanchor=0.5, xpos=0.35)
with charamove


shi "……"

show hanako emb_downsad
with charachange

show hanako emb_downsad at Transform (xanchor=0.5, xpos=0.97)
with charamove


"静音に探るようにじろじろと見られて、華子はうつむいてじりじりと後ずさる。もう神経質そうにドアの端をつかんでいるその指先しか、こちらからは見えない。"


"リリーを嫌っている関係で、華子もまとめて毛嫌いしているのだろうか。"


"たぶんそうなんだろう。それは華子にもわかっているはずだ。"


hi "どうした、華子？"

show hanako emb_timid
with charachange


ha "あ……あの、リリー、来てませんでしたか？"


mi "悪いけど、砂藤さんならいないよ。あー……朝には来てたけど"

show hanako emb_downtimid
with charachange


"華子は落ちつかなげに静音を見つめ続ける。静音もいつもの観察眼で華子をにらみ返す。あいつはいったい何がしたいんだ？"


"もちろん静音は目をそらしたりしない。それにあいつ自身がそもそも威圧的だ。華子がどれだけおびえているか、想像するに余りある。"


"普段どおりの静音に対する華子の反応を見るのは、ちょっと気の毒になる。両極端の二人が出会うとこうなる、ということなのかも。"

show hanako emb_timid
with charachange


ha "ど……どこにいるか、知りませんか？"

show shizu behind_frown
with charachange


shi "……"

show misha hips_frown
with charachange


mi "ちょっとでも常識があるんだったら、自分の教室で学園祭の仕事をしてると思うけど。でもどこかで油を売ってるとしても、知りませんけどね"



label jp_A23a:

scene bg school_scienceroom at bgleft
show hanako emb_timid at Transform (xanchor=0.5, xpos=0.97)
show shizu behind_frown at Transform(xanchor=0.5, xpos=0.35)
show misha hips_frown at Transform(xanchor=0.5, xpos=0.15)
with None

hide hanako
with charamoveoutright


"華子はすばやくうなずき、早足で出て行く。"

stop music fadeout 2.0

show misha hips_grin
with charachange


mi "なんの話だったっけ？　そうだ、学園祭の成功に向けて、わたしたちすごくがんばってるわけなんだよ"


"そのために他人をあんなふうに責め立てるって言うのか。"


hi "そうかい、まあせいぜい頑張ってくれよ"


"俺は立ち上がり、二人にこれ以上だらけた態度を叱責される前に教室を出る。"

scene bg school_hallway3
with locationchange


"ホールは予想通り少しは静かだ。皆、部活や学園祭の準備に取り掛かっているんだろう。あるいはその両方で。"


"俺が怠けているという静音の言葉がぼんやりと頭の中に反響する。"


"準備を手伝わないことに悪い気がしてくる。だけど俺は具体的に何かしようという意欲が欠けているようだ。"


"学園祭については、もう遅いだろう。静音とミーシャをアテにすれば別だけど、もちろん頼る気はない。部活は……いや、わからないな。"


"俺は部活に意気込むような人間ではないのかもしれない。"

play music music_soothing fadein 4.0

scene bg school_dormext_half
with locationskip


"校舎から寮までの道を半分ほど進んだところで、俺は寮の前に人影を見つける。"


"琳だ。"


"今日も琳は壁画に向かっているようだ。"


"俺は琳に歩み寄るが、向こうは俺が近づいてくるのに気づいていないようだ。"

scene bg mural_unfinished
show rin basic_awayabsent_close at tworight
with locationchange


"琳はひっくり返した箱の上に座り、熱心につま先のブラシで描いた絵を眺めている。"


"壁画は昨日から大分進展したようだった。しかし、俺が見る限りではまだ半分程度といったところだろう。"


"より多彩な着色がされたようだ。そして捻れた人のような絵も色がつけられ、数も増えていた。"


"実に印象的かつ独創的だ、と言わざるを得ない。どんな基準で見ても俺は芸術には詳しくない。けど、それでもこの絵は素晴らしいものに見える。"


"俺は琳を驚かせて集中を途切れさせてしまわないよう、咳払いをして注意を引く。"


rin "待って"


"琳は相手が誰なのか確かめようともしない。"


"しかし、ここは待とう。"

stop music fadeout 6.0


"……"


"……"


"……"


"……"

with shorttimeskip


"……"


"１５分ほどしても、琳の集中は途切れていないようだ。もう十分長い間待ったし、琳の肩を叩いて注意を引くことにする。そのくらいはしてもいいだろう。"


"琳は俺の方にぎこちなく頭を向けると、股の高さで目を止める。"

show rin basic_deadpan_close
with charachange


rin "ああ、久夫"

play music music_rin fadein 0.3


"わかったのか？　顔を見て言ってくれれば良かったんだけど……"


hi "よくわかったな……大変そうだな"


"１５分前からいたのがなかったことのように会話が始まる。でもそんなことはいい。少なくとも話が始まったんだから。"


hi "よく描けてるな"


"それは確かだ。ペンキの層が重なり合い、並び合い、実に印象的なヒトの形を作り出す。しかし琳はムッとした表情になる。"

show rin basic_deadpanupset_close
with charachange


rin "描いてる途中の絵に口出ししちゃダメ。７年間不幸になるんだよ"


hi "そりゃおっかない。じゃあ今のは取り消すよ"


"それでも、やはりいい絵に見える。果たしてそう考えたら１４年間不幸になるんだろうか、と疑問に思う。"

show rin basic_awayabsent_close
with charachange


"琳は壁に向き直ると、足の親指で絵を小突く。"

show rin relaxed_nonchalant_close
with charachange


rin "ペンキ、混ぜてくれる？　もう使い切っちゃいそうなんだ"


"琳はピンクっぽいペンキが半分ほど残ったボウルを覗き込む。"


"俺はここに残って、琳の企画を手伝うつもりなどなかったのだけど……というよりも、何をするつもりでもなかった。"

show rin basic_absent_close
with charachange


"俺は琳を見やる。彼女も俺をぼんやりと見る。"


hi "じゃあ、今回だけな"

show rin basic_awayabsent_close
with charachange


"琳は別のブラシを拾い上げ、淡い赤のペンキに浸す。何十もの似たようなボウルが琳を取り囲んでいる。それを見る限り、琳はここに何時間も座っていたのだろう。"


"ふと不思議に思う。つまりそれは琳が授業をサボっているということになるが、まあ琳ならやりかねないだろう。"


"俺は少量の赤と白のペンキをボウルに流し込み、壁に塗られたものに合わせようとする。"


"どうも上手くいかない。"


"そもそも琳が前もって十分な量のペンキを混ぜておいてくれれば、こんな面倒なことにはならなかったのに。しかしまったく同じ色を作るのは不可能でも、できるだけ近い色にすることくらいはできる。"


hi "ちょっと訊くけど、こんなに大きい絵だと一人じゃやりきれないんじゃないのか？"

show rin basic_deadpan_close
with charachange


rin "まあ、私はまだそんな風に考え出すほど歳でもなければ偏屈でもないから"


hi "まあそうなんだろうな"

show rin basic_deadpannormal_close
with charachange


rin "そういうこと"

show rin basic_deadpancontemplation_close
with charachange


rin "足は痛むけどね。ナメクジみたいな感じがする。ナマコで作ったナメクジみたいなさ"


hi "その姿勢のせいか？"


rin "うん。もっと体を横にしてやりたいな。言ってることわかる？"


rin "ま、でも仕方ないよね。壁にむかって『横になってくれ』なんて言えないし"

show rin negative_spaciness_close
with charachange


"そう言うと、琳は体を伸ばす。足と背中が普通の人間よりもはるかに大きく曲がる。琳の軽々とした身のこなしに驚かされる。"

show rin negative_annoyed_close
with charachange

show rin negative_spaciness_close
with charachange


"ふくらはぎを伸ばしていると、琳の普段ならうつろな顔に、少しだけひるむような――少し痛んだのだろうか――表情が浮かぶ。"


"琳には生活していくために、常人をはるかに超えたスタミナと器用さがあるに違いない。それでもこの壁画の作業で疲れが溜まっているようだ。"


hi "どうしてそんなに無理するんだ？　少し休憩するとかしろよ。疲れてるなら明日また続ければいいじゃないか"

show rin basic_deadpannormal_close
with charachange


"その言葉に琳は動きを止める。"


"しかも長い間。心の中であくびをしているような感じだ。"


"……"

show rin basic_deadpan_close
with charachange


rin "私はそうは思わないな、久夫"




rin "別に無理なんかしてないよ"


hi "……でも、大分無理してるように見えるぞ"

show rin basic_deadpannormal_close
with charachange


rin "いや、無理するしないとか、そういう話じゃないんだよ"

show rin basic_awayabsent_close
with charachange


rin "男の子がいるんだ"


hi "男の子？"

show rin basic_absent_close
with charachange


rin "うん"


hi "どこに？"

show rin basic_deadpannormal_close
with charachange


rin "美術部に"


hi "ああ……はいはい。それで？"

show rin basic_deadpan_close
with charachange


rin "その子、盲目なんだ"


hi "あぁ……目が見えなかったら、どうやって絵を描くんだ？"

show rin basic_awayabsent_close
with charachange


rin "さぁね"


hi "それで、何でそいつは美術部に？"

show rin basic_absent_close
with charachange


rin "そこがミソ。目の見えない彼は美術部にいる"


"そんな一言ずつじゃなくて、もっとまとめてしゃべってくれればいいのに。これじゃ会話じゃなくて尋問みたいだ。"

show rin basic_awayabsent_close
with charachange


rin "その子は芸術と呼べるようなことは何も出来ない、いい？　それでも彼はやって来て、絵を描いてる"

show rin basic_deadpannormal_close
with charachange


rin "どーしてだ？"


hi "さぁ、わからない。どうしてだ？"

show rin basic_deadpan_close
with charachange


rin "私もわからない。だから訊いたんだよ"


hi "……それで？"

show rin basic_deadpannormal_close
with charachange


rin "そう頻繁に描くわけじゃないけど、でも彼の描く絵ってすごい面白いんだよね"


hi "ああ、きっとそうなんだろうな"

show rin basic_lucid_close
with charachange


rin "私も１回やってみたんだ。目、つむって"

show rin basic_deadpannormal_close
with charachange


rin "でもつまんなかった。床をきれいにするのに苦労したし。それからもうやってない"

show rin basic_deadpandelight_close
with charachange


rin "でもその子、彫刻は上手くなってるんだ"


hi "へぇ"


"琳はこの話を通して何か言いたいことがあったのかもしれない。だけどその言いたいことを忘れてしまったのかもしれない。"


hi "美術部ってのは面白いヤツがいっぱいいるんだな"

show rin basic_deadpan_close
with charachange


rin "そうでもないよ"


"何だかぶっきらぼうに言うが、皮肉めいた感じはまったくしない。"


hi "違うのか？"

show rin basic_awayabsent_close
with charachange


rin "違うんだよ。別に面白い人たちじゃないの。普通、私は面白くもない人にはたいして興味湧かないよ"

show rin basic_absent_close
with charachange


rin "君は湧くのかもしれないけど"


hi "そうかもな"


"……"

show rin basic_awayabsent_close
with charachange


rin "でも、その子は面白いの"

show rin basic_lucid_close
with charachange


rin "たぶん私はあの子に似てるんじゃないかな？　あるいはキミが似てるのかも。ひょっとしたら皆似てるのかも"


rin "出来ないことをやろうとするのは、それが本当は出来るからなんだよ"


"奥の深い話だな、と思う。そしてそれを琳に伝える。"


hi "お前も奥の深いヤツだな"

show rin basic_deadpannormal_close
with charachange


rin "んーん。私なんて浅い、いっつも考えの足りない人間だよ。皆そう言うんだけどなぁ"

show rin basic_deadpanamused_close
with charachange


rin "私って一度に４つのことしか考えられないんだ。知ってた？"


hi "……いや、今知ったよ"

show rin basic_lucid_close
with charachange


rin "で、今は２階の女子トイレ、アイス味のアイスクリーム、足の中指、あと髪を切ることを考えてるってわけ"

show rin basic_awayabsent_close
with charachange


rin "そろそろ髪、切りに行かないとね"

show rin negative_spaciness_close
with Dissolve(0.1)

show rin basic_delight_close
with Dissolve(0.1)

show rin negative_spaciness_close
with Dissolve(0.05)

show rin basic_delight_close
with Dissolve(0.05)

show rin negative_spaciness_close
with Dissolve(0.05)

show rin basic_delight_close
with Dissolve(0.05)

show rin negative_spaciness_close
with Dissolve(0.1)

show rin basic_delight_close
with Dissolve(0.2)


"琳は景気良く頭を振って、乱れた髪を逆立たせて見せる。その仕草は琳も気に入っているようだった。"

show rin basic_awayabsent_close
with charachange


"俺たちが沈黙に陥ると、琳はそこらをぼんやりと歩き始め、時折ブラシを突きまわしていく。俺はもうしばらく美術部のことを考えていた。"


"俺は芸術について、未知の領域にまで足を踏み入れつつあるような気がする。琳と会っているときの俺の様子ときたら、まるで煙草でも吸い始めた未成年みたいだ。"
"だとしたら、琳と話すのはもうやめたほうがいいってことになるかもしれないけど。"


"琳の存在自体は何かと混乱のもとだけど、俺は琳のことも芸術も嫌いじゃない。暇つぶしに絵を描いたことだってある。ただ俺にはそれ以上の創作意欲や技術がないだけだ。"


"それで、何か絵に描こうとすると『白紙症候群』にかかって、何も出来なくなってしまう。"


"あるいはなんとかヘタクソな絵を描き上げては、頭の中のイメージを紙に描きだせない、自分の能力のなさに必然的にイラついて、それ以上努力もせずに諦めてしまうか。"




"琳にはどう見てもそんな問題はない……でも琳は別の意味で俺を苛立たせる。琳と一緒にいると、何も映らない鏡を見ているような気分になる。"


"そんなことをしていると、自分の正気を疑いたくなる。"

show rin basic_absent_close
with charachange


"琳は箱に座り、右に左に体を揺らす。この落ち着かない沈黙が落ち着くようだ。そして再び俺を見すえる。あるいは俺の肩の向こう側を。どこに焦点を合わせているのか、まるでわからない。"


"そろそろこの場を離れようと思う。そうすれば琳は気を散らさずに作業を進められるし、俺も一人でやりたいことが出来る。もっとも、俺は今日はやることはないが……"


hi "あ、しまった"

show rin basic_deadpan_close
with charachange


rin "何が？"


hi "いや何も。華子にリリーが探してたって伝えるのを忘れてたんだ"


hi "知ってるか？　俺のクラスの……"

show rin basic_deadpanamused_close
with charachange


rin "ああ、あの子ね。『謎のトイレ少女』"

show rin basic_amused_close
with charachange


rin "面白い人だよね。３週間前、１回の休みの間に５回もトイレに行ってたんだよ。間違いなく世界記録"

show rin basic_deadpandelight_close
with charachange


rin "すごい謎だよね"


hi "それで『トイレ少女』なんて呼んでるのか？"

show rin basic_absent_close
with charachange


rin "他にどんな理由があるってのさ。あったとしても、永遠に謎だよ。トイレの中まではついていかなかったから"


"……"

show rin basic_awayabsent_close
with charachange


rin "それともその前の週だったかなあ？　確かそうだったかも"


"……"


rin "あの子を見てるとお腹が減るんだよね"


hi "そういうことは言うなよ"


hi "……少なくとも、本人の前では"

show rin basic_deadpannormal_close
with charachange


"琳は振り返って俺をぼんやりと見る。俺がなぜとがめたのか、わかってないみたいだ。"


"しかし琳はそれ以上ちゃんと理解する様子を見せないので、俺はこの話を諦める。"


hi "それじゃあ、夕飯でも食べに行くか？"

show rin basic_awayabsent_close
with charachange


rin "ううん、まだいい"


"琳は空腹そうな視線を壁に向け直す。少しばかり気力が戻ったように見える。少なくとも、さっきまでの無気力さは少しだけ薄れている。"


"まるでその壁が、琳が夕飯にありつく前に打ち破らなければならないもののようだ。"


"俺はそう感じる。琳への妙な共感が俺の中に生まれて、一人で小さく笑う。"


"色々とおかしなところはあるけど、やはり琳はすごいやつだ。"


hi "俺は行かなくちゃ"


hi "ごゆっくり"

stop music fadeout 3.0


"琳はすでにブラシを新しいペンキに浸し始めている。当然俺の声は聞こえていないか、聞こえていたとしても返事をするつもりはないだろう。"





label jp_A24:

stop music fadeout 6.0

scene bg school_scienceroom at bgleft
show hanako emb_timid at Transform (xanchor=0.5, xpos=0.97)
show shizu behind_frown at Transform(xanchor=0.5, xpos=0.35)
show misha hips_frown at Transform(xanchor=0.5, xpos=0.15)
with None

show bg school_scienceroom at right 
show hanako emb_timid at right
show shizu behind_frown at offscreenleft
show misha hips_frown at offscreenleft
with charamove

hide misha
hide shizu
with None


hi "リリーを探してるの？　今朝君を探してたけど、すれ違いになっちゃったみたいだね"


"少しの間、華子は言葉に詰まる。その簡単な質問に答えるべきなのか、わからない様子だ。"

show hanako emb_blushtimid
with charachange


ha "は……はい"


hi "一緒に探そうか？"


hi "もしよかったら、だけど"

show hanako emb_downtimid
with charachange

show hanako emb_blushtimid
with charachange


"まだ気を許してくれてはいないらしく、華子は肩をこわばらせてかすかにうなずく。やっぱり、一人でいるほうがずっと気が楽なんだろう。でも、もう後には引けない。"


"なぜかわからないけど、華子はいつもひどく不安そうな表情をしている。そのおかげで俺まで身構えてしまう。"


"華子がいつも気を張っている理由……というか、華子みたいな人が存在する理由が、なんとなくわかる気がする。"


"でも、そういう人のそばでどう振る舞うべきなのかは、いまだにわからない。"


hi "もうすぐ夕食だね。リリーと一緒に食べようとしてたの？"

show hanako emb_downtimid
with charachange

show hanako emb_blushtimid
with charachange


"華子はかすかにうなずく。"


"だとすれば、食堂に入ろうとしていたに違いない。"


"そしたら、夕食をとっている人たちなんかがいて、昼休みのように混んでいた、と。"


"夕食の時間は長いから、実際は昼休みより空いているはずだ。でも、どうして華子が入るのを思いとどまったのかはわかる。"


"かばんを手に取り、華子と教室を出る。俺の歩くペースに合わせて早足になった華子を見て、速度を落とし、歩調を合わせる。"

scene bg school_hallway3
with locationchange


"すぐにちょうど良い早さで廊下を歩けるようになる。"

show hanako def_worry at right
with charaenter


"なんだか一緒に散歩しているような気分だ。女の子と散歩したことなんてないけど。"


"華子のほうはそう思っていないらしく、同じペースで歩いてはいても、俺の手の届く範囲にくることはない。"


"まだ俺のそばだと少し落ち着かないらしい。華子の内気さを思えば、仕方ないだろう。少なくとも、今は。"

scene bg school_cafeteria
with locationchange

play music music_night fadein 3.0


"食堂に着くころには、もう人混みも少なくなっていたけど、リリーはどこにも見あたらない。"

show hanako emb_downsad at center
with charaenter


"華子は普段よりさらに深くうつむく。"


hi "他のところは探してみたの？"

show hanako basic_worry
with charachange


ha "と、図書室だけです……本、読んでたから……"


"やっぱり、華子は授業をさぼって図書室に行っているのか。"


hi "そうか、じゃあちゃんと調べたわけじゃないんだ。俺だったら、リリーは自分の教室にいると思うな。静音が言ってたみたいに。じゃないか？"

show hanako cover_worry
with charachange


ha "そ、そうですね"

show hanako basic_normal
with charachange


"ほんのちょっぴりうなずいて、華子は賛成する。"


"まったく、やりにくいったらない。"


"華子とやりとりするためには、二枚重ねで詰め物入りのシルクの手袋が必要なんじゃないだろうか。"


"なんとなく空気がぎこちないのは、お互いに黙っているからだ。なにか世間話でもすれば、ちょっとは俺に慣れてくれるかもしれない。"


hi "それで、いつも放課後はリリーと一緒にいるの？"

show hanako emb_downtimid
with charachange


ha "は、はい"


"どういう答えを期待していたんだろう。それに、何でそんなことを聞いたんだろう。わかりきった事じゃないか。"


"華子は積極的に友達を作るタイプではなさそうだ。だから、きっとリリーが唯一の友達なんだろう。"


hi "クラスが違うとつらいんじゃないか？"


"華子はコクコクと条件反射のようにうなずく。リリーのゆったりした物腰や話し方と比べ、華子は返答をできる限り素早く簡潔に言おうとしている。"

show hanako emb_downsmile
with charachange


ha "でも、リリー……教室に寄ってくれるんです。忙しい時でも……"


"華子はそう言うと小さくほほえむ。リリーが自分を助けようとしてくれることに感謝しているようだ。"


"かわいい笑顔だ。特にこれ以上話すこともなく、この会話が終わったことに二人ともほっとする。"

scene bg school_staircase2
with locationchange


"ロビーに戻るために二人で階段を上っていると、下りてきた生徒の集団と鉢合わせになる。えさ場に向かう魚の群れのような勢いだ。"

show hanako cover_worry_close at Transform(xanchor=0.4, xpos=0.0)
with easeinleft


"向こうはこっちのことなんて気にしていないようだけど、いつの間にか華子は俺の後ろに回っている。"


hi "大丈夫？"

show hanako basic_worry_close
with charachange


ha "い、行きましょう……"

hide hanako
with easeoutleft


"生徒たちはこっちに目を向けることもなく通り過ぎていく。建物に入ると、華子はまた俺の横に陣取る。俺への不安を少しの間忘れていたのに、また元通りだ。"

scene bg school_lobby
show hanako basic_normal at center
with locationchange


"３階へと上がる間も、華子は気を緩める様子がない。"


"引っ込み思案な人や、内気な女の子にだって会ったことならある。でも華子の持つ他人への恐怖は、それをはるかに超えているようだ。"


"橋渡しになるリリーがいなければ、こんな風に俺の横で歩くことさえできなかったかもしれない。華子は、人前では完全に心を閉ざしてしまうらしい。"


"リリーの教室に向かう間、張り詰めた沈黙が続く。その間、華子の内気さについて考え、かわいそうに思う。"

scene bg school_hallway3
with locationskip

stop music fadeout 4.0
$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0


"３階に上がると、リリーの教室から出ている騒音が廊下にまで聞こえてくる。こんなに騒々しいとは思いもよらなかった。"


hi "どうやら、リリーはここらしいな……"


"なんだ、簡単じゃないか。もしかして、華子は一度ここに来たけど、やっぱり背中を押してほしくてまた俺のところまで来たんだろうか？"


"まあ、もしそうなら、俺を少し信用し始めているってことだけは確かだ。良い傾向に違いない。"


"ようやく３－２の教室にたどりつく。露骨に俺の背に隠れる華子とともに、俺はドアを開ける。"

play sound sfx_dooropen
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
play music music_another fadein 1.0

scene bg school_room32 at bgright
with locationchange


"中は作業の真っ最中だ。生徒たちがそれぞれ慌ただしく働きながら、一斉に話している。"


"ペンキ缶や、製作中の飾りと垂れ幕を見るに、今度の文化祭の準備に違いない。"


"まずリリーを見つけないと……"


"……{w} いた。"


"喧騒の中でリリーを見つけるのは驚くほど簡単だ。それは彼女の見た目のせいじゃない。"


"リリーが教室の前に立っていて、周りに２、３人の生徒が集まっている。どうやら準備作業のリーダーか、まとめ役をしているらしい。"


"机が足りないせいで、床の上で様々な生徒たちが背中を丸め、話し合っている。それをすり抜けてリリーの所にたどり着くと、俺はいつもの癖で手を上げる。"


hi "よう、リリー"

show lilly basic_surprised at center
with charaenter


"リリーは同級生の背の低い女の子に話しかけるのを止め、なんとか声を聞き取ろうと顔を上げる。"


li "すみません、どなたでしょう……"


hi "あ、ごめん。久夫だよ。華子も一緒"

show lilly basic_smile
with charachange

show lilly basic_smile at twoleft
show bg school_room32 at center
with charamove

show hanako basic_normal at tworight
with charaenter


ha "う、うん"


"華子はかなりびくびくしている。周りの人数を考えると、もっともなことだ。"


"リリーは現状把握のために一息おいてから、さっきの生徒に向き直る。"

show lilly basic_smileclosed
with charachange


li "しばらくアドバイスは森屋さんにしてもらって下さい。瀬藤くんは垂れ幕の一つに色を着けるので手一杯ですから"


"素早くうなずくと、その生徒は去っていく。方向を確認するために、慎重に指を壁に這わせている。"

$ renpy.music.set_volume(0.1,1.0)


"ちょっと待て……瀬藤？　それって健二のことか？"


"俺は急いで振り返り、華子の向こうを見るために体を傾ける。"


"案の定、部屋の隅で健二が背を丸めて、一枚の布に色を塗っている。目はハケからほんの数センチのところに留めたままだ。あいつに会った時、俺の顔を見分けるためにどれだけ近づいてきたかを思い出す。"

$ renpy.music.set_volume(1.0,1.0)

show lilly basic_smile
with charachange


li "ごめんなさい、このクラスにはちゃんと目が見える方が少なくて。なので、少しでも視力のある方は引っ張りだこなんです"


"そうだ、３－２は特に視力が弱い学生のためのクラスだ。彼らにとって文化祭の準備はとても骨の折れることに違いない。"


hi "手は足りてる？　必要だったら手伝えるかもしれないよ。たぶん、華子も"


"何かに集中するのは、華子にとって良いことだろう。でも、自分から手伝いを申し出る勇気があるとは思えない。華子がうんうんとうなずくのを見て、その判断は正しかったと確信する。"




"リリーが安堵のため息をつく。"

show lilly basic_weaksmile
with charachange



li "助かります。みんなが夕食に行くまでには、終わらせることができるかもしれませんね"

show lilly basic_listen
with charachange


li "あの大きな垂れ幕に色を塗っている方の手伝いをお願いできます？　瀬藤くん一人でやるには大仕事なんですが、誰も手伝うことが出来ないんですよ"


hi "健二と？　わかったよ"

show lilly basic_surprised
with charachange


"リリーは俺が健二を知っていることに驚いているらしい。無理もない。"


li "お知り合いなんですか？"


hi "寮の部屋が隣同士なんだ。お互い、会わないほうが難しいよ"

show lilly basic_ara
with charachange


li "そうですか。こんなに早くお友達ができるなんて良いことですね"


"お友達……その言葉を健二に使っていいものか。"


"このやりとりの間の華子の沈黙に、手伝いを申し出たそもそもの理由を思い出す。"


hi "じゃあ健二を手伝うよ。何をすればいいかはあいつが知ってるんだろ？"

show lilly basic_smileclosed
with charachange


li "ええ。何かあれば聞いてください"

hide lilly
hide hanako
with charaexit

$ renpy.music.set_volume(0.5, 2.0, channel="ambient")


"わかった、と口をそろえて言い、華子と俺は教室を横切っていく。"


"健二は床にしゃがんでいて、自分の前にある白いキャラコをじっと見ている。"

show kenji tsun at Transform(yanchor=0.45, ypos=1.0, xalign=0.5)
with charaenter


hi "よう、健二"


"……返事はない。シートの上に鉛筆でスケッチされた、半分塗りかけの大きな漢字に、ペンキをつけたハケを走らせている。"


hi "健二？"

show kenji tsun at center
with charamove


ke "ん？　なんだ？　誰だよ？"


"こいつのクラスメイトへの接し方がこれなら、一人で作業しているのはまあ当然だろう。"


hi "俺だよ、久夫。あっちで―― {w=.5}{nw}"


ke "ああ、そうだ、そうだな、わかってるよ。でもお前ここで何してんだよ？"


"話を聞こうとしないその態度にカチンとくる。"


"こいつは自分の仕事に熱中するタイプに違いない。自分が終わるまで、誰かに邪魔されるのがいやなんだろう。"

show kenji tsun at twoleft
show bg school_room32 at bgleft
with charamove

show hanako cover_distant at tworight
with charaenter


"健二との話の途中、後ろから出てくる華子の足音が聞こえ、彼女がここにいることを思い出す。"


hi "垂れ幕の手伝いをしようとしてただけだよ。華子と俺で"

show hanako cover_worry
with charachange


ha "こ……こんにちは……"

show kenji happy
with charachange


ke "おお。あー……やあ。まあ、いいんじゃないの"


"華子が関わってくると、すぐに態度をコロっと変えやがった。こいつの上っ面だけの親切な振る舞いに、寒気を覚える。"


"ああ、わかった。女か。やっぱり、いい考えじゃなかったかもな。"

stop music fadeout 2.0

scene bg school_room32 at bgleft
show kenji neutral_close at left
show hanako basic_distant_close at right
with locationskip


"いやいやながら、華子と俺は垂れ幕を挟んで健二の反対側にしゃがむ。下に置かれたいくつかのペンキ缶に注意する。"


"３－２は……そばの屋台？"


hi "お前のクラスは日曜の学園祭でそばを売るのか？"

show kenji happy_close
with charachange


ke "ああ。外でいくつか屋台、とかを"


"『とかを』だって？　こいつのあいまいな性格のせいで、もやもやした気持ちが生まれる。とは言え、今は作業が最優先だ。"


hi "で、お前はこれをどう割り振りたいんだ？　お前が文字をやって、俺たちは縁をやるか？　それとも、お前が縁をやるか？"

show kenji tsun_close
with charachange


ke "文字は俺がやる。縁を頼む"


"こいつ、驚くほど気合いが入っているな。"

show hanako basic_distant_close
with charachange


"俺がハケを取ろうと手を伸ばしたときには、華子はもう使う色で悩んでいる。"

show hanako basic_normal_close
with charachange
show hanako basic_distant_close
with charachange
show hanako basic_normal_close
with charachange


"ハケを入れるころには、華子は細かい模様を描き始めていた。華子の気を逸らす、という俺の考えは成功したようだ。"


"紺色の線を描きながら、俺たち三人は黙々と作業を始める。"


"やがて、華子が作業中なのをいいことに、健二がこっちに体を寄せてなにやら耳打ちしてくる。おかげで俺の作業は邪魔されてしまう。"

show bg school_room32 at center
show kenji tsun_close at center
show hanako basic_normal_close at offscreenright
with charamove

show kenji neutral_close
with charachange

play music music_kenji fadein 0.5


ke "さて、何でここにいるんだ？"


hi "華子がリリーを探すのを手伝ってほしいって、それだけさ"

show kenji tsun_close
with charachange


"健二はどうやら俺の動機に納得していないようだ。"


ke "なるほど。俺はお前を誤解してたようだ"

show kenji happy_close
with charachange


ke "潜入捜査中ってわけだな？　組織の奥深くまで"


"そうだよな。こいつに本当のことを教えるより、すぐばれるような嘘をついてやるか、ちょっと挑発してやったほうがましだっただろう。"


hi "だからお前はここにいるのか？"


ke "当然だ。かったるいけど、情報収集には自分で潜入するのが一番だからな"

show kenji tsun_close
with charachange


ke "離れるなよ。ここは過酷な学校、過酷な世界だ"


hi "そうだな、とってもキツイよ"


"健二は俺の真意に気づかず、同意を得たことに満足して持ち場に戻る。作業に取り掛からないと。"

stop music fadeout 2.0
stop ambient fadeout 2.0

scene bg school_room32
show kenji neutral_close at left
show hanako basic_normal_close at right
with shorttimeskip


ha "おわりました"


hi "俺も。お疲れさま"


"二人の模様の線をつなぐ。俺の模様はできるだけ華子が描いたものを真似してある。"

scene bg school_room32
with locationskip


"うめきながら腰を上げ、辺りを見回す。"

play music music_dreamy fadein 4.0


"華子と俺以外に教室に残っているのは、垂れ幕を仕上げている健二に、話し合っているリリーと数名の生徒だけだ。"


"腕時計を見て納得する。もうかなり遅い時間だ。"


hi "手を貸そうか？"

show hanako basic_normal at center
with charamoveinbottom


"手を差し伸べると、華子は立ち上がろうと手をつかむ。"


"そうすると、つい華子の手首に目がいってしまう。ここまでやけどが広がっているなら、華子の体は一体どこまで焼けてしまったんだろうか？"

show hanako emb_downtimid
with charachange


"華子がもう一方の手で素早く手首を覆い隠すのを見て、罪悪感に襲われる。"


hi "なかなか綺麗じゃない？"

show hanako emb_timid
with charachange


"華子は驚いたようだったけど、俺が垂れ幕のことを言ったんだと気づく。"

show hanako basic_bashful
with charachange


ha "そう……かも、ですね"


"華子の笑顔からは、達成感がにじみ出ている。俺も同じだ。"

hide hanako
with charaexit


"飾りつけは机や棚の上に置かれ、床の上は片付いている。おかげでさっきより楽にリリーの所に行くことができる。"


hi "垂れ幕は終わったよ。これで全部？"

show hanako basic_smile at tworight
show lilly basic_smileclosed at twoleft
with charaenter


"リリーはうなずいて感謝の意を示す。"

show lilly basic_smile
with charachange


li "ありがとう、久夫さん、華ちゃん。何かお礼にできることは……？"


hi "別にいいよ。どっちみち、自分の部屋で勉強してるよりはマシだから"

show hanako basic_normal
with charachange


ha "気にしなくていいよ"


"リリーはうなずくと、最後の一人を思い出す。"

show lilly basic_surprised
with charachange


li "あ、瀬藤くんはまだここに？"


"俺が答えようとした時、部屋の向こう側から健二が言葉を返す。"


ke "ああ、今終わったとこ"


"ペンキを乾かすために、健二は垂れ幕を空いた場所にそっと滑らせて置き、そそくさと部屋を出ていく。"

show hanako basic_normal at center
show lilly basic_surprised at left
show bg school_room32 at bgleft
with charamove

show kenji neutral at Transform(xalign=1.15)
with charaenter


ke "じゃーな"


hi "おう"

hide kenji
with charaexit

show hanako basic_normal at tworight
show lilly basic_surprised at twoleft
show bg school_room32 at center
with charamove


"他に残っている学生２人がリリーにさよならを告げて出て行くと、俺たち３人だけになる。"


hi "さて、これで全員かな"

show lilly basic_displeased
with charachange


li "もうこんなことはせずに済めばいいんですけど"


hi "放課後も作業するってこと？"

show lilly basic_concerned
with charachange


li "そうです。今年のクラスの企画は意欲的でした。意欲的すぎたのかもしれません"

show hanako emb_smile
with charachange


ha "でも、屋台は良く出来てるよ"


hi "華子の言う通りだよ。たくさん手がかかってるってことさ"

show lilly basic_ara
with charachange


li "あらあら、それを聞いたらみなさん喜びますよ。あとはもう、学園祭までにする仕事は大してありませんから"

show hanako basic_smile
with charachange


ha "ええと……かなり遅い時間だよ。もう行かない？"

show lilly basic_smileclosed
with charachange


li "それが良いですね。久夫さん、一緒に寮に戻ります？"


hi "そうだな、じゃあ一緒に行くよ"

scene bg school_gardens2_ni
with locationskip


"夜の照明で、校庭がまったく違って見える。いつもの青々とした草木と比べて、いろいろなものが穏やかだ。"


"時間が遅いのと、辺りに生徒がいないことが大きいんだろう。寮の門限までの時間を有効活用しようとする、急ぎ足の生徒が一人二人いるぐらいだ。"


"聞こえるのは俺たちの足音と、前方の地面を叩く、リリーの白杖の規則的で緩やかな音だけ。"


"学校での大変な慌しさの後で、ようやく落ち着くことができるのはうれしいものだ。"


"俺は無意識に小さな欠伸を漏らす。"

show lilly cane_smile_ni at twoleft
show hanako basic_normal_ni at tworight
with charaenter


li "疲れました？"


hi "まあね。それでもここの暮らしには慣れてきてると思うよ"


hi "あの……えーと、静音との件……あれはちょっと驚いたけどな"


"リリーたちの大っぴらな口げんかのことをずばり言ってしまい、歯を食いしばる。それでも、いったいどんな事情があったのかをはっきりさせたい。"

show lilly cane_displeased_ni
with charachange


li "あ……そのことは……"


li "あんな人目につく所でごめんなさい。羽加道さんと私とは……以前からこうなんです"


label jp_A24c:





"静音のことを……いや違う、むしろ俺が言ったことを思い出して、リリーの声はわずかに苛立っているようだ。"

show lilly cane_listen_ni
with charachange


li "羽加道さんの肩を持つのはやめていただけますか。あの人を刺激しないでください"


"まあ、あのときの予感はこれではっきりしたな。俺はリリーを怒らせていたんだ。"


"確かに、あの場ではリリーを見捨ててしまったのかもしれない。でも詳しい事情なんて知る由もなかったし、謝る理由だって一切ないはずだ。"


"少しの間、張り詰めた沈黙が二人の間に流れ、華子が俺たちをそわそわと交互に見る。"


"俺が謝りそうにないとあきらめて、リリーは言い争いを投げだし、話題を変える。"



label jp_A24d:




"静音のことを思い出して、リリーの声がわずかに苛立つ。明らかに、これ以上話したくないらしい。"

show hanako basic_distant_ni
with charaenter


"意見を求めて華子をちらりと見る。でも、その表情はいつも通りつかみどころがなく、読むのが難しい。"


"何にしたって、リリーが口げんかについて謝ったのは大したものだと思う。事情はわからないままだけど。"



label jp_A24e:



show lilly cane_weaksmile_ni
with charachange


li "ともかく、学園祭が過ぎてしまえば良いですね"


"話題が変わるのはありがたい。重たい雰囲気がさっと吹き飛ぶ。"


hi "気持ちはわかるよ。前の学校の文化祭はこれよりもっとおとなしかったから"

show lilly cane_smileclosed_ni
with charachange


li "山久学園は学校社会という理想を重視します。それで職員方は文化祭や特別なイベントを行うのが好きなんですよ"


hi "それなのに作業をしてるのは生徒じゃないか。世の中不公平だな"

show lilly cane_giggle_ni
show hanako emb_emb_ni
with charachange


"華子とリリーは同意してクスクス笑う。職員が周りにいないから、俺たちの文句が聞かれないこの状況をありがたく思う。"

show lilly cane_smile_ni
show hanako basic_smile_ni
with charachange


li "私は厳格な女子校から転校してきたので、それがここで役に立っているのだと思います。そこに比べれば、山久はずっとゆったりしてますしね"


"なら、それでリリーは上品な話し方と物腰になったんだろう。"

scene bg school_dormext_half_ni
show lilly cane_smile_ni at twoleft
show hanako basic_smile_ni at tworight
with locationskip


"寮に着き、それぞれの部屋へと別れる時がくる。"


hi "じゃあな、リリー、華子"


"二人は礼儀正しくお辞儀をして、男子寮のすぐ隣にある女子寮に向かう。"

stop music fadeout 4.0

hide lilly
hide hanako
with charaexit


"夜間のいたずらを防ぐために、職員がさりげなく建物の外を見回っている。まあ、それは予想通りだ。"


"職員の横を通り、自分の部屋まで歩きながら、ぐっと腕を伸ばし、首をさする。ずっと床で作業していたから、どっちもズキズキする。"


"だけど実際、やることがあるのは気分が良い。病院で長い間過ごした後では、勉強に宿題、先生たちという日常の出来事も天の恵みとすら思える。"


"こんな日々が続くなら、山久での暮らしはうまくいくかもしれない。"


label jp_A24a:

scene bg school_dormhisao_ni
with locationskip


"頭の隅に残るナースの小言を守り、目覚まし時計をセットする。早起きして、またジョギングに行けるように。"


"約束したからには、ちゃんと守ってみせる。それに、行かなかったら笑美にチクられるに決まってる。"


"だけど、それもそんなに悪くないな。"

$ suppress_window_after_timeskip = True

scene black
with shuteye


label jp_A24b:

scene bg school_dormhisao_ni
with locationskip


"疲れた。ぎりぎりまで寝ていられるように目覚まし時計をセットする。一時間目に間に合えばいい。"


"頭の隅で、早朝ジョギングについてのナースの言葉がしつこく響く。明日の放課後散歩に行って、埋め合わせをすればいいさ。"


"どうせ笑美は気にもかけないさ。賭けてもいい。"

$ suppress_window_after_timeskip = True

scene black
with shuteye

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
