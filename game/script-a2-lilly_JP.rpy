
label jp_L1:

window hide None

scene black
with dissolve

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show


"目覚まし時計がうっとうしく鳴り響き、俺は目を覚ます。時計の数字の鮮やかな赤い光が俺の顔を照らしている。"




play music music_dreamy fadein 2.0


"俺が家で使っていたのと同じものだ。山久学園に来る前の人生から引き継がれた数少ない遺物の一つ。これがあれば新しい人生への移行のショックが和らぐだろう、と思っていた。"






"でも、ちっとも役に立ちゃしない。"





"ベッドからのそのそと起き出し眠い目をこすると、俺は机に近寄る。そこに散らばっている薬瓶を開け、水なしで薬をいくつか飲み込む。"



"今ではこの習慣も体が覚え始めている。その目的を考えれば、これは喜ぶべきことなんだろう。"

$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene bg school_dormbathroom
with locationskip


"かなり目も覚めてきて、俺はバスルームに身を滑り込ませる。"

play ambient sfx_shower fadein 8.0

show steam
with charaenter


"新しい日課がまた始まろうとしている。シャワーの温度が上がっていくあいだ、俺は思いを巡らせる。"



"俺の心の中を占めているのは、鮮やかな色彩の花火と、それを一緒に眺め続けた２人の少女。ほとんど知らない人間のためにこんなにも心動かされるなんて、なんだか変な気分だ。"



"とはいえ、今の状況だって普通じゃないと思う。まあ、少なくとも話し相手はできた……隣の部屋のやつは置いとくとして。"





stop ambient fadeout 2.0

hide steam
with charaexit



"始業時間がだんだん近づいてきて、俺は登校のための準備を整える。"



$ renpy.music.set_volume(1.0, 3.0, channel="music")

scene bg school_scienceroom
with shorttimeskip



"教室の入り口をくぐり、まだ少し早い時間であることに気づく。５、６人の生徒がクラス内をうろついているけど、そのほとんどはまだ寝ているかのようだ。"









"こんな時には自分が朝型人間であることをありがたく思う。まあ、あそこの２人もいつもどおり意気揚々に見えるけど。"





hi "やあ、静音、ミーシャ"


show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charaenter


"静音には俺の挨拶は伝わらないであろうことに突然気づいて、急いで手を振ってフォローする。でも静音はあまり気にしていないようだ。"





"というか、関心もなさそうだ。"




show shizu basic_normal
with charachange


shi "……"

show misha hips_grin
with charachange


mi "ひっちゃ～ん、おはよ！　調子どう？"






"この挨拶はたぶん静音からのものだろう、と想像するしかない。時々ミーシャと静音、どっちの言葉なのかよく分からなくなることがある。"



hi "他の連中よりは元気だと思うけど。２人ともなんだかえらく元気そうだな"



show misha sign_smile
with charachange

show misha perky_smile
show shizu basic_frown
with charachange


"俺がそう言うあいだ、ミーシャは手話で静音にそれを伝える。それに対する静音の返事が手厳しいものであろうことは、彼女の鋭く速い腕の動きで明らかだ。"








"学園祭の準備で大きな働きをしてきた２人を前にして、たぶん俺はもっと言葉を選ぶべきだったんだ。"



show shizu behind_frown
with charachange


shi "……！"

show misha hips_grin
with charachange


mi "新しい生徒だからあんまり仕事しないのも勘弁してあげてたけど、これからもそういうサボり行為が許されるとは思わないでくださいね"








"ミーシャも自分の言い分を付け加えたかったらしいけど、絶え間なく続く静音の手話を見てすぐに翻訳作業に戻る。"

show shizu basic_frown
show misha sign_smile
with charachange


mi "３－２の屋台作りに貢献したってのは感心だけどぉ――"



"へえ。噂が伝わるのは早いもんだな。さもなきゃ、この２人は学校で起こるあらゆる出来事を把握しているんだろう。"


show misha hips_frown
with charachange


mi "――そういう労力は自分がやるべき所に集中して使ってほしいわね。つまり、自分のクラス、ってことね"


"認めたくはないけど、正論だ。俺がそれに対して口を開こうとすると、静音が他になにかを付け加える。それを見てミーシャが微笑む。"


show shizu behind_blank
with charachange


shi "……"

show misha perky_smile
with charachange


mi "それでぇ～、学園祭楽しかった？"


"説教は終わり、みたいだな。"





hi "ああ、楽しかったよ。そっちは？"


show shizu behind_smile
show misha hips_grin
with charachange


"ミーシャがにっと笑いながら大きく首を上下に振り、静音も軽くうなずく。この２人のしぐさは対照的で面白い。"


"その時、ぱらぱらと教室に入ってくる生徒たちの姿が視界の隅に映る。時計に目をやると、数分の遅刻だ。"

show hanako emb_downtimid at offscreenright
with None

show misha hips_grin at left
show shizu behind_smile at Transform(xpos=0.48)
show hanako emb_downsmile at Transform(xpos=1.0, xanchor=0.7)
show bg school_scienceroom at bgleft
with charamove


"華子の席に目を向けると、彼女はすでにそこに座り、満足げに読書にいそしんでいる。今まで気づかなかったけど、いつからいたんだろう。"

show misha hips_grin:
    ease 1.0 xpos 0.2
show shizu behind_smile:
    ease 1.0 tworight
show hanako emb_downsmile:
    ease 1.0 offscreenright
show bg school_scienceroom:
    ease 1.0 center
with None

hide misha
hide shizu
hide hanako
with Dissolve(1.0)


"廊下のほうから重苦しい足音がする。武藤先生が来たのを知って、俺は雑談を切り上げミーシャの隣の席に座る。"



"ドアが開き、先生が重い足取りで教室に入ってくる。いつもより姿勢が悪く、目はほとんど開いていない。この前リリーと華子にここのスタッフの皮肉を言ったけど、どうやらあれは間違っていたらしい。"




play ambient sfx_paperruffling


"先生が教卓まで来ると、クラスの皆がいっせいに教科書を開く。新しい週の一時間目の始まりだ。"

stop music fadeout 3.0
stop ambient fadeout 0.5

with shorttimeskip

play sound sfx_normalbell

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0


"昼休みを告げるチャイムが鳴り、俺はつかの間の休息にほっとしながら目をこする。"


show lilly basic_smileclosed at offscreenleft
with None

show bg school_scienceroom at bgright
show lilly cane_smileclosed at Transform(xanchor=0.2)
with charamove


"思ったとおり、リリーが手に杖を持ち、教室の入り口のそばでじっと華子を待っている。"



"昨日も一緒に過ごすことをオーケーしてくれたことだし、昼食も１人で取るより彼女たちと一緒に取ることにする。"




show hanako emb_smile at Alphain(0.5), Slide(0.5,0.5,0.4,0.5,0.5)
with Pause(0.5)

hide hanako
hide lilly
with charaexit



"華子が驚くべき速さでリリーの元に駆け寄り、俺が呼び止める前に廊下に出て行ってしまう。"



stop ambient fadeout 1.0

scene bg school_hallway3
show lilly back_listen at twoleft
show lillyprop back_cane at twoleft
show hanako emb_downsmile at tworight
with locationchange

show hanako def_shock
with vpunch


"背後の足音に気づき、リリーがほんの少し振り返る。華子がつられて振り返り、俺を見て飛び上がるほど驚く。"


show hanako defarms_strain
with charachange


ha "ひ……久夫くん？"



$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play music music_normal fadein 2.0

show hanako emb_blushtimid
with charachange


ha "あ、その……えっと……こんにちは、久夫くん……"






hi "やあ。驚かせてごめんな"

show lilly cane_smile
hide lillyprop
with charachange


"正しい方向を向くように華子に助けられながら、リリーが振り返って挨拶する。"



show lilly cane_smileclosed
with charachange


li "ごきげんよう、久夫さん。一緒にいかがですか？"





hi "うん、もしよければ。他にすることもなくてさ"




show lilly cane_smile
with charachange


"迷惑なことなんて少しもないとでも言いたげに、リリーが軽くうなずく。"




scene bg school_staircase2
with locationchange

with Pause(0.3)

scene bg school_hallway2
with locationchange



"階を一つ降り、いつもの部屋へと廊下を進む。華子の助けのおかげでリリーも杖や手すりを使うより速く歩ける。そうして俺たちは普段よりも早く部屋にたどり着く。"



scene bg school_miyagi
with locationchange



"予想通り、部屋は無人だった。外から日の光が差し込み、部活動に励む声が遠くのほうからかすかに聞こえてくる。"



"周りを見渡し、空のイーゼルがいくつか壁に立てかけてあるのに気づく。前に来た時はなかったはずだ。美術部も備品置き場としてここを使っているんだろう。"




show hanako emb_smile
with charaenter


ha "チェス盤用意したほうがいいかな？"






"リリーに直接言葉を向ける時の華子の声は普段よりも柔らかく感じる。"


show hanako emb_smile at tworight
show bg school_miyagi at bgright
with charamove

show lilly cane_weaksmile at twoleft
with charaenter



li "ええ。そのあいだに私は紅茶を淹れますね"






hi "あ、よかったら俺がやるよ"

show lilly cane_surprised
with charachange

with Pause(0.3)

show lilly cane_planned
with charachange


"彼女は少しのあいだ考えてから、にっこり微笑む。それを見て俺は申し出たのは正解だったと悟る。彼女の表情はとても読み取りやすい。"


show lilly cane_satisfied
with charachange


li "そうですか。ありがとうございます"




show lilly cane_satisfied:
    ease 0.5 ypos 1.3
    "lilly basic_cheerful" with Dissolve(0.5, alpha=True)
    ease 0.5 ypos 1.0
with Pause(1.0)

hide lilly
hide hanako
with charaexit



"そう言うと彼女は縮めた杖を自分のかばんの取っ手に滑りこませ、それを机の脚に立てかける。そして華子の向かいの席に座る。"








"木製のチェスの駒が盤上に並べられる音を聞きながら、３人分の紅茶を用意する。ああいう境遇で、リリーはどれくらいチェスが上手いんだろう、と考える。"







"俺が湯気の立ち上るティーカップを机に並べるころには、リリーと華子はそれぞれのかばんから出したサンドイッチとおにぎりをほお張りながら、両者とも最初の駒を進めていた。"

$ renpy.music.set_volume(0.5, 2.0, channel="music")

show chessboard:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"彼女たちが使うチェス盤のそれぞれのマスの中央には穴が開いていて、駒の下部にはそこにはめ込むでっぱりがある。さらに、黒いマスは少し浮かび上がっている。"







"リリーがチェス盤の上に手を滑らせ、駒の位置を確認する。チェス盤のシンプルかつ巧妙なデザインに少し感心する。これは目の見えない人のために特別に作られたものに違いない。"







$ renpy.music.set_volume(1.0, 5.0, channel="music")

show chessboard:
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide chessboard
with None


hi "ほら、紅茶入ったよ"

scene bg tearoom_everyone_noon
show tearoom_hanae happy
show tearoom_lillye smileclosed
show tearoom_hisaoe hsmile
show tearoom_chess
with locationskip


"チェス盤の華子側の脇にカップを置くと、華子が小さくうなずく。リリーの手が横に少しそれたので、その指先にそっとカップを触れさせる。リリーには感謝してもらえたようだ。"





show tearoom_hisaoe outside
with charachange


"ようやく席に座り、２人がプレイする脇で紅茶を静かに一口飲む。彼女たちが見せるプレイ中の姿は対照的で、見ていて面白い。"


show tearoom_hanae open
with charachange


"華子は盤上に顔を近づけ、それをじっと見据えながら意識を集中している。一方リリーは姿勢を崩さず、穏やかな外見を保っている。"



"プレイが続行するなか、リリーが俺と華子に穏やかに話しかける。"

show tearoom_lillye smile
with charachange


li "学園祭も終わりましたけど、クラスはどうでしたか？"




show tearoom_hanae shy
show tearoom_hisaoe hthink
with charachange


"華子が先に答えるかどうかを探るために俺が横を見ると、華子も俺と同じことをしている。"

show tearoom_hisaoe sigh
with charachange


hi "良くは……なかったね。クラスの半分は居眠りしてたみたいだし。先生までそんな感じ。おまけにテストもあったしさ"



show tearoom_hanae happy
with charachange


"華子が小さな声でそれに同意する。"




show tearoom_lillye ara
with charachange


li "それは大変でしたね。久夫さんは転校生なのだし"









show tearoom_hisaoe lsmile
with charachange


hi "まあ、なんとかなったけどな。こんなに早くテストを受けるとは思わなかったけど、科学はたぶん俺の一番得意な教科だし"





show tearoom_hisaoe hsmile
with charachange


hi "華子はどうだった？"

show tearoom_hanae open
with charachange


ha "私？　あの……まあまあ……かな……"






"華子は嘘がつけない性格だということがよく分かる。"

show tearoom_lillye thinking
with charachange



"リリーの笑みがほんの少しだけ消える。その反応を見るに、華子は予習なしでもいい成績が取れるほど学業優秀というわけではないらしい。"


show tearoom_hisaoe lsmile
with charachange


hi "リリーのクラスはどうだったんだ？"

show tearoom_lillye giggle
with charachange


li "驚くくらい上出来でしたよ。先生の期待を上回って、欠席者はたったの１人でしたから"




show tearoom_hanae shy
show tearoom_lillye smileclosed
with charachange


"これ以上話すこともなくなり、２人はまたゲームに集中する。"

show tearoom_hisaoe relief
with charachange


"チェスが観戦スポーツだと思ったことはないけど、今回に限って言えば、こんなユニークな状況のゲーム展開には俺も思わず見入ってしまう。"


show tearoom_hisaoe outside
show tearoom_hanae sad
with shorttimeskip



"時間が経過し、両者とも優れたチェス技術を披露する。ポーンを華子よりも二つ多く取ったリリーのほうが優勢だけど、その差はほんのわずかだ。"





show tearoom_hanae open
show tearoom_hisaoe hunsure
with charachange


"……華子が彼女のクイーンをおかしな場所に指すまでは。そのミスをとらえて、リリーがナイトで華子のクイーンを取る。"




show tearoom_hanae shy
with charachange


"すると華子はためらうことなくポーンで盤の反対側にいたリリーのルークを取り、そのポーンをクイーンに昇格させる。"




show tearoom_lillye thinking
show tearoom_hisaoe lunsure
with charachange


"指で盤上の駒をなぞったリリーが、華子の罠にはまったことに気づいてたじろいだ表情を見せる。仕方ないこととはいえ、駒を動かすたびに指で確認しないといけないのはちょっと煩わしいな。"





"こうしている間もなんの反応も示さない華子は、こういうプレイ方法に慣れているに違いない。彼女とリリーはこれ以前にも少なくとも数回はチェスの対戦をしたことがあるはずだ。"




ha "チェック"

show tearoom_hisaoe hsmile
with charachange


hi "すごいじゃないか。いいぞ、華子"

show tearoom_hanae happy
with charachange


"褒められた彼女は驚いたようにかあっと顔を赤らめる。"


ha "あ、ありがとう。うまくいくと……思わなかった"







show tearoom_hisaoe lsmile
with charachange



"リリーを見ると、ちょうど残った駒を確認し終わったようだ。自分のキングを救い出す方法を探っていたけど。"



li "チェックメイトのようですね……"




show tearoom_hisaoe loops
with charachange


hi "えっ？"

show tearoom_hisaoe relief
with charachange


"俺はもう一度盤上を確かめる。"





"その言葉通り、リリーのキングはどこにも逃げ道がない。２人のうちどちらが強いか、というさっきからの俺の疑問にもこれで答えが出た。"


show tearoom_hisaoe sigh
with charachange


hi "そうみたいだな"

show tearoom_lillye weaksmile
with charachange


"リリーが小さくため息をつき、華子が微笑む。２人の反応を見る限り、いつもどおりといった感じだ。"




show tearoom_hisaoe lsmile
with charachange


hi "２人はどれくらいチェスをやってたんだ？"

show tearoom_hisaoe hsmile
show tearoom_hanae sad

with charachange


ha "小さい……ころから"

show tearoom_lillye smileclosed
show tearoom_hisaoe lsmile
with charachange


"華子の短い返答を聞いてリリーがうなずく。"

show tearoom_lillye smile
with charachange



li "出会ってすぐ、華ちゃんが私にチェスを教えてくれたんです。時には私が勝つこともあるけれど……めったにないですね。まだ上手な駒の動かし方を知らないのかもしれません"











"リリーが山久学園に入学し、その後寮に移って華子に出会ったと考えると、つまり彼女のチェス歴は一年ぽっちということか。"



"華子のハイレベルなプレイを見た後では、リリーがなかなか彼女を倒せないのもうなずける。"

show tearoom_hanae happy
show tearoom_hisaoe hthink
with charachange


ha "でも……リリーは私よりも話すのが上手だから……"




show tearoom_lillye ara
show tearoom_hisaoe lthink
with charachange


"華子が素早く褒め言葉を返すのを聞いて、リリーが少し面白がるように感謝の笑みを浮かべる。"






show tearoom_lillye weaksmile
with charachange


li "そう、そういうものかしらね"

stop music fadeout 3.0
play sound sfx_warningbell


"突然昼休みの終わりを告げるチャイムが鳴り、俺たちは皆びっくりする。"

show tearoom_lillye thinking
show tearoom_hisaoe loops
with charachange



li "あら、思っていたよりも勝負が長くなってしまったようですね"







hi "同感だ。教室に戻ったほうがいいな"

show tearoom_hanae shy
show tearoom_lillye weaksmile
show tearoom_hisaoe thinkclosed
with charachange


"華子はすでに片づけ始めている。俺はリリーのかばんを取り彼女に渡す。彼女はうなずきながらかばんを手に取った後、なぜかテーブルの上にそれを置いてしまう。"


play music music_daily fadein 2.0

scene bg school_miyagi
show lilly basic_smileclosed at twoleft
show hanako basic_normal at tworight
with locationskip


li "久夫さん。一つお願いしてもいいですか？"





hi "ん、ああ、いいよ"

show lilly basic_smile at twoleft
with charachange


li "あなたの顔を触らせてもらってもいいですか？"





hi "えっ、ええと……いや、構わないよ。俺は別に"


"俺にとっては完全に不意を突かれた頼みだったけど、冷静に考えてみれば別におかしな頼みでもない。リリーは未だに俺の外見を全く知らない。そして、触ることがそれを知る唯一の方法なんだろう。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show ev lilly_touch_uni
with GenericWhiteout(0.5,0.1,3.0)


"リリーがそっと右手を上げる。俺はそれを手に取ると、自分の顔へと導く。"



"あごから頬へ、そして他の全ての部分へ。リリーの手が俺の顔をなぞるあいだ、部屋は静寂に包まれる。"


"顔を触られるのはもっと煩わしいものだと思っていた。きっとこれも誰かの顔を見るのと同じ、ただ実用のための行為なんだろう。"


"彼女の手は柔らかく、指は驚くほど長くすらりとしている。その動きは、例えそれがほんのわずかであってもいつも的確だ。彼女の触覚は俺のそれよりもはるかに敏感に違いない。"




"最後に彼女は一度だけ俺の髪を軽く撫で、それから手を引く。これで俺の顔の全てが、細かい部分まで彼女の記憶に刻まれたはずだ。この時初めて、俺は華子が一部始終を静かに見守っていたことに気づく。"



$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg school_miyagi
show hanako basic_distant at tworight
show lilly basic_weaksmile_close at twoleft
with whiteout


li "ありがとう、久夫さん"




show lilly basic_smile_close at twoleft
with charachange


li "もう一言付け加えると、久夫さん、とてもハンサムだと思います"





"彼女の言葉を聞いて俺は少し赤くなり、疑念に眉を寄せる。"


hi "でも、見えないのに、どうやって……"

show lilly basic_pout_close at twoleft
with charachange


li "あら、見えないからといって、私に好みがないというわけではないんですよ"





show hanako emb_timid at tworight
with charachange


ha "あの、そろそろ戻ったほうが……"


hi "ああ、そうだな。じゃあリリー、また今度な"



scene bg school_hallway2
show lilly basic_smile at twoleft
show hanako emb_smile at tworight
with locationskip



"廊下を歩いているあいだ、俺は華子がさっきよりも静かに、そしてリラックスしているように見える。"



"華子の肩に手を乗せているリリーも華子の力強いペースからそれを感じ取ったようで、歩きながら微笑んでいる。"



"もし山久での日々がこんな毎日なら、それも悪くないな。なんといっても、ほんの少しの幸せのやりとりこそが人生の喜びには必要なんだ。"


scene bg school_scienceroom
with locationskip

play sound sfx_rumble


"自分の席に着いてかばんを脇にかけた時、俺はあることに気づく。いや、俺の胃袋が、だ。"



"あの２人のことばかりに気を取られて、自分の昼飯を買い忘れていた……"





stop music fadeout 2.0

scene black
with dissolve




label jp_L2:

scene bg school_dormhisao
with locationchange


"土曜日。俺が一週間で二番目に好きな曜日。"


"二番目に授業時間が短い曜日、学校が半日で終わる曜日だから、というのがその理由だ。"


scene bg school_dormhallway
with locationchange


"外の素晴らしい天気と授業時間の短さをめいっぱい楽しめるだろうという自信に満たされながら、俺は自分の部屋のドアを開ける。"

scene bg school_dormhallground
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_footsteps_hard


"そのまま自信に満ちた足取りで廊下を進み、階段を降り、男子寮のロビーまでやって来る。"

$ renpy.music.set_volume(0.6, 4.0, channel="ambient")


"そして自信に満ちたまま後ろを振り返る。後ろから近づく足音の主を確認するために。"

$ renpy.music.set_volume(1.0, 4.0, channel="ambient")


"そして……俺は楽しい一日を過ごす自信を失う。"

stop ambient
play music music_kenji fadein 0.5

show kenji happy:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter


ke "よう、調子どうだ？"


hi "別に、って感じ。午後が楽しみだよ。お前は？"

show kenji happy_close at center
with characlose


"健二が俺の沈んだ肩に馴れ馴れしく手を回す。なんだか様子がおかしい。"




show kenji neutral_close
with charachange


ke "よし、出るか。な？"


hi "とっくに出てたんだよ、お前に引き止められてなければ"




show kenji tsun_close
with charachange

scene bg school_dormext_full
with locationchange



"芝居じみた台詞に対する俺の反応も、健二は全く意に介さない。俺は健二を無視して、寮の外に出て階段を降り始める。"



"すぐに健二が俺に追いつく。金の相談か、それともまた新しい陰謀論を垂れ流すのか。いや、両方かもしれない。"

show kenji tsun:
    center
    xpos 0.6
    easein 0.5 xpos 0.5
with charaenter


ke "お前にちょっと言っときたいことがある"


hi "あっそ"


ke "あの金髪女のことだよ。誰のことか、分かるな？"


"今回は陰謀論か。健二を無視するふりをしたほうがいいかと少し考えたけど、たぶんこいつの言い分を全て吐き出させたほうが早く終わるだろう。"


hi "リリーか？　お前のクラスの？"

show kenji rage at center
with vpunch


ke "お前、下の名前で呼んでんのか！？"






"健二はこの展開に明らかにショックを受けているようだ。俺が答えられるのを期待してたんじゃなかったのか？"





show kenji tsun
with charachange


"健二は気を取り直すと、こぶしを作って咳ばらいをする。芝居がかってるのもいつもどおりだ。"


ke "ふん、まあいい。忠告しといてやる。ほら、男同士の忠告ってやつだ"


hi "何の忠告だよ？　リリーのことか？"


ke "ああ。お前はあいつを知らないんだよ"


"それについてはだいたい正しい。俺がリリーと華子に会ってまだ二週間足らずだ。そのあいだも俺たちはただ昼休みに学校でのつまらない出来事について雑談していたに過ぎない。"


hi "お前だってそうだと思うぞ"



ke "そんなことは問題じゃない。あいつと不自然なくらい長い時間つるんでるのはそっちの方だろうが"






"健二みたいな他人と会話なんてこれっぽっちもしなさそうな奴が、俺が誰と仲良くなるかなんてどうでもいいことを知っている。それを聞いて、俺はげんなりする。"





"でも、待てよ……俺は転入生で、リリーはただ学級委員ってだけじゃなく、背の高い金髪少女だ。"










"こいつの戯言も、学校内で噂が広まっていて、しかも俺がその渦のど真ん中にいるという警告としてありがたく受け取るべきなのかもしれない。"





hi "一緒に昼飯食ってるだけだよ。特別なことじゃない"

show kenji neutral
with charachange


ke "まああれだ、やっちまったもんはしかたない。諜報活動のためなら、ヤバい橋もわたらなきゃいけない。それが男ってもんだ"







