label jp_H11:

scene bg school_miyagi_ss
show hanako basic_distant_close_ss at center
with locationchange



"部屋の色合いが午後の日差しからゆっくりと夕暮れのオレンジ色に染まっていく。時計はかろうじて聞き取れるくらいの小さな音を立てて、ゆったりと背後で時を刻んでいる。"




"しかし、どんなに長い間待っても結末は変えられない。"



"ちっぽけな駒が、チェス盤の上でこつんと小さく音を立てる。"





show hanako basic_normal_close_ss
with charachange



"巻き上げられたゼンマイのように、華子は俺の手番が終わったすぐ後に駒を動かす。"






"こいつはまいったな。俺が１手を打つのに５分かかっているのに比べて、華子は自分がどうすればいいか完全に理解しているみたいだ。"




show hanako basic_smile_close_ss
with charachange

play music music_tranquil fadein 3.0


ha "チェックメイト"



hi "またかあ……今ので戦績は？　３対２だっけ？"


show hanako cover_bashful_close_ss
with charachange



ha "ス……ステールメイトは数えないよ"





hi "ちぇっ。華子は毎日うまくなっていくよな"




"さもなければ、今まで手加減をしていたんだろう。初めてあったときには考えもしなかったけど、華子には本当にチェスの才能がある。"






"チェスは俺たちが放課後に紅茶の部屋でこっそりすることのできる格好の娯楽だ。"





"ここにいると、外で生徒が歩き回る音がかろうじて聞こえてくる。階下から伝わる日常の雑音を聞いていると、山久に来る前の自分の生活を少しだけ思い出す。"
"といっても、あのころの生活には二度と戻れないことはとっくに理解しているけど。"






hi "もう１戦どう？"



show hanako basic_worry_close_ss
with charachange


ha "わ……私、宿題を終わらせなくちゃいけなくて……"


hi "あぁ、そうなんだ。じゃあまた明日にしようか"

show hanako basic_distant_close_ss
with charachange


ha "でも……これ、どうしよう……"



"華子はほとんど駒の残っていないチェス盤を囲んでいるティーセットを指さす。"



hi "心配しないで、やっとくよ"

show hanako basic_normal_close_ss
with charachange


ha "うん……わかった……"

show hanako basic_bashful_close_ss
with charachange


ha "じ……じゃあね"


hi "またね"

hide hanako
with charaexit



"俺は片付けを始め、華子は去って行く。"




"外の体育会系の部活から聞こえてくるホイッスルや声援の頻度が少なくなり、やがて静かになる。"





"心のどこかで、俺はまだそういうチームに入りたいと思っている。あの出来事の前はサッカーや他のスポーツをしていたから、もう自分にはできなくなったことに郷愁を感じるのは当たり前なのかもしれない。"






"でも俺がここにたびたび来る理由は他にある。自分が運動ができなくなったこともそんなに苦には思わない。今ではリリーと仲良くなったけど、華子とのささやかなやりとりには、とても暖かな気持ちになる。"






"自ら作り上げた殻の中にいる華子の本当の姿を見るたびに、毎日感じる小さな満足感。何よりも、それがここに来ている理由なんだ。"









"俺がカップやソーサーをしまっていると、外から話し声が聞こえてくる。ちょっと動きを止めて聞いてみると、どうやら華子とリリーのようだ、何をしゃべっているのか外に出て聞いてみる。"




scene bg school_hallway2
show lilly basic_weaksmile at twoleft
show hanako emb_downtimid at tworight
with locationchange



li "本気なの？"






ha "ほ……本気だよ……"


show hanako emb_timid
with charachange



ha "あっ、久夫くん"




"華子は俺が近づくのに気づいて、ちょっと驚いたような顔で振り返る。ちょうど帰ろうとしていたところを、リリーに捕まえられたに違いない。"




show lilly basic_smile
with charachange



li "あら、久夫さんもいるんですか？"





hi "こんにちは、リリー。どうしたの？"

show lilly basic_smileclosed
with charachange



li "やっとクラス委員の仕事が終わったので、お２人と上海へお茶に行けたらと思っていたんです。気分転換に学校の外で楽しく過ごせたらいいと思って"






hi "それはいいね。でも、華子は宿題しなくちゃいけないんじゃ……？"


show hanako basic_smile
with charachange



ha "そ……そんなに多くないし……"




show lilly behind_cheerful
with charachange



li "よかった。では話は決まりのようですね"




stop music fadeout 2.0

scene bg suburb_shanghaiint at Fullpan(3.0, dir="left")
with shorttimeskip

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0



"３人で中に入りながら、俺は店内を見渡す。いつもどおり中にはせいぜい片手で数えられるほどの人しかいないし、話し声や音もあまりせず、静かだ。"





scene bg suburb_shanghaiint at left
show hanako emb_emb:
    xpos 0.4 xanchor 0.5
show lilly cane_smileclosed at twoleft
with charaenter

play music music_dreamy fadein 6.0



"丘の上から街までのゆるやかな散歩の時と全く同じように、リリーは華子の腕につかまっている。ただ、それがリリーの案内のためなのか、それとも華子を安心させるためなのか、どちらとも判断がつかない。"




show lilly basic_smile
with charachange



"一旦リリーが華子から腕を離すけど、杖を納めるとすぐ元の場所に腕を戻す。その間に優子さんが素早く俺たちの場所へやってくる。"





show yuukoshang closedhappy_up at tworight
with charaenter


yu "上海へようこそ！　ご注文はお決まりでしょうか？"


show yuukoshang neutral_up at Transform(ypos=1.25)
with Dissolvemove(0.5)

show yuukoshang neutral_down at tworight
with dissolvecharamove



"優子さんは深くお辞儀する。優子さんのプロとして行き届いた挨拶は、彼女自身の雰囲気を良くしている。普段の様子から比べれば良い変化だ。"






show lilly basic_smileclosed
with charachange



li "紅茶をお願いします。華ちゃんと久夫さんは？"





hi "パイを一つ、あとコーヒーを"



show hanako basic_smile
with charachange


ha "こ……紅茶で……"

show yuukoshang smile_up
with charachange




yu "はい、ただいま。お好きな席へどうぞ、すぐお持ちいたします"




hide yuukoshang
with charaexit



"優子さんは笑顔でうなずき、厨房へすり足で歩いて行く。俺たちは早々に窓際の席へ向かう。"





hide hanako
hide lilly
with charaexit

show bg suburb_shanghaiint at right
with charamove_slow

show lilly basic_sleepy_close:
    twoleft
    easein 1.0 ypos 1.1
show hanako basic_smile_close:
    tworight
    easein 1.0 ypos 1.09
with charaenter



"みんなで席に滑りこむ。女の子たちは同じ席に座り、リリーが杖を横に立てかける。俺は反対側の席につく。そして、ふと華子の仕草が普段とは違うことに気づく。"







"視線を地面に釘付けにし、目の見えない護衛の後ろに隠れ、自分達以外の周りの世界は存在しないと思い込もうとするのではなく、華子はただ視線を低くしてリリーの世話をしているだけだ。"







hi "大丈夫、リリー？　疲れてるように見えるけど"


show lilly basic_weaksmile_close:
    twoleft
    ypos 1.1
with charachange



"疲れを表に出してしまったことに少し決まり悪そうな様子を見せながら、リリーは軽く頭を下げる。"






li "クラス委員の仕事はとても疲れますね。多くの場合、それは生徒会の相手をする、ということでもありますから"




show lilly basic_sleepy_close
with charachange



li "本当に疲れます"




show hanako basic_normal_close:
    tworight
    ypos 1.09
with charachange


ha "ほ……ほかのクラス委員の人たちはどうなの？"

show lilly basic_reminisce_close
with charachange




li "私よりはましですけど、それほど違うわけではないですね。静音は誰が相手でも鬼監督なのは変わらないから"







hi "なんだか、あまり仕事を楽しんでるって感じじゃなさそうだなあ。そもそもそんなに大変なら、どうして続けてるの？"




show lilly basic_displeased_close
with charachange



li "クラス委員であることは楽しいですし、その責任だってきちんと果たせます。ただ一緒に仕事をする人たちが、時には……"








"リリーの声はだんだん小さくなり、中途半端なところで途切れる。彼女が他人をけなすというのは想像しづらいけど、そうさせる人物がいるとすれば静音しかいないだろう。"





show hanako cover_worry_close
with charachange



"こうした争いごとの話を聞いている華子はちょっと縮こまっているように見える。でも俺が話題をそらそうとする前に、華子は立ち上がる。"




show hanako basic_worry_close at tworight
with dissolvecharamove

show lilly basic_surprised_close
with charachange


li "華ちゃん？"

show hanako defarms_strain_close
with charachange


ha "す……すぐに戻ってくるから"

hide hanako
with charaexit



"そう言って華子はトイレに向かう。これも彼女なりの状況への対処の仕方なのだろう。それが華子の真意であるなら、だけど。"





show bg suburb_shanghaiint at center
show lilly basic_concerned_close at Position(xpos=0.5)
with dissolvecharamove


"けれども、リリーは少し傷ついたように見える。"



hi "心配するなよ。今のはリリーのせいじゃないと思う"




show lilly basic_oops_close
with charachange


li "でも……"



hi "最近、華子がだんだん強くなってきていると思うんだ。リリーも見た……だろう……？"








"今のはちょっとまずかったな。幸いリリーは気を悪くしたようには見えないけど、そろそろ俺は彼女の地雷を踏むことを怖がってばかりいられない。"




show lilly basic_sleepy_close
with charachange



li "そうかもしれませんね。ただ、時々……私には見分けづらいと思うことがあります"







"しばしの静寂が支配した後、２つのティーカップ、パイ、そして湯気だった熱々のコーヒーが俺たちの前に出される。"



show bg suburb_shanghaiint at right
show lilly basic_sleepy_close at Position(xpos=0.3)
with charamove

show yuukoshang closedhappy_down at tworight
with charaenter



"リリーにカップの位置がわかるよう、優子さんが特に気をつけながらカップをリリーの指先へ置いているのに気づく。"




show yuukoshang closedhappy_up
with charachange



yu "はい、どうぞ"




hi "ありがとう、優子さん"


show lilly basic_weaksmile_close
with charachange


li "ありがとうございます"

hide yuukoshang
with charaexit



"すばやく静かにお辞儀をし、優子さんは去ってゆく。"



show bg suburb_shanghaiint at center
show lilly basic_weaksmile_close at Position(xpos=0.5)
with charamove



li "ああ、そうでした。久夫さんに聞きたいことがあったんです。今ならちょうどいいですね"









hi "どうしたの？"




show lilly basic_smileclosed_close
with charachange


li "華ちゃんの誕生日がもうすぐなので、プレゼントを買うためによろしければ今週末、町へ付き合っていただけませんか"



"華子の誕生日がもうすぐ？　華子を少しでも元気づけるいい機会かもしれない。優子さんみたいに、彼女はいつもパニックか抑うつ寸前に見えるし、それにチェス以外で楽しそうにしているのを見たことがない。"








"それはさておき、友達と一緒に街の様子を知るのは、いい週末の過ごし方だと思う。"







hi "わかった、喜んで付き合うよ。他には華子の誕生日に何かやることは考えてる？　パーティかなにか？"




show lilly basic_weaksmile_close
with charachange



li "華ちゃんのことですから、おそらく控えめなほうがきっと――"



show lilly basic_listen_close
with charachange



"リリーは急に言葉を切ると、ティーカップを持ち上げて一口飲む。その理由を俺はいぶかしむ。"





"数秒後、華子がこちらに歩いてくるのがリリーの肩越しに見える。トイレのドアが開く音に気づいたのだとしたら、リリーの耳は相当いいに違いない。"






show bg suburb_shanghaiint at bgleft
show lilly basic_listen_close at Position(xpos=0.3)
with charamove

show hanako basic_normal_close:
    tworight
    easein 1.0 ypos 1.09
with charaenter



"華子は席に座りなおし、すぐに紅茶を飲む。俺たち３人は日が沈むまで静かに飲食する。"







"感じのいい夕暮れ時の過ごし方だ。山久の静かで穏やかな環境に感謝したい気持ちになる。隔絶されているとはいえ、俺はここでの暮らしを本当に気に入り始めている気がする。"




stop ambient fadeout 2.0

scene bg suburb_shanghaiint at bgleft
show lilly basic_smileclosed_close:
    twoleft
    ypos 1.1
show hanako basic_smile_close:
    tworight
    ypos 1.09
with shorttimeskip



"彼女たちが話している間に、俺はコーヒーを飲み終えてマグカップをテーブルに置く。ここのコーヒーは俺にはちょっと苦いけど、それでもかなりおいしい。いずれにせよ、自分で入れるのよりはずっといい。"







"２人は主にそれぞれの読書の好みについて話し合っている。俺はそれに関連した話題にちょっと好奇心を抱く。"






hi "ねえ華子、ちょっと思ったんだけど……チェスや読書以外に好きなことや趣味はある？"


show hanako emb_timid_close
with charachange



"華子は完全にその場で固まってしまう。そんなことに興味を持つ人がいたということ自体にとても驚いているみたいだ。華子が答えを考えつくまでしばらく時間がかかる。"





show hanako emb_downsmile_close
with charachange


ha "うーん……う……歌うのも、ちょっと好きかな。パ、パソコンも好きだけど、そ……そんなに使わないし"




"歌というのはちょっと予想外だ。普段の穏やかな話し方を考えると、華子の歌う声を想像するのは難しい。"







show lilly basic_smile_close
with charachange



"一方でリリーは軽くうなずくだけだ。すでに知っているんだろう。華子と仲良くなってからもう１年くらいは経っているしな。"



show hanako cover_bashful_close
with charachange



ha "ひ……久夫くんは……？"



hi "俺？"

show hanako basic_bashful_close
with charachange



"華子はためらってから、さっと頭を上下に動かす。自分の趣味について話したのだから、俺の趣味のことも聞きたいと思うのは当然のことだ。"





hi "もちろんチェスだろ。で、あとは……うーん……"



hi "サッカーもあったな、でも今はもうできないけど。病院では読書が趣味になったな…えーと……"


show hanako basic_normal_close
show lilly basic_sleepy_close
with charachange



"これは思いもよらず大変だ。リリーと華子はこの話の流れに少し戸惑っているみたいだ。考えれば考えるほど、俺も戸惑ってくる。"






show lilly basic_weaksmile_close
with charachange



li "久夫さんは事故以来、いろんな趣味を始めたみたいですね"







"リリーの助け船は、たぶん俺の言葉を最大限に好意的に解釈したであろう表現でいっぱいだ。でも華子は黙ったままでいる。"







"華子は難しい状況になると、それ以上事態が悪くなるのを避けるために、黙り込むというリアクションを常に取るようだ。さもなければ、自分からその場を離れてしまう。"





$ renpy.music.set_volume(0.2, 0.0, channel="sound")
play sound sfx_phone

show lilly basic_surprised_close
show hanako cover_worry_close
with charachange



"柔らかいベルの音が会話を中断する。リリーがポケットに手を伸ばすと、彼女の携帯の音だったことがわかる。"




show lilly basic_weaksmile_close
with charachange



li "すみません……"



show hanako basic_normal_close
with charachange


ha "ど、どうぞ……"

show lilly invis_close at Position(ypos=1.0)
with dissolvecharamove

hide lilly
with None



"リリーはさっとうなずくと席を抜け出し、俺たちの邪魔にならないように少し離れたところで電話をとる。"





hi "人気があるって、いいよな"


show hanako cover_bashful_close
with charachange


"華子は笑ったけれど、話の種にはならないようだ。"



$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene black
with shuteye


"結局俺は椅子に深く座って目を閉じ、できるだけくつろぐ。"




hi "ここは素敵だし、のどかだね。もし俺が都会じゃなくて、こういうところで育っていたら、どうなってただろうなって思うよ"






ha "ひ、久夫くんは都会から来たの？"





"どうやら華子が話したい話題を見つけたみたいだ。"


$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg suburb_shanghaiint at center
show hanako basic_smile_close:
    center
    ypos 1.09
with openeye



hi "ああ。根っからの都会育ちさ"


show hanako basic_worry_close
with charachange


ha "い、色々変わったでしょ……"



hi "そうだな。でもそういう色々なことをどう理解すればいいのか、まだよくわかっていないんだ。いろんな意味でちょっとカルチャーショックだよ"







hi "華子が初めて山久に来たときもそうだったんじゃない？　ここに新しく来る生徒はたいていそうなるんじゃないかって思うけど"




show hanako basic_distant_close
with charachange



ha "そ、そうでもないよ……"





"それ以上話を続けたくないようで、華子は少し視線をそらす。俺は問うように首を傾けるけど、それ以上の答えは返ってこないまま数秒が過ぎる。"




scene bg suburb_shanghaiint at bgright
show hanako basic_distant_close:
    tworight
    ypos 1.09
with charamove

show lilly back_pout at twoleft
with charaenter

stop music fadeout 8.0



li "その件は月曜日に回せないんですか？　まだこの前の後始末だって全然……"





show lilly back_listen
with charachange



li "わかりました。なんとかして説き伏せてみます。彼女は一度こうと決めたらいつもそうですから"






li "ええ、ありがとう。じゃあまたあとで。さようなら"



show lilly basic_displeased
with charachange



"リリーは会話を終え、パチンと携帯を閉じる。テーブルには戻ってきたけど、席には座らない。"




hi "行かなきゃいけないの？"

show lilly basic_concerned
with charachange


li "残念ですが。クラス委員の仕事でまた呼び出されまして"

show hanako cover_worry_close
with charachange



ha "い、一緒に行こうか"



show lilly basic_weaksmile
with charachange



li "大丈夫よ、華ちゃん。生徒会へまっすぐ行くだけだから。私の用事で良い夜を台無しにする必要はありませんよ"



show lilly basic_smile
with charachange



li "それに、もし華ちゃんが私に付き添って学校に戻ったら、かわいそうな久夫さんのお相手は誰がするの？"




show hanako basic_normal_close
with charachange


ha "わかった……"

show lilly basic_weaksmile
with charachange



li "もしよかったら、また今夜お茶をしましょう。たぶん私も飲みたくなるでしょうから"





show lilly cane_weaksmile
with charachange


"俺たちはその案に賛成し、リリーは別れを告げ、華子から杖を受け取る。"

hide lilly
with charaexit



"リリーの分も払うと俺は申し出たけど、リリーは自分の分を払うと主張し、優子さんに挨拶をして店を出ていく。"





play music music_dreamy fadein 4.0

show bg suburb_shanghaiint at center
show hanako basic_normal_close:
    center
    ypos 1.09
with charamove



"そして……あとは俺たちだけだ。華子と俺をしばらく２人きりで過ごさせるのも結構なことかもしれない。でも普通それが意味するところは、２人で一緒に座ったまま黙りっぱなしになるだけ、ということだ。"






"俺は華子からどんな風に見えているんだろう。"
"自分が怖い人間だと思ったことは一度もないけど、同い年の人がすぐそばでこういう振る舞い方をしていると、ひどく自分を意識してしまう。まるで俺自身が華子の動揺の原因じゃないかという気分になる。"









"こんなにも山久に引きこもるのをやめれば、もう少し他人に慣れてくるかもしれない。でも……ずっと年上の人でも華子の顔を一瞥して強烈な反応をしてしまうのなら、彼女が俺と同じ気持ちになるのもわかる。"







"本当にお手上げだ。華子が山久に残る限り、人付き合いに慣れることはないだろう。でも山久を離れたとしても、華子がどんな努力をしても、その傷跡を受け入れられない人々には跳ね返されてしまうだろう。"







hi "まだしばらくいるんだったら、何か他のものを頼もうか？　夕食と言うほどたくさんは食べていないしさ"




show hanako basic_smile_close
with charachange



"華子は顔を輝かせて、元気にうなずく。俺が話を持ち出したことを喜んでいるみたいだ。優子さんの目を引くと、律儀に注文を聞きに来てくれる。"





scene bg suburb_shanghaiint at bgright
show hanako basic_smile_close:
    tworight
    ypos 1.09
with charamove

show yuukoshang neutral_down at twoleft
with charaenter



yu "追加でご注文ですか？"





hi "スペシャルサンドとホットチョコレートを。ちょっとコーヒーには時間が遅いかな、華子？"



show hanako cover_bashful_close
with charachange


ha "お、同じものをください……"

hide yuukoshang
with charaexit



"優子さんはうなずいてお辞儀すると、つま先立ちでターンして厨房へと戻り、パンや調味料を探し出したり、飲み物を入れるために機械を操作したりと忙しく働く。"






show yuukoshang smile_up at twoleft
show hanako basic_bashful_close
with charaenter




"優子さんが戻ってくるまで俺たちは一言も言葉を交わさない。笑顔で俺たちの注文を持ってきた後、優子さんは別の客に呼ばれてそちらに向かう。"





hide yuukoshang
with charaexit

show bg suburb_shanghaiint at center
show hanako basic_bashful_close:
    center
    ypos 1.09
with dissolvecharamove



"俺は華子と多く話せるかもという期待を捨てて、ちょっとした食事を楽しむことにする。"






"うまいな。ここの食べ物はだいたいおいしいんだ。２、３口食べたあと、何か足りないことに気づく。すなわち、華子の食べる音だ。"




show hanako basic_distant_close
with charachange



"見やると、華子は手付かずのサンドイッチの後ろでそわそわしている。"




hi "お腹すいてないの？"

show hanako cover_worry_close
with charachange



"華子は首を左右に振る。それでも、顔の右側は前髪の房によってほぼ完全に隠れている。"






ha "う、ううん"


hi "そう？　華子の分も食べる準備はできてたのにな"




show hanako basic_worry_close
with charachange



ha "なんだか……こ、困ってるみたい。な、何か……あ、あったの？"





"俺が悩んでいると華子に思われていることにはっとするけど、考えてみると華子の言う通りかもしれない。気づかない間に感情が顔に出ていたのかもしれない。それに華子は鈍い子では決してない。むしろ逆だ。"





hi "俺たちは友達、だよね？"

show hanako emb_downsad_close
with charachange


ha "友達……"



"華子の声色と縮こまる姿勢を見ると、俺はまた別の地雷を踏んでしまったみたいだ。"




"これも華子とつきあうのが難しい理由の１つだ。俺や、おそらくリリーさえも含む、他の人と自分の間に築き上げた心の壁。残念だけど――"




show hanako basic_bashful_close
with charachange


ha "そ、そうだと思う……"



"華子の率直な答えに、俺はちょっと不意を突かれる。何の答えも返ってこないだろうとほぼ諦めかけていたので、なおさらだ。"





hi "う、うん……"



show hanako basic_worry_close
with charachange


ha "ち、違った？　ご、ごめんなさい、わ、私……"




hi "いや、ただ……華子がそう言ってくれて、安心したんだ"






hi "さっきの華子の話とつながるけど、山久に来てからと言うもの、他の人とどう付き合っていけばいいのか少し不安なんだ"






"自分が少し笑っているのに気づく。今ので俺は驚くほど安心していた。自分の顔が笑っているのを自覚しながら、ホットチョコレートを口に持っていく。"






hi "熱っ！"

show hanako emb_downsmile_close
with charachange


ha "だ、だから……"


show hanako emb_smile_close
with charachange



ha "だからまだ飲んでないの。わ、私、飲み物が冷めるのを待ってて……"




hi "なるほど、じゃあ俺も待とう"




"俺たちは一緒にくすっと笑う。この状況は別に面白いわけではないけど、どういうわけか……今は笑うことが一番自然なことに思える。"






"俺たちはお互いがお互いを緊張させあっていたんだろう。華子が何か困っているんじゃないかという考えにとらわれすぎていて、彼女に指摘されるまで俺自身が不安になっていることに気づかなかった。"






"でもそれはそれとして……少しいい気分がする。その人なりに、俺のことをそういう風に考えていてくれる人がいる、というのはなんだかうれしいものだ。"




$ renpy.music.set_volume(1.0, 0.0, channel="sound")
stop music fadeout 8.0

scene bg school_dormext_full_ni
with shorttimeskip




"長い坂道を口数少なくとぼとぼと上り、学校にたどり着いたあと、俺たちは２つの寮の中間にいる。"








"夜間警備員が男子寮と女子寮の間を定期的に巡回している。監視のためと、医療上の問題が起きたときに素早く事態を知らせるためだ。当番の警備員が俺たちに気づいて、さっとうなずいてから見回りを続ける。"




show hanako emb_downtimid_ni at center
with charaenter



"隠す間もなく、華子の口から大きなあくびがもれる。もうかなり疲れているんだろう。"





hi "それじゃ、自分の部屋に戻ったほうがいいかな。また明日、華子"

show hanako emb_smile_ni
with charachange


ha "お、おやすみなさい……"

hide hanako
with charaexit



"それぞれがそれぞれの道を歩き出した後で、俺は止まって振り返る。"


show hanako basic_smile_ni
with charaenter



"華子がそこに立って笑いながら手を振っている。俺も笑って手を振り返す、そして数秒後、彼女は向きを変えて寮への階段を上がり、ドアの向こうへと消える。"



hide hanako
with charaexit



"２人で共有するこんなちょっとした瞬間は、小さな宝物のようだ。１つ確かなことがある。わずかな人にしか見せることのない、華子の小さく繊細ではかない笑顔を、俺は守りたい。"








"華子が近くにいるとき、華子に何かしてあげられるときに感じる気持ちについて考える……それが、今俺たちが分かち合っているものを越える何かにつながる種なのかもしれない、と。"




scene black
with dissolve



label jp_H12:

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play music music_happiness fadein 2.0

scene bg school_track
with locationchange



"夏の太陽は味わい深いけど、田舎の空気と組み合わさると、より素晴らしいものになる。"




"目の前のグラウンドでは、陸上部員たちが騒いでいる。サッカーをしている人がいるかと思えば、会話に興じている人や笑いながらふざけあっている人もいる。"







"大木の陰で芝生の上に座っている俺には、誰も関心を払わない。退屈な学校での１日を過ごした後の、気持ちのいい平和なひとときだ。"


play ambient sfx_footsteps_soft fadein 4.0



"心臓発作が起きる前はよくサッカーをしていたから、彼らを見てとても懐かしく感じるだろうと思っていた。でも今俺が感じている気持ちは、それとはまったく別のものだ。"





stop ambient fadeout 0.3

show miki smile:
    center
    easein 1.0 ypos 1.12
with charaenter



"後ろから足音が近づいてくるのが聞こえたので、見てみるとクラスメートの一人が傍に腰を下ろしている。ここにいるのを気づかれるとは思わなかったし、あまり喋ったことのない子だったのでとまどってしまう。"


show miki grinclosed:
    center
    ypos 1.12
with charachange



mk "おっす"






hi "やあ。三浦さん、だったよね？"





show miki wink
with charachange


mk "美貴って呼んでよ。名字じゃ堅苦しいし"



hi "じゃあ、俺も久夫でいいよ"




show miki smile
with charachange




"俺たちは男子がサッカーをしているグラウンドに目をやる。彼らは第２戦目の用意をしているようだ。それぞれのポジションに向かってみんな散らばっていき、ボールがセンターに運ばれる。"







"思った通り、試合開始の笛が吹き鳴らされて、みんなすぐさま試合に戻る。"






hi "やらないの？"

show miki grinclosed
with charachange


mk "うん、ちょっと休憩"

show miki wink
with charachange



mk "久夫は？　さっき私たちを見てたときはやりたそうに見えたけど"







"じゃあ、やっぱり俺に気づいている人はいたということか。"




hi "長い話になるんだけどね"

show miki grin
with charachange


"彼女の顔には興味をそそられたと書いてある。"



hi "俺が山久にいるのは心臓が悪いからなんだ。今じゃもうサッカーはできないんだ"


show miki smile
with charachange


mk "サッカー選手になりたかったの？"



hi "いや、遊びでやってただけだよ。友達がやってたから俺もやってたんだ"






hi "あそこでプレイしている人たちの誰かが、発作を起こす前の俺だったとしてもおかしくない。でも、あそこに戻りたいって本当に望んでるわけでもないんだ。ちょっと説明しにくいけど"




"たとえ今では体力がほとんどなくなっているとしても、俺の体格はまだしっかりしているし、他のクラブのメンバーともうまくやっていた。"






"考えてみると、自分にはもうできないのに、サッカーをしている人々を見たら、相当嫌な気分になるはずだ。でもそうはならない。それはいいことなのかもしれない。新しい人間になる準備ができている証だから。"




hi "ごめん、なんだかまとまってなくて"

show miki grinclosed
with charachange



mk "いや、よかったよ。本当、聞けてよかった"



show miki smile
with charachange



mk "久夫は心の整理ができてるみたいだね。山久に来る人のなかにはすごく落ち込んでる人もいるんだけど"







hi "そういえば、美貴は陸上部の部員だよね？"



show miki grin
with charachange


mk "うん。ここに来たときからずっとね"



hi "ひょっとして笑美と友達だったりする？　ちっちゃくて、速くて、足のない子。そんなに女子陸上部員が多いとは思えないし"





show miki grinclosed
with charachange


mk "あははっ、笑美ちゃんね。陸上部員じゃなくても誰でも知ってるよ"

show miki smile
with charachange



mk "でも違うの、私は男子とつるむほうが多いから、あんまり笑美ちゃんとは話さないんだ。久夫はどうなの？"






hi "ああ、そうだな、俺はクラブには入ってないんだ。少なくとも正規のクラブには"





show miki wink
with charachange



mk "久夫は華子ちゃんや金髪アマゾネスと仲がいいんでしょ？"




"金髪アマゾネス……リリーについて言えば、少なくとも身長は比喩通りだな。それ以上深く突っ込むことはせず、俺はうなずく。"


show miki grinclosed
with charachange



mk "じゃあ心配いらないね。久夫に友達がいる限り、クラブに入る必要はないよ"




"グラウンドで大きくホイッスルが鳴り、俺たちの注意を引く。１人の選手が足を抱えていて、他の選手たちが試合を中断して駆け寄っていく。その光景に美貴は顔をしかめる。"




show miki serious
with charachange



mk "うぅ、痛そう。あいつ、運が悪かったね"






"美貴がグラウンドを見続けているけど、俺は彼女のけがを思い出してしまう。その左腕の先は手ではなく、切り株のようになっていて、俺が山久に来て以来常に包帯に包まれている。新しいけがには見えない。"







"美貴がまた話しかけようとこっちを向いて、俺に手を見られていることに気づく。彼女は包帯をしている手をもう片方の手で隠し、俺たちは気まずい沈黙の中で座る。"







hi "ご、ごめん。俺まだちょっと……"


show miki smile
with charachange


mk "気にしないで"



"美貴の声は明るかったけど、会話は続かない。山久の障害を持つどの生徒も、その人なりに自分の問題と折り合いをつけている。"
"自分の障害が厄介事の種だと思う人がいるのも当然のことだ。結局のところ俺もその１人なんだし。"






"サッカーの試合で怪我をした男子は、周りに助けてもらいながらなんとか立ち上がると、仲間の肩を借りて足をひきずりつつフィールドを後にする。まだ歩けるのなら、きっとただの肉離れだろう。"






"ホイッスルがもう一度鳴り、１人減ったフィールドでゲームが再開される。"


show miki whistle
with charachange



mk "華子ちゃんやあの金髪の子とつるんでるなんて……すごく奇妙なつきあいだよね"



hi "なんで？"

show miki serious
with charachange


mk "華子ちゃんはその、何ていうかわかんないけど……"


hi "恥ずかしがり屋？"




mk "ううん、そうじゃなくて。なんというか……華子ちゃんはちょっとおかしなところがある、と思う。あんまりいい言い方じゃないんだけど"






