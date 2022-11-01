label fr_E16:

window hide None

scene bg school_scienceroom
with fade

nvl clear
nvl show dissolve

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_normal fadein 3.0


n "\n\n\nMon esprit est ailleurs durant tout le cours de Mutou."


n "Je vais dîner."


n "Avec Emi."


n "Qui veut être ma petite copine, rien que ça."


n "Un rendez-vous..."


n "Et puis elle m'a embrassé."


n "Ce baiser. Je n'arrête pas d'y revenir, le repasser dans ma tête encore et encore."


n "Tout, durant ce moment, semblait s'accorder."


n "\nMon esprit divague, perdu en pensant à Emi."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear
nvl hide dissolve
window show

show muto normal
with charaenter


mu "Nakai ? Allô ?"


"On dirait que j'ai un peu trop dérivé."


hi "Hein ? Quoi ?"

show muto irritated
with charachange


mu "Diantre ! Tu as contracté une sorte d’amnésie !"


mu "Que quelqu'un aille chercher l'infirmier !"


"La classe rit doucement à la bouffonnerie de Mutou."


hi "Désolé, monsieur."

show muto normal
with charachange


mu "Mmh, ça n'arrivera plus et tout ça, hein ?"


hi "Exactement."


"Mutou s'illumine."

show muto smile
with charachange


mu "Bien ! Tant mieux !"


mu "Je détesterais que mon étudiant star se relâche, après tout."

hide muto
with charaexit


"Je m'en sors bien, mais je ne me qualifierais pas d'étudiant star, je crois."


"Je suis sûr que c'est un cours dans lequel tout le monde s'en sort. Il suffit juste de mémoriser des formules."


"Fidèle à mes paroles, je réussis à rester concentré pendant le reste du cours."

stop music fadeout 2.0

show muto normal
with shorttimeskip

play sound sfx_normalbell


mu "Nakai, je pourrais te parler une minute ?"


"Je me demande si je vais avoir des problèmes à cause de tout à l'heure."


hi "Euh, bien sûr."


hi "Je vais avoir des problèmes ?"

show muto irritated
with charachange


"Mutou semble confus pendant un moment."


mu "Je te demande pardon ?"


"Il penche la tête d'un côté et réfléchit un moment."

show muto smile
with charachange


mu "Oh, ça ! Non, non, tu n'auras pas de problèmes."


mu "Je veux juste te poser une question."


hi "Quelle question ?"

show muto normal
with charachange


mu "Rien de terrible, je me demandais juste ce que tu avais prévu après le diplôme."

play music music_another fadein 2.0


mu "Tu comptes aller à l'université ?"


hi "Ouais je pense. Je ne vois pas grand-chose d'autre à faire."


mu "Tu as pensé à ce que tu allais étudier ?"


hi "Pas vraiment, non. Je penserai à quelque chose quand j'y serai."

show muto smile
with charachange


"Mutou se met à rire."


mu "Tu prends les choses comme elles viennent, hein ?"


mu "Je te dirais bien que c'est une mauvaise chose, mais j'ai fait pareil quand je suis allé à l'université."


mu "Enfin, pas vraiment."


mu "Je savais que je ferais sciences, mais je n'étais pas sûr de laquelle."


mu "J'ai fini avec la physique, mais ça aurait tout aussi bien pu être l'astronomie ou quelque chose d'autre."

show muto irritated
with charachange


mu "En fait, j'étais parti pour la chimie en premier, mais il y avait tout un tas de choses..."


"Mutou dévie de son sujet et fronce légèrement les sourcils."


"Il lui faut une minute pour revenir de ses pensées, et j’attends patiemment qu'il continue."

show muto normal
with charachange


mu "Bon dans tous les cas, j'ai fait beaucoup de physique aussi, parce que ça m’intéressait, mais je n'étais pas sûr que c'était pour moi."

show muto smile
with charachange


mu "Alors je suis retourné à la chimie, et me voilà. Tu vois ?"

show muto smile
with charachange


"Il me sourit avec enthousiasme, comme s'il voulait que je confirme que oui, nous y voilà."


"J'ai l'impression que Mutou a un plan pour cette conversation, mais je ne sais pas lequel."


hi "Je suis désolé, je ne vous suis pas."


"Mutou fronce les sourcils et se frotte la nuque, semblant perplexe. Et là il claque des doigts comme s'il venait de se rappeler du sujet de la conversation."


mu "C'est vrai ! Oui ! Toi !"


hi "Moi ?"


mu "Oui ! Tu devrais étudier les sciences !"


mu "Tu es fantastique pour ça."


mu "Sauf si tu préfères faire des maths."

show muto irritated
with charachange


"Mutou affiche une expression sombre."


mu "Je suis pas un grand fan des maths. J'ai toujours préféré les expériences plutôt que les preuves."


hi "Vous dites que je devrais étudier la science à l'université ?"


"Mutou semble perturbé par ma question."

show muto normal
with charachange


mu "Euh, en quelque sorte."

show muto smile
with charachange


mu "Tu pourrais aussi rejoindre le club de sciences !"


mu "Le problème est qu'il n'y a pas de club de sciences."


mu "Mais il pourrait y en avoir un !"


mu "Tu pourrais même être un membre privilégié !"


mu "Un père fondateur !"


mu "Bien sûr, tu aurais besoin de trouver d'autres membres."

show muto normal
with charachange


mu "Enfin, seulement si tu voulais."


mu "On pourrait commencer juste à deux."


mu "Et hum."

show muto smile
with charachange


mu "Je pourrais te donner des choses à lire, et on pourrait en parler."


mu "Hum, et je pourrais t'aider à te préparer pour l'université et tout le reste aussi."

show muto irritated
with charachange


mu "Attends !"


"Mutou fouille dans sa serviette et en sort un livre."

show muto smile
with charachange


mu "Lis ça."


mu "Si c'est intéressant, alors on pourra en parler."


"“Une Brève Histoire dans le Temps ?”"


"Je ne sais pas si j'ai vraiment envie de le lire, mais Mutou semble assez excité à cette idée."


hi "De quoi ça parle ?"

show muto normal
with charachange


mu "Temps. Espace. Espace-temps. Trous noirs et tout ça."


mu "Ce n'est pas si lourd. Juste pour voir si ce genre de choses t’intéressent, tu comprends."


mu "Après les cours, on pourrait en discuter, ou je pourrais te montrer comment faire des explosifs dans le labo."

show muto smile
with charachange


"Il fait un signe de la main en réponse à mon expression confuse."


mu "Je plaisante, désolé."


mu "Bon, je t'ai retenu assez longtemps."


mu "Pense à la science comme carrière, Nakai. Je crois que tu apprécieras."


hi "Euh, d'accord, je le ferai. Merci pour le livre."

stop music fadeout 14.0

scene bg school_hallway3
with locationchange


"Je sors de la classe et regarde l'horloge ; il reste entre beaucoup de temps à tuer jusqu’à la fin de l’entraînement d'Emi."


"Je pense jeter un œil au livre ; je devrais probablement me doucher aussi."


"Se doucher avant un rendez-vous est ce qu'il faut faire, hein ?"


"Je retourne aux dortoirs."

scene bg school_dormhisao
with locationskip


"Je me demande où je suis censé rejoindre Emi."


"Elle a dit “après l’entraînement”, mais elle ne m'a pas dit où je devais la retrouver."


"Je peux juste passer par la piste j'imagine ; c'est probablement le mieux que je puisse faire."


"Si elle a besoin d'une douche, je pourrai aussi attendre dans sa chambre ou un truc du genre."


"Ou dans le couloir, c'est encore mieux."


"Je prends une douche rapide, me rappelant de prendre mes médicaments dès que je sors."


"Maintenant, jetons un œil à ce livre."

stop music

scene black
with dissolve


label fr_E17:

scene black
with None

scene bg school_dormhisao
with vpunch


"Je me réveille en sursaut."


"Merde ! Il est quelle heure ?"


"Un regard à l'horloge me révèle que je suis endormi depuis près d'une heure."


hi "Dieu merci."


"L’entraînement d'Emi devrait bientôt finir."


"Je mets des vêtements au hasard et me dirige vers la piste."

scene bg school_track
with locationskip


"D'une certaine façon, j'ai l'impression qu'on ne fera rien de spécial pour le dîner."


"Emi ne me semble pas du genre à faire les choses de manière très raffinée."


"Mais je sais que j'ai encore beaucoup à apprendre sur Emi."


"Malgré le fait que nous soyons maintenant plus proches, j'ai toujours l'impression de ne pas la connaître aussi bien que je le devrais."


"Bah, j'ai bien le temps d'arranger ça."


"Pour être honnête, j'ai hâte de mieux la connaître."


"Je suis tellement absorbé dans mes pensées que je ne me rends presque pas compte que je suis déjà arrivé à la piste."


"Emi est introuvable."


"Je ne vois même aucun signe du club d’athlétisme."


"Ça peut être gênant."


"Je me tourne en direction du dortoir des filles quand j’entends un cri."


emi "Hé, Hisao !"

play music music_emi fadein 1.0

show emicas smile at center
with charaenter


"Je me tourne et vois Emi tracer une ligne droite jusqu'à moi avec un sac de gym sur l'épaule."


"Elle s'est changée avec des vêtements plus citadins et décontractés, un short et un haut vert olive."


"Ses lames de courses ont été remplacées par des jambes plus réalistes qui ne tromperaient sûrement personne."


"Emi ne semble pas s'en préoccuper, ce qui me fait sourire."

show emicas happy
with charachange


emi "Hé, tu es venu !"

show emicas closedsmile
with charachange


emi "Je veux dire, je savais que tu viendrais, mais voilà..."

show emicas closedsmile_up_close
with characlose


"Je me retrouve soudainement enveloppé dans une étreinte affectueuse, et je me retrouve dans l'incapacité de masquer ce qui doit être sur mon visage le plus grand sourire du monde."


hi "Bah, bien sûr que je suis venu !"


hi "J'aurais été fou de ne pas venir, hein ?"


"Emi réfléchit un moment."

show emicas grin_up_close
with charachange


emi "C'est vrai."

show emicas wink_up_close
with charachange


emi "Je veux dire, je suis géniale, après tout."


"Je hausse les épaules en réponse."


hi "Je le crois, moi, en tout cas."

show emicas blush_up_close
with charachange


"C'est une remarque banale, c'est pourquoi je suis surpris de voir que ça semble avoir pris Emi par surprise."

show emicas smile_up_close
with charachange


"Elle rougit et me sourit chaleureusement avant de poser un baiser sur mes lèvres."


"Maintenant c'est à mon tour d’être surpris."

show emicas grin
with charadistant


"Emi fait un pas en arrière, se posant sur ses talons, semblant contente d’elle-même."


"Mon esprit patauge pour trouver une réponse appropriée."

hi "…"


hi "Je devrais te complimenter plus souvent."

show emicas happy_up
with vpunch


"Emi rit et me donne une frappe joueuse sur l'épaule."

show emicas closedsmile
with charachange


emi "Idiot."

show emicas weaksmile_up_close
with characlose


"Je passe un bras autour des épaules d'Emi et suis content quand elle se colle immédiatement contre moi comme si c'était la chose la plus naturelle du monde."


hi "Alors, où ça ?"

show emicas awayfrown_up_close
with charachange


emi "Je ne sais pas trop."

show emicas neutral_up_close
with charachange


emi "Où est-ce que les gens vont en rendez-vous par ici, de toute façon ?"


"C'est une sacrée bonne question."



hi "Aucune idée."


hi "Pourquoi ne pas juste aller à l'Aura-Mart et prendre quelque chose de tout prêt ?"



"Le visage d'Emi s'illumine quand je dis ça."

show emicas happy_up_close
with charachange


emi "Un pique-nique !"

show emicas wink_up_close
with charachange


emi "Je crois que tu tiens quelque chose, Hisao."

scene bg school_gate
with locationskip


"Emi passe son bras autour de ma taille et nous commençons à nous diriger vers le portail principal."


"Je suis totalement ignorant de ce que je suis censé faire dans cette situation, mais au moins Emi semble être dans le même cas."

scene bg suburb_roadcenter
with locationskip


"Bien que ce soit très agréable d’être avec Emi, je ne peux pas m’empêcher de me sentir un peu tendu."


"Et si je fais mal quelque chose ?"


"Je détesterais me ridiculiser devant elle."

scene bg suburb_konbiniext
with locationchange


"La marche jusqu’à l'Aura-Mart est accompagnée des commentaires d'Emi sur le déroulement de l’entraînement."


"Je reste silencieux sur presque tout le trajet, appréciant juste d’être près d'Emi."


"On attire quelques regards en chemin, mais je m'en moque."


"Nous achetons quelques petits sandwichs et des nouilles instantanées, nous rendant compte trop tard qu'on ne pourra pas les cuisiner dans le parc."

show emicas weaksmile
with charaenter


emi "Pas grave, je les ferai pour déjeuner une autre fois."


hi "Ça me va."

stop music fadeout 2.0
$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_parkambience fadein 2.0

scene bg suburb_park
with locationskip


"Nous arrivons au parc après nous être légèrement égarés, chose dont je tiens Emi entièrement responsable."


"Elle, bien sûr, me blâme moi."

show emicas smile:
    center
    easein 1.0 ypos 1.13
with charaenter


"Nous trouvons un emplacement en dessous d'un arbre et nous asseyons. Je m'adosse contre le tronc et Emi se met en face de moi."

play music music_ease fadein 3.0


hi "On aurait dû amener une couverture ou un autre du genre pour s'asseoir, non ?"

show emicas smile_up:
    ypos 1.13
with Dissolve(0.2)

show emicas smile
with charachange


"Emi hausse les épaules."

show emicas closedsmile
with charachange


emi "Ça ne me gêne pas comme ça."


hi "Moi non plus."

show emicas grin_up
with charachange


"Emi me donne un petit sandwich et nous commençons à manger."


"Sandwich au curry. Intéressant."


"Apparemment je n'ai pas fait très attention quand j'ai acheté les sandwichs."

show emicas wink_up
with charachange


emi "Hé, Hisao. On dirait que le tien est un peu épicé."


"Je secoue la tête, essayant en vain de garder une image de virilité."


hi "Nan, vraiment pas."

show emicas closedsmile_up
with charachange


emi "Je vois, je vois. Ça doit être pour ça que ton visage est devenu aussi rouge."


hi "Oui, exactement. Le manque d’épice m'a euh... fait monter le sang aux joues."


hi "À cause de la déception."

show emicas happy
with charachange


"Emi rit et avale le dernier morceau de son sandwich."

show emicas wink
with charachange


emi "Bon, si tu ne supportes pas, je serais heureuse de t'en débarrasser."


hi "Hé, ce n'est pas parce que tu as englouti le tien très rapidement que ça signifie que je vais te donner le mien."

show emicas pout
with charachange


"Emi fait la moue, et sa voix me fait presque m'étouffer de rire avec mon sandwich."


emi "Aw, allez Hisao !"

show emicas awayfrown
with charachange


emi "Tu n'es pas censé t’inquiéter du fait que je n'aie plus faim ?"


emi "On est en rendez-vous, tu sais !"

show emicas pout
with charachange


emi "Bien que..."


"Emi semble troublée d'un coup."

show emicas frown_up
with charachange


emi "Je ne peux pas dire que je sens une différence."


hi "Mmh ? Comment ça ?"

show emicas awayfrown
with charachange


emi "Qu'est-ce qui fait que c'est un rendez-vous ?"


emi "C'est juste qu'on aurait fait pareil de toute façon."


emi "Mais ça devrait me paraître différent parce qu'avant on déjeunait en tant qu'amis, et maintenant on est à un niveau au-delà d'amis."


hi "On dirait Rin quand tu parles comme ça."

show emicas happy
with charachange


"Un rire s'échappe et Emi sourit."

show emicas closedsmile_up
with charachange


emi "Bon, il est possible qu'elle m'ait mis ça en tête."

show emicas closedsmile
with charachange


emi "On a déjà discuté de ce genre de choses auparavant."


hi "Vraiment ? De moi ?"

show emicas grin
with charachange


emi "Pas vraiment. Juste... de trucs."

show emicas neutral
with charachange


emi "Rin pense que le changement d'“amie” à “petite amie” est arbitraire la plupart du temps."


emi "Comme s'il n'y avait pas de différence entre les deux."


hi "Je peux te trouver une différence moi, tu sais."


hi "Tu n'as pas tendance à embrasser tes amis aussi souvent."

show emicas blush
with charachange


"Pour la seconde fois de la journée, Emi rougit légèrement et rit."

show emicas closedsmile
with charachange


emi "Tu dois avoir raison."


hi "Exactement. J'ai toujours raison pour les trucs comme ça."

show emicas weaksmile_up
with charachange


"Emi roule des yeux et rit un peu."


emi "Alors tu es pas mal intelligent, hein ?"


"Je hoche la tête en approbation."


hi "Ouaip."


hi "Même Mutou le pense. Il dit que je devrais faire des études de sciences après le diplôme."

show emicas neutral
with charachange


"Emi lève un sourcil."


emi "Oh vraiment ?"


hi "Ouais, je crois que je vais peut-être bien faire ça."


"Plus j'y pense, et plus l'idée me plaît."


"Je fais une note mentale pour examiner ça plus en profondeur une autre fois."


hi "Qu'est-ce que tu comptes faire, toi, après les examens ?"


hi "Tu comptes toujours courir ?"

show emicas awayfrown
with charachange


"Emi hausse les épaules, semblant presque un peu hésitante."

show emicas frown
with charachange


emi "Je ne sais pas. Si je suis suffisamment douée et que je peux trouver une équipe, pourquoi pas ?"


hi "Tu veux dire que tu n'es pas sûre ?"

show emicas neutral
with charachange


emi "Je n'y ai... pas vraiment pensé, pour être honnête."


hi "Vraiment ?"


hi "Tu devrais probablement, tu sais. La fin d'année n'est pas dans si longtemps."

show emicas awayfrown
with charachange


"Emi gigote un peu, nerveuse."


emi "Ouais, enfin... dans suffisamment longtemps, hein ?"

show emicas neutral
with charachange


emi "En plus, j'ai d'autres choses auxquelles penser."

show emicas grin_up_close
with vpunch


"Il y a un flash malicieux dans les yeux d'Emi et je me trouve soudainement poussé contre l'arbre."

show emicas smile_up_close
with charachange


emi "Comme m'assurer que c'est un vrai rendez-vous, hein ?"

show emicas closedsmile_up_close
with charachange


emi "Je veux dire, si on ne s'embrasse pas, ce n'est pas vraiment un rendez-vous, hein ?"


hi "J'imagine, o— mmmph." with vpunch


"Fraises et curry. Pas la meilleure combinaison, mais ça ne me gêne pas."

show emicas grin
with charadistant


"Emi s'assoit sur mes jambes et sourit encore une fois."


emi "Voilà. La science approuverait, hein ?"


"J'ai l'image très étrange de Mutou hochant la tête d'un air sérieux et cochant une case sur une liste."


"Je ne peux pas m’empêcher de rire à l'idée."

show emicas neutral
with charachange


emi "Je dois l'avouer, c'est la première fois que je vois un baiser suivi d'un rire comme ça."


emi "Je devrais me sentir vexée ?"


hi "Hein, non, non."


hi "Je suis sûr que la science approuverait."

show emicas happy_up
with charachange


"Emi rayonne, et je me retrouve à avoir de plus en plus de mal à garder mon cerveau en état de marche."


emi "Tant mieux !"


"C'est à ce moment que je remarque qu'Emi a volé le restant de mon sandwich au curry pendant que j'étais occupé par des images de professeurs jonglant avec des presse-papiers."


hi "Hé !"

show emicas blush
with charachange


"Emi essaye d'avoir l'air innocente, mais étant donné qu'elle vient de mettre les derniers morceaux dans sa bouche, ça ne semble pas très bien marcher."


emi "Mmph ? Défolée, pas pu réfifter."


hi "Voleuse !"

show emicas neutral
with charachange


"Un haussement d'épaules de sa part est tout ce que j'ai en réponse."


hi "Tu as utilisé tes ruses féminines sur moi !"


"Je n'avais pas si faim de toute façon, mais je ressens quand même le besoin de dire ce que je pense."

show emicas pout
with charachange


"Emi semble troublée par l'expression “ruses féminines”, mais la compréhension fait son chemin après un moment de réflexion."

show emicas angry_up
with charachange


emi "Ce n'était rien de la sorte !"

show emicas frown_up
with charachange


emi "Tu étais en train de rire ! Les ruses féminines n'ont rien à voir avec le rire !"


"Je ne peux rien dire contre ça."


hi "Ça ne change pas ton méfait."

show emicas happy
with charachange


"Emi rit à mon ton indigné et me donne une poussée joueuse."

show emicas closedsmile
with charachange


emi "D'accord, tu peux avoir les nouilles instantanées."


hi "Tu plaisantes ? C'est horrible ce truc !"


hi "Ça serait plus une punition qu'autre chose de manger ça !"

show emicas wink
with charachange


"Un autre rire de la part de la fille assise sur mes jambes."


"...Qui sont d'ailleurs totalement engourdies maintenant."


show expression im.Composite((295,1200), (0,0), "sprites/emicas/emicas_wink.png") as emicas:
    xalign 0.5 yanchor 0.5 ypos 1.13 subpixel True
    easeout 0.8 rotate -90
with None

show expression im.Composite((295,1200), (0,0), "sprites/emicas/emicas_blush.png") as emicas:
    xalign 0.5 yanchor 0.5 ypos 1.13 subpixel True
    easeout 0.8 rotate -90

with Dissolve(0.2)
with Pause(0.6)

hide emicas
with vpunch


"Je bouge une jambe pour essayer de la dégourdir, ce qui a l'effet inattendu de déséquilibrer Emi, qui tombe sur le côté avec un “Eep !” de surprise."


hi "Oups ! Désolé."


hi "Mes jambes se sont engourdies."


"Emi reste sur le sol, riant."


"Je me lève un peu difficilement, sentant les nerfs de mes jambes revenir à la normale."


"Mes yeux balayent les environs avant de s’arrêter sur Emi, qui ne s'est pas encore levée."

scene ev emi_parkback:
    xalign 0.5 yalign 0.5 zoom 1.1 subpixel True
    ease 10.0 zoom 1.0
with locationchange


"Ses cheveux sont en bataille, ses bras sont écartés et son rire sort gaiement de sa bouche."


"Tout ce qu'il y a à savoir sur Emi semble condensé à cet instant."


"Son énergie, son esprit, son rire enfantin."


"L'envie de m'allonger dans l'herbe avec elle me titille de plus en plus, et j'en viens à être convaincu que je n'aimerais rien de plus que de faire ça."


"Malheureusement le soleil s'est couché, et il est probablement temps pour nous de retourner aux dortoirs."


"Bien qu'Emi serait sûrement contente à l'idée de rester là toute la nuit, je ne crois pas que j'ai cette possibilité."


"En plus j'ai des devoirs à faire."


"Ça ne serait pas logique de commencer à négliger mon travail quand je commence à m’intéresser à l'université et tout, hein ?"


"Je tends une main à Emi pour l'aider à se lever."


hi "On devrait probablement y aller."

show ev emi_parkback_frown
with charachange


"Emi fait une grimace."


emi "T'as raison."

scene bg suburb_park
with locationchange

show emicas weaksmile_close:
    center
    ypos 1.2
    easein 0.5 ypos 1.0
with charaenter


"Elle attrape la main que je lui tends, et je la relève et la serre dans mes bras."


"Cette fois je suis celui qui l'embrasse, incapable de résister en ayant Emi contre moi."


hi "Dommage de devoir partir, hein."

show emicas closedsmile_close
with charachange


emi "Ouais, c'est sûr."

show emicas grin_up_close
with charachange


emi "Mais si on ne retourne pas bientôt à l'école, on va avoir des problèmes."


"Emi me donne une tape dans les côtes d'un air joueur."

show emicas wink_up_close
with charachange


emi "Et tu dois faire tes devoirs, je suis sûre."


hi "Malheureusement, tu as absolument raison."

hide emicas
with charaexit


"Je passe mon bras autour de ses épaules et nous faisons le chemin jusqu’à l'école, accompagnés par des rires occasionnels alors que nous discutons de choses et d'autres."


"Nous discutons d’athlétisme, de l'école, et même de l'odeur d'un des travailleurs de la cafétéria."

stop ambient fadeout 2.0

scene bg school_dormext_full
with locationskip


"Et bien trop tôt, nous nous retrouvons devant le bâtiment du dortoir des filles."

show emicas closedsmile at center
with charaenter


emi "Bon, je pense que je vais y aller."


hi "Il faut bien, hein ?"

show emicas grin_up
with charachange


"Emi sourit de son air espiègle habituel."


emi "Tu vas réussir à survivre sans moi ?"


"Je ris."


hi "Je suis sûr que je m'en sortirai."

show emicas pout_up
with charachange


emi "Tu es horrible ! Tu n'es pas censé dire quelque chose comme “Je vais compter les secondes sans toi” ?"


hi "Nan, je ne crois pas."

show emicas closedsmile_close
with characlose

show emicas weaksmile
with charadistant


"Emi s'approche et me fait un rapide baiser d'au revoir et recule, semblant étrangement timide."


emi "Merci pour le dîner."


emi "Je me suis bien amusée."

show emicas closedsmile
with charadistant


emi "Vraiment beaucoup."


hi "Pareil pour moi."


hi "Alors on refera ça de temps en temps."

show emicas happy
with charadistant


"Emi rit à ma réponse et hoche la tête."


emi "Je te vois demain matin, frais et en forme, hein ?"

show emicas wink
with charadistant


emi "Il faut courir pour éliminer ce sandwich, après tout."


hi "Bien sûr. Malgré le fait que tu en aies mangé la plus grande partie."

show emicas smile_up
with charadistant


emi "Oui, malgré ça."

show emicas grin_up
with charadistant


emi "À plus tard, Hisao !"

stop music fadeout 3.0

show emicas invis:
    xpos 0.6
with dissolvecharamove

hide emicas
with None


"Alors qu'Emi se tourne pour se diriger à l'intérieur, je remarque quelque chose d'étrange."


"Quelque chose de si étrange que je suis surpris de ne pas l'avoir remarqué plus tôt."


"Elle boite légèrement, favorisant la jambe gauche."

play music music_pearly fadein 8.0


hi "Hé, Emi !"

show emicas invis at tworight
with None

show bg school_dormext_full at bgleft
show emicas neutral at center
with dissolvecharamove


emi "Mmh ?"


hi "Elle va bien ta jambe ?"

show emicas awayfrown
with charachange


"Emi semble confuse, ou du moins fait semblant."

show emicas frown
with charachange


emi "De quoi tu parles ?"


hi "Ta jambe droite. Tu boites."

show emicas blush
with charachange

show emicas frown
with charachange


"Il y a un très bref instant d’inquiétude sur le visage d'Emi."


"Soit elle ne voulait pas que je le sache, ou elle ne pensait pas que je le remarquerais - ou, je préfère penser ça, elle ne l'avait pas remarqué elle-même."

show emicas neutral_up
with charachange


emi "Oh, ça."


"Elle hausse les épaules comme si ce n'était rien."

show emicas awayfrown
with charachange


emi "J'ai dû me la déplacer un peu durant le pique-nique."

show emicas wink
with charachange


emi "Aucune idée de ce qui aurait pu causer ça, bien sûr."


"Je repense à ce qui est arrivé sous l'arbre."


hi "Ah."


hi "Tu aurais dû me le dire ! On aurait pu arrêter et la réparer, tu sais."


"Emi fait un signe de la main."

show emicas smile_up
with charachange


emi "Nan, c'est pas bien important."

show emicas weaksmile_up
with charachange


emi "Ne t'en inquiète pas, d'accord Hisao ?"

show emicas closedsmile_up
with charachange


emi "Je vais bien."





label fr_choiceE17:
menu:
    with menueffect
    "Pourquoi est-ce que j'ai le sentiment qu'elle se convainc autant elle que moi-même ?"
    "Insister.":




        return m1
    "En rester là.":


        return m2


label fr_E17a:



hi "Tu es vraiment sûre ?"


hi "Tu ne veux pas l'ajuster avant de monter les escaliers ?"


hi "Tu pourrais te faire mal sinon, hein ?"

show emicas awayfrown_up
with charachange


emi "J'ai dit que j'allais bien, Hisao."

show emicas frown
with charachange


emi "Sérieusement, ne t’inquiète pas pour ça."

show emicas weaksmile
with charachange


emi "J'ai de l'expérience dans ce domaine, après tout."


hi "Ouais, c'est vrai."


"Emi sourit d'un air rassurant."

show emicas grin
with charachange


emi "Honnêtement, Hisao, j'apprécie que tu t’inquiètes mais je vais vraiment bien."

label fr_E17b:



"Bah, elle ira bien."


"Je pense qu'elle dirait quelque chose si elle avait vraiment un problème."


"En plus je suis sûr qu'elle s’énerverait si je continuais de revenir sur le sujet."

label fr_E17x:

show emicas smile
with charachange


emi "Il faut vraiment que j'y aille."

show emicas wink_up
with charachange


emi "Tes tentatives pour me garder avec toi sont vouées à l’échec !"


hi "Hah. Bien sûr."


hi "Je prolonge juste les au revoir."


"Un autre sourire illumine le visage d'Emi."

show emicas happy_up
with charachange


emi "Bonne nuit, Hisao."


hi "Bonne nuit."

hide emicas
with charaexit

stop music fadeout 5.0


"Alors qu'elle boite pour rentrer, je me retrouve à espérer qu'elle aille bien malgré le fait qu'elle m'a assuré qu'elle allait bien."


"Je crois que je peux considérer ce premier rendez-vous comme un succès."


"Bah, de toute, n'importe quel jour se finissant avec Emi qui me plaque contre un arbre pour m'embrasser ne peut pas être mauvais, hein ?"


"Je retourne à ma chambre, remerciant mentalement les dieux que Kenji ne me tende pas une embuscade dans les couloirs, et commence à faire mes devoirs."

scene black
with dissolve




label fr_E18:

scene bg school_dormhisao
with locationchange

play music music_night fadein 5.0


"Le matin est bien trop tôt à mon goût."


"Ça n'aide pas que j'aie eu du mal à dormir la nuit dernière."


"J'avais trop de choses auxquelles réfléchir. Mon esprit refusait de ralentir."


"Au lieu de ça, j'ai rejoué les scènes du toit, du parc, et tout le reste encore et encore dans mon esprit."


"Il y a encore une petite partie de mon cerveau qui est paranoïaque et qui se demande si tout ça n'était pas qu'une sorte de blague."


"Que je vais retrouver Emi à la piste et qu'elle va agir comme si rien ne s'était passé hier."


"Repoussant ces pensées au fond de mon esprit, j’enfile mes vêtements de sport et ouvre la porte."

scene bg school_track
show emi basic_grin_gym at center
with locationskip


"Emi m'attend avec son sourire habituel."

show emi basic_annoyed_gym
with charachange


emi "Tu es en retard !"

show emi basic_closedgrin_gym
with charachange


emi "Ou du moins, tu n'es pas en avance aujourd'hui."

show emi excited_hesitant_gym
with charachange


emi "Tu es fatigué ou un truc du genre ?"


"Je me retrouve à me frotter l’arrière de la tête."


hi "Quelque chose comme ça, ouais."


hi "Beaucoup de choses en tête, tout ça."

show emi basic_closedgrin_gym
with charachange


"Emi rit un peu à mon commentaire en dessous de la vérité."

show emi basic_grin_gym
with charachange


emi "Ouais, je n'ai pas bien dormi non plus."

show emi excited_proud_gym
with charachange


emi "J'étais contente que tu ne sois pas en avance, parce que je ne l'étais pas non plus."


"Je me demande si la même chose nous a gardés éveillés."


"L'image de son visage où coulent des larmes me passe devant les yeux."


hi "Qu'est-ce qui t'a empêché de dormir ?"

show emi sad_shy_gym
with charachange


"L'expression d'Emi s'assombrit, mais elle remarque ma curiosité rapidement et fait un sourire forcé."

show emi sad_grin_gym
with charachange


emi "Rien d'important."


"Il est évident qu'il y a quelque chose qu'elle ne me dit pas."


"La question est : devrais-je insister ?"


"Quelque chose l’embête clairement depuis un moment."


"Je veux l'aider, mais est-ce que ça ne serait pas juste être un fouineur ?"


"Elle sait que je tiens à elle, après tout."


hi "Tu es sûre ?"


hi "Si quelque chose t’embête, je suis là pour t'aider à arranger ça."

show emi basic_closedhappy_gym
with charachange


"Emi se met à rire, mais ce n'est pas son rire habituel. Il y a un truc qui le rend presque amer."

show emi sad_grin_gym
with charachange


emi "Arranger ça ?"


emi "Je ne pense pas que ce soit le genre de choses qui peuvent s'arranger, Hisao."


"Un sourire presque sinistre passe sur ses lèvres."


"Comme un sourire de résignation."

show emi sad_pout_gym
with charachange


emi "Je ne crois pas que tu puisses m'aider, de toute façon."


"Ça fait mal."


"Je ne veux pas lui dire, mais ça n’empêche rien."


"Elle ne réalise pas que je veux être là pour elle quand les choses tournent mal ?"


hi "Bon, je ne vais pas insister."


hi "Mais je suis là pour toi si plus tard tu décides que tu veux en parler."


hi "Ça pourrait aider."

show emi sad_shy_gym
with charachange


"Je peux voir le débat faire rage dans les yeux d'Emi."


"On dirait qu'elle veut m'en parler, mais qu'elle n'est pas sûre de pouvoir."


hi "Hé, oublie ça pour l'instant, d'accord ?"


hi "On a de la course à faire."


"À la mention de la course, quelque chose qu'elle peut gérer, Emi redevient elle-même."

show emi basic_closedhappy_gym
with charachange


emi "Ouais !"

show emi basic_grin_gym
with charachange


emi "Dépêche-toi et étire-toi, Hisao !"

show emi excited_proud_gym
with charachange


emi "Il faut qu'on s'active !"

play ambient sfx_emipacing

hide emi
with easeoutleft

stop ambient fadeout 3.0


"Elle part comme une balle, bien plus rapidement que ce à quoi je suis habitué."


scene bg school_track_on
with locationchange

scene bg school_track_running
with Dissolve(2.0)


"J'essaye quand même de tenir le rythme avec elle, testant mes limites."


"Ça me donne une impression de liberté, comme si mon cœur n'était plus important."


"Je me retrouve à avoir envie de rire, en avançant plus vite que ce que j'avais estimé être mes limites."


"Les avertissements de l'infirmier sur le fait de ne pas me pousser me traversent l'esprit, mais je les ignore."


"La sensation que j'ai, cette envie de risquer une crise cardiaque pour quelque chose d'aussi trivial qu'une course de bon matin, ne me ressemble pas."