show kenji tsun
with charachange



ke "ただし、あまり深入りしすぎないよう気をつけるんだぞ"



hi "健二さ、さっぱり分かんないんだけど"

show kenji happy
with charachange


ke "いいさ、他の連中もたいてい分かってない。だから俺が助けてやるんだよ"




scene bg school_gardens
show kenji neutral
with locationskip


ke "あいつには注意しろ、いいな？　あいつ、一見無害に見えるけど、俺、聞いちまったんだよ。とんでもねえ話をよ"

show kenji tsun
with charachange


ke "生徒会のことは知ってるな？"


"その言葉を口にすると、健二は思わずぶるっと身を震わせる。こいつと静音を同じ部屋に閉じこめた様子を想像するのは、愉快な頭の体操だ。２人は会ったことあるんだろうか。"





hi "ああ、静音とミーシャは同じクラスだからな。俺はなんとか生徒会には入れられずに済んだけど"





show kenji happy
with charachange


ke "よしよし、それでいい"

show kenji tsun
with charachange


ke "だが、あの金髪女はどうだ？　あいつもいたんだよ。あの生徒会によ。ど・ま・ん・な・か・に、だ"




hi "へえ。で？"


ke "今はいない"

stop music fadeout 3.0


hi "……"


ke "マジ、考えてみろって。絶対なんかあったはずだろ"



"俺はしばらく立ち止まり、必要以上に想像を膨らませてしまう。"



"この前の２人のいがみ合いもそれで説明がつく。少なくとも部分的には。待て、いや、そうとも言い切れない。生徒会を去ったこと自体にも何か原因があるはずだ。"



"結局のところ、これだけでは２人の確執が過去にさかのぼるということ以外何も分からない。"


hi "そうかもな。でも、それが俺にどう影響するんだよ"

show kenji neutral
with charachange


ke "よし、じゃあよく聞けよ。リリーはどう見ても日本人じゃない"






hi "そうだな"


ke "なら、あいつの国籍はどこだ？"


"その質問に答えるために口を開こうとして、俺は答えを知らないのに気づく。実際、それについてほとんど考えたことがなかった。"


"全く訛りのない言葉遣いと完璧な日本人の振る舞いを披露するリリーに接していると、そんなことは大して重要じゃないように思える。だけど、今こうして健二に言われてみると少し気になってしまう。"


hi "正直、知らないな。イギリス人か？　イギリス人って紅茶好きだし"






"ステレオタイプな考え方に頼るべきじゃないんだろうとは思うけど、それくらいしか手がかりがない。"




show kenji happy
with charachange

play music music_kenji fadein 1.0


ke "お前、何にも考えてねえな。代わりに考えてやる俺がいてラッキーだぞ"


hi "はぁ、そりゃどうも"


"健二が俺の皮肉をあっさり無視する。"

show kenji neutral
with charachange


ke "よし、じゃあ答えてみろ。莫大な権力を持ってて、薄ぎたねえ金持ちで――金髪ってのはみんな金持ちなのは知ってるな？――長い抗争の歴史を持ってて、でっかい組織に属してたのはどいつだ？"





hi "ローマカトリック教会か？"

show kenji tsun
with charachange


ke "……あー、まあ、それもそうだ"

show kenji neutral
with charachange


ke "だが、マフィアもそうだ。おいおい、金持ち、外人ときたら、あの金髪女がつながってないわけないだろうが"


"健二の推測に使われる論理は疑わしいことこの上ないけど、やつが話をやめる気配はない。"




scene bg school_hallway3
show kenji neutral
with locationskip


ke "で、あいつがどっから来たと俺が考えてるか、分かるな？"


hi "イタリア？"

show kenji tsun
with charachange


ke "イタリア本土なんかザコだよ。シチリア島に決まってる。マフィア連中はみんなあそこ出身だからな"





show kenji happy
with charachange


ke "いや待て、違うな、ロシアだ。くそっ、最悪だ。あそこのマフィアはマジもんだぜ。元KGBだらけだろ、私兵に、筋金入った密輸に、それから何だ？"




hi "待て待て、ストップ、ちょっと落ち着けって。お前、結局何が言いたいんだよ？"


show kenji neutral
with charachange


ke "あいつが何するか分かんねえってことだよ。お前の邪魔はしねえよ――そんなのはエージェントのやり方じゃない――ただ、気を付けろってこった"




show kenji tsun
with charachange


ke "いずれ時が来たら、俺たちはあらゆる手助けが必要になるんだ。お前を失いたくはないんだよ、同志"




"まあ、少なくともこいつは俺の身を案じてくれているんだろう。それなりに。"

stop music fadeout 4.0

show kenji tsun:
    center
    easeout 0.5 xpos 0.6 alpha 0.0
with None


"別れてそれぞれの教室に入っていく時に、俺は健二に向かって手を振る。奴にそれが見えるのかどうか分からないけど。"




scene bg school_scienceroom
with shorttimeskip

play ambient sfx_crowd_indoors fadein 2.0


"本をかばんの中に詰め込みながら、先週図書室で借りた数冊の本にちらりと目をやる。全部読むのにまる二日かかったこの本、返しに行った方がいいな。"






"華子も誘おうかと少し考えるけど、もう教室にいない。まあ、一人の方が勉強もはかどるだろう。"





"クラスメイト数人と手を振り合ってお互いに別れを告げた後、俺は教室を出る。"

stop ambient fadeout 1.0

scene bg school_library
with locationskip


"かばんを開けカウンターの返却口に本を突っ込む時、俺は向こう側にいる奇妙な人物に気づく。高齢で白髪の女性だ。優子さんが喫茶店で働いているあいだの代理だろう。"




"空いた机を探し始めるけど、見つけるのは難しそうだ。それほど生徒がいるわけじゃないにしても、彼らはみんな各自の机を確保してしまっている。"


"その時、見慣れた髪を持つ人物に気づき、俺は点字本コーナー近くの机に歩み寄る。"

show lilly basic_smileclosed
with charaenter


"リリーは落ち着き払った様子のまま、点がいっぱいのページの上に指を滑らせている。彼女が読書に集中しているのかどうか、俺にはよく分からない。"








hi "やあ、ここ、座っていいかな？"

show lilly basic_surprised
with charachange


li "えっ？　ああ、もちろんですよ……"





"手元の本に意識が集中したままのようで、リリーの言葉はだんだん尻すぼみになる。"


play music music_lilly fadein 10.0

show lilly basic_smile
with charachange


li "あら、久夫さん"

show lilly basic_smileclosed
with charachange


"俺が反対側の席に座るあいだ、リリーが会釈する。俺は化学の教科書をかばんから引き出すとそれを素早くめくり、今授業で習っている部分を開く。"


"しばらくのあいだ、俺たちは座った場所でそれぞれのやり方で読書にいそしむ。"


"だけど、リリーを見て今朝の健二の言葉が脳裏をよぎる。そのことと、点字を読む人を見たことがないという事実のせいで、俺は彼女をちらちら見ずにはいられない。"


"リリーはそれに気づく術がない。そのことに罪悪感を感じた俺は、彼女に直接質問を投げかけることにする。実際、血筋のことは別に機密事項というわけでもない。それに、彼女の動きを見ていて気づいたこともある。"







hi "あのさ、リリー。ちょっと聞いてもいいかな？"





show lilly basic_smile
with charachange


li "ええ、いいですよ。どうかしましたか？"




hi "リリーって……少なくともハーフとかクォーターなのかなあ、って。違う？"




show lilly basic_giggle
with charachange


"彼女はくすりと笑うと、本を机に置く。"

show lilly basic_cheerful
with charachange


li "私からすれば、皆さんがそのことで神経質になるのがいつも面白いんですよ。姉さんも、私や姉さんの見た目は他の人たちととても違って見えると言っていました"






show lilly basic_smile
with charachange


li "詳細は少し込み入っていますが、私は日本人とスコットランド人のハーフなんです"




"……スコットランド？　明らかに俺の最初の予想と違う。それをうっかり言いかけて、慌てて口をつぐむ。"



"それがどこにあるのか、記憶を呼び起こしてみる。イギリスって意味では、スコットランドも悪い所じゃない……のかなあ。"





"まあ、イギリスという俺の最初の予想は、少なくとも地理的には驚くほど近かったわけだ。だけど、同時に別の疑問が湧いてくる。"








hi "でも、全然訛ってないけど……？"

show lilly basic_weaksmile
with charachange


li "そこが込み入っているところですね。母は外国人ですが、私は日本で生まれ育ったので"





hi "ああ、なるほど"


"待てよ、もし晃さんの仕事が忙しくなったという理由でリリーが寮に移ってきたのなら……"






hi "じゃあ、家族の人は学校のそばで住んでるってわけじゃないの？"




show lilly basic_reminisce
with charachange


"リリーが小さくため息をつく。俺がこんなに突っ込んだ質問をするとは思っていなかったようだ。さっきの彼女の気さくさはただの飾りだったんだろうか？"


li "いいえ……実際は、もう長いあいだ会っていません"


"話の全体はまだ見えてこないけど、リリーの境遇についてこれ以上図々しく詮索したくはない。彼女の態度が急に変わったのは、この話題が気まずいと感じているということだろう。"





hi "じゃあ……英語も話せるんだ？　正直言ってスコットランドのことはあまりよく知らないんだけど、そこの公用語だってことは知ってるよ"


"話題が変わったおかげでリリーも落ち着きを取り戻す時間を得たようだ。"



show lilly basic_smileclosed
with charachange


li "ええ、そうです。私が小さいころは家族も家の周りでほとんど日本語を使っていましたが、同時に姉さんと私にスコットランド人としての教育を施すことも怠りませんでした"

show lilly basic_smile
with charachange


li "英語を流暢に話すことはできますが、学校でも勉強しています。主に語学力を保つため、それからちゃんとした資格を得るために"




hi "じゃあ、バイリンガルなの？　すごいな"


show lilly basic_weaksmile
with charachange


li "そこまではいきませんが、両親が英語を話せるというのは大きな利点でしょうね。点字の洋書も入手は難しくありませんし。少なくとも優子さんに助けてもらえればの話ですが"

show lilly basic_smileclosed
with charachange


li "なにより、ここでの英語教師の需要が比較的高いことも学習のモチベーションを得る助けになりますしね"


"英語教師の需要？　なぜそんなことを言い出したんだろう。俺はしばらく考え込む。"


hi "つまり、英語教師になりたいってこと？"

show lilly basic_cheerful
with charachange


"リリーが力強くうなずく。"



"はっきりした将来の目標を持つのは素晴らしいことに違いない。今まで自分の将来について真剣に考えたことは一度もないので、少しうらやましい気持ちになる。"



hi "ふうん……"



show lilly basic_smile
with charachange


li "どうしたんです？"


hi "いや……教師のリリーって簡単に想像できるよ。似合ってる"




show lilly basic_emb
with charachange


"リリーがしばらく無言になる。ほんの少しうつむき、苦笑にも似た笑みをもらす。こんな彼女を見るのは初めてだ。"






"リリーの学級委員としての立場と信頼できる人柄を考えると、教職というのは確かに彼女の人格に合った職業のように思える。"






hi "ごめん、ちょっと言い過ぎた。でも本当だよ"




show lilly basic_weaksmile
with charachange


"リリーが俺の言うことを打ち消すかのように自分の顔の前で手を振り、すぐに元の表情に戻る。"


li "いえ、そうではなくて……同じことを言ってくれた人は過去に一人だけでしたので"


stop music fadeout 8.0


"短い、気まずい感じの沈黙が後に残る。気づかないうちに、また面倒な話題に首を突っ込んでしまったようだ。"



"リリーを少し元気づけてあげないと。彼女が胸の内を明かすように仕向けたのはこっちなんだし。"





hi "この後食堂で昼食でもどう？"






"これで少しリリーが元気を取り戻すかもしれない。少なくとも複雑そうな家庭環境のことから彼女の気を紛らわせることができるんじゃないか。"





show lilly basic_planned
with charachange


"彼女の笑顔を見る限り、狙いどおりの効果を得ているようだ。"

show lilly basic_ara
with charachange


li "誘ってもらえるのは嬉しいのですが、あそこの食べ物は……"




"あっという間に話の流れが変わってしまう。だけど、リリーの言うとおりだ――あそこの飯はあまりうまくない。"




hi "上海なんかどう？　華子も来るかどうか聞いてみるか"






show lilly basic_surprised
with charachange


li "ああ……"


hi "どうかした？"



show lilly basic_weaksmile
with charachange



li "久夫さんに言われなかったら忘れてしまうところでした。もうすぐ華ちゃんのお誕生日なので、明日プレゼントを買いに街に行こうと思っていたんです"





hi "もしお誘いなら、喜んで。一緒に行くよ"



"ここの市街のつくりに慣れておくのはたぶんいいことだ。ほとんど行ったことがないので、一人なら絶望的に迷ってしまうだろう。"




show lilly basic_smile
with charachange


"この日曜日の計画に満足したかのように、リリーがうなずく。"


"そして俺たちはまた読書に戻る。その直前に、俺はもう一度だけちらっとリリーを見たけど。"


"たぶん俺は自分の境遇について考え過ぎていたんだろう。ここにいる誰もが、それぞれ違った特別な境遇にいるんだ。"


"外出して頭をすっきりさせるのは、俺にとっていい気分転換になるだろう。"

scene black
with dissolve



label jp_L3:

play ambient sfx_traffic fadein 10.0

scene black
with None

scene bg city_street1 at Fullpan(16.0, "left")
with locationchange


"店頭の窓際に置かれたテレビを突っ立ったまま観るのにも飽きて、たいした苦労もせずその場から離れる。"


"山久に来てからというもの、街の光景は全く別世界のように感じる。"



"廊下を走らない。教室では常に穏やかに節度をもって過ごすこと。部屋を出るときは人とぶつからないように左右を確認する。エレベーターは動作障害を持つ生徒専用。階段は一列に並んで昇り降りすること。"



"こんな軍規ともいえるような厳格な基準に比べたら、商店街は外国も同然だろう。"


"学校だって学園祭の時は少しは羽目を外したりもするけど、やっぱり外の世界はあそことは全然違う。"


"変な気分だ。倒れる前は大都会に住んでいたので、俺にとってここは山久やその周辺よりも自然な場所に感じるはずなのに。"



"それでも、自分が浮いている気がしてしまう。高架の遊歩道や人３人分よりも高い看板で飾り立てられた高層ビルも、すれ違う群集の反応から俺の注意をそらすことはできない。"

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")

show lilly cane_smileclosed_cas_close:
    center
    xpos 0.2
    easein 1.0 twoleft
show bg city_street1 at left
with Dissolve(1.0)


"リリーは俺の肩に片手を乗せたまま、もう片方の手で杖を持ち、それをメトロノームのように規則正しく動かしながら地面を突いている。振り返ると、彼女は相変わらず当たり障りのない微笑を浮かべ続けている。"




"制服姿のリリーしか見たことがなかったので、もしベンチに立てかけられた杖と彼女の特徴的な髪がなかったら、俺は危うくそこに座り俺を待つ彼女に気づかないところだった。"


"人々がリリーをちらちら見るのは、彼女の背の高さのためか、外国人風の外見のためか、それとも目が見えない様子のためか。その全てかもしれない。どういう理由であっても居心地悪く感じることに変わりはない。"

show lilly cane_smile_cas_close
with charachange


li "久夫さん、どこから見て回りましょうか？"


"リリーの柔らかい声がそんな俺の思考を吹き飛ばす。"


"人々の注意を引いているということをリリーが知らないとは思えないけど、本人はそれを気に留める様子もない。彼女は外出好きなタイプみたいだから、今ではこういう状況にも慣れてしまっているのかもしれない。"


hi "うーん。ここに来たのは初めてだから、どこに行けばいいのかよく分からないな"



show lilly cane_listen_cas_close
with charachange


"リリーは眉間にしわを寄せ、俺たちがたどるべき道筋を思案する。というか、それを説明する方法を考えている。"


"リリーと一緒にいて気づいたけど、彼女は深く考え込むとほとんど身振り手振りを使わなくなる。"




"表情は変わるかもしれないけど、ぴくりとも動かない。ただ、リリーが普段からジェスチャーをほとんど使わないらしいことを考えると、これは一部には彼女の控えめな性格から来ているのかもしれない。"



show lilly cane_weaksmile_cas_close
with charachange


li "この近くに大きな電器屋さんはありますか？"




"軽く周りを見回すと、目に入るのは洋服屋ばかりだ。それでもすぐに、俺はリリーの描写に当てはまりそうな青く光る看板をかかげる店が少し離れたところにあるのを見つける。"





hi "ああ、ちょうどすぐそこにあるよ。そっちに行ってみようか？"

show lilly cane_smile_cas_close
with charachange


"幸いそれがリリーにとって必要な情報だったようだ。彼女がうなずき、俺たちはその店を目印に、まだ見ぬリリーの目指す場所へと歩き出す。"



stop ambient fadeout 2.0

scene ev icecream
with shorttimeskip

play music music_happiness fadein 2.0


"店主" "どうぞ。バニラ一つ、チョコレート一つですね"

scene bg city_street2 at center
with locationchange


"カウンター越しに代金を渡すと、俺はアイスを持って遊歩道の手すりに腰掛けるリリーの元へ戻る。"



"リリーにこんなお茶目なことをされるとは思わなかった。アイス屋台に俺を連れて来ただけじゃなく、俺にアイスを買うようにせがんだりして。まあ、少なくとも彼女の分のアイス代は渡してくれたけど。"


show lilly cane_smileclosed_cas at Transform(xanchor=0.5, xpos=0.2, ypos=0.2, yanchor=0.0)
with charaenter


"案の定、リリーは俺が残してきた場所で辛抱強く俺を待っている。たぶん彼女は今日の外出をただの買い出し以上の出来事にすべく計画を練っていたのかもしれない。"



show lilly cane_smileclosed_cas:
    ease 1.0 xpos 0.5 xanchor 0.5 ypos 0.15
show bg city_street2:
    ease 1.0 left
with None

show lilly basic_satisfied_cas_close:
    xanchor 0.5 xpos 0.2 ypos 0.2 yanchor 0.0
    ease 1.0 xpos 0.5 xanchor 0.5 ypos 0.15 
show bg city_street2:
    ease 1.0 left
with Dissolve(1.0)


"俺はリリーに声を掛けると、彼女の伸ばす手の中にゆっくりとバニラアイスを持っていき、彼女がそれをしっかりと握るのを確認してから、手を離す。"


"少なくともリリーの味覚は正常だってことだ。アイスをせがまれた時、変な味のアイスを頼まれるんじゃないかと心配したけど。"


hi "はい、お釣り"

show lilly basic_smileclosed_cas_close at Transform(xalign=0.5, ypos=0.15)
with charachange


li "いいですよ。お釣りは取っておいてください"



"断ろうとするけど、こんな少額のために彼女に逆らうのも無益だと思い直す。俺はその小銭をポケットに滑り込ませて、自分の乏しい小遣いのささやかな足しにする。"


show lilly basic_smileclosed_cas_close
with charachange


"リリーが立ち上がる様子もないので、俺は彼女の隣に座り、アイスを食べ始める。"


hi "夏の天気っていいよな。しばらく続くといいけど"

show lilly basic_weaksmile_cas_close
with charachange


li "久夫さんもそう思います？　なんだか冬が好きなのは私だけのような気がしてきました"


"俺は彼女の言葉を聞いてしばらく考え込む。"


hi "まあ、そうかもしれないな"

show lilly basic_pout_cas_close
with charachange


"その言葉でリリーが狙い通りの反応をする。膨れっ面の彼女ってかわいいな。"


hi "だって、冬ってあまりいいことないだろ。着込まなきゃいけないし、それでもまだ寒いし"

show lilly basic_reminisce_cas_close
with charachange


li "北国に住んでよく雪遊びをしていたので、私は冬に少しノスタルジーを感じます。暑さも苦手ですしね"


hi "少なくともスカートははけるじゃないか。それには文句言うなよ"

show lilly basic_giggle_cas_close
with charachange


"彼女がくすくすとおかしそうに笑う。俺たちはすでに溶け始めている残りのアイスをまた食べ始める。"

play ambient sfx_crowd_outdoors fadein 2.0

hide lilly
show crowd at left
with shorttimeskip


"ぼんやり座って食べながら、行き交う群衆を眺める。人々の会話が断片的に聞こえてくる。"

show lilly basic_satisfied_cas_close at Transform(xalign=0.5, ypos=0.15)
with charaenter




"リリーを見ると、律儀にアイスを上の方からなめていて、自分のアイスが溶け始めていることには全く気づいていない。"






hi "アイス、溶けてるよ"

show lilly basic_surprised_cas_close
with charachange


li "えっ、どこですか？"



hi "ええと……ちょっと下のほうかな？"

show lilly basic_listen_cas_close
with charachange



"リリーが自分の口を上から下のほうへと持っていくけど、どこでアイスがたれているのか見つけられない。そこから先は俺が彼女を左右にガイドするゲームみたいになって、やがてついにその場所を探し当てる。"






"はたから見れば異様な光景に違いない。目をつぶってアイスを何度も回している少女と、隣で少女に指示を出している男。ガキの頃にやった目隠しゲームの変化形みたいなものかもな。"




show lilly basic_smileclosed_cas_close
with shorttimeskip


"長いあいだかかって俺とリリーはようやくアイスを食べ終わり、しばらく軽いおしゃべりの時間を過ごす。"



stop music fadeout 3.0

show lilly back_listen_cas_close
with charachange


"話している最中、リリーがいつもの調子ではっと頭を上げる。明らかに何かに注意を向けている様子だ。"

show lilly back_smileclosed_cas_close
with charachange


li "あ……"


hi "どうした？"

show lilly back_smile_cas_close
with charachange


li "あの辺りに姉さんがいないでしょうか？　声が聞こえたような気がして"



show lilly back_smile_cas_close at Transform(xpos=0.25)
show crowd:
    bgright
    xpos 0.55
show bg city_street2:
    bgright
    xpos 0.55
with dissolvecharamove





"驚いて、リリーが顔を向けるほうへと目を凝らす。でもこんな騒音の中で本当に晃さんの声を聞き分けられるのか、少し疑問に思う。"


show akira basic_boo behind crowd:
    tworight
    xpos 0.78 ypos 1.13
with charaenter


"だけどリリーの言うとおり、縦横無尽に行き交う人々のほんの少しの隙間からスーツを着た金髪女性の姿が見える。"





"俺は彼女がこちらに気づくように手を大きく振る。"


hi "砂藤さん！　おーい、砂藤さーん！"


show akira basic_smile
with charachange


"晃さんは俺の呼ぶ声に気づいた様子で、立ち止まって俺の方を見る。その時、俺は晃さんが誰かと一緒にいるのに気づく。"


"だけど、ここからじゃよく見えない。そうこうするうちに、２人が俺とリリーのいる場所に向かって歩き出す。"

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
play music music_ease fadein 4.0

show akira basic_smile:
    ease 1.0 ypos 1.0 alpha 0.0
with None

show akira basic_smile as akira2 behind lilly:
    tworight
    xpos 0.78 ypos 1.13 alpha 0.0
    ease 1.0 ypos 1.0 alpha 1.0
with Pause(1.0)

hide akira
with None

show lilly back_smile_cas_close at Transform(yalign=1.0)
with charamove


"２人がそばに来たので、リリーと俺は立ち上がってほこりを払う。"

show lilly back_giggle_cas_close
with charachange


li "姉さん？"

hide akira2
show akira basic_laugh behind lilly:
    tworight
    xpos 0.78 ypos 1.0
with charachange


aki "よう、２人とも"



show lilly back_giggle_cas_close at Transform(xpos=0.1)
show akira basic_smile at Transform(xanchor=0.5, xpos=0.6)
show crowd at center
show bg city_street2 at center
with dissolvecharamove

show hideaki bored at right behind akira
with charaenter


"晃さんが俺に向かって会釈をし、俺もすぐに会釈を返す。隣にいる女の子に視線を移すと、ちょうど彼女と目が合ってしまう。その時、晃さんが女の子の頭にぽんと手を乗せる。女の子がそれに驚く様子はない。"

show hideaki normal
with charachange


hh "会ったことはなかったよね。僕は秀明。初めまして、久夫さん"




"男の名前、だよな？　危ない所だったな。秀明くんは晃さんの手に強制されるかのように俺にお辞儀している。"






show lilly basic_smileclosed_cas_close at Transform(xpos=0.18)
with charachange


li "あら、秀明くんもいるの？　お元気？"



show hideaki thinking
with charachange


hh "晃さんがしっかり面倒見てくれてるよ。おかげさまでね"



show akira basic_laugh
show hideaki sad
with charachange


