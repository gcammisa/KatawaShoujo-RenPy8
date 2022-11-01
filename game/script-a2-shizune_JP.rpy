label jp_S8:

window hide None

scene bg school_dormhisao
with locationchange

with Pause(1.0)

nvl clear

nvl show dissolve

play music music_dreamy fadein 5.0


n "\n\n翌朝、昨日の夜はなんてすばらしかったのだろうと記憶を反芻する。思い出が強すぎて、考えるのをやめることができない。"


n "回想にふけっている場合ではなさそうだ。一時間目からテストがある。"


n "あー、ほんとに不公平だよな。どうしてこんなことをしてくれるんだ？　過去何週間かの作業の集大成として学園祭を日曜日に開いておいて、その翌朝から続けて試験をやるってのか？"


n "悪趣味な冗談に違いない。"


n "試験自体はそれほど心配はないけど、せめてあと１週間くらいあとに延ばせなかったのか、と疑問に思う。"


n "\n\nまあ、少なくとも今朝は天気がいいから、始業前に外で予習ができるな。"

nvl hide dissolve

scene bg school_courtyard
with locationskip

nvl clear

nvl show dissolve


n "\n\n教室にいるよりは外にいるほうがずっと気分がすっきりする。静かなのは言うまでもない。今日はみんな相当遅くまで寝ているんじゃないか、と思い始める。"


n "読み返していたノートをちょっと地面において、まだ学園祭の屋台が散らかっている校庭に目を向ける。"


n "日差しが明るく、屋台から目を奪うような提灯や人混みがない時に見ると、妙なことに気づく。"


n "昨日静音やミーシャと一緒に見て回った屋台のほとんどは、俺たち自身で作ったものだった。"



n "\n……"




n "\nかわいらしいじゃないか。静音が考えたんだろうか？　あいつのことだから、意図的にやったに違いない。俺がそのことに気づいて、自分たちが苦労して成し遂げたものを目の当たりにすることを期待していたのか？"

play sound sfx_footsteps_soft fadein 5.0
stop music fadeout 4.0

nvl hide dissolve

show shizu basic_normal at center
with charaenter

window show



"芝生を踏みしだく足音が聞こえて、俺は振り向く。ちょっと行き過ぎた妄想をしてしまうけど、そこには何の表情も浮かべていない静音が立っているだけだった。"


play music music_shizune fadein 1.0

show shizu adjust_happy
with charachange


shi "……"


hi "おはよう"


"どうしていつも、静音には聞こえないってことを忘れるんだろう？"


"たぶんミーシャが俺たち二人のために通訳してくれることに慣れすぎてしまって、俺が静音の耳が聞こえないこと、そこから生まれる問題に直面することがあまりなかったからだ。"


"そうなったのは昨日が初めてだったと思う。"



"とにかく静音に手を振る。少なくともこのくらいはできるけど、手話を全然知らないことを考えれば、静音と会話ができるなんて決して思えない。"


"このまま予習に戻ったら失礼だろうか？　他にどうすればいいのか正直わからない。"


hi "ミーシャはどうしたの？"

show shizu behind_blank
with charachange


shi "……"


hi "話が分からないからってだけじゃなくてさ。二人ともいつも一緒だし、一人でいるのは見慣れないなって"


"バカみたいなのは分かってるけど、どういうわけか静音に話しかけていると気まずさが薄れる気がする。"

show shizu basic_normal2
with charachange

show shizu adjust_happy
with charachange

show shizu behind_blank
with charachange


"驚いたことに、静音は全然怒り出さない。手話を始めるけど、それはいつもの仕草とは違う。静音の手の動きはもっとゆっくりしていて、仕草もより単純だ。"


"俺はすぐに気づく。これは手話でもなんでもないけど、それでも静音は俺と会話しようとしているんだ。"


hi "じゃあそれは『手話を一般人にもわかりやすくしたもの』なのか？"



show shizu behind_frown
with charachange



"もしこっちから手話で返そうとしたら、俺はただのバカにしか見えないじゃないかと恐怖する。静音の表情を見ると、今みたいな形でやりとりをしようとするのはあまりうまくないと思い始めているみたいだ。"



"もっといいやり方があるだろう。"


"メモ帳に書くか？　まあ紙と鉛筆はあるけど。でも他に何がある？"


"携帯とか？　あるけどここではあまり使い道がないから、ほとんど持ち歩いていないし、静音が持っているかどうかも知らない。"

show shizu adjust_happy
with charachange

show shizu basic_normal
with charachange


"静音が先に動く。ちょっと待ってと指を立て、かばんからメモ帳とペンを取り出して一言書き付ける。"

window hide



$ written_note("おはよう")




show shizu basic_normal2
with charachange

window show


shi "……"


"俺はぼんやりと静音を見つめる。向こうからは似たような、でももっと威圧的な視線が返ってくる。静音はメモ帳を俺に向かってずいと突き出す。明らかに返事を求めている。"

window hide


$ written_note("おはよう")

show shizu behind_smile
with charachange

window show


"静音は不釣り合いなくらいうれしそうな笑顔を見せる。勝ち誇ったようにペンを回しながら、次はどうしようかと考えている。"




hi "おいなんだよ、大げさだな"






show shizu basic_frown
with charachange


"まるで今のが聞こえたかのように、静音はぶっきらぼうに眼鏡を押し上げると、ものすごい勢いで書き始める。"

window hide


$ written_note("メモ帳使いなさい！　書いて書いて書いて書いて書いて書いて書いて書いて書いて書いて書け書け書け書け書け書け書け書け書け書け書け！")



window show


"どうすりゃいいんだ。そのメモ帳を受け取って『わかった』って書けばいいのか？"


"スムーズで流れるような会話とは遠くかけ離れている。ミーシャがたやすく静音と会話できているのがねたましくなる。"

window hide

show shizu behind_blank
with charachange


$ written_note("試験勉強してるの？")

window show


"こんな簡単な『はい』か『いいえ』の質問だったら、うなずくだけで返しても許されるに違いない。"

window hide

show shizu adjust_smug
with charachange


$ written_note("すごく朝早いのね。学園祭の後はみんな遅くまで寝てるのに。つまりあなたは普通じゃないってことね。")



window show


"……そうなのか？"

window hide


$ written_note("お前だっているじゃないか。")

window show



"しかし返事を静音に渡す前に、さっき気がついたことを思い出して、書き加える。"


window hide


$ written_note("お前だっているじゃないか。\n\n昨日は楽しかったよ。そういえば昨日見て回った屋台、俺たちが作ったのばっかりだったな。だから見覚えがあったのかもしれない。あれも勝負だったのか？")

show shizu behind_frown
with charachange

window show


"静音は憤慨したように首を左右に振る。"

window hide


$ written_note("そんなんじゃありません。")



show shizu basic_normal2
with charachange


$ written_note("あなたが作った屋台だから、それが一番大事だと思った。見に行かなきゃいけなかったの。誰でもみんな、自分の仕事の成果を味わう権利がある。あなたにも自分の成し遂げたことを見て、楽しんでほしかった。")



window show



"なんだか心が打たれる。それでも、どうして静音がそこまでしてくれるのか、疑問を抱かずにはいられない。静音に答えるときにそう尋ねる。"





window hide

show shizu behind_blank
with charachange

stop music fadeout 3.0


$ written_note("あなたが落ち込んでたから。")

window show



"俺はずっと落ち込んでたんだ、と言いたかったけど、やめる。その通りだ、俺は相当腐ってたし、しょっちゅうそれを表に出していたから、静音が気づいていたというのはありうることだ。"
"じゃあ静音がしてくれたことは全部、ただ俺を元気づけるためだったのか？"



hi "ありがとう"


"気づくまもなく、そうつぶやいている。でも静音は気にしていないようだ。代わりに今度はメモ帳に書く。静音はそういうことに慣れていないかのように、１回だけうなずく。"




"二人の間の沈黙が一秒ごとにどんどん膨れあがり、俺にはそれを破りたくてもどうすることもできない。何もかも紙に書かないといけないんじゃ、さりげなく何かをすることなんてできるわけがない。"






window hide

show shizu adjust_happy
with charachange


$ written_note("試験がんばってね。")

window show


"静音は俺の目の前にメモ帳を押し出して、俺の意識を破る。また先手を取られた。いつも通りだな。"

hide shizu
with charaexit


"静音が学校に向かう間、俺は少し悲しい気分になってしまう。"

window hide

nvl clear

nvl show dissolve


n "\n\n一生の中で一番長い２０分だったような気がする。それもみんな、メモ帳をやりとりすることで一対一の会話をするなんて経験が今まで全くなかったからだ。おかげでほぼずっと頭の中が真っ白だった。"



n "こういうことがあると、手話を勉強したいという気になる。"



n "言うだけなら簡単だ。でも山久みたいな学校なら、たぶん手話のクラスがあるだろう。だとしたら、やってみない理由はほとんどない。"


n "そのことを聞ける唯一の人物は、今のところは、ミーシャだ。"


n "俺はどれだけ真剣に手話クラスのことを知りたいんだろう？　選択肢は二つある。放課後まで待つか、今すぐミーシャを探しに行くかだ。"


n "今すぐ行くことにする。でもミーシャがどこにいるか分からない。女子寮に行って探すのが一番確率が高そうだけど。どっちにしても、静音と一緒にいないなら、たぶんそこにしかいないだろう。"

nvl hide dissolve

nvl clear

scene bg school_dormext_full
with locationchange

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_daily fadein 1.0

nvl show dissolve



n "\n\n男子が朝っぱらから何気なく女子寮の中をうろついているなんて許されないだろうけど、静音の目の前でミーシャに手話クラスのことを聞くなんて絶対にありえない。"





n "ミーシャもいつかは学校に来るだろう。大体同じクラスなんだから、あいつも同じテストを受けなきゃいけないんだ。"


n "ここで待っていれば、そのうち会えるに違いない。"


n "俺がノートを読み返している間に、通り過ぎてしまわないといいんだけど。"



n "\n\n結局、かなり長い間待つことになった。生徒たちが学校に集まる間、ミーシャは遅刻だろうかと疑問を抱く。"



n "やがてミーシャの姿が目に入る。地面をぴょんぴょんと跳ねるのを見て、盲目でもなければあれだけ目立つ髪は見逃さないだろうと思い至る。"





$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

nvl hide dissolve

show misha hips_grin at center
with charaenter

window show


mi "こんちわ、ひっちゃ～ん！　おっはよ～！"


hi "おはよう"


"授業が始まるまであまり時間がないので、単刀直入に切り出す。"


hi "なあ、一つ質問してもいいか？"

show misha perky_smile
with charachange


mi "質問？　んん～……おっけー、ひっちゃん～！　もちろんもちろん～！　時間ならあるから、でも遅刻したせいだけどね！"


hi "どういう意味だ？"

show misha hips_grin
with charachange



mi "はは、本当はもっと早く起きなきゃいけなかったんだけど、すっごく疲れてたし～……早起きしてたら勉強しなきゃいけなかったけど、早起きしなかったから問題ないんだよ～！　それでどうしたの、ひっちゃん？"



hi "そうだ、ここには手話のクラスがあるよな？"

show misha hips_smile
with charachange


mi "あるよ～！　選択科目だよ！　どうして知りたいの、ひっちゃん？"



"どういうわけか、その質問を聞いた俺はあっさりとパニックを起こす。"




hi "別に。面白そうだなって思って。でも今から履修するのはもう遅いんだろ？"


"今のはバレバレじゃないだろうか。でもミーシャはこういうことにはそもそも気づきそうにないので、俺が必要以上に警戒しすぎているということなんだろう。"

show misha sign_smile
with charachange


mi "う～ん？　あー、でもねひっちゃん、手話のクラスを取る生徒は毎年減る一方だって聞いたよ。だから！　受けたかったら、きっと入れてくれると思うよ～！"

show misha hips_grin
with charachange


mi "手話の勉強するつもりなの、ひっちゃん？"


hi "……ああ"

show misha perky_smile
with charachange


mi "ひっちゃん、手話ができるようになったら、しっちゃんはとっても喜ぶと思うよ～。もしよかったら、放課後に一緒に職員室に行かない？　きっとクラスに入れてくれるよ"


hi "それは助かるな"


hi "でも俺が手話を勉強したがってること、静音には言わないでくれよ"

show misha perky_confused
with charachange


mi "どうして？"


hi "静音を驚かせたいんだよ。それに今朝そのことを言って、午後になって授業を取れませんでした、なんてことになったら気まずいだろ"

show misha perky_smile
with charachange


mi "え～。確かにそうだね、ひっちゃん。でもそれ難しいよ～……すごくすてきな話なのに……"


hi "俺も生徒会に入ってるし、勉強してみてもいいと思ったんだ。基本だけだとしても何も知らないよりは一歩前進さ。それに静音も俺も、いつまでも電話か何かみたいに全部お前を通して話すわけにはいかないだろ？"






"……"




with Pause(2.0)

show misha hips_laugh
with charachange


mi "わはは～！"

show misha hips_grin
with charachange


mi "そうだね、ひっちゃん～！"



"……"



stop music fadeout 4.0
play sound sfx_warningbell


"鐘が鳴って一時間目の始まりを告げ、会話は途中で遮られる。授業が終わってから先生に聞くことにするか。"


"ミーシャのリアクションはなんだか変だった。でも日が経つにつれ、そのことは忘れてしまう。"

scene black
with dissolve


label jp_S9:

scene bg school_scienceroom
with locationchange

play sound sfx_normalbell


"ベルが鳴り、教室の正面に立つ先生が手話で授業の終わりを知らせる。"





play music music_normal fadein 3.0



"クラスに入るのは驚くほど簡単だったけど、まだ数日しかたってないし、俺自身もまだ手話の授業には慣れてない。手話そのものは思っていたよりもわかりやすいものだった。でもクラスメイトのほとんどは難聴者だ。"





"その上、授業のやり方が徹底している。俺が手話クラスをとってもいいかと聞いたとき以来、先生が言葉を発するのを聞いていない。異質な考え方だ。とても不安になる。"




scene bg school_hallway3
with locationchange



"教室を出た直後に、自分のすぐ左から聞き覚えのある弾けた笑い声がするのが空気を伝わってくる。"




show misha hips_grin at center
with charaenter


mi "こんちは、ひっちゃん～！"


"ミーシャは俺とは別の手話クラスを取っているので、この辺で会うのは初めてだ。同じクラスじゃなくて良かったのか悪かったのかは、まだ判断がつかない。"


"一緒のクラスだったらもっと授業もおもしろくなったかもしれない。でも気まずい状況に陥る可能性も大幅に上がるだろう。"


hi "よう"

show misha sign_smile
with charachange


mi "こんなところで会ってびっくりしたよ、ひっちゃん！　……あっ、そうだ！　手話のクラス取ってるんだよね！　そうでしょ～！"

show misha perky_smile
with charachange


mi "どんな感じだった、ひっちゃん？"




hi "新しく言語を学ぶってのは簡単じゃないけど、なんとなく感じはつかんでる気がするよ。いくら他の言語と違いがあるっていっても、英語よりは簡単だからな"

show misha cross_grin
with charachange


mi "はは～！　そうなんだ、ひっちゃん？"

show misha cross_smile
with charachange


mi "う～ん……わたしもそう思うよ！"


"冗談だったんだけど、ミーシャは真剣に受け取ったようだ。"


"ミーシャは俺に手話を通訳しつつ、同時に静音と別の言語で会話する、ということを苦もなくこなす。いったいどうすればあんなことができるんだろう、と不思議に思う。"


"今までは、その見事な技能を当たり前のものだと思っていた。"


"誰かが俺の肩にぶつかって、謝ってくる。学校ももうすぐ終わる時間だからか、ちょっと人が多くなってきた。"


hi "廊下じゃなくて、どこか別のところで話した方がいいな。屋上でも行かないか"

show misha sign_smile
with charachange


mi "おっけ～！"


"行きすがら、話を進めることにする。道中は驚くほど静かで、会話を続けるには差し支えない。"

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

scene bg school_staircase1
with locationchange

stop music fadeout 5.0



hi "先生を見続けなきゃいけない、ってのに慣れるにはまだ時間がかかりそうだ。今までずっと、先生の話を聞きながら落書きすることを当たり前のことだと思ってたんだろうな。それにノートを取るのもずっと大変だよ"



hi "初級クラスは人数は少ないけど、俺はもう遅れ始めてる。やることはたくさんあるな"




play sound sfx_door_creak
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_roof
with locationchange


hi "あー、こっちのほうがずっといいな"



"振り返ってミーシャを見ると、ミーシャは腰に手を当てて、頬を膨らませながら俺をにらみつけている。"


show misha hips_frown
with charaenter

play music music_happiness fadein 4.0


mi "ひっちゃん、遅れてるの？　そんなの全然だめじゃない！"


hi "他の生徒から１週間遅れてクラスに入ったんだぜ。そこまで悪くはないだろ"

show misha sign_smile
with charachange


mi "じゃあね、ひっちゃん、今まで勉強したことの復習しよう。そしたら～！　わたしが個人指導してあげる。い～い？"




"『わたしが個人指導してあげる』なんてセリフをエロい映画以外で聞くのは初めてだ。思ったより全然興奮しないな。"





hi "まだ個人指導までしてもらわなくてもいいような気がするけど"


show misha perky_sad
with charachange


mi "え～……"


"普段よりもがっかりしているように見える。ミーシャのこういう表情を見ると、俺も気まずくなってしまう。"

show misha hips_frown
with charachange


mi "わたし手話の先生になりたいんだよ、ひっちゃん！　でも～、先に誰かと個人指導の練習ができたらすごく助かるんだ。ちょっとの間でも、役に立つ経験になるよ"


hi "ああ、まあ、そうだな。それは確かに"


hi "手話の先生を目指してるなんて知らなかったよ"



"俺の気を滅入らせるためにわざとこんなことを言っているのか、と疑ってしまう。正直とても悪いことをしてしまった気分だ。ミーシャはそういうことが得意だからな。"






"それでも筋は通る。俺が見る限り、ミーシャは今でも手話がとても上手だ。もちろん聴覚障害者との接し方だってわきまえている。ただ、ミーシャが教えるのが得意なタイプと考えたことは一度もなかったけど。"

show misha hips_grin
with charachange


mi "ははは～！　この学校に来たいと思ったのはそれが理由なんだよ、ひっちゃん！"

show misha sign_smile
with charachange


mi "それにね、ここの学費はとっても高いんだよ。手話の先生を志望しているおかげで、わたしの学費はすこし免除されてるの。それがなければ、ここに通い続けられてたかわからない"




hi "なるほどな。ミーシャの指導が下手だって思ってるわけじゃないんだよ。ただ自分がまだ指導してもらう必要があるかどうかわからないってだけで"

show misha perky_sad
with charachange


mi "そうだね。ひっちゃん頭いいもんね"


hi "そんなことはないよ。それじゃ俺が傲慢みたいじゃないか"


hi "わかったよ。じゃあ教えてください。お願いします"

show misha cross_laugh
with charachange


mi "あははは～！　ほんとに？　おっけ～！　おっけおっけおっけ～！　やったぁ～！　ありがと、ひっちゃん～！　わたしがんばるよ！"

show misha sign_smile
with charachange


mi "今すぐ始めよ～！"


hi "早すぎだろ"

show misha perky_sad
with charachange



"……"




mi "しっちゃんがいたらな～……"


hi "今朝は会わなかったのか？"

show misha sign_smile
with charachange


mi "授業中に話しかけるのって大変なんだよ、ひっちゃん！　今日は生徒会の活動もないし～"


hi "まあ、今週はずっと試験だったしな。これで生徒会まであったら怒るぜ。全部終わるのが楽しみだよ"



show misha perky_confused
with charachange


mi "生徒会が再開したら、さぼったりしないよね、ひっちゃん？"


hi "当たり前だろ。俺も生徒会に入ってるんだから"


hi "心配するなよ。突然行かなくなったりはしないから。約束は約束だ"



"あまり信じていない様子で、ミーシャは１秒ほど沈黙する。"




show misha sign_smile
with charachange


mi "しっちゃんは生徒会のことをすごく真剣に考えてるんだよ、ひっちゃん。ひっちゃんが入会してから、いいところを見せようとして、前よりもずっと生徒会の仕事をがんばってる"


show misha hips_frown
with charachange


mi "ほかにも入った人はいたけど、すぐに来なくなっちゃったの。しっちゃんはもっと生徒会に興味を持ってくれる人を増やそうとしたけど、うまくいかなかった"



show misha perky_sad
with charachange


mi "入ってくれる人がいても、そのうちに来なくなっちゃうの。なんだかんだって理由を付けて、来るのをどんどん先送りにして、結局顔を出さなくなって"

show misha sign_smile
with charachange


mi "でも……ひっちゃんは本気で言ってるんだって、信じるよ"


"ミーシャがしゃべる間、その両手が自分の意志を持っているかのように傾いたり動いたりして、口にした言葉を手話にして伝えている。俺の目はその手元から離れない。"




show misha perky_smile
with charachange


mi "ひっちゃんが入会するって言ってくれたとき、しっちゃんはすごく喜んでたんだよ"

show misha hips_smile
with charachange


mi "しっちゃんは、ひっちゃんが面白い人だって思ってるよ。面白くない人だったら、参加するだけの意欲がない。もしあったとしても、面白くない人だったらすぐやめちゃう、って"


mi "しっちゃんはそう言ってた"

show misha hips_grin
with charachange


mi "だから～！　ひっちゃんがちゃんと続けてくれるようにするのがわたしの役目ってわけ～！"


hi "だから俺に個人指導したいってことか？　なんかずるい奴だな"

show misha cross_laugh
with charachange


mi "ほんとに、ひっちゃん？　わたしのこと、そんな風に言われたのって初めてだよ～！　わははは～！"


"これじゃあ、もう生徒会の仕事からは逃げられそうにないな。"


"この数日間のことを考えると、そもそも生徒会に入った唯一の理由は静音だったことに気づき始めていた。あいつの負けず嫌いさと強気さに俺は興味を引かれている。"


"そんなことはミーシャには言えないけど。"

show misha sign_smile
with charachange


mi "じゃあね、ひっちゃん、今日の授業で習ったことを復習しましょう～！"


hi "お前、俺が今日授業でやったことなんて知らないだろ"

show misha hips_grin
with charachange


mi "う～ん、そうだねひっちゃん～！　おっけー、じゃあ基本から始めようか～！　一番最初から全部教えてあげるよ～！"


hi "それ、冗談だよな？"

show misha perky_confused
with charachange


mi "え～？"


hi "本気なのか？　そんなの授業だったら何日もかかるし、しかも俺たちは学んでるレベルだって違うんだぜ……"

show misha sign_smile
with charachange


mi "こんなの自転車に乗るようなものだよ、ひっちゃん～！　基本は絶対忘れないの！　わはは～！"

show misha sign_confused
with charachange


mi "でも、わたしは自転車の乗り方わかんないんだけどね～……"


"なんてこった。"

show misha hips_grin
with charachange


mi "うんうん～。わたしはいつかは先生になりたいから、もちろん自分が何やってるかはわかってるよ……おっけ～！　おっけおっけおっけ～！　じゃあ始めるよ～！"


stop music fadeout 3.0

show misha perky_confused
with charachange


mi "えっと……"

show misha sign_confused
with charachange


mi "……んんん～……"

show misha perky_sad
with charachange


mi "あははは～……"



"ミーシャはものすごくがんばっているように見える。ということはこれはまずいのかもしれない。"
"まあ、言語を学ぶことと教えることにはとても大きな違いがあるし、その最初のステップはたいていの場合一番難しいところだ。正直、俺だってミーシャよりうまくやれるとも思えない。"



"でもなあ……"

show misha sign_confused
with charachange




mi "えっと……公式な話をすると、１８世紀に……あー……名前は発音できないけど、フランスの人が手話を発表したの。その人は世界初のろう学校を1755年に始めて、でも文書には残っていない手話の歴史が……"






show misha sign_sad
with charachange


mi "どこから話せばいいのかわからないよ。ごめんね～……とにかく～、手話の歴史はお話を始めるには一番いいでしょ？　でしょ？　ね～！"

show misha hips_grin
with charachange


mi "あ、待って、５０音の方がいいかも。おっけ～、じゃあ５０音できまりね！"




play music music_another fadein 0.5

show misha sign_smile
with charachange


mi "おっけ、ひっちゃん～！　これが基本の基本だよ。でもこれが手話のすべてだって思いこんで、いろんな具体的なしぐさや単語を忘れちゃう人もいるの"

show misha hips_smile
with charachange


mi "それでも基本を知らないとどうにもならないからね！　これが『あ』だよ。わかる？　じゃあひっちゃん、やってみて！"


hi "それならもう知ってるけどな"


"ともかく、ミーシャのご機嫌をとることにする。"

show misha hips_grin
with charachange


mi "ははは！　そうだよ、その調子！"

show misha sign_smile
with charachange


mi "じゃあ、これが『い』で、これが『う』だよ"


"ミーシャは左右それぞれの手でひとつ文字を形作る。でもどちらの手がどの文字かは言わない。"

show misha perky_smile
with charachange

show misha sign_smile
with charachange

show misha hips_grin
with charachange


mi "で、『えお、かきくけこ、さしすせそ、たちつてと、なにぬねの』……"
mi "……『わを』、最後に『ん』～！"






"ああ、こりゃ大変だ。"


hi "やっぱり今日は生徒会の仕事をしようって静音が思ってたりはしないかな？　そっちに行ってもいいぜ"

show misha sign_smile
with charachange


mi "そんなわけないでしょ、ひっちゃん～！！　ほら、もう一回やるよ！　あいうえお、かきくけこ……ひっちゃんの番～！"


hi "じゃあ、やっておかないといけない生徒会の仕事とか、そういうものは本当にないんだな？"

show misha hips_smile
with charachange


