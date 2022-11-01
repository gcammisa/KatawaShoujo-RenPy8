label jp_A38:


window hide None

scene black
with dissolve

scene bg school_dormhisao
with openeye

play music music_daily fadein 4.0

window show


"翌日。頭がくらくらするのを感じながら目を覚ます。もう正午近い。"

$ renpy.music.set_volume(1.0,0.0, "ambient")

"朝寝坊しても問題はない。今日は日曜で授業はないのだから。"


"とはいえ今日は、ただの日曜じゃなくて学園祭の日でもある。"


"窓の外には、もうそばの屋台に人がいるのが見える。ジャンクフードに目がない人たちのために、麺をお皿に乱暴に盛りつけている。"


"一握り分の朝の薬を一気に飲みこみ、今日一日どう過ごそうかと考える。"


"来週には試験があるけど、みんなが言うほど忌々しくは思わない。多分、本当はもっと心配してなきゃいけないんだろうな。"


"まあすぐに勉強しないといけないわけでもないし、この学園祭の日にどう過ごしたって自由なはずだ。"

scene bg school_dormhallway
with locationchange


"朝の雑用を済ませ、廊下へと出る。外で何か食べるものを探そう。"


"健二の部屋の前を通りすぎようとした時ふと思いつき、あいつが今日どうするのか聞いてみることにする。"


"あいつに予定があるのか気になる。みんな何かしらやってるし。"


"と言いながらも、自室に防音シェルターなんかを作り終えているあいつの姿もありありと想像できる。"


"あるいは要塞みたいなものとか。もちろん『女子立ち入り禁止』と掲げてあるやつ。"


"……そして『女子』が横線で消され、その下に『何人たりとも』と乱暴に書き直されてるんだ。"

stop music fadeout 2.0

play sound sfx_doorknock2


"健二の部屋のドアを叩く。幸い、何の注意書きも掲げられてはいなかった。"
"また落ち着かないカチャカチャという鍵の音が聞こえてくる──少なくとも１０個はあるようだ。ドアがバタンと開く。"

show kenji neutral at Slide(0.0,0.3,0.0,0.2,0.5)
with Dissolve(.5)


ke "誰だ？"


hi "それは開ける前に聞くもんだろ"

show kenji neutral at center
show bg school_dormhallway at bgright
with charamove

play music music_kenji fadein 1.0


ke "ああ、久夫か。くそ、朝早いな"


hi "いや特に早くないと思うけど"

show kenji happy
with charachange


ke "なんの用だ？"


hi "特に。ただ今日どうするのか聞きたくて"


hi "もう生徒はみんな外に出てるぞ"

show kenji rage
with charachange


ke "外のどこだよ？　どうして？"


hi "……なに？"


ke "なにってなんだ？　今日って特別な日か？　なんでそんな所に。どんなやつらが？"

show kenji tsun
with charachange


ke "いや、聞こえるぞ。騒がしいな……まさか……侵略が始まったっていうのか？"


"急に心配そうな顔をする健二。"

show kenji neutral
with charachange


ke "今日って何曜日だ？"


hi "ああ、お前にはあのでかい屋台の列も見えないんだろうな……売ってる人間も……"


ke "いったい何の話だよ？　俺はスナイパー避けに、いつもカーテン閉めてるんだよ"


hi "あー、学園祭だよ。知ってる……よな？"

show kenji tsun
with charachange


ke "ああくそ、今日だったのか？　あー、くっそ。ああ……ちくしょう"


ke "忘れてたなんて信じられねえ、まだ要塞も完成してないのに。これはまずいぞ"


ke "今日は本当にひどい日になるぞ。お前、教えてくれてよかったぜ。今日は悪い日になる"


hi "なぜ？"

show kenji neutral
with charachange


ke "おいおい、あいつらがあちこち歩き回るんだぞ。あいつらだよ。窓の外の。リア充してるやつら！"


"健二はこめかみをイラついたようにこする。急に顔色が悪くなった。"

show kenji tsun
with charachange


ke "ものすごく騒がしくなるぞ。くそ、今日は外に行くつもりだったのに、もう台無しだ。何もかも台無しだ"


ke "こんなのってあるかよ。ひでえ、ひどすぎる！"


ke "なんだこれ。本当にひどすぎるぞ。もうどこにも行けないじゃねえか。どこにも逃げられない"


"気が立ってるようだ。気が狂ってると言ってもいいかも知れない。"

show kenji neutral
with charachange


ke "信じられない。今日がこの日だったのか"


ke "くそ、それなのに準備もできなかった"

show kenji tsun
with charachange


ke "何の準備もできなくて、こんな事になっちまって、俺にはどうしようもないんだ。お前がもっと早く言ってくれれば良かったんだ"
ke "というか、まあ、知ってるけど……もっと早くに気づくことだってできたはずだろ！　そしたらどれだけ準備できたか、考えてみろよ……"


hi "悪いな。知ってると思ってた"


hi "つまり、お前今日は特に予定ないんだな？"


hi "天気は良いしさ。昨日は風が強かったから今日は寒くなるかと思ってたけど、そんなこともなかったし、部屋にこもってる理由なんてないだろ。お前も学園祭見に行くといい"


"健二は唸って顔を手で覆う。"


ke "んな、無理、無理！　そんなことできるか。外のあいつらに踊り食いにされちまう。わかるんだ"


"こんなの冗談に決まってる。しかし奴はまじめな顔で言っていた。割とまじめだ。"

show kenji happy
with charachange


ke "お前こそ今日は予定あるのか？　一緒にここにいようぜ、俺の要塞建設を手伝ってくれよ。一緒にやれば、まだ間に合うかもしれない"

label jp_A38a:



hi "生徒会のやつらに付き合わないといけないんだ。賭けに負けちゃってさ"



"そういえば、いつどこで待ち合わせるか決めていなかった。外の混雑で行き違いになりそうなので、ここであいつらを待つことにする。どうせ二人とも、運営であちこち走り回って忙しいだろうし。"


"不思議なもんだ。あんな馬鹿げた勝負で静音に負けた代償はずっと高くつくと思ったのに。これは俺が静音と一緒に過ごすための口実でしかないんだ。だとしたら、あいつは俺に楽しんで欲しいだけなんだろうな。"


"静音は言葉を発して気持ちをはっきり伝えることはできないけど、どちらにしてもその気持ちは善意のものなのかもしれない。俺は静音を好きになり始めてるな、と思う。"


hi "すっぽかすこともできるけど、そんなのもったいないだろ。それに俺だって行きたいんだ。なんだ、ほら、今日ってかなり楽しそうじゃん。行けば面白いことになりそうだし"

show kenji tsun
with charachange

stop music fadeout 1.0


ke "生徒会？　はあ？　そんなのまだ存在してたのか"


ke "それってあれだろ、野郎二人だけなんだろ？"


hi "二人とも女の子だけど"

play music music_tension

show kenji rage
with charachange


ke "マジで？　かわいいか？　くそ、そんな、待てよおい……かわいいのか？"


ke "いや！　やっぱりそんなのどうでもいい！　生徒会長は狂ってると聞いたことがある……誰だか知らないけど、絶対に口をきかなくて、いつもパシリを使って命令を伝えるってな"

show kenji tsun
with charachange


ke "ちっ、どの学校でも同じだな……冷血なクソアマか。どこもクソアマだらけだ"


ke "そいつらが女子二人だとしたら、お前は２対１で数の上では負けてるわけだ。お前、危険な状況だぞ。何が起きるか、わかったもんじゃない"


ke "ちっ、生徒会め、女二人だけなのになんて権力を持ってやがる"


ke "奴らを止めないといけない"


ke "わかるんだ、生徒会はフェミニストの陰謀を推進するべく何かたくらんでる。そんな団体信用できないね"


ke "これはよくない。よくないぞ！"

show kenji rage
with charachange


ke "くそ。最悪だ！くそ！"



label jp_A38b:



hi "わからない。かなり腹減ってるからまず何か食べようと思ってた。それから学園祭の様子を見に行こうかと"


hi "お前のクラスの出し物もすごそうじゃないか。俺も自分が手伝ったやつぐらいは見ておきたいな。あとリリーとも話したいし"


hi "そういえば、お前はクラスを手伝わなくていいのか？"

show kenji rage
with charachange


ke "お前正気かよ？"


ke "あのアマろくなこと考えちゃいないぞ。俺にはピンと来たぜ。あの女の存在は、俺の遥かな展望を遮る黒い影だ"


ke "目が見えないだけある"


hi "なんだそれ"


hi "それに、お前も目……"

show kenji neutral
with charachange


"健二は手で俺を制す。"


ke "あくまで診断上のことだ"


ke "比喩的に言えば、俺はどんな奴らよりも遠くを見据えている"


"健二は自分の言葉を強調するために、表情を殺して『比喩的な遠く』へ目をやる。あごをしゃくって男らしく見せようとしている。視線の向かうほんの2メートル先は廊下の壁だがもう好きにしてくれ。"

show kenji tsun
with charachange


ke "俺には人類の未来が見えるんだ。女どもの脅威を抑えない限り、未来は暗いままだ"


ke "奴らはどこにでもいる"



label jp_A38c:



hi "んー、美術部に入ったからそこの人らと行くかな"

show kenji rage
with charachange


ke "お前、何したって？"


hi "美術部に入った"

show kenji tsun
with charachange


ke "お前、なんてバカな真似するんだよ。大変だぞ。美術部にいる女がどんなか、わかってないだろう。不安や悩みを抱えた美少女たちが、ひとの心臓をえぐり出して生のまま食べちまうんだぞ"


"まあ、美術部の部員は一人知ってるけど、あの琳が急に病的な殺人者になるとは思えない。"


hi "そりゃないな"


ke "そういうこと言うな。自分をごまかすんじゃない。お前、自分が何を相手してるのかわかってないだろう。一番たちが悪い奴らなんだぞ"

show kenji neutral
with charachange


ke "派手な見かけでお前を引きずり込んで、思ってもみないような時にバン！　だ"


hi "何をバン？"


"健二はその質問にやや動じたみたいだけど、やつの狂気はおさまらない。"

show kenji tsun
with charachange


ke "どうでもいいだろ"

ke "慎重にいけよ、慎重にな"



label jp_A38d:



hi "そうだなあ……腹減ってる感じだけど、体を大事にするって約束しちゃったからな。健康増進、てやつ"


hi "たこ焼きはよしたほうがいいのか、それとも直行すべきか。どうしようかなあ"

show kenji tsun
with charachange


ke "約束？　なんか不吉な感じだな。見返りはなんなんだ？"


hi "何もない、と思うけど？　見返りとか、そういう約束じゃないよ"


hi "同じ学年の笑美って知ってるだろ？　共闘を約束したっていうか"

show kenji rage
with charachange


ke "ひいいいいいいいいい！"


"恐怖に染まった健二の顔と、急に飛び出した金切り声に背筋が凍る。『悪魔に魂を売りました』と告白されたカトリックの聖職者みたいな反応だ。"


ke "笑美だって！　お前悪魔に魂を売って、しかも何ももらわなかったってことか？！"


ke "お前、一体どうしたんだよ？"


ke "自分の関わってる相手が誰だかわかってるのか？"


ke "あいつは歩く危険物だぞ。あいつのピンポイントな高速タックルで毎月どれだけの人間が病院送りにされてるか知らないのか？"

show kenji tsun
with charachange


ke "あいつも奴らの仲間だ！　男らしいものはすべて服従させようとする巨大な陰謀の中心人物だ"


ke "今聞いてることが信じられない。俺はお前の判断力を信じてたんだぞ。俺たちは仲間だと思ってたのに"


ke "手遅れになる前にやめるんだ"


ke "学園祭もそうだ。あいつらの策略の一部なんだぞ"



label jp_A38e:


"健二はイライラとスカーフをいじり回している。どんどん加速して、まるで火でも起こそうとしてるみたいだ。と、パニック症状が落ち着いてきたのか、指の動きも段々落ち着いてきた。"

show kenji neutral
with charachange


ke "隠れ場所を探さないと……安全な避難場所を。それからこんなひどい一日を経験しなくて済むように、自分でぶっ倒れるんだ"


ke "ちょうどいいのを持ってる。準備しないと"

show kenji tsun
with charachange


ke "学園祭には行くなよ"


hi "ああ"

show kenji neutral
with charachange


ke "またな、久夫"

stop music fadeout 2.0

hide kenji
with charaexit


"ドアが低い音を立てて閉まる。健二の言った事をどう思えばいいのかわからなかった。"




label jp_A44:

show bg school_dormhallway at bgright
with None


"静音とミーシャと何をしようか、と考える。準備は念入りにしておいた方がいいと思い、俺は部屋に戻って財布にお金を補充する。"

scene bg school_dormhisao
with locationchange


"今日は金魚すくいは出てるのかな。"


"あれは本当は難しいのに、見た目はずっと簡単そうなんだよな。でも金魚なんてとったところで、別に飼う理由なんてないんだけど。"


"こんな小さな部屋で、魚なんて飼ってどうするんだ？　料理して食べるのか？"


"静音かミーシャにあげてもいいけど、それは俺にとっての一線を越えてしまっている気がする。"


"本当に困ったもんだ。二人ともかわいいけど、どっちも脈があるとは思えない。にもかかわらず、俺は実際にプレゼントした場合のことを考える。"
"今晩あいつらに何かあげたら、どんな反応をするだろうか、と想像する。金魚とか、ぬいぐるみとか。"


"ミーシャならたぶんいつもと同じように笑うんだろう。静音は俺の手からはたき落としたりするかもしれない。"


"なんか、やっぱりいい考えじゃないな。"



"よし、準備オーケーだ。"


with shorttimeskip



"かなり時間が経ってから、これはまた静音が心理戦を仕掛けてきているんじゃないかと思い始める。そうでないとしても、ちょっと遅い時間になっている。"



"ちょっと外に出て二人を探すことにする。とはいえ、どこを探せばいいか見当はついていない。今日あいつらを見つけるのは特に難しそうだ。"

scene bg school_dormhallway
show shizu behind_blank_close at center
with locationchange


"外に一歩出たとたん、静音にぶつかりそうになる。"


hi "よう、静音。ミーシャはどこだ？"

show shizu behind_frustrated_close
with locationchange


"どうにかして手話で伝えようとするけど、実際はただのでたらめだ。ミーシャに少しやり方を教わらないとだめだな。"


mi "ここだよ！"

play music music_comedy

show shizu behind_frustrated_close at Slide(0.5,0.5,0.7,0.5,1.0, time_warp=_ease_time_warp)
with None

show misha hips_grin behind shizu at Slide(0.5,0.5,0.3,0.5,1.0)
show shizu behind_frustrated_close at Slide(0.5,0.5,0.7,0.5,1.0,time_warp=_ease_time_warp)
with Dissolve(0.7)


"にこにこと笑いながら、ミーシャが静音の後ろから飛び出す。"


mi "ちゃんとひっちゃんが一緒に学園祭に来てくれるか、確かめに来たんだよ"

show shizu basic_angry_close at tworight
with charachange


shi "……"

show misha sign_smile at twoleft
with charachange


mi "約束破ったらだめだからね～！"


hi "約束？　何も約束した覚えなんてないぞ"

show shizu cross_angry_close
with charachange


shi "……"

show misha hips_frown
with charachange


mi "そうやって逃げようとするのやめなさい！"

show misha perky_sad
with charachange


mi "行こうよひっちゃん、楽しいから！　どっちみち行かなきゃいけないんだよ、でないとダメ人間になっちゃうよ！"

show misha perky_smile
with charachange


mi "びくびくしながら一日中部屋に引きこもってるような人みたいにはなりたくないでしょ？"


"俺は真向かいにある健二の部屋のドアを、ミーシャの肩越しに見る。"


"あいつに聞こえてないといいけど。でもミーシャは聞かせたかったんだろう。"


hi "そんなわけないさ、当たり前だろ。ちょっとした冗談だよ。今出かけるところだったんだ。二人ともわざわざ来なくてもよかったのに"

show misha cross_laugh
with charachange


mi "ほんとに？　あははは！　ひっちゃんがどうにかして逃げようとするんじゃないかって、しっちゃんが心配してたんだよ！"

show misha hips_grin
with charachange


mi "ひっちゃんがいなきゃだめなの～！"


hi "えっ？"


"今、心臓が一拍飛んだ気がする。"

show misha perky_smile
with charachange


mi "ゲームの屋台があるんだけど、わたし狙うのへただからぬいぐるみが落とせないの……それにしっちゃんは物は投げないって言うし"


hi "なんだ"


"俺ががっかりしたのにすぐに気づいて、静音がこっちを見つめてくる。組んでいた腕を開いて、眼鏡を直す。"

show shizu adjust_happy_close
with charachange


shi "……"


mi "何だと思ったの？　わたしは何も投げないからね"

show misha perky_confused
with charachange


mi "どうして、しっちゃん？　それ変だよ……"

show misha perky_smile
with charachange


mi "まあとにかく、ひっちゃん、ボール投げくらいはしたことあるでしょ、ね～、ね～？　なので！　一緒に来なきゃだめなの！"


"こいつらの理屈には唖然とさせられる。冗談で言っているのか、それとも本気なのかわからない。"


hi "へっ、それ冗談だって知らなかったら、怒ってるところだぞ"


hi "冗談だよ、な？"

show shizu behind_frown_close
with charachange


shi "……"


mi "本気なんだよ、ひっちゃん～！　本気ったら本気本気本気なの！"


hi "ああそうかい。安心したよ"

show shizu basic_normal2_close
with charachange


shi "……"

show misha hips_smile_close at closeleft
with characlose


mi "ほら、行こうよ！　聾バンドが窓の外で準備してるよ"


"ミーシャは俺の手をつかんでドアから引っ張り出そうとする。まあ本気じゃないのは明らかだけど。"

hide shizu
with None

show shizu basic_normal2_close behind misha at tworight
with None

show shizu adjust_blush_close
with charachange

stop music fadeout 3.0


"静音は俺たち二人を見て、少し頬を赤くしつつ落ち着かなげに眼鏡をいじっている。"


"俺はこういう気軽な触れあいには慣れてないけど、ちっとも不愉快じゃない。文句なんてあるわけないだろ？"

play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_courtyard
show crowd
with locationskip

play music music_running


"まだ外は明るいけど、そろそろ太陽が木々の向こうに落ちようとしている。"


"全生徒の半分が学園祭にくり出しているようだ。先生たちも何人か端っこに立って、フルーツポンチを飲んでいる。"


"ボウル丸ごと空にしてしまいそうな勢いだ。売り子をしている女子がおろおろしている。"


"占い師が何人か、暇そうに友達とおしゃべりしている。一方、近くに来た人を手当たり次第に捕まえて占い始めている生徒もいる。"


"ああいうやり方はちょっと積極的すぎると思うけど、やる気があることの現れなんだろう。見ていて元気は出るけど、自分がそれについて行けるかどうかはわからない。"

show shizu basic_normal2 at tworight
show misha perky_smile at twoleft
with charaenter


shi "……"

show misha sign_smile
with charachange


mi "なにか食べ物買おうよ。ひっちゃん、おなかすいた？"


"そう言えば、朝から何も食べてないな。"


hi "焼きそばはあまり食べたくないんだけど"

show misha hips_grin
with charachange


mi "いいよ、揚げ物ならほかにもあるから！"


hi "揚げ物じゃない食べ物はあるのか？"

show shizu adjust_smug
with charachange


shi "……"


mi "アメならあるわ。ジャンクフードはお祭りの真髄よ！"

show misha cross_laugh
with charachange


mi "わはははは！"

show shizu behind_smile
with charachange


shi "……"

show misha hips_grin
with charachange


mi "行こ、わたし――じゃなくて、しっちゃんが――一品だけおごってあげる～！"


mi "ひとつ？"

show shizu adjust_smug
with charachange


shi "……！"

show misha sign_smile
with charachange


mi "ひとつだけよ～！　思いっきりボールを投げられるように腹ごしらえするだけだからね！"

show misha perky_smile
with charachange


mi "あー、でもまだ準備の終わってない屋台もあるみたいだよ。だから欲しい物があってもゲットできないかも"


"俺はあたりを見渡し、屋台の多さに驚く。信じられない、このお祭りは町内で開催されるものよりも大きいんじゃないか。"


"ミーシャの言葉に反して、もう学校のほとんどはお祭り気分のようだ。"


"少なくとも全生徒の半分の興奮したしゃべり声で、空気がうなりをあげている。"


"料理をしている匂いがする。おかげでどんどん空腹感が強くなる。"