"Quoique."


"Ou plutôt, ça devrait être le cas ?"


"J'ai un cœur en mauvais état, oui."


"Il ne sera jamais capable d'égaler la vitesse et l'endurance dont est capable celui d'Emi."


"Bien que je ne serais probablement pas aussi bon même si j'avais un cœur en parfaite santé."

stop music fadeout 6.0


"Alors que nous arrivons à la boucle finale, je sens mes jambes crier pour protester, mais pour la première fois, je les ignore."


"J’accélère pour finir en sprint, rattrapant presque Emi."


"Ce qui est impossible, bien sûr."


"Mais même comme ça, ça reste vraiment agréable."


"Oh bien sûr, mes jambes semblent être sur le point de prendre feu, et j'ai du mal à rester debout."


"Mais il y a eu quelque chose de plus aujourd'hui."


"Tout ça grâce à la fille qui sourit sur la ligne d'arrivée, m'attendant."

scene bg school_track_on
show emi basic_grin_gym at center
with locationchange

play music music_emi fadein 1.0


hi "C'était un peu plus rapide que d'habitude."


"Mon commentaire est reçu avec un sourire et un haussement d'épaules."

show emi excited_proud_gym
with charachange


emi "Je ne pouvais pas te laisser croire que j'y allais mollo avec toi, hein ?!"

show emi basic_closedgrin_gym
with charachange


emi "Mais tu t'en es bien sorti."


hi "Je n'aurais pas pu faire ça sans toi."

show emi basic_confused_gym_close
with characlose


"Ressentant toujours l’endorphine de la course et saisi d'une vague de gratitude, je serre Emi dans mes bras."


hi "Merci."


hi "Vraiment, je ne dis pas juste ça comme ça."


hi "Je te suis redevable."

show emi basic_hes_gym_close
with charachange


"Emi semble gênée par mes mots, visiblement mal à l'aise."


emi "Ne sois pas bête, Hisao."

show emi basic_grin_gym_close
with charachange


emi "Il fallait bien que quelqu'un te traîne dehors, hein ?"

show emi basic_closedgrin_gym_close
with charachange


emi "Et ce n'est pas comme si tu ne faisais rien pour moi, hein ?"

show emi basic_grin_gym_close
with charachange


emi "J'ai besoin de courir avec quelqu'un, tu te souviens ?"

show emi basic_shock_gym_close
with charachange


"Je secoue la tête, ne laissant toujours pas partir Emi qui arrête de gigoter et lève la tête pour me regarder avec le rougissement le plus fort que je n'ai jamais vu sur son visage."



hi "Non, ce n'est pas vrai."


hi "Tu voulais courir avec quelqu'un, mais tu n'en avais pas besoin."


hi "Si je n'étais pas venu le jour après le festival, tu aurais couru quand même, hein ?"


hi "Mais ça ne marche pas dans le cas inverse."


hi "J'ai seulement réussi à venir quelques fois avant le festival."


hi "Et sans toi, je n'aurais sûrement pas pu du tout."

show emi basic_closedgrin_gym_close
with charachange


"Emi me sourit et appuie sur ma poitrine avec un doigt."

show emi excited_proud_gym_close
with charachange


emi "Tu es vraiment paresseux, Hisao."


hi "Hé, je te faisais un compliment !"

show emi sad_grin_gym_close
with charachange


emi "Ben... de rien, alors."


hi "Je te le revaudrai d'une façon ou d'une autre."

show emi basic_hes_gym_close
with charachange


emi "Oh, euh, enfin..."

show emi basic_closedgrin_gym_close
with charachange


emi "Ce n'est pas nécessaire, tu sais."

show emi basic_happyblush_gym_close
with charachange


emi "Je veux dire, je t'aime bien, Hisao."

show emi sad_grin_gym_close
with charachange


emi "Et pouvoir courir avec toi le matin n'est pas une mauvaise chose pour moi non plus, alors..."


"Pour quelqu'un qui reçoit autant de compliments, elle ne semble pas habituée à la gratitude."


"Je ne trouve rien d'autre à dire, alors nous restons silencieux."


"Je deviens conscient de la respiration d'Emi, de l'humidité de ses vêtements, et de son odeur."


"Venant de n'importe qui d'autre, ça sentirait mauvais."


"Venant d'Emi, ça lui va d'une façon qui ne serait la même pour personne d'autre."


"Sa peau est fraîche, un peu collante avec la transpiration, et une légère brise fait qu'elle a la chair de poule."

show emi excited_amused_gym_close
with charachange


"Presque sans y penser, je me penche et m'approche de la bouche d'Emi qui s'est déjà avancée pour rejoindre la mienne."


"Ses lèvres sont douces, et elle gémit joyeusement alors que nous nous embrassons, envoyant des vibrations de sa bouche à la mienne."


"Tout semble s'accorder à ce moment, nous nous complétons parfaitement."

show emi basic_grin_gym_close
with charachange


"Le baiser se finit, et je laisse finalement mes bras s'aligner le long de mon corps."

show emi basic_closedgrin_gym_close
with charachange


"Emi me sourit chaleureusement et rit encore une fois."

show emi basic_closedhappy_gym
with charadistant


emi "Allez Hisao, on ferait mieux d'aller voir l'infirmier."

stop music fadeout 1.0


"Puis ça arrive."

show emi basic_closedhappy_gym:
    ease 0.25 ypos 1.05
    ease 0.25 ypos 1.0
with None

show emi excited_sad_gym:
    ease 0.25 ypos 1.05
    ease 0.25 ypos 1.0
with Dissolve(0.25)


"Alors qu'elle se tourne pour commencer à marcher, elle pousse un petit cri et trébuche en avant."


hi "Emi !"

play music music_rain fadein 2.0

show emi excited_sad_gym_close
with characlose


"Je bondis pour la redresser et remarque avec une certaine inquiétude qu'elle s'appuie sur la même jambe qu'hier soir."


hi "Ta jambe..."

show emi basic_hes_gym
with charadistant


"Emi semble paniquée et me repousse."


emi "Ça va !"


"Je dois avoir une expression meurtrie, parce qu'elle se dépêche de s'excuser."

show emi basic_shock_gym
with charachange


emi "Désolée ! Désolée !"


emi "Je ne voulais pas te pousser comme ça !"

show emi basic_closedsweat_gym
with charachange


emi "J'étais juste..."


"Elle cherche les mots à dire."

show emi sad_depressed_gym
with charachange


emi "Ce n'est rien, vraiment."


hi "Ne t'inquiète pas pour ça."


"Elle est tellement perturbée que je décide de laisser tomber tout ça."


"Mais il y a cette sensation gênante dans mon estomac qui ne veut pas partir."


"J'ai essayé de faire un pas et de l'aider, et elle m'a repoussé."


"Souriant, je repousse ces pensées au fond de mon cerveau et me concentre sur Emi."


hi "Je ne veux juste pas que tu souffres, c'est tout."

show emi sad_pout_gym
with charachange


emi "Tu n'as pas à t’inquiéter pour moi, vraiment."

show emi sad_grin_gym
with charachange


emi "Je vais bien !"


"Oui, tu dis ça, mais je ne te crois pas."


label fr_E18a:



"Pourquoi tu ne me dis pas ce qui ne va pas ?"


"C'est comme si elle était offensée par le fait que j'essaye de l'aider."


"Qu'est-ce que je suis censé faire ?"

label fr_E18b:



"Je continue de m’inquiéter pour toi malgré tout, et le fait que je n'ai rien dit hier me fait me sentir encore plus coupable aujourd'hui."


"J'aurais au moins dû demander."


"Est-ce qu'elle aurait réagi de la même façon hier soir ?"


"Je ne le saurai jamais."

label fr_E18x:

stop music fadeout 2.0

scene bg school_nursehall
with locationskip


"J'essaye toujours de comprendre ce qui s'est passé sur la piste alors que nous arrivons devant le bureau de l'infirmier."


"Emi lève une main pour frapper, hésite et se tourne vers moi avec un sourire coupable."

show emi sad_grin_gym:
    yalign 1.0 xanchor 0.5 xpos 0.47
    easein 0.5 center
with charaenter


emi "Dis, je peux te demander quelque chose ?"


hi "Bien sûr."

show emi excited_proud_gym at center
with charachange


emi "Tu peux dire à l'infirmier que je le verrai plus tard ?"

show emi basic_grin_gym
with charachange


emi "Je viens juste de me rappeler que j'ai des... trucs à faire avant les cours."

show emi sad_grin_gym
with charachange


emi "Alors il faut vraiment que je m'active."

show emi sad_shyblush_gym
with charachange


"Je la regarde avec attention, et elle semble mal à l'aise sous mon regard."


"Ouais, elle évite clairement l'infirmier."


"Sa jambe..."


"Bah, peu importe. J'ai dit que j'aiderais, et c'est ce que je vais faire."


"Mais je m'assurerai sans faute qu'elle voie l'infirmier avant la fin de la journée."


hi "Ouais d'accord, je lui dirai."

show emi excited_smile_gym
with charachange


"Emi réagit comme si je venais de lui offrir un poney à noël."

show emi excited_joy_gym
with charachange


emi "Merci beaucoup !"

show emi excited_amused_gym
with charachange


emi "T'es le meilleur, Hisao !"

show emi excited_amused_gym_close
with characlose


"Je suis récompensé pour ma complicité dans son mensonge par un baiser, et d'un coup ça vaut la peine, ou du moins c'est ce que je me dis."

hide emi
with charaexit


"Alors qu'Emi sort du bâtiment, faisant de son mieux pour ne pas boiter, je frappe à la porte du bureau."


nk "Ah, Hisao. Entre donc."

play music music_nurse fadein 1.0

scene bg school_nurseoffice
show nurse neutral at center
with locationchange


nk "Je ne vois pas Emi avec toi."

show nurse fabulous
with charachange


nk "Elle n'est pas encore malade, hein ?"


"D'après le ton de sa voix, je ne crois pas que l'infirmier s'attende à ce que je dise “Ouais, elle est malade.”"


hi "Erh, elle a dit qu'elle avait quelque chose à faire, et elle a dû partir vite, mais elle viendra vous voir plus tard aujourd'hui."

show nurse concern
with charachange


"L'infirmier pousse un soupir exaspéré."


nk "Sérieusement, cette fille..."


hi "Mmh ?"

show nurse neutral
with charachange


nk "Elle m'évite."


nk "Hier elle est sortie si vite qu'elle n'a même pas retiré ses prothèses. Et maintenant ça."


"Bon, au moins ce n'est pas juste moi qu'Emi veut éviter d’inquiéter."


"C'est... réconfortant, je crois."


"J'ai quand même l'impression que je devrais dire quelque chose pour sa jambe. J'ai dit que je mentirais pour elle, mais elle a vraiment besoin de le voir."


hi "Maintenant que vous le mentionnez, elle boitait pas mal aujourd'hui."


hi "Et hier soir aussi."

show nurse concern
with charachange


"Les yeux de l'infirmier se plissent aux mots “hier soir”."


nk "Et que faisiez-vous exactement hier soir ?"


hi "On était euh, en rendez-vous."

show nurse fabulous
with charachange


"L'infirmier lève un sourcil, comme surpris."


nk "Vraiment ? Intéressant."


hi "Hein ?"

show nurse neutral
with charachange


nk "Oh, ce n'est rien."


"Il détourne le regard, penseur, puis me sourit."

show nurse grin
with charachange


nk "Tu ne penses pas que tu peux être capable d'utiliser tes charmes de petit copain pour la faire venir me voir aujourd'hui, par hasard ?"


hi "Bien sûr que je peux !"


hi "J'avais prévu de le faire de toute façon."


hi "Je crois qu'elle s'est vraiment fait mal et qu'elle fait semblant de bien aller."

show nurse neutral
with charachange


nk "Mmh, oui. Ça lui arrive."


nk "Elle a peur que je la fasse arrêter de courir."


hi "Vous le feriez ?"

show nurse concern
with charachange


nk "Je n'en ai pas envie, mais si c'est suffisamment grave pour qu'elle boite, ben..."


nk "Je vais devoir voir ce qui ne va pas avant de me prononcer."


hi "Je vois."


"Emi, interdite de courir ? Blasphème."


"Je ne sais pas si elle est capable de fonctionner sans courir."


"Ça ne m'étonne pas qu'elle ne veuille pas admettre que quelque chose ne va pas."


hi "Bon, je vais m'assurer qu'elle vienne vous voir."

show nurse neutral
with charachange


nk "Bien. Oh, et avant que j'oublie..."

show nurse grin
with charachange


"Il me sourit à sa façon avec un léger soupçon de menace."


nk "N'oublie pas que je sais quels médicaments tu prends."

show nurse neutral
with charachange


nk "Fais bien attention avec Emi, hein ?"


"Woaw, il a l'air sérieux."


hi "Compris."


hi "Je ne ferai pas de mal à Emi. Ce n'est pas envisageable."

show nurse grin
with charachange


nk "Parfait !"


show nurse fabulous
with charachange


nk "Je détesterais que tu sois en retard."


hi "Hein ?"

show nurse grin
with charachange


nk "En retard, comme dans Hisao Nakai le retardataire."

show nurse concern
with charachange


"Il fronce brièvement les sourcils, mécontent."


nk "Ça sonnait mieux dans ma tête..."

show nurse neutral
with charachange


nk "Bon, dans tous les cas..."

show nurse grin
with charachange


nk "Sors d'ici avant de louper ta première heure !"


nk "Je suis sûr que tu as des choses à faire. Du vent !"

stop music fadeout 6.0


"Alors que je pars, je remarque l'infirmier sortir son téléphone et composer un numéro."

show nurse concern
with charachange


nk "Meiko, votre fille fait encore des siennes..."


"Je ferais mieux de retourner à ma chambre, ou je serai vraiment en retard."


"Attends, il n'était pas censé vérifier mon cœur aussi ?"



label fr_E19:

scene bg school_scienceroom
with shorttimeskip

play sound sfx_normalbell


"La sonnerie de la pause déjeuner retentit, et je sors de la torpeur dans laquelle je me suis englouti durant les cours de ce matin."


"Mon manque de sommeil de la nuit dernière, doublé du rythme intensif de la course de ce matin, m'a un peu épuisé."

$ renpy.music.set_volume(0.15, 0.0, channel="ambient")
play ambient sfx_rooftop fadein 1.0

scene bg school_staircase1
with locationskip


"Malgré ça, je monte plusieurs marches à la fois durant mon chemin jusqu'au toit."


"J'ai un léger sentiment d'exaltation maintenant, ajouté au plaisir qu'on a normalement lorsque l'on mange avec des amis."

play sound sfx_door_creak
$ renpy.music.set_volume(0.5, 1.0, channel="ambient")

scene bg school_roof
with locationchange


"Oui, Emi et Rin sont toujours mes amies, mais Emi est devenue plus que ça maintenant."


"Rin est retournée à son endroit habituel sur le toit, presque comme si elle n'avait jamais été absente."

scene ev rin_roof_boredom
show hisao rin_roof
with locationchange


hi "Tu te sens mieux alors ?"

show ev rin_roof_surprised
with charachange


"Un sourcil levé est la seule réponse que je reçois."


rin "Mieux que quoi ?"

play music music_rin fadein 6.0


hi "Erh, mieux que comment tu te sentais hier."

show ev rin_roof_nonchalant
with charachange


"Rin réfléchit intensément à la question."


rin "Je ne sais pas vraiment."


rin "Je crois que c'était plutôt pas mal pour un hier, mais c'est tout flou."


hi "Trop de médicaments pour le rhume ?"

show ev rin_roof_doubt
with charachange


rin "Ben, je dormais. Et c'est généralement assez bien."

show ev rin_roof_boredom
with charachange


rin "Mais je ne peux pas me rappeler ce que ça fait d’être endormi, parce que je n'en suis pas consciente."


rin "C'est un vrai problème."

show ev rin_roof_nonchalant
with charachange


rin "Mais cela dit, si je savais à quel point c'était bien, il est possible que je ne dormirais plus."


rin "Mais je continue d'essayer alors je pense que c'est de cette façon que j'arrive à ne pas être trop fatiguée."


hi "Un mystère éternel pour te garder endormie la nuit ?"

show ev rin_roof_boredom
with charachange


rin "Peut-être que mystère n'est pas le bon mot. Intangibilité est peut-être la façon la plus exacte de le décrire."


hi "Je vois."


"Non, je ne vois pas du tout. Je n'ai aucune idée de ce dont elle parle, mais c'est pas grave, c'est souvent comme ça."

show ev rin_roof_doubt
with charachange


rin "Tu te rappelles comment c'est de dormir ?"


rin "Comme hier, tu te rappelles ce que tu ressentais en dormant ?"


hi "En fait, je n'ai pas vraiment beaucoup dormi hier."

show ev rin_roof_nonchalant
with charachange


rin "Mmh."


rin "Peut-être que c'est parce que tu t'en rappelles subconsciemment."


hi "En fait, je crois que je m’inquiétais pour Emi."

show ev rin_roof_surprised
with charachange


rin "Emi ne s’inquiète pas suffisamment elle-même ?"


"Je n'avais pas pensé à ça, mais ça me fait réfléchir."


hi "D'accord, mais est-ce qu'elle demanderait de l'aide si elle en avait besoin ?"

show ev rin_roof_doubt
with charachange


"Rin fronce les sourcils, et j'en lève un. Est-ce que j'aurai une vraie réponse ?"


rin "Probablement pas. Il y a une chose pour laquelle elle devrait demander de l'aide ?"


hi "Sa jambe, pour commencer."


"Ça semble attirer l'attention de Rin."

show ev rin_roof_disgust
with charachange


rin "Jambe ?"


hi "Elle lui fait mal, mais elle ne veut pas voir l'infirmier."


"Rin secoue la tête en signe de désapprobation."

show ev rin_roof_doubt
with charachange


rin "Il faut que tu la forces."

show ev rin_roof_nonchalant
with charachange


rin "Comme quand elle me force à aller en cours. Pour son bien."


rin "Sinon elle pourrait perdre ses jambes à nouveau, et ça c'est trop bizarre."


rin "Perdre quelque chose deux fois."

show ev rin_roof_doubt
with charachange


rin "Surtout si tu ne les retrouves pas après la première fois."


rin "Sauf si les prothèses reviennent au même que de les retrouver."

show ev rin_roof_nonchalant
with charachange


rin "Mais c'est une sorte de perte différente, hein ?"


hi "Je pense bien."

show ev rin_roof_boredom
with charachange


rin "Mmh. Je me demande..."

stop music fadeout 0.5

show emi rin_roof
with charaenter


emi "Demande quoi ?"

scene bg school_roof
show emi basic_grin at center
with locationchange


"Emi s'est faufilée discrètement jusqu’à Rin et moi, bien que Rin ne semble pas vraiment surprise. Ce qui n'est pas surprenant en soi."

show bg school_roof at bgleft
show emi basic_grin at twoleft
with charamove

show rin basic_deadpannormal:
    tworight
    ypos 1.25
    easein 0.5 ypos 1.2
with charaenter


"Rin réussit à se redresser d'une façon experte, jetant son corps vers l'avant et s’arrêtant au moment exact pour se stabiliser."

show rin basic_absent:
    ypos 1.2
with charachange


hi "Ta jambe. Comment elle va ?"

show emi sad_annoyed
show rin basic_awayabsent
with charachange


"Ma remarque me vaut un froncement de sourcils et un regard mécontent."


emi "Ça va, je crois."

show emi sad_shy
with charachange


emi "Pas de quoi s’embêter."

show rin basic_absent
with charachange


hi "Dis ça à l’infirmier."


hi "Il insiste beaucoup pour que tu ailles le voir, tu sais."

show emi sad_pout
show rin basic_awayabsent
with charachange


"Emi fait la moue comme si je venais de lui dire qu'elle allait être punie."


emi "Il s’inquiète trop."

show emi basic_grin
with charachange


emi "Ce n'est pas grand-chose, juste une petite douleur."


"J'essaye de me retenir de rouler les yeux d'exaspération."

show rin basic_absent
with charachange


hi "Si ce n'est rien, tu ne devrais pas avoir de problème à aller le voir, hein ?"

show emi basic_annoyed
show rin basic_awayabsent
with charachange


"Emi plisse les yeux, suspicieuse."


emi "C'est lui qui te fait dire tout ça ?"

show rin basic_absent
with charachange


hi "Bon, peut-être. Un peu."


hi "Mais ce n'est pas le sujet. Je t'aurais rappelé de le voir de toute façon."


hi "Ça serait terrible si tu venais à te faire vraiment mal et à ne rien y faire."


hi "Ça empirerait les choses, et je ne veux pas te voir avoir mal, tu sais ?"


hi "Traite-moi de fou, mais je préfère quand même te voir heureuse et en bonne santé."

show emi sad_grin
show rin basic_awayabsent
with charachange


"Après chaque phrase, Emi déplisse sa grimace, jusqu’à finir par sourire, quoiqu'un peu timidement."

play music music_daily fadein 4.0


emi "Bon, si tu dis ça comme ça, alors je vais devoir aller le voir."

show emi excited_proud
with charachange


emi "Sinon tu continueras de t’inquiéter et je n'en verrai jamais le bout, hein ?"

show rin basic_absent
with charachange


hi "Exact. Je continuerai de t’embêter pour ça, et ça pourrait plomber l'ambiance dans nos rendez-vous."




hi "“Tu trouves ça bon, Hisao ?” “Parle à l'infirmier, Emi.”"


hi "“Comment était ta journée, Hisao ?” “Parle à l'infirmier, Emi.”"


hi "“Hisao, je suis prête à ce qu'on le fas—” “{b}Parle à l'infirmier, Emi.{/b}”"


hi "Tu vois ? Ça ne marche pas très bien."

show emi basic_closedhappy
show rin basic_awayabsent
with charachange


"Emi rit à mon imitation de sa voix très aiguë et me donne une tape amicale."

show emi excited_amused
with vpunch


emi "Ma voix n'est pas si aiguë, idiot."

show rin basic_deadpan
show emi excited_circle
with charachange


rin "Je l'ai trouvée plutôt bien imitée."

with Pause(3.0)


"Emi et moi regardons Rin un moment avant d'éclater de rire."

show emi sad_annoyed
show rin basic_awayabsent
with charachange


"Emi croise les bras et souffle, semblant agacée."

show emi sad_angry
with charachange


emi "Vous êtes deux idiots."

show rin basic_absent
with charachange


hi "De si vilains mots de ta part, jeune fille."


hi "Je suis abasourdi que tu puisses m’appeler, moi, un idiot."


hi "Honnêtement, je suis juste... je ne sais pas quoi penser."

show emi basic_annoyed
show rin basic_awayabsent
with charachange


"Emi me tire la langue."


emi "Salaud, va."

show emi basic_grin
with charachange


emi "Alors Rin, comment va le club d'art ces jours-ci ?"

show rin basic_surprised
with charachange


"Rin, apparemment aussi surprise que moi par le soudain changement de sujet, prend une minute pour réfléchir avant de répondre."

show rin basic_lucid
with charachange


rin "Je crois que ça va."

show rin basic_deadpancontemplation
with charachange


rin "Bien que Nomiya n’arrête pas de me dire de travailler plus."

show rin relaxed_nonchalant
with charachange


rin "Mais je ne crois pas qu'il comprenne mes méthodes."

show emi sad_annoyed
with charachange


emi "Je l'ai toujours trouvé un peu flippant."

show rin basic_lucid
with charachange


"Rin réfléchit à sa réponse une seconde."

show rin basic_awayabsent
with charachange


rin "Je n'ai jamais vraiment remarqué."

show rin basic_deadpancontemplation
with charachange


rin "Mais je ne fais pas très attention à lui la plupart du temps, c'est peut-être pour ça."


hi "Il y a souvent des réunions de club ?"

show emi basic_closedgrin
with charachange


emi "Tu envisages de rejoindre le club, Hisao ?"

show rin basic_absent
with charachange


hi "Quoi ? Nan, j'ai déjà décidé de rejoindre un club."

show emi excited_happy
show rin basic_awayabsent
with charachange


emi "Vraiment ? Lequel ?"

show rin basic_absent
with charachange


hi "Bon, ce n'est pas vraiment un club, pour être honnête..."

show emi excited_proud
show rin basic_awayabsent
with charachange


emi "Oh, tu as rejoint le club de thé ?"

show rin basic_absent
with charachange


hi "Non, j'ai euh... rejoint le club de sciences... je crois."

show emi basic_confused
show rin basic_awayabsent
with charachange


"Emi semble légèrement confuse."


emi "On a un club de sciences ?"

show rin basic_absent
with charachange


hi "Erh, pas vraiment. C'est juste moi."

show emi basic_closedhappy
show rin basic_awayabsent
with charachange


emi "Hisao, ce n'est pas un club. C'est être assis tout seul dans sa chambre à lire des livres."


hi "Non, en fait c'est juste moi et Mutou."


hi "Je suis juste le seul étudiant pour l'instant."

show emi basic_confused
show rin basic_lucid
with charachange


emi "Mutou ? Vraiment ?"


"Elle pense à quelque chose."

show emi basic_happy
with charachange


emi "Oh, c'est de ça dont tu parlais hier ? Ta réunion avec Mutou ?"


hi "Ouais, c'était notre première réunion."

show emi basic_closedgrin
with charachange


"Emi rit un peu."

show emi basic_grin
with charachange

emi "Nerd."


hi "J'y peux rien si je suis intelligent."

show emi excited_proud
with charachange


emi "Tu sais, j'aurais pu avoir besoin de ton aide il y a des années."


emi "Tu aurais dû avoir ta crise cardiaque plus tôt, Hisao."


"Je ris, et réalise que c'est probablement l'une des très rares fois où j'ai ri à propos de ma crise cardiaque."


hi "En y repensant..."

show emi sad_grin
with charachange


emi "Ouais..."

play sound sfx_warningbell


"La sonnerie met un point final à notre conversation."


hi "Hmm, je pense qu'on ferait mieux d'y aller."

show emi basic_grin
with charachange


emi "Ouais, y faut bien."

show emi excited_amused:
    xpos 0.45
with dissolvecharamove


emi "Allez Rin, toi aussi."

show rin basic_surprised
with vpunch


"Rin a apparemment commencé à somnoler, alors Emi lui donne une frappe sèche."

show rin basic_deadpanupset
with charachange


rin "J'y étais presque."

show emi basic_closedgrin
with charachange


emi "Désolée, mais tu as besoin d'aller en classe."

show rin relaxed_nonchalant at tworight
with dissolvecharamove


rin "Je désapprouve, mais peut-être que si je dors en classe j'y arriverai cette fois."

show rin relaxed_boredom
with charachange


rin "Changer d'endroit aide parfois pour ce genre de choses."


"Ni Emi ni moi ne prenons la peine de demander ce que sont ces “choses”."

stop music fadeout 3.0
stop ambient fadeout 2.0
scene bg school_hallway3
with locationskip


"Alors que nous arrivons en classe, Emi m'embrasse rapidement et continue son chemin dans le couloir, traînant Rin derrière elle."

show shizu behind_blank:
    tworight
    xpos 0.8
    easein 0.5 tworight
show misha perky_smile:
    twoleft
    xpos 0.2
    easein 0.5 twoleft
with charaenter


"Je me tourne pour entrer dans la classe et me retrouve face au duo Shizune et Misha."

play music music_shizune fadein 1.0

show shizu adjust_happy
with charachange

shi "…"


"Misha semble mener un combat perdu d'avance pour s’empêcher d'éclater de rire pendant qu'elle traduit le discours de Shizune."

show misha hips_grin
with charachange


mi "Bien que nous soyons contentes, voire ravies de voir à quel point tu réussis à te faire des nouveaux amis et à te forger des relations - avec une fille si mignonne d'ailleurs, Hicchan~..."


"Je crois que la fin de la phrase était de Misha."

show shizu basic_normal
with charachange

shi "…"

show misha hips_frown
with charachange


mi "Nous nous sentons néanmoins obligées de te rappeler poliment que les signes publics d'affection sont strictement interdits - vraiment ? C'est décevant, Shicchan - par l'article huit du code de conduite inscrit dans ton manuel étudiant."

show shizu adjust_smug
with charachange

shi "…"

show misha sign_smile
with charachange


mi "Dans ce cas, cependant, l'ignorance de la loi peut passer comme ton excuse, et nous serons éventuellement clémentes..."

show shizu behind_smile
with charachange

shi "…"

show misha hips_smile
with charachange


mi "...et les papiers nécessaires pour vous punir tous les deux ne feront que s'ajouter à une montagne de travail déjà existante que nous affrontons, nous, membres du Conseil des Étudiants - et en plus, vous êtes trop adorables ensemble~ !"

show shizu adjust_happy
with charachange

shi "…"

show misha hips_grin
with charachange


mi "Donc, considère ça comme un avertissement, et s'il te plaît évite un tel comportement à l'avenir. Du moins quand Shizune peut te voir, Hicchan~ !"


"Le boniment entier est si ridicule que je ne peux pas m’empêcher de répondre de la même manière pompeuse."


hi "Eh bien, je suis maintenant éclairé par tes propos."


hi "Je m'excuse platement pour mes actions irréfléchies et vais m'efforcer de contenir mes impulsions primaires qui, j'en ai peur, me poussent à afficher de tels signes inappropriés d'affection en public."


hi "Loin de moi l'envie d'accabler un Conseil des Étudiants déjà surchargé de travail par de telles frivolités, je ferai de mon mieux pour rendre vos vies plus faciles à l'avenir."


hi "Au moins, quand Shizune peut me voir."


"Cette dernière phrase est ponctuée d'un clin d’œil à Misha, qui a enfin perdu le contrôle de son rire."

show misha cross_laugh
with charachange


mi "Wahaha~ !"

show misha cross_grin
with charachange


mi "Bien dit, Hicchan~ !"


"Riant un peu moi-même, nous entrons dans la classe."

stop music fadeout 2.0
scene bg school_scienceroom
with shorttimeskip


"Les cours se passent sans événement intéressant et après que la cloche ait résonné, je me retrouve encore une fois seul avec Mutou."

show muto smile at center
with charaenter


mu "Bon, on dirait que nous sommes tous rassemblés pour la seconde réunion du Club de Sciences."

play music music_another fadein 2.0
show muto normal
with charachange


mu "Ou c'est le premier ? Qu'est-ce que tu en penses, on devrait compter hier comme une réunion ou pas ?"


hi "Eh bien, on a formé le club hier, non ?"


hi "C'était les affaires du club, alors on peut définitivement interpréter ça comme une réunion."

show muto smile
with charachange


"Mutou sourit à sa façon habituelle tendue et mal à l'aise. Je me demande si les muscles de son visage ne sont pas formés correctement pour le laisser sourire naturellement."


mu "Tu as vraiment un truc pour ça, je crois. La pensée logique, je veux dire."


hi "Je crois, ouais ?"

show muto normal
with charachange


mu "Un scientifique parle avec autorité, Hisao. La réponse est “Oui, c'est vrai.”"


mu "Quand le monde veut savoir comment quelque chose marche, on lui dit. Même si tout ce qu'on a n'est qu'une hypothèse décente."

show muto smile
with charachange


mu "Mais nous nous devons d'avoir l'air certain quand même, parce que nous sommes l'autorité en la matière, hein ?"


"Il rit, pour accorder avec son sourire et sa blague bizarre. Je fais de mon mieux pour ne pas grimacer, mais je ne pense pas que ça marche bien."

show muto normal
with charachange


mu "C'est entièrement faux, bien sûr."


mu "Nous en savons beaucoup, bien sûr, mais personne n'est un expert de la façon dont fonctionne le monde, et c'est dû au fait que personne ne peut être sûr. Sans certitude, il n'y a pas d'experts."


mu "Mais on aime bien prétendre, des fois."


hi "Il y a certains trucs dont on peut être certain quand même, non ?"


mu "Oui... mais non."


mu "Nous savons que la gravité est là, par exemple."


"Pour illustrer, Mutou prend un stylo et le fait tomber."


mu "Tu vois ? Encore là. Mais c'est bien de vérifier de temps en temps."


mu "C'est pour ça qu'il y a toujours des chercheurs qui travaillent sur la gravité."

show muto smile
with charachange


mu "On est assez certain de comment elle marche, mais il y a toujours une chance que quelque chose ne soit pas de la façon qu'on le croit."


mu "Alors tu vérifies, et vérifies, et vérifies. C'est tout le principe de la science, Hisao."


"Tout le temps où je l'ai écouté, j'ai été comme captivé. Mutou semble vraiment passionné par tout ça... je crois. C'est difficile à dire, parfois."


"Comment fonctionne le monde..."


"Comment fonctionnent les humains."


"Comment fonctionne l'univers."


"Toutes ces questions doivent avoir une réponse."


"Et même, cela dépendra du domaine dans lequel je me spécialiserai, peut-être que je pourrai même trouver une façon de réparer mon cœur. Cela dit, ce n'est pas vraiment une priorité pour moi."


"En plus, alors que nous commençons à discuter du livre qu'il m'a donné hier, je me retrouve davantage intéressé par ce sujet que par ma maladie cardiaque."

show muto normal
with shorttimeskip


"Avant que nous ne le réalisions, une heure est passée."


mu "Bon, mettons fin à cette réunion, d'accord ?"


mu "On aura une autre réunion... demain, ou euh... après-demain."


"Il réfléchit un moment."


mu "Disons après-demain. J'ai beaucoup de copies à corriger."


hi "D'accord. À après-demain alors."

scene bg school_hallway3
with locationchange

stop music fadeout 5.0


"Alors que je sors de la classe, je réalise que je n'ai rien de prévu ce soir."


"Emi et moi n'avons rien prévu, donc..."


"Je vais aller à la bibliothèque alors. C'est mieux que de faire des devoirs dans ma chambre, après tout."

scene black
with locationskip_in



label fr_E20:

play music music_happiness fadein 2.0
scene bg school_library
with locationskip_out


"La bibliothèque est toujours plus fraîche que le reste du bâtiment."


"Probablement pour empêcher que les livres soient abîmés par la chaleur et l'humidité."


"Les livres sont des objets robustes, mais si tu veux les garder en bon état, il faut en prendre soin un minimum."


"J'ai quelques livres qui sont tellement abîmés que les pages restent encore à peine accrochées à la couverture."


"Ça semble impossible de les utiliser, mais si on les manie avec précaution..."


"Je m'avance jusqu'au comptoir, où je vois Yuuko occupée avec quelque chose."

show yuuko neutral_up at center
with charaenter


"Elle me sourit alors que j'arrive et me fait un signe."

show yuuko closedhappy_down
with charachange


yu "Bonjour, Hisao."

show yuuko happy_down
with charachange


yu "Contente de te revoir ! Qu'est-ce que tu cherches cette fois ?"


hi "Rien de particulier. Je n'ai juste pas très envie de retourner à ma chambre, c'est tout."

