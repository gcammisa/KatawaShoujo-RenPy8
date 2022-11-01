label jp_A31:

scene black
with None

scene bg school_scienceroom
with Dissolve(2.0)

play music music_normal fadein 3.0


"生徒たちが土曜の朝のホームルームのために教室に集まってくる。みんな夜通し作業をしていたのか、疲れが目に表れている。"


"準備期間は残り一日しかないので、それほど驚くことではないだろう。ありがたいことに、今日の授業は半日しかない。それを耐えきれば、残りの時間は俺たちだけのものだ。"

show muto irritated at center
with charaenter


"武藤先生が疲れでふらふらとよろめきながら教室に入ってくる。金曜の夜更かしを満喫しているのは生徒だけではないのだろう。"


"先生は何も言わずに、黒板にページと設問の番号をいくつか走り書きして、自分の机にドスンと座りこむ。"


"彼らしからぬ振る舞いだけど、クラスの誰もそのことをどうこう言おうとはしない。"

play sound sfx_paperruffling

hide muto
with charaexit

stop sound fadeout 6.0


"黙ったまま、みな教科書をめくり勉強にかかる。この雰囲気を壊したくないので、俺も同じようにする。"


"疲労でみんなから社交性がなくなっている。紙をパラパラとめくる音以外には、物音一つない。"


"俺の隣の二つの席が空席なのも、その理由の一つだろう。どういうわけか、ミーシャと静音は欠席している。たぶん学園祭関係の、生徒会の仕事だろう。"


"ミーシャがいないととても静かだ。"


"ミーシャは生まれた時から今のようにがさつなんだろうか。それとも静音がしゃべれない分を『埋め合わせて』いるのか。"

show muto normal at center
with charaenter

stop music fadeout 2.0


mu "中井、ちょっと話いいか？"


"ミーシャのことで頭がいっぱいになっていて、武藤先生が俺のところに来ていることに気づきもしなかった。"


hi "はい……なんですか？"


mu "教室の外で話すほうがいいかもしれないな……"

play sound sfx_dooropen

hide muto
with charaexit


"どうやらいい話ではなさそうだ。だけど俺は立ち上がり、武藤先生について廊下に出て行く。"

play sound sfx_doorclose


label jp_A31b:

scene bg school_hallway3
show muto normal at center
with locationchange




"武藤先生は廊下に立ち、頭をかきながら言いたいことをまとめている。なんなのかわからずに、俺は黙って待つ。"


mu "看護師長からこの前のことを聞いたんだが"


"ああ。そのことか。"


hi "ええと、まあ、心配するようなことじゃないです"

show muto irritated
with charachange


mu "違う。断じて違う。お前の健康を害するものは、それがなんであれ心配すべきことだ"


mu "俺たちは、お前がここでの生活に慣れることができるよう最善を尽くしている。そのために、お前の体の限界や、それをどう乗り越えていくかを考えているんだ"


mu "このことに関してちゃんと言っておかないと、俺の怠慢だということになる"


hi "ああ、はい。わかりました。ごめんなさい"


"武藤先生は落胆し目を閉じる。今の言い方は良くなかったかもしれない。"


mu "どうも反省しているようには聞こえないな。反省したふりをしたいなら好きにすればいいさ。だけどな、ここは普通の学校じゃないんだ"


mu "お前を含めた生徒みんなが、同世代の学生と同じ水準の教育を受けられるように、たくさんの人が時間と労力とお金を費やしている"


mu "アドバイスを、それも医師のアドバイスを無視して、その全てを無駄遣いするような真似は全くのわがままだ"


"これは武藤先生の本心なのだろうか。それとも、生徒に罪悪感を抱かせ、『正しい』ことをさせるために何度もやってきた演技なのだろうか。どちらにせよ、それは効いている。"


hi "わかりました。俺には初めてのことばかりで、すみません。もう自分の限界はわかったし、これからは無理はしません"

show muto smile
with charachange


"俺がちゃんと理解したことに満足して、武藤先生は少し気が楽になったようだ。"



label jp_A31c:

scene bg school_hallway3
show muto normal at center
with locationchange




"武藤先生は廊下に立ち、頭をかきながら言いたいことをまとめている。なんなのかわからずに、俺は黙って待つ。"


mu "で、どうだ？"


hi "どう？"


"武藤先生の話はちょっとわかりにくいとは思っていたけど、これは度が過ぎてる。"

show muto irritated
with charachange


mu "ほら、あれだ。もう一週間経って落ちついただろう。で、どうなんだ？"


hi "えーと、順調だと思いますよ"

show muto normal
with charachange


mu "そうか。それとどうなんだ、お前自身の……体調は？"


"『体調』という前の間はすこし余計な気がした。"


hi "今のところは何も問題ないです"

show muto smile
with charachange


"安堵のゆらめきが武藤先生の顔をよぎる。"


mu "そうか、それは良かった。ナースが少し心配してたからな。お前は無理しすぎてるんじゃないか、と"


mu "彼の都合が悪いときは、代わりに様子を見ておいてくれと頼まれたんだ"


hi "なるほど……"

show muto normal
with charachange


mu "あまり調子に乗って、羽目を外さないでくれよ。俺たちはお前が普通の学校と同じ水準の教育を受けられるよう努力はしているが、お前の体にも限界があることは自覚してもらわないといけない"


mu "お前がその限界を理解することと、その中でお前のポテンシャルを最大限に伸ばすことが、俺たちの目標なんだ。わかるか？"


hi "とりあえずは。というか、何も馬鹿なことをするつもりはありません"

show muto smile
with charachange


mu "まあ、最初はそれでいいだろう"





label jp_A31d:

show muto normal
with charachange

play music music_normal fadein 3.0


mu "じゃあ次の質問だ。勉強のほうはどんな具合だ？　しばらく入院していたのはわかっている。授業はそれほど進みすぎていないよな？"


hi "そう思います。入院していたときも勉強してましたし、そんなに大変じゃないです"

show muto irritated
with charachange


"先生はそれを聞くと、あごを叩いて眉をつり上げる。"


mu "そうか……学ぶことの大切さを理解している生徒は、まだこの世に存在しているようだな……"


"それは言いすぎだと思う。俺を生かすためのあのつまらない監獄の中で、暇つぶしをしなければやっていけなかったというだけだ。"


hi "ええ、まあ。こういうことに遅れないようにしないといけないですから。ですよね？"

show muto smile
with charachange


mu "まさにその通りだ。この世界では一歩間違えると置いていかれてしまう、だろう？"


hi "えーと、はい。そうはなりたくないです"

show muto normal
with charachange


mu "そう、まったくそうだ。毎週、新しい科学的発見がある。そのほとんどは普通の人間にとってなんの意味もない。だがな、そのどれもが次の大発見へのカギとなりうるんだ"


hi "覚えておきます……"


"武藤先生のまじめな話は終わったようだ。そして、少しおっちょこちょいな、いつもの彼に戻った。"


"思い返してみれば、武藤先生はこっちのほうがいいなと思う。普段から予想のつかない人だけど、このほうがまだわかりやすい。"

show muto smile
with charachange


mu "さて、これで話すことは話したな。中へ戻ろうか"


"そう言ってもらえて、心の底から安堵する。"


hi "はい、先生。先生のいう通りにします"

show muto normal
with charachange


"武藤先生は少しためらう。"


mu "そういう言い方をしてくれた生徒はお前が初めてだよ"


"一瞬、返事をしようかと考える。でも心の奥底から、黙って教室に戻れという声が聞こえてくる。"

play sound sfx_dooropen

scene bg school_scienceroom
with locationchange

stop music fadeout 5.0


"ドアの音を聞いて、生徒が数人びくっとし、急いで黒板の問題に取り組んでいるふりをする。"

play sound sfx_doorclose


"気にも留めずに机に突っ伏して寝ているやつらもいる。ありがたいことに、武藤先生はどうやら気がついていないようだ。"


"先生は教卓に戻って、引き出しから科学雑誌を取り出す。さっきの俺との話に影響されたんだろうな。"


"教室は、武藤先生と俺が話をする前の沈黙に近い状態に戻る。"


"疲労と期待の入り混じった雰囲気が教室に満ちている。誰もが休みたがっているか、さもなければ最後の準備を進めたがっている。"

play sound sfx_normalbell
play music music_daily fadein 8.0


"壁の時計が残りの授業時間をゆっくりと刻んでいき、ようやくチャイムが鳴り響く。解放だ。"

show muto normal at center
with charaenter


mu "お前たちが帰る前に言っておくが、回答は月曜までに提出するようにな"

hide muto
with charaexit


"クラス全員がすぐさま怠けたことを後悔し、ため息をつく。それでも、もっと差し迫った問題が目前にあることを敏感に感じてもいる。"


"学園祭の土壇場の準備にみんな出て行ってしまい、またたく間に教室は空になる。"


"俺は残って課題をさっさと終わらせようとする。そうすれば週末の間はそのことを気にせずにすむ。学園祭とか、いろいろあるしな。"

show bg school_scienceroom at bgleft
show hanako emb_downtimid at right
with charamoveinright


"俺を除くと、残ってるのは華子だけだ。リリーを待っているのは間違いない。"


"リリーが華子を迎えにわざわざこの教室まで来るというのも変な話だ。そうやって動き回るのは、少なくとも華子よりリリーのほうが大変なんじゃないだろうか。"


"でも俺には関係ないことだ。当然、華子からそのことを聞いたりはしない。"


"席は近いのに、俺も華子も会話を始めようとはしない。息の詰まるような沈黙が教室を包む。"


"沈黙のまま時間は過ぎていく。１５分たった程度だろうけど、もっと長く感じる。俺はノートのページをめくり、華子は読んでいる小説のページをめくる。"




"段落一つを終えようとしたところで、鉛筆の芯が筆圧で折れてしまう。"




"俺のいらだった溜息と、手探りで鉛筆削りを探す音が、教室の雰囲気を壊しているような気がする。"


"華子はかたくなに俺のほうから目をそらす。"


"やがて、リリーの姿が入り口に現れる。"

show lilly basic_smileclosed at offscreenleft
with None

show bg school_scienceroom at center
show hanako emb_downtimid at offscreenright
show lilly basic_smileclosed at left
with charamove


li "華ちゃん？"

show lilly basic_smileclosed at twoleft
show bg school_scienceroom at bgright
show hanako emb_downsmile at center
with charamove


"名前を呼ばれただけで華子は席から飛び出し、リリーのところまで駆け寄る。"

hide lilly
with charaexit

show hanako emb_downsad
with charachange

show hanako emb_downsad at Slide(0.5,0.5,0.7,0.5,1.0,time_warp=_ease_out_time_warp)
with None

hide hanako
with charaexit

"二人はしばらく静かに話をしていたけど、すぐにリリーは廊下に出て行く。華子はゆっくり教室に戻ってきて、また席に着く。"

show hanako emb_downsad at offscreenright
with None

show bg school_scienceroom at bgleft
show hanako emb_downsad at right
with charamove


"二人が仲たがいでもしたのかと思って、俺は全くの好奇心から、視界の端に華子をとらえる。"


"しばらくの間、華子は気落ちしたように机を見つめながら、何もせずに頬杖をついて座っている。"

show hanako emb_downtimid at right
with charachange


"退屈に耐え切れなくなったらしく、華子のきゃしゃな体はかばんに手を伸ばし、小さな本を取り出す。"


"そういえば、図書室で見た時に読んでいた本とは違うものだ。この分では、本を読むのがかなり早いに違いない。"


label jp_A31e:

hide hanako
with charaexit

stop music fadeout 4.0


"華子は席で本を読もうと落ち着かない様子だったけど、１０分ほどすると本を閉じて、リリーと同じく教室を出て行く。"


"俺も出たほうがいい、宿題はほとんど終わっているし、教室では他にすることもない。"

scene bg school_dormhisao
with locationskip


"あまりやる気が出ない。ただまっすぐ部屋に向かい、一日の残りを本を読んで過ごす。"

$ suppress_window_after_timeskip = True

scene black
with Dissolve(3.0)




label jp_A32:

scene bg school_scienceroom at bgleft
show hanako emb_downtimid at right
with None

hide hanako
with charaexit

stop music fadeout 4.0


"華子は席で本を読もうと落ち着かない様子だったけど、１０分ほどすると本を閉じて、リリーと同じく教室を出て行く。"


"俺も出たほうがいい、宿題はほとんど終わっているし、教室では他にすることもない。"


"とはいえ、他の場所ですることがあるわけでもない。"

play music music_tranquil fadein 3.0

scene bg school_hallway3
show crowd
with locationchange

play ambient sfx_crowd_indoors fadein 0.3


"校内は活発なミツバチの巣のようだけど、俺に気をとめる者は誰もいない。"


"どの教室でも、たくさんの生徒たちが働きバチのようにうるさくおしゃべりしながら、いろいろな作業に夢中になっている。俺はそれを横目にみながら、ぶらぶらと散歩する。"


"まるでまだ放課後じゃないみたいだ。"

stop ambient fadeout 0.3

scene bg school_courtyard
show crowd
with locationskip

play ambient sfx_crowd_outdoors fadein 0.2


"外はもう少し静かだけど、でもそれほどじゃない。"


"みんなとにかく急ぎ足で、右へ左へと駆けていく。忙しくて、活気がある。"


"俺の気分は正反対だ。真昼の日差しが俺の体から気力を全部吸い取っているみたいだ。おかげで全身がだるい。"


"俺のシャツの中を流れていく暖かく柔らかな風は、まるでクッションのようだ。"


"俺は気だるいあくびをしながら、何をしようか考える。"


"まずは本を寮に置いてこよう。それからは……まだ何も決めていない。"


"健二は部屋にいるかもな。"

stop ambient fadeout 2.0

scene bg school_dormext_half
with locationchange


"寮に戻る途中、向こうから笑美がやってくるのを見かける。あの奇妙なランニング用の義足はつけていないけど、走ってやってくる。俺が手を振ると、笑美は横滑りしながら足を止める。"

show emi basic_closedgrin at center
with charamoveinright


emi "やっほー、久夫くん！"


"鼻には白の、あごには緑のペンキが跳ねているけど、笑美はいつも通りに満面の笑みを見せる。"

show emi excited_happy_close
with characlose


"笑美は俺に身を寄せ、こちらを問いただすような雰囲気を強める。"


emi "なにしてんのっ？"


hi "別に何も。学園祭で何もすることがなくて。他のみんなは重要そうなことやってるみたいだし"

show emi excited_laugh_close
with characlose


emi "完璧！　それなら、あたしと琳を手伝ってよ！"


hi "学園祭の準備か？　うーん、そんなに役に立てるかどうかわからないけど"

show emi excited_proud_close
with characlose


emi "大丈夫！　あたしもそんなに役に立ってないからさ！"


"笑美は俺の手首をつかむと、むりやり俺を学校に引きずり戻そうとする。"

scene bg school_lobby
show crowd
with locationskip

play ambient sfx_crowd_indoors fadein 0.3


"笑美が歩く速度はむしろジョギングに近く、それについていくだけでも俺の足はもつれる。"

scene bg school_staircase2
with locationchange


"階段では笑美は少し速度を落とす。彼女の足では登りづらいのだろう。あるいは、笑美もとうとう息を切らしたか。"

stop music fadeout 7.0

scene bg school_hallway3
show crowd
with locationchange


"結局俺たちははるばる３階まで戻り、５分前に出た３年生の教室のある廊下にたどり着く。笑美が来るのがわかっていれば、ここで待っていたほうがまだ良かっただろう。"


hi "それで……琳はまだ壁画を描いてるのか？"

show emi basic_closedgrin at center
with charaenter


emi "うん！　いろんなペンキとかブラシとか材料が要るんだって。それであたし、美術室に取りに来たの"


hi "で、その手伝いに俺が要るってわけだ"

show emi basic_grin
with charaenter


emi "うん……琳が、久夫くんが前に手伝ってくれたって言ってたから、また手伝ってくれるかなーと思って"


hi "なるほどな"

stop ambient fadeout 1.0

scene bg school_classroomart at bgright
with locationchange

play music music_another fadein 0.5


"で、笑美のおかしな理屈のおかげで、俺はまた美術室に来て、他人のために材料を集めて回ってるわけだ。"


"美術室は俺たち以外は誰もおらず、空気中を埃が寂しく漂っている。笑美はすかさず後ろの壁まで跳んでいくと、ポケットから小さな、しわくちゃの紙切れを引っ張り出す。"


"彼女がそこに殴り書きされた内容を読んでいる間、俺はあたりに散らばっている資材に注目する。"


"たくさんのペンキ缶やボトルが乱雑に棚に並べられている。"


"そのいくつかはまるでそこに何十年も放置されていたかのように見える。前の世代の美術部の遺物のように。"


"ずっしりと積み重ねられた画用紙の束の横には、様々な大きさのブラシと仕分けされていないクレヨンが詰まった箱がある。"


"ペンキやテレビン油、新鮮な紙の匂いが淀んだ空気の中を漂い、俺の小鼻の中で混ざり、いかにも美術的な匂いへと変わっていく。"

show emi basic_closedgrin at offscreenright
with None

