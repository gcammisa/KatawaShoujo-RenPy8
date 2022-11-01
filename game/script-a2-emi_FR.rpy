
label fr_E3:

window hide None

scene black
with dissolve

$ renpy.music.set_volume(1.0,0.0, "ambient")
play sound sfx_alarmclock

window show


"L'alarme de mon réveil perturbe le silence matinal, et je me retrouve à chercher une raison valable de me lever."

window hide

scene bg school_dormhisao
with openeye

window show


"Les cours ne commencent pas tout de suite, mais j'ai accepté de courir avec Emi le matin."


"Pourtant, je ne suis pas intéressé par la course comme hobby, ni comme moyen d'allonger ma durée de vie."


"Cependant, je me sens obligé de respecter la promesse que j'ai faite à Emi hier, c'est pourquoi je me retrouve à mettre un short et un t-shirt."

scene bg school_courtyard
with locationskip


"L'air frais du matin me caresse le visage alors que le soleil matinal fait briller la rosée sur l'herbe, m'aveuglant presque."


"Alors que je me dirige vers la piste, une pensée me traverse l'esprit."


"Et si c'était une sorte de blague qu'Emi me fait ?"


"Est-ce que ça me surprendrait vraiment ?"


"Bah, je ferais probablement pareil au nouveau après tout."


"Au moins, je suis sûr qu'Emi et Rin ont parié sur le fait que j'allais venir ou non."

scene bg school_track
with locationchange


"Je commence à trépider alors que la piste est en vue."

show emi basic_annoyed_gym at center
with charaenter

play music music_emi fadein 1.0


emi "Tu es en retard !"


"On dirait qu'Emi est déjà là. Quel soulagement."


hi "Pas selon ma montre. On est tous les deux en avance, en fait."

show emi basic_closedhappy_gym
with charachange


emi "Zut, tu m'as eue sur ce coup-là."


"Emi est assise dans les gradins, installée avec son équipement de course, attendant patiemment ma venue."


hi "Je suis contente que tu sois vraiment venue. J'ai eu peur que ça puisse être une blague ou un truc du genre."

show emi basic_grin_gym
with charachange


emi "Nan, je ne ferais jamais se lever quelqu'un aussi tôt pour rien."

show emi excited_proud_gym
with charachange


emi "Et puis en plus, Rin me doit 500 yen maintenant. Elle ne pensait pas que tu viendrais vraiment."


"Je le savais !"


"C'est gentil à Emi d’être de mon côté, au moins."

show emi gymbounce_once
with Dissolve(0.1)


"Emi saute pour descendre des gradins et commence à s'étirer."

play sound sfx_gymbounce

show emi gymbounce
with Dissolve(0.05)


"Elle est remarquablement souple, presque comme une danseuse."


"Je me mets en place pour m'étirer aussi, mais je me rends compte que je ne sais pas vraiment comment bien m'étirer."


"Ça fait très longtemps que je ne me suis pas étiré pour quoi que ce soit, si je ne compte pas la course de la semaine dernière."


"Et même là, je ne crois pas m’être vraiment étiré non plus."


"Le spectre de mon long séjour à l’hôpital apparaît encore une fois."


"Je ne peux pas dire non plus que j'étais vraiment actif avant mon séjour à l’hôpital, alors je suis peut-être juste morose."

show emi basic_closedgrin_gym at center
with charachange


"Emi rit un peu alors qu'elle me regarde m'étirer."

show emi basic_grin_gym
with charachange


emi "Non non non Hisao, tu dois rester en position pendant plus longtemps que ça."


hi "J'essaye ! Mais ça fait un peu mal."

show emi excited_proud_gym
with charachange


emi "Ha ! C'est parce que tu n'es pas en forme. Tu dois trouver un peu de souplesse en toi, comme ça."

hide emi
with charamoveoutbottom


"Pour faire une démonstration, Emi se penche et passe sa tête entre ses jambes."


"Dieu te garde, Emi."


hi "Je vois. C'est le genre de chose que je dois essayer de faire ?"

show emi basic_closedgrin_gym
with charamoveinbottom


emi "Bien sûr ! Être souple est important pour un coureur. Tu seras capable d’être plus rapide si tu t'étires."


"Je ne trouve pas ça logique, mais Emi semble le croire dur comme fer."


"Avec l'aide d'Emi, j'arrive à m'étirer correctement."

show emi basic_grin_gym
with charachange


"Je ne peux pas m’empêcher de remarquer que quand elle se demande comment expliquer certaines choses, elle se mord les lèvres."


"C'est adorable."

show emi excited_proud_gym
with charachange


emi "Pas mal, Hisao. Allez, on ferait mieux de commencer à courir."

show emi excited_happy_gym
with charachange


emi "On va commencer avec juste un kilomètre et demi, d'accord ?"

show emi basic_happy_gym
with charachange


emi "Ça fait quatre tours de piste, d'accord ?"


hi "Ça me semble bon."

show emi basic_happy_gym:
    center
    easeout 0.5 xpos 0.4 alpha 0.0
with None

stop music fadeout 2.0


"Ça devrait pas être trop dur, hein ?"

scene bg school_track_on
with locationchange


"Un vague souvenir d'avoir couru un kilomètre cinq en sport me revient à l'esprit."


"Ouais, c'était pas si dur."

play music music_running fadein 0.5

scene bg school_track_running
with Dissolve(2.0)

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

play ambient sfx_emijogging fadein 1.0


"Emi part avec un rythme assez soutenu, et je me retrouve derrière."

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi basic_grin_gym at left
with charamoveinleft


emi "Essaye de suivre, d'accord Hisao ?"


hi "D'accord."

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with charamoveoutleft


"On passe le premier virage sans incident, bien que je sente déjà mon cœur accélérer légèrement."


"Au second virage, je commence à respirer par la bouche."


"Emi ne semble même pas fournir d'effort."


"Comme pour démontrer sa supériorité, elle se tourne et commence à courir à l'envers."

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi basic_closedgrin_gym at center
with charaenter


emi "Est-ce que ça va, Hisao ?"


hi "Jamais... été mieux."

show emi excited_proud_gym
with charachange


emi "Oh vraiment ? Peut-être que je devrais accélérer alors, mmh ?"


hi "Oh... non, je ...ne voudrais pas..."


hi "...que... tu t'é... puises."


"Mon essoufflement me rend moins convaincant que je ne l'aurais espéré. Emi se contente de sourire et se retourne."

show emi excited_proud_gym at left
with charamove


emi "C'est toi le chef, Hisao. On va rester à ce rythme."

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft


"J'ai le sentiment qu'on se moque de moi."


"Si je n'étais pas en si mauvaise condition physique, je serais probablement vexé."


"Au troisième tour, ma respiration se résume à des râles."


"Et je suis trempé de sueur. Dégoûtant."


"On prend la première courbe du quatrième tour, et Emi se tourne pour me voir et affiche un sourire narquois."

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi basic_closedgrin_gym at left
with charamoveinleft


emi "Et c'est parti !"

play ambient sfx_emisprinting

hide emi
with easeoutleft

$ renpy.music.set_volume(0.3, 0.5, channel="ambient")


"Elle part à une vitesse phénoménale alors que je reste coincé au même rythme lent."


"Au moment où je finis la courbe, elle est déjà à la deuxième."


"Alors que je suis à la deuxième ligne droite, Emi continue de courir et me rattrape."

play ambient sfx_emijogging

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi excited_proud_gym
with charamoveinright


emi "Allez Hisao ! Tu peux le faire !"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with charamoveoutleft


"Je lui répondrais bien, mais je suis trop occupé à remplir mes poumons d'air et à ignorer les brûlures musculaires dans mes jambes."


"Une partie de moi veut dire quelque chose comme “Peut-être que {b}tu{/b} peux, mais je suis sur le point de mourir, là.”"


"Mais encore une fois, je doute vraiment de pouvoir parler à cet instant."


"Emi reste à mon rythme alors que je finis le second tour et franchis la ligne d'arrivée."

stop ambient fadeout 1.5

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

stop music fadeout 5.0

show bg school_track_on
show emi basic_happy_gym
with locationchange


"Son sprint semble l'avoir fait transpirer."


"Ce qui rend son t-shirt légèrement transparent. On dirait qu'elle porte un soutien-gorge de sport noir."


"Je me sens légèrement coupable à l'idée d’être le genre de gars qui regarde la poitrine des filles, mais mes jambes et ma poitrine me brûlent tellement que je m'en préoccupe peu."

show emi excited_proud_gym
with charachange


emi "Pas mal pour un premier effort, Hisao."

play music music_happiness fadein 0.5


hi "Gen— ...til à toi... de dire... ça."


"Emi semble être, même si ce n'est pas vraiment essoufflée, au moins en train de respirer un peu plus fort qu'au début de notre course."


"Ça doit être dû au sprint qu'elle a fait."

show emi basic_grin_gym
with charachange


emi "Dis, je dois faire quelques sprints, tu devrais marcher le long de la piste pour te refroidir."


emi "Puis on s'étirera, et on aura fini, d'accord ?"


hi "Ça me semble bien."


"Mes jambes sont en feu et ma respiration est encore forte, mais étonnamment mon cœur semble bien supporter l'effort."


"Un autre triomphe de la médecine, j'imagine."

show emi basic_closedhappy_gym
with charachange


emi "Tu devrais mettre tes mains derrière la tête. Ça facilite la reprise de souffle."

$ renpy.music.set_volume(0.3, 1.0, channel="ambient")

play ambient sfx_emipacing

hide emi
with charamoveoutleft


"C'est surprenant, mais elle a raison. Je commence à marcher le long de la piste, content de récupérer mon souffle."

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

show emi blur at offscreenright
with None

show emi blur at offscreenleft
with move

$ renpy.music.set_volume(0.3, 0.5, channel="ambient")

hide emi
with None


"Je sens un courant d'air alors qu'Emi passe en sprintant à côté de moi."


"La regarder courir est vraiment fascinant."


"Ce n'est pas juste parce qu'elle est sur prothèses, bien que ce soit intéressant."

show ev emi_run_face_zoomin
show ev emi_run_face as unlockstub behind ev
with dissolve


"La chose vraiment intéressante est la façon dont son visage change."


"Je ne peux le voir que de brefs instants alors qu'elle court, mais ses yeux semblent s'illuminer d'une grande joie."


"C'est comme s'il n'y avait rien d'autre dans le monde que la piste et elle."

stop ambient fadeout 0.5

$ renpy.music.set_volume(1.0, 0.5, channel="ambient")

scene bg school_track_on
with locationchange


"Au moment où j'arrive à la dernière courbe, Emi semble avoir fini sa course."


"Elle a le souffle court maintenant, mais elle affiche un sourire satisfait sur le visage. Elle me fait coucou de la main alors que je m'approche d'elle."

show emi basic_grin_gym at center
with charaenter


emi "Ça fait du bien, hein ?"


hi "Eh bien en fait, ouais."

show emi sad_grin_gym
with charachange


emi "Tu veux faire un autre tour avec moi ? Je dois descendre le rythme aussi."


"Une partie de moi a bien envie de s’asseoir et de ne pas bouger, mais quelque chose me dit que ça serait une mauvaise idée."


"Et puis aussi, si je m'assois, je ne suis pas sûr de me relever."


hi "Ouais, pourquoi pas ?"


"Emi met ses mains derrière la tête aussi, ce qui lui donne l'air très détendue."


"La position de ses bras soulève légèrement son t-shirt, ce qui me permet de voir une fine bande de son ventre."


"Je fais de mon mieux pour agir comme un gentleman et ne pas regarder, mais le contraste entre sa peau et son short rouge attire vraiment l’œil."

show emi basic_grin_gym
with charachange


emi "Alors comment tu te sens, Hisao ?"


hi "Étonnamment bien, en fait. J'ai mal et suis fatigué, mais... étonnamment bien."


"Aussitôt que je dis ça, je réalise que c'est vrai."


"Ouais, j'ai aussi envie de m'allonger et de mourir, mais j'ai l'impression d'avoir accompli quelque chose."


"C'est presque comme une lueur dans tout mon corps qui persiste malgré la douleur."

show emi excited_proud_gym
with charachange


emi "Ouais, c'est la drogue du coureur."


hi "La drogue du coureur ?"

show emi basic_hes_gym
with charachange


emi "Ouais, ça a quelque chose à voir avec... l’adrénaline ?"


"Emi réfléchit un moment alors que nous marchons, essayant de se rappeler."

show emi basic_closedgrin_gym
with charachange


"Puis elle hausse les épaules et sourit."

show emi basic_grin_gym
with charachange


emi "Je ne me rappelle pas en fait. Mais c'est une sensation agréable, hein ?"

show emi basic_happy_gym
with charachange

stop music fadeout 0.5
play sound sfx_heartstop


emi "Mieux que le sexe, hein ?"


"J'ouvre la bouche pour répondre avant même d'enregistrer ce qu'elle vient de dire."

hi "…"


"Emi regarde mon visage quelques instants avant d'éclater de rire."

play music music_comedy fadein 1.0

show emi excited_laugh_gym
with charachange


emi "Désolée, désolée ! Je n'ai pas pu résister ! Tu es juste trop prévisible !"


hi "Pourquoi j'ai accepté de courir avec toi déjà ?"


"Emi ne fait que rire encore plus fort. Elle m'attrape le bras et le tourne, lui permettant de bien voir ma montre. Son visage change dès qu'elle voit l'heure."

show emi basic_shock_gym
with charachange


emi "Oh non ! On ferait mieux de se dépêcher, Hisao !"

show emi basic_closedsweat_gym
with charachange


emi "Les cours commencent dans une heure, et je dois prendre une douche !"


hi "Je devrais probablement faire de même..."

show emi basic_hes_gym
with charachange


emi "Je dois voir l'infirmier aussi... peut-être qu'il me fera une note pour mon retard !"


hi "Pourquoi est-ce que tu dois voir l'infirmier ?"

show emi basic_closedgrin_gym
with charachange


"Emi pointe ses prothèses du doigt, comme si ça expliquait tout."

show emi basic_grin_gym
with charachange


emi "Il est important de vérifier s'il n'y a pas d'irritation."


emi "Tu sais, à cause de la transpiration et de la friction, tout ça."

show emi excited_amused_gym

with charachange


emi "Normalement j'y vais seulement après l’entraînement, mais si on fait ces courses matinales, alors je devrais aller le voir deux fois par jour."


"Attends, donc Emi n'a commencé ces trucs matinaux que depuis que je suis là ?"


hi "Si c'est plus pratique pour toi qu'on coure ensemble plus tard..."

show emi sad_grin_gym
with charachange


emi "Ne sois pas bête ! Je voulais courir le matin depuis un moment déjà."


emi "Mais si je n'ai pas de partenaire avec qui le faire, j'aurai plus de mal à continuer."

show emi basic_grin_gym
with charachange


emi "C'est toujours plus facile de continuer si abandonner signifie laisser tomber quelqu'un d'autre, tu sais ?"

show emi basic_closedgrin_gym
with charachange


emi "Alors tu seras mon partenaire de course tous les matins !"

show emi excited_proud_gym
with charachange


emi "On a tous les deux besoin de l'exercice, alors ça s'arrange bien, tu ne crois pas ?"


hi "Ouais, c'est parfait."


"Mais il fallait que ce soit moi ?"


"Bah, je peux pas trop me plaindre non plus. C'est assez fun d’être avec Emi."


"Et elle a raison. J'ai besoin d'exercice. C'est un ordre du docteur, même."

show emi basic_happy_gym
with charachange


"Emi me fait un signe de la main en guise d'au revoir."


emi "Bon, j'y vais ! Viens manger avec nous ce midi, d'accord ?"


hi "Quoi ?"

show emi basic_closedhappy_gym
with charachange


emi "Le midi ! Tu sais, quand tu manges ? Au milieu de la journée ? Viens manger avec nous !"


hi "Où ça ?"

show emi basic_grin_gym
with charachange


emi "Sur le toit. Rin aime bien être là-haut."


hi "Quand ?"

show emi basic_annoyed_gym
with charachange


emi "À l'heure du déjeuner, quand d'autre ? C'est une question bête."


hi "Ouais, mais je ressentais le besoin de me faire préciser les trois détails."

show emi excited_laugh_gym
with charachange


"Emi sourit et se met à rire. Je ne crois pas avoir déjà vu une fille sourire autant."

show emi excited_happy_gym
with charachange


emi "Pas mal, Hisao. À plus !"

play ambient sfx_emisprinting

hide emi
with easeoutleft

stop ambient fadeout 2.0
stop music fadeout 8.0


"Sur ce, elle part comme une fusée en direction du bâtiment scolaire."


"J'imagine qu'elle va voir l'infirmier d'abord."

scene bg school_dormbathroom
with locationskip


"Je me dépêche de retourner à ma chambre et vais à la douche, où je découvre que l'eau prend un moment à se réchauffer."

play ambient sfx_shower
with vpunch


"Le choc de l'eau froide me tue presque."

show steam
with Dissolve(2.0)


"J'arrive à faire chauffer l'eau tant bien que mal et profite un moment d'avoir les muscles détendus."


"Mon cœur, étonnamment, ne semble pas perturbé par la course."


"J'imagine que c'est une bonne chose, même si je me sens un peu comme une mauviette."


"Je veux dire qu'au moins j'aurais une excuse au-delà de juste “Je ne suis pas en forme” si mon cœur me causait des soucis."


"J'imagine que je vais devoir continuer de courir, sinon Emi ne me lâchera jamais."


"C'est seulement après être sorti et m’être séché que je réalise qu'il ne me reste que dix minutes pour m'habiller et aller en cours."


"Zut."


label fr_E4:

scene bg school_dormbathroom
show steam
with None

stop ambient fadeout 1.0

scene bg school_scienceroom
with shorttimeskip

window show

play sound sfx_normalbell


"Les aiguilles de l'horloge me libèrent enfin de l'ennui d'un autre cours dénué d'intéret."


"Me lever de ma chaise s’avère être plus difficile que je ne l'aurais cru."


"Mes jambes me tuent à cause de ce matin."


"Peut-être que faire ça avec Emi n'était pas une si bonne idée après tout."


"Cela mis à part, courir m'a donné une faim de loup."

play ambient sfx_crowd_indoors fadein 1.0

scene bg school_hallway3
show crowd
with locationchange


"Je suis à mi-chemin de la cafétéria quand je me rappelle que j'ai déjà un repas avec moi."


"Mes parents ont pensé que me donner des plats tout prêts pour mon emménagement serait une bonne chose."


"Le couloir est rempli d'étudiants se dirigeant vers la cafétéria."


"Aller dans l'autre sens est comme nager à contre-courant - mais j'ai rendez-vous sur le toit."

stop ambient fadeout 4.0

scene bg school_staircase1
with locationchange


"Il me faut un moment pour trouver les escaliers menant au toit, mais je suis prêt à parier qu'Emi et Rin ne sont pas encore là-haut à cet instant."


"En fait, je crois que j'ai vu Emi parmi les gens se dirigeant vers la cafétéria."

play sound sfx_door_creak
$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 0.5

scene bg school_roof at bgright
with locationchange


"Je passe l’entrebâillement de la porte et prends une grande inspiration."


"L'air frais me passant sur le visage et le corps me ferait presque oublier la douleur que j'ai aux jambes."

show rin basic_awayabsent at center
with charaenter


rin "Peut-être que si je suis à l'envers..."

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_rin fadein 1.0


"Je suis presque surpris que Rin soit déjà là."


hi "Qu'est-ce que ça changerait ?"

show rin basic_deadpan
with charachange


rin "Des trucs dans les nuages."


hi "Tu ne pourrais pas juste... les regarder à l'endroit ?"

show rin basic_deadpanupset
with charachange


"Rin roule des yeux dans un état proche de l’exaspération."


rin "Dans ce cas je n'aurais pas de nouvelle perspective."


hi "Être à l'envers donne vraiment une nouvelle perspective ?"

show rin basic_delight
with charachange


"Ah ha ! Je l'ai eue par surprise. Elle semble pensive."


rin "Tu as peut-être raison. Peut-être de côté."

hide rin
with charamoveoutbottom


"Alors que Rin s'allonge sur le banc pour regarder le ciel, j'abandonne."

play sound sfx_impact2
with vpunch

show emi basic_closedgrin at center
with charaenter


"Heureusement, Emi choisit ce moment pour exploser la porte avec deux sacs dans les mains."


"Elle a presque fait sauter les gonds."

show emi basic_hes
with charachange


emi "Désolée si j'ai été si longue ! Il y avait une tonne de personnes dans la queue."

show emi basic_grin
with charachange

show emi basic_grin at twoleft
show bg school_roof at center
with charamove


"Elle pose le premier sac devant Rin et s'assied sur le banc à côté d'elle."


hi "Tu achètes le repas de Rin aussi ?"

show emi basic_closedgrin
with charachange


emi "Des fois, ouais. Je demanderais bien à Rin de me rendre la faveur, mais je ne sais pas trop comment elle porterait tout ça."

show rin basic_deadpan at tworight
with charamoveinbottom


rin "Et puis en plus je ne lui paierais jamais à manger."


"Si Rin est offensée par le commentaire de Emi, elle ne le montre pas. Emi renifle comme si elle allait pleurer."

show emi basic_annoyed
with charachange


emi "C'est ingrat à toi."


"Je ne suis pas sûr qu'elles ne font que plaisanter ou si j'assiste au début d'un crêpage de chignons."

show emi basic_closedgrin
show rin basic_amused
with charachange


"Les deux filles se fixent du regard pendant quelques instants tendus avant de se mettre à sourire."

show rin basic_awayabsent
with charachange


rin "Dis Emi, tu crois qu'être à l'envers donne une nouvelle perspective aux choses ?"


"Je n'ai pas déjà eu cette conversation avec elle ?"

show emi basic_hes
with charachange


"Emi semble pensive, semblant prendre la question au sérieux."


"Après une longue et profonde pause, elle parle."

show emi basic_closedsweat
with charachange


emi "Aucune idée."


"Bah, au moins elle est aussi perdue que moi."

stop music fadeout 4.0

show emi excited_happy
with charachange


emi "Dis Hisao, tu viens à la rencontre d’athlétisme, hein ?"


"La question sortant de nulle part me prend par surprise."


hi "Euh... Je sais pas encore."

show rin basic_absent
show emi sad_annoyed
with charachange


emi "Honnêtement, Hisao, après tout le mal que je me suis donné à te laisser courir avec moi ce matin, tu ne viendrais même pas à une rencontre d’athlétisme ?"

show rin basic_awayabsent
with charachange


"Ce n'était pas elle qui m'a demandé de courir avec elle ?"


"En fait, elle ne m'a pas vraiment donné le choix."


hi "Attends, non, je n'ai pas dit ça..."

play music music_ease fadein 3.0

show emi basic_closedgrin
show rin basic_absent
with charachange


"Elle s'illumine comme si je venais d'accepter de lui donner un million de dollars."

show emi basic_closedhappy
with charachange


emi "Alors tu viendras après tout ! C'est super !"


"Je n'ai pas dit ça non plus !"

show rin basic_deadpan
with charachange


rin "J'irai aussi, alors je m'assurerai de sa venue, Emi."

show emi basic_grin
show rin basic_absent
with charachange


emi "Bonne idée, Rin ! Peut-être qu'on pourra prendre à manger ou quelque chose du genre après la rencontre ?"


"J'ai l'impression de m’être fait escroquer, mais pas par elles deux."


"Plus par une force extérieure, me poussant irrévocablement vers ma destinée."


"...Ou peut-être que je ne devrais pas lire de livres qui parlent autant de conspirations. Sinon je vais finir par parler comme Kenji."


"Enfin, j'imagine que je n'ai pas d'autre choix que d'y aller maintenant."


"Je ne crois pas que je pourrais supporter de les décevoir toutes les deux."


"Je n'en entendrais jamais la fin."


hi "C'est quand déjà ?"

show emi basic_annoyed
with charachange


emi "La semaine prochaine, bêta ! Je te l'ai dit il y a quelques jours."


hi "Non c'est faux."

show emi sad_shy
with charachange


emi "J'ai oublié ? Enfin, tu n'oublieras pas de venir, hein ?"


hi "Bien sûr que non ! Je mettrai même une note sur un calendrier et tout !"

show rin basic_lucid
with charachange


"Rin hoche sagement la tête."

show rin basic_deadpancontemplation
with charachange


rin "C'est probablement une bonne idée tu sais. Sauf si le temps change son cours."

show emi basic_confused
with charachange


emi "C'est possible ça ?"

show rin relaxed_nonchalant
with charachange


"Rin hausse les épaules sans conviction."

show rin negative_spaciness
with charachange


rin "Ce n'est pas encore arrivé, mais on ne sait jamais..."

show emi basic_closedgrin
with charachange


"Cette fois c'est Emi qui hausse les épaules."

show emi basic_closedhappy
with charachange


emi "On n'y pourra rien si ça arrive."


show rin basic_deadpannormal
with charachange


rin "Sauf si tu voyages dans le temps."


hi "Vous ne pensez pas vraiment que c'est possible, hein ?"

show emi basic_confused
with charachange


emi "Je ne crois pas... non ?"

show rin relaxed_nonchalant
with charachange


"Rin hausse encore les épaules. Ça semble être sa réponse de base pour tout."

show rin basic_deadpandelight
with charachange


rin "Je crois pas. Mais je me réserve le droit de changer d'opinion à n'importe quel moment."


"Pour Rin, cette phrase semble plausible, c'en est dérangeant."


"Le fait de réaliser ça me fait un peu peur."


"Je me demande si Emi a souvent cette sensation."

show emi basic_closedgrin
with charachange


"Si c'est le cas, elle ne le montre pas en tout cas. Elle se contente de hocher la tête."

show emi basic_grin
with charachange


emi "Comme prévu."

show rin basic_deadpanupset
with charachange


rin "Qu'est-ce que ça veut dire ?"

show emi sad_grin
with charachange


"Cette fois, c'est Emi qui hausse les épaules."


"C'est comme si elle utilisait les propres armes de Rin contre elle."

show emi excited_proud
with charachange


emi "Ta réponse est le genre de chose à laquelle je m'attendais de ta part, c'est tout."

show rin negative_worried
with charachange


rin "Je suis vraiment aussi prévisible ?"

show emi basic_closedgrin
with charachange


"Le sourire d'Emi approche le jubilement."


emi "Nan, c'est juste que ton imprévisibilité est assez prévisible."

show rin relaxed_nonchalant
with charachange


rin "Ah bah ça va alors."

play sound sfx_warningbell


"Je n'ai pas la chance de savoir si Rin était sérieuse ou non, la sonnerie retentissant."


"Je n'ai pas vu le temps passer."


"Être avec elles deux était bien trop intéressant."

show emi basic_shock
with vpunch


"Emi bondit, une expression de panique sur le visage."


emi "Oh non ! J'avais besoin de passer par ma chambre pour prendre mon cahier pour le cours suivant !"

show rin basic_deadpandelight
with charachange


rin "Tu n'aimerais pas avoir une machine à remonter le temps maintenant ?"


"Rin semble assez fière d'elle en disant ça, comme si elle venait de gagner le débat."


"Emi ignore le commentaire de Rin."

show emi basic_hes
with charachange


emi "Désolée Hisao, mais tu pourras t'occuper de jeter les emballages ?"

show emi basic_closedsweat
with charachange


emi "Je nettoie moi-même d'habitude, mais je dois me dépêcher !"


hi "Ouais, pas de problème."

hide emi
with easeoutleft


"Emi fonce avec une rapidité à laquelle je pouvais m'attendre de sa part."

hide rin
with charaexit


"Je n'ai pas pris la peine de demander pourquoi Rin ne pouvait pas aider. Elle semble être déjà préoccupée par quelque chose d'autre."


"Elle est sûrement habituée à ce qu'Emi fasse le rangement, et je doute qu'Emi ait déjà pris la peine d'en discuter avec elle."


"Il ne me faut pas longtemps pour tout ranger, alors j'ai largement assez de temps pour jeter ce qui doit l'être et aller en classe."

stop ambient fadeout 1.0

scene bg school_scienceroom
with locationskip


"Misha m’accueille avec un signe de la main et un sourire sournois alors que je franchis la porte."

show misha cross_grin at center
with charaenter


mi "Je ne t’ai pas vu à la cafétéria, Hicchan."


hi "Ouais, je trouvais que c'était trop bondé."

show misha hips_grin
with charachange


"Le sourire de Misha s'élargit encore."


mi "Oh vraiment ? Tu es sûr que tu n'avais pas un petit ren—dez—vous ?"


hi "Q... quoi ? De quoi tu parles ?"

show misha sign_smile
with charachange


mi "Tu étais sur le toit, hein ? Avec Rin et Emi, rien de moins ! Casanova, va !"


hi "On... on a juste déjeuné, c'est tout !"

show misha cross_laugh
with charachange


"Misha éclate de rire, attirant l'attention de plusieurs de mes camarades de classe."


mi "Wahahaha ! Tu es tellement adorable quand tu rougis comme ça, Hicchan !"

show misha cross_grin
with charachange


"Elle m'adresse un clin d’œil complice."

show misha cross_smile
with charachange


mi "Ne t’inquiète pas, ton secret est en sécurité avec moi."


hi "Il n'y a pas de secret !"

show misha perky_confused
with charachange


mi "Oh ?"


"Misha semble déçue et s'illumine à nouveau."

show misha hips_grin
with charachange


mi "C'est le temps qui le dira~ !"


"Je ne sais pas de quoi elle parle, mais heureusement notre professeur arrive et le cours commence."

stop music fadeout 2.0




label fr_E5:

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell


"Et enfin, un autre jour de classe touche à sa fin."


"Je ne m'y attendais pas, mais j'ai réussi à rester éveillé toute la journée."


"Je suis presque sûr que ça peut compter comme un miracle."


"Mes jambes ne semblent pas avoir envie de me porter."


"Courir m'a vraiment éreinté."

scene bg school_hallway3
with locationchange