show yuuko neutral_down
with charachange


"Yuuko hoche la tête."

show yuuko smile_up
with charachange


yu "Bon, si tu n'es pas occupé, peut-être que tu pourrais m'aider à chercher quelque chose ?"


hi "Bien sûr, de quoi tu as besoin ?"

stop music fadeout 5.0

show yuuko worried_up
with charachange


"Yuuko pose un doigt sur ses lèvres et regarde autour d'elle furtivement."


"Elle semble vérifier qu'il n'y ait pas d'oreilles indiscrètes."


yu "Approche-toi."

show yuuko worried_up_close
with characlose


"Je fais quelques pas hésitants en avant."


"Yuuko parle doucement dans un chuchotement confidentiel."

show yuuko neutral_up_close
with charachange


yu "Je suis sur la piste du Monte-en-l'Air de Yamaku."

play music music_tension fadein 0.5


hi "Le quoi ?"

show yuuko panic_up_close
with charachange


yu "Shh ! Les murs ont des oreilles, Hisao."



yu "Ou ils le pourraient."

show yuuko worried_down_close
with charachange


yu "Mais écoute ! Ces livres manquants, tu t'en rappelles ?"


hi "Euh, ouais ?"

show yuuko worried_up_close
with charachange


yu "Eh bien ils n'étaient pas disparus ! Ils ont été volés !"


yu "J'en suis convaincue !"


hi "Je me rappelle que tu as dit quelque chose de la sorte plus tôt, mais comment tu sais ça ?"


"Yuuko se penche plus près et chuchote encore plus bas."

show yuuko closedhappy_down_close
with charachange


yu "Parce que j'ai trouvé une de ses caches !"


hi "Tu as quoi ?"


"Yuuko semble fière."

show yuuko happy_up_close
with charachange


yu "J'ai trouvé une de ses caches ! C'était en dessous d'un des escaliers dans le dortoir des garçons !"


yu "Trois livres que je cherchais, tous là !"

show yuuko closedhappy_up_close
with charachange


yu "Je soupçonnais un voleur avant, mais ça le prouve !"


hi "Tu as repris les livres alors ?"

show yuuko panic_up_close
with charachange


"Yuuko affiche la même expression que si je venais de lui suggérer de se balader nue."



yu "Tu es fou ?"

show yuuko worried_down_close
with charachange


yu "Il ne peut pas savoir que je suis après lui ! Il pourrait disparaître pour éviter d’être capturé !"


hi "Euh... huh. Donc en quoi est-ce que tu as besoin de mon aide, alors ?"


"Yuuko regarde autour d'elle encore une fois et s'approche encore plus."

show yuuko neutral_down_close
with charachange


yu "Tu dois espionner pour moi."


hi "Espionner ?"


yu "Ouais, quand tu es dans les dortoirs, tu sais."

show yuuko closedhappy_down_close
with charachange


yu "Garde un œil ouvert pour voir s'il y a des activité suspectes."


"C'est quoi suspicieux pour elle ?"


"Je veux dire, Kenji est un mec assez suspect, mais je doute qu'il aille souvent en classe, alors ça ne doit pas être pour aller à la bibliothèque pour piquer des livres."


"D'un autre côté, où est le problème d'accepter ? Au moins ça me permet de mettre fin à cette conversation bizarre."


hi "Ouais, c'est pas un problème."

show yuuko closedhappy_down
with charadistant


"Yuuko se redresse et tape des mains, contente."


yu "Super !"

show yuuko worried_down
with charachange


yu "Maintenant, dépêche-toi et parle de quelque chose d'autre au cas où quelqu'un arrive !"

stop music fadeout 2.0

show yuuko happy_down
with charachange


yu "Alors, comment se passe l'école ?"


hi "Euh, assez bien en fait."


hi "Je cours le matin avec—"

show yuuko closedhappy_up
with charachange


yu "Emi Ibarazaki, hein ?"

play music music_comedy fadein 2.0


hi "Euh, ouais."


hi "Comment tu savais ?"

show yuuko smile_down
with charachange


yu "Je vous ai servis tous les deux au salon de thé, tu te rappelles ?"

show yuuko closedhappy_down
with charachange


yu "J'en ai déduit que si tu devais courir avec quelqu'un, ça serait probablement avec elle."


"Elle semble contente d’elle-même."


hi "Impressionnant."


hi "Bref, oui. Je cours le matin."


hi "Et euh, on sort ensemble aussi maintenant."

show yuuko closedhappy_up
with charachange


"Yuuko tape dans ses mains, toute joyeuse."


yu "Vraiment ? C'est génial !"


yu "Je suis sûre que vous êtes super ensemble !"

show yuuko neutral_down
with charachange


yu "J'adore voir les gens se trouver l'un l'autre comme ça, tu sais ?"


yu "Je me suis même dit la fois où tu es entré au Shanghai “Je me demande s'il finira avec l'une de ces filles.”"


hi "...Vraiment ?"


"Yuuko ne semble pas remarquer mon ton quelque peu étonné et hoche la tête."

show yuuko closedhappy_down
with charachange


yu "Yep ! Je pouvais le voir que tu allais finir avec l'une des deux, tu sais."

show yuuko neutral_down
with charachange


yu "J'ai l’œil pour ce genre de choses."

show yuuko worried_down
with charachange


yu "Bien sûr..."


"Son expression s’attriste légèrement."


yu "Je ne suis pas aussi douée que toi pour trouver quelqu'un."


hi "Aw, je suis sûr que ce n'est pas vrai."

show yuuko neutral_down
with charachange


yu "Oh, c'est vrai."


yu "J'ai rencontré ce garçon une fois..."

show yuuko smile_down
with charachange


yu "On s'entendait vraiment bien, mais il était plus jeune que moi."

show yuuko neutral_up
with charachange


yu "C'était un peu bizarre, mais pas extrêmement non plus."


yu "Ce qui était vraiment bizarre est qu'il a disparu un jour, et que je ne l'ai pas revu depuis."


hi "Huh. C'est effectivement étrange."

show yuuko worried_up
with charachange


yu "N'est-ce pas ?"

show yuuko neurotic_down
with charachange


yu "J’espère que ce n'est pas quelque chose que j'ai fait..."


"Je me sens obligé de la rassurer."


hi "Je suis sûr que non."

stop music fadeout 4.0

$ renpy.music.set_volume(0.5, 0.0, channel="sound")
play sound sfx_phone
show yuuko panic_up
with vpunch


"Alors que j'allais essayer de la rassurer un peu plus, nous sursautons tous les deux lorsqu'une sonnerie provient soudainement de ma poche."

show yuuko worried_down
with charachange


"Yuuko soupire pour s'en remettre alors que je sors le téléphone de ma poche. Je me sens un peu bête d'avoir indirectement causé ça."

scene bg school_library_yuuko_blurred
show phone mobile:
    alpha 0.0 xalign 0.5 yanchor 0.5 ypos 0.7 subpixel True
    easein 1.0 ypos 0.5 alpha 1.0
with locationchange
with Pause (0.5)


hi "Emi ? Quoi de neuf ?"


emi "Ah dieu merci, je ne t'avais jamais appelé avant, alors je ne savais pas si le numéro marcherait ou si tu allais décrocher et je ne peux pas—"

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play music music_pearly fadein 2.0


hi "Woaw, Emi, du calme."


hi "Qu'est-ce qu'il y a ?"


"Il y a une pause de l'autre côté de la ligne, durant laquelle je peux entendre Emi essayer de contrôler sa respiration pour se calmer."


"Quelque chose l'a terriblement troublée, et ça commence à me troubler aussi."


emi "Est-ce que tu peux juste..."


emi "Tu peux passer ?"


emi "Du genre, maintenant ? Ou bientôt ?"


emi "J'ai vraiment, vraiment besoin de te parler."


"Il y a un ton suppliant dans sa dernière phrase que je ne pense pas avoir déjà entendu de sa part."


hi "Bien sûr, j'arrive tout de suite."


hi "Ne bouge pas, d'accord ?"


"Alors que je commence à être bien troublé, je me mets également à dire des choses qui ne sont pas bien logiques."


emi "D'accord. Je t'attends."


hi "À tout de suite."

show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with None

scene bg school_library
show yuuko worried_down at center
show phone mobile:
    alpha 1.0 xalign 0.5 yanchor 0.5 ypos 0.5 subpixel True
    easeout 1.0 ypos 0.7 alpha 0.0
with locationchange
with Pause (0.5)

hide phone
with None

with charaexit


"Je presse le bouton pour finir l'appel avant de remettre le téléphone dans ma poche, m'excusant auprès de Yuuko de fuir comme ça, et pars en courant."

scene bg school_girlsdormhall
with locationskip


"Peut-être qu'une autre fois je me serais arrêté pour penser à l'heure, ou à quel point c'est suspect pour un garçon d'aller dans le dortoir des filles à cette heure."


"Sauf que là tout de suite je suis juste inquiet car je vais rejoindre Emi, découvrir ce qui ne va pas et voir comment je peux l'aider."

play sound sfx_doorknock2


"Je frappe à sa porte et on me répond avec un petit “Entre”."

scene bg school_dormemi at left
with locationchange


"Quelque chose ne va pas du tout dans la scène que je vois."


"Emi est là, oui."


"Mais elle est dans un fauteuil roulant."


"Et ses jambes sont manquantes. Je regarde dans sa chambre et les vois dans un coin, comme si elles avaient été jetées là."

show emiwheel weaksmile at center
with charaenter


"Emi répond à mon entrée par un sourire de travers qui exprime à la fois sa joie de me voir et un mal-être extrême."


emi "Salut, Hisao."


"On dirait qu'elle a pleuré, mais si c'est le cas, elle a arrêté maintenant."


"Je remarque que j'ai un peu le souffle court, ayant monté les marches deux à deux pour venir ici."


"Mon cœur ne semble pas s'en soucier cela dit. Je note ça dans un coin et y repenserai une autre fois."


"Une fois où je ne regarderai pas, abasourdi, ma petite amie dans un fauteuil roulant."


"Réalisant que je n'ai toujours pas répondu à sa salutation, mon cerveau se met en route."


hi "Emi ? Qu'est-ce qu'il s'est passé ?"

show emiwheel pout
with charachange


emi "Je crois que j'aurais dû t'écouter, Hisao."

show emiwheel sad
with charachange


emi "J'ai chopé une mauvaise infection à la jambe. Je ne suis pas autorisée à me mettre dessus pendant au moins quelques semaines."


"Elle sort un rire amer, chose qui ne devrait pas arriver de sa part."

show emiwheel frown
with charachange


emi "Ha, je ne peux même pas marcher."


emi "J'aurais pu utiliser une béquille et garder une de mes jambes, mais je ne vois pas l’intérêt."

show emiwheel awayfrown
with charachange


emi "Pourquoi faire ça ? On ne peut pas courir avec une seule jambe."

show emiwheel pout
with charachange


emi "Au moins de cette façon je peux toujours, je sais pas, rouler vite ou un truc du genre."


hi "O-ouais, c'est bien, non ?"


"Ma tentative gênée de voir le bon côté des choses semble appréciée, mais pas vraiment efficace."


"Emi hausse encore une fois les épaules."

show emiwheel awayfrown
with charachange


emi "C'est juste... une gêne."

show emiwheel frown
with charachange


emi "Je veux dire, on ne peut même pas manger sur le toit maintenant. Pas d’accès aux fauteuils."


hi "Ouais, mais c'est pas grave, hein ?"



hi "On peut toujours manger ensemble, c'est le plus important."

show emiwheel weaksmile
with charachange


"Ce sourire tordu encore une fois. Ça fait mal à voir."


emi "J'imagine, ouais."

show emiwheel frown
with charachange


emi "Mais comme j'ai dit, c'est une gêne."

show emiwheel awayfrown
with charachange


emi "Je veux dire, je n'ai pas utilisé de fauteuil roulant depuis..."

stop music fadeout 10.0


"Elle réfléchit pendant une seconde."

show emiwheel pout
with charachange


emi "Peut-être sept ans ? Quelque chose comme ça, du moins."


emi "Longtemps."

show emiwheel weaksmile
with charachange


emi "J'ai peur d'avoir un peu perdu la main."


hi "Bah, heureusement c'est temporaire, hein ?"


"Emi hoche la tête."

show emiwheel neutral
with charachange


emi "Ouais, bien sûr."


emi "Ce n'est pas comme si je les avais perdues de façon permanente."

show emiwheel awayfrown
with charachange


emi "Mais ça reste super chiant quand même."


"Je hoche la tête, compatissant."


"Je ne peux pas faire grand-chose d'autre, après tout."


"Qu'est-ce que je vais faire, dire “J'te l'avais dit” ?"


"Bien que je lui {b}aie dit{/b} d'aller faire voir sa jambe."


"Mais quand j'ai remarqué, c'était déjà trop tard de toute façon."


hi "Tu as besoin d'aide pour quelque chose ?"


hi "Euh, enfin, je peux faire quelque chose ?"

show emiwheel closedsmile
with charachange


"Emi secoue la tête et il y a un peu de son sourire normal qui est revenu."


emi "Nan, je me débrouille bien toute seule."

show emiwheel grin
with charachange


emi "Bien que si tu veux m'aider à me mettre sur le lit, ça m’épargnerait d'avoir à rouler jusque là-bas."


"Je rougis, malgré moi."


"Emi rit."

play music music_heart fadein 0.5

show emiwheel wink
with charachange


emi "Tu es tellement prude, Hisao."


hi "Je ne suis pas prude ! Je ne voudrais juste pas profiter d'une jeune fille telle que toi."


hi "Tellement peu galant."

hide emiwheel
with charaexit

show bg school_dormemi at right
with charamove


"Je pousse la chaise d'Emi jusqu'au lit, la soulève et la dépose facilement dessus. Elle s'arrange rapidement et s'assied au bord."

show emi basic_grin:
    center
    ypos 1.0
    easein 0.5 ypos 1.1
with charaenter


"Elle est un peu plus lourde qu'elle en a l'air. Ça serait méchant de le dire à voix haute, bien sûr."


hi "Eh beh, t'es pas légère."

play sound sfx_pillow
show comic vfx2
show emi excited_amused:
    center
    ypos 1.1
with hpunch

with Pause(0.5)

show comic vfx2:
    truecenter
    easeout 0.5 yanchor 0.3 alpha 0.0
with Pause(0.5)


"Emi me frappe avec un oreiller."

show emi basic_closedgrin
with charachange


emi "Salaud."


hi "Je dis juste ça comme ça."


hi "Ça doit être toute cette course."

show emi sad_shy
with charachange


"À la mention de la course, le sourire d'Emi vacille légèrement."

show emi sad_pout
with charachange


emi "Bon, je ne vais pas avoir à m’inquiéter de ça pendant un moment, hein ?"

show emi sad_grin
with charachange


emi "Peut-être que je vais perdre du poids."


hi "C'est comme ça qu'on perd du poids, non ? En arrêtant les activités physiques ?"


show emi basic_closedgrin
with charachange


emi "Je suis sûre que c'est ce que recommanderait l'infirmier."


hi "En parlant de ça, tu vas toujours venir le matin ?"


hi "Je détesterais courir seu—"

show emi sad_depressed
with charachange


emi "Ah, merde..."


"L'interjection soudaine d'Emi, plus un murmure qui dit trop fort autre chose de trop profane, m’interrompt, choqué."


"Elle est penchée en avant, essayant de cacher le fait qu'elle pleure, couvrant ses yeux de sa main."


"Bien sûr, ses petits soubresauts et bruits rendent assez évident le fait qu'elle pleure."


hi "Oh, je suis désolé."


hi "Oublie ce que j'ai dit, d'accord ?"

show emi sad_depressed_close at center
with characlose


"Je passe un bras autour d'elle et la serre contre moi."


"Je ne trouve rien d'autre à dire ou à faire. Comment est-ce qu'on réconforte quelqu'un qui vient de reperdre ses jambes ?"

show emi sad_pout_close
with charachange


"Emi passe ses bras autour de moi et reste comme ça un moment."


hi "Désolé."


hi "Je suis vraiment pas doué pour réconforter."


emi "Ne dis pas ça."


emi "Je vais bien, vraiment."


"Sa voix est légèrement étouffée dans ma poitrine. Je lui tapote la tête pour la rassurer."


hi "C'est l'état d'esprit à avoir."


hi "Tu traverseras tout ça sans problème, je le sais."


hi "En plus, je suis là pour t'aider, tu te rappelles ?"

show emi sad_shy_close
with charachange


"Emi lève la tête et me regarde avec ses yeux encore humides."

show emi sad_grin_close
with charachange


emi "Tu peux ? Tu peux vraiment ?"


"Son sourire est tordu, et quelque chose brille dans son regard."


"Je ne sais pas si elle se moque ou non."


hi "Bien sûr. Après c'est sûr, tu n'es pas légère et tout, mais -{w=0.5}{nw}"

play sound sfx_impact

show emi excited_amused_close
with vpunch


extend " mmph !"


"Mon commentaire très spirituel est interrompu par Emi qui presse soudainement ses lèvres sur les miennes. Je suis pris par surprise et me cogne la tête contre le mur derrière son lit."


hi "Aïe."

show emi basic_hes
with charadistant


"Emi recule, essayant d'avoir l'air inquiète plutôt que sur le point de rire."


emi "Est-ce que ça va ?"

show emi excited_proud
with charachange


emi "Désolée !"


"Je me frotte l’arrière de la tête et lui souris."


hi "Tu m'as pris par surprise."


hi "Ça va devenir une habitude ? Je vais me faire passer un savon par Shizune et Misha à chaque fois ?"


"À la mention du duo, Emi se met à rire."

show emi basic_closedgrin
with charachange


emi "Sérieusement, ces deux-là..."

show emi basic_grin
with charachange


emi "Si je ne savais pas pourquoi, je serais intriguée de savoir pourquoi elle traîne avec quelqu'un de tellement sérieux."


hi "Tu parles de laquelle ?"

show emi basic_closedhappy
with charachange


emi "Tu sais exactement de qui je parle, Hisao. Misha est loin d’être sérieuse."


hi "Quelle est la raison, alors ?"

show emi basic_confused
with charachange


emi "Hein ?"


hi "La raison pour laquelle Misha traîne avec Shizune."

show emi basic_closedgrin
with charachange


"Emi ignore ma question avec un sourire."


emi "Aucune idée."


hi "Je vois."

show emi basic_grin
with charachange


emi "Bref, tu sembles oublier ta question d'origine, hein ?"


hi "Oh, ouais, c'est vrai."


hi "Ça ne te gênerait pas de me prévenir, quand ça arrive ?"


hi "Sinon je vais réussir à finir avec un trauma crânien."


"J'argumente en me frottant la tête."

show emi excited_amused
with charachange


"Emi rit très fort."


emi "Tu pourrais mettre un casque."

show emi excited_proud
with charachange


emi "C'est le cas de certains ici, tu sais."


stop music fadeout 1.0


hi "Ou je pourrais juste me venger !"

play sound sfx_pillow

show emi excited_circle
with vpunch


"J'attrape un oreiller et l'envoie dans la tête d'Emi."

show expression im.Composite((295,1200), (0,0), "sprites/emi/emi_excited_circle.png") as emi:
    xalign 0.5 yanchor 0.5 ypos 1.0 subpixel True
    easeout 0.8 ypos 1.25 rotate -90
with None

show expression im.Composite((295,1200), (0,0), "sprites/emi/emi_excited_sad.png") as emi:
    xalign 0.5 yanchor 0.5 ypos 1.0 subpixel True
    easeout 0.8 ypos 1.25 rotate -90

with Dissolve(0.5)
with Pause(0.3)

play sound sfx_impact

hide emi
with vpunch


"Emi bascule et tombe du lit en cognant le sol avec un boum."

show emi sad_pout:
    center
    ypos 1.2
    ease 1.0 ypos 1.0
with Dissolve(1.0)


"Son bras réapparaît rapidement sur le lit, et elle réussit à se redresser."


"Il y a vraiment beaucoup de force dans ce petit corps."


"Son visage est baissé, me laissant croire que j'aurais pu accidentellement lui faire mal."


hi "Emi ? Ça va ?"


hi "Tu ne t'es pas cogné la—{w=0.3}{nw}"

show emi excited_smile_close
with vpunch


"Une main se lève et m'attrape le col. Elle m'attire avec un mouvement brusque, son visage est maintenant à quelques centimètres du mien et elle sourit effrontément."


hi "Emi... ?"

show emi excited_smile_close:
    subpixel True
    linear 0.1 ypos 1.7 zoom 2.0
with None

scene white
with Dissolve(0.1)

play sound sfx_impact

scene black
with Dissolve(0.75)


"Elle me donne un grand coup de tête, et cela fait un énorme bruit quand nos têtes s'entrechoquent."

scene bg school_dormemi at right
show emi basic_closedgrin at center
with openeye


"Je m'assieds et me frotte le front maintenant endolori alors qu'Emi affiche un petit sourire narquois."

show emi basic_grin
with charachange


emi "Et {b}ça{/b} comme vengeance, t'en penses quoi ?"

play music music_running


hi "C'est injuste !"


hi "Tu ne peux pas te venger d'une vengeance !"


"Pour quelqu'un à qui il manque les jambes, Emi est étonnamment agile."

show emi basic_grin:
    center
    parallel:
        "emi basic_closedgrin" with Dissolve(0.2, alpha=True)
    parallel:
        easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None


"J'essaye de l'attraper mais elle roule sur le côté et me frappe avec son oreiller."


"Bien sûr, les chances sont contre elle. Je peux me lever, déjà."

scene black
with vpunch


"Ouh !"

window hide

show evh emi_grinding_victorytall:
    xalign 0.5 yalign 1.0 subpixel True
    easein 12.0 yalign 0.0

with Dissolve(1.0)

with Pause(6.0)

window show


"Je n'y arrive pas, après tout. Emi m'a fait trébucher avec succès et est maintenant assise sur moi, triomphante, alors que je suis allongé sur le dos. Je ne sais même pas comment elle a réussi ça."


emi "J'ai gagné."


"Ses yeux brillent de malice. J'ai été battu à plate couture, et par une fille qui fait la moitié de ma taille en plus."


"Cela dit, perdre n'est pas si horrible. Emi est assise sur moi et c'est quelque chose que moi, ou mon corps, ne peut pas facilement ignorer."

scene bg school_dormemi
with locationchange


"J'ouvre la bouche pour parler, mais Emi se précipite pour m'embrasser avant que je ne puisse dire un mot. Je n'oppose aucune résistance alors qu'elle presse ses lèvres contre les miennes, pas que j'en ai envie de toute façon."


"C'est... différent, d'une certaine façon."


"Elle se retire, languit sur ma lèvre et m'embrasse à nouveau. Sa langue rentre dans ma bouche, explorant. Je peux sentir une chaleur se répandre à travers mon corps alors que mon cœur commence à battre plus vite."


"Mon esprit commence à s'embrouiller et je suis vaguement conscient de ma main qui passe sur la blouse d'Emi. Emi pousse un léger gémissement quand j'arrive à sa poitrine, puis il y a un rire, et puis—"

scene evh emi_grinding_victory
with locationchange


"Je regarde une Emi qui me sourit."


emi "Je te l'avais dit. Ça fait ma seconde victoire."


hi "Quoi ? Ça ne compte pas, tu as utilisé tes atouts féminins."

show evh emi_grinding_wink
with charachange


emi "“À l'amour comme à la guerre”, hein ?"


emi "Ha, et tu rougis même ! Je ne savais pas que tu étais du genre à rougir, Hisao."


hi "Tu rougissais aussi, tu sais. Probablement ton coté prude."


"Même moi je dois admettre que c'est quelque chose d'idiot à dire à une fille qui est à califourchon sur moi et qui, jusqu’à maintenant, explorait mes amygdales."

show evh emi_grinding_grin
with charachange


emi "Alors comme ça, je suis prude ?"


emi "Bon alors, voyons voir qui rougit le premier, d'accord ?"


"Je ne sais pas vraiment si le ton de sa voix me terrifie ou m'excite, mais cette question devient rapidement discutable."

label fr_E20h:

show evh emi_grinding_half_undress
with charachange

show evh emi_grinding_half_grin
with charachange


"Avec des gestes experts, elle retire sa blouse et la jette avec précaution à côté du lit. Son soutien-gorge et sa jupe la rejoignent rapidement."


emi "Ha !"


"Je combats le rougissement qui monte. C'est assez difficile."


hi "L'escalade, hein ?"

show evh emi_grinding_off_yawn
with charachange


"Ma propre chemise s'ensuit, enlevée avec quelques difficultés à cause de ma position. Emi bâille d'un air moqueur."


emi "Il va falloir que tu en fasses plus que ç—"

show evh emi_grinding_off_closesurprise
with charachange
stop music fadeout 3.0


emi "Ah...!"


"Mes mains caressent doucement la peau nue d'Emi, lui causant des frissons. On dirait que mes mains agissent toutes seules, encore une fois. Si notre position le permettait, je finirais probablement de la déshabiller."


"Je commence à dire quelque chose à propos du rougissement d'Emi, mais nous arrivons très rapidement tous les deux à la limite de quelque chose que nous retenons à peine. La conversation s’arrête et je sens mes bras perdre de l'énergie."

play music music_one fadein 0.5


"Aucun de nous, cependant, n'était préparé pour cette soudaine nouvelle sensation."

show evh emi_grinding_off_closearoused
with charachange


"Une chaleur indescriptible me parcourt, venant à la fois de moi, et apparemment, d'Emi aussi."


"Avec une main sur ma poitrine pour se stabiliser et une autre tenant la mienne pour s'assurer que je ne vais pas profiter de son corps encore une fois, elle semble assez contente d’elle-même."

show evh emi_grinding_off_aroused
with charachange


"Et puis, après un mouvement d’hésitation, elle bouge."


"Et elle bouge encore."


"Et encore."


"Alors qu'elle bouge, la respiration d'Emi s'accélère. Ma respiration commence à s’accélérer et à devenir plus saccadée aussi."


"Le corps d'Emi frissonne et tremble contre le mien, je peux sentir qu'elle commence à perdre l'équilibre. Ça doit être difficile de rester stable sans avoir ses jambes."

show evh emi_grinding_off_closesurprise
with charachange


"Je la stabilise du mieux que je peux, plaçant mes mains sur ses hanches. Elles sont fermes et contractées."


"C'est logique, vu à quel point elle court. La puissance potentielle dans ces muscles les fait tressaillir alors qu'elle répond à mon toucher."


"Ce que je n'arrive pas à prendre en compte est le fait que ma tentative pour stabiliser Emi la fait glisser vers l'avant et, eh bien... la sensation est fantastique."

show evh emi_grinding_off_arousedclosed
with charachange


"Sa culotte glisse facilement contre mon pantalon, et il ne faut pas longtemps pour qu'on trouve un rythme."


"Mais Emi refuse de s'y tenir, allant parfois rapidement, parfois lentement, même s’arrêtant par moments. Je ne suis pas sûr de savoir si elle fait ça pour jouer avec moi, ou si c'est pour que ce soit mieux pour elle, mais je m'en moque."


"La chaleur entre nous est de plus en plus intense, et je ne peux pas m’empêcher de pousser un petit gémissement. Le son semble encourager Emi."


"Je commence à ponctuer ses mouvements avec un peu des miens, ce qui vaut à sa modeste poitrine de bondir en rythme avec mes mouvements. Sa respiration commence à s’accélérer alors que nous continuons, et la mienne fait de même."


"Avec les yeux clos, ses lèvres se plissent dans l'expectative. Je parviens à me redresser pendant quelques instants, nos bouches recherchant le contact l'une de l'autre, sa poitrine glissant contre la mienne alors que notre transpiration se mélange."



"Alors que je me laisse tomber à nouveau, mon pantalon est trempé de transpiration. Je le retirerais bien si ça ne signifiait pas arrêter ce que l'on fait."


"Et je ne veux pas arrêter ce qu'on fait, arrêter cette pression s'intensifiant, ce titillement à l'arrière de mon cerveau."


"Emi glisse de plus en plus vite, haletant forcément, sa voix semblant incapable de transmettre ce qu'elle ressent. Son corps, quant à lui, s'en sort très bien."

show evh emi_grinding_off_come
with charachange


"Soudainement elle se met à bouger un peu plus frénétiquement alors que ma propre respiration me fait presque mal, finissant dans une poussée finale qui m'envoie au-delà d'une sensation déferlante dont je ne connaissais même pas l'existence."

scene white
with Dissolve(3.0)


"Mon esprit se vide, et je n'entends plus rien alors que je succombe à la sensation de l'orgasme. Pendant quelques secondes, le monde entier semble s’évanouir à l'exception de cette sensation d'Emi et moi, ensemble."

show evh emi_grinding_off_end
with Dissolve(1.0)


"Et puis... ça passe. L’ouïe me revient, et je me retrouve à regarder dans les yeux la fille qui est sur moi."


"Pendant quelques minutes, aucun de nous deux ne parle. Le bruit de notre respiration venant de nos poitrines alourdies de l'expérience est la seule chose qui perturbe l'immobilité de la pièce."


"Finalement, à contre-cœur, elle se retire de moi et s'assied contre le mur, je la rejoins."

label fr_E20x:

scene bg school_dormemi at right
with locationchange

show eminude smile_close
with charachange


emi "Alors... j'ai rougi ?"


hi "Je n'ai pas fait attention."


hi "Et moi ?"

show eminude neutral_close
with charachange


"Emi hausse les épaules, respirant toujours un peu fortement."

show eminude weaksmile_close
with charachange


emi "Pas fait attention non plus."


hi "Bon, peut-être qu'on devrait—"

play sound sfx_dooropen

stop music fadeout 0.3

show rin basic_deadpan behind eminude:
    center
    xpos 1.0 xanchor 0.0 alpha 0.0 subpixel True
    easein 0.5 right alpha 1.0
show eminude blush_close
with vpunch


rin "Il faut que j'utilise ta fenêtre."


"Mon premier réflexe est de me cacher, mais je me rends compte que je suis toujours épuisé et assis à côté d'une Emi torse nu, donc aucune échappatoire possible."

show rin basic_awayabsent:
    right alpha 1.0
with charachange

show rin basic_absent
with charachange

show rin basic_awayabsent
with charachange


"Les yeux de Rin passent sur Emi, moi, et se concentrent sur la fenêtre."

show rin basic_deadpannormal
with charachange


rin "Il y avait un nuage."

play music music_comedy fadein 0.5

show eminude neutral_close
with charachange


emi "Un nuage ?"

show rin basic_lucid
with charachange


"Rin hoche la tête."

show rin relaxed_nonchalant
with charachange


rin "Je le regardais depuis ma fenêtre, mais il n'est pas resté devant ma fenêtre."

show rin negative_spaciness
with charachange


rin "Alors il faut que j'utilise ta fenêtre."

show eminude closedsmile_close
with charachange


"Emi remue un peu, et je dois tousser pour couvrir mon rire."


emi "Tu as besoin de la fenêtre pour longtemps ?"


emi "On est euh..."

show eminude wink_close
with charachange


emi "Occupés."


"Cette fois je ne peux pas retenir mon rire."

show rin negative_annoyed
with dissolvecharamove


"Rin nous ignore tous les deux et regarde par la fenêtre."

show rin basic_deadpanupset
with charachange


"Ses épaules s'affaissent, et elle semble déçue."


rin "Mmh."


rin "Il a changé en quelque chose d'autre."


rin "Décevant."

show eminude grin_close
with charachange


"Emi a du mal à garder une expression sérieuse."


emi "Désolée d'entendre ça, Rin."

show eminude pout_close
with charachange


emi "On pourrait avoir un peu d'intimité maintenant, s'il te plaît ?"

show rin relaxed_nonchalant
with charachange

with Pause(0.2)

show rin relaxed_nonchalant:
    easeout 1.0 xpos 1.0 alpha 0.0 xanchor 0.0 subpixel True
with Pause(1.0)

play sound sfx_doorclose

hide rin
with None


"Rin hausse les épaules, comme pour dire “Peu importe” et passe le pied autour de la porte, la fermant derrière elle."

show eminude happy_close
with charachange


"Nous nous laissons aller tous deux à rire, incapables de gérer autrement la visite bizarre de Rin à un si mauvais moment."


"Après que notre rire se soit tari, je regarde Emi. On est tous les deux complètement épuisés."

stop music fadeout 5.0


hi "Bon."

show eminude neutral_close
with charachange


"Emi lève un sourcil."


emi "Bon ?"


hi "Encore ?"

show eminude wink_close
with charachange


"Emi sourit et rit, puis hoche la tête."

show eminude grin_close
with charachange


emi "On devrait sûrement enlever les vêtements, cette fois."

$ suppress_window_after_timeskip = True

scene black
with dissolve


label fr_E21:

window hide None

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show


"La lumière du soleil passe à travers ma fenêtre peu après que mon alarme ait ruiné le silence matinal."

play music music_dreamy fadein 6.0


"Je me sens engourdi."


"Les événement de la veille me reviennent en tête et je me mets même à rougir."


"C'était une soirée bien remplie - et ça explique pourquoi le bas de mon dos est si endolori."


"Le chemin du retour, comme je m'en rappelle, a été plutôt intense."


"Mon pantalon a été... souillé, j'ai dû le laver dans la salle de bain avant de retourner à ma chambre."


"Mais il y avait toujours une tache bien évidente sur le devant."


"Heureusement pour moi, la seule personne que j'ai croisée sur le chemin du retour était Kenji."


"Et il n'a rien remarqué du tout."


"À part le fait que j'étais là."


"Bien sûr, il m'a demandé comment s'était passée ma soirée et si j'avais obtenu des informations importantes."


"Je ne sais même pas si j'ai ouvert la bouche pour répondre, j'étais trop fatigué pour m'en préoccuper."


"Et ce matin, j’admets que je me sens assez épuisé."


"J'ai pourtant promis à Emi que je la verrais sur le terrain, et je détesterais la décevoir."

scene bg school_track
show emiwheel weaksmile at center
with locationskip


"Elle est en effet en train de m'attendre à la piste au moment où j'arrive."


"Faisant de son mieux pour avoir l'air joyeuse, malgré le fait qu'elle est assise dans un fauteuil roulant."


"Je lui fais signe et commence à m’étirer."


hi "Tu es en avance."

show emiwheel frown
with charachange


"Emi fronce les sourcils et secoue la tête."

show emiwheel angry
with charachange


emi "N'importe quoi."


emi "{b}Tu{/b} es en retard."

show emiwheel grin
with charachange


emi "Trop dormi, Hisao ?"

show emiwheel wink
with charachange


emi "Trop crevé ?"


"Au moins elle semble être elle-même."


"Comme prévu, elle ne semble pas trop timide pour mentionner notre... précédente activité."


hi "Hé, tu es chanceuse que je sois venu tout court."