scene bg school_classroomart at bgleft
show emi basic_closedgrin at right
with charamove


"笑美はメモ書きを読み解くと、それらを様々なペンキ缶に記されたマークと見比べ、一致したものを見つけ出しては俺に手渡す。"

show emi basic_grin
with charachange


"首を伸ばして一番上の棚を見ようとするけど、なかなか届かない。"

show emi basic_annoyed
with charachange


"どうがんばっても、笑美の視線は棚より低いままだ。あきらめた笑美は、おもちゃ屋にいる子供のようにものほしそうに棚を見上げ、腹立たしげに息を吐く。"

show emi annoyedbounce
with None


"怒った笑美は、今度は上下に跳び始めた。どうやら一瞬だけ見えるラベルを素早く読み取って、手に取ろうとしているようだ。"

show emi basic_closedsweat at center
with charachange


"当たり前だけど、まったくうまくいかない。それどころか危うく棚そのものを倒してしまいそうになる。"


"俺が手を貸してやったほうがいいわけがやっとわかった。"


hi "ほら、俺がやるよ。そんなに高くは跳べないだろ。それに怪我でもされちゃかなわないし"


hi "あと俺、君より２倍は背が高いからさ"

show emi sad_angry
with charachange


emi "そんなことないもん！"


"笑美は顔を真っ赤にしてすっかり機嫌を損ね、そっぽを向いてしまう。"


hi "冗談だよ、冗談。で、そこは俺が見るよ、な？"

show emi basic_annoyed
with charachange


"笑美は俺をもう一度にらみ付けるけど、それ以上の反論はできない。むくれたように『ふーん』といって俺に向き直る。"

hide emi
with charaexit


"そして俺は棚の一番上からペンキを集め始める。その下で、笑美はしゃがみ込んで戸棚から集められるだけのものを集める。"


"笑美がこちらを見ていないことを確認してから、やれやれと頭を振る。"


"笑美が自分の身長にコンプレックスを抱いている、というのは驚きだった。知っていればからかったりなんてしなかったのに。"


"笑美はおおらかそうだけど、でも弱点は誰にでもあるってことか。"

show emi basic_grin at center
with shorttimeskip


"材料を大体集め終え、トレジャーハンターの戦利品のように机の上に並べる。そこで俺はようやく、笑美が怒ったのは背が低いことをからかったせいではないのかも、ということに気づく。"


"自分にできないことがある、と言われるのがいやなのかもしれない。たとえばジャンプすることのように。"


"でも笑美自身はもうすべてを忘れてしまったようだ。怒りっぽいけど、忘れやすい……彼女はそういうタイプなのだろうか？"


"少なくとも、もう気にしてはいないようだ。残りの材料を集めて、琳のところへ戻る間、笑美はずっと楽しそうにおしゃべりを続ける。"

scene bg school_courtyard
show crowd
with locationskip

play ambient sfx_crowd_outdoors fadein 0.2


"二人で寮に戻る間、俺はレディーファーストの精神を発揮してほとんどの材料を引き受ける。"

show emi basic_annoyed at center
with charaenter


emi "琳は絵を完成させなきゃって必死なの。悪いのは本人なんだけどさ。もっと早く始めていれば良かったのに"


hi "あいつ、完成できそうか？"

show emi basic_closedgrin
with charachange


emi "わかんない。あたしは大丈夫だと思うけど、でも琳がすることは予想がつかないからなあ"

show emi basic_annoyed
with charachange


emi "今朝、琳が寮の前でひざを抱えて横になってたのをあたしが見つけたの。琳、一晩中寝てなかったんだ。夜勤の看護の人が気づかなかったなんて信じられなくて"

show emi basic_grin
with charachange


emi "しかも、それでまた狂ったように絵を描いてる"


hi "ああ、確かに琳が……動揺してる、っていうのかな。俺も気づいてはいたけど"

show emi basic_closedhappy
with charachange


"笑美はその言葉と、明らかに気まずそうな俺の態度にクスクス笑う。"

show emi basic_happy
with charachange


emi "あたしは気にしてないよ。琳も、ちょっと変な風になることがあるってだけだもんね"


"それには俺も同意する。でも俺と違って、笑美は琳の……あの余りにズレている部分に対しても冷静でいられるようだ。"


"でもこっちの二人からは、ミーシャと静音のような距離の近さは感じない。あの二人が一体となったように何かに取り組むのを見ていると、どこからが静音でどこからがミーシャなのか、判断するのは難しい。"


"あの二人は似ても似つかないというのに。笑美や琳と同じように。"


"そして琳は他の誰よりも、俺が今まで出会った誰よりも異なっている。"


hi "ああ、あいつはともかく……個性的なやつだよな"


"俺はもう一度『個性的』という言葉を使う。その一言で琳の性格を言い表せるかのように。だけど実際には、琳の奇妙さについての長ったらしい説明を言い換えているだけだ。"

show emi basic_closedhappy
with charachange


"俺が適切な言いかたを探していると、笑美はくつくつと笑う。"

show emi basic_grin
with charachange


emi "とにかく、変わってるよね"

show emi excited_proud
with charachange


emi "ところで、さっきね、琳、箱の上に３０分もずっと座ってたんだ"


emi "それで、ずっとつま先を見てるだけなんだよ"

show emi basic_closedhappy
with charachange


"彼女はもう一度クスリと笑う。何が面白いのかわからないけど、とにかくおかしい、そう思わせる笑い方だ。"

stop music fadeout 3.0

show emi basic_grin
with charachange


emi "ずっとだよ"

stop ambient fadeout 2.0

scene bg school_dormext_half
with locationskip

play music music_happiness fadein 2.0


"作業場はひどい散らかりようだけど、壁画自体は前回見たときよりもさらに広く壁に描かれている。"


"醜く捻じ曲げられた人の形が赤、ピンク、そしてオレンジを基調にして彩色されている。奇妙で、空想的な……何か、がその隙間を埋めている。"


"これは……良いものだ。他に一言でこの絵を表現しきる言葉は思い浮かばない。だから俺は『良い』という差し障りのないところに落ち着く。"


"でも正直、この壁の周りは壁画の進み具合と同じペースでどんどん散らかっているみたいだ。"


"地面にはたくさんのペンキ缶や様々な美術用具、そして空のソーダの瓶が転がっている。"

show rin negative_spaciness at center
with charaenter


"当の琳はこの混沌のど真ん中で、自身がその一部分であるかのように、とても居心地良さそうに突っ立っている。"


"ズボンのすそはひざまでまくり上げられ、細い脚があらわになっている。笑美の顔と同じく、ネイティブアメリカンの出陣化粧みたいに色とりどりのペンキがかかっている。"

show emi basic_grin at offscreenleft
with None

show rin negative_spaciness at tworight
show bg school_dormext_half at bgright
show emi basic_grin at twoleft
with charamove


"笑美は俺を置いて琳の元へ駆け寄ると、その正面に元気よく跳びこんでみせる。"

show emi basic_closedhappy
with charachange


emi "ただいま！"

show rin basic_awayabsent
with charachange


rin "早かったね。また廊下、走ったの？"

show emi excited_proud
with charachange


emi "久夫くんが手伝ってくれたの"

show emi basic_grin
with charachange


"笑美は勝ち誇ったように俺を指差す。"

show rin basic_absent
with charachange


"琳は笑美の指がさすほうを目で追って振り向き、俺のいる方向を見る。"

show rin basic_deadpannormal
with charachange


"彼女はぼんやりと俺にうなずきかける。夕べから眠っていないようだ。うつろで生気のない視線は、俺を見ているようで少しずれている。目の動きもスローモーションの動画のようだ。"


rin "やあ、久夫。手伝ってくれてありがと"


hi "礼なんていいよ"

show rin basic_deadpan
with charachange


rin "もう言っちゃったよ"


hi "気にするなよ"


hi "進んでるみたいだな。見た感じ、良く描けてるよ"

show rin basic_deadpannormal
with charachange


rin "でもそんなこと言うともっと不幸になるよ"


hi "わかってる。それでも俺は構わないよ"

show rin basic_deadpandelight
with charachange


rin "へー、良いこと言うじゃん。もちろん私にとってだけど。君じゃなくてね"

show rin basic_awayabsent
with charachange


rin "芸術家はいつも不運に見舞われてるんだよ。四六時中、自分の描きかけの絵を見てないといけないんだから"


rin "だから芸術家は恋愛もできないし、好きなテレビ番組も打ち切られちゃうし、若いうちに謎の病気で死んじゃう。深くて謎めいた宇宙の法則だよ"

show rin basic_lucid
with charachange


rin "盲目でもない限りね"


"琳は眠りに落ちるかのようにしばらくの間考え込む。"

show rin basic_absent
with charachange


rin "男の子がいてね"

show rin basic_deadpannormal
with charachange


rin "美術部になんだけどね、盲目なんだ。だからさ。見えないの"

label jp_A32a:


hi "それ、前にも話したじゃないか"

show emi basic_hes
with charachange


"ちらりと脇にいる笑美を見やれば、彼女も俺にこの話は前に聞いたと言いたげな視線を送る。"


"でも、俺も笑美も琳に何も言わない。なので琳はつまらないお笑い芸人のように、モノトーンな独り言を続ける。"

label jp_A32b:

show rin basic_awayabsent
with charachange


rin "あの子は芸術家になるべきだよ。不運には絶対見舞われないよ。間違いない"


rin "いいアイディアだと思わない？"

show rin basic_lucid
with charachange


hi "目の見えない人しか芸術家になるなって？　そうは思わないよ"


"……"

show rin basic_deadpan
with charachange


rin "確かにそうかも"

show rin negative_spaciness
with charachange


"一連の思索をほっぽり出して、琳は壁画を吟味するためにまた振り向き、鼻歌を歌いだす。その歌は聞いたことがあるような気がするけど、名前までは思い出せない。"

show emi basic_closedgrin
with charachange


"笑美はその場を整理しようと、持ってきた材料を並べ、ペンキ缶を動かす。"

show rin basic_awayabsent
with charachange


rin "笑美、プルシアンブルーのペンキちょうだい"

show emi basic_confused
with charachange


emi "プルシアンブルーってどれ……"


"笑美は７、８個ある、それぞれ濃さの違う青の缶をなすすべもなく見つめる。"

show rin basic_deadpan
with charachange


rin "プルシアンブルーが入ってるやつだよ"

show emi basic_annoyed
with charachange


emi "もう、琳！　それじゃ全然わかんないよ！"


"俺も周りを見渡してみる。でも俺だってプルシアンブルーがどういう色なのか知らない。青とプルシアにいったいどういう関係があるんだろう。"


"……というか、そもそも『プルシア』ってなんなんだ。聞いたことがある気がするけど、思い出せない。"


"どの青を見てもほかに比べてプルシアンって感じはしない。でも、缶のラベルに書いてある小さな字を読むと、どれも中身がプルシアンじゃないってことがわかる。"


hi "ここにはプルシアンブルーなんてないぞ"







label jp_A33:

scene bg school_dormext_half at bgright
show rin basic_deadpan at tworight
show emi basic_annoyed at twoleft
with None


"笑美はため息をつく。"

show emi basic_closedsweat
with charachange


emi "あたしが戻って取ってこないといけないかなあ"

show emi basic_grin
with charachange


emi "でも、あたしのクラスの企画を手伝うって約束しちゃったんだ。だから戻ってくるのはしばらく後になるの。２、３時間ぐらい、あたしがいなくても大丈夫？"

show rin basic_deadpannormal
with charachange


"琳がうなずくと、笑美は去っていった。"

stop music fadeout 2.0

hide emi
with charaexit

show rin basic_deadpannormal at center
show bg school_dormext_half at center
with charamove


"俺は他にできることもないし、琳が絵を描くのを観たかったので、その場にとどまる。"


"箱の上に座り、かばんから今日の本を取り出す。２週間何もせずに酒を飲み続けている３人の男の物語だ。"

play music music_pearly fadein 2.0

hide rin
with charaexit


"琳は一箇所に青のペンキを塗り終えると、今度は別の箇所へ移動する。"


"琳は黙々としっくいの壁にむかって足を振る。ペンキが重ねて塗られていき、壁画はだんだん形を成していく。"


"俺はのんびりとページをめくる。この章では、男たちは主人公の友人の家でビールを飲んでいる。これまでは主人公のアパートだった。"


"特に面白いというわけでもない。ある架空の人物の人生の一部分。どうしてこれが書かれなくてはいけなかったのか、不思議で仕方ない。"


"一体なぜだろう。何かを創造する理由……想像もつかない。"


"琳が絵を描く理由もそうだ。琳と笑美は、まるで敵討ちのように自分の境遇にまっすぐ立ち向かっている。その意味では二人は同じのような気がする。"


"実際、琳はそんなことを言っていた。『できないことをやろうとするのは、それが本当はできるから』と。"


"そういう意味だったのか？　それが琳の『理由』か？　笑美の理由かもしれないな。あの子は結構頑固だから。"



"琳からはそういう印象を受けない。考えてみれば、琳からはなんの印象も感じたことがない。というか、話すたびに毎回違った印象を受ける。"


"琳はなぜあんなことを言ったのだろう。なぜ琳、いや人は絵を描き、色を塗り、彫刻を彫り、物語を書くのだろう。"


"俺は今まで何かを作りたいという衝動に駆られたことは一度もない。だから俺に理解できるとは思えない。"


"むなしい気分になる。"


"ぞっとする話だ。それが正しいのかどうか、はっきり判断することもできそうにない。"


"俺はこれでいいのだろうか？　琳をうらやむ気持ちがあるのは否定できないけど、それが俺の落ち度とは思えない。"


"俺は俺、琳は琳、だ。"


"そうは言っても、俺も何か探さなくてはいけない。病院にいたときのように、読書に没頭するんじゃなくて、何か……この気の迷いが少しでもまぎれるようなものを。"


"戸惑う気持ちを抑えられない。この新しい学校や生活、周囲の人間のおかげで、その感覚はどんどん強まる。"


"俺だって、ここの人たちの中にとけ込もうとがんばっている。それに俺が会った人たちは、みんなといってもいいほどいい人ばかりだ。"


"それでも、まだ自分がよそ者みたいな気分がする。俺はここにいてはいけないんじゃないか、と。"

stop music fadeout 2.0


"考えを振り払う。つい上の空になってしまった。本もめくっていなければ、琳の手助けもしていない。"


"琳は俺に頼みもせず、自分の足で缶からペンキを注ぎ足そうとしている。あるいは頼んだけど俺が聞きそびれたのかもしれない。"


"どちらにせよ、ふらついていて危なっかしい。"

scene bg mural_part
show rin basic_awayabsent_close at tworight
with locationchange

play music music_soothing fadein 0.5


"琳が缶の中身を道端にぶちまけそうになっているのを見て、俺は飛び上がって手を貸す。"


"俺は琳の足から缶を取り上げ、代わって中身をボウルに注ぎ込む。"

show rin basic_absent_close
with charachange


"俺も琳も何も言わない。俺は一瞬、琳のぼさぼさの前髪越しに見上げる視線を感じる。"


"何を思っているのかわからない。完璧なまでのポーカーフェイスだ。でも、驚きのようなものが少しだけ混じっている。"


"何を考えているのだろう。俺が何を考えているのか、だろうか。それとも何も考えていないのか。"


hi "お前の考えてることに１セント賭けてやるよ"

show rin basic_deadpan_close
with charachange


rin "あれ、セントなんて持っているの？"


hi "いや、持ってない"

show rin basic_deadpancontemplation_close
with charachange


rin "じゃあ教えてあげない。私は何も考えてないから、久夫は運がいいよ。ただ今は考えちゃったけど"


"琳は顔をしかめる。とても不満そうだ。"


rin "何も考えないって難しいんだよ。でも大事なことなんだ"


"なぜ大事なのか訊こうとしたところで、年老いた男が近づいてきた。見たところ琳に用事があるようだ。"

scene bg school_dormext_half at bgright
show nomiya smile at center
with locationchange


no_ "やあ、調子はどうかな？"

show nomiya smile at twoleft
show bg school_dormext_half at center
with charamove

show rin basic_awayabsent at tworight
with charaenter


rin "できます"


"琳は壁から目を離そうとせず、自然なそぶりで答える。そこから、二人が知り合いであることがわかる。"


"この男には会ったことがない。当然、彼は誰なんだろうと思う。ここの先生なのか？"


"髪の色は薄れて、銀色っぽい白髪になっている。色の抜け具合から染めているようにも見えるけど、そうでないことを祈ろう。"


"小さな丸い眼鏡が鼻にかかっているけど、彼はそのレンズを『通して』というよりは、その『上から』物を見ているようだ。"


"彼は壁画をしげしげとそのレンズ越しに観察する。"

show nomiya talk
with charachange


no_ "よし、よし"


no_ "実に大胆な構図だ！"


"彼は壁画を端から端まで見ながら、明らかに俺たちに聞こえるように独り言を喋り続けた。"

show nomiya veryhappy
with charachange


no_ "実にいい、実に……"


"どういう意味で『いい』のかはわからないけど、琳は気にしているようではなく、作業場を見回している。そこかしこに、いろんな色のペンキが入ったボウルが散らばっている。"

