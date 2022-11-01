


label jp_NOP1:
window hide None

scene black
with None

scene bg op_snowywoods
show snow
with Dissolve(2.0)

window show

play music music_serene fadein 2.0


"そよ風が吹き、頭上の葉の落ちた木々が、木製のウインドベルのようにざわつく。"


"教師や生徒の目に付きにくいこの場所は、夏になると落葉樹の林が美しい緑の屋根を形作る。カップルには人気の隠れ場所だ。"


"でも今のような真冬では、緑どころか薪の下に立っているような気分になる。"


"この寒さでかじかんでしまわないよう、丸めた手に息を吐いてから激しく手をこする。"


hi "いつまで待ってればいいんだ？　手紙には午後４時って書いてあったはずだけど"


"そう、この手紙……知らないうちに、俺の数学の教科書に挟まれていたんだ。"


"俺としては、下駄箱の中に手紙が入っている、みたいなほうが好みだった。でもこれはこれで、少なくとも相手が積極的だってことはわかる。"


"手紙の真意について思いを巡らせているうちに、雪は徐々に強くなっていく。"


"白く塗りつぶされた空から、雪のかけらが静かに降り続ける。この静止した世界の中で、時の流れを示すものは他にない。"


"凍りついた森にゆっくりと降り積もる雪を見ていると、時間の流れも遅くなったような気がしてくる。"

play sound sfx_rustling


"乾いた雪の上を歩く、さらさらという足音が静かな空気を乱し、俺は驚く。誰かが後ろから近づいてくる。"


mystery "こんにちは……久夫くん？　来てくれたの？"


"ためらいがちな、かろうじて聞き取れる問い。"


"それでも、俺はその繊細な声が誰のものかすぐに気づく。"


"心臓の鼓動が一回飛んだような気がした。"


"何百回も聞いたことがある声。でもそれは、他人との話を脇から聞いていただけでしかなかった。"


"俺は振り返り、夢見ていたその声に向き合う。胸の鼓動が速まっていく……"

window hide

$ ksgallery_unlock("evul other_iwanako")
scene ev other_iwanako_start
show snow
with GenericWhiteout(0.5,0.0,5.0)

window show


hi "岩魚子？　ここで待ってろって手紙……お前だったのか？"


"ちくしょう。昼からずっとうまい台詞を考えてたのに、その結果がこれかよ。"


"ダサすぎる。"




"岩魚子" "んん……そう。友達に渡してって頼んだの……受け取ってくれてよかった"


"そのはにかんだ、嬉しそうな微笑みに俺はひどく緊張し、指一本動かすことさえできない。"

stop music fadeout 10.0

window hide

scene bg op_snowywoods
show snow
with GenericWhiteout(0.5,0.0,2.0)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

with Pause(0.7)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.7)

window show


"心臓が暴れ始めている。この胸を突き破って彼女を食ってしまおうとしているかのように。"

window hide

scene ev other_iwanako
show snow
with GenericWhiteout(0.5,0.0,3.0)

window show


hi "それで……えっと……寒い中で、こうしているわけだけど……"


"また風が木々を揺らす。その不協和音も耳に心地よい。"


"突然の風に、岩魚子がわずかにたじろぐ。"


"風がやむと、どこからか得た信念に支えられたかのように、岩魚子は姿勢を正す。"


"岩魚子の目が俺の目をとらえる。その長い黒髪をのろのろと指で巻く。"


"その間ずっと、気がかりな心臓の鼓動はどんどん激しくなっていく。"

window hide

scene bg op_snowywoods
show snow
with GenericWhiteout(0.5,0.0,2.0)

window show


"のどが苦しい。しゃべろうと思っても言葉が出てこない。"




"岩魚子" "あのね……"

window hide

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.4)

window show




"岩魚子" "……わたしと……"

stop music fadeout 0.5

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




"岩魚子" "……つきあってくれるかなって……"


"俺は身動きもせず、立ちつくす。心臓だけが激しく脈打ち続けている。"


"返事をしたいのに、声帯がちぎれそうなほど引っ張られているような感じがして、声が出せない。"

play music music_tragic fadein 0.05




"岩魚子" "……久夫くん？"


"のどをさすろうと腕を伸ばしたとたん、目がくらむような痛みが腕に走る。"




"岩魚子" "久夫くん？！"

window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

window show


"全身が凍り付く。俺は恐怖で目を見開く。"

window hide

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

with Pause(0.15)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

play sound sfx_heartfast
show heartattack alpha
with Dissolve (0.1)

hide heartattack alpha
with Dissolve (0.8)

with Pause(0.05)

play sound sfx_heartstop
show heartattack alpha
with Dissolve (0.1)

stop music fadeout 0.3

show heartattack residual
with Dissolve (0.8)

window show




"岩魚子" "久夫くん！"


"胸の鼓動が突然止まり、ひざの力が抜ける。"

window hide

show passoutOP1
with None

nvl show Dissolve(0.2)


n "俺のまわりの世界――葉の落ちた木々の天蓋、どんよりとした冬空、俺に駆け寄ってくる岩魚子――すべてが黒く塗りつぶされる。"


n "意識を失う前に覚えていたのは、助けを呼ぶ岩魚子の叫び声と、いつまでもざわざわと鳴り続ける、頭上の木々の音だけ……"

nvl hide Dissolve(3.0)

nvl clear

with Pause (1.0)

scene black
with None


label jp_NOP2:

window hide None

scene black
with None

centered "あの心臓発作から４ヶ月が経った。" with dissolve

scene bg hosp_room
show sakura
show hospitalmask
with Dissolve (1.5)

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_rain fadein 4.0

nvl show dissolve


n "その間に付き添いなしでこの病室を出た回数は、たぶん片手で数えられるだろう。"


n "一人で考えるための時間としては、４ヶ月はかなり長い。そんなわけで、自分の状況を受け入れるための時間はたっぷりあった。"


n "不整脈。"


n "妙な言葉だ。耳慣れない、知らない言葉。お近づきにはなりたくない言葉。"


n "まれに起きる病気で、心臓の動きが不規則になり、ときには鼓動が極端に速くなる。場合によっては致命的だ。"


n "どうやら俺はずっと前からこの病気にかかっていたらしい。今まで何の問題もなく過ごせていたのは奇跡的だ、と言われた。"


n "本当に奇跡なのか？　俺を励ますつもりで言ったのだろう。生きていることにもっと感謝しなさい、と。"


n "だからって喜ぶ気には全然なれなかった。"

nvl clear


n "両親は俺よりもショックだった、と思う。二重に痛手を受けたようなものだった。"


n "俺は丸一日かけてすべてを飲み込むことができていた。でも親にとっては突然のことだ。病気を治すために家を売る覚悟までしていた。"


n "もちろん、不整脈は治らない。"

nvl clear


n "この……容体、の発見が遅れたせいで、俺は回復のために入院治療を受けなくてはいけなかった。"


n "最初に入院したとき、みんな寂しがってくれていると思った……"


n "最初の一週間ほどは、俺の病室は花と風船と手紙でいっぱいだった。"


n "でも見舞いに来る人はすぐにいなくなり、見舞いの品もやがて届かなくなった。"


n "こんなにカードや花が届いたのは、俺にお見舞いを送ろうという動きがクラスの活動になったからだ、と気づいたのはその時だった。"