mi "何言ってるの、ひっちゃん？　ほら、やってやって～！"


hi "こうか？"

show misha sign_smile
with charachange


mi "ちがうよ、こう！"


hi "こんな感じ……"

show misha perky_smile
with charachange

show misha sign_smile
with charachange


mi "こうだよ～！"


hi "あー……そっか……"

show misha perky_sad
with charachange


mi "しっちゃんがいたらよかったな。いたらずっと簡単にできたのに。ははは、普通はそうやって手話を教えるんだけどね。先生が二人でね～！　ひっちゃん、知ってた？"




hi "いや"


"静音がここにいたらどうなるか、脳内で想像してみる。"


"……"

show misha hips_frown
with charachange


mi "ひっちゃん～！　話聞いてる？"


hi "聞いてるよ"

show misha sign_smile
with charachange



mi "しっちゃんが言ってたけど、手話は何かを言う前に頭の中ですべてを考えないといけないから、他のどんな言語とも違うんだって"
mi "つまり、一つ一つの単語がもっと重みを持ってるってことだよ、ひっちゃん。言葉の一つ一つが普通よりも大事なの"



show misha cross_smile
with charachange


mi "だから～、ちゃんと、集中してね"

show misha sign_smile
with charachange


"ミーシャは手話の基本について、駆け足で講義を続ける。やがて、俺にもわかる内容を話し始める。"





"終わってみると、俺は感心していた。最初はちょっとつまずいたけど、本気になったミーシャはとても教えるのがうまい。"


stop music fadeout 4.0

scene bg school_roof_ss
show misha sign_smile_ss at center
with shorttimeskip


"しばらくして、もう遅い時間になっていることに気づく。俺はミーシャにお礼を言って別れを告げ、寮に戻る。"

stop ambient fadeout 1.0

scene bg school_dormhisao_ss
with locationskip


"たくさんのことを学んだ日だった。"

scene black
with dissolve


label jp_S10:

play sound sfx_doorknock

scene bg school_dormhisao
with vpunch


"ドアをバンバンと叩く大きな音が聞こえてきて、俺は飛び起きる。"


"最初に頭に浮かんだのは静音だった。こんな時間にあんな大きな音でノックする人は、耳が聞こえない人か、さもなければ大馬鹿野郎に違いない。"


hi "誰だよ？"


"もちろん、静音だったら今の声も聞こえないし返事もできない。"


"返事がないので、ちょっとうれしくなる。しばらく静音に会っていなかったし。"

play sound sfx_dooropen

scene bg school_dormhallway
show kenji tsun at center
with locationchange

play music music_kenji fadein 2.0


"ドアを開けると、健二が廊下に立っている。その目つきが神経質に右へ左へと素早く動く。"


hi "なんだ、お前かよ"

show kenji neutral
with charachange


ke "そうだよ俺だよ。なんだそのリアクションは？"


hi "まあな、俺が誰だって聞いたときに答えてくれていれば、もっと相手に合った返事ができたんだけどな"

show kenji tsun
with charachange


"健二はしかめ面をして、静音とまるで同じしぐさで眼鏡を持ち上げる。"


ke "どうしてそんな変な顔してるんだ？"




"これまでこいつのおかしな言葉や行動に何百回顔をしかめても気づかなかったくせに、どうして今だけは俺の表情がわかるのかと不思議に思う。その理由を問い詰めたいけど、そうするにはもう疲れすぎている。"




hi "静音がそういう風に眼鏡を持ち上げるんだよ。知ってるだろ、生徒会長。なんか変だなって"

show kenji rage
with charachange


ke "んだとお？　同じことする女子がいるってどういうことだよ？　そいつは眼鏡にさわるってのか？　これは俺の専売特許だ、俺の技だぞ"






ke "どこのどいつだそのビッチは？　どうしてビッチどもは俺のやることに首突っ込んで、俺のやることをパクりやがるんだ？"



show kenji tsun
with charachange


"健二の気分は怒りから恐れに一瞬でひっくり返る。"




ke "あいつ、俺を取り替えちまおうとしてるのか？　ポッドピープルか？　いや待て、それじゃ完全なコピーだ。ポッドウーマンか？"







ke "まるで俺が最も恐れていた２つのことがくっついたみたいだ"


show kenji rage
with charachange


ke "まさにそうだ！"



"そんなわけあるかよ……"


show kenji neutral
with charachange



ke "おい、今日は町に行くのか？"



hi "あー、後で行くかもな"

show kenji happy
with charachange


ke "よし。バッチリだな。郵便局で受け取ってもらいたい……ブツがあるんだ。繊細な秘密の代物だ"


"健二はひそひそと話す。その郵便物について普段の声の大きさで話すだけでも、それが危険にさらされるとでも言わんばかりに。"


hi "直接ここに送ってもらうことだってできるんだぜ"

show kenji neutral
with charachange


ke "できるかよ。学校に送ってもらったら、生徒会がそれを受け取って、奴らが俺たちに渡すんだ。手紙が自分の手に渡るのとはわけが違う"


ke "俺は生徒会は信用しない。ここの男たちは郵便なんて受け取ってないんだぜ"

show kenji tsun
with charachange



ke "あいつらは全部盗んでるに違いない！　自分たちに送られたから、自分たちには盗む権利があるとでも思ってるのか？"
ke "俺には見えるぜ、あいつらが郵便物の山にひじまで腕を突っ込んで、持てるだけお宝をつかみ取っていくのが。反吐が出るぜ"



hi "その、どこからともなく手紙を取り出して手渡してくれる郵便屋さんってのはどこに行けば会えるんだよ？"


ke "知らん。生徒会が殺したんだろうよ、生徒の私物を独占し続けるために"


hi "そんなことはないだろ"


hi "でもまあ、それが頼みごとか？　わかったよ、お前の郵便は受け取りに行ってやるけど、いずれこの貸しは返してもらうからな。お前まだ俺から借りた金があるだろ"

show kenji neutral
with charachange


ke "教えてくれてありがとうよ。ブツを受け取ったらお前に返す"


ke "そうだな、悪いけど、それまではマジで返せないんだ。まだ一文無しでさ"


hi "じゃあ俺はお金のために受け取りに行ってやるわけだ、仕事みたいに。そもそもなんでそのブツが必要なんだよ？　金でも入ってるのか？"

show kenji happy
with charachange


ke "ちげえよ"


"俺は本気であきれる。"


hi "どうして自分で受け取りに行かないんだ？"

show kenji neutral
with charachange


ke "今日はこれから自分の部屋を作戦司令室に模様替えするんだ"


ke "日が経つごとに、俺はフェミニズムの危険をより強く自覚するんだ。あれは本当にあらゆるところに存在する。イランのようなところでさえ。どこまで浸透しているかなんてわかりゃしない"

show kenji tsun
with charachange


ke "戦争が始まったとき、俺たちの性の戦いのために国という概念を乗り越えることができていなかったら、待っているのは大混乱だ"


ke "誰がどちらの側につくのか、誰もわからない。対フェミニズムの戦争はただの第三次大戦じゃない、地球上に現存するあらゆる生命の終わりだ"


ke "俺たちが負ければ、我らが柔順な大和撫子はみんなソシオパスのレズビアン至上主義者に強姦されて、奴隷にされてしまうんだ"





ke "その間に、戦争で死ななかった一握りの男たちは去勢されて、トイレの修理とフェミニストの勝利を記念する巨大なモニュメント建造を強いられるんだ"



hi "おかしいだろそれ。お前おかしいだろ。考えすぎだと思うぞ"





ke "日が経つごとに、お前はつくづくいけてない奴だって思うぜ"






hi "まだ４回くらいしか話してないけどな、俺ら"


show kenji neutral
with charachange


ke "ああ。悪い"


hi "なんでもいいよ。お前の郵便は取ってきてやるから"

show kenji happy
with charachange


ke "助かるぜ"

play sound sfx_doorslam

stop music fadeout 0.5

scene bg school_dormhisao
with vpunch


"俺はドアを閉じ、またベッドに飛び込む。"

play ambient sfx_alarmclock


"頭を枕に乗せたとたんに、ひどくやかましいベルの音が耳を刺し、それが目覚まし時計だと気づく。目覚ましが今鳴るということは、そもそもこの時間に起きていなきゃいけないということだ。"


"少なくとも平日なら。"

play sound sfx_impact


"目覚まし時計を拾い上げて、見もせずに放り投げる。ベッドと壁の間にはまりこみ、音は鳴り続ける。というか、どんどん音が大きくなっているようだ。"

stop ambient




"時計を掘り出したころには、もう寝直せないほど目が冴えてしまうのはわかりきっている。今できることといえば、町に行って健二のふざけた郵便を受け取りに行くことだけだ。でもそれにはまだ時間が早すぎる。"




"シャワーを浴びてから薬を飲む。昨日夕食を食べなかったし、その前の昼飯もとても軽かったので、今日はとても腹が減っている。"


"羊の足か何かのように、ぼりぼりと薬をかみ砕いて食べる。信じられないくらい苦くてまずい。"



"まあ、良薬は口にまずい、だったっけ。まだ腹は減っているし、時間はたっぷりあるので、町に出て朝ご飯を食べられる場所を探すことにする。"



"前にいつ外で食事をしたか思い出せないし。それに天気もいいし。行ってやろうじゃないか。"




scene bg school_road
with locationskip

play music music_soothing fadein 3.0



"町に行く道は覚えていたよりも長かった。しばらくぶりだったのと、一人で来ることがめったになかったからだろう。時間が早すぎるので、道を走る車もほとんどなくて、いつにない静けさだ。"


scene bg suburb_roadcenter
with locationchange


"最初に食事ができる場所を探す。真っ先に上海が思い浮かぶけど、サンドイッチやケーキよりはしっかりしたものを食べたい。"



"まだ時間はかなり早いけど、先に健二の荷物を受け取りに行くことにする。"




"郵便局で荷物を受け取るのはすぐに終わったけど、その荷物を見た瞬間に、こんなものを学校まで持って帰るのかと激怒する。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

show kenjibox:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"その箱は巨大で、両手を使わないと持てない。腹立たしいことに、大して重いわけでもない。"





"しばらくその辺を散歩しようと思っていたのに、これを持ち歩きながらというのは大問題だ。これでは上海に行くしかないみたいだな。"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

show kenjibox:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide kenjibox
with None


"他の店はどこも閉まっているし、そうでない店もメニューに大した違いはない。そのこともあって、優子さんの仕事に少し貢献してあげたいという気持ちになる。"

stop music fadeout 4.0

scene bg suburb_shanghaiext
with locationchange


"ドアを開けて中に入ろうとする前に、誰かが後ろから肩を叩く。振り向くと静音がいる。本能的にミーシャの姿を探すけど、ここにはいないようだ。"

show shizu adjust_happy at center
with charaenter


ssh "おはよう"


"手話のクラスは早くも役に立っているみたいだ。すぐに手話で返事をしたくなるけど、そうすると俺が自分の実力以上に手話を理解していると思われてしまうかもしれない。"







"とりあえず、静音に手を振るだけにしてドアを開ける。静音も朝の紅茶を飲みに来たのであって、わざわざ俺に挨拶しにここに来たわけじゃないだろう。俺について店内に入ってくるので、実際その通りだったとわかる。"


play sound sfx_storebell

scene bg suburb_shanghaiint at bgright
with locationchange



"中は完全な廃墟だった。今は混雑する時間というわけではないけど、他に見かけた店には少なくとも何人かは客がいたぞ。"





"実際通りかかるたびに見ているけど、上海はいつも客が入っていない。これでどうして商売を続けていられるんだろう？"




show yuukoshang happy_down at center
with charaenter


yu "いらっしゃいませ、こんにちは！　ご来店ありがとうございます！"

show yuukoshang neurotic_down at Transform(ypos=1.25)
with Dissolvemove(0.2)

play sound sfx_impact
with vpunch

with Pause(0.3)

show yuukoshang neurotic_down at center
with charamove


"斧を振り下ろすかのような速度で優子さんがお辞儀をする。そのとき俺が抱えていた箱が頭に当たって、地面に落ちてしまう。"

play music music_comedy

show yuukoshang panic_up
with charachange


yu "大変、ごめんなさい、ほんとにごめんなさいごめんなさいごめんなさい、本当に申し訳ありません！"


hi "大丈夫ですよ、あと『ご来店ありがとうございます！』はなくていいですから。もう優子さんとは知り合いだし"

show yuukoshang worried_up
with charachange


yu "でも、それも私の仕事だから"

show yuukoshang worried_down
with charachange


yu "今日は早いのね。ご注文は？"


hi "とりあえず、コーヒーだけで"

show shizu invis at right
with None

show yuukoshang worried_down at twoleft
show shizu behind_blank at tworight
show bg suburb_shanghaiint at center
with dissolvecharamove


"静音はなにを頼みたいんだろう。ミーシャがいないと、それを知る手段もないし、本人に聞くことさえできない。その辺はまだ手話クラスで教わっていない。ここにいるってことは、静音も何か頼むつもりなのは確かだ。"


hi "ええと、俺は静音の注文は知らないんです。静音にもいつもの注文ってあるんですか？"


hi "ああでも、他のものを頼みたいと思ってるかもしれないな。念のためメニューをもらってもいいですか"


"メニューを探してあたりを見回すけど、多少なりともメニューっぽく見える物体は一つも見あたらない。"




show yuukoshang neurotic_up
with charachange


yu "メニューは……すぐに探してくるね"


hi "は？"

show yuukoshang worried_up
with charachange


yu "あの……メニューはあるの。ただ……レアなだけで"


"ただのレストランのメニューじゃないか。特別限定版とかじゃないんだぞ。"

show shizu basic_normal2
with charachange


shi "……"


hi "変なの"

show yuukoshang neutral_down
with charachange


yu "静音ちゃんがそう言ってるの？"





hi "いえ、静音には聞こえてないですよ。ただ、わざわざメニューを探し回らないといけない喫茶店っていうのはへんてこだな、って"

show yuukoshang worried_up
with charachange


yu "へんてこ……?"

show yuukoshang neurotic_down
with charachange



yu "そうだわ……その通りよ。全然理屈に合わないわ。そんなことばっかりよ……"
yu "たとえば、どうして店の名前が上海なの？　洋風の喫茶店なのに……名前は中国風だし……それに建物は古いけど、私の制服はこんなに今風であかぬけてるし……"



"優子さんは今にも気絶しそうだ。そうしたら前のめりに倒れて、大変なことになるだろう。"

show yuukoshang panic_up
with charachange


yu "私、もうここで働けないわ"


"思考がぐるぐる回ったあげくに、よりにもよってとんでもない結論にたどり着いてしまう。"




hi "いや、待ってくださいよ。この辺にはいっぱい喫茶店があるけど、そういうところがあるからこの店が際だつんですって。いけてると思いますよ、ほんとに"
hi "お願いだからやめないでくださいよ。ほら、商売だって順調なんでしょ？"



show yuukoshang worried_up
with charachange


yu "そうでもないの……"


hi "やっぱり、ここは優子さんにぴったりの職場だと思いますよ。お似合いですから、やめちゃだめです"



"こんな危機的状況を丸く納める羽目になったのは生まれて初めてだ。"




stop music fadeout 2.0






"最終的にはどうにか優子さんを落ち着かせて、静音が欲しいのは普段頼んでいる品だろうと説得することができた。"




hide yuukoshang
with charaexit

show shizu basic_normal2 at center
show bg suburb_shanghaiint at bgleft
with charamove

show shizu basic_normal2:
    ypos 1.15
with charamove


"優子さんは飲み物を用意しにその場を離れる。そのころには静音が席を選んでいた。"

play music music_dreamy fadein 4.0


"他には客はいない。優子さんもおしゃべりな方ではないから、店内はとても静かだ。"



"俺は気にはしないけど、静音とコミュニケーションをとる手段があればよかったな。俺たちが二人きりになれる機会はとても少ない。静音とミーシャはほとんど常に一緒にいる。時には一心同体かと思えるくらいだ。"



"そして今、ここには俺と静音しかいない。そして俺は静音を理解できず、静音に俺を理解してもらうこともできない。ひどい話だ。"


hi "今日はあの小さいメモ帳持ってないのか？　週末だからってのはあるけどさ、そういう準備をしてないってのはお前らしくないな"


hi "まあ、いいよ。メモ帳を使うのはあまり好きじゃないし。ただこういうときは役に立っただろうな"

show shizu behind_blank
with charachange


shi "……"

show shizu basic_normal
with charachange


shi "…… ……"


"静音は手話をし始める。短い早口のように手を動かし、紅茶を一口飲むたびに手を休める。普段とは振る舞いを変えるという意志が全く見えないので、おかしな感じがする。"


"俺が静音に向かって話しかける理由の大部分は、自分が長い沈黙に慣れていないせいだ。ふと、ある意味それは静音にとっても同じなのだろうか、と思う。でもそれはなさそうだ。"

"どちらかといえば、静音は誰が相手でも振る舞い方を変えないタイプなんだろう。"



hi "なあ、ミーシャはお前がいたから生徒会に入ったみたいだな。俺も同じだよ。お前が無理矢理引っ張りこんだからだけどさ"


hi "いやまあ、ほんとに無理矢理ってわけじゃないか。お前がいなかったら、俺も生徒会には入ってなかった"


"なんかロマンチックな言い方になってしまった。ほのかに頬が赤くなるのを感じる。これじゃ自分が大馬鹿みたいだ。"





hi "でもお前が生徒会に入った理由はまだ聞いてないな。今考えてみると、最初に聞いておけばよかった話だけど、すごく興味がわいてきたよ。ミーシャに聞くって覚えておかないとな"




show shizu behind_blank
with charachange


shi "……"


hi "そっちが理解できないとしても、お前と話すのは楽しいなって思うんだ。お前も同じように思ってるのかな"


hi "もしそうだったら……すごく、いいな"

show shizu adjust_happy
with charachange


shi "……"


hi "ミーシャがやってるみたいに手話を自然に使えるようになるのは、俺には無理だと思うけど、でも紙とペンよりはステップアップには違いないよな？"

show shizu basic_normal2
with charachange


shi "……"

stop music fadeout 4.0


"もう二人とも飲み物は飲み終えていた。静音は俺の横の椅子に乗せてある箱に目を落とす。"


show shizu adjust_happy
with charachange


shi "……"


hi "人に頼まれて受け取ってきただけだよ、俺のじゃない"

play music music_running fadein 0.5

show shizu basic_sparkle
with charachange


"静音が箱を開けようとして自分の方に引き寄せるので、俺は心臓が口から飛び出しそうになる。あわてて椅子を自分の足で引き寄せて、取り戻そうとする。"



hi "何やってるんだよ、開けちゃだめだろ。人の郵便物を勝手に開けるなよ。違法だぞ、それ"

show shizu basic_frown
with charachange


shi "……"


hi "だめ！"

show shizu cross_angry
with charachange


shi "……！"


"一度こうと決めたら、静音を止めることはできない。目つきは興奮で満ちていて、このくだらない箱を巡って争う気でまんまんだ。これではあっという間に綱引きのような事態になりかねないことに思い至る。"




show shizu behind_frown
with charachange


"ほとんど席からずり落ちそうになって、航空管制官みたいに腕を振り回していると、ようやく静音は矛を収める。"




show shizu behind_frown at center
with charamove


"好奇心を満たすことができずに不機嫌な静音は、頬を膨らませて席を立つ。"


"そろそろ戻る時間か。結構長く居たし。俺は立ち上がる前に、用心深く箱を持ち上げる。"

show shizu basic_happy
with charachange


"突然、静音が興奮したように手を合わせると、ポケットからマーカーを取り出して健二の箱になにやら書き込む。"


hi "ちょっと、何してるんだよ！　俺のじゃないって言ってるだろ！"


hi "おい！"


"箱で視界がさえぎられて、静音の姿も見ることができない。"


hi "わかったよ、とりあえず下におろすから"


"何を書いたのかは見ないといけないしな。"

window hide


$ written_note("運ぶの手伝ってあげる。", {"background":Frame("vfx/cardboard.jpg",0,0, tile=True)})


show shizu adjust_smug
with charachange

window show


"まだ書き終わっていなかったようで、静音はその後ろに荒々しく線を引いて、何か裏があることを示す。"

window hide


$ written_note("運ぶの手伝ってあげる。\n ___________________\n\nただし、勝負！　最初によろけた方が負け、負けた人は一人で最後まで持って行くこと。", {"background":Frame("vfx/cardboard.jpg",0,0, tile=True)})

window show


hi "そんなバカな話があるかよ。それじゃあ５０％の確率で俺が一人で運ぶはめになるじゃないか"


"正直、もうすでにバカみたいな気分になっている。静音には俺の声が聞こえないのを度忘れしていた。俺はしゃべるのをやめて首を振る。"

show shizu behind_blank
with charachange


shi "……"

show shizu cross_angry
with charachange


shi "……！"

show shizu adjust_angry
with charachange


shi "……！"


"静音が何を言っているのかさっぱりわからないけど、とても強い勢いで訴えかけてくる。明らかにこれがいい考えだと思っているようだ。"


"まあ、もしこの箱だかなんだかを落としたら、静音が一人で運ぶことになる。どう考えても俺にとってはその方が楽だ。"


"可能性は半々、だったら……それ以外に静音が考えそうな企みに比べれば高いに違いない。いいだろう、乗ってやる。"

show shizu basic_normal_close
with characlose


"考えてみれば、これはどうやって運べばいいんだろう。すると静音は箱の片側をつかんで持ち上げる。俺は反対側を持つ。こんなのでいいんだろうか？　これじゃとても歩きづらい。"

show bg suburb_shanghaiext
with locationchange


"俺たちは上海を離れる。道に人がいないことを願っている自分がいる。優子さんは俺たちのやっていることを見て戸惑っていたようだし、これ以上目撃者が増えたら、事態はよけいに悪くなるだろう。"

show shizu adjust_happy_close
with charachange

show shizu basic_normal_close
with charachange


"腕を不自然な角度に曲げたまま歩いていても、静音は全く気にならないようだ。自信たっぷりの笑顔を浮かべて、時々おかしな手振りを見せる。"

show bg suburb_roadcenter
with locationchange


"やがて人々がこちらをじろじろ見始めるようになり、いつもの朝の通行人で道がいっぱいになる。"


"間抜けな気分になってくるけど、今ギブアップしたら静音に降参の合図と受け取られるに違いない。ここまではうまくやっていると思うし、そんなことを認めるわけにはいかない。"




show shizu adjust_happy_close
with charachange

show shizu basic_normal_close
with charachange


"最初は、静音の手振りは単に勝負がつく前から勝ち誇っているだけだと思っていた。でもすぐに、静音は自分の行きたい方向を知らせているのだと気づく。"



"これは競争なんかじゃない、ということに徐々に思いいたる。"

"そもそも大して難しい話じゃないし、それにこれはどちらかといえば共同作業だ。ただ、静音は成功したらご褒美を出すかわりに、失敗したら罰を与えることにしたというだけだ。"


stop music fadeout 3.0

show shizu adjust_blush_close
with charachange


"箱の底でお互いの指が触れ合って、静音は手を遠ざける。そのおかげで静音は箱を落としそうになる。"


"まあ、これで静音はゲームオーバーだな。"


"静音は不機嫌そうな感じだ。俺が静音を負けさせるためにわざとやったと思っているんだろうか？　そうだとしても、大して気にしてはいないようだ。『恋と戦争は手段を選ばず』ってな。"




show shizu basic_frown
with charadistant


"箱を引き取って俺が運ばないといけない気がする。でもそうしようとすると、静音に押し戻される。"

play music music_shizune fadein 1.0


"俺に説教するかのように静音がにらみつけてくるけど、実際にはできない。両手で箱を持っているので、口をふさがれているようなものだ。"

show shizu basic_normal2
with charachange

show shizu basic_normal
with charachange


"悲しげな表情がちらりと静音の顔に浮かぶ。たぶん、そのことに気づいたのと、自分はこうした制約を受け入れなくてはいけない、ということを自覚させられたからか。"


"それでも、静音はこれ以上ないくらい誇りに満ちている。そのおかげで自分が損を被る状況だというのに。賭けに負けたのを俺が見逃すことを静音は認めない。"


"勝負にあっては禁じ手なし、ただし結果は文字通りに受け入れるべし、か？"





"静音は面白いタイプの人物だな。"

show bg school_dormext_full
with shorttimeskip


"寮までの行進は何事もなく終わる。道中、静音は巨大なルービックキューブのように時折箱をくるくると回して時を過ごす。また暇つぶしに思いついた遊びのようだ。"


"中身にはいいとは思えないけど、俺もどうでもいいと思ったので放っておく。"



"これが静音なりの物事のこなし方なのかもしれない。何もかも勝負事にしてしまう。確信は持てないけど。"






"静音を精神分析しようとするのは無駄な努力みたいだ。知り合ってからの短い間、俺は何度も驚かされている。"

show shizu basic_normal2 at centertremble_nl
with None

stop music fadeout 6.0



"静音がふるえているのに気づく。風が強くなっているし、学校も結構高いところにある。寒がっているのもうなずける。でも俺の上着を渡したら、静音は拒否するだろうか？"




play sound sfx_rustling

show shizu basic_normal2_close at center
with characlose


"俺は上着を脱いで、文句を言われる前に静音の肩にかける。その肩はあまりに細くて華奢で、ずっと手で触れていたくなるほどだった。"



show shizu adjust_blush_close
with Dissolve(0.2)


"俺の指が触れたとき、静音は驚いたようにびくりとする。"


hi "ごめん"

show shizu basic_normal_close
with charachange


shi "……"

show shizu adjust_happy_close
with charachange


shi "……"


"静音の指が箱の上で軽やかに動く。箱を引き取るべきかと思ったけど、そうはさせてくれないだろう。静音はかろうじて素早い手振りを見せる。その後で手を止めたのは、もっと言いたいことがあったからだろうか。"