show rin basic_deadpan
with charachange


rin "久夫"


hi "ん？"

show rin basic_deadpannormal
with charachange


rin "この色、もう少し"


hi "ちょっと待っててくれ"


"俺は２つのペンキを半々の分量でボウルに注ぐ。琳が壁画の、人の顔を塗るのに使ったような、淡いピンクを目指して。"


"琳は俺の作業を見ている。なんだか緊張するな。琳の表情はとてもおとなしくて、実は俺が何かへまをするのを待ちかまえているんじゃないか、という気分になる。"


"男も驚いたように俺のほうに振り返る。俺がいることにたった今気づいたかのようだ。"


"あるいは、本当にそうなのかも。"

show nomiya talk
with charachange


no_ "おや、こんにちは。どなただったかな？"


hi "えっと、３－３に転校してきた中井久夫です。初めまして"

show nomiya frown
with charachange


no_ "武藤先生のクラスか？　それはそれは！"

play sound sfx_birdstakeoff

show nomiya veryhappy
with vpunch


"彼は大声で笑う。やかましいほどの大声だ。小鳥が木から飛び立っている。"

show nomiya talk
with charachange


no_ "私は野宮紳一。担当は美術だ"


"この人が美術の教師か。確かに美術教師というような風貌だ。第一印象から察する限りでは。"

show nomiya smile
with charachange


no "それで、どういうわけで我が愛弟子の手伝いをやっとるのかね？"



label jp_choiceA33:
menu:
    with menueffect
    "俺は……"
    "いえ、たまたまここにいただけなので……":




        return m1
    "実は美術部に興味があって":


        return m2


label jp_A33a:


hi "少し美術部に興味があって"


"そのつもりはなかったのに、口を滑らせてしまう。"

show nomiya talk
with charachange


no "どういうことだね？"


hi "いや……たいしたことじゃないです"


hi "そのうち美術部に行ってみてもいいですか？　見学程度になるかもしれませんけど"


hi "部活か何かに入ったほうがいいかと思ってたから、それで……"


"後先なんて全く考えていない。でもこの１週間で、ぼんやりとだけど、決心のような気持ちが俺の中に生まれ始めていた。"


"何かをやりたい。どこかへ属したい。"


"それが美術部だって構わない。俺は不器用かもしれないけど、それでもいい。"


"野宮先生は喜んでいるようだ。"

show nomiya veryhappy
with charachange


no "ほう、入部希望かね？　よろしい、新入部員はいつでも大歓迎だ"


no "活動はいつでもやっているぞ。我々は芸術の様々な側面を追求し、そして自らの手で実践しておる"

show nomiya frown
with charachange


no "……もしくは足で"


"先生はきまり悪そうに咳払いするけど、琳は気にしていないようだ。俺以外にも言葉遣いに苦労している人がいると知って、少し安心する。"


"先生は光り輝く大きな懐中時計をわざとらしく見て、自分の失言から立ち直る。そしてさらにわざとらしく額を打つ。"

show nomiya veryhappy
with charachange


no "私はそろそろ行かねばならない。何か質問があれば、手塚のほうでハッキリさせてくれるだろう"


"琳が『ハッキリ』というのは何か違う気がする。しかし先生は急いでいるようだったので、俺はそれ以上の追及はしない。"

show nomiya smile
with charachange


no "手塚、制作が順調に行っているようで安心したよ"

show nomiya talk
with charachange


no "明日になってサジを投げないように言っておこうと立ち寄ったんだ。学園祭に何人か人を呼んでおいたんでな。もちろんお前にも会いたいと思うだろう"

show nomiya smile
with charachange




no "では中井、月曜日にな。待っているぞ"

stop music fadeout 6.0

hide nomiya
with charaexit

show rin basic_deadpannormal at center
show bg school_dormext_half at bgleft
with charamove


"先生が去っていく。俺たちはまた２人きりになった。琳は相変わらず何事もなかったかのように作業を続けている。実際何事も起きなかったわけで、俺はいったい何を考えてるんだ、と自問する。"


"中学のころの成績からして、俺は芸術とは昔から相性が悪かった。"


"部活なら必修の授業とは話が違うかもしれない。やってみなきゃわからないさ。"



"その辺のことで何か意味のある質問をひねり出そうとするけど、何も思いつかない。"


"実際に部活に顔を出して、様子を見てみるか。"


hi "それで、先生はお前の絵を見せるためだけに人を呼んだってのか？"

show rin basic_absent
with charachange


rin "芸術家のお友達が多いからね。そういう話が大好きなんだよ"

show rin basic_awayabsent
with charachange


rin "きっと、その人たちと一緒にそういう話をしてほしいんだと思う"


hi "なんだ、嬉しくなさそうだな？"


"琳は投げやりに肩をすくめる。自分の絵、いやどんな絵画についても、人と話をするのはいやだ、という印象を受ける。"

show rin basic_deadpan
with charachange

play music music_rin fadein 5.0


rin "芸術のことを話すのはあんまり好きじゃないんだ。そもそも芸術って言葉がなくても通じ合うものだから。わざわざ口で話す必要なんてないでしょ？"


hi "まあ、それはわかる"

show rin basic_deadpannormal
with charachange


rin "退屈してて、それを理由に退屈について話すようなものだよ"


hi "それ、どういう意味だ？"

show rin negative_spaciness
with charachange


rin "今退屈だ、ってことを話したことはない？　意味ないし、面白くないよ。『ああもう、退屈』としか言うことがないんだから"
rin "一度、１週間ずっと退屈してることについて意味のある説明を考えてみたことがあるんだ"


rin "そうしたら最高に退屈な１週間になったよ"


hi "でも、それなら筋が通ってるじゃないか。そうだろう？"

show rin basic_deadpan
with charachange


"琳は何も言わず、意味はないけど本当はあるんだ、とでも言いたげな視線を俺に向ける。"


hi "とにかく……どうだろうな、芸術については言えることはほとんど思い浮かばないよ"


hi "というか、お前が今描いている絵だってそうだよ。どう考えればいいのか、俺にはわからない。いい絵だなとは思うけど。この絵はなんの絵なんだ？"

show rin basic_deadpannormal
with charachange


rin "これはなんの絵でもないよ"


"……"

show rin basic_deadpandelight
with charachange


rin "それが私の言いたかったこと。だから言ったの"

show rin basic_deadpannormal
with charachange


rin "今のは少し嘘も入ってるけど。それが本当だったらいいなと思ったから、言っちゃった"


rin "壁画をやってみろって言ったのは先生なんだけど、私は何を描けばいいのか全然わからなかった。考えてはみたけど、何も思いつかなかった"

show rin negative_spaciness
with charachange


rin "で、結局わからないまま描いちゃった"


hi "じゃあ、『今は』何を描いてるんだ？"

show rin basic_absent
with charachange


rin "わかんない"

show rin basic_delight
with charachange


rin "そうだ。この絵を『わかんない』ってタイトルにしようか"

show rin negative_worried
with charachange


rin "あー、また考え始めちゃった。これじゃダメ"

show rin basic_absent
with Dissolve(0.15)

show rin negative_worried
with Dissolve(0.1)

show rin negative_worried
with Dissolve(0.05)

show rin basic_absent
with Dissolve(0.05)

show rin negative_worried
with Dissolve(0.05)

show rin basic_absent
with Dissolve(0.05)

show rin negative_worried
with Dissolve(0.05)

show rin basic_absent
with Dissolve(0.05)

show rin negative_worried
with Dissolve(0.1)

show rin basic_absent
with Dissolve(0.15)

show rin negative_worried
with Dissolve(0.5)


"琳は頭を振って『考え』を振り払う。赤みがかった琥珀色の髪が大きく揺れる。"

show rin basic_deadpannormal
with charachange


rin "笑美がいて助かるっていうのはこういうことなんだよね。笑美がいると何も考えずにいられるから"


rin "知ってるでしょ、あの子がどうでもいいことを何時間も喋りまくるの。頭が泡風呂用の入浴剤でできてるみたい"

show rin basic_deadpandelight
with charachange


rin "君も似てるかも。でもそうでもないかな。君がいてくれるとすごく助かるから"

stop music fadeout 5.0


"褒めてるのかそうでないのかわからない。どっちでもないのかも知れない。琳はとにかくはっきりしないやつだからな。"


hi "で、お前が何も考えなくて済むように、俺は何をすればいい？"

show rin basic_deadpan
with charachange


rin "ここにいて"

hide rin
with charaexit


"何をしたらいいかわからないまま、俺は空き箱に座って、ただ琳が作業を続けるのを眺め、ぼんやりとビール飲みの本のページをめくる。"

play music music_dreamy fadein 1.0

scene bg mural_part
show rin negative_spaciness_close at tworight
with locationchange


"琳の表情は穏やかで、その考えは――それがなんであれ――深緑の瞳の向こうに隠れている。いや待てよ、琳はたぶん何も考えていないんだな。"


"琳は静かに鼻歌を歌う。時々、歌うのをやめて俺にペンキやブラシを渡してほしいと丁寧に頼む。"


"琳の集中力は見事なものだ。ただでさえ睡眠不足みたいだし、完成へのプレッシャーもあるだろうに。"


"壁画は少しずつ形を成し、細部も綿密に描き込まれていく。色もより複雑に絡み合い、空白を埋め、完成に近づいていく。"


"芸術へ向かう熱意や意欲というのは何なのか、ということをまたも考えている自分に気づく。"


"人はどこから発想を得るのだろう？　発想はどこからともなくあらわれるものじゃない。魔法のようにインスピレーションを与えてくれる神様なんてものもいないだろう。"


"発想には原点と目的があるものだ。"


"それを考えているうちに、琳は壁画のことで嘘をついているか、少なくとも事実を曲げている、という確信が強まる。琳自身も気づいてはいないのかもしれない。"


"作ろうとしているものについてなんの考えも持たずに、創造的なことはできない。それは言葉の定義に反する。"


"何かを描くにはブラシの動きを一振り一振り決めなくてはならない。たとえ無作為に描いていたとしても、それは意識的な選択だ。"


"だから琳の描く絵は――この壁画であっても――何を描くかという意図的な目的か発想が元になっているはずなんだ。"


"琳が言ったとおりに『何も考えないこと』が彼女の発想だとしたら、それは発想のうちに入るんだろうか？"


"矛盾だろうか？　普段から琳はそういう風に話しているように思う。だから琳がそのことに気づいてないとしても、特に驚くことじゃない。"


"そのことを話すべきだろうか、と思う。でも琳と理屈の話を議論したいのか、というと自信がない。"


"そうなったら、たぶん俺たちのどちらかの頭があっという間にショートしてしまうだろう。俺はその考えをあきらめる。"

show rin basic_awayabsent_close
with charachange

show rin negative_spaciness_close
with charachange


"琳は落ち着きなく体をひねっている。"


show rin negative_annoyed_close
with charachange

show rin negative_spaciness_close
with charachange


"いつものようなぼんやりとした顔にも、時折苦しそうな表情が浮かぶ。偶然で出るような表情じゃない。"

show rin negative_annoyed_close
with charachange


hi "大丈夫か？"


rin "うん。いや"


rin "また背中が痛くなってきた"


rin "この絵、大っきいからね、やっぱり。それにこんな姿勢じゃ描くのも大変なんだよ"


hi "休憩でも入れるか？"

show rin basic_deadpanupset_close
with charachange


rin "この部分が終わってからにする"

show rin negative_annoyed_close
with charachange


"もちろん、琳はその後も休憩はとらない。そして俺もそれ以上は言わない。きっと言っても無駄だろう。"

scene bg school_dormext_half_ss
with locationchange


"琳は作業を続け、俺も琳に付き添う。琳の作業を見ているのは好きだ。それにこれからは同じ部活に属することだし。"

stop music fadeout 4.0
$ renpy.music.set_volume(0.5,0.0, "ambient")
play ambient sfx_cicadas fadein 3.0

scene bg school_dormext_full_ni
with Dissolve(3.0)


"琳がこの壁画の完成を宣言したとき、辺りはすっかり暗くなっていて、どうやって琳が完成したと判断できたのか俺にはわからなかった。"


"お祝い気分も、普通の達成感もない。疲れてぶっきらぼうな『終わった』という言葉だけがあった。そして俺たちは寝床へと向かう。"

stop ambient fadeout 3.0

$ suppress_window_after_timeskip = True

scene black
with Dissolve(3.0)


label jp_A33b:


hi "自分でもよくわかりません。きっと他にやることもなかったんです"

show nomiya veryhappy
with charachange


"彼はもう一度大きく笑う。そして時計に目をやる。"

show nomiya smile
with charachange


no "私はそろそろ行かねばならない。手塚、制作が順調に行っているようで安心したよ"

show nomiya talk
with charachange


no "明日になってサジを投げないように言っておこうと立ち寄ったんだ。学園祭に何人か人を呼んでおいたんでな。もちろんお前にも会いたいと思うだろう"

show nomiya smile
with charachange


no "それと、月曜の部活動は休みだ。ちょっと町から出るのでな。何かしたいことがあれば自分たちでやるといい"

hide nomiya
with charaexit

stop music fadeout 4.0

show rin basic_deadpannormal at center
show bg school_dormext_half at bgleft
with charamove


"彼は大げさに身を翻し、大股に去っていく。"


"なんて変わった先生だろう。"


hi "俺も行かなきゃ。またな、琳"


"手を振ると、俺は寮の階段へと引き返す。"


"きっとこの本を今日中に読み通せれば、明日は丸一日学園祭に足を運べるだろう。"

$ suppress_window_after_timeskip = True

scene black
with Dissolve(3.0)




label jp_A34:

scene bg school_dormext_half at bgright
show rin basic_deadpan at tworight
show emi basic_annoyed at twoleft
with None

stop music fadeout 6.0

show emi basic_closedgrin
with charachange


emi "じゃあ、追加でとってこないとね"


"いや、プルシアンブルーのペンキをもう一缶取ってくるだけの簡単な仕事に、わざわざ２人で行くこともないだろう。"
"そう言おうと口を開くけど、すでに笑美が俺の腕をつかんで引っぱり始めていた。"

hide emi
with charaexit


"琳に手を振るけど、あいつは俺たちが立ち去っていることにすら感づいてないみたいだ。"

play ambient sfx_crowd_outdoors fadein 0.5

scene bg school_courtyard
show crowd
with locationskip


"まあ、プルシアンブルーを探して見当たらなかったらその時気づくだろう。"

scene bg school_lobby
show crowd
with locationskip

play ambient sfx_crowd_indoors fadein 0.5


"たぶん。"

scene bg school_staircase2
with locationskip


"……"

scene bg school_hallway3
show crowd
with locationskip


"やっぱり気づかないだろうな。"

stop ambient fadeout 2.0

scene bg school_classroomart
with locationskip


"琳はどこまで変なやつなんだと考えるのに忙しい俺をよそに、笑美は俺を美術室へと引っ張っていく。"


"息が切れだしているのを感じる。"


hi "そんなに急がなくてもいいだろ？"

show emi basic_confused at center
with charaenter


emi "ん？"


"何かを見極めようとしているかのように、笑美が俺に値踏みするような視線をよこす。"


hi "いや、ずいぶん急いでるみたいだからさ"


hi "これじゃ体が持たないよ"


"笑美は納得がいった、という顔をする。"

play music music_emi fadein 0.3

show emi excited_proud
with charachange


emi "まさか久夫くん、もう息切れしちゃったの？"


"笑美がふざけ半分の口調で俺を責め立てる。"


"否定したい衝動に駆られるけど、足を止めてからこっち、自分が荒い息をしていることに気づく。"


"まあ、バレバレだよな。"


hi "ちょっとな。みんながみんな体調万全ってわけにはいかないんだよ"


hi "人それぞれだろ？"

show emi basic_annoyed
with charachange

"笑美は眉をひそめる。あまり良くない表情だ。"


hi "あー、それってつまり……"


hi "体を鍛えろってこと？"


"確かにそんな決心はしたけどさ。"


"ランニング中に粗動が起きたことで、俺は走る習慣をつけなきゃいけないと本気で感じている。"


"なんだかんだで、あんな人騒がせなことになるまでは気分良かったし。"


"いや、気分が良かったわけじゃなかった。でもあれは……楽しかったのか？"


"一方で笑美は、俺の言葉を聞いて何か決心したらしかった。"

show emi basic_closedgrin
with charachange


emi "うん、その通りだよ"

stop music fadeout 1.0

show emi basic_annoyed
with charachange


"笑美の瞳が真剣になる。"


emi "一緒にやろうよ"


"……"


hi "今なんと？"

show emi basic_grin
with charachange


emi "朝にさ"


emi "今からあたしたちランニングパートナーだよ"

show emi basic_closedhappy
with charachange


emi "メニューもすっかり考えてあるんだよ。実はね……"

play sound sfx_paper


"くしゃくしゃの紙を取り出す。"

show emi excited_amused
with charachange


emi "ちょうど持ってきてるんだ"

play music music_running


"俺は紙を受け取ってザッと目を通す。"