show miki wink
with charachange



mk "悪い子ってわけじゃないの。全然いい子だと思うよ"




show miki serious
with charachange



mk "ただ……付き合いづらいんだ"




"それはまるで、美貴かクラスの誰かが過去に華子と親しくなろうとしたことがあったけど、うまくいかなかったという風に聞こえる。"





"山久にかぎらず誰だって問題は抱えているものだということを考えると、美貴はかなり厳しいことを言っていると思う。"
"とはいえ俺は昔から華子を知っているわけじゃないから、なにか俺の知らないことがあったのだとしても驚きはしない。"





hi "なるようになるさ。華子はいい子だし、それこそが肝心な問題だと思うよ"




"美貴は目を細めて、笑みを広げる。"

show miki grin
with charachange


mk "久夫は華子ちゃんのことが本当に好きなんだね"

label jp_choiceH12:
menu:
    with menueffect
    "美貴は本当に遠慮のない物言いをするな。"
    "認める":








        return m1
    "否定する":



        return m2


label jp_H12a:



hi "正直に言うと……そうだよ。誰にも言わないでくれると助かるんだけど"


show miki wink
with charachange


mk "おっと、信用してちょうだい。大丈夫よ"

show miki grinclosed
with charachange



mk "正直かわいいところあるなって思っちゃったわ。久夫がそのつもりなら止めるつもりなんてないよ"




hi "ありがとう"



"美貴はそう言うけれど、華子が『問題』を抱えているとたった今話してたじゃないか。それでも、俺は自分の言った言葉を守りたい。"
"華子の問題は関係ない。何が起ころうとも対処してみせる。俺は彼女の助けになりたいんだ。"





"もし、落ち込んで引きこもる華子から何かを引き出せる可能性がほんの少しでもあるのならば、何があろうと俺は努力してみせる。華子が王子を必要としているのなら、俺がその王子になってやる。"




"華子との関係の可能性を考えていると美貴がニヤニヤと俺の顔を覗き込んでくる。俺は間違いなく赤面しているだろう。美貴から目をそらしたけど彼女を笑わせるだけの結果になる。"






label jp_H12b:


hi "そうは思わないな。ただの友達だよ"

show miki serious
with charachange


mk "へえ。ちょっとお似合いかなって思っていたんだけどな。結局、男の子と女の子がボーイフレンドとガールフレンドである必要はないってことかな"



"美貴の言うことは正しい、たとえ俺が華子に特別な感情を抱いていたとしても。華子とはいい友人だし関係を壊したくはない。けれどそれ以上の存在になりたいとも思っている。難しいな。"





label jp_H12c:



"美貴はほかの女の子たちとは違った雰囲気を漂わせている。彼女と話していると、むしろ男子と話しているような気がする。男とつるんでることのほうが多いと言われても、その印象は変わらない。"






"腕時計をチラッと見るともう数分で昼休みが終わろうとしている。教室に戻らなくてはならない時間だ。"


hi "そろそろ昼休みが終わるよ。戻ろうか？"

show miki smile
with charachange



mk "うん、そのほうがいいね"


show miki smile at center
with charamove



"芝生から身を起こして塵を払うと、美貴が起き上がるのに手を貸す。手をとり軽々と起き上がると、むき出しの腕の引き締まった筋肉が動くのが目に入る。"




hi "そういえば、美貴はなんで女子の制服を着ていないの？"

show miki whistle
with charachange


mk "ああ、暑いし窮屈だからだよ。男子の制服の方がいいの"



"美貴がその意見を強調するように腕を振り回すと、その副作用として彼女の体のとある部分が目立ってしまう。なるほど、女子のブラウスだったら窮屈だろう。"




scene bg school_gardens
with locationchange



"俺たちは話をしながら、中庭を通り抜けるように本校舎へと歩き始める。"





show miki smile at center
with charaenter



mk "久夫もだいぶ慣れてきたみたいだね。安心したよ。試験が近づいてることを考えると、この時期に転校生が来るってのはかなり驚きだったんだよ"



hi "思い出させないでくれよ……"

show miki grinclosed
with charachange



mk "あはは、大丈夫だって。詰め込み勉強すれば問題ないよ"




hi "いいアドバイスには聞こえないけど"


show miki grin
with charachange



"美貴は笑いながら俺の肩を何回もたたく。学業のことをあまり真面目に考えているようには思えない。"



show miki wink
with charachange



mk "久夫は頭がよさそうだし、武藤先生はもう君のことを気に入ったみたいだし。師弟みたいだよ"






hi "それがいいのか悪いのか考えないとな"





hi "俺はまだこの学校をどう捉えたら良いのか分かってないんだ。もう２、３週間はここにいるけど、まだなにかに驚いて呆然とすることがある"





show miki smile
with charachange



mk "もう少しすれば慣れるって。他のとこと同じ、ただの高校だよ"






"簡単に言うけど、ここをそんな風に考えたことは一度もない。俺にとって山久は人生の大変化を象徴するものだ。"
"俺はもはや普通ではなくなった。俺は『変わって』いた。そして他の『変わっている』人たちと共に学ぶことになったんだ。"





"けれども、昼休みの間気軽に話したり、他の人がサッカーをしているのを見たりしてクラスに戻っている――どれも完璧に普通だ。美貴の言ったとおりなのかもしれない。"





"きっと俺は華子にも同じように目を向けるべきなんだろう。みんなそれぞれの問題を抱えているっていうのは山久に限ったことじゃない。結局、ここも他の学校と同じ、ただの高校だ。"






"話しながら歩いていると、自分の顔が笑っていることに気づく。美貴と俺はほぼあらゆる意味で違っているけれど、クラスメートのことをちょっとでも知ることができてよかった。"




stop music fadeout 2.0

scene black
with dissolve



label jp_H13:

play music music_daily fadein 2.0
$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

scene bg misc_sky
with locationchange


"リリーを待つあいだ、頭の周りにそよ風が初夏の香りを運ぶ。"


"小さな白い雲が空に散り、青色の単調さを断ち切る。"


li "久夫さん？　いらっしゃいますか？"


"リリーの声が、そよ風と一体であるかのように軽快に聞こえてくる。"


"俺はリリーの様子を伺うために空を見つめるのをやめる。"

$ renpy.music.set_volume(0.8, 1.0, channel="ambient")

scene bg school_gate
show lilly cane_surprised_cas at center
with locationchange



"桃色のオフショルダーのセーターと足首まである褐色のスカート、そして褐色のサンダル。とてもきれいな姿だ。"





hi "よお、ここだよ、リリー。門の近く"


hi "華子からはうまいこと逃げ出せたのか？"

show lilly cane_weaksmile_cas
with charachange



li "ええ。私が週末の間に外出するのは珍しいことではありませんから、華ちゃんがなにかを疑うことはないでしょう"


show lilly cane_sleepy_cas
with charachange


li "それに……他に会う方がいるようですし"



"リリーは言葉を続けるべきではなかったかも、というように唇を閉じる。にわかには信じがたい話だ。"



hi "華子が誰かに会うって？　本当に？"

show lilly cane_weaksmile_cas
with charachange



li "いえ、ただ……セラピストの方と週末によく会っているので"





hi "ああ、なるほど。それなら十分納得がいくな"


show lilly cane_reminisce_cas
with charachange



"リリーはばつが悪そうに腕をさする。その困惑した表情を一目見て、俺はすぐに華子のことから話題を変える。"




hi "ふうん……"



show lilly cane_surprised_cas
with charachange



li "なんですか？"




hi "不思議に思ってたんだ……リリーは１人で街を出歩けるの？"


show lilly cane_listen_cas
with charachange



"リリーは盲目のことを話題にするのを躊躇する俺にため息をつく。ときどき、俺は本当にバカな失敗をするな。"




li "ええ、できますよ。友人や姉さんと一緒のほうが楽ですけどね"




"リリーとお姉さんの仲はどうなっているんだろう。一人っ子の俺には兄弟や姉妹がいるということがどういうものなのか想像もつかなくて、リリーがなんだかうらやましく思えてくる。"



hi "そっか。そうそう、あと数分でバスが来るから、そろそろ出ないといけないな"

show lilly cane_weaksmile_cas
with charachange



li "そうですね。乗り遅れたら、長く待つはめになりますから"


stop music fadeout 6.0
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_road
with locationchange



"そういうわけで、俺たちは丘の上のバス停へと向かう。校門からは少しばかりの距離だから便利なものだ。"



hi "ここからの眺めはいいな。都会から移ってきたから、こんな景色を見る機会なんてなかったんだ。ましてや毎日なんてさ"

show lilly cane_smile_cas at center
with charaenter


li "私にとってもここは良い場所です。穏やかで、都会の喧騒や臭いからも離れていて"


show lilly back_listen_cas
show lillyprop back_cane at center
with charachange



"いつものジェスチャーでもって、リリーが頭を上げる。なにかを聞きつけた証拠だ。"


show lilly back_smile_cas
with charachange


li "あら、バスが来るようですね……"



"バスが丘を上がってくるのを見ようと道路を見下ろす。リリーの耳は本当に便利なんだな。"





"バスが丘を上がって停留所に到着するまでいくらもなく、俺たちは１分とかからず街へと繰り出していく。"



stop ambient fadeout 2.0

scene bg city_street1
with shorttimeskip

play music music_ease fadein 2.0
$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0


"街を歩いていると、疑いようのない郷愁を感じる。都会の臭い、交通量、そこら中にある見上げるようなビル群……高架歩道をのぞけば、俺の生まれた都市によく似ている。"




"公園を歩くのと同じくらい気軽に街中を歩いているけど、車が俺の下を走り回っているというのはなんだか奇妙な感じだ。"




"建造物としての高架歩道の見事さについて忙しなく考えていると、俺は驚かされる。"



show lilly cane_smileclosed_cas_close:
    center
    xpos 0.4
    easein 1.0 xpos 0.5
with charaenter



"リリーが俺の腕を抱え込んでいたことに気づくまで少し時間がかかる。もう片方の手には長く伸ばした白杖をもっている。"



"一瞬、俺は驚いたけど、それをリリーに気づかれないよう十分に平静を装う。リリーが俺に引率を頼むのはこれが初めてじゃないけど、前は俺の袖口を掴むだけだった。"



"町中のような、人の多い入り組んだ場所を進んで行く時に、しっかり体を近づけておく方が楽だとリリーが考えるのは当然だ。でもリリーに比べたら、俺はこういう接触には全然慣れていない。"



"俺が歩き出すのをリリーが待っているあいだに、俺たちのあいだの沈黙が大きくなっていることにようやく気づいて、俺はすぐさま脳をフル回転させる。"



hi "なあ、華子が歌うのが好きだったなんて驚きだよな。華子が歌ってるところ、聞いたことある？"


show lilly cane_smile_cas_close at center
with charachange



li "もちろんありますよ。何度かカラオケで一緒に歌ったことがあるんです、姉さんも一緒で。私はカラオケがあまり好きとは言えませんが、２人は気に入っていますよ"




"俺がはじめに思っていたより、華子がカラオケで歌うというのは似合っているかもしれない。小さな部屋の中で、自分と知り合いだけ。"




"他に華子を見物する人は誰もいないし、華子にとっては警戒を解くことができる貴重な機会になるだろう。"




hi "華子を街のカラオケ屋に連れて行って、そこでバースデーパーティをするっていうのもいいかもな。もしあいつが気に入れば"



show lilly cane_sleepy_cas_close
with charachange



li "うーん。その興奮に華ちゃんがうまく対応できるかどうか、何とも言えませんね"





"俺は反論しようとするけど、リリーの表情からは、今の提案をもう少し考えているのがわかる。結論が出るまで、本当に長い時間がかかる。"


show lilly cane_weaksmile_cas_close
with charachange




li "とはいっても、今の時点では、華ちゃんのために楽しい誕生日の思い出を作ってあげるのが一番良いと思います。いつまでも華ちゃんが普通ではないような扱いをし続けても仕方ありませんから"







hi "そう思う。なにか悲しみ以外の思い出があれば、元気になるかもしれないな"






"なにか毎日目にすることができるものを買ってくれば、過去の嫌なことを忘れて、友達がいるってことを思い出せるかもしれない。"





"なんにせよ、華子はこういうことも乗り切れると思う。華子のそばで過ごしているうちに、俺は華子がはじめに思っていたほど恐がりでか弱いわけではないことを知った。"



hi "さて、そろそろ出発しないか？　このあたりの地理は詳しくなくてさ"

show lilly cane_smileclosed_cas_close
with charachange

stop music fadeout 6.0


li "そうですね。まずはなにか食べることにしませんか？"



hi "俺もまだ食べてないから、ちょうどいいな"


show lilly cane_cheerful_cas_close
with charachange


li "どこかいいところをお願いしますね、久夫さん"


"リリーがいたずらっぽい笑みを浮かべると、それに応えて俺も反射的に笑顔になる。たとえそれがリリーには見えないとしても。"



hi "よーく分かってるよ、心配しないで"


stop ambient fadeout 1.0
play music music_another fadein 4.0
scene bg city_karaokeint
with locationskip



"店内に入ると、俺はパイ２つと、セットで紅茶を一緒に注文してテーブルに戻る。"



show lilly basic_smileclosed_cas_close:
    center
    ypos 1.1
with charaenter



"このカフェはリリーも気に入りそうなタイプだと判断した。こぢんまりとして静かだけど、手入れが行き届いていて高級感がある。リリーの優雅な笑顔からすると俺は……正しい選択をしたのかどうかはわからない。"



"なんだかんだで、笑顔でないリリーを見ることなんて滅多にないんだから。"



"それでも、俺は角の席の、リリーのすぐ近くに座ってささやかな食事を広げる。"

show lilly basic_planned_cas_close
with charachange



"リリーは目の前に置かれたパイの上に用心深く頭をもっていくと、上品にその芳香をかぐ。"


show lilly basic_cheerful_cas_close
with charachange


li "レモンパイですね？　ありがとうございます"



hi "いいって。すぐそばに紅茶があるから、倒さないように気をつけて"


show lilly basic_weaksmile_cas_close
with charachange



"リリーは感謝するようにうなずくけど、かすかに弱々しくなった笑顔から察するに、わざわざ言うまでもなかったみたいだ。たぶん音を聞くだけで位置は伝わっていたんだろう。"



"話はそれぐらいにして、俺たちはほとんど黙り込んだまま食べものを腹に流し込む。リリーはなにか食べながら話し合うのを良しとしないだろうし、俺もそうするのが好きだとはいえない。"



"そうしているうち、俺たちは食事を終え、残っていた紅茶も飲み干す。最初に沈黙を破ったのはリリーだ。"


show lilly basic_smile_cas_close
with charachange




li "おいしかったです。本当にいいところを選んだんですね、久夫さん"





hi "こんなに街を見て回ったのは初めてだったから、見た目が良さそうなところを選ぶぐらいしかできなかったよ"



hi "ああ……くそ。ごめん"



"リリーの前でうっかり視覚に関することを持ち出してしまったことにひどく罪悪感を覚える。でもリリーはあまり気にしてなさそうだ。むしろ逆に、俺の不恰好な謝罪を面白がっているかのように見える。"


show lilly basic_smileclosed_cas_close
with charachange



li "優しいんですね、久夫さん。でも、ときどきそれが裏目に出てしまわないか心配になります。わざわざ私のために言葉を選ぶ必要はないんですよ"




"リリーは自分の障害のことにも本当にうまく適応している。それでも俺は急いで話題を変える。リリーが持つその自信を、俺も共有しているとはいい難い。"




hi "ここには長いこと住んでたの？　見た感じずいぶんとこの辺りに慣れてるみたいだからさ"


show lilly basic_planned_cas_close
with charachange



"リリーはすばやく顔の前で手を振って、その指摘を否定する。"


show lilly basic_smile_cas_close
with charachange



li "そんなことはありませんよ。山久には高校の初めからいますけど、姉さんが送り迎えをしてくれていましたから、それほど街を歩いたことはないんです"




hi "ああ、そうか。寮には最近まで住んでいなかったって言ってたっけ"




"これは本当に驚きだ。てっきりリリーは少なくとも山久に入学したときからここに住んでいたと思っていた。少なくとも数年はいるだろうと。"



show lilly basic_smileclosed_cas_close
with charachange




li "生まれてからはほぼずっと家族と暮らしてきましたけど、その後は姉さんと二人きりで。ずっと昔に家族がインヴァネスに移ってしまって、姉さんも働く時間が長くなったので、私も引っ越すことにしたんです"





hi "インヴァネス？　スコットランドのどこかだっけ？"

show lilly basic_surprised_cas_close
with charachange



li "あら、話していませんでしたか？　私の家族は今スコットランドに住んでいます。母の生まれた場所なんです。父方は主に日本人ですけど"



"ははあ。ときどきリリーの容姿について疑問が頭をよぎっていたけど、聞いてみようとは思わなかった。その答えがこれってわけだ。"



hi "正直にいうと、思いもしなかったよ。なんの訛りもないところを考えると、リリーはこっちで生まれたの？"


show lilly basic_giggle_cas_close
with charachange


li "大正解です。そうでなければ、早いうちから英語を教わることもなかったでしょうから、自分の生い立ちには感謝しています"

show lilly basic_smile_cas_close
with charachange


li "久夫さんはいかがですか？"


hi "なにが？"



"リリーはしばらく考える。話題を変える前に聞くことを考えておいた方がよかったんじゃないかな。"


show lilly basic_weaksmile_cas_close
with charachange


li "そうですね……なにか将来に向けた計画はありますか？"


hi "実をいうと、最近はなにも考えていないんだ"


hi "発作とそれから数ヶ月の入院生活のあとだから、リリーや華子と毎日を楽しんでいるだけで十分なんだ"



"実際、『将来』については長いあいだ考えたことがない気がする。考えても仕方のないことのように思える。"


show lilly basic_sleepy_cas_close
with charachange



li "高校生活も今年で最後です。どの道、このあとは自分の力で生きていかないといけないんですよ"




hi "それは分かってるよ。その時以来、ちゃんと考えたことはないってだけで……"


show lilly basic_weaksmile_cas_close
with charachange



"リリーは言葉を続けようと口を開くけど、その代わりに小さいため息をつく。俺の置かれている状況について、深入りできるほど十分に分かっていないことに気づいたんだろう。"




li "まあ、誰にも自分のペースというものがありますからね。いずれいい機会に恵まれるといいですね"



hi "……そうだな。考えておくよ"

stop music fadeout 2.0

$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

scene bg city_street2
show lilly cane_smileclosed_cas_close
with shorttimeskip


"街中へと戻るさなか、リリーはまた俺の腕を抱える。"

show lilly cane_smile_cas_close
with charachange


li "それで、プレゼントについてはなにか良い案は浮かびましたか？"



hi "実をいうと、全然。昔から贈り物を選ぶっていうのは得意じゃなくて"


show lilly cane_weaksmile_cas_close
with charachange



li "おかしな言い方ですけど、今はとにかく……見て回るべきなのかもしれませんね？"




"リリーがそんな言葉を発するのを聞いて、俺はしばらく面食らう。"



hi "えー……そうだな。どうやって？"

show lilly cane_cheerful_cas_close
with charachange



li "そうくると思いましたよ。簡単です。久夫さんがウィンドウショッピングをして、何があるか私に教えてくれれば"


show lilly cane_smileclosed_cas_close
with charachange



li "なにか興味を引くものがあれば、いいアイディアが浮かぶかもしれません"




hi "なるほど……まだ自信はないけど、リリーを信じるよ"


show lilly cane_smile_cas_close
with charachange



li "何とかなると思いますよ。華ちゃんや姉さん、それに私はうまくやってますから"


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg city_street3
with locationskip



"リリーの割り切った、むしろ楽観的な言葉とともに、俺たちはこの区域でのショッピングに出発し、俺はリリーに見えるものすべてを口で説明していく。"




"華子がウィンドウショッピングにいくとは考えにくい。流行を重視するタイプだとは思えないし、雑誌なんかを読むのも見たことがない。実際、俺が見たことのある、彼女の趣味といえば読書だけだ。"




hi "正面に雑貨の店があるな。ほとんど食器ばかりみたいだけど"



show lilly cane_sleepy_cas_close at center
with charaenter



li "華ちゃんがそういうものをそれほど欲しがっているとは思えません。それにどんなメッセージを添えるんです？"



hi "うーん……『もっと料理をしてね』とか？　そんなに悪くないと思うんだけど……"

show lilly cane_weaksmile_cas_close
with charachange


li "そういうことは、ときにはそっとしておいてあげたほうがいいんですよ、久夫さん"



"またしても、華子のキッチンでの努力は必ずしもうまくいくとは限らないんだなと察する。リリーはときどき手を貸してやらないといけなかったんだろう。"




hi "どれどれ、次は本屋だ……これはいいんじゃないか、いつも本を読んでるんだし"


show lilly cane_concerned_cas_close
with charachange


li "そうですが、本だと少し問題もあります。私は華ちゃんがすでに読んでいる本とそうでない本がわかりません"


hi "商品券ならどうだ？"

show lilly cane_listen_cas_close
with charachange



li "商品券を贈ることほど人間味のないことはありませんよ。『あなたのことをよく知らなくて、何が気に入ってもらえるかわかりませんでした』と言っているようなものです"




hi "その人が欲しいものを確実に手に入れられると思ってたんだけどな"


show lilly cane_displeased_cas_close
with charachange



li "人にものを贈るということは、相手の人にどれくらいの愛情を持っているかを示すものでなくてはなりません。ささやかな贈り物ひとつも決められないなら、いったいどれだけその人のことを考えたといえますか？"




hi "わかったわかった。商品券はなし"





"リリーは熱が入りすぎているみたいだけど、言いたいことは俺にもわかる。人に贈るものを選ぶときは、少なくとも少しは気持ちを込めるべきだ。"




"毎日俺たちのことを思い起こさせるようなものを華子に贈るというのに、商品券のなにがいいっていうんだ？"




hi "それなら、去年はなにを贈った？"


show lilly cane_smile_cas_close
with charachange



li "陶器の人形です。華ちゃんが話し相手がほしいときに、その気持ちを楽にしてくれるかもと思ったんです"


show lilly cane_weaksmile_cas_close
with charachange



li "人形なら華ちゃんを非難したりしませんからね、結局のところ"



hi "それなら、人形を売っているところを探すのがいいかな？"

show lilly cane_smileclosed_cas_close
with charachange


li "気をつけて見ていただければありがたいです"




hi "構わないよ、でももっと早く言ってくれればよかったのに"




show lilly cane_cheerful_cas_close
with charachange



li "でもそうしたら、久夫さんは自分で考えることはしなかったでしょう？"




"またしてもリリーの言うとおりだ。俺の脳は今、通り過ぎる店の一軒一軒を贈り物の選択肢として見定めている。もしリリーが最初から人形店の話をしていたら、俺はほかのことを一切考えなかっただろう。"


$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

scene bg city_street4
with locationskip



"俺たちは通りをさまようけど、人形店のようなものも、他にプレゼントに良さそうなものも見あたらない。"





"探しものという単純な行為が俺の頭を明晰にする。先週の出来事は徐々に消え去り、俺は華子に贈りものをするのを楽しみにしている……"




"……贈るものが見つかれば、の話だけど。"




hi "望み薄だな。街に来ればなにかしら見つかると思ってたのに。それに、この通りは確かにさっきも歩いたよ"


show lilly cane_oops_cas_close at center
with charaenter



li "なんだかもう諦めたみたいに聞こえますよ、久夫さん"



hi "そうじゃないけど、思っていたより大変だなって"

show lilly cane_smileclosed_cas_close
with charachange



li "あまり狭い考えにとらわれないでください。実際にお店に入って、中を見て回った方がいいかもしれませんよ？"



hi "それが良さそうだな。俺もウィンドウショッピングがうまくいったことなんてなかったし"

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg city_street3 at right
with locationskip



"リリーと俺はもう一度、町中の通りという通りを見て回り、今度は目に留まった店にも入ってみる。ところが結局、特別ふさわしいものはなにも見つからない。"



"華子の好みは、その極度に引っ込み思案な性質のおかげで、どんなに調子のいいときでも聞き出すのは本当に難しいし、俺たちが知ったところでそれに応えるのも難しい。"


show lilly cane_sleepy_cas_close at center
with charaenter


li "少し休憩しませんか？　なんだか息が切れてしまいました"

show lilly cane_sleepy_cas_close:
    ypos 1.05
with charamove

show bg city_street3 at left
show lilly invis:
    xpos 0.8
    ypos 1.05
with dissolvecharamove



"俺は同意して、リリーをガードレールに寄りかからせると、近くの自動販売機へ飲み物を２つ買いにいく。"



"自動販売機ですぐさま自分用にレモネードを買った後、俺はちょっと困ってしまう。リリーの好みがわからないので、当てずっぽうで女の子が好きそうだけどあまり変じゃないもの――いちごミルクを買う。"


show bg city_street3 at right
show lilly cane_weaksmile_cas_close:
    center
    ypos 1.05
with dissolvecharamove


hi "戻ったよ"



"俺はリリーに近づき、彼女が伸ばした腕に紙パックを渡す。リリーがちゃんと手でつかんだことを確認してから俺も手を離す。"


show lilly cane_smile_cas_close
with charachange



"リリーは手先で輪郭を探ってからそれを開け、ためらいがちにすする。その後の満足そうな笑顔で、俺の選択が正しかったことがわかる。俺たちは数分間、そろって静かに飲みながら休憩する。"


$ renpy.music.set_volume(0.2, 0.0, channel="sound")
play sound sfx_phone

show lilly cane_surprised_cas_close
with charachange



"聞き覚えのある柔らかなベルの音が、リリーのいるほうから聞こえてくる。リリーはすぐに謝りながら手をポケットに入れると、携帯電話を引っ張り出す。"


show lilly cane_weaksmile_cas_close
with charachange


li "出ても構いませんか？"


hi "ああ、いいよ。気にしないで"

show lilly back_listen_cas_close
show lillyprop back_cane_close:
    center
    ypos 1.05
with charachange



"リリーは俺にうなずいて礼をすると、向こうをむいて携帯電話をさっと開き、顔の横に持って行って電話に出る。"


show lilly back_smile_cas_close
with charachange



"リリーの声のトーンからすると、電話の相手は友人かなにかなのは間違いない。聞こえてくる会話の断片からすると、単なるうわさ話にすぎないみたいで、俺はその会話からすぐに耳を離す。"





"他にすることもなくて、俺はリリーを見ている自分に気づく。本当に可愛い子で、その容姿が学校での人気ぶりを揺るがすことはないだろう。性格も外見も、華子とリリーはあまりにも正反対なのが興味深い。"



show lilly back_smileclosed_cas_close
with charachange



"数分のあいだ、俺は寄りかかってジュースを飲みながらリリーを見ている。間もなく、リリーは相手に別れを告げて電話を切ると、携帯電話をポケットに戻し、またガードレールに寄りかかる。"


hide lillyprop
show lilly cane_weaksmile_cas_close
with charachange


li "すみません、クラスの友人からでした"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_can_clatter



"俺は缶の中身を飲み干すと、ごみ箱に放り込む。その後すぐにリリーも比較的早く飲み終えて、紙パックを俺に手渡す。"


$ renpy.music.set_volume(0.1, 2.0, channel="ambient")


hi "友達がたくさんいるみたいだな"

show lilly cane_smile_cas_close
with charachange


li "え？"




"リリーは興味を引かれて、俺が話を続けるのを待つ。"





hi "リリーと華子は本当に対照的だと思ってたんだ。リリーがやっている色々なことを華子がするところとか、リリーの知り合いと華子が人づきあいしているところは想像しづらいからさ"


show lilly cane_giggle_cas_close
with charachange



li "本当に華ちゃんのことをよく考えているんですね"




hi "さあね。俺はただ……華子が不思議なんだと思う。もっと華子のことをよく知りたい気がするんだ。簡単じゃないけど"


show lilly cane_weaksmile_cas_close
with charachange



li "まるで華ちゃんとの関係が不安だと言っているみたいですね"




hi "そういうんじゃないよ。ただもっと華子の力になりたいんだ。友達でいるとか、色々と。華子が俺のことをどう思っているのかだってよくわからないし"


show lilly cane_smile_cas_close
with charachange



"こういう話はリリーの気を強く引くみたいだ。華子はリリーに俺のことをなんて言っていたんだろう。"


show lilly cane_smileclosed_cas_close at center
with dissolvecharamove


"俺はガードレールから身を起こすリリーに、なにを思っているのか聞こうとする。"

show lilly cane_cheerful_cas_close
with charachange



li "それでは行きましょうか？"



"その声と表情から、話をはぐらかしているのがわかる。思わせぶりなことをしている自覚は十分にあるはずだ。"





"ため息をついて俺も起き上がると、あたりを軽く見回す。俺たちにはやることがあるんだし、この件は後でまたリリーに聞くとしよう。"



"新聞売り場とコンビニのあいだに小さな店がある。ドアの上にある看板には飾り立てた英字で『Othello's Antiques』とある。"






"通りを歩いているだけでは見落としてしまうけど、俺たちはその場にとどまっているし、俺は目を凝らして見て回っていたから、かろうじて気づけたんだ。"


$ renpy.music.set_volume(0.3, 6.0, channel="ambient")



hi "そういえば、リリー……華子にあげたっていう人形は新品だった？"


show lilly cane_smile_cas_close
with charachange


li "ええ、そうですけど、どういうことですか？"


hi "良さそうな店を見つけたんだ、車道の向こうに"

show lilly cane_surprised_cas_close
with charachange



li "まあ？　何のお店ですか？　おもちゃ屋さんかなにか？"




hi "骨董品屋だよ。たぶん一番いい選択だと思うな"


show lilly cane_satisfied_cas_close
with charachange


li "本当ですか？　この辺りにそんなものまであるなんて知りませんでした"



hi "俺もだよ、最初に来たときは気づかなかった。うまい具合に隠れてたんだ"


show lilly cane_smileclosed_cas_close
with charachange


li "それでは、のぞいてみましょうか"



"この新たな発見によって、俺たちは素早く体のほこりをはらって店に向かう。リリーの手が案内役の俺の肘を探り当てる。"


stop ambient fadeout 0.5

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_storebell
play music music_soothing fadein 0.5
$ renpy.music.set_volume(1.0, 4.0, channel="ambient")

scene bg city_othello at right
with locationchange



"店の中は奇妙な、じゃ香のような匂いがする。内装は店というよりガレージに近い。床じゅうにものが散らかっていて、一見しただけでは整理されている様子はない。"


show shopkeep neutral at center
with charaenter



"店主はそのとても小さな目で、まるで退屈しているかのような視線を俺たちに向ける。ひどく疲れた表情をしていて、その服装もはっきりいって時代遅れだ。彼は丁寧にこちらに会釈すると、読んでいた本に戻る。"


hide shopkeep
with charaexit



"リリーが俺の腕をぎゅっと抱きしめる。俺は華子へのプレゼントを見逃さないようにすることと、リリーがうっかりなにかにぶつからないようにすること両方に気を配らなければいけないことに気づく。"



show bg city_othello at center
with charamove_slow



"それをこなすのは実に難しい。雑然とした店内の配置に加えて、いろんなものが棚から突き出していたり、家具の上に乗っていたりするせいだ。それでもついに人形やテディベアが満載された古い机にたどり着く。"




hi "ここが正解だと思う。思いつく限りのどんな種類の人形もあるんじゃないかな"


show lilly cane_smileclosed_cas_close at center
with charaenter