hi "Toute cette activité cardiovasculaire la nuit dernière, j'ai presque cru que j'aurais à voir l'infirmier après."

show emiwheel wink
with charachange


"Emi se met à rire, puis son expression devient rapidement inquiète."

show emiwheel blush
with charachange

stop music fadeout 8.0


emi "Hé, ce n'est pas euh..."


emi "Je veux dire, tu n'es pas..."


hi "Allez, crache."

show emiwheel awayfrown
with charachange


emi "C'est juste que ça serait difficile à expliquer si tu avais un souci pendant qu'on..."


hi "Oh."

hi "{b}Oh.{/b}"


"Maintenant qu'elle le dit, c'est une inquiétude légitime."


"Je n'y avais pas vraiment pensé hier soir, bien sûr - d'autres choses plus pressantes m'occupaient la tête."


hi "Ben, je ne pense pas que quoi que ce soit que nous, euh, {b}fassions{/b} soit plus fatigant qu'une de nos courses matinales, et je les tolère très bien, alors..."

show emiwheel frown
with charachange


"Emi réfléchit un instant."

show emiwheel evil
with charachange


"Une lueur sournoise apparaît dans ses yeux."

play music music_emi fadein 2.0


emi "Dis..."


hi "Mmh ?"

show emiwheel grin
with charachange


"La lueur disparaît et Emi me regarde d'un air attristé."


"Je ne peux pas m’empêcher d’être vaguement suspicieux."

show emiwheel happy
with charachange


emi "J'ai oublié de prendre une paire de gants."


hi "Pourquoi tu as besoin de gants ?"

show emiwheel smile
with charachange


"Emi montre la chaise roulante sur laquelle elle est assise."


emi "Pour ça, bien sûr !"

show emiwheel wink
with charachange


emi "Bien sûr, je peux bouger et me déplacer sans problème même sans gants, mais je veux être capable de pouvoir bien pousser."

show emiwheel grin
with charachange


emi "Et pour avoir ce genre de vitesse, il faut avoir des gants si tu ne veux pas de cloques."


hi "Alors quoi, tu me laisses m'occuper de ça alors ? Je dois y aller tout seul ?"

show emiwheel awayfrown
with charachange


"Emi pense pendant une minute - ou fait semblant de penser."

show emiwheel closedsmile
with charachange


emi "Mmh... si je me rappelle bien, il y a une paire ou deux de rechange dans le local sportif."


"Elle a sérieusement envie de le faire, alors."


"Mais avec son uniforme scolaire normal ? Je m'attendais à ce qu'elle porte son uniforme de sport pour quelque chose comme ça."


hi "Hein, qu'est-ce qu'ils font là-bas ?"

show emiwheel frown
with charachange


"Emi me regarde bizarrement."


emi "Sérieusement ? Tu ne penses pas qu'il puisse y avoir une paire de gants de course dans un local de sport d'une école pour handicapés ?"


"Bon, dit comme ça, c'est sûr que c'est plus logique."


hi "Je suis encore en train de m'habituer à cet endroit, hein. Ménage-moi un peu."

show emiwheel grin
with charachange


emi "Je peux laisser passer ça cette fois."

show emiwheel wink
with charachange


emi "Maintenant viens, j'ai besoin de ton aide."


"Je ne sais pas pour quoi faire, mais je ne sais pas non plus pourquoi il y aurait des gants de course dans le local, alors je ne vais pas insister."

scene bg school_sportsstoreext
with locationchange


"Emi se déplace facilement jusqu'au local, bien que je peux entendre comme un grognement dans sa respiration."


"C'en est presque mignon."


"Je me dépêche un peu pour arriver avant elle à la porte, l'ouvrir sera plus facile pour moi que pour elle."

play sound sfx_door_creak

show emiwheel neutral:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter



"La porte s'ouvre et Emi commence à entrer dans le local, mais se retrouve coincée à l’entrebâillement."


"On dirait qu'il y a une petite marche après la porte qui est trop élevée pour qu'elle puisse la passer avec le fauteuil."

show emiwheel awayfrown:
with charachange

show emiwheel awayfrown:
    center
    ease 0.4 xpos 0.45
    easeout 0.2 xpos 0.5
    ease 0.4 xpos 0.45
    easeout 0.2 xpos 0.5
    ease 0.4 xpos 0.45
    easeout 0.2 xpos 0.5
    ease 0.4 xpos 0.45
    ease 0.2 xpos 0.5
with Pause(1.0)


"Elle se heurte contre elle plusieurs fois, sans succès, avant de fixer des yeux la responsable du problème."

show emiwheel angry at center
with charaenter


emi "Stupide chaise."

show emiwheel frown
with charachange


emi "Hisao, tu peux me donner un coup de main ?"


hi "Ouais, pas de problème."

scene bg school_sportsstoreroom
with locationchange


"C'est assez simple pour moi de faire passer la petite marche à Emi, la bousculant légèrement."

show emiwheel blush_close_ni at center
with charaenter


emi "Hé, doucement !"


hi "Oups ! Désolé."


"C'est là aussi que je ne vois pas où je vais et cogne la chaise d'Emi contre un tapis."

play sound sfx_impact

show expression im.Composite((425,1200), (0,0), night("sprites/emiwheel/close/emiwheel_blush_close.png")) as emiwheel:
    xalign 0.5 yanchor 0.5 ypos 1.0 subpixel True
    easeout 0.5 ypos 1.4 rotate 70

with vpunch

hide emiwheel
with None


"Elle pousse un petit cri étonné et tombe de sa chaise en avant."


"Il y a un petit moment de silence où je regarde, horrifié, ce que j'ai fait, et Emi me fixe."


emi "Hisao..."


hi "Oui ?"


emi "Promets-moi que tu ne travailleras jamais dans un hôpital."


hi "Désolé ! Je ne voulais pas !"


"Emi rit, et lève une main."


emi "Tu aurais l’amabilité de m'aider à me remettre dans ma chaise, Hisao ?"

show emi basic_closedgrin_close_ni:
    center
    ypos 1.2
    easein 0.5 ypos 1.0
with charaenter


"Alors que je me penche pour redresser Emi, elle sourit, triomphante, et m'attire dans un baiser qui fait que nous nous désintéressons tous deux du fait de la remettre dans sa chaise."

play sound sfx_door_creak


"En fait, alors que je bouge pour une position plus confortable, il s’avère que la chaise a maintenant repassé la porte qui se ferme en un claquement."

play sound sfx_rustling

hide emi
show eminude smile_close_ni at center
with charachange


"Bon, au moins on a de l'intimité maintenant, ce qui est une bonne chose étant donné que mes mains commencent vite à retirer la chemise et la jupe d'Emi."


"Je suis étonné de me rendre compte qu'elle a oublié de mettre un soutien-gorge aujourd'hui. Est-ce qu'elle avait prévu ça ?"

show eminude blush_close_ni
with charachange


"Elle pose ses mains sur mes épaules tandis que je descends en embrassant Emi dans le cou, faisant particulièrement attention à un emplacement spécial que j'ai découvert hier, juste là où la nuque rejoint l'épaule."


emi "Tu deviens plutôt doué pour ç-haa !"


hi "Je fais de mon mieux."

show eminude frown_close_ni
with charachange


"Emi repousse ma poitrine, insistante, et je me recule en affichant une expression confuse."


emi "J'ai un aveu à faire, Hisao."


hi "Oh ?"


"M'étant redressé, je décide, à la place, de porter mon attention sur sa poitrine."

show eminude blush_close_ni
with vpunch


"Alors qu'elle essaye de parler, ses mots sont saccadés à cause de petits rires que je trouve vraiment adorables."

show eminude wink_close_ni
with charachange


emi "Je n'utilise p-haa vr-hee hee-ment w-woah ! de gants."


"Ma propre réponse est murmurée à sa poitrine plutôt que directement adressée à son visage."


hi "J'aurais dû le savoir..."


"Les mots deviennent vite inutiles."

show eminude closedsmile_close_ni
with vpunch


"Les mouvements d'Emi sont presque frénétiques, comme si elle se retenait depuis qu'on s'était vus ce matin, et maintenant elle est lâchée."


"Je suis presque pris par surprise par son agressivité, sentant qu'elle est presque sur le point de m'arracher la chemise dans la façon qu'elle a de lutter pour être dans la position dominante."


"Quant à moi, j'avoue que je suis aussi dans cette attitude-là, à contre-attaquer, roulant et luttant alors même que je lui caresse la poitrine, même lorsque ses doigts se plantent dans mes épaules, et que je perds la notion d'où nous sommes."

show eminude blush_ni
with vpunch


"Tellement que je roule à côté du tapis et atterris sur quelque chose de petit et assez dur."


hi "Aïe !"

show eminude weaksmile_ni
with charachange


"Emi, toujours rouge et respirant un peu fortement, me regarde et explose de rire."


emi "Désolée, désolée. Ça va ?"


hi "Ouais, je crois. Je sais pas sur quoi j'ai atterri, cela dit."


"Je passe une main derrière mon dos et en sors l'objet incriminé, l'inspectant de plus près."

stop music fadeout 0.2


"“Lubrifiant intime. Saveur citron.”"


"Hein, quoi ?"

play music music_running

show eminude happy_ni
with charachange


"Emi lève les yeux et commence à rire encore plus fort - si c'est possible."


hi "Je crois que ce n'est pas... lié à l’athlétisme."

show eminude closedsmile_ni
with charachange


emi "Haha la vache, je sais à qui c'est !"


hi "Quoi ?"

show eminude wink_ni
with charachange


emi "C'est au capitaine de l'équipe !"


"Ah, mon vieil ennemi. En quelque sorte."


hi "Comment tu sais que c'est le sien ?"

show eminude awayfrown_ni
with charachange


"On dirait que j'ai posé une question bête, ou du moins Emi le pense."

show eminude frown_ni
with charachange


emi "Parce que c'est lui qui m'a dit que le local était un bon endroit pour... comment il appelait ça ?"

show eminude pout_ni
with charachange


emi "“Des rencontres clandestines.”"


hi "Oh ? Il t'a invitée à une ?"

show eminude happy_ni
with charachange


"Emi éclate encore plus de rire."


"La vue d'une Emi nue riant est étrangement sublime."


"Je ressens l'envie de finir notre conversation et retourner à ce que nous faisions, malgré ma question assez précise."

show eminude closedsmile_ni
with charachange


emi "Hisao, le capitaine est gay."


"Oh."


hi "Vraiment ? Et moi qui pensais au début que vous étiez ensemble."

show eminude awayfrown_ni
with charachange


emi "Ben... J'avais un petit quelque chose pour lui quand j'ai rejoint l'équipe, mais il n'était pas intéressé."

show eminude frown_ni
with charachange


emi "Forcément."

show eminude neutral_ni
with charachange


emi "Mais on est de bons amis quand même."

show eminude grin_ni
with charachange


emi "Enfin, c'est lui qui m'a parlé de tout ça, tu sais."


hi "J'hésite à demander."


"J’hésite vraiment. Mais je demande quand même."


hi "Mais pourquoi est-ce qu'il a euh... besoin de lubrifiant d'ailleurs ?"


hi "Je veux dire, il ne... euh..."


"Mais comment est-ce qu'Emi fait pour ne pas rougir ?"

show eminude wink_ni
with charachange


emi "Bien sûr qu'il l'utilise, enfin, tu sais."

show eminude evil_ni
with charachange


emi "Anal."


"J'essaye de réprimer un sourire."


"J'échoue."

show eminude happy_ni
with charachange


"Emi rit aussi."


hi "Et il te {b}raconte{/b} tout ça ?"

show eminude awayfrown_ni
with charachange


"Emi hausse les épaules."

show eminude neutral_ni
with charachange


emi "Ouais, bien sûr."

stop music fadeout 10.0

show eminude closedsmile_ni
with charachange


emi "Il est vraiment enthousiaste pour ça."


emi "Il dit que c'est une sensation imbattable."


hi "Ah... euh."


"L'air ambiant du local semble chargé d'une horrible curiosité."


hi "C'est intéressant."


hi "Ben je vais devoir le croire sur parole."

show eminude neutral_ni
with charachange


emi "Ben..."


"Les oiseaux à l'extérieur arrêtent de chanter."


"Le vent arrête de souffler."


"Quelque part, un homme est en train de boire un café. Il s’arrête avec la tasse aux lèvres."

show eminude neutral_ni
with charachange


emi "On pourrait..."


extend " peut-être..."

show eminude blush_ni
with charachange


emi "Essayer."

play music music_one fadein 5.0


"Ma mâchoire se décroche soudainement et tombe au sol."


hi "Q-quoi ?"


"Emi rougit fortement, se frottant l’arrière de la tête."

show eminude pout_ni
with charachange


emi "Ben, c'est juste qu'on ne peut pas vraiment... faire comme hier soir, tu sais ?"


emi "Ça serait un peu... ça serait dangereux, tu sais ?"

show eminude weaksmile_ni
with charachange


emi "Je veux dire, ce n'était pas exactement une super idée hier soir."

show eminude closedsmile_ni
with charachange


emi "Donc tu sais, on pourrait essayer ça pour voir si c'est euh..."


hi "Aussi bien ?"

show eminude weaksmile_ni
with charachange


emi "Eh bien euh, ouais. En gros."


hi "Ah."

label fr_E21h:

scene evh emi_shed_base1
show emi emi_shed_grin
show hisao emi_shed_neutral
show evh_l emi_shed_up
show evh_r emi_shed_down
with shorttimeskip


emi "Fais attention !"


hi "Tu es sûre de toi sur ce coup ?"


"Je suis positionné derrière Emi, qui regarde par dessus son épaule, un peu rouge."


"Bon, bien sûr, une fois qu'on a décidé de faire ça, on a dû se remettre dans l'ambiance."


"Une fois ça fait, on a vidé la bouteille de lubrifiant et..."


"Nous y voilà."

show emi emi_shed_hesitant
with charachange


emi "Oui, je suis sûre ! Allez, avant que je me calme et change d'avis."


"La respiration d'Emi est toujours un peu lourde, et elle semble presque impatiente."


"Ce qui est normal, j'imagine. On est si proches l'un de l'autre, et on fait traîner les choses."


"Je crois qu'on est tous les deux temporairement fous."


"Du moins ça va être mon alibi quand tout ceci sera fini."


"J'essaye de ne pas penser aux détails de ce que je m’apprête à faire."


"Je ne pense pas que ça va être très propre."

show evh emi_shed_base2
show hisao emi_shed_closed
with charachange


"Prenant une respiration qui est autant pour me calmer moi qu'elle, j'entre lentement."


"Il y a beaucoup de résistance, c'est comme si nos deux corps étaient réticents à l'idée de le faire."

show emi emi_shed_shock
with hpunch


"Le corps entier d'Emi se tend, et alors que je suis partiellement rentré, la sensation est étonnamment agréable, si ce n'est un peu étrange."


"Emi, quant à elle, ne semble pas à l'aise."


"Son expression est presque comique."

show hisao emi_shed_neutral
with charachange


hi "Tu veux que j’arrête ?"


"La respiration d'Emi s'attarde un peu dans sa gorge, et il lui faut quelques secondes de plus qu'en temps normal pour répondre."

show emi emi_shed_closed
with charachange


emi "N-non, continue. C'est juste bizarre."


"Elle rit un peu."


"Je ne peux pas lui en vouloir. Je suis surpris d'avoir même réussi à former une phrase."

show hisao emi_shed_closed
with charachange


"C'est... chaud."


"La sensation est vraiment étrange."


"Le lubrifiant scintille d'une manière peu naturelle."


"Ça me met mal à l'aise."


"Je continue de me frayer un chemin à l'intérieur d'elle, avançant lentement et écoutant avec attention la respiration d'Emi."

show evh emi_shed_base3
show emi emi_shed_hesitant
with charachange


"J'atteins ma limite et m’arrête. Emi se tourne encore, mordant sa lèvre inférieure."


emi "Tu vas essayer de bouger, ou on va juste rester bêtement comme ça ?"

show hisao emi_shed_neutral
with charachange


hi "Non, je voulais juste te donner une chance de t'ajuster."


"Ça ne veut rien dire."


"Quand est-ce qu'on a décidé de faire ça déjà ?"

show emi emi_shed_grin
with charachange


emi "Je ne pense pas qu'il y ait quoi que ce soit à ajuster, Hisao."

show emi emi_shed_hesitant
with charachange


emi "Essaye de bouger. Peut-être que ça sera mieux ?"


"Elle a l'air de douter, mais n'est pas prête à s'avouer vaincue maintenant qu'on a été aussi loin."

show emi emi_shed_closed
with charachange


"Je commence à bouger lentement et ça semble nous convenir à tous les deux, et Emi ferme les yeux pour essayer de se concentrer sur cette nouvelle sensation."


"Alors que je commence à trouver un rythme, j'arrive lentement à retrouver la même sensation d'abandon que je ressentais hier."

show hisao emi_shed_closed
with charachange


"Je ferme les yeux et essaye de me perdre dans la sensation, sauf que..."


"Quelque chose ne va pas."


"Emi ne fait aucun bruit."


"J'ai très vite appris hier qu'Emi n'est pas du tout silencieuse quand elle apprécie."

show hisao emi_shed_neutral
with charachange


"Alors que j'ouvre les yeux, je crois qu'Emi essaye de se mettre dans le bain, mais ça ne semble pas bien marcher pour elle."


"Elle a les yeux fermés et elle se mord la lèvre, mais semble plus être dans la tolérance que le plaisir."


"Un peu “bon, c'est un échec, mais avec de la chance ça sera bientôt fini”."


"Je suis un peu mal à l'aise, là."


"Pour dire vrai, je n'ai pas envie d’arrêter."


"Mais en même temps, ça ne semble pas être bien pour Emi - ou si c'est le cas, ça monte bien plus lentement que pour moi."


"Je me sens mal. J'ai envie qu'Emi apprécie, aussi."

show evh_r emi_shed_up
show emi emi_shed_shock
with charachange


"Je passe un bras autour d'Emi pour lui toucher la poitrine, ce qui la surprend."

show hisao emi_shed_sweat
with charachange


"Ce qui fait qu'elle se resserre fortement autour de moi, ce qui m'inflige une vague de plaisir."

show evh emi_shed_base4
show hisao emi_shed_neutral
show emi emi_shed_closed
show evh_l emi_shed_down
with charachange


"Mon halètement semble amuser Emi, mais son sourire s'efface vite en un gémissement alors que je bouge mon autre main sur son ventre et commence à glisser jusqu'au duvet entre ses jambes."


"Le mouvement de mes hanches qui s'accélère et les poussées de mes mains sur le bas-ventre d'Emi font arriver les gémissements et halètements auxquels je suis habitué."

show hisao emi_shed_sweat
with charachange


"Je me concentre uniquement sur mes mains, une qui glisse et caresse, l'autre qui lui touche la peau douce et sensible, elle a la chair de poule, frissonne et transpire alors que son propre orgasme la fait se resserrer, jusqu’à ce que je ne puisse plus—"


"Nonjenepeuxplus—"

show hisao emi_shed_closed
with charachange


"AhjesuisdésoléEmijevais"


"Je donne une dernière poussée, mes doigts se resserrant sur le téton d'Emi et rentrant entre ses jambes."

window hide

play sound sfx_flash
with SilentWhiteout(0.1,0.0,0.1)
play sound sfx_flash
with SilentWhiteout(0.1,0.0,0.4)
with GenericWhiteout(0.5,1.0,4.0)

window show


"Le dos d'Emi convulse et se redresse tandis qu'un cri aigu fait écho dans le local, et je sens la vague de mon propre orgasme annihiler toute autre sensation dans mon corps."

show evh_l emi_shed_up
show evh_r emi_shed_down
with charachange


"Les bras d'Emi perdent leur énergie et elle tombe en avant, suffisamment violemment pour nous séparer et tirer sur quelque chose d'important pour moi dans le processus."

label fr_E21x:

play sound sfx_impact

scene bg school_sportsstoreroom
with vpunch


"Le changement soudain entre le plaisir et la douleur me fait perdre l'équilibre, et je tombe sur Emi."

stop music fadeout 2.0


emi "Aïe !"


hi "Aïe."


"Je roule sur le côté pour soulager Emi et me redresse, respirant fortement et essayant d'ignorer la douleur dans mon entrejambe."


"Emi se plaint un peu alors qu'elle se tourne. Elle attrape quelques mouchoirs qu'on avait préparés d'avance et s'essuie avant de remettre sa culotte et s'adosser étrangement contre un mur."


"Respirant toujours fortement, je décide de m’asseoir contre le mur à côté d'elle. Le froid du mur contre mon dos est appréciable."

show eminude sad_close_ni at center
with charaenter


emi "Ça fait {b}mal{/b} à la fin !"


hi "Ouais, je euh..."


hi "Ce n'était probablement pas une super idée."


"Emi se repositionne pour rester assise à côté de moi sans avoir mal. À en juger par sa grimace, ça ne marche pas vraiment."

show eminude pout_close_ni
with charachange


emi "Ouais, je vais devoir en parler avec le capitaine."

show eminude angry_close_ni
with charachange


emi "C'est évident qu'il mentait."

play music music_ease


"Le ridicule absolu de la situation me vient soudainement à l'esprit, et je commence à rire."

show eminude happy_close_ni
with charachange


"Emi secoue la tête et commence à rire avec moi."

show eminude grin_close_ni
with charachange


emi "Dis, Hisao."


hi "Ouais ?"

show eminude pout_close_ni
with charachange


emi "On fera plus jamais ça, hein ?"


hi "Ouais, je crois que ma curiosité est satisfaite sur ce coup."


"Emi hoche la tête, approuvant."

show eminude closedsmile_close_ni
with charachange


emi "Bien."

show eminude smile_close_ni
with charachange


emi "Je crois qu'on devrait se concentrer sur les bases, tu penses pas ?"

show eminude blush_close_ni
with charachange


emi "Je veux dire, la plupart de tout ces trucs, c'est nouveau pour moi."


hi "Comment ça, “la plupart” ?"

show eminude grin_close_ni
with charachange


"Emi sourit malicieusement."

show eminude closedsmile_close_ni
with charachange


emi "Je ne te le dirai jamais."


"Une pensée désagréable me vient à l'esprit."


"Encore plus désagréable est la pensée d'avoir à demander à Emi."


"Pourtant, après ce qu'on vient de faire, ça devrait être du gâteau."



hi "Dis, il y a un lavabo ?"


hi "J'aimerais un peu, erh."


hi "Me laver un peu."

show eminude blush_close_ni
with charachange


"La mâchoire d'Emi se détache."


emi "Dans le {b}lavabo{/b} ?"


hi "Bah, il n'y a pas vraiment d'autre endroit où je pourrais le faire, non ?"


hi "Et ça euh... Je veux éviter qu'il y ait une odeur."


hi "Que l'infirmier puisse remarquer."


"C'est la conversation la plus bizarre que je ne n'ai jamais eue."

show eminude closedsmile_close_ni
with charachange


emi "Tu as raison."

show eminude grin_close_ni
with charachange


emi "Ouais, il y a euh... C'est au fond."

show eminude smile_close_ni
with charachange


emi "Il y a peut-être du savon, aussi."


hi "Merci."

hide eminude
with charaexit


"Il y a effectivement un petit savon à main, ce qui est mieux que rien."


"Pas de serviette, cela dit. Je vais devoir sécher comme ça."

show eminude grin_ni at center
with charaenter


emi "T'as fini ?"


hi "Ouais, ça ira pour l'instant. Ce n'est pas comme si je n'allais pas prendre de douche après avoir vu l'infirmier."

show eminude weaksmile_ni
with charachange


emi "Tant mieux."

show eminude wink_ni
with charachange


emi "Maintenant aide-moi à trouver mes vêtements. Tu les as balancés quelque part."


hi "Hé, tu n'as pas fait mieux ! Comment je suis censé expliquer ce trou dans ma chemise, hein ?"

show eminude closedsmile_ni
with charachange


emi "Désolée. Je me suis un peu excitée tout à l'heure."

scene bg school_sportsstoreroom
with shorttimeskip


"Il faut un moment, mais nous finissons tous les deux plus ou moins habillés."


"Il y a un moment de panique où aucun de nous deux ne sait où est le fauteuil roulant d'Emi, mais je me rappelle qu'il est passé par la porte et vais le récupérer."

show emiwheel neutral_close_ni at center
with charaenter


emi "Fais plus attention en passant la porte cette fois, d'accord ?"

show emiwheel awayfrown_close_ni
with charachange


emi "Je suis pas très copine avec les bosses là tout de suite."


hi "Je suis désolé qu'on ait essayé ça."

show emiwheel grin_close_ni
with charachange


"Emi hausse les épaules et sourit."

show emiwheel wink_close_ni
with charachange


emi "Bah, ça valait le coup, hein ?"

show emiwheel closedsmile_close_ni
with charachange


emi "Et puis de toute façon, c'était un bon exercice, hein ?"


"Je ne peux pas contredire ça."

scene bg school_nursehall
with shorttimeskip


"Alors que nous allons jusqu'au bureau de l'infirmier, je remarque qu'Emi continue de remuer inconfortablement sur sa chaise."

show emiwheel awayfrown
with charachange


emi "Rah, c'est vraiment bizarre."

show emiwheel neutral
with charachange


emi "Heureusement que je suis dans un fauteuil cela dit, Hisao."


hi "Pourquoi ça ?"

show emiwheel weaksmile
with charachange


emi "Parce que comme ça je n'ai pas à expliquer à l'infirmier pourquoi je marche bizarrement."

hi "Oh."


hi "On ne le fera plus jamais."

scene bg school_nurseoffice
show nurse fabulous at center
with locationchange


"L'infirmier est assez sympathique pour ne pas commenter les marques qu'a laissées Emi sur mes épaules."


"Et il ne dit pas un mot non plus sur le fait qu'Emi gigote sans arrêt sur son fauteuil roulant."


"Soit il ne remarque pas, soit il ne veut pas le remarquer."


"Aussi, il va falloir que je m'assure pendant un petit moment qu'il ne glisse pas de cyanure dans mes médicaments."


"Juste au cas où."

stop music fadeout 4.0
scene bg school_dormhisao
with locationskip


"Je me douche pendant plus longtemps que d'habitude, juste pour être sûr d'être propre après notre petite “expérience”, puis m'effondre sur le lit."


"J'ai cours dans vingt minutes, alors je peux sûrement me permettre une sieste."

scene black
with shuteye




label fr_E22:

scene black
with dissolve

with Pause(5.0)

play sound sfx_doorknock


"Toc toc."


"Qui c'est ?"

play sound sfx_doorknock


"Toc toc."


"C'est pas ça la blague."

play sound sfx_doorknock


"Toc toc."


"J'ai déjà demandé qui c'était !"


"Plus important, il est quelle heure ?"


"Encore plus important, quel jour... ?"

scene bg school_dormhisao
with openeyefast


"Je suis soudainement réveillé par le fait que les frappements à ma porte ne s’arrêtent pas et par le fait qu'il est midi."


"Un jour d'école."


"Maintenant que je suis complètement éveillé, je peux me rappeler pourquoi je faisais une sieste."


"Va falloir que je trouve une meilleure excuse que ça pour mon absence."


"“Désolé de n’être pas venu en classe, j’expérimentais sexuellement avec ma petite copine et ça m'a épuisé.”"


"Ouaip, ça passera bien."

play sound sfx_doorknock


"Je me demande encore combien de temps les frappements vont continuer."


"Va falloir que j'ouvre la porte."

play sound sfx_dooropen

scene bg school_dormhallway
show kenji tsun at center
with locationchange


"Je ne suis étrangement pas surpris de voir Kenji de l'autre côté."


"Bien qu'on dirait que Kenji est surpris de me voir."


ke "Qu'est-ce que tu fais là, mec ?"

play music music_kenji fadein 0.5


hi "Ben, je dormais."

show kenji neutral
with charachange


"Kenji acquiesce."

show kenji happy
with charachange


ke "Assommé. Je vois."

show kenji tsun
with charachange


ke "Je te l'avais dit de faire attention mec avec cette fille, Ibarazaki."


ke "C'est le genre de choses qui arrivent quand tu ne fais pas attention."


"Il fait une tentative pour regarder à l’arrière de ma tête."

show kenji neutral
with charachange


ke "Elle t'a frappé avec quelque chose ?"


ke "Ou elle t'a drogué ?"


hi "Arrête d'essayer de me toucher."

with flash


"Kenji sort une lampe et me met la lumière dans les yeux."


ke "Tu as une commotion ?"


hi "Je n'ai pas été assommé."

show kenji happy
with charachange


ke "Peut-être que tu ne t'en rappelles juste pas."


"Cette conversation ne mène nulle part."


hi "Non, j'ai juste eu une matinée fatigante et me suis endormi."

show kenji tsun
with charachange


ke "Peu importe, mec."


ke "Si tu veux être dans le déni, je ne peux pas t'en empêcher."


ke "Mais tu dois faire gaffe avec cette fille, mec. Elle est pas clean."


hi "Quoi ?"

show kenji rage
with charachange


ke "C'est dangereux d’être près d'elle ; elle est l'une de leurs plus sinistres agents !"


ke "Si tu ne fais pas attention, qui sait ce qui peut arriver !"


ke "Elle a fait tomber des hommes plus forts que toi, tu sais !"


hi "De quoi est-ce que tu parles ?"


hi "Elle est un agent de rien du tout, et elle ne m'a pas assommé, d'accord ?"


hi "Et je doute aussi forcément qu'elle ait fait tomber qui que ce soit."

show kenji tsun
with charachange


"Kenji semble presque offensé."


"Je n'ai aucune idée de pourquoi."


ke "Tu ne me crois pas ?"


ke "C'est dur mec. Vraiment dur."


ke "J'essaye juste de veiller sur toi. C'est ce que font les amis, tu sais."


"On est amis ? Je ne le savais pas."


"Encore une fois, je me demande si Kenji sait ce qu’être un ami implique."


"Je ressens quelque chose proche de la pitié pour lui, se tenant là devant moi."


"Peut-être qu'il pense vraiment veiller sur moi."


hi "Je sais, je sais."


hi "Désolé. Merci pour l'avertissement."


"Je lui tends la main en signe de paix."

show kenji neutral_close
with characlose


"Kenji la serre et la secoue fort, comme si elle était en feu."


"Il y a un silence gênant pendant quelques secondes avant que Kenji se rappelle qu'il est en train de me serrer la main."

show kenji happy_close
with charachange


ke "Bref, j'ai besoin d'un service."


hi "Quel genre de service ? Je n'ai plus d'argent..."


ke "Non c'est faux. Tu as de l'argent dans le tiroir de ton bureau sous un cahier noir. Pour les urgences."


hi "Tu as fouillé ma chambre ?"

show kenji neutral_close
with charachange


ke "Ce n'est pas important."


ke "Je n'ai pas besoin d'argent, de toute façon."


"Il prend un ton très sérieux."

show kenji tsun_close
with charachange


ke "Je suis sur le point de faire une opération majeure."


ke "Je vais faire éclater la conspiration à la lumière du jour si j'ai raison."


ke "Mais c'est dangereux, alors j'ai besoin que tu fasses quelque chose pour moi au cas où je ne reviendrais pas."


hi "Euh, bien sûr mec. Tout ce que tu veux."


"Mais qu'est-ce qu'il prévoit de faire ?"


"Je devrais en parler à quelqu'un ?"

show kenji neutral_close
with charachange


ke "Si je disparais, attends trois jours et envoie mon journal aux médias."


ke "Il est caché dans ma chambre sous un faux fond dans un des tiroirs de mon bureau."


hi "Comment est-ce que je rentre dans ta chambre ? Je n'ai pas de clé."

show kenji tsun_close
with charachange


"Kenji me regarde comme si j'étais fou."


ke "Alors crochète la serrure. Tu sais comment faire, hein ?"


ke "C'est une compétence important à acquérir dès l'enfance !"


hi "Euh, ouais, bien sûr que je sais comment faire."


hi "Je vais m'assurer de euh, faire ça pour toi. Si tu disparais."


"Je ne crois pas que je veuille lire le journal de Kenji."


"Dans tous les cas, Kenji semble assez content que j'aie accepté de faire ça pour lui."

show kenji happy_close
with charachange


ke "Super, mec. Super."


ke "J'te vois plus tard, j'ai des choses à faire."

stop music fadeout 5.0

show kenji happy_close:
    easeout 0.5 xpos 0.7 alpha 0.0
with Pause(0.5)

hide kenji
with None


"Et il est parti à toute allure dans le couloir."


"Il a donné l'impression que c'est vraiment le coup final."


"J'espère que je n'aurai pas à exaucer ses dernières volontés."

scene bg school_dormhisao
with locationchange

play sound sfx_doorclose


"Secouant la tête, je ferme la porte et retourne jusqu’à mon lit."


"Je devrais aller en cours, au moins pour la seconde partie de la journée."


"Mais d'un autre côté, j'ai déjà passé la demi-journée sans aller en cours..."


"Et j'ai envie de lire le livre de Hawking que Mutou m'a prêté..."


"Je suis sûr qu'il comprendra."

with shorttimeskip

play sound sfx_hammer


"Toc toc."


"Cette fois le bruit me fait lever la tête de mon livre."


"C'est bien différent de se faire réveiller."


hi "Qui c'est ?"


emi "Moi ! Tu n'es pas content ?"

play music music_emi fadein 4.0


"La voix est étouffée derrière la porte, mais sans aucun doute c'est Emi."

play sound sfx_dooropen

scene bg school_dormhallway
show emiwheel smile at center
with locationchange


"Je bondis et ouvre la porte, un grand sourire sur le visage."


hi "Hé ! Content de te revoir !"

show emiwheel grin
with charachange


"Emi me sourit en retour, la tête levée depuis son fauteuil roulant."

show emiwheel closedsmile
with charachange


emi "Ouais, je serais venue plus tôt, mais le fichu ascenseur ne marchait pas."

show emiwheel pout
with charachange


emi "J'ai dû attendre qu'ils le réparent."

show emiwheel awayfrown
with charachange


emi "Tu penses qu'ils auraient pu mieux l'entretenir, mais noooon..."


"Je ris un peu à son expression vexée et l'invite à entrer."

scene bg school_dormhisao
with locationchange


"Elle roule facilement à l'intérieur et, avec mon aide, se met sur mon lit."

show emi basic_closedgrin:
    center
    ypos 1.0
    easein 0.5 ypos 1.1
with charaenter


emi "Voilà. Bien plus confortable que cette stupide chaise."

show emi basic_grin:
    ypos 1.1
with charachange


"Un soupir de satisfaction emplit l'air, et pendant une minute nous ne faisons que nous regarder l'un l'autre."


"C'est à ce moment que je remarque les cercles autour des yeux d'Emi."


"Ils ne sont pas si marqués, mais ils n'étaient clairement pas là auparavant."


"Avant que je puisse demander pourquoi, Emi me fixe d'un regard espiègle."