n "本気で心配してくれていた人もいたかもしれないけど、怪しいもんだ。最初だってお見舞いに来る人はほとんどいなかった。一ヶ月目が過ぎるころには、定期的にやってくるのは両親だけになっていた。"


n "最後までお見舞いに来てくれたのは岩魚子だった。"


n "六週間たった後、岩魚子ともう二度と会うことはなかった。お見舞いに来てくれたときも、大して話はしなかったけど。"


n "あの雪の日に、二人の間で起きたことには二度と触れなかった。"

nvl clear


n "病院？"


n "好きこのんで住みたい場所じゃない。"


n "医者も看護師も人間味がないし、個性もない。"


n "みんな忙しいし、山ほど他の患者を抱えているからだろうけど、でも俺には不愉快だ。"


n "最初の一ヶ月くらい、心臓内科の主治医に会うたびに、だいたいいつごろになったら退院できるのかと質問した。"


n "単刀直入な答えが返ってくることは決してなく、治療と手術がうまくいくか様子を見よう、と言うだけだった。"


n "胸に残った手術の傷跡がゆっくりと、時とともに姿を変えていくのを、俺はぼんやりと観察して過ごした。それは何かの前兆のように見えた。"


n "主治医には今でも退院のことを尋ねているけど、今では答えがなくてもがっかりすることはなくなった。どうせもう期待もしていない。話をのらりくらりとかわしているということは、まだ希望はあるってことだ。"

nvl clear


n "ある時から、テレビを見るのをやめた。理由はわからない。ただなんとなくだった。"


n "現実逃避の手段としては、今の俺には合わなかったのかもしれない。"


n "そのかわりに読書を始めた。病院には小さな『図書館』があった。といっても書庫みたいなものだけど。俺はそこにあった本を読み進めていった。"


n "数冊ずつ本を借り、全部読み終わったら、次を借りに行った。"
n "俺は自分が読書好きだということを知った。中毒と言っていいくらいだ。手元に本がないと、自分が裸でいるような気分になり始めていた。"


n "それでも物語は大好きだった。"

nvl clear


n "それが俺の日々の暮らしだった。"


n "一日一日の区別がどんどんつけにくくなった。違いといえばその日に読んでいた本と、外の天気しかなかった。時間というものが何かどろどろした物質に変化して、自分がその中で身動きできずに閉じこめられてしまったような感じがした。"


n "気づいたときには一週間経っていた、なんてこともあった。"


n "ときどき、今日が何曜日かわからないことに気づいて、ショックで固まることもあった。"

n "でもそれ以外のときには、周りを取り囲むあらゆるものが、無関心という俺自身が作り上げた壁を破り、俺の心に突き刺さる。"

n "本のページが鋭く、やけどしそうなほど熱く感じられるようになる。胸の重さが耐えがたくなる。そうなると本をどけて、しばらくただ横になるしかない。今にも泣き出すかのように、天井を見上げながら。"


n "でも、そんなことはめったに起きなかった。"


n "そもそも泣くことさえできなかった。"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl hide dissolve

nvl clear

window show


"今日は医師がやってきてほほえんだ。興奮しているようだけど、それほどじゃない。まるで俺のかわりにいい気分になろうとしているみたいだ。"


"両親もいる。最後に会ってから数日経っていた。二人ともなんだかいい服を着ている。何か特別なことでもあるのか？　パーティじゃないんだぞ。"


"この主治医は、いつもこんな儀式をする。まず時間をかけて書類を整理したあと、それを脇にどける。まるで自分の行為の無意味さをわざわざ強調するかのように。"


"そして俺の隣のベッドの端にさりげなく座る。しばらく俺の目を見つめる。"




"医師" "こんにちは、久夫くん。気分はどうだい？"


"俺は答えないかわりに、少しだけ笑みを返す。"




"医師" "君はもう家に戻れると思う。君の心臓は以前よりも元気になったし、気をつけていれば全く問題ない"




"医師" "君の薬はすべてまとめてある。処方箋はお父さんに渡しておくよ"


"父" "こんなに多いんですか……"

"医師は一枚の紙を父さんに渡す。それを一読して、表情が木のように固まる。"


"父さんの手から紙を取って目を通す。体が麻痺するような感覚。こんなとき、どんな反応をすればいいんだ？"

$ renpy.music.set_volume(0.5, 2.0, channel="music")

scene white
with Dissolve(2.0)

show wallodrugs:
    xalign 0.0 subpixel True
    easein 25.0 xalign 1.0



"不条理なまでに長い薬のリストが俺をじろりと見つめ返す。こんなの無理だ。すべてが文字の海に混ざり合う。"


"正気の沙汰じゃない。"


"副作用、有害作用、禁忌、投薬量が、冷酷なまでの正確さでずらずらと並んでいる。"


"読もうとする。でもあまりにも無意味だ。"


"一言たりとも理解できない。理解しようとしても気分が余計に悪くなるだけだ。"


"これを全部……これから一生、毎日？"

$ renpy.music.set_volume(1.0, 1.0, channel="music")

scene bg hosp_room
show sakura
show hospitalmask
with fade




"医師" "残念だけど、これでも最善を尽くしたんだ"




"医師" "ただ、新しい薬品は常に開発されているから、何年かすればリストの数は減ってもおかしくはないよ"


"何年か……それで気休めのつもりなのか？　黙っていてくれた方がまだ気分が良かった……"




"医師" "それと、これはご両親とも話したんだが、君は前の学校には戻らない方がいいと思っている"


"なんだって！？"




"父" "いいから落ち着け、久夫。先生の話を聞くんだ……"


"落ち着けだって？　その言い方、俺が気に入らないってわかってるのが見え見えだ。在宅学習でもするっていうのか？"


"俺の見せた不安がどうあれ、それは無視された。"




"医師" "君の教育が最も重要だということはみんな理解している。ただ、適切な監督がないのはまずい、と私は思っているんだ"




"医師" "少なくとも、君への投薬が適切だとはっきりするまではね"




"医師" "それで、君のご両親に転校についてご相談した"




"医師" "山久学園という学校がある。障害を持つ生徒の教育を専門にした学校だ"


"障害？　なんだって？　俺は……"




"医師" "学内には看護スタッフが２４時間待機している。評判のいい総合病院もすぐ近くにある。生徒の大半はキャンパス内で暮らしている"




"医師" "一種の全寮制学校と考えればいい。ここには生徒がある程度独立できるような仕組みがある。いつでも手助けが得られる中でね"


"独立だと？　障害児の学校じゃないか。事実をごまかすなよ。"


"そこまで『自由』だっていうなら、２４時間の看護スタッフなんているわけがないし、近くに病院があることが売りになったりするもんか。"




"父" "もちろん、お前が行く気になればの話だ。ただ……母さんも父さんも、家でお前に勉強を教えることはできそうにない"




"父" "何週間か前に、母さんと下見に行ってきた。お前も気に入ると思うよ"


"どうやら選択の余地はなさそうだ。"




"医師" "他の心臓病の患者に比べて、君のような症状の患者は長生きすることが多いんだ。いつかは君も仕事につかなくてはいけないし、これは君の教育を続けるいいチャンスだよ"


"これがチャンスなもんか。チャンスなんて言うな。チャンスだなんて、ふざけるな。"




"医師" "さて、学校に戻れるとわかって嬉しくはないかい？　いつだったか、学校に戻りたいって言っていたよね。同じ学校ではないけど……"


"特殊学校だ。そんなの……"


"侮辱だ。そう言いたかった。俺は格下げされたんだ。"




