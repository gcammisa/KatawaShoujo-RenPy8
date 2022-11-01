label jp_R30:

window hide None

scene bg school_scienceroom
with locationchange

window show

play music music_normal fadein 3.0


"なんとか授業には間に合う、朝食はパスする羽目になったけど。"


"教室はやわらかな日差しに包まれている。"



"ということは、午後にはどうしようもないほど暑くなる。でも今のところは快適だ。"




"ミーシャと静音は活き活きとなにかを話し合っていて、華子は窓の外を眺めている。武藤先生はよろめきながら、今日はなにを教えるのかも覚えていないまま、４分遅れで教室に入ってくる。"




"自分があんなにあっけなく学校に来なくなるさまは想像できないな。たとえたった数週間であっても。"




"一方で、琳はそんな考えにも、実際にそうしてしまうことにも、抵抗はないように見える。"





"とはいえ、どういうわけか俺は琳の常識外れな孤独になし崩しに身を委ねていった。その結果、お互いを傷つけることになると分かっていても。"





"いや、ほんとうにお互いか？　ひょっとしたら傷ついたのは俺だけだったのかも。"


scene bg school_scienceroom_ss
with shorttimeskip



"午後の遅い時間になるまで、今日が月曜だと気づかなかった。美術部の活動がある日だ。"




"それだけじゃない。試験があるので、これが夏休み前の最後の活動だ。"




label jp_R30x:




"もう顔を出す筋合いもないけど……"




"でも先生とは話しておきたい。"

scene bg school_hallway3
with locationchange



"そんなわけで俺は美術室の前で部活が終わるのを待って、所在なげにうろうろすることになる。"




no "今学期の活動は以上だ、諸君！"





"先生の声はドア越しでも届くくらい大きい。熱が入りすぎていて、わざとらしく聞こえる。"




no "次の活動は夏休みが明けてから、２学期の最初の月曜日だ"



no "また元気でこられるようにな！"


no "ではいい夏休みを！"

play ambient sfx_crowd_indoors fadein 1.0
stop music fadeout 4.0

show crowd
with charaenter


"困惑したような返答が唱和されると、教室のドアが開いて生徒たちが流れ出てくる。"



"先生と二人きりで話せるよう、みんなが出ていくのを待つ。もうすぐ夕飯の時間なので、長くは待たずに済む。"


stop ambient fadeout 2.0

scene bg school_classroomart_ss
with locationchange




label jp_R30y:




"琳がいないと、あそこに行く意味はまるでない気がするけど、でも先生と話がしたい。"



scene bg school_classroomart_ss
with locationskip


"俺の水彩画の腕と同じで、今日の活動自体は特に大したことはない。"



"野宮先生はあまり上から目線に聞こえないよう努力しながら、俺を励ましたり助言をしたりするけど、大してうまくいっていない。"




"少なくとも、美術部に入ったことで、俺は芸術が好きなんだということが理解できた。実際に美術部で芸術作品を作り上げることができたら良かったんだけど。"




"みんなの作業の成果が先生の机の上にきれいに重ねられると、先生はまたちょっとしたスピーチをしようと咳払いをする。"


show nomiya talk at center
with charaenter



no "今学期の活動は以上だ、諸君！"




"先生の声はやたらと大きい上に、熱が入りすぎていて、わざとらしく聞こえる。"


show nomiya smile
with charachange


no "次の活動は夏休みが明けてから、２学期の最初の月曜日だ"



no "また元気でこられるようにな！"

show nomiya veryhappy
with charachange


no "ではいい夏休みを！"

hide nomiya
with charaexit

stop music fadeout 4.0



"みんなも同じように返事を返しながら、ぞろぞろと教室を出ていく。"




"俺はその場にとどまって、先生と二人きりになるまで待つ。もうすぐ夕飯の時間なので、長くは待たずに済む。"



label jp_R30z:



"野宮先生は提出された絵に目を通している。そのいくつかは本当によく描けている。"




"琳は美術部の他の誰よりも上手いかもしれないけど、才能があるのは琳だけじゃない。"


hi "すみません、先生……"

play music music_happiness fadein 2.0

show nomiya smile at center
with charaenter


no "んん？　どうかしたのかね、中井？"


"先生は尋ねるように眉をつり上げて、大きく笑みを浮かべる。"


hi "琳のことなんですけど……"

show nomiya frown
with charachange


no "ほう？　手塚がどうかしたのかね？"


hi "いえ、ただ……"



"言いたいことをどう伝えるべきかわからなくて、俺はほんの一瞬、躊躇してしまう。それでも先生のほうからべらべらとしゃべりだすのには十分な時間だった。"


show nomiya smile
with charachange



no "何日か前にさえの画廊に立ち寄ったら、手塚に会ったぞ"




no "展覧会に向けて絵をもう１、２枚描くといっていたな"


show nomiya talk
with charachange



no "本当にうれしかったよ、驚くほどよく努力している。かねがね手塚は少々怠けがちだと思っていたのだがな、課題よりも自分のやりたいことをして……"



"先生は俺の不安と話が脱線していることに気づいたようで、話を終える前に口を閉じる。"

show nomiya smile
with charachange


no "ああ、なにか話すことがあったんだったな。どうしたのかね？"



hi "なんていうか……琳はいろんなことから距離をおこうとしてるみたいなんです、展覧会のこと以外は考えられないみたいに"


show nomiya frown
with charachange



no "そりゃあ、良いことじゃないかね？　手塚は絵に集中しているんだ、そうしなきゃいかんのだからな"



hi "ええ、でもそれとは違うんです。なんだかとりつかれてるみたいで。俺も会いにいったんです、それで……"

show nomiya serious
with charachange


no "なにかちょっかいを出したんじゃあるまいな？"



"先生は一瞬ですっかり怒り出した様子で、俺が言い終わる前に割り込んでくる。"



hi "いえ……そんなことは……ないと思います"



hi "ただ全然学校に来なくなって心配だったんです。琳も様子が変だったし"



hi "いつもより変だったんです、どう見ても"

show nomiya stern
with charachange



no "くだらない！　手塚にとってはろくでもない数学だか物理だかの授業よりずっと重要なことだ"




no "この学校がこれほど融通が利くのはまさにそれが理由なのだ。すべての生徒に自己実現の機会を与えるためだ"


show nomiya serious
with charachange





no "手塚は絵描きなのだから、絵を描くべきだ、違うか？　そして展覧会をやる。それが芸術家というものだ"
no "手塚はそれに集中することを認められるべきなのだ、取るに足らない授業よりもな。それを後押ししてやらねばいかんのだ"




no "そう考えれば、まったく異論の余地はないだろう"



"先生の反論はあまり説得力がないけど、何か言い返そうとしてもなかなかできない。"





"俺がしぶしぶ黙り込むと、先生は俺が納得したととらえたようで、また机の上の提出された課題の束をトランプのようにシャッフルする。"



show nomiya smile
with charachange



no "率直に言って、手塚の展覧会のことを話している間も……"




no "これがどう転ぶか、とても楽しみだよ"

show nomiya dreamy
with charachange



no "手塚はまだ若い、それでいてあれほど優れた技能をもっている。そしてスタイルもな！"




"先生は少し暗くなりすぎた雰囲気を和らげようとして、なにもない空間に向かって話をする。"


show nomiya talk
with charachange



no "中井も展覧会には行くんだろう？"




hi "ええ、たぶん"


show nomiya smile
with charachange


no "うむ、ではまたそこで会おう"

stop music fadeout 3.0

scene bg school_hallway3
with locationchange



"それは下がってよしという合図と受け取る。そしてその通りにする。不満ではあるけど。"




"控えめに言っても、俺の言いたいことは伝わらなかった。"


$ suppress_window_after_timeskip = True

scene black
with dissolve

label jp_R31:



window hide None
nvl clear

scene bg school_scienceroom_bw
with locationchange

nvl show dissolve

play music music_night fadein 1.0



n "\n\n\n\n\n\n\n\n\n翌日、言うべきなのに言えなかったこと、その機会を逃したことがどっとのしかかってくる。今となってはくよくよと考え込むことしかできない。"


nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve



n "\n\n\n\n\n\n\n\n\n２日目。心配になってくる。その心配が疑わしく思えてきてバカみたいな気分になる。今でも琳のこと以外は考えられないおかげで、余計にそう思う。"


nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve



n "\n\n\n\n\n\n\n\n\n３日目。国語のテスト、と同時に、世界史のテストがある。参った。あいつの一番嫌なところは、まるっきり別のことに集中しなきゃいけないのに、俺をこんなにひどい気分にさせるってことだ。"


nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve



n "\n\n\n\n\n\n\n\n\n４日目。数学のテスト。なんと数学のテストだ。なるようになる。どうでもいい。"


nvl clear
nvl hide dissolve

with shorttimeskip

nvl show dissolve




n "\n\n\n\n\n\n\n\n\n５日目。野宮先生がまた展覧会のオープニングに出席するか聞いてくる。行かないと言ってやりたくて仕方ないけど、先生にノーとはいえない。とにかく先生と琳に関することは一切話したくないので、無難な答えを返しておくのがいいってことだ。"



nvl clear
nvl hide dissolve

stop music fadeout 2.0

scene bg school_dormhallway
show rin basic_absent at center
with shorttimeskip

window show



"そして６日目、展覧会の前日。夕食を済ませて寮に戻ると、琳が俺の部屋の前の廊下に立っている。"


play music music_rain fadein 6.0 


hi "何してるんだよ、こんなところで？"



"意図していたよりも怒った口調になってしまう。自分を抑えられないことに少し失望したけど、でもどうしようもない。"




"琳は用もなく偶然そこに居合わせたかのように、ただ突っ立っている。琳のリアクションはなにに対してもそっけなくて、それがまた俺をいらだたせる。"




"良くないな。あれから６日も経っているけど、琳の姿を見ただけで怒りが爆発しそうだ。琳はまだ口も開いてないのに。"


show rin basic_deadpan
with charachange


rin "絵が描きあがったんだ"




hi "画廊にいなきゃだめなんじゃないのか？　準備とかあるんだろ？"


show rin basic_awayabsent
with charachange



rin "いなくていいって"





"さえさんが準備をしてるんだろう。絵を額に入れたり、壁にかけたりとか、そんなことを。"



hi "それで、なんでここにいるんだよ？"

show rin basic_deadpannormal
with charachange



rin "来たかったから"





"またいつもの馬鹿なパターンが浮かび上がる。俺が琳に質問をして、琳は答えになっていない答えを返す。なぜなら、俺たちはそんな形でしか会話ができないからだ。"





"俺が琳のどうでもいいおしゃべりを聞くのは別だけど、それは会話とはいえないだろう。"




"これは演劇なのか？　俺たちは知らないうちに目に見えない役に配されていて、顔を合わせている間は決められた条件にしたがって行動させられて、否応なくお互いに傷つけあうように仕向けられているのか？"






"琳の無頓着な答えと、さらに無頓着そうに肩をすくめる様子を見ても、相変わらず何も分からない。展覧会の準備が済んだことを俺は喜ぶべきなんだろう。"


play sound sfx_dooropen

scene bg school_dormhisao
with locationchange



"部屋に入ると、琳が中までついてくるのが足音でわかる。"



"迎え入れたつもりはないぞ。追い出すつもりもないけど。"

show rin basic_awayabsent:
    center
    alpha 0.0
    ease 0.5 ypos 1.15 alpha 1.0
    parallel:
        ease 0.3 center
    parallel:
        "rin basic_absent" with Dissolve(0.3, alpha=True)
with Pause(0.5)

stop music fadeout 6.0



"琳は俺に黙ってベッドに腰掛ける。朝、部屋を出る前に整えておけばよかった。すると今度は焼けた炭の上にでも座ったかのように立ち上がる。"



"俺は散らかっていない机の一角に寄り掛かって、足だけでも休める。"

show rin basic_awayabsent:
    center
    alpha 1.0
with charachange



"琳はしばらくの間、もの珍しそうに部屋を見回している。そういえば琳はここに来たことがなかったな。"




"一瞬、琳は本当に集中しているような様子を見せる。すべてを感じとろうとしている。これが琳を芸術家たらしめる観察眼にちがいない。"


show rin basic_absent
with charachange



"部屋が小さいから、観察するようなものもすぐになくなるけど、他に何が出てくるでもなくて、空気が気まずい沈黙で満たされる。"





"控えめにいっても冷ややかな雰囲気のなか、俺たちのどちらも警戒して、お互いに相手が先に行動するのを待ち構えている。"





"もちろん、琳ならこの心理戦を永遠にでも続けられる。なら俺が先手を打つしかない。"



hi "それで……"



"琳は絶対に自分から会話を始めないけど、言いたいことがあるみたいだし、俺もさっさと終わりにしたかったので、諦めて自分から話をする。"



"話がしたくないなら、どうしてここにくるっていうんだ？"



"何を言えばいいのか俺にもわからない。怒りたいけど、琳を怒鳴りつけたり、何かをしたりする気持ちにもなれない。"




"俺の声が琳の注意を引いて、琳も同じように言葉を探そうとするけど、どうも琳もここに来た理由をちゃんと理解しているわけではないみたいだ。"


show rin basic_absent_close:
    center
    ypos 1.05
    easein 0.5 ypos 1.0
with characlose



"そこで琳はただ数歩進んで俺に近づき、高さを合わせるために爪先立ちになって……"


window hide

show rin basic_lucid_superclose at center
with charachange



centered "『やっぱりやめておけばよかった』"




centered "『たぶん、あのことは忘れた方がいいよ。私もそうするから』"


window show


"反射的に、そしてほとんど思いつきで、『イエス』『ノー』『たぶん』の言葉がいっせいに頭をよぎる。"



"俺の手が琳と俺の唇の間に割って入る。それは……何かを防ぐために打ち立てた壁だ。"




"琳の温かい息が俺の指に当たる。肌の匂いがあたりに漂い、得体のしれない、言葉では言い表せない感覚が俺をとらえ、俺の視線を琳の目の奥深くへと引きずり込む。"


show rin basic_surprised_close
with charachange

play music music_moonlight fadein 0.5



"琳は驚いたような目つきで、この無作法な手が琳の前進を阻んだ理由をいぶかしんでいる。"




"琳の目は本当に大きく、潤いで輝いていて、俺の目を柔らかな視線でまっすぐ見つめている。俺は視線を合わせることができない。"




"半開きの口のせいで琳の表情はよけいに混乱しているように見える。でもその唇が描く官能的な曲線は全く別の合図を発している。"


show rin basic_upset_close
with charachange


rin "お願い"

show rin negative_angry_close
with charachange


rin "君が必要なんだ"



"俺だけに向けられた言葉が、舌や歯に邪魔される隙を一切与えずに、琳ののどからざらついたささやきとなって出てくる。"


show rin negative_angry
with Dissolve(0.15)
with vpunch




"その言葉で俺は瞬時に正気に返り、不格好に後ずさって琳との距離を少し開く。体を机にこすってしまい、ひどく痛む。"






"琳の言葉遣いのせいかもしれないし、言い方のせいかもしれない、でもその何かが俺を不愉快にする。"





"何かが間違ってる。またしても、何かがとんでもなく間違ってる。"




hi "必要って何のために？"




"もろもろの不快な気分がまた浮かび上がってきて、心臓の鼓動が突然１０倍は速くなった気がする。"


show rin basic_absent
with charachange




"琳の身体が緊張状態からリラックスして、再びまっすぐに立つ。同時に琳の目の焦点がぼやけ、また元に戻る。"




show rin basic_deadpanupset
with charachange



rin "何も考えてなかったと思う。どうしてナイトテーブルのほこりに模様を描くの？"


show rin basic_awayabsent
with charachange


rin "そういう言葉ってあったはずなんだけど、思い出せないや……"


"琳の発言にほとんど話を煙に巻かれてしまった。琳の肩越しにベッドの横の小さいテーブルを見るけど、この距離じゃなにも見えない。"



"で、特に理由はないけど俺が必要だっていうのか？"



"俺が喜ぶと思ってたまたまここに来たっていうのか。一週間も俺を締め出して、文句のひとつも聞いてくれないで。"




"心底から人のためを思ってのことか？"





"来たかったから？"



hi "ふざけんな。俺にはわかってるんだぞ"




hi "お前の気まぐれで好き放題人を煙に巻いて、気まぐれでキスして、気まぐれで無視して、気まぐれで自分の思いつきを満たすためか？"





hi "そういうことか？　そのために俺が必要なのか？"



"俺の声はとても怒っているように聞こえる、俺にとってさえ。"


extend "いい調子だ。"

show rin basic_absent
with charachange


"琳はようやく雰囲気を察したようで、その好奇心に満ちた表情から一瞬で、らしくない表情になる。"


show rin negative_sad
with charachange



rin "違う――"





"琳はそれしか口にせず、落ちつきなく目を動かす。まるで壁のタペストリーに探している言葉が書かれでもしているかのように、部屋中を目で探し回っている。"





hi "じゃあなんだよ？"


show rin negative_confused
with charachange

stop music fadeout 2.0



rin "絵を描かなきゃいけなかったんだ"




"絵。"


"それはそうだろう。それが芸術家のすることだ。"



"その言葉が俺の中にこだまする。つんざくような怒りの音に重なって、血流の中で響き渡る。"


play music music_tragic fadein 2.0



hi "やめてくれよ、琳！　俺はお前の絵のために自由にもてあそばれる、くそったれなミューズじゃない！"






hi "お前が追い求めるもののための踏み台じゃない、俺は俺なんだ！"





hi "自分の将来のことがなんにもわからなくて、だからなんだってんだ？"





hi "俺にだって欲しいものはあるし、気にしてることもあるんだよ！　こんな俺でも悪夢以外の夢だって見られるんだ！"




"俺は叫んでいるけど、そんなことを気にしていられる段階はとっくに通り過ぎている。"


show rin negative_sad
with charachange




"俺の怒鳴り声に対して何の反論もせず、琳は足下を見下ろし、つま先を若干憂鬱そうにもじもじと動かす。"





"俺が怒鳴り終わって初めて、琳はなんとか答えようとする。"


show rin basic_sad
with charachange



rin "私にはこれしかできないんだ。いや、どんなことでもできるけど、でも……私には……できない"


show rin basic_upset
with charachange



rin "私がわりとまともにできることはこれだけなんだ。だいたいの時は"




"完全に理解できる。絵が１番で、ほかのことは全部２番目なんだ。それとも１０００番目か。"




hi "俺のことはどうなんだよ？　なんとも思ってないのか？　俺が美術に興味をもったとき、俺のことを少しでも面白いって思ったか？　しばらくの間でも"




hi "教えてくれよ、本当に知りたいんだ。俺がどう思ってるかなんて一度でも考えたことあるか？　それとも自分さえよければそれでいいのか？"




"言葉が痰のようにのどに引っかかる。"

show rin basic_surprised
with charachange



"琳はおびえているみたいだ。そしてさっぱり理解できていないようだ。俺が何について怒っているのか全くわかっていないかのように。"




"琳がここまでバカだったなんて、信じられない。"


show rin negative_sad
with charachange



rin "そんなつもりじゃ――？"




"今度は琳が途中で言葉を切る。"



show rin basic_upset
with charachange



rin "わからないの？　私にはできないんだ"




hi "何ができないんだ？"




hi "お前は絶対に説明しないじゃないか！　お前が何も言わないのに、どうして俺にわかるっていうんだよ？"




hi "どうして、お前はいつも話さないんだ？"




hi "なんとか言えよ！"




"けど琳は何も言わない。"




"琳に向けて怒りをぶちまけることに満足感を覚える。こんなに満足感を覚えるのは間違っている気がするけど、自分を止めることができない。"


show rin negative_annoyed
with charachange



"真正面から俺の怒りに向き合いたくない琳は窓のほうを向いて、頑なに外を見つめる。見るものなんて何もないのに。"




"怒りのピークが過ぎ去ると、琳の後ろ頭に怒鳴り続ける気力が失せて、ようやく沈黙が戻る。"




"アドレナリンで歪んだ視界を通して、琳のわずかな反応をうかがおうとする。"





"俺の反応はベストとは言えないものだったけど、あらゆるものを気分次第で無視することなんてできないんだ、ということを少しでも琳が気づいてくれればと願う。"





"もし琳に伝わらなかったとしたら残念だ。琳はいつも絶対に人の話を聞かないし、周りの世界からまるで影響を受けていない。"




"でも今回はそうでもないみたいだ。"



"琳の体は涙をこらえるかのように震えているけど、でも琳は泣いてなんかいないことはわかっている。"



"琳の無関心さが俺をあんなに怒らせた。それがなくなった今、俺は困り果てている。もしかして……"




"俺はやり過ぎたのか？"



hi "なあ、俺――"

show rin negative_angry
with charachange



rin "出てって"




rin "出てって、久夫"




"そう呟く琳の声は小さく、くたびれていたけど、その言葉ははっきりと聞こえる。"



"……"


"これ以上言うべきことがあるか？"



hi "ここは俺の部屋だぞ"



"そっけなくうつろなその言葉はこの不愉快な議論、そして更に不愉快かつとても一方的な怒鳴り合いと化したこの議論の締めくくりにふさわしい。"


show rin basic_lucid
with charachange



"ふっと気を取り直すと、琳はただ諦める。その肩を落とした様子からわかる。そして部屋を出て行く。"


hide rin
with charaexit



"わざとそっぽを向いているけど、くちびるの端を強く噛んでいるのが見える。早く止めないと出血しかねない。"




"琳が出ていくと、琳が入ってきたときにドアを開けっ放しにしていたことに、そして俺の怒鳴り声が寮の廊下に響き渡っていたであろうことに気づく。"




"俺はため息をつく。琳がいなくなった今、俺は罪悪感とともに一人残される。"



"少しずつ心臓が落ち着いていくと、今度は不安に駆られる。"


"どうも、これは俺の身から出たことのように思えてくる。"



"琳がどんなに腹立たしくて、常軌を逸していて気に食わないやつだとしても、あれは俺が知っていると思っていた琳じゃない。"



"俺の期待していた琳とは。"



"……"



"展覧会に挑戦するよう琳を説得して、こんなことを引き起こしたのは俺だったっていうのか？"




"この数週間、琳があんな状態になっていたのはひとえに俺の責任なのか？"




"展覧会と、それにかかわる全てのこと以外に、琳のおかしな振る舞いの理由を思いつくことができない。"





"これが俺たちが仲を深めることができる唯一の方法だったのかもしれない。でもその結果は、お互いをもっと遠くへと引き離しただけだった。今となっては、どちらからも手の届かない場所に。"



play sound sfx_impact2
with vpunch


"俺は頭を壁に強く打ちつける。"

play sound sfx_impact2
with vpunch

stop music fadeout 4.0


"２回、確かに痛みを負うまで。"

scene black
with dissolve
label jp_R32:

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 0.5

scene bg gallery_ext
with locationchange



"22nd Cornerへのドアを押し開ける瞬間にも、頭痛がしつこく俺の後頭部をひっぱたいてくる。"





"それを除けば、俺はすっかり落ち着いている。"


$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve



n "\n\n琳に向かって溜まりに溜まった怒りをぶつけると、巨大な重しが心臓から取り外されたような気分になった。"




n "この数週間、俺の心をつかんでいた緊張も跡形もなく消えていった。"




n "この禅の悟りのような状態になって初めて、俺は琳をあんなふうに怒鳴りつけたのはまずかったかもしれないという気になる。"




n "\nあれは俺の本音だった。でもあんな風に怒りをぶちまけて何かいいことがあるか？　あるわけがない。"





n "俺はそんなやつじゃない。普段なら俺は人を怒鳴りつけたりしない。どうして昨日は怒鳴ってしまったのかわからない。"





n "だから俺はずっと後ろめたい気持ちが続いていて、言った言葉も取り消したいと思う。"




n "\n\n琳もきっと怒ってるだろう。自分の取った態度よりも、琳の反応のほうがショックだった。"


nvl clear




n "\n琳はいつも周囲から距離を置いていて、変わることがないとずっと思っていた。だから怒鳴ったあとに琳があんなに怒ったのを見て……琳らしくないと思った。"




n "\n琳は俺の気持ちをわかってくれたんだろうか？"



n "琳の世界はなにもかもが絶対で、自分本位……絶対的に自分本位なんだ。自分以外の他者の視点でものを見ることが一切できないかのように。"




n "でも結局、それができる人なんているんだろうか？　客観性とか利他主義なんて、自分が心優しいと思いたい人たちのための幻想でしかない。"





n "現実がより大きな何かを覆い隠すベールに過ぎないと考える人にとって、芸術が幻想でしかないのと同じように。"





n "もし世界が自分を中心に回っていると考えるのをやめても、あるいは神話的な箱の外側について考え始めても、人は抜け出すことのできないもっと大きな箱の中にいるに過ぎない。"




n "\nそうすると結局、琳も俺たちと同じってことかもしれない。"


stop ambient fadeout 1.0

nvl clear
nvl hide dissolve

play sound sfx_storebell
$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 0.5

scene bg gallery_int
show crowd
with locationchange

window show

play music music_ease fadein 3.0



"ドアをくぐりぬけると、ギャラリーの中は幻想にとらわれた人でいっぱいだ。"





"俺が前に来たときにさえさんがああ言ってはいたけど、ここはとても広いとずっと思っていた。だけど今はこんなにもごった返していて、とても窮屈だ。"



show sae smile at center behind crowd
with charaenter



"俺はすぐにさえさんが活発な話し合いの中心に立っていて、忙しそうに何人かの老紳士と話をしていることに気づく。"




"さえさんは実は結構背が高くて、見た目もどこかクールなので、人混みの中で目立っている。"




"ワイングラスが数十個、後ろの壁に沿って並んだテーブルの上に置かれていて、赤紫色の液体が注がれている。ほとんどの来客が自分のグラスに口をつけている。"





"著名人や芸術の専門家が楽しそうに行き交っていて、琳の作品について当たり障りのない意見を交わしている。ほとんどの人にとっては、そこは第一の目的じゃないみたいだ。"







"周りの人たちから遠ざけられ、爪弾きにされたような気がする。"




"俺は控えめに言っても色んな人相手に話を合わせるのは苦手なので、この状況はひどく気が滅入る。"




"この人混みの中で完全に浮いているので、俺は浮いていないふりをして、できるだけ平静で上品そうな風を装う。"




"こんなの、琳はどうしているんだろう。俺だったらパニくってしまうだろうな。"


$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg gallery_exhibition
show crowd
with locationchange



"不安を投げ打つと、俺は慎重に人だかりをかき分けながら、壁にかかっている額に収められた絵をちらちらと見る。"


$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene rin_exhibition_paintings
with locationchange



"琳の展覧会はギャラリーの壁のスペースの半分を使っている。いくつかの絵はあまり見慣れないものだけど、大体は見分けがつく。"




"そのうちいくつかは美術部の活動中に描いているのを見たし、あるいは琳が自分のポートフォリオから選んでいたときに見かけたのを覚えている。"




"いくつかの未完成の絵も額に入れられて壁にかかっているのに気づく。偶然の産物ってやつだろうか？"






"琳の失敗作でさえ、仮にこれがそう呼べるとしてもだけど、その腕前の証しになった。実に矛盾しているな。"