"晃さんがそれに同意するかのようにニヤニヤしながら秀明くんの頭を強く撫で、彼の頭がそれに合わせてぐりぐりと回る。秀明くんのふてくされた表情がなんだか面白い。"

show akira basic_smile
with charachange


aki "おじさんがまた出張でいないからさ、今日は秀明と街をぶらついてるんだ"

show akira basic_boo
with charachange


aki "あたしは彼氏とデートして過ごしたかったんだけどね……"

show hideaki closed_up
with charachange


"秀明くんが咳払いをして晃さんの考えをそらそうとしている。"




"だけど、秀明くんがそうしているあいだ、俺は考えを巡らせる。２人は親戚同士か？　いや、正確に言えば従姉弟ということか？　まあ、それが晃さんが秀明くんの面倒を見ている理由だろう。"




hi "そういやさ、秀明くん。なんで俺の名前知ってるの？"

show hideaki serious
with charachange


hh "晃さんが教えてくれたんだよ。山久の生徒ってことは、久夫さんも何か障害持ってるの？"









hi "あそこに通ってるのが全員障害者ってわけじゃないよ……"



"これは俺も最近まで知らなかったことだ。絶えず俺に学校関連の情報を流し続ける静音とミーシャに心の中で感謝する。"


"２人のおかげで、俺はこの学校が知的障害者以外なら事実上誰でも受け入れていることを知った。障害者と同じように、健康な人間も差別しないのだ。"


"もっとも、健康な人間がたくさんこの学校に来るとはとても思えないけど。教育水準はかなり高いにしても、こんなへんぴな所にあるし、障害を持つ生徒の補助を重視している学校だし。"



show hideaki angry_up
with charachange


hh "質問をはぐらかさないでよ"


"くそっ、鋭いな。"


"だけど、俺が返事をする前に、秀明くんは自分で答えを探ることにしたようだ。"

show hideaki evil
with charachange


hh "僕が考えるに……心臓かな？"

$ renpy.music.set_volume(0.5, 0.5, channel="music")
$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

show akira basic_lost
show lilly basic_listen_cas_close
with charachange


"晃さんが興味をそそられた様子で好奇の視線を俺に向ける。こんなの絶対まぐれ当たりに決まってる。"


hi "なんでそれが……？"

$ renpy.music.set_volume(1.0, 10.0, channel="music")
$ renpy.music.set_volume(0.5, 10.0, channel="ambient")

show hideaki thinking
with charachange


hh "五体満足に見えるから、外側の障害じゃないでしょ"

show hideaki serious
with charachange


hh "挙動も別に変じゃないから、知的障害ってわけでもなさそうだし"

show lilly basic_planned_cas_close
with charachange


li "でも、山久には知的障害を持つ生徒はいないのよ"

show hideaki bored
with charachange


hh "知ってるよ"

show hideaki serious_up
with charachange


hh "そんなことは置いといて、残った可能性といえば体内の障害しかない"

show hideaki happy
with charachange


hh "まあ、どこかまでは分からなかったから推測だったんだけど、正解みたいだね。久夫さんの反応ではっきりしたよ"



show akira basic_smile
with charachange


"あっけにとられながら、俺は晃さんを見る。晃さんは明らかに秀明くんの推理を楽しんだ様子で、笑いながら肩をすくめている。"





"そう、秀明くんは賢い。でも、かなり思いやりに欠ける。論理的だけど、気が利かない。その態度はある意味、静音を思い起こさせる。外見もだけど。"





show hideaki disapproves
with charachange



hh "どうしてそんなにじろじろ僕のこと見てるんですか？　別に珍しいものでもないと思うんですけど"




"自分の外見がどれだけ普通じゃないか、気づいてないのか？　スパッツと服はたまたま着てきただけと見過ごすことはできても、さすがに頭のリボンはないだろ。"




"だけど、今はそんなことを問題にしてるんじゃない。"


hi "ごめん。君を見てたらある人のこと思い出しちゃってさ"

play sound sfx_impact

show akira basic_boo
show hideaki surprise_up
with vpunch


"晃さんが肘で秀明くんを鋭く小突く。"

show akira basic_laugh
with charachange


aki "だからあの子とそんなに違わないって言っただろ"



show hideaki closed_up
with charachange


"秀明くんが咳払いをして、まっすぐ真面目そうな見た目を保とうとする。"





hh "じゃあ、姉さんに会ったんだね。たぶん僕のフルネームを言えば分かると思うけど"


show hideaki serious
with charachange


hh "僕は羽加道秀明。久夫さんが考えてるのって、たぶん僕の姉さん、羽加道静音のことでしょ"




"えっ、じゃあ秀明くんは静音の弟か。"


"あれ、ちょっと待てよ、もし秀明くんが晃さんのおじさんの息子で静音が彼の姉なら、リリーの父親と静音の父親は兄弟ってことで、それってつまり……"


hi "じゃあ、リリーと静音は従姉妹同士ってこと？"

show lilly basic_concerned_cas_close
show akira basic_smile
with charachange


"リリーがいつになく抑制のきかない様子でうめき声を漏らす。その反応を見て彼女の姉が面白そうにニヤつく。"



"リリーと静音の対立が別の意味合いを持ってしまった。２人の意思疎通の難しさのせいだとばかり思っていたけど、家ぐるみの確執となると事はもっと複雑だ。"


show akira basic_laugh
with charachange


aki "友達は選べるけど、家族は選べないからねえ"

show akira basic_boo
with charachange



"晃さんが気のない様子で肩をすくめる。２人の対立に関して、きっと俺みたいに深刻には考えていないんだろう。"




show akira basic_smile
with charachange


aki "まあ、そういうわけさ。２人はこんな天気のいい日に何してんだい？"



show lilly basic_smileclosed_cas_close
with charachange



li "私たちは華ちゃんのお誕生日プレゼントを買いに来たんです。もう日が近いから、この休日がお誕生日前にプレゼントを買える最後のチャンスなので"




stop music fadeout 7.0

show akira basic_lost
with charachange


"まるでリリーから空は青くなく雲は白くないという言葉でも聞いたかのように、晃さんが変な表情を見せる。"


aki "華子の誕生日って、来月の１０日じゃなかったかい？"

show lilly basic_surprised_cas_close
with charachange


li "ええ……どうして？　それが何か？"

show akira basic_resigned
with charachange



"晃さんの笑みが少し消えた気がする。こんなに騒々しくて気ままな人物には全然似つかわしくない表情をしている。"





aki "じゃあ、まだ電話来てないんだな？"

show lilly basic_oops_cas_close
show hideaki confused
with charachange


"リリーが何も分からないといった様子で首を振る。俺は秀明くんの方を見て何が起こっているのか知ろうとしたけど、彼もただ肩をすくめるだけだ。"

show akira basic_boo
with charachange


"晃さんはしばらくどうするか考えて、また笑顔に戻る。自分の感情をあっという間に隠してしまう晃さんに俺は戸惑う。"

show akira basic_smile
with charachange


aki "よう、チビ助、済まないけど久夫としばらくその辺をぶらついててくれないかな？"

$ renpy.music.set_volume(0.7, 2.0, channel="ambient")

show hideaki normal
with charachange

show lilly basic_oops_cas_close:
    parallel:
        easeout 1.0 xpos -0.5
    parallel:
        linear 0.7 alpha 0.0
show akira basic_smile:
    parallel:
        easeout 1.0 xanchor 1.0 xpos 0.0
    parallel:
        linear 0.7 alpha 0.0
show hideaki normal:
    ease 1.0 center
show bg city_street2:
    ease 1.0 right
show crowd:
    ease 1.0 right
with Pause(1.0)

hide lilly
hide akira
with None


"秀明くんはうなずいて、晃さんに手を振る。晃さんはリリーの肩に腕を回すと、俺の目の届かない所に彼女を連れて行ってしまう。"


"そんなわけで、俺は『チビ助』と２人、取り残される。"


hi "えっと……いい天気だよな"

show hideaki thinking at center
with charachange


hh "そうみたいだね"



"……"


hi "やっかい払いされちゃったみたいだな"

show hideaki serious
with charachange


hh "そうだね"



"なんて茶番劇だ。この子とどう話せばいいのか全く分からない。秀明くんのそっけない返事も全く助けにならない。この会話は成り立たないんじゃないかという気がしてくる。"




show hideaki triangle
with charachange


"秀明くんは明らかに退屈した様子で何も言わずに足をぶらぶらさせ始める。真面目ぶっているけど中身は本当にまだ小さな子供みたいだ。"


"秀明くんとの会話も終わっているような気がするので、俺はここに来たそもそもの目的を達成することにする。"


hi "俺はプレゼントを探しに行くけど、一緒に来る？"

show hideaki normal
with charachange


hh "他にすることもないしね"

stop ambient fadeout 0.5

scene bg city_street3
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0


"しばらくして、俺と秀明くんはコンビニの脇にある小さな店にたどり着く。"


"やっと見つかったその店のショーウインドウには、電化製品やパソコンゲームではなく、人形やぬいぐるみ、木製の工芸雑貨などが並べられている。"






"オセローズ……アンティーク？"


"アンティークショップ？　うーん、もしこの街に華子に合いそうなものがあるとしたら、たぶんここだろう。"


"古ぼけたドアの握りを掴もうとして、秀明くんがふらりとその場を離れようとしているのに気づき、また手を引っこめる。"




hi "入らないの？"

show hideaki triangle at center
with charaenter


hh "しばらく売店にでもいるよ。僕のことは気にしなくていいから"


"秀明くんの声の調子から、彼が店の売り物に全く興味を持っていないのが痛いほど分かる。俺に付いていく義務も感じていないようだ。"

hide hideaki
with charaexit


"秀明くんがそのまま一言もしゃべらず立ち去った後、厚い木製のドアを開けて店の中に入ると、俺の頭上でベルが鳴る。"

stop ambient fadeout 0.5
play sound sfx_storebell

scene bg city_othello at Fullpan(10.0, dir="left")
with locationskip

play music music_soothing fadein 0.5


"古い本と木製の棚から立ち込めるカビ臭さが、疑いようのない時の流れを感じさせる。"




"ドア脇のカウンターを見る。そこでは白髪の男の人が静かに座っていて、ボロボロになった本を読んでいる。この場に似つかわしい雰囲気だ。"


"ゆっくりと通路をぶらつき工芸品や輸入雑貨を見て回っていると、華子以外のある人物のことが頭に浮かぶ。"



"身をかがめて、ガラスケースの中にある年代物の樫の机を眺める。"



"大きさも造りも違う人形が、少なくとも３０体は並んでいる。共通点といえば、ビクトリア風の長いドレスを着ていることぐらいだ。"


"そのひとつの腰のあたりに付いている値札をめくってみる。"


"……とても手が届かない。"


"それぞれの値札を順番にめくっていく。人形がどんどん小さくなっていくのに反して、俺の失望はどんどん大きくなる。"



"それも、一番小さい人形に行き着くまでのことだった。ぎりぎりで手が届く値段だけど、出来はいい。長い赤褐色の髪を持ち、小さな青いドレスに身を包んでいる。"





"このプレゼントなら華子も喜んでくれるだろう。可愛らしくて、けばけばしくない。"


"それを注意深く手に取った後も、俺はしばらく店内を見て回ることにする。店の雰囲気を気に入っているのか、ただの好奇心なのか、自分でもよく分からないけど。"

stop music fadeout 2.0

show bg city_othello at left
with None



"隣の通路に移る前にちらっと隅を見ると、木製のおもちゃが並べられた棚が置いてある。そこにはミニカーもあれば、精巧なからくり人形もある。"


show musicbox closed:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)



"ずらりと並ぶくるみ割り人形の陰に隠れていた、小さくて飾り気のない木箱の存在に気づく。空いている手でそれを持ち上げると、びっくりするほど軽い。"


show musicbox open:
    ypos 0.5 alpha 1.0
with charachange

play music music_musicbox


"箱のふたは簡単に開き、すかさず中にある金属のドラムが回りだす。"


"しばらくのあいだ、ただその場に立ち尽くしたまま、俺は手の平サイズの旋律に耳を傾ける。"



"それがまだ鳴っている時に、小さな値札を指でつまんで顔の近くに持っていく。ものすごく小さな手書きの字で、読み取るのもひと苦労だ。"





"買えない……こともないな。"

show musicbox closed
with charachange

play sound sfx_switch
stop music

show musicbox closed:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide musicbox
with None


"ほんの少し顔をしかめながら、俺は箱のふたを閉じて人形とオルゴールをカウンターまで持っていく。"

show shopkeep surprised at center
with charaenter



"俺が品物をカウンターに並べている時、男の人が姿勢を正してその二つに目を向ける。俺みたいな若い人間がこんなものを買うことに驚きを隠せないようだ。"


show shopkeep thinking
with charachange



"痛い出費だけど、俺は代金を支払い、小さくて中身の透けない袋を持って店を出る。"


play ambient sfx_traffic fadein 0.5

scene bg city_street3
show hideaki serious at center
with locationchange


"秀明くんがその場にいて、俺は驚く。"


hi "おっと……やあ。売店にいるもんだとばかり思ってたけど"

show hideaki bored
with charachange


hh "晃さんから電話がかかってきたんだ。噴水の所でリリーさんと待ってるってさ"


"少なくともこれであの２人を探す必要はなくなったわけだ。"

$ renpy.music.set_volume(0.4, 0.5, channel="ambient")

scene bg city_street2
with locationskip



"俺たちは噴水目指して歩き出す。秀明くんの清楚ないでたちと外見に似つかわしくない振る舞いは、歩いている間でさえ変に対照的だ。"




show lilly cane_reminisce_cas at twoleft
show akira basic_boo at tworight
with charaenter


"リリーと晃さんが立ったまま俺たちを待っている。２人がなにを考えているのか、その表情からではよく分からない。"

show akira basic_smile at tworight
with charachange


aki "よう。じゃあ行くか、チビ助？"

show bg city_street2 at bgleft
show lilly cane_reminisce_cas at left
show akira basic_smile at Transform(xpos=0.55)
with charamove

show hideaki happy at right
with charaenter


"秀明くんも晃さんの元に戻って機嫌が直ったようだ。"

show hideaki happy_up
with charachange


aki "またな、リリー、久夫。華子に誕生日おめでとうって伝えてくれ"


hi "伝えときます。それじゃ"

show lilly cane_weaksmile_cas
with charachange


li "さようなら、姉さん"

hide akira
hide hideaki
show lilly cane_reminisce_cas
with charaexit

show lilly cane_reminisce_cas at center
show bg city_street2 at bgright
with charamove


"その挨拶を最後に、２人は昼下がりの街の喧騒の中へと消えていく。"




"リリーに向き直ると、小さな袋を持っているのに気づく。その時、リリーの様子が以前と違うような気がした理由がわかった。普段は感情を隠したりしないのに、今のリリーの表情と口調は曖昧で、読み取りづらい。"









"かなり気になるけど、リリーが自分の感情を隠そうとしているところを見ると、今の気持ちを俺に根掘り葉掘り聞かれたくはないだろう。"





hi "華子へのプレゼントはもう買った？"

show lilly cane_weaksmile_cas
with charachange


li "ええ。久夫さんは？"


hi "うん。買ったよ"

show lilly cane_sleepy_cas
with charachange


li "それでは、バス停に戻りましょうか？"


hi "分かった。もうすぐ山久行きのバスが来るはずだしな"


"こうして、俺とリリーは歩き出す。"

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")

scene bg city_street1
show lilly cane_concerned_cas_close at twoleft
with locationskip


"さっきと比べて様子が変だ。俺の腕を掴むリリーの手は不自然にこわばっていて、なんだかものすごく気まずい雰囲気になる。"


"沈黙が長い間続く。こんなリリーを見るのは全くいい気がしない。"

show lilly cane_sleepy_cas_close
with charachange


li "華ちゃんのお誕生日会、早めに開かないといけなくなってしまったのですが。久夫さんは４日でも大丈夫でしょうか？"





"別に他にすべきこともないだろうし、俺は反射的にうなずく。その後でこの行為が無意味であることを思い出し、すぐに口に出して返事をする。"





"リリーが冷静になろうと努力している。それが彼女の感情とかけ離れていることは明らかで、その様子は見ていてかわいそうに感じるほどだ。"




show lilly cane_weaksmile_cas_close
with charachange


li "すみません、久夫さん。バスはもうすぐ来るのでしたね？"


hi "そうだよ"


"でも、リリーがそう言った時、俺はあることを思いつく。"


hi "そうだな、リリーはこの後何か予定ある？"

show lilly cane_oops_cas_close
with charachange


li "いえ……特には。どうしてですか？"


hi "今こそリリーの手を取ってどこかに連れ去る時じゃないか、って思ってさ。まあ、そんなことはしないけど、俺を信用してくれる？"

show lilly cane_surprised_cas_close
with charachange


"俺はリリーの手を取り、それを引く。すると彼女のうつろな表情が軽い驚きと好奇心の混じった表情に変わる。"

stop ambient fadeout 2.0

scene bg city_karaokeint
with shorttimeskip

$ renpy.music.set_volume(1.0, 10.0, channel="ambient")
play music music_another fadein 2.0


"ウェイトレスが俺の頼んだ紅茶とコーヒーをテーブルに置く。俺は立ち去ろうとする彼女に軽くお礼を言う。"


"実をいうと、この喫茶店を見つけたのは本当にラッキーだった。俺はどこに行くべきかを考えあぐねていた。いや、むしろ俺はどこかによさそうな雰囲気の喫茶店がないかを探していたんだ。"


"リリーは少し元気を取り戻した様子で、コーヒーをごくごく飲んでいる俺の前でカップから一口だけ試し飲みする。"


"俺が望んだとおり、リリーはその味に気づくと、ぱっと表情を輝かせる。"

show lilly basic_weaksmile_cas_close at Transform(xalign=0.5, ypos=0.15, yanchor=0.0)
with charaenter


li "まあ……素敵！"

show lilly basic_surprised_cas_close
with charachange


li "久夫さん、どうしてこれだと……？"



"きっとリリーのお気に入り、いや少なくとも好みではあるんじゃないかと思って、俺はフレンチバニラティーのストレートを注文していた。紅茶のことはよく知らないけど、その名前から彼女が喜びそうな気はしていた。"



"……リリーがバニラアイス好きだから、って理由だけど。俺は間違いなく紅茶通じゃないな。"



hi "まぐれ当たりだよ。本当に紅茶好きなんだな？"


show lilly basic_smileclosed_cas_close
with charachange



"リリーはティーカップを机に置くと、小さくうなずく。幸いなことに彼女はいつもの微笑みを取り戻している。"


show lilly basic_smile_cas_close
with charachange


li "紅茶を飲むと……なんだか落ち着くんです"


hi "そんなに飲んで、中毒になってない？　カフェイン中毒ってのは最近よくあるけどさ"

show lilly basic_giggle_cas_close
with charachange


li "あら、私が中毒だって言いませんでしたっけ？"




"俺が顔を伏せるとリリーがくすくすと笑う。誰にでも悪癖の一つや二つはあるもんだ。世の中にはもっと悪い中毒だってあるんだし。"



hi "フレンチバニラティーのストレート、か。覚えとかなきゃな"


show lilly basic_smileclosed_cas_close
with charachange


"しばらくのあいだ、黙ったままそれぞれの飲み物を飲む。慣れない環境にいる俺にとって、リリーみたいな人が近くにいてくれるだけでとても心落ち着く。たとえ何もしゃべらず座っているだけでも。"


"リリーもそう思ってくれてるかなあ、と考え始めた時、彼女がカップを置く。"

show lilly basic_emb_cas_close
with charachange


li "久夫さん、少しおかしなことを聞いてもいいですか？"


hi "質問にもよると思うけど"

show lilly basic_weaksmile_cas_close
with charachange


li "久夫さんは……何色が好きなのかしら、って。誰にでも好きな色があるものだから"


"それに答えようとした時、俺はこのありふれているかに思える質問が実はとても奇妙なものであることに気づく。"


hi "好きな色？　でも……"

show lilly basic_pout_cas_close
with charachange


"リリーが頬を膨らませる。いいから答えなさいとでも言いたげだ。そんなことを知っても彼女には何の役にも立たないだろうけど、別に教えたって害にはならない。"




hi "いつも緑に魅かれてたな。たぶんそれが俺の好きな色だ"

show lilly basic_satisfied_cas_close
with charachange


li "緑ですね？　その色のことを考えるとき、久夫さんはどんなものを連想しますか？"


hi "たぶん……夏の芝生や木々かな。あと、軍もだな。迷彩色なんだ"

show lilly basic_planned_cas_close
with charachange


li "男の人って、皆軍隊が好きなようですね"

show lilly basic_smile_cas_close
with charachange


li "だけど……素敵な色のようですね。とても素敵な色"


"リリーが俺の選択を受け入れるかのように小さくうなずく。彼女の中にある色の概念が俺のものとは全く違うということを考えると、それを具体的なものと関連付けるのは確かに理にかなっている気がする。"


hi "もし誰でも好きな色を持ってるならさ、リリーの好きな色は何だ？"

show lilly basic_smileclosed_cas_close
with charachange


li "白。雪の色、それからアイスクリームの色だと教えられました"


hi "それじゃ俺とあんまり変わらないな。好きな食べ物の色だから、って理由だし。でもまあ、白もいい色だと思うよ"


hi "色といえば、ここももうすぐ暗くなるな。立つの手伝うよ"

show lilly basic_smile_cas_close
with charachange

show lilly basic_smile_cas_close at center
with charamove



"リリーが手を差し出す。俺はその手を取って席から立ち上がるのを手伝う。こんな何気ない触れあいには慣れていないおかげで、自分のとは比べ物にならない彼女の手の柔らかさに思わずはっとしてしまう。"





"だけど、リリーがそれを気にする様子はない。理由は明らかな気もするけど、一方ではそれも彼女の上品な物腰の現れのように思える。"



"リリーが自分のポケットに手を忍ばせようとするのを見て、俺は急いでそれを引き止める。"


hi "ああ、いいよ。俺が払う"

show lilly basic_cheerful_cas_close at center
with charachange


li "まあ、ありがとうございます、久夫さん"


"リリーの心の底からの笑顔を見て、お礼の言葉をもらうよりもはるかに大きな見返りを得た気分になる。"

stop music fadeout 2.0

scene bg suburb_roadcenter_ni
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.5, channel="ambient")
play ambient sfx_cicadas fadein 0.5


"俺たちがバスを降りるころには、辺りはもう真っ暗になっている。"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

scene bg school_road_ni
with locationskip


"俺とリリーは無言のまま丘を登っていく。たぶん今日過ごした時間のせいか、俺たちは２人とも少しぎこちなく振る舞っている。"


"リリーが晃さんに会った後に浮かない態度を見せていたのは気になるけど、ほんの少しであっても彼女を励ますことができたという事実を思い出し、なんだか勝ち誇った気分になる。"




"だけど……２人の間の空気が変わってしまったような気がする。ほんの少しだけかもしれないけど、俺たちのどちらも今までそのことを自覚していなかった。"



show lilly cane_weaksmile_cas_ni at center
with charaenter


li "これって……デート、ですよね？"



"そうだ。そのことは２人とも理解している。その問いに対する答えは、修辞的とさえ言えるくらいに明白だ。"




"なんだか気まずいような気もするけど、そんなに悪い気分じゃない。いや、むしろ正反対だ。どういえばいいのか分からないし、もちろんはっきりとは言えないけど、ほんの少し友達以上の何か、という感じがする。"



"理解？　共感？　なかなか適当な言葉が見つからない。それでも……"


hi "リリー、また今度一緒に行こうか？　プレゼントを買いに行くんじゃなくてさ"

show lilly cane_emb_cas_ni
with charachange



"試しに聞いてみても、リリーの様子は変わらない。ただ、その頬がわずかに赤く染まっているのが色白な肌のおかげでかろうじて分かる。そして目の前の道路に向けたままの顔を下げる。ほんの少しだけ。"
show lilly cane_cheerful_cas_ni
with charachange



li "……ええ"

stop ambient fadeout 2.0

scene black
with dissolve




label jp_L4:

scene bg school_girlsdormhall
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")


"学校のかばんを手に、俺は女子寮へと向かう。"



"かばんの中には、小さな箱と、その上に注意深く置かれた人形。しばらくかばんに入れっぱなしにしているけど、この箱をどう扱えばいいのか、まだよく分からずにいる。"




"考えてみれば、奇妙な状況だ。"




"華子の誕生パーティーが近づいていることは分かっていたけど、しばらく前に誰もいない紅茶部屋で小さなメモ書きを見つけるまでは、それが一体どんなものになるのか見当もついていなかった。"




"もう一度手に取り、メモの内容を確認する。目が見えないリリーが書いたとは思えないほどすごく読みやすいシンプルな黒色の手書き。これが彼女の多大な努力と注意の賜物であることは明らかだ。"