"今のは間違いなく『ありがとう』だ。ちゃんと読みとれてよかった。"

scene black
with dissolve

$ suppress_window_after_timeskip = True


label jp_S11:

window hide None

scene bg school_cafeteria
with locationchange

nvl clear

nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_normal fadein 0.5


n "\n\n手話の先生によくやっているとほめられた。"


n "あまり考えすぎないよう努力はしているけど、実はここ最近手話のことで頭がいっぱいで、１日に何度もそのことを考えずにはいられないくらいだ。思ったよりも早く身につき始めているんだろうけど、でもまだまだだ。"




n "手話を読みとるのは問題ない。それだけなら簡単だ。まあ、読むときは集中しないといけないけど、集中さえしていれば十分簡単にできる。"


n "自分で手話をするのも何とかなる。もっと練習が必要なだけだ。でも両方を同時にやるとなったら？　ミーシャの半分の速さでも不可能だ。"



n "俺のレベルからすれば、今の状態は上出来といえる。でも静音と本当に会話できるところまでたどり着くには、もっと努力しないといけない。"


n "\n１歩ずつ着実にそこにたどり着くために、俺は全力を尽くしている。昼休みにできる限りのことを詰め込んでいるんだ。"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

nvl hide dissolve

window show


"『手話入門』の教科書から顔を上げて、静音やミーシャがまわりにいないか確かめる。"





"もちろん、昼休みの時間を勉強につぎ込んでいるので、この数日間あの２人を避け続けるはめになっている。しかも、静音に知られないようにするなら、ずっとこんなことを続けないといけない。"


"背中を角に向けて、１０分おきに辺りを見回していると、追っ手から逃げようとしている犯罪者のような気がしてくる。"



"……"



$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl show dissolve

nvl clear


n "\n\nミーシャは俺の顔を見るたびに、手話を勉強していることを静音に隠す理由を聞いてくる。"


n "思い返してみると、あのときはこれといった理由なんてなかった。でも今はわかる気がする。"



n "静音が俺のことを本当に対等な存在として見てくれるためには、手話を身につけるのは大事なステップだ。"











n "俺が静音と対等な相手として付き合いたいなら、手話を身につけるのはそのための大事なステップだ。"







n "もう１つ大事なステップは、静音に知られてはいけないということだ。最終的に対等な立場で話し合えるようになったときに、俺自身がきちんと準備ができていて、正しく話せるようにしたい。遊びじゃだめなんだ。"





n "そうでなければ失礼だ、と思う。静音もそう考えるだろう。"


n "\nだから俺にとっては、これ以外に選択肢はない。自分でこんなに強く決意したのだから、なおさらだ。"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

nvl hide dissolve

window show



"静音は巨大なオーラをまとっている。目に付くのはもちろん、やってくるのが感覚でわかる。主にミーシャの髪が周りの人混みを灯台みたいに明るく照らすからだけど。それにあの笑い声は１キロ先からでも聞こえるし。"



"でも、ミーシャが一緒でなくても同じことだ。率直さと勤勉さは静音の核心なのだから、あいつが歩くにつれてそれが伝わってくるのは驚くことじゃない。"





"こうした諸々の事情のおかげで、２人がこちらを認めて近づいてくるまでの間に、俺は余裕を持って自分の荷物をまとめて、いかにも普段と同じような表情を作ることができた。"




show shizu behind_smile at tworight
show misha perky_smile at twoleft
with charaenter


hi "よう"

show shizu adjust_smug
with charachange


ssh "生徒会～"

show misha hips_grin
with charachange


mi "せいとかい～！"


"役に立ちそうだと思ったから、『生徒会』は真っ先にやり方を習っていた。"


hi "ああ、しばらくそっちからは逃げ回ってたよなあ"

show misha sign_smile
show shizu behind_smile
with charachange


mi "そうだよ～！"

show shizu behind_smile_close at closeright
show misha perky_smile_close at closeleft
with characlose

show shizu behind_smile_close:
    ypos 1.07
show misha perky_smile_close:
    ypos 1.1
with charamove

stop music fadeout 3.0


"静音が俺の正面右手に座り、ミーシャは左に座る。部屋の隅に座るのは間違いだった。今の俺はまさに『袋のネズミ』だ。"



scene bg school_lobby
with shorttimeskip


"結局、俺は生徒会室に引きずられていく。でも構わない。そろそろこの２人に会いたくなり始めていたところだし。"


"ある意味、このおかげで話が楽になったともいえる。俺を捕まえたことに満足して、静音は俺が今までどこにいたのかを聞いてこない。"


"ドアの前に立ってみて、そこまで熱心に俺を引っ張り戻そうとするほどの大事な事情とはなんだろうと考える。"

scene bg school_council at bgright
with locationchange


hi "ゲームか"


play music music_another fadein 0.5


"部屋の中のゲームの数は本よりも多い。俺が来るたびに、すべての机と、時には床の上にまで本が積んであった理由がやっとわかった。これだけのゲームをしまう場所が必要だったんだ。"

show misha cross_laugh
with charaenter


mi "ははは～！"

show misha hips_grin
with charachange


mi "２人きりで遊び続けるのってつまんないんだよ、ひっちゃん。だから今度はひっちゃんの番だよ、いい？　おっけ～！　じゃあ決まりだね～！"


hi "俺まだ一言もしゃべってないぞ！"

show shizu invis at right behind misha
with None

show misha hips_grin at twoleft
show bg school_council at center
show shizu basic_normal at tworight
with dissolvecharamove

show shizu behind_blank
with charachange


shi "……"

show misha sign_smile
with charachange


mi "ひっちゃん、もう少ししたら、今みたいにゆっくりできる日はしばらくお預けになっちゃうの。だから～、今のうちに楽しんでおくのがとっても大事ってわけ。そう思わない？"


show misha cross_smile
with charachange


mi "もうすぐ七夕だから、わたしたちもいっぱい仕事しないといけないの"

show misha hips_grin
show shizu behind_smile
with charachange


mi "だから、今はいっしょに遊ぼ～！"


"考えてみれば、その通りだ。手話を学ぶことに夢中になりすぎて、全く気がついていなかった。お祭りが１つ過ぎたとたんに、もっと大きな祭りがやってくる。"


"その手伝いに、静音はもう何人か新メンバーを捕まえようとするだろうか。"


hi "そうだな"

show misha cross_laugh
with charachange


mi "ははは～！　やったあ～！　ひっちゃんもそう思うって～！　お祝いしよう！"

show shizu basic_happy
with charachange


ssh "そうだわ、ゲームをしましょう"

show misha sign_smile
with charachange


mi "お祝いにゲームしようよ、ひっちゃん～！"


hi "どうだろうなあ、そういうのって結局俺が痛い目を見て終わることが多いし"

show misha perky_sad
with charachange



mi "ひっちゃんは賭けるものが心配なんだ～"







"ミーシャがとても残念そうな顔をする。いつでもすごく大げさな表情をするので、からかっているのか、それとも本気なのかを見極めるのが難しい。ミーシャはどんなときでも全力を出す子だからな。"


"静音に顔を向ける。さてと、こいつは間違いなく俺をバカにしているな。"



hi "おいやめろよ。でもそうだな、先に何を賭けるつもりなのか教えてくれたら、ゲームしてもいいよ"

show shizu adjust_smug
with charachange


shi "……"

show misha cross_grin
with charachange


mi "すごく日本人的ね、何よりも結果のことを重視するって"



show misha sign_smile
with charachange


mi "ひっちゃん、『木を見て森を見ず』って言葉、聞いたことある？"


hi "ないよ"


"今のは嘘だ。でも俺にもプライドがある。今のところ傷つけられているけど。"


hi "わかったよ、つきあってやる。でもゲームは俺に選ばせてくれ"

show shizu adjust_happy
show misha perky_smile
with charachange


"ミーシャはうなずく。"


hi "それと、そっちが負けたら俺が罰ゲームを決めるからな"



show shizu cross_angry
with charachange


"静音は腕で×印を作る。それは『拒否』の意味なのか、何か必殺技を出そうとしているのか。"


hi "おっと、負けるのを怖がってるのはどっちだ？"


show shizu behind_frown
with charachange


ssh "ほんとに執念深いのね、ほんの軽い冗談なのに、いつまでも根に持つなんて"


show shizu basic_frown
with charachange


ssh "もしあなたが……に噛まれたら、きっと噛み返すんでしょうね"




"今の静音の手話に、１つ読みとれない単語があった。"





show misha hips_frown
with charachange


mi "ひっちゃんはほんとに根に持つよね～、ちょっとした冗談だったのに。たぶん、アルマジロに噛まれてもひっちゃんは噛みつき返すんだろうね！"


hi "アルマジロ？"

show misha sign_smile
with charachange


mi "アルマジロに噛みつき返すなんて、おバカさんだよ、ひっちゃん！"

show shizu behind_blank
with charachange


shi "……"

show misha cross_laugh
with charachange


mi "でもどうせひっちゃんはやり返しちゃうんだよね～！　ははは！"


hi "なるほどな"

show shizu adjust_smug
with charachange


"静音は小さな手振りとともに眼鏡を直す。"

show shizu behind_smile
with charachange


shi "……"

show misha sign_smile
with charachange


mi "ひっちゃん、勝ち負けの結果で何かしたりさせたりとか、そんなことは全然考えてないってば。そういうことがあるだろうって、ひっちゃんが思い込んでただけだよ～"


hi "そりゃどうしてだろうなあ"

show misha hips_grin
with charachange


mi "んん～、どうしてだろうね～！　でもまあいいか～！　そういうのはありませんから。これで気が変わったかな、ひっちゃん？"


hi "まあ……そうだな"

show misha hips_laugh
with charachange


"ミーシャは嬉しさで腕を風車のようにぐるぐる振り回す。おかしな癖だ。たった３人しかいない生徒会室の中でしか、こんな光景を見ることはできないだろう。"


"ここ以外の場所だったら、人の顔を殴り付けてしまうに違いない。"

show misha hips_grin
with charachange


mi "やったやったぁ～！　じゃあ今すぐ始めよ～！"


hi "まあちょっと待て"

show misha hips_smile
with charachange


mi "……"

show shizu behind_blank
with charachange


shi "……"


mi "……"


shi "……"


hi "わかった、わかったよ"


hi "ただし、俺たち全員にできるゲームじゃないとだめだぞ。それが条件だ"


hi "誰か１人が最初からすごく上手いとか、２人しかプレーできなくて残った１人は後ろで見てるだけとか、そういうゲームは好きじゃない。俺たち３人が公平に遊べるゲームじゃなきゃだめだ"

show shizu basic_normal
with charachange


shi "……"

show misha sign_smile
with charachange



mi "チェッカーは？"



"そう言ったとたんに、ミーシャはチェッカーの駒が入った袋を机の上に出す。"



hi "２人しか遊べないじゃないか。今言っただろ――"


show misha hips_grin
with charachange


mi "おっけおっけ～！　それじゃあひっちゃん……モノポリーは？"


"モノポリーの箱がゆっくりと俺に向かってにじりよってくる。俺はその箱をミーシャの手から奪って、椅子の下に置く。"


hi "運任せのゲームは好きじゃないんだ。実力は関係なくて、関わるのは偶然だけだからな。それにそうやって決める前からゲームを出すのやめろよ！"




show misha perky_confused
with charachange


mi "運も実力のうちなんだよ"


hi "違う、そんなわけあるか！"

show shizu adjust_smug
with charachange


shi "……"

show misha sign_smile
with charachange


mi "いつも運がよければ、そうとも言えるかもね～！　でしょ～？"


hi "そこまで行ったら、まるっきり別の話だろ"

show shizu adjust_happy
show misha hips_grin
with charachange


mi "う～ん、う～ん、う～ん、う～～ん。バカラは？　ビー玉は？　人生ゲームは？　すごろくは？　ルーレット？　ブラックジャック？　紙フットボール？　トリビアル・パースート？"


"ミーシャは興奮しながらいろんなゲームの名前を出し始める。まるでリストを読み上げてるみたいだ。"


"名前が上がるたびに新しく箱やボードや駒が現れる。子供向けから、この慎ましい部屋には非常に場違いな、本物らしきピカピカに光るギャンブル用具まで。まるで奇妙なゲーム博物館だ。"


show misha sign_smile
with charachange


mi "３面チェスは？"


hi "そもそもそんなことができるのか？"

show shizu behind_smile
with charachange


ssh "試してみよう"

show misha cross_laugh
with charachange


mi "うんうん～、やってみようよ、本気で～！ あはははは～！"

show shizu basic_happy
show misha hips_grin
with charachange


"２人は子供マジシャンのコンビのように、気取った手つきで背中からチェス盤を取り出す。まあ確かに、マジックには手先の器用さが必要だし、その意味ではこの２人はとびきりだ。"


"俺は驚かないけど、それでもなんだか胸騒ぎがする。"


hi "それやめろっての！"

stop music fadeout 2.0


ha "す、すみません……"


show shizu basic_normal
show misha perky_confused
with charachange


"とても気弱そうな声に気づいて、俺は顔を上げる。"

show hanako invis at offscreenright
with None

show misha perky_confused at left
show shizu basic_normal at center
show bg school_council at bgleft
show hanako emb_downtimid:
    xanchor 0.7 xpos 1.0
with dissolvecharamove


ha "学生証をな、なくしちゃって、ここに来れば新しいのをどこでもらえるか教えてくれるって聞いて……もし、な、何か都合が悪かったら、また来ます"




show hanako emb_timid
with charachange


"華子の視線が部屋の中を漂い、積み上がった台帳や、散らばっている椅子、ひっくり返ったゲーム盤を認める。"


"俺たちみたいな、段取りよくてきっちりしている生徒会が見せるべきイメージとはちょっと違うよな。"


hi "よう"


"沈黙を破る言葉としては、それしか思い付かない。あいにく、華子は余計に驚いてしまったようだ。"

show hanako def_worry
with charachange


ha "……"

show hanako def_strain
with charachange


ha "あの……{w=0.5} 学生証……{w=0.5} 私……"

show misha sign_smile
with charachange


mi "あなた、わたしたちと同じクラスだよね、そうでしょ？　だよね～！　だから～！　そんなに怖がらないで、ね？　こっちおいでよ！"

show shizu behind_smile
with charachange


shi "……"

show misha hips_grin
with charachange


mi "そうだよ、わたしたち先輩だけど、噛みついたりとかしないから！"


hi "先輩じゃないだろ、同じクラスなんだから"

play music music_happiness fadein 3.0


"それでも、２人が話に入ってくれて助かった。"

show misha hips_smile
with charachange


mi "なんて言ったっけ？　学生証だっけ～？　だよね～！"

show hanako basic_distant
with charachange


ha "うん"




"華子はミーシャから目をそらす。内気な性格だし、アイコンタクトを保つのが苦手なのは不思議じゃない。見ている先をたどると、テーブルの上のチェス盤で華子が目を止めるのに気づく。"

show hanako basic_normal
with charachange

show hanako basic_distant
with charachange


"ほんの一瞬だけど、華子が目を大きく開く。静音もそれに気づく。"

show shizu basic_happy
with charachange


shi "……"

show misha perky_smile
with charachange


mi "チェスが好きなの？"

show hanako defarms_strain
with charachange


ha "えっ！？"

show shizu adjust_smug
with charachange


shi "……！"

show misha hips_smile
with charachange


mi "チェスが好きなんでしょ～！　うん、きっとそう、ぜったい～！"

show misha hips_grin
show shizu adjust_happy
with charachange


mi "あ～{w=0.2} そ～{w=0.2} び～{w=0.2} た～{w=0.2} い～？"


"ためらっている。このまま逃げ出してしまうかもしれない。かかわり合いになるのはごめんだ。きっとろくなことにならない。"

show hanako basic_normal
with charachange


"ところが驚いたことに、華子はこの話に乗るべきか真剣に考えているみたいだ。両手の指先を触れ合わせて、じっくりと思慮を重ねている。"





"華子の念入りな考えぶりが、その証明のようなものだ。"



show misha sign_smile
with charachange



mi "今はお昼休みだから、どっちみち待ってもらわないといけないの。だから待ってる間、一緒に遊ぼうよ～！　きっと楽しいよ～！　チェス好きなんでしょ？　見ればわかるよ、ほんとほんと、だから、お願い～。ね？"


show hanako cover_distant
with charachange


ha "う、うん……"




show misha cross_laugh
with charachange


mi "わはは～！　やった～！　大成功、おっけおっけおっけ～！　すご～い！"

scene ev shizu_chess_large:
    subpixel True xanchor 1140 yanchor 1100 xpos 400 ypos 300 zoom 1.0
    easein 10.0 yanchor 1050
with flash




"チェス盤が準備される。"


"最初の１手が肝心だ。"

show ev shizu_chess_large:
    ease 1.0 xpos 400 xanchor 1400 yanchor 400 ypos 300
    acdc_warp 10.0 xanchor 1300


"でも静音は気にする様子もない。"

show ev shizu_chess_large:
    ease 0.5 xanchor 800 yanchor 360
    easein 10.0 xanchor 700 yanchor 360


"華子は指し手を注意深く考える。駒を少しだけ前にずらしたかと思うと、決心しきれずに手前に戻し、何度も何度も考え直している。"





"本当に夢中になっている。華子のことをにわかなどとは呼べない。間違いなく熱烈なチェス愛好家だ。"





"静音もいい加減に応じることはできない。どんな動きをしても、華子は的確に手を返してくる。"


"それでも、このゲームのペースは何かがおかしい。"

scene ev shizu_chess_base:
    truecenter subpixel True zoom 1.05
    easein 5.0 zoom 1.0
with flash



"静音の指し手は速すぎる。いや、それどころじゃない。有り得ない速さだ。まるで次の１手を考えてさえいないみたいだ。静音はスーパーコンピューターの域に達しているのか、それともまじめにやる気がないのか。"



"あるいは、華子があまりうまくないだけなのかもしれない。"

scene ev shizu_chess_base
show sc_shiz normal:
    xalign 1.0 yalign 0.0
with charachange


"静音はポーンの交換を強制する。"





scene ev shizu_chess_base3
with charachange



"ゲームが進むにつれ、華子の手番はどんどん長引いていく。まだそれほど時間が経ったわけじゃないのに。"

"そのとき不意に俺は気づく。華子が１手を指すのに長々と考えているおかげで、静音は次の手を考える時間がたっぷり取れるんだ。"



"そのことを抜きにしても、面白い勝負だ。"

window hide

nvl clear

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl show dissolve


n "\n\n黒のナイトをｆ６へ。"


n "ビショップをｄ３へ。"


n "２人とも真剣に指しているから、いい加減な手は打たない。どちらもはっきりと優勢なわけではない。少なくとも今のところは。俺が見る限り、２人があまり親しくないこともその一因なのかもしれない。"


n "静音は華子にとって得体の知れない相手で、華子は静音にとって未知の相手だ。眉間にしわを寄せる華子の表情で、勝負に没頭しているのがわかる。華子は本当に勝ちたいと思っている。そして静音はいつでも勝ちを狙うやつだ。"


n "２人が親しくないというのはちょっと気が重くなる。でもそのおかげで勝負が活気づいているし、２人ともお互いのことをいい対戦相手として認識できている。"


n "終わってみれば２人は友達になっていた、なんてことになるかもしれない。さもなければチェスのライバルとか。楽観的な考えだけど。"


n "ただ静音とリスクをやったときのことを思い返すと、彼女は面白半分で相手を叩き潰すようなことはしないだろう。"

nvl clear


n "\n\n\n勝負は続く。"


n "静音は４分の間に１２手を指す。なんて恐ろしいプレイヤーだ。"


n "キングがちょっと盤上を追い回されているけど、それでも華子はなんとか持ちこたえる。"


n "ポーンをｈ６へ。"


n "白のナイトをｅ６へ。"


n "終わりは近い。"



n "\n\n……"


stop music fadeout 3.0


n "勝負がついた。"

nvl clear

nvl hide dissolve

scene bg school_council
show shizu adjust_happy at center
show misha perky_smile at left
show hanako basic_normal at right
with locationchange

window show


shi "……"

show misha sign_smile
with charachange


mi "すごくいい勝負だったね～！"

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_ease fadein 5.0

show hanako cover_bashful
with charachange


ha "あ、ありがとう……"

show shizu behind_smile
with charachange


shi "……"

show misha hips_smile
with charachange


mi "接戦だったよ～、負けちゃうかもしれないって思った。すごく上手だね"


"勝っても寛大に、そして敗者に手をさしのべる。華子が自分の負けを素直に受け止めているからだろうか。"


show shizu basic_normal
with charachange


shi "……"

show misha perky_smile
with charachange


mi "楽しかったけど、すごく時間がかかったね。もう授業が１コマ過ぎちゃう！"



mi "チェスはパターンばっかり、このレベルになるとなおさらそう。上級ルールでやってみない～？"





hi "なんだって？"

show hanako cover_worry
with charachange


ha "上……級……？"

show shizu basic_sparkle
with charachange

show shizu adjust_smug
with charachange

show shizu basic_happy
with charachange


shi "…… …… ……"

show misha hips_smile
with charachange





mi "そうそう～！　早指しとか、駒を増やしたチェスとか、他にも二人で組んでタッグチームチェスとか、盤は１面でも２面でもいいよ、そっち次第！"
mi "ほらほらほらほら面白いから、ほんとほんと～！　普通のチェスはすごくテンポが悪くて型にはまりすぎてて、つまんないの"



show misha hips_grin
with charachange


mi "私は素早い思考と大胆さが報われるチェスがやりたいの！　チェスと今言ったゲームを比べるのは、チェッカーと囲碁とか、○×ゲームと将棋を比べるようなものでしょう？　ね～！"

show misha cross_laugh
with charachange


mi "わははは～！　レーザーチェスだってこれよりは面白いかもね、どれか選んで、選んで～！"



show hanako defarms_strain
with charachange


ha "ああああ……"



"ヘッドライトに照らされた鹿みたいだ。チェス盤の前で今にも気絶しそうな華子を見ながら、様々な感情が生まれる。面白そうというのが一番大きいけど、本当に華子が倒れてしまう事態に備えて、俺は少し近くに寄る。"


scene ev shizu_chess_base2:
    truecenter subpixel True zoom 1.05
    easein 5.0 zoom 1.0
with flash


"盤が再び準備される。でも今度は接戦でさえない。"


"静音と手がぶつかるのを怖がって、華子は駒を動かすこともできない。静音は盤上を埋め尽くしている。猛攻撃だ。華子が指したいと思った場所には、それがどこであれ静音が先回りしている。"


"こんなに早く進む勝負は生まれて初めてだ。"

scene bg school_council
show shizu basic_sparkle at center
show misha hips_grin at left
show hanako defarms_strain at right
with locationchange


mi "じゃあルール変えてもう１回やろう～！　カスパロフとディープブルーみたいに、６つの手から一番いい手を選ぶの～！"

hide hanako
with easeoutright


"華子は席を立つと、一目散に部屋から逃げ出す。"

show shizu basic_normal
show misha perky_confused
with dissolve


mi "あれ？　待ってよ！"

hide misha
with charaexit


mi "あー、学生証を再発行してもらえる場所が聞きたかったんじゃなかったっけ？　ちょっと～！　ねえ～？　戻ってきてよ！　待って、待って～！　待ってってば～！"

stop music fadeout 3.0



"おかしなことに、ミーシャが遠ざかるほど、その声はどんどん大きくなっていってる気がする。"


show bg school_council at bgright
show shizu basic_normal at tworight
with charamove

show misha perky_sad at twoleft
with charaenter


mi "追いつけなかったよ～……"

show shizu adjust_happy
with charachange

play music music_normal fadein 3.0


shi "……"


"静音が慰めるようにその肩を叩く。"


hi "まあまあ"

show misha hips_smile
with charachange


mi "まあまあ～！"


hi "落ち込んでたわりには、ずいぶん元気がいいな"

show misha cross_laugh
with charachange


mi "あははは～！"



"……"


show shizu basic_normal2
with charachange


shi "……"

show misha sign_smile
with charachange


mi "ひっちゃん、偶然がからむゲームは嫌い？"


"出し抜けに質問が飛ぶ。でも大事な質問のような気がする。"



"そうでないなら、どうして静音はこっちを向いて、俺の反応を見ているんだ？　俺が静音をちらりと見ると同時に、静音はチェスの駒を指で回してなんでもなさそうなそぶりを見せつつ、こっちを見ていないふりをする。"


show misha hips_grin
with charachange


mi "『運任せのゲームは嫌い』だよね？　ひっちゃんが言ったんだよ～"



hi "そうだな。でも運任せっていうのは、単に運がからむのとは違うんだぜ。運の要素だけでそのゲームが嫌いになるわけじゃない。どんなゲームにだって運の要素はあるしな。だからこそゲームってのは面白いんだ"



hi "最初から自分がどこまでやれるかわかるゲームはつまらないと思う。そんなのはゲームじゃないだろ？　ただ合図をなぞってるだけだよ"


hi "全然自分の思うとおりにできないゲームがあるとしたら、そういうゲームにははまれないと思う"

show shizu behind_smile
with charachange


ssh "なるほどね"

show shizu adjust_smug
with charachange


shi "……"

show misha hips_smile
with charachange


mi "あの子はあまりチェスはうまくないわ"

show shizu basic_normal
with charachange


shi "……"

show misha sign_smile
with charachange



mi "チェスは定石のゲーム。だから～！　あの子には合わないの……あの子は全然定石を知らなかった。ああいう風に、次の手しか見ないで底の浅い指し方をする人は、真剣なチェスのプレイヤーとは言えないわ"


show misha perky_smile
with charachange


mi "チェス盤を見たときに目を輝かせるくらいにチェスが大好きな人なら、チェスのことをちゃんと勉強するはずよ"