show emi excited_happy
with charachange


emi "Bon, je n'ai pas pu m’empêcher de voir que tu n'étais pas au déjeuner aujourd'hui."


emi "En fait, je ne pense pas t'avoir vu du tout."

show emi excited_proud
with charachange


emi "Qu'est-ce qui s'est passé, mmmh ?"


hi "Me suis endormi."


hi "Je ne me suis réveillé qu'à midi, et seulement parce que Kenji m'a réveillé."

show emi excited_amused
with charachange


emi "Qu'est-ce qui t'a autant fatigué, mmh ?"


hi "Exercice exténuant ce matin. Légèrement inconfortable, aussi."

show emi basic_closedhappy
with charachange


"Emi tousse, à moitié en riant, à moitié embarrassée."

show emi basic_happy
with charachange


emi "Rappelle-moi de ne plus jamais le faire."


hi "Pas de problème. Ce n'était pas vraiment fantastique pour moi non plus, pour être honnête."


hi "On va juste éviter ça à partir de maintenant."


hi "Tu as, euh, toujours mal ?"

show emi basic_confused
with charachange


"Emi me regarde, abasourdie."


hi "Quoi ? C'est une question légitime !"

show emi sad_grin
with charachange


emi "Parmi toutes les questions que je pensais que tu ne me poserais jamais, c'est l'une d'entre elles."


hi "Bah, je ne pensais pas avoir à poser la question un jour, alors on est quittes."

show emi basic_closedhappy
with charachange


"Emi se met à rire."


emi "Je crois aussi, hein ?"

stop music fadeout 5.0

show emi sad_shy
with charachange


emi "Bon, puisque tu demandes, oui. Je suis encore un peu endolorie."

show emi sad_pout
with charachange


emi "On ne le fera plus jamais."


hi "Rien à redire."


"Un bâillement lui échappe et je lève un sourcil."


hi "Fatiguée ?"

show emi sad_grin
with charachange


"Emi hoche la tête, un peu endormie."

play music music_serene fadein 8.0

show emi sad_depressed
with charachange


emi "Pas bien dormi."


"Tu dors pas bien ?"


"Je peux voir qu'elle n'avait pas l'intention de me dire ça non plus, il y a eu un léger sursaut de sa part, comme si elle avait été prise en train de mentir, et elle s'est empressée de dire :"

show emi basic_closedgrin
with charachange


emi "C'est pas bien grave cela dit."


hi "Quel est le problème ?"

show emi basic_grin
with charachange


"Emi hausse les épaules et refuse de donner des détails."


hi "Stress des examens ?"



"Un autre haussement d'épaules, mais après une pause, elle hoche la tête avec hésitation."

show emi sad_shy
with charachange


emi "Euh, ouais, je pense."


emi "D'ailleurs, c'est pour ça que je suis venue."


"Elle commence à avoir l'air de plus en plus triste."


"Pas que ce soit très évident, mais elle a les yeux baissés sur ses jambes, elle gigote un peu et parle à voix basse."

show emi sad_pout
with charachange


emi "On euh, il faut qu'on arrête de traîner autant ensemble."


hi "Hein ? Pourquoi ?"


"Emi prend une grande inspiration, comme si elle l'avait préparé."

show emi sad_shy
with charachange


emi "Parce que c'est trop bien d’être avec toi."


emi "Et je ne peux pas me concentrer quand tu es là."


emi "Avec les examens qui arrivent bientôt, je ne peux juste... pas avoir ce genre de distraction."

show emi sad_depressed
with charachange


emi "Sinon mes notes en pâtiraient, j'en ai peur."


hi "Je pourrais t'aider à étudier..."

show emi sad_grin
with charachange


"Elle me sourit, clairement triste de la situation."


emi "J'adorerais si on pouvait, mais on n'étudierait pas vraiment, hein ?"

show emi sad_shy
with charachange


emi "Je veux dire même maintenant, j'essaye d'avoir une conversation avec toi, mais j'ai juste comme envie de, euh..."

show emi sad_shyblush
with charachange


emi "Pas discuter."

hi "Ah."


hi "Submergée par mon impressionnante virilité. Je comprends."

show emi basic_grin
with charachange


"Ça me fait gagner un sourire, au moins."


"Emi secoue la tête."

show emi basic_closedgrin
with charachange


emi "Idiot. Tu es trop sûr de toi."


hi "Bah, je suis irrésistible, je n'y peux rien."

show emi sad_shyblush
with charachange


emi "Erh, plus ou moins. J'imagine."

show emi sad_grin
with charachange


emi "Donc voilà la situation, Hisao."


emi "Je m'amuse trop avec toi, et si je veux arriver préparée aux examens, j'ai besoin d’être seule."


hi "Hé, c'est pas grave, tu sais."


"Ça semble vraiment la gêner."


"En plus, c'est seulement quelques semaines. Et on se verra toujours tous les matins et midis."


hi "On pourra juste traîner ensemble à l'école, pas de problème."


hi "Et après les examens, on ira en rendez-vous pour fêter ça, d'accord ?"

show emi basic_closedgrin
with charachange


"Emi sourit, contente de la proposition."

show emi basic_happy
with charachange


emi "Ouais, bien sûr ! Ça me paraît bien !"

show emi excited_amused_close at center
with characlose


"Comme pour marquer la fin de la conversation, elle s'approche et m'embrasse."


"Le reste de la nuit ne se passe pas à s’inquiéter pour les exams."

stop music fadeout 2.0

scene black
with dissolve



label fr_E23:

window hide None

$ renpy.music.set_volume(0.5, 0.0, channel="music")
play music music_night fadein 4.0

scene bg school_library_bw
with locationchange

nvl clear
nvl show dissolve


n "\n\nC'est bizarre à quel point Emi et moi arrivons facilement à ne pas se voir après les cours maintenant."


n "En fait, j'irais même jusqu’à dire que c'est légèrement perturbant."


n "Aussi facilement qu'on s'est mis ensemble, on arrive à se séparer sans trop de problème."


n "Bon, ce n'est pas exactement vrai."


n "On a tous les deux été un peu déprimés après notre dernière nuit ensemble."


n "Et on se voit tous les matins pour courir (et juste pour courir, je précise)."


n "Pour déjeuner, aussi. J'apprécie particulièrement de manger avec elle."


n "On a tout le temps qu'on veut pour discuter de tout ce qu'on fait à l'extérieur de l'école, tandis que les courses matinales se limitent à la course."


n "Je crois que c'est parce qu'Emi veut compenser pour nos folies dans le local."


n "Mais peu importe à quel point nous rions pendant le déjeuner, je ne peux pas m’empêcher de me sentir un peu inquiet pour elle."

nvl clear


n "\n\nElle semble plus souvent distraite, et je l'ai surprise à gigoter nerveusement plus d'une fois."


n "Je n'ai jamais pensé qu'elle était du genre à se préoccuper des examens, mais ils semblent avoir fait leur effet."


n "Même s'ils n'ont même pas encore commencé."


n "C'est juste l’échauffement, la grande respiration avant de plonger."


n "Demain, les vrais tests commencent."


n "Les vrais examens, du moins."


n "Quant à moi, je ne suis pas inquiet du tout pour les examens."


n "Je ne sais pas tellement pourquoi. Je veux dire, ils sont plutôt importants, mes notes détermineront mes chances d'entrer dans une bonne université."


n "Sérieux, si je suis trop téméraire maintenant, je pourrais condamner ma carrière académique."


n "Mais en y allant, je suis confiant sur le fait que je pourrai passer sans trop de problème."

nvl clear


n "\n\n\n\n\n\nMutou pense que j'ai tout ce qu'il faut en sciences, du moins."


n "Ou comme il dit, “La dernière chose qui devrait te causer des difficultés est ma matière, Hisao. Tes compétences sont bien au-delà.”"


n "Encore une fois, c'est Mutou qui me dit ça."


n "Ses compliments me donnent l'impression que quoi que ce soit d'autre qu'un score parfait serait décevant, ce qui fait que je m’inquiète plus que je le devrais pour l'examen."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve

scene bg school_library
with locationchange

window show


"C'est pour cette raison que je me retrouve à l'école après les cours à étudier mon manuel."


"Assez simple à réviser : quelques formules sur la vélocité, un peu de friction..."


"Une promenade de santé, comparé à mon si craint examen d'anglais. Je n'ai jamais été bon en langues..."



"Alors que je feuillette encore une fois mes notes, mon esprit commence à divaguer."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\n\nAprès la fin de ces examens, les choses deviendront plus faciles."


n "Bientôt on sera diplômés."


n "Et partis à la faculté, avec de la chance."


n "Je me rappelle ma tentative infructueuse pour savoir ce qu'Emi envisage de faire après le lycée."


n "Mmh, elle a évité le sujet plutôt habilement, si je me souviens."


n "On dirait qu'à chaque fois que j'approfondis trop un sujet, elle ne fait que dévier la conversation."


n "Ou me distrait via... d'autres façons."


n "Comme il y a quelques jours, quand Rin n'était pas là..."


n "Haha..."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide None
window show None

stop music fadeout 0.2

show yuuko happy_up
with vpunch


yu "J'ai réussi !"


"Je suis sorti de ma torpeur par le cri triomphant de Yuuko."


hi "Aah !"

show yuuko panic_up
with charachange


"Yuuko semble mortifiée par mon étonnement soudain."

play music music_happiness fadein 2.0


yu "Oh mon dieu !"

show yuuko panic_down
with charachange


yu "Je suis tellement désolée ! J'ai juste - et je ne voulais pas - et c'est juste que-"


"Alors qu'elle bégaie, je m'approche rapidement pour la calmer avant qu'elle ne s'agite trop."


hi "Oh, hé."


"Mes mots semblent inefficaces."


"Yuuko continue de s'agiter dans tous les sens."

show yuuko panic_up
with charachange


yu "Et c'est une bibliothèque et je ne devrais pas—"


hi "Doucement, calme-toi."

show yuuko cry_down
with charachange


yu "Et je montre un mauvais exemple, et maintenant je vais me faire renvoyer parce que je ne peux rien faire correctement—"


hi "YUUKO !" with vpunch

show yuuko worried_up
with charachange


"Crier semble fonctionner, bien que je m'attire la colère de quelques autres étudiants en train de faire leurs devoirs dans la bibliothèque."


"Je capte instantanément l'attention de Yuuko, comme un soldat qui vient juste d'entendre l'ordre d'un capitaine."

show yuuko neurotic_up
with charachange


yu "Désolée ! Désolée !"


hi "Calme-toi, tout va bien."


hi "Tu m'as juste un peu surpris, et c'est uniquement parce que je rêvassais au lieu d'étudier."


hi "Donc en fait, tu m'as remis en selle."


"C'est un mensonge complet. Mais ça semble marcher."

show yuuko worried_down
with charachange


"Yuuko prend une grande inspiration et a l'air d'un peu se calmer."


"Bien qu'elle continue de remuer de sa façon nerveuse habituelle."


hi "Bon, qu'est-ce qui t'a autant excitée alors ?"

show yuuko neutral_up_close
with characlose


yu "Le Monte-en-l'Air de Yamaku !"


"Yuuko arrive à contenir son intense excitation dans un chuchotement."

show yuuko closedhappy_up_close
with charachange


yu "Je crois savoir qui c'est !"

show yuuko happy_down_close
with charachange


yu "J'ai reçu un indice anonyme de son identité !"


yu "Alors j'ai fait un peu d'espionnage et je crois que l'indic avait raison !"


hi "Oh vraiment ? Et qui est ce, erh, monte-en-l'air ?"

show yuuko worried_down_close
with charachange


"Yuuko ferme la bouche, secouant fermement la tête."


yu "Nope, je ne peux pas te le dire."


hi "Pourquoi pas ?"

show yuuko worried_up_close
with charachange


yu "C'est entre le monte-en-l'air et moi."


yu "Je ne peux pas risquer que tu l'avertisses que je suis sur sa trace."


yu "Il pourrait avancer son coup et quitter la ville."


yu "Et je me retrouverais sans coupable."


"Depuis quand est-ce que Yuuko parle comme un détective vétéran ?"


hi "Je ne l'avertirai pas ! Pourquoi je m'en préoccuperais ?"

show yuuko neutral_down
with charadistant


yu "Si tu me poses cette question, alors tu n'as pas besoin de savoir."


hi "Ça ne veut rien dire, mais d'accord."


hi "Et... félicitations ?"

show yuuko closedhappy_down
with charachange


yu "Merci !"

show yuuko worried_up
with charachange


yu "Euh, pourquoi donc ?"


hi "Le euh, monte-en-l'air ?"

show yuuko smile_down
with charachange


"Yuuko hoche la tête et sourit, contente."


yu "Donc ! Tu étudies pour les examens ?"


hi "C'était ce que je voulais faire du moins. Je n'y arrive pas trop, cela dit."

show yuuko worried_down
with charachange


yu "Vraiment ? C'est parce que tu n'arrives pas à trouver un livre ?"

show yuuko panic_up
with charachange


yu "Je suis vraiment désolée !"


yu "J'avais l'intention de réorganiser les étagères depuis des semaines déjà, mais je suis toujours distraite !"


yu "Je suis tellement désolée !"


hi "Wow, attends."


hi "C'est pas ça. J'ai mon livre juste là."


"Pour prouver ce que j'avance et, avec de la chance, calmer Yuuko, je lui montre le livre en face de moi."


hi "J'ai juste un peu divagué, c'est tout."

show yuuko worried_up
with charachange


yu "C'est à cause du bruit dans la bibliothèque ?"


yu "J'essaye d’être plus sévère à propos du bruit, mais je n'arrive pas à me résoudre à crier sur les gens..."

show yuuko worried_down
with charachange


yu "Leurs vies ne sont-elles pas assez difficiles sans que je les agresse avec mon autorité ?"


hi "Non, ce n'est pas le bruit non plus, je te le promets."


hi "Je suis juste..."


"Rah, je sais même pas."


"Inquiet pour Emi."


"Inquiet pour nous."


"Inquiet de ce qui va arriver après notre diplôme."


hi "Emi est un peu bizarre, récemment."

show yuuko worried_up
with charachange


yu "Comment ça ?"


hi "Tu sais qu'on sort ensemble, hein ?"


hi "Je ne sais juste pas si on est vraiment, tu sais..."


hi "Un couple. Ou du moins je ne sais pas si on est vraiment plus que des amis."


"Bien que les amis normalement ne font pas le genre de choses qu'on fait."


"Physiquement on est un couple."


"Copulant, du moins."


hi "C'est comme si à chaque fois que je voulais en savoir plus sur elle, ou sur ce qu'elle voulait faire de sa vie, elle évitait la question."


hi "Comme l'autre jour, je lui parlais au déjeuner des écoles auxquelles je m’intéresse."


hi "Et je lui ai demandé “Tu as regardé les écoles récemment ?”"


hi "Elle hausse les épaules en réponse, dit non, et quand je lui demande pourquoi, elle me dit qu'elle ne pense pas aussi loin."


hi "J'ai demandé pourquoi elle faisait ça, et elle..."


"Je réalise soudainement ce que je suis sur le point de décrire, et décide sagement de ne pas le faire."

show yuuko neutral_up
with charachange


yu "Elle quoi ?"


hi "Erh, elle a changé de sujet."


hi "Ne voulait pas en parler."

show yuuko neutral_down
with charachange


yu "Peut-être qu'elle n'est pas à l'aise avec le sujet ?"


yu "Ou qu'elle pense juste que ça ne mérite pas d’être expliqué."


hi "Ouais, mais ce n'est pas juste ça."


hi "À chaque fois que j'essaye de découvrir ce qui la gêne, elle change de sujet aussi."


hi "C'est comme si elle aimait être avec moi, mais pas être proche de moi."


"Maintenant que je l'ai dit à voix haute, je me sens encore plus mal."


"Yuuko réfléchit à ce que je viens de dire."

show yuuko worried_down
with charachange


yu "Tu sais, j'ai l'impression que tu es plus sérieux dans cette relation qu'elle ne l'est."


"Je peux presque sentir mon estomac se tordre."


"Elle a raison."


"C'est exactement ce à quoi ça ressemble."


hi "Mais est-ce que c'est vraiment ce qui se passe ? Je veux dire..."

show yuuko panic_up
with charachange


yu "Désolée ! Je dis n'importe quoi !"


yu "Tu ne devrais pas prendre mes conseils, tu me connais à peine !"

show yuuko cry_down
with charachange


yu "Je suis juste la bibliothécaire, et je suis célibataire, alors tu peux imaginer que je ne sais pas de quoi je parle !"


hi "Non, je crois..."


hi "Je crois que tu dois avoir raison."


"Même si ça fait mal de juste l'envisager."


"Yuuko semble désespérément essayer de trouver une façon d'adoucir la chute."

show yuuko neutral_down
with charachange


yu "Hum, écoute."

show yuuko smile_down
with charachange


yu "J'ai sûrement tort, mais si tu veux savoir à quel point j'ai tort, peut-être que tu devrais juste lui parler ?"


yu "Prenez-vous du temps seuls à deux et demande-lui."

show yuuko closedhappy_down
with charachange


yu "Et ne la laisse pas changer de sujet, non plus !"


hi "Ouais, je peux peut-être faire ça."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\nOu peut-être que je devrais juste apprécier ce que j'ai."


n "On s'amuse bien ensemble, après tout."


n "Et courir avec elle est agréable, et ce qu'on fait d'autre est agréable, et parler avec elle est agréable..."


n "Est-ce que j'ai vraiment besoin de me rapprocher d'elle ? Ce que j'ai maintenant est déjà bien."


n "Mais c'est bête."


n "Je veux être plus proche d'elle."


n "Je veux être capable de l'aider par rapport à ce qui la perturbe."


n "Mais... peut-être que je devrais attendre jusqu’à ce que les examens soient finis."


n "Peut-être qu'elle ira mieux une fois que le stress sera passé."


n "Si c'est ce qui arrive, alors je n'aurai plus à m’inquiéter."


n "Mais si ce n'est pas le cas, eh bien."


n "Je devrai faire un pas à ce moment-là."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl hide dissolve
nvl clear
window show

stop music fadeout 5.0


"Je remercie Yuuko pour son conseil et retourne à ma chambre."

scene bg school_hallway2
with locationchange


"Peut-être que je serai davantage capable de me concentrer sur les études là-bas."

scene black
with dissolve



label fr_E24:

scene bg school_hallway3
with locationskip
play music music_tranquil fadein 3.0


"Je sors de la pièce après avoir fini mon examen final et soupire de soulagement."


"Comme je l'avais espéré, les examens n'étaient pas si durs. J'ai réussi à m'en sortir partout sauf pour l'examen final d'anglais."


"Mais même là c'était acceptable."


"Je me demande comment s'en est sortie Emi."


"Et aussi, comment elle va ; elle n'avait pas l'air bien du tout aujourd'hui."


"Je veux dire, elle était vraiment contente d’être sortie de son fauteuil roulant, mais elle était vraiment épuisée."


"Quelque chose lui provoque ça, et je commence à vraiment douter que ce soit juste les examens."


"Est-ce que je devrais l'interroger sur ça, cela dit ?"


"Ma torpeur est interrompue par une tape sur mon épaule."

show muto smile at center
with charaenter


mu "Tiens, Hisao."

label fr_choiceE24:
menu:
    with menueffect
    mu "Tu as une minute ?"
    "Je peux certainement lui consacrer quelques minutes.":




        return m1
    "Non, j'ai d'autres choses à faire.":


        return m2

label fr_E24a:






hi "Ouais, pas de problème, je n'ai rien de prévu."

show muto normal
with charachange


"Mutou lève un sourcil comme s'il s'interrogeait sur ce que je viens dire, et m'invite à retourner dans la classe."

hide muto
with charaexit

scene bg school_scienceroom
with locationchange

show muto normal at center
with charaenter


mu "Je voulais avoir ton avis sur quelque chose, si c'est possible."

mu "Je sais que les cours de physique n'étaient clairement pas à ton niveau..."



hi "Ne vous inquiétez pas pour ça. Le club de sciences a largement compensé."

show muto smile
with charachange


mu "Mmh, vraiment ?"

show muto normal
with charachange


mu "Bon en fait, c'est de ça dont je voulais te parler."


mu "Tu trouves que c'est une activité qui vaut le coup ? Juste pour savoir."


hi "Ben ouais, c'était une très bonne façon d'aller plus loin que ce qu'on a fait en cours. Ça valait clairement le coup."

show muto smile
with charachange


"Mutou semble vraiment apprécier ma réponse."


mu "C'est fantastique ! Exactement la réponse que j’espérais."


mu "Tu sais, Hisao, je suis content que tu sois venu. C'est toujours bien d'avoir un étudiant qui est vraiment intéressé par la matière que tu enseignes."


mu "D'une certaine façon, ça rend les autres étudiants plus faciles à gérer."


mu "Tu es un gamin brillant. Tu as glissé sur la physique comme un canard sur l'eau, ou autre chose de similaire."


hi "Euh, merci."


hi "Vous m'avez vraiment bien aidé, surtout avec cette histoire de fac."

show muto normal
with charachange


mu "Une dernière petite chose, Hisao."


mu "Un petit conseil, d'un scientifique à l'autre."


hi "Oui ?"


mu "Que fait un scientifique ?"


hi "Observer le monde autour de soi."

show muto smile
with charachange


mu "Exactement. Bien."

show muto normal
with charachange


mu "Une question simple, mais à laquelle la plupart des gens ne savent pas répondre. C'est l'essence d'un scientifique, Hisao."


mu "Nous observons ce qui est là, et essayons de le comprendre."


mu "Mais, et s'il y a quelque chose que tu ne peux pas comprendre ?"


mu "Que fait un scientifique s'il ne peut pas observer quelque chose ?"


mu "Comment, par exemple, pouvons-nous parler de quarks quand personne n'en a encore jamais vu ? Ou des trous noirs, quand les observer directement est impossible ?"


hi "Eh bien, l'équipement scientifique est assez sophistiqué..."

show muto irritated
with charachange


"Mutou semble presque irrité par ma réponse."


mu "Non, ce n'est pas ça du tout."


mu "Ce sont des outils, j'essaye de t'apprendre une philosophie."

show muto normal
with charachange


mu "Réfléchis. Si tu ne peux pas observer quelque chose directement, alors comment tu l'observes ?"


hi "Euh, en devinant ?"


mu "Comment ? Comment tu observerais le mouvement d'un quark ? Sur quoi tu te bases pour deviner ?"


"Bien sûr."


"J'aurais dû y penser plus tôt."


hi "Les choses qui sont affectées."

show muto smile
with charachange


"Mutou tape des mains et semble satisfait."


mu "Oui, exactement. Bien."


mu "Rappelle-toi ça, Hisao."

show muto normal
with charachange


mu "Si tu ne peux pas examiner quelque chose directement, c'est parce que tu regardes de la mauvaise façon."


mu "Tu dois regarder différemment si tu veux voir la vérité. Et si ça t'échappe, alors regarde ce qui se passe derrière."


mu "C'est l'essence même d’un scientifique. Nous n’arrêtons jamais de chercher pour une réponse. Ne jamais considérer qu'un dossier est clos."


mu "Observe, expérimente, et observe encore plus."


mu "Il y a beaucoup de choses qui n'ont aucun sens, Hisao. Ton travail est de leur trouver un sens."


mu "Dans tous les cas, j’espère que tu as appris ça."


hi "Je crois que je peux m'en rappeler."

show muto smile
with charachange


"Mutou sourit, satisfait."


mu "Bien. Maintenant profite de ton temps libre. Tu l'as mérité."

stop music fadeout 8.0

scene bg school_hallway3
with locationchange


"Je sors de la pièce en me sentant un peu confus."


"Comment on en est arrivés à parler de ça ?"


"Cela dit..."


"Est-ce que je m'y prends mal pour toute cette histoire avec Emi ?"


"Si elle ne veut pas me le dire, est-ce que je peux m'en sortir d'une autre façon ?"



label fr_E24b:


hi "En fait, je dois aller faire quelque chose..."

show muto normal
with charachange


mu "Ah ? Pas grave."


mu "Je voulais avoir un avis sur le club de sciences de ta part. Mais on pourra faire ça plus tard, après tout."


mu "Profite de ton temps libre, d'accord ?"


hi "Je vais faire ça, merci."


"J'aimerais vraiment discuter avec Mutou, mais j'ai d'autres choses en tête."


"Spécifiquement, ce qu'il faut faire pour Emi."


"Est-ce que je peux aller me confronter à elle juste comme ça ?"



label fr_E24c:

scene bg school_dormhisao
with locationskip


"La question continue de tourner dans ma tête après que je sois arrivé à ma chambre."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\nEt si elle s’énerve contre moi ?"


n "Et puis, et si ce n'est rien ?"


n "Si j'y vais et refuse de partir jusqu’à ce qu'elle me dise ce qui ne va pas, je ne serai pas perçu comme trop collant ?"


n "Je ne veux pas commencer une dispute ou quoi que ce soit comme ça."


n "Peut-être que je devrais laisser tomber et voir comment elle va demain avant de faire quoi que ce soit."


n "Ça serait une mauvaise chose de juste laisser passer ?"


n "Ce n'est pas comme si on n’appréciait pas la compagnie l'un de l'autre."


n "Mais aussi bizarre que ça puisse sembler, je veux vraiment... l'aider."


n "Je ne sais même pas en quoi, et s'il y a une chose pour laquelle elle a besoin d'aide."


n "Mais je le veux."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

play sound sfx_doorknock

stop music fadeout 2.0

nvl clear
nvl hide dissolve

window show


"Soudainement, un coup à ma porte me surprend."

play sound sfx_dooropen

scene bg school_dormhallway
show kenji neutral at center
with locationchange


"Je l'ouvre pour voir Kenji."


hi "Oh, c'est toi."

play music music_kenji

show kenji tsun
with charachange


ke "C'est moi ? C'est tout ?"


ke "Si tu avais idée de ce j'ai traversé, ce que j'ai fait, tu serais plus content de me voir, mec."


ke "Je veux dire, c'était un bordel du genre épique, tu-ne-me-reverras-peut-être-plus-jamais quoi."


ke "Et tu es là à la jouer comme si je venais d'acheter du lait au magasin."

show kenji happy
with charachange


ke "Tu un homme de sang froid, Hisao. Je respecte vraiment ça."


hi "Euh, merci, je crois."

show kenji neutral
with charachange


ke "C'est malin de la jouer comme ça, tu sais. Ne montrer aucune émotion."


ke "Garde tes cartes près de ta poitrine."


ke "Sauf si c'est le moment de montrer tes cartes ou si tu as de mauvaises cartes."


ke "Dans ce cas tu devrais te coucher ou récupérer tes gains."

show kenji happy
with charachange


ke "Tu comprends ?"


hi "Ouais, c'est parfaitement logique."


hi "J'en déduis que ta euh, mission s'est bien passée ?"

show kenji tsun
with charachange


ke "Woah, c'est très fouineur de ta part, tu crois pas ?"


ke "Tu ne peux pas dire ça juste comme ça ! Les choses en sont à un stade délicat !"


ke "Une mauvaise action, et BAM ! L'invasion réussit !"


hi "Je croyais que tu allais éclater la conspiration à la lumière de la raison ?"


ke "C'est plus gros que ce que je croyais ; j'ai besoin de mettre à jour mes graphiques."


ke "Et probablement de déplacer certains pions."

show kenji happy
with charachange


ke "Tu veux aider ? J'ai du whisky de... quelque part."


ke "Tu pourras me mettre au courant de ce qu'a donné ton investigation."


hi "Erh, vaut mieux pas. Je euh... suis supposé la rencontrer aujourd'hui."


hi "Je dois y aller, ne pas éveiller les soupçons."

show kenji neutral
with charachange


"Kenji hoche la tête en approbation."


ke "Tu les gardes encore près de la poitrine, hein ? D'accord mec, je respecte ça."


ke "Bonne chance."


hi "Erh, merci."

hide kenji
with charaexit

stop music fadeout 4.0


"Je vais juste me dire, dans l’intérêt de ma propre santé mentale, qu'il me souhaite bonne chance pour ma discussion avec Emi."


"Et si je louche, son analogie complète du jeu de cartes fonctionne ici."


"Il est temps de mettre cartes sur table."


"Ou voir si je peux faire en sorte qu'Emi le fasse, plutôt."


"Avec l'impression d'arriver au bout de quelque chose, je me dirige vers la chambre d'Emi."

scene bg school_girlsdormhall
with locationskip

play sound sfx_doorknock2


"Je monte trois par trois les marches de l'escalier menant à sa chambre et frappe à la porte."


emi "Q-qui est là ?"

play music music_drama fadein 8.0


"Oh. C'est étrange. Sa voix semble légèrement troublée."


hi "Hé, c'est moi. Je passe juste te voir."


emi "Hisao ?"


emi "Entre !"


"Je tourne la poignée pour ouvrir la porte et elle s’avère verrouillée."


"De plus en plus curieux."


hi "Euh, ta porte est fermée."


emi "Oh ouais, désolée. Donne-moi une minute."

show emi basic_grin:
    tworight
    xpos 0.8
    easein 0.5 tworight
with charaenter


"Après quelques minutes, Emi ouvre la porte, souriante."


emi "Désolée, j'ai dû mettre mes jambes, je faisais une sieste."


"Malgré son sourire, il y a clairement quelque chose qui ne va pas."


"Les yeux d'Emi sont légèrement rouges, on dirait qu'elle a pleuré."


hi "Pas de problème."


hi "Euh, ça va ?"

show emi sad_shy at tworight
with charachange


emi "Hein ? Ouais, je vais bien !"


hi "C'est juste qu'on dirait que tu viens de pleurer."



"Bravo Hisao. Tu es bien parti avec ça."


show emi sad_grin at tworight
with charachange


emi "Quoi ? Nan, je vais bien. Je suis juste contente de te voir."

scene ev emi_firstkiss
with flash


"Elle ponctue son affirmation par un long baiser qui continue alors que la porte se claque derrière nous."


"Je sais ce qu'elle veut faire maintenant, et je suis tout aussi douloureusement conscient d’à quel point j'ai envie aussi, mais..."

scene bg school_dormemi at left
show emi excited_amused_close at center
with locationchange


"J’interromps le baiser avec une maîtrise de moi qui m'assassine presque."


hi "Hé, attends."

show emi basic_confused_close
with charachange


"Les yeux d'Emi se plissent de confusion."


emi "Hein ? Attendre pour quoi ?"


hi "Il faut qu'on parle."

show emi sad_grin_close
with charachange


emi "Je suis pas censée être celle qui dit ça ?"

show emi sad_shy_close
with charachange


emi "Et ce n'est pas toujours annonciateur de mauvaise nouvelle ?"


"Elle n'a pas tort."


"C'est généralement la phrase annonciatrice d'une rupture."


"Ou le prélude à une dispute."


hi "Peut-être que ça peut être une bonne chose, cette fois."


hi "Erh, j’espère, du moins."

show emi sad_shyblush_close
with charachange


emi "Oh... Oh."

show emi basic_grin_close
with charachange


emi "Est-ce qu'on peut au moins aller sur le lit ? C'est mon premier jour de retour sur ces trucs, je me réadapte encore."


show emi basic_closedgrin_close
with charachange


emi "En plus l'infirmier a dit que je devrais essayer de les porter moins souvent, vu que courir avec est si éprouvant."


hi "Je peux rien dire contre ça."


"C'est un piège, on le sait tous les deux, et nous nous en moquons tous les deux."


"D'un autre côté, ce n'est pas facile de s’énerver quand on est dans le lit avec la personne qu'on apprécie tant, alors peut-être que c'est aussi le but."

hide emi
with charaexit

show bg school_dormemi at right
with charamove

show emi basic_grin_close:
    center
    ypos 1.0
    easein 0.5 ypos 1.1
with charaenter


"Je pose les jambes d'Emi à côté du lit et m'assois à côté d'elle, passant un bras autour de ses épaules."


"Nous apprécions pendant quelques minutes de pouvoir être dans cette position, en silence."


"Et, bien sûr, j'ai besoin de gâcher le moment en ouvrant la bouche."


hi "Écoute, je sais que... que tu vis un passage difficile en ce moment."


hi "Et je veux t'aider."


hi "Je pensais que c'était juste les examens qui te pesaient, mais maintenant je viens dans ta chambre et tu as pleuré, et ça me tue de voir ça."


hi "Mais je ne peux rien faire si tu ne me parles pas."

show emi basic_closedgrin_close:
    ypos 1.1
with charachange


emi "Je te l'ai dit, je vais bien."


hi "Non c'est faux. Il est évident que quelque chose te ronge."


hi "Tu peux me le dire, tu sais."


"Il y a une légère tension qui apparaît dans la voix d'Emi."

show emi sad_shy_close
with charachange


emi "Pourquoi est-ce que le fait que je dise que je vais bien n'est pas suffisant ?"

show emi sad_annoyed_close
with charachange


emi "Tu es inquiet, je comprends ça. C'est bien."


emi "Mais je vais bien, et ce n'est rien dont tu doives te préoccuper."


hi "Ne pas dormir et être encore plus absente mentalement que Rin n'est pas ma définition “d'aller bien”."


hi "J'ai juste... Je veux juste aider."


emi "Uh huh."


hi "Ouais, je n'aime pas te voir comme ça."


hi "Je veux que tu sois heureuse, tu comprends ?"

show emi basic_annoyed_close
with charachange


"J'ai l'impression que c'est mal sorti, parce qu'Emi me fixe d'un regard glacial."


emi "Alors tu veux me réparer, Hisao ?"


"Elle est clairement en train de s’énerver maintenant."

show emi sad_grit_close
with charachange


emi "Tu veux foncer sur ton cheval de bataille blanc et sauver la princesse ?"


emi "Arrêter les cauchemars, les douleurs des membres fantômes ?"

show emi sad_angry_close
with charachange


emi "Retrouver ce qui a été perdu ?"

show emi sad_depressed_close
with charachange


"Sa voix s’élève encore, et les larmes commencent à couler."


emi "Et bah tu ne {b}peux pas{/b}."

show emi sad_pout_close
with charachange


emi "Personne ne le peut."


emi "Personne ne le fera."


"Je suis tellement abasourdi par son soudain assaut verbal que je reste silencieux."


"Aucun de nous deux ne dit quoi que ce soit pendant un moment."


"Je suis surpris qu'Emi resserre son emprise sur moi plutôt que de me repousser."


"Après une profonde respiration, elle commence à parler de nouveau."

show emi sad_shy_close
with charachange


emi "Écoute, je suis désolée."

show emi sad_depressed_close
with charachange


emi "C'est juste... il y a ces cauchemars."


emi "Sur l'accident."


"Ah. L'accident. J'aurais dû le savoir."



"Ça lui a pris ses jambes après tout, mais elle n'en parle jamais, bien sûr."

show emi sad_pout_close
with charachange