"Je parcours le couloir et arrive jusqu’à ma chambre."

scene bg school_dormhisao
with locationskip


"Je m'assois et fais lentement mon travail sans conviction, comme un vautour qui picore une carcasse peu savoureuse."


"Il sait que c'est ce qu'il mange, mais il n'est pas sûr de ne pas vouloir commander à livrer plutôt."


"Je ne crois pas pouvoir le faire, mais il est important que mon travail soit fait."


hi "Maintenant voyons voir... qu'est-ce que je suis censé faire déjà ?"


"Je sais que c'est un combat perdu d'avance, mais je me battrai quand même."


"Au milieu de mes devoirs de maths, je pose mon stylo."


"Je ne pourrai pas comme ça. J'ai besoin d'une distraction."


"Malheureusement, mes options sont vraiment limitées."


"Je ne suis pas d'humeur à lire."


"Kenji est, ce qui est étrange, hors de sa chambre."


"Si je vais au bureau du conseil des étudiants, je finirai par travailler pour elles."


"Et dieu seul sait où peut être tout le monde, sauf pour..."


"Bah, j'imagine que c'est une option viable."


"J'attrape mes chaussures et me dirige vers la piste. Emi est probablement là-bas."

play music music_tranquil fadein 3.0

scene bg school_track_ss
with locationskip


"Quand j'arrive, l’entraînement du club d’athlétisme vient de finir."


"Le soleil commence à descendre dans le ciel."


"Il est déjà aussi tard ?"

show emi basic_grin_gym_ss at center
with charaenter


emi "Qu'est-ce que tu fais ici, Hisao ?"

show emi excited_proud_gym_ss
with charachange


emi "Tu viens m'espionner, c'est ça ?"


"Je hausse les épaules. Pour être honnête, je ne sais pas vraiment pourquoi je suis là."


hi "Je n'avais rien de mieux à faire."


"Je pense que ça résume bien."


"À ce moment, Emi était la seule personne que j'ai eu l'idée d'aller voir."

show emi basic_annoyed_gym_ss
with charachange


emi "Alors je suis ton dernier recours, c'est ça ?"

show emi sad_angry_gym_ss
with charachange


emi "Y a personne d’intéressant, alors j'ai qu'à aller voir Emi, c'est ce que tu as pensé ?"


"Elle semble en colère."


"Une chance de l’embêter se présente à moi."


hi "Ouais, c'est un peu ça."

show emi sad_annoyed_gym_ss
with charachange


"Emi fait la moue, écarquillant les yeux pour ressembler le plus possible à un pauvre petit chiot."


hi "Une blague ! C'était une blague !"

show emi basic_closedgrin_gym_ss
with charachange


emi "Donc tu es bien là pour m'espionner !"


"Hein, quoi ?"


hi "C'est pas ce que je voulais dire !"


hi "Pourquoi est-ce que je t'espionnerais de toute façon ? Ce n'est pas comme si c'était nécessaire."


hi "Si tu ne dors pas et que tu n'es pas en classe, tu es ici, hein ?"


"Emi rit au commentaire."

show emi basic_happy_gym_ss
with charachange


emi "Bon, tu n'as pas tellement tort - mais tu as oublié quand je mange aussi. Ça m'arrive tu sais."


"Je hoche la tête, lui concédant ça."

show emi sad_grin_gym_ss
with charachange


emi "Et puis je suis avec Rin des fois aussi... donc je ne suis peut-être pas si facile à espionner après tout."


hi "Qu'est-ce que vous faites ensemble ? Vous ne semblez pas avoir beaucoup en commun."

show emi basic_closedgrin_gym_ss
with charachange


"Elle met les mains sur ses hanches et affiche un air supérieur."

show emi basic_grin_gym_ss
with charachange


emi "C'est ce que tu crois. J'ai plein de hobbys cachés, tu sais."


hi "Oh vraiment ? Comme quoi ?"

show emi sad_grin_gym_ss
with charachange


"Emi penche la tête d'un côté, comme si elle essayait de se rappeler ce qu'elle fait de son temps libre."

show emi basic_closedgrin_gym_ss
with charachange


emi "Ben, Rin et moi on va faire du shopping des fois."


"Ça se tient. Emi est une fille après tout. Mais Rin ?"


hi "Rin vient avec toi ?"

show emi basic_grin_gym_ss
with charachange


emi "On passe généralement par le magasin d'art."


emi "Et elle aime bien le magasin de musique qui vend plein de trucs de musique bizarres."

show emi basic_closedhappy_gym_ss
with charachange


emi "Elle dit que ça l'aide à se concentrer."


"C'est plus logique dit comme ça."


hi "Je vois. D'autres hobbys cachés ?"

show emi excited_proud_gym_ss
with charachange


"Emi fait non du doigt."


emi "Eh bien eh bien, pourquoi est-ce que je te révélerais tous mes sombres secrets ? On se connaît à peine !"


"Quelque part je crois que c'est tout ce qu'Emi a comme hobbys."


"Malgré ça, je ne crois pas avoir eu la réponse à ma question."


hi "Même si tu as quelques hobbys, je ne vois toujours pas pourquoi tu traînes autant avec Rin."


hi "Je veux dire, elle est un peu bizarre, non ?"


"Ce commentaire fait éclater de rire Emi."

show emi basic_closedhappy_gym_ss
with charachange


emi "Ha ! Ça doit être la révélation de l'année !"


hi "Alors pourquoi ? Je veux dire, tu es à l'aise pour discuter et tout, alors je me suis dit que tu fréquenterais beaucoup de monde, mais je crois que je ne t’ai vue qu'avec Rin."

show emi sad_annoyed_gym_ss
with charachange


"Emi est sur la défensive. Bizarre."


emi "Hé, je fréquente plein de monde à part Rin ! Tu ne le vois juste pas parce que je ne suis pas dans ta classe."


hi "D'accord, mais ça ne m'explique toujours pas pourquoi tu fréquentes autant Rin."


"Je ne suis même pas sûr de vouloir le savoir."



"J'imagine que c'est parce que le déjeuner était vraiment étrange."

show emi basic_confused_gym_ss
with charachange


"Emi hausse les épaules, faisant très Rin-esque pendant un moment."

stop music fadeout 4.0


emi "C'est parce qu'on a la même vision des choses."


"Si on m'avait demandé ce qu'aurait pu être la réponse la moins probable, ç'aurait été ça."


hi "Comment ça ?"


emi "C'est comme..."

play music music_emi fadein 1.0

show emi basic_grin_gym_ss
with charachange


emi "Bon, Rin peint des trucs, ok ?"


hi "Ouais..."


"Je ne suis pas sûr de savoir où elle veut en venir."

show emi basic_closedgrin_gym_ss
with charachange


emi "Et bah moi, je cours."


hi "Et ?"

show emi basic_happy_gym_ss
with charachange


emi "Et... c'est pour ça qu'on est similaires."

hi "…"


hi "Tu m'as perdu."

show emi basic_annoyed_gym_ss
with charachange


"Emi fronce les sourcils, comme pour essayer de comprendre sa réponse."


emi "Ben, peut-être que c'est parce qu'on fait des trucs pour les mêmes raisons."


hi "Hein ?"

show emi sad_grin_gym_ss
with charachange


emi "Tu sais, on suit nos passions."


hi "Donc tu es passionnée par la course et Rin est passionnée d'art, c'est ça ?"


emi "Euh, je crois. Laisse-moi réfléchir..."

show emi basic_closedgrin_gym_ss
with charachange


emi "Eh bien, Rin m'a expliqué une fois, mais je ne sais pas si j'ai bien suivi."


"Pas surprenant. Je crois que les explications de Rin rendraient confus n'importe qui."

show emi basic_grin_gym_ss
with charachange


emi "Elle dit qu'on est toutes les deux à la recherche d'un extrême."


emi "Aussi, elle essaye toujours de trouver une nouvelle façon d'exprimer une sensation particulière ou un truc du genre."

show emi sad_grin_gym_ss
with charachange


emi "Et je cours à cause de la sensation que j'y trouve."


emi "Et vu qu'on ne permet à rien de nous ralentir, on a une connexion basée là-dessus."


hi "Comment ça “ralentir“ ?"

show emi basic_confused_gym_ss
with charachange


"Emi semble surprise et pointe ses jambes du doigt."


emi "Tu sais, parce que je suis une coureuse. Et que Rin est une peintre même sans bras."


emi "Alors on respecte la détermination l'une de l'autre."

show emi basic_closedhappy_gym_ss
with charachange


emi "Et c'est pour ça qu'on est souvent ensemble."

show emi sad_grin_gym_ss
with charachange


emi "Je crois."


"Bon, je ne suis pas sûr de comprendre... mais d’après l'expression confuse d'Emi, peut-être qu'elle non plus."


emi "Honnêtement, ce n'est pas quelque chose auquel je pense beaucoup."


emi "On s'entend bien - c'est tout ce qui importe vraiment."


"Elle n'a pas tort là-dessus."


"Une autre question me passe par la tête, et vu que je n'ai rien de mieux à faire, je la pose."


hi "Qu'est-ce qui a fait que tu t'es mise à courir, d'ailleurs ?"

show emi basic_closedgrin_gym_ss
with charachange


emi "Oh, je cours depuis que je suis toute petite !"

show emi basic_grin_gym_ss
with charachange


emi "Mon père était un coureur, et aussitôt que j'ai pu marcher, il a commencé à m'apprendre à courir."

show emi sad_grin_gym_ss
with charachange


emi "C'était notre truc père/fille, tu sais ?"

show emi sad_depressed_gym_ss
with charachange

stop music fadeout 10.0


emi "Notre hobby mutuel."


"Une ombre passe sur son visage, et je suis choqué de la voir... triste."


"Est-ce que quelque chose est arrivé entre eux deux ?"

show emi basic_shock_gym_ss
with charachange


emi "Mince, je n'ai plus beaucoup de temps."

show emi basic_closedsweat_gym_ss
with charachange


emi "Désolée, mais j'ai quelques tours à faire avant d'aller voir l'infirmier !"

play ambient sfx_emipacing

hide emi
with easeoutleft

$ renpy.music.set_volume(0.3, 1.0, channel="ambient")


"Elle court sur la piste, les cheveux au vent."


"J'ai l'impression qu'elle va beaucoup plus vite que ce matin."


"Alors qu'elle tourne sur la piste, j'aperçois son visage."

scene ev emi_run_face_zoomout_ss
with locationchange


"Elle est comme ce matin, si ce n'est qu'elle a les yeux un peu plus sévères."


"Elle a raison après tout."


"Je ne connais pas grand-chose d'elle."

scene bg school_track_ss
with locationchange


"Je la regarde courir un petit moment, et me lève pour retourner à ma chambre."


emi "Hé !"


"Elle voit que je pars et fait des signes pour attirer mon attention."


emi "N'oublie pas ! Même heure demain matin, compris ?"


hi "Compris."

stop ambient fadeout 2.0


"Je retourne à ma chambre."


"Les devoirs m’appellent."


label fr_E6:

scene bg school_track_ss
with None

scene bg school_dormhisao_ni
with shorttimeskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")


"Je n'arrive pas à dormir."


"Mon corps est fatigué, mais mon cerveau est éveillé, fixant le plafond dans ma chambre baignée par la nuit."


"J'essaye de trouver quelque chose à quoi penser, espérant pouvoir épuiser mon cerveau."


"La seule chose à laquelle j'arrive à penser est que je n'arrive pas à penser."


"Ça ne marche pas très bien."


"Je me demande si c'est un effet secondaire des médicaments, bien que ça me semble bizarre que ça prenne aussi longtemps à se manifester."


"Encore une fois, peut-être que je ne suis pas aussi habitué à mon nouvel environnement que j'aurais voulu le croire."


"Je ne sais pas ; pour une raison inconnue, je suis éveillé et ne devrais pas l’être."


"C'est ridicule."

play sound sfx_switch

scene bg school_dormhisao
with Dissolve(0.2)


"Ignorant la raideur de mon corps, je sors du lit et regarde mon horloge."


"Quatre heures du matin. La dernière fois que j'ai regardé il était seulement une heure, alors peut-être que j'ai un peu dormi."


"Je ne sais pas."


"Je mets quelques habits et sors de ma chambre."


"Une marche pourrait me faire du bien."

scene bg school_courtyard_ni
with locationskip


"Je suis surpris de la froideur de l'air comparé à la tendre chaleur du jour."


"Je peux presque voir mon souffle alors que je parcours le campus, attendant que le soleil se lève ou que je m'endorme."


"À ce point, les deux options m'iraient."

scene bg school_track_ni at left
with locationchange


"Je me retrouve à la piste d’athlétisme - où pour la première fois, Emi n'est pas en train de courir."


"Ce qui est normal ; il est trop tôt, même pour elle."


"Les sièges des gradins sont froids, mais dans cette situation-là, j'apprécie."

show bg school_track as overlay:
    left
    alpha 0.0
    linear 15.0 alpha 0.5
with None


"Le soleil commence à se montrer à l'horizon, et je suis tristement certain que je ne dormirai pas plus cette nuit."


"Les rayons légèrement renforcés du soleil commencent à me réchauffer, et je regarde la rosée sur le terrain commencer à lentement s’évaporer."


"Mon esprit se calme, un peu."

stop music fadeout 2.0

scene black
with shuteye

window hide

with Pause(3.0)

play sound sfx_rustling

window show hpunch


"Quelqu'un me secoue."


emi "Hé, réveille-toi !"


hi "Hein ? Où ? Quoi ?"

scene bg school_track
show emi basic_shock_gym_close at center
with openeyefast


"Je crois que je me suis endormi après tout."

show emi basic_annoyed_gym_close
with charachange


emi "Qu'est-ce que tu fais là ? Tu vas attraper un rhume !"

play music music_dreamy fadein 4.0


"Je me frotte le yeux et suis confronté à Emi, qui est penchée et me regarde avec une expression inquiète."


"Je suis toujours un peu dans le pâté, donc ma réponse sort en un murmure."


hi "Pouvais pas dormir. Regardé le soleil se lever."

show emi basic_confused_gym_close
with charachange


emi "On dirait quelque chose que dirait Rin."


"Je hausse les épaules et ressens la raideur que l'on ressent en dormant quelques heures sur un banc."


hi "Ah bon ? Je saurais pas dire."

show emi basic_grin_gym_close
with charachange


"Emi sourit un peu à ma réponse quelque peu bizarre."

show emi basic_closedgrin_gym_close
with charachange


emi "Donc, tu pouvais pas dormir, hein ? Alors il est évident qu'il va falloir courir encore plus aujourd'hui !"


"Même si je ne la connais que depuis une semaine, cette façon de gérer le problème fait vraiment très Emi-esque."


hi "Hé, mon corps est suffisamment épuisé après hier !"


hi "C'est mon esprit qui turbine, c'est tout."

show emi basic_confused_gym_close
with charachange


emi "Je vois pas la différence. Si tu cours suffisamment, ton cerveau sera fatigué aussi."


"Je m'interroge sérieusement sur l’intérêt de faire ça aussi tôt le matin."


"Je ne sais pas si mes notes me pardonneront d'épuiser mon cerveau comme ça."

show emi basic_closedgrin_gym_close
with charachange

with vpunch

show emi basic_closedgrin_gym
with charadistant


"Emi me relève du siège avec une force surprenante pour quelqu'un de sa taille."


emi "Allez maintenant Hisao ! On a du travail à faire !"


"Je ne sais pas vraiment si je suis prêt pour ça aujourd'hui, pour être honnête."


"Je veux dire, je n'ai pas beaucoup dormi... et ce que j'ai dormi je l'ai passé sur les gradins !"


hi "Je sais pas... je devrais vraiment courir ?"

show emi basic_annoyed_gym
with charachange


"Emi me fixe du regard."


"Bon sang."

show emi sad_annoyed_gym
with charachange


emi "De quoi est-ce que tu parles ? Bien sûr que tu devrais courir !"


emi "Comment est-ce que tu comptes renforcer tes articulations sinon ?"

show emi basic_annoyed_gym
with charachange


emi "Tu as dormi sur les gradins, nom de dieu !"


emi "La meilleure façon de faire partir cet endolorissement est de courir un peu."


emi "Maintenant arrête de te cacher dans les gradins et descends de là !"


"Je ne peux rien dire. Je suis sûr qu'elle me tuerait si je refusais."


"Je me lève et vais sur la piste."

scene bg school_track_on
with locationchange


"Le soleil réchauffe assez bien l'air."


"Emi et moi commençons à nous étirer, et je me retrouve encore une fois à éviter de la regarder."


"Si c'est ce que je dois voir tous les matins, je devrais être capable de m'y habituer."

show emi basic_annoyed_gym
with charachange


emi "Tu sais Hisao, ce n'est pas poli de fixer du regard comme ça."


hi "Je ne te fixais pas ! Je le jure !"


"Emi lève un sourcil et réfléchit pendant une seconde, comme si elle évaluait ma réponse."


"Il y a un bref moment où j'ai peur pour ma vie."

show emi basic_closedhappy_gym
with charachange


"Mais alors elle sourit et rit, secouant lentement la tête."

show emi basic_grin_gym
with charachange


emi "Tu n'avais pas à nier aussi vigoureusement, tu sais."

stop music fadeout 5.0


"En réponse, je claque des mains et change de sujet."


hi "Bon ! On s'est suffisamment étirés, non ?"

show emi sad_grin_gym
with charachange


"Emi hausse les épaules."


emi "Tu te sens étiré ? C'est vraiment en fonction de ce que tu ressens."


"Eh bien, je me sens prêt à courir, si c'est ce qu'elle veut dire."


hi "Ouais, je suis prêt."

show emi basic_grin_gym
with charachange


emi "Pareil qu'hier, d'accord ?"


emi "On va juste courir un kilomètre et demi à un rythme constant."

show emi basic_closedhappy_gym
with charachange


emi "Ne t’embête pas pour ta vitesse, occupe-toi juste de garder le rythme, d'accord ?"


hi "C'est toi la chef."

play music music_running fadein 0.5

show emi basic_grin_gym
with charachange

play ambient sfx_emijogging

hide emi
with charamoveoutleft

$ renpy.music.set_volume(0.5, 2.0, channel="ambient")


"Emi sourit encore une fois, et nous partons."

scene bg school_track_running
with Dissolve(2.0)

"…"

"…"


"Je crois que je vais mourir."


"On n'a même pas fini le premier tour que mes jambes sont en feu."


"Ma respiration est ponctuée de râles."


"Je peux sentir la transpiration sur mon sourcil, et on n'en est qu'à la deuxième boucle."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi basic_closedgrin_gym at left
with charamoveinleft


emi "Allez Hisao ! Tu as encore trois tours à faire !"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft


"Je ne peux pas le faire..."


"Je ne peux pas le faire."


"Je ne peux pas le faire !"


"Je crois que je vais vomir."


"Sans que je m'en rende compte, on est au second tour. Emi ne transpire même pas."


"Comment est-ce qu'elle peut faire ça sans effort ?"


"Sans que je sache pourquoi, je continue d'avancer."


"Elle est comme une machine."


"Troisième tour. Qu'est-il arrivé au second ?"

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi excited_proud_gym at left
with charamoveinleft


emi "Tu y es presque, Hisao !"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft


"Menteuse ! On en a encore deux !"


"Je ne peux rien faire."


hi "Je... ne... peux pas... le... faire."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi basic_annoyed_gym
with charamoveinleft


"Emi se retourne et commence à courir à l'envers."


"Son visage affiche une colère qui me surprend."

show emi sad_angry_gym
with charachange


emi "Ne dis jamais ça !"


emi "Si tu dis ça, tu as déjà perdu."

show emi sad_angry_gym at left
with charamove


emi "Continue d'avancer ! Si tu es en vie, tu peux continuer d'avancer, merde !"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft


"Whoa, grossier. On en est au quatrième tour maintenant."


"Elle a vraiment l'air de vouloir que je continue d'avancer."


"Mes jambes avancent. Avancent. Avancent. Elles me semblent si molles."


"Je suis dans la boue, ou dans de la mélasse, ou dans du goudron."


"Je ne peux pas continuer."


"Je vais continuer."

$ renpy.music.set_volume(1.0, 1.0, channel="ambient")

show emi basic_grin_gym at left
with charamoveinleft


emi "Dernière ligne droite, Hisao ! Donne tout ce que tu as !"

$ renpy.music.set_volume(0.5, 0.5, channel="ambient")

hide emi
with easeoutleft


"Je fais avancer mes jambes aussi vite que je peux."


"Elles refusent d'obéir."


"Pourtant, elles continuent d'avancer."


"Pourtant, je finis."

stop ambient fadeout 0.5

show emi excited_happy_gym at center
with charaenter

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")


emi "Et voilà, Hisao ! Je savais que tu pouvais le faire !"


"La colère qu'Emi affichait il y a un tour a disparu, et est maintenant remplacée par de la fierté."


"Elle est radieuse, comme si elle venait de gagner une médaille d'or."

scene bg school_track_on
show emi excited_happy_gym at center
with vpunch


"Je m’arrête brusquement et tombe sur les mains et les genoux, luttant pour respirer."


"Mon cœur bat plus fort qu'il n'a pu le faire depuis longtemps."

stop music fadeout 1.0

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)


"Je ne crois pas qu'il ait fait ça depuis..."

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)


"Oh non."

scene black
with shuteyefast

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)


"Calme-toi s'il te plaît."

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)


"Calme-toi, arrête de t'emballer."

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)


"Je tousse, et pour je ne sais quelle raison, un sourire se forme sur mon visage."

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)


"Alors c'est comme ça que je meurs, hein ?"

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)


"En essayant de prendre soin de ma santé ?"

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)


"Tellement ironique."

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.5)

play sound sfx_heartfast
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)


"Je suis prêt à abandonner."

play sound sfx_heartslow
show heartattack
with Dissolve (0.1)

hide heartattack
with Dissolve (0.8)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.8)

play sound sfx_heartslow
show heartattack alpha
with Dissolve (0.1)

hide heartattack
with Dissolve (0.2)


"Mais soudainement, mon cœur ralentit."


"Deux mains m'attrapent sous les bras et me relèvent."

scene bg school_track_on
show emi basic_confused_gym_close at center
with openeye


"Je lève les yeux et vois Emi se tenant devant moi, avec un mélange de joie et d’inquiétude."


emi "Debout !"

show emi sad_grin_gym_close
with charachange


emi "Allez, tu ne retrouveras jamais ton souffle comme ça."


"D'une certaine manière, j'arrive à me relever. J'essaye de lever les bras au-dessus de ma tête, mais ils sont de plomb."


"Je commence à marcher le long de la piste pendant qu'Emi reste près de moi, comme si elle avait peur que je tombe ou quelque chose du genre."


"Elle n'a peut-être pas tort."


"Je me sens horriblement mal, et le dis."

show emi basic_closedhappy_gym_close
with charachange


"Emi rit."

show emi basic_happy_gym_close
with charachange


emi "Mais tu as fini, non ?"

show emi basic_grin_gym_close
with charachange


emi "Tu as dit que tu ne pouvais pas, mais tu as pu."


emi "Ça n'a pas valu le coup ?"


"Je ne suis pas sûr, et n'ai pas vraiment assez de souffle pour le dire."


"Mais le petit sourire que j'ai eu tout à l'heure n'est pas parti."


"Peu importe si mon cœur est faible."


"J'ai survécu ce matin."


"Je survivrai peut-être demain, aussi."

scene bg school_track
with shorttimeskip

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")

play ambient sfx_emisprinting


"Dès qu'il est certain que je ne vais pas m’effondrer, Emi se met à sprinter."


"Je ne sais vraiment pas comment elle peut sprinter après avoir couru un moment, mais elle est dans un bien meilleur état physique après tout."


"Encore une fois, alors que je marche sur la piste, je ne peux pas m’empêcher de regarder Emi courir."



scene ev emi_run_face_zoomin
with locationchange


"C'est bizarre, mais elle est comme une personne différente quand elle utilise toute son énergie comme ça."


"La dernière fois j'ai remarqué ses yeux, mais cette fois c'est sa bouche qui retient mon attention."


"Elle n'a pas son sourire normal."


"Elle sourit quand même, mais c'est quelque peu pincé."


"C'est presque triste, comme si elle menait un combat perdu d'avance mais s'en moquait."


"Elle semble courir avec encore plus d'entrain, comme elle l'a fait hier."


"De la transpiration commence à couler le long de son visage, mais elle continue d'avancer."


"Sa bouche s'ouvre enfin quand elle ne peut plus faire passer suffisamment d'air par le nez."


"Alors qu'elle passe encore une fois devant moi, les jambes forçant, les bras bougeant en rythme, et ses lèvres légèrement entrouvertes..."


"Elle est magnifique."

stop ambient fadeout 2.0

scene bg school_track
with shorttimeskip

play music music_normal fadein 3.0
$ renpy.music.set_volume(1.0, 0.0, channel="ambient")


"Après qu'on ait tous les deux fait quelques tours de terrain pour baisser le rythme, Emi revient à son état normal."


"Sa transformation est terminée."

show emi basic_happy_gym at center
with charaenter


emi "Pas mal aujourd'hui, Hisao."


"Il y a presque de l'admiration dans sa voix."


hi "Comment ça ? Je me serais arrêté si tu ne m'avais pas crié dessus."

show emi sad_shyblush_gym
with charachange


"Emi rougit un peu, semblant embarrassée."


emi "Désolée pour ça, je ne peux juste pas... supporter de voir les gens abandonner."


emi "Surtout pour quelque chose comme ça."

show emi sad_grin_gym
with charachange


emi "Dire “Je ne peux pas continuer” alors que tu es en train de continuer en même temps est bête."


emi "C'est juste pour ça."


hi "Quoi, dire des choses bêtes ?"

show emi basic_annoyed_gym
with charachange


"Emi me tire la langue."


emi "Idiot. Montrer que tu es en vie."


"Montrer que je suis en vie, hein ? Je ne savais pas que ça devait être aussi douloureux."


"Mais ça fait quand même du bien."

show emi excited_proud_gym
with charachange


emi "Et puis en plus, c'est un des jours les plus durs."


hi "Comment ça ?"

show emi basic_grin_gym
with charachange


emi "À chaque fois que tu commences à t’entraîner, c'est difficile le premier jour, vraiment dur le second jour, et plus facile le troisième."


emi "Tu auras encore des jours qui seront vraiment durs, mais ils arriveront de moins en moins souvent."


hi "Donc ça finira par devenir vraiment facile, hein ?"

show emi basic_closedhappy_gym
with charachange


emi "Ouais, bien sûr."

show emi basic_closedgrin_gym
with charachange


emi "Mais alors là tu auras à augmenter la difficulté, sinon tu ne progresseras jamais."


emi "Tu feras ça trop facilement et perdras le sentiment d'accomplissement."


hi "Donc j'aurai à courir plus que quatre tours, hein ?"

show emi excited_proud_gym
with charachange


emi "Yep ! Mais pas avant un moment - tu dois faire attention, tu sais."


"Une pensée frappe Emi, et son visage s'illumine."

show emi basic_closedhappy_gym
with charachange


emi "J'ai compris !"


hi "Compris quoi ?"

show emi basic_happy_gym
with charachange


emi "Tu peux venir avec moi pour voir l'infirmier ! Comme ça tu ne t'effondreras pas raide mort ou quoi que ce soit !"


"Vraiment charmant."


hi "Hum... quand ?"

show emi basic_grin_gym
with charachange


emi "Tout de suite, bien sûr ! Tu vas avoir besoin de prendre une douche et tout, hein ? On n'a pas beaucoup de temps alors !"


"M'attrapant la main, elle part, m’entraînant avec elle."

stop music fadeout 2.0


label fr_E7:

scene bg school_nurseoffice
show nurse neutral at center
with shorttimeskip


nk "Ma foi, tu es bien pressée aujourd'hui, hein Emi ?"

play music music_nurse fadein 2.0


"Je n'ai aucune idée de comment on est arrivés aussi vite au bureau de l'infirmier, mais nous y voilà."

show nurse neutral at twoleft
show bg school_nurseoffice at bgleft
with charamove

show emi basic_grin_gym at tworight
with charaenter


"L'infirmier sourit à Emi et semble m'ignorer complètement."

show nurse grin
with charachange


nk "Tu as largement assez de temps pour prendre une douche et aller en classe, tu sais."

show nurse concern
with charachange


nk "Il n'y a pas besoin que tu coures dans les couloirs comme ça. Je pouvais t'entendre à un kilomètre !"


"D'une certaine façon, je ne crois pas qu'il soit vraiment en train de réprimander Emi."


"On dirait que c'est une sorte de routine entre eux deux."


"Emi fait une assez mauvaise imitation d'une expression de remords."

show emi excited_sad_gym
with charachange


emi "Je suis désolée ! Je ne le ferai plus !"

show nurse grin
show emi basic_closedhappy_gym
with charachange


"L'infirmier et Emi rigolent tous deux à leur blague perso."

show emi basic_grin_gym
show nurse neutral
with charachange


"Soudainement, on dirait qu'il me remarque."

show nurse fabulous
with charachange


nk "Ah, bonjour Hisao."

show nurse neutral
with charachange


nk "Qu'est-ce qui t’amène ici ?"


hi "Eh bien, j'ai—{w=.3}{nw}"

show emi basic_closedgrin_gym
with charachange


emi "Hisao m'a officiellement rejointe durant mes courses matinales."


"Je commence à expliquer, mais Emi m’interrompt."

show emi basic_happy_gym
with charachange


emi "J'ai pensé qu'il pourrait avoir besoin de venir te voir pour qu'il ne meure pas ou autre."

show nurse fabulous
with charachange


"L'infirmier lève un sourcil à la remarque d'Emi."


nk "Oui, ça me ferait perdre mon job assez vite, dit comme ça, hein ?"

show nurse neutral
show emi basic_grin_gym
with charachange


nk "Bon alors Hisao, voyons voir ton état."


nk "Soulève ton t-shirt s'il te plaît."