mi "軽く勉強するだけでも、プロ相手だって少なくとも２手先を読めるようになるわ"

show misha hips_frown
with charachange


mi "どうしてあんなにチェスが好きな子が……あれだけ熱心なのに……チェスをまるでわかっていないの？　上辺だけの関心しかない人よりも知識がないなんて"


"静音は手の中の駒を下に置く。ルークだ。"

show shizu behind_frown
with charachange


shi "……"

show misha hips_smile
with charachange


mi "あの子の気持ちは本物だけど、チェスに対する気持ちは本物じゃない。わかる、ひっちゃん～？"

show misha perky_smile
with charachange



mi "チェスに偶然なんてないの～！　それを理解するのはとても大事なの。ゲームの中の偶然はいいことよ、みんなにチャンスを与えるから。ゲームに変化を付ける程度で、うまい人が不利になるわけじゃない"
mi "チェスがつまらないのは、ゲームじゃないから。私にとっては数式みたいなものなの"


show misha sign_smile
with charachange


mi "華子はそういうのが大好きっていうタイプじゃないし～"

show shizu adjust_angry
with charachange


shi "……"

show misha cross_frown
with charachange




mi "何かが大事だと思ったら、人は戦う。戦うことはと――とうとさ？　の証明よ。少なくとも、私はそう思う"


mi "でなければ～！　その場で負けを認めるの～！　あんまりそれが大事だから、思考停止しちゃう。最初のは情熱的な愛情、２つ目は穏やかな愛情よ"


show shizu basic_normal2
with charachange


shi "……"

show misha hips_smile
with charachange


mi "私はあの子と勝負しようとした。キングを追いかけ回して餌に食いつかせようとした。でもあの子はうまくいく手だけにこだわったから、うまくいかなかった"


mi "一番やりにくかったのは、あの子が速く手を指していたとき。それはつまり、その状況でどう指せばいいか、はっきりわかっていたということだから"

show misha sign_smile
with charachange


mi "つまり誰かが教えたってこと。どういうことかわかる、ひっちゃん～？"


hi "よくわからない"

show shizu adjust_happy
with charachange


shi "……"

show misha hips_grin
with charachange


mi "あれだけチェスが好きなのに、全力を出せていないということは、チェスそのものじゃなくて、それにまつわる思い出が好きなのよ。真剣勝負の道具として見るには大切すぎるってこと"

show shizu behind_blank
with charachange


shi "……"

show misha perky_smile
with charachange


mi "だから、チェスを通じて仲良くなることはできないの。言葉がなければね"

stop music fadeout 5.0


"まあ、お前の友達の作り方は誰にでも通じるやり方じゃないぞ、静音。"


"少なくとも俺が見る限り、静音の顔に浮かぶ表情に悲しみの色はない。でもその言葉はとても悲しい。"



hi "なあ、一勝負しないか"



hi "まだチェス盤もあることだし"

play sound sfx_warningbell


"でもチャイムの音に俺は遮られる。"

scene black
with dissolve

$ suppress_window_after_timeskip = True



label jp_S12:

window hide None

scene bg school_council
with locationchange

nvl clear

nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_daily fadein 0.5


n "\n暮らしは以前の通りに戻った。まあ、かなり珍しい時期に転入したし、そもそも最初の数週間だって普通だったとは言いがたい。どちらかと言えば、色々なことがだんだん落ち着いて、正常になったんだろう。"



n "ここで過ごした時間は思ったよりも長いんだな。"


n "転入する前に山久で起きていたであろう様々なことや、俺がいなくなってから前の学校で起きたことについて、考えずにはいられない。"


n "こういう気持ちはどこからわき上がってくるんだろう。後に残した気持ちなんて大してないのに。"



n "ここには好きなことがずっとたくさんある。そうでなければ、生徒会とか静音とかミーシャに関わりたいなんて思ったりしない。この学校が最初に思っていたようなところだったなら、何かを気にかけることは難しかっただろう。"




n "だからこういう日課のような感覚でさえ、ある意味で気持ちを明るくしてくれる。"


n "放課後に待ち受けている生徒会の仕事の量には恐ろしくなる。今度ばかりはさぼりを決め込みたくなる。それでも自分にできることがあるという感覚はいいものだ。"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

window show

show shizu basic_normal
with charaenter


"静音は俺の横に出席簿の束を降ろす。"

show shizu adjust_happy
with charachange


ssh "また手伝ってくれてありがとう"


show shizu adjust_happy at tworight
show bg school_council at bgright
with charamove

show misha hips_grin at twoleft
with charaenter


mi "今度もありがと、ひっちゃん～！"



"それにしてもすごい量の仕事だ。また手話のクラスをさぼる羽目になってしまったけど、もう静音とミーシャの会話をほとんど理解できるレベルにはなっているので、それほど気にはならない。"



"ただ、静音はまだそのことに気づいていない。俺は自分の手話に間違いなく自信が持てるレベルになるまで、このままで通す覚悟を決めている。ちょっと子供じみた考えかもしれない。"

show shizu behind_frown
with charachange


ssh "あと五日もしないうちに七夕だけど、屋台の組み立ては明日にならないと始めないんだって"

show misha sign_smile
with charachange


mi "ひっちゃん、明日からまた屋台の組み立てを手伝わないといけないかも"


hi "どうしてさ？　だったらそもそも何のために屋台をばらしたんだよ？　何日もかかったんだろ？"

show misha hips_grin
with charachange


mi "うん！　そうだよ～！　ひっちゃんはそのときいなかったけど～"


hi "言ってくれれば手伝ったのに"

show shizu basic_normal
with charachange


ssh "あれだけ学園祭を楽しんだのに、後片づけで退屈させたんじゃ意味がないでしょ"

show misha hips_smile
with charachange


mi "学園祭のすぐ後に片づけをさせて退屈させるなんて意味がないでしょ。そしたら楽しい気分が台なしだよ"

show shizu behind_smile
with charachange


ssh "それに……"

show misha hips_grin
with charachange


mi "あははは～！　ひっちゃんはどうせ怠け者だから、逃げようとしたに決まってるって～！　しっちゃんは追いかけっこをするのは嫌いだって"


hi "きついこと言うな"

show shizu adjust_smug
with charachange



"静音は手で口を覆って、体を震わせ始める。全く音を立てないせいもあって、笑っているのだと気づくのが一瞬遅れる。"



"そんな姿を見るのは少し妙だけど、笑いそのものは鼓膜をつんざく大声はないにしても、ミーシャのように朗らかなものだ。"

show misha sign_smile
show shizu adjust_happy
with charachange


mi "んん～、でもそれっていい質問だよ、ひっちゃん"


hi "えっ？"

show misha hips_grin
with charachange


mi "屋台のこと～！"

show shizu basic_normal2
with charachange



ssh "保管場所の問題よ。屋台は一つ一つがかなり大きいから、あんなにたくさんの屋台を保管する場所なんて校内にない。外部の倉庫を使うお金を出すわけでもないから、そう決めたの。非効率だけどお金はかからない"


show misha sign_smile
with charachange


mi "つまり～！　学校の中にはそんなにたくさん屋台を置く場所がないんだよ、ひっちゃん"

show shizu behind_frown
with charachange


shi "……"

show misha perky_confused
with charachange


mi "あー、そうだねそうだね、うん、あるけど、でもお金出したくないんだよね～！　ごめんね、しっちゃん～……"

show shizu basic_normal2
with charachange


ssh "これも前の代のせいなの"

show shizu behind_frustrated
with charachange


ssh "学校側は外部の倉庫を使うコストが上がりすぎていると判断したの。前の代の生徒会は弱腰過ぎて、毎年２回も６０個の屋台を組み立てて取り壊すのはばかばかしいって主張することができなかった"

show shizu adjust_angry
with charachange


shi "……！"

show misha cross_grin
with charachange


mi "おっけ～！！"

show shizu behind_smile
with charachange


shi "……"

show misha perky_smile
with charachange


mi "ひっちゃん、何か食べようよ～！　もう丸一日働いたみたいな気分だよ～……"


hi "実際働いてるよ。言われてみれば腹へったな。昼を食べるつもりだったけど、どういうわけか食堂がものすごく混んでたから、面倒くさくなったんだ"

show misha cross_laugh
with charachange


mi "あははは～！　今日はサイドメニューにすごく特別な品があったから混んでたんだよ"


hi "どんなだよ？　いや、言わなくていい。どうせ俺には食べられないから関係ないし"

show shizu adjust_smug
show misha hips_grin
with charachange


"静音は妙に満足げだ。今度はどういう裏があるんだか。"

show shizu behind_smile
with charachange


ssh "このときのためにあらかじめ準備してたの"


"自己満足の笑顔を浮かべながら、かばんからあらゆる種類の食べ物を取り出す。その９割以上は食堂から持ってきたものだ。"

stop music fadeout 5.0


"しかもすごい量だ。一人が買える数には制限があったんじゃないのか？"



"つまりこの獲物は不正に入手されたに違いない。"



hi "子牛のカツレツサンドは昼休みになったとたんに真っ先に売り切れるんだぞ。それを買えたなんて感心したよ"


hi "ありがと"

show misha perky_smile
show shizu basic_sparkle
with charachange


"すばやく手を伸ばすけど、静音もすぐにそれを奪い取ろうとする。"

play music music_another fadein 0.5

show shizu basic_happy_close
with characlose



"お互いの手が触れあって、一瞬だけ静音が手をゆるめるけど、すぐに二倍の力で押し込んでくる。"
"あの燃えるような競争心が瞳の中で危険なまでに閃いている。静音の指が俺の手をまさぐり、隙間を見つけてこじ開けようとする。"



"俺も一ミリたりとも動かない。このパンのためなら命だってかけてやる。このチャンスを逃したら二度と食べられないかもしれないんだ。"


"でもこんなことを続けていたら、パンを握りつぶしてしまって全然食べられなくなる、という可能性も重々承知している。"


hi "ミーシャ……手を離さないとパンがつぶれるぞって静音に伝えてくれよ"

show misha perky_confused
with charachange


mi "ふーーーーーん？　どうして自分で言わないの？"


"やろうと思えば静音とは普通に会話できるということをいとも気軽にばらされて、俺は肝を冷やす。わざとじゃないかと疑いそうになるけど、きっとジュースのストローを紙パックからはがすのに夢中だっただけだろう。"


hi "別におかしくないだろ？　パンを離したくないんだよ"


show misha sign_smile
with charachange


mi "じゃあわたしからはしっちゃんには言えないな"

show misha hips_grin
with charachange


"ミーシャは手のひらを上に向けて肩をすくめ、満面に笑みを浮かべる。"


hi "どうしてだよ？"

show misha sign_smile
with charachange



mi "だって～！　ひっちゃんはそのパンを取り合ってるんだから、信用できないの～！"
mi "しっちゃんが返事しようとしたら、パンから手を離さなきゃいけなくて、そしたらひっちゃんの勝ちでしょ。どうだかどうだか、それが狙いなんじゃないの、ひっちゃん？"




show misha cross_smile
with charachange



mi "それじゃ不公平だもん、だからわたしは中立になるの！　スイスみたいにね～！"



hi "スイス？"

show misha perky_smile
with charachange


mi "スイスのこと知ってる？"


hi "そりゃ知ってるよ……中立なんだろ、国も人も"



show shizu basic_sparkle_close
with charachange


"静音が生意気そうに俺をじろじろ見る。舌の先をちょっとだけ歯の間から出しながら、しっかりと子牛のカツレツサンドを引っ張り続けている。"

show shizu adjust_happy
with charadistant


"突然、静音はパンを手放して両手を上に上げる。手のひらは上向き。世界共通の和平の身振りだ。"

show shizu behind_blank
with charadistant


ssh "こんなのはお粗末な決着の付け方だと思わない？　それにパンをつぶしてしまうかもしれないし"

show shizu behind_frown
with charadistant


"こちらをにらみつけてくる。おとなしい表情は瞬時に責めるようなしかめ面に変わる。"

show shizu adjust_angry
with charadistant


shi "……！"

show misha hips_frown
with charachange


mi "ひっちゃん！　パンを離しなさい！　今は交渉中なんだから！"


"俺は渋々パンを手放す。"

show misha perky_smile
show shizu behind_blank
with charachange


"横からミーシャの手が飛び出す。指でテーブルをばたばたと叩きながらこっちまで手を伸ばしてくる。"

show misha hips_grin_close
with characlose


mi "あ～！　はは～！　わたしのことは気にしないで、そもそも子牛の肉なんて好きじゃないし。わたしはこっちのサンドイッチをもらうね～！　それと飲み物も……"

show misha perky_smile
with charadistant


"注意深く飲み物を拾い上げると、ミーシャはすぐに身を引く。"



"ミーシャの考えも間違っていない。他のものを選んだっていいんだ。いっぱいおいしそうな食べ物があるんだから。チキンカツ丼パンもおいしくて人気のある、よく売れている品だ。でもこれはもう食べたことがある。"




show shizu basic_angry
with charachange


ssh "あなたって本当に幼稚ね、久夫。あなたが他のものを選べば何の問題もないのに。チキンカツ丼パンだってすごくおいしいのよ"

show misha hips_smile
with charadistant



mi "ほんとに幼稚だね、ひっちゃん。代わりにチキンカツ丼パンにしたら？すごくおいしいよ～！"



hi "でももう食べたことがあるんだよ"

show shizu behind_frown
with charachange


shi "……"

show misha hips_frown
with charachange


mi "ひっちゃん～！　どうしてその子牛カツレツパンに、と・く・べ・つ・に、こだわるの？"


hi "普通は手に入らないからだよ。珍しいものはもっとおいしいんだ"

show shizu basic_frown
with charachange


ssh "子供みたいね"

show misha cross_frown
with charachange


mi "子供みたいだよ、ひっちゃん"


hi "お前はどうしてチキンカツ丼パン食べないんだよ？"

show shizu adjust_blush
with charachange


ssh "そんなことは重要じゃないの"


"真っ赤になりながら、静音は狡猾そうな笑みを浮かべて話を続ける。"

stop music fadeout 6.0

show shizu basic_happy
show misha perky_smile
with charachange


ssh "あなたとは話しても無駄ね。もうけりを付ける方法は一つしかない。勝負しましょう"

show misha sign_smile
with charachange


mi "そんなの関係ないよ。かわりに勝負でけりをつけるよ～！"


"なんとなく、こうなるような気がしていた。論理的な帰結だ。"


"静音は長い間勉強し続けていた。今の今まで、ほとんどずっとだ。期末試験も終わったことだし、たまりにたまったエネルギーを放出しないといけないんだろう。"


hi "勝負って、どうするんだよ？"

hide misha
with None
show misha perky_smile behind shizu at twoleft
with None

show shizu behind_blank_close
with characlose



ssh "国家の運命さえ決したという人類最古のゲーム――じゃんけんよ"


show misha sign_smile
with charachange


mi "じゃんけんで決めるよ"

show misha perky_confused
with charachange


mi "ほんとに？　なんかすごい真剣な感じがしたよ、しっちゃん……"

play music music_shizune fadein 1.0


"静音の言葉遣いに冗談っぽさはまったくない。真剣そのものだ。"


hi "わかった、わかった"

show shizu adjust_happy_close
with charachange


"静音は手を後ろに引く。俺も同じようにする。"


hi "じゃんけん、ぽん！"

show shizu basic_angry_close
with charachange


"二人ともグーを出す。あいこだ。完全に読み切っていたはずなのに。グーは無敵なのだ。静音は渋い顔をする。予想外の展開にとても不愉快そうだ。計画通りとは行かなかったかな？"

show shizu adjust_angry_close
with charachange


ssh "あいこで！"

show shizu basic_frown_close
with charachange


"どちらもチョキだ。"


hi "くっそー"

show shizu adjust_angry_close
with charachange


ssh "あいこで！！"

show shizu basic_frown_close
with charachange


"また二人ともグーを出す。しかし三つ目の手がチョキを出している。"

show misha hips_grin
with charachange


mi "面白そう、わたしもやっていい？"

show misha cross_laugh
with charachange


mi "はははは～！"

show shizu behind_frown_close
with charachange


ssh "…… …… ……"

show misha perky_smile
with charachange


mi "決闘なの、しっちゃん？"

show shizu adjust_angry_close
with charachange


shi "……"

show misha sign_confused
with charachange


mi "え～、決闘のルール？　む～……そうだね、そうだね～！　わたしよくわかってないから……"

show shizu cross_angry_close
with charachange


shi "……"

show misha perky_confused
with charachange


"静音の手話が速ければ速いほど、俺には読みとるのが難しくなる。実際、ミーシャでさえ追いつくのが大変そうだ。"


hi "なんて言ってるんだ？"

show shizu adjust_angry_close
with charachange


ssh "もう一回！"

show shizu basic_frown_close
with charachange


"またあいこだ。何度やっても、静音は勝負を続けようとする。やがてその一言もすっ飛ばして、俺たちはわき目もふらずにひたすらじゃんけんを繰り返す。"


"完全に適当な手を出し続けるようになっても、ずっとあいこが続く。数学的にはものすごい偶然だ。"

stop music fadeout 8.0

show misha hips_grin
with charachange



"ミーシャは俺たちのまわりをうろうろしながら、ずっとその様子を見ている。そしてあいこになるたびにげらげらと笑う。１６回目のあいこの後、静音はテーブルから椅子を押し出して立ち上がる。"


show shizu behind_blank_close
with charachange


shi "……！"

show misha hips_smile
with charachange


mi "もう終わりだよ、ひっちゃん～！　何を間違えてたのかわかったから、次の勝負で全部終わるよ。覚悟してね、いい～？　おっけ～！"

show misha sign_smile
with charachange



mi "ひっちゃんの思考プロセスは見切ったし～、勝負の仕方もわかったよ。次の手は読めたから、うまくあしらっちゃうよ"



"こんなの全部初耳だ。もう何のためにじゃんけんを続けているのか思い出せない。"

show shizu adjust_happy_close
with charachange


"静音は自信たっぷりにニヤリと笑う。恐れ知らずの大胆さがその顔に浮かぶ。その手を後ろに引きながら、冷静な目つきに負けず嫌いの気合いを光らせて、俺にも同じようにしろと言葉もなしに迫る。"


"プロのボウリング選手か何かのような、見事なフォームだ。たかがじゃんけんだというのに。"

show shizu basic_happy_close
with charachange


"パーがふたつ。"

play music music_comedy

show shizu cross_stunned_close
with charachange


"とたんに静音の体から緊張が解ける。怒りの表情を浮かべながらこめかみをこすり、タイヤがパンクするような音に似たため息を長々と吐き出す。この勝負を始めたときよりもずっと腹が減っていることに俺は気づく。"


hi "半分こしようぜ"

show shizu behind_blank_close
with charachange


"パンを半分に割って、片方を静音に差し出す。静音はそれを受け取る。"

show shizu adjust_happy_close
with charachange


ssh "ありがとう"


"手の中のパンを、観察するようにじっと見ている。"

show shizu basic_normal2_close
with charachange


ssh "でもなんだかむなしい気分がする"

show shizu basic_normal2_close
with charachange


"気持ちはどうあれ、静音は結局パンを口にする。"


"突然、この状況をずっと観察していたミーシャが視界の端に入る。"

show misha hips_grin
with charachange


mi "ひっちゃん～……今のはとってもアツアツだったと思うよ"


hi "おい、何言ってるんだよ"

show misha cross_laugh
with charachange


mi "わははははは～！"

show misha hips_smile
with charachange

stop music fadeout 5.0


"笑って、ミーシャは二つ目のサンドイッチをかじる。"


"静音とはそれ以上勝負をせずにすんだので、俺たちはしばらく無言のまま食べ続け、そして作業に戻る。"

scene bg school_council_ss
with shorttimeskip

play music music_tranquil fadein 3.0


"いつもの書類整理を仕上げながら、これは高いテンションで一週間を始めるための静音なりのやり方なんじゃないか、と俺は密かに考える。"


"結局、本番の仕事が始まるのは明日からだし。屋台の組み立てで両手がふさがってしまうので、静音が『話す』ことはあまりできなくなる。"



"たぶん最初の時のように、とても退屈で疲れる作業になるだろう。だとしたら、俺は静音の気遣いに感謝する。こういう一日があるのはいいことだ。これからの日々に向けて楽しい気分になれる、というのは。"
"それも静音の考えのうちだったんだろう。"



"……まだ健二の小包を始末していなかったことも思い出す。あれは邪魔くさいし、しかも包みを受け取ってからずっと健二を見かけていない。"

scene bg school_lobby_ss
with locationchange


"その日の生徒会の活動が終わってから、俺は静音とミーシャと別れて、飲み物を買いに自動販売機へ向かう。短い道のりだけど、数秒も経たないうちに誰かが付いてきている気配を感じる。"

scene black
with hands_in


"誰かの手が俺の目を覆う。"


mi "だ～れだ！"


hi "静音か？"


mi "わははは～！　わたしだよ、ひっちゃん～！"


hi "ああ、わかってるよ"

scene bg school_lobby_ss
with hands_out

with Pause(0.3)

show misha hips_frown_close_ss at Slide(0.3, 0.5, 0.5, 0.5, 1.0)
with Dissolve(1.0)


mi "じゃあどうしてしっちゃんだって言ったの～？　時々は間違ったっていいんだよ、ひっちゃん～！　ひっちゃんはプライド高すぎだよ"

show misha sign_smile_close_ss at center
with charachange


mi "とにかく～、生徒会の後は、いつも予定とか何もないでしょ～？　だから、寮にまっすぐ戻るだけなんだよね？"


hi "ほかにどこに行くってんだよ？"

show misha hips_grin_close_ss
with charachange


mi "おっけ、よかった～！　ばっちりだよ、ひっちゃん～！　今日はひっちゃんとお話ししたかったから、とっても都合がいいよ！"


"人気のない校舎で、放課後に高校生が二人きり。夕日が空をロマンチックな琥珀色で染める中、かわいらしい女の子が話があると言ってくる。"


"なんて秘密めいたおいしいシチュエーションなんだ。俺は想像をたくましくしてしまう。自分が妄想しているような状況になるとはとうてい思えないけど、そういうふりをするのは楽しい。"



play sound sfx_can
show misha perky_confused_close_ss
with Dissolve(0.2)



"缶コーヒーを開ける音で、そんなクサいムードを保つチャンスも吹っ飛んでしまう。想像も付かないほど大きな音だったけど、状況も手伝ってよけいに大きく聞こえる。俺は失望と安心の混ざったため息をつく。"







hi "で、何だよ？"

show misha perky_smile_close_ss
with charachange


mi "えっ？　ああ！　実はね～……授業に追いつけてない科目があって、このままだとまずいかもしれないの～！　これ以上先延ばしにはできないの"

show misha perky_sad_close_ss
with charachange


mi "もう真剣に授業に取り組まなきゃだめだって先生に言われて、それでちゃんと授業を聞かないといけないの。なんてったって～、これでもう３回目だからね"


mi "ごめんね～！　ほんとにごめんね、ひっちゃん"


hi "どうして謝るんだよ？"

show misha sign_sad_close_ss
with charachange


mi "しばらくひっちゃんとしっちゃんの生徒会の仕事を手伝えなくなっちゃうの～。２、３日だけだから、ほんとに！　絶対がんばってできるだけ早く復帰するから！　でも～……"


"うれしい気分とは言えない。今週はものすごく忙しくなる予定じゃなかったのか？　なんて間の悪い。静音なら何か手を回してミーシャを救い出せるんじゃないかと、思わず聞いてしまいそうになる。"


"でもミーシャは純粋に申し訳なさそうにしている。そんなことを口にするのはただの馬鹿野郎だ。"




"それに、本人がこれ以上先送りできないと言うのなら、俺はミーシャを信じたい。生徒会の仕事だって驚くほど真剣に取り組んでいるのだから。"


hi "ああ、わかったよ。大丈夫。去年は静音と二人きりでなんとかしたんだろ？　きっと俺にだってできるさ。心配すんなって"

show misha hips_grin_close_ss
with charachange



mi "ほんとに？　ありがと、ひっちゃん～！　まじで！　やったやった～！　ひっちゃんが納得してくれるって思わなかったよ～！　仕事がすっごくたくさんあるから、心配すると思ってたよ、七夕とかいろいろね～！"



"なんだよ、やけに俺のことをわかってるな。"


show misha sign_smile_close_ss
with charachange


mi "……でも～！　ひっちゃんはすごく冷静だね～！　うれしいよ～……"


hi "はは、そうだな。たしかにそうだよ、そのことは考えてたけど、でも大したことじゃない。それでパニックになったりはしないよ"


hi "静音と話すのにメモ帳をずっとやりとりし続けるのはちょっと大変かもしれないけどな"

show misha hips_frown_close_ss
with charachange


mi "ひっちゃん、自分も手話が使えるってしっちゃんに言っちゃいなよ！　どうして言わないのかわかんないよ"



hi "まだだめだ。ほとんどわかるようになってるけど、間違いないようにしておきたい。てか、実際どうでもいいんだけど。ずっと秘密にしてるのは俺もつらいよ。それに静音と本当に会話できたらいいだろうなって思う"



hi "大丈夫だよ、そのうちあいつには言わないといけないから。そのためのいいタイミングを考えてるところなんだ"

show misha hips_smile_close_ss
with charachange


mi "そのことなら心配ないよ、ひっちゃん～！"


hi "どうして？"

stop music fadeout 3.0

show misha sign_smile_close_ss
with charachange



mi "えっと～、それはわたしが……ひっちゃんはしっちゃんの言葉がわかるよって教えてあげた……っていうか"
mi "しっちゃんも同じことを心配してたの。お互いのことを理解できないんじゃないかって～！　だから～！　わたしも心配してたけど、最後には結局うまくいったね～！"



show misha sign_confused_close_ss
with charachange


mi "ははは？"