li "それなら、選ぶのも簡単になりそうですね。なにかひとつ取ってくれませんか、久夫さん？"




"そうくると思った。心のなかに華子を思い浮かべて、目の前の、どの人形が華子にぴったりか想像してみる。"




"そのコレクションの上を視線がさまよう。どれも申し分ないように見える。あまりに多くの種類があって驚かされるけど、最終的にそのうちのひとつが目に止まる。"



hi "これならどうかな？"




"俺は少なくともいくらか値段は手ごろな、小さな陶器の人形を手に取る。ビクトリア風の緑のドレスと、ブロンドの髪に小さな茶色の帽子をかぶっている。なんだかリリーみたいだ。"

show lilly cane_listen_cas_close
with charachange





"そっとリリーに人形を手渡すと、リリーは少し集中している表情をしながら、繊細な手つきで人形に触れる。"


show lilly cane_smile_cas_close
with charachange



li "確かにすてきな感触です。久夫さんは、華ちゃんにはこれが合っていると思いますか？"



hi "きっとね。華子の部屋にもぴったりだと思う"

show lilly cane_smileclosed_cas_close
with charachange



li "それなら久夫さんの判断を信じます。久夫さんも他に何か買いますか？　それとも共同の贈りもの、ということにしますか？"




hi "うーん、どうしようかな。俺からもなにか贈りたいとは思うけど、人形をもう一つ贈るのはあまりいい考えじゃないと思う。もしかしたら……"




"店のなかを見回しているうちに声が小さくなってしまう。俺たちからそう遠くない位置にライティングテーブルがあって、その上に置かれている装飾された箱に目が止まる。"




hi "待ってて、気になるものがある……"


show lilly cane_ara_cas_close
with charachange



li "あらあら、早かったですね"





"俺は用心深くガラス製品の山を通り抜けると、箱を手に取る。木でできた側面には、城の周囲で起こる古い戦いの様子が彫刻されている。"



"ところが上蓋はあまりにも見慣れたものだ。光沢のある黒と白の四角い木が互い違いに並べられている。"



sk "それはとてもいいものだよ。外国のチェスセットだ"





show bg city_othello at bgleft
show lilly cane_smileclosed_cas_close at twoleft
with dissolvecharamove

show shopkeep neutral at tworight
with charaenter


"店主がとつぜん現れて、俺は少し驚く。近づいてくるのがまったく見えなかった。"



"俺たちがなにを探しているのかすら分かっていないように見えて、手助けをしてくれているんだろう……さもなければ俺たちが万引きするんじゃないかと疑って、目を離さないようにしているのか。"




hi "俺……友達にあげるプレゼントを探してるんです"


show shopkeep happy
with charachange



sk "そうか。それなら、このチェスセットはうってつけだ"




"突然思い至る。とても良さそうに見えるチェスセットだけど、ここは骨董品屋だ。割引価格とはいかないだろう。"



hi "どれくらい古いものなんですか？"

show shopkeep neutral
with charachange


sk "レプリカだからね、私が見るに、せいぜい５年といったところだろう"


hi "そうなんですか。おいくらですか？"

show shopkeep thinking
with charachange



"店主は答える前に少し考え込む。ちょっと面食らう。"


show shopkeep neutral
with charachange



sk "今なら７０００円でどうかね"




"俺は少し尻込みする。そんなにするとは思ってなかった。でもこの品は完璧だ。一方で今の値段は、店主が俺に払えそうな額を見事にはじき出したことの証なのかもしれない。"




hi "５０００円にできませんか？"

show shopkeep thinking
with charachange


sk "５５００円、それ以上は駄目だ"



hi "分かりました。そうだ、あの人形もお願いします……"


show shopkeep neutral
with charachange



"店主は俺の肩を見越すと、リリーとその手に取られた人形に注目する。目を細めると、明らかにしばらく時間をかけて態度を変える。"



"その間に、店主がわずかに顔をほころばせる。"



sk "ああ……"



"多分、店のなかにあるものすべてがレプリカというわけではないんだろう。"


show shopkeep thinking
with charachange


sk "本当にその人形がほしいのかい、お嬢さん？"

show lilly cane_smile_cas_close
with charachange


li "ええ、友人の判断を信じます"

show shopkeep surprised
with charachange



sk "よく見て……あ、いや、失礼した……"


show lilly cane_smileclosed_cas_close
with charachange



li "お構いなく。できればラッピングをしていただきたいのですが"


show shopkeep neutral
with charachange


sk "ああ、構わないが、それは２万円なんだ……"





"リリーはハンドバッグに手を入れると、新札らしき５０００円札を４枚取り出す。"


show lilly cane_cheerful_cas_close
with charachange


li "はい、２万円です"

show shopkeep thinking
with charachange


"店主はうやうやしくお金と人形を受け取ると、カウンターに向かう。俺はリリーの腕を取ってそこまで案内する。"


hi "本当にいいのか？"

show lilly cane_smileclosed_cas_close
with charachange



li "構いませんよ。私は……必要なお金はありますから。さっきも言いましたが、久夫さんの判断を信じてます"




"２つのことに対してなんだか悪い気がしてくる。俺の勧めでリリーに大金を使わせてしまったことと、俺の選んだプレゼントは値打ちが足りないような気がしていることにだ。"




"そうはいっても、リリーはお金のことに言及するときは、いつもどこかばつが悪そうに見えるな……"


show shopkeep neutral
with charachange



"俺も同じように店主に品物とお金を渡す。店主はお金をレジにしまうと、人形をラッピングし、続いて同じようにチェス盤に取り掛かる。"




"やがて店主はラッピングを終えて、プレゼントを俺たちに渡してくれる。"


show shopkeep happy
with charachange



sk "帰り道に気をつけてな。是非またおいで"




hi "どうも"


show lilly cane_smile_cas_close
with charachange


li "本当にありがとうございました"


"帰ろうとする俺たちに、店主は深々と頭を下げる。"

stop music fadeout 6.0
$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0

scene bg city_street3
with locationchange

show lilly cane_weaksmile_cas_close at center
with charaenter



li "丸１日かかってしまいましたね。でも、ようやくいいものが見つかりました"



hi "そうだな"



"そのプレゼントもいまやきれいに包まれていて、俺は華子にそれを渡すのが待ちきれなくなっている。これが贈りものを買うときの普通の反応だ。受け取る人が実物を見たときの反応を知りたいんだ。"




"それに、華子のもとへ戻って、その様子を自分の目で確かめたいという気持ちもある。"



hi "さて、そろそろ戻ろうか？"

show lilly cane_smile_cas_close
with charachange


li "そうですね。今日はたくさん歩いたので、寮に戻って休みましょう"


"リリーのいうとおりだ。店を探す必要はもうないし、足も棒のようになってしまった。"


hi "それじゃあ学校に戻ろうか。俺も早く休みたいよ"



"リリーが腕を伸ばしてきて、俺もリリーと腕を組む。俺たちは一緒になってバス停へと向かう。"

stop ambient fadeout 2.0

scene black
with dissolve


label jp_H14:

play music music_pearly fadein 5.0

scene bg school_scienceroom at right
with locationchange


"武藤先生はいつものように、教科書から方程式や公式をひとつひとつ、やる気のない声で読み上げる。"



"自分の教えていることに胸を高鳴らせているのかもしれない。先生は時折、資料にのめり込むかのように、場違いな情熱の火花を散らすことがある。"




"ほぼ毎日がそんな感じだ。俺たちが教わっていることは極めて単純なので、先生に集中し続けるのがどんどん難しくなっていく。そのうちに足がまた痛み出してきて、余計に集中できなくなる。"




"昨日、リリーと連れ立って街を歩いたことを後悔しそうになっている。"




"病院を出てから、俺はほとんど運動をしてこなかった。近くの店まで往復くらいじゃ運動のうちに入らない。"
"山久に来てすぐの頃に笑美が誘ってくれてはいたけど、俺はもう以前の健康状態に戻るという考え自体をほぼあきらめていた。"




"街を何時間も歩き回ったせいでこんなに痛みが出ているのは間違いないだろう。気分が沈むし、発作が起きて以来、自分にできなくなったもう一つのことを思い出してしまう。情けなくなってくる。"


show muto normal at twoleft
with charaenter


mu "次は……池沢？"

show hanako defarms_shock at tworight
with vpunch



"先生が華子に質問をするとは妙だけど、前例がないわけじゃない。華子は驚いてぴょんと立ち上がると、すぐに視線を先生にくぎ付けにする。"



"先生が華子を呼ぶのは稀なことだと、華子自身もわかっているから、クラス中の目が華子に向く。こうなってしまうと、誰かに視線を合わせようなんて大冒険はできるわけがない。"

show hanako def_worry
with charachange


ha "は……はい"



mu "この酸化還元反応の例では、メタンが反応して燃焼することで、もうひとつ、ここには載っていないものが発生する。それは……？"


show hanako emb_downtimid
with charachange



"つまらない質問なのに、華子は集中を切らすまいとしているかのように下唇を小さく噛んで、しばらく臆病そうに待ってから答える。"


show hanako emb_timid
with charachange


ha "ええと……ね、熱？"

show muto smile
with charachange


mu "その通り。投じたよりももっと大きい熱を発する反応、これが発熱の反応だ"

show hanako invis:
    ypos 1.1
with dissolvecharamove

hide hanako
with None



"先生がうなずくのを受けて、華子は再び席について安堵のため息をつく。"



"落ち着かないスタートだけど、まあこんなものか。"



"華子の誕生祝いに、いつも引きこもっている華子の部屋や紅茶の部屋とは違う場所へ連れ出せたらいいだろうな。これまでの前進ぶりを見れば、街へ出るのにそう問題があるとは思えない。"


show muto smile at center
show bg school_scienceroom at center
with charamove


mu "さて、この授業の残りの時間は１２章の問題を３、４人のグループでやってもらいたい。わからないことがあれば聞いてくれ"

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 8.0

show muto invis:
    ypos 1.1
with dissolvecharamove

hide muto
with None



"武藤先生はフォルダーからルーズリーフを何枚か取り出すと、教卓に戻って自分の仕事を始めてしまう。そういうことは授業の最中じゃなくて、授業が終わったあとでするものだと思ってたけど。"


show shizu invis_close:
    tworight
    xpos 0.8
show misha invis_close:
    twoleft
    xpos 0.2
with None

show shizu behind_blank_close at tworight
show misha hips_smile_close at twoleft
with dissolvecharamove



"とにかく、俺は右のほうを見て、グループを組む相手を探す。２つの笑顔が俺の近くに浮かんでいて、俺の意見はたいして尊重されそうにない。"



hi "俺たちがグループになるみたいだな"

show misha hips_grin_close
with charachange



mi "ひっちゃ～ん！　わたしたちと一緒にやりたいの？　やった、やったあ～！　よかったよ～！　久々だもんね～！"


show shizu behind_blank_close:
    ypos 1.09
show misha hips_smile_close:
    ypos 1.09
with dissolvecharamove



"教室に机を引きずる雑音が響きはじめると、静音も同じように机を俺の机の前に移動させる。不愉快なほどやかましいこの教室の騒音が聞こえないっていうのは運がいいよな。"





"正直にいえば、結果として静音やミーシャと一緒にやることになったのは良かったと思う。俺と静音はこの科目が結構得意だし、ミーシャは……とても字がきれいだ。"


show hanako silhouette behind shizu at center
with charaenter



"ミーシャのほうを向くと、その後ろに背の高い影が見える。ミーシャもその人影に気づいて、暗い色の髪をしたこちらを見ている人物のほうへ振り返る。"



show shizu behind_blank_close at Position(xpos=0.8)
show misha perky_smile_close at Position(xpos=0.2)
show hanako basic_worry
with dissolvecharamove



mi "ごきげんよう、は～なこ！"



show hanako emb_timid
with charachange



ha "あの……こんにちは……"




"俺とミーシャの視線を追って、静音もようやく華子に気づく。すぐにミーシャの肩を小さく叩いて注意を引くと手話を始める。"


show shizu adjust_happy_close
with charachange


shi "……"

show misha sign_smile_close
with charachange


mi "しっちゃんがね、グループを探してるなら入ってもいいって～！"

show hanako emb_downsmile
with charachange



"この申し出に、華子は下を向いてわずかに赤面する。クラスの中では俺たち３人が一番なじみがあるから、華子が最初に俺たちのところへ来るのは自然なことだ。"



"そうはいっても、華子がグループに混じろうとするなんて滅多になかったことだろう。"

hide hanako
with charaexit

show shizu behind_smile_close:
    tworight
    ypos 1.09
show misha hips_smile_close:
    twoleft
    ypos 1.09
with dissolvecharamove



"華子が机を持ってくるために少しの間その場を離れ、静音とミーシャは華子が背を向けたとたんにぐるりと俺のほうに振り返る。"



show shizu adjust_happy_close
with charachange


shi "……"

show misha perky_smile_close
with charachange


mi "また一緒だね、ひっちゃ～ん！　最近全然遊んでくれないよね……"



hi "どうしてだろうな？　２人ともいつだって何かしら下心がありそうだからな"


show shizu basic_frown_close
with charachange


shi "……"

show misha hips_frown_close
with charachange




mi "ひどいよ、ひっちゃん……まるでわたしをばかにしてるみたいだよ～！"



show misha hips_grin_close
with charachange


mi "でも～！　ひっちゃんのことだからね、そんなの冗談だってわかってるよ！"


hi "いいユーモアセンスだな。もし誰かが他人の優しさにつけ込んでいたっていうならひどい話だけど。なにか仕事を手伝わせたりとかさ"


show shizu adjust_smug_close
with charachange


shi "……"

show misha cross_laugh_close
with charachange


mi "わはは～！"



"俺が挑発を受けて立つ気があることに少し驚いたのか、静音が一瞬興奮したように見える。でも華子が戻ってくるのを見ると、微笑んで後ろへ下がる。今日の心理ゲームは早めに終わるみたいだ。"


show hanako invis_close behind shizu at center
with None

show shizu behind_blank_close at Position(xpos=0.85)
show misha perky_smile_close at Position(xpos=0.15)
show hanako emb_downtimid_close at Position(ypos=1.09)
with dissolvecharamove



"華子はミーシャと向かい合うようにそっと机を置く。その目はじっと下を向いている。俺は教室内を見回してみるまで、それがどうしてなのかわからなかった。"




"ほとんどの生徒はグループを組むのに忙しいけど、何人かは物好きそうな視線を華子に向けている。この距離だと、その関心が見るだけにとどまっているのか、噂話もしているのかはわからない。"




"妙だな。華子がグループワークを嫌がって教室から逃げ出してしまってもみんな平然としているのに、こうやって努力している華子を今度は悪いことでもしたかのようにじろじろ見ている。"




"俺たちはみんなで態勢を整えて、４つの机をくっつけてできた広いスペースに教科書とワークシートを広げる。やがてクラスの全員が作業に取りかかり始める。"



show misha sign_smile_close
with charachange



mi "ねえ、華子～！　一緒になれてよかったね～"


show hanako basic_distant_close
with charachange


ha "う、うん"

show shizu adjust_smug_close
with charachange


shi "……"

show misha hips_grin_close
with charachange



mi "ひっちゃんが最近わたしたちのことを避けてるのはあなたのせい～？　しっちゃんはちょっと感じ悪いって言ってるけど、でもひっちゃんが可愛い女の子と一緒に過ごしたいって思うのはわかるよ～！"


show hanako cover_worry_close
with charachange


ha "そ、そういうわけじゃないと思うけど……"


"慣れない勘繰りをされて、華子はそわそわしはじめる。"



"普通の人ならここで会話は終わりだろうけど、ミーシャは華子と正反対のタイプだ。たとえば、ミーシャは相手の表情や雰囲気をまったく読みとれないけど、華子はそういうものに過剰なくらい敏感だ。"




"そのおかげで、俺が割り込んでもっと楽な話題に会話を持って行く隙もないくらい、ミーシャはすごい勢いで華子を質問責めにする。"


stop music fadeout 7.0

show misha hips_smile_close
with charachange



mi "ホント～？　そっか～！　昨日はひっちゃんと一緒じゃなかったんだ？"


show hanako emb_downsad_close
with charachange


ha "う……ううん……"



"隠し事もとっくにばらされてしまった気分だ。リリーは誕生日パーティーを計画してることはもちろん、プレゼントを買いに行っていたことも華子には知らせないようにしていた。今そのことがばれるのはまずい。"



hi "ああ、俺……他のことしてたんだ。つまりさ……"

show shizu behind_blank_close
with charachange


shi "……"

show misha sign_smile_close
with charachange



mi "ホント～？　あんなにわたしたちを邪険に追い払うほど大事な用事ってなんだったのかな～！　華子と一緒にいるんじゃなかったら、一体なんだったのかな～？　これは興味深いよ……"




"これじゃまるで尋問じゃないか。本人にそんなつもりがなくても、ミーシャがこうして他人にプレッシャーを与えられるということが驚きだ。"


show hanako defarms_strain_close
with charachange


ha "リ、リリーと一緒にい、いたの？"

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")



"出し抜けに、華子が正解にたどり着く。ひどく物静かで恥ずかしがり屋だけど、勘も鋭いんだ。"



hi "な、なんでそうなるんだよ？"

show hanako emb_sad_close
with charachange



ha "き、昨日リリーが同じようなこと言ってたから"


show shizu basic_happy_close at Position(xpos=0.8)
with charachange


shi "……"

show misha hips_smile_close
with charachange


mi "怪しいな～！　ひっちゃ～ん！　ひっちゃんに説明を求めます！"



hi "なあ、課題をやらなきゃいけないんじゃないのか？"


show misha cross_smile_close
with charachange


mi "でも～！　不可解だよね……華子も知りたがってるよ～！"



"俺は華子のほうに振り返る。実際その通りで、顔を見れば華子も知りたがっているのははっきりしている。それに、もう説明なしで見逃してもらえる状況ではなくなっているみたいだ。"




"心のなかでリリーに謝る。リリーは本当に秘密にしておきたかったんだろうけど、もうこれ以上は無理だ。"




"色々な相反する感情がどっとわき上がるのを感じる。あまりにごちゃ混ぜになってしまい、識別するのが大変だけど、落ち着いてしゃべろうとしても、頭の中でそれがぶつかり合う。"




hi "わかった、言うよ。リリーと一緒に街に行ったんだ。でもお前らが考えてるようなことじゃないぞ"



hi "リリーと俺は……その……華子の誕生日プレゼントを、だから……"



"言ってしまった。でも、思っていたより華子はこのことを好意的に受け取ってくれたみたいだ。"


show misha perky_confused_close
show shizu adjust_blush_close at Position(xpos=0.85)
show hanako emb_downtimid_close
with charachange



"沈黙が俺たちのグループを覆い、静音とミーシャは決まり悪そうにお互いを見合っている。こんな結果になることは予測していなかったんだろう。"




"ミーシャが華子を見上げて謝ろうとして、そのまま固まる。華子は今にも泣き出しそうな表情で、身じろぎもせずに机の真ん中を見つめている。今のをよく受け取ってくれたというのは間違いだったみたいだ。"


show misha perky_sad_close
with charachange


mi "華子？　ごめんね……"



"何秒か間が空くけど、華子は頭を上げて首を振る。"



show hanako emb_timid_close
with charachange


ha "だ、大丈夫……"



"その表情はどこか変で、とても疲れているかのようだ。不自然だけど、心配するような感じじゃない。誰もこれ以上会話を続けるつもりもなく、俺たちは教科書を開いてグループワークに取りかかる。"


play music music_rain fadein 12.0
$ renpy.music.set_volume(0.5, 5.0, channel="ambient")

show shizu basic_normal2_close at Position(xpos=0.8)
with charachange


"退屈なものだ。あてがわれた方程式には少し時間がかかるけど、ほとんどがうんざりするほど機械的に進みそうだ。"



"しかも、思っていたよりスムーズに進んでしまうものだから、気まずい空気が俺たちを覆ってしまう。それでも俺たちは先に進んでいく。"




"静音の表情を見ても、この課題に対して俺と同じような見通しを持っているのがわかる。そして俺たちは２人揃って計算結果を書き留める。"


show misha perky_confused_close
with charachange



"かたやミーシャは唇をしわくちゃにして、俺たちのしていることを理解しようとしているのが明らかだ。"
"華子は静かに傍観して、俺たちの書き出したものや俺の言うことを理解している。ふだん先生が話しているときに見せるのと同じ表情だ。"






"華子の出席が良くないのが本当に残念だ。華子みたいに情報を取り入れられるなら、ちゃんと授業に出ていれば相当いい成績が取れるだろう。だから静音は華子にこんなに厳しくあたるんだろうか？"


show misha perky_smile_close
with charachange



mi "ねえ華子、これわかる～？"




"ミーシャは華子のほうを見るけど、本心は手助けを求めているというより、同類を見つけたがっているだけのように思える。"


show hanako emb_downtimid_close
with charachange


ha "私……うーん、そんなには……たぶん……"


"答えるだけでそんなに緊張するものかと驚いたけど、華子は座りなおす。息をついて、上半身と頭を縮ませる姿はしぼんでいく風船を思わせる。"



hi "大丈夫か？　良かったらもう１回説明するけど"



"華子はわずかに頭を振る。ああ言ってはいるけど、華子にはこれ以上説明はいらないだろうと思う。"
"そんなことには何一つ気づかず、ミーシャがすばやく割り込んでくる。結局俺はどうやってこの答えにたどり着いたのかをひとつずつ、ゆっくりと説明する。"





"こうやっていると、このやり方が全員にとって機械的ではないかもしれないけど、内容を理解している俺には機械的に感じることに気づく。そのことに俺は満足感を覚える。"





"ミーシャがなにを閃いたか握りこぶしを手のひらに打つと、俺はまたいい気分になる。俺の説明をちゃんと理解したミーシャは、次の方程式を最低限のアドバイスだけで、自分一人で解くことができた。"




"このやりとりの間ずっと、華子はいつになく無反応だ。"




"普段からとても静かではあるけど、それでも目の前にある教室の様子に定期的に目をさまよわせていたり、不安げに手を動かしたり、定期的に肩を揺らしているところは目にすることがあった。"




"すっかり見慣れているそんな小さな動きが、今は全く見られない。まったく動かない人間というのはどう見てもおかしい。ミーシャでさえなにか変だと察している。"


show misha perky_confused_close
with charachange


mi "華子？　大丈夫？"


ha "う、うん……"


hi "本当に大丈夫か？"

show hanako emb_downsad_close
with charachange


ha "大丈夫だよ"



"今度は少し強い口調で言うけど、そのまま向こうを向いてしまう。そんな言い方では余計に怪しくなるけど、同時にそれ以上このことを話したくないと思っているのは伝わってくる。"




"さっきの非常に気まずい会話からまだ完全には立ち直れていないこともあって、俺もそう深追いしたくはない。"




"俺たちは元の作業に戻って、回答について疑問が浮かぶたびに議論する。でも時間が経つにつれて、華子が全く口を開いていないことに気づく。もどかしい気分だ。せっかくここまで良くなってきたというのに。"




"リリーがあれだけ秘密にしたかったサプライズをばらしてしまった静音とミーシャがなんだか腹立たしくなってくる。俺のせいでもあるのはわかってる。どうにか秘密にしておくことだってできたかもしれない。"


show shizu behind_frustrated_close at Position(xpos=0.85)
with charachange



"静音は華子が黙り込んでいることには気づいていて、しかもいらだっている。顔を見ればわかる。静音は耳が聞こえないのに、華子のいつにない静かさにミーシャよりも早く気づいたのは妙な感じだ。"


show shizu adjust_frown_close
with charachange


shi "……"

show misha sign_smile_close
with charachange



mi "なんだかすごい静かだね～。華子ももっと作業しなきゃ～！　そのうちわたしたちも、もっと大きな計画をやるかもしれないんだよ。あとでアイスやケーキで打ち上げができるくらいのね"
mi "でもいつまでもそんな態度じゃ、誘ってあげないよ～！"




"華子をからかって殻から引っ張り出そうとしているんだ。でもそんなやり方が華子に効くとは思えない。余計に困らせるだけだ。"




hi "２人とも、そんなにからかうなよ"


show shizu behind_smile_close
with charachange


shi "……"

show misha hips_smile_close
with charachange



mi "ひっちゃん、悪気があって言ってるんじゃないよ～！　それにしっちゃんは誰が相手でもからかうって言ってるよ"


show misha perky_smile_close
show shizu behind_blank_close
with charachange



"でもそれきり２人はからかうのをやめて、ミーシャは俺に質問をしてきて話をそらす。ミーシャが解いている問題の難しさを見ると、今のが巧みなはぐらかしなのか、単なる偶然なのかは判断がつかない。"




"俺がミーシャに説明をする間、静音がずっと反論するものだから、必要以上に時間がかかる。そしてミーシャもすぐに俺よりも静音を信じてしまう。静音の話を通訳し忘れてしまうくらいすぐに、だ。"



hi "なあ、もう時間になるぜ。少し急がないと"

stop music fadeout 4.0

show misha perky_confused_close
with charachange



mi "ひっちゃ～ん！　なんだかしっちゃんみたいな言い方だよ……"




hi "時計を見ただけでそれかよ？　まったく、本当にそれだけでか？　時間をチェックしてるだけで、俺は生徒会長になるってわけかよ？"


stop ambient fadeout 4.0

$ ksgallery_unlock("evul hanako_breakdown_down")
scene evbg hanako_breakdown:
    truecenter
    1.0
    zoom 1.05 subpixel True
    easein 8.0 zoom 1.0
show evfg hanako_breakdown_down:
    truecenter
    1.0
    zoom 1.1 subpixel True
    easein 8.0 zoom 1.0
with silentwhiteout

play music music_tragic fadein 8.0



"華子の進み具合を見ようと、その机に目を向けて凍り付く。俺たちのワークシートは計算式でいっぱいなのに、華子のそれはまだ半分しか埋まってない。この２０分間、華子はなにも書いていなかったみたいだ。"





"それに気づいたとき、俺は自分の馬鹿さ加減に自分を蹴り飛ばしてやりたくなる。"




"華子のように繊細な人間が、あんな出来事をそう簡単にやり過ごせるわけがないと理解してなきゃいけなかったんだ。でも俺は気まずい状況を抜け出すことに夢中で、気づくことができなかった。"




"華子はこの３０分の間に徐々に心を閉ざしていった。俺はそれに気づきようもなかった。ペンは手に持ったままだけど、普段のようにそれをゆっくりと回したりはしない。華子は全く身動きをしていない。"


$ ksgallery_unlock("evul hanako_breakdown_up")
scene evbg hanako_breakdown:
    truecenter
    1.0
    zoom 1.0 subpixel False
show evfg hanako_breakdown_up:
    truecenter
    zoom 1.0 subpixel False
with charachange



"静音やミーシャ、そして俺の視線を感じとって、華子が少しずつ距離を離そうとする。それがなければ、華子がまだ意識を保っているかどうかも見分けられなかった。"
"俺たちは視線をそらす。少なくとも俺にとっては、こんな状態になってしまったことへのやましさのためだ。"




"外側から見ると華子はほとんど完全に停止してしまっているけど、内側ではまた別の事態が起きているのはわかっている。"





"いったいなにが華子をそこまで萎縮させるんだろうか。まるで自ら消え失せることを望んでいるかのようだ。"




"今ではクラスの全員が、作業を仕上げる合間に華子をちらちらと盗み見ている。"




"ミーシャがどうしたのか聞こうとするけど、それじゃ余計にひどくなるだけだ。華子が椅子にくぎ付けになってなければ、きっと今すぐに教室を飛びだしているだろう。"


$ ksgallery_unlock("evul hanako_breakdown_closed")
show evfg hanako_breakdown_closed
with charachange



"ミーシャの問いかけは教室中に響きわたるほど声が大きい。それがどれほど華子を困らせているかは想像もつかないので、俺は一瞬、ミーシャをいさめようと構える。"



"もちろんそんなことをすれば、状況がさらに悪くなるだけだ。"



"華子はもっと強くなれたと信じていたし、実際そうなったけど、まだ十分じゃなかったし、俺も過信していたんだ。いま、華子は教室の中央でひとり怯えきっている。"
"しかも俺が華子のためになにかすれば、さらに周囲の注目を引いてしまう。"



"ひどく腹立たしい。ミーシャが気をもみ、静音でさえくちびるをかんでいる。"



"３人ともこの状況に対処できないので、俺は先生を呼ぶことにする。俺たちよりはいい判断を下してくれるだろう。"




"顔を上げて先生と視線を合わせ、身振りだけでこちらに来てもらうよう伝える。できる限り騒ぎは起こさずに済ませたかった。これ以上華子に注目が集まることは何としても避けたい。"




"華子にも俺たちのグループが、特に華子本人がクラス中から注目されているのがわかっているはずだ。何か問題があれば、華子が原因に違いないとみんな知っているからだ。"




"みんな華子のことを知っていて、みんな真っ先にその結論に飛びつく。さぼり癖のおかげで、この普通でない山久という場所にあってさえ、華子は普通の生徒じゃないというレッテルが貼られてしまっている。"




"どれだけ華子があんな風にじろじろ見つめられていたか、見当もつかないだろう。あまりにクラスの連中から凝視されるから、ああやって人の視線を恐れて、萎縮するようになってしまったのかもしれない。"




"武藤先生が華子のところへやってくるまでの時間は永遠にも感じられたに違いない。華子はいまにもその場に崩れ落ちそうだ。"


scene bg school_scienceroom
show shizu behind_blank_close:
    tworight
    xpos 0.85 ypos 1.09
show misha perky_sad_close:
    twoleft
    xpos 0.15 ypos 1.09
show hanako emb_downtimid_close:
    center
    ypos 1.09
show muto irritated behind shizu at tworight
with dissolve



"先生は静かにどうしたのかと俺たちに聞くけど、華子を見て言葉を切る。"


show misha perky_sad_close
with charachange


mi "どうしよう……驚かせちゃったのかな……？"

show muto normal
with charachange



mu "心配するな"



"先生はミーシャを落ち着かせると、身をかがめて華子の顔をまっすぐ見据える。"

show muto smile
with charachange


mu "池沢、どうかしたのか？"



"優しく、静かな声だ。クラス中が華子の異常に気づいた今、みんな華子の周囲で普段らしからぬ行動をしている。"


show muto smile_close
with characlose



"華子はなにも返事をしないので、先生は優しく華子の肩に手を置く。"


show hanako emb_downsad_close at centertremble_sit
with charachange



"先生に触れられて、華子は身を振るわせはじめるけど、やはり顔を上げない。机の上の方程式を見つめ続けている。視線の焦点はまるで定まっていなくて、式も何も見えていないように思える。"




"さらに状態が悪くなっている。ほんの１時間前まで、華子は先生とごく普通に話ができていたはずだ。"


show muto irritated
show hanako emb_downsad_close:
    center
    ypos 1.09
with charadistant



"先生は立ち上がりながら顔をしかめる。その表情もさっきまでとは変わっていて、先生でさえこの状況には動揺しているみたいだ。"


show muto normal
with charachange



"先生は自分を落ち着かせるために一度息をつくと、とても静かな声で話し出す。こんなに早く事態を制することができるのはさすがだと思う。"




mu "それだけか？　じゃあなんともないんだな？"


play ambient sfx_crowd_indoors fadein 8.0



"誰にともなくそう言う。でも、その言葉には華子を遠巻きに見ている生徒たちのほとんどを振り向かせて、元の作業に戻らせるほどの説得力がある。"




"先生は左右を素早く見やる。まだ俺たちの周りの机で、こちらを珍しそうに見ている奴らもいるけど、それをのぞけば俺たちは注目の的になるのは避けられたみたいだ。"