emi "Et je m'en accommode tout à fait bien généralement, parce que je peux courir."


emi "Courir me vide la tête comme rien d'autre ne peut le faire."


emi "Je n'ai pas à m’inquiéter d'autre chose pendant que je cours."


emi "Je me concentre juste sur ma respiration et sur le rythme."


emi "C'est plus facile comme ça. La vie est plus facile comme ça."

show emi sad_shy_close
with charachange


emi "Juste continuer d'avancer, tu sais ? Rien d'autre n'importe, juste tourner au prochain virage."


emi "Et puis il y a la prochaine courbe, et la prochaine, et la prochaine, jusqu’à ce que je ne puisse plus continuer, ou réfléchir, ou faire quoi que ce soit d'autre que ralentir et marcher jusqu’à ce que je reprenne mon souffle."


emi "Après quelque chose comme ça, rien d'autre ne compte."

show emi basic_annoyed_close
with charachange


emi "Mais je suis restée coincée dans ce foutu fauteuil roulant pendant trop longtemps. Alors pas d'échappatoire."

show emi sad_shy_close
with charachange


emi "Aujourd'hui ça a juste un peu débordé."


hi "Tu aurais pu m'en parler, tu sais."


hi "Tu n'avais pas à subir ça toute seule."

show emi sad_grin_close
with charachange


"Emi sourit tristement, comme si elle essayait d'expliquer à un enfant que le feu brûle tout."


emi "Si, je le devais. Et je le dois."


hi "Mais pourquoi ?"


hi "Pourquoi tu dois continuer de subir ça toute seule ?"


hi "Pourquoi tu ne peux pas me faire suffisamment confiance pour me laisser t'aider ?"


"Encore ce sourire."

show emi excited_amused_close
with charachange

show emi sad_grin_close
with charachange


"Emi se penche et me fait un bisou sur la joue, d'une façon presque maternelle."


"Elle garde sa bouche proche de mon oreille, et m'avoue une chose."

show emi sad_shy_close
with charachange


emi "Parce que, Hisao."


emi "On m'a déjà arraché une fois tout ce que j'avais."

show emi sad_depressed_close
with charachange


emi "Je ne sais pas ce que je ferais si ça arrivait encore une fois."


"Elle s’arrête, comme si elle n'était pas certaine de devoir continuer."


"Je peux sentir mes tripes qui se retournent."


"Elle continue."

show emi sad_shy_close
with charachange


emi "Alors je ne peux pas compter sur toi."


emi "Ou sur l'infirmier."


emi "Ou qui que ce soit d'autre."

show emi sad_pout_close
with charachange


emi "Juste moi."


emi "C'est comme ça que ça doit être."


"Ayant fini son petit discours, elle baisse les yeux et se couvre la bouche avec le dos de la main."


"La conversation est clairement terminée. Je cherche quelque chose à dire, mais ne trouve rien."


hi "Je..."


hi "Peut-être que je devrais y aller."


hi "J'ai des... trucs."


"Emi ne relève même pas les yeux."


"Elle semble fatiguée, ou soulagée."


"Je ne peux pas savoir clairement."


emi "D'accord, Hisao."


emi "Va t'occuper de ces trucs."


emi "Je te vois demain."

hide emi
with charaexit

with Pause(0.2)

show bg school_dormemi at left
with charamove


"Je sors du lit et me dirige vers la porte, m’arrêtant devant."


hi "Dis, Emi..."

show emi sad_shy at tworight
with charaenter


emi "Ouais ?"

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\nIl y a un millier de choses que je voudrais dire."


n "Je suis trop confus pour en sortir une seule, bien sûr."


n "Après avoir admis qu'elle ne me laissera jamais être trop proche, j'ai l'impression que {b}mon{/b} monde vient de m’être arraché."


n "Qu'est-ce qui s'est passé dans cet accident ?"


n "Je sais qu'elle a perdu ses jambes, mais ça n'a jamais semblé la troubler."


n "Qu'est-ce qui s'est passé ?"


n "Qu'est-ce qui fait tellement peur à une fille pour qu'elle n'accepte pas d'aide, même de la part de quelqu'un qu'elle aime ?"


n "Je ne sais pas."


n "\nMais je veux savoir."


n "Je veux tellement savoir, que le fait qu'on me refuse la réponse me fait l'effet d'un coup de couteau dans le ventre."

$ renpy.music.set_volume(1.0, 1.0, channel="music")

nvl clear
nvl hide dissolve
window show


emi "Hisao ?"


emi "Tu disais ?"


"Je me tiens toujours devant la porte."


hi "...Rien."


hi "Laisse tomber."

scene bg school_girlsdormhall
with locationchange

play sound sfx_doorclose
stop music fadeout 6.0


"Et je ferme la porte."


"Et je parcours le couloir."


"Descends les escaliers."

scene bg school_dormext_full_ni
with locationskip


"Passe la porte."


"Dans le noir."

scene bg school_dormhisao_ni
with locationskip

play music music_night fadein 1.0


"D'une façon ou d'une autre, j’erre jusqu’à arriver à ma chambre. Mon cerveau fait du un kilomètre-heure, tournant au ralenti."

window hide
nvl clear
nvl show dissolve


n "\n\nJe ne sais pas comment gérer ça."


n "Je pensais qu'avancer était une bonne chose."


n "Arrêter de rester dans un passé que je ne peux pas changer. Vivre dans le présent et regarder vers le futur."


n "\n\nAprès tout... ça avec Emi, je ne sais plus maintenant."


n "Elle disait la vérité. C'est plus simple de juste regarder au prochain virage, ignorant le chemin parcouru."


n "Pas d’inquiétudes pour l'adversaire laissé derrière. Aucune importance les spectateurs sur les côtés."


n "Et malheureusement, pas le temps de s'occuper d'un coéquipier qui est un peu en retard."

nvl clear
nvl hide dissolve
window show


"Je me laisse tomber sur le lit, regardant mon plafond comme si les réponses y étaient inscrites."


"Mais ce n'est pas le cas, bien sûr."

window hide
nvl clear
nvl show dissolve


n "\n\n\n\n\nElle fuit littéralement quelque chose - mais n'ai-je pas fait la même chose, faisant de mon mieux pour oublier mon hospitalisation ?"


n "Je vais mieux, mais ma santé ne va pas miraculeusement s’améliorer."


n "\nEmi doit gérer deux jambes à la place d'un cœur en moins, mais elles ne vont pas miraculeusement réapparaître non plus."


n "\nPeut-être qu'on ne peut pas aller mieux que ça."

nvl clear
nvl hide dissolve
window show


"La pièce devient de plus en plus sombre, jusqu’à ce que je ne puisse plus vraiment discerner le plafond."



label fr_E25:

scene bg school_dormhisao
with shorttimeskip


"Le matin arrive bien trop vite, talonnant une nuit sans sommeil."


"C'est comme ça qu'Emi a passé ses nuits récemment ?"


"Regardant le mur, ou le plafond. Essayant d’arrêter de penser à ce qui la perturbe."


"Elle, dans mon cas."


"Ce sentiment de gêne dans mon estomac est toujours là."

window hide
nvl clear
nvl show dissolve


n "\n\n“Je ne peux pas compter sur toi.”"


n "\nDes mots dits si facilement."


n "Presque comme si elle me taquinait, ou me châtiait pour avoir suggéré que la terre était plate."


n "\n“C'est comme ça que ça doit être.”"


n "\nLa façon dont ça doit être est nulle."


n "Je me sens si mal que j'ai presque décidé de ne pas aller courir."


n "Ça serait idiot de faire ça. Ce n'est pas quelque chose que je dois faire juste pour la voir."


n "D'accord, c'était la raison d'origine, mais c'est quelque chose de plus maintenant."

nvl clear


n "\n\n\n\nJ'ai commencé à apprécier de courir tout court."


n "Il existe de pires façons pour garder la forme, après tout."


n "Je n'aurais jamais pensé que je dirais ça après un peu plus d'une semaine, mais—"


n "\nJe me sens beaucoup mieux après avoir couru, comme si peu importait ce que j'allais faire de ma journée, j'avais au moins fait une chose."


n "Ça me réveille, aussi. Et Emi elle-même dit que courir lui vide toujours la tête. Peut-être que ça aidera à vider la mienne."


n "\nJ'espère."

nvl clear
nvl hide dissolve

scene bg school_track
with locationskip

window show


"Le matin est tiède et clair, si ce n'est légèrement humide. L'été s'annonce."


"Emi est déjà en train de s'étirer quand j'arrive, et me salue avec un sourire et un geste de la main."

show emi basic_closedgrin_gym at center
with charaenter


emi "Salut, Hisao !"


"La voir si joyeuse est comme recevoir un coup de pied à l'entrejambe."



"Comment est-ce qu'elle peut être si joyeuse après hier ?"

show emi excited_amused_gym_close
with characlose


"Je lui fais un petit geste de la main et suis surpris de la voir me serrer dans ses bras."

show emi sad_shy_gym_close
with charachange


emi "Hé, à propos d'hier."


"Et voilà."

stop music fadeout 1.0

show emi basic_grin_gym_close
with charachange


emi "Je voulais te remercier."

show emi excited_happy_gym_close
with charachange


emi "J'ai réussi à dormir un peu pour la première fois depuis un long moment, et je crois que c'est grâce à notre conversation."

show emi basic_closedgrin_gym_close
with charachange


emi "Alors, merci."

play music music_rain fadein 4.0


"Comment est-ce qu'elle peut bien dormir après notre discussion ?"


"Elle m'a dit qu'elle ne deviendrait pas plus proche de moi qu'on ne l'est déjà."


"Et ça l'a aidée à bien dormir ?"


"Mais sérieux, c'est quoi ça ?"


"Emi n'a soit pas remarqué ma perplexité, ou a choisi de l'ignorer."


"Je ne sais plus avec elle maintenant."


hi "Oh, pas de problème. Content d'avoir pu aider."


"Le venin qui menace de se glisser dans ma voix est contrôlé pour l'instant, mais je pense que je ferais mieux de me mettre à courir maintenant avant de faire quoi que ce soit de stupide."

scene bg school_track_on
with locationchange


"Emi semble tout autant avoir envie de commencer, et peu après nous courons sur la piste."


"Je peux voir qu'elle se sent plus relaxée."

scene ev emi_run_face:
    truecenter
    zoom 1.0 subpixel True
    acdc_warp 20.0 zoom 1.1
with flash


"Sa course est revenue aux mouvements gracieux que je me rappelle avoir vus la première fois où je l'ai regardée."


"C'est un contraste énorme par rapport à la façon presque brutale dont elle s'est forcée autour de la piste ces derniers jours."


"Notre discussion semble vraiment l'avoir aidée."


"Dommage que ça ne m'ait pas aidé moi."


"Je me remets dans le rythme de la course, repensant à l'époque où je ne pouvais pas me permettre de penser à autre chose qu'à mes jambes en mouvement et ma respiration soutenue."


"Ces jours semblent finis."


"Du moins pour les premiers tours."

scene bg school_track_running
with Dissolve(2.0)


"Énervé par le manque de succès que j'ai à essayer de me vider la tête, j’accélère le rythme."


"Ah, il y a la sensation de brûlure dans mes jambes."


"La respiration ressort en râles, mon cœur frappant dans ma poitrine. Je dois faire attention à ça."


"Mais il semble s’être renforcé ; je peux le sentir pomper le sang dans mes veines."


"Le son fait écho dans mes oreilles, mais au lieu d’être paniqué comme je l'étais ce jour dans la neige, je suis au contraire rempli d'allégresse."


"Oui, ça marche ! Mon cœur, cette faille fatale qui m'a fait atterrir ici, s'est amélioré."


"Je suis capable de continuer d'avancer maintenant, et peut-être qu'un jour je serai capable d’arrêter de m'inquiéter autant."


"Pour l'instant, ça n'a aucune importance de n'avoir aucune idée de quoi faire pour Emi et moi."


"Tout ce qui compte est que mes bras et jambes continuent à s'alterner de concert."


"Rien d'autre."

show bg school_track_on
with locationchange


"Alors que j'atteins la ligne d'arrivée, je me rappelle que courir aide vraiment, bien que ce ne soit pas autant que je le voudrais."


"Je me sens mieux, et alors que je marche quelques tours pour me refroidir, je commence à me rappeler la nuit dernière d'une manière moins émotionnelle."


"Emi veut que je reste à distance d'elle."


"Je n'arrive pas à m'y résoudre."


"Il doit y avoir une autre façon, une possibilité que je n'ai pas envisagée."


"Même si je ne sais pas ce que c'est."


"Zut, je me sentais presque optimiste."

show emi excited_joy_gym at center
with charaenter


emi "Bien joué, Hisao ! Tu t'es vraiment amélioré !"


"Bien joué. C'est tout ce que je peux espérer pour le moment, hein ?"


"Félicitations, Hisao. Tu es pathétique."


"Il faut que je change mon attitude."


hi "Bah, tu sais, je suis génial après tout."


"Et pourtant je continue de dire des choses que je ne pense pas."


"Bientôt je serai aussi doué qu'Emi pour cacher mes problèmes."

show emi basic_closedgrin_gym
with charachange


emi "C'est ce que je pense aussi."


"Pourquoi est-ce qu'elle me fait ça ? Dire quelque chose comme ça avec une réelle affection dans la voix qui me fait chavirer le cœur ?"


"Elle ne le pense pas. Elle ne peut pas."


"Je dois être moins doué que je le pense, parce qu'Emi me regarde avec attention."

show emi basic_confused_gym
with charachange


emi "Hé, tu te sens bien ?"

show emi basic_hes_gym
with charachange


emi "Peut-être qu'on devrait aller voir l'infirmier, hein ?"


hi "Ouais, je voudrais pas te claquer dans les pattes."


"Emi semble un peu choquée par mon ton aigre."

show emi basic_shock_gym
with charachange


emi "Ne dis pas de choses comme ça !"

show emi sad_shy_gym
with charachange


emi "Tu l'as déjà fait une fois, tu sais."


"Pourquoi est-ce qu'elle agit aussi affectueusement ?"


"Ça ne l’intéresse pas vraiment, elle a été très claire là-dessus."


"Mais malgré tout ça, je me retrouve à m'excuser, même si je ne devrais pas. Même si elle est très probablement juste en train de jouer un rôle."


hi "Désolé, hein."


hi "Allez, allons voir l'infirmier."


"Je n'arrive pas à me calmer durant tout ce temps."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\n\n\nÀ chaque fois que j'ai l'impression d'avoir réussi à outrepasser ce qui est arrivé la nuit dernière, Emi fait quelque chose ou dit quelque chose qui me témoigne de l'affection, et je me retrouve à la case départ."


n "L'image de la fin de notre conversation me hante."


n "C'est comme un coup de couteau final qui me laisse dépossédé de l'espoir qu'Emi et moi puissions être plus que ce que nous sommes déjà."


n "Et qu'est-ce qu'on est maintenant ? À peine plus que des amis qui baisent."


n "Ce n'est pas comme si je n’appréciais pas le temps que je passe avec elle, je l'ai déjà dit l'autre jour."


n "J'étais même sur le point de ne rien lui dire, juste me mettre en selle et laisser les choses avancer, hein ?"

stop music fadeout 2.0

nvl clear
nvl hide dissolve

scene bg school_nursehall
with shorttimeskip

window show


"Avec cette pensée en tête, je me retrouve devant le bureau de l'infirmier, ruminant toujours tandis qu'il vérifie comment va Emi."


"Emi bondit hors de son bureau, me fait un bisou, et part telle une fusée, vers les douches je présume."


"Pendant ce temps, l'infirmier m'invite dans son bureau pour notre vérification rituelle."

$ renpy.music.set_volume(1.0, 0.0, channel="music")
play music music_nurse fadein 0.5

scene bg school_nurseoffice
show nurse neutral at center
with locationchange


nk "Un problème aujourd'hui ?"


hi "Nan. J'ai même poussé un peu plus que d'habitude aujourd'hui, et j'ai réussi à le gérer."

show nurse grin
with charachange


nk "C'est étonnamment risqué de ta part, Hisao."


nk "Tu traînes trop avec Emi, elle déteint sur toi, ce qui n'est pas forcément une bonne chose."


"À la mention du nom d'Emi, et malgré mes efforts pour me contrôler, je me retrouve à froncer les sourcils, contrarié."

show nurse fabulous
with charachange


nk "Eh bien, voilà qui est nouveau."

show nurse neutral
with charachange


nk "La dernière fois que j'ai vérifié, ta réponse habituelle à la mention du nom d'Emi était un sourire, pas un froncement."

show nurse concern
with charachange


nk "Qu'est-ce qui s'est passé exactement entre vous deux ? Parce qu'Emi ne semble pas réagir pareil que toi."

show nurse neutral
with charachange


nk "Elle semblait bien plus relaxée qu'elle n'a pu l’être depuis plusieurs semaines, ce qui est inhabituel de sa part à ce moment de l'année."


hi "Comment ça ?"

show nurse fabulous
with charachange


nk "De quoi ?"


hi "Pour “ce moment de l'année.” Je n’arrête pas d'essayer de trouver ce qui la perturbe, mais elle se referme dès que j'aborde le sujet."


hi "Et la nuit dernière, elle a dit—"

show nurse neutral
with charachange


nk "Laisse-moi deviner. Elle ne te le dira pas, parce qu'elle dit qu'elle ne peut pas te faire confiance ?"


nk "Et maintenant tu es brisé, parce que tu penses que tous les deux vous étiez plus qu'elle ne pense que vous êtes, c'est ça ?"


hi "Euh, plus ou moins."


hi "Mais comment vous savez ça ?"

show nurse grin
with charachange


nk "Hisao, je suis l'infirmier. C'est mon travail de connaître ces choses."

show nurse neutral
with charachange


nk "En plus, je connais Emi depuis assez longtemps pour savoir qu'elle essayerait de faire quelque chose comme ça, ça lui ressemble bien."


"Il dit ça d'une manière semi-affectueuse, semi-frustrée qui semblerait plus appropriée s'il avait une cigarette pendue aux lèvres."


"En fait, il semble faire de même avec un stylo."

show nurse fabulous
with charachange

label fr_choiceE25:
menu:
    with menueffect
    nk "Écoute, je peux te donner un conseil ?"
    "Bien sûr, pourquoi pas ?":




        return m1
    "Non, ce n'est pas mon problème.":


        return m2


label fr_E25a:






"Qu'est-ce qu'a dit Mutou hier ?"


"Si je ne peux pas observer quelque chose, alors je dois observer ce qui est autour."


"Ça vaut le coup d'essayer."


"L'infirmier connaît Emi mieux que moi, je vais tenter le coup."


hi "Bien sûr, je suis ouvert aux propositions."


hi "Honnêtement, je suis un peu perdu."


hi "Je n'ai aucune idée de comment gérer ça."

show nurse grin
with charachange


nk "Je n'aurais jamais remarqué."


"Il sourit en disant ça, je crois qu'il se moque."

show nurse neutral
with charachange


nk "Donc, voilà le topo : Emi est... têtue."

show nurse grin
with charachange


nk "Tu devrais savoir ça depuis le temps, et si tu ne le sais pas, alors tu es assez peu observateur, mais je vais t'accorder le bénéfice du doute."


hi "Comme c'est aimable."

show nurse neutral
with charachange


nk "Bref, si elle a décidé qu'elle ne voulait pas parler de ce qui est arrivé, alors elle ne parlera pas de ce qui est arrivé."


nk "Elle a dit quelque chose sur ce qui l’embêtait ? Même un indice ?"


hi "Ben, elle a dit qu'elle faisait des cauchemars sur l'accident..."

show nurse fabulous
with charachange


nk "Vraiment ? Tu fais des progrès alors. C'est bien."

show nurse neutral
with charachange


nk "Bon, je pense que je peux te renseigner un peu sans violer ma politique stricte de non-ingérence si ça permet qu'Emi arrête de prendre des décisions stupides."

show nurse concern
with charachange


nk "C'est bientôt l'anniversaire de son accident."


nk "Elle déprime à ce moment-là, parce que c'était un événement très traumatisant, vu ce qu'elle a perdu."


hi "C'est l'autre truc. Elle agit comme si elle avait perdu plus que ses jambes. Qu'est-ce qui s'est passé ?"

show nurse fabulous
with charachange


nk "Woah ! Nope, je ne te répondrai pas. Tu devras demander à quelqu'un d'autre pour ça, parce que c'est une boîte de Pandore que je ne suis pas prêt à ouvrir."

show nurse neutral
with charachange


nk "Si Emi veut que tu saches, elle te le dira en temps voulu."


nk "Tu dois être patient, c'est tout."


hi "Pourquoi est-ce que vous m'aidez pour tout ça ?"

show nurse grin
with charachange


nk "Parce que tu es bien pour elle. Elle te fait confiance, même si elle ne le pense pas."


nk "Et tu es la personne qui, dans cette école, a le plus de chance de l'aider à ce moment de l'année."

show nurse neutral
with charachange


nk "Elle n'acceptera pas mon aide, mais elle pourra accepter la tienne si tu ne foires pas."

show nurse fabulous
with charachange


nk "Alors ne foire pas, d'accord ?"



label fr_E25b:


"Conseil ? À quel propos ? Je ne crois pas qu'il y ait quoi que ce soit que je puisse faire de toute façon."


hi "Pas vraiment. Je ne crois pas qu'il y ait quoi que ce soit que vous puissiez dire pour aider."

show nurse neutral
with charachange


nk "On ne sait jamais, Hisao."


hi "Non, je crois que j'en ai une assez bonne idée."


hi "Emi est juste têtue sur certaines choses, et ça m’embête, mais je ferai avec."


hi "Ne vous inquiètez pas pour nous."

show nurse concern
with charachange


"L'infirmier ne semble pas me croire, mais hausse les épaules."


nk "Fais à ta façon p'tit."



label fr_E25c:

$ renpy.music.set_volume(0.3, 0.0, channel="sound")
play sound sfx_hammer


"J'ouvre la bouche pour répondre mais quelqu'un frappant à la porte m’interrompt."


emi "Hé, vous êtes toujours là-dedans ?"

show nurse grin
with charachange


nk "Un moment, Emi."


nk "Laisse-nous une seconde pour remettre nos pantalons."

$ renpy.music.set_volume(1.0, 0.0, channel="sound")
play sound sfx_doorslam

show emi invis:
    tworight
    xpos 1.0
with None

show bg school_nurseoffice at bgleft
show nurse grin at twoleft
show emi basic_annoyed_gym at tworight
with dissolvecharamove


"La porte s'ouvre dans une explosion et Emi fusille l'infirmier du regard."


emi "Salaud."

show nurse fabulous
with charachange


nk "Je ne voulais pas te donner de faux espoirs."


hi "Hé, vous pouvez... me laisser en dehors de ça ?"


hi "Bref, quoi de neuf, Emi ? Tu as oublié quelque chose ?"


"Je prends un ton joyeux avec elle."


"Pas besoin de l’embêter pour rien. On peut être deux à jouer à “tout va bien”."

show emi sad_grin_gym at tworight
with charachange


emi "En fait, j'ai oublié de te demander quelque chose."


hi "Ah ? Quoi donc ?"

show emi basic_happy_gym
with charachange


emi "Tu veux venir avec moi jusque chez moi ?"

show emi basic_closedgrin_gym
with charachange


emi "Ma mère fait le dîner, et je me suis dit que tu voudrais peut-être te joindre à nous."

show nurse grin
with charachange


nk "Eh bien, avec plaisir."

show emi basic_closedgrin_gym:
    parallel:
        "emi excited_proud_gym" with Dissolve(0.2, alpha=True)
    parallel:
        ease 0.2 xpos 0.6
        ease 0.2 tworight
with Pause(0.5)


"Emi frappe joyeusement l'infirmier dans le bras."


emi "Pas toi, idiot. Tu es déjà venu la semaine dernière."

show emi sad_grin_gym at tworight
with charachange


emi "Je parlais à Hisao."

show nurse neutral
with charachange


nk "Oh ? Comme c'est intéressant ! Rencontre avec la mère !"


hi "J'adorerais y aller avec toi, Emi. Merci."

show nurse fabulous
with charachange


"L'infirmier lève un sourcil, mais ne dit rien."


emi "Super ! Je serai dans ma chambre, passe après t’être lavé et changé et on ira prendre le bus !"


hi "Ça me semble bien. À tout à l'heure !"

stop music fadeout 2.0

show emi excited_amused_gym_close
with characlose


"Cette fois, c'est moi qui me penche pour un bisou rapide avant de me précipiter à ma chambre."

scene bg school_dormhisao
with locationskip


"Quel déroulement intéressant."


"Peut-être qu'on devient plus proches après tout."


"Peut-être qu'Emi est finalement prête à s'ouvrir un peu."


"Ou peut-être qu'elle est juste polie, et qu'un repas gratuit semble une bonne façon de s'excuser pour la veille."


"Super. Maintenant je ne sais pas si je dois être excité, nerveux, ou déprimé."


"J'opte pour une combinaison des trois et file sous la douche."

scene black
with dissolve

$ suppress_window_after_timeskip = True



label fr_E26:

window hide None

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_businterior fadein 2.0

scene ev busride
with locationchange

nvl clear
nvl show dissolve


n "\n\n\nJe ne pense pas trop aimer prendre le bus."


n "En fait, je suis assez sûr de moi à propos de cette affirmation."


n "Ça remue beaucoup, et ça a une drôle d'odeur, et on peut sentir chaque bosse sur la route."


n "Je n'ai pas vraiment hâte de le prendre."


n "\nEn plus les jambes d'Emi n’arrêtent pas de faire un bruit de métal qui attire l'attention de tout le monde dans le bus."


n "Elle est encore en short, et elle a des longues chaussettes sur ses prothèses pour qu'elles n'aient pas l'air trop fausses."


n "Mais ça n’empêche pas les regards bizarres à chaque fois que ses jambes s'entrechoquent."

nvl clear


n "\n\n\nJe change nerveusement de position sur mon siège, et Emi lève un sourcil interrogateur."


n "Elle ne semble pas se préoccuper des regards ; soit ça, soit elle ne remarque même pas que les gens regardent."


n "Je suis sûr qu'elle a eu son lot de regards curieux auparavant. Après un certain moment, je doute qu'elle s'en rende compte tout court."


n "\n\nPas qu'elle me le dirait si je lui demandais, de toute façon."


n "Un autre fait est que je ne suis pas seulement installé inconfortablement dans ce bus."


n "J'ai du mal à accepter le fait qu'Emi semble essayer de se rapprocher de moi en même temps qu'elle me repousse."

nvl clear



label fr_E26a:


n "\n\n\nL'infirmier a dit qu'elle me faisait confiance, même si on ne le dirait pas."


n "Mais je ne suis pas sûr de pouvoir faire confiance à l'infirmier."


n "Il est protecteur avec Emi, tout comme je suis protecteur avec Emi, et il est probable que je dirais quelque chose de gentil sur elle si quelqu'un me le demandait."


n "\nPeut-être qu'il fait juste ça."


n "\nPourtant, il y avait quelque chose quand il avait l'air honnêtement surpris qu'Emi m'invite chez elle."


n "Peut-être que la nuit dernière a aidé plus que je le pensais, mais je suis toujours inquiet."

label fr_E26b:

stop ambient fadeout 12.0

nvl clear


n "\n\n\nRencontrer les parents est une étape importante, hein ?"


n "Non pas que je n'ai pas déjà rencontré la mère d'Emi, mais c'était en tant que connaissance."


n "Maintenant ça sera en tant que petit ami d'Emi, avec tout ce que ça sous-entend."


n "Je peux sentir mon cœur battre dans ma poitrine, un écho de cet après-midi enneigé que je pourrais croire appartenir à une autre vie."


n "Sauf que là, je n'avais aucune idée de ce qui se passait ; je n'avais également aucun médicament pour m'aider à empêcher les choses de devenir hors de contrôle."


n "J'ai parcouru un long chemin en terme de santé physique, et pour la seconde fois aujourd'hui j'ai l'impression que je serai capable de vivre normalement maintenant, ou au moins aussi normalement que possible."


n "\nMaintenant si je pouvais gérer ma relation amoureuse de la même façon que j'ai géré mon cœur, je serais en super forme."

stop ambient fadeout 1.5

window hide None

nvl clear
nvl hide dissolve

scene bg city_street4
show emicas smile_close at center
with shorttimeskip

$ renpy.music.set_volume(0.2, 0.0, channel="ambient")
play ambient sfx_traffic fadein 2.0

window show


emi "Bon, nous y voilà."

play music music_soothing fadein 2.0


"Emi m'attrape la main dès que nous sommes descendus du bus. Elle commence à marcher presque immédiatement."

show emicas wink_up_close
with charachange


emi "Allez, il y a quelques pâtés de maisons à traverser jusqu’à chez moi."


hi "Quoi ? Oh, d'accord."

scene bg city_alley
with locationchange

stop ambient fadeout 12.0


"Je suis Emi dans la rue, observant son rythme confiant."


"Elle va assez vite pour une simple marche."


"Elle doit être anxieuse après tout."


hi "Donc, ta mère fait ce genre de choses souvent ?"

show emicas neutral_close at center
with charaenter


emi "Nan, pas trop fréquemment. Elle n'est pas trop du genre à jouer les hôtesses."


hi "Ah bon ?"

show emicas awayfrown_close
with charachange


emi "Ouais, c'est toujours mon père qui la poussait pour qu'il y ait des gens qui viennent."


"Cette soudaine référence à son père me prend par surprise."


"Et d'après l'expression sur le visage d'Emi, je ne suis pas sûr qu'elle voulait le mentionner. Je crois qu'elle n'en a parlé qu'une seule fois."


"Tout ce dont je me rappelle est que la mère d'Emi m'a dit qu'il n'était plus là."


hi "Oh ? Ta mère préfère la solitude ?"

show emicas happy_up_close
with charachange


"Emi rit, soit en soulagement du fait que je n'ai pas parlé de son père ou parce que ma phrase était vraiment drôle."


emi "Pas du tout ! C'est à cause d'elle que je suis aussi aussi extravertie, tu sais."

show emicas closedsmile_close
with charachange


emi "C'est juste qu'elle préfère être une invitée plutôt qu'une hôtesse ; c'est moins stressant comme ça, d'après ce qu'elle dit."


hi "Elle n'a clairement jamais eu à rencontrer la mère de sa petite copine lors d'un dîner."


"Emi rit encore et répond d'un ton taquin."

show emicas wink_close
with charachange


emi "Nerveux, Hisao ?"

show emicas smile_close
with charachange


emi "Tu ne devrais pas, tu sais ! Ce n'est pas grand-chose ! Juste un dîner chez moi, c'est tout !"


hi "Ouais, mais tu as déjà ramené un petit copain chez toi avant ?"


"J'avoue que je suis vraiment curieux de connaître la réponse."


"Je connais très peu du passé sentimental d'Emi - je ne sais même pas si elle a eu d'autres relations."

show emicas awayfrown_close
with charachange


emi "Non, effectivement."

show emicas frown_close
with charachange


emi "Eh bah, ça représente peut-être quelque chose d'important après tout."


hi "Oh bien, maintenant je me sens deux fois plus nerveux."


"Quoique, pour dire la vérité, je suis assez content d'entendre que je suis le premier."


"Peut-être qu'on a quelque chose de spécial après tout."

stop ambient
stop music fadeout 10.0

scene bg emi_houseext
with locationchange

play sound sfx_hammer


"Rassuré par cette nouvelle pensée, je réussis à considérablement me calmer jusqu’à ce que nous arrivions juste devant la porte de la maison d'Emi et qu'elle frappe."

show emicas grin_up at center
with charaenter


emi "Hé, maman, ouvre ! On est là !"

show bg emi_houseext at bgleft
show emicas grin_up at twoleft
with charamove

show meiko smile at tworight
with charaenter


"La porte s'ouvre, et Mme Ibarazaki se tient debout en train de sourire à sa fille. Son sourire est toujours étonnamment similaire à celui d'Emi."


"Je ne pourrai jamais m'y faire."

show meiko wink
with charachange


emm "Tu sais, les gens attendent généralement quelques minutes avant de commencer à crier."

show emicas pout_up
with charachange


emi "Et la plupart des mères disent bonjour à leur fille au lieu de leur crier dessus tout de suite."

show meiko happy
with charachange


emm "Ah, bien sûr. Bienvenue à la maison, ma chérie. Tu m'as manqué."

play music music_another fadein 0.5

scene bg emi_kitchen
with locationchange


"Une étreinte affectueuse plus tard, nous sommes à l'intérieur et c'est seulement à ce moment que la mère d'Emi semble se rappeler que je suis là."

show meiko smile at center
with charaenter


emm "Et bonjour à toi aussi, Hisao. Comment vas-tu ?"


hi "Je vais bien, merci. C'est agréable de ne pas avoir à s’inquiéter de l'école pour un petit moment."

show meiko happy
with charachange


emm "Ah oui, tu as fini tes examens, hein ? Ça doit être un sacré soulagement pour vous deux."


hi "C'est un poids en moins, c'est sûr."

show bg emi_kitchen at bgright
show meiko happy at tworight
with charamove

show emicas happy at twoleft
with charaenter


emi "Moi aussi ! Je crois que j'ai bien dormi hier pour la première fois depuis des semaines grâce à ce seul fait."


"Si cette nouvelle est une surprise pour la mère d'Emi, elle ne le montre pas. Pourtant, sa réponse trahit un certain intérêt."

show meiko smile
with charachange


emm "Ah bon ? Je suis contente de l'entendre, Emi. Tu sais que je suis inquiète quand tu es mal à cause des... euh, examens."


"La mère d'Emi connaît clairement quelque chose que j'ignore - ou du moins, elle ne sait pas qu'Emi m'a dit pour les cauchemars."


"C'est intéressant, pouvoir observer Mme Ibarazaki couvrir Emi ; cet instinct protecteur pour être sûre que je n'en sache pas plus que ce qu'Emi est prête à me dire."


label fr_E26e:


"Apparemment Emi a plus en commun avec les quarks que je ne l'aurais cru."


"Elle va vite, est impossible à comprendre quand on la regarde simplement, et pourtant elle a un effet sur tous ceux qu'elle rencontre."

label fr_E26f:


"Je me demande si Mme Ibarazaki se rendra compte que je sais pour ses cauchemars, ou si elle va juste continuer de tout garder secret pour tout le monde ?"

show emicas weaksmile
with charachange


emi "Ouais, ça n'a pas été aussi dur cette année que ça a pu l’être avant, Hisao m'a aidée à rester concentrée."


"D'accord, je sais que ça c'est faux. Elle a même coupé contact avec moi en dehors des heures d'école durant les examens !"


"Mais... elle m'a effectivement vu durant la journée. Et elle m'a dit plus d'une fois que les courses matinales étaient la seule chose qu'elle avait hâte de faire durant les examens, donc peut-être que ce n'est pas tellement un mensonge."