"Je suis soudainement conscient du fait qu'Emi est dans la pièce et rougis un peu."


"L'infirmier semble remarquer mon manque d'aise et s'en amuse."

show nurse grin
with charachange


nk "Un peu timide, hein ?"


"Il se penche pour s'excuser envers Emi."


nk "Désolée Emi, j'ai essayé de t'offrir un show gratuit, mais ça n'a pas marché."

show emi basic_annoyed_gym
with charachange


"Emi se raidit légèrement et jette un regard énervé à l'infirmier."


emi "T'es con."

show emi excited_proud_gym
with charachange


"Emi se penche pour s'excuser auprès de moi."


emi "J'attendrai dehors, d'accord Hisao ?"

hide emi
with charaexit

show nurse grin at center
show bg school_nurseoffice at center
with charamove


"Je commence à baragouiner que ce n'est pas bien grave, qu'elle n'a pas à partir, mais elle est déjà sortie et l'infirmier rit en la voyant s'en aller."

show nurse fabulous
with charachange


nk "J'en suis encore capable ! Ha !"


hi "Je ne comprends pas."

show nurse grin
with charachange


"Il rit encore, comme s'il y avait une blague à mes dépens."


nk "J'arrive encore à l’embarrasser et à l’énerver. C'est une compétition qu'on a depuis un moment déjà."


"C'est assez moche dit comme ça, et on dirait qu'il s'en rend compte aussi."

show nurse concern
with charachange


nk "Erh. C'est assez mal sorti, en y repensant."


hi "Je ne comptais pas dire quoi que ce soit..."


nk "Non non, tu as raison. Je devrais te mettre au courant pour que tu ne te fasses pas une mauvaise idée de la chose."

show nurse neutral
with charachange


nk "Je suis assez nouveau ici, en fait. J'ai été engagé l'année où Emi est arrivée ici."


nk "Avant ça, j'ai travaillé avec Emi pendant sa réhab à la suite de son accident."


"Woaw, quoi ?"

show nurse concern
with charachange


nk "On a dû lui amputer les jambes après un accident de voiture assez violent. Ça l'a presque tuée, et a réussi à—"


"Il s'interrompt brusquement. Je cligne des yeux après avoir reçu autant d'informations imprévues."


nk "Bah, ce n'est pas à moi de raconter tout ça. Bref, on se connaît depuis un bon moment."


nk "Donc on a une relation légèrement plus familière que celle qu'aurait un élève avec un infirmier."


"Il semble embarrassé, comme s'il avait fait quelque chose de stupide."


"On dirait qu'il est vraiment inquiet pour ça. Je lui fais un signe pour lui dire que ce n'est pas important."


hi "Ne vous inquiétez pas, monsieur. Je promets d’être discret."


"Je me demandais comment Emi avait perdu ses jambes, et c'est un des scénarios auxquels j'ai pensé."


"Il y avait tellement de façons différentes pour que ce soit arrivé, mais entendre vraiment les faits... c'est toujours un peu choquant."

show nurse neutral
with charachange


nk "Bon, merci. Tu es un bon garçon, Hisao."


nk "Je peux comprendre pourquoi Emi est devenue amie avec toi."

show nurse fabulous
with charachange


nk "Elle est indomptable, tu sais."


hi "Comment ça ?"


nk "Tu ne l'as pas vue apprendre à marcher. Elle continuait pendant bien plus longtemps que les autres à l’hôpital. Elle refusait d'abandonner."


nk "Normalement il faut des années pour arriver au point où tu peux envisager de courir. Emi a réussi à le faire en une année."


"Il est presque fier d'elle, comme un père qui regarde sa fille gagner une compétition."

show nurse neutral
with charachange


nk "Bah, elle aurait sûrement réussi encore plus vite si on ne l'avait pas empêchée."


hi "Empêchée ? Pourquoi ?"

show nurse concern
with charachange

stop music fadeout 4.0


nk "Parce qu'elle continuait tellement longtemps que ses jambes commençaient à saigner là où frottaient ses prothèses."


nk "C'est une vraie inquiétude - c'est pour ça qu'elle vient chaque jour après avoir couru."


nk "Sans parler du risque d'infection si ses jambes se coupent et que ses prothèses sont sales."

show nurse neutral
with charachange


nk "Mais assez parlé de ça."

show nurse fabulous
with charachange

play music music_nurse fadein 2.0


nk "Si tu ne sors pas vite, Emi va penser qu'on fait quelque chose."


"En disant ça, il m'adresse un clin d’œil et commence à écouter mon cœur."


"Le stéthoscope est trop froid."


"Il aurait vraiment dû le réchauffer avant de l'utiliser."


"Après quelques instants il se radosse, satisfait."

show nurse neutral
with charachange


nk "Eh bien, ça me semble assez bon, Hisao. Tu n'as pas eu de douleur à la poitrine pendant que tu courais, hein ?"


hi "Non, pas vraiment. J'ai eu du mal à reprendre mon souffle cela dit - et mon cœur battait très vite à la fin, aussi."

show nurse concern at center
with charachange


"L'infirmier fronce les sourcils, puis hausse les épaules."

show nurse neutral at center
with charachange


nk "C'est probablement parce que tu n'es pas en forme... mais si ça ne s’améliore pas, alors tu dois me le faire savoir, hein ?"


nk "Ne te force pas trop - et bien sûr si tu as une douleur à la poitrine, viens me voir immédiatement, d'accord ?"


"Je remets mon t-shirt, et l'infirmier passe la tête dans le couloir pour appeler Emi."

show nurse neutral at twoleft
show bg school_nurseoffice at bgleft
with charamove

show emi basic_annoyed_gym at tworight
with charaenter


emi "Qu'est-ce qui vous a pris aussi longtemps ? Maintenant je vais être en retard !"

stop music fadeout 2.0

show nurse fabulous
with charachange


"L'infirmier m'adresse un regard appuyé."

show nurse grin
with charachange


nk "Je draguais Hisao, c'est tout."

play music music_comedy fadein 0.5

show emi sad_annoyed_gym
with charachange


emi "Quoi ?! Roh, qu'est-ce que je t’ai dit sur le fait de draguer mes amis ?"


"Je m'attendais à ce qu'Emi soit choquée par sa remarque, mais à la place elle semble énervée, réprimandant l'infirmier comme s'il était un enfant qui avait volé des cookies."


"Pendant ce temps, j'essaye de ne pas rougir à l'insinuation de l'infirmier."

show nurse fabulous
with charachange


nk "J'essayerai de ne pas le refaire, mais j'ai bien peur que le jeune Hisao soit à tout jamais perdu pour le genre féminin !"

stop music fadeout 0.5


hi "C'est pas prêt d'arriver."

with Pause(3.0)

play music music_comedy fadein 0.5

show nurse grin
show emi excited_laugh_gym
with charachange


"Je ne voulais pas dire ça à voix haute, mais l'infirmier et Emi me regardent un instant avant d’éclater de rire à nouveau."

show emi basic_happy_gym
with charachange


emi "Je t'avais dit qu'il était drôle, hein ?"


"Huh. Apparemment Emi parle de beaucoup de choses avec l'infirmier."

show nurse fabulous
show emi basic_grin_gym
with charachange


nk "Eh bien Hisao, tu devrais peut-être te dépêcher, tu dois encore prendre une douche avant le début des cours, non ?"


"Zut ! Il a raison, et il ne me reste qu'une demi-heure !"


hi "Merci pour votre temps. À plus tard Emi !"

scene bg school_nursehall
with locationchange

stop music fadeout 5.0


"Je me précipite hors de la salle alors que l'infirmier commence à enlever les prothèses d'Emi."


"Alors que je suis dans le couloir, je peux encore entendre sa voix."


nk "Emi, tu dois faire plus attention..."

scene bg school_dormhisao
with locationskip


"Je retourne à ma chambre et me douche en un temps record. Je réalise que je suis debout depuis déjà quatre heures, et que les cours n'ont même pas encore commencé."


"Ça va être une très, très longue journée."


"J’espère que je ne vais pas m'endormir en classe."

$ suppress_window_after_timeskip = True

scene black
with dissolve


label fr_E8:

window hide None

scene black
with dissolve

show bg school_dormhisao
with openeye

window show

play music music_pearly fadein 5.0


"Le soleil levant du matin passant par ma fenêtre me réveille à la place de mon alarme, et je réalise qu'on doit être dimanche."


"Emi a gentiment daigné me donner les week-ends."


"Je ne sais pas si je me suis réveillé hier ou si j'ai juste dormi toute la journée."


"Mes jambes protestent alors que je sors du lit."


"Cette course m'a vraiment exténué."


"Cela dit, je ne peux pas nier qu'Emi avait raison."


"C'est devenu un peu plus facile."


"J'étais inquiet du fait que courir finisse par me taper sur les nerfs, mais jusque-là ça ne m'a pas vraiment gêné."


"Enfin, ça fait juste une semaine."


"J'ai encore bien l’occasion de maudire le son de mon alarme le matin."


"Pas que je puisse arrêter maintenant."


"Comme l'a dit Emi, c'est plus difficile d’arrêter quelque chose quand tu le fais avec quelqu'un d'autre."


"Et franchement, je ne pense pas pouvoir me confronter à une Emi déçue."


"Elle me ferait probablement ses yeux de chiot malheureux et je me sentirais mal."


"Ce qui me rappelle... je n'avais pas quelque chose de prévu aujourd'hui ?"

$ renpy.music.set_volume(0.3,2.0,channel="music")

scene bg school_track_fb
show emi basic_closedhappy_gym_fb at center
show noiseoverlay
with flashback


emi "Dis, tu viens à ma rencontre d’athlétisme dimanche, hein ?"

show emi basic_grin_gym_fb
with charachange


emi "Pourquoi je demande, bien sûr que tu viens."

show emi sad_grin_gym_fb
with charachange


emi "Hein ?"


"Encore ces yeux de chiot malheureux."


hi "Bien sûr que je viens !"


hi "Je te le dois bien, hein ?"

show emi excited_proud_gym_fb
with charachange


emi "Exactement ! Alors n'oublie pas, d'accord ?"

$ renpy.music.set_volume(1.0,2.0,channel="music")

scene bg school_dormhisao
with flashforward


"Zut, la rencontre d’athlétisme d'Emi !"


"Je ferais mieux de me dépêcher si je ne veux pas louper sa course, vu que c'est la seule raison pour que j'aille à la rencontre de toute façon."


"Louper sa course enlèverait tout intérêt d'y aller."

scene bg school_courtyard
show crowd
with shorttimeskip

play ambient sfx_crowd_outdoors fadein 3.0


"Et donc, je me retrouve vite entouré par une foule de gens, tous sortis pour voir notre équipe d’athlétisme en compétition avec une autre école comme la nôtre."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear

nvl show dissolve


n "\nJe l'avoue, c'est presque rassurant de savoir qu'on n'est pas la seule école comme ça."


n "Après avoir vu qu'il y a {b}deux{/b} écoles avec des étudiants... déficient..."


n "...Tu te sens moins déficient."


n "Tu ne te sens plus unique aussi, ce qui dans la plupart des cas serait une mauvaise chose, mais dans celui-ci ne l'est franchement pas."


n "Ça fait partie des avantages de Yamaku, je pense."


n "Apprendre que tu n'es pas unique - même apprendre qu'il y a beaucoup de personnes qui tueraient pour avoir ton problème au lieu du leur."


n "Certains ici ne sont pas là parce qu'il leur manque une jambe ou qu'ils ont un problème au cœur."


n "Certains d'entre eux sont sûrs d’être morts dans deux, voire trois ans s'ils ont de la chance."


n "Et ça c'est seulement s'ils ont le traitement pour."


n "C'est un réconfort assez mince de pouvoir dire : “Bon, au moins j'ai eu la chance de faire le lycée.” C'est triste."

$ renpy.music.set_volume(1.0, 2.0, channel="ambient")
$ renpy.music.set_volume(1.0, 2.0, channel="music")
nvl clear

nvl hide dissolve

window show

stop music fadeout 3.0


"Je suis sorti de ma torpeur morbide par l'apparition de Rin près de l'entrée des gradins."

show rin basic_deadpannormal at center
with charaenter


rin "Tu es venu."


hi "Bien sûr. Je l'avais dit, non ?"

show rin basic_deadpanamused
with charachange


rin "Ça ne veut pas forcément dire que tu devais être là tout le long."

show rin basic_awayabsent
with charachange


rin "Beaucoup de gens disent des choses sans avoir l'intention de les faire."


hi "Eh bien ce n'est pas mon cas."

play music music_soothing fadein 0.5

show rin relaxed_boredom
with charachange


"Rin hausse les épaules. Semblant ennuyée par la conversation, elle tourne les talons et se dirige vers les stands."


rin "Je dois de l'argent à Emi maintenant."


hi "Pourquoi ça ?"

show rin basic_absent
with charachange


rin "Je ne pensais pas que tu viendrais."


rin "Emi le pensait."

show rin basic_awayabsent
with charachange


rin "Alors je lui dois 500 yen."


hi "Vous pariez beaucoup quand même, hein ?"


"Et un autre haussement d'épaules de la part de ma camarade sans bras."


show rin basic_deadpan
with charachange


rin "Je ne trouve pas."

scene bg school_track
show crowd
show rin basic_deadpan
with locationchange


"On arrive dans les gradins, et Rin lève la tête."

show rin negative_spaciness at center
with charaenter


rin "Là-haut."

show rin basic_deadpancontemplation
with charachange


rin "Je suis sortie pour voir si tu viendrais."


"Pour le pari, je suis sûr."


"Rin ouvre la marche, et peu après on s'assoit sur un banc presque désert."

$ renpy.music.set_volume(0.3, 3.0, channel="ambient")

show rin basic_deadpancontemplation at tworight
show bg school_track at bgright
show crowd:
    linear 1.0 alpha 0.0
with charamove

hide crowd
show meiko smile at twoleft
with charaenter


"Il y a une femme plus âgée assise à côté de Rin - la mère de quelqu'un j'imagine."


"Elle a les cheveux assez longs et tressés. En voyant Rin, elle lui adresse un sourire qui me semble familier."

show meiko happy
with charachange


emm_ "Eh bien, voilà qui est surprenant."

show meiko wink
with charachange


emm_ "Je pensais que tu allais chercher un snack, pas un garçon."


hi "Hein ?"

show rin basic_surprised
with charachange


rin "Un snack ?"

show rin relaxed_nonchalant
with charachange


rin "Je me demandais pourquoi j'étais descendue."

show meiko happy
show rin basic_awayabsent
with charachange


"La femme rit, encore une fois d'une façon qui m'est familière."


"Où est-ce que je l'ai déjà vue ?"

show meiko smile
with charachange


emm_ "Eh bien, je pense que tu as toujours été le genre de personne à aller chercher quelque chose et revenir avec quelque chose d'autre."


emm_ "Mais je suis impolie ! Je ne me suis pas encore présentée."


emm_ "Je suis Meiko Ibarazaki, la mère d'Emi."

show meiko happy
with charachange


emm "Enchantée."


"Ah bah, voilà qui explique tout."


"C'est comme une version plus grande, plus âgée, et mieux formée d'Emi."


"À part ses cheveux qui sont plus foncés que ceux d'Emi, la ressemblance est vraiment flagrante."

show rin basic_absent
show meiko smile
with charachange


hi "Oh pardon, je suis Hisao. Hisao Nakai."


hi "Et vraiment, vous n'avez pas à vous excuser de ne pas vous être présentée, madame Ibarazaki."


hi "Ce devrait être le travail de Rin dans cette situation, n'est-ce pas ?"

show meiko happy
show rin basic_awayabsent
with charachange


"La mère d'Emi rit encore une fois."


emm "Je vois que tu ne connais pas Rin depuis très longtemps."

show meiko smile
with charachange


emm "Il est mieux de ne pas attendre de Rin quelque chose comme ça."

show meiko wink
with charachange


emm "Elle a d'autres choses en tête, je dirais."

show rin basic_deadpannormal
with charachange


"Rin hoche la tête, semblant approuver cet avis."

show rin basic_deadpan
with charachange


rin "Elle a raison."

show rin basic_lucid
with charachange


rin "Je pensais aux couchers de soleil."

show meiko happy
show rin basic_awayabsent
with charachange


emm "Tu vois ? On n'a pas d'autre choix que de nous présenter nous-mêmes."


"En manque de meilleure réponse à fournir, je hoche la tête."


"Mme Ibarazaki se radosse un peu à son siège et lève un sourcil."

$ renpy.music.set_volume(0.0, 0.5, channel="ambient")

show meiko serious
with charachange

stop music fadeout 0.8


emm "Donc, depuis quand est-ce que Rin et toi sortez ensemble ?"


"Je n'ai qu'un silence en réponse alors que mon cerveau se met en route. Mais juste avant que je puisse trouver quelque chose à dire, la mère d'Emi éclate de rire une nouvelle fois."

play music music_soothing fadein 0.5
$ renpy.music.set_volume(0.3, 0.5, channel="ambient")

show meiko happy
with charachange


emm "Ha ! Tu es du genre à rougir, hein ?"


"Je ne sais pas s'il y a un moyen pour que je garde ma dignité dans cette situation, alors je choisis de marmonner une réponse."

show meiko smile
show rin basic_absent
with charachange


hi "Peut-être."

show rin basic_awayabsent
with charachange


emm "Donc ça doit être tout nouveau entre vous, hein ?"

show rin basic_absent
with charachange


hi "Non, ce n'est pas à cette question que—"

show meiko happy
show rin basic_awayabsent
with charachange


"Un autre rire."

show meiko smile
with charachange


emm "Je sais, mais c'est drôle de te voir embarrassé."

show meiko wink
with charachange


emm "Je suis désolée. Pardonne une vieille femme qui s'amuse."


"Vieille femme ?"


"Elle ne me semble pas si âgée."


"Clairement Emi tient ses traits juvéniles de sa mère."

show rin basic_absent
with charachange


hi "Je peux le pardonner."

show meiko happy
show rin basic_awayabsent
with charachange


emm "Comme c'est gentil à toi."

stop music fadeout 6.0

show rin basic_deadpan
with charachange


rin "Ça commence."

stop ambient fadeout 2.0

scene ev emitrack_blocks at Fullpan(12.0, dir="left", time_warp=_ease_in_time_warp)
with locationskip


"Je dirige mon attention sur la piste, où se préparent les participants pour le premier sprint."


"On dirait que c'est le 400 mètres."


"Je passe en revue les coureurs et vois Emi."

scene ev emitrack_blocks_close
with flash


"Elle sourit, semblant presque sûre d'elle."

show insert startpistol at right
with easeinright


"Le starter lève son pistolet."

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")

play sound sfx_startpistol
play ambient sfx_emisprinting

scene ev emitrack_running at Fullpan(1.0, dir="left", time_warp=_ease_in_time_warp)
with silentflash


"Emi explose presque en partant, disparaissant des starters, devenant comme floue."


"C'est incroyable. Même alors que les autres sprinters convergent en se rapprochant de la ligne du milieu, Emi reste devant tout le monde."


"Au moment où elle prend le dernier virage, d'autres coureurs la rattrapent."


"Leurs efforts restent cependant vains, puisque dans une dernière accélération, Emi finit avec au moins une demi-seconde d'avance."

scene ev emitrack_finishtop:
    xalign 0.5 yalign 0.0 zoom 4.0 subpixel True
    0.2
    linear 0.3 zoom 1.05
    easein 8.0 zoom 1.0
with flash

stop ambient fadeout 1.0
play sound sfx_crowd_cheer


"Mme Ibarazaki crie et applaudit très fort, et semble contente comme n'importe quel autre parent encourageant son enfant."


"Emi bondit sur place, semblant contente d’elle-même."

scene bg school_track at bgright
show meiko happy at twoleft
show rin basic_deadpandelight at tworight
with locationchange

play music music_daily fadein 2.0


"J'applaudis avec le reste des spectateurs."


"L'annonceur (dont la voix ressemble étrangement à celle de Misha) donne joyeusement les résultats."

show meiko smile
show rin basic_awayabsent
with charachange


emm "Je crois qu'elle est plus rapide que la dernière fois."

show rin basic_absent
with charachange


hi "C'était incroyable."

show meiko happy
show rin basic_awayabsent
with charachange


"Mme Ibarazaki sourit avec fierté."


emm "Emi est une fantastique coureuse."

show meiko smile
with charachange


"Nous ne disons plus rien alors que le prochain évènement se prépare."


"Je suis surpris de voir Emi se représenter sur la piste."

show rin basic_absent
with charachange


hi "Mais, elle ne vient pas juste de courir ?"


"La mère d'Emi hoche la tête."

show rin basic_awayabsent
with charachange


emm "Oui, mais elle court plusieurs fois pour l'équipe. Surtout les sprints."

show meiko happy
with charachange


emm "Ça fait beaucoup, mais Emi peut s'en sortir."


"D’après ce que je vois, elle a raison."


"Emi ne semble pas fatiguée, comme si elle n'avait pas couru du tout."


"S'il n'y avait pas de la transpiration visible sur son t-shirt, ça ne se verrait pas."

show rin basic_absent
with charachange


hi "C'est quelle course là ?"

show meiko smile
show rin basic_awayabsent
with charachange


emm "Le 200 mètres."


emm "Elle fera celui-ci, le 100 mètres, et le relais."

show rin basic_absent
with charachange


hi "Je vois."

show rin negative_spaciness
with charachange

play sound sfx_startpistol
play ambient sfx_emisprinting


"Encore une fois le pistolet résonne, et encore une fois Emi décolle comme une fusée."



"Un son de battement dévie mon attention de la course."


"C'est le pied de Rin."


"Elle semble complètement absorbée par la course."

show meiko happy
with charachange

stop ambient fadeout 1.0
play sound sfx_crowd_cheer


"La mère d'Emi applaudit encore une fois, et j'en déduis que la course est finie."


"Les sprints ne semblent pas durer très longtemps."


hi "Ton pied."

show rin relaxed_surprised
show meiko smile
with charachange


rin "Mmh ?"


hi "Ton pied tapait sur le banc."

show rin basic_deadpan
with charachange


rin "Oh."


hi "Tu sembles assez concentrée, je suis surpris."

show rin basic_deadpansurprised
with charachange


"Rin me regarde, intriguée."


rin "Pourquoi est-ce que je ne le serais pas ?"


hi "Sans raison, je pensais juste que le sport ne t’intéressait pas."

show rin relaxed_nonchalant
with charachange


rin "Mmh, tu dois avoir raison."


rin "Ce n'est pas si intéressant."

show rin basic_deadpannormal
with charachange


rin "Mais je regarde Emi, pas le sport."


hi "Je ne te suis pas."

show rin basic_lucid
with charachange


rin "Emi est la plus Emi-esque quand elle court."


rin "On n'a pas souvent l'occasion de voir Emi en tant qu'Emi très souvent."

show rin basic_deadpanamused
with charachange


rin "Mais là, tu peux. Tu vois ?"


"Elle dirige mon attention vers la piste, là où le 100 mètres est sur le point de commencer."

stop music fadeout 6.0
stop sound fadeout 2.0

scene ev emitrack_blocks_close
with locationskip


"Je regarde Emi avec attention."


"Alors qu'elle se positionne sur les starters, son corps entier semble se détendre, mais c'est une fausse relaxation."


"Je peux voir qu'elle est en fait comme un ressort."

scene ev emitrack_blocks_close_grin
with locationchange


"Alors que le starter dit aux coureurs de se préparer, sa tête se relève et ses yeux se plissent."


"Sa bouche se tord dans ce qui pourrait être le début d'un sourire ou d'un grognement."

play sound sfx_startpistol
play ambient sfx_emisprinting

scene ev emi_run_face_zoomin
with locationskip


"Quand le pistolet retentit, c'est comme si elle était relâchée d'une cage, comme si elle bougeait toujours à une vitesse hallucinante, mais qu'on ne pouvait le voir que lorsque le tir dissipe l'illusion d'immobilité."


"C'est fini en quelques secondes, mais pendant ces quelques secondes, j'ai l'impression d'avoir vu quelque chose de très personnel d'Emi."

stop ambient fadeout 1.0
play sound sfx_crowd_cheer


"Aussitôt qu'elle franchit la ligne d’arrivée, son expression revient à son sourire normal."


"Le général conquérant revient dans sa ferme."


hi "Impressionnant."


hi "Elle est vraiment impressionnante. Je ne l'ai jamais vue aller aussi vite."

scene bg school_track at bgright
show meiko smile at twoleft
show rin basic_deadpanamused at tworight
with locationchange


emm "Eh, ne me regarde pas, je suis bien trop relax pour courir aussi vite."

show meiko worry
show rin basic_awayabsent
with charachange


emm "Non, je crois que la prouesse d'Emi vient du côté de son père."


"À la mention du père d'Emi, Mme Ibarazaki semble troublée, presque triste."


emm "C'est lui qui l'a amenée à courir, tu sais."

show rin basic_absent
with charachange


hi "Ouais, elle me l'a dit."


"Je me demande si ce serait impoli de demander quelque chose sur le père d'Emi."


"Mais après l'expression qu'il y avait sur son visage il y a quelques jours, je me sens contraint de demander."


hi "Où est son père maintenant, si je peux me permettre ?"


"La mère d'Emi hésite, ne voulant clairement pas répondre mais ne voulant pas être impolie non plus."

show meiko serious
show rin basic_awayabsent
with charachange


emm "Il... n'est plus là."


hi "Je suis désolé, je ne voulais pas vous rappeler de mauvais souvenirs."

show rin basic_absent
with charachange


hi "C'est juste qu'Emi semblait un peu triste quand elle a mentionné son père l'autre jour."

show meiko worry
show rin basic_awayabsent
with charachange


emm "Ce n'est pas surprenant."


hi "Mmh ?"


emm "Ils étaient très proches."

show rin basic_absent
with charachange


hi "Je vois."

play sound sfx_cellphone


"Une sonnerie retentit de la poche de Mme Ibarazaki. Mettant sa main à l’intérieur, elle en ressort un téléphone portable et le regarde."

show meiko serious
show rin basic_awayabsent
with charachange


emm "...Sérieusement, des sms ?"


emm "Il a quel âge, seize ans ?"


hi "Mmh ?"

show meiko smile
with charachange


emm "Oh, ce n'est rien."

show meiko wink
with charachange


emm "Je dois aller rejoindre un ami."

show meiko happy
with charachange


emm "Tu pourras dire à Emi que je suis très fière d'elle et que je l’appellerai ce soir ?"

show rin basic_absent
with charachange


hi "Bien sûr."

hide meiko
with charaexit

show rin basic_absent at center
show bg school_track at center
with charamove

show rin basic_awayabsent
with shorttimeskip

play music music_tranquil fadein 2.0


"J’admets que je pense à autre chose pendant un moment."


"Je ne me rends même pas compte que le relais est sur le point de commencer. Mais quand je regarde, je ne trouve pas Emi."


hi "Je croyais qu'Emi devait faire le relais."

show rin basic_deadpan
with charachange


rin "Elle fait la ligne d'arrivée."

show rin basic_deadpannormal
with charachange


rin "Alors elle ne va pas courir avant un moment."


hi "Ah."

show rin basic_deadpandelight
with charachange


rin "Tu l'as vue ?"


hi "Hein ?"


rin "Emi en tant qu'Emi."


hi "Peut-être."

show rin basic_deadpanupset
with charachange


rin "Mmh. Peut-être cette fois."

play sound sfx_startpistol


"La course commence, et j'encourage l'équipe d'Emi alors qu'elles se passent le témoin."

play ambient sfx_emisprinting

scene ev emitrack_running:
    truecenter zoom 1.0 subpixel True
    ease 20.0 zoom 1.05 xalign 0.0 yalign 0.0
with locationskip


"Finalement, je vois Emi sprinter sur la piste pour être la dernière à prendre le témoin."


"Encore une fois je suis surpris de voir à quel point elle est gracieuse quand elle court."


"C'est vraiment magnifique."


"L'expression d'assurance et de détermination sur son visage ne fait qu'accentuer ça."


"Emi en tant qu'Emi, j'imagine."

stop ambient fadeout 1.0
play sound sfx_crowd_cheer

show ev emitrack_finish
with locationskip


"Mais alors qu'elle franchit la ligne d'arrivée, je la vois légèrement trébucher."


"Vraiment très peu, mais elle a trébuché."

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")

scene bg school_track
show rin negative_worried at center
with locationskip


"Rin inspire rapidement sur le coup, et semble inquiète pendant une seconde."


rin "Oh, Emi..."


hi "Tu crois qu'elle s'est fait mal ?"

show rin basic_surprised
with charachange


rin "Tu l'as remarqué toi aussi ?"

show rin negative_confused
with charachange


rin "C'est pas bon."

show rin negative_annoyed
with charachange


"Elle fronce les sourcils, comme si elle se décidait à faire quelque chose."


"Mais ça semble être trop fatiguant, et elle finit par hausser les épaules."

show rin basic_deadpanupset
with charachange


rin "Bon, allons-y."


rin "Il faut acclamer les vainqueurs."

show rin basic_deadpanamused
with charachange


rin "Essaye de trouver une couronne de laurier."


hi "Ça ne va pas être facile."

show rin basic_deadpannormal
with charachange


"Rin hausse les épaules."

show rin basic_deadpan
with charachange


rin "Au moins on a essayé."


"Enfin, on n'a pas essayé longtemps."


"Pas du tout même. M'enfin, peu importe."

stop music fadeout 5.0
stop sound fadeout 5.0
play ambient sfx_crowd_outdoors fadein 2.0

scene bg school_track_on
show crowd
show rin basic_awayabsent at center
with locationskip


"Emi est entourée par son équipe, acclamée pour sa course."


"Rin semble attendre qu'Emi remarque qu'elle est arrivée."


"Ouais, c'est pas comme si elle pouvait lui faire signe."



"Mais encore une fois, je ne suis pas sûr qu'Emi le ferait même si elle pouvait de toute façon."