$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

scene bg gallery_exhibition
show crowd
with locationchange



"琳の姿はどこにも見あたらない。おかしいな。混んでいるとはいえ、このギャラリーは確かにかなり小さいから。"




"ある意味よかったと思う。昨日のことのあとで、どんな顔をして琳に会えばいいのかわからない。来るべきでさえなかったのかも。"




"でも、いろいろな人に来ると約束してしまった。琳も含めて。だから……"





"くそ、これじゃまるで理にかなっているか（あるいはないか）どうかじゃなくて、その場の愛想みたいなものに動かされてなにごとも決めているみたいじゃないか。"



scene bg gallery_int at right
show sae smile at center
show crowd at right
with locationchange



"俺はさえさんに忍び寄って、声をかけられるようになるまで、立ち話が途切れるのを待つ。"




"さえさんの声はほとんど喧噪に埋もれてしまっているけど、琳のことを話しているのが断片的に聞きとれる。"




sa "ええ、彼女は地元の高校生で……来年卒業するんですが、きっとさまざまな美術学校が興味を持つかと……"





sa "……まだ成長期の早い段階にある子の展覧会をするのも面白いと思いまして……"




"本当に妙な感じだ、小さな町の小さなギャラリーでやる小さな展覧会に過ぎないのに、これじゃ琳がちょっとした有名人みたいじゃないか。"




sa "実は、私の友人が……"


play sound sfx_impact
with vpunch



mystery "久夫くんじゃん！"




"俺の盗み聞きは馴染みのある声と、馴染みのある背中への平手打ちに邪魔される。それが誰のものかは、振り返らなくたってわかる。"



hi "よお、笑美"

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

show emicas invis:
    center
    xpos 0.15
with None

show bg gallery_int at left
show sae invis:
    xpos 0.75
show crowd at left
show emicas happy at center
with dissolvecharamove

hide sae
with None



emi "おっす！　美術部の代表かなにかできたの？　他に学校の子、見かけないからさ……"



hi "うーん……さあ。それが本当ならそうなのかもな"


hi "お前はどうしたんだ？"

show emicas neutral
with charachange



emi "あたしがなによ？"



hi "えーっと……"

show emicas angry_up
with charachange



emi "あたしが美術に興味あるなんて思ってなかった？　そーゆーこと？　久夫くん"




hi "いや、そういうつもりじゃ……まあ少しは思ってたかもな、そういう言い方するなら"




hi "そうじゃなくて、お前はいつも琳とつるんでるけど、お前が美術の話をしてるのなんて聞いたことなかったからさ……"


show emicas awayfrown_up
with charachange



"笑美は機嫌を損ねて、面白くなさそうに辺りを見回す。"


show emicas closedsmile
with charachange



emi "確かにそうだよ。芸術なんて全然わかんない。でも琳は陸上の競技会に来てくれたから、恩返しするのが公平って話だよ"


show emicas wink_close
with characlose



"笑美は身を乗り出してくる。秘密がありそうな素振りをしようとするけど、悪巧みをしているようにしか見えない。"




emi "久夫くんは芸術ってわかる？"




hi "いや。わからない"




hi "全然"


show emicas closedsmile_close
with charachange



"俺が目立つように頭を振ると、笑美もくすくすと笑って元気よく頭を振る。"


show emicas happy_close
with charachange



emi "あたしもなんだ！"


show emicas wink_close
with charachange



emi "ねえ、琳と話しにいこうよ！　まだなんでしょ、あたしもまだだから"


show emicas happy_up_close
with charachange


emi "いこ！"

show nomiya invis behind emicas:
    center
    xpos 0.8
show rin invis:
    center
    xpos 1.1
with None


show bg gallery_int at center
show crowd at center
show emicas neutral_close:
    xpos 0.15
show nomiya smile:
    xpos 0.55
show rin basic_awayabsent:
    xpos 0.85
with dissolvecharamove



"笑美が俺を琳のところまで無理矢理引っ張り始める前に、野宮先生が笑美の後ろから琳を連れて現れる。"




"琳は特別な格好はしていなくて、いつもの制服に乱れた髪のままだ。"




"自然な格好でいるのが琳には一番似合っているのかもしれない。"


show emicas happy_close
with charachange


emi "先生、こんにちは！　琳も！"


"笑美は臆することなく元気に先生に挨拶する。先生は振り返って、混乱したように見下ろす。"

show nomiya frown
with charachange


no "君は？"

show emicas frown_up_close
with charachange



emi "山久学園の茨崎です。３－４の。覚えてませんか？"







"自分を知らない人間が存在しうるという可能性に、笑美は明らかにショックを受けたようだ。"


show nomiya talk
with charachange


no "おお、すまない。手塚と同じクラスだったな？"

show emicas wink_close
with charachange


emi "はい！"

show nomiya smile
with charachange


no "許してくれ、美術をとっていない生徒を覚えるのは苦手なものでな"

show emicas closedsmile_up_close
with charachange


emi "気にしないでください！"

show emicas happy_close
with charachange


emi "こんちは、琳！"

show rin basic_deadpan
with charachange


rin "やあ"

show emicas happy_up_close
with charachange


emi "とってもすっごい展覧会でよかったね！　きっと大ヒットになるよ！"


"笑美は腕を乱暴に振り上げて力説すると、俺の顔に当たりそうになる。"

show emicas wink_up_close
with charachange



emi "それにほら、久夫くんも来てくれたよ！"

show rin relaxed_nonchalant
with charachange


"琳は俺のほうを見ないし、挨拶もしない。"


hi "おめでとう、琳"



"視線は逸らしたまま、サンダルをじっと見ている。"


show emicas closedsmile_close
with charachange



"俺たち２人の間の緊張に気づかず、昨日の出来事についても知らない笑美は、無反応な琳に向かってあれこれとおしゃべりを続けている。"




"きっと笑美は、琳からあまり反応が返ってこないことに慣れているんだろう。"


stop music fadeout 5.0
$ renpy.music.set_volume(1.0, 3.0, channel="ambient")



show sae invis behind rin:
    center
    xpos 1.25
with None

show bg gallery_int at right
show crowd at right
show emicas invis:
    xpos -0.35
show nomiya smile:
    xpos 0.25
show rin relaxed_nonchalant:
    xpos 0.55
show sae neutral:
    xpos 0.8
with dissolvecharamove

hide emicas
with None



"やがて野宮先生とさえさんが琳のほうを向いて、琳を紹介する。"



"予想はついていたけど、来客が琳の腕を見て困惑する瞬間をとらえる。"


show sae smile
with charachange



"幸い、さえさんはそれに感づいて、俺たちの学校のことを簡潔に説明する。"




"疑問に満ちた顔つきが興味深々なものに早変わりする。"



"男性" "君の作品についてなにか話してくれないかね？"


"男性" "成長がとても目覚しいと私は感じたんだ、君自身は過去の作品といまの作品の違いについてなにか思うことは？"



"男性" "その若さで抽象画に手をつけるというのは本当に珍しいね"




"女性" "どうやって描くのか見てみたいわ！"




"男性" "ああ、まったくだ！　足を使うんだろう？　慣れるまでは相当苦労したんだろうね、立派なことだ"




show rin basic_surprised
with charachange


rin "私……うーん……"

play music music_rain fadein 8.0



"男性" "卒業しても芸術家としての道を進むつもりかい？"




"琳はあまりにたくさんの質問を浴びせられて、全部に答えることは望むべくもない。"




"その方がいいのかもしれない。琳は馬鹿げたことを口走ることが多すぎるからな。"




"男性" "それで、どこからアイディアを得るのかね？"

show rin relaxed_boredom
with charachange



rin "それ、４番目、いや５番目に最悪……"




"琳はずっと言葉を詰まらせている。期待のこもった質問にどんどんいらだちが募っているようだ。"


show rin negative_annoyed
with charachange


rin "ああ……"



"みんな琳が何か言うのを待っているけど、琳は黙りこくったままだ。"




"質問が一つ重なるたびに、琳の苦痛が増えていくだけだ。"


show rin basic_sad
with charachange



"慣用句で言うところの『一言多すぎる』質問を、俺は聞き損ねる。"




"エンジンが止まってしまうかのようだ。"



show rin basic_sad:
    1.2
    parallel:
        easeout 0.5 ypos 1.2
    parallel:
        "rin basic_lucid" with Dissolve(0.3, alpha=True)
with Pause(1.5)

stop ambient fadeout 7.0

scene ev rin_gallery:
    truecenter
    zoom 0.9 subpixel True
    easein 30.0 zoom 1.0
with Dissolve(0.2)
play sound sfx_pillow
with vpunch



"琳はしばらくの間ただ固まっていて、そしてジャガイモで一杯の袋のように、不恰好にひざから崩れ落ちて床に座り込む。"



"女性" "どうしたの、大丈夫？"


rin "わかんない……"


no "手塚？　どうしたんだ？"



rin "なにがおかしいのかわかんない……"




"凄絶な沈黙が琳を取り囲む人たちに覆い被さる。"




"みんな身動きもできず、琳の突然の……発作、のようなものにどう反応したらいいかわからないでいる。"



"空虚な目で前を見つめながら、琳は深く息をついて、空気が薄くなっているかのように震えて息を切らしている。"

play sound sfx_rustling
stop music fadeout 1.0

scene bg gallery_int at right
show crowd at right
show nomiya serious:
    center
    xpos 0.25
show rin negative_sad_close:
    center
    xpos 0.55 ypos 1.2
    ease 0.8 ypos 1.0
show sae scowl:
    center
    xpos 0.8
with locationchange




"誰もどうにもできないのを見て、俺はむりやり琳のもとに歩み寄ると、床から立ち上がらせて俺のほうへ寄りかからせる。"





hi "外の空気でも吸うか？　よし、ちょっと外に出よう"




"俺は返答を待つこともせず、琳の肩を引っつかむと、茫然とした顔つきの野宮先生やさえさん、笑美や他の来客の前を通り過ぎていく。"



hi "失礼します"

play sound sfx_storebell
$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 1.0

scene bg gallery_ext
with locationchange



"戸口に立つと、涼しい夜の空気が俺の顔に当たる。"


show rin negative_sad_close_ni at center
with charaenter


"琳を放すと、琳は石の壁に寄りかかって、息を整えようとする。"


hi "大丈夫か？"


show rin negative_confused_close_ni
with charachange


rin "なにもいえなかったよ……"



"琳はいまだに俺のほうを見ようとしないから、俺もそっぽを向く。"

play music music_dreamy fadein 4.0



"街灯やネオンサインが俺の視界をぼんやりと、盲目に近い状態にまで歪めてしまい、俺は仕方なく視線を戻す。"




"少なくとも琳は話している。俺に向けてではないとしても。"




hi "何を言いたかったんだ？"




"俺たちのどちらも、目に見えない友達としゃべっていると想像すればいいのかもしれない。"


show rin basic_sad_close_ni
with charachange



rin "わかんない"


show rin negative_sad_close_ni
with charachange



rin "なにかの意味のありそうな、なにか"



"……"



"長い間、沈黙が続く。"



"琳と二人きりになるのは居心地が良くない。俺はその場にないものが存在する……あるいはその場にあるものが存在しない、という想像をするのは得意じゃない。"





hi "戻ったほうがいいぜ"



hi "さえさんが招待した人もいるんだ。きっとお前に会って話したいんだと思うぞ"




hi "ほら、質問とかいろいろ聞いたり。お前があんなにがんばって描いた絵のことをさ"


show rin negative_angry_close_ni
with charachange




rin "あんな風に質問してほしくない。正しいことなんて絶対言えないのに"





hi "じゃあ何がどうなればいいんだよ？"



"……"

show rin relaxed_doubt_close_ni
with charachange


label jp_choiceR32:
menu:
    with menueffect
    rin "人が私に質問しなくてすむようになってほしい"
    "でも興味を持ってくれる人がいて嬉しくないのか？":








        return m1
    "でもそんな人に出会って、それでどうするんだよ？":



        return m2

label jp_R32a:

$ renpy.music.set_volume(0.2, 0.2, channel="ambient")



hi "でも、みんながお前の絵に興味を持ってくれて嬉しくないのか？"




hi "というか、お前が展覧会やら何やらをやってきたのはそのためなんじゃないのか"




hi "そりゃみんなだって質問するよ、面白いと思ったらさ"


show rin negative_annoyed_close_ni
with charachange



rin "月明かりのなかで裸でお風呂に入りたいと思ってたのに、日の出が２回続いたときみたいだね"



show rin negative_angry_close_ni
with charachange



rin "悪くないよ、でも……"




"……十分じゃない。琳の的外れな例えは理解できないけど、俺は琳に代わって言葉を補う。"




hi "わからないなあ"




hi "もっと嬉しそうにしてみろよ。今夜はお前が主役なんだから"




hi "みんなお前の絵を観にきてるんだぜ。すごいことじゃないか"



"俺は琳が肯定なり否定なり、何か言うのを待つけど、じっと考え込んだままだ。"




"琳は俺の質問に答えるのも、何が気に入らないのか説明するのもいやなんだ。"




"琳に言いたいことがあったとしても、その言葉は語られないまま終わる。"




"口にすることができない言葉だ。"



"俺は通りを吹き抜ける冷たい風に身震いする。風はうなりをあげて沈黙を破る。"


hi "もう中に戻ろう"


hi "みんな心配してるぜ"

stop ambient fadeout 0.5
play sound sfx_storebell

scene bg gallery_int
show crowd
show nomiya talk at twoleft
show sae neutral at tworight
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0



no "ああ、戻ったか！　気分はどうだ？　ここはずいぶんと暑いからな、油断しているとめまいを起こしてしまうぞ"


show nomiya veryhappy
with charachange



"先生は豪快に、不愉快なくらいに笑う。"


show nomiya talk
with charachange



no "元気がないときは何か飲むといいぞ、手塚"


show nomiya talk:
    center
    xpos 0.25
show sae neutral:
    center
    xpos 0.8
with charamove

show rin basic_lucid:
    center
    xpos 0.55
with charaenter


"琳は弱々しくうなずくけど、先生に琳が大丈夫なことを納得させるのには十分みたいだ。"



"先生は琳を少し前に押し出して、さっきまで話をしていた人に引き合わせる。"


show nomiya smile
with charachange


no "さて、さっき話していたことですが……"


"男性" "ええ、お会いできるのを楽しみにしてましたよ……"

stop music fadeout 8.0


"俺は会話から締め出されて、ほかのいろいろな議論の喧騒が、不明瞭な騒音になって俺の耳を満たす。"



"笑美もどこかへ行ってしまった。"



"人ごみの中心に立っていると、驚くほど寂しい気持ちになる。"



"琳だけじゃなく、誰もが何かの一部になっているような気がする。でも俺はその一部じゃないんだ。"




"俺も琳のことが嬉しい。それは本当だ。でも、同時に俺はまだ何も成し遂げていないという気にもなる。"




"琳は人間が持つ可能性の生きた証だ。琳は障害を乗り越えて、それを長所にまでした。"


stop ambient fadeout 4.0



"琳は嬉しいはずだ。"




"俺には何ができるんだ？"



"琳はここまでやり遂げた。でも俺はどこまでやれる？"

scene black
with dissolve


label jp_R32b:

$ renpy.music.set_volume(0.2, 0.2, channel="ambient")



hi "でもそんな人に出会ったとして、それでどうするんだよ？"




hi "それが万事を解決する究極の何かだって、不幸な恋人たちが末永く幸せになるようなものだって、ほんとに思ってるのか？"





show rin basic_absent_close_ni
with charachange



"俺の質問に虚ろな視線が返ってくる。琳の目の暗がりはオブラートに包まれた皮肉にも動じない。"


show rin negative_worried_close_ni
with charachange



rin "ううん、思ってない"


show rin negative_annoyed_close_ni
with charachange



rin "でもそうなったら、少なくともひとりぼっちじゃなくなるよ"




"琳は街の光に向かってささやくけど、どのみち俺にも聞こえてくる。"


show rin negative_sad_close_ni
with charachange



rin "やらなければよかった。今はまだ"



hi "展覧会をか？"

show rin basic_lucid_close_ni
with charachange



"琳はうなずくと目を閉じて、そうできることを証明するかのように静かに息をつくと、また独り言をつづける。"



hi "どうしてだ？　星のめぐり合わせが悪いなんていうつもりか？"


show rin basic_sad_close_ni
with charachange



rin "違う、そうじゃない。ちゃんと２回確認して、正しい方の、つまり左足で起き上がったし、他のことは全部左、じゃなくて右足でやったよ"



show rin negative_sad_close_ni
with charachange


rin "私なんだ"

show rin negative_worried_close_ni
with charachange



rin "私が間違ってたんだ"


hide rin
with charaexit


"琳はまっすぐ立つと伸びをして、俺の前を過ぎて通りに踏み出す。"



hi "おい、どこ行くんだよ？"


show rin basic_absent_ni
with charaenter



"琳は立ち止まって振り向くと、いぶかしげに俺を見る。"


show rin basic_awayabsent_ni
with charachange



rin "学校。帰る"



hi "え……なんでだよ？"

show rin basic_absent_ni
with charachange



rin "私でいたいから"

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

hide rin
with charaexit



"完全に混乱した俺を後に残して、琳は立ち去ってしまう。"




hi "琳！"




"でも……琳の言ったことは本当に俺の心に響いた。もしかしたらその言い方のせいかもしれない。"




"それとも{b}琳が{/b}言ったという事実が響いたのかも。"





"琳に何か言い返したい、この感じを忘れる前に。"





"その願いを聞き入れてくれたかのように、琳は足を止める。振り向かないまま、俺が言いたいことを言うのをただ待っている。考える時間なんてなかったけど……"



hi "なあ……琳……俺……ひとりぼっちでいなきゃいけないなんてことはないと思うぞ。もしそういう人に出会えないとしても"




"俺の声が届いてるかはわからないけど、どっちにしろ、琳は何も反応を見せない。"




"とうとう、琳はギャラリーから立ち去ってしまう。"


play sound sfx_storebell
stop ambient fadeout 0.5

scene bg gallery_int
show crowd at center
show nomiya frown at twoleft
show sae doubt at tworight
with locationchange

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0


no "うん？　手塚はどうした？"



"俺は頭を振るだけしかできないけど、それでは答えとしては不十分だったみたいで、結局何か言わざるをえない。"



hi "帰ってしまいました"


show nomiya stern
with charachange


no "なんだって？"


"ぞっとするような表情が先生の顔に山火事のように広がる。"


show nomiya serious
with charachange



no "なんということだ！　大失態だ！"




no "なにを考えているんだ、自分の人生でいちばん重要な機会だというのに、ただ逃げ出しただと？"


show nomiya stern
with charachange



no "お前もだ！　なぜ止めなかった？　この責任は取ってもらうぞ……"


show sae neutral
with charachange


"さえさんが静かに手をあげて制止する。"


"止めに入ってくれてよかった。周りのお客から変に見られはじめている。"

show sae smile
with charachange



sa "まあまあ、紳一。きっと人前に出て緊張しちゃったのよ。あの子のことはあなたたちほどはよく知らないけど、でもちょっと変わった子だという印象はあったから"






sa "こういうこともあるわ"


show sae neutral
with charachange



sa "きっと大丈夫よ。具合が悪くなったとでも言っておくわ。それなら納得してもらえるはずよ"


show nomiya frown
with charachange


no "しかし……"

show sae smile
with charachange



sa "周りをごらんなさい、みんなワインとおしゃべりで楽しそうじゃない"


show nomiya serious
with charachange



no "客はいいだろうが、こっちはチャンスを逃しているんだ！　人脈とコネと面識を広げるチャンスを！"


show emicas invis_close:
    center
    xpos -0.35
with None

show bg gallery_int at left
show crowd at left
show nomiya serious:
    xpos 0.5
show sae smile:
    xpos 0.9
show emicas frown_close:
    xpos 0.15
with dissolvecharamove



"どうにもならないことで大人たちが言い争っているのをよそに、笑美が俺の袖を引っ張って気を引く。"



"どうやら笑美も愉快ではないみたいだ。"

show emicas awayfrown_close
with charachange


emi "いこうよ"


hi "どこへ？"

show emicas frown_up_close
with charachange



emi "琳を探し出してケツに蹴り入れてやるの"



hi "なんだって？"

show emicas angry_close
with charachange



emi "もう信じらんない、ほんとに馬鹿なんだから！"




emi "琳ったらこんなことするなんて！　まったく、常識のかけらもないよ！"




"笑美は真剣に怒っている。足りないのは耳から昇る湯気だけだ。"





"笑美の気持ちもわかる気がする。笑美は確かにそういうタイプだからな。"




"『諦める』という言葉は笑美の辞書には絶対載らなさそうだなと思っていた。笑美は誰の辞書にも載っていてはいけないと思っているのかも。"




hi "今夜はそっとしておいてやるのがいいと思うけどな"


show emicas angry_up_close
with charachange



emi "なにそれ？　今度は琳の専門家ってわけ？"





"笑美は断固とした態度を見せて、対決するように両手を腰に当てる。"







"俺にもけんかを売りたいみたいだ。"





hi "いや、そんなの最初から無理だと思う"




hi "あいつのケツに蹴りを入れたって、あいつのためになるとは思えないってだけさ"


show emicas frown_close
with charachange



"俺の憂鬱なコメントは驚くほど効いた。笑美は小さく肩を落としてため息をつく。"




emi "わかってるよ、そんなの"




hi "そうなのか？"


stop music fadeout 2.0

show emicas awayfrown_close
with charachange



emi "前にやったときは、なんにも変わらなかったから"


stop ambient fadeout 1.0

scene ev busride_ni
with locationskip

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
play ambient sfx_businterior fadein 2.0



"学校に戻るがらがらな深夜のバスはしんとしている。"




"俺たちは一言も話さず、窓の外を流れる光を眺めている。"


stop ambient fadeout 1.0

scene bg school_dormext_full_ni
with locationskip

play music music_soothing fadein 0.5



"夜の学校の敷地内は静かで、青白い月と黄色い照明だけに照らされている。"





"俺たちは男子寮の前でおやすみを言う。"


show emicas awayfrown_up_ni at center
with charaenter



"笑美が反射的にぐっとこぶしを握るので、俺は笑美が俺の視界から消えたとたん、琳に襲いかかったりしないよう念を押さずにはいられなくなる。"




hi "琳を叱りに行ったりしないって約束しろよ？"


show emicas angry_up_ni
with charachange


"笑美は俺を見上げる。その目は怒りに煌々としていて、俺はなるべくなだめるように視線を合わせる。"


"その怒りが自分に向けられているのでないなら、怒っている女性と顔を合わせるのは簡単だ。"



"不釣り合いなにらめっこが続いたあと、笑美は負けを認めて、ため息をつくと頭を振る。"


show emicas closedsmile_ni
with charachange



emi "優しすぎるんだよ、久夫くんは"


show emicas weaksmile_ni
with charachange



emi "知ってた？"



"そういうと、少しばかりの笑顔が笑美の口元をつり上げる。かなり落ち着いたみたいだ。"


"急に雰囲気が変わるもんだな。"



"最初からそこまで怒ってたわけじゃないのかもな。"




"気分屋なのかもしれない。"




hi "もしそうなら、お前の好きにさせてたよ"

show emicas wink_ni
with charachange


emi "ということは、琳にだけ優しくしてるってこと？"




"俺たちのどちらも無意味な冗談の裏に気遣いを押し隠してるけど、結局それが俺の気分を良くしてくれる。"





"笑美は俺を挑発しようと、面白半分のにやけ顔で眉毛を揺らす。そうはいくか。"



hi "いや、お前だけには優しくしないってことだよ"

show emicas angry_up_ni
with charachange


emi "ちょっと！"


stop music fadeout 2.0


hi "おやすみ、笑美"

scene black
with dissolve

label jp_R33:

play music music_daily fadein 0.5

scene bg school_scienceroom
with locationchange


"夏休み前の最後の日も終わりに近づいている。"


"科学が期末テストの最後の科目で、それで俺たちは解放される。"



"少し天気が悪いけど、クラス全員の自由への切なる思いは、教室の中で目に見えるかのようだ。"




"今日は雨かもな、何とも言えないけど。"


$ renpy.music.set_volume(0.5, 1.0, channel="music")

scene ev rin_doodle
with locationchange



"テストはやたら簡単で、とっくに全部解き終えてしまったので、武藤先生が終了を告げるまで用紙の裏にだらだらと落書きをしている。"




"そうすれば、ミーシャが俺の肩越しに答えをこっそり覗いてくるのも防げる。"




"不注意な先生はだませるかもしれないけど、俺にはミーシャが覗こうとしていると断言できる。"





"きっとミーシャはこうやってテストを乗り切るしかないんだろう。別に義理立ててやる気にはならないので、俺はミーシャを無視して周りを見渡す。"


$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg school_scienceroom
with locationskip


"静かだ。"



"静かに紙をめくる音と、先生の絶え間ない咳き込みだけが聞こえる。"




"その静けさに、俺の周囲への注意は徐々に意識の裏側へと漂って行き、代わりに別のものに置き換わる。"




label jp_R34:
scene bg school_scienceroom
with None

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n夏休みだって？"



n "休みの間も学校に残るやつはいるし、家族のもとへ帰るやつもいる。"




n "俺はどうすればいいかわからない。帰りの電車の切符を買いに行かなきゃいけないけど、そうする気分になれない。"





n "多分実家から電話してくるだろう。母親にいつ帰ってくるんだとうるさく聞かれるし、俺もどう答えればいいか見当がついていないだろう。"




n "\nほんとにうんざりする。今の琳との関係を考えれば、ただここから抜け出して、ケリがついたふりをするなんてできないと思う。"




n "\nそれに今、琳は別の問題を抱えている。展覧会のオープニングはいい骨休めになると思っていたけど、それはとんでもない間違いだった。"




n "\n\n話がどんどんもつれていっている気がする。"


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

play sound sfx_doorknock

window show



"テスト終了１５分前の静かだけど慌しい空気に、ドアを叩く鋭いノックが割り込んでくる。"


show muto normal at center
with charaenter

$ renpy.music.set_volume(0.2, 0.0, channel="sound")


mu "どうぞ"

stop music fadeout 1.0
$ renpy.music.set_volume(1.0, 8.0, channel="sound")
play sound sfx_footsteps_hard

show bg school_scienceroom at bgleft
show muto normal at twoleft
with charamove

show nomiya serious at tworight
with charaenter



"ドアが開くと、野宮先生が現れる。ジャケットの裾を風のようにはためかせながら入ってくる。"



"武藤先生をちらっと見ると、先生も見返す。"

play music music_tension

show muto irritated
show nomiya stern
with charachange



"お互いにその視線で相手を推し量る間に、渋い表情が二人の顔に同時に広がる。"


no "すみませんがね、中井君を少しお借りしたいんですよ"


mu "ええ、{b}こちらこそ{/b}すみませんけどね、野宮先生。今テストの真っ最中でしてね"




"二人がお互いをにらみ倒そうとして、真夏の午後に突然冷たい空気が広がる。"


show nomiya serious
with charachange



no "緊急なんですよ。それに中井はもう解答を終えているようですが？"