window hide



$ written_note(u"久夫さんへ\n\n私の部屋でパーティーを開きます。午後６時、女子寮の２２５号室に来てください。\nこんな形でお伝えしてしまってごめんなさい。学級委員の仕事がまだ残っていますので。\n\n砂藤リリー", text_args={"color":"#000000"})


window show


"俺はおどおどしながら廊下を進み、リリーの部屋の前まで来る。少しためらったけど、ついに決心してドアを鋭く３回ノックする。"

play sound sfx_doorknock2
with Pause(0.5)


"ドアの向こうで短いくぐもった言葉が交わされるのが聞こえる。耳を凝らすと、華子とリリーの声だということが分かる。"


"会話が終わり、リリーが俺に呼びかける。"


li "久夫さんですね？"


hi "うん。書き置き見たよ"


li "どうぞ。鍵は開いていますよ"



"部屋を間違えていなかったことにほっとした俺は、ドアの取っ手を下げて部屋の中へ入っていく。"


play sound sfx_dooropen


"ドアが開いた時、挨拶しようとしていた俺は息を呑む。"

window hide

play music music_one fadein 10.0

scene ev lilly_bedroom:
    truecenter
    zoom 1.1 subpixel True
    ease 15.0 zoom 1.0
with GenericWhiteout(0.5,0.1,4.0)

window show




"パジャマに身を包んだリリーが部屋の真ん中にあるローテーブルのそばに座り、その向かいにはナイトガウンを着た華子が座っている。制服姿でしかない俺はひどく場違いな気持ちになる。"






"２人の可愛らしい姿をちらりと盗み見て、不本意ながらもリリーの細長い色白の脚から視線を引きはがす。"



hi "や、やあ。俺……必要な物、全部持ってきたと思うけど"

scene ev lilly_bedroom_large:
    xpos -130 ypos -400 subpixel True
    acdc_warp 12.0 ypos -800
with flash



"リリーが微笑んでうなずく。自分がこんなに色っぽい姿をしていることに、本人は気づいているんだろうか。ダークブルーの薄いシルクのパジャマがよく似合い、それが彼女の目と体の曲線をさらに際立たせている。"






"昨夜のリリーの曖昧でためらうかのような様子は、いつもの挑発的な性格に取って代わられたみたいだ。彼女が自信を取り戻したのはいいことだけど、あの時の様子がどうしても頭に浮かんでしまう。"





scene ev lilly_bedroom_large:
    xpos -830 ypos -200 subpixel True
    acdc_warp 12.0 ypos 0
with flash



"華子のほうを見ると、緊張した面持ちでリリーの向かいに座っている。こんなに地味な寝巻きを着ているのも別に驚くことじゃないけど、とても可愛く見える。"



hi "やあ、華子。誕生日おめでとう"


ha "えっと……あ、ありがとうございます"


"華子はすごくおどおどしている。知り合った時よりも俺にかなり打ち解けた態度を見せるようになってきた彼女だけど、たぶん今みたいな状況には慣れていないんだろう。"

scene ev lilly_bedroom
with flash


li "久夫さん、どうぞ座ってください。すぐにお茶を入れますね"


hi "じゃあ遠慮なく"

$ renpy.music.set_volume(0.8, 2.0, channel="music")

scene bg school_dormlilly
with locationchange



"俺が近くの壁際にかばんを置いて座ろうとするあいだ、リリーは机の脇から湯気の立つ赤色のティーポットを手に取り、それぞれのティーカップに中身を注ぐ。"



"大分落ち着きを取り戻してきて、俺は自分がリリーの部屋に来るのはこれが初めてだということを思い出す。"



"最初に気づくのは、部屋の中に立ち込めるほのかな香り。俺の部屋のものとは何となく違う……たぶんかすかな香水か、マニキュアだろう。何にせよ女の子の持ち物っぽい香りがする。"





"それと、リリーの部屋は見た目が地味だ。ベージュ色の壁に、機能的だけど簡素な収納棚。ポスターや壁掛けの類いは見当たらない。際立って実用的だけど、リリーは目が見えないのだから当然のことだろう。"





"俺が唯一不自然に感じたのが、床の上にうず高く積まれているいくつかの本の山だ。どれも膝から腰の高さまである。何冊かの表紙にはタイトルが書いてあるけど、他の本には点字以外に何も書かれていない。"




"文字として印刷されているタイトルも例外なく英字なのが興味深いけど、全く予想外ってわけじゃない。そういえば以前、リリーの両親が彼女と晃さんに英語を教えたと言ってたっけ。"



hi "いい部屋だな、リリー"

show hanagown distant:
    center
    ypos 1.15
with charaenter


"肩越しにお礼の言葉を聞く。華子のほうを振り返ると、自分の膝元をじっと見据えながら、神経質そうに自分の寝巻きを手でぎゅっと掴んでいる。"


"その理由に今になって気づく。この姿だと華子のやけどの跡が普段よりもはるかにはっきりと見えてしまうからだ。やけどの跡は首元にまで達していて、さらに右肩の全体を覆っている。"



"華子のためのパーティーだというのに、当の本人は俺がいるせいで全然楽しめていないようだ。"



hi "それで、何歳になった？　１８歳？"

show hanagown worry
with charachange


"感情を隠すのが苦手な華子の驚いた様子からすると、どうやら彼女は俺の存在を頭の中で消し去ろうとしていたようだ。なんだかすごく気まずいな。"


ha "は、はい"


hi "いいことといえば、あと二年で酒が飲めるってことだな。それで、どっちが年上？　華子、それともリリー？"

show hanagown normal
with charachange


ha "リリーです。に、二月が……誕生日だったから。久夫くん……は？"




hi "今年のしばらく前だよ。もう過ぎちゃったな"





"俺が病院に閉じ込められている間に過ぎてしまったってことは言わないでおく。あの時は……人生のどん底だった。"


show hanagown distant
with charachange

show hanagown distant:
    tworight
    ypos 1.15
show bg school_dormlilly at bgright
with charamove

show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2 
with charaenter

play sound sfx_teacup



"予想通り、会話はすぐに途切れてしまう。その直後にリリーが飲み物を支度し終えて、３人分のティーカップを並べる。"



"自分のカップを取ってすぐ、今まで飲んでいた紅茶よりもはるかに強い香りと味がすることに気づく。"



hi "あれ、学校で飲む紅茶と味が違うな"


show lilly basic_smile_paj
with charachange


li "あそこで飲むのとはまた違う種類のお茶ですよ。オレンジジャイプールを飲むのは初めてですか？"


hi "覚えてる……限りは。そもそも普段はコーヒーを飲んでるからな。この前街に行った時みたいにさ。でも、これもいけるな"

show hanagown normal
with charachange



"落ち着いて紅茶を飲んでいると、華子がだんだんリラックスしてきたようだ。少なくとも俺がいることに対する緊張はほぐれている気がする。"




"３人ともほぼ同時にそれを飲み終える。華子の脇に、食べろと言わんばかりにケーキが置いてある。華子はそのケーキへの期待を隠すことができない様子だ。"


stop music fadeout 4.0


"よく考えてみたら、俺だってケーキをとても楽しみにしているんだ。だけど、まず先にやるべきことがある。"


hi "リリー？"

show lilly basic_planned_paj
with charachange


li "ええ、いい頃合いですね"


"２人ともそれぞれが何を考えているのかよく分かっている。リリーが立ち上がって彼女の贈り物を持ってくると同時に、俺も体を横に傾けてかばんの中から華子のために買った人形を探り出す。"


"そして、それぞれ隠し持った贈り物を同時に机の上に置く。"

show lilly basic_cheerful_paj
show hanagown normal_blush
with charachange


$ doublespeak (li, hi, "お誕生日おめでとう！", "誕生日おめでとう！")



"華子はただただ驚き、しばらくそれを見つめたまま無言で座っている。"



"俺のビクトリア朝ドレスと小さな帽子に身を包んだ木製の小さな人形が、リリーの薄茶色のふっくらしたクマのぬいぐるみと並んで置かれている。"

show hanagown distant
with charachange



"華子がそのささやかなプレゼントから目を離すことなく、自分の寝巻をぎゅっとつかみながら言葉を発する。"


show hanagown distant_blush
with charachange


ha "あ…ありがとう……リリー、それに……久夫くんも……"


play music music_serene fadein 6.0

scene unlock_ev lilly_hanako_hug_end
show black
show ev lilly_hanako_hug:
    xalign 0.5 yalign 1.0 alpha 0.0 subpixel True
    parallel:
        linear 5.0 alpha 1.0
    parallel:
        easein 15.0 yanchor 0.0 ypos -0.15

with locationskip


"リリーが前に出て華子を柔らかく抱きしめる。華子の声がうわずり出す。"


"リリーにぎゅっとしがみつく華子を見て、胸の奥が暖かくなるのを感じる。俺はその光景を前に笑顔を隠したくても隠すことができない。"


"リリーが華子の頭に自分の顔を優しくあてがい、俺にはほとんど聞こえない、とても静かな柔らかい声でささやく。"



li "お誕生日おめでとう、華ちゃん"


hi "誕生日おめでとう"



"華子は小さくうなずき、しばらくリリーの胸元にすがってから体を離して目をぬぐう。"





"誰かが、いや誰であっても、そばにいて愛してくれる。華子にとってはそれだけで特別なことなんだと思う。今、リリーと俺がその役割を共有している。きっと俺は、そのことをいつまでも感謝し続けるだろう。"



scene ev hanako_presents1
with locationskip


"華子は人形とテディベアを優しく手に取ると、穏やかな笑みを浮かべながらその両方を胸元に引き寄せる。"


"長いあいだ、３人とも幸せな沈黙に包まれながら、ただ座り続ける。その沈黙はリリーの柔らかい招きの声が発せられるまで続く。"


li "では、ケーキを食べましょうか？"

scene bg school_dormlilly
show lilly basic_smile_paj:
    twoleft
    ypos 1.2
show hanagown smile:
    tworight
    ypos 1.15
with locationskip



"リリーの提案に、俺と華子は期待を隠し切れずに答える。"


hi "異議なし"


ha "うん"

stop music fadeout 2.0

scene bg school_dormlilly
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
show hanagown normal:
    tworight
    ypos 1.15
with shorttimeskip


hi "ふう、うまかった"

play music music_dreamy fadein 4.0


"すっかり満足してくつろぐ。リリーも華子も俺と同じように満足したようだ。ちょっと苦労したけど、俺たちはそのケーキを全部食べ切ることができた。"

show hanagown normal_blush
with charachange


ha "私、もう食べられない"

show lilly basic_weaksmile_paj
with charachange


li "次回はもう少し小さなケーキを買ったほうがいいですね"

show hanagown smile
with charachange



"華子と俺が声を出して笑う。だけど来年の今ごろには俺たちは山久を卒業しているという事実を思わずにはいられない。"



"俺にとってはある意味がっかりする事実だ。やっと普通らしい生活に戻り始めた気がしているところなのだから。"


"リリーのこざっぱりした秩序ある部屋をぼんやり見回していると、再び彼女の本の山が俺の目に飛び込んでくる。"


"ちょっと軽はずみかもしれないけど、俺は好奇心を抑えることができない。それに、リリーだって断ったりはしないだろう。"


hi "なあ、リリー。リリーの本、見せてもらってもいい？"

show lilly basic_smile_paj
with charachange


li "ええ、もちろんです、久夫さん"

show lilly basic_planned_paj
with charachange



li "ですけど、もし久夫さんが二つの言葉の壁を克服できたら、とても驚きですよ"



hi "二つ？　点字と……ああ分かった、英語か"

show lilly basic_smile_paj
with charachange


"リリーがうなずく。"


hi "リリーが英語を勉強してるってのは知ってたけど、まさかここまでのレベルだとは思わなかったよ"

show lilly basic_giggle_paj
with charachange


li "他の人が私のコレクションを借りてしまうのを防ぐ完璧な方法といえますね"



"リリーは冗談交じりにそう言うけど、それを聞いて俺は少し失望する。周りにこれだけたくさん本があるのにそれを読むすべがないというのは、まるでからかわれているみたいだ。"




"華子が静かにくすくす笑う間、俺は一番近い本の山に手を伸ばして、ちらりと見ただけで一番上の本を取り上げる。『Death on the Nile』、表紙に大きく書かれたその文字だけが、印刷されている唯一の文字だ。"


$ renpy.music.set_volume(0.5, 0.5, channel="music")
play sound sfx_paper
show ev braille at Fullpan(10.0, dir="right")
with locationskip



"リリーと華子が話し込んでいるあいだ、俺は膝の上で本を開き、しばらく座り込む。"



"それぞれのページに打ち付けられた点たちを感じ分けようとしても、それらはお互いに混ざり合ってしまい、俺には全く区別できないように思える。"



"もっと簡単なものだと思っていた。だけど多少訓練すれば、俺より優れた触覚の持ち主なら点字をかなりの速さで読み取れるようになるだろう。"


$ renpy.music.set_volume(1.0, 0.5, channel="music")

scene bg school_dormlilly
show lilly basic_smileclosed_paj:
    twoleft
    ypos 1.2
show hanagown normal:
    tworight
    ypos 1.15
with locationskip


"たぶんさっきから続いていたであろう沈黙に気づいて点字のページから目を上げると、華子はおかわりした紅茶を飲み、リリーは微笑んでいる。"


hi "なんかおかしい？"

show lilly basic_smile_paj
with charachange


li "いいえ、その逆です。久夫さんの探究心はとても愛らしいですよ"


"その言葉を聞いて、俺は異常に嬉しくなる。同時に自分の頬が少し熱くなるのを感じたけど。"


hi "ありがと。でも、他にやり方が分かんないよ"


show lilly basic_weaksmile_paj
with charachange



li "本当のことを言うと、別の学校から転入してきた久夫さんが私たちをどう見ていたのか、よく分からなかったんです"


stop music fadeout 12.0

show lilly basic_reminisce_paj
with charachange


li "もし久夫さんが私たちに同情の目を向けていたら、私はきっととても傷ついたと思います"

show hanagown distant
with charachange



"リリーの声が鋭さを帯びる。きっとそれは彼女のプライドから来ているに違いない。華子をちらっと見ると、彼女はいつもよりも感情を押し殺した様子で、俺ではなくリリーの方を見ている。"



hi "心配ないよ。俺だって自分の置かれた立場を考えたら、他人の同情なんかできるわけないし"


hi "俺が発作を起こした後、俺に最初に会いに来た時の親の顔なんかさ……あんな顔、誰にも見てほしくないよ"

show lilly basic_oops_paj
show hanagown distant_blush
with charachange


"これ以上話すのはやめようと自重するけど、もう手遅れだ。目の前の２人とも、特にリリーが、困惑した様子を見せる。"

show lilly basic_emb_paj
show hanagown worry
with charachange


li "ごめん……なさい。そんなに深く聞くつもりは……"

show lilly basic_listen_paj
with charachange

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_doorknock2



"少しの間、気まずい沈黙がその場を支配する。ありがたいことに、俺も簡単に気づけるほどのしぐさでリリーがはっと顔を上げて、沈黙が終わる。"



hi "なんか聞こえる？"

show lilly basic_surprised_paj
with charachange


li "ドアが……"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_dooropen

show lilly basic_surprised_paj:
    left
    ypos 1.2
show hanagown distant_blush at Transform(xpos=0.4)
show bg school_dormlilly at bgleft
with charamove


"リリーの言葉を頼りに、皆いっせいにドアに注目する。彼女の言う通り、ドアのレバーが音を立てながら回り、黄色と黒の閃光が部屋に滑り込んでくる。"

show akira basic_laugh at right
with easeinright

play music music_running

show lilly basic_listen_paj
show hanagown worry
with vpunch


aki "砂藤晃、ここに参上！　誕生日おめでとう、華子！"

show hanagown worry_blush
with charachange


ha "えっと……ありがとうございます……"

show akira basic_smile at Transform(ypos=1.15, xpos=0.8, xanchor=0.5)
with dissolvecharamove


"脇に背の高い袋をどさりと置きながら、晃さんが机のそばに座る。トレードマークである陽気な空気を振り撒いて、登場するのも大騒ぎだ。"

show hanagown distant
with charachange


"寝巻をぎゅっと掴んでいる華子も、落ち着きを取り戻すにつれ震えがおさまる。彼女は前にも晃さんに会ったことがあるはずだ。晃さんとリリーの関係がどれだけ近いかを考えれば別に驚くことじゃない。"



"晃さんは、ひときわ目立つ華子のやけどの跡を微塵も気にしていない様子だ。だけど同時に、華子のシャイな性格に気を使っているようなそぶりも全くない。"

show lilly basic_weaksmile_paj
with charachange


li "姉さん、お仕事があるって言っていた気がするけれど。しばらく抜け出すことができたの？"

show akira basic_boo:
    ypos 1.15
with charachange


aki "あー、まあね。残業してる連中をほっとくのも気が引けるから、すぐ帰らなきゃいけないけど"

show akira basic_smile
with charachange


aki "でも、可愛い華子お嬢ちゃんの誕生日に来ないのも気が引けてさ、それで今こうしてここにいるわけさ"

show hanagown smile
with charachange


"晃さんが華子に向かってにんまり笑うと、華子がかあっと赤くなりながら自分の膝に目を落とす。恥ずかしくて笑顔を抑えようとしているのか、何度も口を開いたり閉じたりしている様子だ。"


"その反応が、自分の外見を恥ずかしがるときよりも素早く力強い反応に見えて、ちょっと奇妙だ。華子はお礼に小さくうなずくのがやっとだったけど、それには感謝の気持ちが余すところなく現れている。"


"きっと、華子の注意を前向きな意味で引くことができる人は数えるほどしかいないだろう。俺に比べてはるかにうまく華子を扱い喜ばせることができる晃さんを尊敬してしまう。"

show akira basic_laugh
with charachange


aki "さてと、帰る前に……"

play sound sfx_rustling


"晃さんは脇に置いてある袋に手を伸ばすと、その中身を華々しく披露する。"

show wine:
    yalign 0.5 xanchor 0.0 xpos 1.0 alpha 0.0
    easein 1.0 alpha 1.0 xanchor 1.0
with Pause(1.0)


"それは二本のガラス瓶で、その両方とも貼られているラベルに長ったらしいフランス語名が書かれている。"

show hanagown normal
with charachange


"華子が驚きと好奇心の混じったおかしな表情を見せる。たぶん俺も同じ表情をしているだろう。ことの成り行きを見ていないリリーは、なにが起こっているのかに気づいていない。"

show hanagown normal_blush
with charachange


ha "晃さん……これはちょっと……"

show lilly basic_surprised_paj
with charachange


li "何ですか？"


hi "ワインだよ。赤一本、白一本"

show lilly basic_pout_paj
with charachange


li "ね、姉さん！　それは……！"

show akira basic_smile
with None

show wine:
    easeout 1.0 alpha 0.0 xanchor 0.0
with Pause(1.0)

hide wine
with None


aki "まあまあ。静音がここにいて責め立てるわけでもあるまいし"


hi "リリーの言う通りですよ。校内の飲酒は禁止です"


hi "……というか、校外でもですよ。俺たちがまだ未成年だってこと忘れたんですか？"

show akira basic_laugh
with charachange



aki "よく言うよ、ボトルを持ったまま飲みたくてしょうがないって顔してるくせに"





"一本取られたな。俺は純粋にほんの少しだけでも試してみたい。華子はボトルを手にしてはいないけど、反対からはほど遠い気持ちであることはその表情から明らかだ。"


show lilly basic_displeased_paj
with charachange



"リリーは手で額をさすり、晃さんへの反論をあきらめる。おかしな『規則』と『規制』など気にも留めない晃さんには何を言っても無駄だとわかっているんだ。"


show lilly basic_displeased_paj
with charachange



li "校内の誰にもそんなこと絶対に言わないでね。お願いだから"


show akira basic_smile
with charachange


aki "あたしもバカじゃないよ。心配すんなって"

show akira basic_boo
with charachange


aki "そうだ、もうすぐ仕事に戻んなきゃ"

show lilly basic_oops_paj
with charachange


li "そんなに早く？　今来たばかりなのに……"

show akira basic_resigned
with charachange


aki "ごめんよ、リリー。でも、２人の顔を見れてよかったよ。久夫、君もね"


hi "じゃあ、また"


ha "あの……さ、さようなら……晃さん……"

show akira basic_resigned at Transform(yalign=1.0)
with charamove

hide akira
with charaexit


"晃さんはよいしょと立ち上がると、俺たちと机上の二本の品をその場に残して部屋の外へと躍り出る。"

show lilly basic_oops_paj:
    twoleft
    ypos 1.2
show hanagown normal_blush:
    tworight
    ypos 1.15
show bg school_dormlilly at center
with charamove


hi "……面白いな"

show lilly basic_arablush_paj
show hanagown normal
with charachange


"ワインボトルを手に取る華子の横で、リリーが姉のおふざけに苦笑する。"

show hanagown distant_blush
with charachange


ha "それで……"


hi "どう思う、リリー？"

show lilly basic_weaksmile_paj
with charachange


"リリーは机にひじをついて、鼻筋を押さえながらどうすべきか考えている。自分の姉の思考に全く付いていけないようだ。"

show lilly basic_smile_paj
with charachange

stop music fadeout 3.0


li "そうですね……もうここにあるのだし。少しいただきましょうか"


"リリーがそう言うと同時に、俺は部屋の中を見回してコップのありかを探す。"

scene bg school_dormlilly_ni
with shorttimeskip

play music music_night fadein 0.5


"頭上からの小さなうめき声を聞いて、俺はリリーが数分前に少しベッドで体を休めるために飲酒を切り上げたのを思い出す。"


"精根尽き果てた俺は、ようやく立ち上がると身を引きずるようにベッドの脇まで移動して、そこにもたれかかるように座り込む。"

show bg school_dormlilly_ni as ovl1:
    xalign 0.5 alpha 0.4 yalign 0.5 zoom 1.0
    ease 1.0 xalign 0.55 alpha 0.5 rotate 1 zoom 1.05
    ease 1.0 xalign 0.5 yalign 0.5 alpha 0.0 rotate 0 zoom 1.0

show bg school_dormlilly_ni as ovl2:
    xalign 0.5 alpha 0.4 yalign 0.5 zoom 1.0
    ease 1.0 xalign 0.45 alpha 0.5 rotate -1 zoom 1.05
    ease 1.0 xalign 0.5 yalign 0.5 alpha 0.0 rotate 0 zoom 1.0


hi "なんてこった"

show lilly basic_listen_paj_ni:
    center
    ypos 1.2
with charaenter


li "うぇ……"


"リリーのうめき声は生気を失っているかのようだ。"


hi "飲み過ぎじゃないか？"

show lilly basic_concerned_paj_ni
with charachange


li "頭が痛いです"


hi "ほら、やっぱり飲みすぎだよ"


"俺は頭を後ろにもたれかけ、ぼんやりと天井を見つめる。まったく、なんて災難だ。"


"世間のバカがやるみたいに、俺たちは次々とグラスを空けながら夜を過ごした。華子はただ横に倒れ込んで寝てしまい、俺はリリーほどには気分が悪くない自分を奇跡だと感じている。"

show lilly basic_sad_paj_ni
with charachange


li "ねえ、久夫さん？　今夜のこと、すみません。こんな……ことになるなんて"


hi "大丈夫だよ、リリー。正直、すごく楽しかったし"

show lilly basic_weaksmile_paj_ni
with charachange


li "本当ですか？"


hi "うーん。たぶん華子もそうだよ。いや、絶対"

show lilly basic_reminisce_paj_ni
with charachange


"短い沈黙の後、仰向けのリリーが再びうめき声を上げる。"


hi "大丈夫か？"

show lilly basic_weaksmile_paj_ni
with charachange


li "久夫さんの言う通り、飲みすぎました。何時ですか？"


hi "時間？　ええと、今は……"


"俺はすばやく腕時計を見る。視界がぼやけて数字をほとんど読み取れない。"


hi "夜中過ぎだ"

show lilly basic_concerned_paj_ni
with charachange


li "では、もう門限は過ぎていますね"


hi "ああ、そうだろうな。今夜はここで寝なきゃな"


"それを言い終わると同時に、俺は起き上がろうとするリリーからシーツがずり落ちる音を聞く。"

show lilly basic_oops_paj_ni
with charachange


li "華ちゃん……"


hi "あっ、いや、寝てろって。起きなくていいから"

show lilly basic_displeased_paj_ni
with charachange


li "久夫さん、私が……"


hi "どう見ても俺よりリリーの方が具合悪そうだぞ。ちょっと休めって"

show lilly basic_oops_paj_ni
with charachange


li "でも、華ちゃんが……"