"Ça ne lui ressemble pas vraiment d'attirer l'attention sur elle. Ou de réagir physiquement autrement qu'en haussant les épaules."


"Dans tous les cas, je n'ai pas envie d'attendre, alors je fais un signe à Emi, qui lève la tête et me sourit - erh, nous sourit."

show bg school_track_on at bgright
show crowd at bgright
show rin basic_awayabsent at tworight
with charamove

play music music_emi fadein 1.0

show emi basic_closedhappy_gym at twoleft
with charaenter


emi "Ah, tu es venu !"

show emi excited_proud_gym
with charachange


emi "Alors Rin me doit de l'argent, hein ?"

show rin basic_deadpanupset
with charachange


rin "On voulait apporter une couronne de laurier, mais Hisao n'a pas réussi à en trouver une."

show emi basic_grin_gym
with charachange


hi "Hé, toi non plus."

show rin basic_deadpan
with charachange


rin "Ce n'était pas à moi de chercher."


hi "Quand est-ce qu'on a désigné des rôles ?"

show rin basic_deadpannormal
with charachange


rin "Quand j'ai dit “Essaye de trouver une couronne de laurier”."

show rin basic_deadpandelight
with charachange


rin "Suis un peu."


"Je hausse les épaules. Rin doit déteindre sur moi."


hi "Apparemment c'est ma faute après tout, Emi."

show emi basic_closedhappy_gym
show rin basic_awayabsent
with charachange


"Emi rit devant Rin et moi."

show emi basic_happy_gym
with charachange


emi "C'est pas grave, je suis sûre que tu te rattraperas."

show rin basic_absent
with charachange


hi "Euh, bien sûr."

show rin basic_awayabsent
show emi excited_amused_gym
with charachange


emi "Bien ! Alors, j'étais comment ?"

show rin basic_absent
with charachange


"Je m’empêche de sortir “magnifique” ou “incroyable” et finis par dire “très impressionnante”."

show emi basic_closedgrin_gym
with charachange


"Emi semble contente de ma remarque."


"Je ne mentionne pas à quel point c'est impressionnant vu qu'elle n'a pas de jambes. Je crois qu'elle doit déjà le savoir."


"En plus, d'une certaine façon, j'ai l'impression que ça gâcherait ses efforts."

show emi basic_grin_gym
show rin basic_awayabsent
with charachange


emi "Contente de l'entendre ! J'étais inquiète d'avoir été un peu lente sur le relais, mais je m'en suis sortie, hein ?"

show rin basic_absent
with charachange


hi "En fait, j'ai remarqué que—{w=.4}{nw}"

play sound sfx_impact

show rin basic_deadpanupset
with vpunch


"Rin me donne un coup pied pour m’empêcher de finir ma phrase."

show emi basic_confused_gym
with charachange


emi "Hein ? De quoi ?"

show rin basic_deadpancontemplation
with charachange


rin "Il a remarqué. À la fin."

show emi basic_annoyed_gym
with charachange


emi "Mmh, c'est pas bon."

show emi sad_grin_gym
with charachange


emi "Je pense que l'infirmier voudra jeter un petit coup d’œil plus tard."

show emi sad_grit_gym
with Dissolve(0.2)

show emi sad_grin_gym
with charachange


"Il y a de l’insouciance dans sa voix, comme si ce n'était pas grand-chose, mais je remarque aussi une légère crispation sur son visage."


"Comme si elle essayait de cacher le fait qu'elle avait mal."


"Et il y a sa respiration aussi qui est un peu vive."


"Elle doit s’être fait vraiment mal."


"Elle doit remarquer mon inquiétude, parce qu'elle s'approche de moi et pose sa main sur mon épaule."

show emi basic_closedgrin_gym_close
show rin basic_deadpannormal
with characlose


emi "Hé, tu sembles un peu inquiet !"

show emi basic_grin_gym_close
with charachange


emi "Je vais bien, vraiment !"


emi "Juste fatiguée de la course, c'est tout."

show emi excited_proud_gym_close
with charachange


emi "Et puis c'est pas une petite douleur qui va m’arrêter."


hi "Ah non ?"

show emi basic_closedgrin_gym_close
with charachange


"Emi sourit, et pendant un moment elle a la même expression que quand elle sprintait, féroce et imbattable."


"Ou pour dire ça autrement, vraiment très belle."

show emi basic_grin_gym_close
with charachange


emi "Ce n'est pas encore arrivé du moins."


hi "Bon dans ce cas, je n'ai pas de raison de m’inquiéter, hein ?"

show emi basic_closedhappy_gym_close
with charachange


emi "C'est bien vrai ! Je suis Emi Ibarazaki, la plus rapide du monde sans jambes ! Je ne m’arrête devant rien !"


hi "Impressionnant."

show emi basic_closedgrin_gym_close
with charachange


"Emi rit, et semble se rappeler quelque chose."

show emi basic_grin_gym_close
with charachange


emi "Oh, avant que j'oublie..."


emi "Rin et moi allons faire quelque chose dimanche prochain en guise de fête d'après-rencontre d'athlétisme."

show emi excited_proud_gym_close
with charachange


emi "Tu devrais venir avec nous !"

show emi sad_grin_gym_close
with charachange


emi "Normalement on ferait ça le lendemain, mais vu qu'on est déjà dimanche, j'ai des devoirs à faire et tout ça."

show emi basic_closedgrin_gym_close
with charachange


emi "Et il y a notre course matinale, bien sûr."


hi "Oui, bien sûr."


hi "Oh, c'est vrai. Ta mère voulait que je te dise qu'elle est fière de toi."


hi "Elle t’appellera ce soir."

show emi basic_happy_gym_close
with charachange


emi "Je me disais bien que je l'avais vue dans les gradins !"

show emi basic_closedhappy_gym_close
with charachange


emi "Je suis contente qu'elle ait pu venir !"

show emi sad_grin_gym_close
with charachange


emi "Avant c'était mon père qui venait à mes rencontres, mais ma mère a assez bien pris le relais."

show emi sad_shy_gym_close at Transform(function=tf_lefttremble)
with Dissolve(0.1)


"Elle frissonne légèrement, et je réalise qu'elle est encore en sueur."


"Il commence à y avoir un peu de vent aussi."


"Je n'ai pas froid du tout, et j'ai ma veste avec moi, alors sans un mot je lui mets sur les épaules."

play sound sfx_rustling

show emi basic_shock_gym_close at twoleft
with vpunch

with Pause(0.5)

show emi basic_grin_gym_close
with charachange


"Emi sursaute légèrement puis me sourit."

show emi basic_closedhappy_gym_close
with charachange


emi "Wah, merci !"

show emi sad_grin_gym_close
with charachange


emi "Il commence à faire un peu froid, je crois."


hi "Ouais, je me disais aussi."


"Juste au moment où je commence à me demander si donner ma veste à Emi pourrait être mal interprété, un garçon en uniforme de sport approche."


"Coéquipier" "Hé Emi ! Tu vas louper la cérémonie !"

show emi basic_closedgrin_gym_close
with charachange


emi "Ah oui, merci !"

show emi basic_grin_gym
show rin basic_awayabsent
with charadistant


"Elle se tourne vers Rin et moi."


emi "Vous n'avez pas besoin de rester là pour la cérémonie, ça prend des plombes."

show emi basic_closedgrin_gym
with charachange


emi "En plus, tu devrais faire tes devoirs si tu ne veux pas rester éveillé tard, Hisao."

show emi excited_proud_gym
with charachange


emi "On court demain matin ! N'oublie pas !"

show rin basic_absent
with charachange


hi "Comment pourrais-je ?"

show emi basic_closedhappy_gym
show rin basic_awayabsent
with charachange


emi "Pas faux. Je veux dire, c'est passer du temps avec {b}moi{/b}, après tout."

play sound sfx_emirunning

hide emi
with easeoutleft

stop sound fadeout 3.0

show bg school_track_on at center
show crowd at center
show rin basic_awayabsent at center
with charamove


"Sur ce, elle nous fait un signe de la main et part en courant pour recevoir ses médailles, ou quoi qu'ils puissent donner en guise de médaille de nos jours."

scene bg school_courtyard
show crowd
show rin relaxed_nonchalant at center
with locationskip

stop music fadeout 7.0


"Rin et moi nous éloignons de la piste, et elle reste profondément dans ses pensées durant presque tout le trajet jusqu'aux dortoirs."


"Alors que nous allons nous séparer, elle se met à parler."

show rin basic_deadpan
with charachange


rin "Tu ne récupéreras probablement pas ta veste, je crois."


hi "Je suis sûr qu'elle me la rendra à un moment ou à un autre."

show rin basic_deadpannormal
with charachange


rin "Intéressant. Tu prends les choses comme elles viennent, hein ?"

show rin basic_deadpandelight
with charachange


rin "Très Emi-esque."

hide rin
with charaexit


"Sur ce drôle de commentaire, elle se tourne et se dirige vers le dortoir."


"Franchement, c'était si important que ça ?"


"Emi avait froid et, sauf si je me trompe, avait mal."


"Résoudre un de ses problèmes me semblait être une réaction assez logique."


"Bien que j'imagine qu'il soit aussi possible que je perde ma veste si Emi ne se rappelle jamais qu'elle doit me la rendre."


"Rin n'a pas tort d'un côté."


"Pourtant, ça ne m’inquiète pas tellement."


"Après tout, il fait plus chaud récemment."


"Je n'ai pas besoin d'une veste."


"Bizarre. Je crois que j'avais l'habitude d’être un peu plus responsable de mes affaires."


"“Emi-esque”, hein ?"


"Peut-être que ce n'est pas une si mauvaise chose."

stop ambient fadeout 2.0

scene black
with dissolve


label fr_E9:

scene bg school_nurseoffice
show nurse concern at center
with locationchange


nk "Tu n'as pas oublié de prendre tes médicaments, hein ?"

play music music_nurse fadein 0.5


nk "J’entends un léger murmure."


nk "Tu devrais y aller doucement pendant quelques jours."


"Les mots de l'infirmier me font plus mal que pourraient le faire les courses du matin."


"Y aller doucement pendant quelques jours ?"


"Je savais que j'aurais dû me taire."


"Je garde les yeux sur le sol, me sentant complètement idiot."


"Bien sûr que j'ai oublié de prendre mes médicaments."


"Je me dépêchais de sortir de ma chambre le matin pour aller sur la piste avec Emi."


"Après la rencontre d’athlétisme il y a quelques jours, je me suis senti... motivé."


"Alors j'ai fait quelques tours d’échauffement avant qu'Emi arrive."


"Mais aujourd'hui pendant que nous courions, j'ai ressenti une légère douleur dans la poitrine."


"C'était léger, et seulement pour une seconde, alors je l'ai mentionné à l'infirmier."


hi "Pour dire vrai, ce n'était pas bien grave."


hi "Je veux dire, j'ai continué de courir et j'ai fini la course sans problème, alors ça ne pouvait pas être bien grave..."


"Pourquoi est-ce que j'ai l'impression d'inventer des excuses pour l'infirmier ?"


"Et puis en plus, pourquoi je justifie le fait de continuer à courir si j'ai mal ?"


"En fait, j'ai surtout envie de ne pas inquiéter Emi, qui semble inquiète de toute façon."


"Je ne suis pas sûr de comprendre comment elle à réussi à savoir que quelque chose n'allait pas, mais elle a dit que j'avais un peu trébuché."


"C'est elle qui a insisté pour que je le dise à l'infirmier, alors maintenant je me sens mal de l'avoir inquiétée."


"L'infirmier secoue la tête avec regret pendant qu'Emi fait les cent pas dans le couloir."


nk "Hisao, je sais que c'est difficile pour toi de t'habituer à une nouvelle routine, mais si tu ne veux pas avoir de gros problèmes, il va falloir que tu t'y fasses."


nk "Tu ne peux pas te permettre d'oublier tes médicaments, et tu ne dois pas trop faire d'efforts."


hi "Mais si je ne fais pas d'efforts, comment est-ce que je vais m’améliorer ?"


"Je ne sais pas d’où ça sort."


"L'infirmier semble avoir une idée."

show nurse fabulous

with charachange


nk "Je me demande où j'ai déjà entendu ça ?"

show nurse grin
with charachange


"Il sourit et pose sa main sur mon épaule."


nk "Ha ! Elle déteint sur toi, à ce que je vois."

show nurse concern
with charachange


"Son expression change à nouveau, et il revient en mode sérieux."


nk "Écoute, je ne dis pas que tu ne dois pas faire d'effort."


nk "Mais ça ne veut pas dire que tu ne devrais pas prendre tes médicaments, ou que tu ne devrais pas t’arrêter si ta poitrine commence à te gêner."


nk "J'aimerais ne pas avoir de décès pendant que je suis infirmier ici."

show nurse neutral
with charachange


nk "Ce n'est pas un objectif facile, c'est sûr, mais j'ai toujours apprécié un bon challenge."


"Je déteste l'admettre, mais je crois qu'il a raison."


"Je dois me rappeler de prendre mes médicaments."


hi "Vous avez raison. Je suis désolé de vous inquiéter."


show nurse fabulous
with charachange


nk "Qui est inquiet ? Tu es un garçon intelligent, hein ?"

show nurse neutral
with charachange


nk "Je sais que tu peux être responsable, Hisao. Dans une situation comme la tienne, tu dois apprendre à être responsable très vite."


hi "Je sais, je sais."


"Son expression devient soudainement sournoise."

show nurse fabulous
with charachange


nk "J'imagine que tu as commencé à apprécier tes courses avec Emi alors, hein ?"


hi "Ouais, elles m'ont vraiment aidé."


hi "Je veux dire, jusqu’à aujourd'hui je me sentais bien plus en forme."


hi "En plus c'est vraiment impressionnant de voir Emi courir. Vous l'avez vue à la rencontre d’athlétisme ?"


hi "Elle était incroyable !"

show nurse grin
with charachange


"L'infirmier hoche la tête, souriant tout en même temps."


nk "Elle l'était, Hisao. J'ai regardé quelques courses avant d'avoir à travailler sur quelque chose, mais elle m'a tout raconté."

show nurse fabulous
with charachange


nk "Gentil à toi de lui avoir prêté ta veste, d'ailleurs."


hi "Hein ? Ah oui, c'était pas grand-chose."


"J'avais complètement oublié ça. Je ne l'ai toujours pas récupérée."

show nurse neutral
with charachange


"L'infirmier fait un sourire comme s'il venait de dire une blague."


nk "Peut-être pas pour toi, mais Emi a vraiment apprécié."


nk "Et je sais qu'elle aime aussi courir avec toi le matin."


"Sa dernière phrase me prend un peu par surprise. Oui, elle a mentionné que c'est plus facile de tenir une résolution quand il y a quelqu'un en plus, mais je ne pensais pas lui faire une faveur."


hi "Je pensais qu'elle me faisait une faveur en m'aidant à suivre les ordres du docteur."


nk "Elle fait plus d'efforts quand tu es là."


nk "S'il y a quelqu'un qui court avec elle, elle en fait plus."


nk "Et elle en fait encore plus quand tu es là parce que c'est toi."


hi "Qu'est-ce que c'est censé vouloir dire ?"

show nurse grin
with charachange


nk "Oh ho, tu voudrais vraiment savoir, hein ?"


"Il rit comme un scientifique diabolique."

show nurse neutral
with charachange


nk "Non sérieusement, c'est parce que tu es son ami."


nk "Si Rin courait avec elle, je suis sûr que ça serait pareil."


nk "Enfin, probablement."


nk "Mais ce n'est pas le sujet."


nk "Le fait est que tu l'aides, même si tu ne le sais pas."

show nurse fabulous
with charachange


nk "Et elle en est reconnaissante, même si elle ne le dit pas."


hi "Comment ça “même si elle ne le dit pas” ?"

show nurse neutral
with charachange


nk "Emi ne parle pas beaucoup, mais elle et moi nous connaissons depuis suffisamment longtemps pour que je puisse savoir ce qu'elle ressent la plupart du temps."


"Je l'avoue, je n'ai aucune idée de quoi il parle."


"Emi m'a toujours semblé assez bavarde à moi."


hi "Je vois."


"L'infirmier réalise soudainement qu'il divaguait et arrête de parler, semblant un peu embarrassé."

show nurse fabulous
with charachange


nk "Bref, tu n'as pas à arrêter tes exercices du matin."

show nurse neutral
with charachange


nk "Mais contente-toi de marcher au lieu de courir pendant quelques jours. Laisse les choses se calmer."

show nurse concern
with charachange


nk "Et prends tes fichus médicaments !"

scene bg school_nursehall
with locationchange

stop music fadeout 0.3
play sound sfx_impact

show emi basic_confused_gym_close
with vpunch


"Je ris et sors du bureau, me heurtant immédiatement à Emi."

show emi basic_confused_gym
with charadistant


hi "Oups, désolé."

show emi basic_hes_gym
with charachange


emi "Tu vas bien ? Qu'est-ce qu'a dit l'infirmier ?"


emi "Tu dois aller à l’hôpital ?"

show emi basic_shock_gym
with charachange


emi "Holala, c'est ma faute, hein ?"

show emi basic_closedsweat_gym
with charachange


emi "Je t'ai trop poussé, hein ?"

show emi excited_sad_gym
with charachange


emi "Je suis une horrible personne !"


"Les mots se déversent comme un torrent. Elle est vraiment agitée."



"Je ne m'attendais pas à ce qu'elle soit si inquiète pour moi, à vrai dire."


"Je dois la rassurer... mais comment est-ce que je peux faire ça ?"


"Je fais la seule chose qui me vient à l'esprit."

show emi basic_shock_gym_close
with characlose

play music music_serene fadein 6.0


"Je la serre dans mes bras. Emi se tend légèrement, alors je lui caresse la tête d'une façon que j’espère être rassurante."


hi "Hé, du calme."


hi "Je vais bien, d'accord ? Ne t’inquiète pas."

show emi basic_hes_gym_close
with charachange


"Je peux sentir le corps d'Emi se relaxer alors que je continue de lui assurer que je vais bien."


"Elle passe ses bras autour de moi, comme pour confirmer que je ne vais pas tomber raide mort."


"Une mèche de ses cheveux passe devant mon visage. Ça sent la sueur, ou l'odeur que doit avoir l’adrénaline. C'est l'odeur de l'effort."


"Et un soupçon de fraises. Ça vient de son shampoing, j'imagine."


hi "Je dois juste me rappeler de prendre mes médicaments, c'est tout."


hi "Ne t’inquiète pas pour ça, ce n'est pas ta faute."

show emi sad_depressed_gym_close
with charachange


emi "T'es sûr ?"


"Sa voix est étouffée, surtout parce qu'à ce moment son visage est pressé contre ma poitrine."


hi "Ouais j'en suis sûr. J'ai juste besoin d'y aller un peu plus doucement pour les prochains jours."


"Je me rends soudainement compte à quel point nous sommes collés."


"Je me rends aussi compte à quel point c'est agréable d’être aussi proche d'elle."


"Je peux sentir le cœur d'Emi se calmer, et je dois résister à l'envie de poser mon menton sur sa tête."

show emi sad_grin_gym_close
with charachange


emi "Ça va alors."


emi "Tu m'as vraiment inquiétée, Hisao."

stop music fadeout 1.5

show nurse concern behind emi:
    center
    xpos 0.0 xanchor 0.3
    easein 0.5 xanchor 0.2
with Dissolve(0.5)


nk "Emi, tu comptes venir un de ces jours ?"

show nurse grin
with charachange


nk "...Oh, je suis désolé, j’interromps quelque chose ?"

show emi basic_shock_gym
with vpunch


"Nous nous séparons comme si l'autre venait de prendre feu."


show emi basic_hes_gym
with charachange


"Emi se passe la main dans les cheveux nerveusement et rit."

play music music_emi fadein 1.0


emi "Bien sûr que non !"

show emi sad_shy_gym
show nurse fabulous
with charachange


emi "Je euh... te verrai plus tard, d'accord ?"

show emi basic_closedgrin_gym
with charachange


emi "Oh, et Hisao ?"


hi "Mmh ?"

show emi basic_annoyed_gym_close
with characlose

with hpunch


emi "Prends tes fichus médicaments !"


"La dernière phrase est ponctuée d'un coup de poing à l'épaule."


hi "Ouais, ouais, je m'en rappellerai."


hi "À plus tard."

show nurse grin
with charachange


"L'infirmier sourit encore comme s'il savait quelque chose de drôle que je ne savais pas, et me fait signe alors que je retourne à ma chambre, sentant le feu me monter aux joues."

stop music fadeout 8.0

scene bg school_dormhisao
with locationskip


"J'ai besoin d'une douche."


"Une douche froide, pour chasser les pensées qui s’accumulent dans ma tête."


"Elle était vraiment douce."


"Mes pilules m'attendent quand j'arrive à ma chambre."


"Je les avale sans y réfléchir."


"Je ne sais pas pourquoi je ne pensais pas à les prendre après avoir couru. Pour je ne sais quelle raison, je me disais que je les prenais en me réveillant ou alors pas du tout."


"Mais non, elles doivent juste être prises toutes les vingt-quatre heures. L'heure exacte importe peu."


"Mes pensées dérivent de nouveau vers l'étreinte dans le couloir."


"C'est bizarre, on aurait pu attendre de quelqu'un qu'il sente mauvais après une course, mais pour je ne sais quelle raison, Emi sentait... normal. Comme si la légère odeur de transpiration semblait être appropriée pour elle."


"J'ai vraiment besoin de cette douche."

scene black
with dissolve

$ suppress_window_after_timeskip = True


label fr_E10:

window hide None

scene bg school_roof
with locationchange

nvl clear

nvl show dissolve

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0


n "\n\nBizarre que ça me paraisse si naturel d'aller sur le toit ces jours-ci."


n "Je n'aurais jamais fait ça dans mon ancienne école."


n "À l'époque j'aimais manger seul... non, ce n'est pas tout à fait vrai. Bien que j'aimais être assis seul, j'aimais aussi regarder les gens."


n "J'ai toujours pensé que j'étais quelqu'un comme ça, mais apparemment j'avais tort."


n "Mais encore une fois, je pensais aussi être quelqu'un avec un cœur normal, mais voilà."


n "Je ne me connais pas si bien."


n "Maintenant je suis sur le toit pour déjeuner avec deux personnes."


n "Qui sont toutes les deux des filles, ce qui est encore plus étrange."


n "Bizarrement, je me sens plus proche d'Emi et de Rin que j'ai pu me sentir proche de n'importe qui dans mon ancienne école."


n "J'ai le sentiment qu'elles viendraient me voir si je me retrouvais à l'hôpital."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

nvl hide dissolve

nvl clear

window show


"Je me concentre sur la vue que m'offre le toit, bannissant de telles pensées de mon esprit."


"Il y a une légère brise et le soleil est haut dans le ciel."


"Le ciel en lui-même est d'un grand bleu, libre de tout nuage. Il fait agréablement chaud, et je suis assis là à attendre mes amies, fermant les yeux et appréciant la sensation du soleil sur ma peau."

$ renpy.music.set_volume(0.1, 2.0, channel="ambient")

window hide

scene black
with shuteye

with Pause(4.0)

window show


"Des voix parviennent à mes oreilles."


emi "—dirait qu'il s'est endormi, Rin."


rin "Peut-être qu'il fait semblant, pour nous leurrer dans un faux sentiment de sécurité."


emi "Pourquoi est-ce qu'il ferait ça ?"


rin "Aucune idée."


emi "Cela dit, tu n'as pas tellement tort."


emi "On devrait lui donner un coup de pied pour s'assurer qu'il dort vraiment."

stop music fadeout 1.0


hi "Hein ? Quoi ?"

$ renpy.music.set_volume(0.5, 5.0, channel="ambient")

scene bg school_roof
show rin basic_absent at tworight
show emi excited_happy_close at twoleft
with openeye

play music music_ease fadein 3.0


"Emi s'approche lentement de moi, me regardant avec attention."

show emi basic_closedgrin_close
with charachange


emi "Oh, tu es réveillé, on n'aura pas à te donner de coup de pied alors."

show rin basic_deadpan
with charachange


rin "Ça faisait partie de ton super plan ?"


hi "De quoi est-ce que tu parles ?"

show emi basic_grin_close
with charachange


"Emi hausse les épaules, ses couettes virevoltant en même temps."

show emi basic_closedhappy_close
with charachange


emi "Je ne sais pas non plus."

show emi sad_grin_close
with charachange


emi "Tu dois être plutôt fatigué pour t'endormir ici."

show emi basic_closedgrin_close
with charachange


emi "Bien que ça doit être assez confortable, j'imagine."

show emi basic_closedgrin_close:
    yanchor 0.9
with ease
with vpunch


"Elle s'assoit à côté de moi et commence à manger."

show rin basic_absent
with charachange

show rin basic_absent:
    yanchor 0.77
with charamove


"Rin s'assoit en face de nous deux, ce qui me rend encore plus conscient qu'il y a une fille assise à côté de moi."


"Si je ne la connaissais pas mieux que ça, je jugerais que Rin a fait ça exprès."


"Je me concentre sur mon repas, essayant d'ignorer les conversations que peuvent avoir Rin et Emi."


"Malgré mes efforts, je me retrouve toujours à regarder Emi à chaque fois qu'elle parle."

show emi basic_grin_close
with charachange


"Je remarque sa façon de plisser les lèvres quand elle réfléchit à quelque chose, comme si ça l'aidait à se concentrer."

show rin basic_deadpan
with charachange

show emi basic_grin_close at Transform(function=tf_leftrock)
with None

show emi basic_closedhappy_close at Transform(function=tf_leftrock)
with charachange


"Rin dit quelque chose qui fait rire Emi, et je remarque, sûrement pour la première fois, comment elle rit avec son corps entier, se balançant d'avant en arrière, la tête jetée en arrière, presque comme si elle était sur le point de tomber."


"J'ai probablement l'air d’être un tordu à regarder comme ça."

show emi basic_confused_close
with charachange


"C'est à ce moment que je réalise qu'Emi me regarde. Sa voix est un peu haussée, elle vient sûrement de me poser une question."


hi "Hein ? Désolé, j'étais un peu dans la lune."

show rin basic_deadpannormal
show emi basic_annoyed_close
with charachange


"Emi roule des yeux, et un léger soulèvement de sourcil de Rin est le seul signe qui montre qu'elle est intéressée par ce qui se passe."


emi "J'ai dit, tu as eu en cours la fiche de projet d'avenir toi aussi ?"

show emi basic_grin_close
with charachange


emi "Tu sais, un de ces trucs : “Qu'est-ce que tu feras après le lycée ?”"


hi "Je ne... crois pas. Peut-être qu'on en aura une demain."

show emi excited_happy_close
with charachange


emi "Qu'est-ce que tu comptes écrire ?"


"C'est une très bonne question."


"J'ai toujours pensé que naturellement j'irais à la fac après le lycée, mais je n'ai aucune idée de ce que j'y ferai à ce moment-là."


"Et avec ma crise cardiaque et tout, je me suis vraiment concentré sur le jour présent au lieu de faire des plans pour l'avenir."


"Je peux recommencer à prévoir des choses maintenant, je pense."


"J'ai toujours aimé avoir au moins un vague plan pour l'avenir, ça serait bien d'en avoir un autre à nouveau."


"Bien sûr, ça ne change pas le fait que pour l'instant je n'ai absolument..."


hi "...Aucune idée."


hi "J'ai toujours pensé que j'irais à la fac. Ça ou devenir un salaryman. C'est assez populaire."


"Mais ce que je veux vraiment faire ? Question difficile."


"Je pense que je n'ai pas vraiment envie de quoi que ce soit."

show emi basic_closedhappy_close
with charachange


emi "Tu ne sembles pas très excité à cette idée, on dirait."

show emi basic_closedhappy_close at Transform(function=tf_leftrock)
with None


"Elle rit en disant ça, et je suis encore une fois fasciné par son rire."


"C'est si... féminin. Aigu et apaisant, comme un... petit oiseau."


"Ça sort d'elle, arrivant de son ventre et remontant jusqu’à sa bouche."


"Je ne peux pas m’empêcher de rire aussi - c'est contagieux."


hi "Ouais, je ne suis pas tellement satisfait de l'idée du salaryman."


hi "Mais pour être honnête, je n'ai pas beaucoup pensé à l'avenir récemment."


hi "Je pense que, ces jours-ci, je suis plus concentré sur le fait de vivre un jour à la fois."

show emi basic_grin_close
with charachange


"Emi réfléchit un moment et sourit."


emi "C'est une très bonne idée, Hisao !"

show emi excited_proud_close
with charachange


emi "Moi j'ai juste écrit “Pirate.”"


"Je reste immobile quelques secondes, et éclate de rire."


"Je m’arrête et réussis à sortir une question."


hi "Tu n'es... tu n'es pas vraiment sérieuse, hein ?"

show emi sad_annoyed_close
with charachange


"Emi semble offusquée."


emi "J'ai déjà les jambes pour ça, alors je me suis dit que..."

show rin basic_amused
with charachange


"Même Rin semble amusée par ça."

show emi basic_annoyed_close
with charachange


emi "Attends voir, je serai la terreur des hautes mers !"


emi "Je le montrerai à vous tous !"

show emi basic_closedhappy_close
with charachange


emi "J'ai même commencé à travailler ma voix de pirate !"

show emi basic_closedhappy_close at offscreenleft
with ease

hide emi
with None

show emi basic_closedhappy at offscreenleft behind rin
with None

show emi basic_annoyed at left
with ease


"Elle bondit d'un coup et commence à fanfaronner en direction du bas du bâtiment en criant des ordres."

show emi basic_annoyed at center
with ease


emi "Yarr, matelots, attaquons ces marsouins, à l'abordage !"

show emi basic_annoyed at twoleft
with ease


emi "On portera leurs tripes comme jarretières !"

show rin basic_deadpanamused
with charachange


rin "Est-ce que tu sais ce que ça veut dire ?"