"時間、日付、周回数、すべてが設定されている。"


"一日ほんの２、３周からだんだん増えていって……"


"なんだこれ、俺にマラソンでも走らせるつもりか？"


"それに、これだけの計画をまとめる時間がどこにあったんだ？"


"そもそも、いつからこの計画を練ってたんだ？"


hi "これ、前から考えてたのか？"

show emi sad_shy
with charachange


emi "少しね"

show emi sad_grin
with charachange


emi "でもほんとはナースくんのアイデアなんだよ！"

show emi basic_closedgrin
with charachange


emi "久夫くんが言われたとおりに運動するように、ちゃんと見ててくれってナースくんに言われたんだ！"



label jp_A34a:


"巨大な陰謀？"


"健二は気づいていたのかも……"


hi "『見てる』というにはちょっとやり過ぎじゃないか"

show emi sad_grin
with charachange


emi "えっと、実はね、ちょっと前から朝練のランニングパートナーを探してたの"


"ああ、健二！　この陰謀が明かされる瞬間をお前が見られたら！"


hi "そもそも、なんのためにパートナーがいるんだ？"

show emi basic_annoyed
with charachange


emi "自分一人でやるより、練習を続けるのが楽だから"


emi "当たり前でしょ？"


emi "誰かに頼りにされてたら、そうそう止めようなんて思わないでしょ？"


hi "なるほど。するとお前だけじゃなくて、俺も確実に走り続けることになるわけだ"


hi "つまり俺はナースの言葉に従うことになって……"

show emi excited_proud
with charachange


emi "……あたしもナースくんの言った通りに久夫くんを見てあげられる！"

show emi basic_closedgrin
with charachange


emi "話が早いね、久夫くん"


hi "いやだって言ったら？"


"もちろん断るつもりなんてない。"


"でもこんなに巧妙な計画には、せめて形だけでも抵抗を見せておかないと。"

show emi basic_grin
with charachange


emi "そうだなー、そしたらほっぺ膨らませるよ"


emi "久夫くんは茨崎笑美のほっぺを膨らませた男として生きていかなきゃいけないよ"

show emi basic_closedgrin
with charachange


emi "そんな気がとがめること、やだよね？"

show emi sad_depressed
with charachange


"見せつけるように、笑美はほっぺを膨らませ始める。"


"こんなに可愛らしく、そして見ていて心の痛むものは今まで見たことがない。"


hi "わかったよ！　わかったから！"


hi "とにかく……それをやめてくれ！"


hi "子犬でもぶったような気分だ！"

show emi basic_closedgrin
with charachange


emi "じゃあ決まりだね？"


emi "ランニングパートナーになってくれるんだね？"


emi "トレーニングこなすよね？"


emi "食事プランも？"


hi "食事プラン？"

show emi basic_grin
with charachange


emi "うん、食事プラン！"

show emi excited_proud
with charachange


emi "体を鍛えるには、健康な食生活をしないといけないんだよ！"


"トレーニングメニューをよく見てみる。"


hi "食事プランなんて載ってないぞ"

show emi basic_shock
with charachange


emi "あっホントだ！　渡すの忘れてたよ！"

play sound sfx_paper

show emi excited_amused
with charachange


"またしわくちゃの紙を取り出して、渡してくる。"


"こっちはもう少し大ざっぱな内容だ。"

show emi excited_happy
with charachange


emi "それ考えるのナースくんに手伝ってもらったんだ"


"俺を健康にしておこうというナースの努力の数々には驚かされるな。"


"生徒にスパイ活動をさせるような保健の先生というのもあまり聞いたことがない。食事の計画を一緒に考えるなんてなおさらだ。"


"しかし、俺が今いるのは普通の学校じゃないということだろう。"


"それはそんなに悪いことではないのかもしれない。"


"でもこの食事プランによると、明日の学園祭で買えそうな食べ物はほとんど全部禁止されている。"


"うーん。"


hi "それで、ランニングはいつから始めるんだ？"

show emi basic_grin
with charachange


emi "学園祭のあと"


hi "終わってすぐ？　学園祭で俺が何か食べてたらどうする？　腹が痛くなるだろ"

show emi basic_annoyed
with charachange


emi "学園祭の次の日のことだよ"


hi "わかってるよ、そんなの"


"俺たち、何かやることがあったんじゃなかったか？"


hi "そうだ！　琳にペンキを持って行かないといけないんじゃないか？"

show emi basic_shock
with charachange


emi "あっいけない！　忘れてた！"

stop music fadeout 8.0

scene bg school_dormext_half_ss
with shorttimeskip


"ペンキを持って壁画のところまで帰る頃には、琳はすでにどこかへ消えていた。"


"まあ仕方ない。"


"笑美と俺はここで別れることにして、ペンキは地面に置いていく。"


"琳が見つけるだろう。いつにせよ、とにかく帰って来れば。"

scene bg school_dormhisao
with locationskip


"学園祭は明日だ。実は俺も少し興奮している。"


"同時に、今日までの間に相当疲れているのも確かだ。少し本を読んでからベッドに潜る。"

$ suppress_window_after_timeskip = True

scene black
with Dissolve(3.0)


label jp_A34b:



stop music fadeout 1.0


"くそ、なんでみんな俺の問題に口出ししようとするんだ？　ナースは許可されてるというか、むしろそれが義務なんだろうけど……"


hi "あのな、そういうのはよくないと思うんだ"


hi "俺の問題だから、他の誰にもあまり関わって欲しくないんだよ"


hi "自分で解決しないといけないんだ"

show emi sad_depressed
with charachange


emi "昨日のことを怒ってるの？"


"笑美は頬を膨らませていて、どこか傷ついた子犬のように見える。怒りたくたって、怒れるわけがない。"


hi "いや、そんなんじゃない。どちらかといえば、俺の責任だし"


"壁に背を預けて、笑美から顔をそらす。"


hi "ただ……わからないけど、なんかまずい気がするんだよ"




label jp_A35:

scene bg school_scienceroom at bgleft
show hanako emb_downtimid at right
with None


"だけど、リリーはどうして彼女を置いていったんだろう？　華子の反応からして、いつもと様子が違うようだったけど。"


"……"


"……あ、そうか。琳と俺たちがばったり会う前に、今日は町に行くんだってリリーが話してたっけ。"


"あのときの散歩を思い出して、外を見る。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene bg misc_sky at Fullpan(15.0)
with locationchange


"うららかな日差しに、午後のひとときを楽しみながら散歩している人たちがちらほら見える。その光景に、学園から出かけたいという気持ちが強まる。ここに座っているだけじゃなくて、何か別のことをしたい。"


"俺は最大の欠点――先送りぐせ――に負け、歴史は日曜に勉強するのが一番だと決める。あるいは月曜。今日以外ならどの日でもいい。"


"うめき声を上げながら、勢いをつけて椅子から離れる。健二と過ごすべきかどうか、短く自分に問いかける。"


"あいつは『いい天気だから外で皆と楽しむ』タイプの人間じゃない。間違いなく。また後で会えばいいか。"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_scienceroom at bgleft
with Dissolve(1.5)


"方針を変えて華子と話をしようか、という考えを少しだけ頭の中でもてあそぶ。でも、華子の席を見るとすでに空っぽだった。図書室に向かったに違いない。"



label jp_choiceA35:
menu:
    with menueffect
    "何か暇つぶしのネタがあるはずだ……"
    "町に散歩に行く":




        return m1
    "図書室に行く":


        return m2

label jp_A35a:


"華子を追いかけて図書室に行くのは少しおせっかいすぎる。やっぱり、華子が教室を離れる理由はあったわけだし。"


"それはそれとして、リリーとは話をしておきたい。そして、せめてお礼を言いたい。学級委員としての大変な役目もあったのに、俺の世話をしてくれたんだから。"


"町を散歩してみようか。運がよければリリーを見つけることができるはずだ。いい運動にもなるだろう。"

play music music_tranquil fadein 3.0

scene bg school_courtyard
with locationskip


"門を目指して、学校の中庭を歩いていく。通りがかった数人の同級生に軽く頭を下げると、同じように会釈が返ってくる。"


"運動部のかけ声がここまで聞こえる。この騒々しさからすると、グラウンドは今、人であふれているに違いない。"



"リリーが昨日言っていたことを思い出す。俺は学園祭で忙しい中に放り込まれたのだと。"


"俺が自分の立ち位置を探り、勉強の遅れを取り戻そうとしている間、他のみんなはいつも通りの校内活動をしている。よそ者だという感覚はまだ拭いきれない。少なくとも、今は。"


"まあ、何もかもが嫌ってわけじゃない。"


"ここが私立学校だということは、外を歩けばすぐにわかる。単に敷地が大きいだけでなく、建物自体が汚れもなく清潔で、公立の安っぽいブロック作りの建物とはかけ離れている。"


"それに、ここでは人とのより強いつながりも感じる。少なくとも、親しみやすい雰囲気がある。前の学校は、仲間内でグループになっていればいいという感じだった。"

scene bg school_gate
with locationchange


"そうするうちに門にたどり着き、町へ向かって歩き出す。"

scene bg suburb_roadcenter
with shorttimeskip


"まあ、これは結構有意義だった。"


"町のかなりの部分、町外れの丘の上にたたずむ家さえも見て回る。帰る前に、公園のまわりを散歩しようと思い立つ。"


"ずっと都会に住んでいたから、こぎれいな服のビジネスマンや、着飾った女の子がまったくいないことにかなりの違和感を感じる。"


"目に映るのは、歩道で足を引きずっている風変わりなお年寄りと、小さな店の軒先で熱心に世間話をしているおばさんたちだけだ。"

stop music fadeout 8.0


"公園へ続く道を歩いていると、すぐにその人たちからも気が逸れる。でもそのせいで、周りのものをできるだけ見ようと無理しすぎたかもしれないと気づく。"


"息がゼイゼイといいだし、胸がますます締めつけられる。これ以上頑張るのはやめよう。"

play ambient sfx_parkambience fadein 1.0

scene bg suburb_park
with locationskip


"公園に入るとざっと辺りを見回し、二台ならんだ自動販売機の近くにある、ぐらつくベンチを見つけて座る。"


"数分間ずっと座ったままうつむき、無理矢理深呼吸をする。青春真っ盛りの十代というより、老人になった気分だ。"


"入院生活や手術、薬物治療のせいに違いない。くそっ。"


"そうするうちに呼吸は正常になり、胸の筋肉も緩む。俺は少なからずほっとする。とりあえずは、これで一時休憩も終わりというわけだ。"

stop ambient fadeout 1.0

scene bg suburb_shanghaiext
with locationchange


"遠くの角に喫茶店がある。じゃあ、のども渇いてるし寄っていくか。"

play sound sfx_storebell

scene bg suburb_shanghaiint at bgright
with locationchange

play music music_dreamy fadein 2.0


"ドアの上の小さなベルが鳴り、誰もいないカウンターに俺が来たことを合図する。"


"立ったまま、少しの間待つ。時々、カウンターの端から端まで目をぼんやりと動かし、呼び鈴を探す。"

show yuukoshang neutral_down at center
with charaenter


"そのうちに、カウンターの少し後ろにあるドアが開く。現われた人物に、俺はとても驚いてしまう。"


hi "ゆ……優子さん？"


hi "こんにちは。ここで働いてるなんて知りませんでしたよ"


"優子さんをどう呼べばいいのか、さっぱりわからない。理屈の上では学園の職員だけど、どうやらここのウェイトレスでもあるようだし。"

show yuukoshang neurotic_up
with charachange


yu "あー、うん、えっと……"


"優子さんは急いでカウンターに立ち、上半身を思いきり下に放り出して大げさなおじぎをする。"

show yuukoshang closedhappy_down
with charachange


yu "上海にようこそ！　ご注文はお決まりですか？"


"いきなり注文とるのか。なるほどな。"


hi "どうしようかな……じゃあ、コーヒーをもらえます？"

show yuukoshang neutral_down
with charachange


yu "かしこまりました。すぐにご用意いたします"


hi "えーと、ありがとうございます"


"優子さんの堅苦しさにはびっくりだ。とても真面目に仕事をしているらしい。"

hide yuukoshang
with charaexit


"優子さんに案内されながら、空いているテーブルがないか振り返ってざっと見まわす。他に客はいないわけだし、簡単な話だ。"

show bg suburb_shanghaiint at bgleft
with charamove


"窓際のテーブルに向かう途中、席の仕切りのそばで黄色の何かが目に飛び込む。"

show lilly basic_smileclosed at twoleft
show akira basic_lost at tworight
with charaenter


"思った通りだ。一目見れば、テーブルについているのがリリーだと十分わかる。とは言っても、リリーの向かいに座っているスーツ姿の人には見覚えがない。"


"金髪で肌が白く、少し背の低い彼は……彼女か？　彼女だろう。リリーの身内に違いない。"


"スーツの人がコーヒーをひと飲みしてから二人とも黙っているので、リリーに声をかけようと決める。そもそも、ここに来たのは彼女に会うためでもあるんだから。"


hi "やあ、リリー"

show lilly basic_smile
with charachange


li "……久夫さん？"


hi "ああ。また会ったね"

show akira basic_smile
with charachange


"スーツの少女は俺を見上げ、穏やかな笑顔で俺の制服に目をやる。"


aki_ "知り合い？"


hi "た……たぶん"


"俺とリリーの関係を表すのに、それより正しい言い方は思い浮かばない。"

show lilly basic_smileclosed
with charachange


li "あの……お掛けになりませんか？"


"リリーは俺ではなく、その横の空間に向かって言う。でも言いたいことは伝わったので、俺はリリーの横に座る。"

show lilly basic_weaksmile
with charachange


li "紹介しないといけませんね"

show lilly basic_smile
with charachange


li "久夫さん、こちらは砂藤晃、私の姉です。姉さん、こちらは中井久夫さん。山久学園の学生なの"


"俺の予想は正しかったようだ。改めて紹介された晃さんは会釈をくれ、俺もそれに答える。"


"でも、俺を分析するかのような晃さんの視線に、俺は答えない。"

show lilly basic_smile at left
show akira basic_smile at right
with charamove

show yuukoshang neutral_down at center
with charaenter


"晃さんがそうしているうちに、優子さんがテーブルまで来る。コーヒーを慎重にテーブルに置き、おじぎをして去っていく。"

hide yuukoshang
with charaexit

show lilly basic_smile at twoleft
show akira basic_smile at tworight
with charamove


"カップの両側にそっと手を触れてみると、すでに飲むのにちょうどいい温度だ。一口飲むと、風味もいいことがわかる。"


"優子さんは、司書よりもこっちのほうが向いているようだ。"


"じっくりと飲んでから、椅子にもたれてくつろぐ。"


"晃さんの分析はすぐに終わる。どうやらすぐに飽きてしまったらしく、彼女はリリーのほうを向く。"

show akira basic_boo
with charachange


aki "それで、最近学校はどう？"


"二人の会話を聞いていると、晃さんは知らない人にはまったく無関心らしい。"


"別に構わないけど。俺は二人の邪魔をせずに身を引き、香りのいいコーヒーをくつろいで飲み続ける。"

show lilly basic_smileclosed
show akira basic_smile
with shorttimeskip


aki "話聞いてると、結構忙しいみたいじゃん？"

show lilly basic_smile
with charachange


li "もう姉さんのご飯は作らなくてもいいのにね"


"二人が話すにつれて、だんだんわかってきたことがある。目を見てリリーの感情を判断しようとしても、まったくできないということだ。"


"無意識にそのことを思うと、少し居心地が悪くなる。"

show akira basic_lost
with charachange


aki "うわ、冷たいなあ。どうせ自分の分だけ料理してたんじゃないの？　あたしは残り物をもらってただけでさ"

show lilly basic_displeased
with charachange


li "そうじゃなくて……ねえ、一人でちゃんと食事できてるの？"

show akira basic_resigned
with charachange


aki "当たり前さ。料理してるときに爆発なんてしないよ"

show akira basic_annoyed
with charachange


aki "大体は"

show lilly basic_listen
with charachange


li "それって……"

show akira basic_laugh
with charachange


aki "ははは！　いいよいいよ。どうせそのうち練習しなきゃいけなかったんだから"

show lilly basic_listen at left
show akira basic_laugh at right
with charamove

show yuukoshang neurotic_up at center
with charaenter


yu "あの、リリー？"

show lilly basic_smile
show akira basic_boo
with charachange


"優子さんが来て、そこにいるみんなの気が逸れる。リリーのために１杯の紅茶がテーブルに置かれる。"

hide yuukoshang
with charaexit

show lilly basic_smile at twoleft
show akira basic_boo at tworight
with charamove


"晃さんは時計をちらりと見て席から勢いよく立ちあがり、俺に会釈をする。"

show akira basic_smile
with charachange


aki "それじゃ、もう行かないと。話せてよかったよ、リリー"

show lilly basic_oops
with charachange


li "姉さん、まだいいでしょう……？"



"リリーはお姉さんが急に帰ってしまうことを心底悲しんでいるようだ。もう二度と会えないとでも思っているように見える。"

show akira basic_resigned
with charachange