"父" "お前が思ってるのとは違う。あそこの生徒はみんなとても生き生きとしているぞ。人それぞれに"




"父" "この学校は、まだ自分の人生を生きて、学んでいける生徒に合わせて作られているんだ。ほんの少し、なんらかの手助けが必要だというだけの話だ"




"医師" "お父さんの言うとおりだ。それに、この学校の卒業生でめざましい活躍をしている人はたくさんいる。障害があるからといって気後れする必要は全くないんだ"




"医師" "別の病院にいる私の同僚も、そこの卒業生だよ"


"そんなこと知るか。障害があるから気後れしなくていい？　障害ってのはそういうものじゃないのか。"


"こんな大事なことが勝手に決められていたのが、本当に腹が立った。でも俺に何ができる？　『普通の』生活なんてとっくに問題外だった。"

stop music fadeout 10.0


"変な話だ。俺の人生はなんだかつまらないってずっと思ってきたのに、今となってはそれが恋しくてたまらない。"


"文句を言いたい。ショックや疲れのせいで反応できないのだ、と思いたい。今なら大声でわめくことだって簡単にできるだろう。どうにかして元の学校に戻せと。でも、そうはしない。"


"俺は何も言わない。もう意味がないってことはわかってるんだ。"


"俺は何もかもにひどく疲れて、部屋を見回す。この病院、医師たち、俺の病状、何もかも。今の気分を変えてくれるようなものは一つもない。"


"もう選択の余地はないんだ。それはわかっている。でも障害者学校に行くと思うと……いったいどんなところなんだ？　前向きに考えようといくら努力しても、さっぱりうまくいかない。"


"でもやってみよう。"


"再デビューってのは悪くないな。"


"それくらいしか思いつかない。でも少なくとも何かはある。仮に特殊学校だとしても、何かはある。まっさらからのスタートだ。"
"俺の人生はまだ終わっちゃいない。あきらめてそんな考えに身を任せるのは間違ってる。"


"最低でも、俺の新しい人生がどうなるのかは見届けることにしよう。"

window hide




label jp_A1:

window hide None

scene bg school_gate
with Dissolve(3.0)

play music music_happiness

window show


"ひどく気取った校門だった。"


"ふつう門というのはそういうものだけど、これはやりすぎだ。"


"赤レンガ、黒い鍛鉄と灰色のしっくいでできた門からは、歓迎という気持ちがまるで感じられない。"


"学校の門というのはこうあるべきものなのだろうか、と考えてみるけど、正直わからない。たぶん違う気がする。"


"もちろん、いつまでも門のことを考えていても仕方ないので、足早に中に入った。驚くほど気分がよかった。"


"前に進むのは気分がいいものだ。"

scene bg school_courtyard
with locationchange


"歩をゆるめず、山久学園の本校舎へと向かう。両親は荷物を寮に運び込んでいるので、今は一人きりだ。中には俺を待っている人がいるはずだった。"


"敷地の中は大いに草木が茂り、緑にあふれていた。"


"校内の様子は学校というより、むしろ公園のようだ。木々や刈りたての草の匂い、その他もろもろの公園っぽいものの間を、清潔感のある遊歩道が通り抜けていく。"


"『清潔』とか『衛生的』なんて言葉が頭の中に浮かび上がり、俺は身震いする。"


"そんな思考を振り払う。今は心を開くんだ。お前の新しい人生だぞ。ありのままを受け入れなきゃだめだ。"


"そう自分に言い聞かせる。"


"葉の生い茂った木々のむこうにいくつか大きな建物が並んでいる。ただの学校にしては大きすぎるし、多すぎる。"


"なにもかもがずれている感じだ。俺の思っている学校と、この場所は全然かみ合わない。"


"これは『不気味の谷』だ。これが新しい学校だと聞かされてはいたけど、頭の中ではそうは思えないんだ。"


"この気持ちは心底からのものなのか、それとも障害者の学校というものへの先入観のせいなんだろうか。"


"そういえば、中に入ってから一人も人を見かけない。なんだか気味が悪いな。"


"誰かここにいてくれたら、と思う。異次元に迷い込んでしまったような気分にならずに、もっと確かなものに自分をつなぎ止めることができるのに。"


"木々が風に合わせてうなり、あたり一面にきらめく緑の色彩が俺の目を引く。"


"その光景がまた病院のことを思い起こさせる。緑は気持ちを落ち着かせる色だから、手術室の中は緑色で塗られているんだ、って。"


"じゃあどうしてたくさんの緑に囲まれてるのに、俺はこんなに不安なんだ？"


"……"


"きざったらしい造りの本校舎の前に立ったその時、俺はあの門が気に食わなかった理由にやっと気づき、動揺する。"


"あれは俺が引き返す最後のチャンスだったんだ。戻るような生活なんてどこにもなかったとしても。"


"いずれにしても、あの門をくぐってしまった今、もう絶対に戻ることはできなくなった。"


"弱気になり、頭の中でそれを意識しながら、正面のドアを開く。"

scene bg school_lobby
with locationchange


"中に入ると、姿勢の悪い、背の高い人が俺に気づく。ロビーには俺たちしかいないので、当たり前だけど。"

show muto normal at center
with charaenter


mu_ "君が……に……な……仁木君だな？"


hi "中井です"

show muto smile
with charachange


mu_ "そうだったな。よろしい。君の担任で理科を担当している、武藤だ"


mu "ようこそ"


"固くもゆるくもない握手を交わすと、先生は時計に目を落とす。"

show muto irritated
with charachange


mu "看護師長が簡単な入寮時検診をするから来るようにと言っていたが、今は時間がない"


hi "後で行けばいいですか？"

show muto normal
with charachange


mu "そうだな。午後でも問題なかろう。君をクラスのみんなに紹介しないといかん。もう全員待っているしな"


"待ってるだって？　他人の注目の的になるのはあまり好きじゃないけど、こういう状況じゃ仕方ないか。"


"何が待ち受けているのかわからない、ってのは本当に心細くなる。"


"そんなことを考えていたら、先生の言っていることを聞きそびれそうになる。"

label jp_choiceA1:
menu:
    with menueffect
    mu "クラスに自己紹介はするか？"
    "どうしてですか？":





        return m1
    "はい、もちろん":


        return m2

label jp_A1a:


hi "どうしてですか？　しないとダメですか？"


mu "もちろんそんなことはない。だから聞いたんだ"


hi "はい"


mu "では行こうか"



label jp_A1b:


hi "はい、もちろん。ていうか、普通しませんか？"


mu "普通はそうだ。だが他人の注目の的になりたくない子もいるからな"


"たぶん俺もそういうタイプだ。でも自分の第一印象は自分から与えるべきだ、と思う。"


hi "確かにそうですけど。でも大丈夫です"


mu "では行こうか"



label jp_A1c:

scene bg school_staircase2
with locationchange


"先生に続いて階段を上がっていくと、胸の動悸が激しくなっていく。自分の病気のことを考えずにはいられない。"

scene bg school_hallway3
show muto normal at center
with locationchange


"３階の廊下の、３つ目のドアに３－３と書いてある。"

play sound sfx_dooropen


"武藤先生がドアを開け、中に入る。"

show muto normal at Alphaout(0.5), Slide(0.5,0.5,0.4,0.5,0.5,_ease_out_time_warp)
with Pause (0.5)

hide muto
with None


mu "みんなおはよう。また遅れてすまない"