show shizu behind_frustrated
with charachange


shi "……"

show misha perky_confused
with charachange


mi "ほら、ひっちゃん、もう食べ物がどんどんなくなってるよ！　たこ焼き食べたかったら、今すぐ行かなきゃ！"

show misha hips_grin
with charachange


mi "わたしもたこ焼き食べるよ～！　ほら、食べようよ！"


hi "そうだな、もうずっとたこ焼きなんて食べてないし。俺も行くよ"

hide shizu
with charaexit

hide misha
with charaexit


"ミーシャに俺の返事を通訳する暇も与えず、静音は歩き始め、足早にたこ焼きの屋台に向かう。ミーシャと俺はそれを追いかける。"

scene bg school_stalls1
with locationchange


"ミーシャは笑いながら静音に向かってスキップする。静音は指を３本立てて、たこ焼きを３皿注文する。"


"今まで一度も気づかなかったけど、あんなに高級茶にこだわってた静音が、屋台の食べ物にも入れ込んでいるっていうのはちょっと変な感じだ。"


"俺は静音がくれたたこ焼きの皿を受け取り、食べ始めるべきかと考える。見た感じ、ものすごく熱そうだ。"


"煙が出てるし、表面の油も泡立ってる。"

show misha hips_smile at Slide(0.2,0.5,0.3,0.5,1.0)
show shizu behind_blank at Slide(0.8,0.5,0.7,0.5,1.0)
with Dissolve(1.0)


"静音とミーシャは俺を見る。自分たちの前に俺が食べ始めるのを待ってるみたいだ。"


"引き下がるわけにはいかないので、お皿の隅っこにさっそうと突き立っていた小さなプラスチックのフォークを取り、たこ焼きの一つを刺す。"

show misha hips_grin at twoleft
show shizu basic_normal at tworight
with charachange

stop music fadeout 12.0


"でもまだ俺がたこ焼きを口に入れてもいないのに、静音もミーシャも熱心に食べ始める。"
"静音は素早く、でも少しずつたこ焼きをかじっている。ミーシャは小さな子供のように、おいしそうに食べている。"


"結局のところ、二人とも他の生徒と同じ、ふつうの子供なんだってことか。"


"なんだかいいなあ。こうして他の人とぶらぶらして、一緒にいるのを楽しむなんて、俺にはそんな機会はずっとなかったな。"


"ここにくる前だって、この一年はずいぶん忙しかった。忙しすぎて、自分が今まで何を見逃してきたのか、全然気づいていなかった。"


"ここにいると、安らかな気持ちになる。"


"この雰囲気は心が落ち着く。こんなお祭りがまだあったなんて知らなかった。"

show misha perky_confused
with charachange


mi "あれ？　ひっちゃん、それ食べないの？"


hi "いや、食べるぞ"

show shizu adjust_smug
with charachange


shi "……"

show misha sign_smile
with charachange


mi "熱すぎるからっておじけづいてるんじゃないでしょうね"


hi "んなわけないだろ"


"二人にからかわれることだって、心温まる気がしてくる。"

$ renpy.music.set_volume(0.6, 2.0, "ambient")

scene bg school_stalls1_ss
with shorttimeskip

play music music_tranquil fadein 1.0


"ぼうっと光る紙の提灯が、夕焼けのなかで暖かく灯っている。きれいな光景だな、と思いながら、俺は食べ物が冷める前に急いで食べる。"

show shizu behind_smile_close_ss at center
with charaenter


"たこ焼きの最後の一口を食べ終わる前に、静音が俺の前に歩み寄る。ぴんとまっすぐに立って、腕は背中の後ろにしっかりと回している。"


"できるだけ真面目そうに見えるように努力しているのがわかる。"
"でもその静音でさえ、機嫌のよさを隠しきれていない。顔に少しだけ笑みが浮かんでいる。"

show bg school_stalls1_ss at bgright
show shizu behind_smile_close_ss at closeright
with charamove

show misha cross_laugh_ss at twoleft
with charaenter


mi "あははは～！　行こ、ひっちゃん、ゲームしようよ！"


hi "設営だって終わってないんじゃないのか？"

show shizu adjust_happy_close_ss
with charachange


shi "……"

show misha cross_grin_ss
with charachange


mi "ないけど、そんなの関係ないない～！　ほら行こうよひっちゃん、急がないと混んじゃうよ！"

show misha hips_grin_close_ss at closeleft
with characlose


"ミーシャは俺の肩に手をおいて、すごい大声で笑う。"

show misha perky_smile_close_ss
with characlose


mi "行こ行こ！　今年は景品がすごく良さそうなんだよ、ほんとほんと～！　わたしたちみたいな美少女に、景品とってあげたくないの？"


"ミーシャが全力で『かわいい』ポーズをしてみせる。正直言って、すごくかわいい。"
"同じことをしてくれるんじゃないかと期待して、静音の方を見る。でも静音は、頭おかしいんじゃないか、とでも言いたげに俺を見るだけだ。"

show shizu cross_wut_close_ss
with charachange


shi "……"

show misha hips_grin_close_ss
with characlose


mi "ミーシャ、それやめなさい！"

show misha perky_confused_close_ss
with charachange


mi "待って……わたしミーシャ……"

show shizu basic_normal2_close_ss
with charachange


shi "……"

show misha sign_smile_close_ss
with charachange


mi "ひっちゃん急いでよ、さっきからずっとそのたこ焼き持ったまま立ってるじゃない！"

show misha cross_laugh_close_ss
with charachange


mi "ははははは！"

show misha cross_smile_close_ss
with charachange


hi "俺は何でも味わって食べたいんだよ。これだってそうだ"

show shizu basic_sparkle_close_ss
with charachange

show shizu adjust_smug_close_ss
with charachange


"何の警告もなく、静音が俺の手からたこ焼きをつまみ、笑いながら自分の口に放り込んでしまう。"


"あまりに素早い出来事で、俺には止めようがなかった。"

show misha cross_laugh_close_ss
show shizu behind_smile_close_ss
with charachange


"何が起きたのか理解する前に、ミーシャは突然大笑いし、静音も俺に微笑みかける。たぶん声を出して笑うのに一番近い表情だろう。"

show shizu adjust_happy_close_ss
with charachange


shi "……！"


mi "ま、これでかたづいたわね～！　わはは！　はははは！"

stop music fadeout 6.0


"静音が俺の右手を、ミーシャが左手をつかむ。"

show shizu behind_smile_close_ss
with charachange


shi "……"

show misha hips_grin_close_ss
with charachange


mi "一緒に来るの！　今晩はお楽しみがたくさんあるんだから、全力で遊ばなきゃだめだよ！"

show misha cross_laugh_close_ss
with charachange


mi "はははは～！"

$ renpy.music.set_volume(1.0,2.0, "ambient")

scene bg school_courtyard_ss
show crowd_ss
with shorttimeskip

play music music_ease fadein 6.0


"もうかなりの人数になった人混みを駆け抜けながら、俺たちは片っ端からゲームで遊ぶ。"
"輪投げ、モグラたたき、それに今まで一度も聞いたことがないようなゲームまで。"


"ほとんど勝てないけど、それでも楽しい。"


hi "なあ、金魚すくいはあるのか？"

show shizu behind_smile_ss at tworight
show misha hips_smile_ss at twoleft
with charaenter


shi "……"


mi "もちろん！　あれが好きだなんて知らなかったよ、ひっちゃん！"


hi "まあ、一度やってみたいと思ってたんだ。見た感じ、そんなに難しそうじゃないし"

show misha hips_grin_ss
with charachange


mi "それ本気で言ってるの、ひっちゃん～？"

show misha cross_laugh_ss
with charachange


mi "わははは～！　おっけ、おっけー！　じゃあやってみようか！　このへんにあるはずだよ！"

show shizu basic_normal_ss
with charachange


shi "……"

show misha perky_smile_ss
with charachange


mi "でも、金魚をどこで飼う気？　金魚鉢は持ってるの？"


hi "いや、ないけど……"

show misha hips_grin_ss
with charachange


mi "食べちゃうのかも！"

show shizu adjust_smug_ss
with charachange


shi "……"

show misha cross_laugh_ss
with charachange


mi "はははははは！　あはははははは！"

show misha cross_grin_ss
with charachange


mi "わかった、ひっちゃん、わたしたちが金魚とれたら、ひっちゃんにあげるよ！"


hi "へえ、ほんとに？　また勝負か？　いいぜ"

show shizu basic_happy_ss
with charachange


"静音は興奮したように俺を金魚すくいの屋台に追い立てる。はしゃぎ気味の自分の顔を隠そうとしてるんだろう。"

scene bg school_stalls2_ss at bgright
with locationchange


"幸い、二人とも一匹も取れずに終わる。俺も同じだけど。"

show bg school_stalls2_ss at bgleft
with charamove

$ renpy.music.set_volume(0.6,2.0, "ambient")

"その直後に、二人は俺をとりわけ大きくてカラフルな屋台の前に連れていく。俺が作るのを手伝ったやつだ。思わず笑ってしまう。"


"こいつは覚えてるぞ。作るのに本当に苦労したんだ。"


"屋台の主は髪を茶色に染めた普通っぽい人で、俺たちが近づいたとたんにこっちに気づく。俺の目を引くものが二つほどある。"


"まず目に付いたのは、ピラミッドみたいに積み上げた不透明な瓶にボールを投げて、できるだけたくさん倒すゲームだ。"


"ボール４つで５０円。いいじゃないか。"


"次に目に付くのは、点字で書いてあるゲームの遊び方だ。そのことについて何か言おうと思って、静音とミーシャも気付いているか確かめてみる。"


"二人とも見ていないか、それを全く変だと思っていないか、どちらかのようだ。"


"屋台の人" "よう！　羽加道さん、よく来てくれた！　屋台出すの手伝ってくれて、ほんとにありがとう。楽しんでる？"


"ミーシャが一部始終をあっという間に通訳する。静音はそれをちらりと見てから、屋台の人ににっこりと笑う。"

show shizu behind_smile_ss at Slide(0.8,0.5,0.7,0.5,1.0)
show misha perky_smile_ss at Slide(0.2,0.5,0.3,0.5,1.0)
with Dissolve(1.0)


shi "……"

show misha hips_grin_ss at twoleft
with charachange


mi "はは～！　大したことないですよ、全然、ほんとに～！　すごく楽しいです。今までわたしたちが手がけた学園祭の中でも最高だと思いますよ！"

show misha perky_smile_ss
with charachange


mi "白木さん、わたしたちもこれやりたいんですけど、いいですよね、ね？"

show misha hips_grin_ss
with charachange


mi "もちろん～、このかわいくて仕事熱心な生徒会メンバーが学園祭のために費やした時間に免じて、景品をプレゼントしてくれたら、すごくうれしいです！"




"白木" "ははは、はは……だめ"


"何はともあれ、この白木さんは度胸があるな。"


hi "あの、俺この屋台作ったんですけど。すごい大変だったんですよ。人生の貴重な時間を２時間も無駄にしたんですから"
hi "一回くらいやらせてもらってもいいと思いますよ"

show misha hips_frown_ss
with charachange


mi "わたしも！"

show shizu basic_angry_ss at tworight
with charachange


shi "……"


mi "わたしもね！"

show misha perky_confused_ss
with charachange


mi "あー……"


"しばらくためらってから白木さんは降参し、肩をすくめて俺たちにボールを４つずつ渡す。"

show misha hips_grin_ss
show shizu behind_blank_ss
with charachange


"一秒も立たないうちに、静音とミーシャは自分のボールを俺の前にドカドカと置く。"


hi "なんだよこれは？"


hi "まさかこれだけ大騒ぎしておいて、遊びもしないっていうんじゃないだろうな？"


hi "白木さん相手にみんなでたかっておいて、そりゃないだろ"




"白木" "そうだよ……"

show shizu basic_frown_ss
with charachange


shi "……"

show misha sign_smile_ss
with charachange


mi "白木さんは黙っててくださいね～！"

show shizu adjust_happy_ss
with charachange


"静音は俺に向かって、素っ気なくひらひらと手を振る。ミーシャは静音の言葉を通訳すべきか、白木さんを気遣うべきか、迷っているようだ。"

show shizu adjust_smug_ss
with charachange


shi "……！"

show misha hips_grin_ss
with charachange


mi "あははは！　ひっちゃん、騎士道精神はどこに行っちゃったの？　わたし――しっちゃんは、ボールは投げないのがポリシーなの！"

show misha hips_smile_ss
with charachange


mi "あー、ごめんねひっちゃん、わたしもボールを狙って投げるのうまくないんだ。でもひっちゃんは上手なんでしょ、ね、ね？"
mi "ひっちゃんなら大丈夫だよ！"

stop music fadeout 3.0


"見た目は簡単そうだな。瓶もそんなに遠くないし、問題はボールがプラ製の穴あきボールだってことだけだ。"

play sound sfx_impact


"瓶の一つに向かって思い切り投げてみる。ボールはあっさりと跳ね返る。"

show shizu behind_blank_ss
show misha perky_confused_ss
with charachange


hi "なんだこりゃ？"




"白木" "あー、そうそう、見た目ほど簡単じゃないんだよね。瓶に水を入れてあるから。企業秘密な"

show misha hips_frown_ss
with charachange


mi "それずるーい！"


hi "だから４球５０円ってわけか。なんて悪質なんだ"

show shizu basic_angry_ss
with charachange


shi "……"

show misha hips_smile_ss
with charachange


mi "がんばって、ひっちゃんなら倒せるよ！　あと１１個もあるんだから！　いけー！"


hi "お前がやったらどうだ"


hi "静音？　やってみない？"

show shizu behind_blank_ss
with charachange


"静音はきっぱりと頭を横に振る。"


"俺は笑う。正直、これはかなり楽しい。"

play sound sfx_impact
play music music_soothing fadein 3.0


"俺は振りかぶって、瓶でできたピラミッドにもう一球投げる。ほんの少しだけ瓶をずらすことに成功する。"

show shizu basic_normal_ss
show misha perky_smile_ss
with charachange


"静音もミーシャも、猫みたいな形をしたぬいぐるみに向けて物欲しそうな視線を送っている。"


"結局、この二人はそんなに違わないんだな。"


"ときどき、静音がしゃべれたらミーシャみたいにしゃべるんだろうか、なんて考える。"


"いや、そこまで似てはいないか。"

play sound sfx_impact


"実は結構簡単だ、ということに気づいて、俺はもう一球投げる。一番下の段にある瓶を二つ同時に倒せれば、楽勝だ。"


"人数は少ないけど、もう観衆が集まり始めていて、プレッシャーが本気でかかってくる。あと９球だ。"

play sound sfx_dropstuff


"野球のピッチャーのように振りかぶり、力の限りボールを投げると、瓶はがらがらと倒れる。"

show shizu behind_blank_ss
show misha cross_laugh_ss
with charachange

show stuffedcat:
    alpha 0.0 yalign 0.5 xanchor 0.5 xpos 0.6 subpixel True
    easein 1.0 xpos 0.5 alpha 1.0
with Pause (1.0)


"勝ち誇りながら、俺は景品の猫のぬいぐるみを要求する。ミーシャは自分が景品を取ったかのように騒々しく笑う。"


"静音はいつもの無表情な顔で俺を見つめてくる。静音もぬいぐるみをほしがってるのは明らかだ。"

show stuffedcat:
    easeout 1.0 xpos 0.4 alpha 0.0
with Pause (1.0)

hide stuffedcat
with None

show shizu basic_normal2_ss
with charachange


shi "……"

show misha hips_grin_ss
with charachange


mi "ひっちゃん、おめでとう～！　そのぬいぐるみ、どうするの？"


"この問いに正解はない。慎重に答えないと。"




hi "どうしようか……わからないな"


mi "じゃああああ～、ひっちゃんがいらないなら、わたしがもらってもいいよ……"

show shizu adjust_smug_ss
with charachange


shi "……"

show misha cross_grin_ss
with charachange


mi "自分で取っておきたいなら構わないわよ、ひっちゃん。ぬいぐるみが好きだなんて知らなかった。繊細なのねえ"


hi "取っとかないよ。ぬいぐるみなんて持ってても仕方ないし"

show misha cross_smile_ss
with charachange


mi "じゃあわたしがもらってもいい？"

show shizu behind_blank_ss
with charachange


shi "……"


"二人の視線が俺の心にガリガリと穴を開ける。"


"こんな決断はしたくない。俺は屋台に向き直る。"


hi "すいません、このぬいぐるみ、もう一つありますか？"




"白木" "実はあるんだよ。もう一つだけ"


hi "じゃあ元通りセットしてください。もう一つも狙うから"


"まだ８球ある。"

play sound sfx_pillow


"ゲームの準備が済むと、俺はすぐに全力で投げるけど、外してしまう。"

show misha hips_grin_ss
with charachange


mi "ははは！　もう一個ゲットするつもり？　楽な逃げ道を選んだね、ひっちゃん？"


hi "そんなに楽なら、お前がやってみろよ"


mi "遠慮します～！"

show misha perky_smile_ss
with charachange


mi "ところでひっちゃん、ボール投げてるときくらいぬいぐるみは置いたら？"


hi "いい"

show shizu adjust_smug_ss
with charachange


shi "……"


mi "残り一つしかないんだから、取りなさいよ！　取れなかったらおしおきよ～！"

show shizu behind_smile_ss
with charachange


shi "……"


mi "でもわたしにぬいぐるみを渡したくないからって、うまい言い訳考えたよね！　あ、今の『わたし』はわたしのことだからね～！"

show shizu adjust_happy_ss
with charachange


shi "！"

show misha cross_laugh_ss
with charachange


mi "あはははは～！　冗談だって！"


"ミーシャに悪意がなかったのは見ればわかる。静音も笑っているし、そのジョークをおもしろがっているようだ。でもその後は少しがっかりしていたように見える。"


"俺は静音にぬいぐるみを渡すことにする。少なくとも今は。巨大な猫を抱えたまま狙いをつけるのはちょっと難しい。"

show shizu behind_smile_ss
show misha perky_smile_ss
with charachange


shi "……"


mi "ありがと、ひっちゃん。しっちゃんも喜んでるみたいだよ、ひっちゃん～！　でも、わたしにももう一つ取ってくれるんでしょ、ね？"


hi "今取ろうとしてるんだよ、そうだろ？"

stop music fadeout 5.0

show shizu behind_smile_ss at Slide(0.7,0.5,0.8,0.5,1.0, time_warp=_ease_out_time_warp)
show misha perky_smile_ss at Slide(0.3,0.5,0.2,0.5,1.0, time_warp=_ease_out_time_warp)
with None

hide shizu
hide misha
with Dissolve(1.0)

play sound sfx_pillow


"もう一度投げる。でも今回はまるで狙いが外れる。"


"腕もなんだか重く感じる。血がちゃんと流れていないかのようだ。"


"俺は心の中で自分をしかりつける。この程度のことで疲れるなんて情けない、と思う。"


"そして、これは自分の心臓のせいじゃないか、と思い至る。もしそうだったら、どう考えたらいいのかわからない。"

play sound sfx_impact


"こんなちょっとしたことなのに、自分の死すべき運命を思い起こさせられるという事実に、気が滅入る。"


"たぶん、そのことを忘れられるときが来ることは絶対にないんだろう。"


"今日だって、きれいな夜に美しい場所で、何も考えずにお祭りを楽しめると思っていたのに、自分がここにいる理由からは逃れられないんだ。"


"自分の人生を通じて、こんなに心が落ち着くと感じたことはなかった。今まで訪れたどんな場所とも違う、この場所で。"

play sound sfx_pillow
play music music_sadness fadein 2.0


"考えたくなかったことを、もう考えずにいることができない。"


"俺はただ、死ぬためにここに送られたんじゃないか、と。"


"この数日は俺の人生で最高の部類だった。本当に自分が生きているんだ、と感じられたのは、とても久しぶりだった。"


"でも結局、階段を上りすぎたり、ボール投げのときに力を入れすぎたりするだけで、自分がいつ死ぬかわからないという事実を思い出すはめになる。"

play sound sfx_pillow


"俺は未来永劫それに縛られるんだ。"


"落ち込んだ次には腹が立ってくる。そっと人生を楽しもうとしているのに、今の俺の生活は結局これまでにないくらいはかないものになっている。"


"俺が死ぬとしたら原因は何になるんだろう、と考える。何でもありだろう、こんなに体が弱くてボロボロだったら。"
"下手に転ぶとか、胸を殴られるとか、たまたま野球の球が飛んでくるとか。"