aki "ごめん、もう仕事に戻らなきゃいけないんだ。さっさと戻らないと、ゴチャゴチャうるさいからさ"


"とてもくだけた話し方だ……晃さんのきちんとした身なりからは、誰も想像できないだろう。"

show lilly basic_concerned
with charachange


li "さよなら、姉さん……"

show akira basic_smile
with charachange


aki "ほら、そんな暗い顔するんじゃないの。またそのうちに来るからさ。じゃあね"

hide akira
with charaexit


"そう言って晃さんは片手を高く上げ、上海から軽快に出ていく。"


"リリーはまだかなり落ち込んでいるようだ。俺はリリーの気を紛らわすために、何かおしゃべりをしようと試みる。"

show lilly basic_concerned at center
show bg suburb_shanghaiint at center
with charamove


hi "いいお姉さんみたいだね"

show lilly basic_displeased
with charachange


li "私たち、一緒に暮らしていたんです。でも、今は私が学園に住んでいるのでめったに会えないんですよ"


"リリーとはとても話しやすいのに、俺はまだ彼女のことをよく知らない。今考えると、リリーが俺からいろいろ聞き出したことには驚かざるを得ない。"


hi "一緒に住んでたの？　この辺のどこか？"


li "ずっと南のほうです。さすがに山久学園に通うには遠くて"

show lilly basic_reminisce
with charachange


li "そのことと、姉さんの仕事時間が長くなったこともあって、最終的に寮に引っ越すしかなくなったんです"


"なるほど、それで料理の話をしていたのか。どうやらリリーは落ち着きを取り戻したらしく、元気になったようだ……まあ、それなりに。"

show lilly basic_weaksmile
with charachange


li "もう体は休まったみたいですね"


hi "なに？"

show lilly basic_smileclosed
with charachange


li "最初に入ってきたときよりも息が落ち着いたようですし"


"俺の呼吸をそんな風に聞き分けられるなんて……リリーの耳はとても良いに違いない。"


hi "ああ。ちょっと散歩するだけのつもりだったのに、結局町中を歩いちゃったよ"


"散歩の話でのどの渇きを思い出し、一口飲むために身を乗り出す。"

play sound sfx_teacup


"そして、リリーも香りの強い紅茶に口をつけ始める。"


"もう学園に戻ったほうがいいかもしれない。いつまでも勉強を後回しにすることはできないし、学園祭の前にはちゃんと寝ておきたい。"

stop music fadeout 4.0


"椅子から立ち上がり、テーブルからコーヒーの染みの付いたカップを取る。"

show lilly basic_surprised
with charachange


li "帰るんですか？"


hi "うん。リリーも戻る？　時間も遅くなってるし"


"リリーは少し待って、ティーカップの上に身を乗り出す。俺を見ているかのようだ。"

play music music_lilly fadein 3.0

show lilly basic_smile
with charachange


li "優子さん、コーヒーをもう一杯もらえますか？"


yu "いいわよ、すぐもっていくね！"


hi "わかりやすい……やり方だね"

show lilly basic_giggle
with charachange


"リリーはその作戦に対する率直な意見にくすくすと短く笑う。彼女の落ち着いた容姿からすると、それは驚くほど子どもっぽく、屈託がない。"


"まあ、俺には断る理由がほとんどない。正直、どう考えてもノーとは言えない。"


"わざとらしくため息をついて、俺はリリーの向かいの席に座る。"


hi "話し相手が欲しかったの？"

show lilly basic_cheerful
with charachange


li "うーん……ちょっと聞きたいことがある、とでもいいますか……"


"また質問モードに入っているらしい。いつになく俺に興味を持っているみたいだ。さもなければ、好奇心かもしれない。"

show lilly basic_smile
with charachange


li "ご兄弟は何人いらっしゃるんですか？"


"そんなに意外な質問でもないな。"


hi "いや、一人っ子だよ。正直、そんなに近い関係の人がいるってだけでうらやましいよ"

show lilly basic_smileclosed
with charachange


li "なるほど……"


"俺は眉を上げるけど、もちろん見られてはいない。短い沈黙が、俺の問いかけを十分に伝えてくれる。"

show lilly basic_smile
with charachange


li "前にも他の人たちにそう言われたことがあるんですよ"


li "私のそばにはずっと姉がいたので、客観的に考えてみるのはなかなか難しいですね"


"リリーの言いたいことは大体理解できる。生まれ育った環境と別の立場に自分を置いてみるのは難しいんだろう。"


"彼女たち姉妹はかなり仲が良いに違いない。"


"できるだけ俺たちの邪魔にならないように優子さんがうやうやしくやってきて、テーブルにカップを一つ置く。"


"リリーが優子さんにお礼を言うそばで、俺はくつろぎながらこの目の前の一筋縄ではいかない子を眺める。"


"いつも隙がなくて、他人と話すときは理性的に自分をコントロールしてる感じだけど、子どもみたいな好奇心も持っているんだな。"


"とはいえ、リリーもごくたまに心の内をのぞかせることがある。それは彼女の考え方に迫ることができる絶好のチャンスだ。"


"目の前にある自分の飲み物に手を伸ばし、もっと早く気づくべきだったことに気づく。"


"……俺はリリーのことを知りたいと思い始めている。"

stop music fadeout 2.0

scene bg school_gate_ni
with shorttimeskip

play ambient sfx_cicadas fadein 0.5


"かなりのペースだったのに、学校の大きい鉄製の正門に着いた時にはもう日が暮れている。"


"学園のすぐ隣に住むことでぶらぶらできる時間がたっぷりあるのはうれしいけれど、そうできる生徒はほとんどいないんだと感じずにはいられない。"

scene bg school_courtyard_ni
with locationchange


"空き時間に校内を行き来している生徒の数に比べると、町中では驚くほど人を見かけない。"


"学園にあるかなりの数の宿泊設備と施設を考えると、多くの生徒は外に出ること自体にあまり意味を感じないのかもしれない。まして、華子や健二みたいなタイプは言うまでもない。"


"そう考えると、静音やミーシャ、リリーのような生徒はこの学校ではむしろ例外なのだろうか。"

stop ambient fadeout 1.0
scene bg school_dormhallway
with locationskip


"寮の部屋にぶらりと戻りながら、俺は前の学校と山久学園を比べ続ける。そうするほどに、これまでに起こったいろんなことにここまで慣れてしまった自分に驚く。"

$ suppress_window_after_timeskip = True

scene black
with Dissolve(3.0)




label jp_A36:

window hide None

scene black
with dissolve

play sound sfx_doorknock

scene bg school_dormhisao
with openeye

window show


"８時５分過ぎ、バンバンと何かを叩く音が聞こえてくる。信じられないくらい大きな音に俺は飛び起きてしまう。ドアの外からだ。"

scene bg school_dormhallway
show shizu behind_blank at tworight
show misha hips_smile at twoleft
with locationchange

play music music_comedy fadein 0.3


"すぐにドアを開けると、静音とミーシャが目の前に並んでいる。二人とも少し疲れているように見える。ミーシャのくたびれ具合の方が目立っているけど。"


hi "今ノックしたのはどっちだよ？"


"建物の中にいる人全員が思ったであろう問いを、俺は尋ねる。"

show misha hips_grin
with charachange


mi "あははは、そんなのどうでもいいじゃん、ひっちゃん！"


"ミーシャは顔色ひとつ変えず、あっけなくスルーする。"

show misha hips_smile
with charachange


mi "あれぇ？　ひっちゃん、まだパジャマ着てるの？　もう８時なのに起きないんだ？"


"ミーシャの髪が湿っているのに気づく。あの巻き髪もかろうじて形を保っている。"


hi "まあな。せっかくの週末だし、少しゆっくり寝ようと思ってたんだ。今週はマジで睡眠不足だったし"


"今の皮肉はちゃんと通じただろうか。"

show shizu basic_normal2
with charachange


shi "……"

show misha hips_grin
with charachange


mi "じゃあちょうどいいわ！　わたしたち、起こしに来てあげたんだから！"

show shizu adjust_happy
with charachange


shi "……"

show misha sign_smile
with charachange


mi "それはおいといて、ひっちゃん、どうしてわたしたちがここに来てるのか、知りたくない？"


"予想はつくけど、できればその先は言ってほしくないなあ。"

show misha perky_smile
with charachange


mi "授業さぼって、いっしょにいいとこいかない？"


hi "なんですと？"

show misha hips_smile
with charachange


mi "授業さぼって、いっしょに楽しいことしない？"


"俺はてっきり、こいつらがまた奴隷労働を俺に強いるとばかり思っていたんだけど。"


hi "マジで？"

show misha hips_grin
with charachange


"ミーシャはにっこり笑い、大げさにうなずく。"


"この斬新なアプローチは気に入った。ただ授業をさぼるという提案がこの二人から出てくることにはちょっと驚く。いくら土曜日で半日しかないからって。"


hi "二人ともそんなにしょっちゅう授業さぼって、気にならないのか？"

show shizu behind_smile
with charachange


shi "……"

show misha perky_smile
with charachange


mi "問題にはなってないみたいよ！　ひっちゃん、今の時期になると学校もほとんど動きがなくなるの"

show misha hips_smile
with charachange


mi "それに今日は土曜日だよ～。楽しいことしたくないの？"


"二人が全く気にしていないことに、俺は驚愕する。"

show shizu adjust_smug
with charachange


shi "……"

show misha perky_smile
with charachange


mi "別に無理に来てくれっていうわけじゃないけど、ただ一緒に遊んでくれるかなって思ったの！"

show shizu behind_blank
with charachange


shi "……"

show misha hips_smile
with charachange


mi "で……どう？　一緒に行かない？　ねえ行こうよ、机に頭乗っけて座りっぱなしより、ずっと楽しいよ～！"


"別に大事な授業を聞き逃すってこともないだろうし、俺がいなくて誰かが困るってこともないだろう。"


hi "じゃあわかったよ。大した授業もないし。何するつもりなんだ？"


"ある疑いが脳裏をかすめて、俺は目を細める。"


hi "待てよ……また俺に生徒会の仕事をやらせるための引っかけじゃないだろうな？"

show shizu basic_angry
with charachange


shi "……"

show misha perky_confused
with charachange


mi "違うわよ、そんなわけないでしょ！"

show misha hips_frown
with charachange


mi "そんな風に考えるのって、すっごく意地悪だよ、ひっちゃん"

show shizu behind_frown
with charachange


shi "……"

show misha hips_smile
with charachange


mi "……それに、あなたはもう生徒会に入ってるのよ。忘れたの？"

show misha hips_grin
with charachange


mi "何かやってほしいと思ったら、わざわざだます必要なんてないもんね～！"

show misha hips_laugh
with charachange


mi "ははは！"

show misha hips_smile
with charachange


"こういうふうに圧力をかけられるのは初めてだ。かわいい女子の二人組でなければ、こんなことはできない。"

stop music fadeout 3.0


"俺は少し気を緩める。心配しすぎかもしれない。どうやら二人とも本当に俺と遊びたいだけみたいだ。"


"とはいうものの……"


hi "仕掛けとかはないんだな？"

play music music_shizune fadein 4.0

show shizu basic_angry
with charachange


shi "……"

show misha hips_grin
with charachange


mi "ないわよ！　いいかげんにしなさい！"


hi "まあ、そこまで言うなら"


"不意に、自分がまだパジャマを着ていることに気づく。"


hi "先に着替えさせてくれるか？"

show shizu adjust_smug
with charachange


shi "……"

show misha hips_smile
with charachange


mi "えー？　どうして、ひっちゃん？　その格好、ばっちりだよ！"


hi "それでもこの格好じゃないほうがいいんだよ。俺は"

play sound sfx_doorclose

scene bg school_dormhisao
with locationchange


"ミーシャに返事をする隙を与えずに俺はドアを閉め、さっさと制服を身につける。"

play sound sfx_dooropen

scene bg school_dormhallway
show misha perky_smile at twoleft
show shizu basic_normal at tworight
with locationchange


"廊下に戻ると、静音とミーシャが熱心に話し合っているのが見える。"


"手話で会話している人は、うっかり相手の目をつついたりはしないのかな。"

show shizu behind_frown_close
with characlose


"そんなことを考えていると、静音がいらだたしげに俺の肩を叩く。"


shi "……"

show misha hips_smile
with charachange


mi "じゃあ、ささっと町まででかけるよ！　水曜日に行ったお茶屋、覚えてる？"


hi "お茶屋？"

show shizu behind_frustrated_close
with characlose


shi "……"

show misha perky_confused
with charachange


mi "覚えてないの？"


hi "ああ、あの喫茶店か"

show misha hips_smile
with charachange


mi "お茶屋！　上海っていうのよ。中国はお茶の発祥の地ですからね。行こ、ひっちゃん！　なんと今日はわたしがおごってあげる！"

show misha hips_grin
with charachange


mi "あー……わたしじゃない、わたしじゃないよ、じゃなくてしっちゃんがね！　あはは～！"


hi "ちょっとなあ……"

show misha sign_smile
with charachange


mi "いいとこだって、すごく落ち着くよ！　なんていうか……半分喫茶店で、半分レストランで、半分おしゃれで、半分……図書館で……"


"なに？"


hi "ずいぶん半分が多いな"


"でもミーシャは気づいていないようだ。"

show misha hips_smile
with charachange


mi "だから～！　行こうよ、こんなに時間が余ることってめったにないんだから！"

show shizu adjust_smug_close
with charachange


shi "……"

show misha hips_grin
with charachange


mi "でも忙しいんだったら、無理にとは言わないわ！　絶対に絶対にひっちゃんがいなきゃいけない、ってわけじゃないから！"

show misha cross_laugh
with charachange


mi "はははは！"

show misha cross_grin
with charachange


"こんな見え見えの挑発作戦は今まで見たことがない。今日はなんだか疲れてるし、先生方が俺の行方を探してるかもしれない。もしかしたら。"


"一方で、俺は転校して以来一度もまともに町に出たことがない。だから出かける理由としてはちょうどいい。"


"それに何か食べたいと思っていたところだ。静音のおごりならなおさらいい。今は完全に金欠だし。"


hi "わかったよ、じゃあ行こう。道案内よろしくな"

show misha hips_smile
show shizu behind_smile_close
with charachange


mi "やった～！"

stop music fadeout 2.0

scene bg suburb_shanghaiint
with shorttimeskip


"３０分ほど歩いて、お茶屋にたどり着く。客は俺たちだけみたいだ。"

play music music_another fadein 2.0

show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charaenter


hi "朝はいつもこんなに静かなのか？"


"つまり、いつもこんな感じで閑古鳥が鳴いてるのかってことだ。"

show shizu basic_normal
with charachange


shi "……"

show misha perky_confused
with charachange


mi "ちがうわ、なんだか変。ねえ、でも悪い話じゃないんじゃない？"


hi "そうだな"

scene ev shizu_shanghai
with locationchange


"俺たちは大きな木製のテーブルの席につく。そこで俺はこの店が何を出すのか知らないことに思い至る。"
"前に来たときは、ただ優子さんのおすすめを頼んだだけだった。"


hi "なあ、メニューとかないか？"

scene ev shizu_shanghai_normallaugh
with charachange


mi "ないよ！"


"ずいぶん気合いの入った返事だな。"

scene ev shizu_shanghai_smirklaugh
with charachange


shi "……"

scene ev shizu_shanghai_smirknormal
with charachange


mi "で、ひっちゃん、注文は決まったの？"

scene bg suburb_shanghaiint at Fullpan(8.0)
with locationchange


"店内を見回しても、メニューのようなものは全く見あたらない。"


"わけわかんねえよ、この店どうなってるんだ？　なんなんだよ？"


"秘密の店とか、そういうのか？　普通なら秘密の握手をしないと中には入れないとか？　それともウインクしたりうなずいたりとか？"


"誰かの紹介がないとだめなのか？　血の誓いでも立てろってのか？　くそ、この前とは全然様子が違うじゃないか。"

scene ev shizu_shanghai
with locationchange


hi "どうするかな、前はコーヒーしか頼んでない気がするけど？　ここでは何を出すんだ？"

scene ev shizu_shanghai_smirknormal
with charachange


shi "……"

scene ev shizu_shanghai_smirklaugh
with charachange


mi "お茶！"


hi "いや、まあ、そりゃ……"


hi "お茶だけじゃないだろ？　お茶だけってことは、なあ？　他のものだってあるだろ？"

scene ev shizu_shanghai_normallaugh
with charachange


shi "……"

scene ev shizu_shanghai
with locationchange


mi "そりゃそうよ～！"


hi "そりゃそう、って？　何がそうなんだよ？　メニューもないじゃないか。メニューはどこだよ？"


"またこいつらは悪ふざけをしてるんだ。逃げ場はない。俺にできるのは、覚悟を決めてふりかかる仕打ちに耐えることだけだ。"


"もう店から出たくなってくるけど、でも俺はもう座ってしまっている。"


"今出ていくのは不作法だ。お行儀のいい振る舞い方、という暗黙のルールが、炎の壁のように俺の脱出を阻む。"


"俺は様子を見ることにする。こいつらの注文した物を頼もう。男が頼んでも変じゃないものなら、だけど。"