stop music fadeout 2.0


"俺はドアの前で一瞬ためらい、その場に立ちつくす。"





label jp_A2:

scene bg school_hallway3
with None


"ああもう、落ち着けよ！　大きな一歩だって、そんなことはわかってる……でもこんなに早くから心配したって仕方ないだろ。"

scene ev hisao_class_start
with fade

play music music_normal fadein 0.5


"俺は先生の後を追って教室に入り、中を見渡す。新しいクラスメイトの興味津々の視線に目を合わせないため、でもあった。"


"とても広い部屋だ。天井はやけに高いし、机と壁、机同士の隙間にもゆとりがある。"




"壁の一面には黒板がかかっている。古めかしい高窓が、よけいにその大きさを強調している。"


"生徒の机は下に本を入れる棚のついた、よくある木製の机。いすは金属のフレームと木でできている。単純で能率的だ。"


"俺は教室の正面で足を止めて、他の生徒に向き合う。みんなどこの学校にもいそうな、普通の生徒に見える。でもそれじゃあ、どうしてこんなところにいるんだろう？"

scene ev hisao_class_move
with None


"たぶん俺と同じように、どこか悪いところがあるんだろう。一目見ただけではわからないってだけで。そう考えてから、一人の女子の右手に親指がないことに気づいて少し動揺する。"


"自分のことを話している人には自然と耳を傾けるものだけど、先生がクラスに俺のことを紹介している途中で意識が離れてしまう。"


"黒い髪がちらっと見えて、自分が見られていることに気づく。とても長いストレートの髪が目立つ女の子。俺が見返しているのにその子は気づいて、手で自分の顔を覆う。"
"そうすれば自分の姿が目に見えなくなる、と言わんばかりに。"


"教室の後ろに、杖をロッカーに立てかけている男子がいる。この年で杖、というのは変な感じだ。"


"別の女子はなんだか変な風に手を動かしている。手話か？　その子は眼鏡の枠越しに俺をじっと見ると、また手を動かし始める。"


"あの子、なんかかわいいな。その隣に座っている、陽気そうなピンク色の髪の子も。あれを見逃す人はまずいないだろう。どうして教室に入ったときに気づかなかったんだ……"


mu "……新しいクラスメイトだ。温かく迎えてやってくれ"


"先生が手を叩くと、みんなもそれにならう。最前列にいる、片手がない女子を除いて。少し身がすくむけど、身に余る拍手へのお礼にお辞儀をしてそれを隠す。"


label jp_A2a:


"拍手が終わると、短い沈黙が落ちる。口を開いて沈黙を破ろうとする人は誰もいないようだ。"


"自分が何か言わないといけないと悟って、先生が口を開く。ぶつぶつとよく聞き取れないつぶやきの後、勢いを失ってまた黙り込み、俺の紹介をし始める。"


"みんな大して興味はなさそうだ。"


"自分で自己紹介する、と言っておくべきだったのかもしれない。"


"俺について何も知らないことに思い至ったのか、先生はまた俺の名前を言い間違えて、黒板に名前を書くよう俺に指図する。"


"その通りに名前を書いて、気まずい思いのままクラスの皆に向き直る。"


label jp_A2b:


"クラス全員の沈黙が、お前が話す番だと俺に促す。"


hi "ええと……中井久夫です"


"で？"


hi "趣味は読書とサッカー。転校生ですけど、みんなと仲良くやっていきたいです"


"それで？"


"こんなつまらない自己紹介があるかよ。誰だって思いつきそうなありきたりな自己紹介じゃないか。もっと何か言わなきゃ。何か面白いことを。"


"でも結局俺は何も言わず、先生が話を続ける。"

"ほとんど話なんてしてないけど、みんな満足したらしい。女子の何人かが俺をちらちら見ながら小声で話している。最悪の事態は避けられたみたいだ。"


"……"


label jp_A2c:

scene ev hisao_class_end
with None


"先生が仲良く云々とまたぶつぶつ言っているのを聞きながら、教室をざっと見回す。"


"みんな真剣に聞いているようだ。話が終わると、また拍手が起こる。なんだか変な感じがする。"

"今度は最前列の子も、片手でもう一方の手首を叩いて拍手する。手首から先はなく、包帯で巻かれている。"


"申し訳ない気分になる。"

scene bg school_scienceroom at bgright
show muto normal at center
with fade


mu "今日は君がクラスとなじめるように、グループワークをやろうと思う。構わないか？"


hi "はい、大丈夫です"

show muto smile
with charachange


mu "よろしい。羽加道といっしょにやるといいだろう。羽加道は学級委員だ"


mu "知りたいことがあれば何でも説明してくれるぞ。まさに適任というやつだな。そうだろう？"

hide muto
with charaexit


"知らないよ、そんなの。"


"先生は課題を配ると、３人組で作業するようにと伝える。"


"そういえば羽加道というのが誰だか知らないじゃないか。鈍いぞ俺。助けを求める俺の視線に先生が気づく。"


mu "ああそうだった。羽加道ならそこだ。羽加道静音"

show misha perky_smile at center
with charaenter


"先生が名前を呼ぶと、明るいピンクの髪と金色の瞳の、陽気そうなかわいい子が俺に手を振る。俺はその女子の隣の、窓際の席に座る。"


hi "君が羽加道だよな？　よろしく"

stop music fadeout 1.0

show misha cross_laugh
with charachange


mi_shi "ははは～！"


"なんだよ？　そいつの笑い声に不意をつかれる。"

show misha hips_grin
with charachange


mi_shi "こっちこそよろしく！　{w=0.5}でもぉ～！"


mi_not_shi "こっちこそよろしく！　でもぉ～！{fast}　わたしは羽加道じゃなくて、ミーシャ！　羽加道しっちゃんはこっちだよ～！"


play music music_shizune fadein 1.0

show misha hips_grin at twoleft
show bg school_scienceroom at center
with charamove

show shizu basic_normal at tworight
with charaenter


"くすくす笑いながら、ミーシャはとなりの女子を指さす。さっき手話を使っていた子だ。どうやら最初からずっと俺のことを見ていたらしい。俺の存在を認めて、さりげなくうなずく……ほんの少しだけ。"


"念入りかつきれいに梳られた短い髪。上品そうな鼻先には卵形のレンズの眼鏡。濃い青色の瞳は数秒ごとに分析モードと退屈モードに切り替わっているように見える。"


hi "よろしく"

show shizu behind_blank
with charachange


shi "……"

show misha perky_smile
with charachange

show misha sign_smile
with charachange

show misha perky_smile
with charachange


"羽加道はすぐにミーシャに向き合う。ミーシャは微笑んでいくつか素早い手振りを見せる。"

show shizu adjust_happy
with charachange

show shizu behind_smile
with charachange


"羽加道はうなずくと、なにごとか手話で返す。"


"まさか先生にかつがれたんじゃないだろうな。『みんなと話せる』だの、『説明にはまさに適任』だの言って。"

show misha hips_smile
with charachange


mi "ちょっと混乱してるかな？　かな？　でもわたしがしっちゃんだと勘違いするのはしかたないよ！"


mi "しっちゃんは耳が聞こえないの。だからわたしが代わりにしっちゃんや他の人の話すことを翻訳してるの"

show misha hips_grin
with charachange


mi "わたしは通訳みたいな人なの～！　しっちゃんもよろしくって言ってるよ！"