show emi basic_confused
with charachange


"Bizarrement, Rin interrompt Emi dans son élan."

show emi sad_shy
with charachange


emi "Pas vraiment."

show emi basic_closedgrin
with charachange


emi "Mais tout est dans l'élocution !"

play sound sfx_warningbell

show emi basic_hes
show rin basic_awayabsent
with charachange


"La sonnerie l’empêche de continuer sa démonstration."

hide emi
with easeoutleft


"Emi s'enfuit immédiatement, nous laissant Rin et moi seuls sur le toit."

show rin basic_awayabsent:
    xpos 0.5
show bg school_roof at bgleft
with charamove

show rin basic_deadpancontemplation
with charachange


"Rin me fixe du regard pendant de longs instants."


hi "Il y a... un problème ?"

show rin basic_lucid
with charachange


"Rin réfléchit quelques secondes à la question."


"Après une longue pause, elle secoue la tête."

show rin basic_deadpannormal
with charachange

rin "Nope."


hi "Oh, hum..."


extend " pourquoi tu me fixes, alors ?"

show rin basic_awayabsent
with charachange


"Rin secoue la tête à nouveau."


rin "Nope, je ne comprends pas."


hi "Comprendre quoi ?"

show rin basic_deadpan
with charachange


rin "Cette histoire de fixer. Emi et toi semblez comprendre, mais pas moi."


"Super. Elle m'a vu en train de fixer Emi. Maintenant elle va sûrement penser que je suis un pervers ou un truc du genre."


"En fait, peut-être pas. On parle de Rin, après tout."


"Pourtant, je ressens le besoin de me justifier."


hi "Je ne fixais pas du regard, j'étais juste fatigué."

show rin basic_deadpancontemplation
with charachange


"Rin souffle, mais ne dit rien."


hi "Non, vraiment ! J'étais juste... distrait, c'est tout."

show rin basic_lucid
with charachange

rin "Mmm."

stop music fadeout 4.0


"Pressé de terminer cette conversation, je pars en direction de la classe."

stop ambient fadeout 2.0

scene bg school_scienceroom
show misha cross_grin at twoleft
show shizu behind_blank at tworight
with locationskip


"Je suis accueilli par les spectres jumeaux Shizune et Misha, et elles semblent avoir envie d'en démordre."


"Enfin, Shizune tout du moins."


"Misha semble surtout être sur le point d'éclater de rire à tout moment."

play music music_shizune fadein 3.0

show misha perky_smile
with charachange


mi "Encore sur le toit, Hicchan ?"

show misha hips_frown
with charachange


mi "Tu sais que c'est dangereux, hein~ ?"

show shizu basic_angry
with charachange

shi "…"

show misha sign_smile
with charachange


mi "C'est vrai~ !"

show misha hips_smile
with charachange


mi "L'école ne peut pas être tenue responsable si quelque chose arrive pendant que tu es là-haut, tu sais !"

show misha cross_frown
with charachange


mi "Et puis aussi, on pourrait te dénoncer pour avoir fait quelque chose d'interdit~ !"

show misha cross_frown_close
with characlose


"Misha se penche et me chuchote à l'oreille."

show misha sign_smile_close
show shizu behind_smile
with charachange


mi "Mais on ne le fera pas, Hicchan !"

show misha hips_grin_close
with charachange


mi "Parce que vous êtes trop mignons tous les trois ensemble~ !"

show misha cross_laugh
with charadistant


"Elle se redresse et se met à rire devant mon rougissement."


mi "Wahahaha~ !"

show misha cross_grin
with charachange


mi "Tu es trop facile à embêter, Hicchan~ !"


hi "Roh, allez."


hi "Je suis encore nouveau ici, en quelque sorte."


hi "C'est pas cruel de s'attaquer aux nouveaux comme ça ?"

show misha hips_grin
with charachange


mi "Nope~ !"

show misha sign_smile
with charachange


mi "C'est pour t'aider à t'habituer à ton nouvel environnement !"


hi "Ah, je vois."


hi "Enfin... tu as vraiment à t'appliquer à ce point ?"

show misha hips_grin
with charachange


mi "Yep !"

show misha hips_smile
with charachange


mi "Ah ! D'ailleurs, Hicchan, on te cherchait ce matin, mais tu n'étais pas dans ta chambre !"


hi "Bien sûr que je n'y étais pas. J'étais soit à mes exercices matinaux, soit ici en classe, en forme et à l'heure."


hi "Contrairement à toi."

show shizu basic_angry
show misha hips_frown
with charachange


"Shizune semble irritée, et un instant plus tard, Misha aussi. Elle essaye, du moins."


mi "C'était pour le conseil des étudiants ! Tu devrais être reconnaissant de tout le travail qu'on fait pour toi~ !"


hi "Oh mais je le suis, je le suis. Donc pour quoi est-ce que vous aviez besoin de moi ?"


"Pas pour une autre tentative de m'entraver pour que je fasse leur sale boulot, j’espère."

show misha sign_smile
with charachange


mi "On devait te donner quelque chose~ mais vu que tu n'étais pas là, on l'a laissé dans ta chambre !"


hi "Quelque chose ? Comme quoi ?"

show misha hips_grin
with charachange


mi "Oh, tu le sauras quand tu retourneras à ta chambre, Hicchan~ ! Wahahaha~ !"

hide misha
hide shizu
with charaexit


"Le fait que Mutou entre dans la classe interrompt notre conversation, et nous retournons à nos sièges."

stop music fadeout 10.0


"C'est seulement après que je me sois assis à mon bureau et que le professeur ait commencé à parler, que je me rappelle quelque chose d'étrange."


"Que voulait dire Rin avec “Emi et toi semblez comprendre” ?"


"Est-ce qu'Emi fixait quelque chose aussi ?"


"Pendant un bref moment, j'envisage la possibilité qu'Emi me fixait du regard de la même façon que je la fixais."


"Bien sûr, c'est ridicule."


"Quand bien même, je dois avouer que ça ne me gênerait pas si c'était vrai..."


"Mais il est mieux que je pense pas ça. Pas besoin de me donner de faux espoirs."


"En y pensant, depuis quand est-ce que j'ai des espoirs comme ça d'ailleurs ?"


"Je secoue la tête dans le souhait de la vider, et me concentre sur la leçon."

scene bg school_dormhallway
with shorttimeskip


"Après les cours, je me dirige vers le dortoir. Mutou nous a vraiment assaillis de travail aujourd'hui."

play sound sfx_impact2

show kenji tsun at left
with vpunch


"Avant que je puisse ouvrir ma porte, je suis soudainement intercepté par Kenji qui vient de sortir tel une furie de sa chambre, dans un orage de papiers."


ke "Hé, il faut qu'on parle."

play music music_kenji fadein 1.0


ke "À propos de tes manigances sur le toit, mec."


ke "Il faut que ça s’arrête."


hi "Quoi ?"


ke "Ce que tu fais sur le toit avec ces femmes à qui il manque des membres !"


ke "C'est des femmes, mec ! Tu te feras tuer à traîner avec elles comme ça !"


hi "Je ne te suis pas."

show kenji neutral
with charachange


"Kenji soupire et ajuste ses lunettes, avant ce qui peut être compris comme une tentative de s'expliquer patiemment."


ke "Écoute, on est amis alors je te le dis pour ton bien."


ke "Mais si je devais tuer quelqu'un, je le ferais en le jetant du toit en faisant passer ça pour un accident."

show kenji tsun
with charachange


ke "Et si j'y ai pensé, tu peux être sûr qu'elles y ont pensé aussi."


ke "Elles sont rusées - presque autant que moi."


hi "Je vois."

show kenji happy
with charachange


ke "Bien."


ke "Je suis content qu'on ait eu cette discussion."

show kenji neutral
with charachange


ke "Prête-moi 500 yen."


hi "...Excuse-moi ?"

show kenji tsun
with charachange


ke "Il faut que je boive quelque chose, mec !"


ke "Je suis resté à l'intérieur toute la journée et l'eau du robinet a été compromise, et je suis sûr que tu le sais."


ke "Alors j'ai besoin de prendre quelque chose en canette, compris ? Mais pour faire ça, j'ai besoin de 500 yen."

show kenji neutral
with charachange


ke "Et vu que je viens de te sauver la vie avec mon précieux conseil, tu peux au moins me prêter 500 yen."


"500 yen pour qu'il parte, ce n'est pas grand-chose."

stop music fadeout 6.0

show kenji happy
with charachange

show kenji happy:
    easeout 0.5 alpha 0.0 xanchor 0.2
with None


"Je donne l'argent à Kenji, qui hoche la tête en guise de remerciement avant de partir rapidement vers la sortie, mais pas avant d'avoir verrouillé sa porte."


"Qu'est-ce qu'il peut être fatiguant. Je ferais mieux d'y aller, au cas où il change d'avis."

scene bg school_dormhisao
with locationchange


"Mh ?"


"Alors que je ferme la porte, je marche sur quelque chose sur le sol."


"C'est un rectangle de papier coloré. Ah, ça doit être le “quelque chose” que Misha a mentionné auparavant."


"Probablement un prospectus du conseil des étudiants qu'elle a glissé sous la porte."


"Cependant, en le ramassant, il s’avère que je n'aurais pas pu me tromper plus que ça."


"Quelqu'un m'a vraiment envoyé une lettre postale écrite à la main."


"Qui s’embête à faire quelque chose comme ça de nos jours ? Et pourtant, aussi improbable que ça puisse paraître, c'est bien une lettre que j'ai entre les mains."



"Je prévoyais de finir mes devoirs, me faire mon dîner et aller au lit pour pouvoir être prêt pour le sport de demain matin."


"Cependant, la lettre a naturellement attisé ma curiosité. Je m'assois à mon bureau et l'examine."

scene ev hisao_letter_closed:
    xalign 0.5 yalign 0.5 zoom 1.1 subpixel True
    acdc_warp 10.0 zoom 1.0
with locationchange

play music music_rain fadein 5.0


"C'est la première fois que je reçois du courrier ici, alors ça me paraîtrait spécial même si ce n'était pas quelque chose d'aussi rare qu'une lettre écrite à la main."


"Ce qui m’inquiète encore plus est le nom de l’expéditeur, parfaitement écrit au dos de l'enveloppe."

"“Iwanako.”"


"Je n'ai aucune idée de la raison pour laquelle elle m'écrirait. Je n'ai pas été en contact avec qui que ce soit de mon ancienne école depuis que j'ai été transféré, et Iwanako est vraiment la dernière personne que j'aurais imaginée m'envoyer une lettre."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\n\n\n\nLa dernière fois que j'ai vu Iwanako c'était vraiment étrange, même embarrassant. Elle est venue dans ma chambre d’hôpital, m'a épluché une pomme par courtoisie et on est presque restés assis en silence pendant une heure."


n "Elle a dit “au revoir” et ne m'a pas regardé dans les yeux quand elle est partie."


n "C'était une fin assez naturelle à la série de visites qui étaient probablement assez douloureuses pour nous deux."


n "Chaque fois qu'elle est venue me voir à l’hôpital j'ai voulu lui parler, mais quelque chose m'en a toujours empêché."


n "Chaque fois que je n'ai pas parlé a rendu la fois d’après encore plus difficile."

nvl clear


n "\n\n\n\nElle semblait se sentir si coupable que je ne voulais pas dire quoi que ce soit qui pourrait lui faire du mal, et je n'ai jamais trouvé les bons mots."


n "Je crois qu'Iwanako se blâmait pour ma crise cardiaque. C'est ridicule bien sûr, mais le savoir et le croire sont deux choses très différentes."


n "Je lui ai dit que ce n'était pas sa faute, elle a hoché la tête et je pense vraiment qu'elle a compris que si ça n'avait pas été ça, alors tôt ou tard quelque chose l'aurait déclenchée."


n "Et pourtant elle semblait si désespérément triste à chaque fois qu'elle ouvrait la porte et entrait dans ma chambre."


n "Je n'ai jamais réussi à dire les choses que je voulais dire. En fin de compte, ça lui aurait peut-être fait encore plus de mal."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl hide dissolve
nvl clear

scene ev hisao_letter_open
with locationchange

window show


"Avec précaution, j'ouvre l'enveloppe et en sors la lettre."

window hide


$ written_note("Cher Hisao,\n\nComment vas-tu ? J’espère que tu vas bien et que tu es content dans ta nouvelle école. Tu manques à tout le monde ici. Presque toute la classe de seconde année s'est retrouvée en classe 3-1 pour la dernière année, donc nous sommes plutôt confiants pour le début de l'année. Je suis sûre que tu aurais été assigné à cette classe aussi.")


$ written_note("Pas mal de monde est anxieux parmi les étudiants de troisième année pour les examens finaux, même s'ils ont lieu beaucoup plus tard. Les professeurs nous harcèlent tout le temps avec ça - même M. Tachibana qui est, d'ailleurs, notre professeur principal cette année. Tu y crois à ça ? J'étais sûre qu'il prendrait sa retraite après la deuxième année, mais il est là, embêtant tout le monde pour les examens.\n")


$ written_note("Je crois que des choses comme ça sont la raison principale pour laquelle tout le monde est nerveux parmi les troisième année. Je dois admettre que je perds quelque peu confiance aussi, même si j'ai toujours assez bien géré les examens.\n\n\n\n\n")


$ written_note("Ça fait bizarre de penser qu'on est déjà des seniors, hein ? Le temps passe vraiment vite. Je me demande où il est passé. Les nouveaux semblent si jeunes et, d'une certaine façon, si innocents. Je me demande si j'étais comme eux en première année. J'ai eu ce sentiment nostalgique pendant tout le premier trimestre.\n\n\n")


$ written_note("Il y a d'autres choses dont je veux te parler. Je t'écris parce que j'ai l'impression que j'aurais dû te dire certaines choses après l'incident de l'hiver. Je regrette vraiment de ne pas avoir été capable de le dire en personne, et je n'ai aucune excuse pour ça.\n\n\n\n\n")

window show


"Ouais bon, je crois que j'en ai assez."

scene bg school_dormhisao
with locationchange


"Je chiffonne la feuille et la jette à l'autre bout de la chambre. Je loupe mon tir, alors la lettre roule sous ma table plutôt que d'aller dans la corbeille."


"C'était une excuse pour m'avoir abandonné. Sauf que je sais que je n'en ai plus besoin maintenant."


"Le temps que j'ai passé à l’hôpital me semble tellement lointain, et maintenant j'ai d'autres choses à l'esprit."

stop music fadeout 8.0


"Emi, pour commencer."


"Ce n'était pas agréable de me faire abandonner durant mon séjour à l’hôpital, mais ce n'est plus quelque chose qui me tracasse maintenant."


"En fait, je n'avais pas pensé à l’hôpital depuis bien longtemps, jusqu’à ce que cette lettre arrive. C'est presque énervant de l'avoir reçue."


"Je dois étudier pour mes examens aussi. Je n'ai pas de temps pour le passé."


"Bon, et ces devoirs..."

scene black
with dissolve



label fr_E11a:

scene black
with None


hi "Alors quel est le plan pour aujourd'hui ?"

play music music_daily fadein 1.0

scene bg school_girlsdormhall
with dissolve


"J’attends patiemment dans le couloir du dortoir des filles juste devant les chambres d'Emi et de Rin."


"Emi est apparemment en train d'aider Rin à s'habiller."


"Ce qui est logique, je n'ai aucune idée de comment Rin s'habillerait sinon."


emi "Pique-nique !"


hi "Pique-nique ?"


emi "C'est ce que j'ai dit !"


hi "Ça m'a l'air bien."


emi "Oui, hein ?"


"Rin choisit ce moment pour faire une observation."


rin "Le ciel semble menaçant aujourd'hui."


"En fait, j'ai remarqué ça aussi sur le chemin. Malgré le soleil du petit matin, l’après-midi semble avoir pris une tournure un peu plus sombre."


"Il y a une lourdeur qui est généralement signe avant-coureur d'une tempête."


"Je me demande si j'aurais dû prendre mon parapluie..."


hi "Elle a pas tort."


hi "Emi, tu es sûre que tu veux quand même prendre le risque de te retrouver sous la pluie ?"


"Je ne sais même pas pourquoi je prends la peine de demander."

show emi basic_shock:
    center
    xpos 0.9
    easein 0.5 xpos 0.7
with charaenter


"Emi surgit hors de la chambre de Rin en semblant être choquée que j'aie pu suggérer d'abandonner."


emi "Bien sûr !"

show emi basic_annoyed
with charachange


emi "Quoi, la menace de la pluie est censée m’arrêter ?"


"Je ne peux pas m’empêcher de sourire à sa réponse belliqueuse. C'est presque comme si elle défiait la pluie de venir."


"Si mère nature se baladait dans la rue, Emi se bagarrerait sûrement avec elle."


"Ou au moins elle la défierait à la course."


"En fait, Emi semble agressivement joyeuse aujourd'hui."

show rin basic_absent:
    center
    xpos 0.9 alpha 0.0
    ease 1.0 xpos 0.7 alpha 1.0
show emi basic_annoyed at twoleft
show bg school_girlsdormhall at bgleft
with charamove


"Rin sort dans le couloir, semblant comme à son habitude."


hi "Bon, on est prêts à partir ?"

show emi basic_closedhappy
with charachange


emi "Je suis prête !"

show rin basic_deadpannormal:
    tworight alpha 1.0
with charachange


"Rin hoche la tête et dit un seul mot."

show rin basic_deadpan
with charachange


rin "Panier."


hi "Pardon ?"

show rin basic_deadpannormal
with charachange


rin "Le panier. Dans la chambre d'Emi. Tu devrais le prendre."

show emi basic_hes
with charachange


"Emi plaque une main sur sa bouche, embarrassée."

show emi basic_closedsweat
with charachange


emi "Oh mince ! J'ai presque oublié ! Bien joué, Rin !"

show emi basic_closedsweat at offscreenleft
with ease

with Pause(0.3)

show emi basic_closedgrin at twoleft
with ease


"Emi fonce dans sa chambre et en ressort avec ce qui semble être un panier de pique-nique bien garni."

with vpunch


"Alors qu'elle me le tend et que je le porte, je confirme qu'il est bien rempli. Sérieux, elle a pris tant que ça à manger ?"


"...Et aussi, ou est-ce qu'elle a eu l'argent pour tout ça ?"


hi "Alors, on y va ?"

show emi basic_grin
with charachange


emi "Yep !"

show rin basic_awayabsent
with charachange


"Rin hoche encore une fois la tête et nous nous dirigeons vers la sortie du dortoir."

scene bg school_courtyard_rn
with locationskip


"Je fronce les sourcils devant le ciel qui est devenu bien gris durant les dix minutes où j'étais à l'intérieur."


"Et pourtant, Rin ne semble pas inquiétée par des choses aussi insignifiantes que la couleur du ciel. Elle bondit presque joyeusement alors que nous marchons."


"Ce qui me rappelle..."


hi "Où est-ce qu'on va ?"


"Emi est interrompue dans sa lancée et me jette un regard embarrassé."

show emi sad_shy_rn at center
with charaenter


emi "Tu sais, je n'y ai pas vraiment encore pensé."


emi "Qu'est-ce que tu en penses, Hisao ?"


"Eh bien, il y a l'endroit où on a mangé durant le festival, mais ça serait bien de sortir du campus aussi. Cependant, je ne sais pas s'il y a des bons endroits pour ça en ville."


"Alors que je suis sur le point d'ouvrir la bouche, Rin lance une suggestion."

show emi sad_shy_rn at twoleft
show bg school_courtyard_rn at bgleft
with charamove

show rin basic_deadpan_rn at tworight
with charaenter


rin "Il y a un parc en ville pas loin du magasin d'art."

show emi basic_closedhappy_rn
with charachange


emi "Très bonne idée Rin ! J'avais totalement oublié cet endroit !"


"Crise évitée."


hi "Tu sais comment y aller, Rin ?"

show rin basic_deadpannormal_rn
with charachange


"Rin hausse les épaules."

show rin basic_awayabsent_rn
with charachange


rin "Sûrement."

show emi excited_amused_rn
with charachange


emi "Ça me suffit !"


"Je préférerais être sûr... bah, peu importe."


hi "Ouvre la voie, Rin."

scene bg school_gate_rn
with locationchange


"Nous sortons rapidement du campus et nous dirigeons vers la ville."

scene bg school_road_rn
with locationchange


"Le panier est un peu lourd. J’espère que le parc n'est pas loin."

scene bg suburb_roadcenter_rn
with locationchange


"Nous passons devant le magasin de fournitures d'art, Rin ralentissant pendant que nous passons devant."


"Emi remarque le changement de rythme de Rin et s’arrête."

show emi basic_grin_rn at twoleft
show rin relaxed_nonchalant_rn at tworight
with charaenter


emi "Tu veux y entrer, Rin ?"

show rin basic_awayabsent_rn
with charachange


"Rin hausse les épaules."

show rin basic_deadpan_rn
with charachange


rin "J'ai besoin de rien."

show emi excited_proud_rn
with charachange


emi "Tu es sûûûre ?"

show rin basic_delight_rn
with charachange

show rin basic_deadpandelight_rn
with charachange


"Il y a une légère ébauche de sourire sur le visage de Rin, rapidement remplacée par son expression habituelle."

show rin basic_deadpan_rn
with charachange


rin "La vie est incertaine, mais de ça je suis sûre."

show rin basic_deadpanamused_rn
with charachange


rin "Gentil à toi de proposer."

show emi basic_closedhappy_rn
with charachange


emi "Enfin c'est pas comme si j'étais celle qui portait le panier."

show emi basic_grin_rn
with charachange


emi "Mais je parie que ça ne gênerait pas Hisao dans tous les cas, hein ?"


hi "Oh, bien sûr que non. Ce n'est pas lourd."


"Je plie le bras pour montrer."

show emi excited_laugh_rn
with charachange


"Emi réprime un petit rire en pointant du doigt le parc où nous sommes arrivés."

$ renpy.music.set_volume(0.02, 0.0, channel="ambient")
play ambient sfx_rain fadein 15.0

scene bg suburb_park_rn at bgright
with locationchange


emi "Oh, je me rappelle cet endroit !"

show emi basic_closedhappy_rn
with charachange


emi "Je t’ai vue ici l'autre fois, tu te rappelles, Rin ?"

show emi basic_closedhappy_rn at twoleft
show bg suburb_park_rn
with charamove

show rin basic_deadpannormal_rn at tworight
with charaenter


"Rin lève légèrement un sourcil."

show rin basic_deadpan_rn
with charachange


rin "Peut-être."

show rin relaxed_boredom_rn
with charachange


rin "Je ne peux affirmer ni l'un ni l'autre."

show rin relaxed_nonchalant_rn
with charachange


rin "Les souvenirs sont assez traîtres tu sais."


"Je m'en rappellerai moi. On est arrivés en un morceau après tout."


"Le soleil n'est plus visible, mais ni Emi ni Rin ne semblent s'en préoccuper."

scene ev picnic_normal:
    yalign 1.0 subpixel True
    easein 8.0 yalign 0.0
with whiteout








"On trouve un endroit où s’asseoir sur l'herbe et je pose avec joie le panier."


"Il y a vraiment beaucoup à manger. Peut-être qu'on est censés être rejoints par certains des membres de l'équipe d’athlétisme d'Emi ?"





emi "Je meurs de faim ! À l'attaque !"


"Elle commence à manger comme si elle n'avait rien eu depuis des années."

stop music fadeout 2.0

play sound sfx_thunder

show ev picnic_rain:
    yalign 0.0
with charachange





$ renpy.music.set_volume(0.2, 0.5, channel="ambient")

show rain light
with dissolve


"Alors que je tends la main pour me servir, je sens la première goutte de pluie tomber dessus."


hi "Oh oh."


hi "On dirait que le temps ne va pas coopérer avec nous après tout."

hide ev
show bg suburb_park_rn behind rain
show emi sad_grit_rn behind rain:
    twoleft
    ypos 1.15
show rin basic_absent_rn behind rain:
    tworight
    ypos 1.2
with flash


"Emi regarde méchamment le ciel, comme si ça allait suffire pour arrêter la pluie."


"Je croirais presque qu'elle peut le faire. C'est un sacré regard qu'elle a là."

show emi basic_annoyed_rn
with charachange


emi "Il ferait mieux de coopérer."

show emi sad_angry_rn
with charachange


emi "Tu m'entends ciel ? Tu arrête de pleuvoir, tout de suite !"


"Le ciel ne semble pas enclin à l'écouter, malgré son ton impératif."

$ renpy.music.set_volume(0.5, 4.0, channel="ambient")

show rain medium
with dissolve


"Au lieu de ça, la pluie ne fait que s’accroître. Rin fronce le nez à la tournure que prennent les évènements."

show rin basic_deadpan_rn
with charachange


rin "Regrettable."

show emi basic_confused_rn
with charachange


emi "Comment ça ?"

show rin basic_deadpannormal_rn
with charachange


"Rin hausse les épaules."

show rin relaxed_nonchalant_rn
with charachange


rin "Je pourrais peindre la scène si on n'était pas dehors. Dommage de louper ça."


"Elle ne semble pas en colère ou énervée, juste un peu déçue."

show emi basic_closedhappy_rn
with charachange


"Emi rit en réponse au commentaire de Rin."

show emi basic_grin_rn
with charachange


emi "On aurait dû s’arrêter au magasin d'art après tout alors, hein ?"

$ renpy.music.set_volume(1.0, 6.0, channel="ambient")

show rain normal
with dissolve


"La pluie s'intensifie encore un peu, offensée que nous n'ayons pas encore fui."


"Malgré la chaleur ambiante, la pluie est assez froide. J'aurais dû prendre mon parapluie."


hi "Hé, on devrait probablement aller à l'intérieur pour rester secs."

show emi basic_confused_rn
show rin basic_absent_rn
with charachange


emi "On est déjà plutôt mouillés, Hisao."


hi "Ouais, mais on pourra sécher comme ça et peut-être attendre la fin de la pluie. Tu n'as pas envie d'attraper un rhume, n'est-ce pas ?"

show emi basic_annoyed_rn
with charachange


"Emi envisage l'idée pendant un moment. Je sais qu'une partie d'elle a envie de rester sous la pluie juste pour narguer le temps."


"Malheureusement pour elle, le temps se moque pas mal de ce que nous faisons."

show emi basic_closedgrin_rn
with charachange


emi "Tu dois avoir raison."

show emi sad_grin_rn
with charachange


emi "Où est-ce qu'on peut aller ?"


"Je n'ai pas de réponse pour elle. Les environs sont toujours nouveaux pour moi."


"Bien que je m'habitue lentement à l'école, la ville proche reste un mystère."


"Tout ce que je connais est le magasin de fournitures d'art, et c'est juste parce qu'on vient de passer devant."

show emi basic_closedgrin_rn
with charachange


"Heureusement, Emi claque des doigts en signe de triomphe."

show emi basic_happy_rn
with charachange


emi "Voilà ! Il y a un salon de thé pas loin !"


emi "On pourrait prendre un thé et sécher, no problem !"


"Ça ne semble pas être une mauvaise idée."


hi "Super ! Tu sais où c'est ?"

show emi basic_grin_rn
with charachange


"Emi hoche la tête, semblant confiante."

show emi basic_closedgrin_rn
with charachange


emi "Bien sûr !"

show emi basic_hes_rn
with charachange


emi "Je crois."

show emi excited_laugh_rn
with charachange


emi "Mais ça sera une aventure dans tous les cas, hein ?"


hi "Aventure, hein ? Eh bien, ça peut être drôle."


"Tant qu'on ne reste pas sous la pluie, je serai content."

show emi basic_grin_rn at twoleft
show rin basic_absent_rn at tworight
with dissolvecharamove


"Le panier de pique-nique est un peu plus léger maintenant au moins."


hi "Ouvre la voie !"

show bg suburb_roadcenter_rn
hide rin
hide emi
with locationchange


"Rin et moi suivons Emi alors qu'elle descend les rues d'un pas confiant."

show emi basic_confused_rn at center behind rain
with charaenter


emi "Maintenant à gauche ici..."

show emi excited_joy_rn
with charachange


emi "Là ! Le Shanghai !"


"Emi sourit, triomphante, en arrivant au salon de thé."

show bg suburb_shanghaiext_rn
hide emi
with locationchange


label fr_E11x:


"En y pensant, je suis déjà venu ici auparavant. Il semble y avoir pas mal de monde à l'intérieur. Entièrement la faute de la pluie, je suis sûr."

play sound sfx_storebell
stop ambient fadeout 0.5
play music music_jazz fadein 2.0

scene bg suburb_shanghaiint
with locationchange

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

with Pause(1.0)

show yuukoshang neutral_down at center
with charaenter


yu "Bienvenue ! Puis-je—"

show yuukoshang happy_down
with charachange


yu "Oh, c'est toi."


"Yuuko semble connaître Emi."

show yuukoshang happy_down at tworight
show bg suburb_shanghaiint at bgright
with charamove

show emi basic_closedhappy at twoleft
with charaenter


"Emi sourit joyeusement, contente d’être reconnue."

show emi basic_grin
with charachange


emi "Salut Yuuko ! Y a de la place pour nous ?"

show yuukoshang neutral_down
with charachange




label fr_E11y:


"Il semble y avoir pas mal de monde à l'intérieur. Une conséquence de la pluie, je suis sûr."

play sound sfx_storebell
stop ambient fadeout 0.5
play music music_jazz fadein 2.0

scene bg suburb_shanghaiint
with locationchange