"もうやる気を失っていたが、それでも俺はゲームを続ける。"

stop music
$ renpy.music.set_volume(0.0,0.0, "ambient")
play sound sfx_heartfast

show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)


"突然、ほんの一瞬だけ胸に痛みを感じる。痛みは現れてすぐに消えるけど、俺をほんの少しよろめかせるには十分だ。"

$ renpy.music.set_volume(0.4,10.0, "ambient")

show shizu adjust_blush_close_ss at Slide(0.8,0.5,0.7,0.5,0.5)
show misha perky_confused_close_ss at Slide(0.2,0.5,0.3,0.5,0.5)
with Dissolve(0.5)


"静音が驚いて飛びのく。俺の方に近づいて、心配そうな目で見つめてくる。ミーシャが手を俺の肩に置く。"

play music music_pearly


mi "ちょっと、ひっちゃん、大丈夫？"


hi "ああ、大丈夫。ちょっと気分が悪くなって。病気かもしれない。これ以上続けるのは無理だと思う"

show misha hips_frown_close_ss at twoleft
with charachange


"ミーシャは顔をしかめる。"


mi "無理しないで。そんなに調子悪かったら、余計にひどくなるよ"

show shizu basic_normal2_close_ss at tworight
with charachange


shi "……"

show misha hips_smile_close_ss
with charachange


mi "ねえ、まだお祭りは始まったばっかりだし、ずっとゲームばっかりやってたじゃない。疲れたなら少し休もうよ"

show misha sign_smile_close_ss
with charachange


mi "いいね、しっちゃん。わたしもちょっと疲れてたし！　学校中走り回ってたから、みんな疲れてるんだと思うよ、ひっちゃん！"


"俺はうなずく。二人とも何もおかしなことには気づかなかったようだ。よかった。"

scene bg school_courtyard_ni
show crowd_ni
with shorttimeskip

$ renpy.music.set_volume(1.0,2.0, "ambient")


"俺たちは人混みの海を通り抜けていく。その間、ミーシャが知っている人の顔を陽気に逐一教えてくれる。"
"静音は猫のぬいぐるみをぼんやりと腕に抱えている。二人とも楽しんでるみたいだな。"


"突然、俺は罪悪感に胸が痛む。"


"俺が病弱なせいで、みんなが遊びをやめるはめになったんだ。"

show shizu behind_smile_ni at tworight
show misha perky_smile_ni at twoleft
with charaenter


shi "……"


mi "ひっちゃん、わたしたち二人ともおなか減ってきてるんだけど。ひっちゃんはどう？"


hi "腹減ってしょうがないってわけじゃないけど、食べ物は欲しいな"

show misha hips_smile_ni
with charachange


mi "十分だよ、ひっちゃん～！　じゃあ、何食べようか？"


hi "俺は何でもいいよ"

show shizu adjust_happy_ni
with charachange


shi "……"

show misha hips_grin_ni
with charachange


mi "あ！　じゃあサンドイッチはどう？　あと飲み物もいるわね！　ミーシャが全部買ってくるから！"

show misha perky_confused_ni
with charachange


mi "えっ？"

show shizu behind_smile_ni
with charachange


"静音が俺を見て微笑む。そのとき、静音は冗談で俺を元気づけようとしているのかも、と気づく。俺は笑い声をあげる。"

show shizu adjust_happy_ni
with charachange


shi "……"

show misha perky_smile_ni
with charachange


mi "ひっちゃん、結構混んできてるから、ここで食べるのは無理かも。それに周りがうるさいし"

show misha sign_smile_ni
with charachange


mi "屋上に行って食べる方がいいんじゃないかな"


hi "俺は構わないよ。眺めもいいだろうし、少しは風もあるだろうし"

show misha hips_grin_ni
with charachange


mi "じゃあ決まりだね！　今のうちに食べ物と飲み物、買ってきた方がいいね……じゃあまた後でね～！"

hide misha
with charaexit

stop music fadeout 6.0


"ミーシャはぎこちなく手を振り、走り去る。"


"さっきまでは紙提灯が夜をどう照らすのか気づかなかった。でも見えるようになってみると、それは見事な眺めだ。"


"蛍が頭の上で飛んでいる。その柔らかな光は、夜空に輝く雪が降っているかのようだ。"


"町中ではこんな光景を見ることはできないだろう。"

show shizu adjust_happy_ni at Slide(0.7,0.5,0.5,0.5,0.5,time_warp=_ease_time_warp)
with None

show shizu cross_angry_close_ni at Slide(0.7,0.5,0.5,0.5,0.5,time_warp=_ease_time_warp)
with Dissolve(0.5)


"静音がいらだたしげに俺の袖を引っ張り、腕を組む。俺の気がそれているのが不満だといわんばかりに顔をしかめる。"

show shizu basic_angry_close_ni at center
with charachange


shi "……"


hi "俺が手話わからないってこと、知ってるだろ"

show shizu behind_frown_close_ni
with charachange


shi "……"


"考えてみれば、耳が聞こえない人にそんなことを言うのって、なんか俺がバカみたいじゃないか？　静音には聞こえないんだから。"

show shizu behind_blank_close_ni
with charachange


"理解できない、ということが伝わるのを期待して、俺は肩をすくめる。静音は頭を振ると、手をさっと振って話を終わらせる。"


"ミーシャに手話のレッスンを頼んだ方がいいかもしれないな。"

$ renpy.music.set_volume(0.3, 1.0, "ambient")

scene bg school_roof_ni
with locationskip


"屋上に上がると、この学校の巨大さに改めて驚く。敷地はあまりに広大で、今までそれに気づかなかったことが信じられない。"


"静音の後について屋上を横切る間、空に輝く星に目を奪われてしまう。"

show shizu behind_smile_close_ni at center
with charaenter


"静音と俺はベンチに座る。静音は機嫌良さそうに、柔らかく微笑む。そよ風がその髪の毛を吹き抜ける。"


"お祭りを見下ろすと、そこは琥珀色にきらめく提灯と揺れ動くうちわの海のようで、その中に人があふれかえっている。"
"そのうち何人かはお祭りらしい浴衣姿だ。"


"実際、女の子はほとんど浴衣を着ているみたいだ。どうして静音もミーシャも今日は着飾ってないんだろう。"


"二人とも浴衣姿は似合うだろう。俺はつかの間、二人ならどんな柄の浴衣を着るだろうか、と考える。"


"静音はたぶん古風な感じで行くんだろう。でもミーシャはちょっと想像しづらい。"


"ミーシャが到着して、息を切らせながらこっちに走ってくる。腕に抱えた食べ物を落とすまいとがんばっている。"


"食べ物を全部地面に置いてから、ミーシャはごろりと地面に寝そべる。"

show shizu behind_smile_close_ni at tworight
show bg school_roof_ni at bgright
with charamove

show misha hips_grin_ni behind shizu at twoleft
with charaenter


mi "あははははははははは～！　いやー時間かかっちゃった！　ほら、二人とも何が欲しいか言わなかったから、甘酒と、サンドイッチと、あとアメもあるよ！"
mi "いろんな物をちょっとずつだよ！"


hi "こりゃいいや。じゃあ食べようぜ"


"ミーシャは小さな三角形のサンドイッチを一口かじる。"

show misha hips_smile_ni
with charachange


mi "で、ひっちゃん、学園祭はどう？　楽しいでしょ？"


hi "ああ"

show shizu adjust_happy_close_ni
with charachange


shi "……"


mi "今夜は星がきれいね。本当、これ以上ないってくらいいい日"

play music music_serene fadein 5.0
$ renpy.music.set_volume(0.1, 2.0, "ambient")

scene black
show bg misc_sky_ni at Fullpan(30.0)
with locationchange


"下の方から聞こえる人々の話し声と、遠くに聞こえるコオロギの鳴き声は、かすかな音楽のようだ。"


"俺は甘酒の缶から一口飲み、ミーシャの方を見る。"
"ミーシャは地面に背中を伸ばして、気持ちよく寝ているように見える。半分だけ入ったリンゴジュースの缶を腹の上に乗せている。"


"静音は足を体に寄せて座り込んでいる。空を見上げながら、落ち着かない子供のように体をゆっくりと前後に揺らしている。"


"二人とも本当にかわいいな。まわりを見てみると、ガールフレンドやボーイフレンドと手をつないでいる生徒がたくさん見つかる。"


"俺たちからそう遠くないところで、カップルが何組か互いに手をつなぎながら、星を見上げたり、お祭りの光を見下ろしたりしている。"


"心のどこかで、同じようにしたい、と思っている自分がいる。"


"静音とミーシャを見ながら、俺もいつかはどちらかに告白すべきなんじゃないか、と思う。思い切って賭けに出る価値はあるんじゃないか、と。"


"静音が手首にしている細い時計の、金色の針が動くのが俺の目に止まり、もう夜が遅いことに気づく。でも祭りはまだまだ盛況だ。"


"静音は俺が取った猫のぬいぐるみの手を今も握っている。俺の視線に、静音が気づく。"


shi "……？"


"ぶっきらぼうに、俺にぬいぐるみを差し出す。俺は笑い、俺がもらってどうするんだよ、と聞きたくなる。でも聞いたところで静音には理解できない。"


"静音が理解してくれることを期待して、俺は首を振り、自分でとっておけと伝えようとがんばってみる。"


"学校の外を見てみると、本当にたくさんの人がいる。みんな楽しそうで、陽気そうだ。"


"それを見ていると、俺も満足した気分になる。"


"本当にたいしたものだ。今日このためにがんばった価値があった。"


"それでも、俺はさっきから続いている罪悪感と憂鬱を振り払うことができずにいる。いつまでも引っかかっていて、忘れることができない。"


"静音が何事か手話で話しかけてくるけど、俺にはわからない。俺が何を言っても、静音には決して聞き取れない。"


hi "わからないよ、静音"


hi "まあいいや。俺たち二人とも、自分のせいだと思ってるのかな。とにかく、お前の手話わからなくて、ごめんな"


hi "あのさ、お前がむりやり俺を学園祭に連れてきたことに、思わず感謝しちゃいそうなくらいなんだ"
hi "でもお前とデートしようと思ったら、お前のそういう押しの強いところももっと考えとかなきゃいけないかもな"


hi "いや、ほんとは……嬉しいよ。今日は楽しかった"


hi "お前、もっと笑ったらずっとかわいいと思うよ。いい笑顔してるよ"

stop music fadeout 5.0

show shizu behind_frustrated_close_ni at center
show bg misc_sky_ni at right
with charaenter


"いらだったように静音は立ち上がる。手を背中に回し、夜空の星を背にして堂々と、自信に満ちて見える。"

stop ambient fadeout 2.0

show shizu out_serious_close_ni
with charachange


"突然、静音は空に向けて腕を広げる。両手で空を持ち上げているように、俺には見える。"


"俺の目の前にあるすべてのものをよく見てみろ、と言っているかのようだ。"

show shizu epictransition
show cityscape zoom behind shizu
show hill enter behind shizu


"お祭りの明かりを浴び、色とりどりの浴衣に彩られた学校、蛍の光に照らされた屋上、あまりに広大な空。畏敬の念さえ感じる光景だ。"


"静音は何がしたいんだろう？　ゆっくりとだけど、俺はわかり始める。この美しい眺めは、この世には十分すばらしいことがあるという証なんだ。"
"そして、それを憂鬱な気分で台無しにするのは許されないことだ、と。"


"静音の性格がそれを強調しているのを、ひしひしと感じる。"


hi "ありがとう、っていえばいいのかな"

hide shizu
show hill pairtouch at center
with charachange


"俺は目をそらす。でも静音は俺の肩をつかむ。腕時計が俺の頬に触れる。"


"左手で、静音は空を指さす。"

play ambient sfx_fireworks fadein 1.0

show fireworks behind hill
with None
show fw_screen behind fireworks
with Dissolve(5.0)


"かすかなはじける音とともに、空に花火が上がり始める。一つ一つが色とりどりの輝きを振りまきながら、ゆっくりと闇に消えていく。"


"前に花火を見たのがいつのことだったか、思い出すこともできない。ましてこれだけ大がかりなものは。"
"それどころか、花火は学校の敷地から打ち上げられているようだ。ほとんど信じられない。"


"空の光は町のほうから打ち上がった二度目の花火と混じり合う。デュエットのように、お互いを引き立たせるよう時間を合わせていたみたいだ。"


"花火は１５分ほど続き、そして終わる。"


"静音は自分がまだ手を俺の肩に置いていたことに気づいて、少し気まずそうにそっと手を引っ込める。"

stop ambient fadeout 5.0
hide fireworks
hide fw_screen
show hill pairnotouch
with Dissolve(5.0)


"いつもの落ち着きを取り戻すと、静音はにっこりと笑い、手を腰において胸を張る。"


"静音はこういうときが一番、普通の十代の女の子らしく見える。元気で、機嫌が良くて、気ままで。"


"考え込みながら、俺は静音と食べる。徐々に減っていく人混みを、二人で静かに眺める。"


"静音は少し体を前に倒しながら座り、あごをそっと手の上に乗せている。その満足そうな表情には少しだけもの悲しさが混じっている。"


"そして今までずっと、猫のぬいぐるみの手先をそっと握っていた。"


"俺は疲れを感じはじめて、また明日な、と静音に伝えてから寮に戻り始める。静音には聞こえない、ということには気づきもしなかった。"


"冷たい夜の空気の中でも、俺はぬくもりと活気を自分の中に感じる。"

stop music fadeout 4.0


"星々を背に力強く立ち、自分を哀れむなと告げる静音の姿が、なかなか心から離れない。"


"もし……恋に落ちるにはほんの一瞬で十分だとしたら、俺はもしかしたら静音に恋してしまっているのかもしれない、と思う。"


"本当に、少しだけ。"

window hide





label jp_A39:

show bg school_dormhallway at bgright
with None


"なんだか落ち着かない。今度はこっちまで疑わしい気分になり始める。"


"わざわざ行くべきだろうか？"


"読もうと思っている本もある。"


"存在するかどうかもわからない、アングラな郵便網に関する本だ。"


"短いし、一日で読み終えることができるだろう。"


"だけど、そんなことをして時間をつぶしてていいんだろうか？"


"まぁ、そうだな。当然いいに決まってる。"


"でも、外に出るのがもっといい考えだろう。"


"学園祭を見に行くんだ。"


"他の屋台なんかの出し物を適当に見て回るとするか。"


"マジな話、俺はこの一週間、どっちかというと愛想のいいキャラを保ってきた。せめてそれを崩さないための努力くらいはした方がいい。"


"何か食べ物を取ってこいよ、と俺の胃が言っている。"


"もう昼食時だ……外の屋台で何か買い漁るくらいはできるだろう。"

play music music_soothing fadein 1.0
play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_courtyard
show crowd
with locationskip


"すぐに外に出ると、いろんな生徒たちと、その親かもしれない人たちに取り囲まれる。"


"ときどき、きっと街から学園祭を見にやってきたんだな、という人がちらっと目に留まる。"


"そういう人たちは、見れば一目でわかる。"


"じろじろ見ずにはいられない人たち――その目の奥には、こんな考えが透けて見える。『で、{b}この{/b}生徒はどこが悪いんだ？』と。"


"思わず大声で怒鳴りつけてやりたくなる。"


"でもその一方で、俺自身も一週間ずっと同じことをしていなかったといえるだろうか？"


"嫌悪感みたいな波が押し寄せてくる――俺自身の偏狭さへの罪悪感だ。"


"……"

$ renpy.music.set_volume(0.6,2.0, "ambient")

scene bg school_stalls1
with locationchange


"そんな思索を脇に押しやって、空腹のせいで、胃が野火のようにひりひりと痛むのに意識を集中させる。"


"何かの揚げられる香りが俺を約束の地――食事の買える場所へと導く。"

stop music fadeout 0.6


"ちょうど注文したものが出てくるところで、大きな声で呼び止められる。"

show emi basic_annoyed at Slide(0.7,0.5,0.5,0.5,0.5)
with charaenter


emi "ちょっと、それどういうつもり？"

play music music_comedy fadein 0.5


hi "朝――じゃない、昼飯を食べようとしてんだよ"

show emi sad_annoyed at center
with charachange


emi "朝ごはん？"

show emi sad_angry
with charachange


emi "今起きたばっかりってこと？"


hi "えっと……"


"突然、朝寝坊してたことが犯罪みたいに感じられてくる。"


hi "いや、昼飯って言ったんだよ……マジで"


"笑美は信じていない。"


hi "ブランチかな？"

show emi basic_annoyed_close
with characlose


emi "そんな朝ご飯、全然健康的じゃないよ！"


"笑美は俺の食事をひったくると、こちらをにらみつける。"


"どういうつもりだよ、こいつ？"


hi "おい、それ俺の朝飯だぞ！"

show emi sad_annoyed_close
with charachange


emi "お昼ごはんじゃなかったの？"


hi "それ俺の……とにかく、俺の飯だっつーの！"


"笑美は両手を腰に当てると、説教を始める。"

show emi basic_annoyed_close
with charachange


emi "食事プランのこと、ホントにもう忘れちゃったの？"


emi "もっと健康に気をつけなきゃ、久夫くん！"

show emi sad_angry_close
with charachange


emi "心臓はどうなのよ？"


hi "心臓は別に問題ないよ！　だいたいは"


"返事の代わりに、笑美はあきれたように視線を上向ける。"

show emi basic_annoyed_close
with charachange


emi "どうだか"

show emi basic_closedgrin_close
with charachange


emi "問題がなかったら、この学校には来てないでしょ？"


"確かに、この子はいいところを突いている。"


"だけど、こっちとしても譲歩するつもりはない。"


hi "別にそんなに心臓が悪いわけじゃないって！"


hi "たまにちょっとだけ脂っこいものを食べるくらい、どうってことないに決まってるだろ！"


"よく言うよ。ちょっとランニングしただけでへばったくせに。"

show emi basic_annoyed_close
with charachange


"笑美は納得してないようだ。"

"そりゃそうだろう。俺だって納得していない。"


emi "そうかもね。だけど、いつも真っ昼間まで寝てるようなら話は別！"


"突然、笑美の顔に何か企むような表情がよぎる。"

show emi basic_grin_close
with charachange


emi "そもそも、最初から日課の運動をちゃんとこなしてたら、こんなことにはなってないわけだし……"

stop music fadeout 6.0


hi "あのさ、今週は本当にいろいろあったんだって！"


hi "たとえばさ、俺は危うく死ぬところだったんだぞ！　あと人にいっぱい会ったし、屋上でしばらく過ごしたし……"

show emi sad_annoyed_close
with charachange


emi "そういうの、サボりの言い訳にはならないでしょ"


emi "ちょっと死にかけたからって、基礎体力作りを怠けていいことにはならないの"

show emi basic_closedgrin_close
with charachange


emi "朝のランニングとかね"


"笑美は、ちょうど今重要なことが決まったみたいにうなずく。"

show emi basic_happy_close
with charachange

play music music_emi fadein 0.5


emi "じゃ、これで決まりってことで！"

show emi excited_proud_close
with charachange


emi "久夫くんは、自分のやり方が間違ってたって認めて、あたしの日課をちゃんと守るんだよね？"


emi "明日朝早くに会えるんだよね？"

show emi excited_happy_close
with charachange


emi "一緒に走ってくれるんだよね？"


hi "あのさ、それがいい考えだってのは昨日ちゃんとわかったから"

hi "何度も説得してくれなくていいって"


"すんなりと説得されたわけじゃなかったんだけど。"


"健康的な食生活を送るべき――笑美の言うことはなんだかんだいって正しい。なのに今、俺はひどく不健康なものを注文している。"


"おいしいんだけどな！"


"おいしさより大事なことなんてないんじゃないか？"


"生きることくらいか？"


"もし笑美がここで俺のひどい判断を叱りつけてくれなかったら、俺はたぶん……"


"いや、ちょっと待てよ。"


"突然、疑問が心に浮かぶ。"


hi "あのさ、なんで俺の健康のこと、そんなに心配するんだ？"

show emi basic_closedgrin_close
with charachange


"笑美は肩をすくめて笑みを見せる。"

show emi basic_grin_close
with charachange


emi "久夫くん、転校生じゃない"


emi "たぶん友達もまだいないでしょ、違う？"

show emi sad_grin_close
with charachange


emi "それに、今週ずっと迷惑かけちゃったでしょ？"


emi "怒らないで付き合ってくれた借りもあるし"

show emi basic_happy_close
with charachange


emi "あと、ナースくんにも約束しちゃったし"