"Dans tous les cas, entendre qu’être là a pu l'aider, même un peu, me fait plaisir."


"La mère d'Emi lève un sourcil à cette affirmation. Soit elle ne croit pas Emi, soit elle est aussi surprise que je le suis."

show meiko happy
with charachange


emm "Eh bien, apparemment c'est une bonne chose que vous soyez tous les deux devenus aussi proches."

show meiko smile
with charachange


emm "Je te dirais bien de prendre soin de ma fille, Hisao, mais apparemment tu le fais déjà."

show emicas closedsmile
with charachange


"Emi sourit et semble être fière que j'aie réussi à rentrer dans les bonnes grâces de sa mère aussi facilement."


hi "En fait, je dirais plus que c'est votre fille qui prend soin de moi. Elle m'a forcé à sortir et courir."


hi "Je suis probablement plus actif depuis que je l'ai rencontrée que je n'ai pu l’être, même avant..."


"Je n'y ai jamais vraiment pensé comme ça, ni apprécié l'ironie."


"Je n'étais pas très actif avant ma crise cardiaque. Des matchs de foot de temps en temps ne comptent pas vraiment."


"Donc maintenant que je suis certain que j'ai un cœur faible, {b}maintenant{/b} je cours chaque jour, forçant la chance avec l'aide de ma médication."


"Je souris silencieusement, puis réalise que je n'ai pas fini ma phrase."


hi "Enfin, avant que j'aie ma crise cardiaque et atterrisse dans cette école."


"Ça sort si naturellement. Il y a eu un moment où j'aurais réfléchi à deux fois avant de parler de ce qui ne va pas avec moi."


"Mais maintenant ? Ça semble idiot de s'en préoccuper, surtout en compagnie d'Emi et de sa mère."


"Si Emi peut se moquer de son handicap, alors moi aussi."


"Je repense à la rencontre d’athlétisme, où Emi déclarait être la fille sans jambes la plus rapide."


"Son manque évident n'a jamais semblé la gêner, du moins pas en public."


"Être coincée dans un fauteuil roulant la frustrait, je le sais. Mais même ça elle s'en est occupée toute seule, malgré mes efforts pour l'aider."

show meiko happy
with charachange


emm "Emi a un don pour stimuler le côté actif des gens. Je n'ai jamais vraiment su comment elle faisait."


"Ses yeux de petit chiot, pour commencer."

show meiko smile
with charachange


emm "Je ne suis pas surprise qu'elle ait réussi à t'entraîner dans un exercice journalier."


emm "Si Rin n'était pas aussi têtue qu'elle, je suis sûre qu'Emi l'aurait fait courir aussi."

show emicas happy
with charachange


emi "Oh, ça me rappelle ! Rin te dit bonjour."

scene bg emi_dining
with locationchange


"Je dévie de la conversation pendant que nous nous dirigeons vers la cuisine pour manger."


"Ça sent très bon ici, et la quantité qu'a faite la mère d'Emi est impressionnante."

show meiko smile at tworight
show emicas happy_up at twoleft
with charaenter


emi "Woah, il y a assez pour nourrir une armée entière ici !"

show meiko happy
with charachange


emm "C'est trop ? Ben vous pourrez toujours prendre les restes quand vous partirez."


hi "Ça serait bien ! Je prends à manger à la cafétéria depuis trop longtemps. Quelque chose cuisiné maison serait un changement agréable."

show emicas smile
with charachange


emi "Comme il dit. Merci, maman."


"Le repas est aussi savoureux qu'il sent bon et il y a un vide dans la conversation pendant que nous mangeons tous."


"Emi attaque son plat avec son appétit habituel, et je dois admettre que je suis plutôt rapide moi-même sur ce coup-là."

show meiko wink
with charachange


emm "Et donc Hisao, j'ai entendu dire que ma fille et toi êtes devenus assez proches, mmh ?"


"Le réflexe de dire quelque chose comme “Pas vraiment” est tellement fort que j'ouvre la bouche pour le faire, mais je me contrôle juste avant."


"On est proches, je ne peux pas dire le contraire. Je veux dire, Emi m'a amené ici après tout."


"Heureusement, Emi et sa mère prennent mon manque de réaction comme le signe que je suis pris par surprise plutôt qu'autre chose."


hi "Ha, je crois bien. Je blâme les courses du matin."

show emicas pout_up
with charachange


emi "Tu fais sonner ça comme si c'était une mauvaise chose, Hisao."

show meiko smile
with charachange


emm "Eh bien, moi j'y trouve un soulagement."


hi "Pourquoi ça ?"

show meiko worry
with charachange


emm "Emi a toujours été une fille populaire, mais ne s'est jamais fait beaucoup d'amis proches."


"C'est une nouvelle pour moi. J'ai toujours vu Emi discuter avec ses camarades de classe dans le couloir."


"Et l’équipe entière d’athlétisme semble l'adorer, mais c'est vrai qu'elle choisit de s'isoler avec Rin et moi durant le déjeuner."


"Pas exactement le comportement qu'on attendrait d'une fille populaire, après tout. Encore une fois, j'ai expérimenté son refus de la promiscuité, alors je ne suis pas tellement surpris."

show meiko serious
with charachange


emm "Je commençais à avoir des doutes."

show emicas awayfrown_up
with charachange


"Emi roule des yeux et marmonne quelque chose que je ne comprends pas."

stop music fadeout 1.0


hi "Hein ?"

show emicas neutral_up
with charachange


emi "Quoi ?"


hi "Qu'est-ce que t'as dit ?"

show emicas blush
with charachange


emi "Rien."

show meiko happy
with charachange


"Mme Ibarazaki s'étouffe avec sa boisson à cause d'un rire."

play music music_comedy fadein 0.5


emm "Tu fréquentes l'infirmier depuis trop longtemps, Emi."


emm "Je vais devoir lui toucher un mot de l'effet qu'il a sur ma fille."


hi "Étrangement, je ne pense pas que ça puisse marcher."

show emicas evil
with charachange


emi "J'ai appris surtout grâce à toi, de toute façon. Pas grâce à l'infirmier."

show meiko smile
with charachange


emm "Ne l'écoute pas, Hisao. C'est une menteuse née."

show emicas awayfrown
with charachange


emi "Hmph. Ouais bien sûr."


hi "Oh, je ne sais pas, Emi. Je crois que ta mère n'a pas forcément tort."

show emicas angry_up
with charachange


emi "Quoi ? Traître ! Tu es censé prendre ma défense là !"


hi "Ouais, mais il est vrai que tu as menti pour ta jambe après la rencon—{w=0.3}{nw}"

with vpunch


extend " aïe !"


"Un coup de pied dans le tibia par ce qui me semble être un pied en plastique m’interrompt, mais pas avant que les sourcils de Mme Ibarazaki se lèvent."

show meiko serious
with charachange


emm "Comment ça ta jambe ?"

show emicas awayfrown
with charachange


emi "Ce n'était pas grand-chose, c'est tout... J'ai juste été, erh, dansunfauteuilroulantunpetitmoment."


"Les derniers mots murmurés sont rapidement décryptés par la mère d'Emi - je suspecte qu'elle ait de l'expérience pour ce genre de chose - et un air inquiet apparaît sur son visage."

show meiko worry
with charachange


emm "Donc c'est pour ça qu'il a évité mes appels..."


emm "Oh Emi... Je sais à quel point tu détestes être dans un fauteuil roulant."


emm "Pas étonnant que tu aies été de si mauvaise humeur récemment !"

show emicas frown
with charachange


hi "Ouais, elle est bien plus heureuse sur ses pieds, pour ainsi dire."

show meiko serious
show emicas awayfrown
with charachange


emm "Bien évidemment ! Elle a passé bien suffisamment de temps dans un fauteuil après l'accident."

show emicas frown
with charachange


hi "Elle n'a pas immédiatement eu de prothèses ?"

show meiko worry
show emicas awayfrown
with charachange


emm "Non, elle devait finir de guérir avant qu'ils la laissent commencer le type de thérapie qui doit être suivie pour pouvoir utiliser ces choses."


emm "Surtout vu qu'elle voulait courir avec."

show emicas frown
with charachange


hi "Je ne savais pas."

show emicas weaksmile_up
with charachange


emi "Ouais, c'était chiant. Oh, tu as vu la muraille de Rin au festival ?"


"Le changement soudain de sujet de la part d'Emi fait que je réalise tardivement qu'elle a été mal à l'aise sur sa chaise durant tout le temps que sa mère et moi avons passé à parler."


"J'aurais dû me rendre compte qu'elle est un peu gênée quand on parle de son accident. Même avec sa mère."

show meiko serious
with charachange


emm "Non, je n'ai pas pu venir au festival, tu te rappelles ?"

show meiko happy
with charachange


emm "Bien que j'en aie eu un aperçu lorsque j'étais à la rencontre d’athlétisme. J'ai trouvé ça bizarre."

show emicas closedsmile
with charachange


emi "Je crois que c'est plus ou moins ce qu'elle visait. Elle a beaucoup parlé de ça en disant que c'était comme un rêve. Ou qu'elle essayait de le rendre comme un rêve."

show meiko smile
with charachange


emm "L'art de Rin est une des choses que je ne comprendrai sûrement jamais."

show emicas wink
with charachange


emi "Ce n'est pas surprenant. Je ne pense pas que Rin s'attende à être comprise."

show emicas grin
with charachange


emi "Elle m'a dit une fois que l'art permettait aux gens de comprendre des choses qu'ils ne comprendraient pas autrement, mais en même temps elle ne pense pas que ça marche vraiment comme ça."


"Je suis surpris qu'Emi en ait suffisamment parlé avec Rin pour avoir l'opinion de Rin sur le sujet."


"Bien que je ne pense pas que Rin puisse dire la même chose pour Emi."


"Sauf si, bien sûr, Emi m’empêche volontairement de savoir quoi que ce soit, ce qui est possible, mais y penser est désagréable."


"Je reste sur ce fil de pensée désagréable un moment, ne faisant plus attention à la conversation."

show meiko serious
with charachange


emm "D'ailleurs Emi, je voulais te demander..."

show emicas neutral
with charachange


emi "Mmh ?"

show meiko worry
with charachange


emm "Tu vas rendre visite à ton père cette année ?"

stop music fadeout 3.0


"D'après la façon dont elle le dit, on dirait que la mère d'Emi parlait de la pluie et du beau temps. D'après la façon dont réagit Emi, ce n'est clairement pas de ça dont elles parlent."

show emicas awayfrown
with charachange


"Elle se raidit et a un léger recul de la tête comme si elle venait de se prendre une claque."

show emicas sad
with charachange


emi "On peut en parler plus tard ?"


"Sa voix semble fragile, tendue. On dirait qu'elle a été vraiment secouée par la question."


"On dirait que Mme Ibarazaki a mal jugé à quel point nous pouvons être proches Emi et moi."


"Il n'est pas bon, apparemment, de discuter de certaines choses quand je suis là. Son père est l'une de ces choses."


"L'accident qui a pris ses jambes est probablement une de ces autres choses, et sa réaction de tout à l'heure, lorsque je discutais avec sa mère, en est un signe."


"Il ne faut pas longtemps à la mère d'Emi pour se rendre compte qu'elle a foiré."

show meiko happy
with charachange


emm "Bien sûr ma chérie. Désolée d'aborder le sujet, je voulais savoir si je pouvais prévoir-"

show emicas neutral
with charachange


emi "C'est bon. T’embête pas pour ça."


"Emi remue nerveusement, comme si elle était embarrassée par sa propre réaction. J'avoue que son comportement est déroutant."


"Elle a mentionné son père plus tôt aujourd'hui devant moi ! Il y a moins de quelques heures, même !"


"Pourquoi une question aussi simple que celle qui est de savoir si elle va aller rendre visite à son père provoque une réaction aussi forte ?"



"Sauf si la sérénité qu'elle clamait avoir après notre discussion de la veille s'est évaporée."


"Ou que ça n'a pas aidé autant qu'elle le pensait. Ou le clamait."

show emicas weaksmile
with charachange


emi "Je euh, reviens. Je vais au petit coin."

hide emicas
with charaexit

show bg emi_dining at bgleft
show meiko smile at center
with dissolvecharamove


"Emi se lève soudainement et sort de table, me laissant seul avec Mme Ibarazaki."


"Je suis un peu dans le doute. Je devrais la suivre, ou rester ici ?"


"Il est évident que le départ d'Emi n'est pas dû à un besoin naturel. Quelque chose l'a embêtée, et je dois savoir ce que c'est."



label fr_choiceE26:
menu:
    with menueffect
    "Qu'est-ce qu'il faut que je fasse ?"
    "La suivre.":




        return m1
    "Parler avec sa mère.":


        return m2

label fr_E26c:




"La seule façon de savoir est d'aller voir à la source. Et la source est en ce moment même en train soi-disant d'utiliser les toilettes."

scene bg emi_kitchen
with locationchange


"Je m'excuse poliment et pars dans cette direction, et m’arrête en voyant Emi non pas dans la salle de bain, mais dans la cuisine juste à côté du salon."

show emicas sad
with charaenter


"Emi a laissé la porte ouverte, et alors que je m'approche, je peux voir qu'elle se tient à la table pour tenter de se ressaisir, un effort qui échoue aussitôt que j'ouvre la bouche."


hi "On ne dirait pas que le besoin naturel était urgent."

show emicas angry
with charachange


"Emi sursaute et me fixe du regard."

show emicas angry_up
with charachange


emi "Qu'est-ce que tu fais là ? Je ne suis pas venue ici pour être avec d'autres personnes."


hi "Je voulais juste t'aider. Tu sembles assez secouée."

show emicas awayfrown
with charachange


emi "J'ai dit que c'était rien, hein ? En plus, je croyais qu'on avait établi que tu ne pouvais pas m'aider."


hi "Non, on a établi que tu étais têtue."

show emicas angry
with charachange


emi "Regarde qui parle. Le gars qui m'a suivie."


hi "C'est différent ! Je veux t'aider avec... peu importe ce que c'est."

show emicas awayfrown
with charachange


emi "C'est drôle, parce que {b}je{/b} veux juste que tu me laisses seule."


hi "Mais pourquoi ? Pourquoi tu ne peux pas juste me faire confiance ?"

show emicas frown
with charachange


emi "On a déjà parlé de ça, Hisao. Je dois gérer ça toute seule."


hi "Je ne suis pas d'accord ! Tu as besoin de mon aide, et tu refuses juste de la prendre !"


"Ma formulation est un peu maladroite."

show emicas angry
with charachange


emi "Besoin ? J'ai {b}besoin{/b} de ton aide ?"

play music music_tragic fadein 0.5

show emicas angry_up
with charachange


emi "Eh bien, c'est une bonne chose qu'on se soit rencontrés, hein ? Parce que sinon, je pense que j'aurais juste été une personne brisée, hein ?"


emi "Non, c'est une fichue bonne chose que Hisao soit venu pour tout arranger, hein ? Parce que Dieu sait à quel point j'en suis incapable, hein ?"


emi "Je suis juste la pauvre petite fille sans jambes et émotionnellement fragile, c'est ça ?"


hi "Emi, tu sais que je ne pense pas ça-"

show emicas angry
with charachange


emi "Vraiment ? Parce que si tu pensais différemment alors je ne crois pas que tu serais là, disant que j'ai besoin de ton aide."


emi "J'ai été assez loin dans la vie en tant qu’être humain sans toi."


hi "Alors quoi, rien de ce que nous avons partagé n'est important ? Je suis juste le gars avec qui tu traînes ?"

show emicas awayfrown
with charachange


emi "Tu es mon petit ami, Hisao, pas mon sauveur."


hi "Ah bah non, ça c'est bien clair. Tu n'envisages même pas que je pourrais t'aider, hein ?"


hi "Tu gardes juste tout emprisonné à l'intérieur de toi et espères que courir résoudra tes problèmes, sinon tu viendras me voir et on fera les idiots jusqu’à ce que tu te sentes mieux."


hi "C'est pas ça aller bien, Emi. Ce n'est pas ça le sens d'une relation amoureuse."

show emicas frown
with charachange


emi "Eh bien c'est ça pour moi, Hisao."

show emicas sad
with charachange


emi "J'aimerais-"


"Elle semble reconsidérer ses paroles. Un instant de douleur, de doute s'affiche sur son visage. Pendant un moment je crois qu'elle est sur le point de pleurer."

show emicas frown
with charachange


"Mais le moment passe, et maintenant elle s'est ressaisie encore une fois. Quel que soit ce qu'elle voulait, ce ne sera pas dit."


emi "Écoute, j'ai juste... je ne peux pas faire ça maintenant."


hi "Quoi, avoir une conversation sérieuse ? Être ouverte ? Être honnête ? S’intéresser un minimum à autre chose que toi-même et tes problèmes ?"

show emicas angry_up
with charachange


emi "Qu'est-ce que tu sais de mes problèmes ? Rien ! Tu ne sais pas ce que j'ai vécu, alors arrête de prétendre que tu sais."


hi "Je sais que tu fais des cauchemars, et je sais que ton père est parti. Qu'est-ce qui lui est arrivé ?"

show emicas sad_up
with charachange


"Emi a un mouvement de recul comme si je venais de lui mettre une claque. La fragilité est revenue dans sa voix."

show emicas sad
with charachange


emi "Ça suffit."


"C'est idiot. La conversation entière n'a été que des variations d'Emi mettant des murs entre nous."


hi "Quoi, tu ne veux même pas répondre à cette question ? Très bien, garde tes secrets. Tu peux les emporter dans ta tombe, pour ce que je m'en moque."

show emicas blush
with charachange


"Les yeux d'Emi s'écarquillent sous le choc. Quand elle ouvre à nouveau la bouche, c'est une voix basse, dangereuse, qui en sort."

show emicas grit
with charachange


emi "Sors de ma maison, Hisao."


"Le soudain changement de ton de sa part annule instantanément ma colère et me fait réaliser la sainte horreur de ce que je viens de dire."


hi "Emi, je ne voulais pas-"

stop music fadeout 2.0

show emicas angry
with charachange


emi "J'ai dit {b}pars{/b}, Hisao."


emi "Dis à ma mère qu'elle a cuisiné un fantastique repas mais que tu as oublié quelque chose d'important, et sors de ma maison."


"Elle tremble maintenant, tremblant avec colère, ou tristesse, ou détermination. Sa voix est toujours basse, contrôlée. Presque un grognement."


"Je tends la main pour la poser sur son épaule, pour m'excuser d'avoir été trop loin, mais elle recule pour m'éviter."

show emicas angry_up
with charachange


emi "Sors d'ici."

show bg emi_dining at bgleft
show meiko serious at center
with locationchange


"Qu'est-ce que je peux faire ? Je sors de la cuisine et vais dans le salon, m'excuse auprès de Mme Ibarazaki et m'en vais."

$ suppress_window_after_timeskip = True

scene black
with dissolve





label fr_E26d:


"Il y a un silence gênant à table pendant un moment après qu'Emi soit partie. Je ne sais pas quoi dire."

show meiko serious
with charachange


"La mère d'Emi soupire, rompant le silence."

play music music_moonlight fadein 5.0


emm "Désolée pour ça, Hisao. J'oublie parfois qu'Emi est sensible sur certains sujets."


emm "Et je parlais du fauteuil roulant, en plus..."


hi "Je devrais aller auprès d'elle ?"

show meiko worry
with charachange


emm "Doux jésus non ! Elle n'est pas sortie de table pour continuer la conversation, tu sais."


hi "Mais si elle est troublée, quelqu'un ne devrait pas l'aider ?"

show meiko serious
with charachange


emm "Si c'était n'importe qui d'autre, je te dirais oui. Mais ma fille est têtue comme une mule, et si elle veut être seule alors c'est mieux de la laisser seule."


emm "Sinon elle dira probablement quelque chose qu'elle regrettera, ce qui te fera dire quelque chose que tu regretteras, et je préférerais que ce dîner ne se finisse pas avec l'un de vous deux sortant en trombe de la maison."

show meiko happy
with charachange


emm "Si ça venait à arriver je serais une terrible hôtesse, hein ? J'ai déjà fait une bêtise aujourd'hui."


hi "C'est pas grave, je n'aurais pas dû aborder le sujet du fauteuil apparemment."

show meiko serious
with charachange


"Mme Ibarazaki fronce les sourcils, clairement plus troublée par le départ d'Emi qu'elle ne le laisse savoir."


emm "J'aimerais qu'elle ne fasse pas ça. Ça ne fait que m’inquiéter plus, tu sais."


hi "Elle fait ça souvent ?"

show meiko smile
with charachange


emm "Quoi, s'enfuir aux toilettes ? Non, pas vraiment. Mais cacher des blessures à sa mère ? Eh bien, c'est un peu plus commun."


emm "À chaque fois que je me rends compte qu'elle me ment comme ça, elle m'assure que la seule raison est que ce n'était pas grand-chose."


hi "Si ça peut vous consoler, je suis sûr que la seule raison pour laquelle je l'ai su c'est parce que je la voyais tous les jours."

show meiko happy
with charachange


"Ma remarque déclenche un rire sec de l'autre côté de la table. Mme Ibarazaki soupire, un peu tristement."

show meiko smile
with charachange


emm "Encore hésitante à être proche des gens, hein ? Je continue d’espérer qu'elle passe au-delà de ça."


emm "C'est drôle, vraiment. Elle a tellement bien rebondi après son accident, de tellement de façons..."

show meiko serious
with charachange


emm "J'imagine que certaines choses ne disparaissent jamais vraiment."


"D'après ce que je vois, cette histoire semble la troubler encore elle aussi."


"Elle semble être un peu plus encline à parler de l'accident maintenant qu'il n'y a pas Emi, cela dit."


hi "Dites, j'ai une question, si ça ne gêne pas trop."

show meiko smile
with charachange


emm "Oh ?"


hi "Qu'est-ce qu'a perdu Emi exactement dans cet accident ? L'infirmier a dit qu'elle devient comme ça quand c'est l'anniversaire, et elle refuse d'en parler avec moi..."

show meiko happy
with charachange


emm "Donc tu t'es dit que je te mettrais à la page, mmh ?"


hi "Euh, ouais. Avec de la chance."

show meiko serious
with charachange


emm "Eh bien, il y a un problème avec ta requête, tu sais."


hi "Laissez-moi deviner : vous avez promis à Emi que vous ne le diriez à personne si elle ne voulait pas que cette personne le sache, et vous ne savez pas si elle veut que je sache ?"


emm "Quelque chose comme ça. J'ai promis à Emi qu'elle serait celle qui raconterait l'histoire aux gens."


hi "Mais ce n'est pas important ? Je veux dire, ça a clairement eu un énorme effet sur elle, si elle est toujours comme ça si longtemps après l'accident."

show meiko worry
with charachange


emm "C'est vrai. Ça a un effet de longue durée sur elle. Il y a certaines choses sur lesquelles elle ne passera probablement jamais."


"Pendant un moment Mme Ibarazaki semble incroyablement attristée, comme si une vieille blessure l'ennuyait."


emm "Je pense qu'il y a certaines choses au-delà desquelles je ne passerai jamais..."

show meiko happy
with charachange


"Un autre rire sec, et d'un mouvement de tête la mère d'Emi repousse son souvenir."

show meiko smile
with charachange


emm "Écoute, il y a quelque chose que tu dois absolument comprendre sur ce qu'Emi pense de l'accident."


hi "Et donc ?"


emm "Ce n'était pas grand-chose."

stop music fadeout 1.0


"J'arrive à retenir ma mâchoire de tomber au sol de surprise, mais ça me demande de l'effort."


"Ça doit être la chose la plus ridicule que je n'ai jamais entendue."


hi "Je vous demande pardon ?"

play music music_sadness fadein 3.0

show meiko serious
with charachange


emm "D'accord, peut-être que ce n'est pas aussi simple, mais c'est assez vrai. Emi pense que l'accident ne l'a pas définie, et que tout ce qu'elle a perdu ce jour ne la définit pas non plus."


emm "Elle n'est pas “la fille qui a perdu ses jambes”, elle est “La Fille sans Jambes la Plus Rapide.” Son optimisme et son énergie sont sortis de l'accident sans une égratignure."


hi "Et pourtant ça va au-delà, non ? Je veux dire, la nuit dernière elle m'a dit qu'elle refusait de compter sur qui que ce soit parce que le perdre ça serait trop douloureux."

show meiko smile
with charachange


emm "Pas vraiment. Tu as dit qu'elle ne veut pas te parler de l'accident, même si tu lui as déjà demandé auparavant."


emm "Si elle ne veut pas t'en parler quand tu demandes, c'est parce que pour elle, ce n'est pas quelque chose que tu as absolument besoin de savoir. Même si elle n'était pas terrifiée de trop se rapprocher de quelqu'un, elle refuserait quand même d'en parler."


hi "Elle a peur d’être trop proche de moi ?"

show meiko happy
with charachange


emm "Mon dieu, oui. Avec toute cette histoire et le fait qu'elle soit sortie indemne de l'accident, elle a acquis la connaissance néfaste de la rapidité avec laquelle tout peut vite finir."

show meiko smile
with charachange


emm "Donc elle ne va pas laisser les gens devenir trop proches d'elle, et elle va tout faire pour traverser toutes les difficultés qui se mettent sur son chemin toute seule et sans l'aide de personne."


hi "Mais je ne pense pas qu'elle {b}puisse{/b}."

show meiko serious
with charachange


emm "Ah bon ? Tu es sûr que tu sors avec ma fille et pas avec quelqu'un d'autre ? Fais-moi confiance Hisao, elle peut surmonter ça toute seule."


hi "Mais elle a ces cauchemars, et elle ne dort pas bien, et—"

show meiko smile
with charachange


emm "Et ça arrive chaque année. Dis-moi, si elle n'était pas capable de surmonter ça toute seule, tu penses vraiment qu'elle serait toujours en vie ? Elle se serait suicidée, ou un équivalent tout aussi mélodramatique."


hi "Alors quoi, je ne devrais pas essayer de l'aider ?"

show meiko serious
with charachange


emm "Je n'ai pas dit ça ! Je déteste voir ma fille comme ça, et savoir qu'elle peut compter sur quelqu'un me détendrait."


emm "Tu as juste besoin de comprendre qu’accepter de l'aide va contre tout ce en quoi croit Emi à propos d’elle-même et de la façon dont marche le monde."


emm "Si tu veux toujours offrir ton aide, alors c'est à toi de décider. Honnêtement, j'aimerais que tu le fasses, mais ça serait idiot de ne pas te prévenir que ça ne va pas être facile."

show meiko smile
with charachange


emm "Il faut juste que tu sois patient avec elle. Elle est déjà plus proche de toi qu'elle n'a jamais été proche de qui que ce soit à Yamaku."


hi "Je n'ai pas tellement l'impression que nous soyons si proches."

show bg emi_dining at center
show meiko serious at tworight
with dissolvecharamove

show emicas evil at twoleft
with charaenter

stop music fadeout 0.3


emi "Bien, ça rend les choses plus faciles."


"La voix d'Emi me provoque presque une crise cardiaque."


hi "Woah ! Je ne t'ai pas entendue revenir, Emi."

show emicas angry
with charachange


emi "Comme c'est pratique."


hi "Attends, tu écoutais ?"

show emicas angry_up
with charachange


emi "Non. Il s'est juste avéré que je suis revenue au bon moment."

show meiko worry
with charachange


emm "Emi, Hisao était juste—"


"Emi lève un doigt, interrompant sa mère."

show emicas grit
with charachange


emi "En chemin vers chez lui ? Ouais, je sais."


"Emi tremble de colère maintenant, semblant vaguement trahie."


emm "Emi, ne sois pas ridicule, on était juste—"

show emicas angry_up
with charachange


emi "Tu as {b}promis{/b} !"

play music music_rain fadein 0.5


"La douleur qu'elle exprime dans ce dernier mot est presque trop pour moi. L'idée que je puisse lui faire aussi mal me donne l'impression d'être frappé dans le ventre."


"La mère d'Emi semble tout aussi troublée que moi."


emm "Et j'ai tenu ma promesse ! Écoute-moi, il n'y a pas de raison pour qu'on jette les gens hors de la maison."


"La mère d'Emi semble être à la fois en colère contre l'explosion de sa fille et embarrassée que je sois spectateur de ça."



"Il n'y a qu'une seule vraie solution au problème, je pense."


hi "Ce n'est pas grave, je vais partir."


emm "Vraiment, ça ne me semble pas nécessaire..."


hi "Ne vous inquiétez pas. Merci pour le dîner, Mme Ibarazaki, et pour les conseils."

show meiko serious
with charachange


emm "C'était avec plaisir, Hisao. Je suis désolée qu'on n'ait pas pu prendre de dessert."


hi "Ce n'est pas grave. Je dois faire attention à ce que je mange, de toute façon."


hi "Bonsoir, Emi, Mme Ibarazaki."


"La formalité de nos conversations, mélangé au fait que je me prépare à partir, semble sortir Emi de sa colère."

show emicas frown
with charachange


emi "Non, attends. Je suis désolée, j'ai été tellement... et après la nuit dernière j'ai juste pensé... Tu n'as pas à partir, je retire ce que j'ai dit, ce n'est pas grave—"


"Je ne peux pas m’empêcher de légèrement sourire. Elle peut à peine articuler ses excuses, et j'aimerais vraiment rester..."


"Mais je ne crois pas que je puisse. J'ai besoin de penser à ce qu'a dit sa mère, et à ce que je vais faire pour nous."


"Je ne veux pas risquer de mettre accidentellement Emi en colère encore une fois non plus."


hi "Non, je crois que je ferais mieux de partir. Tu sembles plutôt secouée et, eh bien, j'ai juste envie de t'aider encore. Je sais que tu préférerais que je ne le fasse pas, alors je vais partir à la place."

show emicas sad
with charachange


emi "Mais—"


hi "Hé, ce n'est pas grave. Tu ne veux pas de cavalier sur un cheval blanc, c'est ça ? Promets-moi juste une chose, d'accord ?"

show emicas frown
with charachange


emi "Quoi ?"


hi "Ne sois pas énervée contre ta mère, d'accord ? Elle ne faisait que me donner des conseils, c'est tout."

show emicas sad
with charachange


"Emi hoche la tête, hésitante, comme si cette simple chose était la limite de ce qu'elle pouvait concevoir. Elle est bouleversée, mais je ne peux rien faire pour ça pour l'instant."


emi "D'accord."


hi "Je te vois demain, d'accord ? On court demain matin, n'oublie pas !"


"Je peux voir que j'ai fait mal à Emi en décidant de partir. Mais il n'y a rien que je puisse faire pour elle comme ça, et je sais qu'elle est trop têtue pour admettre qu'elle veut que je reste."


"Je regarde diverses émotions passer sur le visage d'Emi alors qu'elle essaye d'enregistrer ce qui vient d'arriver."

show emicas weaksmile
with charachange


"Peu après vient cet air calme, comme hier soir, tout comme sa voix qui s'efforce d’être paisible."


emi "D'accord, Hisao. À plus tard."


"Aucun de nous deux n'a envie de laisser paraître d’émotion à ce point, et j'ai du mal à garder une expression neutre, alors je tourne les talons et franchis la porte."

stop music fadeout 7.0

scene bg emi_houseext
with locationskip


"Je ferme lentement la porte derrière moi, m’arrêtant un moment alors que le loquet claque, gardant la main sur la poignée."


"Est-ce que j'ai pris la bonne décision ? Est-ce que j'aurais dû rester et essayer d'arranger les choses ?"


"Non, j'ai décidé. Pas comme ça devant sa mère. Malgré tout, je préférerais éviter à la mère d'Emi d'avoir à faire face au type de colère qui a surgi hier soir."


"Même si elle y est sûrement habituée, j'ai un certain instinct protecteur qui veut garder intacte l'image d'Emi en tant que fille joyeuse."


"Avec un sursaut, je réalise que ma main est toujours refermée sur la poignée. Je la retire, la range dans ma poche, et pars dans la rue maintenant assombrie."

scene bg school_dormhisao
with shorttimeskip

play music music_pearly fadein 1.0


"Je laisse sortir un long souffle."


"L'attente jusqu'au lendemain matin ne va pas être facile."


"Dans tous les cas, je dois penser à ce que je vais dire à Emi. Je dois m'excuser, et je dois parvenir jusqu'à elle d'une façon ou d'une autre."


"D'ailleurs, quelque chose m'a trotté dans la tête sur le chemin du retour."


"La lettre d'excuse d'Iwanako."


"J'étais si préoccupé par ma nouvelle vie quand je l'ai reçue que je n'ai même pas pris la peine de vraiment la lire."


"Maintenant que je me trouve dans une situation similaire, ma curiosité se réveille. Qu'est-ce qu'elle voulait me faire savoir à ce point ?"


"Et puis, lire ses pensées pourrait aider à réorganiser les miennes."


"Je me rappelle m'en être débarrassé. Zut, où est-ce que j'ai jeté ce truc ?"


"Je regarde sous mon bureau. Il n'y a rien, alors je cherche dans des endroits plus difficiles d’accès, même s'ils sont moins plausibles."

"…"


"Bon, maintenant je sais où était ma chaussette perdue, au moins."


"Toujours pas de lettre, cela dit."


"C'est quand je passe mon bras sous mon chevet que je sens quelque chose de chiffonné coincé contre le mur."


"Grognant un peu à cause de l'effort, je ressors ma découverte et l’amène à la lumière."

"Bingo."

play sound sfx_paper

scene ev hisao_letter_open_2
with locationchange


"Je m'assois à mon bureau et déplie la feuille chiffonnée. Avec un clic, j'allume la lampe de la table."


"Passant les plaisanteries sans importance, je cherche l'endroit où je me suis arrêté la dernière fois. Ah, voilà."

window hide


$ written_note("Il y a d'autres choses dont je veux te parler. Je t'écris parce que j'ai l'impression que j'aurais dû te dire certaines choses après l'incident de l'hiver. Je regrette vraiment ne pas avoir été capable de le dire en personne, et je n'ai aucune excuse pour ça.\n\n\n\n\n")


$ written_note("La vérité est que les fois où je t’ai rendu visite à l’hôpital, je me suis inquiétée pour toi. Je ne parle pas de ta santé. Tu semblais plus distant et découragé. C'était naturel après ce qui est arrivé, mais j'avais l'impression que tu avais abandonné quelque chose à ce moment-là. Le bonheur, peut-être ?\n")

window show


"Abandonner le bonheur..."


"Ça me semble malheureusement familier."

window hide


$ written_note("Je voulais exprimer mes sentiments, mais les mots ne sortaient pas. Je ne pouvais rien dire pour te réconforter. Je suis vraiment désolée de ne pas avoir pu t'aider quand tu en avais le plus besoin, même si je t’appréciais tant. Au moins maintenant, finalement, je peux être honnête.\n\n\n\n")