"二人がこっちを向いて、うまそうなおやつを石にしようとしている二頭のバジリスクみたいに俺を見つめる。"




"もうかなりの間ヒマにしていたのは事実なので、野宮先生の言うとおりだけど……"


show muto normal
with charachange



mu "中井、もう一度解答を見直してくれるか？"




"武藤先生は妙なイントネーションで、メッセージを送るかのように特定の言葉に重みをつけていう。"




"先生たちの視線のプレッシャーで、俺の頭が急激に揺れる。それがなんらかの解答として受け取られたみたいだ。"


stop music fadeout 6.0

show muto irritated
with charachange



mu "そうか。なら野宮先生と一緒に行くといい、中井"




mu "かばんは持って行け。解答用紙は私のところに提出すること"


show muto smile
with charachange


mu "いい夏休みをな"



hi "あっ、ええ、先生も"




"世界全体が……いや、少なくとも教室内が、テストの手を止めて固唾を呑んで見守るなか、俺は立ち上がり、荷物をまとめてドアのところまで歩いていく。"




"首の後ろに視線を感じる。クラスのみんなは俺が居残りかなにかさせられると思ってるんだろう。夏休み前の最後の日に。"





"先生が俺に何の用事があるのか知らないけど、たぶん居残りではないだろうし、何か琳と関係のあることなんだろう。"


scene bg school_hallway3
with locationchange

play sound sfx_doorslam
with vpunch



"野宮先生は俺をどこへ連れて行くでもない、全く人のいない廊下で十分だったみたいだ。"


show nomiya serious at center
with charaenter

play music music_pearly fadein 1.0


no "手塚がどこにいるか知らないか？"


"琳は先生を避けようとしてたってわけか……そりゃそうだろうな。"



"いつまでも逃げ続けてはいられないってことに、琳は気づいてるのかな。"



hi "さあ"



hi "琳のホームルームは隣ですけど、もう聞きには行ったんですよね"


show nomiya stern
with charachange



no "当たり前だ！　このいまいましい学校の隅から隅まで探したぞ。女子寮もだ"




no "昨日、手塚を見たのはお前が最後だ。それにお前は手塚の友達だろう"


show nomiya serious
with charachange



no "お前も考えるんだ。心配じゃないのか？"




"心配だけど、俺になにができるだろう。"




"昨日、琳は理解しがたいことをした。琳自身にとってさえもだ。"




"本当に混乱しているみたいだった。"




hi "琳は考える時間が欲しいってだけかも知れませんよ。展覧会をやることについて考え直してたんじゃないかって気がします"




"違うかもしれないけど。何がまずかったかなんて、琳は全然説明しなかったし。"


show nomiya frown
with charachange



no "何を考え直したというんだ？"




hi "さあ。そんな気がしたってだけです"




"先生相手にこの態度はちょっと不誠実だけど、これは俺が首を突っ込むべきことじゃない。"




"先生は俺のもとへ来た……そうだ、どうして？　俺が琳の親友かなにかだとでも思ってるんだろうけど、この件で俺が役に立てるとは思えない。"


show nomiya serious
with charachange



"先生は機嫌を悪くし、困惑して頭をかく。"




no "いったいどうしてしまったんだ？　実に手塚らしくない、いつも目標に向かって邁進していたというのに"




"『目標に邁進』だって？　琳を説明する言葉としては見当違いな気がする。"




"俺からすれば、よく言っても琳はいつも何かに追い立てられているようだった。"




hi "その、失礼なことを言うつもりはないんですけど、そもそも琳をそっち向きに後押ししたのは先生じゃないんですか？"


show nomiya dreamy
with charachange



no "手塚の目標は私の目標だ。それが師のつとめというものだ"




hi "そうかもしれません。ただ俺は、絵を描くことで琳が幸せになれるのかわからなくて"


show nomiya stern
with charachange



no "お前にそんなことを言う筋合いはないぞ、中井"




"先生は急に怒りで声を荒げる。何かまずいことでも言ったか？"


show nomiya serious
with charachange



no "何もわかっていないな。幸福の問題じゃない。何を得るにしても、そこには支払うべき犠牲というものがあるのだ"


show nomiya stern
with charachange



no "ただより高いものはない。しかし手塚が一瞬でも疑いを持ったせいでその才能を無駄にするなどということを私がしただろうか……許しただろうか？　そんなはずはない！"




no "絵を描くことも作業だ、他と何の違いもない。お前には手塚がやすやすと絵を描いているように見えるかもしれん、だが手塚は毎日懸命に取り組んでいるんだ"



no "非凡であるためには、非凡なる努力を積み重ねなければならない"



"先生がしゃべればしゃべるほど、琳はそんなこと考えていないという気持ちが強くなる。実際にどう思っているのかなんて全くわからないけど。"


show nomiya serious
with charachange



no "手塚がなぜ夏休みを犠牲にし、休んだ授業や試験を後から埋め合わせてまで作品を展示しようとしたのか、私にはよくわかるぞ"




no "これが手塚の選んだ道だ。それを最後まで進むのは容易なことではない"




no "手塚は若いし、この学校の他の子たちと同じように苦労を負っているが、そんなことは言い訳にはならない"



"そこで話は終わる。"


hi "でも――"

show nomiya smile
with charachange


no "お前には手塚にとっての芸術のようなものがあるのか？"


hi "いえ……"



"そのとおりだ。自分の将来についてはあいまいな考えしかない。狙うべきゴールもない。がむしゃらに追い求める夢もない。"




"俺は何か興味を持てそうなこと、やる気をかき立てられるようなことを求めて美術部に入った。"



"そんなものを見つけられたか？"



"結局俺が見つけたのは……琳だけだった。"




hi "いえ、俺にはあんな情熱はないです"


show nomiya serious
with charachange


no "それでは理解できまい"



"先生はきっぱりと言う。そこに反論の余地はない。"




hi "でも……琳は自分でもわかってないのかも知れません"




"それでも、俺は反論する。当てつけ以外の何物でもないけど。"


show nomiya stern
with charachange



no "理解していないわけがなかろう。この数週間ずっと授業を休むどころか、学校にも登校せずに展覧会に全力で取り組んでいたんだ。ばかげたことを言うな"




"ばかげたことを言っているつもりはない。でも反論しなかったので、野宮先生は自分の勝ちと思ったみたいだ。"


show nomiya smile
with charachange



no "とにかく、手塚はあまり顔を出さなかったが、展覧会のオープニングは大成功だった"




no "多くの人が手塚の作品に関心を持ってくれた。しかも一枚はそれなりの値段で売れたんだ"




hi "へえ、それは良かったんじゃないですか？"



show nomiya veryhappy
with charachange



no "ああ、すばらしい知らせだ！　手塚もこれを聞いて目を覚ましてくれればと願っていたのだがな……"




"先生はため息をつくと、眼鏡を外してジャケットで拭き、もう一度鼻にかけ直す。"


show nomiya smile
with charachange



no "とにかくだ、もう行かなくてはならん。さえや他の方々との間で、収拾をつけないといけない件があるのでな"




no "もし手塚を見たら、私のところへ来るよう伝えてくれ。それと、いい夏休みをな"



hi "どうも……"

stop music fadeout 6.0
play sound sfx_footsteps_hard
$ renpy.music.set_volume(0.0, 4.0, channel="sound")

hide nomiya
with charaexit



"先生が角を曲がって見えなくなると、俺は琳が実際にいそうな場所をじっくりと考える。"




"琳はそういう『秘密の場所』を一つどころか六つは知っていそうだ。"




"この混乱を解決したいという気持ちと、これを最後に投げ出してしまいたいという気持ちとをはかりにかける。"




"使われていない教室がすぐ先にある。"



"どうしようか？"


"……"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_dooropen

scene bg school_room34
with locationchange


"ドアを押し開けると、暗い影だけが俺を出迎える。"


hi "おーい"


label jp_R35:

scene bg school_scienceroom
with None

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n夏休みだって？"



n "休みの間も学校に残るやつはいるし、家族のもとへ帰るやつもいる。"




n "俺も地元に帰って、俺がちゃんと元気にやってるって報告したほうがいいんだろうな。"




n "学校に残ったって、大してやることもないだろうし。"




n "次の学期はぴりぴりするだろうな。みんな卒業したあとのことを真剣に考えないといけなくなる。"



n "\n\nそれは俺もだけど……"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene ev rin_doodle_all
with silentwhiteout

window show



"自分の落書きを見て、それを取っておこうという気が失せる。生気のない線がぐちゃぐちゃに絡まっている。テスト用紙の裏でなければ紙の無駄でしかない。"


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve



n "\n\n\n特に何を描くつもりでもなかったからだろうか。"




n "暇をつぶしたかっただけなので、絵もまさしく俺みたいになったんだ。"




n "どこへ向かうあてもない。"



n "\nもっと才能があれば簡単なんだけどな、琳みたいに。"


n "あいつなら簡単だ。"



n "なんだかうらやましくなる。"




n "それなのに琳はちっとも嬉しそうじゃなくて、腹が立つ。"


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene bg school_scienceroom
show muto smile at center
with locationskip

window show



mu "よおし……それまで！"




"武藤先生のテストの終わりを告げる声に、クラスの半分から不満のうめき声が上がる。"




"無理もない、テストはなんだか難しかったからな。"




"武藤先生はそんなに厳しいほうじゃないけど、俺たちのクラスには大きな期待を寄せている。俺たち全員が科学者になるのがお望みなんだろう。"


show muto normal
with charachange



mu "鉛筆を置いて、回答用紙を提出するように"



"いちばん大きなうめき声は俺のすぐ横から聞こえてくる。"

show misha invis_close:
    center
    xpos -0.2
    ypos 1.13
with None

show bg school_scienceroom at bgright
show muto normal at tworight
show misha perky_sad_close:
    xpos 0.15
with dissolvecharamove


"ミーシャの落胆が手に取るようにわかる。"



"希望をなくした暗いオーラがミーシャの席から漂ってきて、俺は驚くと同時に同情する。"

show muto smile
with charachange



mu "さて、お前たちを解放する前にホームルームをしないといけないが、いくつか連絡事項があるだけだし、すぐに済むだろう……"




"先生の連絡が重要だったためしがないので、俺は片耳で話を聞くだけだ。"




"ミーシャはあまりに落ち込んでいて、話を聞いているふりもできないみたいだ。"



"打ちひしがれたように、机に頭を突っ伏している。"


hi "元気だせよ、ミーシャ"


hi "夏休みだぜ！　テストの心配はするなよ"

show misha sign_smile_close
with charachange


mi "ありがと、ひっちゃん"


"渋い顔がかすかな笑顔になると、興奮の火花がその目にともる。"

show misha perky_smile_close
with charachange



mi "夏休みはなにするの、ひっちゃん？"

show misha hips_smile_close
with charachange




mi "わたしはしっちゃんの家に行くんだ。こーんなすっごい豪邸なんだよ！　超楽しみ～！"



show misha hips_grin_close
with charachange


mi "最高の夏休みになること請け合いだね～！"



"ミーシャはたった数秒で自分の不遇をきれいさっぱり忘れ去ったみたいで、椅子の上で熱狂をかき立てるように上下に跳ねる。"




hi "俺はなんにも予定なし、かな……"

show misha sign_smile_close
with charachange



mi "そうなの～？ ひっちゃんもさ――"

show misha perky_confused_close
with charachange



"ミーシャの肩をたたく指が、注意をそちらへと向かわせる。"


show muto irritated
with charachange



"静音が武藤先生を指差していて、先生は期待するように２人を見返している。"


show misha sign_confused_close
with charachange



mi "あれれ！　ごめんね、しっちゃん。先生の話、もう終わってたんだ、えへへ～"



"ミーシャは咳払いをして、深く息をつくと……"

show misha hips_grin_close:
    ypos 1.0
with dissolvecharamove


mi "起立！"


"俺もみんなと一緒に立ち上がる。"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve



n "\n\nここに来たときから、いつも不思議に思っていた。"




n "車椅子から離れられない生徒は、この毎日の習わしを『正しく』行えないことをどう思っているんだろう？"




n "利便のために他の多くの習わしを省略している場で、これだけを続けるというのは不作法というものだろうか？"




n "誰かに聞いたことは一度もないけど、ここに来てからの数週間のあいだに達した結論は、間違いなく彼らはそれを侮辱と感じていない、ということだ。"



n "みんなわかってるんだ。"



n "この学校のいいところはそこだ。どんなことであれ、むやみに堅苦しいことを言うやつはいない。誰もが……お互いを理解し、思いやっている。"


stop music fadeout 4.0


n "\n\n世界全体がそうなればいいのにな。"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene black
with locationchange

window show



mi "れぇーい！"




scene bg school_dormhisao
with shorttimeskip

play sound sfx_paper
play music music_tranquil fadein 3.0



"紙を指でつまんだときに擦れる音を聞きながら、俺はゆっくりとページをめくる。"


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve



n "じっとしていられない。"



n "夏休みだ。"



n "授業もない、宿題もない、美術部の集まりもない。なんでも好きなことをして過ごせる、ただただ自由な時間。"





n "なにもする気がしない。"



n "ミーシャを励まそうとしたけど、俺自身、それほど元気がない。"



n "正直なところ、自由な時間というのには怖気づいてしまう。病院のことと、とにかくやり過ごすしかなかった長くて無意味な日々を思い出させる。"




n "唯一の違いといえば、俺は病棟に閉じ込められていて、地獄の門番のような看護婦に見張られていたということくらいだ。"




n "あのときは、本を読むことがいい気晴らしになったけど、夏休みをそれだけで過ごすというのはなんだか……ガリ勉みたいだ。"



n "別にいま本を読んでいることとは関係ないけど……いまはただ時間をつぶして、不安を紛らわせているだけだ。"



n "それに俺の関心は他のことに向いている。でもあっちこっちに広がりすぎていて、そのどれも把握できていない。"


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

window show


"それでこの本は、火曜日からゆ{w=0.3}っ{w=0.3}く{w=0.3}り{w=0.3}と{w=0.3}読み進めているわけだ。"



"作者がこの本を書くのにかかった時間よりも長くなりそうだ。"




"しばらく読むのをやめたり、また少し読んだり、最初から読み直したり、同じページを２回ずつ読んだりする。"




"ダメだ。ぜんぜん集中できない。"




"念のためにこの本を持って、新鮮な空気と、暇つぶしのネタを求めて外に出る。"


scene bg school_courtyard
with locationskip


"校門へ向かう生徒たちとすれ違って、中庭に向かう。"



"そのうち何人かがトランクを引っ張っているのを見るに、気の早いやつはもう家路につくみたいだ。"



"どんなに山久が居心地のいい場所でも、我が家は我が家なんだろうな。夏休み中、ずっとここに残るのもいるらしいけど。"



"太陽の高さに関係なく、中庭はその中央に常に陽が当たるくらいの大きさがある。"




"俺は真ん中で足を止めて暖かさを体で感じる。"




"本校舎の方を見ると、まぶしさで目を開けていられないくらいだ。"




"もうほとんど人がいなくなってしまったみたいだ。"




"今日は優子さんはいなかったから、次に図書室から本を借りられるのは休みが明けてからだな。"




"どこかに公立図書館があるのは間違いないけど、面倒すぎてどこにあるのか探す気にはなれない。"


scene bg school_lobby
with locationskip



"ロビーも同じくらい人の気配がなくて、俺はのんびりとした散歩を考えていたよりも早く切り上げて、寮に戻るはめになる。"




"とはいえ、そもそも何を考えていたのかよくわかっていなかった。"


scene bg school_girlsdormhall
with locationskip


"衝動的に、琳か笑美がいないかと思って俺は女子寮に足を運ぶ。"



"でも二人ともいないので、自分の無気力をくよくよと嘆くために部屋に戻る。"


window hide

scene bg school_dormhisao
with locationskip

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear
nvl show dissolve



n "\n\n琳としっかり話さないといけない。"




n "あいつには本当にイライラする。"




n "\n\n重力と概念的に等価な何かに逆らうかのように、琳は狂気や不可解さ、不安定さの隙間をぬうような、細いジグザグの線の上でバランスをとっている。"




n "琳は俺の心を動かしもする。俺が知らなかった……いや正確には、存在してほしくなかったような方法で俺を試す。"




n "\n\nこの気持ちは本当に愛なんだろうか。それとも俺が思い違いをしているだけなのか。"




n "こんなことを考えるなんて、狂気に違いないよな？"


nvl clear



n "\n\nそれから一日中、琳や病院、山久や夏休みのことが頭を駆けめぐった。"



n "\n集中することにさえ集中できない。"



n "\n考えがでたらめに浮かんでは消え、小さすぎる思考のかけらへとばらばらに崩れていく。"




n "\n俺は本を拾い上げてどうにか１００ページ読み進めたけど、明日までにはどういう話だったのかきれいさっぱり忘れている自信がある。"




n "\n部屋を掃除しようとするけど、それさえわずらわしいことだった。時間がかかりすぎるし、細かいところにより多くの注意を払わなきゃいけない。"




n "いつものことだけど。『やることがない』というのは、やることがあってもなにもしないということなんだ。"


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene bg school_dormhisao_blurred_ss
show phone mobile at center
with shorttimeskip

window show



"案の定、母親から電話があって、明日か、それがだめなら明後日の新幹線のチケットが取れるかどうか確認すると約束してしまった。"


window hide
nvl clear

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

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl show dissolve



n "\n\nどっちにしろ明日は街に出る。買い物でもしよう。"




n "別に必要なものがあるわけじゃないけど、サマーセールをやってるかもしれないし、なにか……買ってもいいだろう。"


stop music fadeout 10.0



n "\n\nどうして自分に無理強いしてるんだ？"




n "昔は、やることがなくたって何も不満に思わなかった。時々運動場でボールを蹴るのは別として。"




n "今は、どうにも落ち着いていられない。"




n "俺が変わったからなのか、それとも俺のいる世界が変わったのか？"


nvl hide dissolve
nvl clear

scene bg school_dormhisao_ni
with shorttimeskip

window show



"１１時になると、暗闇が俺を眠りへと誘う。"


window hide

show pills:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)

window show



"ナイトテーブルの上に薬の容器が当たり障りなく並べられている。まったく魅力的でないし、むしろ露骨に現実を突きつけてくる。"




"夜だから３つの容器を開けて、大きな楕円形の薬と、２つの小さな丸い薬、それから自分で半分に割る大きくて平たい薬を容器から取り出し、容器を閉めて、新鮮な水道水で一気に飲みこまないといけない。"


window hide

show pills:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide pills
with None

window show


"水は金属の味がする。"



"それでも薬と一緒に飲み込んで、俺はシャワー室へ向かう。"


scene bg school_dormbathroom
with locationskip



"歯磨きという頭を使わない作業は、考えを整理するのにちょうどいい。"




"塊の中から一つの思考が現れ、はっきりと他の思考の上にそびえ立っている。"


window hide
nvl clear
nvl show dissolve


n "\n\n\n\n\n\n\n\n\n琳に会いたい。"



n "怒って琳を怒鳴りつけたのを、休みの前の俺たち２人の最後にはできない。"


nvl hide dissolve
nvl clear

scene bg school_dormhisao_ni
with locationskip

nvl show dissolve


n "\n\n\n\n\n\n\n\n琳に会わないと。明日には。"



n "混乱した心は眠りにあっけなく打ち倒される。"


nvl hide dissolve
nvl clear

$ suppress_window_before_timeskip = True

scene black
with shuteye
label jp_R36:


$ renpy.music.set_volume(1.0, 0.0, channel="music")
$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0

scene bg misc_sky_rn
show rain normal
show hisaowindow
with locationchange



"数え切れないくらいたくさんの悪い予兆のように、雨が俺の夏休みに降り注いでいる。"




"幸い、俺は迷信なんて信じない方だけど、この悪い天気じゃこっちの気も滅入る。"




"朝からずっとこの調子で、やみそうもない。"




"分厚い灰色の雲の塊が、空と一緒に俺の気分にも影を落とす。"



"ふと思い立って、朝のうちに掃除を終えたけど、その後は窓から空を眺めて晴れるのを願うだけだった。"



"ひっきりなしに雨が屋根や道路を叩く音に聞き入ってしまう。単調な雑音が気をおかしくさせる。"



"……"


"…………"

$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

scene bg school_dormhisao_rn
with locationchange


"こうしててもはじまらない。行かないと。"




"今すぐ荷造りするべきか、それとも後にするか？"


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg school_dormhallway
with locationchange



"荷造りは後にして外に出る。健二の部屋の前で足を止めると、ドスンという奇妙な音が聞こえてくる。"


show rain normal behind bg
with None



"あいつが何をしているのか知るのが恐ろしいので、絶対にノックはしない。"


$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show bg school_dormext_full_rn as bg2 behind rain
hide bg
with locationskip



"頼りの傘を差して雨中に繰り出すと、女子寮に向かって空き地を横切る。"


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg school_girlsdormhall
with locationskip

play sound sfx_doorknock2


"琳の部屋のドアをノックしても返事はない。代わりに後ろのドアが開く。"

play sound sfx_dooropen

show emicas invis:
    center
    xpos 0.3
with None

show emicas happy at center
with dissolvecharamove

play music music_emi fadein 0.5



emi "久夫くん？　こんちわ！"


show emicas awayfrown
with charachange



emi "ひどい天気だね。朝のジョギングも走れなかったよ"




"笑美は眉をひそめるけど、俺だったら喜びそうなものだ。笑美の朝のジョギングは気楽なものとはほど遠いからな。"



hi "ああ、よお。俺――"

show emicas neutral
with charachange



emi "もし琳を探してるなら、そこにはいないと思うよ"




hi "最近あいつに会ったか？"

show emicas grin_up
with charachange


emi "うん、ちょうど今朝起こしにいったときにね"



"起こしたことを話に出した笑美は猫のようにあくびして、俺はばかみたいな気分になる。"




"そりゃ笑美は琳に会ってるに決まってる。いつも琳を起こして、着替えを手伝っているんだから。弁当を作ってやることだってある。"




"共通点なんてなさそうなのに、姉妹みたいだな。"



label jp_R36a:



"どっちが姉だろう？　きっと笑美だな。全然そんな感じじゃないけど。"




"周りには間抜けだと思われてそうな雰囲気があるけど、笑美はほんとうに熱心だ。"





"この明るい笑顔の裏で、こんなにもまっすぐであることが奇妙に思えるのはどうしてだろう？"



label jp_R36x:

show emicas frown_up
with charachange


emi "それで、何時間か前にギャラリーにいったよ……ちょっと、聞いてる？"



"きっと俺は妙な顔でもしてるんだろう。笑美は不思議そうに顔を傾け、興味津々のまん丸い目つきで俺を見ている。"


show emicas neutral
with charachange


emi "ねーえ？"



"そのあどけない表情は俺の注意を引こうとしているみたいだ。"



hi "ああ、聞いてるよ……"

show emicas weaksmile
with charachange


emi "ひとつ聞いてもいい？"


hi "もちろん"

show emicas awayfrown
with charachange


"笑美は眉間にしわを寄せると、なにかに備えるかのようにくちびるを舐める。"

show emicas frown
with charachange


emi "どうして琳のこと、そんなにかまうの？"

show emicas neutral
with charachange




emi "ていうか、久夫くんはあたしよりもずっと琳と一緒にいると思うんだ。琳とは一緒のベッドで寝たりもしてたんだよ、その、最近までは、ね"





hi "あいつの髪をくしゃくしゃにして出入り禁止になったからだろ？"


show emicas blush
with charachange



"恐怖のショックで笑美の目が２倍は大きくなり、いつも以上にお皿のような形に広がる。同時に頬と耳はかなり真っ赤になる。"


show emicas angry_up
with charachange




emi "琳、話したの！？　うわあ……琳のやつ首絞めてやる、さもなきゃもっとひどい目に……"



"笑美の軽蔑が俺に向かないように笑いをこらえる。"

show emicas closedsmile
with charachange



"笑美はすぐに屈辱から立ち直り、同時に琳のことも許したみたいで、俺に視線を戻す。"


show emicas smile
with charachange



emi "とにかく、久夫くんは琳に惚れちゃったりしてるわけ？"






"おっと。マジで求婚相手の姉に問い詰められてるような気がするぞ。笑美はなんだかおせっかい気味だ。あまりいい意味ではなく。そもそもいい意味でのおせっかいなんてありうるのかどうか怪しいけど。"









"正直に言うと、ミーシャとなら似合いのパートナーになれるだろうな。恐ろしすぎる。"



hi "もう２つ目の質問じゃないか、答えてやる必要はないね"



"俺は素早く、純粋なクールさと無関心さで固めた表情を作ろうとする。"




"俺自身の気持ちをごまかせているかどうかも怪しい。"


show emicas evil
with charachange



"少なくとも、笑美は眉毛を危なっかしく揺すっていて、口元は嫌味な作り笑いを浮かべている。"



emi "それはイエスってこと？"


hi "いいや、イエスじゃない"

show emicas neutral
with charachange



"立ち入りすぎたその質問に答えなかったことには明らかに不満なようだけど、諦めるだけの分別はあるみたいだ。"


show emicas wink
with charachange



"それでも子供のように俺に舌を突き出して、またクスクスと笑う。"


show emicas closedsmile
with charachange



emi "それが君の答えなら、これ以上話すことはないかな"



"別に怒ってるわけじゃないことはすぐわかる。"

show emicas happy
with charachange




emi "それに荷造りしないといけないしね。バスに乗り遅れたらママが心配しちゃう"




emi "じゃあね！"


hi "ああ、またな"

stop music fadeout 4.0

hide emicas
with charaexit

play sound sfx_doorclose


"笑美が部屋に引き下がると、俺は廊下でひとりきりになる。"



"俺と琳の間のことは笑美には関係ない、だろ？"




"だから俺はけんかのことも笑美には話さずじまいだった。琳も何も教えていないに違いない。"




"たぶん……友達同士であっても、話さないことはあるんだろう。"



"……"



"さて、琳がギャラリーにいるなら、俺もあっちまで足を延ばさないとな。"




"やっと部屋から出られたんだから、街まで出るのも大したことはないだろう。"




"切符を買いに行くこともできたけど、家に帰るのは後回しだ。少なくとも明日までは。"


show rain normal behind bg
with None


"この雨の中、荷物を抱えて駅までいくのはごめんだ。荷物っていったってそう多いわけじゃないけど。"

$ renpy.music.set_volume(1.0, 3.0, channel="ambient")

show bg city_street4_rn as bg2 behind rain
hide bg
with shorttimeskip



"雨はあらゆる輪郭をとても不明瞭にする。だんだんと消え去っていくかのように。"




"街の景色が、はっきりとした建物や車の形から、濃淡のはっきりしない灰色の、形を持たない集まりに変わっていく。"





"土砂降りの中を歩く羽目になったかわいそうな人たちは、できるだけ急いで移動して、お互いの不運を哀れみあっている。"


show bg gallery_ext_rn as bg2
with locationchange


"最後の曲がり角、いわば２２番目の角を曲がる。こんな駄洒落に喜んでいるなんて馬鹿みたいだ。"


"ドアは俺を暖かく招き入れてくれる。"

$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
play sound sfx_storebell 
play music music_soothing fadein 0.5

scene bg gallery_int
with locationchange