"もうだめだ。"


play music music_running


hi "あああああああああああああ！！"


hi "俺がどれだけバカみたいに見えるかお前わかってるのか？　こっちは丸一日手話なんてわかりませんってふりしてたのに、静音は最初から知ってたって、本気で言ってるのかよ？"


hi "きっと『私のことをわからないふりをして、とんだ大バカね』なんて思ってるに違いないんだ。俺は自分で自分を笑い物にしちまったんだぞ"


hi "なんてことさせてくれるんだよ！？"

show misha hips_frown_close_ss
with charachange


"ミーシャは顔をしかめる。自分が思っていたような受け止め方を俺がしていないことに、言葉を失っているようだ。俺が落ち着くのを見届けるまで、ミーシャは口を開かない。"

show misha hips_smile_close_ss
with charachange



mi "……でもひっちゃん、結局これが一番だったと思うよ～！"





"俺のパニックが収まるまで辛抱強く待った上で、ミーシャはまばたきもせずに言う。"


"その陽気な言い方は、さっき俺に向けて爆弾を落とした瞬間から今までの時間がすっ飛ばされたような気分にさせる。ある意味、かなりおかしい。"


hi "お前ってほんとに単細胞だよな、知ってたか？"




show misha hips_grin_close_ss
with charachange



mi "知ってるよ～！"




stop music fadeout 4.0


"どうせもう後の祭りだ。ミーシャがこれだけ断固たる確かさでこれがうまく行くと信じているなら、その可能性に賭けてみる価値はあるのかもしれない。"


"それに、もしうまくいかなければ、全速力で走って逃げるさ……"


"埋め合わせをしようと、ミーシャは自動販売機のドリンクをもう一つおごってくれる。とてもささやかなお詫びの印だけど、大事なのは気持ちということだろう。それにミーシャの思いやりは心からのものだ。"


"ついでにおごりなので、俺はそれに甘える。"



scene black
with dissolve


label jp_S13:

scene bg school_dormhisao
with locationchange



"今日もひと握り分の薬をコップの水で飲み下す。"







"８時間の熟睡から目覚めてみると、昨夜の心配ごとがいったいなんだったのか、もう思い出せない。やたらと大きな錠剤を半分にかみ砕きながら、俺はあれこれ理屈付けをして不安な気持ちを打ち消し続ける。"


$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_dreamy fadein 2.0

window hide

nvl clear

nvl show dissolve



n "\n\n\n\n\n静音は俺が手話の授業を受けていたことを昨日ずっと知っていて、でも何も詮索しなかった。"




n "口がきけないからといって、自分の気持ちを伝えることができないわけじゃない。いや、だからこそあいつは遠慮せずに気持ちを表に出しているように見える。"


n "回りくどい言い方をしたり、気持ちを抑えたりしない。誤解の余地がないように、いつも悪びれることなく自分の意見をはっきりと伝える。"


n "つまり、昨日の時点で静音が怒っていなかったのなら、最初から怒ってなんかいないということだ。そもそも、俺が何か間違ったことをしたわけでもない。"

nvl clear



n "\n\n\n\n\nでも俺の不安が静まるにつれて、しばらくミーシャ抜きで静音と二人きりで過ごさないといけないことに思いが至る。昨日はあまり気にしなかったけど、どんどん心配になってくる。確かにもう手話はかなり理解できるようになった、でも……"



n "その理解が初級よりもましだと言うには大いにためらいがある。それに静音はいつもそうするけど、手話のスピードが上がったら、ついていける気がしない。"


n "手話をするのだって得意とはいえない。ミーシャのように両方を同時にこなすのはまだまだ遠い夢だ。"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene bg school_scienceroom
show misha hips_grin at twoleft
show shizu behind_smile at tworight
with shorttimeskip

window show


mi "ひっちゃん～！"


hi "なんだよ？"

show misha sign_smile
with charachange


mi "忘れちゃだめだよ、今日は屋台の組み立てを手伝ってくれるって言ったよね～！　放課後に校舎の裏だよ、おっけ～？"


hi "はいはい、わかってるよ"

show shizu adjust_happy
with charachange


shi "……"

show misha hips_smile
with charachange


mi "前に手伝ってくれたときはね、ひっちゃん、とっても助かったんだよ～！　今度は前よりももっと大事だから、絶対さぼったりしちゃだめだからね、わかった？"


"その理由を聞きたいけど、聞くチャンスは得られなかった。それに授業についていけていないと知っている以上、ミーシャの気を散らすのは良くない。昼休みなら聞いてもいいだろうと思ったので、結局そうする。"

scene bg school_cafeteria
show misha sign_smile at twoleft
show shizu behind_blank at tworight
with shorttimeskip



mi "それはね、ひっちゃん、町のお祭りは言葉通り、ふるさとや町の歴史を祝うものでしょ"



show misha hips_grin
with charachange


mi "七夕はそうじゃなくて、お願いや恋人のお祭りなわけ～！　だからずっと大事なお祭りなんだよ、そうでしょ？　そうだよ～、当然だよね～"


hi "七夕ってほんとにそういうお祭りだったっけ？"

show shizu basic_frown
with charachange


shi "……"

show misha cross_frown
with charachange


mi "ひっちゃんは遊び心ってものが全然ないよ……"


"不機嫌そうに頬を膨らませると、風船がしぼむときのようにぷうっと息を吹き出す。"

show misha hips_frown
with charachange


mi "そういうことにもっと感謝の気持ちを持たなきゃだめだよ、おいしいものを食べておめかしするための口実だとしてもね～！"

show misha sign_smile
with charachange


mi "そうしないなら、ひっちゃんには失望しちゃうよ、わかった？"




stop music fadeout 5.0


"何か返事をしようとする間もなく、ミーシャは横を向いてコロッケを一口で飲み込む。"

scene bg school_gardens2
with shorttimeskip


"放課後、校舎裏で静音と落ち合う。見る限り、どうやら昨日のうちに準備をすべて済ませていたようだ。"

show shizu adjust_happy at center
with charaenter



"軽く手を振って俺を迎えると、すでに手に持っていたハンマーを見せびらかして、後ろにある屋台に向かって腕を伸ばす。"
"いくつかはもう途中まで組み上がっているけど、それ以外はひもで縛った板がごちゃごちゃと山積みになっているだけだ。"


hide shizu
with charaexit

show bg school_gardens2_ss as overlay at Alphain(20.0), center
with None

play ambient sfx_stallbuilding fadein 8.0




"時間が経つにつれ、薬の効果には限りがあることを思い知る。今もありえないくらい体が疲れる。幸い、静音はこっちに背中を向けているから、理由を詮索される心配なしにたっぷり休憩することができる。"




"でもちょっと考えてみると、俺はハンマーを叩く音が途切れるのを静音が聞き取れない弱みにつけこんでいる。そのことがとても後ろめたく思えてくる。喜ぶなんてとんでもないことだ。"



"静音の勤勉さは尊敬に値する。仕事にうんざりしているどころかいらだっているのも明らかだけど、それでもペースを落としたりはしない。片手で釘を打つのに疲れると、もう一方の手に切り替えている。"




hi "静音――"



"名前を呼んだ直後、バカみたいな気分になる。"


"今の気持ちは静音には言えない。俺の手にもハンマーがある。結局、静音に遅れずについていかなきゃだめだという気分になってくる。"


"俺だってさぼってはいられない。俺たち二人だけしかいないのだからなおさらだ。手話を伝える時間も、そのチャンスもない。お疲れさまと言葉をかけることさえできない。"


"そんな何気ない一言でさえ、ハンマーをおいて静音の注意を引き、手を動かして手話で伝えなければいけない。"



"単純な手ぶりだというのに、不必要に複雑になってしまう。道に向かって踏み出した一歩が、思っていたよりも長かったときのように。"



"それを理解できるくらいには静音とは長く付き合ってきたつもりだけど、それでも俺は度忘れしてしまっていた。"


"釘が木材に埋め込まれるリズミカルな音が空気を満たしている。"


"しばらくして、なんだかいいなと思えてくる。目の前の仕事の単調さをまぎらわそうと、静音がハンマーを打つのと同じタイミングで、そして裏拍子を取るように交互に釘を打ってみる。もちろん静音は気が付かない。"




"音が聞こえないことで、静音にとってはよけいに作業が退屈でつまらないものに感じられたりするんだろうか？"

stop ambient fadeout 3.0


"振動が指に伝わっているのに、自分の行動の結果を耳で聞くことができないというのは、おかしなことなのか？　音という概念を知らないこと自体、静音はそもそも気にしているんだろうか？"


"気が散ってしまった俺は、静音の頭が目の前に飛び出してくるまで、そばに忍び寄られていたことに気づかない。"

scene bg school_gardens2_ss
show shizu adjust_happy_ss at center
with charaenter

play music music_soothing fadein 5.0


ssh "休憩してるの？"


his "ああ、そんな感じ"

show shizu behind_smile_ss
with charachange


ssh "いいわ、そうしましょう"



show shizu basic_normal_ss
with charachange


ssh "手話がわかるのね"

show shizu behind_blank_ss
with charachange


ssh "お互いにとって好都合ね。私には隠してたけど"


hi "ははは……"

show shizu basic_normal2_ss
with charachange


ssh "どうして？"


his "どうしてって、何が？"

show shizu behind_blank_ss
with charachange


ssh "どうして手話のクラスをとろうって思ったの？"



"静音の視線は一秒たりとも俺の目から離れない。俺の反応を見たいのだとしたら、周辺視野で十分だろう。一度何かが視界に入ったら、静音は絶対に目をそらさない。"




"静音の目は驚くほど鋭く、夜の湖のように暗い。不思議な感じがする。"


his "そうしたかったからさ。そのうち役に立つかもって思ったんだ。実際役に立っただろ？"

show shizu adjust_happy_ss
with charachange


ssh "そうね"

show shizu basic_normal_ss
with charachange


shi "……"


his "ごめん、今の一言もわからなかった"


his "ほらな？　時々今みたいなことになるんだ。ミーシャがいてくれたらよかったな"

show shizu behind_blank_ss
with charachange



ssh "ミーシャには追いつかないといけない勉強があるんでしょう？　私にも責任があるかもしれない"
ssh "ミーシャには補習は必要ない。成績は上出来とは言えないけど、自分の決めたことが他の人にどう影響するかは理解している。その点は他の人よりもずっと優れているわ"




show shizu basic_angry_ss
with charachange


ssh "特にどこかの金髪よりはね"


hi "あー……"


"結構根に持つタイプなんだな。"



show shizu behind_smile_ss
with charachange


ssh "あなたの手話はとても上手ね。そんなに早く覚えるなんておかしいでしょ"




his "もう手話のクラスを始めてからずいぶんたつからね。それにしばらく続けていると、集中できるっていうか、しみこんでくるっていうか、だんだんわかりやすくなっていくし。いい感じだよ"





his "それに、本当にわからないときはミーシャもいるし"

show shizu adjust_smug_ss
with charachange


shi "……"

show shizu behind_smile_ss
with charachange


shi "……"


"うかつだったな。今の手話はひとつもわからなかった。前言撤回か。"


his "まあ、そうだな、本当はそんなに簡単じゃない。実際には死ぬほど難しいよ。割れたガラスのかけらを拾うようなものだな"


his "でもある意味、興味深くもあるんだ。冒険みたいな。まあ、ちがうけど……"

show shizu basic_normal2_ss
with charachange


ssh "ガラスのかけらを拾うのは冒険とは言わないでしょ"


his "言うさ。同じくらい難しいってこと"

show shizu behind_blank_ss
with charachange


ssh "ほうきとちりとりを使えば簡単よ"



"俺はイライラして、悲しくなってくる。"



"顔を上げると、静音が手にソーダの缶を持っているのに気づく。"


hi "どこでそれを？"

show shizu adjust_happy_ss
with charachange


"手話で伝えるのを度忘れしたけど、俺の目線を追っていた静音には伝わる。そして背中からもう一缶取り出し、こっちに放り投げる。俺は両手でそれを受け止める。"

show shizu behind_smile_ss
with charachange


ssh "あなたの分も持ってきたの"

play sound sfx_can


"静音は手を止めると、缶のタブに爪をかけてふたを開け、そのまま脇に置く。"

show shizu basic_normal_ss
with charachange


ssh "そんなにがんばって私のことを助けてくれるんだから、私だってあなたのことを気にかけないとね。当然でしょう"

show shizu behind_blank_ss
with charachange


ssh "でもあなたが手話を習うというのなら、それは全く話が別。感心するのが当たり前。二つを分けるのは義務かどうかよ"

show shizu adjust_happy_ss
with charachange

stop music fadeout 8.0


ssh "私、とてもうれしい"

show shizu behind_smile_ss
with charachange


"ドリンク缶を一息に飲み干すと、静音は後ろに腕を伸ばし、さっと立ち上がる。"

show shizu adjust_smug_ss
with charachange


ssh "オーケー！　仕事に戻るよ！"

hide shizu
with charaexit


"そうして、話は終わる。静音はさっきと同じように仕事に精を出す。口の端にわずかに残る笑みが、多少なりとも休憩を取ったという唯一の証だ。"



show bg school_gardens2_ni as overlay at Alphain(10.0), center
with None


"同じように作業に戻りながら、なにもかもうまくいく、というミーシャの言葉は正しかったのだと思う。今のところは、すべてのことがいい方向に向かっている。"


"暗くなり始める頃、ミーシャが顔を出す。俺と同じくらい疲れているみたいだ。そしてこの辺で終わりにしようと静音が告げる。"



"今日の成果にカバーをかけてそれぞれに帰り道につく間、俺は静音とミーシャが寮へと戻る間に、二人が流れるように会話し、やすやすと一緒に笑い合うのを見つめる。"



"ミーシャの手話のうまさに改めて感心する。いったい俺はあんなレベルに達することができるんだろうか。そもそもそんな時間はあるんだろうか。"

scene black
with dissolve


label jp_S14:

scene black
with None

play sound sfx_impact

scene bg school_dormhisao
with vpunch



"今朝一番の出来事は、ベッドから出たとたんに健二の小包につまずいて、まだ目もちゃんと覚めていないのに頭から床に突っ込んだことだ。"




show kenjibox:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)



"手近にある鈍器でこいつを殴りつけてやりたい衝動に駆られる。ホームラン狙いだ。でも朝が早すぎてそんな気力も出てこない……それに中身も傷ついてしまうだろう。さすがにそれは意地が悪い。"




show kenjibox:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide kenjibox
with None

scene bg school_dormhallway
with locationchange



"俺は箱を廊下に押し出す。それはなんなくなめらかな床を滑って、健二の部屋のドアにぶつかると、ほとんど聞き取れないくらいやわらかな音を立てる。"
"その直後に１ダースほどの錠前が、盛り上がる交響曲のように立て続けに外れる。"


play music music_kenji fadein 0.5

show kenji tsun at Slide(0.4, 0.5, 0.5, 0.5, 0.5)
with charaenter


ke "誰だ？"


"と健二が言い、返事も待たずにのこのこと廊下に出る。どういうわけか健二らしくない見事な優雅さで、転ぶことなく箱の上をまたぐ。俺には全くの偶然だというのが明らかだったけど。"



hi "俺だよ。お前の小包、受け取ってきたぞ。お前が今上に立ってる"


show kenji happy at center
with charachange


ke "わかってる。ありがとよ"


hi "……ああ、まあ別に"


hi "で、中身は何だよ？"

show kenji tsun
with charachange


"健二は縮み上がると、一瞬で身構えて動揺し始める。"


ke "なんでもねえよ"


hi "いいだろ、教えろよ。気になるんだよ"




hi "俺それにつまずいて首を折りそうになったんだぞ。それにそのバカみたいにでかい箱を目の前に抱えて、前も見えないまま道を渡らなきゃいけなかったんだ……お礼に中身が何か教えてくれたっていいんじゃないの"





ke "秘密のブツなんだよ。バラしたら秘密でもなんでもなくなるだろ、だからだめだ。大したもんじゃねえよ"


hi "へえ、大したもんじゃないなら教えたっていいだろ"


ke "大したもんじゃないんだから、知る必要なんてないだろ？"


hi "知りたいことの何がおかしい？"


ke "どうして知りたいんだよ？"


hi "どうして知ったらいけないんだよ？"

show kenji neutral
with charachange


ke "どうして俺の質問に質問で返すんだよ？"


hi "どうして俺の最初の質問に答えないんだ？"


ke "どうして俺の最後の質問に答えねえんだよ！？"


"どちらも言葉を返すたびに声がうわずっているのに気づく。廊下の奥でドアが開いて、誰かが不審そうな表情で頭を突きだして様子をうかがっている。"


"きっと２人ともバカみたいに見えているに違いない。でもそれに気づけるほど恥の意識を自覚しているのは俺だけだろう。賭けてもいい。"



hi "わかったよ、じゃあそいつは墓場まで持ってけ。どうせ学校の準備しなきゃいけないしな"

show kenji tsun
with charachange



ke "なんだよ、ちげえよ。何をそんなに急いでるんだ？　少しつき合えよ。コーヒー飲むか？　しばらくぶりだしな。そういえば、お前が小包を持ってくるのがあんまり遅かったから、死んだのかと思ってたんだぜ"







hi "そもそも俺がそれを運ぶのを引き受けた時点で運が良かったって気づけよ、このうぬぼれ屋！"





show kenji neutral
with charachange



ke "おいおい、落ち着けって。ほんと、お前って突っかかるよな。生徒会のアレのせいか？　あいつらとつるんでるって聞いたぞ"




hi "俺から聞いたんだろ。お前に教えたときに"


ke "マジで？"


ke "ああ、まあ、そのなんだ。あいつらはろくでもないってことだ"


show kenji tsun
with charachange



ke "お前は新入りだからな、知ってるはずもないだろうけど、この辺じゃあいつはさまざまな対立の原因なんだ。お前が来る前に、あいつはバッジの着用を義務化しようとした。長い話だから、座った方がいいかもな"









"椅子がないかとあたりを見回すけど、このいまいましい廊下に立っているので１つも見あたらない。俺は指を立てて、そのことを健二に伝えるべきかと考えるけど、こいつはもう話し始めている。"
"せっかく腕を動かしたのを無駄にしたくないので、かわりに腕時計に目をやる。"




ke "実行されていたら、本物の恐怖政治になってただろうな"




hi "待てよ、起こりもしなかったことであいつのことを判断するっていうのか？"

stop music fadeout 8.0


ke "そうだよ。とにかく、あいつの案は得点バッジみたいなものだった。でも減点バッジもあったんだ"




hi "それが何の役に立つんだ？"

show kenji neutral
with charachange


ke "知らん。一度も実施されなかったしな。でもヤバそうだったから、話を聞いたときは何週間か部屋から出なかった"



hi "じゃあお前は何か大きな変化があると聞いて、部屋にこもって全部やり過ごそうとしたわけだ"


show kenji tsun
with charachange


ke "いや、どうにかしようと決心したんだ。しばらくあとに生徒会室を見つけたから突撃した。要求書を持って、賛同者がいると見せかけるためにその辺の生徒をひっつかまえてな"


hi "待てよ、じゃあ最初から起こりもしなかった上に、誰も気にしてなかったってことか？"

show kenji rage
with charachange

play music music_tension



"勢いが付いた健二には俺の言葉が聞こえていない。自分のわめき声のエネルギーに包まれ、完全に理性を失って腕を振り回している。まるでギャング・サインを適当にやっているみたいだ。"






ke "俺は机に詰め寄って、あいつに言ったんだ"
ke "『おい、このファシスト女！　なんだこのバッジ計画ってのは？　この象牙の塔で、俺たちを愚民の集まりみたいに傲慢に見下しやがって、世の中のことが全然わかってねえな！　何様のつもりだ！』"






ke "『エリート意識丸出しにしやがって。お前は運転手付きの車を持ってて、スラム街を運転させて、人を指さして笑うような、そういうたぐいのとんでもない金持ちに違いない……』"



ke "『……それにこの世の最後の恐竜の生き残りが排泄した高いコーヒー豆を、黄金の頭蓋骨で淹れたコーヒーしか飲まないんだろう』"




ke "『そんなことができると思ってるのか？　歴史の教科書を開いてみろ。こういうクソみたいなことのおかげでブルジョアジーはいつも血塗れの革命で追放されるって知らないのか？　愚かだ！　お前はバカだ！』"




ke "『確かに、革命派はたいてい何もかもどうしようもなく台無しにして終わっちまうもんだ。だがこんなルールを作るのは狂人だけだ……』"



ke "『俺も民衆を苦しめるためならこんなルールを作るだろう。だがこいつは本物で、お前はそれを制度化しようとしている！』"
ke "『どこまで俺たちの権利を踏みにじろうというんだ？　俺たちは人間だ！　これは正義ではない！』"




show kenji neutral
with charachange


ke "そう言ってやった"

show kenji rage
with charachange





ke "んで、大衆にアピールするために『我々の持ち物は奪えても、我々の自由は奪えなあああい！』ってシュプレヒコールを上げてやった。あのウィリアム・ウォラスの映画みたいに"
ke "映画じゃ持ち物は奪われたけど自由は奪われなくて、その後殺されたけどな"





stop music fadeout 5.0

show kenji tsun
with charachange


ke "……でもあいつは無視しやがった。くだらない書類書きから顔も上げやがらねえ"



ke "俺の理論がヤツを圧倒したのかもしれない。反論しようがなくて耳を閉ざしたんだ。あるいは、ただのろくでなしだったのかも。とにかく、あいつは答えなかったし、未来は変わることを拒んだんだ"




ke "あげくのはてに、帰り道に学生証をどこかでなくしたことに気づいた。これが俺の人生の物語さ。絶え間ない、一見すれば無意味な戦いだ。スポンジでできた手で、レンガの壁を登るようなもんだ"


hi "おい、何も変わらなかったっていったよな。でも静音がくだらないバッジをみんなにつけさせることはしなかったんだろ。じゃあ変わったんじゃないか"

play music music_kenji fadein 0.5

show kenji happy
with charachange


ke "ああ、それはそうだな。それじゃあ悪い結果じゃなかったのかもしれないな"



"女子２人の存在がそんなに悪いものじゃないと健二に認めさせることができたなら、それは意味のあることといえるんじゃないだろうか。"
"俺はそう思うことにする。この会話から脱出できるチャンスになるのだからなおさらだ。気づかない間に、ひどく長い時間が経ってしまっていた。"


stop music fadeout 2.0

scene bg school_dormext_full
with locationchange


"できるだけ急いでいつもの朝の手順をこなす。寮を出るときに腕時計をもう一度チェックして、すでに遅刻していることに気づく。"

scene bg school_scienceroom
with shorttimeskip

play music music_daily fadein 1.0


"幸い、その後の１日は平穏に進む。授業が終わった後、再び静音に会いに向かう。"

scene bg school_gardens2
with locationskip




"校舎の裏で、完成した屋台に寄りかかっている静音を見つける。屋台の一部には紙切れやテープの切れ端が残っている。前に使われたときの張り紙の名残だ。"
"静音はぼんやりと手の中で釘を回しているけど、俺にはまだ気づいていない。"





"静音にそっと忍び寄る誘惑は耐えがたい。外国の野生動物ドキュメンタリーを何年も見続けていたので、心の準備はできている。こちらは風下で、状況は理想的だ。"
"でも考えれば考えるほど、まずい考えなんじゃないかという気がしてくる。"




"途中で捕まったらただのバカみたいに思われる。俺だと気づかれなかったら、こっちがけがをするかもしれない。どっちにしても、思いやりがないと思われるだろう。"
"やっぱり変なことはしないほうが一番いいだろう……まったく面白くないけど。"


show shizu adjust_blush at center
with charaenter


"静音の正面に歩み寄ると、少しびっくりされる。"


his "何を驚いてるんだ？　さぼってるところを見つけちゃったか？"

show shizu behind_blank
with charachange


ssh "違うわ、休憩してたの"


his "汗一つかいたように見えないけどな。大した休憩じゃないか、生徒会長"

show shizu behind_frustrated
with charachange


"静音の目がしばらくあちこちに動く。どうやら動揺させることができたようだ。"


"怒った表情が顔に浮かぶ。すこし緊張しているのも見える。でも引き下がることはできないのだろう。静音にとっては問題外なんだ。指がいらついたように小刻みに動いている。"


show shizu basic_normal2
with charachange


ssh "今日は突っかかってくるわね。私を切れさせようとしてるの？　勝負がしたいの？　日が沈むまでにどっちがたくさん屋台を作れるか勝負よ"



his "違う、違うよ！　からかっただけ。いいって、ちょっとくらい生徒会長をからかえなかったら、それは本物の生徒会じゃない。そう思うだろ、な？"



show shizu behind_frown
with charachange


ssh "生徒会の会則にはそういう決まりはないから、それはないわ"


his "会則なんてないだろ！"


"少なくとも俺はあるとは思っていない。こいつらが忠誠を誓うのは出前メニューの山だけだ。"

show shizu adjust_smug
with charachange




ssh "とにかく、もっと早く来られたのかもしれないけど、来てくれてよかったわ。さっさと金づちを持って。昨日やり残したところから始めるわよ"





hide shizu
with charaexit

play ambient sfx_stallbuilding fadein 0.5


"また屋台の組み立てにとりかかりながら、思っていたよりも仕事の量がずっと少ないことにだんだん気づき始める。それどころか静音によれば、運が良ければ今日中には終わってしまうらしい。"


"この前に同じような作業をしたときは、静音、ミーシャ、そして俺でほぼ丸４日かかった。俺の思い過ごしなわけがない。"

stop ambient fadeout 2.0


his "なあ、これってあまり大した作業量に見えないぞ"

show shizu behind_blank at center
with charaenter


ssh "大した量じゃないからよ"

play ambient sfx_parkambience fadein 10.0