hi "二人とも先に頼んだら？　レディーファーストでさ"

scene ev shizu_shanghai_smirknormal
with charachange


shi "……"


mi "うまく逃げたわね、ひっちゃん。でも～、わたしたちもう注文してあるんだ！"


hi "どうすりゃそんなことができるんだ？　どうやって？　誰に？"


mi "わたしたちは常連で、しょっちゅうここに来てるから、もうわざわざ注文しなくてもいいの！"

scene ev shizu_shanghai
with charachange


shi "……"


mi "まあ、このくらいで勘弁してあげる。メニューならわたしたちが下敷きにして座ってるに決まってるじゃない～！"

scene ev shizu_shanghai_normallaugh
with charachange


mi "ははは！"


"他のテーブルを見渡してみる。メニューはどこにもない。つまり、ドアの近くかどこかにまとめて積んであるに違いない。"
"なんてものの上に座ってるんだ。それにどういう素早さで回収したのか。"


hi "まあどうでもいいけど。じゃあ一つもらってもいいか？"

scene ev shizu_shanghai_smirklaugh
with charachange


shi "……"

scene ev shizu_shanghai_smirknormal
with charachange


mi "取りたければ取ってもいいわよ。でもひっちゃんはそんな、わ……い……せつ？　なことする人じゃないわよね？"


"俺はコーヒーだけでいいと二人に告げて、冷たいテーブルの上に突っ伏す。"

scene ev shizu_shanghai_borednormal
with charachange


shi "……"

scene ev shizu_shanghai_boredlaugh
with charachange


mi "コーヒー？　ここはとても高級なお店なのよ。それなのにコーヒーなんて頼むつもり？"


"こいつら、またなんか企んでるな。"


hi "だったら、お前と同じのにするよ"

scene ev shizu_shanghai_smirklaugh
with charachange


shi "……"

scene ev shizu_shanghai_smirknormal
with charachange


mi "ひっちゃん、しっちゃんはインドの奥地でしか採れない、特別な紅茶を飲むんだよ"


mi "紅茶作りの部族が今でも手作りで作ってて、作り方は何世代も前から受け継がれてきたんだよ"


mi "一年に一回、ワニだらけの川を渡って葉っぱを取りにいかないといけないの。出かけるたびに、生きて帰ってこられない人が出るんだよ"


"そんなの飲めない。後ろめたすぎる。"


hi "じゃあお前と同じのにする"

scene ev shizu_shanghai_smirklaugh
with charachange


mi "わたし、何飲むかわかんない"


"わからないってなんだよ？"


hi "じゃあいいさ、その死人が出るっていうお茶にするよ"


hi "いや、今のなし。コーヒーにする"


hi "ここがそんなに高級な店だっていうなら、コーヒーだって高級なはずだよな？　……誰も収穫するのに死んだりしてない、よな？"

scene ev shizu_shanghai
with charachange


"完璧な答えだ。これなら突っ込む余地なんてないだろう。『やるじゃない』とでも言いたげに静音は肩をすくめる。"


"二人とも二つ目の質問には答えてないけど。"

scene bg suburb_shanghaiint
with locationchange

show yuukoshang neutral_down at center
with charaenter


"ミーシャは優子さんを呼ぶ。"
"優子さんは飲み物と、小さな黒いプラスチックのフォークが刺さった、びっくりするほど小さな黄色いケーキを一つずつ、俺たちに運んでくる。"

hide yuukoshang
with charaexit


"俺は一口でケーキを飲み込む。こんなに食べがいのない食べ物は生まれて初めてだろうな、と感心する。"

show shizu behind_blank at Slide(0.2,0.5,0.3,0.5,1.0)
show misha perky_smile_close at Slide(0.8,0.5,0.7,0.5,1.0)
with Dissolve(1.0)

stop music fadeout 3.0


mi "ひっちゃん、明日は何か予定ある？"


"ミーシャはお茶をごくりと一口飲む。ごく普通のお茶に見えるけど、その音はうさんくさいくらい高級そうに聞こえる。"


"あんなに熱そうな飲み物を、ミーシャはものすごくがさつに飲む。静音やリリーとは正反対だ。"


"予定？　なんか不吉な響きだな。"

play music music_running fadein 8.0


hi "予定？　あるよ"


hi "そう、明日はものすごく忙しいんだ。実はやることが多すぎて、もう空いてる時間なんて全然なくってさ"


hi "そうだ……全然ひまがないんだ。しかもやらなきゃいけない用事はどれもすごく重要なんだ。とにかくものすごく重要なんだよ"

show misha hips_grin_close at tworight
with charachange


"ミーシャはけらけらと笑う。あきらかに信じてない。それを静音に手話で伝えると、静音はとても面白くなさそうな様子でゆっくりとうなずく。"

show shizu basic_normal_close at twoleft
with characlose


"突然、静音はこっちによりかかると、俺をあの分析するような目でじっとにらむ。まるで人間嘘発見器のように、俺がささいな隙を見せてぼろを出すのを待ちかまえている。"


"少なくとも一分はたった後、静音は座り直してお茶を一口飲む。"

show shizu behind_blank
with charadistant


shi "……"

show misha perky_smile_close
with charachange


mi "おっけー、ひっちゃん、そんなに忙しいんだったらしょうがないね。わたしたち明日は何も用事がないから、学園祭に一緒に行きたいかなって思ったんだ！"

show misha sign_smile_close
with charachange


mi "転校してすぐなんだし、ね？　ね？　だから～、わたしたちがあちこち案内して、一緒に楽しいことしようって思ったんだけど、そこまで忙しいんだったらしかたないよ！"

show shizu adjust_happy
with charachange


shi "……"


mi "まあまあ、いいけどね！"

show misha cross_grin_close
show shizu basic_normal2
with charachange


"二人とも完璧に同じタイミングで肩をすくめる。前もって練習でもしたかのように。"

show misha cross_laugh_close
with charachange


mi "あははははは～！"

show misha cross_grin_close
with charachange


mi "ひっちゃん、ほんと心配しすぎだよ"

show shizu adjust_smug
with charachange


shi "……"

show misha cross_smile_close
with charachange


mi "……そもそもひっちゃんがわたしに勝てるわけないんだから、そんなにがんばったってしょうがないでしょ？"

show misha cross_laugh_close
with charachange


mi "はは！　すごいこと言うね、しっちゃん～！"


hi "お前に勝つって？　何言ってるんだ？"


"仕事を押しつけることを言ってるのか？　これは静音にとってゲームでしかないのか。全然気づかなかった。競争だと思ってるのは俺だけだと思ってたのに。"

show shizu basic_happy
with charachange


shi "……"

show misha hips_grin_close
with charachange


mi "わかってるくせに～！　……え？　ひっちゃん、わかってるの？　わたしはわかんないよ"

show shizu adjust_smug
with charachange


shi "……"

show misha hips_smile_close
with charachange


mi "わたしを出し抜くなんて無理よ！　あー、えっと、ひっちゃん、わたしじゃないから……"

show shizu basic_sparkle
with charachange


shi "……"

show misha perky_confused_close
with charachange


mi "なに？　何のこと言ってるの、しっちゃん……"


"静音がずる賢そうに笑って、精神力と知恵の勝負に俺を誘っているのが見える。"


"絶望の淵に立たされたとき、男ははかない希望の切れ端をつかみ、避けがたい運命に全力で戦って不可能に立ち向かわなくてはならない。さもなければ、沈むしかないのだ。"


"たとえ失敗したとしても、自分が勇敢に立ち向かったことだけは、心にとどめられるのだから……"


"……とかなんとか。"


hi "まあ、それはやってみなきゃわからないさ。俺をなめるなよ"

show shizu behind_blank
with charachange


shi "……"

show misha perky_smile_close
with charachange


mi "じゃあひっちゃん、その言葉が本当か、確かめてみる？"


hi "いやまあ、まぐれってこともあるかもしれないだろ。その可能性は無視しないほうがいいぞ"

show shizu adjust_smug
with charachange


shi "……"

show misha cross_grin_close
with charachange


mi "それはないわ～"


hi "あるっての！　待てよ――"

show shizu basic_happy
with charachange


shi "……"

show misha cross_smile_close
with charachange


mi "それじゃあ、賭けをしましょう！"


hi "俺は勝ち負けなんてどうでもいいんだよ"


"今のはあからさまな嘘だ。"


hi "いや待てよ、それどういう意味だ？"

show misha cross_laugh_close
with charachange


mi "わかんなくても大丈夫だよ、わたしもわかんないから！　わははは！"

show shizu basic_normal2
with charachange


shi "……"

show misha perky_smile_close
with charachange


mi "じゃあ決まりね！　よしよし！"


hi "はあ？　お前、俺が今言ったこと聞いてなかったのか？"

show shizu adjust_happy
with charachange


shi "……"

show misha sign_smile_close
with charachange


mi "じゃああとは何を賭けるか決めるだけね！　勝ったほうの賞品と、いいえ、もっと面白いのは負けたほうの罰！"


hi "おい！"


"これはとてもヤバい勝負だ。静音がそもそもヤバい。こいつが勝ち負けでしか物事を考えないのだとすれば。"


"俺と話すたびに静音がそれを勝負扱いするのでは、俺は耐えられそうにない。"


"そういう風にされては頭がおかしくなる。静音は目的のために手段を選ばなさすぎるんだ。今までは、単に冷静なだけだと思っていたけど。"


"それでもなお、俺は興味を引かれている。考えてみれば、俺は静音になんのルールもない勝負を挑んでいたんだ、と気づく。"
"終わるのは俺たちのうちどちらかが……どうなるんだ？"


"つまりそういうことか。そこがあまりに曖昧なんだ。勝ち負けの条件はなんだ？　最初に恥をかいたほうが負けなのか？"


hi "どうだろうな。そんなの考えたことは今まで一度もないんだけど"

show misha hips_smile_close
with charachange


mi "一度も？"


hi "一度も"

show misha perky_confused_close
with charachange


mi "じゃあひっちゃんは一度も賭けをしたことがないってこと？"


hi "二人ともやったことあるのかよ。そっちのほうがびっくりだよ"

show shizu behind_blank
with charachange


shi "……"

show misha hips_grin_close
with charachange


mi "もう、固いこと言わないの……ただの遊びなんだから！　友達同士の～！"

show misha sign_smile_close
with charachange


mi "恥をかかせて苦しめて絶対的な絶望を与えるのが目的なんだから！　そういうことじゃない？"


"静音は思慮深げにこめかみに指を当てる。"

show shizu adjust_happy
with charachange


shi "……！"

show misha hips_smile_close
with charachange


mi "うーん……あ、じゃあこういうのはどうかな。ひっちゃんが負けたら、一日ズボンはかずにパンツ一丁で学校に行くの"


hi "お前ら正気か？"


"こいつらが何を言い出すかと恐れていたことに比べれば、ずいぶんおとなしいけど。"


hi "普通の人みたいにお金をかけるんじゃダメなのか？"

show shizu basic_sparkle
with charachange


shi "……"

show misha hips_grin_close
with charachange


mi "ほんとにお金賭けたら、わたしの掛け金に合わせられるわけないでしょ～！　さあ、そっちの番よ！　……でもえっちな条件は禁止だからね！　わかった？"

show misha hips_laugh_close
with charachange


mi "ははは！"


hi "ちょっと時間をくれ"


"これじゃ、俺は何週間も追い詰められっぱなしになるぞ。"

show misha hips_grin_close
with charachange


mi "おっけ～！　ほら、二人とも急ごうよ、飲み物が冷めちゃうよ！"

show shizu basic_happy
with charachange


"俺はコーヒーの残りをさっさと飲む。静音も俺を激しい競争心に満ちた目で見つめながら、同じように飲む。"


"誰かが命を落としたかもしれないお茶をそんなにあっさり飲んでしまうのは、なんだかもったいない気がする。"

show misha sign_smile_close
with charachange


mi "ひっちゃん、ほんとに明日わたしたちと一緒にでかけたくないの？　楽しみにしてる人はたくさんいるんだから。ひっちゃんだって行ったほうがいいよ"


"俺は言葉にならないつぶやきをぼそぼそという。"

show misha perky_confused_close
with charachange


mi "何言ってるのかわかんないよ……"


"今は考えるときだ。静音の飲み物は俺のより少ないが、それでも俺は静音よりも速く飲みきれる。"


"静音が先に飲みきったら、自分がおごるといったのにもかかわらず、会計を済ませずに俺に払いを押しつけて逃げるかもしれない。"


"俺はまったくお金の持ち合わせがないので、恥をかくことになる。これは負けと見なされるだろう。"


"俺が先に飲み終わってしまったら、俺はお茶屋から逃げ出して払いを静音に押しつけなくてはならない。そして騎士道精神に照らして俺はバカ野郎扱いされる。"
"これも負けと見なされるだろう。静音ならそうするに違いない。"


"引き分けの場合、静音はドアに向けて走り出すかもしれない。俺もそうするだろう。そしてドアの手前で正面衝突。屈辱ではあるけどそれほどではない……代金はミーシャが払うことになる。"


"まるでガキみたいじゃないか。俺は静音と、そして俺自身に失望する。"

show misha perky_smile_close
with charachange


mi "ねえひっちゃん、わたしたちが学園祭のためにがんばって作り上げたものを見て回って、よくやったねって言えたら、とってもすてきだと思うの……"


"自分の目の前で壮大な戦いが繰り広げられているという事実に、ミーシャはまったく気づいていないようだ。俺はゆっくりとうなずき、最後のコーヒーを飲み下す。"


hi "さて、俺は飲み終わったぞ。じゃあ俺はもう帰らなきゃ。ほんとに今すぐ帰るから。ゆっくりな"

show shizu adjust_happy
with charachange


shi "……"

show misha perky_confused_close
with charachange


mi "しっちゃんも帰るの？"


mi "二人ともなんか変だよ、どうしたの？"

scene bg suburb_shanghaiext
with locationchange


"俺は素早くドアへと歩き、静音も続く。会計はミーシャが払うはめになるけど。"

scene bg suburb_roadcenter
with locationchange


"すまん、ミーシャ。"

show shizu behind_smile at center
with charaenter


"俺に追いついた静音が、さっと眼鏡を押し上げて、紙切れを俺の手に突っ込む。"

window hide

$ written_note("そっちが負けたら、あした\n私たちに付き合うこと\n")

window show


hi "お前、今日は俺に勝てると思ってるんだろ？　ちょっと調子に乗ってないか、静音"


"俺の返事が静音には聞こえない、ということを一瞬忘れていた。俺はうなずく。"


"今この瞬間、ほのかな自信をのぞかせながら微笑んでいる静音は、普段よりもずっとかわいらしく見える。"


"静音は活発で気ままに見える。カフェインのせいかもしれないけど。"

show shizu adjust_happy
with charachange


"静音はウインクし、握手するために手を伸ばす。手にスタンガンを隠し持って俺をしびれさせるつもりじゃないか、と一瞬考える。でもそんなのは静音らしくないので、俺はその手を握る。"


"手を握ると、静音はまたメモを俺の手に押し込む。瞬間、それがスタンガンで、俺はショックで死ぬんじゃないか、という考えが脳裏に走る。"

hide shizu
with charaexit


"静音はにやりと笑い、走り去る。"

window hide

$ written_note("ここから学校に帰る道はわからないでしょ。\n\n戻ったら頼みたい仕事があるから。また後でね～")

window show


"俺は芝居がかった仕草でメモを握りつぶす。でも誰もそれを見てはいなくて、俺は悲しくなる。"


"店に戻ってミーシャに帰り道を聞くにはもう遅いだろうか、と考える。"


"でも行きの道順を知らないためにミーシャには苦労をかけた。帰り道を知らないからといって、ミーシャに借りを作るわけにはいかない。"


"それにミーシャに道を聞いてしまったら、静音はそれを勝ちと見なすかもしれない。だめだ。道案内なしでもいける。"

stop music fadeout 3.0


"学校はあのいまいましい丘のてっぺんにある。あそこに行くなんて楽勝だろう？"


"俺はちょっとばかり方向感覚が不自由かもしれないけど、このくらい俺にだってできるに決まってる。"

scene bg school_courtyard
with shorttimeskip

play music music_happiness


"約一時間半後、俺は校門から本校舎までの舗装された道を歩いている。"

scene bg school_lobby
show shizu behind_blank at tworight
show misha hips_grin at twoleft
with locationchange


mi "ははあ！　もう待ちくたびれたよ。やっと戻ってきたんだね、ひっちゃん。よろしい！　さあ仕事の時間だよ、仕事仕事～！"


"ミーシャと静音は１階のロビーで俺を待ちかまえていて、俺はまっすぐそこに飛び込んでしまった。"
"最初に考えていたとおり、校舎を迂回すれば良かったのだけど、そこまでするのも考えすぎだしばかばかしい、と思っていた。"


"ミーシャは分厚いプリントの束を俺のほうにパタパタ振って、俺を挑発する。"

show misha perky_smile
with charachange


mi "手伝ってほしいかな～！"


hi "かな？"

show misha hips_grin
with charachange


mi "手伝ってほしいの～！"