show muto smile
with charachange



"先生と同じようにしている俺に気づくと、いつもの堅苦しい微笑を見せる。"




mu "今すぐ池沢をここの生徒たちから離れたところに連れて行くのが良いと思う。それが池沢のためだ"




mu "中井、それに羽加道。池沢を教室の外に連れていってやってくれるか？　俺がみんなを落ち着かせておく。だから池沢以外のことは心配するな。頼むぞ？"


show misha sign_confused_close
show shizu behind_blank_close
with charachange



"ミーシャのほうを向いて、静音に今の指示を通訳させようとするけど、ミーシャはすでに通訳をし終わっていた。見る限りまだ茫然としているのに、ほとんど考えずに手話ができてしまうというのは驚きだ。"


show muto invis
show misha perky_confused_close
show shizu behind_blank_close:
    xpos 0.85
    ypos 1.0
with dissolvecharamove

hide muto
hide shizu
with None

show shizu behind_blank_close behind hanako:
    tworight
    xpos 0.85
    ypos 1.0
with None



"うなずくと、静音と俺は立ち上がって華子の両側に移動する。武藤先生は一歩退いて俺たちを通すと、俺たちの後ろの机にいる、今の状況についてぶつぶつ言い始めた生徒たちに話しかける。"



show hanako emb_downsad_close at center
with charamove



"俺たちはお互いに目を合わせてから、揃って体をかがめて、それぞれ片方の腕を肩に回して持ち上げる。"


show hanako emb_downsad_close:
    twoleft
    xpos 0.35
show shizu behind_blank_close at tworight
show bg school_scienceroom at bgleft
show misha invis_close at Position (xpos=-0.1)
with dissolvecharamove



"２人とも、うっかり華子を傷つけないようにゆっくりと歩きはじめる。なるべく平静を装ってはいるけど、先生がみんなの気を引いていてくれなかったら、俺たちはもっと多くの視線に囲まれていたはずだ。"




"ようやく、そしてありがたいことに、俺たちはドアのところへたどりつき、通り抜ける。"


stop ambient fadeout 0.5

scene bg school_hallway3
with locationchange



"表には誰もいないので、俺たちは廊下を下っていく。教室にいたときよりも特に気分が良くなっているようには見えない。俺は華子に、とりあえず座りたいかとたずねる。"


show shizu adjust_happy_close at tworight
show hanako emb_downsad_close:
    twoleft
    xpos 0.35
with charaenter



"しばらくの間、俺たちはその場にとどまって華子がなにか言うのを待つ。静音は恐る恐る華子の肩を小さくこするけど、何の反応もない。"


show shizu behind_smile_close
with charachange



"静音がもう一度試すと、やっとのことで華子は頭を小さく振る。２人とも華子を見ていたので、その動きにはすぐに気がつく。"


show shizu adjust_happy_close
show hanako emb_sad_close
with charachange



"静音がもう一度手を肩に乗せると、華子が意識を取り戻して顔を上げる。俺たち２人のひどく不安と心配に満ちた顔がそれに向き合う。"




"華子はしばらく、黙って俺たちを見つめる。最初はパニックを起こしたり、なにか突飛なことをしたりしないか心配だった。"
"でも、華子の表情が生気のない虚ろな目から、いつもの引っ込み思案で臆病な目つきに変わっていくのを見ると、無用な心配だったとわかる。"


show hanako emb_downtimid_close
with charachange



"華子は言葉もなく頭を垂らすと、ごまかすように目を左右に揺らす。戸惑っているというか、むしろ恥じ入っているように見える。"




"なにか、どんなことでもいいから、助け船を出してやりたい。でも俺にはできない。なにが起こったのかも、なにが原因だったのかもわからない。自分の無力さが、全く役に立てないことが情けない。"


show shizu basic_normal2_close
with charachange



"静音はため息をつくと俺を見る。口で言わなくても、何を尋ねているのかはわかる。"




hi "華子をナースの所に連れて行くよ。それでいいか？"




"手振りで俺の意図を伝えようとするけど、ちゃんと静音に伝わってはいない感じがする。"


show shizu behind_frustrated_close
with charachange



"静音は俺の手振りを見てつまらなそうな表情を浮かべる。俺の思ったとおりだった。"


show shizu adjust_frown_close
with charachange



"断固とした動きで宙に指を突き出すと、まずは俺に、次に華子に、そして階段のほうを指差す。そして俺がうなずくのを待ってから、静音自身と、続いて教室のドアを指差す。"





"こういうことは俺よりもずっと上手なんだな、と思う。"


show shizu behind_blank_close
with charachange



"結局その考えは俺と全く同じなので、俺は静音に向かってうなずく。かなり長いあいだ華子を見つめてから、ようやく静音はこの場を離れる。"


hide shizu
with dissolve



hi "ナースのところへ連れて行くけど、いいよな？"


stop music fadeout 4.0



"華子は何も言わず、うなずきもしないけど、自分の力でその場に立ち上がる。そして俺が歩きだすと、素直についてくる。強硬症患者について読んだことはあったけど、今俺はその実例をこの目で見ているんだ。"



"華子はひどく疲れたように見える。あんなことが起きたあとでは無理もないけど。"

stop music fadeout 1.0
scene bg school_nurseoffice
with locationskip



"華子が無言で靴を脱いで医務室のベッドに横たわってから、ナースと俺はその場を離れる。"


play music music_hanako fadein 0.3




"ナースは後ろのカーテンを閉める。２人揃って椅子に腰掛けると、俺は静かに、そして念入りに、起こったこと全てをこと細かに伝える。"





"俺はなにが起きたのか知りたいし、ナースなら誰よりもそれをわかっている可能性が高い。"


show nurse concern at center
with charaenter



"俺の説明の端々で、ナースは相槌を打つ。話し終わると同時に困ったような表情を見せる。"



nk "それにずっと立ち会ってたなんて、とても大変だっただろうね"




hi "大変じゃなかったと言ったら嘘になりますけど。気が遠くなっていたのはわかりました。でもどうしてそんなことが起きたのか、どうして華子がこんな風になっているのか、俺には全然わからないんです"



"ナースはうなずくけど、その表情は曇っている。"




hi "あなたも分からないんですか？"





nk "そうだな……イエスでもあるし、ノーでもある。複雑なんだよ"




nk "患者に対する守秘義務というのは、どこかで聞いたことがあるだろう？"





nk "その意味では、この件はちょっとした地雷原のようなものなんだ。率直に言うけど、これは池沢さんと僕、そして彼女のセラピストだけの問題だ"




"俺は反論しようとするけど、思いとどまる。ナースの言ったことを否定したくても、理性的に考えれば、ナースは何もおかしなことはいっていない。"



hi "わかりました"

show nurse neutral
with charachange



nk "よろしい。何か助けになれればよかったんだけど、いま池沢さんに必要なのは、池沢さんの過去や気持ちを暴き立てることじゃない。そばにいてくれる誰かがいればいいんだ"




nk "友達が必要なんだよ"


show nurse fabulous
with charachange



nk "僕の私見だけど、池沢さんをここに連れてきたのは正解だったね。君も友達も、状況にうまく対処したみたいだ"


show nurse grin
with charachange


nk "ごほうびにシールかキャンディでもと思ったけど、ちょっと君の歳には合わないかな？"



"ナースは偉そうな笑みを浮かべる。空気を明るくしようと努力しているんだろう。笑うような気分じゃないけど、俺もつられて笑ってしまう。"



hi "どうも。ええっと、俺、華子のそばにいてもいいですか？"

show nurse neutral
with charachange



nk "気持ちはありがたいけど、今は休ませてあげたほうがいいだろうね"




nk "夜には寮に帰らせるから、その後で訪ねるといいよ"




"俺は同意して立ち上がる。ナースの前で俺にできることは、とにかくナースのいうことにおとなしく従うことだけなんじゃないか、という気がする。でも病院の医者たちが相手でも同じことだった。"


stop music fadeout 3.0

scene bg school_nursehall
with locationchange



"教室まで戻る道のりが長く感じる。あまりにいろんなことが突然降りかかってきた。その重みが心にのしかかっている。"


scene bg school_scienceroom
with locationskip

play music music_dreamy fadein 2.0
$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0



"もう一度教室に入る間も、俺は華子のことを考え続けている。"




"華子とどう向き合うべきかを考えていると、腹が締め付けられるような気分がする。次に華子と会うときになんて言えばいいのか、今でもわからない。"




"ありがたいことに、クラスの連中は俺には大して注意を向けない。いくつかいぶかしげな視線があったけど、全体的に見てほとんどは起きたことに気づいていない。"





"教卓の近くを通ろうとすると、武藤先生は眉毛をもちあげて俺の注意を引く。"


show muto normal at center
with charaenter


mu "中井……池沢は医務室にいるんだな？"




hi "はい。俺が連れていきました。そうしたらナースが休ませるようにと言っていたので"





"先生はうなずいて、俺が正しい判断をしたことを請け合う。少しの間あごをかくと、席から立ち上がる。"


show muto smile
with charachange


mu "みんな、課題を進めていてくれ。中井、ちょっと廊下で話そう"



"先生は静かに言うけど、それ以外は普段とそんなに違った様子じゃない。教師である以上、当然なのかもしれない。"


stop ambient fadeout 1.0
scene bg school_hallway3
with locationchange



"２人で廊下に出ると、先生が素早く左右に目をやって、うろついている生徒がいないか確認しているのに気づく。"



"廊下はほとんど音がないけど、先生の話を待つ以外には何も考えることができない。"

show muto smile at center
with charaenter



mu "中井、この学校が存在する目的はなんだと思う？"




hi "うーん……障害のある生徒たちの必要に応えるため？"


show muto normal
with charachange


"先生は頭をかきながら振る。"



mu "違う。それが目的なら、学校そのものを新しく作りなおしているさ。階段のない校舎。しゃべるホワイトボード。そういったものをな"




mu "周りを見てみろ、中井。この学校の意義とは、通常の教育では得られなかったはずの未来をお前たち全員に与えることだ"



hi "はあ？"



mu "考えてみろ。俺たちがお前を卒業させて、その後すぐに病院に直行させたいと思っていたとしたら、ここまで手間暇をかけると思うか？"




"先生の単刀直入な言葉にしばらく呆然として、目の前の状況も忘れてしまう。"



hi "いえ……"



mu "そのとおりだ。俺たちはみんなに、社会に役立つ人間となってここから旅立ってほしいんだ"





hi "あの……話がよくわからないんですが……"


show muto smile
with charachange



mu "お前には特に期待してるんだぞ、中井。俺の授業をちゃんと理解している生徒は、たぶんお前が初めてだ"




"そんなことを教師がおおっぴらに言っちゃだめだろう。"




mu "お前なら大学で科学をしっかり学ぶのも簡単なはずだ。考えたことはあるか？"




hi "あるとはいえないですね"



mu "そうか、それならなにを考えた？　お前の将来について、だが……"



hi "俺は……あまり将来のことを考えてませんでした"


"一瞬、リリーが同じことを聞いてきたことをはっきりと思い出す。"



"地面に倒れてあえいでいたあの時から、ほんの５か月くらいしか経っていない。将来のことを考えるにはまだ早い。それに今の俺には華子のことのほうがずっと重要だ。"


show muto irritated
with charachange



"不満そうに溜息をつくと、武藤先生は話を続ける。"


show muto normal
with charachange



mu "この学校そのものがチャンスだと考えることだ。ここには様々な施設といい先生たちがいる。その上、ナースとそのスタッフというおまけつきだ"



mu "お前がすべきことは、将来について考えることをおいて他にないんだ"




hi "ええと……わかりました"




"俺は頭を上げて先生と視線を合わせると、あることに気づく。目の前の問題から完全に話をそらしてるみたいじゃないか。"




hi "すみません、華子が授業をさぼっても先生たちは誰も気にしてなさそうなんですが、どうしてですか？"




hi "華子が授業から抜け出すのを何度も見てますよね？　せめて何か言うべきじゃないんですか？"


show muto smile
with charachange



mu "そうだな、中井、そう簡単なことじゃないんだ。ここの生徒はみんなそれぞれ必要としているものがある。そうでなければこんな学校はそもそも必要ない"




mu "例えば、呼吸が苦しくなったお前を教室に留めておいたりはしない、そうだろう？"



hi "でもそれは……"



"俺が最後まで言い切る前に、先生が割り込んでくる。"


show muto normal
with charachange



mu "池沢の場合も同じようなものだ。しかし池沢に必要なのは心肺蘇生法やペースメーカーじゃない。時間と居場所なんだ"




mu "ここの教職員は池沢が入学した当日からそのことを知らされていた。だから彼女が教室から抜け出したいと思ったときは、そうさせているんだ"


show muto smile
with charachange



mu "それに池沢は優等生じゃないが、テストはどれも合格点を取っている。つまり池沢の学力には影響はない。だったらそれでいいじゃないか？"




"俺は口を開けて抗議しようとするけど、先生の言葉に間違いは見当たらない。華子の症状も、最初は身体的なものだけに見えたけど、一番悪影響を受けていたのは精神の方だった。"




"それでも、やっぱりおかしな気がする。先生はただ華子の問題から責任逃れしてるだけじゃないのか？　華子だって一生こうやって逃げ続けていられるわけがないのに。"


show muto normal
with charachange



mu "お前がまだこういうことに慣れていないのは分かる。お前にとっては大きな変化だろうからな。そうは言っても、卒業までもう１年もない"




mu "この学校になじむ必要はないのかもしれん。お前がおとなしくしつづけていれば、試験でも十分な成績を取れるだろう"




"同意というよりは単に話を聞いていることを示すために、俺はぼんやりとうなずく。この学校には慣れてきたと思っていたけど、とんだ勘違いだと言い放たれたような気がする。"



hi "でも……華子はどうするんです？"



mu "やりたいことをやれるだけの成績を残せるだろうと信じて……いや、願っているさ"




mu "それがなにかはわからないが。すべての生徒がやりたいことを見つけて去っていくわけではないんだ。残念ながら"




"先生は最後の言葉を念入りに強調する。これでも強調し足りないと言わんばかりに。そして俺に今の言葉についてしばらく考える時間を与える。"


show muto smile
with charachange



mu "今日は災難続きだったな。あれだけのことの後だし、集中するのも難しいだろう。今日はもう休んで構わないぞ"




mu "今のところ、お前の成績はいいからな。これまでの授業の分を取り戻すのは難しくないだろう"





"ここまでの説教の深刻さを埋め合わせるかのように、先生はその褒め言葉に小さな笑顔を添える。"




mu "荷物をまとめてこい。また明日な"



hi "わかりました。ありがとうございます"

stop music fadeout 5.0

hide muto
with charaexit



"武藤先生の回りくどい講釈で、俺の考えは散らばったままだった。華子のために何ができるかという考えがはっきりしたわけでもないし、それどころか先生の話で、俺の頭はますます混乱する。"






"華子の『味方の敵』である静音が、俺と同じくらいには華子の手助けができていたことも気がかりだ。でもそれが俺の強がりでしかないのか、純粋な心配なのかは自分でも分からない。"


scene bg school_scienceroom
with locationchange



"教室から自分と華子の荷物をまとめる間も、俺は自分の気持ちを整理しようとする。"




"俺は華子のことを理解しているし、華子に寄り添っていると思いたい……昨日まではそう言えたかもしれないけど、今はもう無理だ。"




"そうできたらよかったのに。"



label jp_H15:

scene bg school_dormhisao_ss
with shorttimeskip

play music music_night fadein 1.0


"考えをまとめようとして、ベッドに横たわる。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear
window hide
nvl show dissolve


n "華子のパニック発作が起きたあと、俺たちの関係や、華子について何を知っているのか、根本から見直そうとしている自分に気づいた。"



n "俺は４ヶ月もの間、病院でかなりつらい時を過ごした。華子の傷跡をひと目見れば、華子は俺よりずっと長く病院にいたってわかる。"



n "いずれにしろ、俺は華子の過去についてほとんど何も知らない。家の火事のことも、ごく簡単に話してくれただけだ。"


n "それに華子の家族のことは？　まだリリーに訊ねずじまいだ。これまで、そのことを話題にするいい機会がなかった。"


n "華子がどこで育ったのか、そして以前いた学校はどんな感じだったのか、俺は知らない。これまでにいた友達や、華子が今まで抱いてきた願いや望みなんかも。そしてどんな音楽や食べ物、映画が好きなのかさえ……昔の友達みんなについて、俺が知っていたあらゆる些細なことが、華子に関しては何もわからないんだ。"



n "今まで華子やリリーと一緒にいて、俺はいったい何をしてきたというんだろう？"

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(0.1, 0.0, channel="sound")
play sound sfx_normalbell

nvl clear
nvl hide dissolve
window show


"遠くから、授業の終わりを知らせるチャイムが聞こえてくる。運が良ければリリーは、華子も俺もいないってことにすぐ気がついて、寮に戻ってくるだろう。"


$ renpy.music.set_volume(0.5, 0.0, channel="sound")
stop music fadeout 0.5
play sound sfx_phone


"携帯電話が鳴り、思考が中断される。山久に来てから、電話がかかってくるなんてことはめったになかったから、かなりびっくりする。"

scene bg school_dormhisao_blurred_ss
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)


hi "もしもし、中井久夫です"



li "ああ、久夫さん、見つけられてよかった。普段私たちが行く場所のどこにも見つからなかったから、電話なら一番早く連絡を取れると思ったんです"




"リリーは電話番号を教えた数少ない人のうちの一人だから、たぶんかけてきたのはリリーだって見当をつけとくべきだった。電話越しでも、リリーの声は少し不安そうに聞こえる。"



hi "俺……華子と俺、授業を早退したんだ。華子がパニック発作みたいになって……"



"電話口の向こうが静かになる。背景の雑音が聞こえなければ、俺はリリーが電話を切ったと思っただろう。"



li "わかりました。私の部屋に寄ってくださいますか？　話をしたいです"



hi "もちろん。俺……俺も、ちょっとリリーと話ができたらと思ってたんだ、実は"



li "ええ……よかったです。私にも……ちょっと良くない知らせがあります。直接お話ししたほうがいいと思うんです"


"リリーの声色からは、状況の深刻さを把握しにくい。たいていとても落ち着いた声をしているけど、見方によってはそれはいいことにも悪いことにもなりうる。"


hi "わかった。すぐ行くよ"

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_dormhisao_ss
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None


"机から華子の荷物を取って、まっすぐリリーの部屋へと向かう。"

scene bg school_girlsdormhall
with locationskip

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorknock2


"部屋のドアをノックする俺を、リリーはすぐに中へと呼び入れる。"

play music music_drama fadein 4.0

scene bg school_dormlilly
show lilly basic_sleepy:
    center
    ypos 1.17
with locationchange


"部屋のなかでテーブルのそばに座っているリリーは、少し疲れているようだ。たぶん悪い知らせのせいだろう。"


"リリーの手招きに従って、俺はリリーの正面に座り、テーブルに華子の荷物を置く。"

show lilly basic_weaksmile
with charachange



li "さて、２人そろって待っていても仕方ないですし、久夫さんから先に話していただけますか？　今日何があったんです？"



"あの出来事の記憶はもう薄れ始めているけど、できるだけ詳しくリリーに説明する。"



"華子をグループワークに誘ったこと、静音とミーシャによる尋問、２人で街へ出かけたのがばれたこと、そしてそのあとのパニック発作。"



"静音の反応もほぼ思いつきであとから話に付け加えたけど、リリーはそれを聞いてなんだかほっとしたみたいだ。"



"ライバルは理由もなくライバルになる訳じゃないんだろう。そこには何かしらの経緯があるはずだけど、今はそれを掘り下げるべき時じゃない。"


show lilly basic_concerned
with charachange


li "そうですか。華ちゃん、セラピストとの話し合いが助けになっていると言っていたんですが、私は本当にそうなのか疑問に思っていました。本当に残念なことです"

show lilly basic_reminisce
with charachange



li "華ちゃんの誕生日は以前にも問題の原因になりました。でも久夫さんがそばにいて、そしてもっと本格的にセラピーを受けることで、華ちゃんが良くなってくれればと、そう願っていたんです"


show lilly basic_oops
with charachange


li "今、華ちゃんはどこに？"


hi "最後に見たのは医務室だったよ。もう自分の部屋に戻ってるんじゃないかな"


show lilly basic_sleepy
with charachange



li "私が見に行ったときには、図書室にも紅茶の部屋にもいなかったので、私にもそれくらいしか考えつきません"



hi "悪い知らせがあるって言ってたよね……どうしたの？　華子に関すること？"



"リリーは姿勢を変える。説明するのにふさわしい言葉を探していることを、身体が物語っている。"


show lilly basic_concerned
with charachange



li "おばが、重い病気にかかってしまいました。おばのお見舞いと、そして家族と過ごすため、スコットランドに戻ることになりそうです"



hi "何だって？　大丈夫なの？　いつ出発するんだい？"

show lilly basic_reminisce
with charachange



li "最後に聞いたときは容体が安定しているとのことだったんですが、今はおばがどんな状態なのか、はっきりと分かっているわけではないんです。土曜日に発ちます。予約できたなかで一番早い便です"




"『安定』。『入院が必要である』ことを表す言葉だ。俺も長い間容体が『安定』していたから、それがわかる。"
"そして、必ずしもその人の状態がいいことを示しているわけじゃなくて、ただ状態が悪化していないだけだ、ということも。"




"せめてもの救いは、『安定』が『危篤』よりはよっぽどいいってことだ。少なくともリリーのおばは、死に瀕しているわけじゃない。"




hi "『安定』か……ほっとしたよ"

show lilly basic_sad
with charachange


li "ええ、ですが私は華ちゃんの誕生日にここにいられないことになります"

show lilly basic_concerned
with charachange



li "華ちゃんに話す前に代わりの案を考えられればと思って、今久夫さんに伝えたかったんです。でも今日の出来事があった後となっては、単に誕生日会を取りやめにしても問題ないのかもしれませんね"



hi "俺は……それはあんまりいい考えじゃないと思うな。華子はもう、俺たちが誕生日会を計画してるって知ってるんだし、やめてしまうのは間違ってるような気がする"


hi "それに、リリーのお別れにも、何かしなくちゃいけないだろ？"

show lilly basic_weaksmile
with charachange



li "まるで私が帰ってこないみたいに言うんですね。何も問題がなければ、１週間か、２週間かもしれませんが、その間不在にするだけで済むと思いますよ"



hi "それならひと安心だね"

show lilly basic_oops
with charachange


li "そうすると、久夫さんはどうするのがいいと？"



hi "この状況だと、カラオケはあんまりいいとは思えないな。いい理由で日本を離れるわけでもないから、楽しみすぎるのはよくないって気がするし"



hi "去年の誕生日には何をしたの？"

show lilly basic_reminisce
with charachange


li "去年は……文字通り、華ちゃんを部屋から連れ出すことができませんでした。ドアに鍵をかけていたんです"


li "華ちゃんのために食事を部屋の外に置いて、少なくともちゃんと食べているか確かめることぐらいしかできませんでした"



"こんなに憂鬱そうに振る舞い、そして話すリリーを、これまでたぶん見たことがない。リリーはいちばんの親友を助けることができず、とても打ちのめされた思いをしているに違いないと考えると、気の毒に思う。"




hi "だったら、リリーの出発前に会を開いた方がいいんじゃないかな？"


show lilly basic_weaksmile
with charachange


li "確かに、それが一番やりやすそうですね"


hi "少なくとも華子に、リリーが日本を離れることと、華子の誕生日会の両方について伝えるべきなんじゃないかな。華子の学校の荷物もあるし"

show lilly basic_smile at center
with dissolvecharamove


li "なるほど。いま華ちゃんを訪ねにいきましょうか？"


hi "そ……それがいいと思うよ"



"心のどこかで、俺はどうしても華子に会いたいと思っている。最後に見たとき、華子は死にそうな顔をしていたし、この数時間、ただそのことを考えるだけで心がかき乱されていた。"



stop music fadeout 4.0

scene bg school_girlsdormhall
with locationchange


"俺たちは静かに席を立ち、そろってリリーの部屋から出る。華子の部屋は、同じ廊下、リリーの部屋の隣のドアだ。"

play sound sfx_doorknock2


"軽くノックしても何の反応もないけど、ドアの鍵はかかっていなかった。思いがけずドアノブが手の中で動いたので、リリーはしばらく動きを止め、そしてドアを開く。"


play music music_moonlight fadein 0.5

scene bg school_dormhanako_ni at Fullpan(8.0)
with locationchange


"華子の部屋は驚くほどがらんとしていて、単調だ。真っ白な壁には何の飾りもなく、紺一色のブランケット、ほんの数冊の本やプリント、そして実用品が棚に置いてあるだけ。"


"ベッドシーツまでもが単色だ。部屋全体が、華子の性格と同じくらい控えめなものに感じられる。"

scene ev hanako_cry_closed
with whiteout


"華子はというと、ベッドの上で横たわって丸くなっている。今はもう泣いてないのかもしれないけど、泣き出さないように目はかたく閉じられていて、涙の跡が赤い頬の上にまだ残っている。"


"華子をあまりびっくりさせないように気をつけながら、静かに部屋に入り、机の上に華子のかばんを置く。"


li "こんにちは、華ちゃん。今日あったこと、久夫さんが話してくれました……大丈夫？"

show ev hanako_cry_away
with charachange


"ほんの少しだけだけど、華子の目が開く。"


ha "だ……大丈夫……"

show ev hanako_cry_open
with charachange


"華子は頭を少し傾けて俺を見やり、隠す間もなく俺の渋面に気づいてしまう。"


ha "し……心配さ――させてご――ごめんなさい"

show ev hanako_cry_closed
with charachange


ha "ほ――本当に……もうだ――大丈夫だから……"


"少なくともさっきよりは落ち着いているみたいだけど、見た目も声も、全然大丈夫そうじゃない。今も、ちょっと息をつくだけで、華子の感情は壊れてしまいそうにみえる。"



hi "前にも言っただろ？　謝ることなんてないよ"



li "久夫さんの言う通りです。私たち……私……誕生日のお祝いなんてことを、華ちゃんに隠すべきじゃありませんでした"


"その言葉に華子は身震いする。沈黙が続くことに気づいたリリーは、華子と同じ目線までしゃがむ。"


li "謝るのは私のほうですよ、華ちゃん"

show ev hanako_cry_away
with charachange


"華子は目を開けてリリーを見つめる。暗い分析的な目で、しばらくのあいだ、リリーの顔をじっと見ている。"


play sound sfx_rustling

scene bg school_dormhanako_ni
show hanako emb_downsad_ni:
    center
    ypos 1.3
    easein 1.0 ypos 1.15
with locationchange



"華子はベッドから起きあがって、端に座り直せるくらいには回復していた。リリーの行動は正しかったに違いない。華子は色んなことに思い悩むけど、他人に迷惑をかけることをまず第一に気にしてしまうんだ。"


show bg school_dormhanako_ni at bgright
show hanako emb_downsad_ni:
    xpos 0.6
    ypos 1.15
with charamove

show lilly invis:
    twoleft
    xpos 0.4
with None

show lilly basic_weaksmile_ni at Position(ypos=1.17)
with dissolvecharamove


"リリーは華子が動く音を聞いて前に進み、ベッドの端を手探りし、やがて華子のとなりに座って両手で華子の左手をとる。"



"リリーと華子が一緒にいるとき、俺は自分が場違いに思えてしまう。そんな気持ちは３人がお互いを知っていくにつれ減っていったけど、今でも時折すごくそう思う。今回もそんな感じだ。"




hi "リリー、もし俺が出たほうがいいなら……"


show hanako emb_sad_ni
with charachange


ha "それは……嫌……"

show lilly basic_surprised_ni
with charachange



"華子が勇気を奮い起こしてそう言ったことに、リリーも俺も２人して驚く。半ば口ごもりながら『わかった』としか返せないまま、俺はデスクチェアに座り込む。"


show lilly basic_concerned_ni
with charachange


li "華ちゃん、実は悪い知らせがあるの"



"今度はリリーが話を切り出すのか。俺たち２人がここにいてもいいと、華子があれだけはっきりと認めてくれたので、今がいい頃合い、いや少なくとも、今よりいいタイミングはないとリリーは思ったんだろう。"


show lilly basic_sad_ni
with charachange



li "おばが病気になってしまったので、しばらくの間家族のもとに帰らないといけないの"


show hanako cover_worry_ni
with charachange


"申し訳なさそうにしていた華子の表情が、心配の色に変わる。"


ha "リリーの……家族……スコットランドの、だよね？"

show lilly basic_reminisce_ni
with charachange


li "ええ。姉さんと私は、土曜日に発ちます"

show hanako defarms_strain_ni
with charachange


ha "じ――じゃあ行っちゃうの？"

show lilly basic_weaksmile_ni
with charachange


li "そんなに長くはならないと思います。たぶん１週間か２週間だけ。あっという間に戻ってきますし、久夫さんがここにいてくれるでしょう？"


hi "ああ、俺はどこにも行かないよ"

show hanako basic_worry_ni
with charachange


"ほんの少ししか慰めになってないみたいだけど、華子はなんとか自分の心を奮い立たせて覚悟を決めている。"


ha "お――おばさん、大丈夫かな？"

show lilly basic_reminisce_ni
with charachange


li "わかりません"


"沈黙が降りる。ほかの人の不幸が、本当の意味で華子をいつもの状態から抜け出させるっていうのは、悲しいことだ。"


"俺はここに来たもう一つの理由の方に話題を移すことに決め、部屋に立ちこめる暗い感情から、少なくともいくらかは気をそらそうとする。"


hi "ともかく、リリーのお別れ会をやるのはいい考えだろうって、俺たち思ってたとこなんだ。あと、それと一緒に……うん……"


"華子の誕生日のことに触れる前に話をやめる。華子の心の中にある、あの激しい感情の引き金になってしまいそうだから。"


"リリーは華子の手を優しく握る。"

show lilly basic_weaksmile_ni
with charachange


li "それでもいいかしら、華ちゃん？　ぜいたくなものでも、度を超すようなものでもなくて、ただ私の部屋で、小さな会をするの"

show hanako def_worry_ni
with charachange


ha "じ――じゃあ学校の中だけ？　私たちだけで？"

show lilly basic_smileclosed_ni
with charachange


li "ええ、私たち３人だけ。もしよければ、姉さんにも来てもらうようお願いしますよ"

show hanako basic_normal_ni
with charachange


ha "い……いよ。い――１週間行くだけ？"

show lilly basic_smile_ni
with charachange


li "ええ、１週間か２週間です。それ以上長くはならないって約束します"

show hanako cover_distant_ni
with charachange


ha "わ――わかった……"


"たいていの人は、友達の家族が病気になったと聞けば心配し、そしてパーティーをするなら嬉しくなるだろうけど、華子にとっては両方の出来事が同じ土俵にあるらしい。"



hi "じゃあそういうことで。休んだ方がよさそうだよ、華子。だから、今はみんな部屋に戻るのがいちばんいいんじゃないかな"


show lilly basic_weaksmile_ni
with charachange



li "もしも何か必要になったら、いつでも私か久夫さんに話していいんですよ"



"その声は憂いに富んでいる。リリーほど自信のある人にしては珍しい声音だ。"

show hanako basic_bashful_ni
with charachange


ha "わ……わかった。ありがとう、リリー、久夫くん"



show lilly basic_smileclosed_ni at Position(ypos=1.0)
with dissolvecharamove


li "それでは、おやすみなさい、華ちゃん"