show shizu basic_normal2
with charachange


shi "……"

show misha perky_smile
with charachange


mi "あなた転校生よね？　もうしっちゃん、当たり前じゃん！　じゃなかったら用もないのにみんなの前で立ってるってことになっちゃうでしょ？　でしょ～！"



label jp_A2d:


mi "すごく面白そうな人だよね～！"



label jp_A2e:


"ミーシャはへんてこな顔で俺を見て、言葉を継ぐ。"


mi "あんまり詳しいことはわからないけど、あとでわかるかもね"


"やっぱり自己紹介した方がよかったかもしれない。どんな自己紹介でも、先生がぶつぶつつぶやいて俺の名前を間違えるよりはましだったに違いない。"



label jp_A2f:


mi "転校生が来るってことは知ってたんだけど、今日来るとは知らなかったな。すごい急だよ！　ね、ひっちゃん？"


"ひっちゃん……？"

show misha hips_grin
with charachange


mi "うん！　お似合いだよね？"


"俺、口に出してたか？　びっくりした。そのあだ名は昔から気にいらなかったんだ。"


hi "どこがお似合いなんだよ"

show misha cross_grin
with charachange


mi "似合ってるよ～！　想像してたとおり！"

show shizu adjust_smug
with charachange


shi "……"

show misha cross_laugh
show shizu adjust_happy
with charachange


mi "はははは～！　そうね、いかにもひっちゃんって感じ！"


hi "どうしてみんなそう思うんだ……"

shi "……"


"羽加道が指で机を叩いてミーシャの注意を引く。目にも止まらない早さで、二人は熱心に手振りをやりとりする。"

show shizu adjust_happy
with charachange

show misha sign_smile
with charachange

show shizu behind_smile
with charachange

show misha perky_confused
with charachange


"ミーシャは少し呆気にとられたように見える。"

show misha hips_grin
with charachange


mi "あはは～！　えっと、ごめんごめん！"

show misha hips_smile
with charachange


mi "しっちゃんは学級委員だから、知りたいことがあったらいつでも聞いてね、って言ってるよ"

show shizu behind_blank
with charachange


shi "……"

show misha sign_smile
with charachange


mi "学校は気に入った？　もしその辺を散歩して校内を……{w=0.5}{nw}"

show misha perky_smile:

    "misha perky_confused" with Dissolve(0.5, alpha=True)
with None


extend "じゅくち？{w=0.5}{nw}"

show misha perky_confused:

    "misha perky_smile" with Dissolve(0.5, alpha=True)
with None


extend "する暇がなかったなら、わたしたちが案内してあげる！"


"ミーシャは難しい単語に少しもたつく。すらすらと通訳するけど、そこだけが浮いて聞こえる。"


hi "それは助かるな。今日は寄り道せずに教室に来たから"

show shizu behind_frown
with charachange


shi "……"

show misha hips_laugh
with charachange


mi "ははは～！"

show misha hips_smile
with charachange


mi "それはよくないわ！　初めての場所に行く前には必ず下調べをしなきゃ。学校だけじゃない、どんな場所でもそう～！"

show misha hips_grin
with charachange


mi "いつでもです！　コンビニに買い物に行くときだって！　え～、そうなんだしっちゃん？　ははは～！"

show misha perky_smile
show shizu behind_smile
with charachange


"行く先の下調べ？　確かに、面倒くさくてしなかったか、そこまで気にしてなかったか、どっちかだと思う。"


"もともと転校そのものだって楽しみにしてたわけじゃないし。確かにやってみようって気持ちはあったけど、そこまで真剣には考えていなかった。"


"俺は何も言わない。ミーシャは何か手話で伝えると、最後に肩をすくめる。なんだそれ？　俺に関係あるみたいだけど。"


"机に突っ伏したい気分だ。二人とも笑っているけど、あそこで肩をすくめられたのは予想以上にショックだった。"

show misha perky_sad
with charachange


mi "なんか元気ないね。だいじょうぶ？"

show shizu basic_normal
with charachange


shi "……"

show misha perky_smile
with charachange


mi "お願い、勘違いしないでね～！　人が質問するのをためらうのって本当にいやなの！　人は質問することで学ぶんですから～！"


mi "助けが必要なときに、助けてって頼むのは全然変なことじゃないでしょ！　試験に落っこちたみたいな顔するんじゃないの！"

show misha cross_laugh
with charachange


mi "わははは～！"


hi "わかったよ"

show shizu adjust_happy
with charachange


shi "……"

show misha perky_smile
with charachange


mi "ああそれとね、しっちゃんのことは『羽加道』とか『学級委員』なんて固い呼び方しなくていいからね！　しっちゃんでいいよ～！"

stop music fadeout 0.5

show shizu adjust_blush
with charachange


shi "……"

show misha hips_smile
with charachange


mi "あはは～！　おっけ、それはちょっと気安すぎるね。じゃあ『静音』のほうがいいかな？"

show shizu basic_normal2
with charachange


shi "……"

show misha hips_grin
with charachange

play music music_shizune fadein 5.0


mi "うんうん！　『静音』でいいよ！"


hi "わかったよ。俺もその方がずっと呼びやすいし"


"気持ちがずっと楽になる。二人ともすごく親切で、あんなに心配してたのがバカみたいだ。特に静音。もっと堅苦しいタイプだと思ってたのに。"


"まあ今も似たような感じけど。少しはましになった気がする。"

show shizu behind_frown
with charachange


shi "……！"

show misha perky_confused
with charachange


mi "え？　あっそうだ、課題がほったらかし！　すぐ始めないと、しっちゃんに怒られちゃう"


hi "この課題は結構長いから、今始めないと授業が終わるまでに間に合わないな"

show misha hips_laugh
with charachange


mi "わはは～！　それもね！"

show shizu basic_frown
with charachange


shi "……"


"静音が苛立ったように俺たち二人をにらむ。それくらい手話を知らなくてもわかる。"


hi "はいはい。ちゃんと通じてるよ"

show shizu basic_normal
with charachange


shi "……"

show misha perky_smile
with charachange


mi "放課後に一緒に学校の中を散歩しない？　今日はいい天気だし！　いいでしょ～？"


"やってみると、この課題はかなり手強い。難しいのに加えて、むやみに長い。"

stop music fadeout 6.0

scene bg school_scienceroom
with shorttimeskip


"とりかかるのは遅れたけど、それでもほかのグループよりも数分早く終わらせることができた。静音とミーシャは相当できるんだな。"


"でもこの二人は似ても似つかない。学級委員の方は見た目通りに落ち着いてて、気が強い。一方ミーシャはずっとお茶目で女の子らしい。ちょっと集中力不足なのは言うまでもないけど。"


"実を言うと、課題のほとんどはこの二人が片づけてしまった。なんだか悪いな。"

play sound sfx_normalbell


"時計台の鐘が鳴り、授業の終わりを告げる。昼ご飯の時間だ。"

scene bg school_hallway3
with locationchange


"廊下からミーシャが手招きする。ほかにすることも思いつかず、俺はミーシャについて階段を下る。"




label jp_A3:

scene bg school_staircase2
with locationchange


"武藤先生に出会ったロビーからさらに下り、一番下の階まで降りる。"

play ambient sfx_crowd_indoors fadein 6.0

scene bg school_cafeteria
with locationchange


"食堂はやたらと広くて、古めかしい外見に不釣り合いなくらい近代的なつくりだ。この学校は何もかもそんな感じだな。"