"その答えを聞いて、もう少し詳しく聞きたくなる。良くはないと知りつつ、静音はハンマーを置いて説明する。"

show shizu basic_happy
with charachange


ssh "１週間足らずで、たった２人でこれだけの作業をこなすのは不可能よ。ほんとのことを言うと、最初から屋台の半分は解体せずにしまっておいたの。しまうというより、その辺に隠しておいたってところかな"

show shizu adjust_smug
with charachange


"静音はいたずらっぽく指を振る。"

show shizu adjust_happy
with charachange


ssh "でも今のは秘密だからね。それに商売の秘訣をばらすのは不作法よ"


his "お前はマジシャンじゃないからな"

show shizu behind_smile
with charachange



"ウィンクしながら、静音はかばんからプラスチックの容器を２つ取りだし、手近な板の上に置くと、『ジャジャーン！』とでも言うかのように両手を少し持ち上げる。"


show shizu adjust_happy
with charachange


ssh "今日はお弁当を２人分作ってきたの"

show shizu behind_smile
with charachange


ssh "こっちを食べて。かばんの中で中身が片寄って、少し混ざっちゃったから"


"静音が弁当箱を１つ渡してくれる。それを開けてみる。とてもおいしそうだ。たった今思い出したかのように、静音は箸も渡してくれる。牛焼き肉に見える何かを俺は口に運ぶ。"


his "すごくおいしいぞ"


his "食べ物がほかの食べ物に触れるのは好きじゃないのか？"

show shizu basic_normal
with charachange


ssh "好きじゃない"


his "ずいぶん細かいんだな"

show shizu behind_blank
with charachange


ssh "自分で食べ物を混ぜることもあるけど、いつもじゃないし、何もかも混ぜるわけじゃない。勝手に混ざるのはいやなの。自分が選んでそうしてるってことが大事なのよ"

show shizu basic_normal
with charachange



"断固たる態度で指をさして力説すると、静音は割り箸を割って自分の弁当を食べ始める。"



"食べ続けながら、俺は２つのことに気づく。１つは、ご飯をのぞけば食べ物のほぼ全部が炒め物だということだ。野菜まで炒めてある。"



"そして肉があまりにも多い。静音はいつもこんな食事をしているのか？　これでどうやってあんなに細い体でいられるんだろう。"



"２つ目は、食べている間は静音と話せないことだ。口の中いっぱいに食べ物を含んだまましゃべるのはそもそも不作法だけど、両手が箸と器でふさがっていると、俺たち２人が会話をするのは不可能だ。昨日のように。"



"一緒に過ごしているのに、時間をかけて手話を身につけたのに、静音と話をする時間は少なくなっている感じがする。それなのに、俺は静音のことをもっと理解できているような気がする。"

stop music fadeout 4.0

show shizu basic_normal at tworight
show bg school_gardens2 at bgright
with charamove

show lilly cane_smileclosed at twoleft
with charaenter


"何かが屋台の１つをこつこつと叩く音が聞こえる。目を上げるとリリーが俺のそばに立っていて、杖であたりを探っているのが見える。"


hi "やあ"


"『見落とすところだったよ』と言いそうになるのを危ういところでこらえる。"

show lilly cane_surprised
with charachange


li "あら、久夫さんですか？　なんだかおいしい料理を作っている匂いがしたので、誰だろうって思ってたんですよ"

show shizu behind_frustrated
with charachange


ssh "なんて言っているの？"

play music music_happiness fadein 6.0


"手を動かしながら、まったく別の言葉をリリーに話すのは大変だ。だからミーシャはいつも全部の会話を手話にしているに違いない。ちょっとおかしな感じがするけど、そのほうがずっと簡単そうだ。"


show shizu basic_happy
with charachange


"静音は俺の通訳を見て、ジョークを聞いたかのようにうれしそうに指を合わせる。"

show shizu adjust_smug
with charachange




ssh "ここにある食べ物は全部一時間前に作ったの。一週間過ぎても紙切れ一枚提出できない誰かさんと違ってね。きっとあんたの時間のとらえ方はちょっとずれてるんでしょうね！"





hi "それは……ちょっとひどくないか"

show lilly cane_displeased
with charachange


"自分が耳にしなかった言葉への返事を聞いて、リリーがふと眉を寄せる。"


hi "ああ、悪い。遅い昼飯を食べてるところでさ。全部生徒会長が作ったんだ"

show lilly cane_reminisce
with charachange


li "生徒会長も今ここにいるんですか？"


hi "すぐそこにいるよ"

show lilly cane_listen
with charachange



li "失礼しました、気づきませんでした。普段なら彼女の存在感はずっと目立つんですけどね"
li "しかし生徒会が屋外でお昼を振る舞うなんて知りませんでした。どうして私は招待されなかったんですか？　でもこんなことをするくらい自由な時間があるというのは、いいことだと思います"


show shizu behind_frustrated
with charachange


ssh "なんて言ってるの？"



"……"


show shizu basic_angry
with charachange


ssh "私があんたを招待したところで、どうせ遅れてくるくせに"




"でも静音の言葉をリリーは認識することができない。その事実がますます静音の怒りをつのらせる。"


show shizu behind_frown
with charachange


ssh "ちゃんと一字一句訳してちょうだい。お願い"



"やけに丁寧な言葉遣いだな。自分の怒りをぶつけてくれと俺に頼むなんて、実に残念な話だ。"
"それでも、俺だって何もしないわけにはいかない。返事をして自分の考えを理解してもらうことさえできないなんて、寂しすぎる。静音は絶対に許してくれないだろう。"





"少しだけ言葉を柔らかくしようとしてみる。"


hi "まあ、ほんとのこというと、みんな何時間か前に作ったものなんだ"

show lilly cane_weaksmile
with charachange


li "本当ですか？　いいですね"

show shizu cross_angry
with charachange


ssh "こっちを向きなさいよ、話している相手にちゃんと向き合わないのはすごく失礼よ。上品で礼儀正しいレディの振る舞い方じゃないでしょう"


hi "俺の言ってることは静音の言葉の半分くらいなんだけど。静音は自分が話しているときに相手が自分の方を向いていないのはいやなんだって。静音なら、その、俺の声の右側にいるよ"


"とはいえ、こういう状況ではリリーがそうしないのもわかる。状況は非常に気まずくて、２人の会話の唯一の接点役をつとめるのはとても気疲れする。"


"実は、以前こうやって２人が衝突したときのことを度忘れしてしまっていた。静音が根に持っているのは明らかだし、リリーも彼女なりに敵意をむき出しにしている。"

show lilly cane_displeased
with charachange


li "ごめんなさい、そういうお作法はすっかり頭から抜けてしまっていました。生徒会長がいついかなるときも尊敬とルール厳守を求めるような人だってこと、忘れてしまってました"

show lilly cane_listen
with charachange



li "生徒会はみんなに厳しい統制を要求するんでしょうね。とはいっても、見るからにご自分のお楽しみの時間もあるようですし、常にそういうわけではないんでしょうけど"


show shizu adjust_angry
with charachange


ssh "生徒会は独裁じゃないし、ゼロサムゲームでもない！"

play sound sfx_snap


"静音は指先を銃身のようにリリーに突きだして、大きな音で指を鳴らす。リリーは一瞬ひるんで、明らかに不機嫌そうになる。"


show lilly back_listen
show lillyprop back_cane at twoleft
with charachange



li "そうですか？　ではこんなに長い間生徒会に入って、独裁者みたいに振る舞っていることになおさら感心しますね。そのしつこさには感服します。万事うまくやるには、とても責任感が強くないといけませんから"


show shizu behind_frown
with charachange


ssh "自分がそうありたいほどじゃないわ。あんただって自分のことは文句言えないんじゃないの？"

show shizu cross_rage
with charachange


ssh "あんたも責任感は強いわね。締め切りを延ばしてくれって頼んで、その延ばした締め切りぎりぎりまで仕事を引っ張ったり？　責任感の模範よね！"


hi "静音はそれ聞いて喜んでるよ。でも、リリーも結構責任感あるよねって言ってるみたい"

show lilly cane_surprised
hide lillyprop
with charachange


li "本当ですか？"


hi "大体はね……"


"リリーはあまりうれしくなさそうだ。"


hi "俺たち野外料理会をしてるわけじゃないんだ。ただの昼休みだよ。実は今度のお祭りの屋台を組み立ててるんだ"

show shizu behind_frown
with charachange


ssh "あんたは知らないでしょうね、絶対外出なんてしないだろうから。紅茶でも切らしたの？"


hi "町に行くの？　買い物？"

show lilly back_devious
show lillyprop back_cane at twoleft
with charachange



li "いえ。さっきも言いましたけど、通りかかっただけです。聞こえていなかったようですね。生徒会長の邪魔をしたくはありません。今は何もしていないけれど、きっと２人ともとてもお忙しいんでしょう"



show lilly cane_listen
hide lillyprop
with charachange


li "とにかく、久夫さん、必要があれば生徒会長はきっと仕事を見つけるなり思いつくなりしてくれると思いますよ"



show shizu cross_rageclosed
with charachange


ssh "ギッタギタにしてやる！"




hi "そうだな、すごい忙しくなるよ"



"『ギッタギタ』は難しい言葉だ。自分にも読めたのがうれしい。そんなことに喜んでいる場合ではないけど。ただ、これで２人の言い争いは終わりそうだ。これには祝杯をあげたっていい。"





show lilly cane_listen
with charachange



li "ごきげんよう、久夫さん。さよなら、生徒会長"



hi "ありがと、リリーもな"

show shizu basic_frown
with charachange


ssh "お上品ぶってなさい"

hide lilly
with charaexit

show shizu basic_normal2 at center
show bg school_gardens2 at center
with dissolvecharamove

stop music fadeout 4.0


"リリーが去ったとたん、静音は弁当の残りを全速力でかきこむ。まるでその一口一口が、今の出来事が最初から起きなかったがごとく忘却に追いやる手段であるかのように。"

hide shizu
with charaexit



"食べ終わると、静音は同じ精神状態を保ったまま組み立て作業に舞い戻る。いらだちを仕事で発散しているのはいいことだけど、もう話をするような気分ではないようだ。"



show bg school_gardens2_ss
with shorttimeskip

play music music_tranquil fadein 3.0



"休むことなしにすべての屋台を片づけ、二時間ほどして静音は手を止める。"




"まだ静音には近寄りづらい気がする。会話というのはあっけなく終わってしまうものなんだな。二人きりになって直接話ができるようになるまでこんなに時間がかかったというのに、つらい気持ちになってくる。"


show shizu basic_normal_ss at center
with charaenter


ssh "翻訳、上手だったわ"




his "ほんとか？"

show shizu adjust_happy_ss
with charachange


ssh "一流よ！"


"静音はサムズアップで強調する。"

show shizu behind_blank_ss
with charachange


ssh "……あなたのレベルにしてはね"

show shizu basic_normal_ss
with charachange


ssh "学校には聾の生徒は多くないし、手話のクラスはずいぶん前から閉鎖されそうになってる。クラスメイトだってあまり多くないでしょう、違う？"

show shizu behind_blank_ss
with charachange



ssh "今手話を習っているだけだったら、速度はあまり伸びないの。だから興味もなくなってしまう。単にコミュニケーションを取るだけでも、普通よりもたくさんの労力が必要だから。どんな言語でも同じことだろうけど"


show shizu basic_normal2_ss
with charachange


ssh "こういう状況だと、そもそも手話による会話は本来の……なものではなくなってしまう"


his "今の単語わからなかったぞ。何じゃなくなるって？"

show shizu behind_blank_ss
with charachange

show shizu basic_normal2_ss
with charachange


ssh "じ—{w=0.2}は—{w=0.2}つ—{w=0.2}て—{w=0.2}き—{w=0.2}な"


show shizu behind_blank_ss
with charachange


ssh "これを本当にとらえることができるのはミーシャだけよ"


his "ああ、それは間違いないな"

show shizu behind_sad_ss
with charachange

show shizu behind_blank_ss
with charachange


"一瞬だけ静音の表情が変わり、それを理解する前にあっという間に元に戻る。でもそれを追及してはいけないんだろうという気がする。"


"俺が本当に知りたいのは……"


his "どうしてリリーとそんなにけんかするんだ？"

show shizu basic_frown_ss
with charachange


"体を堅くして、見るからに顔をしかめ、静音は何度も両手の指を合わせたり重ねたりする。目に見えないトランプをシャッフルするかのようだ。"

show shizu behind_frustrated_ss
with charachange




ssh "あなたが見た２回は、『そんなに』というほどたいしたものじゃないわ。去年学校にいたなら、そういう言い方もできるでしょうね"




his "大変だったらしいな。校則でバッジをつけさせようとしたとかなんとか"

show shizu cross_wut_ss
with charachange


his "はは、驚いたか？　その件は後で聞かせて欲しいけど、マジで、でも……お前、リリーのことあまり好きじゃないんだろ？　はぐらかすなよ"

show shizu behind_frustrated_ss
with charachange



ssh "何もはぐらかしてなんかないわ"


show shizu basic_angry_ss
with charachange



ssh "リリーも去年まで生徒会に所属してたの。お互いあまりうまが合わなかった。リリーは前の生徒会と同じように物事を進めようとした。前の生徒会は本当に無能だった。バカだったし、失礼だった"


show shizu behind_frown_ss
with charachange


ssh "私はもっと多くのことがしたかった。それでけんかになったの"

show shizu basic_frown_ss
with charachange



ssh "いっぱいけんかをした"



show shizu adjust_angry_ss
with charachange


ssh "リリーはいつも締め切りを守らなかった"

show shizu behind_frustrated_ss
with charachange


ssh "そしたら、私がやっていることは無意味な、ただのよけいな時間つぶしだって言ってきた。これが意味のない暇つぶしに見える？"


"静音は俺たちのまわりを手振りで示す。"

show shizu basic_frown_ss
with charachange


ssh "無意味なのは何もしない生徒会の方よ。無力で、怠惰で、退屈な。とびきり退屈！"

show shizu adjust_angry_ss
with charachange



ssh "何もしないで部屋に座ってても心は躍らないのよ。そんなのただの時間の無駄。どうしてそんなとこにいなきゃいけないの？　それじゃ私の血はたぎらない。リリーと言い争うと私の血はたぎるのよ！"



show shizu behind_blank_ss
with charachange



ssh "あのときあれだけリリーがやる気を出していたなら、今こんなに熱心に私につっかかる必要もなかったのに"
ssh "でもあれだけの気合いを見せているなら、全くの無駄じゃない。少なくとも何かは残ったわけだし！　まだ心は躍るわね"



his "なるほどな"


his "それでバッジの話は？"

show shizu adjust_happy_ss
with charachange

stop music fadeout 4.0


"静音は笑う。その笑いを隠すかのように手で口を覆っている。自分の笑いだけは、静音がいつも隠そうとする唯一のものだ。"

show shizu behind_smile_ss
with charachange


ssh "あんなの、ただの冗談よ"

show shizu adjust_happy_ss
with charachange


ssh "時にはお楽しみも大事なのよ"

stop ambient fadeout 0.5

scene black
with dissolve



label jp_S15:

scene bg school_dormext_full
with locationchange

play music music_normal fadein 0.5


"翌日、寮舎の近くの自販機でいつも買っているお気に入りの缶コーヒーが売り切れていて、昼休みの始めにあちこち探して回る羽目になった。思ったよりも長い回り道になってしまった。"

scene bg school_gardens
with locationchange


"最近は何もかも忙しすぎて、校庭を歩きながら普段と違う匂いがする理由に気づくのにもしばらく時間がかかる。芝刈りが行われたばかりだった。"


"しばらく立ち止まってあたりを眺める。生徒のグループがいくつかいて、おしゃべりをしたり、芝生の上で遊んでいたりする。その先の小道で先生たちが数人話し合っている。とても牧歌的な光景だ。"


stop music fadeout 2.0


"残念なことに、しばらくして恐怖が間近に迫っている感覚が体に這い登ってくる。自分が一人じゃないという感覚が。"

play music music_kenji fadein 0.5

show kenji neutral at center
with charaenter


ke "よう、久夫、お前か？"


hi "ああ、俺だよ"


"こいつが切り裂き魔か何かじゃなくて健二だったことに感謝すべきなんだろう。まるで俺以外の誰かと会話しているかのように、健二は話し始める。"

show kenji happy
with charachange


ke "やっぱり。その髪型、間違えようがないぜ。普通の人なら絶対そんな頭しないからな"


"無意識に俺は後頭部に手をやる。自分のやっていることに気づいて、俺はバカにされた気分になると同時に、腹も立たないくらい驚愕する。"


hi "ああ……ここで何してるんだ？"

show kenji neutral
with charachange


ke "気温を計ってる"

show kenji happy
with charachange



ke "もうすぐ冬がくる。女どもが外出してセックス・アンド・ザ・シティ式のパワーランチを食べて、人が一杯の都市部で邪魔くさい群れをなして並んで歩くには寒すぎる時期になる"





ke "すると、男たちはふたたびのびのびと通りを歩くことができるようになる。自分たちの遺産を取り戻すことができるんだ"

show kenji neutral
with charachange


ke "その日が来たときに備えて、俺はこの一週間ピザしか食べてないんだ。エネルギーを蓄積するためにな"


hi "そっか"


hi "熊もそういうことするよな"

show kenji happy
with charachange


ke "それがなんだよ？　熊から学べることはたくさんあるんだぞ"


"健二は自分自身に同意するように、力強くうなずく。"

show kenji neutral
with charachange



ke "よし、じゃあこれはどうだ。今日、ミルクを買いに町に出た。新しい店員がいたんだ。ホッケースティックが２本描いてある野球帽をかぶってる格好付けてそうな女子だ。これを格好つけホッケー野球帽女子と呼ぼう"





ke "ミルクに値札がついてないことに気づいて、その女子にこっちに来て値札をつけろと言ったんだ。将来の世代のためにな"



"今日町に行ってたって？　朝の授業をさぼったに違いない。どやしつけてやりたいけど、こいつの言葉の奔流にさえぎられて、割り込むことができない。"


show kenji tsun
with charachange



ke "その女、自分は気分が悪いから邪魔するなと言ってきたんだ。気分が悪い？　気分が悪いだと！？　俺たちは社会生活してるんだぞ。気分が悪いくらいで人同士のコミュニケーションから逃れられると思ってるのか"
ke "今朝起きるだけで俺がどれだけの労力を費やしたと思ってるんだ？　今だって労力を費やしてるんだがな"


show kenji rage
with charachange




ke "こっちは仕事中に{b}ホッケー野球帽{/b}を、しかも{b}屋内で{/b}かぶってる勘違いオシャレ女子大生ごときに重要な質問をシカトされるために、わざわざ朝っぱらからミルクを買いに行ったわけじゃないんだよ"





show kenji tsun
with charachange


ke "とにかく、俺は店の品物をきちんとさせたかっただけだ。値札の付いてないミルク？　そんなもの見つけたら、疑問がわいてくるだけだ。それも重要な疑問だ。答えるのがその女の仕事だろうが、ったく"


ke "女ってやつはこれだから困る。義務感ってものがない"

show kenji neutral
with charachange




ke "俺、よく下痢するんだ。でも文句を言ったりしてないだろ。俺はとにかく困難に耐えて、やるべきことをやるんだ。男ってのはそういうものなんだよ。下痢してたって、前に進み続けるんだ。よりよい明日を夢見て"




hi "あのさ、しょっちゅう下痢するってのは良くないと思うぞ"


hi "そんなにミルク飲むのやめた方がいいんじゃないか"


ke "そんなことできるかよ、そのおかげで今の超絶パワーを保ってるんだぞ。それにこの世界では……女の尻に敷かれる男がどんどん増えている社会で、男の力ってのは絶対に奪うことのできない唯一のものなんだ"



show kenji happy
with charachange


ke "だから俺はあっちこっちにふたを開けたオリーブのビン詰めを放置しているんだ。そういうことができるんだってことを示すために"


hi "開けた後は冷蔵庫に入れてるか？"

show kenji tsun
with charachange


ke "はあ？　そんな、知るかよ、どうだっていいだろ"


hi "開けた後は要冷蔵だろ。小学生のガキだって知ってるぞ"

show kenji neutral
with charachange


ke "奴らはそもそもビンのふたも開けられないから、関係ない"


hi "ああ、それはそうだな"

show kenji happy
with charachange


ke "俺って天才だろ"



"満足げにあごをなでる。俺はそれが科学者のするしぐさだとばかり思っていた。そして武藤先生に会ってから、ひどくがっかりする羽目になった。"


show kenji neutral
with charachange


ke "とにかく、もうあの店には行けない。明らかにビッチどもが幅を利かせてるからな。ただ……変装すれば話は別だ。別の眼鏡をかけるとか"


hi "史上最悪の変装だな"

show kenji tsun
with charachange



ke "ぷー、もう何年も完璧に通用してますぅー。そもそも眼鏡なんてなくたって目は見えるんだよ。これは見た目のためだ。それと顔を隠すために。スーパーマンみたいだろ"





hi "史上最悪だ"



show kenji happy
with charachange


ke "いっとくけどな、人が俺の学生証見ても、俺だってわからないんだぜ"


hi "ほんとか？　見せてみろよ"

show kenji neutral
with charachange


ke "それはだめだ。誰彼構わず学生証を見せびらかすわけにはいかないんだよ。大昔に作ったんだ。時代が違うんだよ。ヒッピーみたいな髪型だったんだ"

stop music fadeout 2.0


"その様子を想像しようとしていると、健二は眼鏡を外す。"

$ ksgallery_unlock("evul kenji_glasses_closed")
scene evbg kenji_glasses:
    truecenter
    subpixel True zoom 0.82
    acdc_warp 20.0 zoom 0.8
show evmg kenji_glasses_closed at kenji_mg_out
show evfg kenji_glasses:
    truecenter
    subpixel True zoom 1.0
    acdc_warp 20.0 zoom 0.8
with whiteout

play music music_friendship




"眼鏡を外したとたんに健二は目を細める。おかげで実際よりもずっと疲れているように見える。"
"健二の言うとおりだった。確かにとても違って見える。もう何年も寝ていないかのようだ。でも、うまい変装と呼べるほどの違いじゃない。"



hi "お前よく寝てないんじゃないか"

$ ksgallery_unlock("evul kenji_glasses_frown")
show evmg kenji_glasses_frown at kenji_mg_out
with charachange


ke "いや"


hi "寝不足っぽいぞ"

$ ksgallery_unlock("evul kenji_glasses_normal")
show evmg kenji_glasses_normal at kenji_mg_out
with charachange


ke "んなわけあるか。これは真実を目撃した男の目だ。シャーマンの目だよ。想像もつかないような、ひどいことだ"


ke "ボトルシップを作ったら母ちゃんが上に座ったときみたいに。そこら中が血と花柄の布切れだらけだった。人生経験ってのはそういうもんだ"



"健二が正真正銘のトラウマになりそうな過去の経験を話してくれたのはこれが初めてだと思う。でもあまり恐ろしがっている風には見えない。"





"ついでに、こいつは俺から３０度くらい左にずれた方向に話しかけている。ということは視覚障害は本当なんだろう。それでも念のため目の前で手を振ってみるけど、何の反応もない。"




ke "ったく、わかってると思うけど冗談だぞ"




"わかったふりをして、俺は笑う。どうしてか、健二と目を合わせるのがいつもよりも難しい。"

show evmg kenji_glasses_closed at kenji_mg_out
with charachange


ke "ちょっとした小ネタ、知ってるか？　目の小さい人はでかい眼鏡をかけるんだ"





hi "どっかで読んだことあるな。そのほうが目が輝いて見えるからだって"




ke "そうなのか？　知らなかったぞ"

stop music
$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_scratch


scene bg school_gardens
show kenji tsun at center
with locationchange

$ renpy.music.set_volume(1.0, 2.0, channel="sound")


"健二は眼鏡をかけ直す。おかしな話だけど、一瞬それを見て安心する。でも眼鏡をかけていようがいまいが、目の前のこいつの相手はしないといけないことを思い出す。"

play music music_kenji fadein 2.0


ke "まあ、とにかく……どっかの絵描き女が俺の肖像画を描きたいと言ってきたんだ。確か。そいつの言っていることが理解できるまで５回くらい話しかけなきゃいけなかった"


"琳に違いない。たぶん。"


hi "その子、どんな格好だった？"

show kenji neutral
with charachange


ke "知らねえ。サンダルはいてる女だった"


"もう少し具体的に言ってくれればいいのに。『腕がなかった』とか。確かに琳はサンダルを履いてるけど、ほかにもサンダルを履いてる気ままな絵描きの女子生徒がいる可能性は結構高いと思う。"

show kenji happy
with charachange



ke "そりゃ考えたさ。いつか自分の存在を証明する文書をすべて焼き払った後に、肖像画を残すくらいはいいだろうって。人々がそれを見て、人類の救い主のことを思い起こせるように。彫像を作るのに必要だからな"




show kenji neutral
with charachange


ke "でももう少し考えて、結局拒否することにした。いい話だったけど、そいつは学校の課題か何かのために描きたかったんだと。絵も展示されるんだと"

show kenji tsun
with charachange


ke "そしたらみんな俺がどういう奴か聞くだろ。でも俺はまだ社会を救ってない。だからこれじゃ意味がないんだ。それに誰かが俺の顔に気づいたら、俺自身のことを説明しなきゃいけない"


ke "そういう一連の出来事にはそもそも関わりたくないんだよ。なんだか妙な状況に巻き込まれたくないんだ。そういうクソッタレな事態はしょっちゅう起きるんだ。目立てば確実にリストに載っちまう"

show kenji neutral
with charachange


ke "だから俺はこんなに念を入れて日常生活の中で周りの奴らにとけ込む努力をしてるんだ。次の一手を打てるまでな"


hi "だろうな"


hi "リストって何だよ？"


ke "リストならいくつもある"