"雨水が傘からしたたって、興味深い、なかば芸術的な模様を床に作っていく。"




"靴が俺の足跡に小さな水たまりを作って、雨水アートを仕上げているのを除けば、俺自身は濡れていない。"


show nomiya smile at twoleft
show sae neutral at tworight
with charaenter



"野宮先生もいて、さえさんとギャラリーの奥で雑談している。でも琳の姿はどこにも見えない。"




"上にいるのかもな。"




"来客は一人もいない。それもそうだろう、首にバケツをひっくり返したような雨をかぶってまで、この天気の中をわざわざやってくる人なんていやしない。"


show sae smile
with charachange


sa "いらっしゃい"


hi "どうも。邪魔してすみません……"

show nomiya talk
with charachange



no "ああ、中井じゃないか"


show nomiya smile
with charachange



no "わざわざここまで会いに来たのか？"




hi "ええと……いえ、ただ思い立っただけです。このあたりをぶらついて買い物してて、それで立ち寄ろうと思って"



"他愛のない嘘が反射的に出て、俺は自分に驚く。"



"琳に会いに来た、とはっきりとは言いたくないのかもしれない。どう見てもそうなのに。"


show sae doubt
with charachange


sa "まあ、ずいぶんな日に買い物するのね。寒いでしょう、お茶でもいかが？"


hi "ありがとうございます、でも平気です"



hi "でも確かに天気は良くないですね。夏休みの初日に雨っていうのはなんだか気が滅入ります"


show nomiya veryhappy
show sae neutral
with charachange


no "はっはっは！　天気なんてそのうち良くなるさ！"


"野宮先生は元気よく笑い声をあげる。耳障りといったほうが近い。"


hi "先生は雨には落ち込まないんですね？"

show nomiya smile
with charachange



no "まあ、晴れた天気も好きだがね。今から人に会うためにここを出るところだったのだが、ジャケットを濡らしたくなかったのでな。これはとても高いんだ"


show nomiya talk
with charachange


no "だがもちろん、気分はいいぞ！"

show nomiya smile
with charachange


no "展覧会はどうだったかね？　すばらしかっただろう？"


hi "ええ、とても凝ってましたね"



"俺の適当な返事は先生をおだてるだけだ。ギャラリーの中を歩き回りながら、展覧会のオープニングについてしゃべくっている。"




"先生は動いているときのほうがよく話すし、声も大きい。部活の時もそうだった。"


show nomiya veryhappy
with charachange



no "もっとたくさんの良い人々と話をして、有益な付き合いを築いていかないとな"


show nomiya smile
with charachange



no "なんと手塚の絵が１枚、大阪から来たコレクターに売れたんだ"


$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

show rin_exhibition_sold at center
with locationchange



"壁の空いたスペースまで先生の視線を追っていく。あそこにどんな絵がかかっていたのか思い出すこともできない。"




"とにかく、今はもうなくなってしまった。"


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

hide rin_exhibition_sold
show nomiya talk
with charachange



no "手塚があのめまいの発作から回復したのは幸運だったな"


show nomiya smile
with charachange



no "あの後、ちょっと口数が少なくなったので、よく休むように言っておいた。とはいえ、手塚は日ごろからかなり内気だったからな"




"内気だって？　とにかく、俺はただ先生の話に合わせてうなずく。"


show nomiya talktongue
with charachange



no "反応はおおむね大好評だった。友人に頼んで、雑誌に小さな記事を書いてもらえるかもしれん――"




sa "紳一、打ち合わせでしょう。高橋さんを待たせてるわ"



show nomiya serious
with charachange



"さえさんの一言に先生は言葉を切り、腕時計を確認する。"



"先生は演説を中断させられたことへの不満に顔をしかめる。"

show nomiya smile
with charachange


no "ああ、そうか。よし、では行くとするか。また９月に会おう、中井"


hi "はい"

hide nomiya
with charaexit

play sound sfx_storebell
stop music fadeout 4.0



"やれやれ。始まったばかりの琳の芸術家稼業のことになると、先生は抑えがきかないな。"




"成功するまでは長い道のりになるんだろうけど、琳がもっと協力的だったら、先生もここまで苦労しないだろうな。"


$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve



n "\n琳はうまくやっているときでさえ、優柔不断すぎる。あのときの『めまいの発作』みたいに。"




n "パニックか何かに陥ってしまったのに、俺はなにも手助けをしなかった。"



n "俺はため息をつく。"



n "これじゃ俺と琳の間の溝は広がっていくばかりだ。"




n "琳はすごいやつになろうとしてるのに、俺は相変わらず泥沼にはまっているような気分だ。自分も何かを成し遂げるために努力するんだと心に決めたのに。"




n "それに加えてけんかまでしてしまった。話をしない期間が長引くほど、仲直りするのも難しくなる。"




n "俺たちがそう望んだとしてもだ。俺は琳の思いが一度もわからなかった。今では自分の思いもよくわからなくなっている。"




n "琳のことを理解できたらいいのにと思う。でも琳は解釈できるようなそぶりをあまり見せない。"




n "なにかを隠しているわけじゃない。ただどの日であろうと、琳の話を理解しようとする俺の試みを受け付けないように見えるだけだ。"


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

show sae smile
with charachange

window show


sa "どうかしたの？"


"俺はギャラリーの真ん中で、長い時間ぼんやりしていることに気づく。"


hi "あー……いえ、別に……"



"俺は近くの絵を見るふりをして、さえさんの気をそらす。"


$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
play music music_another fadein 0.5

scene rin_exhibition_c:
    truecenter
    zoom 1.0 subpixel True
    ease 30.0 zoom 1.1
with locationchange



"前にも見たな。"




"今となっては見慣れた色遣いだ。色がお互いにねじれ、溶け合って、一見すると不規則だけど、言ってみれば景色の裏でなにかが起きているような印象を与える。"




"琳のスタイルはほんとうに琳らしい。抽象的で、理解不能で、色鮮やかだ。"



"不思議だ。"



"芸術家というものを理解するには、芸術を理解しなくちゃいけないんだろうか？"


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg gallery_int
with locationchange


hi "うーん……聞きたいことがあるんです"

show sae smile at center
with charaenter


sa "なにかしら？"



"さえさんはぼんやりとめくっていた雑誌から顔を上げる。俺がふと興味を示したことに嬉しそうだ。"



hi "さえさんはどうやって作品を解釈しているんですか？"


show sae doubt
with charachange


sa "どういうことかしら？"



"その質問が説明なしでは答えることもできないくらい分かりにくいものだったかのように、さえさんの眉は高く上がり、尋ねるような孤を描く。"




hi "バカな質問だったらすみません"



hi "俺はプロのようには芸術を理解できてないと思うんです"

show sae smile
with charachange



sa "あら、何も難しいことなんてないのよ"




"さえさんは俺の質問をシンプルだけど、わかりやすい手首の動きで払いのける。"


show sae neutral
with charachange



sa "みんな好きなように読み取ってるのよ。解釈というのは作り手の意図次第であるのと同じくらいに、それを見る者次第でもある"




sa "『プロ』はみんな自分なりの見方を持ってる。なぜかというと、美学というものがあってね"




sa "芸術にはパターンがある。なんでもそうね。私たちはそのパターンを観察して何らかの結論を導くことができる、と仮定しているの"




"さえさんの声はまるで先生みたいで、聞き手の注意を保つために無作為に言葉を強調しながら講義をしている。"


show sae smile
with charachange



sa "結局は、ものすごく意味のないことなんでしょうね"




"今度は物思いに沈みながら独り言をつぶやくけど、それは俺にも十分聞こえるほど大きい。"




sa "優れた芸術作品は、人に何かを感じさせる。ただそれだけのことね"




sa "気持ちが変われば、作り上げる芸術にも、目にする芸術にも影響を与えるわ"



hi "でも……"

show sae neutral
with charachange


sa "こんな話があるの"


hi "またですか？　この前のには参りましたよ……"


sa "大事なことよ、聞きなさい……"




sa "１００年ほど前、ほぼ無名の芸術家が、その友人のカサヘマスが自殺したという知らせを受けた"






sa "それは彼がその友人と離れていて、しばらく会っていないというときに起きた"



sa "当然、そんな知らせを受けたら、普通よりもさらに大きな葛藤を感じたはずよ"




sa "それから４年間、その知らせにあまりに影響を受けすぎて、この芸術家は単彩の絵を描くこと以外には何もしなかった"




sa "何をするにしても、彼は必ずその同じ色に戻ってきた。その呪縛から抜け出すまでね"




"さえさんはしばらく言葉を切って、俺が話についてきているか確認する。"




"ちゃんとついていってる。ある程度は。俺は語り手が生きがいにしているような、お定まりの相づちを打つ。"



hi "それで……"



"さえさんが期待しているような質問が思い浮かばず、そこから言葉が続かない。"




"半人前のソクラテスのように、さえさんは俺の目の前に啓発のための材料をすべて並べきったと思っていたようだ。"


show sae doubt
with charachange



sa "まだわからないの？"




"ただ、この聴講生はそれを理解するには鈍すぎたということだ。"


show sae scowl
with charachange



"さえさんは俺の鈍感さに不満そうだ。"




sa "ピカソの青の時代は美術史のなかでもっとも賞賛されたもののひとつよ。でもあの名作の数々を描いていたとき、彼が何を思っていたかなんて誰がわかるかしら？"




sa "悲しみ？　慕情？　後悔？"



sa "誰にもわからないわ"



sa "もし今、あなたが青の時代の作品を見れば、ピカソの友人カサヘマスのことを知る前とはまた違った解釈をするでしょう"


show sae neutral
with charachange



sa "芸術に触れるというのはいつでも個人的な経験であって、偶然や状況によってしか相互性は生まれないの"




sa "どんな芸術作品にも無数の説明が存在しうるけど、そのどれも作者の意図するところじゃない、ということもあり得るかもしれない"


show sae smile
with charachange




sa "人は孤島ではない、はずなのにね？"



"俺は最後の言葉がなにを意味するのかわからないままうなずく。"



"さえさんのいったことは意味が通ってる。ひとつを除けば。"




"もし芸術が琳の言ったようにコミュニケーションで、しかしさえさんの言ったように誰もが自分だけの秘密の言語を使っているのなら、人が意思を通じ合うことなんて望みようもないじゃないか？"




"あまりに無意味で、無駄に思える。"



"芸術はやっぱり俺の分野じゃない。"

$ renpy.music.set_volume(0.1, 1.0, channel="ambient")

scene bg gallery_exhibition
with locationchange



"さえさんはまた芸術雑誌を読み始める。俺はギャラリーを一周して、琳が自分の絵から何を見ているのか確かめようとする。"




"大雨に取り巻かれたギャラリーは落ち着いた雰囲気で満たされる。大きな窓のおかげで、あからさまな孤独も多少は快適なものになる。"


play sound sfx_storebell
stop music fadeout 2.0



"ベルの音が穏やかな雰囲気を破る。"


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")

scene bg gallery_int
with locationchange

show rin relaxed_nonchalant at center
with charaenter


"琳が肩でドアを押し開け、入ってくる。"



"そもそも琳に会うためにここに来たのをすっかり忘れていた。"


show rin relaxed_boredom
with charachange



rin "用意できたと思いま――{w=0.3}{nw}"


show rin relaxed_surprised
with charachange


"俺がいることに気づくと、言葉の途中で固まってしまう。"



"針の落ちる音さえ聞こえそうな沈黙はきっかり１.５秒続く。俺もさえさんも口を開くには短すぎたけど、琳が反応するには十分だった。"


show rin negative_annoyed
with charachange


rin "散歩してくる"

hide rin
with charaexit

play sound sfx_storebell



"琳らしくない、向こう見ずな勢いで外に戻ってしまう。雨が降っていることも忘れているみたいだ。"


show rain normal behind bg



"あまり考えることなく、俺は傘をつかむと急いで琳を追う。"


play sound sfx_storebell
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

hide bg
show bg city_street4_rn as bg2 behind rain
show rin negative_spaciness_close_rn
with locationskip



"角を曲がったところで琳に追いつき、傘を開いて俺たち２人の上に差す。その間もほとんど走っていないとついていけない。"




"琳は俺が走ってついてきたことにも、傘を差してやっていることにも文句を言わず、やがて足取りも遅らせたので、俺も体を酷使しすぎるという差し迫った危険なしに追いつけるようになる。"



"全力疾走から落ち着くと、状況を吟味する。"



"この前に、俺たち２人が雨に濡れないよう傘を差したときは、そのことをあまり深く考えはしなかった。"




"でも今は、その時以来のあらゆる出来事が凍るように冷たい球になって、胃の周囲に集まっている。"




"琳の近くにいるのは居心地が悪くて、自分がわずかに動揺しているのを感じる。"




"突然、ものすごくのどが渇いた感じがして、言葉を発するのもままならなくなる。"



"それでも、後に引けるものじゃない。"



hi "なんでそうやって逃げ続けるんだよ？"


show rin negative_annoyed_close_rn
with charachange


rin "君とは話したくない"


hi "俺は話したい"

show rin negative_confused_close_rn
with charachange



rin "話をするたびにつらいんだ、いつも"




hi "時には仕方ないこともあるさ"


show rin negative_sad_close_rn
with charachange



rin "つらいのはいやだよ"



hi "わかった。話すのはよそう"

show rin relaxed_doubt_close_rn
with charachange


rin "じゃあどうするの？"



hi "いいから歩こうぜ"


show rin relaxed_surprised_close_rn
with charachange


rin "歩くだけ？"


hi "歩くだけだ"

show rin basic_absent_close_rn
with charachange


rin "わかった"

label jp_R37:

play music music_dreamy fadein 2.0
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")
$ renpy.music.play(sfx_rain, fadein=2.0, if_changed=True, channel="ambient")

play sound sfx_whiteout

scene white
with Dissolve(1.0)

show rain normal behind white
with None

hide white
show ev rin_rain_away_close behind rain at Fullpan(20.0,dir="up")
with Dissolve(1.0)



"雨のなかを歩いていると、俺たちは通りにできた浅い水たまりを踏んでバシャバシャという足音を立てる。"





"琳はのんびりと、落ち着いた態度で俺の隣を歩いていて、不必要に濡れてしまっていることもまるで気にしていないみたいだ。"




"俺たち２人を覆うには十分な大きさなのに、琳は傘の下から少しはみ出している。"




"袖がびしょ濡れになっているのに気づいてさえいないかのようだ。"



"……"



"心の中では動揺しているようなときでさえ、琳の立ち振る舞いはいつも瞑想的な落ち着きのイメージを連想させる。"




"でも今のこれは瞑想ではない気がする。単に雨に濡れているだけだ。"




"俺ももっと冷静でいられたらいいのに。"




"いつもの超然とした態度を保つには、俺はもう琳と深く関わりすぎてしまった。"




"自分は客観的に物事を見ていると自分自身をごまかしておいて、結局自分が最悪の嘘つきだったと気づいてしまうようなタイプの人間になってしまった気がする。"




"俺たち自身をごまかすための妄想か。自分がいい人間だと思い込むのにこれ以上いい方法なんてあるだろうか？"




"そんな妄想はなくしたほうがいいかもな。"


show ev rin_rain_away_close at Position(yalign=0.0)
show ovl rin_rain_hisaotowards_close behind rain at Position(xalign=1.0, yalign=0.0)
with charachange



hi "しばらく実家に戻るんだけど、その前に会っておきたいと思ってさ"



"もっといい話の切り出し方もあったんだろうけど、琳がはっきりと話をするのを拒んでいるのが、それを難しくする。"




rin "よかったよ。でなきゃ君が誘拐されたと思ったかもしれないから"





hi "そうやってずっと逃げていられると思ってるのか。俺が真面目に話そうとしてるのに"




rin "私はいつも真面目だよ。それに今の私、すごくゆっくり走ってるみたい"




rin "笑美に走り方を教わったほうがいいかも"




"無意味だ。やみくもに皮肉っぽくて意味をなさない言葉を垂れ流す、レンガの壁と話しているみたいだ。"




hi "あの展覧会のオープニングのこと、考えてもみろよ。もしあのまま逃げちまってたらどうなったと思う？"



"琳はそれには答えず、ただ歩き続ける。あるいはゆっくり走っている。俺の質問から沈黙のなかへ逃げ去ってしまう。"



"以前から気づいていたけど、琳は人がそばにいても１人きりでいるこつを知っている。"


show bg city_street3_rn behind rain
hide ev
hide ovl
with locationchange


"俺たちは通りを下っていき、左に曲がる。今度は右に３回曲がって、また左に曲がる。"




"少し前の夜みたいに、俺たちは適当な方向に進んでいる。どこに向かっているかなんてどうでもよかった。"




"大事なのは歩くことと、雨粒が傘を打ちつける音だけだ。"



"雨水が建物の屋根を流れ落ちて、雨どいから広い川になって流れ出てくる。"


"それをまたごうとしても、俺の足は靴越しに濡れてしまう。"



"黙ったまま歩き続ける。この沈黙をまた破りたくなる。でも、そう感じてるのはきっと俺だけだ。"


hide bg
show ev rin_rain_away behind rain
show ovl rin_rain_hisaotowards at Position(xalign=1.0, yalign=0.0) behind rain
with locationchange


hi "どうして展覧会をやったんだ？"



"琳はただぶすっとして肩をすくめると、そっぽを向いてしまう。この時点で俺はさじを投げる。"


window hide

hide ovl
with charachange

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear
nvl show dissolve



n "\n\n\nこんなの意味がない。"




n "\n琳はなにを成し遂げたかったんだ？　オープニングの日の夜に琳の言葉を聞いたとき、琳はなにか……なにか特別なものを求めていたような気がした。"




n "琳は決して手の届かないものを望んでいたように思えた。"




n "琳はバーを高い位置に掲げて、自分の頭の中でそれを飛び越えられなかったんだ。どれだけ他人が琳の絵を気に入っていても。"




n "現実を受け入れられないというのは理解できる。ほとんどの人はそうだ。琳みたいに極端なレベルではないにしても。"



n "\nでも、それは誰にも邪魔されない個人的な世界に引きこもる理由にはならない。"

nvl clear



n "\n\n\nすべてが自分の思い通りになる、歪んだ誇大妄想めいた宇宙論にあてはまるように世界をねじ曲げることはできない。"





n "\n琳のそういうところが一番イライラする。"





n "\n琳は世界を自分のルールに従わせたいと思っている。ルールに合わないすべてのものは無意味だとか不要なものだとして無視している。"





n "仮にも山久にいる人間が、この世界は時にとても不公平になりうる、ということを理解するためのほんの最小限の認識さえ持っていないなんて信じられない。"





n "そうでないものもあってほしい、と願う人はきっと琳以外にもいるだろう。でも事実は事実として把握することはできる。"


$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

hide ev
show bg city_street4_rn behind rain
show rin negative_spaciness_close_rn at center
with locationchange

window show



"俺は横目で琳をちらりと見る。琳はドーム状の覆いを見上げている。わびしいモノクロームの、粗末なまがい物の空だ。"



"雨はただ降りつづけている。"




"まるで今日の雲みたいに、見られたいという気持ちを琳はまったく表に出さない。"




"琳は大好きな空と同じように不機嫌になる。"




"来るんじゃなかった。琳の存在は、まったく同じ理由で俺が激怒したこと、そしてその理由が変えようのないものであることを俺に思い出させるだけだ。"




"謝りたいとは思う。これで終わりにしたくないとも思う。でも、そのどちらも言葉に出すことができない。"


show bg misc_sky_rn
hide rin
with locationchange



"俺たちは雨に濡れた道路を一歩ずつ進む。"



"誰かといっしょに歩いていると、しばしば歩調が潜在意識のなかで申し合わせたかのようにシンクロしてしまうことがある。"



"俺と琳は決してそうならないことに気づいた。"


window hide

stop music fadeout 5.0
$ renpy.music.set_volume(0.3, 3.0, channel="ambient")

show bg misc_sky_rays
show rain light
with Dissolve(3.0)

window show


"時間が過ぎていき、傘の帆を打ちつける雨は、上空の雲がゆっくりと散っていってセルリアンブルーの空をのぞかせていくにつれて弱まっていく。"

show rain light:
    alpha 1.0
    linear 5.0 alpha 0.0
with None

stop ambient fadeout 9.0


"ついに雨は傘を閉じられるほどに弱まってくれた。閉じる前に余計な雨水を振り落とす。"



"傘の開閉に手こずっていると、琳は突然足を止める。俺はもう５歩進むまで琳が隣にいないことに気づかなかった。"




"いまいましい傘はひっかかってしまったみたいだ。"


play music music_innocence fadein 6.0

scene ev rin_trueend_normal:
    truecenter
    zoom 1.2 rotate -6 subpixel True
    easein 6.0 zoom 1.0 rotate 0
with locationchange


"俺が振り向くと、琳が平然とした顔で俺を見つめている。"



rin "『君の気持ちがわかる』って、誰かに言ってほしかったんだ"




rin "そしたら最高だと思わない？"




"今のは前に聞いた質問の答えなのか？　よくわからない。"




hi "ああ……でもどうしてそれがそんなに大事なんだ？"


scene ev rin_trueend_sad:
    truecenter
    zoom 1.0 rotate 0 subpixel False
with locationchange



rin "だってそうじゃなかったら……耐えられないかもしれないから"




"俺はまだ傘をたたむ途中だったので、会話を進めるだけのために適当な返事をした。でも今の琳の言葉に俺の血液は凍り付く。"


scene ev rin_trueend_closed
with locationchange




rin "誰かが冗談を言って笑ったら、自分も一緒に笑うんでしょ？　だって２倍の喜びは３倍の喜びっていうでしょ、違う？"


scene ev rin_trueend_smile
with locationchange



rin "誰かが辛くて悲しんでたら、励まして抱きしめてあげるんでしょ？　だって――"



rin "……"


"琳は固まる。口は半開きのままで、すぐに気づいて閉じる。"

scene ev rin_trueend_normal
with locationchange



"陰鬱さが琳の顔と俺の心を同時に覆う。"




rin "ぴったりの言葉っていうのが絶対出てこないのがどうしてなのか、わからない"




rin "自分で笑おうって思ったときしか笑えないのがどうしてか、わからない"




rin "自分が今にも爆発しそうなのに、どうして私の中から何も出て行かないのか、わからない"




"平然とした無表情の顔は、その言葉を口にしながら揺らぎもしない。"




"いつもの落ち着いた声が普段よりわずかに小さくなる。"




rin "でも誰が……誰がそんな気持ちになりたいなんて思うの？"




"琳が俺を見ると、本当にそれがあろうとなかろうと、俺はその目に映る悲しさを想像する。"



rin "私はいやだ"



rin "そんな気持ちになんてなりたくない"



"それから俺たちはしばらくのあいだ黙り込む。"



"琳はもう言うべき事を一息に言い切ってしまったから。俺は琳の言葉をどう解釈すればいいのか見当もつかないから。"




"琳の言っていることがわからない。さもなければわかっていても、わかりたくないんだ。"




"この二つのことが初めて同時に起こっている。しかも同時に違いない。"





"その皮肉は俺にもわかる。"




hi "俺……誰だって理解されたいんだと思うぞ。みんなそうだ"


hi "でも……それは無理だ。俺だけじゃなくて、誰にとってもだ"



hi "さえさんもそう言ってた"




hi "誰でも他の人に影響を与えるし、逆に影響を受けもする。でも結局、人は自分だけの見方でものを見てるんだ"



hi "誰もみんな……独りぼっちだ。寂しさを和らげるためにお互いを利用しあってるんだ"



"どうしてこんな言い方をしてるんだろう。さえさんの話が真実のように思えた。知らず知らずの間にいつもそう考えていたかのように。"





"さえさんは俺の考えを明確でシンプルな言葉と、あのしょうもないピカソの話で説明してくれたように思えた。"



scene ev rin_trueend_closed
with locationchange


"琳はしおれた花のように頭をうなだれて、前髪を目の前に垂れ下げている。俺にはその目は見えない。"



rin "私をそうじゃない気持ちにさせてくれたのに、どうしてそんなこというの？"



rin "ずるいよ"



"その言葉を乗せた震える声は琳のものとは思えない。"


scene ev rin_trueend_sad
with locationchange



rin "君は違うかもしれないって本当に思ってたんだ。独りぼっちにならなくて済むかもって"




"噛みしめた歯と震える胸を通して伝わる、苦い失望の声。"



hi "ごめんな……"



rin "そう思ってるなら、どうしてそんなずるいこというの？"






"その厳しい声色は、昨日の夜からあり続ける悲しさを除けば、なんの感情も呼び起こさない。"






"もう琳のことは全然怖くない。"





"琳は奔放な絵の天才でもないし、口を開くたびに俺の左脳をずたずたにするような、予測のつかない『愚かな天才』でもない。"







"琳は俺が好きだと思っていた女の子だ。俺の友達になろうとした愛すべき人、期待を裏切ってしまった友達だ。"




hi "違うことを言ったら、うそをついている気がするからだよ"


scene ev rin_trueend_normal
with locationchange


rin "どうして？"



"シンプルな疑問は一番答えづらい。俺は目を閉じて答えを探すのに集中しないといけない。"




hi "俺は芸術家じゃない。お前と同じレベルには絶対なれない"




hi "お前だけに見える世界があって、俺がそこに入り込むには、お前にならなきゃいけないんだ"




hi "それは俺にはできない。お前がどんなに望んでも"



"琳は俺の説明をまつげひとつ動かさずに聞く。"



rin "私だってほんとの芸術家なんかじゃないよ"




rin "私はただ、何かを感じられるような気分になれるから絵を描いてるだけなんだ"


scene ev rin_trueend_weaksmile
with locationchange


"琳はしばらく息を止めて、ため息のように深く吐き出す。"

scene ev rin_trueend_closed
with locationchange



rin "それが、やることにした理由"





rin "私、決めた。やるよ。久夫までそんなこと言うなら、私はそうする"



hi "なにをするんだよ？"



"琳はまた自分自身と会話するという小芝居を始めている。でも俺は今でも琳に言い返せていることがうれしい。"


scene ev rin_trueend_normal
with locationchange



rin "先生とさえさんが、大事なお客さんとしゃべってた。私、東京の大きな美術学校の特待生になったんだってさ"




rin "私がそうしたければ、夏が終わったらそこに転校できるってその人が言ってた"



rin "どうしてかはわかんないけど――"

stop music fadeout 10.0



hi "待て、なんだって？　なんで言わなかったんだよ？"


scene ev rin_trueend_smile
with locationchange



rin "今言ったよ。君が最初に言った相手なんだ、たった今決めたから"




"動揺した俺の横槍に軽い驚きの表情を見せるだけで、琳は平静を保つ。"




"そんな人生が変わるようなことをあっさり口にするなんて、どうかしてる。"





"信じられない。２月の出来事以来、今年はありすぎるくらい変化があったというのに。"



"たとえ悪い方向に進んでいても、なにもかもが変わってしまうのはごめんだ。"


hi "でも、山久はどうするんだよ？　みんなと卒業したくないのか？"


"俺の懇願はなんの感情も引き起こさない。"


rin "みんな？　誰のこと？"


hi "笑美とか、俺とか、とにかくみんなだよ！"