hi "俺が予備の毛布を華子にかけとくから。心配すんなって"

hide lilly
with charaexit


"大あくびをしながら毛布を取るために立ち上がると、柔らかな衣擦れの音を立てながらリリーがまた横になる。"


li "ありがとうございます、久夫さん"


hi "いいよ。こんなことぐらいしかできないからな。リリーも完全に酔っぱらってるな"


li "酔ってなんか……いませんよぅ……ちょっと疲れた……らけでぇ"


"リリーが頬を膨らませ始める。また彼女に酔いが回り、ろれつが回らなくなってきている。俺はベッドの隅に丸めて置いてある毛布を何枚か掴む。"


"静かに華子の元に歩み寄り、起こさないように気をつけながら穏やかに眠る華子の体に毛布をかける。"


"もっとも、こんなに酒臭い華子に俺が何をしても彼女が起きることはないだろう。"


"その場に立って、部屋の状況を最終確認する。"

stop music fadeout 4.0


"泥酔した２人の少女に、女子寮で彼女たちと一晩一緒に寝る野郎が１人。こんなことがばれたら大スキャンダルになることは必至だ。"


"ベッドの脇に戻りそこに座りながら、最後に一度だけリリーをちらりと見る。"


"手足を投げ出しただらしない格好でほんの少し横を向いて、穏やかに身を横たえている。"


"リリーがよく見えるよう彼女のほうに身をかがませる。"

play music music_comfort

scene ev lilly_sleeping:
    truecenter zoom 1.05 subpixel True
    acdc_warp 20.0 zoom 1.0
with locationchange


"リリーの白い肌がベッド上の枕の白に溶け込み、彼女の顔にはまどろみから来る安らかな表情が浮かんでいる。"


"普段は自信に満ちて、前向きで、華子の面倒だってしっかり見ているリリーだけど、今の彼女は痛々しいほど繊細に見える。"


"俺は、華子が受け取ったプレゼントのことを思い返す。"


"華子にとって素晴らしい機会になるだろうと予想はしていたけど、こんなに感動的だとは思いもしなかった。"


"誕生日が来るたびに、毎年毎年。"


"華子とリリー、２人っきり。"


"……きっと、華子が喜んだのはプレゼントのせいだけじゃない。"

scene bg school_dormlilly_ni
with locationchange


"俺は心地の悪い眠りを受け入れるため再びベッドの脇に座り、疲れた腕を体の横にだらりと垂らす。"


li "ねえ、久夫さん"


"リリーがほとんど聞こえないぐらいの小さな声で俺を呼ぶ。もう半分寝ているに違いない。"

scene ev lilly_sleeping:
with locationchange


hi "なんだ？"

scene ev lilly_sleeping_smile
with charachange


li "ありがとうございます"


hi "ありがとう？　何が？"


li "ここにいてくれて"


hi "……いいよ"

scene bg school_dormlilly_ni
with locationchange


"深い寝息を聞き、リリーが完全に眠ってしまったことを知る。"



"俺も目を閉じると、ほどなく眠りに落ちる。"


stop music fadeout 2.0

window hide

scene black
with shuteye



label jp_L5:

window hide None

scene black
with Pause(4.0)

stop music

window show


mystery "久夫さん？"


mystery "久夫さん、大丈……？"


"柔らかい、ほとんど聞こえないぐらいの小さな声が俺の耳をくすぐり、俺はゆっくり目を覚ます。いつもこういう目覚めだったらいいのに。"


"まどろみながら、俺はゆっくりと目を……"

scene bg school_dormlilly
show lilly superclose
with openeye_shock

show lilly superclose_shock
with Dissolve(0.2)


$ doublespeak(hi, li, "うわっ！", "きゃっ！")

play sound sfx_impact2

show lilly superclose_ouch
with vpunch

show lilly basic_concerned_paj:
    xalign 0.5 yanchor 1.0 ypos 1.2
    ease 0.4 ypos 1.4
with Dissolve(0.2)



"目と鼻の先で物珍しそうに様子をうかがうリリーに驚いて、俺は大きな音を立ててリリーに頭をぶつけてしまう。衝撃で２人してひっくり返り、痛みに悲鳴を上げる。リリーのは悲鳴というより、音の出る玩具みたいだ。"





hi "あいててて"

play music music_happiness fadein 6.0


"俺は片方の手で自分の体を支えながら、もう片方の手でゆっくりと額をさする。リリーは少し離れたところで、明らかに痛がっている表情で俺と同じことをしている。"


hi "うう……ごめん。リリーの顔がなんか近かったからさ、反射的に動いちゃって。大丈夫？"

show lilly basic_concerned_paj:
    ease 1.0 ypos 1.2
with Pause(0.5)


li "頭が……"


"大丈夫じゃないみたいだ。よく考えたら、リリーの激しい頭痛の原因は俺とぶつかったからだけじゃないはずだ。"



hi "二日酔いか？　昨日の夜はすごく飲んでたからな"

show lilly basic_sad_paj:
    ypos 1.2
with charachange


"俺が起き上がるあいだ、リリーが俺の言ったことを認めて静かにうなずく。"

show lilly basic_concerned_paj:
    ease 1.0 ypos 1.0
with Pause(0.5)


"俺はリリーに手を差し出し、彼女が立ち上がるのを助ける。彼女の後ろをちらりと見ると、華子がまだ眠りこけている。"

show lilly basic_reminisce_paj at center
with charachange


li "こんなの不公平です……久夫さんと同じくらい飲んだだけなのに……"


hi "なんかそれって俺の記憶と全然違うぞ。それに、女の子は男よりもアルコール耐性が低いんだし"

show lilly basic_displeased_paj
with charachange


li "そんなの慰めになりません"



hi "分かったよ。水くんでくるから。華子につまずかないように気を付けろよ"


hide lilly
with charaexit


"流しのほうに向かいながら、いくらかでも眠気を覚まそうと目をこする。二日酔いの誰かを介抱するなんて、あまりいい朝の過ごしかたとは言えないな。"



"コップに水を満たすのに数秒しかかからない。澄んだ水は薄いカーテン越しに差し込む細い光をきらきらと反射している。"




"リリーはベッドの脇に腰を下ろしているようだ。俺は安らかな寝息を立てる華子を踏まないように気を付けながらリリーに近寄り、彼女が伸ばした手にコップを握らせる。"



show lilly basic_weaksmile_paj_close:
    center
    ypos 1.2
with charaenter


li "ありがとうございます"


hi "どういたしまして"

stop music fadeout 12.0



"俺はリリーの隣に腰掛ける。柔らかなベッドは驚くほど深く沈み込む。"





"リリーが几帳面なしぐさでゆっくり水を飲む。沈黙が長く続き、華子の柔らかな寝息だけが聞こえる。"


show lilly basic_reminisce_paj_close
with charachange


"いくばくかの罪悪感を感じながらも、俺はリリーの顔をうかがい表情を読み取ろうとする。彼女は眉間にしわを寄せ、何か考えごとをしているようだ。"

show lilly basic_emb_paj_close
with charachange



"しばらくためらったけど、俺はついに決心してリリーを元気づけようと彼女の肩に手を置く。それに対してリリーが目に見えるほどたじろいだのは予想外だったけど。"



hi "あっ、いや、ごめん。そんなつもりじゃなくて――"

show lilly basic_sad_paj_close
with charachange


"リリーが、彼女にしては激しすぎると思える様子で素早く頭を振る。"


"そして、自分を落ち着かせるために深呼吸をして、うなだれる。"

show lilly basic_weaksmile_paj_close
with charachange


li "今の私、おかしく見えるでしょうね……"



"それを否定しようとして、すぐにそれは無意味なことだと気づく。そうは言っても、俺は彼女にもっと心を開いて欲しいんだ。"



hi "相談したいことがあるなら、何でも言ってよ"

show lilly basic_displeased_paj_close
with charachange


"自分の感情を見下げるかのように、リリーが自嘲の笑みを漏らす。"

show lilly basic_reminisce_paj_close
with charachange


li "ただ……いろいろなことがあって"

show lilly basic_sad_paj_close
with charachange


li "最近、とりわけ街から帰る時に、おかしな態度を見せてしまって、すみません。今でも少し混乱しているんです"




hi "その気持ち分かるよ、本当に"


show lilly basic_weaksmile_paj_close
with charachange


"リリーが思わせぶりな笑みをこぼしながら指の背に頬を乗せる。"


li "駄目になった２人の愚かな若者、ですね"


hi "おいおい、そんなこと言うなよ。ここを卒業したら、俺もリリーも実世界に戻るんだし"




"実世界？　俺は時々、自分の思考に驚いてしまう。外の世界と比べたときに感じる、山久と周りの町の奇妙な隔絶感に、俺はまだなじんでいないんだろう。"





"これからもなじむことはないのかもな。考えてみれば変な話だ。こんな形で社会から隔離されるのも、思ったほど悪くはない気がする。皮肉な笑みを浮かべるリリーも、俺と同じように面白さを感じているみたいだ。"





"だけど結局、リリーの顔から完全に笑みが消えてしまう。"

show lilly basic_displeased_paj_close
with charachange


li "もうすぐ私、一、二週間ほどスコットランドに戻るんです"


hi "だから華子の誕生パーティーの日を変更したのか？"


"リリーがそれを認めるようにうなずく。"


hi "でも、少なくとも家族と再会できるんだし。楽しみじゃないの？"

show lilly basic_concerned_paj_close
with charachange


li "家族とは６年間会っていません。もう、どう接していいのかさえ分からないんです"


"ちょっと待った……何だって？　俺は口をぽかんと開けたままリリーの言ったことを理解しようとする。"

play music music_moonlight fadein 6.0



"リリーが今１８歳なら、つまり両親と離ればなれになったときはまだ１２歳ってことだ。俺だって共働きの両親と過ごす時間はそんなに多くなかった、でもリリーのは……"



"気の利いた返事を見つけようとしながら、俺は途方もない無力感に襲われる。"



hi "それって……でも、何で？"

show lilly basic_reminisce_paj_close
with charachange


li "なぜ家族が日本を去ったのか、それとも、なぜ今になって姉さんと私が呼ばれるのか、ですか？"


hi "たぶん、両方"

show lilly basic_sleepy_paj_close
with charachange


li "父が勤める会社は本社がスコットランドにあるんです。父が取締役になったので、最終的にそこに永住しなければならなくなりました"


li "母は父に付いて行きましたが、姉さんは父の会社の日本支社に勤めるために、そして私は教育のために、日本に残ることになりました"

show lilly basic_concerned_paj_close
with charachange


li "もう一つの質問ですが……おばが危篤になってしまって"


hi "えっ。それは……お気の毒に"

show lilly basic_weaksmile_paj_close
with charachange


li "いえ。なんだかおかしな気持ちです。私たちはおばのために呼ばれたのですが、ほとんど会ったことがないので。声さえも覚えていません"



"いや、おかしいのはそれだけじゃない。リリーはこんな仕打ちをする家族に対して何の反感も示さない。俺はなんだか恐縮してしまう。"




"とはいえ、物思いに沈むリリーは自分の感情を押し殺しているだけだ。こんなリリーを見るのはつらい。"


stop music fadeout 5.0


"俺は何をすべきか思いつき、ベッドから立ち上がる。リリーがベッドの動きに気づき、はっと頭を上げながら俺を確認するために自分の横へと手を伸ばす。"

show lilly basic_oops_paj_close
with charachange


li "久夫さん……？"

play sound sfx_rustling


"俺は今も壁にもたれかかっている自分のかばんに歩み寄る。かばんの前面を上にめくると、中から半透明の袋を取り出し、そして小さな飾り気のない箱を手に取る。"


hi "手を出して、リリー"

show lilly basic_surprised_paj_close
with charachange



"彼女はしばらく驚いた表情を見せるけど、やがて俺の言う通りにする。"


show lilly basic_surprised_paj_close:
    ease 1.0 xpos 0.4
show bg school_dormlilly:
    center
    ease 1.0 xpos 0.4
with Pause (1.0)

show musicbox closed behind lilly:
    alpha 0.0  zoom 0.5  xanchor 0.0 xpos 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.6 alpha 1.0
show boxstrip behind lilly:
    alpha 0.0  zoom 0.5  xanchor 1.0 xpos 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.6 alpha 1.0
with Pause (1.0)




"リリーの手のひらにオルゴールを置くと、物珍しそうな表情になるのが面白い。いつもの繊細な手つきで触れるのを見ていると、それがまるで息を吹きかけるだけで壊れるような華奢なもののように思えてくる。"



stop music fadeout 2.0



"リリーが無言のままオルゴールを顔の前まで持っていき、その外形とつくりを細い指で感じ取る。"



"そしてついにリリーの指が箱の本体とふたの境目を見つける。彼女の親指によって、ふたは何の苦労もなく開く。"

show musicbox open:
    xpos 0.5 ypos 0.6 alpha 1.0
with charachange

play music music_musicbox


"俺はベッド上のリリーの隣に座り、静かに、真剣に、彼女の顔を見つめる。"


"ちっぽけな金属音の旋律に耳を傾けるあいだ、リリーはぴくりともせず座り続ける。ただ、彼女の口がほんの少しだけ開いている。"


show musicbox closed
show lilly basic_smileclosed_paj_close:
    xpos 0.4
with charachange

play sound sfx_switch
stop music

show musicbox closed:
    ease 1.0 ypos 0.7 alpha 0.0
show boxstrip:
    ease 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

show lilly basic_smileclosed_paj_close:
    ease 1.0 xpos 0.5
show bg school_dormlilly:
    ease 1.0 center
with Pause (1.0)

hide musicbox
hide boxstrip


"長い時間が過ぎた後、リリーは小さな音をたてて箱のふたを閉じる。彼女の手の中の小さな演奏会に幕が下ろされる瞬間。"


"その優しく哀愁に満ちた笑顔は、俺が正しい決断をしたことの表れだ。"


hi "スコットランドへの旅の餞別だと思ってくれ"


show lilly basic_smile_paj_close:
    xpos 0.5
with charachange


li "ええ……"

play sound sfx_rustling

show lilly basic_smile_paj_close:
    twoleft
    ypos 1.2
show bg school_dormlilly at bgleft
with charamove


"その時、俺とリリーの前の床でがさがさとせわしない音がする。華子が目を覚ます音だ。"


show hanagown distant:
    tworight
    ypos 1.3
    easein 1.0 ypos 1.1
with Dissolve(1.0)


"華子は昨日俺がかけた毛布からはい出すと、ぼーっと前を見つめ、眠気を払うために目をこする。"


hi "やっと起きたな"

show hanagown normal:
    ypos 1.1
with charachange


ha "うぅん？　何？"

show lilly basic_planned_paj_close
with charachange



"華子が半分目を閉じたまま部屋の中を見回す。体は起きても頭の中はまだ寝ているようだ。そんな華子の寝ぼけ姿を見て、俺とリリーはくすくすと笑う。"


show lilly basic_planned_paj_close:
    ease 1.0 twoleft
with Pause(1.0)

show lilly basic_planned_paj at twoleft
with charadistant


"リリーがベッドから立ち上がって華子をいたわる。俺は最後にもう一度部屋の中を見回す。"


hi "じゃあ、俺はもう出てった方がいいな。女子寮からの朝帰りなんて、誰かに見られたら質問攻めにあっちゃうだろうし"

show lilly basic_smile_paj
with charachange


li "さようなら、久夫さん"

show hanagown smile
with charachange


ha "あの……さようなら"


"俺は立ち上がって少し軽くなったかばんを手に取ると、ドアに向かって歩き出す。"

scene bg school_girlsdormhall
with locationchange



"だけど部屋から廊下に出た時、背後からリリーの足音が聞こえてくる。"



hi "ん？　どうした？"

show lilly basic_smileclosed_paj_close:
    yalign 1.0 xpos 0.3 xanchor 0.5
    easein 1.0 xpos 0.5
with Dissolve(1.0)


"何も言わず、リリーは俺のほうに体を伸ばす。彼女の手を自分の頬に感じ、俺の体が固まる。それは、俺の頬の全神経が彼女の指と手のひらを捉えているかのような感覚。"

play music music_romance


"その直後、リリーの顔が俺の顔に近づく。軽く、ほんのひと時だけ、彼女の唇が俺のもう一方の頬に触れる。"



"しばらくのあいだ、時が止まる。俺はぼんやりとしながら、そのはかない感覚を取り戻そうとするかのように頬に手を当てる。"


hi "リリー……"

show lilly basic_smile_paj_close at center
with charachange


li "私からのお礼です、久夫さん"


hi "お礼……？"

show lilly basic_cheerful_paj_close
with charachange


li "プレゼントの。よい一日を"

show lilly basic_cheerful_paj_close:
    easeout 1.0 xpos 0.3 alpha 0.0
with Pause(1.0)

hide lilly
with None


"そう言い残して、リリーがドアの向こうに消え、ドアが優しく閉じられる。彼女と華子のくぐもった声が昨日の夜と同じ調子で聞こえてくる。"


"……"


"……こんなことを経験した日が、いい日にならないわけないじゃないか。"

show bg school_courtyard
with locationskip



"俺は軽やかな足取りでその場を去る。女子寮から出てくる俺をちらりと見た人が何人かいた気がするけど、そんなもの気にするほうが難しい。"


stop music fadeout 2.0

scene black
with dissolve



label jp_L6i:

scene black
with None


mi "ひっちゃ～ん"


hi "あっちいけよ"


mi "ひっちゃ～ん"


hi "ほっといてくれ"


mi "ちょっと、ひっちゃんてば～"


hi "だから、寝かせといてくれってのに"


"二晩の不眠を経た後の俺が最も嫌うことといえば、こうしてようやく眠りにつこうとしている時に誰かに叩き起こされることだ。"


"たぶん今は最後の授業中だろう。教科書を枕にしているけど、今となっては眠れるならどんな睡眠だってかまわない。"


mi "ほら、ひっちゃん。しっちゃんだって起きてほしいんだってさ～！"


"静音のことなんかどうでもいいよ。ほっといてくれ。"


mi "もう、ひっちゃんってば、じゃあ、強引に起こさないと……"


"ん、待て、ミーシャが何か……？"


mi "……ね……"


"ヤバい！"

play music music_running

scene bg school_scienceroom
show misha hips_grin_close at center
with vpunch


hi "起きた！　起きた！　起こさなく……ても……"


"自分の顔が真っ赤に上気しているのがはっきりと分かる。"


"授業中の周りの生徒たちは今でも背筋をぴんと伸ばしたまま席に座り、ついさっきまで寝ていた騒がしいバカをじろりと見ている。"


hi "……くそっ"

play sound sfx_impact2
with vpunch


"俺は頭を振り降ろし、ごつんと音をたてながら机に額を打ちつける。"

show misha cross_laugh_close
with charachange


mi "わははははは～！"


"ミーシャのトレードマークである抑制不能な笑い声が教室中に響き渡る。"

show shizu invis behind misha:
    center
    xpos 0.95
with None

show misha hips_grin_close at twoleft
show shizu adjust_happy at tworight
show bg school_scienceroom at bgleft
with dissolvecharamove


"ミーシャのそばにいる眼鏡姿の静音に悲しみの目を向けると、彼女は眼鏡の位置をくいっと直し、必死になって俺への真剣な非難の表情を保とうとしている。"


"よく見ると、顔のニヤつきは隠し切れていない様子だ。"


hi "静音よ、お前もか？"

show shizu behind_blank
with Dissolve(0.3)


"静音はこらえきれなくなった様子で腕を固く組むと素早くそっぽを向く。"

show misha cross_laugh_close
with charachange


mi "わはははははは～！"


"ミーシャが静音をちらりと見て二倍の音量で笑う。俺はあきらめの表情で頭を垂れることしかできない。"


hi "２人とも……"

show misha sign_smile_close
with charachange


mi "授業中に寝てたの誰だっけ、ひっちゃ～ん？"


hi "はいはい、俺ですよ"

show misha hips_frown_close
with charachange


mi "かわいそうなしっちゃんはひっちゃんを起こそうと骨折ってたんだから。ねえ？"

show shizu basic_angry
with charachange


"俺は冷淡な表情の静音に目を戻す。静音は腕を組んで、追い打ちをかけるようにふんっと鼻を鳴らして再びそっぽを向く。"


hi "なんで静音が俺を起こそうとするんだよ？"

show misha hips_smile_close
with charachange


mi "しっちゃんは、ひっちゃんが寝てるあいだに代理の先生が配ったプリントを渡したかったのよ"


hi "プリント？"

play sound sfx_paper
show shizu behind_frown_close
show misha hips_frown_close
show blanknote at truecenter
with vpunch


"その時突然、俺の目の前にプリントが二枚突き出される。"

show blanknote at Transform(xpos=0.3)
with charamove


"プリントを持つ手に沿って視線を這わせると、俺をぎろりと見下ろすふくれっ面の人物の姿がそこにある。この状況は非常にまずい気がする。"


hi "……へえ。ええと、悪かったよ"

stop music fadeout 8.0


"ダメか。静音はまだいらついた表情をしている。俺は両手を合わせると頭を下に振って謝罪する。"


hi "本当に、本当に、すみませんでした"

show shizu behind_frustrated_close
with charachange

show blanknote:
    easeout 0.5 ypos 0.8 alpha 0.0
with Pause(0.5)

hide blanknote
with None


"静音は立腹したまま、ただプリントを俺の机の上に落とす。"


hi "くそっ"

show shizu adjust_angry_close
show misha sign_smile_close
with charachange



"俺は自分の手の向こう側で狂ったように手話を交わしている静音とミーシャを見上げる。静音は相当いらついているようだ。"


show shizu basic_angry_close
with charachange


shi "……！"


"会話というよりは糾弾演説の様相で、時々それを中断して横目で俺を見る。その様子は見ていて冷や冷やするどころじゃない。"



hi "ええと……"

show shizu behind_frown_close
show misha hips_frown_close
with Dissolve(0.3)


"２人が突然手話を中断して、一斉に全く同じ非難の表情を俺に向ける。ミーシャが突然、流れるような動きで俺の頭上に手を振り上げ、それを閃光の如く振り降ろす。"

scene black
with None

play sound sfx_impact2
play music music_running


"反応する暇もなく、俺の頭がびっくり箱人形のように上下に振れる。" with vpunch



"俺は痛みを感じるよりも早く、反射的に手を頭に当てる。"


hi "いてっ！　何すんだよ！？"

scene bg school_scienceroom at bgleft
show shizu adjust_smug_close at tworight
show misha hips_grin_close at twoleft
with openeye


"俺が目を開けると、静音とミーシャがニヤニヤしながらお互いにぐっと親指を突き立てている。"

show misha hips_smile_close
show shizu behind_smile_close
with charachange


mi "しっちゃんが許してあげるって言ってるよ、ひっちゃん～！"


hi "次はもうちょっと非暴力的に許してくれないか？"

show misha cross_laugh_close
with charachange


mi "わはははは～！"



"俺は呆然としながら２人を見る。ミーシャと静音：１点、久夫：０点。"



show shizu adjust_happy_close
with charachange


shi "……"

show misha hips_grin_close
with charachange



mi "あっ、しっちゃんが郵便受けももっとチェックしてって言ってるよ～！"


show letter_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"明るい黄色の封筒を取り出して、はち切れんばかりの笑顔とともに俺に渡す。"




"変だな。俺に手紙なんて、誰が書いたんだ？　でもそれを確認するのにこのタイミングと、何よりこの場はふさわしくない。"


show letter_insert:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide letter_insert
with None



"無残にも奪い去られた居眠りの時間をあきらめ、俺は額をこすりながらゆっくりと立ち上がる。プリントと封筒をかばんに入れて、肩にかける。"


show misha cross_laugh at Transform(yalign=1.0, xanchor=0.5, xpos=0.355)
show shizu behind_smile at Transform(yalign=1.0, xanchor=0.5, xpos=0.615)
with charadistant


"そのまま一歩下がり、軽く会釈しながらその場を離れる。ミーシャは腰に手を当てて笑い続け、静音は俺に会釈を返してそっけなく別れを告げる。"

stop music fadeout 3.0
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_hallway3
show crowd
with locationchange


"開かれたドアから出ていく生徒たちの波に交じって、俺は廊下に出るために角を曲がる。"

$ renpy.music.set_volume(0.7, 0.5, channel="ambient")

show hanako emb_downtimid at center
with charaenter


"……そこで華子と鉢合わせになる。"


hi "わっ。ええと、よう華子"

show hanako emb_timid
with charachange


ha "こんにちは……久夫くん"


show hanako emb_downtimid
with charachange


"忙しくおしゃべりする生徒たちが通り過ぎる中、俺と華子の間には沈黙の空気が流れる。華子は絶えずもじもじしながら、地味な自分の上履きに目を落としている。"