show kenji happy
with charachange


ke "で、お前ここで何してんだよ？"


hi "なにも。たまたま来ちゃっただけさ"


ke "俺なんかしょっちゅうだぜ。まあお前はそれで問題なければいいけどな。俺もう寮に戻るわ。テレビの録画予約しないと"


hi "テレビ持ってるのか？"


ke "ああ。たまにはうちに来いよ。一緒に試合見ようぜ。ハイデフで"

stop music fadeout 4.0

hide kenji
with charaexit


"いったい何を言っているのかと尋ねる前に、健二はいなくなっていた。来たときと同じように去っていった。人のことなんてまるで考えていない。ある意味驚きだな。"


"やっと健二もいなくなったので、華々しい姿の夏の校庭をあてもなく眺める作業に戻る。でも無駄だった。あいつのせいで台無しだ。"

scene bg school_cafeteria
with locationchange

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 1.0



"疲れ切ってはいるけど生きたまま食堂に戻り、また静音と昼でも食べるかと考えるけど、当人はもうミーシャと一緒にテーブルについている。"




"ほかの誰かだったら、二人の声が聞こえるには遠すぎるだろうと考える。でもこれはほかならぬ静音とミーシャだ。"



"その気になれば、二人の会話を『盗み聞き』することも簡単だ。なんて卑劣な考えだろう。でもできるんだ……やりたいとは思わないけど。"



"たった数日だとしても、きっと積もる話がたくさんあるんだろう。二人をそっとしてやりたい気分になる。"


"でも俺の姿を見た瞬間、二人は俺を招き寄せてくる。"

show misha hips_grin at twoleft
show shizu basic_normal at tworight
with charaenter

stop ambient fadeout 5.0
play music music_shizune fadein 1.0


mi "こんちは、ひっちゃん～！"


"ほんの少し離れていただけなのに、ミーシャの声をまた耳にするのは神経にきつくて、俺は顔をしかめる。"



"この数日、静音との会話がほとんど無音だったことを忘れきっていた。きちんと会話することに集中しているうちに、周りの雑音もシャットアウトしてしまっていたんだ。"


"まあ、またそのうち慣れるだろう。ミーシャが戻ってきてくれてうれしい。"

show misha sign_smile
with charachange


mi "遅れてた勉強、全部追いついたよ～！　ちょうど間に合ったよ～、これで七夕祭りも参加できるよ。わはは～"

show shizu adjust_smug
with charachange


ssh "本当に参加禁止なんて言い出したら、私が生徒会の名目で引っ張り出すから"

show misha perky_confused
with charachange



mi "本当に参加禁止なんて言い出したら、しっちゃんが生徒会の名目でわたしを引っ張り出してくれるの～？"



hi "それは職権乱用だろう"

show shizu behind_frown
with charachange


shi "……"

show misha hips_frown
with charachange


mi "それはちがうよ、ひっちゃん～！"

show misha sign_smile
with charachange



mi "もし七夕祭を運営する生徒会メンバーが二人しかいなかったら問題になるでしょ、違う？　そうだよ～、絶対！　少なくとも三人はいなきゃ！　みんなのためなんだから、完璧に筋が通ってるよ、必要なんだよ～！"


show shizu adjust_happy
show misha perky_smile
with charachange



"ミーシャがなんだか物騒な軍隊っぽい自己正当化を、子供っぽくて陽気で大げさな抑揚でまくしたてている間、静音はほんの少しテーブルに乗り出している。"


"でも静音はとても楽しそうに見える。両手の指を重ねて、自分のかわりに真剣そうに頬を膨らませるミーシャの横で笑いを抑えようとしている。"


hi "まあ、そう言うなら"


"実は俺も、今は楽しいと思っている。みんなが、俺たち三人が、お互いこんなに気楽に話せているから。"


"最初は、自分がまずい立場に置かれているかもしれないと思っていた。静音も新入りの案内役なんて役目を押しつけられるのはごめんだろうと確信していた。"


"俺自身もそんな面倒をかけるのはいやだった。静音が聾唖者でなかったとしても気まずかっただろう。"



"たった今、静音は俺たち全員が、生徒会のフルメンバーがお祭りにいなくてはだめだと言った。七夕祭に対して生徒会がなにか権限を持っているとは思わない。みんなで七夕を過ごしたいという、静音なりの表現なんだ。"



"友達がいるってのはいいもんだ。"


"単純な考えだけど、こんなに簡単に仲良くなれたということに、本当に満ち足りた気持ちになる。回りくどい言い方だとしても、そもそも言葉にするくらい静音が強い思いを抱いていることをうれしく思う。"

show shizu basic_normal
with charachange


ssh "どうして私たちが手を振るまでこっちに来て座らなかったの？"



"出し抜けに質問が飛んでくる。ミーシャが質問を繰り返す間、静音の目が答えを待ちかねている。ちょっとからかってやろう。"


hi "そんなに俺に一緒に座ってほしかったのか？"


show shizu behind_blank
with charachange


ssh "私たちは生徒会に所属しているんだから。できるだけ一緒に座るべきよ。それが道理でしょ"



show shizu adjust_happy
with charachange


ssh "それに、こんな美少女二人と一緒に座るチャンスに飛びつかない人なんていないでしょ"


"言葉を切る。こっちが『そこまでかわいくないだろ！』みたいなことを言って負け確定の状況に陥いるのを待っているんだ。俺が餌に食いつかなかったので、静音はさらに活気づいて話し続ける。"

show shizu basic_happy
with charachange


ssh "あなたは異常ね"




"そういう締め方をされるとは思わなかったぞ。"


hi "安易に人を異常呼ばわりしすぎだろ。ほんとに失礼だな"

show shizu adjust_smug
with charachange


ssh "そっちこそ安易に人を失礼って言ってる。あなたも失礼だし、失礼なのも異常。だからあなたは二重に異常ってこと"


hi "そうはならないだろ。こういうのは程度で決まるんだよ"


show misha hips_grin
with charachange


mi "ははは～"


"頬杖をつきながら、ミーシャは目を閉じてゆっくりと低く笑う。"


hi "笑うなよ……"

show shizu behind_blank
with charachange


ssh "こんな状況で笑うんじゃないの"



"俺が自分で手話をしているのにかまわず、ミーシャが俺の言葉をすべて手話で伝えていることに気づく。無駄な行為だけど、ミーシャにとっては無意識の行動なんだ。でも俺だって手話をやめるわけにはいかない。"




"ミーシャが戻ってきたからというだけで手抜きをして手話をしなくなったら、今までやってきたことは何だったんだ？　身についた手話を忘れる危険はおかしたくない。今だって、手を使って会話するととても遅いんだ。"


show misha sign_smile
with charachange



mi "ひっちゃん、もうしっちゃんと二人ですごくいっぱい話してるね～！　やりとりがすごく面白いよ～！　おしどり夫婦みたいだよ、でしょ～でしょ～？"





"今のはいろいろと意味深すぎるだろう。でもミーシャだし、わざと言ったとは思えない。"


hi "ほめ言葉になってないぞ"



"俺たち二人をくっつけようとするミーシャの言葉にも、静音は反応しない。見ていなかったのかもしれない。"
"前から気づいていたけど、時々そういうことがある。そんなに簡単なことだろうかと思うし、どうしていちいち気になるんだろうかとも思うけど、あまり深く考えたくはない。"




"そろそろこの場を離れたい。ミーシャが静音と一緒にいるのを邪魔している気がしてならないし、ミーシャもそう思ってわざと割り込んだのかもしれない。でも二人とも俺を帰してはくれない気がする。"
"ある意味、優しすぎるんだよな。"



hi "とにかくさ、静音、そこまで聞きたいなら言うけど、こっちに来たくないと思ったのは邪魔したくなかったからだよ"


hi "ミーシャが補習とかで一緒にいられなかったから、二人とも積もる話があるだろうし、それを邪魔しちゃいけないなと思ったんだよ。だから近づかなかったんだ"



hi "心配するなよ、ミーシャ。静音を独り占めしたいわけじゃないから"


show misha cross_laugh
with charachange


mi "わはは～！　ひっちゃん！　そういうのじゃないよ～"

show shizu basic_normal
with charachange


shi "……"

show misha hips_smile
with charachange


mi "ひっちゃん、とっても親切なんだね！　しっちゃん反省してるって～、謝ってるよ"


hi "別に謝るようなことじゃないだろ、気にするなって。なあ二人とも、ミーシャも戻ってきたことだし、なにかお祝いすべきじゃないか？　俺はそう思うぜ"

show misha cross_frown
with charachange


mi "ひっちゃん～！　遅れた勉強を取り戻すのはお祝いするようなことじゃないでしょ、普通は"

show shizu adjust_happy
with charachange


ssh "いいえ、いい考えだわ"


hi "タイミングもばっちりだし、生徒会だってたまにはちょっとお楽しみがあるべきだって静音も言ってたしな。ミーシャだって聞いてるだろ？　問題ないさ"

show shizu behind_blank
with charachange


shi "……"



hi "というか、ちょっと待てよ。そもそも授業をさぼりすぎてたから補習を受けるはめになってたんじゃなかったのか？　お祝いするのに授業をさぼってたら、なんかバカみたいだぞ"
hi "タイミングは微妙かもしれないけど、放課後に行ったっていい"


show misha sign_smile
with charachange


mi "どこに行く？"


"答えを考えることもせず、ミーシャが静音の問いを大声で口にする。二人とも完全に俺を無視している。"


hi "おい人の話を聞けよ、そこの二人組近視眼生徒会チーム！"



show shizu adjust_smug
with charachange


shi "……"

show misha hips_grin
with charachange


mi "わはは～！　ひっちゃんだってチームの一員だよ！"



hi "あー、そうだな。そうかも"

show misha hips_smile
with charachange


mi "そうだそうだ～！　そうなんだよ、ひっちゃん！"

show shizu behind_smile
with charachange


ssh "本当、物忘ればかりで厄介よね。あなたに惚れちゃう子には同情するわ"


show misha sign_smile
with charachange


mi "さてと～！　どこに行くのがいいかな？"


"一番気乗りしていなかったミーシャが今ではすっかり乗り気なので、それを突っ込みたくて思わず笑い出してしまう。でもどういうわけかそれを口にする気にはならない。それでもいいんだ。"

stop music fadeout 4.0


"行き先について少し話し合ったけど、結局俺たち三人が知っていて、かつ行く気になれる場所は上海しかなさそうだ。"


"お祝いする場所として喫茶店は悪い場所じゃなさそうだ。特に間違いなくケーキが食べられるとわかっている。ケーキはお祝い用の食べ物として一番だ。"

scene bg suburb_shanghaiext
with shorttimeskip


"それに、しばらく優子さんに会っていない。静音とミーシャもだ。こうした諸々の理由と、とても近いということもあって、気づいたときには二人とともに小さな喫茶店の正面に立っていた。"

play sound sfx_storebell

scene bg suburb_shanghaiint
with locationchange

show yuukoshang neutral_down at center
with charaenter


yu "いらっしゃいませ！"

play music music_dreamy fadein 2.0


"優子さんの声を聞くのも久しぶりで、そのあいさつの気合いの入りぶりにまたしても驚かされる羽目になる。極度に緊張したミーシャみたいなものだ。"

show yuukoshang neutral_down at tworight
show bg suburb_shanghaiint at bgright
with charamove

show misha perky_smile at twoleft
with charaenter


mi "こんちは～！　でも～！　わたしたちの時は、毎回それやらなくてもいいんだよ"

show yuukoshang worried_up
with charachange


yu "やらなきゃだめなの……"

show misha sign_confused
with charachange



mi "でも――"


show misha cross_laugh
with charachange


mi "おっけ～！　おっけ～！　優子さんがそう言うなら！　ははははは～！"



"二人が話している間に店内を見回すといつものように客がいない。今はランチタイム。こういうお店にとってはピークの時間だ。なのに毎度のごとく人の気配がない。わけがわからない。何か理由があるとしか思えない。"


show yuukoshang worried_up at center
show misha hips_smile at left
show bg suburb_shanghaiint at center
with dissolvecharamove

show shizu behind_blank_close:
    yalign 1.0 xpos 1.0 xanchor 0.8
with charaenter


"静音がそっと俺の腕を叩いて注意を引く。"

show shizu adjust_happy_close
with charachange


ssh "何を頼む？"

show yuukoshang neurotic_up
with charachange


"ミーシャが反射的にその質問を伝えると、優子さんは少し動揺したようだ。"


yu "だ、だめよ、それは私が……聞かなきゃ……ご注文はおきまりですか？"


show shizu behind_smile_close:
    ypos 1.1
show misha perky_smile:
    ypos 1.14
with dissolvecharamove



hi "とりあえずコーヒー、かな。どうも"


show yuukoshang neutral_down
with charachange


"ウェイトレスの仕事に対する優子さんの熱心さはある意味尊敬に値する。オーダーの後にケーキと飲み物をテーブルまで持ってくるときの素早さもだ。"

hide yuukoshang
with charachange

show shizu behind_smile_close:
    closeright
    ypos 1.1
show misha perky_smile:
    twoleft
    ypos 1.14
with charamove


"とはいえ、俺たち以外に客はいないわけで。満員の時にどうなるかはわかったものじゃない。"


"静音とミーシャはすぐにむしゃむしゃとケーキを食べ始める。食器を手に持ったままでは話せないからだろう。"


"そもそも友達といっしょにこうして食事をするのは、食べながら会話をするためだ。二人も同じ考えでいるというのは理にかなっている。"


"二人が空のお皿にフォークを置く音が鳴るのを聞いたとき、俺はまだケーキを半分も食べていなかった。"


hi "早食いは体に悪いぞ"

show misha hips_grin
with charachange


mi "ははは～！　ひっちゃん、それおじいちゃんみたいだよ～！"




"身が縮む思いがする。一発殴られた気分だ。"

show shizu adjust_happy_close
with charachange


shi "……"

show misha sign_smile
with charachange


mi "明日は浴衣を着るの、ひっちゃん？"


hi "いや、そもそも浴衣がないし。あったとしても俺はそういうことをするタイプじゃないから"


hi "お前たちはどうなんだ？　二人とも着るのか？"

show shizu behind_blank_close
show misha perky_smile
with charachange


ssh "もちろん"


hi "『もちろん』ってどういうことだよ？　前は着飾ったりしなかっただろ"

show shizu basic_normal2_close
with charachange


ssh "一度そうだったからっていつもとは限らないでしょ！　だいたい状況がまるで違うんだから。七夕じゃなかったのを抜きにしても、学園祭は学校の敷地内で開催したのよ。生徒は学校内では制服着用よ"


"冗談なのは明らかだけど、その言い方はいつもとまるで変わらない。それは普通ではないけど、静音のユーモアのセンスが普通であったためしはないし、俺ももう慣れている。"


"静音は真剣なことをとんでもない風に言うよりも、とんでもないことをさも真剣そうに言うほうが少しだけ得意なんだろう。"


"とにかく、それ以上に悩ましいのは、静音の手話にあわせて頭の中で声が聞こえ始めているということだ。それが静音の手話を逐一読み上げるミーシャの大きな声とぶつかり合って、わけがわからなくなってくる。"

show shizu behind_smile_close
with charachange


ssh "こんどはちゃんと着飾るわよ！"

show misha sign_smile
with charachange


mi "こんどは着飾るよ～！　見ててよ、ひっちゃん！"

show misha hips_smile
with charachange


mi "しっちゃんだけじゃなくて、わたしもね～！"

show misha hips_grin
with charachange


mi "もしかしたら～、髪型も変えるかも"


hi "それはよせよ、ミーシャが違う髪型なんて想像できないぞ"

show shizu adjust_happy_close
with charachange


"静音が指を振って笑顔を見せる。"

show shizu adjust_smug_close
with charachange


ssh "あっさり否定してくれるじゃない。私が髪型を変えたらどうなるでしょうね？"




hi "髪伸ばしてドリルみたいにしたらいいんじゃないか"

show shizu behind_blank_close:
    xpos 1.0 xanchor 0.8
show misha hips_smile:
    left
    ypos 1.14
with dissolvecharamove

show yuukoshang neutral_up at center behind misha
with charaenter


"面白くなさそうだ。幸い、優子さんがこっちに来るのが見える。たぶん食器を下げて追加の注文がないか聞くためだろう。"


hi "優子さん、七夕は何かするんですか？"

show yuukoshang panic_up
with charachange


yu "えっ？"


"そばを通りかかりながらスムーズにコーヒーのおかわりがいるか尋ねる練習をしていたみたいだけど、先に質問されてしまってどうしたらいいかわからないようだ。悪いことしたな。"

show yuukoshang worried_down
with charachange


yu "うん、その……仕事してる……"

show misha perky_sad
with charachange


mi "優子さん～、休日に働かされるの？　え～～～～……"

show yuukoshang neutral_down
with charachange


yu "あの、うちは休日が一番忙しいから。あと旅行客の人も。だから気にしてないわ。全力を尽くさないとね"

show shizu adjust_happy_close
show misha perky_smile
with charachange


ssh "とてもよくわかるわ。尊敬しちゃう"



"最善を尽くすという、自分と同じ決意を共有する優子さんに親近感を抱きながら、静音がうなずく。"
"でも静音にとってはそれはプライドの問題だけど、優子さんはこの仕事と、あと多少の給料アップがなければ本当にやっていけないと思っているだけかもしれない。"



hi "一番忙しいんですか？　じゃあ休日は平均でどれくらいお客さんが来るんですか？"

show yuukoshang neurotic_up
with charachange


yu "あー、その……"

show yuukoshang worried_up
with charachange


yu "……"

hide yuukoshang
with charaexit

show shizu behind_smile_close:
    closeright
    ypos 1.1
show misha perky_smile:
    twoleft
    ypos 1.14
with dissolvecharamove



"優子さんは逃げ、マドラーの入ったカップを洗い始める。失礼だな。ちゃんとしたウェイトレスの接客態度じゃないだろう！　でも何となく答えはわかった気がする。明らかに、商売はよくてカツカツなんだろう。"






"そもそもどうして上海が営業を続けていられるのか、と再び疑問に思う。以前はこういう和洋折衷式の喫茶店がとても流行っていたけど、今ではその流行も過ぎていて、改装するまでそのままにしているだけなのかもな。"




"もしかしたら店のオーナーが金持ちで誰かと賭けみたいなものをしているのか、あるいは誰が一番浪費するかを見るいかれた計画に熱中しているのか。"
"たまたま俺がここに来るたびに、大勢の客と数秒の差で入れ違いになっているだけなのかもしれない。"







"あるいは、ここはただの武器商人の窓口なのかも。"


hi "ほかに誰もいないし、優子さんもいっしょに座りませんか？"


"この店の客の入りについて話せるだろう……でも優子さんは誘いに乗らずに、頭を力強く左右に振る。"

show misha hips_grin
with charachange


mi "七夕のお祝いとか、こういうときに着飾ったりするのって、今まで一度もしたことがないんだ～！　やっと浴衣が着られるよ。やったやった～！"


hi "一度もないってどういうことだ？　去年はどうしたんだよ？"

show misha sign_smile
with charachange




mi "ん～……去年はしっちゃんと、わたしと、３－２の目の見えないクラス委員とでお祭りの屋台をやったんだよ！　焼きそばの屋台だった、と思うよ～？　うん、そうだよ～！　確かに！"



show shizu adjust_blush_close
with charachange


"３－２の目の見えないクラス委員はリリーに違いない。この顔ぶれがいっしょに何か作業ができるなんて驚きだ。でもそういう状況では無邪気なミーシャが一番いい緩衝材になるだろう。"


show misha hips_grin
with charachange


mi "しっちゃんが料理して、リリーが注文を取って、わたしが二人に通訳したんだよ～！"

show misha hips_smile
with charachange



mi "しっちゃんはずーっと、『効率悪い～！　ミーシャ～！　どうしてあなたが通訳なんかしなきゃいけないの？　つまり～、そもそもなんで通訳が必要なの？　え～？』"
mi "『わたしが料理してあなたが注文取ればいいじゃないの！　意味わかんない！』って言ってたんだよ"


show misha sign_smile
with charachange


mi "でも～！　最後はみんな楽しんでたと思うんだ。そうでしょ、しっちゃん～？"

show shizu behind_frustrated_close
with charachange


shi "…… …… ……"



"いやいやながらといった様子で静音は眼鏡を直す。それを見てミーシャが急に笑い出す。"


show misha hips_grin
with charachange


mi "前の生徒会の案だったんだよ～！　だからだよ～！"


hi "じゃあ、前の生徒会ってどんなだったんだ？"


"静音がついに再び介入を決断する。というか、口を出さずにはいられないみたいだ。"

show shizu basic_angry_close
with charachange


ssh "ひどかった"


"単刀直入だな。判決を下すかのように、手で空を切る仕草で言葉を締める。もう少し詳しく説明してくれるといいけど。"

show shizu adjust_angry_close
with charachange


shi "……"

show misha sign_confused
with charachange



mi "大学とか一部の私立高校だと、生徒会には何百万円も予算があって、必要に応じて配布できるの"
mi "わーお！　ほんとに？　何百万も？　あー、そうだね～！　しかも生徒会は学校の活動にずっといっぱい関わってるんだよ、ひっちゃん！"




"その口調からすると、それは俺よりもまず、ミーシャにとって初耳だったみたいだ。"



show misha hips_frown
with charachange


mi "それに比べれば、この学校の生徒会は冗談みたいなものだったの～！　まったく力のない人に権力のある地位を与えたらだめ！　そんなことして何の意味があるの～？"

show shizu behind_blank_close
with charachange


ssh "それで……"

show misha sign_smile
with charachange



mi "……わたしは自分たちの仕事をもっと増やしたかったの～！　それを認めるよう学校やほかの生徒会メンバーを説得するのは大変だった"
mi "実は～、ひっちゃんが見たようなわたしたちの仕事はわたしが引き受けたものなの。リリーが話していたのはそういうこと"


show misha hips_grin
with charachange


mi "しっちゃんがいなかったら、生徒会は来る日も来る日も出席簿を整理するだけだったんだよ～！"

show misha cross_laugh
with charachange


mi "ははは～！　そんなのがいいと思う、ひっちゃん？"

show misha sign_smile
with charachange


mi "もちろん、ひっちゃん、仕事の量が増え始めたとたんに、生徒会のメンバーはほとんどが顔を出さなくなったの"

show misha hips_laugh
with charachange


mi "わははは～！"

show shizu basic_normal2_close
show misha hips_smile
with charachange


shi "……"


"静音の指が注意深く重なり合う。一言付け加えたいのに、そうする気分になれないかのようだ。"


"静音が言ったように、手話では自分が『話す』ことについて考える時間が少しだけ増える。このことについては話せない、と思っているんだろう。"

show shizu behind_blank_close
with charachange


ssh "昔は昔、今は今。いいから明日は楽しみましょう"


"結局、静音が言葉にしたのはそれだけだ。"


hi "そうだな"

show shizu adjust_happy_close
with charachange


shi "……"

show misha perky_smile
with charachange

stop music fadeout 5.0



mi "おっけ～！　じゃあ、今日の生徒会はへ――い――かい？　だね～！"


show misha hips_grin
with charachange


mi "元気よく閉会しないとね。今日はいい日だったから"

show misha cross_laugh
with charachange


mi "あははは～！"

scene bg school_road_ss
with shorttimeskip


"店を出る頃には、学校は終わっていたようだ。俺たちが坂を上っていると、学校から下に降りてくる生徒たちが見える。"


"学校の制服を着た人たちが、何人かすれ違いざまに静音を見る。彼らは静音のことを生徒会長として認識しているのか、それともミーシャの頭に目を引かれているだけなのだろうか。"



"あたりの会話がいやでも耳に入ってくる。話題の多くは七夕の予定だ。そのうちの何人が、俺の組み立てなおした屋台で露店を開いたり、それとも立ち寄るのかな。"




"ちょっと誇らしい気分になる。学校のために何かをしてこんな気分になったことはなかった。"


"静音もこういう気持ちなのかもしれない。聞いてみたいという気になるけど、そんなことを考えるのはバカみたいなものだろう。"

scene bg school_courtyard_ss
with locationskip


"なので、それは思いとどまって、三人で学校に戻ってから別れる。静音は生徒会室へ、ミーシャと俺は寮の部屋へ。"


"二人の姿が見えなくなるまで、明日の待ち合わせをどうするか、また聞き損ねたことに気づかなかった。"

$ suppress_window_after_timeskip = True

scene black
with dissolve


label jp_S16:

window hide None

scene black
with dissolve

scene bg school_dormhisao
with openeye

window show


"今日は休日だというのに、普段と同じ時間に目が覚める。ほかのみんなはあと６時間はぐっすり寝込んでいるだろう。"

play music music_pearly fadein 3.0


"数日ぶりに朝の服用分の薬を飲む。正直、薬のことは頭からすっぽり抜けていた。目の前にずらりと並ぶ薬の容器を見ていると、どうして忘れてしまったのか見当もつかない。"


"１７種類の薬。全部飲み終わると、もう朝食を抜いてもいいくらい腹が一杯になる。"


"もう起きてしまったので、散歩にでも出かけるか。"

scene bg school_dormext_full
with locationskip


"外はいい天気みたいで、よく夢に見たのどかな雰囲気が伝わってくる。"


"田舎の地をあてもなく歩いて、新鮮な空気を味わえたらな、なんて非現実的な空想を以前からしていたものだった。"


"それを実践するチャンスが目に前にある以上、じっとしてはいられない。バカみたいに見えるだろうとわかってはいるけど。"

scene bg school_courtyard
with locationchange


"本校舎に寄り道して飲み物を買ったあと、中に入って屋上で少しぶらぶらしていくことにする。"


"この時間なら結構いい眺めが見られるかもしれないし、俺以外に誰もいないのは確実だ。それに一人きりで屋上に上がったことは一度もない。"

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