"心臓が怖いほど鼓動して、息が浅く、速くなる。"




"こんなのは嫌だ。"




rin "みんなの人生は私の人生じゃないよ"




rin "みんな独りぼっちだって、君が今言ったよね"




hi "そんな意味で言ったんじゃ――"




rin "君っていつも、今を楽しまなきゃとか、自分の人生を生きなきゃとか言ってたよね"



rin "私も自分の人生を生きないと"



"琳は俺の言葉をもっともらしく捻じ曲げて、また逃げようとしている。腹が立ってくる。"




"この話をする琳の気楽さ、確固とした態度、真剣さを俺は許せない。"



"人生を変えることが、一瞬の思いつきでできるとでもいうのか！　冗談じゃない！"



hi "なんでそんなことが言えるんだよ？　どうしてどこかに属そうと努力もしないんだ？"




"必死の非難も効果はない。また打つ手無しになった気分だ。俺がどう出ようと、琳には届かない。"




"琳は腹が立つほど自分の決めたことを絶対視する。琳のことが好きでなければ憎んでいたかもしれない。でもどっちが俺の気持ちなのか、もうわからなくなってしまった。"


scene ev rin_trueend_normal
with locationchange



rin "私ってそういう人間なのかもね。自分自身にしか属さない種類の人間"




hi "そんなの認めないぞ"



"その無関心な目は、俺が琳の決意を受け入れたかどうかなんて気にも留めないようだ。"


"……"



"その沈黙に俺は冷静になり、理性を取り戻す。"




"その間に雨雲が割れて、隠れていた太陽がのぞく。一日が終わる前に最後の暖かな光を照らす時間が残っていた。"



"光と影がモザイク模様になって建物の壁や道路、通りの向こうの公園を囲うフェンスに広がる。"


"琳の影が俺の足まで届くほど伸びる。"



"カウボーイがお互いを睨み合って、今にも銃を抜こうとしている西部劇みたいだ。"



"怖気づいたほうが負けを喫する。"


"琳が背にしている太陽が目に染みて、不利な立場にあることに気づく。"

scene ev rin_trueend_sad
with locationchange


rin "私のこと、嫌い？"


"琳が最初に切り出す。そして俺に反論はない。"


hi "さあな"


"俺の負けか？"


hi "もしそうだとしても、それがどうしたっていうんだ？"



"俺は言葉を、この事態を救いうる言葉を必死に探す。なにも見つからない。"




hi "お前は友達だ、そう約束した。俺は約束を反故にするような男じゃない"



hi "それがいちばん大事なことだと思う。俺たちはもっと――"

scene ev rin_trueend_normal
with locationchange



rin "言わないで"


scene ev rin_trueend_hug
with locationchange

play music music_friendship fadein 4.0



"俺が言おうとしたことを予測すると、琳は俺の胸に飛び込んで、体を俺に押しつける。"



"琳が俺にすり寄るためにつま先立ちをするのがわかる。"



"髪から雨と絵の具用のシンナーの匂いがする。体はいつものように冷たい。そして首筋にあたる息はいつものように熱い。"




"その一つ一つにはとても親しみがあるのに、琳自身に対してはそんな気がしないのがおかしい。"


scene ev rin_trueend_hugclosed
with locationchange



rin "本当に私のことを嫌いになれない自信がある？"





"琳が俺の耳元で囁く。唇の動きが耳たぶに伝わってくるくらい近い。"





"からかっている。馬鹿にしている。これがまた別の状況だったら、欲情してしまうほどくすぐったく思うだろう。男の俺でもクスクス笑ってしまうだろう。"





rin "その方が楽になれるよ"




hi "知るかよ。そうやって抱きつかれてたら難しいんだけど"


scene ev rin_trueend_sad
with locationchange


"俺の不機嫌な声のせいなのかはわからないけど、琳は短い腕を物憂げに見ながら引き下がる。"



"こんなことはして欲しくなかった。"




rin "私、誰ともハグできないんだよ、久夫"




rin "そういう悪い子なんだよ、私"


scene ev rin_trueend_normal
with locationchange



rin "だから行かないといけないんだ"



"３つの短い言葉で、琳は完全に俺の戦意を喪失させる。もう異議を唱えることはできない。"



"反論できないおかげで琳は自由に話を続けられる。その前に重心をもう片方の足に移す。"


scene ev rin_trueend_smile
with locationchange



rin "私なりのやり方で人をハグできるよう勉強するよ"




rin "きっと本当の芸術家になれると思う"




rin "でもそうしたら……もう私ではいられなくなっちゃうかもしれない"




"くちびるに浮かんだかすかな笑みは欺瞞だ。琳ですら予想のつかない未来に対する自信を示す偽りの兆し。"




"希望の兆しと思いたいところだけど、俺にはお見通しだ。"




"琳はただ、あのぎこちない無理やりな笑顔を続けている。"



rin "だから……私のことは忘れて。私も君のこと、忘れるから"


rin "そうすれば――"

scene ev rin_trueend_sad
with locationchange



"何か言おうとする途中で息を詰まらせ、俺は聞きそびれる。"



"聞きたいような言葉じゃないんだろうけど。"



"こんなのは卑怯だ。"




"本気なんだ。琳はいつだって真剣だ。でもこんなの受け入れられない。受け入れられるか。"



"忘れろだって？　そんなことできるわけ……？"



"そう言ってやりたい。でもどう続ければいい？　何もいい言葉が思いつけない。だから反論しないといけない。"




hi "どうしてそんなことが言えるんだ？"


scene ev rin_trueend_normal
with locationchange



"琳は目を上げて俺と視線を合わせる。深くて真剣な目だ。いつもそこにあると思っていた未知の領域の、完璧なイメージだ。"




"この期に及んでさえ、そのまばたきをしない、そこに映るものを決して反射しないひすい色の虹彩から、俺は感情を読み取ることができない。"



rin "簡単だよ。なんだかんだで私、忘れるのは得意だから"


"……"



"琳のずるさに息が詰まりかけるけど、俺は自分の心を焼き続けている質問をどうにか声に出す。"




hi "じゃあ、これで終わりなのか？　これでサヨナラかよ？"



"……"



"琳は俺の質問には答えず、穏やかに俺を見続けていた。"




"その目を見て、もう言葉を発する必要さえなかったんだとわかった。"




"もはや俺たちの間に言葉は存在しなかった。"


stop music fadeout 12.0

scene ev rin_trueend_gone
with locationchange




"琳はきびすを返すと、振り向くこともなく立ち去った。"





"俺の周囲では、世界は変わり続けていた。少しずつ。でも、俺はこの場に立ち尽くしていた。"


scene ev rin_trueend_gone:
    "ev rin_trueend_gone_ni" with Dissolve(10.0)
with None



"夕日が長く細い影を通りに落としながら、水平線に沈んでいた。"




"薄れゆく光の中で、遠ざかる琳の背中は夢の彼方から来ているように見えた。"




"俺たちの距離が少しずつ開いていった。"




"琳が踏みつける水たまりのさざなみは、その小さな存在の限界を迎えるまで広がっていき、跡形もなく消えていった。"




"琳の言葉は俺の心の奥深くで凍り付いたままだった。"


window hide

label jp_R38:


scene bg school_room34
with None

show rin negative_spaciness
with charaenter

play music music_drama fadein 6.0



"陽の差し込む教室の真ん中に琳は立っていて、はためくカーテンの切れ目を通して庭の方をじっと見ている。"




"今までと同じように、琳は驚きも飛び上がりもせず、ただ静かに俺が先に動くのを待っている。"




"まるで教室の常備品の一部にでもなろうとしているかのようだ。"



hi "先生が探してるぞ"



"肩越しにうつろな視線が返ってくるだけだ。その表情は不可解な無感情さをともなっている。"




rin "君も私を探してるの？"




hi "いや、もう見つけた。違うか？"



rin "そうなの？"

show rin negative_annoyed
with charachange



"琳は困惑したように眉根を寄せる。あまりに怪訝そうな表情で、今の質問が本気だったのかどうか疑いたくなる。"




"本気なのかもしれない。"




hi "今のはたとえ話か？"


show rin negative_spaciness
with charachange



rin "ウナギとか洞窟とか、真っ暗な嵐の夜みたいにってこと？"



show rin negative_sad
with charachange



rin "そういう話し方は苦手なんだけどな"



"……"

play sound sfx_doorclose



"唐突に挨拶が終わったので、俺は後ろのドアを閉めて、ほこりの積もった机の上に腰掛ける。"


show rin basic_absent
with charachange


"琳は立ち続けているけど、ようやくこちらを向く。"



"すぐにそうしないで欲しかったと思い直す。琳の期待に満ちた視線があまりに耐え難い。"




"ここは琳の領域で、俺は大目に見られているとはいえ侵入者だ。それでも、琳は俺が何か言うのを待っている。"




"何を言えばいいのかわかっていれば、だけど。"



"……"



"太陽に照らされた沈黙が俺に決断を促す。"




"琳がここにいた場合に野宮先生の短い伝言を伝える以外は、何をするかまったく考えずにここに来た。"




"そしたら琳はいて、俺は他になんて言いたいのかわからない……なんて言えばいい？"




"俺は２つの選択肢の間を行き来する。"




"琳が苦しんでいると、俺も苦しい。これは驚くべき発見だ。そもそも琳が苦しんでいる、という発見と同じくらい大きい。"





"俺に手助けできることはおそらくない。そしてある程度は俺のせいなんだろう。"





"それは、もう琳と関わるのをやめた方がいいってことか？"



"そんなはずはないな。"


hi "それで……どうしたんだよ？"


"……"

show rin relaxed_nonchalant
with charachange


rin "別に"



"琳はしたくもない会話から物理的に抜け出そうとするかのように、またそっぽを向いてしまう。"




hi "なあ琳、俺を避けるのはやめろよ。でないと俺帰るぞ"


show rin relaxed_boredom
with charachange


rin "わかったよ"



hi "帰ってほしいのか？"



show rin relaxed_doubt
with charachange


rin "まだ怒ってるの？"



"たった１０秒で、俺たちは――いや、俺だけか？――会話をこのどん底に沈めてしまう。"



"今までのことを消し去ってしまいたい。それがだめなら、せめてなにもかも忘れてしまいたい。"




"この数ヶ月、そう願ったのは一度だけじゃない。"




hi "とりあえずその話は置いとこうぜ、な？"


show rin basic_absent
with charachange


rin "君がそう言うなら"





hi "そう言ってるだろ。それで……どうしたんだ？"




hi "昨日お前が逃げちまったもんだから、さえさんと野宮先生はあまりいい顔してなかったぞ"




hi "相当なピンチのままでほったらかしにしたからな。先生も何かしら説明を聞きたがってると思うぞ"




hi "お前が今までがんばってきたことを全部放り出したみたいに見えたけど。理由がわからないんだ"


show rin basic_deadpanupset
with charachange



rin "私、間違ったことをしたの？"




"俺の叱責と琳の平坦な答えは、普通の期待や予想される対話とあまりに逆行していて、まるで別人が会話をしているのも同然だ。"





"俺たちのどちらも、今までの俺たちらしくない。琳を見るたびに感じる、このこわばった、束縛されるような感覚が、近ごろは琳自身の立ち居振る舞いにも移っている気がする。"





"取り返しのつかないほど悪い方向に進むのは嫌だ。２月からずっとそう思ってきた。"





"俺はなんて言えばいいんだ？"






"琳はその質問の後、切実でいぶかしげなまなざしを向ける。俺はため息をつき、顔をしかめる。"





"誰も望まない会話というのは最悪だ。"




hi "さあな。というか、この世の終わりってほどじゃないけど、かなりバカなまねだったと思うぞ"


show rin relaxed_nonchalant
with charachange



"琳はため息で答える。でも俺のほど重々しくはない。"


show rin relaxed_sleepy
with charachange



rin "どうしてもできなかったんだ"



hi "でも……なんでだよ？　なにがまずかったんだ？"

show rin negative_annoyed
with charachange



"沈黙、寄る眉根、そして静かな声。"




rin "もういいでしょ、久夫"



rin "納得してもらえるような説明なんてできないよ"



"ああ、琳もこんな話はしたくないんだな。そのほうが良さそうだ。"




"でも琳にしては珍しいな。自分にも限界というものがあると認めるなんて。"





"俺はずっと、琳は自分の注意散漫なところを全く自覚していないと思っていた。だから無意識に自分の言ったことを何もかもぼやかしてしまうんだ、と。"




"……"



hi "お前って、本当に{b}どんなことでも{/b}他人にわかるように説明しないよな"


show rin basic_absent
with charachange



rin "だって他に誰も聞いてこなかったし"


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\n\nそんなことだろうと思った。"




n "でも、俺はずっとお前を理解したいと思ってた。お前がどういう奴なのか知りたかったんだ。"




n "今もそう思ってるんだ、わからないのか？"



n "\n……"



n "\nわからないだろうな。"




n "でもそう思ってるんだ。"


nvl clear




n "\n\n\nだから俺たちはこんなことを続けるのか？　俺もつらいけど、同じくらいお前もつらいんだ。俺たちのどちらにも役には立ちそうにない。"





n "俺たちは取り返しのつかないことを言ったり、やったりした。"





n "まるで……俺とお前が近くにいるだけでお互いに傷ついてしまうのに、わざとそうし続けているかのようだ。"





n "バカみたいだよな？"




n "今でさえ、俺に義理立てることなんかなにもないのに、お前が無理に返事をしているのがわかる。"




n "こういうことを話すのは大変なのに、それでもだ。"




n "\nどうして？"



$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show



hi "お前が絵を描く理由はなんだ？"


show rin basic_awayabsent
with charachange



rin "私……だって、他に何ができるかなんてわからなかったから"




rin "選びようがない、これしかないんだっていう感じだよ"


show rin basic_sad
with charachange



rin "どうしてもアイスキャンディが食べたいのに、お店にスイカ味のしか残ってなかったときみたいな感じ"




"その出来の悪い例えは置いておくとして、琳の返事は何の答えにもなっていない。下手をすると、何も知らない状態よりもさらにわけがわからなくなる。"




hi "でも……絵が描きたくないんだったら……"


show rin negative_spaciness
with charachange



rin "そういうことじゃないよ。君だって心臓発作なんて起こしたくなかっただろうけど、この学校に来なきゃいけなかったんでしょ"


show rin negative_annoyed
with charachange



"琳は言葉を切ると、自分が言ったことが気に入らないかのように顔をしかめる。"


show rin basic_lucid
with charachange



rin "少なくとも私はそう思うけど"




"用心深い補足のあとに続けて、もう一度短く言葉を切り、もう一度わずかに顔をしかめる。"


show rin basic_deadpanupset
with charachange


rin "心臓発作、起こしたいの？"



hi "まさか。起こるのはいやだし、起きて欲しくもなかったよ"


show rin basic_deadpansurprised
with charachange



rin "でも今は調子いいんでしょ、違うの？　それとも、まだそのことが悲しいと思ってる？"




"琳の問いかけで、俺は自分がもう何週間もの間、病気のことをまったく考えていなかったことに気づく。"




"毎日薬を一気飲みしていることをのぞけば、このぶっ壊れた心臓を心配したことはない。それだけは本当に感謝している。"




"新しい人たちと知りあって、新しい学校を知って、新しい町を知って……新しい人生を知った。これらすべてが俺を捕らえ、過去をだんだんと消し去った。"




hi "いや……へえ、俺だって過ぎたことをいつまでも嘆いてはいられないみたいだな"


show rin basic_awayabsent
with charachange




rin "ほらね？　食べなきゃいけないってことになれば、スイカ味だってそんなにまずくはないんだよ"





"その半ばナンセンスな結論付けで、琳は頭の中でこの話題にけりをつけたみたいで、俺はよくわからないけど確認のためにただうなずく。"



"……"


"……"



"沈黙には２つのタイプがある。破りたくなるような気まずいものと、気にならない快適なものだ。"




"前者はまずい。思考が間違った方向に行ってしまう。今の俺みたいに。"




"琳を見ているとひどい気分になる。"


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "こんな気分にはなりたくない。"




n "琳を見ていると……疲れてしまう。俺は本当に頑張った。そして琳は……どうだったのか、見当もつかない。"




n "でも俺たちは結局このざまだし、琳は自分の展覧会のオープニングをめちゃくちゃにしてしまった。"




n "これじゃ行き詰まりだ。"




n "もうこれ以上進む先がない。"




n "昨日、琳に手を差し伸べた。それでもう最後だと思っていた。"




n "琳は背を向けた。"



n "『私でいたいから』。"




n "訳が分からないぞ？　琳は、他の誰と比べても、間違いなく琳だ。"






n "俺の落ち度じゃないのはよかったけど、このことは今でも心に引っかかっている。"





n "どうして琳は逃げた？　昨日はわからなかった。今日もわからない。"





n "琳の言ったことは誰にでも理解できることのような気がするけど、俺にはどうしても理解できない。"


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear
window show



hi "なあ、お前が今言ったことだけど……"

show rin basic_absent
with charachange


rin "どれのこと？"



hi "うーん……絵を描くこと……さえさんが前にそれに近いことを言ってたんだ……本当の芸術家は描きたいから描くんじゃなくて、{b}描かずにいられない{/b}んだって"




hi "そのことがずっと不思議だったんだ。どうして芸術家は絵を{b}描かないといけない{/b}んだ？"




"俺の質問はきっとすごく馬鹿げてる。少なくとも琳は、そう言いたげな目で俺をぼんやりと見ている。"


show rin basic_deadpannormal
with charachange


rin "わかんない。私って芸術家なの？"



hi "まあ、絵は描くし、展覧会もする。十分芸術家じゃないか"


show rin basic_deadpancontemplation
with charachange



rin "やっぱりわかんないけど、でもわかった"




"その直後の考え込むような沈黙が、半永久的に続くかのように思えてしまう。"





"ほとんどの人と違って、琳は物思いをするときの間にボディランゲージや『そうだね』とか『うーん』といった言葉を何も付け足さない。"





"俺はそのほうが良いのかもと思い始めている。普通のやりかたはむしろイライラする。ただ次に言うことを考えているだけなのに、自分自身の声に夢中になってしまってとにかく雑音を出し続けているようなものだ。"





"琳はただ……考えているときは完全に停止してしまう。ぼうっとした人間に反応を返すのは難しいから、これには困惑する。でも感じの悪い雰囲気は薄れている。"


show rin basic_lucid
with charachange



rin "誰かに私の内側にあるものを見てほしいんだと思う。医者とか殺人鬼とは違うやり方でね"


show rin basic_absent
with charachange


rin "私が寂しくならないやり方で"

show rin relaxed_boredom
with charachange



rin "これがいわゆる例え話、なんだよ"




hi "そんな分かりきったことを説明しなくていいから"


show rin basic_deadpansurprised
with charachange


rin "分かりきったことだとは分かりきってないんだけどな"



hi "じゃあお前、自分が描いた絵を誰かに見せたら、魔法みたいにお前の本質が伝わると思ってるのか？"


show rin negative_angry
with charachange



rin "そういうのじゃないよ。それにちょっとだけ近いけど違うんだ。わからない？"




hi "わかるけど……でもわからない"





hi "なあ、お前がそんなことを聞いてくるたびに、俺は軽く絶望してるんだぞ"



show rin basic_absent
with charachange



rin "どんなこと？"




hi "俺がお前をわかってるかどうかってことだよ"





"琳は俺の説明にまるで驚いているみたいだ。"


show rin basic_lucid
with charachange



rin "ああ、今のは別に聞いたわけじゃないよ。答えなくてもいい質問だから"




hi "修辞的ってやつか"




show rin basic_absent
with charachange



rin "そう、それ。質問じゃない質問は修辞的な質問ってこと。すごいね"




rin "そういえば、それってなんか意味が通らないよね。質問じゃない質問ってなんなんだろう？"




hi "修辞的な質問だろ"




rin "何の答えにもなってない答えってなんなんだろう？"




hi "それは修辞的質問なのか？"


show rin basic_deadpanupset
with charachange


rin "君って面白くないね"

show rin basic_awayabsent
with charachange


rin "でも、つまんないなら他の話にするよ？"

show rin basic_lucid
with charachange



rin "といっても他にいいネタはないけど……『お尻に火がついてる君』なんてどう？"


show rin basic_absent
with charachange



rin "これ、私たちの秘密の合い言葉にしようか"




"琳の正真正銘のばかばかしさが、本人が大真面目だってことが分かっているおかげでその倍も滑稽になって、いつもみたいに俺を脱線させる。"




"まるで俺が心配性になるのを防止する安全装置みたいで、俺自身の考えまで、本来あるべきところから引き離してしまう。"




"俺は困惑した笑みを浮かべる。心の中で、だけど。"




"口元が緩んで笑顔になったりはしないけど、俺は今でも琳が真面目になりすぎることをあっけなく回避するのには感心する。"




"琳は自分をいらだたせるものや、悩ますものを（その気になれば）無視して、忘れることができるんだろうか？"




"琳は自分らしくあるがゆえのあれやこれやの苦しみから（その気になれば）自由でいられるんだろうか？"




"それとも、自分らしくあることに辛さを覚えているのは俺だけなのか？"




hi "やめとくよ"




hi "でもまあ、お前と同じ事考えてるって思えることはかなり珍しいけどな"




hi "なんだか……俺とお前の間に深い溝があって、お前はすっと向こう側に行っちまって、俺は……俺のいるところからは絶対に手が届かない、って感じがするんだ"




hi "時々、お前が全然違うところにいるみたいなんだ"




hi "確かにここにいるっていうのに"


"その通りだ。"




"絶対に乗り越えられない断絶がある。理解することを妨げる、想像上のガラスの壁だ。"





"どんな人同士の間にもそういった溝はありそうなものだけど、でも琳が相手だと、それはもっと明瞭だ。"



"琳は俺の考えには反応を見せない。俺が声に出していったことにもそうでないことにも。"



hi "芸術だったらもっとひどいぜ"




hi "俺は芸術には疎いよ、それは認める"



hi "俺が美術部に入ったのは面白そうだと思ったからなんだ"



hi "確かに面白いと思う。俺は芸術が好きだし、お前の絵も好きだけど、お前のことと同じで、芸術は理解できない"




hi "たぶん誰にも本当の意味では理解できないんだと思う"


show rin relaxed_doubt
with charachange



"今のは琳をわずかに不安がらせたみたいだ。"




rin "ほんとにそう思う？"




hi "ああ。芸術ってのは読み取るものであって、理解するものじゃないんだと思う。俺に言わせれば"


show rin relaxed_sleepy
with charachange



rin "そんな考え方、悲しいよ"




hi "そうかもしれないな"





hi "それでお前自身は悲しくなるのか？"


show rin basic_lucid
with charachange


"琳はしばらく考え込むと、驚くほど熱烈に頭を振る。"

show rin basic_deadpannormal
with charachange


"そのあと、琳が初めて俺に目の焦点を合わせる。"



"俺はその両方が嬉しくて、そして安心する。"




hi "それっていいことだろ？　とにかく、ちゃんと先生のところに行って謝ってこいよ"




hi "先生、心配してると思うぞ"




hi "できるか？"


show rin basic_absent
with charachange



"今度は琳はうなずく。"


stop music fadeout 4.0



"ただ、さっきのような勢いはない。"

label jp_R39:

scene bg school_hallway3
with locationchange



"廊下には誰もいない。恐ろしくなるくらいに。"



"野宮先生の『事務所』は３階の廊下の突き当たりにある美術室だ。"

show rin basic_absent at center
with charaenter



"俺たちの足音が不穏に響き渡る。空気がいつもの午後のそれと違う。学校も向こう１ヶ月、誰も戻ってこないのを知っているかのようだ。"




"ドアは開いているけど、あまり歓迎するような気配じゃない。"




hi "俺は……ええと、外で待ってるよ"

show rin relaxed_nonchalant
with charachange

with Pause(0.2)

show rin invis at tworight
with dissolvecharamove

hide rin
with None



"かろうじて分かるくらいかすかにうなずくと、琳は立ち止まらずに、そして当然だけどノックもせず、大股で中に入っていく。"





"中から先生の声が聞こえるまで数秒かかったのは、多分そのせいだろう。"




no "やっと来たか！"


rin "どうも"


"衝突が始まった。ここにいるべきか、別の場所へ行くべきか？"



"盗み聞きしたいのかどうかさえ、自分でもわからない。"



"……"

show bg school_hallway3 at right
with charamove



"好奇心に礼儀が負け、俺は近寄って聞き耳を立てる。"




"２人の声は廊下まで響いてくるけど、それはともかく。"




"俺を除けば、周りには誰もいない。"


play music music_tragic fadein 8.0



no "手塚よ、いったい何を考えていたんだ、大事な夜に姿をくらますような真似をして？"




rin "何も言えなかったんです"




"野宮先生のきつい口調に比べると、琳の声はひどく小さく、弱々しい。"




"その言葉は先生の声に埋もれてしまいそうだ。"




no "言わせてもらうが、お前には非常に失望したぞ、手塚"




rin "全然よくなかったです"





no "今まで私がしてやったことはいい。だがさえはどうなる？　お前に会いたがっていた客はどうなる？"




rin "誰もいませんでした。久夫だって……"




no "お前は我々にひどい恥をかかせたんだぞ、手塚"




no "評判こそが一番大事なんだ、そのくらいは分かっているんじゃないか？"



rin "大丈夫です。私には必要ないです"



no "『必要ない』だと！　知った風な口をききおって！"




"琳の返事は先生をいら立たせるばかりで、その声も一言ごとに大きくなっていく。"




no "芸術家への道は茨の道だ、私が請け合ってやる！　茨の道だぞ！"




no "全体像を見るんだ！　うまくいく時もあればそうでない時もある！"




rin "なんだってそうです。それでもいいんです――"




no "絶好調で楽ちんだったと思っているのかもしれないが、私がいなかったらどれほどのことができたというんだ？"




no "私とていつまでもお前のそばにいてやれるわけじゃないぞ！"




no "狭苦しい部屋に横になって、家賃を３週間も滞納して、４週目もずっと呆然としている時、お前はこの私の言ったことをもう少し聞いておけばよかったと後悔するぞ"




no "春を過ぎて、あまりの無気力に椅子の影がどこまで伸びるか計り続けることしかできない、その時になって初めてお前は自分の生業というものを考えるのかもしれんな！"




rin "そんなの関係ないです"




no "その程度の覚悟で足りるものか"




rin "私は覚悟のある人間じゃないから"






no "覚悟のある人間じゃない、と……"


play sound sfx_impact2
with vpunch



no "なら教えてくれ。なぜ……なぜ……蚊のクソほどの価値しかないなら、なぜわざわざあれだけの苦労をしたというんだ！？"




"やばい、先生がとうとう切れた。"




"先生が琳に怒鳴る声を聞いていると、傍観していることへの罪悪感がつのる。もし琳と一緒に行っていたら、先生もあそこまで怒らなかったかもしれない。"





"もしあのとき琳を引き止めていたら、そもそも先生が怒ることはなかっただろう。"




"今ならまだ教室に入って琳に助太刀してやれるけど……できる気がしない。"




"俺も同じだった。俺も琳を怒鳴りつけた。今はそれが恥ずかしくて仕方がない。"