show hanako basic_normal_ni
with charachange


ha "おやすみ……"

stop music fadeout 4.0

scene bg school_girlsdormhall
with locationchange


"背後でドアが閉まり、俺は長いため息をつく。さっきまで深海にいて、今ようやく息継ぎに上がってこられたみたいな感じが少しする。"

show lilly basic_concerned at center
with charaenter


"リリーもあんまり調子がよくなさそうだ。顔は青ざめ、やつれている。"



hi "大丈夫？"


li "少し疲れただけです。最近は……とても忙しかったものですから"


hi "ちょっとでも寝られたの？　顔色を見れば、『少し疲れた』は控えめな言い方に聞こえるけど"

show lilly basic_sleepy
with charachange


li "授業の前に２、３時間寝られたと思います。大丈夫です"



"こんな時にリリーをせき立ててしまって、申し訳なく感じる。２人とも、今日起こったいろんなことに、かなり疲れているんだと思う。"




hi "休んだ方がいいと思うよ。今日は大変な１日だったし、ずっと起きておくのは肌に良くないって"



show lilly basic_weaksmile
with charachange


li "ご心配ありがとうございます、久夫さん。では、おやすみなさい"


hi "ああ。おやすみ、リリー"

hide lilly
with charaexit


"自室のドアを開けるリリーと別れ、俺も自分の部屋に向かい始める。"

scene ev hanako_cry_closed_fb
show noiseoverlay
with flash



"静かな廊下を進む間も、華子の姿が頭から離れない。縮こまって、かわいそうで、頬に涙を浮かべてなすすべなく横たわっている姿。"
"極端に恥ずかしがりだとはいえ、華子はただ普通の人なんだって思い始めてたけど、問題はもっと深いところに根を張っている。"




"華子がこんなに弱っていて敏感な時に、もっと深い仲になろうとするのは間違っている。友達以上の関係にならなくたって、華子を守り、今後こんなことが二度と起きないようにすることはできる。"




"華子に対して俺が抱いている感情が、友達以上のものになっている可能性……そんなのもうどうだっていい。華子は俺にとって大事な人で、だからこそ俺は華子の弱みにつけいるようなことはできないんだ。"




"だけど、それでも……そんな考えを抱くと、まだ胸にあの痛みを感じる。"


scene bg school_girlsdormhall
with flash


"今は、眠らなきゃ。明日はもっと、いい日になるといいな。"

scene black
with dissolve



label jp_H16:

scene bg school_scienceroom
with locationchange


"華子は教室にいる時よりも、休んでいる時の方が目立つ。"


"華子の空っぽの机が俺を呼んでいる気がする。今見ているのは幻覚であってほしい、華子が魔法のようにここに現れてほしい。そう願って、何度も肩越しに振り返ってしまう。"



"華子は授業を受ける時、できるだけ目立たない存在でいようとする。最近良くなってきていたとはいえ、その事実は決して変わらなかった。"




"クラスの誰もこれまで華子に注意を向けたことはなく、華子が休んでいても、誰もそれに気づかない。まるでそもそも存在すらしていなかったかのように。"




"華子が授業をサボるのは珍しいことではない。華子に知り合う前、確かにリリーはそう言ったけど、それでもすごく嫌な感じがする。"


play sound sfx_normalbell


"授業の終鈴のチャイムが聞こえ自分の席で飛び上がる。そのときようやく、ミーシャが俺の注意を引こうとして脇腹をシャープペンシルで突いているのに気づく。"

show shizu invis:
    center
    xpos 0.4
show misha invis_close:
    center
    xpos 0.1
with None

show bg school_scienceroom at bgright
show misha sign_smile_close at Position(xpos=0.2)
show shizu behind_blank at center
with dissolvecharamove

play music music_normal fadein 3.0



mi "こんにちは……聞こえてますか～？"





hi "おい、やめろよ"

show misha hips_grin_close
with charachange


mi "あ！　聞こえてた！　おかえりひっちゃん、地球に戻ってきたね～！"






hi "一体何の話だよ？"

show misha hips_smile_close
with charachange


mi "なんにもない所をずっとぼーっと見てるから、宇宙人と接触しようとしてるのかも、って思ってたんだよ"





"昨日の夜は本当にあまり眠れなかったから、ミーシャの言葉を疑おうとも思わない。"
"これが薬の副作用によるものなのか、昨日の華子のパニック発作のせいなのか、いつも華子を心配しているからなのか、その全部のせいなのかも分からない。"





"どれだけ眠れなかったか思い出し、疲れ切った様子であくびをして、手のひらであごを支える。"

show misha perky_confused_close
with charachange



mi "ねえ、本当に大丈夫？　昨日のことはわたしもびっくりしたけど……"



hi "ああ……うん、そうだろうね。それでも、また華子と話したいなと思ってたんだ"

show misha perky_smile_close
with charachange


mi "昨日の夜に会ったの？"


hi "ああ、リリーと俺で話をしに行ったんだ"


hi "うーん、ちょっと変かもしれないけど、静音に『ありがとう』って伝えてくれる？　俺と……リリーの両方から"


"厳密にはリリーは静音に感謝してはいなかったけど、昨晩の反応でそうしたがっているのは分かった。少なくとも、俺はそう理解している。"


show shizu adjust_blush
with charachange

show shizu cross_angry
with charachange


shi "……"

show misha sign_confused_close
with charachange


mi "えーと……しっちゃんは、『どういたしまして』って言おうとしてるみたい"


"激しい手話と紅潮した頬を見れば、静音が全く違うことを言っていたと分かる。露骨におろおろしている静音の表情がおかしくて、つい笑みがこぼれる。"



show misha perky_confused_close
with charachange


mi "なにがそんなにおかしいの、ひっちゃん～？　あたしたちが言ったこと？"




hi "いや、違うよ、そうじゃない。ただ、静音は時々すごくかわいいよなあ、って思ってたんだ"





show misha cross_laugh_close
with charachange



mi "わははは〜！　ほんとだね～！　しっちゃんって、ツンツンしてるときはすごくかわいいんだよ！"












"ミーシャが、今の言葉を静音に伝えないようにしているのに気づく。静音の怒りは、『かわいさ』の量からすると、十分その正反対になっているのかもしれない。"





show shizu adjust_frown
with charachange


"にもかかわらず、静音はすぐに落ち着きを取り戻し、ミーシャに何か別の手話をする。"

show shizu behind_smile
with charachange


shi "……"

show misha perky_smile_close
with charachange


mi "ん～？　わかった……ひっちゃん、しっちゃんが３人で一緒に晩ご飯を食べに行こうよ、って"









hi "晩ご飯だって？"



"訴えるような２人の笑顔に心が揺さぶられないよう、２人に少し背を向けて、どうするか考え始める。"




"この誘いは確かに魅力的だ。可愛い女の子２人といっしょに、テイクアウトの晩ご飯。つまるところ、悪くはない。でも、華子が１人で部屋に閉じこもっているという思いが、頭の隅でくすぶっている。"





hi "ごめん、行けないや"


show misha perky_sad_close
with charachange


mi "えー……"

show shizu behind_frown
with charachange


"ミーシャは俺の返答を手話にはしなかったけど、静音はすぐに意味を理解して残念そうに顔をしかめる。"


show shizu basic_normal2
with charachange



"腕を動かし、おそらく抗議か脅迫を表すような手話を始めるけど、途中で止めてミーシャの肩を２度叩く。振り向いたミーシャに対して、静音は手話のかわりにただ肩をすくめるだけだ。"






show misha perky_confused_close
with charachange


mi "うん、わかった。決めるのはひっちゃんだもんね"




hi "もしよければ、必ず別の機会にご一緒するよ"

show misha perky_smile_close
show shizu behind_blank
with charachange


"ミーシャはこの言葉で元気になっているけど、静音はそうでもない。頭を軽く振ってミーシャについてくるよう合図すると、静音はただ無言で手を振って、別れの挨拶をする。"





hide misha
hide shizu
with charaexit

stop music fadeout 3.0



"２人がドアを出て行く間、俺も手を振る。２人の姿が見えなくなるまで。"






"２人がそこまで残念がるとは思わなかったし、２人を厄介払いしたように感じて少し申し訳なくなる。それでも、俺にはやるべきことがあるんだ。"


scene bg school_girlsdormhall at right
with shorttimeskip



"今日は女子寮がやけに騒々しい。１階の談話室でたくさんの女子がわいわいとゲームをしたりテレビを見たりしている。華子のドアの前に立つ今でも、その声が聞こえる。"




"それは華子のいる階の空虚さとは奇妙なくらいに対照的だ。階下からの声で、空虚さがより一層孤独に感じられる。"




"俺は華子が今日教室に来てくれるんじゃないかと期待していた。昨晩リリーと俺とで話をした後だし、余計にそう思った。"
"でも華子を責めるべきじゃないと思う。あれはとてもつらい出来事だったし、それを経験した本人はなおさらつらい思いをしているに違いない。"








scene bg school_dormhanako_ni
show hanagown worry_close:
    center
    xpos 0.39
show expression Solid("#00000022")
show hanako_door_base at right
show hanako_door_door at left
with locationchange

play sound sfx_doorknock2


"華子がどんな状態かも分からないまま、ひと呼吸置いて、茶色のドアを何度か鋭くノックする。"



"俺にできることといえば、なるべく不安を感じないようにしながら、ここに立って華子を待つことだけだ。"


"何秒か経つにつれ、華子は眠っていてノックの音が聞こえなかったのかもしれないと思い始める。でも、手を挙げてもう一度ノックしようとする前に、ドアノブがかちゃりと小さな音をたてる。"


play sound sfx_dooropen

show hanako_door_door:
    xpos -0.05
with charamove


"ドアが少し開く。外を覗くのにちょうど必要な隙間だけを開け、華子の目がこちらを覗く。もし許可さえ下りれば、華子はきっと寮の自分のドアに覗き穴をつけるだろう。"





"俺はただ立って華子に微笑む。ここでは所詮言葉なんて、あまり役に立たないだろうし。"




"華子も同じように黙って俺を見る。ドアの隙間は華子の表情を見られるほど広くはないので、華子が何を考えているか推測することしかできない。"






"お互いを見つめて時が過ぎる。唯一聞こえるのは、１階からの見えないお祭り騒ぎの音だけ。"

hide hanagown
with charaexit



"どのくらい時間が経ったか分からないけど、徐々に華子の目がそれて見えなくなる。部屋に入れてくれるのか、それとも締め出すつもりなのか考え続けていると、ドアがギイッと音を立ててゆっくりと開き始める。"



play sound sfx_door_creak

show hanako_door_door:
    easeout 1.0 xpos -0.2
show hanako_door_base:
    easeout 1.0 xpos 1.1
show bg school_dormhanako_ni:
    center
    easeout 1.0 xpos 0.55
with None

scene bg school_dormhanako
show hanagown normal at center
with silentwhiteout

play music music_comfort



"華子と後ろのベッドルームが全部見えるようになって、華子の髪がかなり湿っているということにまず気がつく。"
"さっきシャワーを浴びたばかりみたいだ。ふわりと漂ってくるシャンプーの香りからも、そのことがよりはっきり分かる。"





"華子は物珍しそうな表情を浮かべている。まるで俺のことをどう理解すればいいのかはっきりとは分かっていないみたいに。そうだとしても、俺だって華子が何を考えているのかはあまり確信が持てない。"






"まるで長い間華子がどこかに行ってしまっていたかのようで、そして戻ってきた今、２人ともお互いに何て言えばいいか分かっていないみたいだ。"



show hanagown distant
with charachange



"華子は俺を凝視していることに気づいてぎこちなく目をそらし、横を向いて自分の足を見つめる。俺は中に招き入れられたと解釈して、華子の横を通り過ぎて部屋へと足を踏み入れつつ、背後のドアを閉める。"




"肩から垂れ下がるぶかぶかの寝間着にできたしわの中で、華子が指をもてあそんでいるのが見える。自分の言いたいことに集中しようとするけど、漂ってくる香りで意識が乱される。"



"驚いたことに、沈黙を破ったのは俺ではなく華子だ。"

show hanagown normal
with charachange


ha "どうして……"


hi "だって……えーと…"


"……どうしてここに来たんだろう？"



"華子が心配だったから、部屋までやってきた。願っていたとおり、華子は俺を部屋に入れてくれた。それから次は……何だ？　俺は何をしようとしていた？　何を言おうとしていたんだ？"



"どうしてここに来る前にちゃんと考えてこなかったんだ……"




"俺は、少なくとも部分的には自分が引き起こしたと思っていることに対して、埋め合わせをしたいんだ。その時から感じている２人の距離をなくしたいし、華子が喜ぶところを見たい。"
"華子のことを何も知らないのに、どうやってそうしようというんだ？"





"ひょっとして……ひょっとしてこれが、あの殺菌されたパステルブルーの治療用ベッドに寝ている俺を見たときに、岩魚子が感じたことなのかもしれない。"




hi "俺はえーと……俺……うーん……"



"深くため息をついて少し神経を落ち着け、どもりを止める。これまでに誰かのまわりにいてこんなに緊張したことはないんじゃないだろうか。"
"こんな状態では嘘はつけないと思う。たとえ嘘をつくことができたとしても、華子はすぐさま見抜くだろう。"




hi "分からない。ただ……華子に会いたかったんだと思う"


show hanagown smile
with charachange


"華子の指が動きを止めたので、少し驚く。俺が顔を見上げると、華子は優しい笑みを見せてうなずく。今のが華子にとって満足のいく答えだったんだろうか？"





ha "あの……せっかくここに来てくれたから……"




show hanagown distant_blush
with charachange


ha "私……久夫くんとチェスをしたい……"








"これだけ頑張ったのに、華子の望みがただチェスをするだけなんて信じられなくて、うなだれそうになる。でも、ためらいがちな笑みを見せる華子の顔を見ていると、これにはそれ以上の意味があると分かる。"





"華子はドアのノックを無視することもできた。俺の顔を見るなりドアを閉めることもできた。俺に帰れと言うこともできた。"







"華子は色んな段階で俺を拒否できたのに、そうしなかった。今、こんなに落ち着いた顔で華子は俺と、初めて２人きりで時を過ごしたときと同じゲームをしたがっている。"




"安堵の気持ちが押し寄せる。"



"全部きっとうまくいく。華子は自分の世界に俺を入れてくれた。こんな風にして２人が一緒にいられる限り、きっと全部うまくいくと思う。"



hi "もちろんだよ"



stop music fadeout 2.0

scene black
with dissolve
label jp_H17:

scene bg school_girlsdormhall
with locationchange


"今日はついに、華子の誕生日会当日だ。"



"正直言うと、パジャマ姿の華子とリリーに会えるのが待ち遠しい。"
"華子の寝間着は、ちょっと控えめだけどむしろ可愛く見えていいなと思ったし、リリーのショートパンツと薄いシルクの上着は、すてきな組み合わせだと思う。"





"でも、この誕生日に対して華子がどう反応したか思い出すと、少し心が沈む。"


"今でもあのとき何が起こったのかよく分からないし、理由もなんとなくしか分からない。でも、華子に聞けば答えが分かるというような、簡単な話じゃないと思う。"

play sound sfx_doorknock2


"そんなことを考えながら、華子の部屋の隣のドアをノックする。"


li "久夫さんですか？"


hi "ああ、俺だよ"



"ぱたぱたとドアに近づく足音が聞こえ、錠がかちりと開く音がする。リリーの部屋のドアに鍵がかかっているのなんて今まで見たことなかったと思う。なんだか少し変だ。"



"ドアが開くと、そこに見える光景は……誕生日会にしては少しさえない感じだ。"

play music music_ease fadein 1.0

scene ev lilly_bedroom
with locationchange




"華子は素早く微笑んでうなずき、テーブル脇の席に戻る。俺はドアを閉め、２人ともそうしてほしいんだろうなと思ったから鍵をかける。"





"そして、目の前の光景は夜のお茶会と同じだと気づく。２人のいつもの光景と同じだ。まあ、驚くことでもないな。"


scene ev lilly_bedroom_large:
    ypos 0 xpos -860
with locationchange


"華子が比較的落ち着いているようでほっとする。多分授業を休んだのがよかったんだろう。そして少し落ち着く時間がとれたんだと思う。"

scene bg school_dormlilly
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
show hanagown distant:
    tworight
    ypos 1.17
with locationchange



"リリーの部屋の真ん中にあるローテーブルの脇、２人の間に座る。俺たち３人に囲まれて、明るい色のティーポットが湯気を立てている。"



"リリーのすぐ傍にある、背の高い茶色の袋が目に留まる。何度かひそかに中を覗こうとするけど、ここからじゃよく見えない。"


"華子の方を見やると、俺と同じくらいその袋に興味津々のようだ。"



hi "なあ、リリー？"



"リリーはティーカップに口をつけて中身を飲み干し、カップを戻して、俺を見る。"


show lilly basic_smile_paj
with charachange


li "何でしょう？"


hi "その茶色い袋は何なんだろう、って考えてたとこなんだけど……"


"リリーはしばらく動きを止め、そして少しだけ生意気そうな笑みを見せる。"

show lilly basic_cheerful_paj
with charachange



li "これは姉さんからのプレゼントなんです。残念ながら、お仕事があって来られないと言っていました"



"リリーはかがみ込んで中にあるものを探し出し、持ち上げる。"



"袋から、１本じゃなく２本の品物が取り出されるのを見て、俺は驚いて眉を上げる。リリーが両手の中指で、それぞれのガラス瓶の首の部分を掴んでいる。だからドアに鍵をかけてあったのか。"


show wine:
    yalign 0.5 xanchor 0.0 xpos 1.0 alpha 0.0
    easein 1.0 alpha 1.0 xanchor 1.0
with Pause(1.0)


ha "ワイン……"



"ボトルがテーブルに置かれて、小さな鈍い音を２回たてる。１本は赤で、１本は白。本物じゃなくて、ノンアルコールワインだと思いたい。でももしそうなら、これだけ用心深くなる必要もないだろうし。"





hi "お酒？　マジで？　本当に大丈夫なの？"


show lilly basic_smileclosed_paj
with charachange



"リリーは上品に微笑んでくすくすと笑う。俺には、リリーが本当に大丈夫と思っているようには見えない。"



li "これは姉さんからのプレゼントですから。少し問題があることは分かっていますが、ちょっとだけ飲む分には大丈夫でしょう"



"もしリリーがこのことを大真面目に考えていたら、こんなに簡単に賛成はしなかったんじゃないかと思う。"
"それはさておき、晃さんはリリーの年長版といった感じで、真面目で責任感のあるタイプだと思っていたけど、どうやら思い違いだったみたいだ。３人ともまだ法律上お酒が飲める年齢にもなってないのに。"





hi "まあ、そういうことなら文句は言わないよ。見た目も悪くなさそうだしね"




"俺は専門家でも何でもないけど、少なくともボトルの見栄えはいい。実家での夕食で、グラス１、２杯くらい親父からこっそり飲まされたのを除けば、どれが何だか分かるほど飲んだことがあるわけじゃない。"


show hanagown smile
with None

show wine:
    easeout 1.0 alpha 0.0 xanchor 0.0
with Pause(1.0)

hide wine
with None



"それに、自分は絶対酒は飲まないタイプだとも言えない。華子の表情を見るに、同じことを考えているみたいだし、ともかく今日は華子の誕生日だしな。"


show lilly basic_smile_paj
with charachange



li "１本開けましょうか？"



hi "うん。じゃあ俺は……"

$ renpy.music.set_volume(0.5, 0.5, channel="music")
$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorknock2

show lilly basic_displeased_paj
show hanagown worry
with vpunch



"部屋のドアを３度、鋭くドンドンドンと叩く音が聞こえてドキッとする。華子の頭はさっと動き、リリーは目を閉じて注意深く聞き耳を立てる。誰もこんなことで身を滅ぼしたくなんかない。"


show lilly basic_oops_paj
with charachange


li "どなたですか？"


mystery "中に入れてよ、寒いって！"


show lilly basic_weaksmile_paj
with charachange

$ renpy.music.set_volume(1.0, 6.0, channel="music")


"リリーはあきらめたようなため息をついて、華子にドアを開けるよう合図する。"

show hanagown invis at tworight
with dissolvecharamove

hide hanagown
with None


"華子は素直に席を立って、寝間着をいじった後に歩き出す。どうも誰がそこにいるのかはっきりとは分かっていないけど、リリーを信じているから、言われた通りにするようだ。"



"ドアを開ける華子のちょうど肩越しに、金髪でダークスーツ姿の人が見える。"



mystery "誕生日おめでとう、華子"



ha "あ――ありがとうございます……晃さん……"


"華子は身体の前で指をいじくりながら、小さくおじぎする。つまり、この人がリリーの、どういう人かつかみどころのないお姉さんなのか。"


show bg school_dormlilly at bgleft
show lilly basic_weaksmile_paj:
    left
    ypos 1.2
with charamove

show hanagown invis at center
show akira invis at right
with None

show hanagown normal at Position(ypos=1.17)
show akira basic_smile:
    right
    xpos 0.95
with dissolvecharamove


"晃さんは背後のドアを閉め、華子の後についてテーブルへと近づく。その間俺はじっくりと晃さんを観察する。"


"晃さんは華子と同じくらいの背丈のようで、かなり雑にカットされた短い金髪の持ち主だ。その外観と、どちらかというと控えめな胸に、男性が着るようなスーツ、そして低めの声から、かなり中性的な印象を受ける。"


show akira basic_ending at Position(ypos=1.18)
with dissolvecharamove


"というわけで、晃さんはテーブルを挟んで俺の向かい側にドスンと座る。"

show lilly basic_smile_paj
with charachange


li "やっぱり来てくれて嬉しいわ、姉さん。お仕事は大丈夫だったの？"


show akira basic_boo
with charachange


aki "ああ。ちょっとしたら戻らなきゃいけないけど、なんとかここまで車で来る時間は作れたんだ"


show akira basic_smile
with charachange


aki "てことは……こっちが久夫ってことかな？"


"晃さんの自信に満ちた笑みが向けられ、俺は礼儀正しくうなずき返す。俺のことをすぐに名前で呼び始めたことから考えるに、あんまり外見ほどお堅い人じゃないみたいだ。"


"いや、もし晃さんが俺のことをすでに知っているとしたら、リリーがしゃべったってことに違いない。何て言ったんだろう。"

show lilly basic_smileclosed_paj
with charachange


li "紹介が遅れてごめんなさい、久夫さん。こちらが私の姉、砂藤晃です"


hi "なるほど。はじめまして"

show akira basic_ending
show hanagown worry:
    0.1
    ease 0.1 ypos 1.15
    ease 0.1 ypos 1.17
with Dissolve(0.1)


"当の本人は大きく両手を叩き、華子が驚いて少し飛び上がる。"

show akira basic_lost
with charachange


"晃さんもこれに気が付いたようで、ほんの一瞬不安そうな顔をしてから調子を戻す。"


show akira basic_smile
with charachange


"今になってようやく、晃さんが華子の傷に全く余計な注意を払っていないことに気がつく。華子も晃さんのそばにいて、リラックスしているとは言えないにしても、居心地はよさそうだ。"

show akira basic_laugh
with charachange



aki "じゃあ、プレゼントはもう開けたんだ？　久夫とこっちのバースデーガールはすごく飲みたがってるみたいだし、我慢しても意味ないよ"



show lilly basic_cheerful_paj
with charachange




"好奇心を隠しきれなかったことが少し恥ずかしくて俺はぎこちなく顔をそむけ、リリーはくすくすと笑う。"
"でも俺と一緒にワインを試したいと華子の目が訴えるので、無関心を装うのに失敗した、といった風に俺の表情は落ち着く。"




show lilly basic_smile_paj
show akira basic_smile
show hanagown distant
with charachange



"晃さんはたやすく１本目のボトルから栓を抜き、華子がグラスを取りに行く。そして俺は４人にたっぷりと白ワインを注ぐ。"



"白ワインのほうが赤ワインよりもアルコールが少ない、とどこかで聞いたことがあるから、白で始めるのが一番だろう。"


hi "華子に、そしてリリーの旅行に乾杯"



show lilly basic_giggle_paj
show akira basic_laugh
with charachange


$ doublespeak (li, aki, "乾杯！")





show hanagown smile
with charachange


ha "か――乾杯……"

show lilly basic_smileclosed_paj
show akira basic_smile
with charachange



"伝統的な乾杯をして、みんなで薄い黄色の液体をひと口飲む。親と飲んだのとは全然違って、豊かな香りがアルコールの風味をほぼ完全に隠している。"




"多分これが、ちゃんとしたワインの味というものなんだろう。いや、まだお酒に慣れてない俺たち３人のために、好みに合いそうなワインを晃さんが選んでくれただけかもしれない。"


"少なくとも、まだ誰も慣れてないといいんだけど。"


hi "これはなかなかいいですね。もっと何か……きついものだと思ってました"

show akira basic_ending
with charachange


aki "もしこれが気に入らなかったら、他にも何種類か選べたよ"




hi "ワインのことはかなり詳しいみたいですね"


show akira basic_smile
with charachange


aki "ちょっとだけ。どっちかっていうとビール好きなほうだし"


show akira basic_laugh
with charachange


aki "まあ、お酒はひと通り飲むけどね"


"自分の主張を示すかのように、晃さんはワインを再び注ぎ、グラスをあおる。"

stop music fadeout 6.0

show akira basic_smile
show hanagown normal
with charachange



"グラスいっぱいのワインが晃さんののどに吸い込まれていくのを、華子と俺とで静かに見つめる。そのしぐさに感心すべきか困惑すべきかわからないけど、まあ真似しようという気には全くならない。"


show lilly basic_displeased_paj
with charachange


"リリーはお姉さんの自慢話に少し顔をしかめる。でもそうしながらも、グラスからワインをちびちび飲んでいるのがわかる。"


show lilly basic_weaksmile_paj
with charachange


li "ともかく、姉さんの贈り物は開けて試したわけですから、私たちの贈り物のほうに移りましょうか？"

show hanagown worry
with charachange


ha "お――贈りもの？"

play music music_twinkle fadein 6.0

show lilly basic_smile_paj
with charachange


li "ええ、あなたにプレゼントがあるんです。やはり、今日はあなたの誕生日ですから"

show lilly basic_smileclosed_paj
with charachange


li "これは、私から"


"リリーはテーブルの下から、丁寧な包装が施された人形を取り出して華子に渡す。"


"華子はプレゼントを、まるでガラス製品のように扱う。注意深くプレゼントを裏返し、包装紙を止めてあるテープをはがす。徐々に紙が人形からはがれ落ち、エメラルドグリーンのドレスが現れる。"

show hanagown normal_blush
with charachange


ha "これ……綺麗"



"華子にどんな反応を期待していたのかよく分からない。華子の部屋に人形がほとんどなかったので、あまりそういうものには頓着しないんだと思っていたけど、今の華子の眼の輝きはなんだかいつもと違う。"




"華子は包装を解いたときと同じくらい丁寧に、人形の向きを変える。まるで手の中でバラバラになりそうだといわんばかりに。"


show lilly basic_weaksmile_paj
with charachange


li "気に入ってくれて嬉しいわ。実は、久夫さんが選んでくれたの"


"華子は、部屋に自分一人きりではないということを突然思い出したようで、焦点を人形から移す。"

show hanagown smile
with charachange


ha "う――うん、気に入ったよ。あ――ありがとう、リリー、ひ――久夫くん"





hi "実は、俺からもう１つプレゼントがあるんだ……"


"かばんに手を伸ばして、包装紙にくるまれたチェスセットを取り出す。"


hi "ほら。誕生日おめでとう"

show hanagown normal
with charachange


"華子はリリーがくれた人形を丁寧に脇に置き、リリーのときと同じくらい慎重に俺のプレゼントを開ける。"





"間もなくして、チェス盤の四角い格子柄が見え、華子は表面の彫刻に優しく指を滑らせる。"

show hanagown normal_blush
with charachange


ha "あ！"





"ほぼ偶然に、華子は蓋の留め金を開けてしまい、途中で本人がびっくりしている。華子は蓋を開け、灰色のチェスの駒を一つ取り出す。"




"華子はさっきの人形と同じくらい、この駒にも夢中になっているみたいだ。"



hi "珊瑚でできてるんだって。染色されてない、自然の珊瑚。そう説明されたよ"

show hanagown smile
with charachange


ha "ありがとう、久夫くん……"



hi "どういたしまして。やっぱり華子の誕生日なんだから"

show hanagown distant
with charachange


ha "そうだね……私の誕生日……"


"今また反応に少し元気がなくなったように見えるけど、華子は注意深くチェスボードの蓋を閉める。"

show akira basic_lost
with charachange





"晃さんの笑顔がかなりわざとらしい感じになりだしている。晃さんが華子のそばで用心して振る舞っているように見えるところからすると、教室であったことについて何か知っているんだろうか。"



hi "いつかまた勝負しなくちゃね"

show hanagown smile
with charachange


ha "ぜ……ぜったいに最初は久夫くんとするから……"










show ev hanako_presents2:
    truecenter
    subpixel True zoom 1.1
    acdc_warp 10.0 zoom 1.0
with whiteout



"華子はリリーからもらった人形を手に取り、チェスの駒を上に置いた小さなチェス盤と一緒に胸に抱く。"


"そうすると少し落ち着くようで、俺たちはしばらくの間ただ静かに座る。"



"華子が純粋に喜んでいるのを目にした数少ない機会の１つだと思う。彼女は２人との友情を、力の限りしっかりと胸に抱いている。"


show akira basic_boo
show lilly basic_smile_paj
with None

hide ev
with locationchange


ha "ありがとう、リリー。ありがとう、久夫くん"


show hanagown worry_blush
with charachange



"お礼を言う途中で、華子はチェスの駒を落としてしまい、急いで拾おうと少し手探りする。"


show hanagown distant
with charachange



"見つけると、華子はチェスセットを下に置き、神経質な様子でワインをごくごくと飲む。まるで現実が自分の意識に猛スピードで戻ってきて、いちばん早い逃げ道がグラスの中にあるとでもいうかのように。"



hi "なあ、ゆっくりな。そんなに早く飲んじゃだめだよ……"

show lilly basic_weaksmile_paj
with charachange


li "久夫さん、これはパーティーですから……"



"そう言いながらも、声は華子を少し心配しているようだ。やがて、華子ほど積極的にではないものの、リリーも華子を追うようにワインを飲む。"



"リリーはグラスから少しワインをすすり、飲み込む前に舌の上でワインを落ち着かせているようだ。俺はこれが一番いい方法なんだろうなと思って、自分でも同じようにする。"


hi "この会は君の送別会みたいなものでもあるから、少なくとも少しは旅行を楽しむことを願うよ、リリー。おばさんが大丈夫だといいね"

show hanagown worry
with charachange


ha "わ――私も、おばさんが大丈夫だといいな、リリー……"

show lilly basic_surprised_paj
with charachange


"自分自身の家族の境遇を乗り越えて、リリーの幸せを願う華子の熱意に、リリーと俺は少しばかり驚かされる。俺はちょっと感動する。"

show lilly basic_weaksmile_paj
with charachange



li "まあまあ、２人ともありがとう。家族に会ったら、必ずあなたたちのお気遣いを伝えますね"


show akira basic_smile
with charachange


aki "最後には全部うまくいくよ、リリー。心配するなって"




"部屋の雰囲気が目に見えて暗くなったので、俺は話題を変えることにする。"



hi "じゃあ、ケーキを食べ始めようか？"

show hanagown normal
show lilly basic_smileclosed_paj
show akira basic_ending
with charachange