"俺は状況をはっきりさせようと、鼻筋を押さえながら目をぱちぱちさせる。ただでさえ眠くて仕方ないのに。"



hi "何か用があるんだろ、華子。何だ？"

show hanako emb_blushing
with charachange


ha "え、えっと……これを……渡したくて……"


hi "ん？"

show hanako basic_worry
with charachange



"華子が小さな四角い紙を俺に差し出す。俺はもう一度まばたきをしながら、そこに書かれている内容をゆっくりと読み取る。"


window hide



$ written_note("卵×２\nパン×１\n全粒粉シリアル×１\nタイム×１\n")


window show

play music music_happiness fadein 0.5


hi "……買い物リスト？"



"俺はびっくりして上を向く。"


show hanako emb_timid
with charachange



ha "いつもリリーと一緒に行くんだけど、行けないから、それで……"



hi "俺にお使いを頼みたいのか？"

show hanako defarms_shock
with charachange



ha "い、嫌ならいいの！　ただ私、たぶん、えっと……"



"華子がパニックに陥る。俺はため息をつく。また負けか。今回は不戦敗だけど。"


"俺はやれやれと笑いながら華子の頭にぽんと手を乗せ、彼女を落ち着かせる。"


hi "いいよ。俺も行こうと思ってたんだ。ここに書いてあるものだけでいいのか？"

show hanako def_worry
with charachange



"華子はうなずくと、今度は深くおじぎをする。それも二回、感謝の意をはっきりと示すかのように。"


show hanako cover_distant
with charachange



ha "こ、校門の外で６時に会う予定だったの……ありがとう、自分で買いに行くつもりだったんだけど、明日のテストのために勉強しなきゃいけないから"



hi "テスト？　ああそうだ、科学か。勉強の調子はどうだ？"

show hanako cover_bashful
with charachange


"華子の表情がほんの少しだけ明るくなる。"

show hanako basic_bashful
with charachange


ha "前よりも……たくさん勉強してるから。たぶん……大丈夫です"


hi "そうか、がんばってるな"

show hanako basic_smile
with charachange


"華子も笑い始める。俺のよりもはるかに心のこもった笑顔だ。"



"俺にはこれ以上テスト勉強をしなくても大丈夫だという完璧な自信がある。だけど、華子が図書室で読書に没頭する代わりにテストのための努力をしているという事実を知って、胸が熱くなる。"



hi "買ってきたら夜にでも部屋に持っていくよ。じゃあな"

stop music fadeout 3.0
$ renpy.music.set_volume(1.0, 3.0, channel="ambient")

hide hanako
with charaexit


"俺は軽く手を振って華子と別れる。"


"リリーに会う前に、宿題をやっとこう。時間までにはできるはずだ。"

stop ambient fadeout 1.0

scene bg school_gate_ss
with shorttimeskip

play music music_soothing fadein 2.0


"やたら難解な数学の問題と格闘していて、リリーと会うことになっている時間を少し過ぎてしまう。"


"ほんの数分だけど、俺を慌てさせるのに十分な遅刻だ。俺は校庭へと飛び出し、校門を出る。"

scene bg school_road_ss
with locationchange


"そこで右に曲がり、坂の下にある小さな町へと向かう。他の生徒が何人かバス停に向かって逆方向に歩いていく。"




"俺は右手をポケットに突っ込み、夕暮れのオレンジ色の光の中を歩いていく。"


"ありがたいことに、うだるような夏の暑さは和らぎ始めていて、涼しいそよ風が吹き抜けている。"

show lilly back_listen_ss at center
show lillyprop back_cane_ss at center
with charaenter


"手を頭上に高くかざした時、俺は右手に杖を持つ見慣れた人物の姿を捉える。"


hi "あ、リリー"

show lilly cane_listen_ss
hide lillyprop
with charachange


"リリーが立ち止まり、後ろを振り返る。彼女は頭をわずかに振りながら、声の正確な位置を探り当てようとしている。"


hi "やあ、俺だよ"


"俺はすばやくリリーに追いつくと、彼女の横に並ぶ。そして彼女のゆっくりとしたペースに合わせるようにして再び一緒に歩き始める。"

show lilly cane_smile_ss
with charachange


li "ごきげんよう、久夫さん"


hi "こんちは"

scene bg misc_sky_ss at Fullpan(10.0, dir="right")
with locationchange


"俺は空を見上げる。"


"オレンジのはっきりとした色合いが雲に映え、歩道をもその光で満たす。木々の作り出す長い影が下り坂の道路へと伸びる。"

scene bg school_road_ss
show lilly cane_smileclosed_ss
with charachange


li "それで久夫さん、どうしたんですか？"


hi "下まで行って買い物しようと思ってさ。華子が俺を使いに出したんだ"


show lilly cane_surprised_ss
with charachange


li "華ちゃんが、ですか？"


hi "ああ、明日のテスト勉強があるからって。俺も行こうと思ってたから、華子のもついでに買ってくるつもり"


"リリーももちろん俺の手を借りられるよ、とは言わなかったけど、２人とも暗黙の了解としてそれが分かっている。"


show lilly cane_weaksmile_ss
with charachange


li "華ちゃんが勉強していると聞いて、嬉しいですよ"


hi "華子が俺にお使いを頼んだ時、俺も同じこと思ったよ"

hide lilly
with charaexit


"俺とリリーは坂を下り続ける。道すがら、聞き慣れたリリーの杖の音が周りにこだまする。時々通り過ぎる車の音や枝葉のざわめきを除けば、至福にも感じられる静けさだ。"


"ああ、俺はようやく今日最初の安らぎを得ることができる。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene evbg lilly_sunsetwalk:
    truecenter subpixel True zoom 0.9
    acdc_warp 20.0 zoom 1.0
show evfg lilly_sunsetwalk:
    truecenter subpixel True zoom 0.85
    acdc_warp 20.0 zoom 1.0
with locationskip


"俺はリリーのほうを見る。"



"その透き通った表情からは落ち着いた自信あふれる空気が決して失われないように思える。彼女の人柄についてもたぶん同じことが言えるだろう。"




"リリーは正面に伸びる道路を向いたまま、静かに歩き続ける。俺は目を上げて、顔に当たるひんやりとした空気を味わう。"




"ついこの間に人生の転機を迎えて以来、こんなに心安まる気持ちになった瞬間はたぶんないだろう。"




"その瞬間が、買い物に行く途中なんて。おかしな人生だよな。"


$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_road_ss
with locationskip


"ポケットの中でくしゃくしゃになったメモ書きが手に当たるのを感じ、俺は内容を確認するためにそれを取り出す。"



hi "ええと、なになに……卵、パン、シリアル、タイム、レタス、薄切りハム……"


show lilly cane_weaksmile_ss
with charaenter


li "なんだか久夫さんの買い物のついでにしては量が多いようですね"


hi "ああ。あの子、どんだけ食ってるんだ？"


"そう言って、突然我に返る。そうだ、すぐそばに人がいるんだった。"


hi "い、いや、つまりその……"

show lilly cane_giggle_ss
with charachange


"リリーが心底おかしそうに笑う。"

show lilly cane_planned_ss
with charachange


li "あらあら、久夫さんったら"



"忍び笑いが言葉に混じる。でもリリーはその笑いを抑えようとはしない。"



show lilly cane_satisfied_ss
with charachange



li "今日の久夫さんは、ずいぶんはっきりと言いますね？"



hi "ああ、まいったな。でもさ、やっぱり多いよ"

show lilly cane_smileclosed_ss
with charachange


li "普段は私と華ちゃんで一緒に買い物に行くので、華ちゃんが何を買うのか知っています。毎週同じものですよ"


hi "へえ。華子は料理うまいの？"

show lilly cane_weaksmile_ss
with charachange


"リリーが苦笑する。"


li "だいたいは私が作ることになります。姉さんのためにお料理をしていたので、華ちゃんのために作るのも問題はありません"


hi "リリーが料理を？　でも……"

show lilly cane_cheerful_ss
with charachange



"愉快そうな、陽気なハミングが俺の横から聞こえてくる。俺の言葉をしょっちゅう面白がってくれているのは、純粋にそうなのか、それとも彼女の目が見えないことに触れる俺を気遣っているだけなのか？"


show lilly cane_smileclosed_ss
with charachange



li "コツがあるんです。見えないために作るのが難しいお料理も確かにありますが、ほとんどはほんの少し余計に時間がかかるだけですよ。例えば、指はとても便利な計量器具として使えますし"




"それは分かるけど、でも自分を傷つけないよう相当気をつけなきゃいけないはずだ。晃さんは働き、両親もいない間、リリーは何年も１人で料理を作ってきたみたいだ。何回くらいそんなことが起きただろうと思う。"




"会話はそこで途切れてしまう。"



"華子といるときの気まずい沈黙と比べると、リリーは自分の考えていることを話し、言うべきことがない時には沈黙を守ることに満足しているみたいだ。"




"足元の滑らかな道路はオレンジ色の光で照らされ、ときおり落ちている葉っぱが踏み歩く俺の下でぱりぱりと音を立てる。また睡眠不足に苛まれて、俺は大あくびを漏らす。"


show lilly cane_smile_ss
with charachange



li "昨日の夜はよく眠れなかったんですか？"



hi "二晩全然寝れなかったよ。たぶん不眠症だな"

stop music fadeout 8.0

show lilly cane_oops_ss
with charachange



"リリーが急に心配そうな顔をする。誰かが心配してくれるのは純粋に嬉しいけど、リリーが俺の健康を心配する時はいつも俺に落ち度があるような気がする。"




li "不眠症なんですか？　ナースさんに診てもらわないんですか？"




hi "いや、必要ないって。前にも何度かこういうことがあったしさ。薬のせいで時々眠れなくなるんだ"


show lilly cane_concerned_ss
with charachange



li "……ああ。あの……すみません"



hi "おいおい、リリーのせいじゃないだろ。少なくとも今夜は不眠の心配はなさそうだし"

show lilly cane_sleepy_ss
with charachange


li "時々、久夫さんのことが心配になります"


hi "俺のことが……心配？"



"俺は手を回して首の後ろをかく。これははっきりさせといたほうがいいな。"



hi "なあ、リリー……"

show lilly cane_smile_ss
with charachange


li "はい？"


hi "変なこと言うようだけどさ……俺の心臓のことは忘れてくれないかな"

show lilly cane_oops_ss
with charachange


"リリーが困惑した様子を見せる。無理もない。"


hi "つまり、何が言いたいかっていうと……そのことで俺を特別扱いしないでほしいんだ"

show lilly cane_emb_ss
with charachange


"リリーがほんの少し首をかしげる。彼女の白い頬が、ほとんど気づかないぐらいほのかに赤く染まる。"


li "でも、久夫さんの身の周りのことを心配するのは自然なことですよ……"


hi "いや、まあ、俺を気遣ってくれる人がいるんだって分かるのは嬉しいけどさ"

show lilly cane_smileclosed_ss
with charachange



"こんなことを言うのはちょっと恥ずかしいけど、でも本心だ。リリーは冷静さを取り戻すためにひと呼吸置いて、優しく微笑む。頬は今も染まったままだけど。"



"店への最後の下り坂を、沈黙を保ちながら歩く。"

scene bg suburb_konbiniint
with shorttimeskip

play music music_daily fadein 4.0


"女性店員" "いらっしゃいませ！"


hi "まず俺が買うものを取って、それから華子のものを探そうかな"

show lilly cane_smileclosed at center
with charaenter



"入口そばの買い物かご置き場から使いこまれた赤いかごを二つ取ると、その一つをリリーに渡す。"


show lilly cane_smileclosed at Transform(ypos=800)
with charamove

show lilly basic_smileclosed at Transform(ypos=800)
with charachange

show lilly basic_smileclosed at center
with charamove


"リリーはこの前と同じように買い物かごを床に置き、縮めた杖を取っ手の間に滑り込ませてから、再びかごを右手で持ち上げる。"

$ renpy.music.set_volume(0.5, 0.5, channel="music")

show lilly basic_smileclosed at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with None

show lilly basic_smileclosed_close at Slide(0.5,0.5,0.3,0.5,1.0, time_warp=_ease_time_warp)
with Dissolve(1.0)



"リリーが俺の腕に自分の腕を添える。短い間にこんなにも自然に触れあえるようになるなんて、自分でも驚きだ。必要に迫られたからだろうな、きっと。"


show lilly basic_smile_close at twoleft
with charachange


li "行きましょうか？"

$ renpy.music.set_volume(1.0, 2.0, channel="music")


hi "そうだな"


"俺とリリーが店内を見て回るあいだ、たまにそばを通り過ぎる人は俺たちを全く気に留めない。俺たちをじろじろ見てひそひそ話をする街の人々とは大違いだ。"



show lilly basic_smileclosed_close
with charachange



"売り場の通路を順に通りながら、俺はリリーが必要なものを彼女に素早く確認し、それを俺の欲しいものと一緒に取ってそれぞれのかごに入れる。"




"買い物みたいな、すごく簡単なことでこんなにも頼られるなんて、おかしな気分だ。やっぱり、リリーが必要なものを選び出すには華子がいないとまず無理なんだろう。"




hi "よし、俺と華子の買い物、両方とも終わったよ。リリーは他に何か欲しいものある？"


show lilly basic_smile_close
with charachange



li "いえ、これで全部です"



hi "じゃあ、行くか"




"おかしなことに、レジの前には長い列ができている。店の大きさからレジが一カ所しかないことを考えると、これはしばらく時間がかかりそうだ。"




hi "ちぇっ"

show lilly basic_surprised_close
with charachange


"俺の不満の原因を見ることができないリリーが、それを知りたそうな面持ちでこちらを見る。"


hi "レジ待ちがいっぱいいるよ。けっこう待たなきゃいけないみたいだな"

show lilly basic_weaksmile_close
with charachange


li "おかしなこともあるものですね"


"俺とリリーはあきらめの心境で、しぶしぶ列の一番後ろに並ぶ。"

$ renpy.music.set_volume(0.5, 10.0, channel="music")


"１人終わり、列が動く。もう１人終わり、また列が動く。"


"俺とリリーが列の先頭に来るころには、俺はほとんど眠りこけてしまう。リリーが俺の背中を優しく叩き、動くよう俺に促す。"

show lilly basic_oops_close
with charachange


li "久夫さん……久夫さん！"

$ renpy.music.set_volume(1.0, 0.3, channel="music")


hi "ん？　ああ、ごめん"

show lilly basic_displeased_close
with charachange


"俺が動くと、リリーがはっと息をのむ。俺は華子と自分の物をそれぞれ別の袋に分ける。"


"女性店員" "ありがとうございました、またお越しくださいませ！"

stop music fadeout 5.0

scene bg suburb_konbiniext_ni
show lilly basic_smileclosed_ni
with locationskip


"店から出るころには、リリーは買い物袋を１袋持ち、俺は両手を完全にふさぐ４袋と格闘している。持ち歩くのは大変だけど、ありがたいことに中身はそんなに重くない。"



"買い物に長い時間がかかったことは空を見上げるまでもなく明らかだ。道路は暗闇に包まれ、街灯がそれを照らしている。"

show lilly cane_smile_ni
with charachange


"リリーが杖を元の長さに伸ばすと、俺たちは誘い込むような光を放つ店を背に、来た道を寮に向かって引き返す。"

scene bg school_road_ni
with locationskip

play music music_dreamy fadein 8.0


"車は全く通らないけど、こすれ合ってガサガサ鳴り続ける俺の買い物袋がその静けさを派手に打ち破る。"

show lilly cane_ara_ni
with charaenter


li "あらあら、久夫さんがたくさん食べていると分かって嬉しいですよ"


hi "俺だって育ち盛りだし、食えるものはなんでも食わなきゃ！"

show lilly cane_weaksmile_ni
with charachange


li "ふぅん……男の人になれたら、素敵でしょうね"


hi "な、何だって？"



"思いがけない言葉にすっとんきょうな声を上げて驚く俺に気づいていないのか、それとも無視しているのか、リリーが調子を変えずに言葉を継ぐ。"


show lilly cane_smile_ni
with charachange


li "だって、食べている時でも体重をほとんど気にしなくていいですし"


hi "ああ、そういうことか。まあ、女性は俺たち男よりもそういうこと気にするみたいだな"

show lilly cane_smileclosed_ni
with charachange



li "そうですよ。正直言って、少しうらやましいです"



hi "いや、俺たちだって体重のこと全く無視できるってわけじゃないよ"


"リリーが同意するようにうなずき、俺たちは歩き続ける。"



hi "ああ、そうだ"


show lilly cane_smile_ni
with charachange


li "何ですか？"



hi "華子が、リリーの誕生日は年の初めだって言ってたな。なにか特別なことはやった？"


show lilly cane_listen_ni
with charachange


"リリーが黙り込み、しばらくその出来事を思い返している。"

show lilly cane_weaksmile_ni
with charachange


li "いいえ、特には。夜に華ちゃんと私で小さなパーティーをしたくらいです"


hi "でも、リリーの誕生日って大イベントじゃないか"


"華子と２人っきりで夜を過ごすなんて、誕生日の過ごし方としてはとても寂しく聞こえる。"


"俺にとって誕生日は、家族との触れ合いの機会だ。２人とも働いているにもかかわらず、両親は誕生日には俺と一緒に過ごそうと努力してくれたし、それができなくても、少なくとも事前にパーティーは開いてくれた。"


"そこまで考えて、リリーが長いあいだ家族と会っていないと言っていたことを思い出す。彼女はその後も晃さんとさえ別れて暮らさなければならなくなったんだ。"



"でも、買い物みたいなありふれた状況にも同じことが言えるんじゃないか。外装に書かれていることを読めないリリーにとって、単なる買い物だけでも誰かの手助けなしでは大変だろう。"



"結局、今のリリーには華子と俺、そして仕事をしていない時の晃さんしかいないんだ。"


"そうは言っても、リリーには俺たち以外にも普通の友達がたくさんいるように見える。優子さんみたいな人たちは言わずもがなだ。"


"親密な付き合いをする人と表面的な付き合いをするだけの人、リリーはそれを彼女自身で選り分けて区別しているようだ。"


"自分の人生をしっかりと保ち、自分の意思を持って生きているように見えるリリーに、俺は少し気後れしてしまう。"



"それでも、華子はリリーと誕生日を一緒に祝い、俺はこうしてリリーの買い物を手伝っている。おかしな共生関係、なんだろうな。"


show lilly cane_oops_ni
with charachange


li "久夫さん、大丈夫ですか？"


hi "えっ、何で？"



li "いえ、ただ、久夫さんがとても静かに思えたので"


hi "ああ、ごめん。考えごとしてたんだ"

show lilly cane_smileclosed_ni
with charachange


li "あら？"


label jp_choiceL6_1:
menu:
    with menueffect
    "やれやれ、リリーの好奇心を刺激しちまった。個人的な考えすぎて話すのは気が引けるけど……"
    "話をはぐらかす":




        return m1
    "正直に話す":


        return m2


label jp_L6a:



hi "最近起こったことを考えてただけだよ。心配すんなって"

stop music fadeout 2.0

show lilly cane_listen_close_ni
with characlose


li "ふぅん？"


"リリーが体を近づけて俺を深く覗き込み、俺は思わず体をそらす。"


hi "おいおい、リリーだってそういうことあるだろ？"

show lilly cane_cheerful_close_ni
with charadistant


li "だって、まるで私に何か隠しているように聞こえるから……"

play music music_lilly fadein 4.0


"うっ。なんでこの子はこんなに鋭いんだ？"


"だけど、リリーの顔にはふざけているようなかわいい笑顔が浮かんでいる。"



"リリーが……俺をからかってる？　もしそうであっても、これ以上は話したくない。"



hi "言っただろ、何でもないよ"

show lilly cane_displeased_close_ni
with charachange


"リリーが納得いかない様子で眉をひそめる。"



li "そうなんですか？"



hi "そうだよ"

show lilly cane_surprised_close_ni
with charachange


li "久夫さんって、嘘が下手ですね"



hi "それは認めるけど、だから俺は嘘をついてないってことだよ。俺は信用に値する人間さ"


show lilly cane_weaksmile_close_ni
with charachange


li "ええ、そうですね。だけどまあ、今回だけは許してあげます"


hi "許す？　何を許すって？"

show lilly cane_giggle_close_ni
with charachange

with Pause(0.2)

show lilly cane_smile_ni
with charadistant


"リリーがくすくすと笑い、また静かに歩き出す。彼女は今何を考えているんだろう？"

stop music fadeout 4.0


"俺は肩を落としながら暗い空を見上げる。"


"これは自分の頭の中で整理しなければいけないことだろう。全てをリリーに頼るのはよくない。"


label jp_L6b:




hi "何ていうかさ……リリーは本当にいつも自分自身をきちんとしてるみたいだなって思って。華子にもああやって頼られているのに。俺だって、転入してきたばっかりの時はリリーに頼ってたって認めるよ"



hi "そういう性質を持ってるのって、いいことだと思う"


"俺はリリーのほうを向き、彼女の反応をうかがう。"

stop music fadeout 2.0

show lilly cane_listen_close_ni
with characlose


"リリーは眉をひそめながら無理やり前を向く。その顔には気まずい感じの表情が浮かんでいる。まるでふさわしい返答の言葉を懸命に選んでいるかのようだ。"


hi "……リリー？"

show lilly cane_weaksmile_close_ni
with charachange


li "お礼を言うべきなのでしょうが……私が他の人を必要としていないと思うのなら、買いかぶりすぎです。華ちゃんが私に頼ることに、私が何の見返りも求めていないと考えるのも間違いですよ"


"リリーが少しためらいがちに言う。その内容は、俺にとってはもうほとんど分かっていたことだけど。"




"目が見えるかどうかに関係なく、同じ立場に置かれたら誰でもそうするだろうけど、リリーがあんなに努力して自立した生活を保とうとしているのなら、自分が必要としていることを他人に話すのは難しいのかもな。"







"だけどこの時になって初めて、俺はリリーがあることに触れていないのに気づく。話が個人的な話題になり過ぎるのを避けるため、冗談半分でそれを聞いてみることにする。"



hi "そうなの？　じゃあ、俺は？"

play music music_lilly fadein 2.0

show lilly cane_smile_ni
with charadistant


"リリーが突然前方に駆け出し、俺の行く手を遮るようにして振り返る。"

show lilly behind_cheerful_ni
with charachange


"微笑みながら両手を後ろに回し、前かがみになる。"


li "久夫さんは、違いますよ"

show lilly back_giggle_ni
show lillyprop back_cane_ni
with charachange


"そう言うと、リリーはくるりと向きを変え、俺の前をとても軽やかなステップで歩き出す。"


"俺は目を見開いて呆然とした笑いを浮かべることしかできない。こんなにも無邪気でいたずらっぽい姿のリリーを今まで見たことがない。"


"じゃあ……俺は『違う』のか。それがどういう意味なのか正確にはよく分からないけど、リリーの性格からして、彼女がわざとあいまいな言葉を使ったのは間違いない。"


"俺とリリーの関係が変わってきている。少なくともそれは、俺がここで自立し始めて、以前よりももっと自分の身の回りのことに目を向け始めたからだ。"


"それはつまり……たぶん個人的な好奇心でもあり、俺の今の状況にもっとうまく馴染もうとする自分自身の願望でもあるんだろう。"


"だけど、リリーのことについてはまだよく分からない。だから、彼女が今言った言葉、俺の今の感情にとても近いそれが、俺をこんなにも煙に巻いている。"


"俺は杖を左右に打ち道を登っていくリリーを見ながら、このことについてはまた後で考えようと決め、今はただ笑うことにする。リリーの素敵な面を見ることができた。この出来事は忘れたくないな。"

stop music fadeout 2.0


label jp_L6c:


scene bg school_girlsdormhall
with shorttimeskip

play music music_normal fadein 4.0


"ついに俺とリリーは女子寮にたどり着く。二つの買い物袋の束のせいで両腕がずきずきする。"


hi "はあはあ……ようやく着いたな。ふう"

show lilly invis:
    right
    xpos 0.95
with None

show lilly cane_smileclosed at right
with dissolvecharamove


"俺は手の甲で額を拭うために前かがみになる。リリーは自室のドアの前に立ち止まると買い物袋を床に置き、ポケットの中のカギを探っている。"

show lilly cane_smile
with charachange


li "ありがとうございます、久夫さん。本当に助かりました"


hi "いや、こんなの何でもないよ"

show lilly cane_smileclosed
with charachange


li "久夫さんにとっては何でもなくても……私にとってはとても大きなことですよ"

show lilly invis:
    right
    xpos 1.05
with dissolvecharamove

play sound sfx_doorclose

hide lilly
with None


"そんな言葉を残し、リリーは閉まるドアの向こう側に消える。"