"琳に怒りをぶつけるのが当然だと思ったのは、ただ……ただ俺があんなにいらだっていたのは琳のせいだと思ったからだ。"




"先生にも俺にも、そんな資格なんてなかった。"



"……"


"ひどい沈黙が廊下を襲う。"



"琳は野宮先生に何も言えないでいる。"




"答えが尽きてしまったのか、それとも反論しても先生を怒らせるだけだと分かっているのか、どちらなのかはわかりようもない。"





"先生も言うべきことはもうないみたいだ。息が切れただけかもしれないけど。"





"一瞬、２人がお互いをただ見つめ合っている様子を想像する。片や猛烈な怒りで、片や……そういえば、なんだろう？"




"俺には琳の気持ちはわからない。昔も、今も。"




"先生も琳が何か言うのを期待してるんだろうけど、琳は黙ったままなので、最後には少し静かな、しかし怒りの収まらない声で続ける。"




no "あれだけの労を費やした結果がゼロなら……いったい何の意味があると言うんだ？"




"それでも、琳は何も言わない。"


no "すまない。つい興奮してしまった"



"ぜんぜん悪いと思ってるように聞こえない。むしろ口から言葉を吐き出すかのような、冷たく鋭い響きだ。"




no "期待をしすぎていたようだな。結局、お前は芸術家ではなかったということだ"




"本当に、ぜんぜん悪いと思ってないな。"


show nomiya serious:
    tworight
    alpha 0.0
    parallel:
        linear 1.0 center
    parallel:
        linear 0.4 alpha 1.0
        0.2
        linear 0.4 alpha 0.0
with Pause(1.0)

stop music fadeout 4.0



"先生は部室を飛び出すと、俺に気づくことなく階段を下っていく。"




"先生がいなくなった後、俺は慎重に中を覗き込む。"


scene bg school_nomiya at right
show rin basic_awayabsent at center
with locationchange


"取り残された琳は先生の机の前で突っ立っている。"

show rin negative_spaciness
with charachange



rin "ごめんなさいって言えなかった"




"俺ではなく、教室の湿った空気に向かって言う。"




"でも部屋は琳に答えたりしない。俺が答えないと。"




hi "あれはフェアじゃないよな……先生怒ってたけど、それでも……"



"どう言葉を締めようか決められない。先生を見下すのは、２日前の俺の振る舞いを見下しているみたいだ。"



"バカだけど、今にしてみればその通りだ。"


show rin negative_spaciness_close
with characlose



"琳は答えず、その場に棒立ちになっているので、俺は琳に歩み寄る。"




"琳は立ち向かって自分の意見を貫いた。ある意味、それは予想外だった。"




"琳らしいのからしくないのか、俺には何とも言えないけど、いずれにせよ、琳はやった。"




"俺に対しては一度もそんなことはしなかった。"




"してくれたならとも思う。そうすればこんなひどい気持ちにはならなかったかもしれない。"




"最近の俺は本当に何でもかんでも願ってるな。"



hi "琳？"

show rin negative_annoyed_close
with charachange


rin "あっち行って"

label jp_R40:

scene bg school_nomiya at right
show rin negative_annoyed_close at center
with None

play music music_sadness fadein 6.0



hi "なんで……何言ってるんだよ？"


show rin negative_angry_close
with charachange



rin "君も私に怒ってるんだ、そうでしょ？"




rin "君は友達だと思ってた。先生のことも"



"琳の声はこれまで聞いたことのないようなもので、苦々しく、針のように鋭い。琳はじっとつま先を見下ろしている。"



hi "そういうことじゃないと思うぞ"




hi "先生はお前に、お前じゃない別の何かになってほしいと思ってたんだ。それで……"


show rin basic_surprised_close
with charachange



"俺は深く息をつくと、ようやく琳の目をとらえて、お互いに見つめ合う。"




hi "……ごめん。俺も、俺たち二人が別の何かになれたらと思ってた……もっと、友達以上の何かに"





hi "だから俺は自分を抑えられなくてあんなにイライラしてたのかもな、先生と同じように"


show rin relaxed_doubt_close
with charachange



rin "何がもっとなの？　私にはこれ以上の私はないよ、私はこれで全部。わけわかんないよ"



"ああ……答えはわかりきってる、そうだろ？"



"友情の意義を考えていたときのことを思い出す。友達を支えてやるために、どんなことでも全て我慢する、ということを。"




"友情が別のものへの足がかりになりうると考えていた俺は、友達として失格だったんだろうか？"





"そんな考えがあったから、俺は我慢を続けることが、友情をつなぎ止めることができなかったのかもしれない。"




"今も昔もこんなに琳は常識外れだけど、俺自身がそれに腹を立ててはいけなかった。琳相手にあんな感情を抱き始めていたならなおさらだ。"




"で、俺は失格なのか？"




"琳の目はそう問いかけているように見える。"



"……"


hi "ごめんな、琳"



hi "俺はお前の友達にはなれないかもしれない"



hi "俺は絶対に、お前の親友ではいられないと思う"




"こんなことを口にするのは、それを俺たちのどちらかが聞きたいからじゃなくて、それが本当のことだからだ。"



"でも、これは伝えなければいけないことだ。"



"俺の決定的な言葉は、身震いするような沈黙を生む。なぜって、それ以上何を付け加えることがあるだろう？"



"……"

show rin negative_confused_close
with charachange


rin "どうして？　どうしてこうなっちゃうの？"

show rin negative_sad_close
with charachange




rin "みんな頼んでもないのに、して欲しくもないことして、みんな私に怒ってて、もう何がどうなってるのか全然わからなくて、何もかもから逃げ出したい気持ちになるのを抑えられなくて……"



show rin basic_lucid_close
with charachange


"琳は目をぎゅっと閉じると、深く、静かに息をつく。"

show rin basic_upset_close
with charachange



"まぶたが開くと、そこに見えるのは深緑色の絶望だけだ。"




rin "{b}私の何がおかしいのかわかんないよ！{/b}"




"琳の狂乱した叫びは俺を一瞬ぼうぜんとさせる。そして一瞬の間、俺たちはお互いの顔を見つめ合う。"




"琳の困惑した目は、その答えを必死に俺の目に求めているけど、それを見て俺は悲しくなるだけだ。俺に答えられないことはわかっているから。"




hi "俺にもわからないよ"



hi "でもな、どんなことだって正しくも間違ってもないって言ったのはお前だぞ"




hi "そういうものなんだよ"





hi "それを受け入れるか、頑張って変えていくか、諦めるしかないんだ"





hi "お前のことが嫌いなわけじゃないぞ。先生だってそうだ"




hi "俺はただ……もうだめだと思ったらそこで諦めちまうような人間なんだろうな"




hi "もしそういうのが嫌だとしても、これが……つまり……現実なんだよ"




"俺はひどく残酷なことを言っているけど、自分でも止められない。言葉が舌からゆっくりと、動かしがたい確かさで転がり出る。"


show rin basic_surprised_close
with charachange



"それがまるで本物の打撃のように、琳にぶつかるのがわかる。"




"その目の隅に水がわき上がるけど、拒絶されたショックで目は大きく開いたままだ。"


show rin basic_crying_close
with charachange


"青白い肌に涙がこぼれ始めても、琳はそれを止めようとしない。"



"涙が一つ一つ、床にまで落ちていく間、琳は立ち尽くしたまま、うつろな不信感に満ちた目で俺を見つめる。"



rin "……"



"でもやがて現実が追いついてくる。"


show rin negative_crying_superclose
with vpunch



"琳はしぼんでしまうかのように前に倒れこむと、俺のシャツに深々と顔をうずめる。"




"俺が支えてやると、その体は重く、羽のように軽い。"




"琳は泣きじゃくりも、喚きもしない。ただ俺に寄りかかり、その熱い涙をシャツ越しに下の肌まで染み込ませる。"




"そして俺も琳のなすがままにさせ、手をその肩に回して、ぎこちなく抱きしめる。でも琳をなだめる役にはまるで立っていない。"




"指先に琳の背骨を感じる。その堅いぎざぎざがこの状況の救いのなさを思い起こさせる。"




"俺の手に触れる、その華奢な肩が震えているのは見ていてかわいそうだ。自分自身が琳の悲しみの理由の一部だったという絶望が、俺の心をずたずたにする。"


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\n\n\n女の子を泣かせるのは一番卑劣な行いだ。"


n "\nそれが琳であっても。琳だからこそ。"


n "\n超然としているその裏では、琳もひとりの人間だったんだ。"




n "戸惑い、恐れ、途方に暮れていた。他の人と同じように。"





n "琳の行動や言葉には大抵の場合、道理も分別もないと思っていた。でも今だけは、琳の気持ちが本当に理解できる気がする。"




n "\n\nでもそれを説明できる言葉も、慰める言葉も存在しない。"


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear

show bg school_nomiya:
    "bg school_nomiya_ss" with Dissolve(8.0)
show rin negative_crying_superclose:
    "rin negative_crying_superclose_ss" with Dissolve(8.0, alpha=True)
with None

stop music fadeout 5.0



n "\n\n\n\n\nだから、俺たちは言葉もなく立ち尽くし、静かに涙が涸れるのを待っている。"





n "時間が痛いほどゆっくりと過ぎていく。緩慢に空気中を漂うほこりの小片さえ、静止しているかのように見える。"




n "お定まりの壁掛け時計がドアの上からカチカチと鳴り、気分をかき乱す。"




n "俺は秒数を数えることにする。そうすればもっと時間を長く感じられる。"



n "\n\n……"

play music music_serene fadein 9.0

nvl hide dissolve
nvl clear

show rin basic_crying_superclose_ss
with charachange

window show



"やがて琳は少し体を動かし、まだ俺の胸に顔を押しつけたまま、シャツに向かってつぶやく。"



rin "もう少しここにいさせて"

show rin negative_crying_superclose_ss
with charachange


rin "お願い、久夫"


rin "少しだけでいいから"



"心地よいなにかが俺の意識に押し寄せてくる。あれだけいろんなことがあった後でさえ、俺には琳をここにいさせてやることしかできないけど、琳が今望んでいることはそれだけだ、という気づきが。"



hi "ああ"



"かくして、琳はそこにとどまる。"




"それでも俺は、きちんと琳を抱きしめるためにその身を引き寄せることができずにいる。"




"そうしたらあまりに悲しくなってしまうに違いなくて、耐えられる自信がなかった。"


$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve




n "\n\n俺たちは決して、相手のためにと自分が望んでいるような存在にはなれないかもしれない。そんな実感がダイヤモンドのように硬い悟りへと結晶化する。"





n "痛みが電気ショックのように心を突き抜ける。"



n "痛い。"



n "この確かさが……痛い。"




n "俺たちはお互いにとってどんな存在になれるだろう？　どうしようもなく意味がなさそうなのに、必死になってお互いにしがみつくことに何の意味がある？"





n "琳になんて言えばいい？　琳を慰めるにはどうすればいい？"




n "俺には一つもわかりはしないし、恐らく理解していたとしてもさらに痛みをもたらすだけだ。"




n "この痛ましい事実を考えたくなくて、無理やり心を空っぽにする。"




n "思考はすぐに落ち着く。悲しみは散っていき、俺と琳、そして胸に当たる繊細な暖かさと柔らかさだけが残る。"



nvl clear



n "\n俺はいつ琳のことを好きになったんだろうか？"






n "思い出せないけど、あのオレンジ色の午後、風邪を引いた琳をはっきりしない理由で見舞いに行ったときの、あの温かいくちびるの感触よりずっと前だったというのは確かだ。"






n "琳の気ままな態度、琳を取り巻く異質な雰囲気、琳を琳たらしめるすべてのもの……それらが圧倒的な力で俺をとらえた。"





n "琳がありとあらゆるものを受け入れ、自分がそこに認めた価値だけを与え、あらゆるものを公平に偏見なく比較し、自分の望み通りに世界を見る、そのやり方。"






n "それは俺には決してできないことだ。俺にとっての琳はたぶん、琳にとってのどんなものよりも、強くインスピレーションを与えてくれる存在だった。"





n "琳はあまりにも自由に見えた。まさに自由な精神だった。その一方で、あらゆることを絶えず不安がっている俺は、恥ずかしくなるくらい引っ込み思案に見えていた。"




n "だから俺は琳に強くしがみついたんだろう。俺のどんよりとした人生とはあまりに違う、琳の世界に入り込もうとして。"


nvl clear



n "\n\n気づかないうちに、あの抗いようのない力が俺を危険なほど近くに琳に引きつけたけど、でも結局、それは俺にとって異質すぎるものだった。"




n "そして俺はよりによって、ニュートンの法則も忘れていた。"







n "引力は物体間の距離の二乗に反比例する……"





n "じゃあ、２人の人間がお互いに感情を抱いていたら……"




n "へっ。"




n "感情は宇宙の法則に支配されていないというのに、俺はずいぶん前から琳という明るく輝く星の衛星になっていたんだと思わずにはいられない。"




n "\n惑星琳。"




n "\nそんなことを考えて笑ってしまいそうになる。確かに、琳は本当に別の星から来たように思えることがある。緑の肌と触手はないけど。"


$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

show rin negative_sad_close_ss
with charadistant

window show



"俺の抑えた笑いのせいだろうか、琳は体を引き離し、俺もそれを止めない。琳のぬくもりが消えたあとの冷たさと、あんな荒唐無稽な考えをめぐらせたことにちょっとした恥ずかしさを感じる。"




"琳に悪影響を受けたせいだということにする。でも同時に、琳が実際には人の心を読めなくてよかった思う。"




"琳の苦い涙は涸れて、少しは琳らしい様子になる。"


show rin basic_sad_close_ss
with charachange




"それでも途方に暮れた表情はまだ残っている。琳の視線は落ち着きなくあたりをさまよい、そして俺に留まる。"





rin "今のはなんだったの？"



rin "教えてくれる？"



hi "はあ？　どういう意味だよ？"


show rin basic_upset_close_ss
with charachange


rin "私、泣いてた"


"自分でも信じられないかのように、おずおずという。"


hi "そうだな……"


"……"



"琳はこの深い戸惑いを感じずに済むような導きを請うかのように、俺を見つめ続ける。"



"……"

show rin basic_sad_close_ss
with charachange


rin "どうして？"


hi "悲しかったんだろ"




hi "そう言ってほしいのか？　でもそんなのわかりきってるだろ？"



show rin negative_confused_close_ss
with charachange



rin "わからない。泣くのって変な感じ"




hi "なんだそれ？　そんなわけないだろ。というか、誰でもすることだぞ。それがふつ――"




"『普通』と言い終わる前に俺は言葉を飲み込む。"




"今俺が話しかけている人物には、そういう基準は当てはまらない。"


show rin negative_worried_close_ss
with charachange



rin "こんなのおかしいってずっと思ってたんだ、私の中にあるものと違うって。自分がどんな風に感じてるのかちゃんと説明できない、っていうか"




rin "だから、もしかしたら私は自分の感じてることがわからないんじゃないかって思い始めた。おかしいのは私自身なんじゃないかって――"




rin "そんなことを考えてた"


show rin negative_sad_close_ss
with charachange



rin "私……絵を描くだけで十分だと思ってた。少なくともそれだけはうまくできると思えたから"




rin "頑張れば私の中にあるものはみんな絵にできるって思ってた。実際にできてたんだ"




rin "でも、もうそれだけじゃ足りなくなってる。だって私以外の誰にも見ることができないなら、私はやっぱりひとりぼっちだから"


show rin basic_absent_close_ss
with charachange



rin "挑戦したのは間違いだったの？　あのせいでみんなすごく怒ってたから"


stop music fadeout 6.0



"琳が一度にこんなにしゃべるのはほとんど見たことがない。"





"しゃべり終えると、琳はただ口を閉じる。その様子はあまりに当たり障りがなくて、たった今まであんなことをしゃべっていたのが信じがたい。"




"なんて考えればいいのかわからない。"



"……"




"琳は誰かに自分が描いた絵を見てほしいと、それを通じてどうにかして自分の本質を見抜いてほしい、気持ちを理解してほしいと思って必死になっていた……"




"それは……それ以外の方法では表現できないと思っていたから、なのか？"





"それが正しいとか間違ってるなんて、誰が言えるんだ？"




"俺が琳に手を差し伸べようと努力していたように、もしかして琳も今までずっと俺に手を差し伸べようとしていたのだろうか？"



"……"




"俺は考えるために、そして長いこと立ちっぱなしだった足を休めるために、机に腰掛ける。"



play music music_innocence fadein 12.0



hi "あのさ、面白い本を読むとか星空を眺めるとかしたときにさ、こう……深いものを感じるんだ。例えば……ああもう、なんて言ったらいいんだろう"





hi "だけど言葉にしようとした瞬間、何かが失われる気がするんだ。頭の中で思っていたのに比べて、リアルさとか正確さがなくなってしまうみたいな"





hi "なんか偽物っぽい感じがするんだ。まったく、今言ったこともなんだか偽物っぽいな"




"俺はおかしいのと、自嘲の中間くらいの意味で笑みを浮かべるけど、琳は反応を見せない。"



hi "まあとにかく……"



hi "自分の本当の気持ちを他人にわかってもらえるように表現することなんて、誰にもできないのかもしれないんだ"




hi "現実なんて、人が頭の中で考えてることには絶対に比べようがないんだ"




hi "比べられるものなんてあるわけがない。お前の絵だってそうだ。お前にとっては違うのかもしれないけど"




hi "でも、何もかも頭の中にしまっておけるわけじゃないよな。そんなことしたら本当に爆発しちまう"




hi "俺が言いたいのはさ……自分の気持ちを表現するのは間違ってるとは思わないってことさ。絵をその手段にしたとしても"




hi "ただ、それ以外の方法で表現するよりも、他の人によく理解してもらえるなんて期待はしない方がいい、ってだけだよ"




hi "というか、そもそも人に理解してもらうなんて無理だよ"




hi "物事はなんでもすごく主観的だからさ。お前はお前の見方で世界を見るけど、それは他の人の見方とは違うんだ"


show rin basic_sad_close_ss
with charachange



rin "でも、そんなのってひどいよ"




hi "そうかもな、ある意味では"



"……"

show rin relaxed_doubt_close_ss
with charachange



"琳はできるだけ打ちひしがれたように顔をしかめる。それでもそれほどじゃないけど、琳があまりいい気分でないのを理解するのには十分だ。"



rin "そんなの、やっぱり悲しくなっちゃうな"


hi "ああ、そうだろうな"



hi "俺にできることがあればよかったんだけど"




"苦々しくは聞こえないよう言ったつもりだけど、俺自身は少しだけ苦い思いをしている。"



"これは俺の問題だ。俺は琳の望むようにはなれない。同じ理由で、琳も俺の望むようにはなれない。"


"……"

show rin negative_worried_close_ss
with charachange



"琳は難しい表情をすると、慎重に言葉を選んでいる。"




"琳にも何かを口にするのが難しいときがあるんだな。"


show rin basic_sad_close_ss
with charachange



rin "しかたないんだろうね"


show rin basic_absent_close_ss
with charachange



rin "……でも……君が言うなら……"


show rin basic_awayabsent_close_ss
with charachange


rin "少しは気が晴れるかな"


"……"



"こういうとき、一見どうでもいいようなことが一番大事なことだったりするのがおかしい。"




"今の琳の声がとても小さくて、かろうじて聞き取れるくらいだったこととか。"




"琳が下を向くと、その短い前髪が目を覆ってしまうこととか。"


show rin basic_blush_close_ss
with charachange



"そして、それが琳の頬から耳の先まで真っ赤に染まっているのを隠せていないこととか。"



"とても興味深い、濃い赤に染まっている。"



"水を打ったような静けさが後に続く。"




"見てはいけないものを見てしまったみたいで、かなり気まずい。わざと見たわけじゃないけど。"




"何と言ってやればいいのか分からない。でも分かっていなきゃいけないはずだという気がしてならない。"




"琳もわかってはいない。"




"それでも、こうして黙り込んでいても、失われるような勢いはない気がする。"




"そんな状況であっても切れることのない、奇妙な無言の関係で俺たちがつながっているかのように。"


show rin relaxed_nonchalant_close_ss
with charachange



"琳はしきりに体重を足から足へ移動させながら、部屋中を見回している。俺を除いて。"




"最後にこの空気を破るのは彼女だった。"


show rin basic_deadpan_close_ss
with charachange


rin "いこっか？　もうここにはいたくないや"



hi "ああ、そうか、そうだよな。どこに行く？"




"俺の返事も琳の提案と同じくらいに、緊張を隠し切れていない。"


show rin relaxed_sleepy_close_ss
with charachange




rin "好きなとこに行っていいよ。私、寝たいんだ。もう何週間も満足に寝られてなかったから"



show rin basic_lucid_close_ss
with charachange




rin "頭のなかでライトブルーの蝶々がたくさん飛んでるみたいなんだ。だからうまく考えられなくてさ"



show rin basic_deadpannormal_close_ss
with charachange



rin "そこまで明るいブルーの蝶なんて存在しないと思うけどね、今朝の笑美のパンツみたいに"


show rin negative_spaciness_close_ss
with Dissolve(0.1)

show rin basic_absent_close_ss
with Dissolve(0.1)

show rin negative_spaciness_close_ss
with Dissolve(0.05)

show rin basic_absent_close_ss
with Dissolve(0.05)

show rin negative_spaciness_close_ss
with Dissolve(0.05)

show rin basic_absent_close_ss
with Dissolve(0.05)

show rin negative_spaciness_close_ss
with Dissolve(0.1)

show rin basic_deadpannormal_close_ss
with Dissolve(0.2)



"琳が頭を振ると、俺はウルトラマリン色の蝶が琳の耳から飛び出してくるんじゃないかと身構える。"



show rin basic_deadpanamused_close_ss
with charachange



"小さな笑みが琳の口元を引っ張りあげる。"




rin "それで思い出した。青のことだよ、パンツじゃなくて"


show rin basic_deadpandelight_close_ss
with charachange



rin "たくさんの蝶は『群れ』って言うんだね。私、調べたんだ"




"それを聞いて、疑問で俺の眉はつり上がる。"




hi "じゃあ、どうしてそう言わないんだ？"


show rin basic_absent_close_ss
with charachange



rin "他の言い方のほうがいいんだ"




"じゃあ、どうしてわざわざ調べたんだ？"




hi "じゃあそう言えばいいだろ？"


show rin basic_awayabsent_close_ss
with charachange




"琳はうなずいて口を閉ざす。俺と向き合っていたその視線は、窓越しに屈折する濃いオレンジ色の日差しに引っ張られて脇にそれる。"





"そのまましばらく、俺たちはそうしている。琳が窓の外を黙って見ているのを、俺が黙って見ている。"



hi "おい……大丈夫かよ？"

show rin basic_absent_close_ss
with charachange



"琳は目の端で、また何か言いたげに俺を見る。反射する日の光も、それ以上琳の本音を明らかにはしない。"




rin "それは考えないといけないね"




"ついに琳がさらけ出した、存在さえ知らなかったこの手がかりにすがる思いで、この会話を続けたいと願う。"


show rin basic_awayabsent_close_ss
with charachange



"だけど琳は上の空で窓の外を見ていて、いずれにせよ意味のある返事をしそうにないのはわかりきっている。"




"これは琳の防御機構みたいなものだ。筋が通った思考を避けるための。"



"琳の心はそれ自体が蝶のようで、高揚したときはいつもどこかを飛び回っている。"



"琳のベールの裏側が見えたと思ったとたんに、琳は俺の手の届くところから飛び出してしまう。"



"これが琳なんだろうな。"



"俺が安心できるようになるには、とにかくこれを受け入れるべきなのかもしれない。"




hi "わかった"



hi "じゃあ部屋まで送るよ"


show rin basic_absent_close_ss
with charachange


rin "ありがと"

show rin basic_lucid_close_ss
with charachange


rin "ほんとに"

stop music fadeout 12.0

scene bg school_hallway3
with locationchange



"生徒の姿がない、無人の学校の廊下はとても寂しげだ。"




"夏休みが始まって一時間も経ってないのに、建物は打ち捨てられたように見える。この静けさに割って入るのは俺たちの足音だけだ。"




"この変化は突然だけど、それは生徒と先生のいない学校が、死に絶えた空っぽの殻でしかないことを表している。"




"まるで学校が、荒れ果てて静寂とチョークの粉で満たされた、俺たち２人だけのプライベートな世界になったみたいだ。"


scene bg school_staircase2_ss
show rin relaxed_sleepy_close_ss at twoleft
with locationchange


rin "私も変わらないといけないね"



"３階の階段を降りながら、琳は出し抜けに言う。俺がついこの間考えていたことを正確に繰り返している気がする。"





hi "時には、人は変わらなくちゃいけないのさ"


window hide
nvl clear
nvl show dissolve



n "話せることはもっといっぱいあったけど、それがその日俺たちがお互いに言った最後の言葉だった。"




n "その言葉さえすべてを包み込む静けさに沈み、まるで会話などなかったかのように、よどんだ空気の中へ消えていった。"



nvl clear
nvl hide dissolve

$ suppress_window_before_timeskip = True

scene black
with dissolve

label jp_R41:

play music music_dreamy fadein 2.0

scene bg school_dormhisao_rn
with charachange