"この控えめな提案には意図したとおりの効果があったようで、みんなの顔がかなり明るくなる。"

show hanagown normal_blush
with charachange


ha "う――うん、お願い……"

show lilly basic_surprised_paj
with charachange


li "ケーキですか？　ケーキがあるなんて知りませんでした……"



hi "ここに来る前に、お菓子と一緒に１つ買っておいたんだ"



show lilly basic_giggle_paj
with charachange


li "すばらしいわ、久夫さん。少なくとも久夫さんだけは、ケーキのことを忘れていなかったんですね"



"こうやって雰囲気が変わることをみんな歓迎しているようなので、俺はかばんからケーキを取り出して切り分け始める。"




"ワインとチョコレートケーキは合わないものだろうと思っていたけど、誰もそんなことは気にしていないみたいだ。みんな食べ始め、会話が一時的に途切れる。"




"はじめのうちは、このアイディアを警戒していた。華子のパニック発作の後とあって、今夜は最悪の事態も覚悟していた。"
"でも、思うに、華子の誕生日にいい思い出をつくるというリリーの考えはうまく行っている。それに、リリーの送別会を兼ねるというのも。"




"プレゼントへの反応から、華子がすごく感謝してくれていることが分かる。"

show lilly basic_smileclosed_paj
show akira basic_smile
show hanagown drunknormal
with shorttimeskip



"華子は自分のグラスにもう１杯ワインを注ごうとするけど、結局いくらかテーブルにこぼしてしまう。"
"華子はもう２、３杯は飲んだから、これまでお酒を飲んだことがなかったことを考えると、ちょっと頭がふらつくように感じているとしても不思議はない。"


show hanagown drunksad
with charachange


ha "ご――ごめんなさい、リリー……汚してしまうつもりはなかったの……私……"


hi "心配するなって。俺がやるよ……"

$ ksgallery_unlock("unlock_ev lilly_hanako_hug_end")
show ev lilly_hanako_hug:
    xalign 0.5 yalign 1.0 subpixel True
    easein 12.0 yanchor 0.0 ypos -0.15
with whiteout


"リリーは横に手を伸ばし、動揺した華子を優しく腕に抱き寄せる。それを見て俺は動きを止める。"


li "大丈夫よ、華ちゃん。あなたがここにいてくれるだけで私は嬉しいわ"


"華子はほんのわずかにうなずいて返事する。リリーがこんな風にして華子を支えるのがちょうどいいんだろうな。もしリリーがそうしてなかったら、華子がどんな風になってたかなんて想像もつかない。"



"２人のこんな様子を見て、こんなに２人が仲良くしている瞬間に立ち会えることをありがたく思う。晃さんでさえ、この光景に笑みをこぼさずにはいられない。"




"こんなに早く新しい友達を作れるとは夢にも思っていなかったし、それに他の誰でもなくこの２人と友達になれたことにはなおさら感謝している。"


stop music fadeout 3.0

show lilly basic_cheerful_paj:
    xpos 0.02
    ease 1.0 xpos 0.0
show hanagown drunksmile:
    xpos 0.48
    ease 1.0 xpos 0.5
with None

hide ev
with locationchange



"２人はゆっくりとお互いから離れ、俺が素早く作業に戻るあいだに、華子はいくらか落ち着きを取り戻す。"




"俺はリリーのティーセットの中にタオルを見つけ、こぼれたワインを拭き始める。だけど拭き終えるころには、華子とリリーは２人してもう１本のボトルのコルクを抜き、自分たちのグラスを満たしていた。"


show akira basic_ending
with charachange



aki "ってことはどうやら、ワインを楽しんでくれてるみたいだね。ただし、このあとおかしくなりすぎないように気をつけろよ"




"みんな律儀にうなずいて同意するけど、未成年にお酒を提供したのがそもそも晃さんであることを考えると、この注意はちょっとおかしく聞こえる。"

play music music_comedy fadein 0.5

show lilly basic_cheerfulblush_paj at Position(xpos=0.0)
show hanagown drunkgiggle at Position(xpos=0.5)
show akira basic_boo
with shorttimeskip



"２杯目のワインは１杯目よりももっと早く減っていき、誰も気づかないうちに２本目のボトルも空になっている。"
"俺たちが飲み干すのを晃さんが手伝う一方で、華子はその晃さんとほぼ同じくらいの量を飲んだらしい。"




"俺もちょっと頭がふらっとするけど、驚くくらいうまく自分の許容量を計算できていたらしい。"
"華子は気だるそうに微笑み、人形の髪をもてあそんでいる。華子は……俺ほどうまく節制できなかったみたいだ。間違いない。"




"華子が元々こんなに酔っぱらうつもりだったとは思わないけど、一気に酔ってしまったみたいだ。身体が華奢なことも、酔いが早く回ってしまう理由のひとつだろう。"




"リリーはグラスを手の上で揺らしながら、縁に指を這わせている。頬は赤くなっているけど、ひどく酔っぱらうまでには至らずに済んでいるみたいだ。晃さんは、いくぶん予想通りだけど、ほぼ変わっていない。"



"でもちょっとだけ、さっきより笑みが大きくなってるかも。多分。"

show hanagown drunkgiggle:
    ease 0.1 ypos 1.15
    ease 0.1 ypos 1.17
with None

show hanagown drunkpout
with charachange


"華子が突然しゃっくりをして、偶然人形を倒してしまう。"

show hanagown drunksad
with charachange


ha "た……多分もう寝た方がいいかも。あ――ありがとう、久夫くん、ありがとう、リリーとああああきらさああああん"




"途中でくすくす笑い出すのをかろうじて抑えながら、華子は晃さんの名前を呼ぶけど、かなりろれつが回っていない。完全に酔っている様子を俺は面白がっているけど、それを少し申し訳なく思うべきか悩む。"



"華子がこんなに気楽に振る舞っているのを見るのは本当に変な感じだ。お酒の助けを借りた時だけ、というのが残念だけど。"

show akira basic_ending at Position(ypos=1.0)
with dissolvecharamove


aki "ほら、手伝うよ"


"華子が部屋から出るのを手伝おうとして、晃さんは立ち上がろうとするけど、リリーが鋭い咳払いをして、晃さんは動きを止めた。"

show lilly basic_planned_paj
with charachange


li "久夫さん、お願いできますか？"

show akira basic_lost
with charachange


"晃さんは少し面食らったようだし、俺も同じだと認めざるを得ない。リリーのお願い自体全然嫌じゃないし、ましてあんな笑顔で頼まれたら……ただ、かなり不意をつかれた。"


hi "も――もちろん。問題ないよ"

hide hanagown
with None

show hanagown drunksad:
    center
    ypos 1.17
with None

show hanagown drunkgiggle_close at Position(ypos=1.0)
show akira basic_smile
with dissolvecharamove

stop music fadeout 4.0



"チェスセットを拾い上げ、華子が立つのを手伝う。晃さんを除けば、俺がおそらく部屋でいちばん素面なことを考えると、多少責任を感じる。華子は片手で人形を大事そうに抱き、もう片方の手を俺に差し出す。"




show hanagown drunkgiggle_close:
    parallel:
        ease 0.5 xpos 0.45
        ease 1.5 xpos 0.55
        ease 0.5 center
    parallel:
        1.5

        "hanagown drunkgiggle_close_ni" with Dissolve(1.0, alpha=True)
show bg school_dormlilly:
    ease 1.0 xpos 0.45
show akira basic_smile:
    ease 1.0 xpos 1.0 alpha 0.0
show lilly basic_planned_paj:
    ease 1.0 xpos 0.05 alpha 0.0
with None

show bg school_girlsdormhall:
    center
    xpos 0.6
    ease 2.5 xpos 0.4
with Dissolve(1.0)

hide akira
hide lilly
with Pause(0.5)

show bg school_dormhanako_ni:
    center
    xpos 0.45
    ease 1.0 center
with Dissolve(1.0)


"俺たちはよろめきながらドアを出て廊下へ向かい、そして華子の部屋に入る。華子は途中で何度も俺にぶつかる。"

play sound sfx_switch

scene bg school_dormhanako
show hanagown drunkgiggle_close at center
with Dissolve(0.2)


"部屋に入ると、俺は部屋の電気を点け、華子は戸棚に目を向ける。そこには優雅な人形が一体、がらんとした部屋を見つめて座っている。"


show hanagown drunksmile_close
with charachange


ha "ほら……ここなら安全だから……"

show ev hanako_dolls
with locationchange


"華子は、人形をもう一体のとなりに慎重に置き、ドレスのしわを伸ばす。"


"髪や服を完璧に整えられて、人形は静かに座っている。リリーの部屋のティーポットとちょうど同じように、人形は華子の部屋を染める単調な白黒とはっきりしたコントラストを成している。"








show hanagown drunksmile_close:
    ease 0.25 ypos 1.05
    ease 1.0 ypos 1.0
with None

hide ev
show hanagown drunkdistant:
    ease 0.25 ypos 1.05
    ease 1.0 ypos 1.0
with charadistant



"華子の２つだけの、本当の持ち物である人形たちが安全なことに満足して、華子はかなりよろめきながら１歩下がって立ち上がる。"
"もし必要なら華子を受け止めようと俺は前に進むけど、華子は助けなしにバランスを取り戻す。"




"華子が下の戸棚をながめるしばらくの間、俺たちは２人して黙って立つ。"

show hanagown drunkdistant:
    ease 1.0 xpos 0.48
    ease 1.0 xpos 0.5
    repeat
with Pause(0.5)




"１、２分すると、華子は左右に少し揺れ始める。これにはかなり戸惑う。"



hi "大……丈夫か？"

show hanagown drunksmile at center
with dissolvecharamove



"俺もこの部屋にいることを今思い出したかのように、華子は顔を上げてこっちを向く。"


show hanagown drunksmile_close:
    ease 1.0 ypos 1.05
with vpunch

stop music fadeout 0.3
play sound sfx_pillow



"意外にも、華子は俺の方に２歩踏み出して俺の身体に両腕を回し、そして頭を俺の胸に預けてくる。"


play music music_heart fadein 0.5


"さっきの飲酒で弱まった感覚すべてが、また生き返ってきているように感じられ、自分の心臓が脈打っているのが聞こえる。"


"華子の息から香るワインの匂い、服を通じて感じられる指の感触、あごの下にある髪の香り……"



"思い切って華子に触ることもせず、俺の両手は自分の前に置かれたままだ。華子を抱きしめたい、抱きしめて、何もかも大丈夫だよと伝えたい。"
"そんな誘惑がすぐそこにある……でも、そうするのは間違っている気がする。本当に、すごく間違ってる。"



hi "華子……"

show hanagown drunknormal_close at Position(ypos=1.05)
with charachange


ha "でも私あなたとリリイイイイと一緒にいたいいいい"


"華子の言葉の伸ばし方は、少しミーシャを思い起こさせる。そんなこと聞いても多分うれしくないだろうけど。"


hi "できないって分かってるだろ。やっぱり華子は女で俺は男なんだし、リリーは寝なきゃいけないし"

show hanagown drunkpout_close
with charachange


"華子は不満げなうめき声をあげる。こんなに過激に振る舞うなんてほんとに変だ。"



hi "心配するなって、明日また会えるだろ、な？"



"安心させるために、華子の頭の上に手を置くことにする。華子がこんな状態のうちは、体に触れるという意味で俺が自分に許せるのはここまでだ。"




"華子は俺の胸に鼻を押しつける。俺はこの状況が余計に不安になってくる。華子の腕が俺の背中できつく締められると、脱出しようと急いで決心する。"



"両手を華子の肩に置き、しっかりと、けど優しく肩を押す。さっきより少しきつく抱きしめられるけど、徐々に華子は離れていく。"

show hanagown drunkworry_close
with charachange



ha "行っちゃやだ……"




hi "華子、たのむよ。ここであんまり時間をかけたら、晃さんとリリーが変なことを考え始めるよ"




"絶対にそうだ。そんな危険は本当に冒したくないし、俺は今ものすごく不安なんだ。"




"今の華子の振る舞いに意味を読み取ろうとなんかしちゃいけない。アルコールで抑制が効かなくなることの他に、人は酔っぱらうと、必ずしも現実に基づかない、色んな行動をとるって読んだことがある。"




"そしてそれを抜きにしても、華子の言っていることは何通りにも解釈できる。華子が大丈夫なら、とにかくできるだけ早くこの部屋から出るぞ。"


show hanagown drunkworry_close:
    ease 0.1 ypos 1.03
    ease 0.1 ypos 1.05
with Pause(0.2)


"華子はもう一度しゃっくりをする。部屋の真ん中に立ってもの寂しそうにしていて、まさにひどい格好だ。"



"どんどんお酒が入るにつれ華子の性格は変わり、そして今、部屋で俺と２人きりになって、さっきの明るさはどこかへ行ってしまったみたいだ。俺たちが心配しないように、陽気に振る舞ってただけなんだろうか？"




"そうだったとしても……華子に一体何をしてやれたというんだろう？　俺自身、自分の病気に関しては、まったく同じことをしているんだから。"


show hanagown drunkworry_close:
    ease 1.0 ypos 1.1 alpha 0.0
with Pause(1.0)

hide hanagown
with None



"自分の思考から離れ、なんとか華子を徐々にベッドへと向かわせる。ベッドの上の乱れたシーツを直そうとする華子の努力は、ほとんど役に立たずに終わるけど。"



hi "今日はごめん、華子。多分このことを何も覚えてないだろうって分かってるけど……誕生日おめでとう。もっと華子のために色々できなくてごめん"


"華子は一瞬俺を見上げる。俺の言ったことが実際に通じたかは全然分からないけど、華子の目が穏やかに閉じられ、そのことについて聞く機会はなくなる。"

play sound sfx_switch

scene bg school_dormhanako_ni
with Dissolve(0.2)


"俺は安心してため息をつき、華子から静かに離れて、部屋を出ながら電気のスイッチを消す。"

stop music fadeout 4.0

scene bg school_girlsdormhall
with locationchange


"リリーの部屋のドアを再び開けるのを少しためらって、華子について聞かれた場合に何て言うべきか素早く練習しようとする。数秒経っても、まだ何も思いつけない。"

scene bg school_dormlilly
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
show akira basic_smile:
    tworight
    ypos 1.18
with locationchange



"ドアを開け、もし通りがかった生徒がいてもワインを見られないようにドアが背後で閉まったのを確認してから、ローテーブルについた２人に注意を移す。"



"晃さんは何気ない笑みを見せていて、リリーも同じだ。華子の部屋とは雰囲気が変わってくれてありがたい。"

show lilly basic_smile_paj
with charachange


li "久夫さんですか？"


hi "ああ。華子をベッドに連れて行ったよ。今はもう寝てる"

show lilly basic_weaksmile_paj
with charachange


li "それはよかったです。正直なところ、あの子があんなにたくさん飲むとは思いませんでした"

show akira basic_lost
with charachange


aki "なあ、大丈夫だって。あの子は今は全然心配ないよ、ベッドで布団にくるまれてるんだし。その状態なら……"




"晃さんの声がぎこちなく小さくなるけど、リリーと俺はなにも言わない。すごく不安や恐れを感じている人は、お酒を飲むことで、絶え間なく続くそういった感情から楽に逃げられるんだろう。"


play music music_night fadein 4.0


"華子のために何かもっとできればいいのに。自分が役立たずに思える。"


"リリーを見て、街で自分の心に問いかけたことについて振り返ってみる。リリーとの関係は友達であって、今までもそういう風にしか感じてこなかったけど、今ならその理由が分かる気がする。"



"初めて会ったときから、リリーは華子と俺のためにそばにいてくれた。でもリリーは誰に対してもそんな感じで、みんなの気分をよくしようとしてくれてるんだ。"



"このことは心に留めておくとして、じゃあ俺と華子との間の絆はいったい何なんだ？"



"俺が授業中に何気なく引き起こしてしまったパニック発作の後、関係を修復して、俺たちはまた友達に戻ったように感じている。でも、華子のことがもっともっと気になってきている。"



"華子と他の女の子をまったく同じように見ているとはいえないけど、あんなことになったら相手が華子じゃなくても気にかけてしまうのが普通なのかもしれない。"


hi "ねえ、晃さん？"

show akira basic_boo
with charachange

show akira basic_smile
with charachange


"晃さんはあくびをしてから俺を見る。かなり遅い時間になってきている。"


hi "華子に何があったか知っているんでしょう？"

show akira basic_resigned
with charachange


aki "うん。リリーが教えてくれた"


show akira basic_boo
with charachange



aki "あの子の誕生日をちょっと明るくするのを手伝いに来られるように、休憩がとれるようかなり頑張って交渉したんだ。あたしと華子、すごく仲良いしね"




"晃さんほど外向的な人からそんなことを聞くのは驚きだけど、華子がリリーを通じて晃さんと知り合うようになったのなら、慣れる時間が持てたのかもしれない。"


show akira basic_smile at tworight
with dissolvecharamove


aki "じゃ、そういう事で、もう行かないと。今でもちょっと遅刻だし"


show lilly basic_oops_paj
with charachange


li "でももうこんなに遅い時間で……"

show akira basic_boo
with charachange


aki "ごめん。仕事が山積みだから、残業だよ"


show akira invis:
    xpos 0.8
with dissolvecharamove



"晃さんはよいしょと立ち上がって、俺の脇を通ってドアへと向かう。部屋を立ち去る直前に、俺たちのほうを振り返る。"


show akira basic_lost:
    tworight
with dissolvecharamove


aki "フライトの時間とか他の諸々のこと、忘れてないよね？"

show lilly basic_smileclosed_paj
with charachange


li "ご心配なく、全部準備してあるわ。出発の日が近づいたら、荷物をまとめるだけ"


show akira basic_ending
with charachange


aki "さすが。じゃあまた今度"


show akira invis:
    xpos 0.8
with dissolvecharamove

hide akira
with None


"それから晃さんは、手を高く掲げてお別れの挨拶をしながらドアを通り、やがて見えなくなる。"

show lilly basic_smileclosed_paj at Position(xpos=0.5)
show bg school_dormlilly at bgright
with charamove


hi "お姉さん……確かにすごい人だね"

show lilly basic_giggle_paj
with charachange



"たぶん今の発言は、実際に口にする前にちゃんと考えるべきだったと思う。にも関わらず、リリーはこの評価をかなりおもしろがっているように見える。"



hi "あんなに飲んでたけど大丈夫？　酔ってるけどただうまく隠してるとかじゃない？"

show lilly basic_smileclosed_paj
with charachange



li "私は本当に大丈夫ですよ。節制できますから。そう言うことなら、久夫さんもとても落ち着いているようですね"



hi "ああ、まあ、リリーの言う節制ってのは俺にも当てはまるみたいだね"


"少しためらって、俺はテーブルを挟んでリリーの正面に座る。自分の考えをまとめるだけのためだとしても、このことは直接話したい。"


hi "ずっと聞きたかったんだけど、決心するのに少し時間がかかって……"


hi "あのパニック発作を引き起こした理由について何か心当たりはある？　何か華子の誕生日に関することだと思ったんだけど、それ以上のことは何も分からないんだ"


hi "晃さんでさえ華子といるときはすごく気を遣ってたから、晃さんも知ってるんだろうね"

show lilly basic_reminisce_paj
with charachange


"リリーの笑みが消え、誕生日会のお祭り騒ぎがもう本当に終わってしまう。"


li "実は、私自身詳しいことを全部知っているわけではないんです"


li "家が火事に遭った、と華ちゃんはあなたに言いましたよね。私と華ちゃんが出会って、長い時間を一緒に過ごしたあと、私にもそれだけ言ってくれたんです"

show lilly basic_concerned_paj
with charachange


li "他には……何も教えてくれたことはありません"


hi "リリーにも言ったことがないんだ……"

show lilly basic_sad_paj
with charachange



li "最悪を想定したとして、華ちゃんの過去に何があったんでしょうか？　孤独な人生？　おそらくは家族の死？　場合によっては、自分のせいで家族が死んだ、と思い詰めているのかも？"




"ほとんど何も知らない華子の過去について思いを巡らせるだけでも、寂しさを感じる。そんな苦難を生き延びて、その記憶を胸に生きることは、想像なんかとは比べものにならないほどつらいに違いない。"




"リリーも同じように暗い顔をしているけど、俺の目の前で少なくともいくらか平静を取り戻しているようだ。"



"確かにワインのおかげで、俺たち２人ともいつもより腹を割って話している気がするけど、いずれにせよこのことを徹底的に話すのはいいことに思える。"



hi "なんだかこのことに関しては自分が無力に思えるよ。あんな風に言われてしまうと、一体華子に何をしてやれるんだろう？"

show lilly basic_sleepy_paj
with charachange



li "お伝えしてもいいのか分からないんですけれど、華ちゃん、私たち２人で様子を見に行った翌日に久夫さんが訪ねてきてくれたって、私に話してくれました"


show lilly basic_weaksmile_paj
with charachange



li "あの発作のあと、あの子がこんなに早く、こんなに大きな一歩を踏み出せるなんて想像していなかったのは事実ですし、それに久夫さんがそんなことをしてくれるなんて思ってもいませんでした"
li "久夫さんの行動がよかったんだと思います"



hi "そんなことないよ、本当に"


hi "ただ……こんな時には、もし山久や、少なくともこの街を離れなきゃいけないなんてことが全くなかったら、その方がいいんだろうなと時々思うんだ。周りに他の人がいない方が、物事がかなりやりやすくなるし"


"この発言に対してリリーがこんなに困った顔をするなんて思ってもみなかった。しばらくの間リリーは考え込んでいる様子だ。"

show lilly basic_oops_paj
with charachange


"リリーは話し出そうとするけど、すぐに止めて、また考え込む。これには少し当惑させられる。"

show lilly basic_reminisce_paj
with charachange


li "私は……"

show lilly basic_smile_paj
with charachange



li "久夫さん、金曜の晩は何か予定が入っていますか？"



hi "金曜の晩？　いや……"


hi "翌日はスコットランドへ飛ぶ日だろ？　着く前から疲れるようなことをするのはいい考えじゃないと思うけど"

show lilly basic_weaksmile_paj
with charachange



li "私のことなら大丈夫です、ご心配なく。できれば明日の晩にしたいんですが、華ちゃんはしばらくの間気分がよくないんじゃないかと思ったので"



"華子の明日の様子を想像して、俺は顔をしかめる。お酒の許容量がかなり低いのに、たくさん飲んで吐かずに済んだだけでも恵まれていると考えるべきなのかもしれない。"


hi "じゃあ、リリーの計画が何であれ俺は参加できるよ。一体何なの？"

show lilly basic_smileclosed_paj
with charachange


li "何も珍しいことじゃありませんよ。ちょっとした遠足です"

show lilly basic_cheerful_paj
with charachange



li "あと、そろそろ帰った方がいいですよ、久夫さん。門限までもう時間がないと思いますし"



"ああくそ、門限か。すっかり忘れてた。"


"リリーのベッド脇にある時計に目をやるけど、文字盤がないのでなんだか変に見える。リリーの目が見えないことを考えると、それが道理にかなっているんだろう。"


"傲慢な見回り警備員に怒られる危険は冒したくないので、立ち上がって、リリーの言うとおり自分の寮に戻ることにする。"


hi "じゃあな。華子もリリーも、朝起きられたら、明日会おう"

show lilly basic_smileclosed_paj
with charachange


li "お気遣いありがとうございます、久夫さん。では、その時に"

scene bg school_girlsdormhall
with locationchange


"そう言って、俺はドアの外に出て廊下を進む。"


"リリーの考えがいいものだったらいいな。"

stop music fadeout 2.0

scene black
with dissolve
label jp_H18:

scene black
with dissolve

play sound sfx_doorknock


"ドアがドンドンと叩かれている。自分の頭に釘が打ち付けられているみたいだ。"



"１回、２回、３回、俺はイライラと長い息を吐く。叩いているのが誰であれ、ただ立ち去って欲しいと切に願いながら、まぶたを固く閉じて耐える。"




"とんでもなく気分が悪い。頭がまるで鉛でできてるみたいな感じで、腕は重いし、すごく吐き気がする。３０分前に目が覚めてからずっとこんな感じだ。ベッドから起き上がる気力さえ出せない。"



"つまり……これがいわゆる二日酔いってやつか。"



"大人ぶってお酒を必死になって試してみたがる少年少女には、これがおそらく一番効く仕打ちってことなんだろうか。こんなに気持ち悪くなるのなら、もう一度飲みたいとは思えない。"


play sound sfx_doorknock



"もう一度ドアがドンドン叩かれ、小さな部屋に音が響きわたる。もうあきらめてくれてればいいのに。あいつらのためにベッドから出るつもりなんて全くない。"



"数秒たち、数分たつ。もうノックの音は聞こえないから、叩いていたのが誰であれ、もう立ち去ったに違いない。ありがたい。"

play music music_dreamy fadein 2.0

scene bg school_dormhisao
with openeye


"時計を見やると、そろそろ服を着替えて授業の支度を始めないといけない時間が近づいている。でも、今の俺にそんなことができるなんて思えない。"


"授業をサボるのは嫌いだけど、この調子だと大して何もできないだろう。鏡を見て確認するまでもなく、自分がめちゃくちゃな顔をしているってことも分かる。"

scene bg school_hallway3
with shorttimeskip


"朝の混雑のおかげで、しばらくの間あまり怪しまれることなく教室の外に立っていられる。昨日学校を休んだことについて、武藤先生が何も変な質問をしないでくれるといいんだけど。"


"具合が悪かった、そこまでは本当だ。隠さなくちゃいけないのはそうなった理由だけ。"


"その真相はうまく省きつつ、切り抜けられる。そう自信を持って、できるだけ自分が普通に見えるように、大股で教室に入る。"

scene bg school_scienceroom
with locationchange


"ドアを開けて一歩足を踏み入れた瞬間、何十もの視線を感じる。みんなそれを隠そうともしないし、いくら何でもこんなのは想像してなかった。"

show hanako emb_emb:
    tworight
    ypos 1.15
with charaenter

show hanako emb_downtimid
with charachange



"教室じゅうを素早く見渡し、華子を見つける。一瞬目が合うと、華子は下を向いてじっと机を見つめる。"




"うっかり話してしまったんだろうか？　武藤先生は教師という意味ではいい人かもしれないけど、校内での未成年飲酒はそうそう見逃してもらえるようなものじゃない。"




"いくらか恐怖におののきながら、先生を見る。"

show muto normal at twoleft
with charaenter


mu "今日は気分はましになったか？"


hi "はい。お気遣いありがとうございます"



"先生は俺に席に着くよう身振りで示す。席に近づくあいだ、自分の身体を支える足が、棒になったような感じがする。今日は長い１日になりそうだ。"


scene bg school_scienceroom at bgleft
with shorttimeskip

stop music fadeout 2.0
play sound sfx_normalbell



"昼休みを知らせるチャイムが鳴るとすぐに、何があったのか聞くために華子の机に向かう。"



hi "華子……言っちゃったの……？"

show hanako emb_emb:
    center
    ypos 1.15
with charaenter


"華子は俺を見上げ、首を横に振る。ああ、本当によかった。"

show hanako emb_downtimid
with charachange


ha "ただ……"


hi "ただ……？"



mi "おやおや、こんにちはひっちゃん。今日また会えてうれしいよ～！"


show bg school_scienceroom at bgright
show hanako emb_downtimid:
    right
    ypos 1.15
with dissolvecharamove

show shizu basic_sparkle at center
show misha perky_smile at twoleft
with charaenter

play music music_happiness fadein 2.0



"俺は顔をしかめ、背後から聞こえる間違えようのない声に目をやる。その口調は、ふだんのミーシャ以上に元気に満ちあふれていて、違和感を禁じ得ない。"





"ミーシャの嬉しそうな笑顔はいつもとまったく変わらない。でも静音の笑顔、これはすごく不吉なことのあらわれだ。その笑顔は『完全に追い詰めたぞ』という意味に変換されて、頭の中に入ってくる。"





hi "やあ、静音、ミーシャ。お前ら、えーと……俺に会えて嬉しそうだな"




show shizu adjust_smug
with charachange


shi "……？"

show misha hips_grin
with charachange


mi "昨日は気分がよくなかったの、ひっちゃん～？"


hi "そう、そうなんだよ。でも少なくとも今は、マシになってる"

show shizu behind_smile
with charachange


shi "……"

show misha cross_smile
with charachange


mi "それを聞いて安心したよ、ひっちゃん"


"静音が俺を罠にはめようとしている気がするのは、なぜだろう？"


hi "本当にそう思ってるようにはあんまり聞こえないけど"

show shizu adjust_happy
with charachange


shi "……"

show misha hips_smile
with charachange



mi "やだなあ、ひっちゃん、わたしたちはひっちゃんがすっかりよくなって純粋に嬉しいだけだよ～"




show shizu basic_happy
with charachange


shi "……"



"静音は間違いなく喜びに満ちあふれている。静音がこんな風になる理由なんて１つしかない。ああ、なんてこった。"


show misha perky_smile
with charachange



mi "実際、わたしたちはひっちゃんのこと、すごく心配してたんだよ。だって……"


show misha sign_smile
with charachange


mi "ひっちゃんと、華子と、リリーはみんな、同じ日に授業を休んでたんだから"




"ああ、やっぱりバレてた。すっかりバレてるから、打ちのめされてため息をつくことしかできない。"



hi "きっとお前ら、この件でいろいろ想像してると思うけどさ。もしできたら……誰にも言わないでもらえないかな？"




show misha cross_smile
with charachange


mi "それはちょっと手遅れだね、ひっちゃん～"



"教室に入ったときに向けられた視線を考えると、きっとミーシャの言うとおりなんだろう。でも、ことはまだ明白な非難というよりも、むしろ漠然とした疑いの段階でしかないようだから、きっと大丈夫だ。"


show hanako emb_downsad
with charachange



"華子が、さっきより少し深く頭を垂れる。こんな注目は俺にとっても充分やっかいだし、華子にとっては言うまでもないことだ。静音とミーシャの反応を見るに、２人だってそれに気づいているだろう。"


show shizu basic_angry
with charachange


shi "……"

show misha hips_frown
with charachange



mi "なんでわたしたちがひっちゃんをこんなに困らせてるかっていうと、昨日の朝ひっちゃんに無視されたからなんだよ～！"



"昨日の朝？　その時は全般的にひどい状態で意識がもうろうとしていたから、思い出すのに少し時間がかかる。"




hi "ああ、そうか、ドアのノックだ。あれはお前らだったの？"




show shizu behind_frown
with charachange


shi "……"

show misha cross_frown
with charachange



mi "そうだよ、せっかく朝早くに苦労してひっちゃんの寮まで行ったのに、ずーっとそこで放ったらかしにされたもん"



hi "ごめん、俺……吐き気？　がして困ってたんだ。吐き気で困ってた"



"信じてないな。しかたないけど。"


show shizu behind_frustrated
with charachange


"静音はあきらめて頭を垂れ、ポケットに手を伸ばす。"


"白と黄色をしたものがポケットから少し飛び出ていて、それを静音が引っぱり出す。とても鮮やかな飾りがついた封筒だ。"

show letter_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"静音が封筒を俺に向けるので、当然俺が受け取る。"



mi "わたしたちがあれだけ頑張って渡そうとしてたのはこれなんだよ、ひっちゃん！　ちゃんと確かめないから……"


stop music fadeout 5.0



"封筒に書かれた文字を俺の目が認識して、ミーシャの声が聞こえなくなる。"


stop music fadeout 0.3


hi "岩魚子……"


"少しの間封筒を見つめ、ふと自分の周りに人がいることを思い出す。"