show shizu cross_angry
with charachange


shi "……"

show misha sign_smile
with charachange


mi "手伝うのよ！"


"ミーシャはいつもの陽気でのんきそうな口調で話す。それでも静音のどきっとするような強烈な厳しさは伝わってくる。"


hi "命令みたいに聞こえるな"


mi "ほんとに？　そうなの？"

show shizu behind_frown
with charachange


shi "……"

show misha perky_confused
with charachange


mi "え？　そうなんだ？"

show misha hips_laugh
with charachange


mi "あー、ごめんひっちゃん、ほんとにそうみたい！　はははは！"


"全然悪いと思ってるように聞こえないんだけど。"

show misha hips_grin
with charachange


mi "もうほとんど何もかも済んでると思ってたんだけど、実はここにある張り紙を全部立て看板に貼り付けないといけないの"

show shizu adjust_angry
with charachange


shi "……"

show misha sign_smile
with charachange


mi "人手が多いほど仕事も楽になるのよ！"

show misha hips_laugh
with charachange


mi "そしてみんなが得をするの！　ははははは！"

show shizu basic_angry
with charachange


shi "……"

show misha hips_smile
with charachange


mi "どっちみちこれはあなたの仕事なんですからね。生徒会の一員として。あなたもその一人なのよ"


mi "生徒会の"


mi "一員として"

show misha hips_laugh
with charachange


mi "あははは～！"

show shizu behind_blank
with charachange


shi "……"

show misha perky_smile
with charachange


mi "簡単な仕事だから、今片付けておくほうがいいの。大した量じゃないから。ちょっとだけよ、ほんとに～！"

show shizu basic_normal2
with charachange


shi "……"


mi "それにひっちゃんが手伝ってくれるとほんとに助かるわ！"


mi "ほんとに、ほんとに助かるわ！"

show misha hips_grin
with charachange


mi "それに、あんなに親切におごってあげたんだから、今度はそっちがお返しする番よね！"


hi "じゃあ結局お茶屋のあれは罠だったってことかよ！　この裏切り者！"

show shizu behind_blank
with charachange


shi "……"

show misha cross_smile
with charachange


mi "そんな言い方しないで。それは全然関係ないから。ひっちゃんが生徒会に入ったことをお祝いしたかったのよ！"


"じゃあどうしてその話を出したんだ？"


hi "でも――{w=0.3}{nw}"

show shizu cross_rage
with charachange


shi "……！"

show misha hips_grin
with characlose


mi "でもじゃない！　いいから来なさい！"

show misha hips_grin at offscreenleft
show shizu cross_rage at offscreenright
with ease

show misha cross_smile_close at closeleft
show shizu cross_angry_close at closeright
with ease


"俺が話を終わらせる前に、二人が俺の腕を両側からつかんで、生徒会室に引きずっていく。"

show misha cross_laugh_close
with charachange


"二人が俺の後ろで秘密の目配せを交わすと、ミーシャはめまいがするほど大笑いする。"

show shizu basic_angry_close
with charachange


shi "……！"


mi "えっと、ひっちゃんには選択肢はないと思うよ！　はははは！"

show misha hips_grin at twoleft
show shizu basic_angry at tworight
with charadistant


mi "わたしたち二人がいるんだから、逃げたりしたらだめだからね！　わたしたちを見くびらないでよ！"

show shizu behind_frown
with charachange


shi "……！"


mi "ひっちゃん、どっちみちわたしたちを手伝うのはあなたの義務だからね！　生徒会の一員として！"


hi "わかった、わかった！　忘れるわけないだろ？"


hi "でもマジでさ、他に手伝ってくれる人はいないのか？"

show misha perky_confused
with charachange


mi "たとえばだれ、ひっちゃん？"


mi "ひっちゃん、昨日は喜んで手伝ってくれたじゃない……"


hi "昨日は今日じゃない！"


hi "そうじゃなくて、俺以外の誰かだよ！"


hi "どうして生徒会には他に誰もいないんだ？"

show shizu cross_wut
with charachange


shi "……！"

show misha cross_laugh
with charachange


mi "そんなのこっちが知りたいわよ！　……あは……あははははは！"


"ミーシャの笑い声が廊下にとどろく。俺のしかめ面には気づきもしない。そうだった、こいつら二人しかいないんだ。そうだろ？"


hi "ああ、そうだった。わかった。じゃあ手伝うよ"

show misha hips_grin
with charachange


"ミーシャは舌を歯に滑らせる。大いにご満足のようだ。"


mi "それでこそひっちゃん！　やっぱり頼りになるよね！"

show shizu behind_smile
with charachange


shi "……！"


mi "ほんとにわかりやすいよね～"

stop music fadeout 2.0

scene bg school_council
with locationskip


"生徒会室に入ると、俺は開いた口がふさがらない。張り紙、立て看板、案内板の数は常識外れだ。"


"みんな工事現場の材料のように、あちこちに積み上げられている。俺はすぐさま静音とミーシャに知らせる。"


hi "これだけ案内板があれば、学校の外壁の周りにもう一周壁を作れるじゃないか！"

play music music_ease fadein 4.0

show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charaenter


mi "ははは～！　ほんとに？　まあ、こんなにたくさんあれば、もしかしたら……"

show shizu basic_angry
with charachange


shi "……！"

show misha perky_confused
with charachange


mi "え？　ちがうの？"


mi "どうして知ってるの、しっちゃん？"

show shizu behind_frown
with charachange


shi "……！"


mi "ほんとに？"


hi "まさかほんとに考えてたとか言うなよ！？"

show misha hips_grin
show shizu adjust_smug
with charachange


"静音はためらったあと、少しだけ眼鏡を上げる。ミーシャは聞いていてとても不安になる笑い声を上げる。"


"じゃあ考えはしたってことか。"

show shizu basic_normal2
with charachange


shi "……！"


mi "あはは！　それは……関係ないの、ひっちゃん！　案内板を作るのにとりかかってくれるかしら？"


hi "はいはい"


hi "でもやっぱりだまされた気分がするんだけど。大した量じゃないって言ってなかったか？"

show shizu behind_blank
with charachange


shi "……！"

show misha hips_smile
with charachange


mi "あー、えっと、しっちゃんはわたしたちの仕事がそんなに多くないって言いたかったの"

show shizu basic_normal
with charachange


shi "……！"


mi "誰かがあなたの仕事を監督しないといけないでしょ、やり方が正しいかどうか、ね。わたしたちがその監督ってわけ"


hi "それで、お前たち二人は何するんだよ？"

show misha cross_laugh
show shizu basic_happy
with charachange


mi "ひっちゃんを見てるの！　はははは～！"

show shizu adjust_happy
with charachange


shi "……！"

show misha perky_smile
with charachange


mi "いいえ、今のはただの冗談よ、ひっちゃん。もちろんわたしたちも手伝うわ。本当は生徒会にはもっとたくさん人がいるはずなの"

show misha perky_sad
with charachange




mi "今年はたまたまハズレの年なの。いつもよりも人数が少なくて。まあ、去年だってそんなに多くはなかったんだけどね"





mi "それに今年は仕事の量もずっと多いの"

show shizu behind_smile
with charachange


shi "……！"

show misha perky_smile
with charachange


mi "あと、しっちゃんはひっちゃんと一緒に仕事するの好きだから。わたしもね！"


mi "実はね、ふだんよりもずっと仕事がはかどったんだよ"

stop music fadeout 7.0


"それはありがたく受け取っておこう。最近、二人とも会うたびに少しずつ疲れが溜まっていっているように見えるから。"


"生徒会の仕事はどうやら２４時間常に続く仕事のようだ。それに俺が見聞きした限りでは、生徒会にはこの二人しかいない。まあ俺が三人目か。"


"二人ともほぼ休みなしで働かないといけない。俺と一緒にいないときは、どれだけの時間をこの部屋で過ごしているんだろう、と思う。"


"静音と一緒にいないとき、ミーシャが居眠りをしているのも見たことがある。静音だけでも、普段の授業と生徒会の仕事を合わせて、週６０時間は働いているはずだ。"

scene bg school_council_ss
with shorttimeskip

play music music_tranquil fadein 3.0


"２時間が過ぎる。俺は画鋲を取ろうとするけど、箱はもう空だった。俺が何か言う前に、静音が空箱を取り上げる。"

show shizu adjust_happy_ss at tworight
show misha perky_smile_ss at twoleft
with charaenter


"静音は笑うと、慣れた仕草でそれをもう一つの空き箱とともにごみ箱に投げ入れる。"

show shizu behind_smile_ss
with charachange


shi "……！"

show misha hips_grin_ss
with charachange


mi "そっちもなくなったの、ひっちゃん？　大丈夫だよ、しっちゃんがもう少し取ってくるって言ってる"

show misha hips_laugh_ss
with charachange


mi "はははは！"

show misha hips_grin_ss
with charachange


mi "こっちも一箱使い切ったけど、ひっちゃんも一箱使い切るまで次を取ってくるのは待つことにしたの"


"今の説明は何かがおかしいと俺は直感する。"


hi "待てよ、じゃあどっちもたった今画鋲を使いきったってことか？　ずいぶんおかしな偶然だよなあ？"

show misha perky_smile_ss
with charachange


mi "ああ、えっと、実はね、ひっちゃん、こっちは２０分前に画鋲を使い切ってて、残りの箱は一つしかなかったの。ひっちゃんにあげたのがそれ"


mi "それにひっちゃんはすごく使うのが早いでしょ、だから～！　どっちも画鋲がなくなるまで次を取ってくるのは待ったほうがいいって思ったの！"

show misha sign_smile_ss
with charachange


mi "そしたら、しっちゃんが一度に全員分の画鋲の箱を持ってこられるってわけ。効率いいでしょ、ね～！"

show shizu basic_normal2_ss
with charachange


"静音は部屋を出る素振りを見せながらうなずく。"


hi "ちょっと待て、じゃあこの２０分間お前らは何してたんだ？"

show shizu adjust_happy_ss
with charachange


shi "……！"

show misha hips_grin_ss
with charachange


mi "あはは～！　決まってるでしょ、何もしてないわよ！　できることなんてないでしょ？　ひっちゃん、こっちは画鋲なかったんだもの！"

show shizu behind_smile_ss
show misha cross_grin_ss
with charachange


"静音とミーシャはしめしあわせるように視線を交わすと、完全にタイミングを合わせて、驚くほど大げさに肩をすくめる。"


hi "なるほどな。ちょっと休憩ってわけか。お前ら頭いいな"

show shizu adjust_smug_ss
with charachange


shi "……！"

show misha hips_grin_ss
with charachange


mi "あら、言われなくてもわかってるわ"


hi "誰のアイデアだ？"

show misha hips_smile_ss
show shizu adjust_happy_ss
with charachange


mi "わたしたち二人に決まってるじゃん！"

show misha cross_laugh_ss
with charachange


mi "あははは～！　えっと、ひっちゃん、ほんとは全部しっちゃんのアイデアなの"

show shizu behind_smile_ss
with charachange

hide shizu
with charaexit

stop music fadeout 3.0


"俺はすぐさま静音に振り向く。静音は素っ気なく手をひらひらと振りながら、驚くほど明るい笑顔を見せると、あっという間にドアの向こうに姿を消す。"

show misha cross_grin_ss at twoleft
with charachange

show misha cross_grin_ss at center
show bg school_council_ss at bgright
with charamove


"じゃあどうして素直に休憩したいって言わないんだよ！？"


"今まで静音とミーシャは両極端ってくらい違うと思っていた。ミーシャは普通の女の子と同じようにいつも元気でお茶目。一方静音はいつも冷たい感じがした。"
"強引なまでに仕切りたがりで、なんとなく怖いけど、でもそんな感じだった。"


"静音には全く冗談が通じないんじゃないか、と思うことも何度かあった。"
"あいつはかわいいけど、笑ってるところはほとんど見たことがない。その他もろもろの仕草は言うまでもない。"


"あの分析するような視線、いつも変わらず冷静な表情、それにあの筆跡だってそうだ。静音の書く字はいつも機械のようにきっちりしている。まるで活字みたいだ。"


"でも静音とミーシャは、俺が思っていたほど違っているわけじゃないんだ。"


hi "ちょっと驚いたな"

play music music_shizune fadein 5.0

show misha perky_confused_ss
with charachange


mi "どうして？"


hi "静音がさ。ああいう風に冗談かますやつだとは知らなかったから"


"俺が言いたかったのは、あいつがあんなに女の子らしいことができるとは知らなかった、ってことだ。正直、あれはマジでかわいかった。"

show misha perky_smile_ss
with charachange


mi "まあ驚くよね、ひっちゃん"


hi "最初にお前に会ったときだって、お前と静音がこんなに似てるとは知らなかったしな"


"この二人がどうやって巡り会ったのかは前から知りたかったんだ。"


hi "二人とも昔から知り合いだったりするの？"


hi "幼なじみとか？"


hi "家が隣同士とか？"

show misha perky_sad_ss
with charachange


mi "はは……ごめん、ひっちゃん、全然そういうのじゃないんだ。そうだったらもっと面白かったんだけどね"

show misha perky_smile_ss
with charachange



mi "わたしがここに転校したとき、しっちゃんのとなりの席になったの。しっちゃんはすごくまじめな人っぽかった"


show misha sign_smile_ss
with charachange


mi "それで思ったの。『もしかしたら、この学年が終わるまで、ずっとこの人の隣で過ごすかもしれないんだ！』って"


mi "『だから仲良くなれたらいいな！　でも～、わたしのこと好きになってくれるかなあ』"

show misha hips_grin_ss
with charachange


mi "そのあとしっちゃんが耳が聞こえないって知ったの。実はね、ひっちゃん、最初はしっちゃんがわたしのこと無視してるって思ったんだよ～！"

show misha hips_smile_ss
with charachange


mi "でもわたし、たまたま手話をちょっと知ってたから、わたしたちは仲良くなったの"


"どこでミーシャが手話を覚えたのか知りたかったけど、その話はまたの機会ってことにしよう。"

show misha perky_smile_ss
with charachange


mi "今は、いつも一緒にいるって感じだね。うれしいんだ。わたし、話を聞いてくれる人がいてくれたらいいなってずっと思ってたから"
mi "しっちゃんも話し相手がいて喜んでると思うの！　だからどっちも得してるってわけ"


hi "へえ。そりゃいいな"

show misha hips_grin_ss
with charachange


mi "それだけ？　なんかがっかりしてるみたいだよ、ひっちゃん。なにを期待してたの？"

show misha hips_laugh_ss
with charachange


mi "あははははは！"

show misha hips_grin_ss
with charachange


mi "あのね、ひっちゃん、わたしもしっちゃんもひっちゃんにちゃんとお礼を言ってなかったと思うの"


hi "何に？"

show misha perky_smile_ss
with charachange


mi "生徒会に入ってくれて。ほんとに役に立ってくれたんだよ、ひっちゃん！　おかげで今までよりずっと長く眠れると思うよ～！"


hi "まあ、役に立てて嬉しいよ。女の子が夜眠るのを手助けできるならね"

show misha hips_smile_ss
with charachange


mi "面白いこというね、ひっちゃん"


mi "しっちゃんも、手伝ってくれてることにはすごく感謝してるよ"

show misha hips_smile_ss at twoleft
show bg school_council_ss at center
with charamove

show shizu behind_frustrated_ss at tworight
with charaenter


"その瞬間、戻ってきた静音が部屋に入る。ぶっきらぼうに紙パックのジュースを飲みながら、少しいらだっているように見える。"

show shizu adjust_happy_ss
with charachange


shi "……"

play sound sfx_dropstuff


"皮肉めいた笑みを浮かべながら、画鋲の箱を床に放り投げる。"

show shizu basic_normal2_ss
with charachange


shi "……！"

show misha sign_smile_ss
with charachange


mi "あ、しっちゃん"

play sound sfx_crunchydeath

show shizu behind_frown_ss
show misha sign_confused_ss
with charachange


"ミーシャはしゃべろうとして口を開く。でも静音が突然紙パックを握りつぶし、骨が折れるような音を響かせるので、ミーシャはすぐに口を閉ざす。"

show shizu basic_angry_ss
with charachange


shi "……！"

show shizu adjust_angry_ss
with charachange


shi "……"

show shizu behind_frown_ss
with charachange


shi "……！"


"一つ一つの荒々しく揺れる手振りは、たぶん悪口なんだろう、というのがわかる。"


hi "なんて言ってるんだ？"

show misha perky_confused_ss
with charachange


mi "これ取ってくるの、すごく大変だった、って……"

show shizu basic_angry_ss
with charachange


shi "……！"

show misha sign_confused_ss
with charachange


mi "その言い方は控えめすぎると思うよ、しっちゃん……"


"静音は少し落ち着きを取り戻し、眼鏡を直して指で前髪を軽くなでつける。"

show shizu adjust_happy_ss
with charachange


shi "……"

show misha perky_smile_ss
with charachange


mi "考えてみれば、たいしたことじゃなかった？　前向きな考え方だね、しっちゃん！"

show misha hips_smile_ss
with charachange


mi "よおし、じゃあわたしたちも仕事に戻らなきゃだよ、ひっちゃん！"