"俺は目をぱちくりさせる。ただの真摯な感謝以外の何物でもない言葉だけど、なにか別の意味があるような気がしてしょうがない。"


"とにかく今は、そんなことを考えている暇はない。俺にはまだやることがある。"

scene bg school_dormhanako_ni
show hanako emb_timid_close:
    center
    xpos 0.45
show hanako_door_base at right
show hanako_door_door at left
with locationchange

play sound sfx_doorknock2


"俺は後ろを振り返り、華子の部屋のドアを立て続けに二度ノックする。今も手に持っている買い物袋がガサガサと音を立てる。"

play sound sfx_dooropen

show hanako_door_door:
    xpos -0.05
with charamove


"数秒後、ドアがゆっくりと開く。よく見ていなかったら、ドアが動いたことさえ気づかないぐらいだ。"


"俺は頭を横にひねり、ドアとドア枠の間にほんの少しできた細長い隙間を覗こうとする。"


hi "やあ華子、買ってきたぞ"

show hanako basic_normal_close at Position(xpos=0.4)
with charachange


ha "ああ！"

show hanako_door_door:
    xpos -0.3
show bg school_dormhanako
with dissolvecharamove


"その声とともに、ドアが完全に開く。華子の肩越しには彼女の地味な部屋の様子がうかがえる。ほとんど飾りっ気のない、たぶん俺の部屋よりももっと平凡な部屋だ。"


"俺は右腕を差し伸ばす。持った買い物袋がその重さで俺の腕にのしかかる。"

show hanako emb_smile_close
with charachange


ha "あ、ありがとう、久夫くん"


show hanako emb_downtimid_close
with charachange



ha "ここまでずっと運ばせてしまって……ごめんなさい"



hi "いいよ、気にすんなって。でも毎日は勘弁だぞ、いいな？"

show hanako basic_normal_close
with charachange


"俺は陽気に笑いながら買い物袋を華子に渡す。ゆっくりと重みを伝えるように渡すと、華子はそれを苦もなく受け取る。"



hi "じゃあ行くよ。おやすみ、華子"

show hanako cover_bashful_close
with charachange


ha "おやすみなさい。えっと、ま、また明日……教室で……"

show hanako_door_door at left
with charamove

play sound sfx_doorclose


"華子は両手に買い物袋を持ったまま深いおじぎをし、部屋の中に下がってドアを閉める。"

stop music fadeout 5.0

scene bg school_dormext_full_ni
with locationskip



"バランスを取るため買い物袋を一つずつ両手に持ち、自分の寮へ戻る。"



"そうしているあいだも、リリーの陽気な笑顔が俺の頭から離れない。あんなリリーは、俺が最初に彼女に出会った時には想像すらできなかった。"


"確かに、俺がリリーと華子に出会ってからの数週間、俺とリリーの距離はどんどん近くなっているように思える。"


"俺が毎日リリーと過ごす時間。俺たちが共有する幸福のほんの少しの交換。リリーとの距離が縮むにつれて得られる、そんな小さな喜びの瞬間たち。"


"確信は全然ないけど、この気持ちはただの友情ってわけじゃないような気がする。"

scene bg school_dormhisao
with locationskip



"自分の部屋に戻ると俺は買ってきたものをしまい、夜に備える。"


show letter_insert:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"明日の時間割で必要な教科書とノートをかばんに入れかえている時、放課後にミーシャから受け取った黄色い封筒が出てくる。"


"次々と起こる出来事に気を取られて中身を見ることができなかった手紙だ。一体誰が書いたんだろう？"


"封筒の裏側にきれいに書かれた名前を見て、俺はその場で固まってしまう。彼女の字を見るのは本当に久しぶりだ。そうじゃなかったら、これが彼女の筆跡であることを見過ごすはずがない。"



"『岩魚子』"


"どうして……俺に手紙なんか？　彼女がそんなことをする特別な理由が俺には思いつかない。"



"開けないでおこうとするけど、それも意味のないことだ。もしこのままにしておいたら、俺が手紙に手を付けるまでの間もその存在自体が俺を悩ませ続けるだろう。"


scene ev hisao_letter_open
with shorttimeskip

play music music_rain fadein 6.0


"俺は机に広げられた便せんに目を落とす。そこに描かれた明るくて夏っぽい装飾が幸せそうに輝きを放っている。"



"ピンク色でつづられている文字は、便せんに引かれた黄色いひまわりの線とはひどく不釣り合いだ。手書きはきれいで、その一文字一文字が行き過ぎなほどの丁寧さで思慮深く書かれている。"



"この手紙が渡された時、俺はそれをほとんど気にも留めなかった。だけど今は、この手紙の内容が俺の頭から離れようとしない。"

window hide
nvl clear
nvl show dissolve


n "\n\n\n電話や電子メールの方がもっとてっとり早くて簡単だろう。岩魚子がどうして俺とのやりとりにこんな時代遅れな手段を使ったのか真意は分からないけど、その答えは手紙の内容を読めば十分明白な気もする。"


n "手紙を使えば差出人と受取人の距離を適切に保つことができる。電話と違って会話に直接加わる必要もないし、電子メールと違って迅速な返事を期待されることもない。"



n "\n『３年生になって、みんな卒業試験のことで頭がいっぱいになっています』とか『私たちがもう最高学年だっていうのが、とても変な感じだと思わない？』とかいう記述はただの世間話だ。俺が病院にいた時でも岩魚子に向けたどんな話題からも引き出せたような世間話。"




n "だけど、手紙の最後の部分、これこそ岩魚子がこの手紙を送った本当の理由だ。思い付きで書き加えられたかのような、最後の数行。"

nvl clear
nvl hide dissolve

play sound sfx_paper

scene ev hisao_letter_open_2
with locationchange

nvl show dissolve


n "\n\n\n\n\n\n\n『もう一度会うことはできるのかな。もしかしたら、会わないほうがいいのかも？』"




n "本来なら心が痛むはずの一文だ。別れっていうのは厄介なものだといつも耳にしていたけど、これはお互いがとっくに分かっていたことを再確認しているだけのように思える。"



n "世間話に過ぎない前置きの文章こそ俺が一番傷ついた部分だ。それがどうしてなのかは、どれだけ長く座って明るく夏っぽい便せんに目を落としていても分からない。"

nvl clear


n "\n\n\n\n\n\n\n\n『もし連絡を取りたいと思ったら、ぜひお返事ください』"




n "これが返事を返すようなたぐいの手紙じゃないのは明らかだ。結局、この手紙はただのやっかい払いでしかない。俺たちの関係が終わったことを岩魚子が自分自身に念押しするための最終通告なんだ。"


stop music fadeout 3.0

nvl hide dissolve
nvl clear

scene bg school_dormhisao
with locationchange

window show



"そんなわけで、俺はほとんどためらうことなくその便せんと封筒をくしゃくしゃに丸めてゴミ箱の中に投げ捨て、その存在を消し去ってしまう。"




"過去からの邪魔が入ったおかげで今日の楽しかった夜も台無しだ。複雑な思いを抱えたまま、俺はベッドにもぐり込む。"



"皮肉なことに、眠りにつくまでしばらく時間がかかってしまう。"

scene black
with dissolve

$ suppress_window_after_timeskip = True

label jp_L7:

window hide None

scene black
with dissolve

nvl show dissolve



n "\n\n\n\n汗をびっしょりかきながら、恐怖の瞬間を待つ。"

$ renpy.music.set_volume(0.7, 0.0, channel="music")
play music music_tension fadein 6.0



n "時計がカチカチとなるたびに全身の筋肉がこわばり、毎分ごとに髪の毛がどんどん逆立ってくる。"



n "それがやって来る。俺には分かる。"

play sound sfx_slide


n "\n\n{image=vfx/reddash.png}{color=#FF0000}{b}死。{/b}{/color}"


n "死がやって来る。一枚の紙という形を取って。"

$ renpy.music.set_volume(1.0, 0.5, channel="music")

nvl clear
nvl hide dissolve

scene bg school_scienceroom at bgright
with locationchange

window show


"俺は前の席の生徒から回ってくる紙の束を受け取り、そこから一番上の一枚を取って残りを後ろに回す。"



"紙の右上を見て、恐れていたものがその小さな赤丸の中で現実のものとなったことを知る。"


stop music
play sound sfx_thunder
with vpunch


"４３点。"



"俺はうなだれ、あきらめのため息を漏らす。小声で悪態をつくと、似たようなオーラが教室全体から伝わってくる。おかしなことだけど、それによってほんの少しだけ気が楽になる。"




"同病相憐れむ、ってやつか。"




"先生が口を開く。クラスの全員が避けようのない猛攻撃に身構え……"


play music music_normal fadein 1.0

play sound sfx_normalbell



"……だがしかし、土壇場で命拾いをする。"



"誰もが急いでかばんを取り、昼休みのために大慌てで教室を出て行く。だけど、先生が捨て台詞を吐くように言う。"



"教師" "この結果については次の時間に話をするからな。言わんでも分かるだろうが、話すことはたっぷりとあるぞ"



"うめくような声が教室内で一斉に漏れ、その声を残して皆が落胆したように教室を出て行く。"

scene bg school_hallway3 at bgright
with locationchange



"俺は廊下を歩きながら、紙をかばんの中にくしゃくしゃと押し込む。ただでさえ昨日は厄介な手紙を受け取るはめになったってのに、今度はこれかよ。"



hi "英語なんて嫌いだ……"

stop music fadeout 0.7


mystery "ひ――{w=0.3}さ――{w=0.3}お！"


"いかつい女性の声が俺の背後から荒々しく呼びつける。"

play music music_tension


"俺はその場で凍りつき、顔から血の気が引く。まるで俺の脳みそが体から切り離されてしまったかのようだ。"


"俺は正体不明の声の主を探ろうと、目だけをゆっくりと右に向ける。"

stop music fadeout 0.3


"……誰もいない？"


"やがて俺の顔もそちらに向き始め、そしてついに振り返る決心をする。ゆっくり、ゆっくりと、俺はそちらの方に顔を向け――"

play sound sfx_impact


hi "ぎゃあああああ！" with vpunch


"俺はあまりの驚きに声を張り上げ、かばんを落として飛び上がる。"


"やがて平静を取り戻し、振り返ると……俺も気づけていたはずなんだ。"


hi "笑美"

play music music_running

show emi excited_proud at center
with charaenter



emi "びっくりしたでしょ、久夫くん"



"いたずらっぽい笑顔でそこに立ち、手を差し伸ばして指を内側に突き出している。俺の肋骨を指で突っついたのは笑美だったんだ。"


"俺は顔をしかめ、いら立ちに髪をかきむしりながら笑美を見下ろす。"


hi "こんな挨拶ってありえないだろ"

show emi sad_pout
with charachange


emi "もぅ、ノリが悪いんだから"



hi "そんなもの、英語の授業に置いてきたよ。俺にノリを取り戻してほしいなら英語の先生に言ってくれ"

show emi sad_shy
with charachange



"笑美がぷうっと膨れながら子犬のような目で俺を見つめる。リリーのおかげでこの手に耐えられるようにはなったけど、笑美の背が小さいことも加わって、結局俺の気分は和んでしまう。"




hi "それで、調子はどうだ？　しばらく見なかったけど"

show emi basic_closedgrin
with charachange


emi "相変わらずよ。あたしの走りが速すぎちゃって、誰も朝練に付き合ってくれないし"

show emi basic_annoyed
with charachange


emi "ほんと、寂しいわよね"



"笑美のこういう謙虚なところはいつ見ても面白いな。"


show emi basic_grin
with charachange


emi "だけどさ……"



"ヤバい。"


show emi sad_shy
with charachange


emi "あたしの考えてること、分かるよね、久夫くん？"


"感情がすぐに表に現れるのは俺の一番悪い癖だ。笑美はすぐにそれを見て取る。"



"ラッキーなことに、この場を抜け出すチャンスをくれそうなある人物が近づいてくるのに気づく。"



hi "あっ、やあ、華子"

show emi sad_shy at twoleft
show bg school_hallway3 at center
with charamove

show hanako emb_downtimid at tworight
with charaenter



"笑美の膨れっ面に最大限気づかないふりをしながら、俺は華子を呼び寄せようと手を振る。華子が小さく手を振り返す。"


show hanako emb_smile
with charachange


ha "こ、こんにちは、久夫くん……笑美ちゃん"


show emi basic_closedgrin
with charachange


emi "やっ、華子"


hi "すぐ華子とリリーの所に行くから"


hi "そういやさ、笑美。昼休みの連れといえば、琳が一緒にいないのは珍しいな"

show emi basic_shock
show hanako defarms_shock
with vpunch



emi "あっ！　琳！"


stop music fadeout 3.0

hide emi
with easeoutleft



"それきり一言の挨拶もなく、笑美は俺たちのことを放り出して廊下を走り去ってしまう。琳が待っていることを忘れていたに違いない。"




"華子と俺は無言で立ち尽くす。ただ呆然と、果てしないエネルギーを持つとも思えるあの物体が走り去るのを見守るしかない。"


play music music_running

show emi basic_closedgrin at left
with easeinleft


emi "あっ、そうだ、久夫くん……"



"屋上への階段に向かう廊下の角に消える直前、笑美が突然ブレーキをかけるとくるっと振り向いて、あっけにとられている俺と華子に向き合う。"

show emi excited_proud
with charachange



emi "あたしも英語嫌いなんだ"


stop music fadeout 4.0

hide emi
with easeoutleft


"その言葉を残し、消え去る。"


"俺は完全に煙に巻かれてしまったような気持ちで、うなだれて大きなため息をつくことしかできない。"

show hanako basic_smile
with charachange



"背後からの小さなくすくす笑いを聞いて俺が振り返ると、笑美がいた場所で華子が微笑んでいる。"


play music music_daily fadein 4.0

show hanako basic_smile at center
show bg school_hallway3 at bgleft
with charamove


"俺は床に落ちている自分のかばんを拾うと、素早くほこりを払い落す。"


hi "こんちは。忙しい？"

show hanako def_worry
with charachange


ha "英語……嫌いなの？"



hi "えっ？　ああ、ええと、いや。こないだの英語のテストのことでさ。点のことでくさってたら笑美に見られちゃって"


show hanako emb_downsad
with charachange


ha "ああ、ごめんなさい……"



"きまりの悪そうな表情で華子が顔をそむける。傍から見れば、まるで彼女が俺にうっかり死んだ家族の話題を振ってしまったかのような光景だろう。"



hi "おいおい、華子のせいじゃないよ。華子はどうだった？"

show hanako emb_sad
with charachange


"華子が上目づかいで俺を見る。俺と目を合わせないようにしているけど。"

show hanako basic_worry
with charachange


ha "まあまあ……かな"


"気まずい沈黙が流れる。華子の周囲ではいつものことだ。"

show hanako basic_bashful
with charachange



ha "あっ、リリーが……屋上でお昼一緒にどう、って"




"まあ、他に取り立てて重要な用事もないか。"



hi "もちろん。すぐ行くよ"

show hanako cover_distant
with charachange


ha "えっと、私……食堂でお昼買ってくる……から"


hi "行ってきなよ。別に俺に許可取らなくてもいいんだぞ"

show hanako basic_smile
with charachange


ha "わ、分かった。行って……きます"

hide hanako
with charaexit

stop music fadeout 5.0


"華子がおどおどしながら返事をして、それから小さくうなずくと食堂のほうへと急いでいく。"

play ambient sfx_crowd_indoors fadein 2.0

show crowd:
    bgleft
    alpha 0.0
    parallel:
        ease 1.0 center
    parallel:
        linear 2.0 alpha 1.0
with None

show bg school_hallway3 at center
with dissolvecharamove


"華子は今日の昼飯を持ってこなかったんだろう。廊下を歩いていると、教室から出てくる生徒の数がどんどん増えていき、俺とすれ違いながら華子が向かったのと同じ方向へ歩いていく。"


"俺が屋上への階段へと向かうころには、忙しくおしゃべりする人だかりを押しのけないと前に進めないほどの混み具合になっている。"

stop ambient fadeout 0.5

scene bg school_staircase1
with locationchange

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_rooftop


"俺はついに最後の人ごみをかき分け、階段を上る。ほっとして少し前かがみになり、息を整えてから屋上へとつながるドアを開ける。"

play sound sfx_door_creak
$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

scene bg school_roof
show white
with locationchange


hi "うわっ、くそっ！"


"夏の強い日差しで何も見えなくなり、俺は瞬時に目を横にそらす。"

show white:
    alpha 1.0
    linear 10.0 alpha 0.0

show lilly basic_smile behind white:
    left
    ypos 1.2
show emi basic_grin behind white:
    center
    ypos 1.15
show rin basic_absent behind white:
    right
    ypos 1.17
with charaenter


mystery "ん？"

play music music_soothing fadein 8.0


"ゆっくりと視界が戻り、やがて周りにいる人物の姿がはっきりしてくる。"



"リリー、笑美、琳が屋上で一緒に座っている。学園周りの丘の頂上に茂る森が彼女たちの周りにあるフェンス越しに見える。その様子はまるで額縁のようだ。"



show emi basic_closedgrin
with charachange


emi "あっ、久夫くん！"

show lilly basic_smileclosed
show rin basic_deadpannormal
with charachange



"リリーと琳が気づいたかのように軽くうなずき、それからそれぞれが深い会釈をする。"



"どこかおかしな組み合わせの３人に向かって俺は歩き出す。そのあいだも笑美が食べかけのバナナの残りを平らげるスピードに驚愕せずにはいられない。"



hi "やあ。３人が一緒にいるの見ると、なんか変な感じだな"

show lilly basic_weaksmile
with charachange


li "今日は奇遇が重なる日のようですね。笑美ちゃんと琳さんも、私や華ちゃんと同じように屋上で昼食を取ろうとしていたので"

show emi basic_annoyed
with charachange



emi "そっちが盗ったんじゃない！　この場所はあたしたちのだったのに！"



hi "落ち着けよ。学校の場所は盗めないだろ"


"俺はリリーのそばにどさっと腰を下ろし、四人が半円の形で向き合う。"

show rin basic_deadpanupset
with charachange


rin "笑美は正しいと思うけど"


hi "琳もそう思うのか？"

show rin basic_deadpan
with charachange


rin "蝶がリリーの共犯者なんだ"


hi "ちょ……"



"俺が周りを見回すと、琳の言う通り、小さな黄色い蝶が俺の視界を横切っていく。"




hi "じゃあ聞くけどな、その蝶がどうやってリリーがこの場所を『盗む』のを助けたんだ？"


show rin basic_lucid
with charachange


rin "そいつが私たちの会話を偵察してリリーに教えたんだ"




"琳にまともな理屈を期待した俺が間違ってた。まあそれでも、もうしばらく話を合わせてやるのも悪くないだろう。"



hi "リリーは蝶と話せる、って言いたいのか？"

show rin basic_awayabsent
with charachange




rin "馬と話せる人だっているんだよ。ホースウィスパラーっていうんだ"



show rin basic_deadpanamused
with charachange




rin "リリーは蝶ウィスパラーに違いないよ"





"俺は頭を抱える一方で、笑美は琳に食ってかかる。どうやら笑美には琳のユーモアのセンスは通じないらしい。"



show emi basic_confused
with charachange




emi "ウィスパラーってのはそういうのじゃないでしょ"




"笑美と琳が冗談話に花を咲かせるあいだ、俺はリリーの方を振り返る。彼女は小さな弁当箱の中のカレーライスを食べ終えようと懸命に木の箸を動かしている。"




hi "そんなことより、リリーはどうしてここにしたの？"

show lilly basic_smile
with charachange


li "新鮮な空気を時々味わうのも悪くはないですしね"

show emi basic_shock
with charachange


emi "あーっ！"


"論理の概念を琳に教えようと無駄な努力をしていた笑美がそれを中断する。"

show emi sad_annoyed
with charachange



emi "あたしたちだって同じ理由で来たのよ！"



"どうせ笑美ひとりの考えに違いない。琳はただ笑美の気まぐれでここに引っ張って来られただけだ。だけど、それはたぶんリリーと華子にも当てはまるだろう。"

show lilly basic_weaksmile
with charachange


li "まあまあ。一緒に過ごしましょう"

$ renpy.music.set_volume(0.001, 1.0, channel="music")

play sound sfx_door_creak


show lilly basic_surprised
show emi basic_hes
show rin basic_awayabsent
with charachange



"リリーが言葉を発すると同時に、屋上のドアがきしむ音を立てて開く。皆がそこから現れる人物に注目する一瞬のあいだ、沈黙がその場を覆う。"


show lilly basic_surprised:
    xanchor 0.5 xpos 0.4
show emi basic_hes:
    xpos 0.68
show rin basic_awayabsent:
    xpos 1.08
show bg school_roof at bgright
hide white
with charamove

show hanako basic_distant:
    xanchor 1.0 xpos 0.0 yalign 1.0
    easein 3.0 xanchor 0.0 xpos -0.06
    ease 1.0 ypos 1.17
with None


"華子がゆっくりとこちらに向かって来る。目は地面に伏せたまま、注目を浴びたことを静かに悔いている。琳と目が合った時、華子がほんの少しだけこわばった様子を見せる。"


"華子がこちらに歩いて来て俺の隣に座り、ほとんど目も上げずに食堂のパンを口に運んでいるのを見て、心配な気分になってくる。"



show rin basic_absent
show emi basic_grin
show hanako basic_normal:
    xanchor 0.0 xpos -0.06 ypos 1.17
with charachange


hi "そういや、リリーと笑美はどうやって知り合ったんだ？"

$ renpy.music.set_volume(1.0, 8.0, channel="music")

show lilly basic_smileclosed
show rin basic_awayabsent
with charachange



li "笑美ちゃんの運動能力は校内でもちょっと有名ですからね。陸上部のメンバーの中でも飛び抜けて速くて、先週の競技会では三浦美貴さんにも勝ったほどですよ"




"三浦美貴って……ああ、同じクラスで前の席に座ってる日焼けした子か。彼女の身長と引き締まった体を考えたら、あの子に勝てるというのは相当すごいことだ。"

show emi excited_amused
with charachange


"笑美の方を見やると、自分でもそのことを十分承知しているようで、自慢げに笑っている。"

show emi excited_happy
with charachange


emi "でさ、久夫くん。英語のテスト何点だったの？"


"あちゃ。"

show rin basic_absent
with charachange


hi "ノーコメント"

show emi basic_annoyed
show rin basic_awayabsent
with charachange


emi "ぶぅぅ～"


"笑美が頬を膨らませてむくれるけど、あっという間に元の表情に戻る。"

show emi excited_proud
with charachange


emi "いいわ。あたしの点を教えるから、久夫くんも教える。どう？"

stop music fadeout 4.0

show rin basic_absent
with charachange


hi "分かった、分かった"

show emi basic_closedhappy
show rin basic_awayabsent
with charachange


emi "よーし、３つ数えた後で、いっせいに点を言うのよ"

show emi excited_joy
with charachange


emi "いーち……{w=1.0}　にーぃ……{w=1.0}　さん！{w=1.0}{nw}"

show emi basic_closedgrin
with charachange


$ doublespeak (hi, emi, "……", "３２点！")


"俺はいたずらっぽくにやにや笑う。"

play music music_comedy

show hanako cover_smile
show lilly basic_cheerful
show rin basic_amused
show emi excited_sad
with charachange
with vpunch
play sound sfx_impact


emi "あーっ！　ずるい！　ずるい、ずるい、ずるい、ずるい！"

show rin basic_absent
with charachange


hi "笑美が言ったんだぞ。俺じゃない。だけどさ、俺よりも低い点を取れるなんて、ちょっと驚きだな"

show emi sad_grit
show rin basic_awayabsent
with charachange


emi "がるる～！"


"笑美が姿も声も侵入者を威嚇する小型犬のようになる。今まで見た中で最も恐ろしい光景、とはとても言えないけど。"

show lilly basic_displeased
show hanako basic_normal
with charachange



li "どちらにしても、３２点よりは高得点、というのも自慢できることではありませんよ。それ以下なんてなおさらです。どんな教科であっても"


show rin basic_absent
with charachange


hi "そうだな、リリー"

show rin basic_awayabsent
show emi sad_shy
with charachange


emi "ごめんね、リリー"

show lilly basic_smile
with charachange



li "もしよければ、英語のお勉強をお手伝いしますよ。喜んでお助け――"


show emi basic_closedgrin
with charachange


emi "いい、いい、大丈夫。でも、ありがとね。ほんとに"

show lilly basic_reminisce
show hanako basic_smile
show rin basic_deadpanamused
with charachange



"リリーは自分の知識を伝授する望みを打ち砕かれて、少しがっかりしているように見える。彼女以外の全員が笑いを隠しきれずにいるのを見るに、リリーも笑美もあまり同情は得られなかったみたいだ。"