"そう……なんだ。この小さくて走るのが大好きな女の子は、俺に健康になって欲しいんだ。"


"まぁ、このくらいならどうってことはないか。"


hi "わかったよ、そりゃ……そうだよな"


hi "気にかけてくれてありがとう"


hi "じゃあ、明日の朝ってことでいいな？"

stop music fadeout 1.0

hide emi
with charaexit


"これで話は終わりだと思い、背を向けて立ち去ろうとする。"

emi "ちょっと待って！"

play music music_running

with vpunch


"襟を手で掴まれたと思ったら、後ろに引っ張られる。" with vpunch


hi "おい、そんな乱暴にするなって！"


hi "今度はなんだよ？"

show emi sad_shy_close at center
with charaenter


"いらつき混じりの質問に、笑美はだいぶ傷ついているようだ。"


emi "付き合ってあげた方がいいんじゃないかって思って"

show emi basic_annoyed_close
with charachange


"笑美の目が細められる。"


emi "それに、これからまた揚げものなんかをこっそり食べに行くつもりだったんでしょ？"


"いや、そんなつもりはなかったんだけど、言われてみればそれもいい考えかもしれない。"


hi "違うよ！"

show emi sad_annoyed_close
with charachange


"またにらみつけられる。"


hi "ごめん、少しくらい買おうかなと……"


"まだにらみつけられてる。"


hi "ごめん、たくさん"


"おいおい、俺のやってることって自分にとっても他人にとっても危険なんじゃないか。"


"もっと健康にならなきゃいけないって納得したそばから、すぐ次の不健康な習慣のことを考え始めてるなんて。"

show emi basic_closedgrin_close
with charachange


emi "やっぱりね！　ホント信用できないんだから"

show emi basic_grin_close
with charachange


emi "これはもう、ずっとついてないとダメみたいだね"


"バカみたいなシチュエーションだ。"


"通行人に、俺の半分くらいしかない小さな女の子から説教されてる姿を見られたら、どう思われるだろう。"


"そろそろあきらめた方がいいかもしれない。"


hi "わかったよ、好きにしてくれ"


"俺はため息をつく。"


"こういう状況でも、やれるだけのことはやってみよう。"


hi "何がしたいんだ？"

show emi basic_confused_close
with charachange


"笑美は少し考え込む。"


emi "うーん、壁画のとこに行くって琳に約束したから……"

show emi basic_grin_close
with charachange


emi "じゃあ、それでいこうよ！"


"正直、俺としても壁画がどうなったのかちょっと興味がある。だからさっきと同じで、このくらいならどうってことはない。"

$ renpy.music.set_volume(1.0,2.0, "ambient")

scene bg school_courtyard
show crowd
with locationchange


"うなずいて同意すると、笑美は目的地へ向かって突っ走り、俺は入場者たちの間をほとんど体ごと引きずり回されている。"

stop music fadeout 6.0
stop ambient fadeout 2.0

scene bg school_dormext_full at bgright
with locationchange


"寮にたどりつくころには、心臓がバクバク言っているのがわかる。"


"たったこれくらいで動悸がするなんておかしいだろう。"


"体を落ち着かせるために、何度か深呼吸をする。"


"俺はこの学校で見た目が一番普通な部類に属してるけど、やっぱりここにいなきゃならないんだ。"


"ときどき、いっそ手か何かをなくしていたらよかったのにと思いそうになる。"


"それだったら少なくとも周りから浮いてはいないはずだ。"


"でも実際はそうじゃなくて、俺は病気にすら見えない。"


"呼吸を整えようとしてる今でさえ、単に具合が悪そうに見えるだけだ。"


"笑美は振り向いて、俺の不調に気づく。"

show emi basic_hes at Slide(0.4,0.5,0.5,0.5,0.5)
with charaenter


emi "まさか、あたしの眼の前で死んだりしないよね？"

show emi basic_shock at center
with charachange


emi "お願い、死なないでよ！"

show emi sad_depressed
with charachange


emi "そしたらみんなあたしのせいになっちゃう。そんな寝覚めが悪いの、いやだよ"


emi "それに、この前あんなことがあった後だし、ほんとに勘弁だよ。絶対ナースくんに、みんなあたしが悪いって言われちゃう"

play music music_soothing fadein 8.0


hi "い……いや、大丈夫だから"


hi "やっぱランニング、始めた方がいいみたいだな"

show emi basic_closedgrin
with charachange


emi "でも久夫くん、なんだか知らないけど脂っこいものを食べたがってたよね"

show emi excited_proud
with charachange


emi "ね？　あたしと出会ってよかったでしょ？"


"まったくだ。"


hi "たぶん"

show emi basic_grin
with charachange


"もちろん、笑美に学園祭会場を引きずり回されたりしなければこんなことにならなかったってことは、付け加えたりしなかった。"


"琳が突然現れて、その先の会話は中断される。"

show rin basic_absent at Slide(1.0,0.5,1.0,1.0,1.0)
with Dissolve(1.0)


rin "ああ、君たちか"

show rin basic_absent at tworight
show emi basic_grin at twoleft
show bg school_dormext_full at center
with charamove

show rin basic_awayabsent
with charachange


rin "こんちは、笑美"

show emi basic_closedhappy
with charachange


emi "こんちは、琳！　久夫くんが心臓発作を起こしそうになったから、連れてきたよ！"

show rin basic_absent
with charachange


hi "んなことないって！"


"俺の抗議は無視される。"

show emi basic_grin
with charachange


emi "壁画がどうなったか見たくて寄ったんだ！"


"琳はゆっくりうなずく。"

show rin basic_awayabsent
with charachange


rin "あぁ、あっちだよ"

show rin basic_deadpan
with charachange


rin "よく見えるよね"


"気がつくと考えている――琳はここで、壁画の前にどのくらい立っていたんだろう。"


"今まで一人でも、立ち止まってちゃんと壁画を見た人はいたんだろうか？"


"俺たちが一番最初なのか？"


"もちろんどう考えたって、壁画を目にするのは俺たちが最初じゃない。"


"というか、壁画はすごく大きい。"


"目に入らないわけがない。"


"その一方で、誰も壁画のことで実際に琳に話しかけたとは思えない。"


"俺たち以外には、ってことだ。"


"何か言わなきゃならない気がする。"


hi "すごくいいな"

show rin negative_spaciness
with charachange


rin "まだ出来映えには満足してないんだ"


rin "だけど、こんなものかな"


"琳はほとんどあきらめてしまっているみたいだ。"


"どういう出来上がりを考えていたのかはわからないけど、でも思った通りにはならなかったんだろう。"

scene bg mural at Fullpan(100.0, dir="left")
with Dissolve(2.0)


"俺たちは壁画の前に立って、その全容を理解しようとする。"


"俺は壁画の構図に集中しようと全力を尽くす。"


"実際、かなり興味深い。"


"色が突然まじりあって、俺はその中に引きずり込まれてしまう。"


"何もかもに夢みたいにおぼろげな質感があって、思わず眠くなってしまうくらいだ。"


"笑美と俺が取ってきてやった色を見つけようとする。"


"頑張ってみても、プルシアンブルーは見つからない。"


"まあいいか。"


"どこかにあることは確かなんだけど。"

scene bg school_dormext_full
show rin basic_awayabsent at tworight
show emi basic_closedgrin at twoleft
with Dissolve(2.0)


"俺の足が痛み始めても、琳は動こうとしない。"


"笑美が口を開く。"

show emi basic_confused
with charachange


emi "ねぇ琳、何か食べた？"

show rin basic_deadpan
with charachange


rin "当然。食べなきゃ生きていけないよ"

show emi basic_hes
with charachange


emi "じゃあ、５時間以内には？"

show rin relaxed_nonchalant
with charachange


rin "たぶん食べたよ。でもまたお腹すいてるし、勘違いかもしれない"

show emi basic_closedgrin
with charachange


"笑美はにっこり笑って、両手を打ち合わせる。"

show emi basic_grin
with charachange


emi "そっか！　じゃあ一緒に食べ物買いに行こうよ！"


"琳はうなずいて同意する。"

show rin basic_deadpannormal
with charachange


rin "いいよ。あの人たちにいなくなったって気づかれないように、急がないとね"


"たぶん、気にしないと思う。"


"あの人たちってのが誰なのかは知らないけど。"

stop music fadeout 3.0
$ renpy.music.set_volume(0.6,0.0, "ambient")
play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_stalls1 at Fullpan(8.0)
with locationskip


"屋台に戻ると、俺は揚げ物に恋焦がれるような視線を投げかける。"


"いや、やめておいた方がいい。"


"どうせ、笑美が許してくれるわけがないんだから。"

stop ambient fadeout 1.0

scene bg school_gardens
show emi basic_closedgrin at twoleft
show rin basic_awayabsent at tworight
with locationchange

play music music_ease fadein 9.0


"芝生にいい穴場を見つけて座り、それぞれに買ってきたものを食べる。"


"というか、俺が買ってきたんだけど。なぜか食べ物の代金を俺が全部払うことになってしまった。"


"びっくりしたことに、俺の食べ物（揚げてない）はとてもおいしい。"


"笑美と俺が食べるあいだ、琳はじっと……あちこちを見つめ、ときどき一口二口自分の食べ物を口にする。沈黙が降りる。"


"俺は一番先に食事を終え、芝生に寝転がる。"


"笑美が食べ物からちらりと顔を上げる。"

show emi basic_confused
with charachange


emi "疲れた、久夫くん？"


hi "ちょっと、かな"

show emi basic_annoyed
with charachange


emi "ねぇ、明日の朝、寝過ごしたりしちゃダメだからね"

show emi excited_proud
with charachange


emi "朝のランニング始めるんだよ、覚えてる？"


"実は、すっかり忘れていた。"


"俺は、実のところただ楽しんでいたんだ。"


"この二人と学園祭をぶらつくのは意外と楽しかった。"


hi "ああ、目覚ましをセットしておくよ"

show emi basic_annoyed
with charachange


emi "来ないとダメだからね！"

show emi basic_closedgrin
with charachange


emi "来なかったら怒るよ！"


hi "そうならないように、神様に祈っとくか"

show rin basic_lucid
with charachange


rin "神様は関係ないと思う"

show rin basic_deadpan
with charachange


rin "何か変なアクシデントが起きて、目覚まし時計がショートしなければ、だけど"

show rin basic_deadpannormal
with charachange


rin "そういうのって、神様の気まぐれかもしんないね"

show emi basic_grin
with charachange


emi "じゃあそんな気まぐれなんて起こさないでよね"


"一つの計画が、頭の中で形をなす。"


"ちょっと罪悪感を感じないでもない計画だけど、とにかくやってみよう。"


"ちくしょう、少しくらい揚げ物食べたっていいじゃないか。"


"それにどっちにしても、明日から走り始めるんだろ？"


"だから、本当の日課は今じゃなくて、全部その時に始まるんだ。"


"ゆえに食事制限が始まるのは明日からであり、それゆえ今日は不健康なものを食べても構わないということだ。"


"病院に入る前、好き放題に食べていたあらゆるものへの最後の別れとでもいうかな。"


hi "実はさ、部屋に戻ろうと思うんだ"


hi "宿題があったし、明日走るつもりなら、今夜は早く寝ないと……"

show emi basic_annoyed
with charachange


"笑美がまた目を細める。"

show emi sad_annoyed
with charachange


emi "あそこでこっそり揚げもの買ったりしないよね？"


hi "いやあ、お腹いっぱいでそんなことする気にならないよ"


"お腹を叩いて強調してみせる。"


hi "それに、お前らのせいで一文無しになっちゃったしな"

show emi basic_closedhappy
with charachange


"笑美はくすくす笑う。びっくりするくらい心地いい声だ。"


"またしても痛みのような罪悪感。"


"笑美は、俺が嘘をついてることに気づいてるはずだろ。"


"それとも、そんなに信じやすいだけなのか？"


"なんだか極悪人みたいな気分になる。"

show emi excited_proud
with charachange


emi "これもあたしの計画のうちだよ、久夫くん"

show emi basic_closedgrin
with charachange


emi "じゃあ、また明日の朝に会おうね"

show emi basic_grin
with charachange


emi "ごちそうさま！　あとあたしたちと付き合ってくれてありがと！"


"こっちは笑美が俺に付き合ってくれてると思ってたんだけどな。"

show rin relaxed_surprised
with charachange


"琳はうなずいて同意すると、足を俺に向けて振る。"


rin "『また明日』とは言わないよ。それって未来を予知するみたいなもので、私にはそんなことできないからね"


hi "……"


hi "なるほど"


hi "じゃあな、二人とも"


"変なことだけど、今日部屋を出る決心をしてよかった。"


"ここでの二週目のスタートとしては悪くないだろう。"

stop music fadeout 9.0
play ambient sfx_crowd_outdoors fadein 1.0

scene bg school_stalls1
with locationchange


"笑美の視界から外れているのを確認すると、俺は屋台へと直行してケーキを買う。"


"少なくとも、揚げものじゃないよな？"


"最初の予定よりも少しマシになってる。"


"笑美に嘘をついてしまって、まだちょっと悪いとは思ってるけど。"


"あいつ、俺の健康のことを心の底から気にかけてくれているみたいだ。"


"なんか埋め合わせをしてやらなきゃ。"


"部屋に戻った方がよさそうだ。"


"{b}本当に{/b}しなきゃならないことがあるんだから。"

stop ambient fadeout 1.0

scene bg school_dormhisao
with locationskip


"今朝読もうとしていた本を手に取ると、ベッドに倒れこんで、花火大会の間じゅう読み進める。"

$ renpy.music.set_volume(0.1,0.0, "ambient")
play ambient sfx_cicadas fadein 2.0

scene bg school_dormhisao_ni
with Dissolve(2.0)


"結局、歩き回った（より正確には走り回った）のがまずかったんだ。"


"ほんとに不健康だな、俺。"


"笑美が朝ランニングに引っ張り出してくれるっていうのは、なんだかんだいって実にいいことかもしれない。"


"楽しみなことなんだ。"

stop ambient fadeout 2.0

window hide






label jp_A40:

play ambient sfx_crowd_outdoors fadein 0.3
play music music_soothing fadein 0.5

scene bg school_dormext_full
show crowd
with locationskip


"体を押すように正面のドアを抜け外に出ると、陽気な喧騒が俺を迎える。"


"昨日から今朝までのあいだに、学校の敷地はお祭り会場へと様変わりしていた。"


"正門から校舎にかけての通りにはカラフルな屋台が並んでいる。"


"何人かはまだ色々なものを運んで行ったり来たりしているけど、それ以外のほとんどはリラックスしてカウンターにつき、準備が整っているようだ。"


"今ゆっくりしている生徒たちは、早起きして準備を終わらせていたんだろう。"


"自分は何もしていないことに悪い気がしたが、すぐに思い直した。"


"なんだかんだで、俺はしがない新入りなのだから。"


"すでに外からのお客が学園内を散策している。"


"はしゃぎまくる子供を心配げに追いかける、そんな若い家族がいて……"

"……生徒の中にも両親と一緒の人がいて……"


"……そして老若男女さまざまな人々が、理由はわからないがここにいる。"

play sound sfx_warningbell


"カリヨンが鳴り、学長の甲高い声が拡声器から雑音混じりに学園祭の幕開けを告げる。"


"みんな乗り気ではなさそうだけど、それでも律儀に拍手を返す。"


"学園祭……前の学校には祭らしい行事はまったくなかった。その事を考えると特に、祭なんて古臭い気がする。とはいえ、祭には不思議な高揚感がある。"


"4ヶ月間もずっとベッドで寝て過ごしていたとはいえ、忙しく過ごしたこの一週間の後に、休日とは実にありがたいものだ。"


"俺は病院にいる間、数学の授業にでも出られればと思っていたのを思い出す。"


"ついこの間先生が説明してくれたのに、学園祭のプログラムを忘れてしまった。"


"俺も他のクラスの出し物を見ながら辺りを散策しようと思い、寮の階段を降りていく。しかし、俺は階段の下に目をとめる。"

stop ambient fadeout 1.0

hide crowd
show rin relaxed_boredom at tworight
with Dissolve(2.0)


"何人かの人が琳の壁画を見物している。その制作者は脇で壁にもたれかかってくつろいでいる。とても退屈そうで、少し元気がなさそうに見える。"


hi "おはよう"

show rin relaxed_surprised
with charachange


rin "やあ"


hi "調子はどうだ？"

show rin relaxed_nonchalant
with charachange


rin "ん、別に"


rin "動けなくて"


hi "動けないって？"


rin "歩けないの。昨日のせいで足が言うこと聞かなくてさ"


hi "痛むのか？"

show rin relaxed_sleepy
with charachange


rin "わかんない、たぶん"


"壁画の作業は琳が言っている以上に大きな負担だったんだろう。俺はてっきり、ただの筋肉痛だと思っていた。もっと詳しく聞こうと思ったけど、琳はすぐに話題を切り替えてしまう。"

show rin basic_awayabsent
with charachange


rin "先生のお友達、来たよ"

show rin basic_absent
with charachange


rin "そんで町に下りていったよ、お昼食べに。私も誘われたけど。足が痛くてよかった"


hi "でも、動けなくてここに座ってるんだろ？　どこも良くないじゃないか"

show rin basic_lucid
with charachange


rin "歩けるようになるまで待つよ。考えてみれば、そのうち治るはずだよね"


rin "先生、私がちゃんと描き終えてて嬉しそうだった"


hi "そりゃそうだろう"

show rin basic_awayabsent
with charachange

stop music fadeout 5.0


rin "でも、本当にこれ、完成してるのかなあって"


hi "ん？"

show rin basic_deadpanupset
with charachange


rin "昨日、全部描き終わったと思ったんだ。でも今見るとなんだか自信持てなくて。もっと細かいところ描かないと。多分、きっと。どこで終わりにするか決めるのって難しいんだ"


"未完成だったとしても、この白日の下では実にすばらしいものに見えるけど。"

play music music_another fadein 2.0

scene bg mural at Transform(xalign=0.05)
with Dissolve(2.0)


"主に絵を構成しているのは、何度も何度も繰り返し描かれている、人間のさまざまなパーツだ。どれも著しく奇妙な形で、そしてほとんどが醜く変貌している。"


"一見、粗く見える。構図は適当で、塗り方もごく基本的なように見える。だけど、一つ一つのパーツに念入りな考慮と注意が注がれている。"

show bg mural at Transform(xalign=0.25)
with charamove


hi "これは頭から蛙が伸びてるのか？"


rin "それ、金魚"

show bg mural at Transform(xalign=0.45)
with charamove


hi "これは？"


rin "なんでもない"

show bg mural at Slide(0.45,0.45,.6,0.6,25.0, time_warp=acdc_warp)
with None


"それにしても……"


"この壁は幅が広く、壁画全体を見渡すには首を動かし回さないといけない。"


"一枚の絵としては考えるのは難しい。描かれているものはそれぞれ噛み合っているようには見えないからだ。でも、それらがある種全体像を構成している。"


"抽象的すぎて何を表現しているのかまるでわからない。でもいい絵だ。それだけでも十分だ。"


"俺は琳の隣に腰を下ろし、同じように壁にもたれかかる。"


"次々と来客が校内に入ってきて、学園祭の陽気な騒がしさは大きくなる一方だ。"


"多くの出し物が集まる本館や中庭の周囲にある屋台から寮は離れているため、ここに人はあまり来ていない。"

show rin negative_spaciness_close at offscreenright
with None

show rin negative_spaciness_close at tworight
show bg mural at Transform(xalign=0.6)
with MoveTransition(3.0, factory=MoveFactory(time_warp=_ease_time_warp))


"琳の表情に退屈が表れ始めている。まるで琳が周囲の喧騒から隔てられているかのように。"


"彼女はずっと黙ったままだ。まだ痛むのだろうか？"


hi "それで、先生のお友達ってのは壁画のこと、なんて言ってた？"

show rin basic_deadpannormal_close at tworight
with Dissolve(1.5)


"俺が問いかけると、琳は白昼夢から我に返る。けだるそうに顔をこっちに向ける。"

show rin basic_deadpan_close
with charachange


rin "よくわからない"

show rin basic_awayabsent_close
with charachange


rin "気に入ってたのかな？　ホントに気に入ってたのかもね"


hi "お前はどうなんだ？　絵には満足してるのか？　俺も手伝いみたいなことはしたからさ。お前が嬉しくないってのも嫌だぞ"


"琳は下唇を噛み、首を傾げる。"

show rin negative_sad_close
with charachange