"校庭に面した大きな窓からは、正門が見える。"


show misha hips_grin
with charachange

play music music_ease


mi "食堂だよ～！"


"当たり前のことを大げさに説明するので、俺たちに視線が集中する。でもミーシャは気にもしていないみたいで、俺たちはそのまま列に並ぶ。"

hide misha
with charaexit


"メニューの品目はかなり多い。これはいいなと思ったけど、大半は特殊な食事が必要な生徒のためのものだと気づく。"


"やれやれ。病院に戻ったような気分になる。患者の状態に合わせて、厳密に計量された食事。"


"俺は適当に食べ物を選ぶと、静音についてテーブルに向かい、静音の正面に座った。"

show misha hips_frown at twoleft
show shizu basic_normal at tworight
with charaenter


"あまり食べる気の起きない食事を無感動につまんでいると、ミーシャが横から俺をつついて注意を引き、静音を指さす。"

show misha perky_smile
show shizu basic_frown
with charachange


shi "……"


"手話はわからないので、ちんぷんかんぷんだ。"


"礼儀としては『話している』人の方を向くのが正しいのかな？"

show misha hips_smile
show shizu behind_blank
with charachange


mi "知りたいことはある？"


hi "何について？"

show misha hips_grin
with charachange



mi "何でもよ！　わたしたちは案内役なんだから、何かあるんだったらそっちから質問しなきゃ～！"


label jp_choiceA3:
menu:
    with menueffect
    hi "うーん、そうだなあ…"
    "図書室について聞く":




        return m1
    "静音の聾について聞く":


        return m2
    "特に聞きたいことはない":


        return m3        

label jp_A3a:


hi "そうだ。この学校に図書室はある？　最近読書にはまってるんで、見てみたいんだ"


"ミーシャは眉をひそめる。読書を健全な趣味と思っていないのが見え見えだけど、すぐに笑顔を取り戻す。"


mi "あるよ～！　２階にあるから、今度案内してあげる！"


hi "ありがとう"


"二人が話し続ける中、俺は食事を再開する。"



label jp_A3b:


"静音は面白い子だ。ちょっと話を聞いてみたいと思う。"


"でもそんな立ち入った話は聞けないよなあ。"


"うーん……"


"結局他に聞くことも思いつかず、二人が話し続けている間、ずっと食事を食べ続ける。"



label jp_A3c:


hi "なんにも思いつかないや、マジで"

show misha sign_smile
with charachange


mi "おおー！　じゃあわたしたち、ちゃんといい仕事してるってことだよね？　だよね～？"


"……"


hi "えー……まあ、そうかもね"

show misha hips_grin
with charachange

show shizu behind_smile
with charachange


"ミーシャが輝く笑顔でこっちをまっすぐ見る。素早く通訳された静音もそれに続く。"


"二人のちょっと大げさな熱意に俺は頭を振り、食事に集中しはじめる。"



label jp_A3d:


"ミーシャと静音は俺のことを横目で見ながら、生き生きと手話をやりとりする。でもミーシャはその会話を訳さない。"


"女子同士の秘密のおしゃべりってやつか。"


"……"

stop music fadeout 3.0
$ renpy.music.set_volume(1.0, .5, channel="ambient")
stop ambient fadeout 3.0


"ほどなく、会話が手話だけじゃ場が持たない、ということに気づく。"

scene bg school_scienceroom
with shorttimeskip

play music music_daily fadein 0.5


"教室には早めに戻ったけど、一番乗りではなかった。"

show hanako emb_downtimid at Transform(xanchor=0.8, xpos=1.0)
with charaenter


"さっき見かけた黒い髪の女子が、一番後ろの列の机の上に突っ伏している。"

show hanako defarms_shock
with vpunch

show hanako defarms_shock at Transform(xanchor=0.6, xpos=1.0)
with charamove


"ミーシャがサイのような乱暴さで教室に突入したので、その子は驚いてびくりと震える。"


"自分の席にさらに小さく縮こまる。あの子が緊張してるのがこっちまで伝わってくる。俺たちがここにいるだけで、徐々に石に変わってしまうんじゃないか。"


"ミーシャと静音は気づいていないのか気にしていないのか、その子を通り過ぎて自分の席に戻り、おしゃべりを始める。"

show hanako defarms_shock at offscreenright
with charamove

hide hanako
with None


"ほかの生徒が徐々に教室に戻り、最後に先生がやってきた後も、その子のことがずっと気になった。"


"学校生活のリズムに合わせるのは変な気分だ。頭では覚えているのに、体の方は忘れてしまっているような感じ。"


"授業も終わりに近くなり、俺はあくびをしながら残りの時間を数える。"


"転校初日からこんなに疲れてちゃダメだろう。"


"病院暮らしが長かったおかげでこうなってしまったのかもしれない。体が弱くなり、活力がなくなった気分さえする。"

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell


"やがて終業のベルが鳴る。"


"やっと今日の授業が終わった。"


"俺の隣で、ミーシャと静音が短い会話を交わす。しばらく考えごとをしてから、ミーシャが俺の方に振り返る。"

show shizu behind_blank at tworight
show misha perky_smile at twoleft
with charaenter


shi "……"


mi "ひっちゃん、残念だけど今日は学校を案内してあげられないの。仕事がたくさんあって、わたしたち急がないと"

show shizu basic_normal2
with charachange


shi "……"


mi "あなたなら大丈夫よね、きっと"


hi "ああ、待って！　看護師長に会ってこいって先生に言われてたんだ。どこに行けばいい？"

show shizu behind_smile
show misha hips_grin
with charachange


mi "そうなの？　それくらいならおやすいご用だよ～！"

mi "ついてきて。看護の人たちは別の建物にいるから、外に出ないと"

hide shizu
hide misha
with charaexit

scene bg school_hallway3
with locationchange


"吹き抜けの階段を下りて、外に向かう生徒たちに合流する。道中、同じ廊下にある３年の教室を二人が教えてくれる。"

scene bg school_courtyard
with locationskip


"外にでると、二人は本校舎のとなりにある小さめの建物に足を進める。"


"どちらも同じ様式で作られているので、本校舎の一部のように見える。"

show shizu behind_smile at tworight
show misha perky_smile at twoleft
with charaenter


shi "……"


mi "ここは副校舎よ。事務関係の重要な部署がたくさん入ってる。山久財団の事務局とか、看護の人たちの部屋もこの中にあるわ。水泳プールだってあるのよ！"


hi "事務とは関係なさそうだけど？"

show shizu behind_frustrated
with charachange


shi "……"

show misha hips_grin
with charachange


mi "何言ってるの、ひっちゃん！　理学療法のために決まってるでしょ"

show misha sign_smile
with charachange


mi "とにかく、看護スタッフの施設もみんなこの中にあるから。看護師長の部屋は１階だよ"

show misha hips_smile
show shizu behind_smile
with charachange


mi "あとは一人でも大丈夫だよね～？　それじゃあね！　また明日！"



hi "ああ、ありがとう。じゃあな"

stop music fadeout 5.0

hide shizu
hide misha
with charaexit


"この建物丸ごと、実際の教育に関係ないことでいっぱい？"


"まあ、こういうところには必要なんだろうな。"

scene bg school_nursehall
with locationchange


"俺は中に入る。本当に先生が言ったように、手短に済めばいいんだけど。"


"左側の白いドアに『看護師長』と文字が入った緑色の十字と、名札がかかっている。"