stop music fadeout 0.5
$ renpy.music.set_volume(0.0, 4.0, channel="ambient")

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show



"だけど、愉快に笑いながら座っていると、俺は胸が締め付けられ、自分の声が突然失われるのを感じる。"


window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show



"俺は数秒のあいだ静かに座り、ただひたすら心臓の鼓動に集中する。ほんの小さな痛みだけど、だんだんひどくなっていく感じがする。"


play music music_tragic fadein 0.5

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
with Dissolve (0.2)

window show



"深呼吸……深呼吸だ……"


window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show



"俺は上目づかいで、いくらかでも周囲に注意を向けるように努力する。笑美が彼女の視界の端で俺の苦悶の表情をとらえて、突然固まるのが見える。"


show emi basic_hes
with charachange


emi "ねえ、久夫くん……大丈夫？"

show hanako def_worry
show lilly basic_surprised
show rin basic_deadpanupset
with charachange


hi "ああ、大……丈夫だ……"

window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

window show


"俺は再び視線を落とし、落ち着きを取り戻そうとさらに努力を重ねる。痛みを和らげるためにこぶしを握り締める。"

window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

with Pause (0.7)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.2)

stop music fadeout 4.0

window show


"ほんの少し時間がかかったけど、ありがたいことに痛みが和らぎ始める。"

$ renpy.music.set_volume(0.5, 4.0, channel="ambient")


"俺が再び顔を上げると、沈黙と悲痛な面持ちだけが目に入る。たぶん自分の状況を説明した方がいいだろう。"

play music music_rain fadein 10.0



hi "不整脈なんだ。大丈夫、ただの……心臓粗動だから"


show lilly basic_listen
with charachange


li "本当に大丈夫ですか？　ナースさんを呼びましょうか？"


show hanako def_worry:
    ypos 1.0
with ease



"リリーの言葉を受けて、華子が素早く立ち上がりドアに向かって走り出す。"



hi "待ってくれ、華子。リリー、大丈夫だ"

show rin basic_deadpan
with charachange



rin "君、ジュクジュクでシワシワのトマトみたいだよ"



hi "はあ？"


"自分の手を額に当てると、汗のしずくでびっしょりになっているのが分かる。俺は袖口でそれを拭い取る。"



hi "ありがとう。この通り、大丈夫だよ。ただ俺はちょっと……虚弱、なのかもな"


show hanako basic_worry
with charachange

show hanako basic_worry:
    ypos 1.17
with charamove

show emi sad_shy
show rin basic_deadpanupset
show lilly basic_sleepy
with charachange


"陽気だった全体の雰囲気がどんよりした空気に変わってしまう。あまりにも気まずくて、誰もがどうふるまったらいいのか分からない。"



"そしてもちろん、全ては俺のせいだ。よりによって今、みんなのいる前でこんなことになってしまうなんて。"


stop music fadeout 8.0

show lilly basic_weaksmile
with charachange


li "そうだ、笑美ちゃん？"

show emi basic_hes
show rin basic_awayabsent
with charachange


emi "へっ？"



"笑美がジュースのパックをくわえたまま見上げる。"


show lilly basic_smileclosed
with charachange


li "まだ私の点数を言っていませんでしたね？"

show emi basic_annoyed
with charachange


emi "うん、まあ。でもリリーはハーフだからノーカンだよ"


"俺は眉を上げて、詮索するようにリリーのほうを向く。"

show rin basic_absent
with charachange


hi "とにかくさ、リリーは何点だったの？"

show lilly basic_cheerful


"リリーがこしゃくな笑みを浮かべる。"


show rin basic_awayabsent
show lilly basic_planned
with charachange


li "１００点。満点です"

play music music_lilly fadein 0.5


"そんなバカな。俺は口をあんぐり開けたままあっけにとられることしかできない。"



"あのテストは下手をするとネイティブであっても常識外れな難しさだった。それを考えると、リリーは辞書の一部を頭にたたき込むくらいのことをしたとしか思えない。丸暗記の才能があるのかもな。"


show rin basic_absent
with charachange


hi "な……"

show rin basic_awayabsent
show emi sad_pout
with charachange


emi "ほら見てよ！　ハーフじゃなきゃこんないい点は取れないよ"

show rin basic_absent
with charachange


hi "『見て』……"

show rin basic_awayabsent
show emi basic_closedsweat
with charachange


emi "あ……"

show lilly basic_giggle
show hanako basic_smile
with charachange


"笑美の反応を見てリリーと俺がにやりと笑う。俺が最初にその小さな地雷を踏んだ時と同じ反応だ。だけど、リリーの外国の家系で一つ思い出したことがある。"

show rin basic_absent
with charachange


hi "ああ、そうだ。リリーは明日スコットランドに飛ぶんだよね？"

show rin basic_awayabsent
show lilly basic_smile
with charachange


li "その通りです。笑美ちゃんも知っていましたよ。数日前同じクラスの友人に話しただけなのに、噂というのはあっという間に広まってしまうようですね"

show emi sad_grin
with charachange


emi "休みに世界を半周できるなんて、すごく素敵だよね"

show emi excited_happy
with charachange


emi "ねえ、あっちで何かおみやげ買ってきてくれない？"

show rin basic_absent
with charachange



hi "なんだよ、ずいぶん遠慮してるな"



show lilly basic_giggle
with charachange


"リリーが陽気にくすくす笑う。明らかに笑美の遠慮のなさを予想していたかのようだ。"



"昼休みの残りの時間は今まで通りに続く。ありがたいことに、心臓発作が起きる前の陽気な雰囲気も完全に戻っていた。"


stop music fadeout 8.0

scene bg school_roof
show lilly basic_smileclosed:
    center
    ypos 1.2
with shorttimeskip


"皆適当に挨拶を済ませながら別れていき、リリーと俺だけがこの場に残る。"


hi "なあ、リリー？"



"リリーはかばんの中に物をしまい終え、かばんを閉めた後でほんの少し顔を上げる。"


show lilly basic_smile
with charachange


li "はい？"



hi "ええと……さっきは助け船を出してくれて、ありがとな。俺も何とかしたかったんだけど、どうしたらいいか分からなくてさ"




"できるだけ無愛想に聞こえないように言おうとする。でも昨日の手紙、テストのひどい結果、それにこの心臓のおかげで、そうするのがとんでもなく難しい。"


show lilly basic_weaksmile
with charachange



"リリーが寛大に微笑んでうなずく。気にせずにいてくれればと思うけど、彼女の性格からすれば、そうもいかないだろう。"




li "笑美ちゃんは体は丈夫ですが、それでも人間なんです。私たちだってあなたのことは心配しているんですよ、久夫さん"




hi "ちょっと待った、なんで俺のことが心配なんだ？"

$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

show lilly basic_displeased
with charachange


"リリーの笑顔が消え、かわりに息がつまるほどの真剣な表情になる。"



li "久夫さん、私たちはあなたの置かれている状況を知らないわけではないんです"





li "それは……"



show lilly basic_concerned
with charachange


"リリーの言葉が突然途切れる。言いたいことを俺に言うべきかどうか迷っているんだ。俺は弱々しく笑うとリリーの肩に手を乗せる。"

play music music_twinkle fadein 10.0


hi "やめてくれ。自分が心配するだけで十分だよ。俺の重荷をみんなにも背負わせたくない"

show lilly basic_oops
with charachange


li "でも……"


hi "もしみんなが俺のことを心配したら、俺はみんなが心配してるってことを心配しなきゃならなくなる。意味……分かるかな"


hi "俺は大丈夫だよ。分かった？"

show lilly basic_reminisce
with charachange


"リリーはしばらく考え込んでいるようだ。どう答えるべきかを注意深く探っている。"

show lilly basic_weaksmile
with charachange


li "久夫さん、お昼ご飯の包み紙は残っていますか？"


hi "ある……と思うけど？　確かめてみるよ"

play sound sfx_rustling


"俺はかばんの中を引っかき回して昼食の残りくずを探り、ついにサンドイッチのパックに使われていた正方形の紙を見つける。"



"俺は眉をひそめ、いぶかしげな表情さえ浮かべながら、その紙をリリーの手に優しく乗せる。リリーは何もしゃべらず、指で紙の周りをなぞって角の位置を感じ取っている。"


show lilly basic_smile
with charachange


li "大きさは十分ですね……"



"２人で屋上に座ったまま、午後の授業まで刻一刻と時が迫る。リリーは紙を地面に広げると、真剣な様子で作業を始める。"


show lilly basic_smileclosed
with charachange


"辺りは静寂に包まれる。俺は驚くほど手慣れた様子で正方形の紙の上を動くリリーの指に見とれる。こちらを小さく折り、あちらを大きく折り。リリーの指先はゆっくりと、でも着実に紙を折っていく。"


"顔を上げると、そこにはリリーの落ち着いた穏やかな表情がある。リリーの視線は紙の位置のはるか上を向いていて、そのおかげで彼女の作業姿がいっそう興味深いものに見える。"


"最後の一折りを終えると、リリーが少し肩の力を抜く。完成したようだ。彼女が手の上に乗せて持ち上げたときになって初めて、俺はそれが何であるかを知る。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene white
with dissolve

with Pause(0.1)

scene ev lilly_crane:
    truecenter
    zoom 1.1 subpixel True
    ease 15.0 zoom 1.0
with Dissolve(4.0)


"小さな折鶴。"


"包み紙を使ったおかげで薄茶色のそれは、とても繊細かつ巧妙に見える。"


hi "折紙折れるんだ？"


li "小さい頃、自分で習ったんです。このおかげで少し器用になりましたよ"


hi "へえ……"



"少しまごつきながら、俺はその小さな鳥をリリーの色白な手のひらから取る。息を吹きかけただけで壊れてしまう物を扱うかのように注意深く。それはとても上手に折られていて、しっかりと形を保っている。"


$ renpy.music.set_volume(1.0, 2.0, channel="music")

scene bg school_roof
show lilly cane_smile at center
with locationskip


"俺とリリーはそれぞれのかばんを取り、ドアに向かう。リリーは杖を元の長さに伸ばしている。"

stop ambient fadeout 2.0

scene bg school_hallway3
with locationskip



"２人で廊下を歩いているあいだも、俺はリリーの手作りの品をもっとよく見るためにそれを自分の顔の前に近づける。リリーは方向を定めるために銀色の手すりに手をかけている。"




"もし器用さを鍛えるためにリリーが一人で折紙を習ったのなら、彼女の置かれた状況を考えたら手を使うということは大きな意味を持っていて……ああ、そうか。"



"俺はこの鳥の持つ意味に気づいて、微笑む。"



"『ここにいる人は誰でも、自分の状況に折り合いをつける方法を自分で見つけないといけないんです。もしここで困ったことがあったとしても、あなたは独りではないんですよ』"



hi "ありがとう、リリー。嬉しいよ"

show lilly cane_cheerful
with charaenter



"リリーが優しい笑顔で俺にうなずく。いつもの振る舞い通り、余分な言葉を発することもなく。"


show lilly cane_smileclosed
with charachange


li "久夫さん、私はただ、あなたに体を大切にしてもらいたくて"


hi "心配いらないよ、大切にする"

show lilly cane_smile
with charachange


li "約束してくれますか？"


hi "約束する"

hide lilly
with charaexit

stop music fadeout 7.0


"こうして、俺たちは別れる。"



"俺がいつ死んでもおかしくないということ。それを周りの誰もが知っているということ。どっちが俺にとってより不愉快なのか、正直言ってよく分からない。"



"俺はその日その日を生きるだけなんだろう。手の中の思いがけないプレゼントを見て、俺は独りじゃないと知る。こんな状況であっても、独りじゃないんだ。"


"もし皆が、誰かが、俺を心配したら、俺は笑おう。"


"皆の心配を吹き飛ばしてしまうくらい、俺は笑おう。"

scene black
with dissolve



label jp_L8:

scene black
with dissolve

play sound sfx_normalbell

scene bg school_scienceroom
show muto normal at center
with locationchange


"チャイムの音が鳴った瞬間、皆が一斉に安堵のため息をつく。"

play music music_happiness fadein 2.0


"午前中のほとんどが延々と続く化学量論の授業に使われていた。うんざりするほどの暑さに覆われている教室で教えるには全くふさわしくないトピックだ。"

hide muto
with charaexit


"これ以上何かを教えようとするのは無益な行為だと知って、武藤先生があきらめた様子で教卓の上にある今日の分の教材を片づけ始める。"

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

show hanako basic_normal at center
with charaenter



"たわいもない雑談が教室を賑わし始めるころ、俺は華子が席を立ち俺の机にやって来るのに気づく。最近の華子は以前に比べて内気な態度がずっと和らいでいて、俺はそのことに少し満足感を味わっている。"


show hanako basic_smile
with charachange


ha "こんにちは、久夫くん"



hi "やあ。じゃあ、リリーを呼びに行くか？　フライト時間を考えたらそろそろ出なきゃいけないころだし"

show hanako cover_worry
with charachange


ha "あの……そのことで……"

show hanako basic_worry
with charachange


ha "リリーがクラスの人たちと少し一緒に過ごすかもしれないって"


"考えてみればつじつまが合う。リリーのクラスは俺たちのクラスよりもほんの少し早く授業が終わるので、普通なら彼女はもう俺たちの教室に来ているはずだ。リリーのクラスが彼女を見送っているに違いない。"


hi "そっか、まあいいや。俺たちはリリーの教室の外で待ってればいいよな？"

show hanako emb_smile
with charachange



"華子がくすくすと笑い、うなずく。俺と華子はおしゃべりをしながら３－２の教室に向かう。"


stop ambient fadeout 1.0

scene bg school_hallway3
with locationchange


"目的地に着いた時、教室の中の何気ない面白い光景が俺の目に留まる。"




"クラスの背の低い女子生徒の一人がリリーをぎゅっと抱きしめている。彼女の背はリリーのあごの位置よりも低い。他の数人の友達もリリーの周りに集まっている。リリーはただ優しく笑い、彼女に抱擁を返している。"





"リリーはとても人気者らしい。静音の３－３での厳格かつ公平な支配とは対照的に、リリーはいわば３－２の母なる存在のように見える。彼女の身長と容姿については言うまでもない。"



"教室の隅の席で持ち物をかばんにしまっている健二のひときわ目立つクールな態度も予想通りだ。奴がリリーの旅立ちが引き起こす大騒ぎに全く無関心であることは疑うべくもない。"


"横をうかがうと、華子が俺が見ていたのと同じ方向に視線を向けている。俺はついに教室に入っていく決心をする。"

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

scene bg school_room32
show crowd at center
show lilly basic_surprised at center
with locationchange


hi "こんちは、リリー。俺と、それから華子だよ"

show lilly basic_surprised at twoleft
show crowd at bgleft
show bg school_room32 at bgleft
with dissolvecharamove

show hanako emb_downtimid at tworight
with charaenter


"リリーの周りにできた人だかりに直面して、華子がひときわうろたえる。華子も努力はしているけど、社会の場に対する不安を完全に克服するのは彼女には難しいだろう。"


show hanako emb_emb at tworight
with charaenter


ha "こんにちは……"


"リリーが俺と華子の位置をうまく探し当てるけど、クラスメイトがあっという間に再び彼女を俺たちから引き離す。そのときリリーがほんの少しいら立った表情を見せるけど、それも無理はない。"

show lilly basic_smileclosed
with charachange


li "こんにちは、久夫さん、華ちゃん。フライトまでまだ時間は十分ありますか？"


"俺はちらりと自分の腕時計に目をやる。空港までの移動時間を考えても、どんなハプニングがあったとしても１０分、いやたぶん１５分は余裕がある。"



hi "ああ、数分は残ってるよ。まだ乗り遅れる心配はないな"


"クラスメイト" "あら、池沢さん？"



"あちゃあ。俺たちまでうっかりリリーの社交の輪にまぎれ込んでしまったみたいだ。"



"その女子生徒は健二のような弱視のグループの一人らしく、牛乳ビンの底のような厚いメガネをかけている。無造作にカットされた短髪は、彼女の興奮した表情によく似合っている。"


show hanako def_shock
with charachange


ha "こ、こんにちは……あの……"



"彼女は華子の手を取るとぶんぶんと激しく上下に振る。女の子ってのはどうして友達の友達というだけの関係でこんなに親しくできるのか、俺にはさっぱり分からない。"



"華子が緊張の挨拶を交わしているあいだ、俺は健二の姿を求めて教室の中を見まわす。探してみたけど、奴は誰にも気づかれずに教室を出て行ってしまったようだ。"



"しばらくのあいだ、健二がどういう進路を進めば奴の唯一のスキルを適切に生かせるだろうかと俺は考えをめぐらせる。その後で、もっと切実な事柄へと思考を移す。"

show lilly basic_smile
show hanako cover_distant
with charachange




"華子が急に周りの女の子たちの興奮を呼び起こしたことに、リリーは多少用心しつつも、喜んでいるように見える。リリーには見えないだろうけど、華子はこんな状況でも俺が予想していたよりずっと落ち着いている。"




"周りの生徒の集団にもみくちゃにされながらも、俺はようやくリリーの元にたどり着く。"


hi "心配ないよ、華子は大丈夫だ"

show lilly basic_weaksmile
with charachange


li "ありがとうございます。華ちゃんが参ってしまうかもしれないと思ったので"


"クラスメイト" "心配ないわよ、私たち優しいもん！"

show lilly basic_concerned
with charachange


"俺とリリーは同時に顔をしかめる。他の生徒たちが近寄ってくるあいだも、華子は相変わらず張り付いたような引きつった笑顔を見せている。"


"華子もたった一ヶ月前まではこんな状況に決して馴染めなかったに違いない。俺はなんだか信じられない気分になる。俺が華子と２人っきりで最初に出会った時も、彼女は全力疾走で図書室から出て行ってしまったんだ。"


hi "さて、必要なものは全部持った？"

show lilly basic_smile
with charachange


li "荷づくりはすべて終えました。出発の時にそれを部屋まで取りに行かないといけませんが。それから、華ちゃんと私は着替えないと"


hi "じゃあ、そろそろ行ったほうがいいな。華子？"

show hanako cover_bashful
with charachange


"華子がハッと俺たちのほうを振り返る。周りに群がる連中から抜け出せるチャンスを得た彼女の顔には、ありがたいという表情がありありと浮かんている。"

show hanako basic_bashful
with charachange

stop music fadeout 2.0


ha "い、今行きます！"

stop ambient fadeout 0.5

scene bg hosp_ext
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0
play music music_tranquil fadein 3.0


"タクシーでの長い旅は、俺たち３人が皆後部座席に押し込まれていたにもかかわらず驚くほど快適だ。逆の見方をすれば、『にもかかわらず』という言葉はたぶん適切じゃない。"




"リリーがタクシー代を払い、みんなで車を降りる。華子は左右をきょろきょろとうかがっている。幸い、周りにはそれほど人はいない。ほとんどの人は外でうろつくこともなく建物の中にいるみたいだ。"



show akira basic_boo at tworight
show hideaki bored:
    yalign 1.0 xanchor 0.5 xpos 0.9
with charaenter



"すぐにフェンスにもたれかかって時間つぶしのおしゃべりをしている晃さんと秀明くんを見つける。そばの車輪とハンドルの付いた大きな黒い旅行かばんもフェンスに立てかけてある。"


show hideaki surprise_up
with charachange


"まず秀明くんが俺たちに気づき、晃さんに俺たちを指し示す。すると晃さんがやたら大げさにこちらに手を振る。"

show akira basic_laugh
with charachange


aki "おい！　お～い！"


"２人のほうに向かうため、俺はリリーの旅行かばんを手に取る。リリーがうなずいて俺に感謝の意を表す。"

show akira basic_smile
show hideaki normal
with charachange



aki "あたしの荷物は全部ここにあるよ。リリーはちゃんと持ったかい？　飛行機のチケットも？"


show lilly basic_smileclosed_cas at twoleft
with charaenter


li "心配しないで、全て持っているわ。姉さんは？"

show akira basic_laugh
with charachange


aki "うん。準備オッケーだな"

show hideaki evil
with charachange


hh "ちなみに、準備中にトラブルもなくはなかったけどね"

play sound sfx_impact

show akira basic_kill
show hideaki ohshit
with vpunch


"当てつけがましいコメントをした秀明くんの頭が硬く締め付ける腕によって乱暴に引き回される。"



show akira basic_boo
show hideaki sad
with charachange



aki "ははっ、ああ。なんていうか、ズボンのポケットにチケット入れてるの忘れちゃっててさ。ズボンを洗濯……"


show lilly basic_concerned_cas
with charachange



li "いやだ、もう……"


show akira basic_laugh
with charachange



aki "大丈夫、大丈夫。最近はオンラインで予約したチケットはプリントアウトできるって知ってたかい？　すげえよな"


show hideaki bored
with charachange



"秀明くんの苦渋の表情が、この解決法を見つけるのも簡単じゃなかったことを物語っている。大事にならずに済んでよかった、のかな。"


show lilly basic_weaksmile_cas
with charachange



li "じゃあ、そろそろ行ったほうがいいわね。チェックインはもう始まっているはずだから"


show akira basic_lost
with charachange

stop music fadeout 2.0


aki "ああ、そうだな"



"２人の口調にはある種の感慨深い気持ちがこもっている。後に残していく人々のことは言うまでもなく、何年も経った後の家族との再会はとても大きな出来事だろう。"


show hanako emb_sad_cas at center
with charaenter

play music music_serene fadein 4.0


ha "リリー……"



"華子は別れを告げるためにリリーにそっと抱きつき、リリーも心からの抱擁を返す。それからリリーと俺は軽く抱き合い、お互いに別れを告げる。"




"そばでは晃さんと秀明くんが軽いハグを終えて体を離し、いくつか言葉を交わしている。もし２人の滑稽なほどの身長差がなければ、とても素晴らしい光景になっていただろう。"


show lilly basic_smile_cas
show akira basic_smile
show hanako emb_downtimid_cas
show hideaki normal
with charachange



"リリーは告げるべき別れの言葉を全て告げ終えると晃さんの腕につかまり、２人は大きなガラスのドアの向こう側へと歩いていく。"


show lilly back_smileclosed_cas
with charachange


li "さようなら、久夫さん、華ちゃん！"

show akira basic_laugh
with charachange


aki "またな！　バカな真似するなよ、チビ助！"

hide lilly
hide akira
with charaexit


"２人の姿が中の人だかりに埋もれて完全に見えなくなるまで、俺たちは手を振り続ける。"


"そうして……俺たちは取り残される。"


hi "さてと……行っちゃったな"

show hideaki bored
with charachange


"すでに立ち去ろうとしている秀明くんのほうを振り返る。"


hi "またな"

show hideaki bored_up
with charachange

show hideaki invis:
    xpos 1.0
with dissolvecharamove

hide hideaki
with None



"秀明くんは晃さんっぽいやり方で無造作に手を振る。そうしてついに、外で立っているのは華子と俺だけになる。"


show hanako emb_timid_cas
with charachange


"俺は華子の肩の上に手を乗せる。彼女は今もぼんやりとビルのフロントドアを見つめ続けている。まるで去りゆく２人のどちらかをもうひと目見られるかもしれないと期待しているかのように。"


hi "心配ないって、時間なんてあっという間に過ぎるからさ"

show hanako basic_normal_cas
with charachange


"華子はしばらくためらっていたけど、やがてうなずく。"


"焼けつくような夏の日差しを浴びながら、俺と華子は近くのバス停まで歩いていく。"

hide hanako
with charaexit


"本当に奇妙だ。俺が今までと違う見方でリリーを見始めたちょうどその時、彼女は自身の過去への巡礼ともいえるべき旅へと去ってしまう。"


"だけどそれはある意味、俺が山久に来てからずっと続けてきたことなんだ。"



"俺の身に起こってきた全てのことを考える限り、俺は決して特別なんかじゃない。誰もがそれぞれ違った状況にいて、各々が違う道のりで今いる場所にたどり着いたんだ。"




"それでも、俺がこれからどう歩むべきなのかが未だによく分からない。俺の人生は一度リセットされたも同然だ。そうして心にぽっかりと空いてしまった穴をまだ満足に埋められずにいる。"




"リリーが旅立ってしまったことは、きっと俺にはいいことなのかもしれない。頼るべき人がいない今、今まで以上に自分の面倒は自分で見なきゃいけない。華子の側にもいてやらなきゃな。"



"あんなにも現実から引き離されたかに思えた長い病院生活の後で、これほどたくさんの転機を短期間に迎えるなんて、なんだか変な気分だ。だけど、それがますます俺の意識を集中させる。"



"自分の人生を立て直すためのチャンスを一つたりとも逃すわけにはいかないんだ。"


stop music fadeout 3.0
stop ambient fadeout 3.0

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