$ renpy.music.set_volume(0.4, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0


"夏休み最初の日にはがっかりだ。"



"目を覚ましたら、鉛色の空から聖書に出てきそうな大雨が降っていた。"



"そのときの俺は楽観的だった。"



"夏のにわか雨だろうと思っていた。数分のうちにザーッと降って、それで終わりだと。"


show rain normal behind bg
with None



"そんな都合良くはいかなかった。"


$ renpy.music.set_volume(0.7, 1.0, channel="ambient")

hide bg
show bg misc_sky_rn as bg2 behind rain
show hisaowindow
with locationchange



"雨水は絶え間なく青灰色の空から降り注いでいて、窓ガラスを小さな川になって流れ落ち、寄せ集められて遊歩道に小さな池を作る。"




"その様子は２時間半前から全く変わっていない。"


$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

scene bg school_dormhisao_rn
with charachange


"そこで、俺はぐずぐずと掃除をしたり本を読んだりして、それに飽きたら荷物をまとめたりする。"



"この天気のおかげで気分もひどく沈んでしまい、何をするにもきちんとやるのが大変だ。"


play sound sfx_impact2



"何かがひどく大きな音で部屋のドアにぶつかって、俺を無気力から呼び起こす。"




"健二がバカみたいな屋内ボウリングでもやっていないことを祈ろう。"



"……"



"ドアのほうまで歩いていって開けるまで、それ以上廊下からはなにも聞こえてこない。"


play sound sfx_dooropen
$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
stop music fadeout 2.0

scene bg school_dormhallway
show rin basic_absent
with locationchange


"琳だ。"



"その姿を見て、もう少し嬉しい気持ちになれたら良かったんだけど。でも琳が俺に会いに来たことに驚いてそれどころじゃなかったし、それに琳はずぶ濡れだ。"




"制服のシャツも水浸しで、体中からしずくが垂れて足下に水たまりを作っている。"




"雨のしずくが短い前髪から滴り落ちると、今度は鼻を滑り降りて、鼻先から落ちていく。"



"ひとつ。{w=0.7} また、{w=0.7} ひとつ。"




hi "あー……よお"



hi "気分はどうだ？"

show rin basic_deadpannormal
with charachange



rin "普通の『中』かな"


play music music_rin fadein 2.0


"どういう意味なのかわからないその言葉は置いておいて、琳は間違いなく調子が良くなさそうだ。"


hi "ずぶ濡れじゃないか"

show rin basic_absent
with charachange



rin "外にいたからだよ。知ってた？"




hi "なんで外にいたんだよ？　気づいてなかったのかも知れないけど、外は大雨だぞ"


show rin basic_deadpancontemplation
with charachange



rin "気づいてなかった。確かに大雨だね。散歩してたんだ"




hi "それがお前の言う『自己憐憫に浸る』ってやつなのか？"


show rin basic_deadpanupset
with charachange


rin "私ってそんなに憐れかな？"



hi "いや、お前がそう考えてそうだって言ったんだ"


show rin basic_awayabsent
with charachange



rin "考えてない。それに雨は悲しいものじゃないよ"


show rin basic_absent
with charachange



rin "雨の中を歩いたことないの？"



hi "そりゃああるよ。ただ、それなりに用意をしてだぞ、傘とかさ"

show rin basic_lucid
with charachange



rin "青と白のしましまの傘を持ってるって想像すればいいんだよ"




hi "雨が頭に当たってるときにそれは難しいんじゃないか"


show rin basic_deadpannormal
with charachange


rin "もっとちゃんと想像して"


"……"


"ああ、確かにいつもの琳に戻ってる。"



"本人にそんなつもりはなくても本当に頭にくる、嫌味半分のぶしつけな言葉。こちらに見えるよりも多くのものを求めてくる、うつろでぼんやりとした視線。"





"本当に……すごく琳らしいな。"


show rin basic_deadpan
with charachange



rin "入れてもらわないとだめかも。この濡れてるのとか、服とかどうにかしないと"




"脳がすぐにその意味を理解して、言葉に詰まってしまう。琳がやすやすと踏み入ってくるのとはまるで対照的だ。"



hi "それなら笑美に……"

show rin basic_lucid
with charachange



"琳は激しく頭を振ると、水しぶきをあたりにまき散らす。"



rin "もう帰っちゃったよ"

show rin basic_awayabsent
with charachange




rin "それに笑美、これ以上心配したり大騒ぎできなくなるまで心配したり大騒ぎするからね。そうなるまでいつも時間がかかってうっとうしいし"



show rin basic_absent
show rain normal behind bg
with charachange




rin "はっきり言うと、私が聞いてられるよりも時間かかるんだよね。で、君は世話焼きってタイプじゃなさそうだと思ったから"







$ renpy.music.set_volume(0.4, 1.0, channel="ambient")

hide bg
show rin invis_close at center
show bg misc_sky_rn as bg2 behind rain
show hisaowindow behind rin
with locationchange

show rin relaxed_nonchalant_close_rn:
    ypos 1.1
with Dissolvemove(0.5)

stop music fadeout 8.0
play sound sfx_rustling


"琳はベシャっという音を立てながら、俺の机の上にどっしりと座り込む。"


"ずぶ濡れの服が机の上のものを濡らすけど、琳は気にもとめない。"


"……"



hi "わかった。いいよ。手伝うよ"




hi "どっかにタオルがあったな。乾いた服に着替えるか？　制服でもいい？　お前のより大きいけど、でも……"

show rin basic_lucid_close_rn
with charachange



rin "おまかせするよ"


show bg school_dormhisao_rn
with locationchange


"少し探すと、使っていない制服とふかふかのタオルがクローゼットの奥から出てくる。"

hide bg
with locationchange



"片手にタオル、もう片方に制服を持って、次にどうすればいいのかわからないまま琳のほうに向き直る。"




"どうかしてるな、俺は。普通の男だったら間違いなく――{w=1.0}{nw}"


show rin basic_absent_close_rn
with charachange


rin "心配するのやめて。なんでもないんだから"



"きっと俺の怖じ気づいた様子がはっきり見てとれたんだろう。"




"まるで、琳には何でもお見通しみたいだ。"




"俺は心配を押しやると、俺のシャツと全く同じように、琳のシャツに並んでいる８つのボタンに集中する。"




"一番上のボタンだけは手こずったけど、それを乗り越えた後は、少し震えのおさまった手で他のボタンを外していく。"



$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
play music music_heart fadein 0.5

scene ev rin_wet_pan_down:
    center
    yalign 1.0 subpixel True
    easein 20.0 yalign 0.0
with whiteout



"濡れたシャツを横に放ると、琳の青白い、ライトブルーのブラジャーに覆われただけの上半身が露わになる。好きな色だと言っていたのをすぐに思い出す。"





"あまり……余計なことは考えまいとする。でも琳の体を、この複雑な気持ちとしか呼びようのないもので見ないようにするのは無理がある。"





"それをなんて思えばいいのかわからなくて、俺はただ琳を見る。琳は……もろく見える。"




"まるで貝のようだ。辛うじて形を保っている、今にも壊れそうな存在。"




"一本一本の肋骨が青白い肌の下に見えて、呼吸に合わせて上下に動いている。"





"琳はとても華奢だと普段から思っていたけど、展覧会のオープニングの前の熱に浮かされたような制作期間のせいで体重が減ったのかもしれないと思い至る。"





"ちゃんとしたものを、十分に食べてたんだろうか？　絶対まともな食事なんてしてないだろう。量も多分足りてない。"





"俺が好意を抱いている子の、醜いけども美しい、人としてのぎりぎりの水準しか満たしていないこの肉体は、それ自体が美学と矛盾していて、それが奇妙なほど似合っている。"




"俺の目は琳の鎖骨から肩をたどって、その腕が突然途切れるところまで降りていく。"




"いや、ぎりぎりでさえない。そう思うと悲しくて胸が痛むし、そう思ったことへのやましさも感じる。"


scene ev rin_wet_arms:
    center
    xalign 0.0 subpixel True
    linear 20.0 xalign 1.0
with flash



"使われていないせいで、琳の腕はほとんど骨と皮の状態まで退化していて、制服の長い袖に隠れていない今はとても短く見える。"




"俺がネガティブな反応を示さなくなったのは、学校の仲間たちが色々と身体的に普通でないことに、大体慣れてしまったということなんだろう。"







"どうして琳が袖を長いままにしておくのかいつも不思議だった。ただ肘があるはずのあたりを簡単に縛っているだけだ。"




"あまり実用的には見えないけど、そもそも琳は実用的という言葉からはほど遠いやつだった。"




"琳はこれが気に入っているのかもしれないし、それがとにかく重要なのかもしれない。特に深い理由はないのかもしれない。"




"理由を聞いてみたくなって、もう少しでそうしかけるけど、この琳の惨状を先に世話してやらないといけない。"


scene ev rin_wet_face_down:
    center
    yalign 0.0
with flash



"互いにとげとげしい挨拶の言葉が尽きてしまってから、琳は口をつぐんでいる。"




"じゃあ雑談する必要はなさそうだな。"


scene ev rin_wet_towel_down
with charachange



"俺はベッドの上に置いたタオルを手に取ると、琳の頭にかぶせて、雨水が大体取れたと思えるまでくしゃくしゃと髪を拭く。"



scene ev rin_wet_towel_up
with charachange


"琳はタオルの下から無感情な目で俺をのぞき見る。"



"言葉もなく何かを訴えようとしているように見える。"



"そういう感じの目だ。"



"でも琳の考えはその表情からは読み取れなくて、ただタオルで肩や髪の毛のあたりを拭き続ける。"




"沈黙が恐ろしくて、耐え難い。"




"俺たちのコミュニケーションは突然、俺の手とタオルの動き、それから前後に揺れる琳の体の動きだけになってしまう。"





"俺の途切れ途切れの息と琳の静かな息が、共通するリズムを探り合うけど、そんなものはここには存在しない。"




"琳の心音が聞こえるような気がする。それとも俺の心臓が早く打ち過ぎているだけなのか。"





"耳の脇の乱れた髪を拭いてやると、琳は突然俺の手の甲にほおを押し付けてくる。"





"その接触は電撃のようで、ショックが全身を貫く。"



scene ev rin_wet_towel_touch
with charachange




"琳が求めているのが安らぎなのか、温もりなのか、単に俺に触れたいだけなのかはわからないけど、俺は琳の柔らかなほおに触れかえして、撫でさすらずにはいられない。"




"そして眼を閉じて、琳は俺の指にキスをする。くちびるで関節をなぞりながら。"



"言葉では表しようがないくらい悲しくなる。"




"お互いに恋か何かに落ちている少年と少女……いや違うか……まだ……"


$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve




n "何かが壊れている。俺と琳はそんな感じがする。目を合わせるのを避けて、視線をお互いに少ししか交わさないところとか。琳の閉じこもった、臆病そうな姿勢とか。俺がその繊細な形を壊してしまうのを恐れて、陶器の人形相手のように琳に触れるところとか。"







n "今までにないくらい俺たちの距離が近づいているというのに、ちっとも嬉しいと思えないこととか。昨日みたいに。"





n "いつから優しさと空しさが同じ意味、同じ言葉になり、愛情から出る行為はただ渇望をかき立てるだけになってしまったんだ？　……どうして俺たちはこんなことになっちまったんだ？"





n "『よせ、それには答えるな』。そう自分に言いたいけど、意識の上ではとっくに答えは分かってしまっている。逆らっても無駄だ。"




n "それでも俺はここにいて、琳もいる。そして琳ならどんな問題にぶつかってもそれを解決できるような気がする。"




n "もし琳にできるなら、どうして俺にはできなかった？　どうして俺たちにはできなかった？"




n "そうするのは大変すぎて、難しすぎて、不確かすぎるように思う。"




n "だから今の俺には、琳がまた風邪を引かないように乾かしてやることしかできない。"


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve
nvl clear

scene ev rin_wet_face_up
with charachange

window show



"琳の頭を撫でて、濡れていても断固として整えられるのを拒否する髪を整えようとする。"





"黒い、ぼんやりとした目が俺のあらゆる動きを追う。"




hi "ズボンもか？"

scene ev rin_wet_face_down
with charachange




"琳はうなずいて答えると、背をそらして足を開く。その誘うような蠱惑的な動きに、悪い予感のようなぞっとする感覚が背骨を上へ下へとうごめいていく。"






"でもこの沈黙のせいで自分が引き離されているような気分になり始めていて、それだけでは冷静さを取り戻せない。"




"このことを、さもなければ何でもいいから琳と話すべきか。考えなきゃいけないのに考えることもせず、俺は無意識に動く。"





"この沈黙は魔法だ。鈍い雨の音と指に感じる琳のやわらかな肌の感触からなる、秘密の世界に俺たちを縛り付けた約束だ。"





"ズボンのボタンはしっかり留まっているけど、驚くほど簡単に外れる。"




"琳が座っているせいで、脱がせるのが難しい。しかも俺を手伝うために立ち上がる気もない。"


scene unlock_evh rin_h2_pan_surprise
show evh rin_h2_pan_surprise:
    xalign 0.5 yalign 0.0
with whiteout



"あらわになった足をさっさと拭いてしまおうと、俺は気まずいながら刺激的な気分で琳の足の間にひざまずく。俺の手と同じくらい、琳にとって大切なものだということを思い出しながら。"




"タオルで足首を拭いていると、琳は俺のほおに太ももを触れさせ、かかとで俺の背中を小突いて俺を引っ張り寄せる。"


"俺は琳の無言の目を見上げる。琳もそれを待っていた。"




"その控えめな、期待するような視線は、今度はそっちの番だと言っているみたいだ。"




"……"




"すぐさま琳の内ももに手を触れる。"


show unlock_evh rin_h2_pan_away
show evh rin_h2_pan_away
with charachange



"琳は息を止めようとしていたかのように、はっと息を呑む。"




"じゃあ、これはどうだ？"


show unlock_evh rin_h2_pan_closed
show evh rin_h2_pan_closed
with charachange



"太ももに軽くキスをすると、それだけで琳は落ち着きを失い、目を閉じて、かろうじて聞き取れるくらい小さな悲鳴を漏らす。"





"……お前もこれを望んでるのか？　もう大丈夫なのか？　こんなことをしても？"



show evh rin_h2_pan_closed:
    subpixel True
    acdc_warp 8.0 yalign 1.0
with None



"……もしかして？　もしかしたら……"



"もやもやした考えが焦点の定まらない心の裏に浮かんでいる。"



"なんだろう、この状況のせいで考えるのが難しい。頭いっぱいに綿が詰まっているみたいだ。"





"でも構いやしない。今の俺たちに必要なのは考えることじゃなさそうだ。"



label jp_R41h:
show evh rin_h2_nopan_closed:
    yalign 1.0
with Dissolvemove(0.5)

$ renpy.music.play(music_heart, fadein=0.5, if_changed=True)





"布地がとても小さいおかげで、琳のパンティを引き抜くのはズボンよりもずっと簡単だ。"




"それは琳の足からどこかへと滑り落ちて、俺の視界から消える。"



"琳の足がまだ雨に濡れているのを見ると、上手く拭けてやれていなかったみたいだ。"


"まあいいさ。"

show evh rin_h2_hisao_closed
with charachange


"理性よりも本能に導かれ、俺は近づいて別の湿った場所に口をつける。"



"肌への緩やかな舌の動きに、肉へのキスに琳も応える。"



"琳の筋肉は俺のしていることが不快であるかのようにリズミカルに収縮する。"





"俺が吸いつくときに、琳が声が出ないよう我慢しているのを聞くのは……非現実的だ。"





"今朝の出来事全てがあまりにも非現実的だ。醒めつつある夢の、漠然とした現実味のなさのように。"




"俺も琳相手に、今こうして、こんなことをしているのが信じられない。でも俺は流れに身を任せている。"




"それに、後戻りできるようなタイミングはとっくに通り過ぎてしまった。"




"俺はあちこち動き回って、いろんな手で琳を攻め立ててみる。琳の弱いところを探しあてようとする。じらして、悦びに狂わせようとする。俺がそうしたい、琳相手にそうしたいからだ。"




"だけど琳は声ひとつ上げず、身悶えもしない。俺が何をしようと、琳をこれ以上狂わせることはできないのかもしれない。"




"乱れた重い呼吸に混じる意味をなさない喘ぎ声は、錯乱した人間のそれだけど、それを引き起こしているのは俺じゃない。"




"俺はそれを琳から解き放っただけだ。"




"どんどん濡れてくる。俺はそれを飲む。俺の内側で熱が高まっていくのを感じる。"




"こうやって琳の全てを感じるために、琳の一番深いところへたどり着こうとする。"




"俺の行為の一つ一つ、すべてに違った反応が返ってくるけど、どれも純粋な情欲によるものだ。"


show evh rin_h2_hisao_closed:
    subpixel True
    acdc_warp 16.0 yalign 0.0
with None



"琳は欲望に浸っていて、今なら俺に何をされても構わず身を任せようとしている。"






"琳が解き放たれるその時がいよいよ近づいてくる。でもそこに至る道は狂気の上り坂だ。"





"それでも琳は止まらない。"




"押し寄せる甘いけいれんの波に、もう筋肉が緩むひまもない。"




"琳はただただ体をこわばらせていく。あまりに縮こまっていて見るからに辛そうだけど、それでも俺は逃がさない。"




"俺は止めないし、琳が求めているのもわかっている。琳はどうしようもなく俺にこうされたがっている。"





"片方の足が俺の肩にかかって、さらに俺を引き寄せる。近すぎて窒息しそうな気がしてくる。"




"俺はさらに続ける。それ以外の可能性はありえないから。"


stop music fadeout 8.0
stop ambient fadeout 12.0



"琳を喘がせるボタンを押し、その足が引きつるように俺の背中を締め付け、快感で我を忘れているまさにその瞬間、俺は本来の目的や、あるべきだったことを全て忘れてしまう。"




"琳が来たこと……あとどこかの時点でタオルもあった。それしか覚えていない。"






"そんなことは全部どうでもいい。大事なのは、今俺たちがしていることだ。"




"琳が迎えた絶頂は俺をも貫いて、今まで経験したことのない形で俺を興奮させる。"




"その興奮が俺を心配させる。緊張する。落ち着かない。"


show evh rin_h2_hisao_away:
    yalign 0.0
with Dissolvemove(0.5)



"琳の体が弛緩すると、俺はまた下の場所にキスしようとするけど、琳はびくっと驚いて跳びはねてしまう。"


show evh rin_h2_hisao_surprise
with charachange


rin "待って……久夫……もういい"


rin "こっち来て"

scene bg school_dormhisao_rn
with locationchange


"俺は立ち上がって琳が着ている最後の衣服を脱がせる。"


"琳は息をつくために俺のほうにもたれかかる。シャツの内側に吐き出された暖かい空気が俺をくすぐる。"



"手探りで、俺は琳の背中から肩甲骨の下に手を回して、ブラジャーの留め具を探す。"




"それは思っていたよりも簡単に外れて、そのまま床のどこかに落ちる。"


play music music_romance fadein 10.0

scene ev rin_pair_base_clothes
show rp_hisao normal at truecenter
show rp_rin normal at truecenter
with whiteout



"俺に触れる琳のむき出しの肌の感触がたまらなくて、俺はもっとそれを味わいたくなり、そのまま琳を抱きしめる。"



"琳の髪は雨の匂いがする。俺は雨音が止んでいることに気づく。"



"俺は我に返る。俺たちだけの現実を覆っていたクッションはもうなくなってしまい、今起きていることをよりはっきりと理解する。"


show rp_hisao frown
with charachange



hi "なあ、友達同士でこういうことはするもんじゃないぜ"





"会話というごく簡単な行為が、時には圧倒的に難しくなることもあるんだと再認識しながら、俺はささやく。"



show rp_rin talk
with charachange


rin "私の友達、やめちゃうの？"






"そういう意味じゃない。でも琳の真剣な声色と、その問いの裏で幾重にも重なった含意に、俺は言葉を詰まらせる。"


show rp_hisao smile
with charachange


hi "いや"

show rp_rin smile
with charachange



rin "私……それでもいいと思うんだ。もしそうなっても"




"俺は琳を抱きしめると、その髪に微笑みかける。今度だけは琳の言っていることが完全に理解できる。"


show rp_rin frown
with charachange


rin "君、濡れてる"



"琳の肌に残っていた水気が俺のシャツに染み込んでいた。"





"なんだか、わかりきったことを言う琳の言葉も今の俺には嬉しい。"



show rp_hisao normal
with charachange


hi "そうだな。濡れてる。お前のせいだぞ"

show rp_rin normal
with charachange



rin "君が見たいな"


play sound sfx_rustling

scene ev rin_pair_base
with charachange



"言われたとおりに、俺は後ろに下がってシャツのボタンを外す。琳のときよりもずっと早く済む。"




"突然急かされているような気分になって、俺は急いで手を進める。"




"琳に触れずにいる一秒一秒が時間の浪費だ。チャンスの無駄遣いだ。"




"ベルトのバックルが邪魔をする。いつもなら一瞬で外せるのに。"


show rp_rin closed
with charachange



"手こずっていると、気づかないうちに琳が足を持ち上げて、つま先で俺の胸をなぞり始める。"


show rp_hisao frown
with charachange


"俺は琳が見ている部分を見下ろす……"


hi "心臓……"



"俺は反射的に胸の中央の傷跡を押さえて後ずさる。"






"発作の後に受けた手術の浅い傷口はもう治っているけど……まあ、ひどく不快とまではいかなくても、あまりきれいなものじゃない。"




"ほとんど目には見えないけど、琳は細かいところによく気が付く。琳が見たいって言っていたのはこれが理由なのか？"




"琳にちょっかいを出していたせいで、このことを忘れていた。でも今は体のことに関わる不愉快なことが一気に浮かんできて、鉄砲水のように心を突き抜けていく。"




"やれやれ、それに年を取ったおっさんがセックスの最中に心臓発作を起こす話を山ほど思い出してしまった。もしも……"


show rp_rin talk
with charachange


rin "久夫"


"……"



"雰囲気を壊しかけたことに気づいて、つっかえながら言い訳をする。"


show rp_hisao normal
with charachange


hi "ああ……悪い。ちょっとな……"

show rp_rin smile
with charachange


rin "触らせてよ"



"艶やかな、誘うような目だ。少しも恥じらうことなく、一糸まとわぬ姿で座っている。琳のこんな格好を見ることになるなんて思ってもみなかった。"


$ renpy.music.set_volume(0.1, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve



n "\n\nああ、わかってる。こんなことになるなんて間違ってる。"





n "琳がここにいるのに、もう聞くべきことも、邪魔なものも何もないのに、何かがずっとおかしいという気の狂いそうな感覚が……"




n "昨日、俺の心臓を捕らえたのと同じ感覚がまた現れる。"




n "俺たちは一緒だ。具体的にどこがどうとは言いづらいけど。とにかく説明しようとしてもとらえどころがないし、変化もしないからだ。"





n "\nこんな関係はうまくいくのか？　俺たちはもっと親しい関係へと変われるんだろうか？"





n "たとえこれから永遠に一緒に過ごしたとしても、決してお互いを理解しあうことができないかもしれないんだ。"





n "でも永遠なんてそもそもありえない。俺たちもずっと一緒にはいられないかもしれないってことだ。"





n "俺たち二人がお互いの違いを乗り越えられたとしても、時の流れは俺たちを容赦なく引き裂くだろう。"



nvl clear



n "\n\n琳は瞬間、気まぐれ、そして衝動の生き物だ。"




n "\n俺とは似ても似つかない。"



n "\nこれははっきりと理解できる事実だ。"



n "何よりも、他ならぬこの理由のために、俺はこの時をものにすべきだ。たとえ俺たちにはこの一瞬しかないのだとしても、それを無駄にしてはいけない。"





n "俺自身、逃れることはできないとしても。琳にもできない。今ならそれが分かる。"




n "\n俺たちには手放すことのできないもの、考えずにはいられないものがある。"





n "感じずにはいられない感覚が。"





n "でも、琳は何のためらいもなく俺を求めようとしている。今ここで。"


$ renpy.music.set_volume(0.2, 1.0, channel="ambient")
$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

show rp_hisao frown
with charachange

window show


hi "ごめんな、俺……"

show rp_rin closed
with charachange


rin "久夫、心配するの、本当にやめたほうがいいよ"




"俺がそれ以上しゃべる前に、琳が割って入る。助かった、そのまま続けていたら何を口走っていたか、わかったものじゃない。"





"いつもと違って現実味のある琳の声が、角を立てることもなく俺を優しくたしなめる。"


show rp_rin smile
with charachange



rin "もっと楽にならなきゃだめだよ"




"琳は淡々と俺を分析する。抜け目ないと言っていいくらいに。"



"琳の目に俺はどう映っているんだろう。"



"くそ。緑色がきつすぎて痛くなってくる。"




"琳の目にはいつも惹きこまれてしまう。いつもそれ自身のためにせわしなく動き回っている、不思議な、虜にされてしまいそうな目だ。"





"でも同時に、俺はその目を恐れていた。"





"そうだ。琳はいろんな意味で怖い。今は特にそうだ。"




"琳は恐ろしくなるくらい分かりやすい。その肌には鳥肌が立っていて、琳が寒がっていて、そしておびえているのが見てとれる。"



"どちらにせよ、俺は身を引き締めると、琳から一歩離れてもう一度抱きしめ、疑いを払いのける。"



"優しく、愛に満ちたその目を見て、俺の疑念はまるで冬の終わりの雪のように溶かされていく。"


scene evh rin_h_closed
with whiteout



"俺がそうしているのと同じように、琳は俺にもたれかかると、休まる場所を探して、こちらの肩に頭を押し当てる。"




rin "楽になって"



"そうだ。"

scene evh rin_h_left
with charachange



rin "過去とか未来とか、そんなことは忘れようよ。そんなの変えられるものじゃないんだから"




"琳に何か言いたかったけど、声を失った俺は曖昧なことをぼそぼそと言うだけだ。"



rin "今は私と一緒にいて"



"言わなくても、琳には俺が言いたかったことが分かったのかもしれない。"



rin "こっち来て"


hi "ここにいるじゃないか"

scene evh rin_h_normal
with charachange



rin "もっと近く"




"全身が前向きの思考しかしていない俺は、その言葉に従い、琳をより強く抱き締める。"


scene evh rin_h_right
with charachange


rin "もっと"



"下半身を押しつける。"


"琳は少し強張る。本当に少しだけだ。"

scene evh rin_h_closed_close
with characlose


rin "もっと"



"最後の嘆願は、もはや祈りに近い。"




"これ以上近づくには、方法は一つしかない。"




"俺は琳との間に手を伸ばして、手を添えながら自分自身を琳の中に潜り込ませていく。"


scene evh rin_h_strain_close
with charachange


"琳のあらゆる筋肉が一度にこわばる。"

scene evh rin_h_strain
with charadistant




"琳は何も言わず、表情も変えない。だからさらに奥へと進み、そして後ろに下がる。"






"再び前へ。琳も俺に合わせて動く。"





"俺たちの動きは一つの連なりへと融合する。前と後、中と外。"




"すべての感覚が鋭敏になり、１０倍にも増幅される。"




"俺の脳はこの興奮を理解するのをとうの昔にあきらめていて、今はその全てを全身で感じることしかできない。"





"琳も同じだ、俺には分かってる。見てとれる。感じとれる。"




"琳の呼吸が速くなる。落ち着きも優雅さもすっかり失い、温かい息を俺の肩に吹きかけている。"




"か細い息遣いの合間に、琳は時折俺に優しく、そっとキスをする。まるでちゃんとしたキスの仕方が分からないかのようだ。"




"でも、そこにためらいはない。"




"俺が一番奥まで入るように、琳は必死に俺にしがみついて、引っ張り寄せる。琳は俺に向かって、俺の周りを動くので、どこからが俺でどこまでが琳なのかわからなくなる。"




"俺たちにあるのは今この時だけで、そこから先にはもう何もないのに、まるで時間なんて無限にあるかのように、俺たちはゆっくりと、耐え難いほどゆっくりと続ける。"



"この感じはまるで――{w=0.7}{nw}"

scene evh rin_h_normal_close
with characlose


rin "待って……"


"俺はわずかに警戒して動きを止める。"


"痛んだのか、それとも……"

scene evh rin_h_right_close
with charachange


"琳は俺を解釈のしようのない目で見る。"



rin "こういうことなの？"


hi "……なんだって？"




rin "私はひとりぼっちにならなくてもいいんだって言ったよね"



scene evh rin_h_left_close
with charachange


"その目は純粋さとぼんやりとした混乱に満ちていて、俺は小さく笑うと、頭をなでてやる。"


hi "ああ、そういうことだな"



hi "雨に降られたときに頼れる人がいるってこと"




hi "それはつまり、お前は独りじゃないってことだよ"




hi "お前にそんな奴がいればの話だけどな"


scene evh rin_h_closed_close
with charachange



"琳がキスで答えると、俺たちは大した理由もなしに動きを止めていたことを思い出す。"



"俺たちは最初からやり直す。ほとんど２人同時に、お互いの動きをリズミカルに真似ながら。"



"俺はより速く動いて、琳に出入りする。汗が琳の汗と混ざりあい、繋がりあった肌がダイヤモンドと真珠のようにきらきらと光る。"


scene evh rin_h_strain:
    truecenter
    zoom 1.2 subpixel True
    easein 20.0 zoom 1.0
with charadistant


"琳ももっと速く動く。この欲望の王座で、俺に体をこすり付ける。"



"酔いしれるような琳の情欲の香り。俺たちの体を繋げる、心が空っぽになるような感覚。心からあらゆる理性が吸い上げられる感覚。"




"その全てが俺の意識を燃やし尽くす。身体の中の切実な気持ちが、俺の本能を焼くのと同じように。"




"その感覚が強まっていき、琳も止まる気配はない。"



"琳は俺の腰に足を回して、俺に肉体の限界まで奥に進ませようとする。１ミリ進むたびに波が背骨を駆け抜けていく。"




"白い輝きが世界を埋め尽くして何も見えなくなり、俺の意識はブラックアウトする。"


stop music fadeout 2.0
stop ambient fadeout 2.0

window hide

scene white
with Dissolve(2.0)

$ suppress_window_after_timeskip = True

with Pause(4.0)
label jp_R42:

window hide None

scene white
with None

$ renpy.music.set_volume(0.1, 0.0, channel="music")
play music music_timeskip fadein 4.0


centered_b "今{fast}" with Dissolve(4.0)



nb "『今』なんて、あやふやですぐに過ぎ去ってしまうものだ。\n"



extend "過去と未来の間にある瞬間？\n"




extend "そんな説明に大した意味はない。\n"





extend "無意味なことを深く考えすぎても時間の無駄だ。\n"




extend "だから今を生き抜くことはいつでも最高の選択というわけだ。\n"




extend "第一、未来を予測することもできず、過去も簡単に忘れてしまう俺たちにとって、今というのは唯一の存在の証明だ。\n"




extend "しばらくそのことを忘れていても、存在することには変わりはない。でもたまにはその一瞬を楽しむのもいいものだ。\n"









centered_alive_j "そうすれば……確かめられるんだ……{color=#fff}生きている、と。{/color}"







show alivetext_j "そうすれば……確かめられるんだ……{color=#fff}生きている、と。{/color}"
with None







show alivetext_j "そうすれば……確かめられるんだ……生きている、と。"





with Dissolve(3.0)

$ renpy.pause()

stop music fadeout 4.0

scene bg school_dormhisao
with Dissolve(4.0)

window show Dissolve(2.0)

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_dreamy fadein 4.0



"そこに立っている、半裸のまま俺の部屋から窓の外を眺めている女の子のほうが、俺よりもよほど『今』をよく理解しているに違いない。"





"俺はといえば……まあ、今のところ自分の状況にちょっと戸惑っている。琳の尻をじろじろ見るんじゃなくて、自分のシャツを探さないといけない。"




"それでも、琳を見るのをやめられない。"

scene bg misc_sky
show hisaowindow
show rinpan relaxed_nonchalant_close at center
with locationchange




"琳は窓ガラスにかじりついている。たぶんガラスに鼻の跡が残るだろう。"





"少なくとも、琳の吐息は跡を残している。雨で冷えた窓が曇っては晴れてを繰り返している。"




"服を着ようと足を引きずって歩いても、考えにふける琳の集中は乱れない。でもそれで構わない。前よりもこういう沈黙が気にならなくなった。"





"シャツのボタンを留め終えるころになって、琳が俺のほうを向かないまま口を開く。"


show rinpan relaxed_boredom_close
with charachange


rin "どっか行こうよ"


hi "どこにだ？"



"琳は窓枠じゃなくて俺を誘っているんだろう、と推測するしかない。でも多分そうだよな。"


show rinpan basic_lucid_close
with charachange


rin "わかってる"


hi "なんだって？"

show rinpan basic_deadpan_close
with charachange


rin "服着るの、手伝って"

show rinpan basic_awayabsent_close
with charachange


rin "今日がその日なんだ、きっと"

show rinpan basic_deadpanupset_close
with charachange


rin "早く、服"



"服、服って……なんてせっかちな声だ。"



"俺はしゃがみこんで、脱ぎ捨てられ、忘れられていた琳のブラを床から拾い上げる。"



"死んだ魚のように指の間にそれを挟むと、琳を脱がせるときに感じた、ぞっとするようなためらいにもう一度襲われる。"





"親密になることは、俺にとってこんなに手に負えないことなんだろうか？"


show rinpan basic_deadpancontemplation_close
with charachange



rin "ほら、脱がすときはすぐできたでしょ。それとおんなじだよ、反対なだけで。逆さにしゃべるようなものだよ"



show rinpan basic_deadpan_close
with charachange


rin "よだんたんかもで、どけだうそしかずむ"




"突然な、そして並外れた琳の頭の回転の速さに唖然として、その意味不明な言葉を逆に読み取るのを忘れてしまう。"





"もちろん練習したところで、あんなに滑らかに逆向き会話に切り替えられるとは思えない。"




hi "うーん、もう一回言ってくれないか？"


show rinpan basic_lucid_close
with charachange


rin "よだんたんかもで、どけだうそしかずむ"


"……"



hi "なるほど。わかった、じゃあやってみる"




"琳の言うとおりだった。留め具の構造は簡単で、３回目の挑戦で小さなプラスチックのフックがカチリとはまる。"



hi "よし"

show rinpan basic_deadpandelight_close
with charachange



rin "てしおなはぎつ"





hi "なに？　それやめてくれよ、俺は逆さ語は話せないんだ"



show rinpan basic_lucid_close
with charachange



"体の動きで逆さま思考を追い出すかのように、琳はかぶりを振る。"





"そういう能力があれば役に立ちそうな人には何人か心当たりがある。"


show rinpan relaxed_nonchalant_close
with charachange



rin "突っかかっちゃった。次は直して"





hi "直す？"


show rinpan basic_deadpan_close
with charachange



rin "そうだよ"




hi "いや、どういう意味かって聞いたんだ"


show rinpan basic_lucid_close
with charachange



rin "そりゃあ、その……きちんとなるように"




"きちんとってなんだよ？"



"……"



"その乳房がどうすれば『きちん』となるのかなんてさっぱりわからないので、俺は見当もつかないまま長々と琳の胸をまさぐり続けるはめになる。"





"もちろん俺は文句なんてないけど、琳は不満を言う。"



show rinpan basic_deadpanupset_close
with charachange


rin "笑美のほうが上手いや"



"確かに否定はできないけど、琳のじれったそうな声は俺をイライラさせる。さっきからなんだか妙に急いでいる感じだ。"




hi "そりゃ悪かったな。なんてったってあいつは{b}女の子{/b}で、実際気心が知れてるからだろ？"


show rinpan basic_deadpanamused_close
with charachange



rin "それはないと思う。君と同じくらいの胸しかないから"



"……"

stop music fadeout 5.0

hide rinpan
show rin basic_absent_close
with shorttimeskip



"やがて琳のブラと胸も『きちん』と収まると、残りの服を着せるのは割と簡単だ。"


hide rin
with charaexit



"まだシャツのボタンを全部留めきっていないのに、琳はドアに向かって突っ走る。"




"他になすすべもなく、俺も琳を追って走る。"


$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_soothing fadein 2.0
play ambient sfx_parkambience fadein 0.5

scene bg school_gardens
with locationskip



"森に続く裏口に向かっていることに気づいたとたん、琳が行きたがっている場所になんとなく見当がつく。その理由まではわからないけど。"





"とはいえ、琳に関する限り、自分の予想が『正解』に近いとはとても思えない。『正解』という言葉の定義にはかなり幅があるけど、それでもだ。"



$ renpy.music.set_volume(0.6, 0.5, channel="ambient")
$ renpy.music.set_volume(0.8, 0.5, channel="music")

scene bg school_forest1
with locationskip



"塀の向こうの森は雨の匂いがする。雨はしばらく前に止んでいるけど、最後の雨粒がまだ下生えから地面に向かって滴っている。"




"のんびりとした琳のペースに合わせて、俺たちはぶらぶらと歩く。おかげで落ち着いた雰囲気を受け止めることができる。"




"琳が少なくとも３本の木に、すれ違いざまに挨拶をするのが聞こえた気がする。でも俺は木々と同じようにそれを無視する。"



"予想通り、琳は丘の上に向かう細い脇道に俺を連れていく。"

scene bg worrytree:
    truecenter
    yalign 1.0
with locationchange



"俺は虹を探して、頭上の枝葉の隙間をのぞき見る。でも、どこにもなさそうだ。"




"いかにも虹が出そうな天気なのにな。太陽は低くなっているし、雨が止んでからそんなに時間も経っていない。"




"まあいいか。"


$ renpy.music.set_volume(0.7, 0.5, channel="ambient")
$ renpy.music.set_volume(0.6, 0.5, channel="music")

scene bg school_forest2
with locationchange



"俺は木のてっぺんから、バランスを崩さずゆっくりと丘を登る女の子の、やせた背中に視線を下げる。"




"俺の数歩先だけど、まだ手の届く距離だ。"




"虹に手が届くなんて絶対に無理だろうけど、琳になら……以前に比べたら、そこまで無理という気はしない。"


$ renpy.music.set_volume(1.0, 0.5, channel="ambient")
$ renpy.music.set_volume(0.4, 0.5, channel="music")

scene bg school_hilltop_border_summer
with locationchange




"開けた草地の上から俺たちを出迎える晴れ渡った空は広大で、美しい。"




"強い風が雨雲を集めて、街から遠くの山のほうへ追いやっている。"



"いい眺めだ、でも……"


"……"

stop music fadeout 6.0

show dandelionsbg thin
show dandelionsfg thin
with None




"小さな白のかけらが俺の視界の端を飛び去って行く。でも振り向いたときにはもうどこかに消えてしまう。"





"また飛んでくる。そして三つ目が。"




"気づいたときには、ほとんど目に見えない小さな白い房が至る所に飛んでいる。"


show rin basic_delight behind dandelionsfg at center
with charaenter



rin "見て、花が"




"ああ。そうか。"


$ renpy.music.set_volume(1.5, 0.5, channel="ambient")
$ renpy.music.set_volume(1.0, 0.0, channel="music")

scene bg school_hilltop_summer
show dandelionsbg dense
show dandelionsfg dense
with locationchange

play music music_comfort fadein 0.5


"以前来たときに辺り一面を覆っていたたんぽぽは、日にちが経って変わっていた。"


"明るい黄色だったのが、ふわふわとした白になっている。"


"そのうちのいくつかはすでに種を飛ばしているけど、ほとんどはまだ風が吹くのを待っている。"



"今日はその風がよく吹いていて、ときどき草を強く揺らすと、あたりはたんぽぽの種でいっぱいになる。"



"ひとつずつ、種は花の先を離れて宙へと舞い上がる。"


"よくあることだけど、琳はどういうわけか見とれている。"

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show rin negative_spaciness behind dandelionsfg at center
with charaenter


"琳はあちこちに頭を向けていて、種が飛び立つたびに、周囲の変化に驚嘆している。"


"俺も白い綿毛が風に乗って地平線に飛び立っていくのを見る。そしてそれが視界から消えた後も、その様を思い描ける。"


"……"

show rin basic_awayabsent
with charachange


rin "久夫"


hi "どうしたんだ？"

show rin basic_absent
with charachange


rin "私のこと、好き？"



"俺ははっとして、琳の突然の真面目な表情に向き合う。もう花を見てはいなかった。"




"いきなりそうやって聞かれると、難しい質問だな。"




"それでも、琳の率直な問いに、急いで答えなきゃという気持ちになる。"



hi "さあな。たぶん好きだよ"


"これじゃ急ぎすぎか。"

show rin basic_deadpannormal
with charachange


rin "それ、どういう意味？"


hi "……さあな"

show rin basic_lucid
with charachange




"琳はため息をつく。俺の煮え切らない答えが不満なんだろう。俺だってそう思う。"


show rin relaxed_nonchalant
with charachange


rin "私もなんだ"

show rin relaxed_boredom
with charachange



rin "好きになるってことがよくわからないんだ"



hi "……"



hi "……大丈夫だよ、そうだろ？"

show rin basic_lucid
with charachange



"はっきり答えるのをためらったのか、琳は肩をすくめる。『私にわかるわけないでしょ？』とでも言いたげだ。"





"琳は一瞬にしては長く黙り込んでしまうけど、それでも俺が後先を考えるには時間が足りなくて……"


show rin basic_absent
with charachange


rin "君のことが好きだよ"



"その３語が、ヘッドライトに見入っているウサギのように俺を硬直させる。でも俺はウサギじゃないし、俺が見入っているのは琳の目だ。それは自分が漏らした言葉に比べてあまりに無表情だった。"


show rin basic_deadpanupset
with charachange



"琳はとても真剣そうだ。すると舌を突き出して少し顔をしかめるので、俺はさっきの言葉以上に困惑する。"




"なんだか不満そうなのはどうしてだ？"



"胸のうちを打ち明けたつもりなのか、俺の反応を、あるいは自分の反応をうかがっているのか？"


show rin basic_awayabsent
with charachange


rin "変な味だね"


hi "……味？"

show rin basic_lucid
with charachange


rin "うん。へーんな味"



"琳は笑う。不安に駆られてなのか。俺としてはそう思いたいけど。でも琳はその奇妙な響きに気づいて、途中で止める。"


show rin negative_spaciness
with charachange



rin "ほら……なんて言えばいいんだろ……そういう言葉ってないと思う"




"自分の言葉の裏に何の意味もないかのように、琳はしゃべり続ける。さっき大事な言葉を形作った舌から、止まることなく軽はずみな言葉がこぼれる。"


show rin negative_worried
with charachange


rin "言葉……うーんとね……"


"ただ。"

show rin negative_annoyed
with charachange


rin "……なんていうか……"


"琳はその。"

show rin basic_deadpanupset
with charachange


rin "……"


"言葉を見つけられない。"


show rin basic_sad
with charachange


rin "……"


"琳は脳が急停止したかのように、言葉を詰まらせてただ俺を見ている。"



"ひどく混乱しているみたいだ。琳が説明してくれるのを待っている今の俺のように。"




"でも琳は何も言わず、ただ数回まばたきをするだけだ。揺らめく長いまつ毛が俺の気を引く。そこを除けば琳は固まっているように見える。"




"そして、俺は琳が戦っていたものの正体を悟る。"



show rin basic_crying
with charachange



"またあの奇妙な涙だ。悲しみも喜びも伴わない。不憫なすすり泣きでも、嬉しい笑いでもない。"




"ただひとりでにこぼれる、唐突な涙。以前琳が教室で見せたような涙。"



rin "ああ"



"たった数滴、騒ぎ立てるほどのものじゃない。だから琳は自分の涙に気づいてもそれを隠そうとしない。"




"琳は泣くけど、その理由は自分でもわかってなさそうだ。俺を見つめ返す潤んだ目を見ていると、どういうわけか胸の中に大きな不安が広がっていく。"




"状況のあまりの不可解さにショックを受けて、こっちまで固まってしまう。"




"もう何が起きているのか、俺には理解できない。"



hi "琳？　どうしたんだ？"


rin "私……"

show rin negative_crying
with charachange



"琳は困惑して頭を振る。なかなか言葉を発することができない。"


show rin basic_crying
with charachange


rin "ごめん……"


rin "君のことが怖くなってきちゃったよ"



"琳はゆっくりとつぶやく。自分の言っていることが信じられないというかのように小さな声だ。俺にも信じられない。"




hi "なんだそれ？　どうしてだ？"


show rin basic_sad
with charachange



rin "わかんない。そう言ったらそんな気持ちになったんだ"


show rin basic_absent
with charachange



rin "人って怖いときは泣くんでしょ？"


show rin basic_awayabsent
with charachange



rin "ね？　私も泣けるんだよ"






"琳は視線をそらして、わざと俺を見ないようにしている。その仕草も、今の言葉も、同じくらい俺を戸惑わせる。"




show rin negative_annoyed
with charachange



rin "私……私さ、君といると時々、すごく逃げ出したくなっちゃうんだけど、でも動けないんだ、足がレモンのパンナコッタになっちゃったみたいで、胸が破裂しそうで……"


show rin negative_sad
with charachange


"琳は意気消沈したように肩を落とす。"


rin "君にはそういうこと、あった？"





"……凍りついた森を覆う鉛色の空と、葉の落ちた枝ががさがさと擦れ合う音が思い浮かぶ。"





"まるで別の人生の記憶みたいだ。"



hi "ああ、一度な"



hi "俺もあのときは胸がすごく痛かったよ"


show rin basic_surprised
with charachange



rin "でもそれって人にはうつらないんじゃなかったの"




"俺は頭を振る。口元に少しだけ、作り気味の笑みが浮かぶ。"





"俺がかかっているもう一方の胸の病は、それこそ人にうつるものだろう。それなら大歓迎だ。"




hi "なにを怖がってるんだ？　俺は自分が怖いやつだなんて思ったこと一度もないぞ"


show rin negative_confused
with charachange




"心の中のもつれはそんなことでは解けないとわかっているみたいに、琳は必死に頭を振る。"





rin "君といると、私以外の誰かにならなきゃって気持ちになるんだ"


show rin negative_sad
with charachange


rin "これって怖いことだよ"

show rin negative_worried
with charachange



rin "君が優しくしてくれるたびにそう思うんだ。昨日みたいに"




rin "そういうとき、どうすればいいか全然分かんないんだ。大変なんだよ"




"琳のかすかな声がかろうじて聞こえる。そのささやきは、口に出すどころか考えるだけでも恥ずかしすぎることの告白だ。"




"琳は恥ずかしがるようなタイプじゃないから言葉に出したんだ。本能に従うかのように怖々とではあったけど。"


show rin basic_upset
with charachange



rin "でもどうにかしたいんだ。でもこの私にできるかわからないんだ"




"少しの間、俺たちはお互いに何か言い出すのを待っているかのように見つめあう。"



"……"

hide rin
show rin basic_upset_close as rin2
with characlose



hi "ほんとに馬鹿だな"


hide rin2
show rin relaxed_surprised_superclose at center
with characlose



"琳の唇は塩っぽくて、俺に怯えている。"


window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.4)

window show


"琳を抱き寄せると、心臓が痛いほど高鳴る。"

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.4)