stop music fadeout 4.0


hi "おう、じゃあやるか"

scene bg school_council_ni
with shorttimeskip


"案内板が片付いた頃には、もう外は暗くなっている。"


"こんな仕事にここまで時間がかかるとは思っていなかった。とはいえ、簡単な仕事だったら、静音もミーシャもそもそも俺に助けを求めたりはしなかっただろう。"

play music music_dreamy fadein 2.0

show shizu basic_normal at tworight
show misha perky_smile at twoleft
with charaenter


"静音は近くの椅子にどさりと座り込むと、整然と自分の指を鳴らし、声を出さずにあくびをする。"

show shizu behind_blank
with charachange


shi "……"

show misha sign_smile
with charachange



mi "今日はこれでおしまいかな！　よかったね、しっちゃん。わたしもすごく疲れてるから"



hi "思ったより時間かかったな"

show shizu behind_frustrated
with charachange


shi "……"

show misha hips_grin
with charachange


mi "そう思う？　ははは、わたしたちもこんなにかかるとは思ってなかったよ！　予定狂っちゃった！"

show misha perky_sad
with charachange


mi "あーあ、すごくおなか減っちゃった。そういえば今日一日何も食べてないよ"


"考えてみれば、俺も朝起きてから何も食べていない。でも今は食い物のことを考えるには疲れすぎている。"


hi "もう食堂の夕食も終わってるだろ"

show misha perky_confused
with charachange


mi "そんなのないよ！　ひっちゃん、食べ物を手に入れる……いい方法はない？"


hi "食べ物を手に入れる？"


"ミーシャの口調はなんだか気に入らない。"

show shizu adjust_happy
with charachange


shi "……"

show misha hips_grin
with charachange


mi "出前取らない？　あー、そうだった。それはアリだね"


hi "出前？　どこから？"


mi "もちろん、町からだよ！"


hi "学校に出前してくれるなんて知らなかったぞ。じゃあ、何を頼むんだ？"

show misha hips_smile
with charachange


mi "中華なんていいかもね！"


hi "お前らが出前とるなら、俺も混ざっていいか？　すごく腹減ってるんだ"

show misha hips_laugh
with charachange


mi "あははは～！　ひっちゃん、最初からそう言えば良かったんだよ！"

show shizu basic_normal2
with charachange


shi "……"

show misha hips_grin
with charachange


mi "なになに？　しっちゃんのおごり？　すごーい！　やったあ！"

show shizu behind_blank
with charachange


shi "……"

show misha cross_laugh
with charachange


mi "わはは、確かにそうだね。しっちゃんのせいで、こんなに遅くまで残るはめになったんだもんね！"

show misha cross_grin
with charachange


"ミーシャは後ろの引き出しからメニューを素早くつかみ、電話番号をゆっくり注意深く回し始める。まるでいつも失敗してるみたいだ。"


mi "ひっちゃん、何がいい？"


hi "ああ、俺は餃子でいいよ"

show shizu behind_smile
with charachange


"俺はお礼のつもりで静音に向けて手を挙げる。静音は本当にかすかに、一瞬だけ笑顔を見せてそれに応える。"

show misha cross_laugh
with charachange


mi "あははははは～！！　ひっちゃん、今夜はしっちゃんが全部払ってくれるって。全部おごりだから、少しくらいぜいたくしても大丈夫だよ！"


hi "じゃあエビチャーハンも頼むよ"

show misha cross_grin
with charachange


mi "りょーかい、りょーかい！　あと、しっちゃんは？"

show shizu basic_normal2
with charachange


shi "……"

show misha hips_smile
with charachange


mi "中華オムレツ？　わかったよ"


hi "おいミーシャ、今のはほんとに『オムレツ』って意味なのか？　もう一回やってみてくれないか？"

show misha hips_grin
with charachange


mi "いいよ！　はは！　ほら、こうやって、こうやって……"

show misha sign_smile
with charachange

show misha perky_smile
with charachange

show misha hips_grin
with charachange


mi "で、ひっちゃんの注文はこれ、ギョーザ！"

show misha perky_smile
with charachange

show misha sign_smile
with charachange

show misha hips_smile
with charachange


mi "エビチャーハン！"

show misha hips_grin
with charachange


mi "わたしはスープと炒め物を頼むけど、こういうふうに言うんだよ……"

show misha sign_smile
with charachange

show misha perky_smile
with charachange


mi "で、これが合計の代金だよ。３６８５円！　"


show misha perky_smile:
    "misha cross_laugh" with Dissolve(0.5, alpha=True)
with None


extend "わはははは～！"


hi "まあ、そんな正確な数字を使う機会がどれだけあるかはわからないけどな……"



mi "あはははは！　おっけ～！　もう注文するけど、ほかに頼むものはないよね。異議なし？　よしよし！"

scene bg school_council_ni
show shizu behind_frustrated at tworight
show misha hips_smile at twoleft
with shorttimeskip


"食事が届くのを待つ間、静音は待ちわびるように割り箸を指でくるくる回す。"


hi "あれ、それどこから取ってきたんだ？"

show misha hips_grin
with charachange


mi "出前を取るのは今日が初めてじゃないんだよ、ひっちゃん"
mi "どうしてか知らないけど、出前の人が山ほど割り箸をくれるの。こっちは二人しかいないって言ってるんだけどね"


hi "それで、生徒会室で何度も長い夜を過ごして出前取ってるうちに、割り箸がたまっていったわけだ？"

show misha cross_laugh
with charachange


mi "その通り！　はははははは！"

show shizu basic_angry
with charachange


shi "……"

show misha perky_confused
with charachange


mi "それは大げさすぎるって？"

show shizu behind_blank
with charachange


shi "……"

show misha hips_grin
with charachange


mi "はは、そうだね、しっちゃん！　ねえひっちゃん、出前を取りつづけて割り箸を１００本集めたら、わたしたちこの宇宙を支配できるんだよ。知ってた？"


hi "俺も昔はそう思ってたよ。小さい時な"

show misha perky_smile
with charachange


mi "ひっちゃん、割り箸をきっちり真ん中で割るのって得意？　わたし一度もうまくできたことないんだ"
mi "それでしっちゃんがためたお箸の山を見つけて、少なくとも２０本くらい使って練習したの"

show misha hips_grin
with charachange


mi "そしたらしっちゃん、すごく怒るんだよ！"

show shizu adjust_blush
with charachange


shi "……！"


"静音は怒りで顔を真っ赤に染め、俺は笑い声を上げる。そんなに子供っぽいところがあるなんて知らなかった。"

stop music fadeout 5.0

scene bg school_council_ni
with shorttimeskip


"食べ物が届き、俺は存分に食べる。飲み物は、静音が廊下の自販機から買ってきてくれた小さなソーダの缶を飲む。"


"二人に食事の礼を言うと、俺は寝床につくために寮に向かう。"

scene bg school_dormhallway
with locationskip


"寮の中は不気味なくらいに静まり返っている。薄い壁越しに聞こえてくる小型のテレビやラジオの、ざわざわとよく聞き取れない音をのぞいては。"

$ renpy.music.set_volume(0.1,0.0, "ambient")
play ambient sfx_cicadas fadein 4.0

scene bg school_dormhisao_ni
with locationchange


"夜の寮は静かで、とても穏やかだ。窓の外からコオロギの鳴き声が聞こえる。空を見上げれば本物の星が見える。"


"疲労した俺は、さっさと眠りにつこうとする。少しだけ、俺の土曜日を奪われたような気分を覚えながら。"

stop ambient fadeout 2.0

$ suppress_window_after_timeskip = True

scene black
with shuteye






label jp_A37:






scene bg school_scienceroom at bgleft
with None


"図書室に行くというのも悪くないだろう。リリーが出かけてしまって、華子はすっかりしょんぼりしてたみたいだったから、話し相手がいたほうがいいかもしれない。"


"かばんを肩に掛けると、俺は教室を出る。"

stop music fadeout 4.0

scene bg school_hallway2
with locationchange


"廊下を図書室へと向かう。途中には、閉じたドアがたくさん並んでいる。"


"どのドアからも、一生懸命なリハーサルの音が漏れ聞こえてくる。あるドアからはロックの曲が鳴り響いてきて、コンサート並みの騒々しさだ。"


"思うに、財政的に恵まれている私立学校のいいところの一つは、今みたいな時に使える教室がたっぷりあるってことだ。"


"それに考えてみれば、学校のグラウンドも建物も、すごくいい状態に保たれている。相当お金がかかっているに違いない。"


"この学校には、とても熱心な後援者がついていると聞いたことがある。"

scene bg school_library
with locationchange

play music music_happiness fadein 1.0


"図書室の壁ごしに、学園祭の準備の音が漏れ伝わってくる。だけど、他に聞こえる音はない。"


"どうやらみんな、外でこの好天を満喫したり、学園祭の準備に取り組んだりしているみたいだ。人っ子一人、ここには見当たらない。"


"優子さんもここにはいない。土曜日は休みなのかもしれない。"




"音を立てないようにして図書室を横切っていく。室内の配置には、もうかなり詳しくなった。俺は奥へと向かう。その隅には、華子専用の小さなスペースがあるんだ。"


"書棚のそばを通りながら、本の背表紙を手でなでていく。その触り心地を感じながら、題名に目を走らせる。"


"病院の図書室でも、いつもこういうことをしていたっけ。世の中には変わらないことがあるんだな。"


"図書室のにおいだってそうだ。どんなに手入れをしても、本の紙は常に、時間とともに劣化していく。"


"たぶん、世界のどこでも、どの図書館に入っても、同じかび臭いにおいがするはずだ。"


"あまり深く考えずに読めるような軽めの本を選んで、読書エリアで華子を探す。"

scene ev hana_library_read_std
with locationchange


"今度も、華子は本棚に背を向けてソファに座っている。教室で読んでいたのと同じ本を手に、ゆっくりとページをめくっている。"

play sound sfx_pillow

show ev hana_library_std
with locationchange


"この前とは違って、静かにソファに座る。その音で華子は俺のことに気づくけど、びっくりはしない。"


"華子に話しかけようとするたびに、こんなデリケートな手続きに従わなければならないなんて、まるで獲物を狩りでもしているような気分だ。"


hi "それ、さっきと同じ本？"


ha "は、はい……もうすぐ読み終わるところです……"


hi "速いな"


"その本……"


hi "その本、読み終わったら借りていい？"


"頭の中が動くより先に口のほうが動いたみたいだ。"


ha "ど、どうぞ……気に入るかどうかわからないですけど……"


hi "大丈夫だと思うよ。だってさ、華子もハマってるだろ？"


ha "そ、そうだと思いますけど"

scene bg school_library
with locationchange


"ソファに腰を落ち着けると、かばんの中に埋もれていた本を取り出して、読書に取りかかる。"


"海賊をテーマにしたライトノベルだ。この本を選んだのは、単にいつも読んでいるジャンルとは違っていたからで、正直なところ目が滑っている状態だ。"


"最後まで読むだけのやる気は出せそうにないし、気づかないうちに思いきり華子の気を散らしてしまったみたいだ。それで俺は、華子に話しかけてみることにする。"


hi "そういえば、リリーは一人で出かけたみたいだね"

show hanako emb_downtimid at center
with charaenter

show hanako basic_worry
with charachange


"華子はうなずいた後で、ようやく本から目を離す。なんだかんだいって、すごく熱中していたんだろう。"


ha "リリーが、人に会いに……出かけなきゃいけないって……"


hi "っていうと？"

show hanako basic_normal
with charachange


ha "あ、晃さんです。リリーのお姉さんで……"


hi "お姉さん？　家族の話は聞いたことなかったな……"

show hanako cover_distant
with charachange


ha "リ……リリーと晃さんって、前は一緒に住んでたんです"


hi "ここの生徒って、みんな寮に住んでるんじゃないのか？"

show hanako cover_worry
with charachange


ha "み、みんなは……つまり私たち……必ず寮に住まないといけないわけじゃなくて"


hi "でも、そっちのほうが楽だろ？　つまりさ、ここだと食事ができるし、学校に近いし……俺なんか、こんなにしょっちゅう時間通りに登校したこと、今までなかったと思うよ"

show hanako cover_smile
with charachange


"隠そうとしてるのにぜんぜん隠せていない華子の笑顔、それを目にして心の底から報われた気持ちになる。"


"心の片隅では、片づけなきゃならない宿題が少しあることはわかってるけど、ここはとても居心地がいい。誰も俺を探しだせないし、お気に入りの企画に引きずり込んだりすることもできない。"


"とはいえ、学園祭について考えていると、別の疑問がわいてくる……"


hi "なぁ、華子、学園祭はどうするつもりだ？"

stop music fadeout 0.2

show hanako def_shock
with charachange


"一瞬、華子がショックのあまり本を放り出すのかと思う。"


ha "え、えっ……？"


hi "明日の学園祭はどうするのかって聞いただけだよ。何か予定ある？"

show hanako def_worry
with charachange


ha "わ……わかりません"


"華子の答え方からすると、これ以上は聞いてほしくないみたいだ。大勢の人ごみとか騒々しい音楽は、あまり彼女の『お気に召さない』らしい。"


hi "ああ、そっか"


"話題を変えなきゃ、話題を変えなきゃ……"

play music music_happiness fadein 4.0


hi "じゃあさ、リリーのお姉さんってどんな人？"

show hanako basic_normal
with charachange


ha "す……素敵な人です。リリーにすごくよく似てて、でも格好が……ビジネスっぽいっていうか……"


hi "ビジネスっぽい？"

show hanako basic_distant
with charachange


ha "あ……晃さんって、いつもスーツを着てて……"


hi "ああ、なるほど。だから、見た目はなんとなくパッとしないんだ？"

show hanako emb_emb
with charachange


"華子はもじもじとかぶりを振る。"


ha "ち、違います……ただ……変わってるだけです"


"正直言って、俺は今興味をひかれてる。華子が、リリー以外の誰かについて話すのを初めて聞いた。その人を好意的にいうのも……"


"だけど、この『謎のお姉さん』の姿を想像しようとしても、思いうかぶのはスーツを着たリリーだけだ。それに、魅力的じゃないリリーなんて想像できない。全然無理だ。"


hi "えっと、いつか紹介してくれるかな"

show hanako basic_bashful
with charachange


ha "い、いいですよ"


"俺たちのささやかな会話は始まったときと同じように唐突に終わり、二人とも読書に戻る。"

stop music fadeout 4.0

scene bg school_library_ss
with shorttimeskip


"窓から差し込むまだらな光のゆるやかな動きだけが、時間の経過を教えてくれる。"


"校舎を満たしていた種々雑多なリハーサルの音はゆっくりと静まっていき、やがて完全に消え失せる。生徒たちが疲れてお腹を空かせ始めたからだ。"


"そんなことを考えているだけで、俺もお腹と背中がくっつきそうになる。そろそろ帰る時間だろう。"


hi "そろそろリリーが戻ってくるかな？　俺、寮に帰ろうと思うんだ。今週はすごく疲れたし"


"今の言葉に嘘は一つもない。新しい学校に転校して、しかもそこが大きな行事を控えて準備の真っ最中ってのは、控えめに言っても相当きついことだ。"


"本を読んでいても、居眠りしそうになる。"

show hanako basic_smile_ss at center
with charaenter


ha "わ、わかりました。わ……私は、もうちょっとここにいたいです"


"華子の本を見ると、読み終わるまでにはあと数ページしか残っていないようだ。"


"一瞬、彼女が読み終わるまで時間をつぶそうかと思ったけど、またしても俺のお腹が収縮して、グウと音を立てる。"


hi "そっか。じゃあ俺は暗くなる前に行くから。また今度会おうな"

show hanako basic_bashful_ss
with charachange


ha "は、はい。またね、久夫くん"


hi "じゃあな"

show hanako defarms_worry_ss
with charachange


ha "ひ、久夫くん？"


hi "ん？"

show hanako emb_smile_ss
with charachange


ha "あ、ありがとう。わ、私に付き合ってくれて"

play music music_dreamy fadein 2.0


"この簡単なフレーズを言葉にするのが、華子にとってどれだけ大変だったことか。俺はしばし言葉を失う。"


"そうか。この学校には俺よりさらに孤独な人間がいるってことだ。"
"俺の場合は、この初めての週に仲間がいなくて困ったことはなかったから、孤独という言葉は適切じゃないかもしれないけど、それでも俺は、どことなく孤独感や孤立感を覚えてきた。"


"華子にとっても、孤独という言葉は適切じゃないかもしれない。なんだかんだいって、彼女にはリリーがいるじゃないか。"


"あまりに長い間、返事もせずに突っ立っていたことに気づいて、俺はそつのない、大げさすぎない笑みを浮かべる。"


hi "どういたしまして"


hi "さよなら、華子"

show hanako emb_downsmile_ss
with charachange


ha "さ、さようなら"

scene bg school_hallway2
with locationchange


"本を読み終えようとしている華子を残して、夕食が待っている寮へと戻る……"

stop music fadeout 3.0

$ suppress_window_after_timeskip = True

scene black
with Dissolve(3.0)

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