show misha cross_smile
show shizu behind_blank
show hanako emb_timid
with None

show letter_insert:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide letter_insert
with None



"３人の顔には、とても不思議そうな、そして幾分こちらを探るような表情が浮かんでいる。なんだか今は一人きりになりたい。"


show hanako emb_sad
with charachange


ha "いわなこ……？"



hi "何でもない。２人とも、これ持ってきてくれてありがとう"


show misha hips_grin
with charachange


mi "これを渡すために色々がんばったんだから、まあその通りだよね～"

show misha hips_frown
with charachange



"俺は後ろに下がってさよならを言う。"
"ドアから出て行く間も、ミーシャは芝居がかったふくれっ面をするけど、静音と華子は俺の反応に興味を持ったままなのが見てとれる。あとでいろいろ尋ねられたりしないといいんだけど。"


$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

scene bg school_gardens2
with locationskip

play music music_serene fadein 2.0


"庭園の香りはいつも通り、すごく心地良い。学園の規模そのものを別にすると、庭園の広さと状態が、学園の資金の潤沢さを一番はっきり示している。"



"明るい緑色の芝生の上で、たくさんの生徒が昼ご飯を食べ、おしゃべりをし、そして遊んでいる。何人かの職員までもが、生徒を見守りながら長いコンクリートの道をぼんやり歩いて、ここでの夏を楽しんでいる。"



"生まれ育った街ではこんな景色を目にしたことがなかった。遠足では見たかもしれないけど、学校や住んでいたところの近くでは一度も見ていないのは確かだ。"


"手紙を読むために座っているベンチまで、夏場の太陽を浴びてあたたかくなっていて、暑さのおかげでまだ一度も制服のブレザーを着ていないことを思い出す。"

show letter_open_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"そう考えると、便せんを飾るひまわりや、鮮やかな黄色が散りばめられた模様はこの季節にちょうど合っている。ここに書かれた言葉も似たようなものならいいのに。"


"このやっかいな手紙が俺の前に現れた時、岩魚子とのことからはなんとか立ち直れたと思っていた。"



"手書きの文字を見ると、せいぜいかすかに見覚えがあるといったくらいで、もう一度眺めてようやく、岩魚子がよくピンク色のペンで書いていたことを思い出す。"
"ほかにいい言葉が見つからないけど、岩魚子はいつも、とても女の子らしかった。"




"でも同時にとても繊細でもあった。岩魚子のそういった面が好きだったかはずっと分からなかった。ただ、この手紙を受け取った今では、その問いはほぼ無意味なものになった。"



"手紙の冒頭は、岩魚子の日常のできごとについて、近況を知らせているにすぎない。俺が昔いたクラスは新年度を幸先良くスタートさせ、多くの生徒が今後の試験に不安を感じている、などなど。"



play sound sfx_paper

hide letter_open_insert
show letter_open_insert_2
with charachange



"でもその手紙は、手短ではあるけどとても個人的な文章で終わっている。手紙の大部分が、ただ最後の衝撃を和らげようとして書かれたような気が少しする。"


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

$ written_note("なんとかして自分の気持ちを伝えたいと思ったけど、それにふさわしい言葉は見つけられませんでした。あなたを慰める言葉を、私は何も言えませんでした。あなたのことがこんなに好きだったのに、一番大事なときに支えることができなくて、本当にごめんなさい。でも少なくとも今は、やっと、もっと自分に正直になれます。\n\n\n\n")

$ written_note("２月と３月の、あの静かな日々に戻れるなら、自分をあきらめないで、とあなたに伝えると思います。きっとそう言います。なんでもいいからあなたに話しかけてさえいれば、こんなに遠くへ行ってしまうこともなかったかもしれません。あなたが自分の力で立ち直れているといいな、と思います。\n\n\n\n")


$ written_note("今の私たちは物理的にも遠く離れてしまっていて、それがなんだかずっと決定的なように感じます。もう一度会うことはできるのかな。もしかしたら、会わないほうがいいのかも？　でも、もし連絡を取りたいと思ったら、ぜひお返事ください。あなたの新しい学校のこととか、今どんな風に過ごしているかとか、とても聞いてみたいです。元気でね。\n\nかしこ、\n岩魚子")

window show

$ renpy.music.set_volume(1.0, 1.0, channel="music")


"というわけで、それで終わりだった。俺たちの関係は終わった。感じよく、きちんと、そしてすっきりしていて、あいまいさは全くない。"



"もう一度やり直せるかもしれない、なんて幻想には一切しがみついていなかった。"
"岩魚子が最後に訪ねてきたとき、俺たちは一言も発さなかった。最後に立ち去るとき、岩魚子が言った『さよなら』のひとことを除いては。"




"いずれにせよ、これでより決定的になったような気がする。この手紙は、俺たちが２人で挑んで、そして失敗に終わった実験の、クライマックスみたいなものだ。"



show letter_open_insert_2:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide letter_open_insert_2
with None



"大きな叫び声で手紙から目を離す。ただ何人かの生徒が馬鹿騒ぎをしているだけで、近くに立っている先生の１人が、話をしようとそいつらに近づいている。"


mystery "大丈夫？"

show yuuko neutral_down at center
with charaenter


"遠慮がちな声が横から聞こえる。華子かなと少しのあいだ思ったけど、実際には優子さんだ。"


hi "ああ、こんにちは、優子さん。図書室にいると思ってました"

show yuuko closedhappy_up
with charachange


"優子さんは雰囲気にとても合った明るい笑顔を見せ、空になったロールパンの包み紙を見せびらかす。なにか軽く食べる間、誰か他の人に代わってもらっているに違いない。"



"それを見て、まだ何も食べていないことを思い出す。でも腹は減ってないし、昼食を１回抜くくらいどうってことないだろう。"


show yuuko smile_up
with charachange


yu "ここ、座ってもいい？"


hi "もちろん。どうぞ"

show yuuko neutral_down at Position(ypos=1.15)
with dissolvecharamove


"優子さんが腰を下ろすあいだに、俺は素早く手紙を封筒に滑り込ませ、ベンチ脇に立てかけてあるかばんにそっと入れる。優子さんは横にあるゴミ箱に包装紙を捨てる。"


"他にあまりすることもないので、俺は身体をうしろに反らせてできるだけ陽射しを楽しみながら、静かに手紙について思案する。"


"青々とした芝生、澄んだ青い空……すべてが昔とは全然違っている。山久が建つ丘から周りにある木々まで、周囲の環境までもが、記憶にある都会の景色とは正反対だ。"



"ホームシックになる、というのはこういうことなのかもしれない。その反面、これは全然いやな感覚じゃない。山久周辺の地域の雰囲気は、確かに全然違うけど、快適でもある。これなら慣れていけそうだ。"


show yuuko smile_down
with charachange


yu "ねえ、中井くん？"





hi "はい？"

show yuuko worried_down
with charachange



yu "さっき『大丈夫？』って訊いたのに答えてくれてないよ。何も言わないでおくつもりだったけど、今もまだ困ってるみたいだから"


show yuuko panic_up
with charachange


yu "でも、もし何も言いたくないのなら、それでいいよ。私全然気にしないし。えっと、こ――こんな変なこと聞いてごめんなさい……"


hi "かまいませんよ"


hi "ただ……山久に来る前の知り合いから手紙をもらったんです。それで色々考えさせられました"


hi "病気のせいで起きた厄介事はほとんど乗り越えられたと思ってたんですけど、今はあんまり自信がありません。こんな手紙、見なきゃよかったって感じです"

show yuuko worried_up
with charachange


yu "それはよくないと思うよ、中井くん"



show yuuko neutral_down
with charachange



yu "私が彼氏に振られたとき、本当に突然だったし、彼は理由なんて全く教えてくれなかった。私、初めはすごく落ち込んでたけど、もう彼を許すことに決めたの"



hi "許すんですか？　少なくともその人、ちゃんと優子さんと話し合おうと思えばできたんじゃないんですか？"


yu "他人とうまく仲良くなれない人ってよくいるでしょ。彼はいつもそんな感じだったから"


yu "いろいろ考えて、理由があって彼と恋に落ちたんだって思うことにしたの。いい人だったし、私が彼の立場だったら、話をしようとするのは同じくらい難しく感じただろうなって"



hi "俺には……もらった手紙とその話がどうつながるのか、いまいち分からないんですけど"

show yuuko worried_up
with charachange


yu "つまり……うーん、どう言えばいいかな……"


yu "その人にとってその手紙を送るのはすごく大変だったはずで、もしそうなら、何をどう書いたらいいか、すごく頑張って考えたはずってこと"


"岩魚子はなんとかこの手紙を書き上げ、俺たちの関係に終止符を打った。そんなこと、俺には決してできなかっただろう。"


"一方で俺はここにいて、リリーが日本を離れるしばらくのあいだは特に、できるだけ華子を守り、力になろうとしている。自分自身の問題にうまく対処することもできていないのに。"

show yuuko neutral_down
with charachange


yu "それで通じるかな？"


"返事をせずに額にしわをよせる俺を見て、優子さんは俺が信じてないって思ってる。どこかの誰かさんとまったく同じで、優子さんは本当に顔色を読みすぎる。"




hi "ええ、わかりました"



hi "実際、手紙はちょっとショックでしたよ。俺、自分を騙してたんだと思います。山久に来たときに俺の人生はリセットされた、って。でもいま急に、そうじゃなかったってことに気づいて"
hi "こういう気持ちとどう折り合いをつければいいのか、ちょっと途方に暮れてるんです"


show yuuko worried_down
with charachange


yu "それは、私にはあんまりお手伝いできないことだと思う。ごめんね"



hi "大丈夫です。優子さんと話せて、頭の中でものごとが少しうまく整理できたと思うんで、とにかく感謝してます"


show yuuko closedhappy_down
with charachange


"優子さんはうなずいて優しく笑う。優子さんはいい人だから、よく神経質になってしまうのを気の毒に思う。"

play sound sfx_warningbell

show yuuko panic_up
with vpunch



"学校のチャイムが鳴り響き、２人ともひどく驚かされる。"




yu "ああ、チャイムが鳴る前に戻ってなきゃいけないんだった！"



hi "あちゃー……"

show yuuko worried_up at center
with Dissolvemove(0.3)


"優子さんはベンチから飛び降りて、それ以上何も言わず、ほぼ駆けっこといった感じで走り出すけど、さっきまで俺と話してたってことを思い出し、突然くるりとこちらを向く。"

show yuuko neutral_up
with charachange


yu "中井くん、またね。元気出してね、分かった？"



hi "努力します。ありがとう、優子さん"

stop music fadeout 9.0

hide yuuko
with charaexit



"素早くお辞儀をして優子さんは別れの挨拶をし、急いで図書室に向かい始める。優子さんの駆けていく姿を見て、すれ違う数人の生徒たちが好奇の目を寄せる。"
"その生徒たちは昼休みを楽しんだあと、教室に戻るため、やる気のなさそうな感じでとぼとぼ歩いている。"



"俺もしぶしぶベンチから立ち上がり、埃を払ってその生徒たちに合流する。"


"庭園を通って本棟に歩いて戻るあいだでさえ、かばんの中の手紙について、ずっと頭のどこかで考えつづけている。"

stop ambient fadeout 2.0
stop music fadeout 2.0

scene black
with dissolve
label jp_H19:

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0

scene bg city_street2_ni
with locationchange


"通りを歩いていると、とても懐かしさを感じる。山久が、昔住んでいた場所とはおそらく正反対のようなものである一方、夜の都市部はすごく慣れ親しんだ感じがする。"



"夜空高くに輝くまばゆい電光掲示板、光で闇を貫く街灯、それに仕事を終えて楽しんでいる社会人や、話に夢中なデート中のカップル達。絶えず目移りする。"


"そのつもりがなくても、街のあらゆる趣きに浸らずにはいられない。感じているその親しみを、舌の上で甘い飴を転がすように味わう。"

show akira basic_boo_ni:
    center
    xpos 0.59
show lilly cane_smileclosed_cas_ni:
    center
    xpos 0.41
with charaenter


"リリーは杖を前後に揺らしながら俺の左側を歩く。晃さんに話しかけながら、案内役の晃さんの腕につかまっている。"


"タクシーやバスでの移動に比べて、晃さんのかなりかっこいい車で送ってもらうのは、とても楽しい体験だった。"

show hanako invis_close:
    center
    xpos 1.0
with None

scene bg city_street2_ni at bgleft
show akira basic_boo_ni:
    center
    xpos 0.39
show lilly cane_smileclosed_cas_ni:
    center
    xpos 0.21
show hanako basic_distant_cas_close_ni at tworight
with dissolvecharamove



"だけど、俺の右側にいる人にとってはそうでもなかったかもしれない。"
"リリーは晃さんの運転には慣れていたし、俺もちょっとした刺激って感じでかなり気に入っていたけど、華子は移動の間はずっと、ドアにしっかりしがみついていた。"


show hanako basic_smile_cas_close_ni
with charachange


ha "よ――夜はいろんなものがすごく、す―素敵に見えるね……"

show hanako emb_downtimid_cas_close_ni
with charachange


"たまたま誰かと目が合ってしまい、華子はまたもやさっとうつむく。"


hi "ああ、そうだな"



"いろんなことを考えて気が散ってしまい、世間話をなかなか続けられなくて、あまり思いやりのある言葉を返せない。"




"都心部の景色のほかに、注意散漫になってしまう原因の１つは、華子の見た目だ。"




"制服やパジャマ姿以外の華子を見るのはこれが初めてだった。校門で待ち合わせをして、最初に華子の服装を見たとき、俺は驚いて言葉を失った。"



"人が近くを歩いていると、華子はかなり下を向く。そのことを考えると、今かぶっている帽子にはおしゃれ以上の意味があるんだろう。"



"初めのうちは、俺たちを都心部に連れ出すというリリーの計画は心配だった。でもいざ夜になってみると、リリーはちゃんと考えていたってことがわかった。"
"夜の闇が華子のやけどの傷跡をうまく隠してくれるおかげで、華子に注意を向ける人はあまりいない。"




hi "さて……街中に着いたけど、これからどうするんですか？"



show akira basic_smile_ni
with charachange



"晃さんがにっこりと笑う。そもそもみんなで出かけるのを提案したのはリリーのほうかもしれないけど、これからどうするか決定を下すのは晃さんなんだろうな、と何となく思う。"


show akira basic_ending_ni
with charachange


aki "まあそのうち分かるさ。とりあえずついて来て"



"俺はうなずき、できるだけしかめっつらをしないようにする。華子の誕生日会でお酒が出てきてからは、あまり晃さんの判断を信用していない。"


$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.1, 0.0, channel="music")
play music music_jazz fadein 14.0

scene bg city_street3_ni
with locationchange


"俺たちは歩き続け、カフェやレストラン、その他の飲食店をどんどん通り過ぎていく。"


"ときおりスーツ姿の酔っぱらいが、たいてい別の人に身体を支えられながら居酒屋から出てくる。でも、この地区周辺のお客さんの大部分は若くておしゃれだ。"



"通り過ぎざま、それぞれのお店で色んな音楽が聞こえては小さくなっていく。重なって生み出される不協和音は耳障りだけど、昔の友達と都会で過ごした頃の記憶が強く思い出されて、あまり気にならない。"



"華子と俺はリリーや晃さんから少し離れて、ふらふらと歩き始める。横からドンと軽めの音が聞こえて、俺は歩みを止める。"

show hanako defarms_shock_cas_ni
with vpunch


ha "ご――ご――ごめんなさい……！"


"華子は謝ってお辞儀する体勢をとったけど、姿勢を戻す頃には、ぶつかられた会社員のおじさんは、いい加減な謝罪のことばをつぶやいて歩き去っていた。"

show hanako emb_downtimid_cas_ni
with charachange



"このことに華子は少し戸惑ったようで、俺と足並みをそろえようと小走りになりながら、また深くうつむくようになっている。きっと自分の正面じゃなくて、下の方ばかり見てたから、人にぶつかったんだろう。"


show hanako emb_timid_cas_close_ni
with charachange


"俺は横にいる華子に少し近づき、片手を肩にまわして華子を引き寄せる。"


ha "久夫くん？"



hi "大丈夫。もっと俺のそばを歩いていいんだよ、もし華子がそうしたいならね"

show hanako emb_smile_cas_close_ni
with charachange


"華子はしばらくためらい、やがて同意してうなずく。"

stop ambient fadeout 1.0
$ renpy.music.set_volume(0.5, 10.0, channel="music")

scene bg city_karaokeext_ni
show crowd_ni
show akira basic_smile_ni:
    center
    xpos 0.39
show lilly cane_listen_cas_ni:
    center
    xpos 0.21
show hanako basic_smile_cas_close_ni at tworight
with locationskip

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 2.0



"これが目的の店かな、と思った所を通り過ぎることを何度か繰り返しながら、ようやく晃さんの目指す場所にたどり着く。"
"今や歩道橋の下に俺たちはいて、いちばん派手で、明るく照らされていた場所も通り過ぎている。"







"少しびっくりしている。周りにいる人たちの平均年齢は明らかに俺たちより高いし、タバコの煙の匂いがかなり厚くたちこめている。"
"でもこの場所は全然みすぼらしい感じではないし、タバコの匂いに対するリリーの反応を見るのはちょっとおもしろい。"




"周りの人の低い話し声に埋もれながらも、ジャズがお店の中から聞こえてくる。薄暗く照らされた看板を見上げ、そのわけがはっきりと分かる。"


hi "ジャズクラブか。正直、こんなの予想してなかったよ"

show lilly cane_giggle_cas_ni
with charachange


"リリーは楽しそうに、鼻にかかった声を出してほほ笑む。"

show lilly cane_smileclosed_cas_ni
with charachange



li "なんだか、予想しておくべきだったような気がしますよ、姉さん"




"外で話をしていると、色んな人に、変に横目で見られていることに気づく。みんな俺たちを見つめてしまっていることに気づくとぎこちなく目をそらすけど、それで見られているということがよりはっきりする。"




"さっき歩いてるときも、時々こんなことがあったけど、今のほうがずっと明白だ。"



"こんな経験、俺はこれまでの人生でしたことがなかった。標準よりちょっと背が高めで、人並みの容姿の日本人青年。何もしなくても注目されてしまうタイプの人間じゃない。"

show akira basic_laugh_ni
with charachange



aki "おいおい、少年少女だからってこんなの楽しめないとか、そんなことないだろ？"



hi "まあ……音楽のことでしたら、俺はあんまり気にならないですけど"

show hanako cover_bashful_cas_close_ni
with charachange


ha "わ――わ……私も……大丈夫……"



"華子はかろうじて言葉を絞り出す。山久で俺たちだけで過ごしているときとは正反対の様子だ。都市部に出て楽しい時間を送るはずが、かなり神経質になってしまっていて、すこし残念に思う。"





"下ばかり向いているので、華子の表情がなかなか読み取れない。顔の傷跡のせいで華子があまり街中に出てこないのは間違いないし、俺自身の傷はすぐに隠せることを少しありがたく思う。"




"リリーも同じように人の視線を引くけど、明らかに別の理由からだ。リリーは日本人には全然見えないし、晃さんもそうだ。遠くから見ると、彼女の目が見えないことより、容姿のほうがずっと目に付きやすい。"



"リリー自身はこの光景を目にすることができないかもしれない。だけど、声の届く距離じゃないと思って変なことをささやいている周りの人達の声が聞こえているのは間違いない。"


"いずれにせよ、リリーは注目されて迷惑そうな様子も、嬉しそうな様子も見せない。"

hide akira
hide lilly
with charaexit


"でも、晃さんは今でもいつも通り自信に満ちた様子だ。さっと微笑んで、大股で、横に立つリリーと一緒に店に入っていく。華子と俺もあとに続く。"

stop ambient fadeout 1.0
$ renpy.music.set_volume(1.0, 10.0, channel="music")

scene bg city_clubint:
    center
    xpos 0.6
show crowd
with locationchange