$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

nvl clear
nvl show dissolve



n "\n\n琳がそんなことを言える、ということが嬉しくはあるけど、やっぱり俺は悲しくなる。"




n "琳の精神、情熱、強さ。みんな俺が愛しいと思っているもの、そして変わって欲しくないと思っているものだ。"




n "それをどう受け止めればいい？　どこに向かっていくのか？　その未来は俺の未来と決定的に違うのか？"




n "そんな不安が俺の心臓から離れることは決してないだろうけど、それを受け入れて生きていくことはできると思う。"



n "ゆっくりと心臓の痛みは消えていき、琳の鼓動と同じ速さになる。"



n "\n\n俺たちはしばらくの間、それに耳を傾ける。"



n "……"

$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
stop music fadeout 8.0

nvl hide dissolve
nvl clear

hide rin2
show rin basic_blush_close behind dandelionsfg at center
with charadistant

window show



"唇が離れると、もう話をしてもいいんだと気づくまでにしばらく時間がかかる。"



"……"

show rin basic_sad_close
with charachange



rin "ほらね？"


show rin relaxed_doubt_close
with charachange


rin "君ってほんとうに優しいよ。そうでないときでもね"


rin "それがいちばん怖いんだ"

show rin relaxed_sleepy_close
with charachange



rin "私……ずっと君の優しさだけが怖かったんだと思う"



"……"




hi "なにがまずいんだ？　怖くたって"



show rin basic_lucid_close
with charachange



"琳は難しい数学の問題でも解くかのように眉間にしわを寄せて、しばらく考え込む。"


show rin basic_deadpanamused_close
with charachange


rin "ううん。もう大丈夫。君なら平気"



"重しが胸から外れたかのように、琳の言葉が俺の心臓を高鳴らせる。俺の心を満たすのは……なんだろう、幸せか？"



"他になにがあるっていうんだ？"



"今の俺の笑顔は本物だ。"


hide rin
show rin basic_deadpanamused as rin2 behind dandelionsfg
with charadistant



"俺と同じように、優しく微笑み返しながら、琳は後ろに下がる。"


show dandelion full:
    alpha 0.0 xalign 0.5 yanchor 1.0 ypos 1.2 subpixel True
    easein 1.0 ypos 1.0 alpha 1.0
with None
show dandelionbg behind dandelion
show dandelions_blurbg behind dandelion
show dandelions_blurfg behind dandelion
hide dandelionsfg
hide dandelionsbg
with Dissolve(1.0)

hide rin2
show rin basic_deadpanamused behind dandelionbg
with None



"琳が肩で顔をぬぐうあいだ、俺は丸くふっくらとした綿毛坊主を拾い上げ、口元に持ってくる。"



show dandelion gone
with Dissolve(1.0)


"ふうぅ……"


"綿毛が風のなかに広がって、新たな場所へと運ばれていく。"


"つい２、３週間前、あれは全然違う姿だったのに。"


"これが変わるってことか。"


"……"

show dandelion gone:
    easeout 1.0 alpha 0.0 yanchor 1.0 ypos 1.2
with None

hide dandelionbg
hide dandelions_blurbg
hide dandelions_blurfg
show dandelionsbg dense behind rin
show dandelionsfg dense
with Dissolve(1.0)



hi "なあ、あの花はあるべき姿に変わっていったんだな。お前がこの前言ったみたいに"





hi "お前はどうだ？　本当の芸術家になれたのか？　それともなれなかったのか？　逃げ出しちまったせいで"



show rin basic_deadpancontemplation
with charachange


"琳はしばらく固まって考え込むと……"

show rin relaxed_nonchalant
with charachange


"……肩をすくめる。"


"それを見て俺は笑ってしまう。"




"琳の気楽で落ち着いたしぐさが愛おしい。そうしたいと思えば、琳は言葉通り、本当に、何の遠慮もなく、その肩にかかる全世界の重みを捨て去ることができるんだ。"





"琳は、ありうる全ての意味で、そしてありえないいくつかの意味でも……自由だ。"




"だからこそ、俺は琳を愛しているんだろう。"


show rin basic_absent
with charachange



rin "どうでもいいと思うな"


show rin basic_deadpandelight
with charachange



rin "今日は雲でも見てようよ"


play music music_twinkle fadein 2.0

scene ev rin_goodend_1
show evbg rin_goodend_base:
    center
    subpixel True xalign 0.0
    1.0
    easein 20.0 xalign 1.0
show dandelionsbg dense
show rin goodend_1:
    center
    subpixel True xalign -0.5
    1.0
    easein 20.0 xalign 1.0
show dandelionsfg dense
show evfg rin_goodend:
    center
    subpixel True xalign -1.0
    1.0
    easein 20.0 xalign 1.0
with whiteout



"琳は５歩進んで大きな岩の上に登り、つま先立ちする。そこがこの原っぱで一番高い場所だ。"




"雲をつかもうとするなら、１センチでもおろそかにはできないから。"




hi "そうだな、雲を見よう。時には本当にしたいことをするってのもいいよな"




rin "うん。そうだろうね"





"頭上高くに広がる青い空を見上げる。"





"深い、紺碧の広大な空が視界いっぱいに、そしてその向こうまで伸びている。"




"でも琳はまだ岩の上にいて、地平線の彼方で雨雲が遠ざかっていくのを見つめている。"



rin "私、決めたんだ"



"琳の夢見心地の声が、風に乗って俺の耳に届く。口調からは決意を感じないけど、その言葉の意味は決意に満ちている。"



rin "結局、私でいるのがいいんだね"

$ renpy.music.set_volume(0.5, 1.0, channel="music")
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

window hide
nvl clear
nvl show dissolve


n "\n\n\nいいだって？　琳の決めることはいつもこう……型破りだ。"



n "まあ、それに気づくのは大切なことなんだろう。"




n "自分自身と折り合いをつけて、自分を受け入れる。自分のありかたを良いと思う。"




n "単純な気の持ちようだけど、それができないとはいかなくても、ひどく苦労する人もいる。"




n "俺もそんな人間の一人かもしれない、ということは十分わかってる。"



n "琳もだ……"



n "結局俺たちはそんなに違わなかったのかもしれない。"





n "他の人を受け入れるためには、まず自分自身を受け入れないといけないのかもしれない。"



n "それが俺たちもまだ踏み出せていない、必要なステップなのかもしれない。"


$ renpy.music.set_volume(1.0, 1.0, channel="music")
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

nvl hide dissolve
nvl clear
window show



"岩の上に立つ琳を見て、琳なら探しているものを見つけられると確信する。"




"そして俺も。"


show ev rin_goodend_1b
show evbg rin_goodend_base:
    subpixel False xalign 1.0
show rin goodend_1b:
    subpixel False xalign 1.0
show evfg rin_goodend:
    subpixel False xalign 1.0
with charachange



"風が琳の髪と服をとらえる。琳は短い腕を広げて、とても小さな、でも琳にとってはこれ以上ないくらい大きな抱擁をする。"




"一瞬、琳が空へと飛びだすかのように見えた。琳をこちらに引っ張り戻そうと、その肩に手を伸ばしそうになる自分を抑えないといけなかった。"




"でも、この光景は見ていることしかできないもの、記憶にとどめるべきものだ。"




"琳の袖が風に吹かれて気ままにはためき、髪もひどく乱れている。沈みゆく太陽がその肌に触れる。"




"俺がいつのまにか大好きになった、琳のなだらかな姿が、冷たい風に吹かれて震えている。風は白い小片を運び、その一つ一つがやがて新しい花を咲かせる。"



"すべてが心に深く刻み込まれる。"



"風の中に散らばっていく小さな種のように、きっと琳も自分の中に世界を作ったりせず、この世界のどこかに居場所を見いだすことができるはずだ。"






"琳もそう信じているんだろうな。天に少しでも近づけるように立って、世界を強く抱きしめている。"




"世界全体が本当にそこに収まってしまいそうに見える。その小さな腕のあいだに。その全てを包み込むような抱擁に。"


show ev rin_goodend_2
show rin goodend_2
with charachange


rin "久夫？"



"琳は気楽そうに、振り向いて俺を見つめ、そして名前を呼ぶ。その声にも視線にも同じように、奇妙な喜びが宿っている。"



show evbg rin_goodend_base:
    subpixel True yalign 0.0
    acdc_warp 12.0 zoom 1.15
show rin goodend_2_hires:
    subpixel True yalign 0.0 xalign 1.0 zoom 0.769
    acdc_warp 12.0 zoom 1.0
    subpixel False
show evfg rin_goodend:
    subpixel True yalign 0.0
    acdc_warp 12.0 zoom 1.45
with None



"赤褐色の髪の下で好奇心いっぱいに輝いている、謎めいた濃緑色の目を見つめる。"




"とはいえ、俺からは遠すぎて実際に見えるわけじゃない。きっと俺の想像が反映しているんだろう。"



hi "どうしたんだ？"



rin "この世界の何もかもがうまくいってるって心の中で感じてるときのこと、なんて言ったらいいのかな？"


stop music fadeout 4.0
stop ambient fadeout 4.0

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