play sound sfx_doorknock2


"俺がノックするのとほぼ同時に中の声が答える。でもよく聞き取れない。"


"なんとなくドアを開けて入ってこいという誘いに聞こえたので、その通りに中に入る。"

play sound sfx_dooropen

scene bg school_nurseoffice
with locationchange


"部屋は大きくはなく、変なにおいがする。気さくそうな男の人が事務いすを回し、俺に向き合う。"


"机はきれいに片づけられているけど、机の下のごみ箱は使用済みの医療器具であふれかえっている。それにコーヒーカップの跡が数え切れないほど机の上にこびりついている。"

play music music_nurse fadein 0.5

show nurse neutral at center
with charaenter


nk_ "やあ。今日はどんなご用かな？"


"若そうでちょっといかつい人だけど、そんな印象も笑ったときのえくぼに押し流される。"


hi "あの、看護師の人ですか？"

show nurse grin
with charachange


"もう何百回も同じことを聞かれているかのように、その人は笑う。"


nk_ "そうだよ。そうドアに書いてないかい？"


nk_ "名前で呼んでくれてもいいし、他のみんなみたいに『ナース』でも構わないよ"


"そりゃそうだ。差し出された手を握らなきゃ、と気づいて、俺は気持ちを切り替える。{w} この人の握手は結構しっかりしていて、親しみを感じる。"


hi "はい……ええと、転校生なんですけど、担任の先生に言われてここにきました。中井久夫と言います"

play sound sfx_snap


"俺の名前を聞いてナースは目を輝かせ、指を鳴らす。"

show nurse fabulous
with charachange


nk "ああ、君があの中井君か。ちょうど今朝君の資料を読んでたところだよ"


nk "慢性不整脈の一種と、先天性の心筋欠損症、だったね？"


"手振りで机の前の肘掛けいすに座るよう勧めてくる。"


hi "ええと、はい"

show nurse neutral
with charachange


nk "うん。まあ、この学校についてはさんざん聞いてると思うから、簡単に説明するよ"


nk "この学校にはあらゆる施設がそろってる。ほとんどは理学療法にかかわるものだけどね"


nk "看護スタッフが昼夜関係なく待機しているから、具合が悪くなったら必ず声をかけるようにね"


"うわさの２４時間待機の看護スタッフか。"


hi "へえ、病院みたいだ"


nk "まあ、厳密には違う。たとえば脳の手術はここではやらないよ"



"あまりに場違いなジョークに聞こえた。なんでそんなことを言ったのか、と考えてしまう。"


hi "そうですね……学校にこんなに医療関係の人がいるって、すごく変な感じがします"


nk "そのうち慣れるよ"


"俺にはそこまで自信は持てない。けど、ナースには気取られないようにする。"


nk "さて、君のファイルはどこだったっけ……"


"彼がパソコンで何かを探したり、紙の束を引っかき回したりする間、俺は室内をつらつらと眺める。"


"俺に言わせると、典型的な普通の医務室だ。"


"ベージュの壁と天井。ダークグレーのタイル張りの床。学校の医務室なら必ずありそうな、数々の医療器具。"


"バカみたいな教育用のポスターまで、四方の壁に張り出されている――一日三回、すべての食品群から食事をとりましょう、だって。"

show nurse grin
with charachange


"笑いながら、ナースは分厚いファイルを書類の山から引き抜いて、それを開く。"


nk "もう不整脈の薬はあるのか。じゃあ朝と夜に忘れずに飲むように。でないと効き目がないからね"

show nurse fabulous
with charachange


nk "それ以外には……なにかスポーツはしているかい？　激しいやつ……そうだな、ボクシングとか？"


"ナースは自分のジョークににやりとするけど、俺は笑わない。"


hi "ええまあ、クラスメイトとたまにサッカーをしてました"


nk "そうか。残念だけど今後はサッカーはやめたほうがいい。少なくとも今はね"


hi "はあ"


"俺の淡泊なリアクションに、ナースは片眉を上げる。でも実際、ボールを蹴って遊ぶのを止められたからって困るわけじゃない。"


"それほどスポーツに燃えてたわけじゃないんだろう。やることがなくてやってただけだ。"


nk "ささいな衝撃であっても、君の心臓にとってはとても危ないんだ。これ以上発作を起こすのはまずい"


nk "前回の発作が起きたのは、胸に衝撃を受けたせいかな？　書類には理由について何も書かれていなかったけど"


hi "ええと……そういうわけじゃ"

show nurse concern
with charachange


"なんとか質問をかわす。ナースはずっと真剣な顔つきで、書類ごしに俺を見やる。"


nk "いずれにしても、健康維持はしないといけない。運動はしたほうがいいな"



nk "さっきも言ったように理学療法なども受けられるけど、君にはそこまで本格的な治療は必要ないだろう"



nk "軽くでいいから、きちんと運動するように"


nk "速歩きか、あるいは軽いジョギングや縄跳びとかだね。水泳もいいかもしれない。プールもあるし"


hi "ええ、聞きました"

show nurse neutral
with charachange


nk "そうかい？　それはよかった"


nk "あとは、もう何度も聞かされてるだろうけど、とにかく無理をしないよう気をつけること"


"指を振って強調する。まあ言われるまでもないけど。もう１００万回は聞いてるし。"

show nurse concern
with charachange


nk "必要のないリスクは決して冒さないこと。体調には気をつけるんだ"


hi "はい"


"書類にもう一度目を通して机に戻す。満足したみたいだ。"

show nurse neutral
with charachange


nk "よし。話はおしまいだ。何かあったら、僕のところに来るようにね"

scene bg school_nursehall
with locationchange

stop music fadeout 2.0


"いつのまにか部屋の外に案内されている。本当にあっという間に済んじゃったな。"




label jp_A4:

scene bg school_courtyard
with locationchange

play music music_pearly fadein 4.0


"本校舎と副校舎の前までやってくる。もっとも、今の俺にはどっちも同じに見えるんだけど。"


"他の生徒をちゃんと見るのは初めてだ。学校から出てきて校門や寮へと向かう生徒の群れを観察する。"


"みんな行く先は決まっているようだ。"


"特殊学校にいる生徒にしては、そのほとんどはそんなに特別には見えない。さっきからずっとそのことを考えている。でもそれは俺だって同じことだ。"


"俺もあいつらと同じということなのか？　俺もその一員なのか？"


"……"


"迷ったりする前に俺も行かないと。"


"夕飯時だけど、空腹よりも疲れを感じる。"


"本校舎から少し離れた寮のほうへとぼとぼと歩いていると、どんどん疲れがたまっていく。"

scene bg school_gardens
with locationchange


"寮へ行く途中に庭園みたいなものがある。植え込みや花が並び、そして圧倒されるような草の香りが空気を満たしている。"


"こういう香りが新鮮に感じられるのも、あまりに長い間、外出することがなかったからだと気づく。"

scene bg school_dormext_start at bgleft
with locationchange


"寮は赤レンガ造りの大きい建物だ。学園の他の建物同様、仰々しい感じがする。俺は覚悟を決めて中に入る。"

scene bg school_dormhallground
with locationchange


"貰っていた鍵をポケットから取り出すのに手間取って余計な時間を食う。"


hi "１、１、９号室だったな……"


"寮の派手な外観とは裏腹に、内側はけっこう新しく、機能的で、そして退屈だ。"