scene bg school_staircase1
with locationchange


"今日の学校は静かだ。人っ子一人いない。屋上への階段にこだまする自分の足音がぞっとするほど大きい。"


"ほぼ完全に無音の手話クラスに延々時間を費やしたのと、このところ静音と長い間一緒にいたことを考えれば、この状況は別にどうってことはないはずだけど、でもやっぱり落ち着かない。"



"以前なら気にも留めなかったちょっとした音も轟音のように感じる。いけない場所に忍び込んでいる気分だ。どうしてこんな感覚になるのかわからない。もしかしたらこの学校、幽霊にとりつかれていたりするのかも。"


play sound sfx_door_creak
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
stop music fadeout 3.0

scene bg school_roof at left
with locationchange


"屋上のドアを開けると、俺は一人じゃなかった。ミーシャがフェンスにもたれながら校庭を眺めている。俺にはまったく気づいていない。"


"その瞬間に、とるべき行動が頭に浮かぶ。手で目隠しをして『誰だ？』って言ってやるんだ。それしかない。"


"途中まで近寄りながら、サンドイッチを買いに行ったばかりの静音が突然戻ってきて、俺がこうやってミーシャに忍び寄っているのを見られたらどんなに格好悪いだろうか、などと考え始める。"


"そんな偶然の誤解が起きないことを無言で祈る。"

show bg school_roof at right
with charamove


hi "誰だ？"


mi "ひっちゃん！"


"一瞬もためらわずに言う。いつもの声の調子から少しもはずれていない。俺のお楽しみは始まる前から終わっていた。"

play music music_soothing fadein 1.0

show misha hips_grin_close at Slide(0.6, 0.5, 0.5, 0.5, 0.5)
with charaenter


mi "こんちは、ひっちゃん！　おっはよ～！"

show misha sign_confused_close at center
with charachange



"反射的に挨拶をしようとしたミーシャの手が、そのままフェンスに引っかかってしまう。"



hi "おはよう。こんなとこにいるとは思わなかったぞ。朝っぱらから何してるんだ？"

show misha perky_smile_close
with charachange


mi "こっちが聞きたいよ、ひっちゃん！　こんな朝早くに何してるの？　ここで会うなんて思わなかったよ～！"


hi "先に聞いたのはこっちだぞ"

show misha hips_grin_close
with charachange


mi "ん～……それもそうだね。わはは～！"

show misha sign_smile_close
with charachange


mi "今の、しっちゃんみたいな言い方だね"


hi "そんなわけあるか"


"……と、まったく説得力のない口調で言う。幸い、俺のへたくそな芝居にはミーシャは気づかない。"


hi "今晩のこと、楽しみにしてる？"

show misha hips_smile_close
with charachange



mi "当たり前だよ、ひっちゃん！　お祭りとかは好きじゃないけど、というかしっちゃんほどにはだけど、でも七夕の屋台はいっつも面白いものや季節の食べ物が一杯買えるんだよ。それに～！　浴衣も着られるし！"



"おかしな言い方だな。お祭りは好きじゃないけど、それにまつわることはみんな好き、と言っているように聞こえる。でも追及するほどのこととも思えないし、俺が誤解しただけかもしれない。"

show misha perky_smile_close
with charachange


mi "ひっちゃんはどうなの～？"


hi "俺だって楽しみだよ。でなきゃ自分ちに引きこもってるだろ？　それが理屈ってもんだ"

show misha hips_grin_close
with charachange



mi "あはは～！　ひっちゃんはそんなに理屈っぽい人じゃないよ～！　だから～！　それってとってもびっくり！"

mi "うん、でもわかったよ。確認したかっただけなの。学園祭の時はあんまり楽しくなさそうだったから。それでわたしもしっちゃんもちょっと心配してたんだよ"






hi "おいおい、俺だって楽しんでたぞ。思ってたより面白かったくらいさ"



show misha perky_smile_close
with charachange


mi "ほんと、ひっちゃん～？　わははは～！　どのへんが面白かったの？　教えて～！"


hi "そうだな、最後の花火。あれは……すごくよかった"


hi "お前は眠り込んでたみたいだけどな"

show misha hips_smile_close
with charachange


mi "え～……わたし、いつも早寝しちゃうから。でも～！　今年は眠ったりしないよ！　絶対最後まで起きてるから！"


hi "七夕には花火はないと思うけどな。雰囲気が全然違うし"





hi "花火をやってほしいって嘆願書を静音に出してもらうよう頼めばいいんじゃないか。それと花火の時間を早めにしてもらえば"

show misha cross_laugh_close
with charachange


mi "はははははは～！　それもありだね～！　すごくいいアイディアだよ、ひっちゃん！"


hi "えっ、いやいやいや違うだろ！　やめろって。冗談だよ"



hi "でも……しっちゃ――静音は怒るかもしれないけどな"


show misha hips_grin_close
with charachange


mi "わはは～。でもひっちゃんはそうしたいって感じに聞こえるよ"

show misha cross_smile_close
with charachange


mi "ひっちゃん～！　しっちゃんのこと、好きなの？"



"イエスともノーとも言えない。しかも座っているのでさりげなく立ち去ることもできない。"


hi "バカなこと言うなよ。俺が好きなのはお前だよ"

show misha perky_smile_close
with charachange



mi "あははは～！　ほんと、ひっちゃん？　ん～！　違うな、今の冗談だよね？　しっちゃんの方がもっと好きに決まってるよ"



hi "ミーシャ、お前早合点しすぎだろ"

show misha sign_smile_close
with charachange


mi "でもしっちゃんって言いそうになったじゃん！　だから～！　わたしは合ってるの。でしょ～？"



hi "お前がいっつも静音のことをしっちゃんって言ってるからだよ。こっちの頭の中から離れないんだ。言葉が移るってのはよくあることなんだぞ。それにたった一回言い間違えただけだし"

hi "お前の理屈だと、お前の方が俺より静音のことを好きじゃなきゃおかしいだろ。それと……お前からかってるのか？"




show misha cross_laugh_close
with charachange


mi "わはは～！"

show misha perky_smile_close
with charachange


mi "そうかもね～"

show misha hips_smile_close
with charachange


mi "おなか減っちゃった。朝ごはん食べた、ひっちゃん？"


hi "いや。薬だけ"

show misha sign_confused_close
with charachange


mi "ふむう……"


"考えている間も手を遊ばせないように、けだるそうに指をくるくると回している。"

show misha hips_grin_close
with charachange


mi "じゃあ何か食べようよ～！　今日は学食の朝ごはん、あるかなあ？"


"そういうことは生徒会のメンバーなら知らなきゃいけないことだと思う。でも俺の口からは言えない。俺だってメンバーだけど知らないし。"


hi "俺が校舎に入ったときは、厨房で働いてる人は誰もいなさそうだったぞ。はっきりとはわからないけど"

show misha perky_smile_close
with charachange


mi "ねえひっちゃん、食べ物が買える自動販売機って聞いたことある？　バーガーとかスープとか、それにピザも！　そういうのがうちの学校にもあったらすごいと思わない～？"


hi "どうだろうな。ああいう自販機って変な感じだなっていつも思ってたから"

show misha hips_smile_close
with charachange


mi "そういう自販機があったらどんなにいいか考えてみてよ、ひっちゃん～！　ほとんど魔法みたいだよ、そうじゃない？"


mi "自動販売機からあったかい食べ物が出てくるなんて、ほんとにすごいよ。わたしなら想像もできないよ。そういう自販機に出会えたら、もう夢みたいだよ！"

show misha perky_sad_close
with charachange



mi "ん～……でも、そんな機械はこの町のどこにもないんだよ～。まだ町に出るのだって早すぎるよ～！　これじゃ朝ごはん食べられないよ、ひっちゃん、一日で一番大事な食事なのに。みんなそう言ってるよ～！"
mi "あー、ごはん食べたーい！ "



hi "ほんとにばかだな。そんなに腹減ってるなら、俺がソーダおごってやるよ"

show misha hips_frown_close
with charachange



"ミーシャは頬を膨らませて、真剣そうな顔をする。"



mi "ひっちゃん、ソーダは朝ごはんじゃないよ。水みたいなものじゃん～"



hi "水みたいじゃない、液体だ。水は食べ物じゃない。液体は食べ物にはなる"




"『そっちこそ静音みたいな言い方じゃないか、ミーシャ？』そう言ってやりたい。その口調さえ、平然とした事務的な態度でとんでもないことを言う静音を彷彿とさせる。"





"でも俺がそう言ったら、今度は俺がまた静音みたいな口のきき方になってしまう。ひどい話だ、あいつの負けず嫌いが本当に移ってしまっている。"




hi "じゃあ何か食い物でも探すか"

show misha cross_frown_close
with charachange


mi "……"

show misha cross_laugh_close
with charachange


mi "おっけー。あはははは～！"

stop music fadeout 3.0
stop ambient fadeout 1.0

scene bg school_lobby
with locationskip


"予想はできていたけど、こんなに早い時間に無人の校舎で食べ物を探す努力は無駄にしかならなかった。"


"捜索をいったん断念した後、朝食をとると誓ったミーシャは一人で探し続ける決断をする。でももうブランチといってもいい時間だけど。"

scene bg school_dormhisao
with locationskip


"俺は寮の部屋に戻る。続く時間はゆっくりと流れ、俺はたまった本を読んで暇をつぶす。"

show bg school_dormhisao_ni as overlay at Alphain(6.0), center
with None

play music music_dreamy fadein 6.0


"いくつかの本は、入院中に読んで以来手も触れていなかったものだ。振り返ってみると、そんなに昔のことでもない。気持ちの上では間違いなくそう感じられるのに。"


"暇な一日、そしてやることが何も思いつかない。少し昼寝をして、今日二度目の着替えを済ませながら、結局静音やミーシャと待ち合わせの場所や時間を全然確認していなかったことに気づく。"


"いずれ向こうから探しに来るだろうとは思うけど、でもそこまでいくと非常にばつが悪い。"

scene bg school_dormhisao_ni
with None


"もう夕方だし、少なくとも先に二人を探す努力はすべきだろう。"

scene bg school_courtyard_ni
with locationskip


"まだ学校内はそれほど人は多くないし、仮に混んでいてもミーシャのピンクの髪を見逃すことなんてあり得ないけど、それでも二人を見つけるのは大変だった。"

scene bg school_gate_ni
with locationchange


"最初に見に行った正門で、ようやく二人にはち合わせる。"

show shizuyu basic_happy_ni at center
with charaenter


ssh "こんにちは！"


"いつもどおりの挨拶を、最後にもったいぶったように手をさっと振って強調しようとする。"

show shizuyu basic_happy_ni at tworight
show bg school_gate_ni at bgright
with charamove

show misha sign_smile_yuk_ni at twoleft
with charaenter


mi "ひっちゃん～！　気分はどう？"


"今夜は浴衣姿の人をたくさん目にしているのに、浴衣姿の二人を見るのは奇妙な感じがする。"



"静音の浴衣はシンプルで上品だ。後から考えれば、わかりきっていたことだけど。普段は大げさな身振りや無茶な態度をとるけど、でも派手に着飾るくらいなら死ぬ方を選ぶと思う。"






"身につけているヘアピンが目にとまる。月明かりを受けて柔らかく輝く真珠の花だ。"



"よく似合っているけど、ある意味では場違いな感じもする。女子高生には、というか、密かに子供っぽいところのある静音みたいな奴にはちょっと精巧すぎるように見える。"





"ミーシャの浴衣はだいたい予想通りで、なんだか似合いすぎている。風船ガムのようなピンクの髪と合わさって、かわいく見えるけど時代錯誤な感じだ。"



hi "二人ともきれいだな"

show misha perky_smile_yuk_ni
with charachange


mi "ありがと、ひっちゃん～！"

show shizuyu cross_angry_ni
with charachange


shi "……"


mi "ひっちゃん、ちょっと遅かったね。しばらく待っててあげたんだけど、時間とか場所は忘れちゃったの？"


mi "まあいっか～！　じゃあいこ、ひっちゃん～！"

show shizuyu cross_happy_ni
with charachange


shi "……"


"ミーシャが話を切り上げてくれたので、実は一時間も前から二人を探していたという、白状してしまったら非常に恥ずかしい羽目になる事態を逃れることができた。"


"こんなに上機嫌な静音とミーシャを見ていると、雰囲気に身を任せて夜を楽しみたいという気分に逆らえなくなる。"



"厄介なことに、今夜は静音の手話が読み取りにくい。一週間くらい手話のクラスに出ていなかったので、無理もないけど。ちょっと集中力をなくしていたんだろう。記憶が薄れている。今回だけではすまないだろうな。"



hi "ちょっと待てよ、どこに行くんだ？　町に出るのか？"

show shizuyu basic_happy_ni
with charachange


ssh "そうよ"


hi "わけわかんねえぞ。学校の中の出し物だってひとつもチェックしてないじゃないか。二人とも俺がいない間に楽しんでたっていうなら話は別だけどさ"

show shizuyu cross_happy_ni
with charachange


ssh "また戻ってくるわ。下から上がってくるのよ"

show misha sign_smile_yuk_ni
with charachange


mi "ははは～！　どっちにしてもね、ひっちゃん、お祭りを全部見たければ町に降りてから戻ってくるしかないの。だから～！　こうすれば、全部終わってくたびれた後は寮の目の前に戻ってくるわけ。完璧だね～！"

show shizuyu basic_happy_close_ni at closeright
with characlose

stop music fadeout 2.0



"確かに理屈には合ってるな。どのみち静音はあまり反論する時間を与えてくれず、俺の腕をつかんでそっと引っ張り出そうとする。"



scene ev shizutanabata:
    truecenter zoom 8.0 rotate 45.0 subpixel True
    easein 1.0 zoom 1.1 rotate 0.0
    easein 8.0 zoom 1.0
with locationskip

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 2.0
play music music_ease



"月明かりと薄い紙で彩られ、低く掲げられた提灯だけが町並みを照らしている。その光景を見ると穏やかな気分になる。"





"町に着くと、あたりの様子をよく見ようと静音が歩みをゆるめる。"


"なので、ちょっかいを出そうとしてわざと早く歩いてみる。でも静音はすぐにスピードを合わせてきて、声のない笑い声を上げながら、空いている方の手でミーシャに手話を見せる。"


shi "……"


mi "まずはなにしよっか、ひっちゃん～？"


hi "あるんだったら、ゲームでもやろうか？"


mi "ゲームは嫌いなんじゃなかったっけ、ひっちゃん"


hi "別にいいよ"



"静音の細い指が俺の指に絡み合う。これで今日二度目だ。今の今までずっと、俺は静音の意志に引きずられてきたような気がする。時にはとても気疲れするけど、でもだいたいは悪くなかったんじゃないかと思う。"




"まるで嵐のように、自分の生き方に他の人を巻き込んでしまえるという性格でしかないんだろう。時にはその言葉が静音に合っているようにも思う。今朝ミーシャに言いたくなかったけど、俺は確かに静音が好きだ。"




mi "ひっちゃん、今度はわたしにも人形ゲットしてくれるんだよね、ね～？"



hi "まだそのこと考えてるのか？　わかったよ、取ってやる"

$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

scene bg suburb_tanabata_ni at bgright
show nightwash
with shorttimeskip



"たわいないことをできるだけいっぱいこなそうとあちこち回っているうちに、時間は思っていたよりも早く過ぎていく。"


show misha perky_smile_yuk at center behind nightwash
with charaenter


mi "スノーコーンだよ！　ひっちゃん、一つ食べる～？"


"俺の答えを待つまでもなく、ミーシャは屋台に駆け寄る。"

show misha perky_smile_yuk at twoleft
show bg suburb_tanabata_ni at center
with charamove

show shizuyu cross_happy_close at closeright behind nightwash
with charachange


ssh "おいしそうね、私も欲しい。誰が代金を払うか、じゃんけんで決めましょう"


hi "もしくは……割り勘でいいんじゃないか"

show misha sign_smile_yuk
with charachange


mi "ひっちゃん～、何味がいい？"


hi "青いやつ"

show shizuyu basic_angry_close
with charachange


ssh "青は味じゃないわ"


hi "わかってるよ……"


ssh "色でものを頼むなんて子供みたい"



hi "そっちがガキっぽいんだよ。お前は何頼むんだ？　イチゴ？　はは！　それこそガキっぽい味じゃないか。イチゴなんて子供しか食べないんだぞ"


show shizuyu cross_angry_close
with charachange


ssh "プレーンを頼みなさいよ。一番大人の味！"


"こういう性格がどこから出てくるのか知りたい。俺の登校初日に最初に話をしたのが静音じゃなかったら、果たしてそんな考えが出てきただろうか。"


"もしそうなっていたら、いつも俺を引きつけ続ける静音の特徴を見逃していたに違いないと思う。"


"俺の言葉が聞こえないこと、負けず嫌いなこと、俺を生徒会に引き入れることにあんなに必死なこと、お茶目さと鋭さが入り交じること、それを知らなかったとしたら……"


"静音はいつも新しい側面を見せて、俺の興味を引き続ける。それがなかったら、俺は彼女を好きになっていただろうか。"


"考えすぎだろうな。"


hi "何か願い事はしないのか？"

show misha perky_confused_yuk
with charachange


mi "しっちゃんは願い事なんてしないんだよ、ひっちゃん！"


hi "ほんとか？　新年の時も？　どうして？"

show shizuyu basic_happy_close
with charachange


shi "……"


"静音は指を重ねて笑みを浮かべるけど、答えない。"


ssh "秘密"

show misha sign_smile_yuk
with charachange


mi "知ってるよ～！"


mi "ひっちゃん、教えてほしい？"

show shizuyu cross_blush_close
with charachange


shi "……！"


hi "ぜひ聞きたい"

show shizuyu basic_angry_close
with charachange



"静音は思いつく限りの力強い『ノー』の表現を次々と繰り出す。"


show misha perky_smile_yuk
with charachange


mi "わはは～！　じゃあ後で教えてあげる。おっけ～？"

show misha perky_sad_yuk
with charachange

stop music fadeout 5.0


mi "なんだか疲れちゃった。今日は早めにお休みするかも～"

show shizuyu cross_blush_close
with charachange


ssh "ほんとに？"



hi "そんなに時間がたった気もしないけどな"



"楽しんでいるときは時間が早く感じるな。"

show misha sign_smile_yuk
with charachange


mi "でも～！　もう経っちゃってるんだよ、ひっちゃん。先に優子さんのとこ行って、それで帰るかも？　それとも～……わかんないな～"

show misha perky_smile_yuk
with charachange


mi "まあ、いいや。わたし抜きで楽しんでね、い～い？"


hi "どうせもうすぐ学校に戻るんだぜ、ミーシャ"

hide misha
with charaexit

show shizuyu cross_blush_close at center
show bg suburb_tanabata_ni at bgleft
with charamove


"ミーシャは聞きたくなかったようで、そのまま立ち去ってしまう。静音も俺と同じように怪訝そうだ。俺はその疑問を口にしなかったけど、静音は理由を話し合いたいかのように手話をし始める。"

scene bg suburb_tanabata_ni at bgleft
show nightwash
with shorttimeskip


"見るものを全部見て回ったあと、時間を確かめると、もうずいぶん遅くなっていることに気づく。俺の体力も底をつき始めている。ここまで持ったこと自体が奇跡的だ。"


"静音も少し疲れているように見える。俺たちは学校への帰り道をたどる。"

stop ambient fadeout 0.5

scene bg school_courtyard_ni
with locationskip

play ambient sfx_cicadas fadein 0.5


"明かりがついていて、生徒で一杯の校舎を目にして、静音はがっかりしているようだ。"


his "どうかしたのか？"

show shizuyu basic_aside_ni at center
with charaenter


ssh "屋上に行きたかったけど、これじゃ人が多すぎる。私も疲れているし、これで良かったのかも"


his "屋上はカップルばかりだろうな。今日は休日みたいなものだし"


his "でもそうでもないかもな。実際、そういうもんなのか？　ここに来る前はお祭りなんて一度も行ったことがないからさ"


shi "……"



his "がっかりしたぞ。学校のお祭りを最後に見てみたいって言ったのはそっちじゃないか。一番いいのは最後に取っておくって"
his "それで今度はもう行きたくないって言うのか？　全然？　お前はもっとエネルギーがあると思ってた。俺は疲れてなんかいないぞ"


show shizuyu basic_happy_ni
with charachange


"今のが負けん気に火をつけたらしく、静音はすぐに頭を上げる。でも言っては見たものの、どこへ連れて行く当てもなかったことに気づく。それに俺自身も本校舎に行く気にはならない。"

scene bg school_gardens_ni at Fullpan(4.0, dir="right")
with locationchange



"幸い校舎の裏は人気もなく、今夜は眺めが良さそうだ。夜中に見るまで、その広さと行き届いた手入れぶりにちゃんと目を向けていなかった。月明かりに照らされて、校庭は果てしなく広がっているように見える。"


show shizuyu basic_happy_ni at center
show bg school_gardens_ni at right
with charaenter


ssh "ただの校庭なのに、とてもきれいね"


"さっきまで、静音は今夜の浴衣みたいな古風な服を着こなすには若すぎると思っていた。でも今は、静音の浴衣姿がとても美しいと思う。"




"その姿が、前の学園祭を一緒に見て回ったときの日のことを思い起こさせる。その時も静音は同じように見えた。"

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_serene fadein 1.0

window hide

nvl clear

nvl show dissolve


n "\nお前のことが好きだ、と伝えたい。はっきりと、一息に。でもこんなことを考えるだけでも、とんでもなく気まずい気分になってくる。"


n "それに静音のことを好きになればなるほど、自分の気持ちを伝えるのが決まり悪く、怖くなってくる。今だってそうだ。今なら別の人を介さなくても伝えられるというのに。"


n "それどころか、前と同じことが今度も起きたらどうする？　もしそうなったら、何ヶ月もの入院生活くらいでは済まないかもしれない。そんなの考えたくもない。"


n "どうにかしてそんな考えを頭から追い出そうとする。心配のしすぎだと思おうとする。"


n "それでも……"


n "あれだけの量の薬を初めて見たとき、それが滝のように俺の前に流れ落ちる様子を想像してしまった。自分が埋もれてしまうくらい、大量に。"



n "今でも時々そのことを考える。当然の懸念とは言えない。でもこういう素晴らしい瞬間には、そんな記憶も忘れられる。"




nvl clear
nvl hide dissolve

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene ev shizuconfess_normal
with flash

window show


ssh "この学校の好きなところは、山のてっぺんにあるってこと"


his "それだけ空に近いからか？"


ssh "そう"


his "俺も学校は好きだけど、どっちかというと空気がきれいなのがいいな"


his "お前はほんと負けず嫌いだよな。負けず嫌いすぎる。お前、鯨に噛まれたら噛み返すだろ"

scene ev shizuconfess_smile
with charachange


shi "……"


"それを聞いて静音は笑い、ウィンクする。"


ssh "それ、そんなに悪いこと？"


"こいつの笑顔は伝染する。"


his "ああ"


shi "……"

scene ev shizuconfess_closed
with charachange


ssh "確かにね。私はひどい子だわ。ちょっとだけ"

scene ev shizuconfess_smile
with locationchange



ssh "でも人を楽しい気持ちにさせることができるなら、まるっきりひどいってわけでもない、そうでしょ？　だったら、それでいいの。実例だっていくらでもあるんだから"





"この瞬間でさえ、静音にとっては勝ち負けのゲームなのかもしれない。"


his "その通りだな"

stop music fadeout 2.0


"ロマンチックな瞬間だ。こんなチャンスは二度と来ないかもしれない。そう思うと、ばつが悪くてバカみたいなことを言わないといけない気になってくる。考えすぎていたら、手が言うことを聞かないだろう。"


his "俺の彼女になってくれるか？"


scene bg school_gardens_ni at right
show shizuyu cross_blush_ni
with locationchange


shi "……"


"今の手話、間違えてなければいいけど。"



"緊張して、逃げ出したくなってくる。でも根を張ったように一歩も動けない。たった一分前まで物音一つ聞こえなかったのに、今は周りの音が全部聞こえてくる。本当に緊張している。顔に出てるだろうか。"



"さっきまでは一時間が一秒で過ぎていった。今は一秒一秒が永遠のように感じられる。"

show shizuyu basic_blush_ni
with charachange


"すると、静音の手が不規則に動いているのが見える。まごつくように手を重ね、一つ一つの仕草のたびに動きが止まる。"


"静音が前に言ったように、手話は話す前に自分の言葉を考える時間がある。今の静音は必死に言うべきことを考えているんだ。"



"何と答えればいいのか分からない状況。静音には思いもよらないことに違いない。"

"どんなに冷静でいようとしても、赤らむ頬は隠せない。こうしている静音はとてもかわいくて女の子らしい。俺と同じくらい緊張しているんだと知って、安心する。"





"その思いも、ある意味で俺が静音と競争していることの表れなんだと気づく。"


show shizuyu cross_happy_ni
with charachange


ssh "うん"



play music music_romance fadein 1.0

show shizuyu basic_happy_close_ni
with characlose


"シンプルな答えだ。でもそう思った途端に、静音は歩み寄って俺を抱きしめてくる。"

stop ambient fadeout 3.0

window hide

nvl clear

nvl show dissolve


n "\n\n\n\n\n\n\n\n\n俺が卵の殻でできているかのような、そして他人を抱きしめる方法を知らないかのような、不安げで注意深い抱擁だった。でも正直言うと、俺だってそんなに詳しいわけじゃない。"


n "指に触れる浴衣はひんやりとしていて、なめらかに感じられた。でも静音のぬくもりも伝わってくる。"


n "結局、これが自分の気持ちを伝える一番いい仕草だと思ったのだろう。"

stop music fadeout 3.0

nvl hide dissolve
return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