rin "ちゃんと出来てはいると思うよ。良くも悪くもない感じ。ただ……それだけかな。きっと、うまく何も考えずにいられたんだろうね"


hi "もう一つ訊いていいか？　これは本当は何を表現してるんだ？　昨日、考えてたんだ。お前が、何も表現してない、なんて言ってたとき"


hi "でもそんなんじゃ理屈に合わないだろ？　何も考えないでものを作るなんてできるはずない、美術だってそうだ"

show rin negative_annoyed_close
with charachange


"琳はしかめ面をして雲を仰ぐ。"


rin "知らないよ。私は説明するの得意じゃないんだ。これはただの壁画。特別なことなんて何もないよ。前も言ったよね"


"俺の質問にイラついているようだ。"


rin "自分で何を描きたいかわからなかった。だからただの壁画を描いたの"


rin "これは壁画を表した壁画ってわけ"

show rin basic_deadpancontemplation_close
with charachange

rin "待って、いい言い方が見つかった。これは『自分で自分を表現してる』んだよ"

show rin basic_deadpannormal_close
with charachange


rin "だから……この絵は最高に壁画らしいんだ。少なくとも私のできる範囲では。君がこの絵に他に何か意味があるって言うなら、それもそうなんじゃない"


"何を言っているんだ。"


"他の意味……自分の口角が上がって、少し困ったような笑顔になっていくのを感じる。"

stop music fadeout 5.0

scene mural all
with flash


"俺は『美術』という言葉を本当に深い意味で理解したことはなかった。"


"美術は発想や思考をやりとりする手段でしかない、という基本的なことはわかる。"

scene bg mural at Slide(1.0,1.0,0.6,0.6,40.0, time_warp=acdc_warp)
with flash


"でも、美術作品をどう理解すべきか、作り手の主張をどうやって推し測ればいいのか、そんなことを学んだことは一度もなかった。"


"別にそれが特別な技術じゃないことはわかってる。でもどういうわけか、俺の脳は美術作品を目に見えるもの以外のことと関連づけることができない。俺の目に見えるのはただの壁画だけだ。"


"そんな技能があれば尊敬する。たしかに、俺でも悪い作品とそれなりの作品、それなりの作品と良い作品の違いぐらいならわかる。"


"でも俺にできるのはそこまでだ。だから俺にこの作品の意図を求めないでくれ、琳。"


"琳の答えのおかげで、俺もこれ以上絵のことを聞くのをためらってしまう。"


hi "ところで、歩けるようになったらどうするんだ？"

play music music_happiness fadein 4.0

scene bg mural at Transform(xalign=0.6)
show rin negative_spaciness_close at tworight
with flash


rin "別に"


hi "何もしないのか？　せっかくの学園祭なのに、遊びにいかないのか？"

show rin basic_absent_close
with charachange


rin "このままでいい"


hi "あんまり人付き合いは好きじゃないんだろ、違うか？"


"自分に言っているような気がした。俺自身、取り立てて言うほど学園祭を楽しんでいない。ちょっとどんな様子かと気になっているだけだ。"


"琳の答えは予想通りだった。"

show rin basic_awayabsent_close
with charachange


rin "そうだよ"


hi "俺もそうみたいだけどな"

show rin basic_deadpan_close
with charachange


rin "行きたかったら行っていいよ"


hi "わかってる。でもお前に付き合うよ。俺もまだこういうことには慣れてないし、気楽にしてて問題ないさ"


hi "まあ一人になりたいって言うなら、もう行くけど"

show rin basic_deadpannormal_close
with charachange


rin "ここにいてくれないかな"


"言葉でぐるぐる巻きになるようなやり取りが、ようやく落ち着いた。琳がそう言ってくれたことに妙に嬉しくなってここに残る。"


"俺も琳がそばにいると気分がいい。琳の持つ奇妙な、でも暖かい静かな雰囲気は沈黙も心地よいものにしてくれる。俺はそれが本当に気に入っている。"


"俺たちは行きかう人々を眺める。俺たちは沈黙し、ほかの人達は楽しそうにお喋りをしている。"


"生徒たちが自室を見せるために家族を連れている。俺たちとその後ろの壁画の横を通り過ぎる。壁画をちらちらと何度か見ていたかも知れない。"


"俺は彼らから隣の連れ合いに注意を移して、謎めいた読めない表情の奥にあるものを見つけようとする。"

show rin basic_awayabsent_close
with charachange

show rin basic_absent_close
with charachange

show rin basic_awayabsent_close
with charachange


"琳の眼は通りすがる人々を追ってせわしなく動く。"


"誰かが壁画を前に足を止めてくれるのを待っているのだろうか。まさか密かに感想を聞けることに期待してるのだろうか？"


"誰も、この絵を描いたのが琳だなんては思わないだろう。俺たちはこうして浮浪者のように座り込んでいるだけなんだから。それに、琳には腕がない。"


"ひょっとしたら、これが琳なりのアピールなんだろうか。そっけないものだ。"


"さらに多くの人が通り、ときには壁画を指差し何かを話すけど聞き取れない。誰かがつま先にかき氷をこぼした。お気の毒に。"


hi "みんな気に入ってるみたいだな"


"空気がダレてきたところで、何か話題にと思ってそう言ってみる。"


"琳はすぐには返事をしない。でも必要に迫られて琳が口を開く時に、ときどき反応が遅くなるのにはもう慣れている。"
"まるで琳が慎重に言葉を選んでいるかのようだけど、実際に出てくる言葉が意味不明なことを考えると、とてもそうは思えない。"

show rin basic_lucid_close
with charachange


rin "何も考えずに見ることのできる絵にしたかったんだ。でもそんなのナンセンスだって気づいたから、あれこれ混ぜこんだような絵になったわけ"

show rin negative_spaciness_close
with charachange


rin "遠くから見るとさ、誰かが蝶の群れを吐きつけたような絵だよ。いじわるな生徒会長さんは嫌がるだろうね……そういう言い方でいいのかな？"


hi "言い方？　何の？"

show rin basic_deadpannormal_close
with charachange


rin "だからそういう。一羽以上の蝶って他に言い方ある？"


hi "蝶？"

show rin basic_deadpanupset_close
with charachange


rin "じゃなくて。『群れ』とか『集まり』とか『大量』とか"


hi "ああ……さぁね。『大群』とか？"


rin "きっと人って蝶みたいに集まるんだね"

show rin negative_confused_close
with charachange


"琳は驚くほど不満そうに壁画を見る。"


rin "真ん中の辺り、もう少し何とかならないかなあ"

show rin negative_annoyed_close
with charachange


rin "いつもは中間色が好きなんだけど、これはお尻が痛むなあ。いや、そのままの意味じゃないけど……でもほんとに痛くなっちゃったんだよね。やっぱりそのままの意味だったみたい"


hi "そう自分を悪く言うなよ"

show rin basic_deadpannormal_close
with charachange


"琳はおもしろおかしそうに俺を見るけど、話すのはやめる。"

scene bg school_dormext_full at bgright
with locationchange


"この辺で、俺はここを立ち去って、もっと建設的な日曜を過ごしたほうがいいんじゃないか、と考え始める。"


"これじゃ社会不適合の極みだ。丸一日フリーで、目と鼻の先では学園祭をやってて、それで俺は何をしてるんだ？"


"琳とこの場にいる……２人の見物人が、ただの見物人であることを嘆く以外にすることもなくこの場にいる。"


"そのみじめさを理解しながらも、俺は何もしない。楽しい一日のために立ち上がりも、歩き出しもしない。"

stop music fadeout 5.0

play sound sfx_rustling


centered "*ごそごそ　もぞもぞ*"


"……"


centered "*もじもじ*"

play sound sfx_rustling


centered "*ごそごそ*"


"……"

scene bg mural at Transform(xalign=0.6)
show rin negative_annoyed_close at tworight
with locationchange


"琳は落ち着きなく体をもぞもぞと動かす。片方の足をもう片方の膝の上で、休みなく揺らしている。"


"とても苛立った表情が顔に浮かんでいる。"


hi "どうかしたのか？"

show rin basic_deadpanupset_close
with charachange


rin "ん、別に。うん"

scene bg school_dormext_full at bgright
show rin basic_deadpanupset:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.8
    easein 0.5 yanchor 1.0
with locationchange


"琳は突然飛び上がる。驚いた、まだ動けないのかと思っていたけど、どうやらそうでもなかったようだ。"

show rin negative_confused at tworight
with charachange


rin "笑美か誰か探してこないと。ちょっと手伝って欲しいことがあるんだ"


hi "俺が手伝うよ"

show rin relaxed_nonchalant
with charachange


rin "ん、いいよ。何かあるといけないから、一人はここにいないと"


hi "馬鹿なこと言うなよ。俺が来てからずっと面白いこと１つなかったじゃないか、かき氷を落っことしたやつがいただけ。だから手伝わせてくれよ、俺も暇なんだ"


hi "それで、なんなんだ？"

show rin negative_annoyed
with charachange


"琳の唇が水平線のように平たく閉じられる。"

show rin basic_lucid
with charachange


"そして目をつむり、深く息をつく。"


"再び開かれたその目は、恐ろしいほど険しく、俺は面食らってしまう。"

play music music_rin fadein 0.5

show rin negative_angry
with charachange


rin "久夫……君がこんなこと聞きたいかどうかはわからないけど、でも関係ない、聞きたくなかったとしても君のせいだからね"


rin "生理が来たからそれで手伝いが欲しいの。でも君と私は、まだ女子トイレまでご一緒して下着を下ろしてもらうほどの仲じゃないと思うんだ。君が手伝うと言ってくれてもね"


rin "そういうわけだから、君にここにいてもらって、私は笑美を探しにいきたいの"


"上昇気流のように、俺の頬に血が上りつめて来ながらも、俺は必死に答えを返そうとした。"
"でも俺の頭に浮かんだのは、出会ってからの４日間、琳の口から聞いた言葉の中で、今のが一番わかりやすかったな、ということだけだった。"


hi "う……うん"

hide rin
with charaexit

stop music fadeout 4.0


"俺は琳と目を合わせないように、誰かの親を見ているふりをして顔をそむける。"


"視界の隅に、琳がさっさと振り向いて去っていくのが見えた。"


"穴があったら入りたい気分だ。"


"琳はいつ帰ってくるだろう……もう戻ってこないんじゃないだろうか。"

scene bg mural at Transform(xalign=0.6)
with shorttimeskip

play music music_dreamy fadein 3.0


"やがて琳はどこからともなく戻ってくると、俺の横の、元いたところに腰を下ろす。"

show rin basic_deadpannormal_close at Slide(0.8,0.5,0.7,0.5,1.0)
with Dissolve(1.0)


rin "ただいま"


"こともなげに言う。俺の失態などなかったかのように。俺も早く忘れてしまいたかったので、口をつぐんでおく。"