"本校舎同様、車椅子が入れるように廊下も扉も広く作られている。廊下の突き当たりにあるエレベーターもそうだ。"


"ちらりと共有スペースを覗いてみる。"


"テレビを見ている生徒が何人かいる。"


"一人が会釈して挨拶をよこし、またテレビ鑑賞に戻る。"


"どうやらこの辺で社交的なのは、あの二人の女子ぐらいらしい。まあ俺としては全く問題ないと思うけど。"


"階段を登り上へ向かう。"

scene bg school_dormhallway
with locationchange


"一本の廊下を幹に、小さな廊下が複数枝分かれしている。"


"それぞれの廊下には部屋が四つ、さらにトイレとシャワー室まである。"


"廊下を半分ほど行ったところで、１１９号室を見つける。"


"両隣の部屋にある表札は空白になっている。この廊下には俺含め二人しか住んでないのだろうと思う。"

play sound sfx_doorknock2
stop music fadeout 3.0


"１１７号室のドア下のすき間から光が漏れている。俺はドアを軽くノックする。"


hi "こんにちは、誰かいますか？"


"内側で誰かの動く音がする。それから何度もドアの鍵がかちゃかちゃと音をたてる。思ったよりずっと沢山の鍵がついているようだ。少しして、キィという音を立てながらドアが開く。"

show kenji tsun at Slide(0.4,0.5,0.5,0.5,0.5)
with charaenter

play music music_kenji fadein 0.5


"ドア口に眼鏡の青年があらわれる。分厚い眼鏡の向こうから俺のことをじーっと見つめてくる。"


ke_ "誰だ？"


"目が見えないのか？　いや、全く見えないわけではないはずだ。もしそうなら眼鏡なんてかける意味ないだろう。"

show kenji tsun_close at center
with characlose


"そいつは俺の方へ乗り出してきて、鼻と鼻が触れそうになる。こいつニンニクくさい……"


hi "俺は中井久夫……隣の部屋に越してくることになったんだ。挨拶しておいた方がいいかとおもっ"

show kenji happy
with charadistant


"そいつは何かに気づいたように急に顔を明るくすると、一歩下がって姿勢を正し、笑顔で手を突き出してくる。ほぼ真っ直ぐに、俺の腹のあたりまで。"


ke_ "ん？　どうした？　俺の名前なら健二だよ"


hi "あー……どうも"


"健二の汗ばんだ手をとって握手する。突然の態度の変化と熱烈な歓迎に、さっきから俺は少し動揺している。"


ke "お前の部屋、さっき怪しいやつらが出入りしてたぞ"


hi "それ俺の両親だと思うよ"

show kenji tsun
with charachange


ke "お前の両親？　確かか？　だって、別人だった可能性もあるだろ。見かけで人を判断しちゃいけない"


"ズレた格言の残響が気まずく漂う。どう返事するか考えている間ずっと。"


hi "いや、俺の両親の可能性は高いんじゃないかな"


"健二はぶるっと震えて大袈裟な身振りをしてみせる。"

show kenji neutral
with charachange


ke "おまえ勇気あんなー"

show kenji tsun
with charachange


ke "俺には信用できないけどね"


ke "俺は信用するのは自分だけだ"


hi "ということは俺はお前と知り合わない方がいいってことかな"


"健二はしばらく考える。"

show kenji neutral
with charachange


ke "いい判断だ"

show kenji happy
with charachange


ke "くそ、お前見た目より頭切れるな、"


ke "多分だけど"


ke "お前どんな顔してんの？　アホっぽいことを願うよ"

show kenji neutral_close
with characlose


"健二は目を細めてまた顔を寄せてくるけど、俺も体を後に反らして避けてやる。"

show kenji tsun
with charadistant


ke "気にするな、大したことじゃない"

hide kenji
with charaexit

stop music fadeout 3.0


"そう言って健二は部屋に戻る。ドアの取っ手をまさぐり探りあて、{w=0.3}{nw}"

play sound sfx_doorslam


extend "後ろ手にバタンと閉める。"


"俺も行こう。１１９号室の鍵穴に鍵を滑り込ませる。"

scene bg school_dormhisao_ss
with locationchange

play music music_night fadein 1.0


"面白味のないベージュの壁、白いシーツ、淡褐色の木の机。それに見苦しいカーテン。"


"誰の部屋でもない。俺が入院してた病室みたいに、人間味がない。"


"ベッドの横に置いたバッグは、朝見たときよりも虚ろに見える。"


"クローゼットは開いたままになっていて、俺の服が入れてある。"


"学校の制服もいくつか掛かっているようだ。"


"ふと見ると、シャツの袖にメモが留めてある。"

window hide

$ written_note("ひっちゃんへ。荷解きを済ませておきました。\nもし制服が合わなかったら事務室に行くといいそうです。\n何かあったら、いつでも電話してね。\n\n母さん父さんより")

window show


"まあ、少なくとも荷解きについては心配する必要はないらしい。"


"荷解きしてくれなくてもよかったのにと思う。そうしたらやることがあったのに。"


"まだ時間が早すぎる。"


"読み終わったメモを机の上において、ベッドで横になる。疲れきっている。"


"こうして横になっていると何か読みたくなってくるけど、何も持っていない。"

"病院にいる間に条件付けでもされたんじゃないだろうか。何もすることがないと本を読みたくなるように。"


"落ち着かない気分が大きくなり続け、ついにベッドから起き上がる。"


"ストレスか何かかも。"


"学園に来る前からかなり不安で張り詰めていたし、結局一日中そのままだった。今もそうかもしれない。"


"くそ、何とか気を紛らわさないと。ずっとこんな風じゃまずい。"


"明日は図書室で本でも借りよう。"


"ああ、そうしよう。"


"ただ今は…………"

show pills:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with Pause (1.0)


"ナイトテーブルの上にきちんと並んだ薬の瓶が目に入る。"


"その瓶をひとつ手にとって振り、中で薬がカラカラと音を立てるのを聞く。それから貼り付けられたラベルを読んでみる。"

window hide

show pills:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with Pause (1.0)

hide pills
with None

$ written_note("中井 久夫\n\n死にたくなければ一日二錠")

window show


"本当にそんなこと書いてるわけないけど、同じようなもんだ。"


"こんな薬品に命が左右されるなんて不愉快だ。少し憤慨するけど、だからって俺にどんな選択肢がある？"


"ため息をついて、これから毎日行うことになる儀式に取りかかる。念入りに服用量を確認し、各瓶から量を間違えないように錠剤を取り出す。"


"……"


"俺は不安と虚無感を感じながら再び横になり、何もない、見慣れない天井をずっと見つめ続ける。"

stop music fadeout 8.0

scene bg school_dormhisao_ni
with Dissolve(3.0)


"部屋はまったくなじんでこない。夜の帳が下り、指のように長い影が部屋に伸びてくる時間になっても。"


"肌に触れる布団が心地よくなってくる。暖かくて、部屋の中の冷たい空気から身を守ってくれる巣のようだ。"


"宵闇の中でもまだ薄暗かった部分──つまり天井のことだ──それもやがて、いつもの夜中の天井のように真っ黒になる。もうその闇しか目に映らない。"


"夜が俺を眠りへといざなう。見慣れぬ部屋と不安に、また寒気が背中を這い上がるのを感じる。"

"俺は見知った世界からどんどん遠ざかっていく。"

$ suppress_window_after_timeskip = True

scene black
with shuteye


return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