$ renpy.music.set_volume(0.7, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0

with Pause(1.0)

show yuukoshang neutral_down at center
with charaenter


yu "Bienvenue ! Puis-je—"


"Je suis surpris de voir que notre serveuse n'est autre que Yuuko."


"Elle est vraiment différente dans son uniforme. C'est difficile de croire que c'est la même personne que notre bibliothécaire."


"Est-ce qu'elle a deux travails ? Ça doit être ça."

show yuukoshang happy_down
with charachange


yu "Oh, c'est toi."


"Yuuko semble connaître Emi."

show yuukoshang happy_down at tworight
show bg suburb_shanghaiint at bgright
with charamove

show emi basic_closedhappy at twoleft
with charaenter


"Emi sourit joyeusement, contente qu'on se rappelle d'elle."

show emi basic_grin
with charachange


emi "Hé Yuuko !"


hi "Salut, Yuuko. Je ne savais pas que tu travaillais ici aussi."

show yuukoshang worried_down
with charachange


yu "Est-ce que je te connais ?"

show yuukoshang worried_up
with charachange


yu "Ton visage me semble très familier, mais je ne crois pas t'avoir déjà vu ici."


hi "Euh, on s'est rencontrés à ton autre travail. À la bibliothèque de Yamaku. Tu te rappelles ?"

show yuukoshang happy_up
with charachange


"Ses yeux s'écarquillent alors qu'elle se souvient."

show yuukoshang closedhappy_down
with charachange


yu "Ouais, c'est ça ! Contente de te revoir..."

show yuukoshang panic_down
with charachange


yu "Oh non, c'est pas bien !"

show yuukoshang panic_up
with charachange


yu "J'aurais dû me rappeler le visage d'un client ! Je suis désolée... Je suis terriblement désolée !"


"Yuuko passe de la prise de conscience à la panique en une seconde avant d’enchaîner plusieurs courbettes rapides d'excuse. J’évite par la même occasion de me cogner la tête contre la sienne."


hi "Woah, hé, du calme !"


hi "Écoute, je n'étais pas un client quand on s'est rencontrés, je ne suis même jamais venu au Shanghai, alors c'est pas un problème."


"Pas la meilleure logique du monde, mais ça semble la calmer un peu."

show yuukoshang worried_down
with charachange


yu "Tu crois vraiment ?"


hi "Euh, ouais, j'en suis sûr. Absolument positif. C'est pas vrai, Emi ?"

show emi basic_closedgrin
with charachange


"Emi a regardé ce petit drame avec un air perplexe sur le visage."

show emi excited_proud
with charachange


emi "Yep, bien sûr !"

show yuukoshang neutral_up
with charachange


yu "Bon, d'accord..."

show emi basic_happy
with charachange


emi "Alors Yuuko, y a de la place pour nous ?"

show yuukoshang neutral_down
with charachange


label fr_E11z:

$ renpy.music.set_volume(0.3, 3.0, channel="ambient")


"Yuuko hoche la tête et nous amène à une table dans un coin, nous laissant des petites serviettes avant de prendre notre commande."

show yuukoshang happy_down
with charachange


yu "Vous avez fait votre choix ?"

show emi basic_closedhappy
with charachange


emi "Du gâteau ! Et du thé aussi, je pense."

show yuukoshang neutral_down
with charachange


yu "Quel genre de gâteau ?"

show emi excited_proud
with charachange


emi "Surprends-moi !"

show yuukoshang worried_up
with charachange


"Yuuko semble mal à l'aise à l'idée de surprendre qui que ce soit, mais elle hoche la tête et se tourne vers Rin."

show rin invis:
    yalign 1.0 xpos 1.0 xanchor 0.6
with None

show yuukoshang neutral_down:
    xpos 0.55
show emi basic_grin at left
show rin basic_absent at right
show bg suburb_shanghaiint at center
with dissolvecharamove


yu "Et pour toi ?"

show rin negative_spaciness:
    right alpha 1.0
with charachange


rin "Je vais prendre une paille. Mes pieds sont tout mouillés."

show yuukoshang worried_up
with charachange


yu "Pardon ?"

show rin basic_awayabsent
with charachange


rin "Les pailles qui peuvent boire. Une, s'il te plaît."

show yuukoshang worried_down
with charachange


"Yuuko ne sait visiblement pas quoi en penser. Son stylo reste immobile quelques secondes, et elle semble sur le point de pleurer avant de se tourner dans ma direction."

show yuukoshang neutral_down
with charachange


yu "Monsieur, votre commande ?"


hi "Juste du thé, je pense."


"Emi me crierait sûrement dessus si je prenais du gâteau."

show emi sad_depressed
with charachange


emi "Oh, allez Hisao ! Ne me laisse pas être la seule à manger quelque chose, j'aurais l'impression d’être une goinfre !"


hi "J'essaye juste de manger sain."


hi "C'est tes ordres, après tout."

show emi basic_closedgrin
with charachange


emi "Bon... aujourd'hui est ton jour de repos ! Tu pourras manger sainement demain !"


hi "Bon alors, je crois que je vais prendre du gâteau aussi."

show yuukoshang neurotic_up
with charachange


"Yuuko semble légèrement embêtée que je change d'avis."


yu "Quel genre de gâteau ?"


"Je regarde Emi et souris."


hi "Surprends-moi."

show yuukoshang smile_down
with charachange


"Yuuko soupire et hoche la tête."


yu "Très bien. Vos commandes seront bientôt prêtes."

show emi basic_grin at left
show yuukoshang neutral_down
show rin basic_awayabsent
with shorttimeskip


"Malgré le fait qu'il y ait du monde, nos commandes arrivent effectivement rapidement."

show emi excited_joy
with charachange


emi "Merci, Yuuko !"


"Yuuko hoche la tête en guise de reconnaissance."

stop music fadeout 4.0

show yuukoshang happy_down
with charachange


yu "C'est un garçon différent de d'habitude, n'est-ce pas ?"


"Hein ? Garçon différent ?"

show emi basic_hes
with charachange


"Emi doit remarquer ma confusion, parce qu'elle semble un peu embarrassée."


emi "Q-quoi ? Oh, ouais, c'est vrai."

show emi sad_grin
with charachange


emi "C'est Hisao, un ami."


hi "On s'est rencontrés."

show yuukoshang smile_down
with charachange


yu "Oh. Le monde est petit."

show yuukoshang neutral_down
with charachange


yu "Bon, dites-moi si vous avez besoin de quoi que ce soit."

hide yuukoshang
with charaexit

show emi sad_grin at twoleft
show rin basic_awayabsent at tworight
with charamove


"Sur ce, Yuuko part rapidement pour aller servir d'autres tables, me laissant en train de réfléchir à sa remarque."


"Un garçon différent, hein ? C'est logique, hein ? Emi est assez populaire après tout, c'est ce que j'ai entendu du moins."


"C'est sûrement celui de son équipe d’athlétisme."


"C'est idiot. Je peux aussi simplement demander à Emi."

show rin basic_absent
with charachange

play music music_comedy fadein 0.5


hi "Alors qui est cet autre garçon, hein ? Tu as un amoureux secret ou quelque chose du genre ?"

show emi basic_closedhappy
show rin basic_awayabsent
with charachange


"Emi rit encore, sauf que j'ai le sentiment que c'est autant nerveux qu'autre chose."

show emi basic_grin
with charachange


emi "C'est juste le capitaine de l'équipe d’athlétisme. Il aime bien venir ici après l’entraînement des fois."

show emi basic_closedgrin
with charachange


emi "Et si on a des choses à se dire, je viens avec lui."


"Mmh, c'est très suspect tout ça..."

show rin basic_absent
with charachange


hi "Oh, je vois."


"Je pourrais en rester là, mais je ne peux pas m’empêcher d'en rajouter une dernière couche."


hi "Donc {b}c'est{/b} un amoureux secret !"


hi "Je le savais."

show rin basic_deadpanamused
with charachange


"Rin regarde la scène, semblant amusée avant de marmonner quelque chose que je ne comprends pas bien."


rin "... t... toute façon."

show emi basic_confused
with charachange


$ doublespeak(emi,hi,"Quoi ?", "Hein ?")

show rin basic_surprised
with charachange


"Rin revient de là où son esprit vagabondait."


rin "Hein ?"


hi "Qu'est-ce que t'as dit ?"

show rin basic_deadpan
with charachange


rin "Hein."


hi "Non, avant ça."

show rin relaxed_nonchalant
with charachange


rin "Aucune idée."


hi "Oh. Bon."


hi "D'accord."

show emi basic_grin
show rin basic_deadpannormal
with charachange


"Je laisse tomber, mais ne peux pas m’empêcher de remarquer qu'Emi semble soulagée que Rin ait interrompu la conversation."


"Peut-être que j'ai été un peu trop loin..."


"Un silence s'installe pendant quelques instants alors qu'Emi et moi sommes occupés avec nos gâteaux."


"Le mien est à la fraise et étonnamment bon."

play sound sfx_slide2

show emi excited_happy_close
with characlose

show emi basic_closedgrin
with charadistant


"Emi semble penser la même chose alors qu'elle tend le bras et prend une fourchetée du mien."


hi "Voleuse !"

show emi excited_proud
with charadistant


emi "Pirate. C'est différent."


hi "Nous ne sommes pas sur l'eau !"

show emi basic_closedgrin
with charadistant


emi "Eh bien, non. Mais il y a beaucoup d'eau dehors, alors ça compte quand même, hein ?"

show emi sad_grin
with charadistant


emi "Et puis tu peux en prendre un peu du mien. Je crois que c'est à la canneberge ou un truc du genre."

show emi sad_depressed
with charadistant


emi "J'aurais dû demander à la fraise. J'aime les fraises."


hi "Sers-toi dans le mien, si tu le veux vraiment."


"Pour je ne sais quelle raison, je me sens obligé d'ajouter :"


hi "Vu que tu l'as déjà fait une fois après tout."

show emi basic_closedgrin
with charadistant


"Emi me tire la langue, mais ça ne l’empêche pas de piquer dans mon assiette. Je goûte un peu de son gâteau aussi."


"C'est à la framboise, et vraiment bon."

show rin relaxed_boredom
with charachange


rin "La pluie s'est calmée."


"On dirait que Rin a raison."


"Au bon moment, aussi. J'ai fini mon repas, et Emi aussi."


hi "Bon, on ferait mieux de payer et de partir avant qu'il ne se remette à pleuvoir."

stop ambient fadeout 1.0

scene bg suburb_shanghaiext_rn
with locationchange


"Il me faut quelques minutes pour avoir l'attention de Yuuko, puis nous payons et partons rapidement."

show emi basic_grin_rn at center
with charaenter


emi "Alors, vous voulez retourner au parc ?"


"Ma machoire en tombe presque."


hi "Tu plaisantes ? Il va sûrement se remettre à pleuvoir."


"En fait, je crois que je viens de recevoir quelques gouttes."

show emi sad_grin_rn
with charachange


emi "Mmh... tu as peut-être raison."

show emi basic_closedgrin_rn
with charachange


emi "Bon d'accord, ça passe pour cette fois, mais tu me dois un pique-nique maintenant. Compris ?"


"Je ne sais pas si elle parle à Rin, à moi, ou à nous deux."


hi "D'accord, d'accord."

show emi excited_proud_rn
with charachange


emi "Maintenant dépêche-toi ! Je voulais faire quelques tours de piste, et ça serait bien de les faire sans la pluie."


hi "Je croyais que c'était ton jour de repos !"

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 6.0

show emi sad_depressed_rn
with charachange


emi "Ben..."


"Emi semble soudainement ne pas avoir envie de s'expliquer."

show emi sad_grin_rn
with charachange


emi "J'ai besoin de m’entraîner."

show emi basic_grin_rn
with charachange


emi "Et il faut que je perde ce gâteau de toute façon."


"Pourquoi est-ce que j'ai l'impression qu'elle ne dit pas tout ?"


hi "Tu es sûre ? Ce n'était pas un gros gâteau..."

show emi basic_closedgrin_rn
with charachange


emi "Non, ce n'était pas un gros gâteau pour {b}toi{/b}. J'en ai mangé la plus grande partie."


"C'est pas faux."

label fr_choiceE11:
menu:
    with menueffect
    "J'ai le sentiment que je devrais au moins proposer de courir avec elle…"
    "Proposer de courir avec Emi.":






        return m1
    "Ne rien dire.":


        return m2

label fr_E11b:



hi "Tiens, je vais courir avec toi."


hi "Je peux tout autant, hein ?"

show emi basic_annoyed_rn
with charachange


"Emi secoue la tête énergiquement."


emi "Non Hisao. Le repos est indispensable pour toi, tu te rappelles ?"


emi "Je ne te permettrai pas de trop forcer ton corps."


"Apparemment elle est plus douée pour donner des conseils que pour les suivre."


hi "Comme tu veux, Emi."


"Je crois que c'est mieux de ne pas insister."

label fr_E11c:




"En y pensant, on dirait qu'elle préférerait être seule."


"Je décide de ne rien dire."

label fr_E11d:



stop music fadeout 12.0

scene bg school_dormext_full_rn
with locationskip


play ambient sfx_rain fadein 2.0
show rain normal
with Dissolve(2.0)


"Alors que nous nous approchons du dortoir des filles, il recommence à pleuvoir."

show emi sad_annoyed_rn at center behind rain
with charaenter


"Emi grimace un peu."


emi "Oh, mince..."


emi "Stupide pluie."


hi "Bah, ça s’arrêtera sûrement bientôt. Tu pourras courir à ce moment-là, hein ?"

show emi basic_grin_rn
with charachange


"Emi souffle, semblant amusée."

show emi excited_proud_rn
with charachange


emi "Comme si je n'allais pas courir sous la pluie."


hi "Eh bah tu ne devrais pas ! Tu pourrais attraper un rhume !"

show emi basic_grin_rn
with charachange


"Emi secoue une main dans l'air."


emi "Ridicule ! Je n'attrape jamais de rhumes."

show emi basic_closedgrin_rn
with charachange


emi "Mon système immunitaire est bien trop fort pour quelque chose comme ça."


"Je ne peux pas m’empêcher de rire."


hi "Bon, je te vois demain alors, hein ?"

show emi basic_happy_rn
with charachange


emi "Ouais !"

show emi basic_grin_rn
with charachange


emi "Merci d’être venu ! Oh, et d'avoir porté le panier !"

show emi excited_amused_rn
with charachange


emi "Je le prendrai pour déjeuner demain. On pourra faire un pique-nique sur le toit !"


hi "Ça me semble bien. À demain !"

hide emi
with charaexit


"Emi attrape le panier et fonce vers l'entrée du dortoir."


"Rin m'adresse une sorte de hochement de tête et va à l'intérieur aussi."


"Rah, temps de chien."


"Il faut que j'aille à ma chambre et que je mette des vêtements propres."

stop ambient fadeout 2.0

scene bg school_dormhallway
with locationskip


"Je suis rapidement devant ma porte, mais suis intercepté par l'apparition soudaine de Kenji, qui semble porter une pile de livres."

show kenji neutral at center
with charaenter


ke "Hé mec, tu peux m'aider ?"


hi "Hein ?"

play music music_kenji fadein 0.5

with vpunch


"Les livres tombent sans précaution dans mes bras alors que Kenji cherche la clé de sa chambre."

show kenji happy
with charachange


ke "Merci, tu me sauves la vie."


ke "Si tu n'étais pas là j'aurais dû laisser ma porte ouverte, et c'est bien trop dangereux."

show kenji tsun
with charachange


ke "C'est l'opportunité parfaite pour préparer une embuscade, ou peut-être poser une bombe si elles ne veulent pas se salir les mains."


ke "Probablement pas."


ke "Trop peur de se casser un ongle si elles doivent me poignarder."


ke "Femmes."


"J'envisage d'essayer de comprendre le torrent verbal qui vient de me tomber dessus, mais préfère rester à l'aise dans l’incompréhension."


hi "Euh... euh."

show kenji happy
with charachange


ke "Bref, où est-ce que t'étais, mec ?"

show kenji neutral
with charachange


ke "J'aurais bien apprécié de l'aide pour porter ces livres depuis la bibliothèque !"


ke "J'ai frappé à ta porte, mais tu n'étais pas là."


hi "Oh, désolé."


"Pas vraiment. Il semble penser à moi comme à une sorte de mule."


hi "J'étais dehors avec Emi et Rin."

show kenji rage
with charachange


"Kenji recule à cause du choc."


"Il réagit comme si je venais d'abattre son chien, s'il avait un chien."


ke "Encore les filles avec des membres en moins ?"

show kenji tsun
with charachange


ke "Qu'est-ce que t'as fait cette fois ?"


hi "Eh bien, on a été au Shanghai—"


"Je suis interrompu dans mon histoire par une exclamation désespérée."

show kenji rage
with vpunch


ke "Le Shanghai ?"


ke "Pourquoi le Shanghai ?"


ke "Non non non non, mec, tu ne peux pas aller à ce satané Shanghai !"


ke "C'est l'endroit le plus dangereux de la ville !"


ke "Une véritable forteresse de leurs meilleurs agents !"


ke "Je le sais ! Je les ai rencontrés !"


ke "Ils ne s’arrêteront devant rien pour te leurrer avec un faux sentiment de sécurité, et puis BAM !"

play sound sfx_impact2
with vpunch


"Il frappe la porte pour être explicite."


ke "Portefeuille disparu. Carte de bus ? Disparue. Identité ? Putain de {b}disparue{/b}, mec !"

show kenji tsun
with charachange


ke "Promets-moi que tu n'iras plus jamais là-bas !"


"Il semble si violemment opposé au Shanghai que je suis prêt à mentir un peu pour pouvoir aller dans ma chambre."


hi "D'accord, je n'irai plus."


"Ou du moins, je ne te le dirai plus."


"Ça semble convenir à mon ami à lunettes."

show kenji neutral
with charachange


ke "Bien, bien."

show kenji happy
with charachange


ke "Désolé d'insister autant, mais je ne connais que trop bien les dangers de ce lieu pour te laisser retourner dans la tanière du loup à nouveau."


ke "Tu es sorti en vie de là une fois, mais deux fois serait forcer la chance."


hi "Ouais bon, j'ai besoin de me changer et euh, de faire mes devoirs. Alors... je te verrai plus tard."

show kenji tsun
with charachange


ke "Hein ?"

show kenji neutral
with charachange


ke "Oh, bien sûr. Peu importe."


"Je me rappelle soudainement que je tiens toujours ses livres."


hi "Tu ferais mieux de les reprendre."


"Je vois le titre d'un des livres, quelque chose qui parle de cryptographie."


"Quel gars bizarre."

stop music fadeout 6.0

show kenji neutral:
    center
    easeout 0.5 xpos 0.3 alpha 0.0
with None


"Kenji prend ses précieux ouvrages et disparaît dans sa chambre."

$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_rain fadein 1.0

scene bg school_dormhisao
with locationchange


"J'ouvre ma propre chambre et y rentre, content d'enlever mes vêtements trempés."


"La pluie dehors redouble d'intensité, et je me retrouve à espérer qu'Emi n'est pas en train de courir par ce temps. Elle semblait si décidée à faire ces tours toute seule que je ne peux pas m’empêcher de me demander si sa jambe lui fait toujours mal."


"J'essaye de me rappeler si je l'ai vue boiter aujourd'hui, mais je n'y arrive pas. J'étais trop occupé à apprécier la journée, même si le ciel s'acharnait sur nous."


"Et alors que je repense aux évènements de la journée, je me retrouve à me concentrer sur ma partenaire de course."


"Son refus complet de permettre à la pluie de gâcher ses plans était incroyablement mignon."


"Mais il y avait quelque chose d'autre, aussi."


"Une sorte d'attitude imperturbable quand il s'agit d'apprécier la journée."


"J'aime vraiment cette qualité."


"Peut-être que j'aurais besoin d’être un peu comme ça aussi."

stop ambient fadeout 2.0
scene black
with dissolve

$ suppress_window_after_timeskip = True



label fr_E12a:

window hide None

scene black
with dissolve

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show


"La sonnerie de mon réveil me sort d'un rêve avec des pirates et d'autres choses dont je n'arrive pas à me rappeler."

scene bg school_track
with locationskip

play music music_pearly

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")


"Je suis encore un peu dans le pâté, et il me faut plus longtemps qu'à l'habitude pour m'habiller et descendre sur la piste."


"Un regard à ma montre m'indique que j'ai raison, et que je suis même un peu en retard."


"Le truc c'est que..."


"Il n'y a pas d'Emi."


"C'est bizarre. Elle devrait être là."


"Elle devrait vraiment être là."


"Je veux dire, j'étais {b}en retard{/b}."


"Apparemment je ne suis pas le seul à avoir eu du mal à me lever ce matin."


"La pensée me traverse l'esprit que la pluie ne s'est jamais vraiment arrêtée hier. Est-ce qu'elle a été courir quand même ?"

label fr_E12b:




"C'est probable. Emi est beaucoup de choses, mais pas prudente. Elle a probablement pensé que la pluie s’arrêterait, et c'est pour ça qu'elle était si catégorie pour courir seule."


"Quand même, j'aurais couru avec elle avec plaisir, même si c'était sous la pluie."


"J'aurais été capable de la faire rentrer à l'intérieur quand c'est devenu assez violent. C'est sûrement pour ça qu'elle a refusé que je vienne avec elle."

label fr_E12c:




"J'aurais dû lui proposer de courir avec elle."


"J'aurais pu lui faire abandonner l'idée, ou au moins m'assurer qu'elle allait bien. Et si elle s'était fait frapper par la foudre ?"


"Je ne me le pardonnerais jamais."

"…"


"D'accord, c'est probablement un peu idiot."


"Emi est une fille débrouillarde. Je doute même qu'elle resterait dehors par un temps orageux."


"Je fais confiance à son jugement là-dessus, du moins."

label fr_E12d:




"Même là, je ne peux pas m’empêcher de me demander où elle est."


"...Bah, je ne peux rien y faire. Je ferais mieux de m'étirer et de courir, et d’espérer qu'Emi arrivera avec un sourire et une excuse."

scene bg school_track_running
with shorttimeskip

show bg school_track_on
with Dissolve(3.0)


"Sur mon tour de refroidissement, je suis forcé d'admettre qu'Emi n'arrivera pas."


"En plus de ça, je n'ai aucune idée d’où elle est. L’anxiété me ronge en même temps que je me demande pourquoi je suis aussi inquiet pour elle."


"La course m'a aidé à me sortir un peu ça de la tête, mais maintenant que j'ai fini, je recommence à m’inquiéter."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

nvl clear

nvl show dissolve


n "\n\nC'était bizarre de ne pas l'avoir avec moi."


n "Carrément troublant."


n "Je me rends compte que j'ai autant couru pour être avec Emi que pour rester en bonne santé - probablement plus pour être avec Emi, maintenant que j'y pense."


n "C'est une de ces choses qui sont totalement évidentes et pourtant, je ne l'ai jamais réalisé."


n "C'est vraiment quelqu'un avec qui j'apprécie d’être."


n "Les révélations sont loin d’être si étonnantes."


n "En même temps, je suis aussi légèrement choqué."


n "Quand est-ce que c'est arrivé ?"


n "Bon, pas le temps d'y penser - bien que j'aie bien envie d'y réfléchir un peu, j'ai bien plus envie de trouver ce qui est arrivé à Emi."


n "Je demanderai à l'infirmier quand j'irai le voir."

$ renpy.music.set_volume(1.0, 2.0, channel="music")
stop music fadeout 2.0

nvl clear

nvl hide dissolve

scene bg school_nurseoffice
show nurse neutral at center
with shorttimeskip


nk "Eh bien, tu sembles en forme, Hisao."


hi "Content de le savoir."


"Je remets mon t-shirt et me lève pour partir, comme d'habitude."


"Sauf qu'au lieu de partir, je pose une question."


hi "Hé, où est Emi ? Elle n'est pas venue ce matin."


hi "Elle va bien ?"

show nurse concern
with charachange


"Bien que j'essaye fortement de cacher l’anxiété dans ma voix, l'expression de l'infirmier m'informe que j'ai échoué misérablement."


nk "Tu veux dire qu'elle ne te l'a pas dit ?"


nk "Elle est au lit, malade."


hi "Quoi ? Malade ?"

show nurse neutral
with charachange


"L'infirmier hausse les épaules."


nk "Ouais, elle est venue à mon bureau tôt ce matin avec de la fièvre."


nk "Pour être honnête, je suis surpris qu'elle ait réussi à venir jusqu'ici."

show nurse concern
with charachange


nk "Elle brûlait de fièvre quand elle est arrivée."


nk "Je pensais qu'elle avait prévu de te le dire, mais elle m'a demandé de te dire - oh zut !"

stop music fadeout 2.0

show nurse neutral
with charachange


"L'infirmier m'adresse un sourire bête qui semble au moins partiellement sincère."


nk "Je lui ai dit que je passerais sur la piste pour te le dire si elle oubliait. Désolé."

play music music_nurse fadein 1.0

show nurse fabulous
with charachange


nk "Mais tu n'as pas besoin de dire à Emi que j'ai oublié, d'accord ?"


"Je retourne à l'infirmier un sourire sournois à mon tour."


hi "Oh, bien sûr que non."


hi "C'est une trop belle occasion pour la gâcher."


hi "Je la garde pour un jour où j'aurai besoin d'une faveur."

show nurse grin
with charachange


"L'infirmier rit."


nk "Bon, je crois que je l'ai mérité."


nk "Mais tu sais, j'ai des tonnes d'informations sur toi que tu ne soupçonnes même pas."


show nurse fabulous
with charachange


nk "Alors ne pousse pas trop le bouchon, d'accord ?"


"Mon expression déclenche un autre rire de la part de l'infirmier."

show nurse grin
with charachange


nk "Je plaisante, Hisao."

show nurse concern
with charachange


nk "Mais sérieusement - ne dis pas à Emi que j'ai oublié, d'accord ?"


hi "Votre secret est en sécurité avec moi."

show nurse neutral
with charachange


nk "Bien. Maintenant allez, sors d'ici."


hi "Attendez, j'ai une dernière question."

show nurse fabulous
with charachange


nk "Balance."


hi "Est-ce qu'elle ira bien ?"

show nurse grin
with charachange


nk "Oh oui, aucun problème."

show nurse neutral
with charachange


nk "Sa fièvre était forte, mais elle avait déjà commencé à redescendre au moment où elle est arrivée à mon bureau."


nk "J'irai sûrement vérifier qu'elle va bien pendant l'heure du déjeuner, mais je pense qu'elle sera debout ce soir quoi que je lui dise."


hi "Mmh, peut-être que je devrais aller la voir après les cours."


"Il me faut une seconde pour réaliser que j'ai parlé à voix haute."

show nurse fabulous
with charachange


"L'infirmier lève un sourcil et m'adresse un regard analytique pendant un moment."


nk "Mmh..."

show nurse neutral
with charachange


nk "Bah, ce n'est pas une mauvaise idée."


nk "Tu pourrais me dire si ça s'est empiré comme ça."

show nurse concern
with charachange


nk "Mais ne fais rien de bizarre, compris ? Je sais quels médicaments tu prends, après tout."


"Je crois que c'était une menace contre ma vie, mais je ne suis pas sûr."

stop music fadeout 7.0

scene bg school_nursehall
with locationchange


"Dans tous les cas, j'assure à l'infirmier que mes intentions sont pures et sors du bureau."


"Intéressant que l'infirmier me voie comme une sorte de prétendant potentiel pour Emi."


"Ce qui est encore plus intéressant est à quel point ça me fait plaisir."


"J'ai besoin d'une douche."


scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell


"La cloche du déjeuner sonne, et je me trouve peu enclin à me diriger vers le toit."


"Après tout, je suis sûr que Rin sait où se trouve Emi, et si c'est le cas je doute qu'elle s’embête à aller là-haut."


"En plus, je doute qu'on ait de quoi discuter si elle y allait. Il est probable aussi qu'elle préférerait être seule là-haut de toute façon, pour que je ne l'interrompe pas dans ses pensées ou autre."


"Malheureusement, je n'ai pas vraiment envie d'aller à la cafétéria non plus."


"Je vais aller à la bibliothèque dans ce cas."


"J'ai besoin d'un nouveau livre à lire de toute façon, ayant fini le dernier que j'avais hier avant de dormir. Peut-être que je pourrai en trouver d'autres du même auteur."

scene bg school_library
with locationskip

play music music_happiness fadein 2.0


"J'adore les bibliothèques."


"Il y a cette odeur de poussière, de papier et d'encre."


"Toutes ces histoires, faits et opinions rassemblés en un seul endroit rendent l'air vivant de potentiel."


"Je ne sais pas encore trop comment me repérer dans la bibliothèque de Yamaku, m'étant surtout contenté des livres que j'ai apportés avec moi, alors je cherche la bibliothécaire pour avoir de l'aide."

"…"


"Mmh. J'imagine qu'elle n'est pas l—{w=0.5}{nw}"

show yuuko smile_down:
    center
    xpos 0.4
    easein 0.5 center
with charaenter


yu "...peux pas y croire."


"Yuuko, ayant l'air distraite, surgit soudainement de l'une des ailes."


hi "Euh, excuse-moi."

show yuuko neutral_down
with charachange


yu "Oh, je peux t'aider ?"


hi "En fait, je cherche un livre..."

show yuuko panic_up
with charachange


yu "Moi aussi !"

show yuuko smile_down
with charachange


yu "“Cryptographie avancée”. On vient de l'avoir, et maintenant il a disparu."

show yuuko worried_up
with charachange


yu "Je voulais vraiment, vraiment le lire celui-là !"


hi "Cryptographie ?"

show yuuko neurotic_up
with charachange


yu "Ouais, mon... euh, c'est..."


yu "Ce gars que je connaissais. Connais. Hum."


yu "Je ne sais pas trop comment décrire ça..."


hi "Sois directe."

show yuuko smile_down
with charachange


yu "Il m'a intéressée à la cryptographie et maintenant le livre a disparu, et je crois qu'il a été volé !"


hi "C'est terrible."

show yuuko worried_up
with charachange


yu "Ouais, surtout parce que maintenant je dois fouiller la bibliothèque entière !"


yu "Même s'il n'est probablement même pas là !"


hi "Tu sembles... occupée."

show yuuko neurotic_up
with charachange


yu "Un peu."

show yuuko neurotic_up:
    center
    easeout 0.5 alpha 0.0 xpos 0.6
with None


"Elle se précipite dans une autre aile, et je me résigne à trouver mon fichu livre moi-même."


"Mmh, y a le choix."

stop music fadeout 2.0

hide yuuko
with shorttimeskip


"Roh sérieux, comment est-ce que j'ai pu me perdre ?"


"Ce ne sont même pas des livres imprimés ! Ils sont tous en braille."


"Ce qui n'est pas étonnant pour une école comme celle-ci, mais honnêtement, c'est un peu énervant."


li "Pardon, est-ce qu'il y a quelqu'un ?"


"Une voix vient d'une des cabines mises là pour étudier."

show lilly basic_displeased at center
with charaenter


"Alors que je m'approche, je constate que Lilly était en train de lire un livre pendant que je parcourais les ailes."


hi "Oh non, je devrais m'excuser. Je ne voulais pas faire autant de bruit."

show lilly basic_ara
with charachange


li "Eh bien, est-ce toi Hisao ?"

show lilly basic_smile
with charachange


li "Je ne t'avais pas entendu depuis un bon moment."

show lilly basic_pout
with charachange


li "Je commençais à penser que tu m'avais oubliée."


hi "Erh, désolé."

play music music_lilly fadein 4.0

show lilly basic_giggle
with charachange


"Lilly rit à sa manière raffinée habituelle et secoue la tête."

show lilly basic_smile
with charachange


li "Je t’embête, Hisao."


li "D’après ce que j'ai entendu, tu as été occupé."

show lilly basic_cheerful
with charachange


li "Courses matinales avec Emi Ibarazaki {b}et{/b} déjeuner sur le toit, si je ne me trompe pas."


hi "Euh, ouais."


hi "On dirait que les nouvelles vont vite."

show lilly basic_weaksmile
with charachange


li "Maintenant je ne peux plus cajoler la pauvre Hanako sur le toit."

show lilly basic_displeased
with charachange


li "Vous êtes toujours tous les trois là-haut, à croire que l'emplacement n'est rien que pour vous."


"Elle me gronde gentiment, bien qu'il est clair qu'elle ne fait ça que pour m’embêter encore une fois."


"Pourtant, je ressens un étrange besoin de m'excuser."


hi "Désolé, on pourrait manger ailleurs si c'est un réel problème—"

show lilly basic_ara
with charachange


li "Oh non, ne t’embête pas pour ça."

show lilly basic_smile
with charachange


li "Hanako et moi avons d'autres choses à faire durant le déjeuner aussi."


li "Tel que lire dans la bibliothèque, comme tu peux le voir."


hi "Oh, Hanako est là aussi ? Je ne l'ai pas vue."

show lilly basic_smileclosed
with charachange


"Lilly sourit, un peu énigmatique."


li "Oh, elle est là quelque part."

show lilly basic_smile
with charachange


li "Mais je suis surpris, Hisao. Tu es ici au lieu de là-haut."


li "Qu'est-ce qui t’amène à la bibliothèque ?"


hi "En fait Emi est malade, alors il n'y a pas de déjeuner sur le toit pour me tenir occupé..."

show lilly basic_giggle
with charachange


"Lilly lève un sourcil à ma phrase avant de sortir un petit rire."


li "Eh bien, la pauvre Rin doit se sentir abandonnée."


hi "Ce n'est pas ça !"

show lilly basic_weaksmile
with charachange


li "Ah, mais j'en suis sûre. Emi a l'habitude d’être l’élément actif du groupe dans lequel elle est."

show lilly basic_sad
with charachange


li "Je suis attristée d'entendre qu'elle est malade. Ce n'est pas trop grave ?"


"J'ai l'impression que Lilly demande surtout par politesse, mais je réponds quand même."


hi "L'infirmier dit que ça va. J'irai voir comment elle va après les cours."

show lilly basic_smileclosed
with charachange


"Et un autre sourcil levé."


li "Eh bien, quel noble gentleman tu fais, Hisao."


hi "Ce n'est rien, vraiment. Je m’inquiète juste pour une amie après tout."

show lilly basic_planned
with charachange


li "Ah, donc c'est juste une amie ? C'est bien dommage."


"Je rougis, content que Lilly ne puisse pas le voir."

show lilly basic_giggle
with charachange


"Mais, à sa façon, elle sait que j'ai été embarrassé par son commentaire quand même, et rit."


li "Je suis désolée, Hisao. Je t’embête encore une fois."

show lilly basic_smile
with charachange


li "Dis à Emi que je lui souhaite de vite se rétablir, d'accord ?"


"Un regard à ma montre me révèle que je suis presque à court de temps pour trouver mon livre."


hi "Bien sûr."


hi "Bon, je dois encore trouver un livre avant la fin de la pause déjeuner, alors je ferais mieux d'y aller."


hi "On se voit plus tard."


"Ce n'était probablement pas la meilleure phrase à utiliser."


"Lilly, cependant, surmonte ma gaffe immédiatement."

show lilly basic_weaksmile
with charachange

stop music fadeout 3.0


li "À la prochaine, Hisao."

scene bg school_hallway2
with shorttimeskip


"Je n'ai pas trouvé le livre que je cherchais, mais finis par sortir avec un autre à la place."


"Mon estomac grogne légèrement, me faisant savoir que j'aurais dû manger quelque chose pour déjeuner."


"Tant pis."


"Je prendrai quelque chose avant d'aller voir Emi plus tard."


label fr_E13:

scene bg school_hallway2
with None

scene bg school_scienceroom
with shorttimeskip

play music music_normal fadein 3.0


"On dirait que le temps a décidé de ralentir dans l'unique but de m’exaspérer."


"Les cours semblent s'éterniser."


"Je soupçonne mon inquiétude d'y être pour quelque chose."

play sound sfx_normalbell


"Bénissant la sonnerie, je sors en quatrième vitesse de la classe, faisant lever quelques sourcils au passage, je suis sûr."

scene bg school_hallway3
with locationchange


"J'ai passé la majeure partie de la journée à me ronger les sangs aussi discrètement que possible."


"Même si l'infirmier pense qu'Emi va parfaitement bien, je veux m'en assurer."

stop music fadeout 14.0

scene bg school_girlsdormhall
with locationskip


"Il ne me faut pas longtemps pour arriver au dortoir des filles et faire mon chemin jusqu’à la chambre d'Emi."


"Me tenant devant la porte, je m’arrête soudainement. Et si elle se repose ?"


"Je n'aimerais pas la réveiller, surtout si elle est encore malade."


"Mais cela dit, si elle dort toute la journée, ça pourrait décaler ses horaires de sommeil."


"Mais c'est important de se reposer quand on est malade, hein ?"


"Je n'arrive pas à décider quoi faire, alors je me contente de rester debout devant sa porte comme un idiot."


"Puis j’entends la voix d'Emi à l'intérieur."


emi "Merci de t’inquiéter, mais je vais bien, vraiment."


"Est-ce que c'est à moi qu'elle parle ?"


emi "Je te verrai à l’entraînement demain !"


"Ah bah non."


"Cela dit, elle ne dort pas, alors je peux frapper sans m’inquiéter."


"Alors pourquoi j'ai le ventre serré comme ça ? Je n'étais pas nerveux en passant l'autre jour, alors pourquoi aujourd'hui ?"


"Je n'ai toujours pas eu le temps de comprendre ce nouvel intérêt concernant le bien-être d'Emi."



"Je n'ai pas beaucoup d'expérience dans le domaine, bien sûr, mais ça semble aller plus loin que des sentiments basiques d'amitié."


"Mais est-ce que je pourrai franchir cette étape ? Est-ce que je pourrais aller jusqu'à risquer ce que j'ai ?"


"Je veux dire, c'est suffisant d’être ami avec elle, non ?"


"Dans tous les cas, je ne devrais pas juste ouvrir la porte et voir comment elle va ? C'est pour ça que je suis venu ici... hein ?"

stop music fadeout 1.5


"Et si elle n'est pas présentable ?"

play ambient sfx_heartslow

with Fade (0.05, 0.0, 0.3, color="#ffc0cb")


"Les images qui me traversent l'esprit poussent mon cœur à battre plus rapidement, littéralement."

stop ambient fadeout 3.0


"Je devrais probablement éviter de penser à quelque chose comme ça. Pas si je veux éviter une crise cardiaque."


"Je réalise soudainement que je me tiens toujours debout dans le couloir comme un idiot."

play sound sfx_doorknock2


"Emi semble toujours être au milieu d'une conversation, mais je frappe quand même. J’espère que l'interruption ne la gênera pas."


emi "Tu t’inquiètes tr— Entrez ! C'est ouvert."


"D'accord. J'ouvre la porte et fais un pas en avant, et c'est à ce moment que mon esprit se met en pause immédiate."

play music music_serene fadein 4.0

scene ev emi_sleepy_face:
    subpixel True
    center
    zoom 1.05
    ease 15.0 zoom 1.0
with whiteout


"Emi est assise sur son lit, les cheveux ébouriffés d'une journée passée à dormir. Je crois que c'est la première fois que je la vois sans ses couettes."


"Son t-shirt et son short de sport, évidemment mis en hâte avant que j'entre, sont assez mal mis et ajustés."

scene ev emi_sleepy_legs at Fullpan(8.0)
with flash


"Ses jambes nues sont posées sur les draps."


"Je n'avais jamais vu Emi sans ses prothèses. Et pourtant elle est là, ses fines jambes finissant en moignons juste sous ses genoux."


"Mais aussi étrange que la vue puisse être, je suis encore plus captivé par ce que je vois au-dessus de la ceinture."

scene ev emi_sleepy:
    subpixel True
    center
    zoom 1.05
    ease 15.0 zoom 1.0
with flash


"On dirait qu'Emi a fini la conversation avec la personne avec qui elle parlait au téléphone, et qu'elle est maintenant en train d'observer ma réaction avec attention d'un œil ouvert pendant qu'elle frotte l'autre encore endormi."


"Sur son visage, au lieu de trouver de l'embarras, se profile un très long bâillement. Ce qui est peut-être normal pour une si petite bouche."


"Un sourire, qui pour un bref moment semble presque coquet, s’affiche au coin de ses lèvres alors qu'elle me voit entrer."


"Je ne peux rien faire à part rester dans un état fluctuant entre la peur, la confusion, et un peu d'attirance."


"Emi enlève rapidement les cheveux qu'elle a devant les yeux, les remettant en place avant de me parler."

scene bg school_dormemi
show emi sad_grin_gym at center
with locationchange


emi "Tu sembles un peu surpris, Hisao."


"Elle éclate de rire et je me retrouve à sourire bêtement et à me frotter l’arrière de la tête."


hi "Désolé, j'ai juste..."


"Jamais vu quelqu'un être aussi attirant tout en étant aussi mal réveillé et ébouriffé."


"Jamais vu sans tes jambes."


"Jamais vu ayant l'air aussi..."


hi "Hum, désolé."

show emi basic_closedgrin_gym
with charachange


"Emi rit encore une fois et se redresse un peu plus."


"Je suis captivé par les mouvements que fait son t-shirt, me retrouvant à l’extrême limite de dérailler."

show emi basic_grin_gym
with charachange


emi "Je me demandais comment tu réagirais."

show emi basic_closedhappy_gym
with charachange


emi "L'infirmier m'a appelée pour me dire que tu passerais, tu sais."

show emi basic_grin_gym
with charachange


emi "Et je sais que tu ne m'avais pas vue... enfin, tu sais."

show emi sad_grin_gym
with charachange


emi "Sans jambes."


"Je réponds d'un ton légèrement étonné."


hi "Oh, tu ne les avais pas ? Je n'avais pas remarqué."


"C'est presque la vérité. Je ne l'ai presque pas remarqué."


"Je n'essaye pas d’être gentil exprès ou autre. Je crois qu'Emi m'en voudrait si je le faisais."

stop music fadeout 0.5
play sound sfx_pillow
show emi basic_annoyed_gym
with vpunch


"Au lieu de ça, elle tire la langue et me balance un oreiller à la tête."


emi "Salaud."


"J'attrape l'oreiller au vol et vise avec précaution avant de le jeter."

play music music_running

show emi basic_annoyed_gym:
    center
    parallel:
        ease 0.5 xpos 0.7
    parallel:
        "emi basic_closedhappy_gym" with Dissolve(0.5, alpha=True)


"Emi rit et roule sur le côté, évitant mon tir, et le mouvement de son t-shirt me distrait suffisamment pour que le prochain oreiller jeté m'arrive en pleine tête."

play sound sfx_pillow


hi "Uwah !" with hpunch


"Je contre-attaque, bien sûr."


"Et maintenant que nous avons chacun contre-attaqué deux fois, une guerre va éclater tôt ou tard."


"Et vu qu'Emi semble être d'une précision bien meilleure que la mienne, eh bien..."


"Ce n'est qu'une question de temps avant que je n'aie à recourir à une attaque suicide."

show bg school_dormemi:
    center
    ease 0.5 bgleft

show emi basic_closedhappy_gym:
    ease 0.5 center

with None

show emi basic_closedhappy_gym_close:
    ease 0.5 center

with characlose


hi "Attrapée !"

show emi basic_hes_gym_close
with charachange


emi "Hii !"

window hide None

play sound sfx_pillow

show comic vfx1
show emi basic_closedsweat_gym_close
with vpunch

with Pause(0.5)

play sound sfx_pillow

show comic vfx2
with hpunch

with Pause(0.5)

play sound sfx_pillow

show comic vfx3
with vpunch

with Pause(0.5)

show comic vfx3:
    truecenter
    easeout 0.5 yanchor 0.3 alpha 0.0
with Pause(0.5)







stop music fadeout 3.0

scene black
with dissolve

window show


"Et maintenant que l'attaque est lancée, eh bien, bien sûr, je dois me battre au corps à corps pour lui reprendre l'oreiller."


"Et avec ce genre de lutte, il est évident qu'on finit dans ce genre de position."

window hide

play music music_twinkle fadein 2.0

scene ev emi_bed_full:
    xalign 0.5 yalign 1.0 subpixel True
    easein 15.0 yalign 0.0

with Dissolve(1.0)

with Pause(3.0)

window show


"Et donc je me retrouve à la regarder, à genoux au-dessus d'elle."


"Elle sourit, les yeux pétillants d'amusement, peut-être un peu en sueur à cause de la bagarre."


"Sa poitrine se gonfle et se dégonfle rapidement, brassant de l'air."


"Le petit côté restant de mon cerveau qui n'apprécie pas la vue et l'odeur d'Emi constate qu'elle doit être toujours malade, parce que son endurance n'est pas ce qu'elle devrait."


"Nous restons comme ça pendant un moment."


"Je ne sais pas combien de temps, parce que tout semble un peu flou. Tout ce qui n'est pas elle, du moins."


"Ses yeux rencontrent les miens, et profondément à l'intérieur je vois presque un soupçon de... quoi, peur ? Désir ?"


"Espoir ?"


hi "Emi... ?"

stop music fadeout 0.5

show ev emi_bed_unsure at center
with vpunch


"Elle tousse soudainement, et je tombe presque dans ma hâte de lui laisser de l'air, et m'excuse pour tout."

play music music_emi fadein 3.0


hi "Désolé, je n'aurais pas dû..."

show ev emi_bed_happy
with charachange


emi "C'est bon, c'est bon."


"Elle m'adresse une tape rassurante sur l'épaule."

show ev emi_bed_normal
with charachange


emi "Alors... qu'est-ce qui t’amène ici ?"


"Elle respire toujours fortement, ce qui fait que sa voix tremble légèrement."


hi "Eh bien, avant que je sois agressé par des oreillers, je venais voir comment tu allais."

window hide None

play sound sfx_pillow

show comic vfx4
show ev emi_bed_frown
with vpunch

with Pause(0.5)

show comic vfx4:
    truecenter
    easeout 0.5 yanchor 0.3 alpha 0.0
with Pause(0.5)

window show


"Ce qui me vaut une autre frappe, et je tombe presque de son lit."

show ev emi_bed_normal
hide comic
with charachange


"Les yeux d'Emi pétillent à nouveau, et je me demande comment j'ai fait pour ne pas remarquer à quel point ils étaient séduisants auparavant."

show ev emi_bed_smile
with charachange


emi "Consumé par l’inquiétude, hein ?"


"Son ton est moqueur, arrogant. Taquin."


"Elle met son avant-bras sur son front avec un air dramatique, un sourire apparent."

show ev emi_bed_unsure
with charachange


emi "Tu ne pouvais pas supporter l'idée de me voir mortellement malade ?"


"Alors que nous récupérons tous les deux après les efforts de notre match de catch, Emi semble avoir fini de me taquiner."


hi "Bon, je ne dirais pas que j'étais consumé par l’inquiétude, mais après que tu ne sois pas venue ce matin comme une super mauviette..."

show ev emi_bed_frown
with charachange


"Emi fait la moue, croise les bras fermement et fait ressortir sa lèvre inférieure."


emi "C'est pas ma faute."


emi "L'infirmier voulait pas."


hi "J'en suis sûr. Je te fais complètement confiance."


"Emi me tire la langue une fois de plus."


emi "T'es qu'un idiot, Hisao."


hi "Alors comment a été ta journée, hein ? Tu as apprécié ne rien faire ?"

show ev emi_bed_normal
with charachange


emi "Pas vraiment, le téléphone m'a réveillé assez tôt."


hi "Le téléphone ?"


emi "Ouais, le capitaine de l'équipe m'a appelée pour s'assurer que j'allais bien."


emi "Et aussi pour me faire savoir que c'était pas grave si je loupais l’entraînement."


"Bien, au moins elle n'était pas toute seule toute la journée. Quelqu'un a vérifié qu'elle allait bien."


"Bien que je n'arrive pas à m’empêcher de penser que ça aurait dû être moi."


hi "Oh, c'est bien."


hi "Il veille vraiment sur toi, hein ?"

show ev emi_bed_smile
with charachange


"Emi hausse les épaules."


emi "C'est son job."


emi "Une partie du travail du capitaine consiste à savoir où sont les membres de son équipe quand ils ne sont pas à l'école."


emi "Ça reste gentil à lui d'appeler, hein ?"


hi "Oui, c'est sûr."


"Emi bâille et gigote pour se mettre dans une position plus confortable."

show ev emi_bed_normal
with charachange


emi "Alors comment était ta journée ?"


hi "Assez banale, tu sais ?"


hi "J'ai couru tout seul, j'ai parlé avec l'infirmier de comment tu allais..."

stop music fadeout 2.0

scene bg school_dormemi_ni
with shorttimeskip


"Je raconte les évènements de ma journée, bien qu'aucun d'entre eux ne soit vraiment intéressant."


"Jusqu’à ce que je sois distrait par un bras passant autour de ma taille."


"On dirait qu'Emi s'est endormie pendant que je parlais, alors je tire sa couverture pour nous couvrir."

play music music_comfort fadein 9.0

scene ev emi_sleep_unsure
with locationchange


"Elle est en boule sur le côté, et maintenant a une jambe au-dessus des miennes, m'entravant."


hi "Hé."


"Ça serait dommage de la réveiller, mais j'ai des choses à faire."

play sound sfx_rustling


"Je la secoue gentiment, mais en réponse elle ne fait que resserrer la prise de son bras sur moi et souffle un peu."


"La résistance dont je fais preuve pour rester comme ça s'effrite vite."


"La sensation de son corps respirant en rythme est à la fois reposant et incroyablement stimulant."


"Ma respiration a du mal à décider si elle veut se relaxer ou s’accélérer."


"Le calme me gagne, et je me retrouve à passer mon bras autour d'Emi."

scene ev emi_sleep_normal
with dissolve


hi "Je crois que je suis amoureux."


"Les mots sortent et restent en suspens dans l'air, n'ayant pas été entendus."


"Du moins je l’espère."

scene ev emi_sleep_weep
with dissolve


"Emi larmoie légèrement en rêvant, et sa poigne se raffermit soudainement encore une fois."


"Pour la première fois depuis que je la connais, je vois des larmes couler sur le visage d'Emi."


"J'ai l'impression que mon cœur est sur le point de se briser."


"Je raffermis également ma prise par réflexe et lui caresse les cheveux d'une façon que j’espère apaisante."


"Des mots pour la rassurer, inutiles dans cette situation, me viennent à l'esprit."


"Peut-être que je devrais la réveiller. On est censés réveiller les gens qui font des cauchemars ?"


"Je n'arrive pas à me le rappeler."


"Ma décision est prise alors qu'Emi s’éveille en sursaut avec un cri."

scene ev emi_sleep_cry
with dissolve


emi "Papa !"


"C'est... plus que je pense pouvoir en supporter sans la réveiller. Je me redresse rapidement et lui secoue gentiment l'épaule."

scene bg school_dormemi_ni
with locationchange


hi "Hé, ça va ?"


"Question idiote."

show emi basic_shock_gym_close_ni at tworight
with charaenter


emi "Hein ? Quoi ?"

show emi basic_hes_gym_close_ni
with charachange


emi "Hisao ?"


"Elle secoue la tête comme pour la vider et se frotte rapidement les yeux."


hi "Tu as fait un cauchemar. Je crois."

show emi sad_shy_gym_close_ni
with charachange


"Emi frissonne encore une fois et me regarde avec une légère appréhension, comme si elle n'était pas sûre d’être vraiment réveillée."


emi "Ou-ouais, je crois."


hi "Tu veux en parler ?"


emi "Mmh ?"


"Un rapide débat interne se tient dans sa tête, et se termine par un haussement d'épaules."

show emi basic_hes_gym_close_ni
with charachange


emi "Nan, je ne m'en rappelle pas trop."


"Je suis presque sûr qu'elle me ment, mais je ne pense pas que je doive insister."

show emi sad_shyblush_gym_close_ni
with charachange


"Emi frissonne encore une fois et se tourne vers moi, semblant un peu penaude."


emi "Désolée de m’être endormie sur toi comme ça."


"Je garde ma voix aussi calme et apaisante que possible."


hi "Hé, ne t’inquiète pas pour ça. Tu es encore un peu malade."


emi "Ouais, je crois que les médicaments pour le rhume m'ont rendue un peu somnolente."


hi "Je crois bien."


"Emi ne me semble pas être le type de personne qui s'endort à des moments incongrus."


"Rin, peut-être. Mais Emi est bien trop énergique."

show emi basic_grin_gym_close_ni
with charachange


"Emi m'adresse un petit sourire, et juste comme ça, elle est redevenue elle-même."

show emi basic_closedgrin_gym_close_ni
with charachange


emi "Bon, prépare-toi pour demain matin, Hisao !"

show emi excited_proud_gym_close_ni
with charachange


emi "On courra deux fois plus pour compenser aujourd'hui !"


hi "Mais j'ai couru ce matin !"

show emi basic_annoyed_gym_close_ni
with charachange


emi "Pas d'excuse !"


hi "Roh d'accord, je t'attendrai !"

show emi basic_grin_gym_close_ni
with charachange


"Emi hoche la tête, satisfaite."


emi "Bien."


"J'estime qu'il est temps pour moi de partir."


hi "Bon, je ferais mieux d'y aller. Surtout si je veux suffisamment dormir pour demain."

show emi basic_grin_gym_ni
with vpunch


"Je sors du lit et me dirige vers la porte."

show emi sad_shy_gym_ni
with charachange


emi "Dis, Hisao..."


hi "Mmh ?"


"Je pivote sur un talon et fais face à Emi."

show emi basic_hes_gym_ni
with charachange


"Elle ouvre la bouche pour dire quelque chose, et dans la même seconde, je la vois hésiter."


"Elle ferme la bouche et la rouvre après."

show emi sad_grin_gym_ni
with charachange


emi "... Merci."


emi "D'être passé, je veux dire."


emi "Tu es le premier visiteur que j'ai jamais eu, à part Rin."


"Ça me surprend. J'aurais cru qu'Emi aurait vu défiler des gens toute la journée."


"Elle est suffisamment populaire, du moins je crois. Elle parle toujours à des gens dans les couloirs."

show emi sad_shy_gym_ni
with charachange


"Emi hésite de nouveau."


emi "Et merci d’être resté après que je... enfin."

show emi sad_depressed_gym_ni
with charachange


"Une grimace douloureuse se profile sur son visage."


emi "Tu sais."

show emi sad_grin_gym_ni
with charachange


emi "Ça m'a aidée."

show emi basic_closedgrin_gym_ni
with charachange


"Elle s'illumine de nouveau et me fait joyeusement un signe de la main."


emi "Je te vois demain !"


hi "Ouais, à plus tard."


"Je suis sur le point de passer la porte quand quelque chose me fait me retourner encore une fois."


hi "Hé, Emi."

show emi basic_grin_gym_ni
with charachange


emi "Mmh ?"


hi "Si tu as besoin de parler, je suis toujours là, d'accord ?"

show emi sad_shy_gym_ni
with charachange


"Emi semble surprise par mon offre."

show emi basic_closedgrin_gym_ni
with charachange


"Son sourire s'élargit encore plus."


emi "Bien sûr, Hisao."

show emi basic_grin_gym_ni
with charachange


emi "À demain matin !"

scene bg school_girlsdormhall_ni
with locationchange


"Je sors de la chambre d'Emi avec la tête qui tourne un peu."


"Est-ce que j'ai bien fait de partir ?"


"Elle allait vraiment bien ?"


"J'ai envie de faire demi-tour, retourner à sa chambre, ouvrir la porte et lui dire..."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl clear

nvl show dissolve


n "\n\nLui dire que je l'aime, lui dire que je la trouve magnifique, lui dire que je serai là quand elle aura besoin de moi."


n "Je veux rester avec elle, la tenir contre moi alors qu'elle se rendort."


n "Combien de nuits a-t-elle passées à se réveiller comme ça ?"


n "Et à réaliser qu'il n'y a personne."


n "Je veux être la personne qui peut être avec elle quand ça arrive."


n "C'est une pensée idiote, je sais."


n "On ne se connaît pas si bien que ça, hein ?"


n "L'idée, bien qu'exaltante, m’inquiète aussi."


n "Inquiet, peut-être, que ça dépasse les limites de notre relation."


n "Et maintenant, comme pour accumuler les problèmes, on dirait qu'Emi est déjà intéressée par quelqu'un d'autre."

nvl clear


n "\n\n\n\n\n\nCe capitaine d’athlétisme qui semble si intéressé par son bien-être."


n "Il est vrai, je ne les ai vus ensemble que quelques fois, mais ça ne change pas le fait qu'ils semblent bien aller ensemble."


n "Et je ne peux pas faire grand-chose pour ça."


n "J'ai besoin de penser à autre chose."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear

nvl hide dissolve

window show


"J'ai des devoirs à faire."


"Peut-être que ça me distraira."

stop music fadeout 2.0

$ suppress_window_after_timeskip = True

scene black
with dissolve


label fr_E14:

window hide None

scene black
with dissolve

scene bg school_dormhisao
with openeye

window show


"Je me sens fatigué ce matin après avoir aussi mal dormi."

play music music_drama fadein 8.0


"Les évènements du jour précédent n'ont pas arrêté de me tracasser."


"Le souvenir d'Emi contre moi."


"Le souvenir de notre match de catch."


"Et le plus gênant, le souvenir de son cauchemar."


"Elle souffrait tellement."


"Je ne peux pas m’empêcher de me demander ce que ça doit être de se réveiller sans quelqu'un à ses côtés."

scene bg school_dormbathroom
show steam
with locationskip

play ambient sfx_shower fadein 1.0


"La douche chaude me réveille. Réveillé, mais toujours inquiet."

$ renpy.music.set_volume(0.5, 1.0, channel="ambient")
$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide

nvl show dissolve

nvl clear


n "\nQu'est-ce qui se passera aujourd'hui ?"


n "Est-ce que les choses redeviendront juste comme avant ?"


n "Fin de l'épisode, retour à la normale ?"


n "On avait une connexion hier. Quelque chose qui nous a presque poussés au-delà des limites d'une amitié normale."


n "Ça aurait été aussi mal que ça ?"


n "Je repense aux yeux d'Emi après notre combat d'oreillers. On aurait presque dit qu'ils me défiaient d'aller plus loin."


n "Presque."


n "Mais je ne peux pas être sûr."


n "De toute façon, le capitaine de l'équipe est probablement premier dans la liste des personnes qu'elle apprécie."


n "Mais j'ai beau penser ça, mon cerveau se moque de moi. Je cherche juste une excuse. Une raison pour que tout aille mal."


n "Une raison pour ne pas essayer."

nvl clear


n "\n\n\n\nCe n'est pas comme si je les avais déjà vus ensemble en dehors d'un entraînement sur le terrain."


n "Et visiblement il n'a jamais été la voir. Emi l'a dit elle-même. S'ils étaient proches, il y serait sûrement allé."


n "Je suis vraiment une mauviette."


n "Je dois le faire quand même, au diable les conséquences."


n "C'est ce que ferait Emi, je crois. Non, je {b}sais{/b} que c'est ce qu'elle ferait."


n "C'est en partie pourquoi je ne suis pas convaincu qu'elle soit intéressée. Elle n'a pas agi non plus."


n "Peut-être à cause du capitaine du club. Il est possible qu'elle vive un amour à sens unique."

nvl clear


n "\n\n\n\n\n\nMais qui pourrait être capable de clarifier leur relation ?"


n "Emi n'est même pas envisageable. Elle rirait sûrement et me demanderait pourquoi je veux savoir... et je ne suis pas encore prêt à répondre à ça."


n "Rin... Rin me donnerait probablement une réponse incompréhensible. Et avec la chance que j'ai, elle demanderait à Emi, qui me demanderait alors pourquoi je veux savoir, et j'ai déjà abordé le sujet."


n "Je me demande..."

nvl clear


n "\n\n\n\n\nEst-ce que je pourrais demander à l'infirmier ? Il semble très protecteur avec Emi. Je suis sûr qu'il le saurait si quelque chose se passait..."


n "Et il m'en doit une pour ne pas avoir dit à Emi qu'il avait oublié de me prévenir qu'elle était malade, alors il restera discret."


n "Et s'il me demande pourquoi je veux savoir ?"


n "Je pourrais esquiver. Juste dire que je suis curieux en tant qu'ami. Il arriverait à me croire, non ?"


n "Bien sûr !"


n "C'est réglé alors."


n "Après avoir couru, je lui demanderai pendant qu'Emi attendra en dehors du bureau."

stop ambient fadeout 2.0

nvl clear

nvl hide dissolve

scene bg school_track
with locationskip

nvl show dissolve


n "\n\n\n\nIl n'y a aucun signe d'Emi quand j'arrive à la piste. Elle est encore trop malade pour venir ?"


n "Je décide de lui donner dix minutes."


n "Je suis un peu en avance, et elle était malade hier, alors si elle prend un moment pour venir, ça ne serait pas surprenant."


n "Quand même, je détesterais perdre du temps, alors je m'occupe en m'étirant et tournant en rond, anxieux."


n "Et si j'ai été trop loin hier ?"


n "Et si elle ne vient pas parce qu'elle est embarrassée ?"


n "Et si..."

$ renpy.music.set_volume(1.0, 2.0, channel="music")
$ renpy.music.set_volume(1.0, 2.0, channel="ambient")

nvl clear

stop music fadeout 2.0

nvl hide dissolve

window show

show emi basic_closedgrin_gym at center
with charaenter


emi "Tu es encore arrivé tôt, Hisao !"

show emi excited_proud_gym
with charachange


emi "Je suis impressionnée."


"Et juste comme ça, je sens la tension sortir de mon corps."


"Emi semble être joyeuse comme d'habitude, rien qui ne laisse transparaître qu'elle était malade l'autre jour, ni qu'elle ait pu passer une mauvaise nuit."


"Malgré ça, je dois demander."


hi "Tu as bien dormi la nuit dernière ?"

play music music_serene


"C'est juste une question comme ça. Rien d'important."


"Le genre de choses que se demandent les gens quand ils se rencontrent lors du café du matin."


"Mais pas pour nous. Du moins, pas pour moi."


"Je ne sais pas si Emi réalise que je suis vraiment inquiet quant au fait qu'elle ait bien dormi la nuit dernière, mais la question lui impose un moment de réflexion."

show emi basic_grin_gym
with charachange


"Après un court moment de ce qui semble être une réflexion intense, elle hoche la tête."

show emi basic_closedhappy_gym
with charachange


emi "Ouais ! Très bien !"


"C'était grâce à moi ?"


"Est-ce que j'ai vraiment aidé ?"


"Ou est-ce qu'elle dit ça juste pour m’empêcher de poser d'autres questions  ?"


hi "Tant mieux."

show emi basic_closedgrin_gym
with charachange


"Emi sourit et commence à s'échauffer."

show emi basic_grin_gym
with charachange


emi "Alors, prêt à commencer ?"


hi "Pfft, si je suis prêt ? Bien sûr que je suis prêt ! J'étais prêt avant que tu naisses !"

show emi basic_closedhappy_gym
with charachange


"Emi rit de ma témérité, et nous nous mettons à courir."

scene bg school_track_running
with shorttimeskip


"Je garde un rythme soutenu tout le temps, et respire régulièrement."

scene bg school_track_on
with Dissolve(2.0)


"Je me sens toujours mort en fin de compte, mais au moins je ne suffoque pas comme un poisson hors de l'eau maintenant."

show emi basic_happy_gym:
    center
    xpos 0.6
    easein 0.5 center
with charaenter


"Emi est rayonnante après la course aujourd'hui."


emi "Bien joué, Hisao ! Tu t’améliores !"

show emi basic_closedgrin_gym
with charachange


emi "Tu seras moitié moins rapide que moi en un rien de temps !"


"Sa dernière phrase est dite avec un ton moqueur auquel j'ai appris à m'habituer."


hi "Oh, vraiment excitant."

play ambient sfx_emisprinting

$ renpy.music.set_volume(0.3,1.0,channel="ambient")

hide emi
with easeoutleft


"Emi commence à faire ses sprints pendant que je fais un tour pour me refroidir."


"Elle se donne vraiment à fond aujourd'hui."

stop ambient fadeout 1.0

scene bg school_track
with shorttimeskip

$ renpy.music.set_volume(1.0,0.0,channel="ambient")


"Au moment où j'ai fini le tour, elle est allongée sur un banc des gradins, semblant vraiment épuisée."


hi "Eh bien, tu ne serais pas en train de pousser un peu trop aujourd'hui ?"


hi "Tu sors juste d'un rhume, après tout."

show emi basic_annoyed_gym at center
with charaenter


"Emi souffle, visiblement agacée, et s'assoit."


emi "Bah ! Je compense juste pour le temps perdu, c'est tout."

show emi excited_happy_gym
with charachange


emi "J'ai fait deux fois plus aujourd'hui, tu sais."

show emi excited_laugh_gym
with charachange


emi "Une bonne course remet le corps d'aplomb, tu sais."

show emi basic_closedgrin_gym
with charachange


emi "Ça fait le vide dans la tête aussi."


hi "Oh ?"

show emi excited_happy_gym
with charachange


"Emi hoche vigoureusement la tête."

show emi excited_amused_gym
with charachange


emi "Ouais ! C'est une bonne solution pour ce genre de choses."


"Elle n'explique pas plus, et je ne demande pas."


"Je pense que je sais pourquoi elle en a tant fait aujourd'hui."


"Être malade n'avait rien à voir avec ça. Quelque chose la troublait."


"Peut-être les cauchemars. Peut-être autre chose."



"Mais ce n'est pas mes affaires."


"Elle me le dirait si elle voulait que je le sache."


hi "Je suis sûr que c'est pratique."

show emi basic_grin_gym
with charachange


emi "Tu n'as pas idée."


"La sincérité dans sa voix confirme mes soupçons."


"Le seul problème est que..."


"Même si je sais qu'elle me le dirait si elle voulait que je sache, je veux quand même savoir."


hi "Quelque chose en tête qui te tracasse ?"


"Emi ne semble pas surprise par ma question."

show emi basic_closedgrin_gym
with charachange


"Au lieu de ça, elle hausse les épaules."

show emi sad_grin_gym
with charachange


emi "Nan, rien qui vaille la peine de s’embêter."


"On dirait qu'elle essaye autant de me convaincre moi qu’elle-même."


"J'ouvre la bouche pour demander si c'est à cause d'hier, mais pense qu'il ne vaut mieux pas."


"Trop de risques qu'elle interprète mal la question."


"En plus, je ne suis même pas sûr de savoir moi-même quoi penser d'hier."


"Je n'arrive à penser qu'à ce que j'ai ressenti quand Emi dormait à côté de moi avant que mon cerveau ne se coupe."


"L'avoir devant moi maintenant, couverte de sueur et me regardant comme ça, rend ma réflexion difficile."


hi "D'accord, pas de problème."

show emi basic_hes_gym
with charachange


emi "On ferait mieux de se dépêcher d'aller voir l'infirmier. On n'a plus beaucoup de temps."


hi "Comme d'habitude en fait."

show emi basic_grin_gym
with charachange


"Emi rit à mon commentaire, un rire sec qui semble vraiment peu Emi-esque."

show emi sad_grin_gym
with charachange


emi "C'est vrai."


"Pendant un bref moment, elle semble vieille, épuisée par de vieilles blessures."


"Mais tout comme hier, elle peut presque littéralement remettre son fardeau sur ses épaules et se redresser."


"Et la voilà redevenue Emi à nouveau."

show emi excited_proud_gym
with charachange


emi "On y va Hisao. J'vais te battre !"

play ambient sfx_emisprinting

hide emi
with easeoutleft

stop ambient fadeout 2.0


"Avec un sourire soudain, elle s'en va comme une fusée."


hi "Hé, c'est pas juste !"


"Je pars après elle, même si je sais que je ne l'attraperai pas, mais je m'en moque."


"Même s'il n'est pas possible que je puisse l'attraper, je courrai quand même après elle."

stop music fadeout 2.0

scene bg school_nursehall
show emi basic_grin_gym at center
with locationskip


"Emi attend à la porte que j'arrive."

show emi basic_closedhappy_gym
with charachange


emi "Eh bien eh bien, regardez qui arrive enfin !"


hi "Ouais, ouais."


hi "Profite de ta victoire tant que tu le peux."

show emi basic_closedgrin_gym
with charachange


"Emi sourit alors que l'infirmier lui tape gentiment le dessus de la tête."

show nurse neutral:
    center
    xpos 0.0 xanchor 0.5
    easein 0.5 xpos 0.1
with charaenter


nk "Ah, te voilà."


nk "Entre donc, Hisao."

play music music_nurse fadein 1.0

scene bg school_nurseoffice
show nurse neutral at center
with locationchange


"Dans ce qui est maintenant devenu une routine, il vérifie ma pression sanguine et mon rythme cardiaque."

show nurse fabulous
with charachange


nk "Un peu vite aujourd'hui, n'est-ce pas ?"


hi "Ouais, j'ai couru après Emi."

show nurse grin
with charachange


"L'infirmier rit."


nk "Ce n'est jamais une bonne idée."

show nurse neutral_close
with characlose


"Il se penche comme pour me chuchoter un secret."

show nurse fabulous_close
with characlose


nk "Je ne sais pas si tu as entendu... mais Emi est un peu une star de l'athlétisme."

show nurse fabulous
with vpunch


"Je prends du recul dans un effet de surprise moqueuse."


hi "Vraiment ? Elle ne m'en a jamais parlé !"

show nurse grin
with charachange


"Nous partageons un rire."

show nurse neutral
with charachange


nk "Elle s'en est bien sortie aujourd'hui ?"


nk "Le rhume n'a pas semblé la gêner ?"


hi "Pourquoi vous ne lui demandez pas directement ?"

show nurse concern
with charachange


"Il roule des yeux, semblant exaspéré."


nk "Bien sûr que je vais aussi lui demander à elle, mais elle me dira qu'il n'y a pas eu de problème, qu'il y en ait eu ou non."

show nurse fabulous
with charachange


nk "Alors je te demande à toi, parce que tu es son ami et que tu me le dirais sûrement si elle avait eu du mal aujourd'hui."


"Quand il le dit comme ça, c'est bien plus logique."


hi "Elle semblait bien aller aujourd'hui, si ce n'est un peu plus fatiguée qu'à la normale."


hi "Elle se sentait déjà mieux quand je suis passé hier, alors je ne suis pas surpris."

show nurse neutral
with charachange


"L'infirmier hoche la tête, bien que je remarque qu'il s'est légèrement tendu quand j'ai mentionné la visite de la veille."


nk "Bien, c'est une bonne chose."


nk "Je pensais aussi que ça n'allait durer qu'une journée. Emi a tendance à récupérer vite des rhumes et autres."


hi "Hé, en parlant d'Emi..."


hi "Est-ce qu'elle et le capitaine de l'équipe... ? Enfin, vous savez."

show nurse fabulous
with charachange


"Une expression suspicieuse s'affiche sur son visage."


nk "Pourquoi tu demandes ?"


hi "Ben, c'est juste qu'ils semblent proches et j'étais curieux, vous voyez ?"


hi "Et je ne lui demanderai jamais, ça serait assez embarrassant."


"Jusque-là, pas de problème. Maintenant il faut lui vendre."


hi "En plus, ils iraient bien ensemble."

show nurse grin
with charachange


"L'infirmier rit."


nk "Tu n'es pas le premier à dire ça."


nk "Mais je crois pouvoir dire avec certitude qu'ils ne seront jamais comme tu l'insinues."


hi "Avec certitude ?"

show nurse neutral
with charachange


nk "Ouaip."

show nurse fabulous
with charachange


nk "Pas que je puisse te le dire, bien sûr. Confidentialité et tout ça."


hi "Ouais bien sûr, vous ne dévoilez rien."

show nurse grin
with charachange


nk "Bien sûr."

show nurse neutral
with charachange


nk "Bon. Sors d'ici. Je suis un homme occupé, tu sais."

stop music fadeout 2.0

scene bg school_nursehall
show emi basic_grin_gym at center
with locationchange


"Je roule les yeux à sa dernière phrase et me dirige vers la porte, faisant signe à Emi d'y aller."

show emi basic_grin_gym:
    center
    easeout 0.5 xpos 0.4 alpha 0.0
with Pause(0.5)

hide emi
with None


"Durant tout ce temps, je me retiens de faire une danse de joie."

window hide

play music music_running


centered "Ils ne seront jamais comme tu l'insinues."

window show


"C'est précisément le type de choses que je voulais entendre."


"J'ai à moitié envie de tenter quelque chose tout de suite avec Emi, mais je crois que l'infirmier désapprouverait."


"En plus, je ne sais toujours pas exactement ce que Emi ressent pour moi."


"Je veux dire, c'est évident qu'elle tient à moi en tant qu'ami, mais quelque chose de plus que ça ? Je ne peux pas en être sûr."


"Pourtant, je ne peux pas m’empêcher d'avoir de l'espoir. J'ai juste besoin de trouver un bon moment pour dire à Emi ce que je ressens."


"Ce détail devrait au moins me tenir occupé pour le reste de la journée."

stop music fadeout 6.0


label fr_E15:

scene bg school_nursehall
with None

$ renpy.music.set_volume(0.5, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

scene bg school_roof
with shorttimeskip


"Le toit est complètement désert."


"Normalement je pourrais compter sur Rin pour être là avant moi, mais elle est étrangement absente."


"Je me demande si elle a décidé d'accompagner Emi à la cafétéria pour une fois. Ça me semble assez peu probable, mais c'est la seule théorie que j'ai."


"J'ai un peu envie d'aller chercher Emi, mais j'ai bien plus envie de rester comme ça, la peau au soleil."


"Je grignote mon repas en attendant qu'Emi et Rin arrivent."


"Il ne faut pas longtemps avant que j'entende les bruits de quelqu'un montant les escaliers."

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_door_creak


"J’attends que la porte commence à s'ouvrir pour parler."


hi "Qu'est-ce qui vous a pris aussi longtemps ?"


hi "Vous m'avez fait attendre."


hi "Vous êtes..."


hi "Hein ?"


"Ça c'est bizarre."

show emi basic_confused at center
with charaenter


"La seule personne se tenant là est Emi, qui semble vaguement confuse."


emi "Comment ça “hein” ?"

show emi basic_grin
with charachange


emi "C'est moi ! Tu sais, Emi ! On court ensemble le matin."


"Elle sourit, et mon cœur se soulève légèrement à ce moment."


hi "Oui, je le sais ça. Je suis juste confus..."


hi "...Où est Rin ?"

show emi sad_depressed
with charachange


"Le sourire d'Emi est remplacé par une expression coupable."


emi "Ouais, à ce propos..."


emi "Je lui ai... en quelque sorte..."

show emi sad_shy
with charachange


emi "Refilémonrhume."

play music music_another fadein 0.5
$ renpy.music.set_volume(1.0, 0.0, channel="sound")


hi "Oh mince."


hi "Il y a un risque que je l'aie aussi ?"


"Ça serait logique, après tout. Emi et moi étions collés l'un contre l'autre hier..."


"Alors qu'est-ce que Rin et elle ont fait pour qu'elle soit malade ?"

"…"


"Du calme mon vieux. Ne pars pas dans cette direction."


"Rin a probablement juste un plus mauvais système immunitaire que moi."

show emi basic_shock
with charachange


"Emi semble choquée par mon commentaire, comme si elle n'y avait pas pensé avant."


emi "J’espère pas !"

show emi excited_sad
with charachange


emi "Je me sentirais mal si tu étais malade à cause de moi, Hisao !"


hi "Oh non, je crois que je sens la fièvre qui monte..."

show emi sad_annoyed
with charachange


"Emi semble terrifiée, puis change rapidement d'expression pour une autre plus autoritaire."


emi "Hisao !"


emi "Tu arrêtes d’être malade tout de suite !"

show emi basic_annoyed
with charachange


emi "Je ne l'accepterai pas !"

show emi basic_annoyed_close
with vpunch


"Elle me saisit par le col juste après."


emi "Tu m'écoutes, système immunitaire de Hisao ?"

show emi sad_angry_close
with charachange


emi "Mets tes fesses en selle et travaille !"


"Je lui fais un salut militaire."


hi "Bien compris, madame."

show emi basic_grin
with charadistant


"Emi fait un pas en arrière et hoche la tête, satisfaite."

show emi basic_closedgrin
with charadistant


emi "Bien."

show emi basic_happy
with charadistant


emi "Et tu n'es pas autorisé à louper ne serait-ce qu'une de nos courses du matin, après tout."


hi "Mais tu as loupé une course toi !"

show emi sad_annoyed
with charachange


"Emi croise les bras et me regarde d'un air hautain."


emi "Oui, mais c'est un cas spécial. C'était moi, et pas toi."


hi "Ça n'explique rien du tout."

show emi basic_confused
with charachange


"Emi semble sidérée."



emi "Tu plaisantes, hein ?"

show emi basic_annoyed
with charachange


emi "Mon explication est parfaitement claire !"


hi "Non pas du tout ! C'est d'une mauvaise foi flagrante !"

show emi sad_annoyed
with charachange


emi "Je ne vois pas le rapport."


hi "Roh, laisse tomber."

show emi basic_closedgrin
with charachange


"Emi semble contente de sa victoire."


hi "Bref, ça va aller pour Rin ? Elle n'est pas très malade, hein ?"

show emi basic_grin
with charachange


"Emi secoue la tête."


emi "Nope ! Elle s'en sortira très bien."

show emi excited_proud
with charachange


emi "Je lui ai pris des médicaments qui devraient l'aider."

show emi basic_hes
with charachange


emi "Bien que j'aurais probablement dû m'assurer qu'elle n'essaye pas de tous les prendre en une seule fois..."

show emi basic_grin
with charachange


emi "Elle l'a déjà fait, tu sais."


"Je ne suis pas tellement surpris."


"Je doute que Rin soit du genre à faire attention aux dosages."


hi "Tu devrais sûrement aller la voir plus tard alors. Juste au cas où."

show emi sad_grin
with charachange


"Emi hausse les épaules."


emi "Je passerai la voir après l’entraînement. Elle ira bien d'ici là."


"Je hoche la tête, considérant la conversation terminée."


"Le seul problème est que je ne sais pas de quoi parler maintenant."


hi "Donc..."


hi "Tu as d'autres rencontres d’athlétisme de prévues ?"

window hide

nvl clear

nvl show dissolve


n "\n\n\n\n\n\n\n\nC'est une technique d'approche pour essayer de savoir si elle est libre ce week-end."


n "Si elle est libre, alors peut-être que je pourrai lui proposer un rendez-vous ou quelque chose du genre."


n "Bon, si j'arrive à formuler les mots du moins."

nvl clear

nvl hide dissolve

window show

show emi basic_grin
with charachange


"Emi secoue la tête."

show emi basic_closedgrin
with charachange


emi "Nan, pas pour les prochaines semaines, je crois. La saison se termine."


"Ah ouais. Je suis arrivé en plein milieu de tout ça, hein ?"


"Est-ce que ça veut dire que les examens arrivent bientôt ? Je devrais sûrement m'en préoccuper."


hi "Qu'est-ce que tu fais le week-end, s'il n'y a pas de rencontre ?"

show emi excited_proud
with charachange


"Un sourcil se lève, et Emi affiche son air taquin habituel."


emi "Tu es vraiment curieux aujourd'hui, hein ?"


"Je hausse les épaules et espère avoir l'air naturel."


hi "Je demande juste comme ça."


hi "Je ne sais pas ce que c'est d’être une star de l’athlétisme, après tout."

show emi basic_closedgrin
with charachange


emi "Pfff, flatterie."


"Elle me fait un signe de la main pour la repousser."

show emi basic_grin
with charachange


emi "Je ne suis pas si douée, tu sais."

show emi basic_closedhappy
with charachange


emi "Tu m'as vue lors d'un de mes bons jours, c'est tout."


hi "Menteuse va."

show emi sad_grin
with charachange

stop music fadeout 6.0


emi "Ha, ouais."


emi "Mais l’humilité est la caractéristique d'un bon athlète."

show emi sad_depressed
with charachange


emi "Du moins c'est ce que mon père disait."


"Elle hausse les épaules et essaye sans succès de cacher l'expression troublée qu'affiche son visage."


hi "Hé, qu'est-ce qu'il y a ? Tu sembles embêtée par quelque chose."


"Emi commence à le nier, puis soupire, abandonnant."


"Je me demande si elle est trop fatiguée, après avoir été malade, pour le nier comme d'habitude."


"Ou si maintenant elle me fait suffisamment confiance pour s'ouvrir."

show emi sad_shy
with charachange

play music music_comfort fadein 9.0


emi "Bon, tu te rappelles de la nuit dernière ?"


"Évidemment. Je hoche la tête pour confirmer."

show emi sad_depressed
with charachange


emi "Ce n'est pas la première fois que ça m'arrive."


emi "Pour dire vrai, ça arrive..."


"Elle s’arrête, comme si elle se rendait soudainement compte de la réalité."


"C'est presque comme si elle était en train de rompre une règle personnelle."


"Mais elle recommence à parler, choisissant ses mots avec attention."


emi "Enfin, pas souvent, mais..."

show emi sad_shy
with charachange


emi "De temps en temps."


emi "C'est juste une de ces semaines où ça arrive."

show emi sad_depressed
with charachange


"Un soupir lui échappe, et elle semble terriblement frustrée."

show emi sad_shy_close
with characlose


"Je m'approche d'elle et la serre dans mes bras, ce qui contrairement à la dernière fois ne semble pas la choquer."


"Au lieu de ça, elle semble se relaxer alors que mes bras passent autour d'elle."


"Nous restons comme ça un moment."


hi "Tu sais, j'étais sérieux hier soir."


hi "Tu peux vraiment me parler s'il y a des choses comme ça qui te perturbent. C'est toujours difficile de faire ce genre de choses seul, tu sais."

show emi sad_grin_close
with charachange


"Emi sourit et rompt le silence, mais reste posée sur mon épaule."


emi "Merci, Hisao."

show emi basic_grin_close
with charachange


emi "Ça ira, je crois."


"Je peux déjà la voir se remettre, se préparant à tout ravaler encore une fois."


"Je pense que le sujet est clos, maintenant."


hi "Donc, tu as repensé à ce plan de carrière ?"

show emi basic_closedgrin_close
with charachange


emi "Pas vraiment."

show emi basic_grin_close
with charachange


emi "Je n'ai pas l'intention de prévoir très loin, tu sais."


emi "Bien que j'imagine que je pourrais au moins commencer à regarder les facs, hein ?"


"Je hausse les épaules."


hi "J'imagine, sauf si tu étais sérieuse pour cette histoire de pirates."


hi "La dernière fois que j'ai vérifié, les pirates n'avaient pas tellement besoin d'aller à l'université."


hi "Sauf s'il y a, genre, une université de pirates quelque part."

show emi basic_closedgrin_close
with charachange


"Emi se met à rire et on dirait un peu la Emi normale, mais il y a un nouvel élément dans son expression."


"Espiègle. C'est comme ça que je la décrirais."


"Emi semble espiègle, à me regarder avec sa tête toujours posée sur mon épaule."

show emi sad_grin_close
with charachange


emi "Tu viendrais avec moi si je devenais une pirate ?"



hi "Bien sûr !"


hi "Qui passerait à côté de l'opportunité de devenir pirate avec toi ?"

show emi basic_grin_close
with charachange


emi "Bon, dit comme ça, c'est sûr."

show emi basic_closedgrin_close
with charachange


"Elle rit encore."


"Je remarque que mon cœur semble s’être accéléré. C'est probablement à cause de sa proximité."


"Ce soupçon de fraises, encore une fois."


"Je ne peux pas m’empêcher de sourire en la regardant."


"Elle est de nouveau contente."

show emi sad_shy_close
with charachange


emi "Dis, Hisao."


hi "Mmh ?"

show emi sad_grin_close
with charachange


emi "Si tu comptes m'embrasser, tu devrais le faire bientôt. Je crois que ça ne va pas tarder à sonner."

stop music fadeout 1.0


"Mes pensées s’arrêtent brusquement."


"Je suis presque sûr d’être bouche bée à cause du choc."


"Tout ce que j'arrive à sortir est un “Hein ?” étranglé."

show emi basic_closedgrin_close
with charachange


"Ce qui amuse Emi encore plus."

show emi excited_proud_close
with charachange


emi "Tu y pensais, non ?"


"Elle s'assoit, mettant son visage au niveau du mien."

show emi basic_grin_close
with charachange


emi "J’apprécierais sûrement ça aussi, tu sais ?"

show emi sad_grin_close
with charachange


emi "Tu es vraiment..."

show emi sad_shy_close
with charachange


emi "...Bref."


"Elle se ressaisit brièvement, ayant l'air d'être sur le point de dire quelque chose d'important."

show emi sad_grin_close
with charachange


emi "Si tu ne t'en es pas encore rendu compte, je crois que je suis quelque peu tombée amoureuse de toi."

show emi basic_grin_close
with charachange


emi "Tu vas devoir prendre tes responsabilités."


"Cette fois son sourire interrompt ma capacité à penser."


"À un moment je me tourne vers elle, et à un autre moment ses bras sont passés autour de mon cou."


"À un autre encore, mes bras sont passés autour de sa taille."


"Je suis incapable de dire précisément quand c'est arrivé."


"Parce qu'à ce moment, il n'y a qu'une voix dans ma tête qui me crie de l'embrasser."


"Je regarde Emi dans les yeux."


"La voilà."


"Cette chose que j'ai vue hier dans le lit. C'est encore là."


"Je me rends soudainement compte qu'elle est inquiète que je puisse la rejeter."

stop ambient fadeout 1.5


"Une inquiétude qui n'a aucune raison d’être."

window hide

play music music_romance fadein 0.5

scene white
show ev emi_firstkiss:
    truecenter
    zoom 4.0 rotate 20 subpixel True
    0.7
    linear 0.3 zoom 1.1 rotate 0
    easein 12.0 zoom 1.0
with GenericWhiteout(0.5, 0.2, 2.0)

with Pause (5.0)

nvl clear
nvl show dissolve


n "\n\n\n\nSes lèvres ont un léger goût de fraises."


n "Elle se laisse aller dans le baiser, et ses bras se resserrent derrière ma tête, s’assurant que je ne me détache pas d'elle."


n "Non pas que ce soit une possibilité."


n "J'ai l'impression que mon estomac se dénoue."


n "Le monde s'évanouit."


n "Il y a juste moi, et elle, et ce banc."


n "Mes bras se resserrent, la serrant plus fort contre moi, appréciant de la sentir."


n "Je respire son odeur, mon esprit essayant désespérément de mémoriser le goût qu'elle a, ce qu'elle sent, ce que c'est de la sentir contre moi."

play sound sfx_warningbell
play ambient sfx_rooftop fadein 4.0

nvl clear

nvl hide dissolve

scene bg school_roof
show bg school_roof_blurred as overlay:
    center
    linear 6.0 alpha 0.0
show emi sad_shyblush_close
with silentflash

window show


"La sonnerie de l'école nous renvoie tous les deux à la réalité, et nous rompons notre baiser."


"Les joues d'Emi sont légèrement rougies, et elle semble reprendre son souffle. Pour sa défense, moi aussi."


"Nous restons là quelques instants, essayant de réaliser ce que nous venons de faire."


"Emi est la première à rompre le silence."

show emi sad_grin_close
hide overlay
with charachange


emi "Alors..."

show emi basic_closedgrin_close
with charachange


emi "... Tu as envie qu'on aille dîner après que j'aie fini l’entraînement ?"


hi "Quelle coïncidence."


hi "J'étais sur le point de te demander la même chose."


"Enfin, en réalité ça aurait été une vraie demande de rendez-vous durant le week-end ou autre. Mais la pensée était là. Je crois."

with vpunch


"Emi me donne une tape joueuse."

show emi basic_happy_close
with charachange


emi "Ouais bien sûr."

show emi basic_closedhappy_close
with charachange


emi "Tu étais toujours en état de choc après t’être rendu compte à quel point je suis douée pour embrasser."


"Nous commençons à redescendre les escaliers en direction de nos classes respectives."

stop ambient fadeout 2.0

scene bg school_hallway3
show emi sad_grin at center
with locationskip


hi "Hé, je ne t’ai pas vue parler juste après non plus."

show emi basic_closedgrin
with charachange


emi "C'est parce que je n'ai rien dit."

show emi basic_closedhappy
with charachange


emi "Je te vois après l’entraînement, Hisao."

show emi basic_closedgrin_close
with charachange

show emi basic_closedgrin_close:
    center
    easeout 0.5 xpos 0.6 alpha 0.0
with None


"Elle se rapproche et m'embrasse brièvement au milieu du couloir, éteignant encore une fois le peu de cerveau qui m'était revenu."

scene bg school_scienceroom
with locationchange


"Alors que je rentre dans ma classe, une Misha rieuse m'accueille."

show misha hips_grin at center
with charaenter


mi "Hicchan, espèce de grand romantique~ !"


mi "Tu t'es déclaré sur le toit ? Hein~ ?"


hi "Euh, en fait c'était elle."

show misha cross_laugh
with charachange


"Ce qui fait éclater Misha de rire."

show misha hips_grin
with charachange


mi "L'amour est imprévisible, hein~ ?"


"Vu que c'est Misha, j'imagine que j'aurais pu m'attendre à ce qu'elle me taquine là-dessus."


hi "J'imagine..."

show misha hips_grin:
    center
    easeout 0.5 xpos 0.4 alpha 0.0
with None


"Avant que je puisse répondre, Mutou entre dans la pièce et Misha retourne à son siège, riant encore un moment."


"Je pense que j'aurai encore ce genre de conversation, surtout après qu'Emi m'ait embrassé en plein milieu du couloir."


"Mais d'un côté, je m'en moque bien."

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 5.0


"Pour la première fois depuis que je suis arrivé ici, mon cœur me semble léger."

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