$ written_note("Si je pouvais revenir à ces jours qu'on passait dans le silence, en février et mars, je te dirais de ne pas abandonner. C'est ce que je dirais. Peut-être que tu n'aurais pas dérivé si loin si j'avais dit quelque chose. J’espère que tu as réussi à te remettre sur pied par toi-même..\n\n\n\n")


$ written_note("Maintenant que la distance entre nous est aussi physique, ça me semble définitif. Je me demande si on se reverra. Peut-être que c'est mieux si on ne se revoit pas. Si tu veux correspondre avec moi, écris-moi par tous les moyens possibles. J'aimerais beaucoup entendre parler de ta nouvelle école et de comment tu vas. Je ne te souhaite que le meilleur.\n\nSincèrement, Iwanako")

window show


"Après avoir fini de lire la lettre, je la plie soigneusement et la pose sur un coin de mon bureau."

$ renpy.music.set_volume(0.5, 1.0, channel="music")

window hide
nvl clear
nvl show dissolve


n "\n\n\nMerci, Iwanako. Je voulais répondre “oui” à ta question de ce jour d'hiver, mais je n'ai jamais pu."


n "Au moment où on s'est revus, il était trop tard."


n "Ou du moins c'est ce que j'ai pensé. Qu'est-ce qui se serait passé si je m'étais comporté différemment, dans cette lamentable chambre stérile d’hôpital ?"


n "Je suis désolé. Ça ne sert plus à rien de se le demander maintenant, mais ça ne sert à rien d'essayer d'oublier non plus."


n "Je suis celui que je suis à cause de tout ce qui m'est arrivé et ce que j'ai hâte d'expérimenter. Présent, passé, et futur."


stop music fadeout 2.0


n "\n\nEt ce passé m'a peut-être donné une importante leçon aujourd'hui."

$ renpy.music.set_volume(1.0, 2.0, channel="music")

nvl clear
nvl hide dissolve






label fr_E27:

window hide None

scene black
with dissolve

play sound sfx_alarmclock

with Pause(2.0)

scene bg school_dormhisao
with openeye

window show


"L'alarme matinale résonne et je roule sur le côté pour l'éteindre. Mes yeux ouverts fixent le plafond."

play music music_night fadein 1.0

window hide
nvl clear
nvl show dissolve


n "\n\nQu'est-ce que je vais faire ? Est-ce que je sors du lit, vais sur la piste, et prétends que rien n'est arrivé ?"


n "Est-ce qu'Emi viendra ? Après les événements de la veille, j'ai un doute."


n "Même si elle venait, qu'est-ce que je ferais ? Passer par-delà la dispute et juste faire la même chose la prochaine fois que quelque chose l’embête ?"


n "Je sais que j'ai parlé hâtivement hier soir, surtout en essayant d'utiliser son père comme levier."


n "Mais est-ce que j'ai dit quelque chose de vraiment déplacé ? Elle ne me laissera pas entrer, jamais, et elle sera forcée de souffrir seule."


n "Rien de ce que je fais, rien de ce que je dis ne va changer ça. Elle ne changera pas, et elle a déjà décidé de me garder à distance."


n "\nEst-ce que je peux vraiment aller sur la piste et la voir, sachant que je ne vais jamais passer au-delà d'où je suis maintenant ?"

nvl clear
nvl hide dissolve

scene black
with shuteye

window show


"Non, j'ai décidé. Je ne peux pas. Pas aujourd'hui. Je roule sur le côté et me rendors."


"Elle ne sera probablement pas là de toute façon."

scene bg school_cafeteria
with shorttimeskip


"Une conversation mentale similaire se répète quand arrive le temps d'aller déjeuner, et je mange à la cafétéria, seul."


"Je ne veux pas la voir ; la pensée seule me rend malade."

scene bg school_track_ni
with shorttimeskip


"Le soir, je vais courir. Je suis seul pour la première fois depuis qu'Emi a été malade après la rencontre d’athlétisme."


"Je ne vais pas voir l'infirmier, juste au cas où il poserait des questions sur Emi."


"Je n'ai pas envie de parler d'elle, non plus."

scene bg school_hallway3
with shorttimeskip


"Le jour suivant, je fais la même chose. Alarme, coupée. Reste au lit. Mange seul, cours seul."


"Pour passer le temps que je passerais normalement avec Emi, je commence à lire plus."


"Ça fonctionne étonnamment bien, jusqu’à ce que je me surprenne à aller me cacher dans des toilettes parce que je l'ai vue marcher dans le couloir entre deux cours."


"Si elle m'a remarqué, elle ne l'a pas montré. Même si je ne pense pas qu'il lui arrive de montrer quoi que ce soit."


"Certainement pas aux filles de sa classe avec lesquelles je la vois parler joyeusement."


"Ou à ses camarades du club d’athlétisme."


"Surtout pas à moi."


"Alarme coupée. Reste au lit."

scene bg school_scienceroom
show muto normal at center
with shorttimeskip


"Mutou et moi avons une longue discussion sur la possibilité que la théorie des cordes soit plausible. Je ne suis pas convaincu pour ma part."


"Plus de quatre dimensions, je peux accepter. Mais un tas de cordes vibrantes à un niveau subatomique ? Ça fait un peu beaucoup."


"On dirait que je ne suis pas le seul à penser comme ça, aussi. Apparemment ce n'est pas une théorie aussi populaire qu'elle a pu l’être."


"Mutou dit que c'est juste parce que personne n'a trouvé la bonne façon d'examiner les données encore."

$ renpy.music.set_volume(0.3, 0.0, channel="ambient")
play ambient sfx_rooftop

scene bg school_roof
with shorttimeskip


"Mange seul."


"Le toit est désert aujourd'hui. Je me demande brièvement où sont Emi et Rin, puis oublie la question. La chose importante est qu'elles ne sont pas là, alors je n'ai pas à leur parler."


"Vu que je n'ai personne à qui parler, j'apporte un livre et lis."


"Il fait bon, si ce n'est un petit peu chaud."


"Avec de la chance, ça sera plus frais ce soir ; une vague d'air frais semble confirmer ma théorie."

stop ambient fadeout 2.0

scene bg school_track_on_ni
with shorttimeskip


"Cours seul."


"C'est plus frais sur la piste. Aucun signe d'Emi, ce qui est exactement ce que je recherche."


"Je m'étire et commence à courir comme à mon habitude, y allant vite pour ignorer le manque de partenaire courant avec moi."


"Mes pensées dérivent malgré tout vers ce rire féminin, ce sourire incorrigible, ces grands yeux gentillets, ce corps incroyablement tonique—"

scene bg school_track_running_ni
with Dissolve(1.0)


"J’accélère le rythme pour me vider la tête. Parcourant la distance entre les virages et moi, trouvant la vitesse qui me fait uniquement penser à la brûlure dans mes jambes."


"Je regarde ma montre en faisant le dernier tour, remarquant que j'ai accéléré."

show bg school_track_on_ni
with Dissolve(2.0)


"Mon cœur est un peu erratique ce soir, alors je fais quelques tours supplémentaires en marchant au cas où."


"Pas une raison suffisante pour attirer l'attention de l'infirmier. Ça va aller. Une pensée très Emi-esque, je l'avoue."


"J’espère qu'au bout d'un moment j’arrêterai de penser autant à elle."

scene bg school_dormhisao
with shorttimeskip


"Je finis un autre livre avant d'aller au lit ce soir. Je devrai m’arrêter à la bibliothèque demain."

play sound sfx_switch

show bg school_dormhisao_ni
with Dissolve(0.2)

with Pause(0.5)

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
stop music fadeout 3.5

scene black
with shuteye

window hide

with Pause(2.0)
play sound sfx_alarmclock
scene bg school_dormhisao
with openeye

window show


"Je ne sais pas pourquoi je continue de mettre l'alarme aussi tôt, mais ça me réveille quand même pareil le lendemain matin. Je la coupe et retourne dormir."

scene bg school_scienceroom
show misha perky_smile at center
with shorttimeskip

play music music_pearly fadein 1.0


"Ce midi, alors que je me prépare pour aller à la cafétéria pour un autre déjeuner seul (j'ai un nouveau livre au sujet de deux escrocs en ancienne Perse que j'ai assez hâte de lire), je suis soudainement pris en embuscade par Misha et..."


"Huh. Juste Misha on dirait."

show misha hips_smile
with charachange


mi "Tu vas encore manger seul, Hicchan~ ?"

show misha sign_smile
with charachange


mi "On a remarqué, tu sais~ !"


hi "On ?"

show misha hips_grin
with charachange


mi "Uh huh ! Shicchan et moi avons remarqué que tu passais plus de temps seul !"

show misha hips_smile
with charachange


mi "Elle voulait savoir pourquoi, alors je lui ai dit que je le te demanderais !"


hi "Je suis surpris qu'elle ne me l'ait pas demandé elle-même."

show misha perky_smile
with charachange


mi "Elle l'aurait fait, mais elle voulait commencer la paperasse. Il y a beaucoup à faire vu que c'est la fin de la période, tu sais~ !"


hi "Pourquoi cet intérêt soudain pour mon bien-être, d'ailleurs ?"

show misha sign_smile
with charachange


mi "Ah, Shicchan a dit “C'est le devoir du Conseil des Étudiants de suivre la santé émotionnelle de ses étudiants ! De permettre qu'un électeur tombe dans la dépression serait un manquement impardonnable aux devoirs du conseil !"


hi "Eh bien, c'est pas un problème alors. Je ne suis pas déprimé."

show misha perky_confused
with charachange


mi "Mais tu manges seul, et personne ne t'a vu avec Emi ! Quelque chose est arrivé, hein, Hicchan~ ?"


"La voix de Misha est légèrement plus sévère, bien qu'elle continue de garder la rallonge à la fin de ses phrases."



label fr_choiceE27:
menu:
    with menueffect
    "Je plisse les lèvres, incertain du choix de ma réponse."
    "Ne pas lui en parler.":




        return m1
    "Abandonner et mettre Misha au courant.":


        return m2







label fr_E27a:

"Je ne suis pas sûr d'aimer l'idée que le Conseil des Étudiants soit au courant de ma vie privée."


hi "Rien d'important."

show misha cross_frown
with charachange


mi "Hicchan, c'est une terrible chose de mentir~ !"


"Elle ne me croit pas."


"D'accord, il faut lui donner un truc, mais pas trop."


hi "On a eu un désaccord qui n'a pas encore été résolu."

show misha perky_confused
with charachange


mi "Oh ? Pourquoi ça ?"


hi "Parce que - écoute, je n'ai pas besoin d'en parler, d'accord ?"


hi "Ce n'est pas grand-chose, d'accord ? Je vais bien."

show misha perky_sad
with charachange


mi "Et Emi ? Elle va bien aussi, Hicchan ?"

stop music fadeout 4.0


"La voix de Misha a prix un ton vraiment sérieux. C'est ridicule."


hi "Je ne sais pas, d'accord ? Je n'ai pas demandé. Les choses sont compliquées en ce moment."

show misha hips_frown
with charachange


mi "Quel genre d'homme es-tu ? Les choses deviennent un peu dures et tu t'enfuis ?"

play music music_rain fadein 4.0


"La remarque soudaine de Misha me prend par surprise."

show misha cross_frown
with charachange


mi "Shicchan appellerait ça un acte de lâcheté, et elle aurait raison !"


mi "Vous étiez proches ! Heureux ensemble ! Tu vas laisser tout ça couler sans combattre ?"


mi "Tu devrais vouloir te battre pour ta petite copine, Hisao !"


"On dirait que Misha parle comme Shizune. Ça ne me surprendrait pas de découvrir que Shizune a donné un script à suivre en fonction de ma réponse."


"Misha pointe d'un doigt impératif la porte de la classe."

show misha sign_smile
with charachange


mi "Maintenant sors de cette classe et va réparer les choses !"


hi "Hum, on a toujours les cours de l'après-midi..."


"Ça ne semble pas dissuader Misha."

show misha hips_smile
with charachange


mi "Alors après les cours ! Tu as intérêt à le faire, Hicchan ! C'est important de ne pas laisser les choses comme ça !"


hi "Pourquoi ?"

show misha cross_frown
with charachange


"Misha me regarde comme quelqu'un regarderait les déjections d'un animal."


mi "Elle ne comptait pas pour toi, Hisao ? C'est important, non ?"


"Huh. Elle a raison."


"Elle comptait... elle compte pour moi."


"Non ?"


hi "D'accord. J'irai la voir après les cours."

show misha hips_grin
with charachange


mi "Super~ ! Je ferai savoir à Shicchan que tu vas bien, alors~ !"


"La cadence revient. J'imagine que ça veut dire que Misha n'est plus en colère contre moi maintenant."

hide misha
with charaexit


"Elle me fait un signe et part en direction du couloir, tandis que je retourne à mon repas."

scene bg school_scienceroom
with shorttimeskip


"Alors que les cours de l'après-midi arrivent à leur fin, je me prépare pour la tâche à venir."


"Je dois voir Emi, Misha avait au moins raison pour ça. Laisser le problème en suspens ne résoudra rien."


"En fin de compte, j'ai besoin de m'excuser pour ce que j'ai dit."


"J'envisage d'aller à sa chambre pour la trouver, mais elle est probablement toujours sur la piste."

scene bg school_courtyard
with locationskip


"Je fais le trajet entre le bâtiment principal et la piste en ayant l'impression d'être un homme condamné."


"J'ai une horrible sensation dans le ventre qui me dit que tout va horriblement se passer, que je ne vais rien accomplir du tout."


"Sauf peut-être planter le dernier clou dans le cercueil de ce qu'Emi et moi avions."

stop music fadeout 2.0

scene bg school_track
with locationskip


"La voilà, comme je m'y attendais, à courir autour de la piste après que tout le monde soit déjà parti se doucher ou dîner."


"Je ne fais pas de signe, et ne signale pas ma présence. Je m'assieds juste sur les gradins et la regarde faire ses tours."

show emi basic_confused_gym:
    center
    xpos 0.6
    easein 0.5 xpos 0.5
with charaenter


"Il lui faut quelques tours avant qu'elle ne me remarque, après quoi elle s’arrête d'un coup, les yeux écarquillés de surprise."

show emi basic_annoyed_gym at center
with charachange

show emi basic_grin_gym
with charachange


"La surprise est rapidement masquée par de la colère qui se met aussi derrière un masque que je connais déjà comme étant impénétrable."


emi "Qu'est-ce que tu fais là ?"


"Pas vraiment la réponse que j'attendais, mais maintenant je n'ai pas tellement le choix."


hi "Je voulais m'excuser pour ce que j'ai dit l'autre jour."

show emi basic_confused_gym
with charachange


emi "L'autre jour ?"

show emi basic_closedgrin_gym
with charachange


"Elle rit, comme une exclamation sèche à ma remarque."

play music music_sadness fadein 0.5

show emi basic_grin_gym
with charachange


emi "Ça fait presque une semaine, Hisao."


hi "Ouais, enfin... mieux vaut tard que jamais, hein ?"

show emi sad_annoyed_gym
with charachange


"Emi croise les bras et me fixe froidement du regard, comme pour me jauger. Après un moment, elle hoche la tête."

show emi sad_grin_gym
with charachange


emi "Hmmph. Tu as raison. L'eau a coulé sous les ponts. Je te pardonne."

show emi basic_grin_gym
with charachange


emi "C'est tout ?"

show emi basic_grin_gym:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None


"Sa question presque impatiente me prend tellement par surprise qu'elle est déjà presque retournée sur la piste avant que je ne pense à lui crier quelque chose."


hi "Non, attends !"

show emi basic_annoyed_gym:
    center
    xpos 0.4
    easein 0.5 xpos 0.5
with charaenter


"Emi s’arrête, se retourne et marche à nouveau jusqu’à moi, respirant un peu fortement et semblant enervée par mon interjection."


emi "Quoi ?"


"D'accord, j'ai besoin d'ajuster le tir, d'une façon ou d'une autre. Je dois savoir où j'en suis, peut-être arranger les choses."


hi "On peut au moins s'asseoir ?"

show emi sad_annoyed_gym at center
with charachange


emi "Je pense que ça ira très bien ici."


hi "D'accord, pas de problème. Écoute, pour nous..."


"Je m’arrête, essayant de penser à une bonne façon de formuler ce que je suis sur le point de dire."


"Mais avant que je puisse me lancer dans une plaidoirie passionnée pour qu'elle me donne une autre chance, Emi a déjà parlé."

show emi sad_shy_gym
with charachange


emi "Il n'y a plus de nous, Hisao."


hi "Pourquoi pas ?"

show emi sad_pout_gym
with charachange


emi "On ne va pas ensemble."


"Elle a sorti cette outrageuse affirmation sans même me regarder dans les yeux."


hi "Je ne te crois pas ! On est très bien ensemble !"

show emi basic_annoyed_gym
with charachange


emi "Dixit le gars s'excusant de s’être fait jeter hors de ma maison la semaine dernière."


hi "C'était une dispute ! J'ai dit quelque chose de vraiment incroyablement stupide et me suis excusé pour ça !"

show emi sad_angry_gym
with charachange


emi "Combien de fois on a déjà discuté du problème qui a commencé la dispute ? Combien de fois je t'ai dit qu'il y avait des limites que je ne franchirais pas, et combien de fois as-tu essayé de les franchir ?"


hi "Parce que tes limites sont stupides !"

show emi sad_annoyed_gym
with charachange


"Emi roule des yeux, croise les bras et penche la tête sur le côté."


emi "Tu vois, Hisao ? C'est pour ça qu'on ne va pas ensemble !"


"Sa voix s'adoucit un peu, et elle s'approche pour me tirer la joue."

show emi sad_grin_gym_close
with characlose


emi "Tu es un bon gars, mais ça ne marche pas nous deux."


"Avec un horrible sentiment, je me rends compte qu'elle s'est entraînée pour ça. Peut-être chaque jour depuis que je suis parti de chez elle."


"Même le tirage de joue semble joué, comme sorti d'un film."


"Elle n'a jamais eu l'intention de me donner une autre chance."


"Merde, je suis sûr qu'elle serait tout à fait à l'aise à l'idée de ne plus jamais me revoir."


hi "Alors, c'est tout ? Rien d'autre à dire que “Bon, c'était bien le temps que ça a duré, mais on s’arrête là.” ?"

show emi basic_closedgrin_gym_close
with charachange


"Ça semble l'amuser bien plus que je ne l'aurais voulu. Elle sort un petit rire assez morbide."


emi "C'est comme ça que j'ai vécu ma vie, Hisao. Tu devrais le savoir maintenant."

show emi sad_grin_gym_close
with charachange


emi "Et c'était bien."


"Un sourire triste. Elle frissonne légèrement, et le sourire s'évanouit."

show emi sad_shy_gym_close
with charachange


emi "Mais c'est fini maintenant, c'est pour le mieux."


"J'ai envie de crier, de lui hurler dessus. Lui faire prendre conscience que c'est stupide, que tout son acte est stupide. Qu'elle a juste peur de moi, peur de ce que signifie être proche de quelqu'un."


"J'ai envie de lui dire que je l'aime et que je ne peux pas juste l'abandonner comme ça."


"Sauf que... ça ne servirait à rien. Elle s'est décidée. C'est fini."


hi "D'accord."

show emi sad_grin_gym_close
with charachange


"Emi hoche la tête, satisfaite. J'ai envie de frapper quelque chose."


emi "Bien."

show emi basic_grin_gym_close
with charachange


"Elle s'illumine de fausse joie."


emi "À plus tard, Hisao."


hi "Non, pas plus tard. Tu ne voudras pas me revoir."

show emi basic_grin_gym_close:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None


"Elle hausse les épaules, comme pour dire “Fais comme tu veux”, et elle me tourne encore une fois le dos, accélérant rapidement dans la courbe de la piste."


"Je me sens engourdi. C'est tout. La fin de la route pour nous, quoi que cela ait pu être. La note finale, du moins."


"Emi tourne sur la piste sans m'accorder un regard. Elle court beaucoup plus vite maintenant, et je ne peux pas m’empêcher de penser à la première course qu'on a faite ensemble."


"J'ai couru pour t'attraper, pour essayer de prouver que je n'étais pas aussi faible que je savais l’être. Mais ça a mal fini pour moi, hein ?"


"Et maintenant, tu es repartie courir trop vite pour moi encore une fois, et je n'ai pas d'autre choix que de courir encore après toi."


"Mais je ne le ferai pas. Pas cette fois. Tu ne me laisseras jamais t'attraper."

stop music fadeout 6.0

scene bg school_dormhisao
with shorttimeskip


"Je ne me rends même pas compte que je m'éloigne de la piste en marchant, ou que j'arrive dans ma chambre, ou que je sors un livre de mon sac pour lire."


"Juste avant de m'endormir, je reprogramme mon réveil. Emi et moi avons eu notre dernière rencontre."

scene black
with shuteye


"Nous ne parlerons plus après ça."





label fr_E27b:



"Bon, que quelqu'un d'autre puisse être au courant de mon problème ne fait pas de mal. Bah, peut-être que Misha pourrait même me donner un conseil."


hi "On s'est disputés chez elle."


hi "Je continue d'essayer de me rapprocher d'elle, et elle ne veut pas me laisser m'approcher, et..."


hi "J'ai dit quelque chose d'idiot et elle m'a mis dehors."

show misha perky_sad
with charachange


mi "Tu lui as parlé depuis ?"


"Misha semble honnêtement inquiète. Je suis surpris, je m'attendais presque à ce qu'elle laisse tomber après avoir découvert quel était le problème."


"Encore plus surprenant est la vitesse à laquelle je me retrouve à tout lui déballer."


hi "Non, pas depuis. Je n'arrive pas à me résoudre à lui faire face après ça."


hi "Je me suis complètement ridiculisé, et maintenant elle me déteste sûrement de toute façon. Surtout que je ne l'ai pas revue depuis."

show misha sign_smile
with charachange


mi "Tu n'es pas très fute-fute, Hicchan."

stop music fadeout 4.0


"Ça ne ressemble pas à un conseil."


hi "Hein ?"

show misha hips_frown
with charachange


"Misha place ses mains sur les hanches et se lance dans un discours qui serait plus plausible s'il venait de Shizune."


mi "La solution à ton problème est simple ! Tu dois aller la voir et t'excuser auprès d'elle ! Laisser les choses comme ça ne fera qu'empirer la situation !"


mi "Et tu ne peux pas savoir qu'elle te déteste sauf si elle te le dit ! Sinon, il n'y a aucune preuve que tes craintes soient justifiées !"


mi "Et si elle compte vraiment pour toi, tu ne devrais pas être inquiet de savoir comment elle prend tout ça ?"

play music music_innocence fadein 1.0


"Soudainement, je réalise qu'elle a raison. J'ai continué de me réveiller aussi tôt parce qu'une partie de moi veut rencontrer Emi sur la piste pour qu'on coure ensemble."


"J'ai continué de courir, parce que je sais qu'Emi s’inquiéterait pour moi si je ne restais pas en bonne santé."


"Quand j'ai été sur le toit hier, j’espérais à moitié qu'elle soit là, et je me suis senti déçu qu'elle n'y soit pas."


hi "Je suis un idiot."

show misha hips_grin
with charachange


mi "Un peu des fois, Hicchan~ !"

show misha sign_smile
with charachange


mi "Alors~ ! Va t'excuser auprès d'elle dès que tu peux, d'accord~ ?"


"J'ouvre la bouche pour dire que j'y vais immédiatement, mais la sonnerie résonne et je réalise que j'ai encore des cours cet après-midi."


hi "Dès que les cours sont finis, je vais la voir. Promis."


hi "Et euh, merci pour le conseil, je crois."

show misha hips_grin
with charachange


"Misha rayonne, comme si j'étais un enfant qui venait d'apprendre l'alphabet."



mi "C'est bien ! Je vais mettre Shicchan au courant que tu vas bien, alors~ !"


hi "Erh, ouais. Fais donc ça."

hide misha
with charaexit


"Avec un signe (et ignorant complètement le fait que des gens commencent à revenir en classe, donc à contresens d'elle), Misha part dans le couloir."


"J'imagine que Shizune et elle ont encore du travail pour le conseil."

scene bg school_scienceroom
with shorttimeskip


"Alors que l'après-midi se passe, je suis impatient que les cours se terminent. J'ai besoin de voir Emi maintenant."


"Je dois essayer d'arranger les choses. Même si Emi me déteste maintenant, je dois au moins m'excuser."


"Je lui dois au moins ça."


"Je devrais aller la voir dans sa chambre ? Non, j'ai décidé, ça reporterait trop les choses. Je connais Emi, je sais que je peux la trouver sur la piste."


"Je n'ai toujours aucune idée de ce que je vais dire quand j'arriverai là-bas, mais je trouve du réconfort dans le fait qu'Emi n'aura probablement rien prévu pour quelque chose comme ça non plus."


"Fais ça à l'instinct. Arrête d’être nerveux, et va juste à la piste. Occupe-toi du reste quand tu y seras."

scene bg school_track
with shorttimeskip


"La piste se fait voir au loin, et le nœud dans mon estomac se resserre. Je résiste à l'envie de me tourner et de partir, et au lieu de ça, je remarque avec satisfaction que j'avais raison, Emi est toujours en train de courir."


"Je ne me fais pas voir immédiatement ; je trouve un siège sur les gradins et la regarde courir, repensant à nos anciennes rencontres."

show emi basic_confused_gym:
    center
    xpos 0.6
    easein 0.5 xpos 0.5
with charaenter


"Après quelques tours de terrain, Emi me remarque et s’arrête d'un coup, une expression de surprise sur le visage qui se transforme vite en colère."

show emi basic_annoyed_gym at center
with charachange


emi "Qu'est-ce que tu fais là ?"


"Pas vraiment la réponse que j’espérais, mais maintenant je n'ai plus tellement le choix."


hi "Je voulais m'excuser pour ce que j'ai dit l'autre jour."

show emi basic_confused_gym
with charachange


emi "L'autre jour ?"

show emi basic_closedgrin_gym
with charachange


"Elle rit, comme une exclamation sèche à ma remarque."

show emi basic_grin_gym
with charachange


emi "Ça fait presque une semaine, Hisao."


hi "Ouais, enfin... vaut mieux tard que jamais, hein ?"

show emi sad_annoyed_gym
with charachange


"Emi croise les bras et me fixe froidement du regard, comme pour me jauger. Après un moment, elle hoche la tête."

show emi sad_grin_gym
with charachange


emi "Hmmph. Tu as raison. L'eau a coulé sous les ponts. Je te pardonne."

show emi basic_grin_gym
with charachange


emi "C'est tout ?"

show emi basic_grin_gym:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None


"Sa question presque impatiente me prend tellement par surprise qu'elle est déjà presque retournée sur la piste avant que je ne pense à lui crier quelque chose."


hi "Non, attends !"

scene bg school_track_on
with locationchange


"Elle ne semble pas m'avoir entendu - ou elle ne veut pas m'entendre - et donc je commence à la pourchasser, ne prenant absolument pas en compte le fait que je ne suis pas habillé pour ça."

scene bg school_track_running
with Dissolve(2.0)


"J'ai mal aux pieds, et le col de ma chemise me donne l'impression d'avoir un nœud autour du cou, mais je continue de la pourchasser, parce que je ne veux pas perdre ma chance."


"Emi n'a pas encore commencé à vraiment accélérer, et c'est la seule raison pour laquelle je suis capable de la rattraper et de tapoter son épaule, juste avant que mes jambes abandonnent l'idée de continuer de courir avec des chaussures."

scene bg school_track_on
with Dissolve(2.0)


"Étonnamment (heureusement ?), courir autant semble avoir servi. J'ai le souffle court, oui, mais au moins mon cœur n'agit plus comme s'il essayait de sortir de ma cage thoracique."

show emi basic_confused_gym_close at center
with charaenter


"Ma tape sur l'épaule a fait s’arrêter Emi, et bien qu'il y ait un instant d’inquiétude quand elle me voit reprendre mon souffle, il semble qu'elle a une assez bonne idée de ce dont je suis capable."


"L’inquiétude n'a pas duré longtemps."

show emi basic_annoyed_gym_close
with charachange


emi "Quoi ?"


"Elle semble tellement irritée que je sois là que je m’énerve presque, mais je suis déjà assez énervé comme ça."


hi "J'ai besoin de m'expliquer. De dire pourquoi je ne peux pas juste laisser les choses comme ça."

show emi sad_annoyed_gym_close
with charachange


"Emi croise les bras et fait rebondir une lame de jambe sur le sol, l’équivalent d'un pied qui tape impatiemment. Même en colère comme elle est, et nerveux comme je suis, elle est toujours magnifique."


emi "D'accord, Hisao. Explique."


hi "Le fait est que je sais que tu es très sensible en ce qui concerne l'accident et ton père."


"Je peux voir le visage d'Emi grimacer à la mention des deux choses qui nous ont lentement éloignés, ou du moins je crois que c'est ça qui nous a éloignés."


hi "Mais c'est pour ça que je veux en savoir plus sur ces sujets, je crois."


hi "Parce que je vois à quel point ils te font mal, et je veux être là pour te réconforter."


hi "Ça me rend malheureux de te voir si fatiguée et déprimée - et ne prétends pas que c'est faux, parce que je sais, d'accord ?"


hi "Je me rappelle cette nuit où tu t'es endormie sur moi et où tu as fait ce cauchemar, et où tu étais contente que je sois là quand tu t'es réveillée."


hi "Je veux être capable d’être là pour toi comme ça, à chaque fois que tu en as besoin."

show emi sad_depressed_gym_close
with charachange


"L'expression sévère s'efface, lentement. Emi m’interrompt avant que je ne puisse continuer."


emi "Juste... arrête-toi là. On ne peut plus se voir, d'accord ?"

show emi sad_pout_gym_close
with charachange


"Elle se précipite maintenant, regardant dans toutes les directions sauf vers moi. Je suis surpris qu'elle ne s'enfuie pas en courant, elle sait que je ne peux pas l'attraper..."


emi "On n'est pas... on n'est pas bien l'un pour l'autre."


hi "Ce n'est pas vrai, et tu le sais."

show emi sad_shy_gym_close
with charachange


emi "Non, c'est vrai. Tu es trop—"


hi "Je sais. Je sais que j'ai été insistant pour connaître ton passé."


hi "Si tu ne peux pas me dire pour l'instant, alors au moins laisse-moi être là, même si je ne connais pas la raison."


hi "C'est bon, je te le promets. Je ne te demanderai pas pourquoi tu as besoin de réconfort, je serai simplement là."

show emi sad_depressed_gym_close
with charachange


"Emi secoue la tête, et des larmes semblent menacer au coin de ses yeux."


emi "Arrête de dire ça !"


hi "Pourquoi ? Parce que tu as peur d'avoir besoin de moi ?"

show emi sad_pout_gym_close
with charachange


emi "Je n'ai pas peur !"


"Je n'arrive pas à éviter de parler sur un ton de réprimande en répondant."


hi "Si, tu as peur. Tu me l'as dit toi-même, non ? Ce n'est pas un problème, vraiment."


hi "Pourtant, je pensais que quelqu'un qui a réussi à se sortir de tout ça et à être aussi énergique et joyeuse que toi, serait suffisamment déterminée pour faire face à cette peur."

show emi sad_angry_gym_close
with charachange


emi "Déterminée ? Qu'est-ce que tu sais de la détermination ?"


hi "Je sais qu'il y a une fille tellement déterminée à prendre soin d'un total étranger qu'elle volerait sa nourriture au festival."


hi "Je sais qu'il y a une fille tellement déterminée à m'aider avec mes problèmes qu'elle ferait un plan diététique et physique complet, et qu'elle ne ferait pas que me dire quoi faire, mais qu'elle suivrait le plan avec moi, même si elle ne pouvait pas courir."


hi "Suffisamment déterminée pour me garder à une distance de sécurité et s'infliger de la douleur émotionnelle si elle pensait que c'était la bonne chose à faire."


hi "Cependant, il y a une chose que cette fille déterminée n'a pas prévu, c'est que je pourrais être aussi déterminé qu'elle, et tout faire pour lui éviter de souffrir."


hi "Je suis tombé amoureux de toi, et je refuse de laisser tomber ça parce que tu as peur de me perdre."

show emi excited_sad_gym_close
with charachange


"Le peu de contrôle qui restait à Emi se brise, et je me retrouve soudainement enlacé par ses bras tandis qu'elle pleure."


emi "Pourquoi est-ce que tu fais ça ? Pourquoi tu ne peux pas me laisser seule ?"

show ev emi_forehead
with dissolve


"Je la serre contre moi et pose un baiser sur sa tête."


hi "Je suis désolé, Emi. Tu m'as aidé quand je suis arrivé, et maintenant je dois t'aider. C'est normal."


emi "Tu es vraiment sans espoir, tu le sais ça ?"


"Elle hoquette et tremble un peu."


hi "C'est drôle, je pourrais dire pareil pour toi."


emi "Tu peux faire quelque chose pour moi, Hisao ?"


hi "Tout ce que tu veux."

scene bg school_track_on
show emi sad_shy_gym_close at center
with charachange


emi "Tu peux partir, maintenant ?"


"J'ai l'impression qu'on vient de m'enfoncer un couteau dans la poitrine."


hi "Partir ?"

show emi sad_pout_gym_close
with charachange


emi "J'ai besoin de... J'ai besoin de réfléchir, d'accord ?"


emi "Je ne peux pas tout te dire pour l'instant. J'ai encore peur, et quand tu es là, je ne peux pas penser clairement."


emi "Mais fais-moi une autre faveur."


hi "Laquelle ?"

show emi sad_grin_gym_close
with charachange


emi "Viens pour courir demain matin ?"


"Je souris, n'ayant pas dû me sentir aussi bien de toute la semaine."


hi "Bien sûr. Je ne manquerais ça pour rien au monde."

show emi sad_grin_gym
with charadistant


"Emi marche à reculons lentement, presque à regret. Elle renifle un peu et me souris, un vrai sourire qui inonde la piste de lumière, surpassant l'obscurité tombante du soir."

show emi basic_grin_gym
with charachange


emi "À demain, Hisao."


hi "D'accord."

show emi excited_amused_gym_close
with characlose

show emi basic_grin_gym
with charadistant


"Elle s'avance soudainement en avant, pose un léger baiser sur mes lèvres et recule timidement."

show emi basic_grin_gym:
    easeout 0.5 xpos 0.3 alpha 0.0
with Pause(0.5)

hide emi
with None


"Tournant sur son pied gauche, elle repart en courant, et je sais que notre conversation est terminée."


"Mes lèvres fourmillent de la chaleur de ce bref baiser et des souvenirs d'autres, plus longs baisers."


"Je retourne à ma chambre avec de l'entrain dans ma démarche."


"Demain quand mon alarme sonnera, je me lèverai."

stop music fadeout 2.0

window hide

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