scene bg mural_ss at Transform(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic behind rin:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.85
    easein 3.0 xpos 0.8 yanchor 0.9
with Dissolve(3.0)


"時間がゆっくりと過ぎていく。日の光が本校舎の向こうから洩れ、俺の目に直に降り注ぐ。だけど俺はその場から動かず、目を細めるだけだ。"


"間もなく、目をわずかに開けているのも辛くなってくる。こめかみが痛み始める。"


hi "頭が痛くなってきた。今日は頭が痛くなる日だ。そういうのってあると思うか？"

show rin basic_deadpan_close_ss
with charachange


rin "お腹でも空いたの？"


hi "頭痛とは関係ないだろ？"

show rin basic_deadpansurprised_close_ss
with charachange


rin "そうだね。私がお腹空いたから訊いてみたの"


"……"


"琳のノーテンキさの前では、俺の苛立ちも馬鹿馬鹿しく思える。そしていつの間にか口元も緩んでいる。"


hi "実は俺もそうだ"


hi "何か食べる物でも買ってくるよ。何がいい？　おごるよ"

show rin basic_lucid_close_ss
with charachange


rin "なんでもいいよ"

show rin basic_deadpannormal_close_ss
with shorttimeskip



"食べ物を調達して戻り、一人分を琳に渡す。残りは俺の分だ。俺たちは言葉も交わさず食事に専念する。"


show rin negative_spaciness_close_ss
show rin_shadow negative at Transform(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9)
with charachange


"琳は口元にフォークをぶら下げたまま、上を見上げる。"


rin "雲ってなんだろね？　私、雲って空の思考なんじゃないかっていつも思ってた。だって、直接さわれないし"


hi "子供のころにそう思ってたのか？"


rin "ううん、先週の話"


rin "たぶん私の思考が時々雲に似てる感じだからじゃない？　もこもこで、白くて、ゆーっくりでさ"


rin "私の心に空が広がってるみたいに。私の心が空そのものみたいに"


hi "心の空？"


rin "目を閉じて空のことを考えてみなよ。他のことなんか考えられなくなるよ"

scene black
with shuteye


"やってみた。確かにそうなった。これは魔法か？"

scene bg mural_ss at Transform(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic behind rin at Transform(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9)
with openeye


"目を開けると、琳は俺をしげしげと眺めている。その間、琳が何も言わないのが気になり、俺はそっぽを向く。"

scene bg misc_sky_ss at Fullpan(20.0)
with locationchange


hi "雲は水分だ。蒸発した水"


hi "地球上のほとんどの水は、いつかは蒸発して雲の一部になるんだろ"


hi "お前から出た汗や涙、血も雲になるんだ。体のほかの水分もみんな。お前が死んだ後もいつかはそうなる。時間はかかるかもしれないけどな"


rin "私より説明、上手だね"


hi "事実だからな"


rin "違いないね"



"俺は食事が冷めないうちに食べ続ける。"


"太陽が寮の上空をまたぎ、壁に煌びやかな影が落ちる。"


"だけど、午後という時間はすでに夕方に差し掛かかり、俺たちの昼飯は夕飯になりつつある。待てよ、こういう時間にとる食事はなんて言えばいいんだ？"


"そうこう考えている間にも、食欲は満たされていく。もう長いこと何も口にしていなかった。"


"……"


"すっかり食べ終えると、俺は満足げにため息をつく。一方、琳はまだ食べ終えていないけど、もう満腹のようだ。"


"壁にもたれかかり、息を吸い込む。見物人はまばらになってきていたけど、学園祭はまだ続いている。みんなそれぞれ楽しんでいるようだ。"


"そりゃ楽しまない理由がない。今日は暑いけど、快適でいられないほど暑すぎはしない。暖かくて、完璧な夏の日と言える。"


"もうすぐ日が落ちる。時間の流れが速かったな。"

scene bg mural_ss at Transform(xalign=0.6)
show rin basic_deadpannormal_close_ss at tworight
show rin_shadow basic behind rin at Transform(xpos=0.8,ypos=1.0,xanchor=0.5,yanchor=0.9)
with locationchange


hi "もうかれこれ６時間はここに座ってるな"

show rin basic_deadpansurprised_close_ss
with charachange


rin "そうだね"

show rin basic_deadpancontemplation_close_ss
with charachange


rin "他にしたいことないの？"


hi "いや、別に"

show rin basic_deadpannormal_close_ss
with charachange


rin "私も"

show rin basic_lucid_close_ss
with charachange


"琳は姿勢を直して壁に寄りかかる。俺もそれにならって、体をくつろがせる。"


"それからの数分間、俺たちは会話もなしにそこに座り続けた。"


"琳が今どんな気分か感じ取ろうと、琳の様子や、体の緊張具合や、顔に浮かぶ僅かな表情に注意する。無駄なことだった。いつもながらに内心が読めない。"

$ renpy.music.set_volume(0.5, 0.0, "ambient")
play music sfx_crowd_outdoors channel 6 fadein 1.0

scene bg school_dormext_full_ss
show crowd_ss
with locationchange


"行き交う人が増えていく。みんな楽しそうに言葉を交わしている。本当に壁画に注目する人は少ない。俺たちに目を向ける人はもっと少ない。"


"俺はぼんやりと道端の小石をいじる。"


"何かすること自体を目的に何かをするなんて、怠惰もいいところだ。"


"次第に太陽は、空を水平線近くから黄金やオレンジ、赤に染めながら、並木の向こうに落ちていく。日没も近い。"


"食べ過ぎて腹の中に鉛が詰まっているみたいだ。でもレンガの壁に寄りかかると驚くほど気分が良い。"


"強い眠気に抗おうとするけど、耐えきれない。"

scene black
with shuteye

stop music fadeout 4.0
$ renpy.music.stop(channel=6,fadeout=2.0)

with Pause(4)
$ renpy.music.set_volume(1.0, 0.2, "ambient")
play ambient sfx_fireworks fadein 1.0

scene bg misc_sky_ni
with openeye


"俺はハッとして目を覚ます。"


"低い轟音が学園中に響きわたっている。輝く火花の残像が星のように視界を駆ける。"


"運動場のほうから何かが空に昇っていく。"


"炎が尾を引き、轟音とともに弾け、赤や黄色が学校上空を照らす。"

show fireworks
with dissolve


"花火だ。"


"夜空のキャンバスに突然瞬いた閃光で俺は目が覚めて、辺りがすっかり真っ暗になっていることに気づく。"


"俺はどれほど眠っていたのだろう？　まだ意識が朦朧としている上に、右腕の感覚がない。"


"腕を曲げようとして、その理由に気づく。"

play music music_twinkle fadein 1.0

show rin basic_lucid_close_ni:
    xpos 1.0 ypos 1.1 xanchor 0.5 yanchor 1.0
    easein 1.0 xpos 0.9
with Dissolve(1.0)


"琳が俺の肩に大きくもたれかかっている。膝に落っこちそうだ。"


"すっかり眠り込んでいる。花火にも驚かない。"


"彼女の口はかすかに開かれ、目は穏やかにつむられている。その寝顔は無垢な子供のようだ。"


"俺は琳を起こそうとして、あるいは起こせないまでも、琳の体にはさまれている右腕を外そうとして、空いている腕でその体をそっと揺する。"


"琳は顔をひくっと動かし、まぶたをギュッと閉じる。起きまいとしているかのようだ。"

show rin basic_deadpanupset_close_ni at Transform(xpos=0.9, xanchor=0.5, ypos=1.1)
with charachange


"彼女は段々と目を開くが、それも半開きで止まった。花火の光がまつ毛を越えて忍び寄ってくると、琳の緑色の眼にその光が映りこむ。琳は俺を見上げて眉をひそめる。"

show rin basic_deadpan_close_ni
with charachange


rin "もう少し寝かせて……"


"いかにも眠そうな声で、か細くつぶやく様に、むにゃむにゃと言う。"


"今の状況がよくわかっていないみたいだ。"

show rin basic_lucid_close_ni
with charachange


"琳はまた俺に全体重をかけるように寄りかかると、肩に頭を落とす。"


"俺に寄り添いながら快適な姿勢を探すけど、同時に俺は快適とはほど遠い状態になる。"


"琳の暖かい体、腕に当たる穏やかな胸の動き、次第に落ち着きを取り戻す寝息。俺はそれを強烈に、ほとんど痛いくらいに意識する。"


"こいつの寝る才能とか、知り合って１週間も経っていない人間を枕にできる気楽さとか、尊敬せずにはいられないな。"


"打ち上げ花火が１つずつ夜空に舞い上がり、赤や緑、金の花を描き出すと、観衆からワッと歓声が上がる。"


"琳との距離が近すぎて落ち着かないけど、それを意識しないよう努力する。他にどうしようもないじゃないか。もう少し、というのが言葉通りであることを願うばかりだ。"


"次から次へと、夜空に眩い光が一瞬生まれては消え、変幻自在の抽象画を描き出す。"


"俺は花火の轟音と琳の静かな寝息に耳を傾けながら、目覚めたばかりでぼんやりする頭をしゃっきりさせようとする。"


"ありがたいことに、琳の言った『もう少し』は本当に少しだけで、花火が終わる前に琳は眠りから目覚める。"

show rin relaxed_sleepy_close_ni
with charachange


rin "寝てた"

show rin basic_awayabsent_close_ni
with charachange

show rin basic_lucid_close_ni
with charachange

show rin basic_awayabsent_close_ni
with charachange


"とうとう琳はパッチリと眼を開け、何度かまばたきをする。"


hi "お前、俺の上で寝てたんだぞ。２回も"

show rin basic_absent_close_ni
with charachange


rin "イヤだった？"


hi "あ……いや……"

show rin basic_absent_close_ni:
    ease 1.0 ypos 1.0


"どもって要領を得なかったにも関わらず、琳はまっすぐに座り、俺から距離を置く。"


hi "お前、重いぞ"




"もちろん嘘だ。琳には重さなんてないも同然だ。でも俺は嘘でも琳に嫌味を言ってやらなきゃ気が済まなかった。俺の怒るふりに琳はまるで反応しない。琳の関心は空の、花火の閃光に惹きつけられている。"


show rin negative_spaciness_close_ni at Transform(xpos=0.9, xanchor=0.5)
with charachange


"色とりどりの爆発に琳はすっかり魅了されたようだ。"


"また腕に血がめぐり始め、痺れるような感覚が腕を上下する。うっとうしいけど、めまいから立ち直るには丁度いい。"


"さらに打ち上げ花火が舞い上がり、明るい光が雲に反射する。"


"俺たちは花火の光景に心を奪われ、並木の枝葉越しにそれをじっと見つめる。"


"もう２、３メートルほど位置をずらせば、もっとよく見えるだろう。けど俺も琳も、そんなことを言い出すことさえしない。"

show rin negative_worried_close_ni
with charachange


rin "私、花火好きなんだ。見てて悲しくなることもあるけどね。きっと花火って自分を見てもらいたいんだよ。だからあんなに音が大きくて明るいんだ"
rin "でも誰かが見てくれるころには、もう消えちゃう"

show rin negative_sad_close_ni
with charachange


rin "まるでみんな現実じゃなかったみたいに"


"……"


hi "いや、現実だよ。まちがいなく"


hi "これはみんな……現実なんだ。わかるだろ？"


hi "考えてみれば、どんなものだって長くは続かない。俺やお前の命だって、長い歴史の中じゃほんの一瞬でしかない。花火と同じで。『パーン！』それでおしまいさ"


hi "でも、俺たちはここにいる。そうだろ？"


"そうだ、これが現実だ。俺の隣に座る琳、花火の轟音、広く限りない空。みんな確かに存在している。たとえ、いずれは消えてしまうとしても。"


"自分の中に温かいものを感じる。琳がこんなにも近くにいるからなのか、それともこれが生きている実感というものなのだろうか。"

show rin negative_spaciness_close_ni
with charachange


rin "なんて言えばいいかわからない"


hi "いいって。ただの独り言だ"


hi "でもあれだよな、花火ってのは綺麗だけどさ……結局ほんの一瞬の煌きのために、こんなに金をかけるのもバカげた話だよな？"

show rin negative_sad_close_ni at Slide(0.9,0.5,0.7,0.5,1.0)
with None

show rin relaxed_doubt_close_ni at Slide(0.9,0.5,0.7,0.5,1.0)
with Dissolve(1.0)


"琳はまだ打ち上がり続ける花火から勢いよく視線をそらすと、体をのけぞらせて不快そうな目で俺を見る。"


rin "うわ、君がそんな皮肉屋だったとは思わなかった"


hi "皮肉屋とは手厳しいな。俺はどっちかって言えば現実主義者だぞ"

show rin relaxed_surprised_close_ni at tworight
with charachange


rin "現実主義って、皮肉屋が自分のことを指して言う言葉じゃないの？"

stop ambient fadeout 1.0
hide fireworks
with dissolve


"最後の花火が銀や青の光を放ちながら打ち上がると、敷地内は一瞬、奇妙な沈黙に包まれる。そしてまもなく、人々は牛の群れのように正門に向かって移動し始める。"


"灰色の煙の塊が運動場から寮に向かって昇っている。鼻をつく火薬の臭いが服や髪についてしまう気がする。"


hi "あれで終わりか？"

show rin negative_spaciness_close_ni
with charachange


rin "多分ね"

scene bg school_dormext_full_ni
with locationchange


"俺は立ち上がって、背筋を伸ばす。レンガの壁に寄りかかって寝たのはやはり失敗だった。"

show rin negative_spaciness_ni:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.8
    easein 1.0 yanchor 1.0
with Dissolve(1.0)

show rin basic_absent_ni at tworight
with charachange


"琳も立ち上がって俺に向き直る。その疲れた表情に期待混じりの視線が見える。"


"うまく焦点を合わせられなくなっているようだけど、琳は俺をまっすぐ見る。この一週間、琳はそれほど俺をまっすぐ見たりはしなかった気がする。"


hi "えっと……それで……"


"俺は突然、まるで偶然のように、今日一日ずっと琳とデート同然に過ごしていたことに気づく。何もしてなかったけど。"


"でも、デートなんかじゃない……ならどうして頬が熱くなって、言葉に詰まるんだ？"


"琳は俺の言葉を待ち続けているけど、俺はかえって何を言ったらいいかわからない。でも幸運なことに、琳の方から状況を解決してくれる。"

show rin basic_deadpannormal_ni
with charachange


rin "おやすみ、久夫"

hide rin
with charaexit


"琳は俺の頭からつま先までを、見定めるようにもう一度長々と見つめる。そして振り向いて、人ごみの中に消えていく。"

stop music fadeout 7.0


"……"


hi "ああ……おやすみ"


"俺はそこに突っ立って、冷えた夜の空気に答える。"


"はあ。"


"結局、学園祭は俺の予想とは大分かけ離れたものとなった。"


"琳と一緒に、ずっと同じ場所で一日を過ごしてしまった。お互いに示しあったわけでも、何をしようと提案したわけでもないのに。"


"俺も琳も他にするべきこともなかったのだろう。"


"琳の温かみがしばらく俺の体に残っていたけど、それも夜の中に消えていく。"

window hide





label jp_A41b:


scene bg school_gardens
with shorttimeskip

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_crowd_outdoors fadein 0.5
play music music_soothing fadein 0.5


"隣のクラスの屋台でプラスチック皿入りのたこ焼きを買う。薄味なそれをおそるおそるかじりながら、校庭に座って人が通り過ぎていくのを眺める。"


"文句は言うまい。ないよりはマシだ。安かったし。"


"学園のほうを向き、誰もが行き来するのを観察するのは食事中のなかなか良い暇つぶしになる。"

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show bg school_courtyard
show crowd
with locationchange


"両親や祖父母に連れられた幼い子どもたちは、催しの喧噪の中を駆け回る。同伴者を引っぱる手と、色とりどりの特大のおやつを持つ手。"


"ここに来ている人たちが年配の人に偏っていることに気づかずにはいられない。町を歩いているときにも気づいたことだけれど。"



"この町は、ここで育ち、出ていきたくない人たちや、数少なくなった穏やかな場所で残りの人生を過ごしたい、そんな人たちの住む町の一つなんだろう。"


"そのことは、山久学園が伝統をとても重視している理由でもあるんだろうな。"

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene bg school_gardens at Fullpan(8.0)
with locationchange


"別に気にはならない。山久学園の穏やかさと、そんな環境は嫌いじゃない。"


"だけど、この暑さとなると話は別だ。ずっと一か所に座っていたので、このうっとうしい蒸し暑さにどうしても意識が向かってしまう。今は一番暑い時間帯だ。"



"もう行ったほうがいいかも――{w=.5}{nw}"

play sound sfx_warningbell


"うお！"


"立ち上がろうとして、鳴り響くカリヨン・ベルの音に息が止まるほど驚く。近くをぶらついていた数人も同じ反応だった。"


"鐘が鳴り止むと、拡声装置がガーガーと響く。それは明らかにおんぼろで、流れてくる校長の挨拶はほとんど聞き取れない。この挨拶で、すでに大盛り上がりを見せる学園祭は正式に開始される。"


"楽しそうなお年寄りたちの笑顔と、退屈してうんざりした若い付き添いの人たちのしかめっ面は対照的で、とても微笑ましい。一方、生徒たちは挨拶を気にも留めていないらしい。"


"それでも、ようやく挨拶が終わると、皆が礼儀正しく一斉に――熱狂的にとは言えないまでも――拍手を送って、やりかけていたことに戻る。"


"できるだけくつろいで見えるようにポケットに手を入れ、何かすることはないかとさりげなく辺りを見渡す。"


"……辺りの人ごみのせいで、遠くまで見るのはちょっと難しい。"


"俺は実証ずみで信頼できる法則に従うことにする。人だかりのできている所に行けばいい。今だったら、中庭あたりだな。"

play sound sfx_can_clatter


"使用済みの皿をゴミ箱に放り込み、俺は校舎に向かう。"

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_courtyard
show crowd
with locationchange


"校舎回りの屋台の数を見て驚く。かなりのクラスがいくつも屋台を開くことにしたに違いない。"


"まずどこに行こうか決めようとしていると、青い模様の縁で赤い文字の、見覚えのある垂れ幕が目に留まる。"


"リリーの屋台は手始めにうってつけだ。リリーたちがあれだけの作業をやっていたし、どんな様子かも気になる。"

$ renpy.music.set_volume(0.5, 2.0, channel="ambient")

scene bg school_stalls2 at Fullpan(8.0, dir="left")
with locationchange


"近づいていくと、準備に時間がかかった理由がわかってくる。"


"他の屋台の多くに比べ、楽に二倍は幅がある。調理器具もぎっしり敷き詰められ、学園祭の催し物というより野外レストランに近い。"


"前にいた生徒がどんぶりを受け取っていなくなったので、俺はカウンターまで進む。"


"売り子の少女はかなりイライラしているようで、俺に待つように言うとカウンターの下へ姿を消す。"


"機会に乗じて、周りをさっと見渡す。"


"向こうがわで鍋や釜が煮えていて、湯気はあちこちから上がっているようだ。重度視覚障害の学生たちは、３－２の担任らしい人に手伝ってもらいながら材料の荷解きをしている。"


"その中にいるリリーにすぐ気がつく。先生と話しながら、箱と包みをすばやく数え上げている。"


"その表情と、リリーと先生が軽く混乱していることを見るに、下準備に何か問題があったようだ。"


"急にまた売り子の少女が現れて、それ以上見ることはできない。その子は振り返って予備の小銭箱がどこにあるか尋ねる。"


"リリーは少し考えてから、その子とカウンターで入れ替わる。先生は急いでどこかに立ち去っていく。"

stop music fadeout 2.0

show bg school_stalls2 at left
show lilly basic_smileclosed at center
with charaenter


li "すみませんでした、少し手違いがあったものですから。何がよろしいですか？"


"ここに来た理由を思い出すのに少しかかる。カウンターに置かれたメニューを読もうとさっと目をやる。"


hi "ああ、ええと、そうだな……味噌汁？"

show lilly basic_surprised
with charachange


li "あら、久夫さん？"


hi "うん。かなり忙しそうだね"

play music music_ease fadein 6.0

show lilly basic_weaksmile
with charachange


"それを認めるかのように、接客用の表情が消える。"


li "いつの間にか私たちの注文に手違いがあったみたいで。何とかしようとしてはいるんですが、必要な物が半分しかないようなんです"


hi "一人前を少なくすれば何とかなるんじゃない？"

show lilly basic_sad
with charachange


li "あまりやりたくないんですが、それしかないようですね。それに、クラスの半分以上がいないおかげで余計ひどいことになっています"


"俺は実際に屋台を切り盛りしている人の数を見るため、リリーの後ろを覗き込む。"


"８人も居ないだろう。"


hi "だから先生はどこかに行ったのか？"

show lilly basic_weaksmile
with charachange


li "ええ。先生はもう何人か手伝ってくれるクラスメイトをかき集めようとしているんです"


"後ろで足音が聞こえたのでこっそり様子をうかがうと、老夫婦が列に並んでいる。ここでだらだら話し込むのはやめたほうがよさそうだ。"


hi "はい、味噌汁のお金"

show lilly basic_smile
with charachange


li "味噌汁……ああ、そうでした。ただいま"


"お金を渡すと、リリーは振り返って味噌汁を頼む。"

show lilly basic_reminisce
with charachange


"リリーが小銭を手のひらに乗せ、白い指でとても効率よく数えていることに気づく。俺が小銭をぴったり払ったことを確かめると、それを小さい金属の仕切り箱に入れる。"

show lilly basic_smileclosed
with charachange




"味噌汁はすぐに出来上がり、注意深くリリーの手に渡される。リリーは振り返り、それを俺に渡す。"


hi "ありがと。またおわんを返しにくるよ"

show lilly basic_smile
with charachange


li "ありがとうございました、久夫さん。そうだ、もう一つ。華ちゃんは見ましたか？"


hi "華子……いや、今日は見てないなあ。どうして？"

show lilly basic_sad
with charachange


"リリーはかなり落胆した様子で、小さなため息をつく。"


li "そうですか。ただ、華ちゃんは学園祭でどうしているかなと思って"

show lilly basic_weaksmile
with charachange


li "また後で戻られるんですよね？"


hi "ああ。俺も華子のこと、探しておくから"


li "ありがとう、久夫さん"

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg school_courtyard
show crowd
with locationchange


"俺は屋台から離れ、座る場所を見つける。湯気を立てる木のおわんを両手でそっと包む。"


"さっきのたこ焼きと比べると、これはずっといい。ちょっと温め方が足りないかもしれないけど、味がそれを十分補っている。"


"味噌汁をすすっていると、他の皆ほど学園祭に関わっていないことに後ろめたい気がしてしまう。"


"俺がほんの一週間前に学校に転校してきたことを考えれば仕方がない。でもそれはまだ、俺の心に重くのしかかる。"


"そして、この学園祭を来客たちほどには楽しめていない生徒がいる、ということも。"


"食べ終えると、おわんを返すために屋台に向かう。"


"特に並んでいる人もいないようなので、俺はのんびりと歩いて行く。"

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene bg school_stalls2
with locationchange


"どうやら先生の任務はうまくいったようだ。今はかなり大勢の生徒が手伝いに来ていて、だいたいの荷は解かれていた。"


"働いている生徒たちのほとんどは落ち着いて見えるのに、リリーは何だかまだ気を張っているようだ。"





label jp_A41a:


stop music fadeout 4.0


"……そうだ。俺のすべきことがわかった。たった一人だとしても、その一人が学園祭を楽しめるようにしてみせる。"


"おわんをカウンターに置きながら、リリーに声をかける。"

show lilly basic_smile at center
with charaenter


li "あら、久夫さん。返しに来てくれたんですね？"


hi "ああ、これ"

hide lilly
with charaexit


"おわんを手渡すと、リリーは皿洗いらしい人の所へそれを持っていく。さっきここで見なかった人たちだし、遅刻したことへのペナルティなんだろう。"


hi "なあ、リリー？"

show lilly basic_smileclosed at center
with charaenter


"リリーは声を聞きつけ、ピンと頭を上げる。俺がまだいると気づいて、カウンターに戻ってくる。"


hi "もっと学園祭を見たくない？"

play music music_another fadein 0.5

show lilly basic_pout
with charachange


"それはできない、とほおを膨らませる彼女。ちょっとかわいい。いつもの控えめな感じとはまったく逆の仕草だ。"


"リリーが何に腹を立てているのか、気づくまでしばらくかかる。マズイ。"


hi "あー……あの、ごめん……"

show lilly basic_giggle
with charachange


"俺を見てクスクス笑うリリーの、いたずら心が垣間見える。"


li "まだこの学校に慣れていないみたいですね？"


"やられた。"

show lilly basic_reminisce
with charachange


li "まだ……私は屋台に残らないといけないんです。荷解きを終えるのに今までかかってしまったもので"


"この学園祭のためにどれだけがんばってきたかを考えれば、リリーがためらっているのは特に驚くことじゃない。"


hi "そうは言っても、だいぶうまくいき始めてるみたいだけどね。それに、手伝いの人も来てくれてるし"

show lilly basic_surprised
with charachange


"そばを調理中の少年が、ニヤニヤしながら俺たちの方を振り向く。"




"生徒" "リリー、いいから休憩してきなよ。今は俺たちだけでどうにかするからさ"

show lilly basic_displeased
with charachange


li "そう言うのなら、まあ……"

show lilly basic_reminisce
with charachange


li "でも、もし助けがいるときは――"




"生徒" "こっちから君を呼ぶよ。ほらほら、俺たちは大丈夫だから"

hide lilly
with charaexit


"彼が『行け』というようにヘラを振ると、とうとうリリーも抵抗をあきらめる。手探りで屋台の裏まで行って、そこにある自分の白杖を手に取る。"


"まずは華子を探さないといけないだろうな。リリーが心配しているようだし、華子はこんな人ごみの中を一人でぶらついて楽しむタイプじゃないだろう。"


hi "じゃあ、華子を探すってことになるかな。まずどこに行こうか？"

show lilly cane_reminisce at center
with charaenter


li "うーん……"


"二人して黙りこみ、少し考える。"


hi "寮の部屋にいるんじゃないかな？"


li "どうでしょう。華ちゃんは部屋にあまり物を置いていないので、することがないでしょうし"

show lilly cane_satisfied
with charachange


li "……あ！　図書室は？"


"本の虫を探すにはいい場所かもしれない。"


hi "図書室だな。じゃあ、最初に調べてみよう"

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg school_lobby
with locationskip


"漏れ聞こえるくぐもった雑踏の音を除けば、校舎内はかなりひっそりしている。"


"全員に十分なスペースを与えるために、催しは全て外のグラウンドで行うようになっているんだろう。他の学校に比べ、ここの学園祭は明らかに大規模だ。"

show lilly cane_smileclosed at center
with charaenter


li "ここは静かで良いですね"


hi "ああ。外の騒がしさよりよっぽどいいよ"

stop ambient fadeout 3.0

scene bg school_staircase2
with locationchange


"俺たちはゆっくり校舎の１階を通り、２階へ続く階段にたどり着く。"

scene bg school_hallway2
show lilly cane_smileclosed
with locationchange


"いかにリリーがドアや障害物を見越しているか気づく。白杖は持ったまま、廊下の手すりに沿って手を滑らせている。"


hi "学園のことをよくわかってるんだね"

show lilly cane_smile at center
with charaenter


"リリーは笑ってこくりとうなずく。"


li "私は何年もここにいますから、何がどこにあるかくらいはわかります"

show lilly cane_sad
with charachange


li "まだ時々寮で迷うことはあるんですけどね。ここほど長く過ごしていませんし、本館ほど作りがよくないので"


li "私の記憶が確かなら、改築して寮として使われる前は使用されていない建物だったはずです"


"それで男子寮と女子寮の見た目が違う理由がわかった。女子寮の部屋が、寝泊まりする部屋にしては変わって見える理由も。"


"リリーは学園に通い始めたときから寮で暮らしていたんだろうと思っていた。けど、昨日彼女が言ったことを思い出す。"




hi "そうだ、前に言ってたね"


hi "入学したら、ほとんどの生徒は寮に住むのかと思ってたよ。少なくとも、大体の人はそうしてるみたいだし"

show lilly cane_reminisce
with charachange


"リリーの表情が少し読みづらくなる。俺の質問は、明らかにデリケートな点に触れたようだ。"


li "そうですね……どう言えばいいか……"

show lilly cane_weaksmile
with charachange


li "みんな……それぞれの理由があるんですよ"


"きっと、華子は『理由』のある生徒の一人なのだろう。だからこそ、リリーは直接的な答えを避ける。俺自身の状況もまた、同じようなものだ。"


"ここに住むかどうかは、誰もが自分で決めなくてはならないんだろう……俺の場合は、決められてしまった。"


hi "それはまあ、仕方ないんだろうな。それでも、山久自体はいい所みたいだけど"

show lilly cane_smile
with charachange


li "そう言ってくれて良かったです。てっきり嫌いになっているかと"


hi "でも、君はどうなの？"

show lilly cane_surprised
with charachange


"この切り返しに、リリーは驚く。"


li "ずっとここにいましたし、なので……"


hi "そうじゃなくてさ。ただ、晃さんのことで落ち込んでるみたいだったから"

show lilly cane_smileclosed
with charachange


li "う～ん"


hi "その顔はなんなのさ？"

show lilly cane_smile
with charachange


li "姉さんは予約済みですよ。残念でしたね、久夫さん"


"このからかいに呆れたジェスチャーを取った俺を、リリーは見ることもできない。"


hi "なあ、心配してたんだぜ。そんな言い方ってないだろう"

show lilly cane_cheerful
with charachange


"リリーのからかうような微笑みと共に、俺たちは廊下の角を曲がって図書室に入る。"

scene ev hana_library_read_std
with locationskip


"入ってしまうと、華子は簡単に見つかる。他に誰も部屋にいないからだ。"

scene bg school_library
with locationchange


"周りに職員はいないし、いつもの図書室の規則に気を使う必要はないだろう。俺は華子に呼びかける。"


hi "おーい、華子"

show lilly cane_surprised at center
with charaenter


li "華ちゃん、いるんですか？"


"俺たちの声を聞くと、華子の頭が本の陰からひょっこり現れる。たぶん、金曜日に読んでいた本と同じものだ。"

show lilly cane_surprised at twoleft
show bg school_library at bgleft
with charamove
show lilly cane_smile at twoleft
show hanako basic_normal at tworight
with charaenter


ha "中井君に……リリー？"


hi "少し寄ってみようかと思ってね。ちょっとした手助けもあって、リリーは屋台から逃げてきたところなんだ"

show lilly cane_pout
with charachange


li "逃げてきたわけでは……"

show hanako emb_downsmile
show lilly cane_surprised
with charachange


"俺たち二人に少し面食らって、華子はクスクスと笑う。"

show hanako basic_bashful
with charachange


ha "私、ちょうど考えてたんです……リリーは学園祭を楽しんでないんじゃないかって"


hi "まあ、これで一緒に楽しめるだろ？"

show lilly cane_smileclosed
with charachange


"二人は楽しそうにうなずき、俺たちは図書室から学園祭へと向かう。"

stop music fadeout 2.0

scene bg school_stalls1_ni
with shorttimeskip

$ renpy.music.set_volume(0.5,0.0, "ambient")

play ambient sfx_cicadas fadein 0.3


"売り子の少女にいくらか小銭を渡して、紅茶の入った二つのスチロールコップを受け取る。その子は明らかに聴覚障害だ。気持ち大げさに会釈をする。"


"二人を校庭に待たせるんじゃなくて、手伝いを頼むべきだったかもしれない。"


"熱い紅茶のコップを二つ（二人の分）落とさないようにしながら、缶コーヒー（自分用、自動販売機で買った）を持つのは簡単じゃない。"


"とはいえ、巧みな技によって何とかバランスを保ちつつ、リリーと華子が座っておしゃべりをしているベンチまで歩いて行く。"

scene bg school_gardens2_ni
show lilly basic_smileclosed_ni at twoleft
show hanako basic_distant_ni at tworight
with locationchange


"本当にいい場所だ。月明かりだけに照らされ、本会場から少し離れた隠れスポット。"


"日中のひどい暑さと比べると、今のこの場所は十分に涼しい。"


"それが大事だってわけでもない。予定されていたらしい打ち上げ花火を見るために、ほとんどの来場者はより花火に近い場所か、見晴らしのいい丘の高台に移動していた。"

show lilly basic_smile_ni
with charachange


li "お帰りなさい、久夫さん"

show hanako basic_normal_ni
with charachange


"リリーは耳がいい。俺はそれほど近づいていたわけではないし、華子さえ俺に気づいていなかった。"


hi "お待ちどうさま。ごめんインスタントで。もうこれしか残ってなかったんだ"


"華子は俺の右手からコップを恐る恐る受け取る。差し出されたリリーの手に、俺はそっともう片方を手渡す。"

show hanako basic_smile_ni
show lilly basic_smileclosed_ni
with charachange


li "学園祭は楽しめたみたいですね、久夫さん？"


hi "ああ、すごく面白かったよ"


"素直な感想だ。まあ、食べ物はほとんど今ひとつだったかもしれないけど、それでもかなり楽しかった。華子とリリーと一緒だから。"


"実際は、この二人の方が俺より楽しんでいたのかもしれない。リリーと俺のそばだと、他人へ見せる華子の内気な性格は、学園祭を楽しめるぐらいまでに落ち着いていた。"

stop ambient fadeout 1.0

$ renpy.music.set_volume(1.0,0.0, "ambient")

play ambient sfx_fireworks
play music music_twinkle fadein 12.0

scene bg misc_sky_ni
show fireworks
with dissolve


"俺たちが座って飲んでいると、花火の上がる笛のような音が聞こえる。夜空に派手な青いシャワーが降りそそぎ、学園祭が終わりに近いことを告げる。"


"学園のグラウンドに散らばった人ごみから、それをもてはやす興奮した歓声が聞こえる。"


"しばらくの間、華子と俺は頭上に上がる花火を眺め、リリーは目を閉じて幸せそうに音を聞く。"


"赤、緑、黄色、星形、円形模様、あらゆる形や色が、次から次へと辺りを満たし、空を舞う。"


"俺が暮らしていた近所のどんな場所にもこんな贅沢な見せ物はなかった。こういった学園祭は都市圏では過去のものだ。"


"こんな光景を、この二人と見る……ここしばらくで一番幸せなことじゃないだろうか。"

scene bg school_gardens2_ni
show lilly basic_weaksmile_ni at twoleft
show hanako basic_distant_ni at tworight
show fireshine
with charachange


li "と……いうことで。とうとう学園祭も終わりですね"


hi "ああ"


"リリーは繊細で、切ないため息をつく。"

show lilly basic_concerned_ni
with charachange


li "きっとまた仕事の多さに不平を言うことになるでしょうけど、やっぱり私たちが次の学園祭の前に卒業してしまうのは残念ですね"

show lilly basic_concerned_close_ni
with characlose


"俺はリリーのそばに行き、そっと肩に手を置く。"


hi "気にするなよ。まだ今年の七夕があるじゃないか"

show lilly basic_smile_close_ni
with charachange


li "そうですね。その時には、行けるといいですね"


"しばし沈黙が続く。聴こえてくるのは花火の散る音だけだ。"


"この二人を見ていると、一緒に町を歩きながらリリーがアドバイスしてくれた言葉を思い出す。"


"『新しい友達を作るというのは素晴らしいことですよ』、か。"


hi "なあ、リリー？"

show lilly basic_smileclosed_close_ni
with charachange


"リリーは聞いていることを示すために、わずかにこっちを向く。華子は頭上に広がる色鮮やかな花火にまだ目が釘付けになっている。"


hi "時々さ、君たち二人と一緒にお茶を飲んでもいいかな？"


"リリーの笑顔は、答えを知るには十分だ。"

show lilly behind_cheerful_close_ni
with charachange


li "ええ、もちろん。久夫さん"

stop music fadeout 2.0
stop ambient fadeout 2.0
window hide




label jp_A42:





scene bg school_stalls2
with None

show lilly basic_reminisce at center
with charaenter


"リリーは全然楽しそうじゃない。でも、彼女が悪いわけじゃない。"


"屋台の問題に加えて、華子のこともまだ気にしているみたいだ。"


"屋台のほうは力になれそうもないから、俺たちの恥ずかしがりな友達のほうをひきうけて、リリーの気を楽にしてやることくらいしか、俺にはできないだろう。"


"おわんをカウンターの上に戻しながら、リリーに声をかける。"


hi "なぁ、リリー、華子のことは大丈夫だよ。俺が見つけて、ついててやるからさ"

show lilly basic_weaksmile
with charachange


"安堵の気持ちが、はっきりとリリーの顔に浮かぶのがわかる。"


li "ありがとう、久夫さん。それと、私のクラスの生徒を見かけたら、ここに戻るよう伝えていただけますか？"


hi "わかったよ。じゃあな。あと、ちゃんと休憩とりなよ"

show lilly basic_smile
with charachange


li "できればそうします。ではまた、久夫さん"

stop music fadeout 10.0
$ renpy.music.set_volume(1.0,1.0, "ambient")

scene bg school_courtyard
show crowd
with locationchange


"リリーを屋台に残して、華子を探しに出発する。"


"リリーにたくさんの客を任せてこの場を離れることには、心苦しさを覚えないでもない。でも、明らかにプレッシャーのかかっている状況だけど、彼女ならきっとベストをつくすんだろうな。"

stop ambient fadeout 0.5

scene bg school_hallway2
show crowd
with locationskip

play ambient sfx_crowd_indoors fadein 0.5


"廊下は、会場中をうろうろ歩き回る来場者たちでごったがえしている。"


"華子はここの近くにはいない。これだけは自信を持って言える。"


"寮には、友達や家族を案内している生徒がいるから、あそこにもいないだろう。"


"自分でもよくわからない直感に従って、俺は人ごみに逆らって進む。"


"ありがたいことに、この学園祭の来場者たちは、普段お祭りで見かける群衆と比べると少しおとなしいみたいだ――ここの生徒のみんなに気を使ってのことなんだろうな。"

stop ambient fadeout 5.0


"人ごみをかき分けながら進んでいくと、すぐに人の数は減っていって、やがて誰一人いなくなる。"

hide crowd
with Dissolve(2.0)


"驚くようなことじゃない。俺が立っているのは図書室の前なんだから。"


"どれだけ熱心な生徒でも、わざわざ学校のこんな場所にまで、誰かを案内したりはしないだろう。"

play music music_happiness fadein 2.0
scene bg school_library
with locationchange


"図書室に入ると、学園祭の喧騒はごく小さな雑音ほどにまで小さくなり、俺はすぐに図書室の後ろの読書エリアへと足を運ぶ。"


"ついたてで仕切られて並ぶ机の向こう側に、ストレートの黒髪に覆われた頭のてっぺんが目に留まる。"


hi "やぁ、華子。ここで会えるんじゃないかって……"

show hanako def_shock:
    xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.9
    easein 0.5 yanchor 1.0
with charaenter


"その頭は、びっくりして少し跳ねると、ついたての上からゆっくりあたりをうかがう。"


ha "ひ、久夫くん？"


hi "よっ。リリーがすごく忙しいんで、代わりに様子を見て来てくれって言われてさ"

show hanako basic_normal at center
with charachange


ha "そ、そうですか。座ります？"


hi "実は、ちょっと腹が減ってるんだ。屋台で食べるもの買ってこないか？"

show hanako defarms_worry
with charachange


ha "あの……わ……私、食事を用意してて……"


"予想できた答えではあるけど、聞いてみてよかった。今日、華子を外に連れていくのは、まず無理だろうから。"


hi "華子たちの喫茶室で食べないか？　ここに来る途中で見たら、誰もいなかったし"


hi "あそこならちょっとした食事も用意できるし、もう少しくつろげるし。どう？"

show hanako cover_distant
with charachange


ha "わ、わかりました。行きましょう"

show hanako basic_distant
with charachange


"華子は本を閉じると、慣れた手つきで丁寧にしまう。"


hi "もういいか？"

show hanako basic_normal
with charachange


ha "う……うん"

stop music fadeout 2.0

scene bg school_hallway2
with locationchange


"俺と華子は並んで、図書室から喫茶室まで歩く。"


"予想通り、周りにはほとんど誰もいない。"


"壁越しに聞こえるざわめきさえなければ、外で大きな学園祭が行われているなんてわからないだろう。"

show hanako emb_downtimid at tworight
with charaenter


"華子は両手でかばんを抱え、文字通り目の前の床を見つめている。"

show hanako emb_downsmile
with charaenter

show hanako emb_downtimid
with charaenter


"ときどき、華子は歩幅を少し乱して、ちょっと短い歩幅で歩いているようだ。"


"最初は特に気にしなかったけど、しょっちゅうそういう歩き方をしていることにすぐ気づく。"


hi "大丈夫か？"

show hanako defarms_worry
with charachange


"華子は急に立ち止まる。"


ha "な、なんですか？"


hi "わかんないんだけど……つまずいてるみたいっていうか……"

play music music_another fadein 0.5

show hanako emb_blushing
with charachange


"華子の頬がピンクに染まり、目線は床へと戻る。"

show hanako emb_downtimid
with charachange


ha "な……なんでもないんです"


hi "あのさ、そんなふうに『なんでもない』って言われたら、もっと聞きたくなるもんだよ"


"答えてくれないんじゃないかと一瞬思う。"


"気にしないことにして、もう一度歩き出そうとする、ちょうどそのとき……"

show hanako emb_emb
with charachange


ha "遊び……なんです"


hi "遊び？"

show hanako emb_downsmile
with charachange


ha "ここの床……わかりますか？"


"おかしな質問だな。他の床と変わったところはない――リノリウムの正方形が形づくるタイルに覆われた床だ。"


"目立つようなものは何もない。"


hi "そりゃ、わかるけど。それがどうかした？"

show hanako emb_downtimid
with charachange


ha "ときどき……近くに誰もいないとき……黒っぽいタイルの上だけを踏んで……"


"説明が続くにつれ、華子の声は次第に小さくなっていき、誰もいない廊下の、耳が痛くなるような静寂の中でも、その声はほとんど聞こえなくなる。"


hi "黒っぽいタイル？"


"華子はもじもじと足を動かして、他よりわずかに黒い色合いのタイルをつま先で指す。"

show hanako emb_downsmile
with charachange


ha "こ、こういうの"


hi "ああ、そういうことか、じゃあこれとかはダメなんだ？"


"俺は近くのタイルを指す。"

show hanako emb_emb
with charachange


ha "う、うん。そんな……そんな感じ"


hi "ああ、なるほどね。この遊び、よくやるの？"

show hanako emb_downsad
with charachange


"華子はかぶりを振る。"


hi "廊下に人がいないときだけ？"

show hanako emb_emb
with charachange


"彼女はうなずく。"


hi "なら、立ち止まっててもしょうがないな。すごく腹減ってきたし"

show hanako emb_smile
with charachange


"彼女はもう一度うなずく。今度はもう少し熱っぽく。"


hi "じゃあ、行こう"

hide hanako
with charaexit

stop music fadeout 5.0


"廊下を歩き出すと、華子が今度は床にあまり気を配っていないのに気づく。"


"俺は思う――どれくらい孤独なら、人はこんな遊びを思い付くんだろう？"


"だけど気がつくと、俺自身も一足一足踏むべきタイルを踏もうとしている。"

play music music_dreamy fadein 2.0

scene bg school_miyagi
with locationchange


"喫茶室の中では、学園祭の喧噪は少し耳につくけど、開いた窓から吹き込む風がそれを埋め合わせてくれる。"


"無意識のうちに、窓辺に歩み寄って大きく深呼吸をする。ときどき俺は、ここの空気が実家と比べてどれほど綺麗かを忘れてしまう。"

show hanako basic_bashful at center
with charaenter


ha "紅茶、いり……いかがですか？"


hi "いただくよ、ありがとう"

hide hanako
with charaexit


"気づいたんだけど、華子と二人きりのときに、彼女が他のところに行きたそうなそぶりを見せないのは初めてだ。"


"窓から向き直って、彼女が紅茶をシンプルなポットに淹れ、皿にサンドイッチを用意してくれている姿を見つめる。"


"前にも華子がこういうことをするのを見たことはあるけど、今度は少し違っている。"


"なんというか……{w}穏やかなんだ。"


"やがて華子は小さなトレイをテーブルに乗せ、カップ２つに紅茶を注いでくれる。"


"淹れたての紅茶の新鮮な香りがそよ風といりまじって、一瞬自分が世界でただ一人の人間のように感じる。"


hi "華子がこの部屋が好きだっていうの、わかる気がする"

show hanako defarms_worry at center
with charaenter


ha "その……どういうことですか？"


hi "つまりさ、外にはたくさん人がいるのに、この中は別の世界みたいだろ"


hi "ここからずっと遠くまで、人っ子一人いないみたいにふるまったっていいわけだ"

show hanako emb_downtimid
with charachange


ha "そ、そうですね"


ha "まるで、世界がこの部屋のことを忘れてしまっているみたいです"

show hanako emb_emb
with charachange


ha "だ、だから、外のことも忘れてしまっていいんです"


"場合によっては、そういう考えが魅力的に感じられることもあるだろう。"


"俺の知るかぎり、昔からあるようないじめは、この学校には存在しない。"


"といっても、華子に話しかけた人を、リリーの他には一人も見たことがない。"


"世界から無視される人にとって、世界の存在を忘れることのできる場所は、特別な魅力があるはずだ。"


hi "それ、一理あるな。この部屋が、なんていうか完全な自由を与えてくれるって感じか"

show hanako emb_smile
with charachange


ha "う、うん"

show hanako basic_bashful
with charachange


ha "あの……チェスってやりますか？"


hi "チェス？　ちょっとくらいやってるかな"


hi "ってことは、華子も前にやったことがあるんだ？"

show hanako basic_distant
with charachange


ha "少し……"

hide hanako
with charaexit


"華子はそれ以上何も言わずに、戸棚に歩み寄ると、小さなチェスセットを探し出してくる。"


ha "よ……よかったら……"


hi "よし、やろう"


"遮ってしまったけど、華子は気にした風ではない。"

scene bg school_miyagi
show hanako basic_normal_close at center
with shorttimeskip


"俺たちは駒を並べ、やがてポーンを避けえない宿命へ向けて次々と突っ込ませる。"


"俺はじっくり時間をかけて、自分の指し手とその先の展開を検討する。その一方で、久々のチェスに懐かしさを感じてもいる。"


"いっとき、ゲームは長ったらしい消耗戦に陥るものの、俺は華子の防御に隙間を見つけて、そこに一筋の切れ目を入れる。"

show hanako basic_worry_close
with charachange


"数手の後、華子のキングは俺の駒に追い詰められる。"


hi "チェックメイト"


hi "華子もなかなかやるじゃないか"


"素直な褒め言葉だ。華子の腕前はかなりいい。だけどときどき俺は、その読みの隙をつくことができた。"


"駒を一つ取り上げて観察する。比較的新しいけど、その割に使い込まれている。"

show hanako basic_smile_close
with charachange


ha "そ……そんなこと"


hi "リリーもやるのか？"

show hanako def_worry_close
with charachange


"華子の答えがないので、俺はこの質問について考え込む。"


ha "す……少し……"


ha "リ、リリーたち以外の人とチェスをしたの、初めてなんです……一緒にしたことがあるのは、リリーと、それから……"

show hanako emb_downsad_close
with charachange


"それから……？"


"華子はあわてて口をつぐんでしまい、答えはわからないままだ。山久に来る前の知り合いなのかもしれない。"


hi "とにかく、相手してもらえて光栄だよ"

show hanako emb_smile_close
with charachange


ha "その……もう一回やりませんか？"


"まるで、俺に腕を切り落としてほしいとでもいうような頼み方だ。競争心に目覚めたんだろうか？"


hi "よし。けど、今度は手加減抜きで行くぞ……"


"さっきも手加減なんてしてなかったんだけどな。華子は、俺の口調が挑戦的なことに気づいたようだ。"

show hanako emb_downsmile_close
with charachange


ha "わ……私もです……"

stop music fadeout 2.0








label jp_A43:


scene bg school_dormhallway at bgright
show kenji happy at center
with None

stop music fadeout 2.0


"予定だって？　何の予定もない。今になって思えば、バカな話だ。"

"女の子をデートに誘うべきだったか？　とはいえ色々考えてみると、俺がそんな事をやりおおせたとは思えない。まだ越してきて最初の一週間なんだ。"


"色んな人の前で無様な姿をさらして無駄にした一週間だ。この場所に慣れようとしながら一人で勝手につまずいていた。"


"考えてみれば、俺は何かやり遂げただろうか。"


"こんな有様の俺が、誰を誘えていたっていうんだ？"


"ちっ、今日の『デート』には健二を誘うのが一番現実的な選択らしい。"


"最高に気が滅入る。こんなにひどい気分は、女の子に告白されて心臓発作を起こしてしまった時以来だ。"


"どうしようもない。"

play music music_kenji fadein 0.5


hi "よくわからないけど、俺は特にすることもないよ。でも要塞なんてちょっと行き過ぎじゃないか"


hi "本当に外には行きたくないのか？　寮に外部の客が入ってこないってわけでもないんだぞ"

show kenji tsun
with charachange


"そう告げると健二は雷にでも打たれたかのような顔をする。"


ke "ちっ、そうかもな。ここも今日は安全じゃない"


ke "他の隠れ場所を探さないとな"


"健二はしばらく押し黙り、考え込む。"

show kenji neutral
with charachange


ke "屋上だ"


hi "屋上がなんだよ？"

show kenji happy
with charachange


ke "今日は屋上に隠れるんだ"


ke "絶好の場所だ。誰も上がってきやしない"

show kenji neutral
with charachange


ke "一時間後屋上で会おう。俺は準備がある"

stop music fadeout 1.0

show kenji neutral at Slide(0.5,0.5,0.4,0.5,0.5, time_warp=_ease_out_time_warp)
with None

hide kenji
with charaexit

play sound sfx_doorslam
with vpunch


"ドアのバタンという音に続けて鍵をガチャガチャ閉める音がする。"


"くそ、あいつどうなってるんだ。"


"そしてあいつのイカれぶりに付き合っている自分。考えると本当に憂鬱になる。"


"できそこないになった気分だ。"

play ambient sfx_crowd_outdoors fadein 0.3

scene bg school_courtyard
show crowd
with locationskip


"外へ出ると、雑踏のざわめきが俺を出迎える。"

"学校中が活気に満ちている。"


"あちこちに屋台が並び、その合間を行き交う人の数もかなりのものだ。"


"この学園祭にこんなに沢山の人が来るとは思わなかった。"


"装飾係たちの並ならぬ努力は認めないといけない。本当に見栄えがいい。"



"みんな楽しそうだ。生き生きとした明るく楽しげな雰囲気。"

play music music_rain fadein 1.0


"そう、俺がこんな気分でさえなければ。"


"今は、そんな雰囲気が何よりも不愉快だ。"


"まあ、仕方ないな。俺は最初の考え通り、何か食べることにする。その後は、屋上で健二の企みを見るくらいはしないと。"


"……"

scene bg school_stalls2 at Fullpan(8.0)
with locationchange


"ゆっくりと敷地内を回って屋台を見ながら時間を潰す。もう、どの屋台のゲームもやりたいと思わないけど。"


"派手な色彩に目が疲れ、どんどん気分が悪くなっていく。"


"何を食べたいのかさえ決められない。豊富な品揃えと群がる客を見ても気分は変わらない。"

scene bg school_stalls1 at bgright
with locationchange


"それなりに食べられるものを出していそうな、一番近い屋台に向かって列に並ぶ。"


"麺類の屋台だった。"


"しかも、あまりおいしくなかった。"


"まあ、少なくとも栄養には違いない。食べられるものならそれで十分だ。"

scene bg misc_sky at Fullpan(25.0)
with locationchange


"全然うまくない麺をかき混ぜながら、他の奴らがどうしているか、ぼんやりと考える。"


"静音とミーシャはどこかで指示を出してるに違いない。"


"あいつらは避けたほうが良さそうだ。準備を手伝わなかった俺をそう簡単には許してくれないだろう。"


"笑美はあちこちで騒いでるだろうな。気が滅入るぐらいに元気よく。"


"あいつを見つけるのは無理だろうし、避けるのも無理だろう。だからどうでもいい。"


"リリーは自分のクラスを手伝ってるだろうし、忙しすぎて他のやつの相手をする暇なんてないだろうな。"


"どうせ華子は誰とも話したがらないだろう。一人でいるかリリーを手伝っているか。"


"琳は自分の壁画の前にいるはずだ。興味を持つ人が現れても特に何もしないだろうけど。"


"静けさを求めて琳のところへ行くのが、この中では一番いい選択に思える。だけど芸術なんて見せられても俺の気は晴れないだろう。だからそれもパスだ。"

scene bg school_stalls1 at bgright
with locationchange


"考え込んでいると、いつの間にか麺は綺麗さっぱりなくなっていた。俺の空腹感も。"


"食事の記憶をシャットアウトしたのか、いいことだ。"


"腹は膨れたけど欲求不満なまま、本校舎へと足を向ける。もう一時間が過ぎようとしている。"

play ambient sfx_crowd_indoors fadein 0.3

scene bg school_lobby
show crowd
with locationskip


"人ごみは外より密なぐらいだ。"

scene bg school_hallway3
show crowd
with locationchange


"廊下にいても密度はすでに耐えがたいぐらいで、教室の中がどうなってるかまで考えてみる勇気はない。"

stop ambient fadeout 1.0

scene bg school_staircase1
with locationchange


"階段をのぼり目的地へ向かう。"


"屋上へ。"


"ありがたいことに、屋上のドアは閉まっていなかったが、手書きの標識がある。"

window hide

$ written_note("{size=50}{b}立ち入り禁止{/b}{/size}")

window show


"やなこった。"

scene bg school_roof at bgright
with locationchange


"ここまで来ると祭の喧騒は驚くほど遠くなる。そして、やはり屋上はがらんとしている。"


"フェンスが壊れた場所の近くに、場違いにも毛布の山がある。"

stop music fadeout 3.0


"まてよ……"

play sound sfx_rustling


"あの毛布、今ちょっと動いた？"


"変だな、風もないのに……"


"そっと手を伸ばしてためしにつついてみる。"

play sound sfx_impact
show kenji rage_close:
    alpha 0.0 xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.7
    easein 0.2 yanchor 1.0 alpha 1.0

with vpunch

$ doublespeak(ke, hi, "わああああああああ！")

play music music_comedy fadein 2.0

show kenji rage:
    center alpha 1.0
with charadistant


"驚いて飛びのく。"


ke "誰だ？"


hi "ばか、健二、俺だ"

show kenji tsun at center
with charachange


ke "くそ、脅かすなよ"

hi "で、こんな所まできて何をするんだ？"

show kenji neutral
with charachange


ke "ピクニックをするんだ"


hi "え？"

show kenji happy
with charachange


ke "ああ。毛布もあるし、プレッツェルもあるしウィスキーもある。究極の環境だろ、おい"


hi "ウィスキー？"


hi "お前酒飲むには年齢がちょっと足りないんじゃ"

show kenji tsun
with charachange


ke "俺は２０歳だしな"


hi "……ちがうだろ"

show kenji neutral
with charachange


ke "俺は２０だしお前もそうなんだよ"


hi "ええ？　あほらしいことを"

show kenji tsun
with charachange


ke "２０ってことにすりゃ少なくともお・前・は・得るものがあるだろう。俺はこのウィスキーが飲めるだけだ……"


"健二は支離滅裂なことをほざいているが、つきあってやることにする。"


hi "で、なんでウィスキーなんて持ってるんだ？"

show kenji happy
with charachange


ke "俺の母さんは学園祭に来られなかった。で、代わりに上等なシングルモルトウィスキーを送ってきた"


hi "よく言うよ"


ke "お前もいる？"


hi "……"


"失うものがあるわけじゃない。今日はもう既に最悪の日だ。"


hi "……もちろん"

hide kenji
with charaexit

show bg school_roof at center
with charamove_accel

show kenji happy_close at offscreenleft
with None

show kenji happy_close at twoleft
show bg school_roof at bgleft
with charamove_decel


"二人で毛布の山の上に腰掛ける。健二が引きずって持ってきたらしい。"


"健二はほとんど満杯のウィスキーを一本取り出してよこす。"


hi "グラスも持ってこなかったのかよ"

show kenji tsun_close
with charachange


ke "そんなものは持ってこない。これはロマンチックなお嬢さんのピクニックとは違うんだよ。なくたっていいだろ"

show kenji neutral_close
with charachange


ke "これは男のピクニックだ"


ke "グラスなし"


ke "ナプキンなし"


ke "ウィスキーだけ。真の男の飲み物だ"


hi "はいはい"

show kenji happy_close
with charachange


ke "それとプレッツェルだ"


"俺はウィスキーの瓶をもっとよく見てみる。"


"１２年物、健二が言った通りシングルモルトウィスキーだ。"


"肩をすくめ、ラッパ飲みする。酸でも飲んだかのように、喉が焼けるような感覚がする。でも味は悪くない。"


"頭に突き抜けてくるような感じがする。口の奥に残る後味。さらに一口飲みたくなる。"

show kenji neutral_close
with charachange


ke "ここでフェミニストどもへの反撃策を練って女の悪口でも言おうぜ。ここなら奴らも聞いてない"

show kenji tsun_close
with charachange


ke "ちっ、グラフ持ってくるの忘れた"


"そうだ、一人で『酒飲みゲーム』でもするか。健二が『女の陰謀』に言及するたびに一口飲むんだ。"

$ wdt_off(False)

stop music fadeout 2.0

scene black
with delayblinds


centered "4、5時間後、いや数日後かも :\n{w}(覚えてない)"

play music music_kenji fadein 0.5

scene ev kenji_rooftop
with delayblinds

window show


ke "お前、気にすんなって！　落ち着けってんだよ！　マジ、マジで！"


hi "俺は落ち着いてるっての、うるせえな！"


ke "そう見えないから言ってるんだよ！"

scene ev kenji_rooftop_kenji
with flash


ke "考えてみろよ。家と土地の値段が急に上がり始めたのはいつだ？　女が労働に加わり始めたときだ。それが共働きの核家族を生み出したからだ"


ke "ああそうさ、グラフは忘れちまったけど、俺を信じてくれよ。すべての社会の退廃には女が関わってるんだ"

show ev kenji_rooftop_large:
    crop (288, 376, 800, 600)
    ease 1.0 crop (1024, 260, 800, 600)


hi "そうか。なんか信じがたいな"


"とは言いながらも、健二の言うこと全部前より筋が通ってる気がする。"


"何もかも話が合ってる。健二が酔っぱらうと説明がうまくなるのか、俺が酔っぱらうと理解力が上がるのか、わからないけど。"

show ev kenji_rooftop_large:
    ease 1.0 crop (288, 376, 800, 600)


ke "違うんだよお前、考えろ。考えるんだ！　もっと深い意味を考えろ！"


ke "『まあ、共働きの方が収入も多いし、所有コストとかも充分払えるんじゃないの』なんてみんなが言い出すかもしれないんだぜ"

show ev kenji_rooftop_large:
    ease 1.0 crop (1024, 260, 800, 600)


hi "言いたいことはわかるけど。日本の土地はずっと高かったぞ"

show ev kenji_rooftop_large:
    ease 1.0 crop (288, 376, 800, 600)


ke "……それに工業化が始まるとふつう地価は上がるもんだ……だが違う！"
ke "これは女のせいなんだ！　ていうか、相関関係と因果関係は同じだからな"

show ev kenji_rooftop_large:
    ease 1.0 crop (1024, 260, 800, 600)


hi "相関関係と因果関係は違うと思ってたんだけど。いや、まあいいや、お前が正しいかも"

show ev kenji_rooftop_large:
    ease 1.0 crop (288, 376, 800, 600)


ke "俺はいつだって正しいんだよ。ああ、工業化だって女どもが始めたに違いないぜ。証拠隠蔽のためにな"


ke "どこまで悪魔的なんだやつらは"


ke "ああ、だからみんなくたばっちまえ！"

scene bg school_roof_ni
show kenji rage_ni:
    xpos 0.5 ypos 1.0 xanchor 0.5 yanchor 0.9
    easein 1.0 yanchor 1.0
with locationchange


"立ち上がる健二に感心する。俺はもう立とうとしても立てないだろう。"
"そして健二は馬鹿でかい声で叫びだす。音量という概念を忘れたみたいに。俺は顔をしかめる。耳を覆いたいぐらいだ。"

stop music fadeout 2.0


ke "ああああ、こんな所じゃなくて下で過ごせたらどれだけよかったか……"

ke "だがそうじゃない。いいか、そういう考え方自体が罠なんだ"
ke "チャンスを逃してると思うだろ。でもそっちの道を進んだ先にあるのは絶望だけだ……"

show kenji tsun_ni at center
with charachange

play music music_sadness fadein 1.5


"健二は俺からウィスキーを奪い返すと、天を仰ぎながら自分の口に注ごうとして結果びしょ濡れになる。"

show kenji rage_ni
with charachange


ke "くそお！　見ての通り俺は狙うのが下手なんだ。んで酒の何が悪いって、飲めば飲むほどよけい下手になるんだよ！"

show kenji tsun_ni
with charachange


ke "今日は絶望の日だ"


"健二の声はすぐにささやきくらいに小さくなるけど、話す速度はずっと早くなっている。酒のせいであまりろれつが回っていない。"


"健二は話しながらウィスキーの瓶を振り回し、中身をあちこちにまき散らしている。"


ke "そうだ、俺の人生の中で一番衝撃的だったこと、なんだと思う？"


"健二が二番目に衝撃的だった出来事とやらを話していたのをぼんやりと思い出す。頭に鳥のフンが落ちたって。"


"特に面白い話は期待してないけど、続けてくれと頷く。"

show kenji neutral_ni
with charachange


ke "思いもしないだろうけどな、俺はこの学校に彼女がいたんだ。確か去年のことだ"


ke "驚いただろ？　ほら、俺誰にも話したことないから"


"ああ、健二に彼女がいたなんて驚くさ。急に酒が欲しくなる。健二からウィスキーを奪い取ってがぶ飲みする。"

show kenji tsun_ni
with charachange


ke "そのころは俺もずっと純粋だった、彼女のことも、普通の女とは違ってまともだと思ってた。だがある日、俺たちは……性交渉に及んだんだ"


ke "まあ悪くなかったよ、でも肝心なのはその直後に起きたことだ。妙な、恐ろしいことが起きた"

show kenji tsun_ni at tworight
show bg school_roof_ni at bgleft
with charamove


"健二は目を細めて、乱暴にフェンスにもたれかかる。"


ke "とてつもない疲れと眠気が襲ってきたんだ！　普通じゃないだろ！　一体何だってんだよ？"


ke "というか普通、誰だってテンションが上がって、アドレナリンが出まくるはずの場面だろ。でも俺はすごい勢いで気力減退してたんだ！"


ke "何か不吉なことが起こっている、そう感じたよ"


ke "そうして俺は知ったんだ……女は危険な生き物で、あいつらにだけ使える例のモノで男の生命力を吸い取ってるんだと"


ke "気持ち悪ぃ話だ"

show kenji neutral_ni
with charachange


ke "ああ、お前はまだましだよ……"


"健二は正しかった。本当に今日は絶望の日だ。今の健二の話の意味を考えたくなくて、俺はさらに飲む。"


ke "今や俺は狂った世界で生きる最後の正気の人間だ……他のやつらが気づいた時には戦争が起きてるだろう。男とフェミニズム軍の大戦だ"


ke "問題なのは男がみんな俺の味方になってくれるわけじゃないってことだ……ひでえ話だ。まあ敷居を下げることもできる。どんな男でもいい。だけど母親や姉に育てられたやつはダメだ。それだけは確かだな"

show kenji tsun_ni
with charachange


ke "ふたなり作品に入れ込んでるやつもダメ"


hi "はー……俺からすると戦争とかありそうにない、起こりそうにないっていうか、なんていうか……あんまり起こりそうにない"


"酔いが回ってきたに違いない。"


"ともかく、この日に屋上なんかにいるということに俺はまだ憂鬱だった。"


"他の生徒ほどに熱心には、学園祭を楽しみにしてはいなかったけど、でも。"


"誰かと行けたら楽しかっただろうな。屋上からでも、みんなが楽しんでいそうなのが音でわかった。俺は大事なものを逃しつつあるのかもしれない。"


"一緒に行くような子がいなかったってだけだ。"


"いや、いたのかも。振り返ってみれば、機会はたくさんあった。あったのに俺は逃してしまったんだろう。"


ke "ちくしょう、これは真の絶望だ……最悪なのは、俺の人生には選択肢がないような気が時々するんだ、わかるか？"


ke "何も選べないまま、ただろくでもないことが起きる、みたいな"


ke "全部仕組まれているような。運命……か何か、みたいな。自分の行動に俺自身が全く口出しできないような"

stop music fadeout 0.2

show kenji rage_ni
with vpunch


ke "早く、俺に何か質問しろ！"


hi "あー……"


ke "今すぐ！"


hi "そんなこと言ったって……"

show kenji tsun_ni
with charachange


ke "ほらな？　これがそういうことなんだよ！　くそ！　最悪だ！　ちくしょう！　わかるかお前？　今、運命に逆らって自分で自分の人生を決めようと思っても、そんなチャンスはそもそもありもしないんだ"


ke "ちくしょー、お前、見損なったぞ。今度こそ失望した。このバカやろう"

show kenji tsun_ni:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 1.0
    easeout 0.7 ypos 0.9 yanchor 0.5
with Pause(0.8)

show kenji tsun_ni:
    rotate 0
    easeout 0.7 rotate 90 ypos 1.0 yanchor 0.3

with Pause(.7)


play sound sfx_impact
with vpunch

hide kenji
with None


"健二がくずおれて膝をつくと、その上半身が横に倒れ、屋上の砂利の上に寝転がる形になる。"


hi "おい、大丈夫か？"


ke "大丈夫じゃねえよ、俺が絶望してるのがわからないのか？"


"皮肉っぽい口調だ。"

show kenji neutral_ni:
    xpos 0.7 ypos 1.0 xanchor 0.5 yanchor 0.0
    easein 0.5 ypos 1.0 yanchor 0.7
with Pause(0.5)


"突然健二は起き上がると、ぎこちなく汚れを払い、ウィスキーを求めて俺の方へ手を伸ばす。俺は手渡してやる。"

show kenji tsun_ni at Transform(xpos=0.7, xanchor=0.5, ypos=1.0, yanchor=0.7)
with charachange


ke "なんだよおい？　くそお、お前ほとんど全部飲んじまったじゃねえか。これだよ、俺の人生に選択肢なんてありゃしないんだ……"


ke "俺の人生って、もう一生こんな感じなのかよ？"


hi "いやあ、一生なんてことはまずないと思うぞ"


"何の話だか知らないけど。頭が混乱している。少しでも集中しやすくなればと、俺は起き上がってフェンスにもたれかかる。"

show kenji tsun_ni at center
show bg school_roof_ni at center
with charamove


ke "ああ、わかってる。全力で戦わなきゃいけないんだ。それしか俺たちの生きる道はない"

play music music_one fadein 6.0

show kenji neutral_ni
with charachange


ke "お前いいやつだな"

show kenji happy_ni
with charachange


ke "この兄弟の絆のおかげで、俺はこの暗い時代でもやっていけるんだ"

show kenji neutral_ni
with charachange


ke "じゃあ女でも探すか"


hi "女をガス？　は？"

show kenji neutral_close_ni
with characlose


ke "探す。女をゲットしに行くんだよ。でも今やらないとだめだ。この酒に酔った勢いがなくなる前に"


"健二は激しく身振りする。狂ったようですらある。"

show bg school_roof_ni at Slide(0.5,0.5,0.75,0.75,0.5, time_warp=_ease_time_warp)
show kenji neutral_close_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji neutral_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
show bg school_roof_ni at Slide(0.5,0.5,0.75,0.75,0.5, time_warp=_ease_time_warp)
with charadistant


"俺は一歩後ずさる。"

show kenji neutral_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji neutral_close_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with characlose


"健二が一歩近づく。"

show kenji happy_close_ni
with charachange


ke "どうしたんだよお前？　恋する気分じゃないってのか？"


hi "正直……んな気分じゃない"

show bg school_roof_ni at Slide(0.75,0.75,1.0,1.0,0.5, time_warp=_ease_time_warp)
show kenji happy_close_ni at Slide(0.5,0.5,0.3,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji happy_ni at Slide(0.5,0.5,0.3,0.5,0.5)
show bg school_roof_ni at Slide(0.75,0.75,1.0,1.0,0.5, time_warp=_ease_time_warp)
with charadistant


"俺はもう一歩下がる。"

show kenji happy_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with None

show kenji happy_close_ni at Slide(0.3,0.5,0.5,0.5,0.5, time_warp=_ease_time_warp)
with characlose


"健二がまた一歩近づく。"


"やつはずいと身を乗り出す。不愉快なくらい近い。"


hi "なんだよ、そんな寄りかかるなよ、邪魔だっての"


ke "寄りかかるって何だよ？　おい、フェンスにそんなもたれ方するなよ。危ないぞ"


"俺は健二から逃れようとするけど、平衡感覚が変でうまくいかない。"


"めまいでよろめきながら、フェンスの柱を掴む。でも体重をかけた途端にフェンスが崩れるのを感じる。"


"……まずい。でも酒で頭が混乱して、なぜまずいのかさっぱりわからない。"

show black behind bg
with None

show n_vignette:
    xalign 0.5 yalign 0.5 zoom 4.0
    linear 0.2 zoom 1.2
with Pause(0.2)

show n_vignette:
    zoom 1.2
    linear 8.0 zoom 0.001
show kenji happy_close_ni:
    xalign 0.5 yalign 0.5
    linear 8.0 zoom 0.001
show bg school_roof_ni_crop:
    xalign 0.5 yalign 0.5
    linear 8.0 zoom 0.001


"でも健二の顔は小さくなっていってるみたいで、少し安心する。"


"ずっと小さくなっていく。あっという間に。"

show nightsky rotation
with None


"ちょっと風も出てきたようだ。なんだか体重がなくなったような感じがする。"


"ボーッとする、まるで頭の中が空っぽになったみたい。"


hi "俺……落ちてる……？"


"体が回転して、そこに夜空が浮かび上がる。落下する俺の指先からウィスキーの瓶が離れ、宙に浮いてどこかへ消えていく。"


"ああ、お似合いな終わり方だな……この最悪な、本当に最悪な日には……"

window hide

stop music fadeout 0.1
play sound sfx_crunchydeath

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