$ renpy.music.set_volume(0.8, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 1.0


"店内の明かりに目を慣らす必要があると思っていたけど、中はそんなに外よりもまぶしくない。"



"テーブルやカウンターに置かれるグラスの音や、常連らしき客がかすれ声でするおしゃべりに混じって、さっきの音楽が今はもっとはっきり聞こえる。"
"右側に目をやると、音楽の出どころがわかる。ジャズグループがいくつかのテーブルをはさんで演奏している。"




"客のほとんどが男性のようで、何人か女性もいるけど、３０歳より下に見える人は１人もいない。もちろん、俺たちを除いて。"



"まるで１９２０年代に足を踏み入れたような感じで、とてもいい雰囲気だ。唯一、自分の年齢のせいで完全にくつろげてはいないけど、もしもっと年をとっていたら、きっとかなり居心地よく感じるだろう。"

show hanako basic_smile_cas_close at tworight
with charaenter


"誰にも見られていないから、華子もさっきより少しリラックスしているようだ。みんな内輪でおしゃべりしたり、お酒を飲んだり、バンドが演奏するのを見たりしている。"

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

show akira basic_smile behind crowd:
    center
    easein 1.0 ypos 1.06
hide crowd
with Dissolve(1.0)


"晃さんは周りを見渡すこともなく、ひょいとカウンターの席に腰を下ろす。きっと前にもここに来たことがあるんだろう。"

show lilly basic_smileclosed_cas:
    twoleft
    xpos 0.25
    easein 1.0 ypos 1.1
with Dissolve(1.0)


"リリーは杖をたたみ、バースツールやカウンターの縁を手探りで確かめて晃さんのとなりに座る。バーテンダーは少しのあいだグラスを磨く手を休めて彼女を見、そしてグラスを置いてこっちにやって来る。"





"バーテンダー" "こんばんは、お嬢さま方。お飲み物は何になさいますか？"




show akira basic_ending:
    center
    ypos 1.06
with charachange


aki "スコッチで。リリーは？"

show lilly basic_cheerful_cas:
    twoleft
    xpos 0.25 ypos 1.1
with charachange


li "私はシャンパ――{w=0.5}{nw}"


show lilly basic_surprised_cas
show akira basic_boo
with vpunch


"晃さんの黒スーツの肘が、リリーの脇腹に鋭い一撃をくらわす。"

show lilly basic_weaksmile_cas
with charachange


li "オレンジジュースをお願いします"




"バーテンダー" "かしこまりました。すぐお持ちします"




"バーテンダーが、２人が注文した飲み物を注ぎ始める。少しして、晃さんは華子と俺もここに来ていることを突然思い出したようで、俺たちのほうに向き直る。"


show akira basic_smile
with charachange



aki "２人ともなにか飲む？　それともそこにずっと立ってるつもり？"



"華子は少しそわそわし始めている様子だ。どこに座っても、華子の隣には誰かがいるし、リリーとは違って華子が確実に２０歳以上に見えるとは思えない。"

show bg city_clubint:
    xpos 0.4
show akira basic_smile:
    xpos 0.3
show lilly basic_weaksmile_cas:
    xpos 0.05
show hanako basic_smile_cas_close:
    xpos 0.5
with charamove


"周りを見渡すと、右手にゲームコーナーがあり、一組のビリヤードテーブルが隅にあるのが見える。両方とも使われてないみたいだ。"



"華子の方を見て、ビリヤードをしたいか聞こうとするけど、華子はすでに熱心にその方向を見ている。今では俺たちはほとんど言葉を交わさなくてもうまくやっていける、ということなのかもしれない。"



hi "あっちでビリヤードやってきます"

show akira basic_boo
with charachange


"晃さんは上体を反らして俺の方を見やり、肩をすくめて座り直す。"

show lilly basic_giggle_cas
with charachange



li "お相手は私だけだけど、姉さんはそれで我慢しないといけないみたいね。残念でした"


show akira basic_smile
with charachange



aki "２人とも、楽しんでおいで"


$ renpy.music.set_volume(0.8, 1.0, channel="music")
stop ambient fadeout 14.0

hide hanako
with charaexit


"俺たちはきびすを返し、誰にも使われていない店の隅へと向かう。先頭に立つのは華子だ。"


"みんなから離れて、静かに楽しくゲームができるという期待から、華子の歩みは明らかに速まっている。その視線は大事なビリヤードテーブルに固く据えられたままだ。"

scene bg city_clubpool
with locationchange


"テーブルは標準サイズで、周りは暗いにもかかわらず、頭上の明るい電灯のおかげでちゃんと照らされている。何か……よくわからないもの……の大きな絵が、壁を覆っている。"


"この隅のあたりにはあまり人がいないため、華子の緊張は少し解けているようだ。"

show hanako basic_smile_cas at center
with charaenter


ha "や……やり方し――知ってる？"


hi "そんなに詳しくはないけど、ああ、知ってるよ"

show hanako basic_bashful_cas
with charachange


ha "じゃあえーと……エイトボールは？"


hi "もちろん"

hide hanako
with charaexit



"壁に据えられたひと組のフックから、華子がチョークと２本のキューを取ってくる。俺はテーブルポケットからボールを取り出し、下にある棚から木枠をつかみとる。"




"俺がテーブルの準備をするあいだ、華子は辛抱強く待っている。"
"俺は最後のボールを木枠に入れ、いくつか最終調整をする。完璧主義なので、どうしても一番下の列のボールをテーブルの縁ときっかり垂直にしたくて、何度も格闘する羽目になる。"




"ボールがちゃんと配置されてゲームの準備ができたので、俺は後ろに下がり、差し出された華子の腕からキューを受け取る。先端を素早く点検し、状態がいいことに満足する。"



hi "ってことはつまり、前にもプレイしたことがあるの？"

show hanako cover_bashful_cas
with charaenter


ha "一度……か二度。ち――ちょっと……ルールが分かるだけ"

$ renpy.music.set_volume(0.5, 1.0, channel="music")



"２人のあいだの空気がちょっとぎこちなく感じられる。人前にいることを考えれば当然のことだけど、華子はまだかなり緊張している。"



"華子でさえ、徐々に沈黙が多くなっていると感じはじめたようで、どもりながらも静かに話し始める。"

$ renpy.music.set_volume(0.8, 1.0, channel="music")

show hanako basic_worry_cas
with charachange


ha "ど――どっちが……ブ――ブレイクする？"


"俺はしばしの間考え、ポケットの中に手を伸ばしてコインを取り出す。"


hi "表なら俺で、裏なら華子ね"


"華子が同意してうなずく。俺はコインを空中にはじき飛ばし、つかむ。つかんだ右手を翻し、コインを左手の甲の上に置く。"


hi "ブレイクするのは華子ってことみたいだね"

$ ksgallery_unlock("ev hanako_billiards_distant")
scene ev hanako_billiards_break
with locationchange


"華子はふたたびうなずき、テーブルの端に場所をとる。"


"華子はふだん俺のそばにいるとき、ここまで静かじゃない。だけどそれが、さっき華子が自分の過去について少しだけ口を滑らせてしまったせいなのか、あまり自信がない。"

scene bg city_clubpool
with flash

play sound sfx_billiards_break



"慣れた手つきでキューが引き寄せられ、それから鈍い音を立ててキューボールのど真ん中に当たる。"
"白いボールが、なめらかで広々とした緑のテーブルを横切るように滑り、反対側の端に丁寧に置かれたボールに突き当たる。"




"ボールが高速でテーブル中に転がる。いい感じにボールがテーブルのあちこちに散る、いいブレイクだった。"
"すでに俺の目は、ポケットするのが一番簡単そうなボールを選びだそうと、１つ１つのボールに素早く視線を送っている。"


play sound sfx_billiards


"華子が脇からしりぞき、今度は俺がショットを打つ。"

show hanako basic_smile_cas at center
with charaenter


ha "すごいね"



"華子がそう言って初めて、俺は自分が狙ったボールがポケットに沈んでいることに気づく。"



"華子の顔を見ると、かすかに笑みが浮かんでいる。ビリヤードをすることで少し緊張がほぐれているようでよかった。"


hi "じゃあ、俺がストライプボールを狙う方みたいだね"

show hanako cover_distant_cas
with charachange



"俺は一歩後ろに下がり、華子に次のショットを打ってもらおうとするけど、なかなかテーブルに近づいてくれない。それどころか、華子は少しうつむいて腕をこすっている。"



"これは、なにか言いたいけど、実際に言えるか自信がないときに華子がするしぐさの一つだ。今ではもう俺にも見分けがつく。"


hi "どうしたの？"

show hanako cover_bashful_cas
with charachange


ha "ただ……す――すてきな……笑顔だったなって。これ……プレイするの好き？"


"俺はひと息ついてテーブルにもたれかかる。"


hi "ああ、好きだよ。けど笑ってたのは、これがかなり懐かしいからだと思う"

show hanako def_worry_cas
with charachange



"華子は何か聞きたそうな様子で首をかしげる。"



hi "前に住んでたところの近くにあるゲームセンターで、しょっちゅう友達とビリヤードしてたんだ。夜もやってた"

show hanako basic_worry_cas
with charachange


ha "ご――ご両親は……"


hi "共働きだったから、俺が家にいなくても気にしなかったみたい。ちょっと勉強するだけでずっと学校の成績も良かったから、夜にほかのことをする時間がいっぱいあったんだ"

show hanako basic_distant_cas
with charachange



"華子の臆病さが、何か聞きたい気持ちに打ち勝ったようで、会話はそこで終わる。それに応じるように、俺はテーブルを離れ、華子に次のショットを打ってもらう。"



scene ev hanako_billiards_smile
with locationchange


"落とすのが簡単そうなソリッドボールがあまりないので、華子は腰を曲げ、少し時間をかけて姿勢をきちんと正す。"

scene ev hanako_billiards_smile_close:
    truecenter
    zoom 1.0 subpixel True
    easein 6.0 zoom 0.8
with flash



"華子はチェスをするときと同じように、リラックスしているけれど、意識を集中させているというふうな顔つきを見せる。"
"スポーツ選手がときどき、邪魔なものが全く意識のなかに入ってこない状態になるっていう話をしているけど、華子もそういうことができるんだろうか。"





"華子はいい姿勢を保っている。もちろん俺よりもいい。ビリヤードの教本に書いてあるような姿勢にすごく近い。"
"一方で俺は、打とうとしているショットに一番合っていると思える姿勢を取ろうとして、身体をゆがめる傾向がある。"


scene ev hanako_billiards_serious
with locationchange


"華子がキューの位置を調節する。キューを引き寄せ、ちゃんと姿勢を保っているか確かめるために何度か予行演習をする。"


"華子はかなり本気でゲームをしている。読書以外で俺が知っている、彼女のたったひとつの本当の趣味だ。こういった体験を華子と共有できて嬉しく思う。"

scene bg city_clubpool
with flash

play sound sfx_billiards


"念入りに検討してから華子はショットを打つ。キューボールはコーナーの近く、少し扱いにくそうな角度で置かれているボールに向かって音を立てて進んでいく。"



"華子の慎重な準備が功を奏し、キューボールが狙っていたボールに命中して、そのボールはコーナーポケットへと転がっていく。"
"一瞬、ボールが穴の縁ぎりぎりで止まるように見えたけど、徐々に傾いていって穴へと落ちる。"



hi "わあ、今のは難しいショットだったよ。あんなことやってのけるんだったら、あんまり勝てる望みはないなあ"

show hanako emb_emb_cas at center
with charaenter


ha "私……そ――そんなにうまくないよ……"


hi "でもショットだけじゃなくて、キューの位置を調節しているときもすごく真剣な顔してた。チェスでもそんな感じだよね"

show hanako emb_downsmile_cas
with charachange


"華子はほめられて少しおろおろする。キューをテーブルに立てかけ、俺の方を向いて立つ。"


ha "ただ……こういうことが好きなの……"


"華子はきつく指をからませ、そして丸めている。"

show hanako emb_downtimid_cas
with charachange


ha "孤児院にいたとき……私……昔す――好きだったこと……やり続けてたから"


ha "ほ――ほかの子とゲームしてたら、そ――それでヘルパーさんたちは満足だったから……"




"そんな風に考えたことは一度もなかった。孤児院の職員は子供たちがみんな、少なくともちょっとは仲良くなってほしいと思うのが当たり前なんじゃないか。"



hi "もし聞いてもいいなら……孤児院ではどんな感じだったの？"


show hanako emb_sad_cas
with charachange


ha "ど――どうして知りたいの？"


"華子を刺激してしまったけど、ちょっとでも応じてくれたってことは、質問に答えてくれる可能性が少しはあるってことだ。以前なら、たぶん何も言わずに逃げ腰になるだけだっただろう。"

show hanako emb_blushing_cas
with charachange


ha "お……教える、けど……"


hi "けど……？"

show hanako cover_worry_cas
with charachange


ha "い……い――いわ……な――なこさんのこと……教えてくれる？"

$ renpy.music.set_volume(0.2, 1.0, channel="music")



hi "岩魚子……？　ああ、あの手紙ね"




"そのことを聞くのにちょうどいいタイミングを、華子はどのくらい待っていたんだろうか。びっくりしたけど、ためらうことはしない。情報を共有するってのは、当然ギブアンドテイクってことだし。"



$ renpy.music.set_volume(1.0, 8.0, channel="music")
$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 8.0


hi "岩魚子は……昔好きだった人だよ"

show hanako basic_normal_cas
with charachange



"少なくとも俺にそのことを聞くあいだは、華子の緊張は静まっていた。好奇心が華子の緊張に勝ったようで、俺は他でもないこのことについて尋ねられてちょっと居心地が悪い。"




"岩魚子に対する気持ちを全部ここではき出すなんて到底できない。"
"先日優子さんと話をした後でも、自分が岩魚子にどんな気持ちを持っているのか俺自身分からないままだし、華子のまわりにいるときはこの話題を避けたい。"


show hanako def_worry_cas
with charachange



"ぎこちない感じで話が終わってしまったので、華子はじゅうぶん満足したという風には見えないけど、考え直してその話題を続けることはやめたらしい。"
"そもそも華子はなんとか俺にそのことを尋ねただけで、俺がその話をしたくないってことは知らなかったんだ。"



"俺はようやく自分のショットを打とうと動きだす。俺たちの間に会話はない。他の客の話し声や、逆の隅から聞こえてくるバンドの演奏が空間を満たす。"

hide hanako
with charaexit


"そこまで難しそうには見えないショットのために静かにテーブルを観察して、ボールめがけてショットを打つ。"

play sound sfx_billiards


"キューボールは狙ったボールをコツンと叩く。軌道はだいたい合ってるけど、力を入れすぎた。ボールは穴の端をかすめて脇へそれ、ポケットを避けるようにして転がる。"


"少し歯ぎしりする。このゲームで俺はかなりいい感じでプレイできていたから、これだけ調子を落としてしまうとイライラする。"



"後ろに下がって華子に順番を譲り、リリーと晃さんが座るカウンターの方を見やる。２人とも話に余念がないといった感じで、楽しい時間を過ごしているようだ。"


scene ev hanako_billiards_serious
with locationchange


"ショットを打つ華子の方に向き直る。さっきと同じ顔つきで、姿勢を正し、キューを鋭く突き出す。"

scene bg city_clubpool
with flash

play sound sfx_billiards


"さっきと同じように、狙ったボールがポケットに沈む。でも、今回のボールは前回よりも手際よくサイドポケットに落ちる。少しずつ華子の調子が上がってきているみたいだ。"


hi "お見事"


"すこしためらった後、華子はこちらに顔を向けることなく俺に話しかけ始める。"

scene ev hanako_billiards_smile_med
with locationchange


ha "孤児院……いいところだったよ。ちょっと山久みたいな感じ……職員さんもす――すごく優しかった"

show ev hanako_billiards_distant_med
with charachange



ha "でも、と――年がたつにつれて、気が付いたの。私だけ、ち――違うって"



"華子が自分のことをこれだけありのままに話すなんて、変な感じがする。俺に聞こえるように言葉を絞り出していて、華子が火事のことを話すって言い張ったときのことを思い出す。"


"俺が昔の話をしてくれるなら、自分もこういったことを俺に伝えなきゃいけない、華子はそう感じているに違いない。"


"華子は話をつづけ、キューを握る手に力がこもる。"

$ ksgallery_unlock("ev hanako_billiards_timid")
show ev hanako_billiards_timid_med
with charachange



ha "ほ――ほとんどの子は養子に行きたがってた、私もそう。でも私とは違って……みんなだんだんいなくなったの、ひ――ひとりずつ。山久に来るころまでには、私……いちばん年上の子たちの一人になってた"



ha "しばらくは、ち――小さい子たちをて――手伝ったりしてたけど、だ――だんだん……"

scene bg city_clubpool
with locationchange


"俺は華子の肩に手を置く。もう無理しすぎてる。"


hi "大丈夫"

show hanako emb_blushtimid_cas_close at center
with charaenter


"一瞬華子は少し驚いた顔をするけど、うなずいてキューをおろし、俺の方を向く。"

show hanako basic_worry_cas_close
with charachange


ha "ほ……本当にそう思う？"


hi "ああ、思うよ。リリーが居なくなるあいだだって、俺がそばにいて華子を守るから。だろ？"

show hanako basic_normal_cas_close
with charachange


"華子が長いあいだじっと俺をみつめるので、ちょっと不意を突かれる。"



"さっきから、やや感傷的な華子の表情は今も変わらないままだ。それに２人のあいだの沈黙も珍しいものじゃない。ちょっと変な感じがするのは、華子がこれだけ長い時間俺と視線を合わせているからだ。"




"まるで俺を評価しようとしているみたいだ。すごく変で、そしてかすかに落ち着かない感じがする。"



hi "華子……？"

show hanako cover_smile_cas_close
with charachange


ha "わ――わかった。ありがとう"


"華子は笑って少し視線をそらすけど、形式的なように感じる。華子は感情を偽るのがあんまりうまくないし、今のも例外じゃない。"


hide hanako
with charaexit



"俺はテーブルの方に進み、自分のショットを打って気分を変えようとするけど、うまくいきそうにない。俺には華子を助けるって任務をやりこなせない、そう思われてるんだろうか？　俺に失望したんだろうか？"



"たぶん考えすぎだろう。今となっては、華子が黙っていてもそれが普通だって受け入れているけど、時々もっとしゃべってくれたらいいのにと思う。"

play sound sfx_billiards


"鈍い音とともに俺が打った白いボールは、狙ったボールへ向かってテーブルを斜めに横切っていく。"

show hanako def_strain_cas at center
with charachange


ha "あ……"


"テーブルの上で起こっていることを、華子は俺と同じように眺めている。ボールが強くぶつかり、穴に沈めるつもりだったストライプボールは、進むべき方向とは違って８番ボールに向かっていく。"


"俺たちが唇をかんで見つめるなか、やっぱりボール同士が当たってしまい、黒いボールがゆっくりとコーナーポケットへと転がっていく。"

show hanako basic_smile_cas
with charachange


"俺にはため息をつくことしかできない。でも華子はまた微笑んでいるみたいだから、無駄なことじゃなかったかもしれない。"



hi "ひどいショットだった、華子の勝ちだよ。久しぶりだったから、かなり腕が鈍ったみたいだ"


hide hanako
with charaexit



"華子は腰を曲げて、残ったボールを１つずつ、一番近いポケットにキューで打って入れ始める。もう１ゲームするか聞くところだったけど、時計をさっと見ると、もうかなり遅い時間になってきている。"




"リリーと晃さんは今もまだカウンターで飲んでいるみたいだ。あの２人をあそこから引き離さないといけないらしい。"




ha "あの、久夫くん……"



scene ev hanako_billiards_distant
with locationchange


"華子の方に向きを戻すと、今もボールを打ちながら、ビリヤードテーブルの方を見ている。声がさっきと違った感じに聞こえる。"

scene ev hanako_billiards_smile
with charachange



ha "私も……久夫くんのためにここにいるから……"


stop ambient fadeout 2.0


hi "あ……"


"突然自分の顔が赤くなる。俺がさっきなんて言ったか考えれば、華子がこういう風に返事するのはごく自然なことなんだけど、実際に聞くとやっぱり衝撃を受ける。"

scene ev hanako_billiards_smile_close:
    xalign 0.0 yalign 0.0 zoom 0.8 subpixel True
    acdc_warp 20.0 zoom 1.0
with locationchange


"俺と華子との関係って、正確にはどんなものなんだろう？　華子を守りたいし、幸せにしたい……これが恋みたいなものなのかはあまり自信がないけど、リリーに対しても同じような感情を抱いているわけじゃない。"


"これまでの人生であんなにたくさんのことを耐え抜かなきゃいけなかった華子を気の毒に思う。家の火事で両親を亡くして、子供時代のほとんどを孤児院で過ごして……そんな人生、想像もできない。"


"でも俺が華子にできることはほとんどないように感じる。リリーが日本を離れる今となっては特に。"

stop music fadeout 10.0

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 4.0

scene bg city_karaokeext
show akira basic_boo_ni:
    center
    xpos 0.39
show lilly cane_smileclosed_cas_ni:
    center
    xpos 0.21
show hanako basic_normal_cas_close_ni at tworight
with locationskip


"華子と俺でテーブルとキューを片付け、店の出口へと向かう途中、リリーと晃さんを迎えに行く。"



"華子と俺の間で、何かが変わったような気がする。それが何なのかはっきりとはわからないけど、今の華子は前とはふるまい方が違う。俺たちの間の距離が、どちらかというともっと離れてしまったように思える。"


show akira basic_smile_ni
with charachange


aki "で、楽しめた？"

show hanako emb_smile_cas_close_ni
with charachange



"華子と俺は２人してうなずき、同意する。ゲームはよかったし、お互いのことをもっと知ることができたから、正直な返事だ。"


show lilly cane_sleepy_cas_ni
with charachange


"リリーがちょっと注意散漫になっているように見える。"


hi "旅行のことが心配かい、リリー？"


"リリーは少し動きを止め、ため息をついて弱々しく微笑む。"

show lilly cane_weaksmile_cas_ni
with charachange




li "少しだけ。家族の一大事ですから"



show akira basic_laugh_ni
show lilly cane_surprised_cas_ni
with vpunch



"その言葉を受けて、晃さんがリリーの肩を叩く。華子も微笑み返している。"


show hanako basic_smile_cas_close_ni
with charachange


ha "リリー、大丈夫だよ。あっちで過ごす時間を楽しめるといいね"

show lilly cane_smile_cas_ni
with charachange


li "ありがとう、華ちゃん。そうできるよう努力します。どれだけ短い時間でも、やっぱり家族のところに帰って一緒に過ごすというのはいいものでしょうし"



"それから、俺たち４人は晃さんの車が停めてある駐車場へと歩き出す。みんなで話を続けるけど、ほとんどがただの世間話だ。"



stop ambient fadeout 2.0
stop music fadeout 2.0

scene black
with dissolve
label jp_H20:

play music music_daily fadein 2.0

scene bg school_girlsdormhall
show lilly basic_smile_cas at twoleft
show hanako basic_normal_cas at tworight
with locationchange


hi "それじゃ、バスで行くの、リリー？"

show lilly basic_smileclosed_cas
with charachange


"リリーはそばにある大きなスーツケースを身振りで示す。"

show lilly basic_weaksmile_cas
with charachange


li "これを持って行かないといけませんから、タクシーを予約しました。あと５分ほどで、校門のところに迎えに来てくれるはずです"


hi "ああ、なるほど"

show lilly basic_sleepy_cas:
    ypos 1.1
with dissolvecharamove


"リリーは手を下に伸ばし、手探りでスーツケースの持ち手を探す。重くてやりにくそうだから、すぐに俺が持つよと申し出る。"

show lilly basic_smileclosed_cas at twoleft
with dissolvecharamove


li "とてもご親切にありがとう、久夫さん"



"リリーは手伝ってもらうことに抵抗がないようで、俺が持っていくことになる。軽いとは言えないけど、別に重いってほどでもない。運ぶのにそこまで苦労しないだろう。"

show lilly basic_weaksmile_cas
with charachange



li "では、お願いします。でも急がないといけません。もしこのタクシーに乗れないと、新しいのを予約するのにかなり長いことかかってしまうでしょうから。華ちゃん、準備できた？"


show hanako cover_worry_cas at tworight
with charachange


ha "う――うん。行こう"

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

scene bg school_gate at bgright
with locationskip


"できるだけ急いで校門まで向かうけど、タクシーはまだ着いてないらしい。"



hi "まあ、朝のちょっとした運動ほどいいものはないからね。ナースにもそういうことをするように言われたし"


show lilly basic_weaksmile_cas at center
with charaenter



li "多分ナースは別のことを指してそう言ったんだと思いますよ、久夫さん。おそらく、もっと定期的に行うようなことを。毎日他人の荷物運びを手伝うつもりですか？"




hi "いや、やらないだろうね。どっちにしろ、ちょっと待たないといけないみたいだ。もう一度タクシーを呼ぶとしたら、あとどのくらい待ってからがいいのかな？"

show lilly basic_smileclosed_cas
with charachange


li "おそらくあと１０分ほどでしょうね。ですが、これまで一度も予約をすっぽかされたことはありません。たぶんちょっと渋滞しているだけでしょう"


hi "そういうことなら"


hi "で、スコットランドまでの飛行時間はどのくらいなの？"

show lilly basic_smile_cas
with charachange


li "記憶が正しければ、だいたい１６時間です。時差があるので、少しわかりにくいんですが"

show bg school_gate at center
show lilly basic_smile_cas at twoleft
with charamove

show hanako defarms_worry_cas at tworight
with charaenter


ha "すごく長い……"


"今になって、華子がいつになく静かすぎることに気づく。うまくストレスに対処できなくて、ひどく緊張しているようだ。"


hi "ああ、そんなに長い間飛行機に乗ってるなんて想像できないよ"



"俺がこれまでに飛行機に乗ったのは、一家で短い休暇を北の方で過ごしたときだけだから、実際どういう感じか想像するのはとても難しい。"
"華子が子供時代のかなりの時間を孤児院で過ごしたんだとすれば、多分飛行機はおろかほとんど旅行したこともないだろう。"


show lilly basic_weaksmile_cas
with charachange



li "そんなに悪いものでもありませんよ。ほとんどの時間を寝るか、英語のスキルを取り戻すのに使ってますから。ここではほとんど英語を使わないので、少し慣れておく必要があるんです"


show hanako cover_worry_cas
with charachange


ha "な――なまりが……問題になるの？"



show lilly basic_smile_cas
with charachange


li "それはそんなに心配しなくていいでしょう。はじめのうちは問題になるかもしれませんが、いったん慣れてしまえば大丈夫なはずです"

show hanako basic_worry_cas at Position(ypos=1.14)
show lilly basic_smileclosed_cas at Position(ypos=1.17)
with dissolvecharamove



"３人で静かに、校門のそばにある小さなベンチまで移動して座る。"



"妙なことだけど、リリーが行ってしまうと分かっていても、かける言葉が何も思いつかない。リリーは頼もしい人だし、俺がいちばん思いを巡らせてる人じゃないからかもしれない。"

show hanako emb_downsad_cas
with charachange



"リリーは目にすることができないかもしれないけど、華子は神経質な様子で爪を噛んでいる。俺は華子に話しかけようとするけど、言葉をかけるよりも先に、懸命に丘を登ってくるエンジンの音が聞こえてくる。"




hi "あ、タクシーがこっちに来てるみたいだ……"


show lilly basic_cheerful_cas
with charachange



li "よく聞き分けましたね、久夫さん。私にも、ついさっき聞こえたばかりでした"



"ちょっと誇らしげな気持ちが押し寄せる。リリーと同時に気づいたってことは、自分の周りに以前よりも注意を払うようになってきてるってことだ。"


"ともかく、タクシー会社への電話も、リリーが電車に乗り遅れるかもっていう心配も、しなくてよさそうだ。"

show hanako basic_worry_cas at tworight
show lilly basic_smileclosed_cas at twoleft
with dissolvecharamove


"タクシーは俺たちの前で停まり、運転手が窓を下ろして身を乗り出してくる。ここにいるリリーがタクシーを予約した砂藤リリーだ、と確認が済んだので、俺たちでリリーの荷物だけを分けておく。"

hide lilly
with charaexit


"運転手はトランクを開け、リリーのスーツケースを手に取る。荷物が積み込まれ、トランクがバタンと閉められるあいだに、リリーは後部座席に乗り込む。"


"運転手は運転席に戻ってドアを閉め、俺たちが別れの挨拶を終えるのを待つ。"

show hanako emb_downtimid_cas
with charachange


ha "気をつけて、リリー"


hi "身体に気をつけてね"


"当然ながら華子は寂しそうだ。声を聞いただけでもそれだけははっきりと分かる。"


li "もちろんです。すぐに帰ってきますから、心配しないで。もう一人、これからも華ちゃんのためにいてくれる人がいるでしょう、ねえ、久夫さん？"


hi "ああ、その通りだよ"

show hanako emb_blushtimid_cas_close
with characlose



"俺は華子のほうを向き、その肩に手を置いて微笑む。"


show hanako emb_downtimid_cas_close
with charachange



"華子はずっと頬を染めたまま、俺と数秒のあいだしか視線を合わせられず、またリリーに向き直る。"



hi "またね、リリー"

show hanako basic_worry_cas_close
with charachange


ha "さよなら！"

stop music fadeout 6.0


"かなり名残惜しそうな様子で、リリーも俺たちに別れの挨拶をする。運転手はそれ以上待つことはせずに再びエンジンをかけ、タクシーは空港へ向かって丘を下りはじめる。"



"タクシーが視界から消えたあとも、どうすればいいのかよくわからないまま、俺たち２人で長いあいだ校門のところに立ち続ける。"


show bg school_gate at bgleft
show hanako basic_worry_cas_close at center
with charamove



hi "さて、どうしようか？"


show hanako def_worry_cas_close
with charachange


ha "わ……わからない"

label jp_choiceH20:
menu:
    with menueffect
    "街のほうに行ってみる？":



        return m1
    "今日はこれで解散にする？":


        return m2



label jp_H20_1:

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")



"無言の衛兵みたいに校門のそばに立っているバス停を見て、妙な考えが浮かぶ。"



hi "街に行って、本屋かなにか探してみる？　今日はこのあと暇だし"



"華子は街に出るのが好きじゃないから、これは大胆な賭けだ。"
"華子をあのジャズクラブまでなんとか連れ出せたことだって、外がかなり暗くなっていたとしても、ちょっとした奇跡だと思ってる。でも純粋に、華子ともっと一緒にいたいんだ。"




"とはいえ、華子は今にも拒否して帰り……"

show hanako basic_smile_cas_close
with charachange


ha "いいよ"


hi "ほんと？"

show hanako basic_bashful_cas_close
with charachange


ha "ほ――本当。行こう"


"華子がなんで俺に賛成することにしたのかはわからないけど、考え直してもらうよう頼む気なんてない。"

stop ambient fadeout 2.0

scene bg city_street2
show crowd
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 2.0


"バスを降りてすぐ、周りがたくさんの人でごった返していることに気づく。あとあと考えてみれば分かりきったことだった。土曜の午後となれば当然、多くの人が繁華街にやってくる。"

show hanako emb_downtimid_cas_close at center
with charaenter



"華子は周りの人から逃げるように俺のそばに近づき、手は俺の腕をきつくつかんでいる。体を俺に寄りかからせて、頭もかなり低くかがめているので、やけどの傷跡は帽子でほとんど隠れている。"



hi "で、えーと、どこに行こう？　本屋？"



"華子のプレゼントや、それ以外にも自分の生活費・雑費のおかげで、家計はかなり厳しくなってるけど、本を何冊か買うくらいの余裕はあるはずだ。どっちにしろ、貯金のためにお金を少し取っておいたしな。"



"一瞬俺の声が聞こえなかったんじゃないかと思ったけど、横に目をやると、華子がかすかにうなずいているのが辛うじて分かる。"

show hanako emb_smile_cas_close
with charachange


ha "う――うん。ど――どこか知ってる？"


hi "ああ。実は、リリーと俺で華子のプレゼントを探しにきたとき、いくつか本屋の前を通ったんだよ"

show hanako emb_downsad_cas_close
with charachange


"華子の表情がほんの少し曇る。これからは華子の誕生日の話を持ち出すのはやめるってこと、覚えておかないと。"

show hanako emb_timid_cas_close
with charachange



ha "２人で……長いあいだ一緒にいたの？"



"いや、そういうことじゃなかったみたいだ。"


hi "やっぱり、華子にぴったりのプレゼントを用意したかったしね"

show hanako emb_smile_cas_close
with charachange


"華子は少し笑みを浮かべ頬を赤らめる。そんな時間はちょっとした宝物みたいな感じだ。"


hi "とにかく、ちょうどここから先に行ったところに本屋があるはずだから、ちょっと見てみる？"

show hanako basic_bashful_cas_close
with charachange


ha "も――もちろん"

scene bg city_street1
show crowd
with locationchange


"歩道橋を通って本屋へと向かうにつれ、人混みが激しくなる。華子も片腕を俺の腕にからませ、歩みが少し遅くなる。"


"歩いているあいだ、車の音が聞こえ、それで華子の気を紛らわすことができるかもしれないと思いつく。"


hi "華子、ちょっと思ったんだけど……いつか車の運転を覚えようとか、そういうことって今までに考えたことはある？"

show hanako cover_worry_cas_close
with charachange


ha "う――運転？"


hi "ああ。ある意味、運がいいようなもんだよ。車の運転を許可される生徒なんて、山久にはそう多くはいないんだから"


"場違いな話題だけど、この状況から華子の気をそらしたい。華子は今、かなり緊張しているから。"


"だけど、多分そんなこと考えたこともなかったんだろう、俺の発言で華子は困っているだけだ。黙ってりゃよかった。"

stop ambient fadeout 0.5

scene bg city_street3 at left
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0


"少しして、リリーと俺がプレゼントを探してたときに通り過ぎた本屋のうちの、一軒の前にたどり着く。"



hi "土曜に閉まってるなんて、どんだけ自信のある本屋なんだよ？"


show hanako def_worry_cas_close at center
with charaenter



ha "本屋さんは……もうあんまり儲からないから。インターネットがあるし。週末は店を閉めないといけなくなっちゃったのかも？"




"華子はかなりテクノロジーに詳しいみたいだ。孤独に抵抗のない人にとっては、そういう知識の探求は向いてるんだろうな。"




hi "なるほど、確かにそうかもな……ネットで本を探す方が簡単だし。とにかく、この案はだめみたいだ。他になにかやりたいことはある？"


show hanako emb_smile_cas_close
with charachange


ha "も――もし……よかったら……プレゼントを買ってくれた場所、案内してくれない？"


hi "もちろん、かまわないよ。ここからそんなに遠くないし"

hide hanako
with charaexit

show bg city_street3 at right
with charamove_slow


"正確な場所はあんまり覚えてないけど、店がある方に向かって出発する。前回はあてもなく周辺を歩き回って半日を費やしたけど、その二の舞はごめんだ。"



hi "ここだ、オセロズ・アンティーク"



show hanako basic_normal_cas_close at center
with charaenter


ha "ち――小さいね"


hi "うん、まあね。リリーと俺も、見つけるのにちょっと時間がかかったんだ"

show hanako basic_distant_cas_close
with charachange


ha "入ってもいい？"


hi "もちろん。開いてるし"

stop ambient fadeout 0.5
play sound sfx_storebell
play music music_soothing fadein 0.5

scene bg city_othello
with locationchange


"華子はドアを押し開け、俺より先に店に入る。今回も、店主のほかに店には誰もいない。"

show shopkeep neutral at center
with charaenter


"俺を見て店主の顔が少し曇る。"



sk "ああ、返品しに来たわけではないだろうな？　ちょっと待った、その子はこないだ一緒に来た子とは違うな……"



hi "えーと、違います、返品のつもりで来たんじゃありません。街まで来たので、ここをもう一度見たいなと思っただけなんです"

show shopkeep thinking
with charachange


"店主は俺の発言を受け、かなり長いあいだ熟考する。高校生が定期的に自分の店に来るなんて、慣れてないんだろう。"

show shopkeep happy
with charachange



sk "ひょっとするとこの子が、お前さん達がプレゼントを買ったお友達かね？"



hi "そうです。彼女へのプレゼントでした"

show shopkeep happy at twoleft
show bg city_othello at bgleft
with charamove

show hanako defarms_strain_cas_close at tworight
with charaenter


"店主は華子のほうを向くけど、車のヘッドライトに照らされた鹿みたいにその場で固まる。"

show shopkeep surprised
with charachange


"店主は華子に話しかけようとする。でも少しあっけにとられて、言葉に詰まった様子だ。"

show shopkeep thinking
with charachange


"華子を凝視してしまっていることに気づいた店主は、視線を脇へそらし、俺たちに向かって遠回しに話しかける。顔つきや全身から、気詰まりで緊張した様子がうかがえる。"



"店主に腹を立てたかった。でも、華子を初めて見たとき、俺も何も考えず同じような反応をしてしまったってことは、よくよく分かっている。"
"俺も、華子を目の前にして、まずびっくりして、つぎに興味津々になり、そしてぎこちなく目をそらした。"


show hanako emb_downsad_cas_close
with charachange


"華子は前よりうろたえてはいないようだ……でも彼女の醸し出す雰囲気は、さっきより悪くなってる。怒りでも、いらだちでもない。どちらかというと、謝罪の気持ち。"

show shopkeep neutral
with charachange


sk "そこのお嬢さん、あんたは運がいいよ。できる限り気にかけようとしてくれる友達がいるんだからね"

show hanako emb_downtimid_cas_close
with charachange


ha "あ――ありがとう……"



"華子とこれだけたくさんの時間を一緒に過ごしてこなかったら、華子が何か言ったことさえ気づかなかっただろう。とは言え、俺たちの方を向かずに言っているせいもあって、店主のつぶやきもかなり聞こえにくい。"


hide hanako
with charaexit

show bg city_othello at left
show shopkeep invis:
    xpos 0.6 alpha 0.0
with dissolvecharamove


"華子は並べられた色んな品物を驚いた様子で見つめながら、店の中へと進む。人形が並べられている場所を見つけ、全ての人形を一体ずつつぶさに見ながら、長い時間を過ごしている。"


"これは最近になってようやく少しだけ知れた華子の一面だ。華子は人形が好きだってリリーから聞いたときはかなりびっくりしたし、鏡台の棚に置かれた『コレクション』を見てなおさら驚いた。"

show hanako basic_normal_cas_close at center
with charaenter


"注意が人形へとそれ、また店主から見えないところにいるため、華子の気分は少し良くなったようだ。でも俺は、さっきからの出来事にかなり戸惑ったままだ。"


"俺にも自分の病気っていう問題があるかもしれないけど、あんな風に他人から、まるで俺がまったく異質なものであるかのような反応をされたことは一度もなかった。"

show hanako basic_smile_cas_close
with charachange


ha "ここ、いいお店だね"


hi "ああ、思ってもみなかったよ。何か買いたいものはある？"

show hanako cover_worry_cas_close
with charachange


ha "お――お金持ってきてない"


hi "まあ、またいつでも来られるしね"


"今はもう、このお店への行き方も分かってるし。"

show hanako cover_bashful_cas_close
with charachange


ha "ま――また来られる？"


hi "もちろん。好きなだけ来たらいいよ"

show hanako basic_bashful_cas_close
with charachange


ha "あ――ありがとう"


hi "感謝する必要なんかないって。この店がどこにあるのかほとんど忘れかけてたし"



"２人とも自分たちの発言を完全には信じてないだろう。むしろ、言うべきだと思ってることをそのまま言っているだけだ。"


show hanako emb_smile_cas_close
with charachange


ha "も――もう学校に戻ってもいい？"


hi "もちろんさ。行こう"

stop music fadeout 5.0
play ambient sfx_traffic fadein 2.0

scene bg city_street3 at right
with locationchange


"バス停へ向かうため店を去るとき、店の裏手で店主がカーテンの隙間からこちらを覗いているのが見える。"


"華子への店主の視線が何を意味しているのか、よくはわからない。ちょっと変な感じがするし、華子がその視線に気づかなかったことに対して、安堵の気持ちと少しのいらつき、その両方を感じる。"

stop ambient fadeout 2.0

scene bg school_dormext_full
with shorttimeskip


"寮と寮のあいだの、コンクリートで固められた場所まで来ると、いったん華子と俺は足を止める。都心部から帰ってくるあいだ、俺たちはほとんど会話しなかった。"

show hanako basic_bashful_cas at center
with charaenter


ha "それじゃ、さよなら"


hi "紅茶か何か飲む？　チェスはどう？"

show hanako emb_emb_cas
with charachange


"華子は困った様子で頭を横に振る。"


ha "つ……疲れたの。またあとでもいい？　宿題があるし……"


"その声は、少し気分が沈みがちなように聞こえる。華子はあきらかにもっと遊びたがってるけど、ちょっと学業の遅れを取り戻さなきゃいけないんだろう。何日か授業に出られなかったし。"


hi "ああ、宿題ね。思い出させてくれてありがとう。俺もやらなきゃいけないことが山積みだ。また明日会おう"

show hanako basic_smile_cas
with charachange


ha "またね、久夫くん"


hide hanako
with charaexit


"俺がさよならを言う前に、華子は向きを変え、女子寮棟の入り口に向かって歩き始めていた。"


"さっき華子が通っていったドアを少しのあいだ見つめてから、その場を立ち去って自分の寮に向かう。"



"今日は疲れる一日だった。"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")



label jp_H20_2:

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")


hi "華子はどうかわからないけど、俺はちょっと昼寝しようかと思うんだ。頭が痛くて死にそう"

show hanako basic_distant_cas_close
with charachange


"華子が一瞬ほっとした様子を見せたことから、俺の予想は正しかったとしか思えない。華子は出歩きたがったりしないだろう。"

hide hanako
with charaexit


"黙ったまま、華子は校門を通って寮へと引き返す。"

scene bg school_dormext_full
with locationskip



"俺たちは寮までの道のりをずっと一緒に歩き、２人が別れなきゃいけない場所でぎこちなく止まる。"


show hanako cover_distant_cas at center
with charaenter


ha "それじゃ、さ――さよなら"


hi "あとで紅茶かなにか飲む？　チェスはどう？"

show hanako emb_timid_cas
with charachange


"華子は困った様子で頭を横に振る。"

show hanako emb_downtimid_cas
with charachange


ha "つ……疲れたの。また明日でもいい？　宿題があるし……"


"ちょっと学業の遅れを取り戻さなきゃいけないんだろう。結局何日か授業に出られなかったし。"


hi "ああ、宿題ね。思い出させてくれてありがとう。俺もやらなきゃいけないことが山積みだ。また明日会おう"

show hanako emb_downsmile_cas
with charachange


ha "またね、久夫くん"


hide hanako
with charaexit


"俺がさよならを言う前に、華子は向きを変え、女子寮棟の入り口に向かって歩き始めていた。"


"さっき華子が通っていったドアを少しのあいだ見つめてから、その場を立ち去って自分の寮に向かう。"


"明日はもっといい日になるさ。"

stop ambient fadeout 1.0
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
