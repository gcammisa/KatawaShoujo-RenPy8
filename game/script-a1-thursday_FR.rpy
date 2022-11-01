label fr_A19:

window hide None
scene black
with dissolve

play sound sfx_alarmclock
stop ambient

show bg school_dormhisao
with openeye

play music music_dreamy fadein 2.0

window show


"Le son d'une alarme me tire d'un sommeil agité et je me réveille en sursaut."


"Je reste sous la couverture pendant quelques minutes, rassemblant de l'énergie pour me lever, tout en trouvant des excuses pour savoir pourquoi je ne l'ai pas fait plus tôt."


"Honnêtement, ça m'irait de rester ici toute la journée. L'école est étonnamment épuisante après une longue pause, et le choc culturel n'a toujours pas disparu, je crois."


"Pourtant, en dépit de l'impression que louper les cours est facile ici, je ne pense pas qu'ils vont me laisser m'en tirer aussi facilement."


"Et l'infirmier n'a de cesse de me rappeler de faire de l'exercice aussi."


"Donc finalement je me lève, avale mes médicaments du matin et mets ma vieille tenue de foot."


"Grâce à mon état, j'ai été dispensé de cours de gym à Yamaku, je n'ai donc pas reçu de tenue de gym."


"Je devrais en commander une au cas où, mais porter mes anciens vêtements de footballeur me rend plutôt nostalgique."


"Je ne peux plus les utiliser pour ça maintenant, alors peut-être qu'ils obtiendront une nouvelle vie de cette manière. Un peu comme moi."

label fr_A19a:




"Après tout, si je commence à prendre soin de moi, je ne peux pas le faire à moitié. Je vais commencer par les bases."


"Bases qui incluent le fait de garder le reste de mon corps en forme avec le peu que je peux faire pour renforcer mon cœur."


"Peut-être que je peux revenir à quelque chose qui s'approche d'une vie normale, ou au moins quelque chose où je suis moins enclin à tomber raide mort à chaque instant."

stop music fadeout 2.0


label fr_A19b:



"Ça me semble un peu stupide, vraiment."


"Mais je suppose que de cette façon, je peux au moins dire honnêtement à l'infirmier que je fais quelque chose pour ma santé."


"Non pas que je sois un grand coureur."


"Mais ça ne peut pas faire de mal d'essayer, j'imagine."
stop music fadeout 2.0


label fr_A19c:


show bg school_track
with locationskip

$ renpy.music.set_volume(1.0, 0.0, channel="ambient")
play ambient sfx_emijogging fadein 0.1


"Je suis surpris de découvrir que je ne suis pas le seul présent sur la piste."


"Mais en plus de ça, il y a un visage que j'ai déjà vu auparavant."


"La fille avec des jambes-prothèses qui m'a renversé dans le couloir hier est en train de courir agilement sur la piste, comme une gazelle à moitié mécanique."


"C'est quoi son nom déjà ? Il est court, mais je n'arrive pas à m'en rappeler."


"Elle semble faire des tours de piste avec des petits bonds assez facilement, ses jambes prothétiques claquant en rythme sur la piste."


"Je me demande quelle raison elle a de courir si tôt le matin. C'est peut-être une raison qui ressemble à la mienne, l'infirmier opprime la pauvre fille pour qu'elle coure, tout comme il m'opprime."


"Je ne serais certainement pas ici si ce n'était pas pour ma santé, et s'il ne m'avait pas demandé de le faire."


"Et même sans prendre en compte cela, c'est aussi parce que je voulais m'en occuper rapidement."


"Le fait que je suis moins susceptible de rencontrer quelqu'un qui serait témoin de mes tentatives pitoyables pour retrouver la forme, n'est qu'un heureux accident."


"J'aimerais partir, mais il semble que mon ancien agresseur m'ait remarqué lors de son dernier tour."


"Elle me fait joyeusement un signe de la main et court vers moi."

show emi basic_grin_gym at Slide(0.7,0.5,0.5,0.5,1.0,_ease_in_time_warp)
with charaenter

stop ambient


emi_ "Bonjour ! Tu t'appelles Hisao, c'est ça ?"

play music music_emi fadein 2.0


"Elle sourit, apparemment contente de s'être souvenue de mon nom."

show emi basic_closedgrin_gym at center
with charachange


emi_ "Tu ne dois pas te souvenir de moi."

show emi basic_grin_gym
with charachange


emi_ "Emi ? Je t'ai rentré dedans dans le couloir hier."

label fr_A19i:

show emi excited_circle_gym
with charachange


emi "“Mademoiselle Ibarazaki ?”"


"Elle imite Misha “imitant” Shizune, ne réussissant pas à obtenir le même genre de cadence modérée dans sa voix haut perchée."



label fr_A19j:


hi "Comment pourrais-je oublier une telle euh, présentation mouvementée ?"

show emi sad_shy_gym
with charachange


"Emi a la décence d'avoir l'air vaguement désolée un moment avant de rire."

show emi sad_grin_gym
with charachange


emi "Ouais, encore désolée à ce propos."


hi "Hmm, eh bien, tant que tu n'en fais pas une habitude, je pense que ça ira."

show emi basic_happy_gym
with charachange


emi "Super !"


"Je ne suis pas sûr qu'elle ait réalisé que je blaguais."


hi "Donc cet “espion-conseiller” dont parlait l'Infirmier... c'est toi ?"

show emi basic_closedgrin_gym
with charachange


emi "C'est exact !"

hi "Oh."


hi "Pour être honnête, je m'attendais à quelqu'un du personnel infirmier."

show emi basic_confused_gym
with charachange


emi "Quoi, es-tu en train de dire que je n'ai pas l'air de pouvoir être un espion ?"


hi "Non, je suis plutôt soulagé. J'étais effrayé qu'il puisse y avoir quelqu'un pour surveiller chacun de mes mouvements."


hi "À moins que tu ne sois ici pour cela."

show emi excited_laugh_gym
with charachange


emi "Non, je suis là pour mes propres raisons, l'Infirmier m'a juste demandé si j'avais vu “un étudiant transféré mal coiffé qui a l'air d'être un peu perdu” autour de la piste."


hi "Du coup, tu es là pour quoi ?"


"Emi prend une pose dramatique."

show emi basic_happy_gym
with charachange


emi "L'entraînement !"


hi "Pour quoi ?"

show emi basic_closedhappy_gym
with charachange


emi "La course !"


hi "Ah, je vois. T'es dans l'équipe d'athlétisme, alors ?"


"Emi hoche la tête avec enthousiasme."

show emi excited_proud_gym
with charachange


emi "Ouaip ! Je suis l'une des meilleures coureuses, aussi !"


"Et modeste en plus de ça."

show emi basic_grin_gym
with charachange


emi "Hé, tu devrais nous rejoindre !"


emi "C'est un bon exercice, tu sais."


"Je pense qu'autant d'activité est sûrement hors de question pour moi."


hi "Nan, je ne suis même pas sûr d'apprécier courir autant que ça."


hi "En plus je n'aime pas spécialement le sport en club, tu sais ?"


"C'est vrai. Je n'ai jamais fait du foot de manière sérieuse non plus."


"Je veux dire, je courais partout avec mes amis et tout, mais c'était vraiment la seule raison pour laquelle je jouais."


"Ce n'était pas pour la gloire de me trouver sur le terrain, c'est sûr."


"Emi semble comprendre ma pensée."

show emi basic_confused_gym
with charachange


emi "Je vois, je vois. Pas dans un club et tout."

show emi excited_proud_gym
with charachange


emi "Mais maintenant que tu es ici, j'imagine qu'on va courir ensemble, hein ?"


hi "Quoi ? Euh, bien sûr, je suppose."


"Emi semble réjouie."

show emi excited_joy_gym
with charachange


emi "Tu vas t'échauffer ?"


hi "Les vrais hommes ne s'échauffent pas."

show emi basic_annoyed_gym
with charachange


emi "Oh non, tu dois toujours t'échauffer ! C'est pas bien, Hisao !"

show emi excited_proud_gym_close
with characlose


"Elle me gronde avec enthousiasme, mais elle sourit et se penche plus près."


emi "Je déteste m'échauffer aussi."

show emi excited_laugh_gym_close
with charachange


"Elle rit tout à coup."


emi "Roh, et je n'ai même pas à m'étendre les jambes !"

play sound sfx_gymbounce

show emi gymbounce
with charadistant


"Comme pour confirmer sa déclaration, elle bondit plusieurs fois, donnant une impression passagère de se tenir sur une paire de ressorts. Ses jambes artificielles semblent être plutôt élastiques."


emi "C'est parti !"

stop music fadeout 1.0

play ambient sfx_emijogging fadein 0.3

scene bg school_track_running
with locationchange


"Donc nous nous élançons tous deux sur la piste, et je peux immédiatement voir qu'elle ne mentait pas quand elle disait être bonne à la course."


"Emi se déplace avec fluidité, en se jetant dans la course dans une sorte d'abandon sauvage."


"Je me rends compte que je me concentre plus sur ma façon de courir."




label fr_A19d:


"Mains écartées, hein ?"


"Et quelque chose au sujet de taper avec la plante du pied, plutôt qu'avec les talons..."


"J'essaye de me mettre au rythme d'Emi, mais c'est plutôt difficile."


"Visiblement, je ne suis pas très bon à ça."


"Peut-être qu'Emi pourrait m'aider à mieux courir une autre fois."



label fr_A19e:




"Franchement, je n'arrive pas à me souvenir s'il faut courir d'une façon particulière, mais je ne peux m'empêcher d'avoir l'impression de mal le faire, d'une façon ou d'une autre."


"Je me sens mal à l'aise face à Emi, qui ne semble jamais rompre la foulée."


"..."


"Je ne pense pas vouloir continuer cela."



label fr_A19f:


"Je ne me sens pas faire plus que quelques tours aujourd'hui, et pas plus vite qu'une marche rapide."

scene bg school_track_on
with Dissolve(4.0)


"Emi continue de courir, et ne semble pas remarquer que j'ai arrêté, jusqu'à ce qu'elle me dépasse une deuxième fois."

stop ambient


"Elle s'arrête rapidement, avec une respiration régulière en contraste avec mon souffle un peu haletant."

play music music_emi fadein 2.0

show emi basic_confused_gym at center
with charamoveinleft


emi "Déjà fini ?"


"Je penche la tête tristement."


hi "Heh, ouais."


hi "Je ne suis pas en très bonne forme en ce moment."

show emi basic_grin_gym
with charachange


"Emi hoche la tête, et me sourit une fois de plus."


"Elle semble sourire beaucoup."


emi "Bref, le plus important est que tu aies commencé, hein ?"

show emi excited_amused_gym
with charachange


emi "La prochaine fois, tu dois juste essayer de tenir plus longtemps, et puis plus longtemps, et plus longtemps, et peut-être que tu deviendras super bon !"


hi "Je vais garder ça en tête."


hi "Mais je pense que je vais aller me préparer pour les cours maintenant."


hi "Tu ne devrais pas toi aussi ?"


"Emi hausse les épaules avec indifférence."

show emi basic_grin_gym
with charachange


emi "Nan, j'ai encore plein de temps."


"Je remarque qu'elle ne porte pas de montre."


hi "Tu es sûre ?"


"Un autre haussement d'épaules indifférent."


emi "Pas vraiment... mais je dois finir mon entraînement quotidien !"

show emi basic_closedgrin_gym
with charachange


emi "À plus tard, Hisao !"


hi "Euh, ouais. À plus."

stop music fadeout 5.0
play ambient sfx_emisprinting

hide emi
with easeoutleft

stop ambient fadeout 2.0


label fr_A19g:



"Je ne sais pas vraiment si l'expérience de ce matin est un succès ou un échec, mais j'admets que je me sens plutôt bien d'être un peu sorti."


"Et comme Emi l'a dit, j'ai juste besoin de continuer pour aller mieux, hein ?"


"C'est en s'entraînant qu'on s'améliore, ou quelque chose dans le genre."


"C'est agréable au moins de sentir que j'ai pris un semblant de contrôle sur ma santé."


"Je vais devoir essayer de continuer comme ça."

scene black
with locationskip_in

label fr_A19h:



"En dehors de me sentir plus fatigué qu'avant, je ne pense pas avoir accompli quoi que ce soit aujourd'hui."


"Je suis tellement pas en forme, que c'en est embarrassant."


"Tout ça n'était peut-être qu'une perte de temps. Je trouverai un autre moyen."

scene black
with locationskip_in




label fr_A20:

scene bg school_dormext_half
with locationskip_out


"Je fais demi-tour vers les dortoirs pour me laver et mettre mon uniforme, en essayant de résister à l'envie de prendre une très longue et chaude douche."


"Je suis fatigué d'avoir couru, donc j'ai juste envie de me détendre, mais je ne veux pas laisser de côté mon habitude de me rendre à l'école avant la plupart des autres élèves."

scene bg school_dormbathroom
show steam
show steam2
with shorttimeskip


"Après avoir quand même pris une longue douche, je me sèche et sors de la cabine pour mettre mes vêtements."

show kenji silhouette_naked at center behind steam
with charaenter


"Venue de nulle part, une ombre apparaît dans la brume, menaçante et irradiant d'une intention malveillante. Elle jaillit hors du brouillard."

play music music_kenji fadein 0.3

hide steam
hide steam2
show kenji neutral_naked
show steam as newsteam behind kenji
show steam2 as newsteam2 behind kenji
with charachange


ke "Yo."


hi "Qu'est-ce que tu fais là ? Bordel, tu m'as fait peur ! C'est quoi ton problème ?!"

show kenji tsun_naked
with charachange


ke "C'est moi qui devrais dire ça. Je t'ai cherché partout mec."


hi "Qu'est-ce que tu veux dire par “partout” ?"


"J'ai envie de lui demander s'il me cherchait comme ça, tout nu, mais je me retiens."


"Je me rends finalement compte que je suis toujours nu et mets rapidement ma chemise devant moi, mais Kenji ne semble pas remarquer quoi que ce soit."


"Ses lunettes sont pleines de buée. Mais alors, pourquoi est-ce qu'il ne les essuie pas ? Sa vision est tellement mauvaise qu'il est constamment dans le brouillard ?"


ke "Tu sais, ta chambre, et... Ouais, ben c'est tout. Hé, je veux dire, j'ai dû me lever quand même. Peu importe. C'est pas grave. Je peux t'emprunter de l'argent ?"

show kenji neutral_naked
with charachange


"Il affiche un visage innocent et regarde au loin, essayant très difficilement d'avoir l'air normal. Ça ne fonctionne pas, il est aussi transparent que ses énormes lunettes."


"Parler de façon normale comme ça, sans rien porter, ça me met mal à l'aise."


"En fait, d'une certaine façon, c'est encore plus gênant d'être nu en face de quelqu'un quand il ne peut pas voir que je suis nu. Sans même parler du fait qu'il est nu aussi."


"J'essaye d'ignorer ce fait, sans grand succès."


hi "De l'argent ? Ouais, pas de problème."

show kenji happy_naked
hide newsteam
with charachange


ke "Génial."


hi "Attends, pour quoi faire ?"

show kenji tsun_naked
with charachange


ke "Ehhhh..."

show kenji neutral_naked
with charachange


ke "Tu ne peux pas juste me le donner parce que j'ai eu la bonne volonté de ne pas te faire les poches pendant que tu étais dans la douche ? J'aurais pu, mais je me suis retenu. Au bout du compte, n'est-ce pas l'intention qui compte ? Allez, sois un pote."


"Ça n'a aucun sens. Si c'est l'intention qui compte, je ne dois pas lui donner l'argent, parce que ses pensées étaient clairement impures et ses intentions sont sans doute encore plus sinistres parce qu'il ne peut même pas me dire ce qu'elles sont."

show kenji tsun_naked
with charachange


ke "Je suis vexé mec, mais puisque tu es comme ça, alors très bien, je pense que je n'ai pas le choix. Je veux commander une pizza, et j'ai déjà la majeure partie de ce qu'elle coûte. J'ai besoin de ton aide pour le reste."


hi "J'aurai un morceau de la pizza aussi, hein ?"


ke "Non."


hi "T'es sérieux ?"

show kenji neutral_naked
with charachange


ke "Ouais. Je t'en aurais bien donné, mais tu as cours, tu n'as pas le temps de manger une pizza."


hi "Et toi alors ?!"


ke "Je ne vais pas en classe, je dois attendre la pizza et payer le gars. Et puis la manger. C'est pas facile. Tu dois obtenir la pizza discrètement. Si tu ne le fais pas, tout le monde te verra. Et la pizza. Et ils en demanderont une part."

show kenji tsun_naked
with charachange


ke "C'est un monde cruel là-bas. Tout le monde veut une part. Alors, tu finis sans pizza dans un monde impitoyable. C'est déjà arrivé, c'est pour ça que je le sais."


ke "Chaque jour, je prévois ma vengeance, de sorte que lorsque les gens qui m'ont fait du tort commanderont une pizza, je sois là. Toujours vigilant !"


"Kenji prend une pose dramatique, sans aucune ironie derrière."

show kenji neutral_naked
with charachange


ke "Mais ouais, je n'ai besoin que de 400 yens. S'il te plaît ! Tu es mon seul espoir ! Je ne peux pas aller à l'extérieur et acheter ma propre pizza, c'est trop loin !"


ke "J'essaie de ne pas sortir sauf si c'est absolument nécessaire. Permets-moi de te raconter ce qui s'est passé la dernière fois que je suis sorti sans tout planifier soigneusement à l'avance."


ke "J'étais à l'extérieur. Je ne me souviens plus ce que je faisais. Quelque chose. Attendre ? Peut-être me demandant comment j'étais arrivé là."

show kenji tsun_naked
with charachange


ke "Et là, venant de nulle part, c'est arrivé."


ke "Comme un éclair, fendant le ciel, comme la façon dont tu découpes un sandwich en deux morceaux égaux pour le rendre plus gérable à tenir et à manger, un oiseau m'a fait caca sur la tête."


ke "Ça a été le second moment le plus choquant de ma vie."


hi "C'était quoi le premier ?"


"Il m'ignore et continue. J'ai envie de le saisir et de le secouer. Est-ce qu'il est juste en train d'essayer de garder son élan ? On va dire ça, même s'il est plus probable qu'il ne m'ait juste pas entendu."


ke "C'est comme dans les openings de certains types d'anime, tu sais qu'il y a toujours un moment où le gars principal combat son rival, et ils se foncent dessus en plein vol et entrechoquent leurs épées avec des grandes auras colorées et des gros zooms."

show kenji neutral_naked
with charachange


ke "C'était comme ça, mais avec du caca."


hi "D'accord."

show kenji happy_naked
with charachange


ke "Donc ouais, j'ai besoin d'argent. S'il te plaît ? Ne me laisse pas tomber, mec. J'ai seulement besoin de 1000 yen."


hi "Je croyais que c'était 400."


ke "D'accord."


hi "Quoi ?"


ke "Je te rembourserai, je te le jure."


hi "Tu ferais mieux, c'est le principe d'un emprunt."

show kenji neutral_naked
with charachange


ke "Je ne sais pas quand je serai en mesure de te rembourser."


hi "Tu as une semaine."

show kenji tsun_naked
with charachange


ke "Aaaaaaaaaaaaaaahhhhhhhhhhhhhhhhhhhhhhhhggggggggggghhhhhhhh......"


"Kenji grimace et fait un bruit de vache agonisante, un fait particulièrement inquiétant étant donné que son bâton bouge librement."


ke "Tu n'es pas censé être si coincé à propos de l'argent entre frères d'armes, mec. Les hommes ont suffisamment de problèmes comme ça. Tu savais que les stars du porno mâles gagnent seulement la moitié de ce que gagnent les stars du porno femelles ?"


hi "Ça ne veut rien dire sauf si t'es une star du porno."


ke "Alors peut-être que je suis une star du porno à côté, luttant pour joindre les deux bouts et que je me bats contre le complot féministe, et vous ne pouvez même pas imaginer ce que c'est, espèce de salauds. Personne ne comprend. Personne."


"Les féministes ne sont pas contre la pornographie d'abord ?"


hi "Encore les trucs sur le complot féministe ?"


ke "Ces trucs sont importants. Je vois que tu t'en fous, mais c'est sérieux là. Les féministes... sont un ennemi dangereux, ne te méprends pas. Tu les prends à la légère, et tu te réveilles un matin avec un couteau dans le dos, bam ! Sorti de nulle part ! "


hi "Comment tu te réveilles le matin si quelqu'un t'a poignardé pendant la nuit ?"

show kenji happy_naked
with charachange


ke "Les femmes sont pas douées pour poignarder les gens."


hi "Je croyais que tu venais juste de dire de ne pas les prendre à la légère."

show kenji neutral_naked
with charachange


ke "Eh bien, je veux dire ne les prends pas à la légère pour tout. Individuellement elles ne sont pas une menace, mais s'il y avait un truc, comme une grande guerre, avec des hommes d'un côté, et les forces féministes de l'autre côté, ça serait moche."

show kenji tsun_naked
with charachange


ke "Et ce jour viendra, où les féministes sortiront de leur quartier général international top secret féministe, et diront “C'est parti, bande d'enculés !”"


hi "N'importe quoi, il n'y a pas de gros building quartier général international féministe, où est-ce qu'elles iraient cacher ça ? Il faudrait que ce soit énorme, ça se verrait une grande forteresse avec uniquement des femmes dedans."

show kenji happy_naked
with charachange


ke "Qui a dit que c'était sur terre ?"


"Je me détourne de Kenji et commence à m'entraîner à froncer les sourcils dans un miroir pour que je puisse trouver quel type de froncement serait le mieux pour exprimer mes émotions. Il ne peut pas me voir à cette distance de toute façon."


"Ce qui, malheureusement, signifie qu'il continue de divaguer, sans tenir compte du sens de ce qu'il dit ou de la sensibilité des autres."

show kenji tsun_naked
with charachange


ke "Ouais, il y a une guerre en cours. Une guerre que peu connaissent, mais elle finira par éclater un jour, et englober toutes les régions du monde connu. Là, il faudra choisir un camp. On devra prendre une position. En fait, c'est déjà en train d'arriver."


ke "Imagine ça, le champ de bataille sanglant. Un vicieux conflit sans fin."


ke "J'ai presque abandonné, quand je pensais que cette cause était stupide... Quand je me suis lassé de la noirceur de notre combat... Quand j'ai cru qu'il y avait un raid féministe à cause d'une coupure de courant et que la fin était proche..."


ke "Mais alors j'ai compris que si je renonçais, tout serait fini, et je me suis dit “whoa” et je savais que je devais prendre ça au sérieux. Parce que je suis le dernier homme sain d'esprit dans un monde de fous. C'est une question de devoir."


hi "Ça doit être un mouvement assez merdique s'il repose sur un seul mec nu, divaguant dans une salle de bains face à un autre mec nu."

show kenji neutral_naked
with charachange


ke "Donc je peux avoir l'argent ?"


"Il bloque la sortie, il commence à faire froid parce que je suis toujours nu, et je veux aller en classe, donc j'accepte de lui passer l'argent."

show kenji happy_naked
with charachange


ke "Génial. Merci, mec. On devrait aller au bowling plus tard."


hi "Bowling ?"


ke "Ouais, c'est le sport ultime. Il n'y a presque pas de joueuses de bowling, ce qui en fait presque le plus viril des sports."


ke "Devrais-je porter ma chemise de bowling rose avec des chaussures assorties ou la vert pastel avec les fleurs ?"


hi "Il y a des vêtements pour le bowling ?"

show kenji neutral_naked
with charachange


ke "Peut-être."


hi "Dans tous les cas, tu ferais mieux de me rembourser."


ke "Je peux te rembourser avec des trucs, hein ?"


"Je n'ai pas le temps de lui demander de m'expliquer ce que ça signifie."


hi "Je ne sais pas. Je dois aller en cours, et t'es dans le chemin."

show kenji tsun_naked
with charachange


ke "Oh. Désolé. Ouais, je ne veux pas te retenir, et j'ai quelques trucs à faire moi-même. Le temps est venu."


hi "Le temps pour quoi ?"

show kenji happy_naked
with charachange


ke "J'aime juste dire ça."


ke "D'accord, maintenant le temps est vraiment venu."


hi "Pour quoi ?"

show kenji tsun_naked
with charachange


ke "Je dois utiliser la salle de bains. Sors d'ici."


hi "J'allais le faire ! Et qu'est-ce que ça veut dire ? C'est une grande salle de bains."


ke "Et ? Je dois être seul sinon je ne peux pas y aller. La pression..."


hi "D'accord. Et si quelqu'un vient ici ?"


ke "..."


ke "Je trouverai quelque chose."


"Je lui fais le froncement de sourcils que j'avais préparé, qui s'avère être assez ridicule. Il ne le remarque pas, donc je m'habille et fonce dans ma chambre, ayant l'impression qu'une éternité s'est passée depuis que je me suis levé."

stop music fadeout 2.0

scene bg school_dormhisao
with locationskip


"C'est du temps que j'ai perdu à jamais. Je me vengerai un jour, d'une façon ou d'une autre."


"Mais dans l'immédiat, je dois aller en cours."





label fr_A21:

scene bg school_scienceroom
with locationskip

play music music_normal fadein 2.0


"Je suis la première personne dans la classe aujourd'hui, même si je pense que je suis arrivé un peu trop tôt. De toute façon être assis ici à attendre vingt minutes est préférable à les passer avec Kenji."


"La combinaison de la fatigue, la frustration et l'ennui fait que je commence à me sentir très fatigué."


"J'ai un moment d'absence pendant une seconde, et je me réveille quand ma tête frappe la surface de mon bureau. Frottant mon front, je réalise que c'est une assez bonne raison pour que j'arrête d'arriver si tôt en classe à l'avenir."


"Finalement, j'entends un bruit venant du couloir, et Lilly apparaît dans l'embrasure de la porte. Elle n'est pas dans cette classe, alors elle doit être ici pour autre chose. Peut-être qu'elle cherche Hanako."


"Lilly s'arrête à la porte, l'air hésitant, comme si elle était un vampire qui ne pouvait pas entrer sans avoir été invité. J'envisage de le faire parce qu'elle a l'air plutôt seule, debout comme ça."


"Elle avance de son propre chef quand même, après avoir ajusté sa jupe et sa chemise comme s'il était important d'avoir l'air convenable en entrant dans notre classe."

show lilly cane_concerned at left
with charamoveinleft


li "Excusez-moi."


"Elle parle dans la salle de classe silencieuse avec une voix délicate. Je réalise que le silence pourrait la déstabiliser à cause de sa cécité donc je le brise."


hi "Bonjour Lilly."

show lilly cane_surprised at left
with charachange

show lilly cane_surprised at center
show bg school_scienceroom at bgright
with charamove


li "Hisao ? Bonjour. Je ne t'ai pas entendu venir."


"Je me demande si elle pense que c'est suspect, je ne lui ai rien dit jusque-là. C'est probable. Si je devais mentir maintenant, ça ne ferait que m'enfoncer."


hi "Eh bien, j'étais déjà là, je dormais jusqu'à maintenant."

show lilly cane_listen
with charachange


li "Oh. Par hasard, aurais-tu vu Hanako aujourd'hui ?"


hi "Non, elle semble venir seulement juste avant que ça sonne... ou après. Tu veux que je lui dise quelque chose pour toi ?"

show lilly cane_weaksmile
with charachange


li "Non, c'est bon. C'est étrange, mais je pense que nous sommes les deux seules personnes dans l'école en ce moment. Je n'ai entendu personne d'autre en venant ici."


hi "Je n'aurais pas dû me lever aussi tôt aujourd'hui, j'imagine."

show lilly cane_smile
with charachange


li "Tu te blâmes pour avoir fait quelque chose que les autres personnes devraient aussi faire ? La ponctualité est une bonne chose. Je le pense, du moins."

show lilly cane_concerned
with charachange


li "C'est une matinée très chargée aujourd'hui. Le festival approche à grands pas, et aujourd'hui est la date limite pour l'inscription aux évènements, les rapports budgétaires, et toute la paperasserie officielle."

show lilly cane_weaksmile
with charachange


li "Il se pourrait que tout le monde tente de remplir les formulaires nécessaires à la dernière minute. C'est peut-être pourquoi c'est si calme aujourd'hui."

play sound sfx_doorslam

show lilly cane_surprised
with vpunch


mi "Salut~ salut~ !"

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


"Misha arrive dans la pièce avec Shizune, en criant, avec une sonorité qui fait visiblement broncher Lilly."

show misha hips_smile
with charachange


mi "Salut, Hicchan~ !"


hi "Salut."

show shizu behind_smile
with charachange


shi "..."

show misha hips_grin
with charachange


mi "Regarde, c'est la déléguée de classe~ ! Bonjour~ !"

show lilly cane_smile
with charachange


"Lilly sourit, probablement amusée par Misha - ou Shizune - qui a utilisé le mot “regarde”."

show lilly cane_smile
with charachange


li "Bonjour."

show shizu adjust_smug
with charachange


shi "..."

show misha cross_smile
with charachange


mi "Bien sûr, tu n'es pas la déléguée de cette classe, hein, hein~ ?"

show lilly cane_weaksmile
with charachange


li "Effectivement."


"Lilly semble un peu plus prudente dans ses réponses à Shizune qu'elle ne l'était avec moi. Je crois vraiment qu'elles ne s'entendent pas du tout."


"Puis je me rends compte que Lilly pourrait en fait ne pas savoir si Shizune est présente ou non et qu'elle essaie de détecter si elle est là, pour savoir à qui elle parle."


"Pour ce qu'elle en sait, elle parle à Misha, mais sachant qu'elle et Shizune sont pratiquement inséparables, elle pourrait s'attendre à ce que Shizune soit celle avec qui elle “parle” vraiment."


"Rah, c'est vraiment compliqué. Je décide d'aider Lilly, pour ma propre conscience plus qu'autre chose."


hi "T'es là tôt, Shizune."

show shizu basic_angry
with charachange


shi "..."

show misha hips_frown
with charachange


mi "Tu étais ici encore plus tôt que nous !"


"Misha gonfle ses joues avec colère. Pourquoi est-ce qu'elle est en colère ? Est-ce qu'elle ressent les émotions à la place de Shizune, aussi ?"


"Le fait que Shizune n'ait pas apprécié mon petit commentaire n'est pas tellement bizarre. C'est vrai, j'étais là avant elles, donc dire quelque chose comme ça peut être mal interprété."


"Surtout de la part de Shizune, qui ne peut pas entendre le ton pour juger l'intention."


"Avant même de savoir si je dois m'excuser ou non, Shizune est déjà passée à autre chose."

show shizu adjust_smug
with charachange


shi "..."

show misha hips_smile
with charachange


mi "Déléguée~ ! C'est une bonne chose que tu sois là~ ! Nous devons parler."

show shizu behind_frown
with charachange


shi "..."

show misha hips_grin
with charachange


mi "Le festival est dans trois jours, hein ? Toutes les autres classes ont déjà remis leurs rapports sur le budget prévu pour leurs évènements ! Même les premières années ! Sauf vous~ !"

show misha cross_laugh
with charachange


mi "Wahaha~ !"

show lilly cane_surprised
with charachange


li "Il est encore temps de le remettre, n'est-ce pas ?"

stop music fadeout 2.0

show shizu cross_angry
with charachange


shi "..."

show misha cross_frown
with charachange


mi "Aujourd'hui ! C'est aujourd'hui la date limite ! Tu prends ton temps, n'est-ce pas ? Si je l'avais fait moi-même, j'aurais eu tous les papiers nécessaires il y a des jours de ça, mais il a fallu que quelqu'un~ ! dise “s'il vous plaît, repoussez la date limite !”"

show lilly cane_displeased
with charachange


li "Oui, c'était moi. Planifier quelque chose de cette ampleur n'est pas une mince affaire, et une semaine est un délai trop court pour s'attendre à ce que toute une classe travaille sur un problème aussi complexe et le finisse."

show shizu adjust_angry
with charachange


shi "..."

show misha hips_frown
with charachange


mi "Tu veux savoir ce qui est plus dur que de distribuer des fonds pour l'évènement d'une classe ? Faire la même chose pour chaque classe de l'école~ ! Celle qui fait ça, c'est “moi” !"


"Misha met ses mains sur ses hanches et se redresse. Woaw, elle est vraiment dans le rôle. Lilly ne semble pas être très amusée, cependant."


hi "Hey, Shizune, tu n'es pas un peu trop dure avec elle ? Il reste encore un jour entier."

show lilly cane_weaksmile
with charachange


li "S'il te plaît, Hisao. C'est bon."


"Lilly semble contente que je prenne sa défense, mais est un peu troublée que je puisse penser qu'elle ne sait pas se débrouiller toute seule."

show lilly cane_listen
with charachange


li "Si c'est à propos du budget, alors je suis déçue que vous pensiez que j'ai oublié. Je sais à quel point c'est important."

show shizu behind_frustrated
with charachange


shi "..."

show misha hips_grin
with charachange


mi "Alors~ ! Je peux l'avoir s'il te plaît ?"


hi "Shizune, elle ne doit pas l'avoir sur elle, là, tout de suite."

show lilly cane_displeased
with charachange


li "Je ne l'ai pas ici en ce moment. J'ai demandé à deux élèves de s'en occuper pour moi. Des élèves de ma classe."


"Elle appuie sur la dernière phrase, à ma grande surprise. Elle est au courant des efforts de Shizune et Misha pour m'enrôler dans le Conseil des Étudiants ?"


"Je suppose que ça a dû finir par se savoir, donc maintenant elle se sert de moi comme un argument contre Shizune. Ça devient de mieux en mieux..."

show shizu cross_angry
with charachange


shi "..."

show misha hips_frown
with charachange


mi "C'était ta responsabilité~ ! Un rapport sur le budget n'est pas quelque chose que tu peux juste déléguer comme ça ; vu que tu es la représentante de classe, c'est à toi de faire ces choses ! C'est horrible ce genre de mépris envers la procédure~ !"

show lilly cane_listen
with charachange


li "Les deux élèves les ont complétés, étant capables de le faire, mais ils ont été malades récemment, donc ils ne pouvaient pas venir à l'école me les rendre. Si tu veux, je ferai des excuses en leurs noms pour avoir été malades."

show misha hips_grin
with charachange


mi "D'accord~ !"


"Bien que Misha ne remarque pas la pique de Lilly, ce n'est pas le cas de Shizune, qui semble être déchirée entre être offensée par l'audace de Lilly et sauter de joie devant la perspective du challenge."

show shizu behind_frown
with charachange


shi "..."

show misha hips_smile
with charachange


mi "Lilly, ils ne vivent pas au dortoir ? C'est à cinq minutes d'ici, tu sais~."


mi "Qu'est-ce qu'ils pourraient avoir à faire dans leurs vies très occupées qui les empêcherait de prendre cinq minutes... pour déposer quelque chose qui va réjouir la classe tout entière ?"


show shizu adjust_angry
with charachange


"Lilly ouvre la bouche pour dire quelque chose, mais Shizune comble le vide entre elles et commence à faire des signes avec fureur, agitant ses mains dans tous les sens, comme un chef d'orchestre."


"Misha fait de son mieux pour essayer de transmettre la même passion, mais n'arrive pas à perdre son ton enjoué habituel. Le résultat est intéressant et quelque peu surréaliste."


shi "..."

show misha cross_frown
with charachange


mi "Et puis c'est quoi cette attitude~ ? J'ai dit que ce n'est pas quelque chose que tu devrais déléguer, tu es déléguée de classe ou pas ?"

show misha hips_frown
with charachange


mi "Dis-moi les noms de ces deux étudiants, ils devraient avoir ton poste si tu ne peux même pas gérer quelque chose d'aussi simple toi-même."

show lilly cane_displeased
with charachange


li "Une formalité ne peut représenter l'ensemble de ce que je suis censée faire."


"Le ton de Lilly devient légèrement impatient, mais elle ne laisse pas Shizune voir à quel point elle devient instable. Elle ne dévoile pas son jeu."


"Shizune, d'autre part, réajuste joyeusement ses lunettes du bout des doigts, sachant que Lilly ne peut ni entendre ni voir à quel point elle est excitée."

show shizu adjust_smug
with charachange


shi "..."

show misha hips_grin
with charachange


mi "Bien sûr, tu en fais tellement, déléguée~ ! Ce doit être très difficile d'être à ta place~ !"

show lilly cane_listen
with charachange


"Lilly se pince les lèvres à l'écoute des mots de Misha, comprenant clairement l'intention derrière, même si Misha les délivre sans le soupçon de sarcasme qu'ils sont censés avoir."


"Shizune et Lilly ne s'aiment pas l'une l'autre, c'est clair, mais ça semble aller trop loin. Apparemment Lilly en a assez et est prête à contre-attaquer."

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



li "J'étais justement en train de discuter du rapport sur le budget. Mais si tu viens me trouver pour t'assurer que je n'oublie pas mon travail, c'est que tu as déjà fini celui du conseil des étudiants ; tu dois vraiment être talentueuse."

play sound sfx_slide
show ev showdown_large:
    ease 0.2 crop (1400,160, 800, 600)
with None


mi "Serais-tu en train de m'accuser de me relâcher ? Il semble que tu me confondes avec toi~ !"

play sound sfx_slide2
show ev showdown_large:
    ease 0.2 crop (280,100, 800, 600)
with None


li "Je ne pense pas. Ce serait vraiment difficile pour moi ; me comparer à toi."


play sound sfx_slide2
show ev showdown_large:
    ease 0.2 crop (1400,160, 800, 600)
with None


mi "Tu as raison, la différence entre nous est comme celle entre l'enfer et le paradis."

play sound sfx_slide
show ev showdown_large:
    ease 0.2 crop (280,100, 800, 600)
with None


li "Et il n'est pas dur de deviner quel côté tu représentes."

$ _window = False

play sound sfx_thunder
scene ev showdown
with Fade(0.2, 0.0, 1.5, color="#FFF")

window show


"L'air entre elles ondule à cause de la chaleur de leur hostilité. Quoique, pas vraiment. Elles ne peuvent plus continuer à le dissimuler, cependant. Même Misha a l'air de commencer à comprendre la vraie nature de cette conversation."

stop music fadeout 5.0

scene bg school_scienceroom
show lilly cane_listen at left
show misha perky_confused at center
show shizu basic_angry at right
with flash

shi "…"

show misha sign_confused
with charachange


mi "Hicchan~ ! Ne te relâche pas non plus~ !"


hi "De quoi est-ce que tu parles ?"

show shizu basic_frown
with charachange


shi "..."

show misha hips_smile
with charachange


mi "Ne prends-tu pas part au festival, Hicchan ? C'est le cas, n'est-ce pas? Alors~ ! J'espère que tu vas en faire beaucoup plus pour être sûr que ça se passera plus en douceur qu'avec cette personne~ !"

label fr_choiceA21:
menu:
    with menueffect
    "Je ne comprends pas pourquoi Shizune est soudainement en colère contre moi."
    "Ne me mêle pas à ça ! J'ai fait ma part !":




        return m1
    "Roh c'est bon. Lâche-nous un peu Lilly et moi...":


        return m2

label fr_A21a:


hi "Pourquoi est-ce que je suis mêlé à ça, encore ? J'ai fait plus que ma part, je pense."


hi "Si t'es en colère contre Lilly, ça n'a rien à voir avec moi."

show lilly cane_reminisce
with charachange


li "Attends une seconde... es-tu en train d'insinuer que la présidente a plus de raisons de crier sur moi que sur toi ?"


"Et merde, je pense que j'aurais pu mieux formuler ma phrase."


hi "Non, je n'en sais rien mais... Je veux dire..."

show shizu behind_frown
with charachange


shi "..."

show misha perky_confused
with charachange


mi "Qu'est-ce que tu dis, Hicchan ?"


hi "C'est juste que je pense que c'est assez injuste que tu dises cela, vu que je vous ai déjà aidées."


"L'ambiance a changé. Cela ressemble à une épreuve de force entre deux cowboys maintenant. Bon, c'était déjà le cas avant aussi, mais cette fois le pointeur de Shizune est sur moi."


"Et celui de Lilly aussi, même si elle reste silencieuse. J'ai peur de l'avoir énervée par mégarde."

show shizu cross_angry
with charachange


shi "..."

show misha hips_frown
with charachange


mi "Tu veux dire que j'ai tort ?"


"C'est une situation vraiment dangereuse."


hi "Il est trop tôt pour en discuter avec toi. ...Oui, je crois qu'il est injuste que tu sois après moi comme ça."

show shizu behind_frustrated
with charachange


shi "..."

show misha hips_smile
with charachange


mi "Hicchan, tu en demandes trop~ ! Mais~ ! Tu n'as pas tort. Ok, ok ok~ ! Tu n'es pas paresseux, Hicchan."

show misha hips_laugh
with charachange


mi "Hahaha~ !"


"Shizune remonte ses lunettes avec son pouce, approuvant presque."

show shizu adjust_happy
with charachange


shi "..."

show misha perky_smile
with charachange


mi "C'est bien ! Si tu n'es pas inutile, tu ne devrais pas laisser qui que ce soit dire que tu l'es~ ! Mais la prochaine fois que je le dirai, ça sera vraiment parce que tu m'as déçue comme Miss la Déléguée de Classe ici, garde ça en tête !"

show lilly cane_displeased
with charachange


"Lilly encaisse la pique silencieusement, un air venimeux figé sur son visage."

show misha hips_smile
with charachange


mi "Déléguée~ ! Shicchan dit : “N'oublie pas le rapport, s'il te plaît~ !”"


li "Je ne l'oublierai pas."

show lilly cane_listen
with charachange


li "Ce sera tout ?"

show misha hips_grin
with charachange


mi "Yup~ !"


li "Sur ce, bonne journée à vous tous."


"Si cela était possible, sa voix aurait coupé l'air de la classe en deux."

hide lilly
with charaexit


"Lilly quitte la salle, naturellement de mauvaise humeur, mais parvient encore à être aussi posée et calme que d'habitude."

show misha hips_grin at twoleft
show shizu adjust_happy at tworight
show bg school_scienceroom at bgleft
with charamove


hi "Shizune, tu es vraiment allée un peu trop loin cette fois."

show misha perky_smile
with charachange


mi "C'est vrai, Shicchan, juste un peu~."


"Si je m'attendais à ce que Shizune admette à contrecœur que j'ai raison, je crois que je m'attendais à trop. Elle ne répond pas."

show shizu basic_normal2
with charachange


shi "..."

show misha cross_laugh
with charachange


mi "Hahaha~ ! Shicchan pense que tu devrais t'occuper de tes affaires."

show misha hips_smile
with charachange


mi "Hicchan, nous avons quelques trucs de dernière minute à faire avant les cours~ ! Il se peut que nous soyons en retard donc~ ! Tu peux nous couvrir s'il te plaît ?"


hi "Ouais."

show misha cross_grin
with charachange


mi "Parfait~ ! Cool~ ! Bien~ ! Merci, Hicchan !"

hide misha
hide shizu
with charaexit


"Elles sortent de la classe même s'il ne reste que dix minutes avant que la cloche ne sonne et signale le début du cours."



label fr_A21b:


hi "Hum, je suis le nouveau, tu te souviens ?"


hi "C'est pas comme si je pouvais faire grand-chose, même si je le voulais."

show lilly cane_displeased
with charachange


li "C'est vrai, il ne faut pas s'attendre à ce qu'un étudiant transféré se plonge directement là-dedans pendant sa première semaine."


"Que Lilly se mette de mon côté est curieusement réconfortant, donc je décide de faire de même."


hi "Ouais, t'es injuste avec nous deux."

show shizu behind_frustrated
with charachange


shi "..."

show misha hips_frown
with charachange


mi "Excuse-moi, mais Mademoiselle la Déléguée a eu tout le temps de s'occuper de son rapport."


mi "Et toi Hisao, nous t'avons offert à plusieurs reprises un poste pour aider aux travaux du conseil des étudiants, mais tu as refusé de t'engager à faire de ce festival un succès."


hi "Ouais, mais comme je l'ai dit plus tôt, je ne suis pas sûr que..."


"Je n'ai pas le temps pour ça maintenant, peu importe ce que je fais, ça signifie se laisser entraîner dans une confrontation avec Shizune, et c'est ce qu'elle veut."


hi "Peu importe. Oublie ça."


label fr_A21c:


"Je leur tourne le dos."

hide shizu
hide misha
with charaexit

show lilly cane_displeased at center
show bg school_scienceroom at bgright
with charamove


hi "Lilly, le cours va bientôt commencer, nous pourrons en reparler plus tard. Je vais dire à Hanako que tu la cherches."


"Je peux sentir Shizune se raidir. Peut-être que c'est la première fois qu'elle se fait ignorer d'une façon aussi abrupte."

show lilly cane_smile
with charachange


li "Merci, Hisao. Je m'en vais maintenant."


"Elle m'accorde le plus beau sourire que j'ai vu de toute la semaine, puis tourne les talons pour sortir."

hide lilly
with charaexit


"Dès que Lilly franchit la porte, je me sens soudainement réticent à me tourner vers Shizune."


"Je peux sentir ses yeux brûlants dans mon dos, et je ne peux pas me résoudre à la regarder. Elle doit être furieuse. Je continue d'espérer que Misha dise quelque chose pour soulager la tension, mais c'est vraiment trop en demander."


"Finalement, je retourne à ma place, écoutant le bruit des pas de Shizune pendant qu'elle sort de la pièce. Elle ne revient que quelques minutes avant le début du cours."



label fr_A21d:

hide shizu
hide misha
hide lilly
with charaexit


"Je leur tourne le dos."


"Je reviens à mon siège et n'écoute pas la fin de la dispute entre Lilly et Shizune."


"Finalement, Lilly quitte notre salle de classe, et Shizune et Misha s'assoient aussi, sans me parler."


"Je peux sentir les yeux brûlants de Shizune dans mon dos. Elle est probablement fâchée contre moi, mais je suis aussi fâché contre elle."


"Je ne comprends pas pourquoi elle m'a m'impliqué dans le débat."





label fr_A22:

scene bg school_scienceroom at bgleft
with shorttimeskip

play music music_daily fadein 0.5


"Hanako n'est pas venue aux cours du matin, laissant son siège vide et solitaire à l'arrière de la salle de classe."


"Je dois lui dire que Lilly la cherchait si je la vois plus tard."


"Après les évènements de ce matin, les cours sont plutôt ennuyeux en comparaison. Je tourne paresseusement les pages de mon manuel."


"Nous avançons à la même vitesse chaque jour, donc lire en avance me donne plus ou moins un aperçu du sujet de la leçon du lendemain."


"L'horloge de la classe est insupportablement bruyante. Le professeur ne dit rien depuis un petit moment, préférant à la place recopier des rangées et des rangées d'équations tirées directement du livre."


"Le cliquetis rythmé de la craie sur le tableau semble se synchroniser à la perfection avec le tic-tac de l'horloge."

show misha cross_smile_close at offscreenleft
with None

show misha cross_smile_close at Transform(xpos=0.1, xanchor=0.5)
show bg school_scienceroom at center
with charamove


"Je commence à copier les équations juste pour passer le temps, ne remarquant pas la tête de Misha par-dessus mon épaule jusqu'au moment où elle est presque au-dessus de moi."


hi "Qu'est-ce que tu fais ?"


"J'essaie de trouver un équilibre entre être suffisamment silencieux pour ne pas attirer l'attention sur moi, mais assez bruyant pour attirer la sienne."

show misha cross_grin_close
with charachange

show misha cross_grin_close at twoleft
show bg school_scienceroom at bgright
with charamove


mi "Qu'est-ce que tu fais, Hicchan~ ?"


"Un éclair de panique me traverse quand Misha se met à parler à un volume normal, alors je lui sors une réponse hâtive, gardant toujours ma voix basse, malgré le fait qu'elle ait annihilé tout espoir que j'aie pu avoir d'être discret."


hi "Je recopie ce truc, qu'est-ce que tu fais ? Pourquoi si bruyamment ?"

show misha perky_confused_close
with charachange


mi "Aw~, vraiment ? Mais tout est dans le livre... C'est pourquoi personne d'autre ne le recopie~ !"


hi "Je sais, pourquoi es-tu aussi bruyante ?"

show misha hips_grin_close
with charachange


mi "Pourquoi es-tu aussi silencieux, Hicchan ? C'est dur de t'entendre."


"Je regarde autour pour voir si quelqu'un a remarqué notre conversation, et il est vraiment évident que tout le monde l'a remarquée, même le professeur."

show shizu behind_smile at right
with charamoveinright


"Shizune sourit timidement et je commence à me demander si Misha ne fait pas ça parce qu'elle lui a demandé."


"C'est à cause de ce qui s'est passé entre Lilly et elle plus tôt ?"


"C'est ce que l'on obtient en essayant d'être raisonnable ? Pour essayer de prendre le train en route ? Shizune est vraiment trop orgueilleuse, mais maintenant je devrais m'attendre à ce genre de comportement de sa part."


hi "Pourquoi est-ce que tu fais ça ?"

show misha perky_confused_close
with charachange


mi "Hein ?"


"Misha ne se rend pas du tout compte du regard inconfortable que nous porte le professeur. Pendant un bref instant, j'ai cru que les choses allaient mal tourner, mais le professeur regarde simplement au loin, comme si ça n'en valait pas la peine."


"J'imagine que c'est une bonne chose, et je m'affaisse de soulagement dans mon siège."

scene bg school_scienceroom at bgright
with shorttimeskip


"Le reste de la journée se passe sans problèmes, et cette fois je suis en mesure de l'apprécier comme il se doit."

play sound sfx_normalbell


"Quand la cloche sonne, je ne suis pas pressé donc je reste un moment, relisant ce qu'on a vu en classe. Je préfère partir le dernier de toute façon, pour ne pas avoir affaire aux attroupements dans les couloirs."


"Je remarque que Shizune et Misha sont restées aussi, parlant à quelqu'un venant d'une autre classe."


"Shizune fait des signes si rapides que ses mains font les mêmes bruits que des épées fendant l'air."


"Misha essaye désespérément de tenir le rythme, mais il est clair qu'elle parvient à peine à comprendre elle-même."


"Je baisse la tête. Je ne sais pas de quoi elles parlent, mais ça a l'air d'être une affaire sérieuse. Probablement bien plus importante que mon cas. Non seulement cela, mais Shizune semble en colère, bien que ça puisse aussi n'être que sa sévérité normale."


"Shizune signe tellement vite que ses poignets craquent, et Misha lutte pour ressortir cela sous forme de mots."


"Parfois, elle bloque comme si elle disait une phrase difficile à prononcer. Et puis en plus de ça, elle doit traduire en signes tout ce que dit en retour l'autre jeune fille."


"Ça semble être une tâche difficile."


"Misha a l'air fatiguée, comme si elle était sur le point de s'évanouir."


"Heureusement pour elle, leur discussion est bientôt terminée et les filles s'asseyent de nouveau à leurs places."

show shizu behind_blank at tworight
show misha perky_sad at twoleft
with charaenter


mi "Uwaaah ! Je suis fatiguée !"


"Elle suspend sa tête mollement au-dessus de son bureau, l'air épuisée."


hi "Les préparations du festival doivent être dures pour toi."


"En effet, les gens de cette école semblent prendre le festival très au sérieux. Chaque fois que je vois des gens se balader avant et après les cours, ils parlent toujours de leurs plans pour le festival."


"C'est pas mal de voir tout le monde être aussi enthousiaste à ce sujet."


"Je suis probablement le seul qui n'a rien à faire."

show shizu basic_normal
show misha perky_confused
with charachange


"Shizune commence à m'adresser des signes et Misha redresse la tête, regardant ses mains avec les yeux un peu dans le vague."

show shizu behind_frown
with charachange


shi "..."


"Elle fait des signes da façon brute, avec de grands gestes théâtraux."


"Misha traduit ses signes pour moi."


"Elle le fait si bien que c'est presque Shizune qui parle, transmettant ses pensées directement par Misha."

show misha cross_frown
with charachange


mi "Eh bien, nous sommes du conseil des étudiants, tu sais, donc nous sommes très occupées."


hi "Sarcasme ?"

show misha perky_confused
with charachange


mi "Huh ?"


"Le ton des actions de Shizune me fait penser qu'elle “parle” avec dédain, mais Misha interprète ça normalement, remplaçant le “ton” de départ de Shizune, par sa propre attitude face aux choses. Je ne pense pas m'y habituer un jour."


hi "Laisse tomber."


hi "Comment je pourrais l'oublier, sachant que vous m'incitez à vous rejoindre au moins deux fois par jour ?"

show misha cross_laugh
with charachange


mi "Hahaha~ ! Mais, Hicchan, certains pourraient dire qu'il y a trop de travail."

show shizu basic_normal2
with charachange

show misha perky_sad
with charachange


mi "Ce serait bien si les élèves montraient un peu plus de soutien pour leurs dirigeants, une certaine considération pour ceux qui travaillent si dur afin de rendre tout cela possible."

show shizu behind_frown
with charachange

show misha perky_smile
with charachange


mi "Avec peut-être, par exemple, un peu d'aide. C'est trop demander, non ? Yep~ ! De l'aide serait appréciée~ ! Venant d'étudiants comme toi~ !"

show shizu adjust_angry
with charachange

show misha hips_frown
with charachange


mi "Si les élèves montraient leur dévouement et leur esprit scolaire, et proposaient de l'aide, mais bon, je n'en ai pas vraiment besoin..."

show shizu behind_smile
with charachange

show misha hips_smile
with charachange


mi "Mais je ne refuserais pas nécessairement... Donc~ ! ça serait bien si quelqu'un voulait..."

stop music fadeout 2.0

show shizu adjust_blush
show misha perky_confused
with charachange


mi "Oh ? Bonjour~ !"

show shizu adjust_blush at offscreenleft
show misha perky_confused at Transform(xanchor=0.5, xpos=-0.45)
show bg school_scienceroom at bgleft
with charamove

show hanako emb_timid at Transform(xanchor=0.5, xpos=0.93)
with charamoveinright

play music music_pearly fadein 1.0


"Je regarde par-dessus mon épaule et vois Hanako regarder timidement dans la salle de classe, la plus grande partie de son corps étant cachée derrière la porte."

show misha perky_smile at Transform(xanchor=0.5, xpos=0.15)
with charamove


mi "Salut ! Encore à jouer la délinquante ?"

show hanako emb_blushtimid
with charachange


"Hanako rougit beaucoup à la pique de Misha, même si ce n'était qu'une blague."

show shizu basic_angry at Transform(xanchor=0.5, xpos=0.35)
with charamove


shi "..."

show hanako emb_downsad
with charachange

show hanako emb_downsad at Transform(xanchor=0.5, xpos=0.97)
with charamove


"Shizune la regarde fixement, ce qui pousse Hanako à baisser le regard et à revenir au point où seuls ses doigts sont visibles, repliés nerveusement sur le montant de la porte."


"Peut-être qu'elle montre son aversion pour Hanako par association avec celle pour Lilly."


"C'est apparemment ça, et Hanako en a aussi probablement conscience."


"Elles semblent avoir momentanément oublié qu'elles essayaient de me convaincre de rester pour la journée."


hi "Qu'est-ce qu'il y a, Hanako ?"

show hanako emb_timid
with charachange


ha "Li... Lilly est là ?"


mi "Désolée, Satou n'est pas ici. Elle, euh, est passée ce matin cependant."

show hanako emb_downtimid
with charachange


"Hanako continue de regarder Shizune avec inquiétude, qui la fixe aussi avec son regard analytique. Qu'est-ce qu'elle essaie de faire ?"


"Bien sûr, Shizune ne détourne pas le regard, et elle est suffisamment intimidante comme ça, je peux à peine imaginer à quel point Hanako doit être terrifiée."


"Ça reste drôle de regarder la réaction d'Hanako face au comportement normal de Shizune. C'est ce qui arrive lorsque deux personnes différentes à l'extrême se rencontrent, apparemment."

show hanako emb_timid
with charachange


ha "Tu... tu sais où elle est ?"

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange


mi "Si elle a un peu de bon sens, elle est dans sa salle de classe, à travailler sur leur projet du festival. Mais qui sait où cette fille est en train de flâner."



label fr_A22a:

show misha hips_grin at Transform(xanchor=0.5, xpos=0.15)
with charachange


mi "Elle doit être en train de se laisser aller quelque part, juste comme Hicchan~ ! Wahaha~ !"


"Rah, pourquoi est-ce qu'elles ont besoin de dire des trucs comme ça ?"



label fr_A22b:

scene bg school_scienceroom at bgleft
show shizu behind_frown at Transform(xanchor=0.5, xpos=0.35)
show misha hips_frown at Transform(xanchor=0.5, xpos=0.15)
show hanako emb_timid at Transform(xanchor=0.5, xpos=0.97)
with None



mi "Elle doit être en train de se laisser aller quelque part~ ! Quelle femme inutile~ !"

show hanako emb_downtimid
with charachange

hide hanako
with easeoutright


"Hanako hoche rapidement la tête et s'en va avec hâte, évidemment pour éviter tout autre contact avec Shizune. Malheureusement, ça fait qu'elles tournent totalement leur attention vers moi."

stop music fadeout 2.0

show shizu behind_frown at tworight
show misha hips_frown at twoleft
show bg school_scienceroom at bgright
with charamove

show misha hips_grin
show shizu behind_smile
with charachange


mi "Mais Hicchan n'est pas inutile, hein ? Hein ? Il l'a dit lui-même~ ! Wahaha~ !"


"Je peux voir où ça va, et je ne veux pas en faire partie, pas après l'expérience d'hier."


hi "Bon, bonne chance pour vos préparations..."


"Je commence à ranger mes affaires, prêt à me diriger vers la sortie."


"Malheureusement, je suis à l'autre bout de la salle."


"La courte distance jusqu'au dortoir me semble être comme un vaste No Man's Land."

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


"Shizune et Misha commencent toutes deux à manœuvrer doucement devant moi, me coupant la route de sortie d'une façon prudente et troublante qui me fait penser à une confrontation entre navires de combat."

show misha hips_grin
with charachange


mi "Je pense que Shicchan dit que tu pourrais nous aider, Hicchan~ !"


hi "Ha, je ne m'en étais pas rendu compte, elle est tellement subtile."

show misha perky_confused
with charachange


mi "Mais~ ! c'est le but, alors, s'il te plaît ? Je ne peux pas continuer, on doit construire des stands pour le festival, et la plupart d'entre eux, c'est nous qui devons le faire, tu peux le croire ?"

show misha perky_sad
with charachange


mi "Marteler des planches ensemble, encore et encore, pendant des heures, c'est vraiment dur !"


mi "Je suis tellement habituée à le faire que je faisais le mouvement en classe, et je ne le savais même pas !"


"Elle frappe son bureau plusieurs fois, imitant des coups de marteau."


mi "C'est tellement répétitif, je ne peux plus le supporter ! Et hier, je clouais des planches les unes sur les autres..."


mi "Et c'était juste une pile de planches clouées ensemble, alors j'ai dû les démonter et tout refaire encore une fois, et je me suis fait crier dessus~ !"


hi "Euh..."

show misha perky_smile
with charachange


mi "Donc..."

show misha hips_grin_close
with characlose


"Elle attrape mon épaule d'une main et sourit, faisant courir rapidement sa langue le long de ses dents avec un air malicieux."


mi "Tu as quelque chose de prévu pour aujourd'hui, Hicchan ?"


mi "Je me demande si tu as quelque chose~."


hi "Évidemment que j'ai des trucs de prévus..."

show misha perky_confused_close
with characlose


mi "Tu vas nous aider, hein ?"


"Je remarque que ses mains bougent constamment."


"Elle convertit en signes tout ce qu'elle et moi disons, pour que Shizune puisse comprendre."


"Shizune est plutôt silencieuse aujourd'hui. Elle est toujours en colère ? Probablement au moins un peu. Je peux le voir à ses yeux. Mais, ça peut aussi être une façon d'essayer de me culpabiliser pour que je lui prête main-forte."


"Je dois trouver un moyen de me sortir de cette situation."


hi "Hé, il faut que j'y aille maintenant. À la bibliothèque. Tu sais, les devoirs..."


hi "Je dois y aller, hein ? Je dois faire preuve de diligence, parce que je suis un nouvel étudiant, et tout, donc je dois faire une bonne impression, hein ? Ouais..."


hi "À plus tard, alors !"

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


"Je me tourne pour aller à la porte, mais Shizune me bloque le chemin, les bras croisés contre sa poitrine et un regard sévère sur le visage."

show shizu basic_angry_close
with charadistant


"Elle agite un doigt moqueur et commence à faire des signes à Misha à la manière d'un chef d'équipe qui donne des instructions à ses soldats."

show shizu basic_angry
with charadistant

show misha perky_smile at twoleft
with charamove


mi "Il ne me semble pas que tu étais sur le point de te rendre à la bibliothèque, Hicchan~ !"

show misha hips_grin
with charachange


mi "C'est vrai, Shicchan~ il me semble qu'il allait probablement se reposer pour le reste de la journée."

show misha hips_laugh
with charachange


mi "Hahaha~ ! Wahaha~ ! Tu es cerné~ !"

show shizu behind_frown
with charachange

shi "…"

show misha hips_smile
with charachange


mi "Allons à la salle du conseil des étudiants~ !"


"Elle laisse échapper un gloussement, et se met à rire ouvertement."

show misha cross_laugh
with charachange


mi "Je suis désolée, Hicchan, je me sens mal, mais ça marche pour tout le monde, hein ?"

show shizu basic_normal2
with charachange

shi "…"

show misha sign_smile
with charachange


mi "C'est vrai, Shicchan ! Oui~, c'est un bon point aussi."

show shizu behind_blank
with charachange

shi "…"

show misha hips_smile
with charachange


mi "Oui, c'est bénéfique pour tout le monde, ça résout tous nos problèmes."

show shizu basic_frown
with charachange

shi "…"

show misha hips_frown
with charachange


mi "Ouais ouais~ ! J'ai également pensé qu'il serait plus sensible à nos efforts."

show misha hips_frown_close
show shizu basic_frown_close
with characlose


"Elles se rapprochent, comme si elles étaient sur le point de bondir."


hi "Hé les filles, deux contre un, c'est pas très loyal, vous croyez pas ?"

show shizu behind_blank_close
with charachange

shi "…"


"Elle continue de regarder devant elle, impassible, et laisse apparaître un sourire sinistre."

show shizu basic_sparkle_close
show misha hips_grin_close
with characlose


mi "Allons, nous avons beaucoup de travail à faire ! Allons à la salle du conseil des étudiants~ !"


hi "Bah, je sais pas..."

show misha cross_laugh_close
with characlose


"Misha rit."

show misha hips_grin_close
with characlose


mi "Impression de déjà vu~ ?"


"Elle glousse, avant de laisser échapper un autre rire."

show misha cross_laugh_close
with characlose


mi "Hahaha, tu sais, mon horoscope a dit que ça allait être une bonne journée pour moi."

show misha perky_smile_close
with characlose


mi "Et maintenant que tu vas nous aider—{w=1.5}{nw}"

show shizu adjust_smug_close
with charachange


"Shizune lui fait des signes rapides."

show misha hips_grin_close
with charachange


mi "Exact~ ! Je veux dire, maintenant que tu as décidé de nous aider, complètement de ta propre volonté, je vais pouvoir me la couler douce ! Quelle chance~ hein ?"


"J'ouvre la bouche pour dire quelque chose mais je réalise que ça ne sert à rien."


"Je recentre ma pensée sur le moyen de me sortir de ça. Non, leurs actions sont clairement délibérées, il est inutile d'essayer de raisonner avec elles."


"On ne peut pas raisonner avec des fous. Je fronce les sourcils, et elles ne remarquent même pas mon mécontentement, ce qui renforce encore plus mes soupçons."


"Elles semblent très relaxées maintenant. Je suppose qu'elles pensent avoir déjà gagné, elles vont donc baisser leur garde."

stop music fadeout 2.5


"C'est plutôt arrogant."


"Elles passent devant moi et se dirigent vers la porte."

hide shizu
hide misha
with charaexit


"Et je fais furtivement demi-tour, me dirigeant vers la porte arrière de la classe pendant qu'elles marchent dans le couloir, tournant vers la cage d'escalier."


"Je laisse échapper un soupir de soulagement et range rapidement le reste de mes affaires pour pouvoir me sauver."

play sound sfx_doorslam


"La porte de la classe claque."

play music music_running fadein 0.5

show shizu cross_angry at offscreenright with None
show misha cross_frown at offscreenleft with None
show shizu cross_angry at tworight
show misha cross_frown at twoleft
with ease

shi "…"


mi "Ce n'est pas très bien, ça. Hahaha, tu pensais vraiment nous avoir eues. N'est-ce pas, Shicchan ?"

show shizu behind_frown
with charachange

shi "…"

show misha hips_grin
with charachange


mi "Ouais, ouais... ...Hahaha !"

show misha cross_frown
with charachange


mi "Et pourquoi ? Je pense que tu nous as dit que tu nous aiderais !"


mi "Et puis tu t'es échappé ! Et tu pensais que tu allais t'en sortir comme ça, n'est-ce pas ?"

show misha cross_laugh
with charachange


"Son expression indignée disparaît et elle commence à rire de façon hystérique, se calmant uniquement après un regard grave de Shizune."

show misha cross_grin
with charachange


mi "Oh, ah... Ouais~, tu pensais pouvoir t'en tirer comme ça ! Mais un criminel retourne toujours sur les lieux de son crime !"


"Je n'ai même pas réussi à quitter la classe d'abord. Non, attends, je n'ai même pas accepté d'aider d'abord."

show misha perky_smile
with charachange


mi "Tu n'es pas très brillant, criminel. Penser qu'il suffit que tu te dérobes à tes fonctions comme ça... Vraiment pas malin, Hicchan !"


hi "Je suis un criminel ? Qu'est-ce que j'ai fait ? Quelles sont les charges ? De quoi est-ce que je suis coupable ?"

show misha hips_grin
with charachange


mi "C'est au tribunal de décider, criminel ! Je ne pense pas que nous ayons à te le dire !"

show misha perky_smile
with charachange


mi "De plus, c'est toi le criminel ici, tu sais ce que tu as fait !"


hi "Tu as déjà lu “Le Procès” de Kafka ?"

show misha hips_grin
with charachange


mi "Non, qu'est-ce que c'est, Hicchan~ ? Qu'est-ce que ça vient faire là ?"


hi "Je l'ai lu il y a quelques mois. C'est à propos de ces gens qui intentent un procès à un gars qui veut juste vivre sa vie. Ils refusent de le laisser tranquille, et il ne peut pas lutter contre le pouvoir."

show shizu basic_frown
with charachange

shi "…"

show shizu behind_frown
with charachange

shi "…"

show misha hips_smile
with charachange


mi "Hicchan, c'est quoi le rapport avec ça ?"

show misha sign_confused
with charachange


mi "Hey~ !, qu'est-ce que ça veut dire ?"


"Elle se tourne vers moi après avoir fait des signes dans tous les sens pendant un bon moment."

show misha hips_frown
with charachange


mi "Tu sais, tu nous as déçues toutes les deux. Tu nous as laissées tomber, Hisao."

show shizu basic_frown
with charachange

shi "…"


mi "Laissées en plan."

show shizu behind_frown
with charachange

shi "…"


mi "Nous laisser tomber. Et dehors dans le froid~."

show shizu cross_angry
with charachange

shi "…"

show misha sign_smile
with charachange


mi "C'est ta façon de traiter une personne ? De fuir tes responsabilités, d'abandonner tes camarades ?"

show misha hips_frown
with charachange


mi "Nous pensons que tu te dois d'honorer ton engagement."


hi "Quoi ? Mais je ne me suis engagé à rien du tout~ !"


"Mon souffle n'arrive pas à sortir de ma gorge et je m'étouffe momentanément."

show shizu basic_frown
with charachange

shi "…"

show misha cross_smile
with charachange


mi "Ce n'est pas vrai, Hicchan ! Tu as dit que tu n'étais pas inutile, tu l'as définitivement dit, oui, définitivement, définitivement, définitivement~ !"

show misha hips_grin
with charachange


mi "Nous te rappelons ces mots maintenant~ ! Tu ferais mieux de te préparer à montrer que tu n'es pas un gars inutile !"


mi "Ton honneur sera souillé pour toujours si tu essayes de t'enfuir~ !"


mi "Donc pour le reste de la journée, on va passer du temps ensemble, juste nous trois, et travailler dur !"

show shizu behind_frown
with charachange

shi "…"

show misha hips_smile
with charachange


mi "Tu ne peux pas nous tromper !"


mi "Tu devrais être heureux, tu rends un grand service à ton école. Ne demande pas ce que l'école peut faire pour toi..."


mi "Mais ce que tu peux faire pour ton école !"

show misha cross_laugh
with charachange


mi "Hahaha !"


mi "Hahahahahahaha !"


"Vraiment déprimant."

show misha cross_grin
with charachange


mi "Courage, courage, Hicchan !"


"Elle me donne une claque dans le dos suffisamment forte pour sortir l'air de mes poumons. Je tousse pour respirer."


mi "En plus, tu n'es pas heureux de passer la journée avec deux jolies filles ?"

show misha hips_laugh
with charachange


mi "Hahahaha !"


"J'imagine qu'elles ont raison. J'ai bien dit ces mots."

stop music fadeout 3.0


"Acceptant mon destin, je les suis dans la salle du conseil des étudiants..."

scene bg school_council_ss
with shorttimeskip

play sound sfx_hammer
play music music_tranquil fadein 3.0


"...Et plante le dernier clou dans la planche. Ça m'a pris tout l'après-midi, et il est presque trop tard pour le dîner. Mais c'est fait maintenant."

show shizu basic_normal_ss at center
with charaenter


"Shizune sort un mètre, et un niveau à bulle, et inspecte rigoureusement."

show shizu behind_smile_ss
with charachange


"Elle sourit, affiche un air satisfait, et fait signe à Misha de venir."

show shizu adjust_happy_ss
with charachange

shi "…"

show shizu adjust_happy_ss at tworight
show bg school_council_ss at bgright
with charamove

show misha perky_smile_ss at twoleft behind shizu
with charaenter


mi "Elle dit que tu as fait un très bon travail. En fait, tu dois avoir un don pour ça."

show misha hips_smile_ss
with charachange


mi "Woaw, je suis impressionnée, aussi. Et c'était rapide, t'as déjà fait ça auparavant ?"


hi "Non. Jamais."


hi "Jamais auparavant."


hi "Et je ne le referai jamais de nouveau."

show shizu behind_smile_ss
with charachange

shi "…"


mi "Eh bien, notre quota pour la journée est de six stands. Dans quelques minutes, Shicchan et moi devrions avoir terminé celui-là."

show misha hips_grin_ss
with charachange


mi "Ça veut dire~... encore quatre à faire !"

show misha sign_smile_ss
with charachange


mi "On passe un bon moment, elle dit~ !"

show misha hips_grin_ss
with charachange


mi "C'est pas super amusant ?"


hi "Quoi ?"


"Je peux penser à un million de choses que je préfèrerais faire, mais je suppose que tout le monde doit faire sa part pour le festival, même moi."


hi "Vous avez de la chance que je vous aide, si je ne voulais vraiment pas, j'aurais pu partir facilement."

show shizu basic_normal2_ss
with charachange

shi "…"

show misha perky_smile_ss
with charachange


mi "Vraiment, Hicchan ?"

show shizu adjust_smug_ss
with charachange

shi "…"

show misha cross_laugh_ss
with charachange


mi "Wahaha~ ! Shicchan pense que tu utilises juste ta bouche ! Les Japonais n'ont pas le réflexe de fuir ou de se battre, Hicchan~ !"


"Shizune fait le signe de la victoire avec ses doigts."

show shizu basic_happy_ss
with charachange

shi "…"

show misha hips_grin_ss
with charachange


mi "Définitivement~ ! Définitivement, définitivement~ ! Si tu voulais vraiment t'échapper, tu aurais pris une mesure immédiate~ ! C'est comme ça que tu sais que quelqu'un est sérieux ; quand il n'a pas de doutes, pas de regrets !"

show shizu basic_normal_ss
with charachange

shi "…"

show misha sign_smile_ss
with charachange


mi "Peut-être que c'était une mauvaise idée de te le dire, maintenant Hicchan sait quoi faire la prochaine fois~."


"Mais, juste le fait qu'elle soit d'accord avec le fait de me le dire montre qu'elle a des doutes quant au fait que je pourrais le faire."


"Ça me donne juste encore plus envie de le faire, et j'ai presque envie d'avoir une opportunité qui se présente à nouveau. Mais si ça arrive, elle pourrait m'avoir d'une autre façon."

show shizu behind_smile_ss
with charachange

shi "…"

show misha perky_smile_ss
with charachange


mi "Shicchan dit qu'elle est contente maintenant."

stop music fadeout 1.5

scene bg school_council_ni
with shorttimeskip

play music music_dreamy fadein 0.5


"Beaucoup, beaucoup plus tard dans la soirée, nous nous retrouvons avec six stands achevés."


"Avec la fierté d'un travail bien fait, nous nous asseyons et admirons le fruit de notre labeur, n'échangeant pas un mot. Juste admirant."


"Je réalise que j'ai un peu soif."


hi "Hé, il y a un distributeur dans le hall, nan ? Il est en route toute la journée, hein ?"

show misha hips_smile at center
with charaenter


mi "Ouais, les boissons sont pas chères, aussi. On y prend habituellement quelque chose les jours comme aujourd'hui."


"Je cherche dans ma poche, et trouve une seule pièce de cent yen."


hi "C'est suffisant ? J'ai plutôt soif."

show misha hips_grin
with charachange


mi "Cent yen ? Tu peux prendre n'importe quelle boisson dans la machine avec ça."


hi "C'est bien, c'est très bien. Bon."

show misha hips_grin at twoleft
show bg school_council_ni at bgleft
with charamove

show shizu adjust_happy at tworight
with charaenter

shi "…"

show misha sign_smile
with charachange


mi "Ah, attends une seconde."

show misha hips_grin
with charachange


mi "Hm ? Qu'est-ce qu'il y a, Shicchan ? Tu veux qu'il te ramène une boisson aussi ? Hahaha !"

show shizu behind_smile
with charachange

shi "…"

show misha perky_smile
with charachange


mi "Hicchan, tu nous as vraiment aidées, donc aujourd'hui, je— je veux dire Shicchan, paye à ta place."

show misha perky_confused
with charachange


mi "Hé, et moi alors ?"

show shizu adjust_smug
with charachange

shi "…"

show misha perky_smile
with charachange


mi "Qu'est-ce que tu voudrais ? Si j'ai soif aussi ?"

show misha perky_confused
with charachange


mi "Évidemment moi aussi !"


hi "Hm, je sais pas. N'importe. Un soda au melon tiens."

show shizu behind_smile
with charachange

shi "…"

show misha perky_sad
with charachange


mi "Hé, attends, Shicchan ! Je veux à boire aussi !"

hide shizu
with charaexit

show misha perky_sad at center
show bg school_council_ni at center
with charamove


mi "Aw... !"

show misha perky_confused
with charachange


mi "Tu sais, c'est à des moments comme ça que je crois qu'elle ne fait que me taquiner."


hi "C'est probablement ça. Je suis sûr qu'elle te ramènera quelque chose, hein ?"


mi "Ouais, elle le fait d'habitude. Mais... on sait jamais..."

hi "Heh."

show misha perky_confused at twoleft
show bg school_council_ni at bgleft
with charamove

show shizu basic_normal2 at tworight behind misha
with charaenter


"Shizune revient avec deux sodas au melon et une brique de jus de fruit."


"Elle me tend un des sodas, et l'autre à Misha."

show misha hips_grin
with charachange


mi "Merci, Shicchan~ ! J'étais sûre que tu m'en rapporterais un, je savais que je pouvais compter sur toi ! Wahahaha !"

show misha perky_confused
with charachange


mi "Mais comment t'as su que c'était ça que je voulais ? Je prends autre chose habituellement."

show shizu behind_smile
with charachange

shi "…"

show misha hips_grin
with charachange


mi "Quoi ? Tu savais que je voulais l'essayer ? Et que j'aime les trucs enfantins comme ça ? Hahahaha !"

show misha hips_laugh
with charachange


mi "Hahahaha !"


"Je fais un geste à Shizune pour la remercier, qui sourit et hoche la tête en retour."

show shizu adjust_happy
with charachange

shi "…"

stop music fadeout 4.0

show misha sign_smile
with charachange


mi "Hé, Hicchan..."


hi "Oui ?"

show shizu behind_smile
with charachange

shi "…"

show misha perky_smile
with charachange


mi "On a passé beaucoup de temps ensemble. Déjà, en si peu de temps, on a fait tant de choses."


mi "On devrait arrêter de tourner autour du pot. Ce que je veux dire c'est,"


"Ça sonne comme si elle allait me demander de sortir avec elle, mais c'est pas possible. Néanmoins, mon cœur bat comme un marteau-piqueur. Rah, ça me rappelle une autre scène similaire plus tôt dans l'année."


"J'essaye de dire quelque chose, mais mon cerveau ne peut pas se décider entre lui dire de s'arrêter ou de continuer."


"Je me sens rougir jusqu'aux oreilles."

show shizu adjust_smug
with charachange

shi "…"

show misha hips_smile
with charachange


mi "Ce que j'essaye de dire est..."

show misha hips_grin
with charachange

play music music_ease


mi "Veux-tu rejoindre le conseil des étudiants ?"


hi "Ah, quelle déception."

show misha cross_laugh
show shizu adjust_blush
with charachange


mi "Hahaha ! Hahahaha ! Hahahahaha ! Wahaha ! Hahahaha !"


mi "Tu pensais qu'elle allait te demander de sortir avec elle, Hicchan ?"


mi "Hahahaha ! Hahaha ! Hahaha ! Hahahaha !"


mi "Hahahahahahahaha !"


"Je me sens très embarrassé maintenant, je peux sentir que je rougis encore plus."


"Shizune essaye aussi de cacher un rougissement après la traduction de Misha et pose plusieurs papiers devant moi."

show shizu behind_frustrated
with charachange

shi "…"

show misha cross_grin
with charachange


mi "Donc, alors ? Tous les papiers sont juste là."

show misha cross_smile
with charachange


mi "Et tu es assis, de toute façon. Tu es comme à la maison ici. Boisson et tout~ !"



show shizu basic_normal
with charachange

shi "…"

show misha hips_grin
with charachange


mi "Qu'est-ce que t'en dis ?"


"Elle baisse la voix et redemande encore une fois un peu plus solennellement."

show misha cross_smile
with charachange


mi "Hicchan, qu'est-ce que t'en dis ?"

show misha sign_smile
with charachange


mi "Tu ne détestes pas vraiment l'idée, hein ?"




"Je suis plus qu'un peu surpris du changement soudain de ton. Je ne sais vraiment pas comment réagir à ça."


"Pour une fois, elle ne crie pas à gorge déployée sans tenir compte du tact."


"Avant, j'étais sûr qu'elle savait déjà que j'allais dire non."


"Cette fois, elle semble vraiment sérieuse."

show misha perky_smile
with charachange


mi "Je pense que peut-être tu devrais nous rejoindre. Pas juste parce que ton aide serait précieuse, mais, enfin, tu traînes déjà avec nous de toute façon."


mi "Je pense que Shicchan apprécierait si tu nous rejoignais. Ce n'est pas comme si tu nous détestais ou quoi que ce soit, hein ?"

show misha perky_sad
with charachange


mi "Ça te causerait aucun tort de nous rejoindre. Et j'apprécierais si tu le faisais."


"Elle semble avoir du mal à trouver ses mots, ce qui est étrange pour quelqu'un de bavard comme Misha."


"Pour certaines raisons, j'en suis presque troublé."

show shizu behind_blank
with charachange


"Mes yeux dérivent vers Shizune, qui me regarde en retour furtivement, distraite par le nettoyage de ses ongles."

show misha perky_smile
with charachange


mi "Si tu ne veux pas nous rejoindre, je te promets qu'on ne t'en parlera plus, mais si tu veux bien, ça nous rendrait vraiment heureuses."


"Elles semblent toutes deux incapables de me regarder dans les yeux."


"Je ne peux pas mentir, la pensée d'être entre ces deux jolies filles est quelque chose qui ne me laisse pas indifférent."


"Je ne cherche pas à faire ce genre de travail tous les jours, mais il y en aura sûrement moins à faire après le festival."


"Du moins, je l'espère."


hi "D'accord. J'imagine que ça peut pas faire de mal, alors, pourquoi pas ?"

show shizu adjust_happy
with charachange

shi "…"

show misha hips_grin
with charachange


mi "Fantastique. Fantastique ! Ahahaha~ !"


"Shizune fait le signe de la victoire avec ses doigts, pleinement satisfaite."

show shizu basic_happy
with charachange

shi "…"

show misha perky_smile
with charachange


mi "Elle va tout compléter, Hicchan. Félicitations, tu es officiellement un membre du Conseil des Étudiants maintenant !"


hi "Super. Je n'attends pas impatiemment d'avoir plein de travail."


hi "Pour être honnête, je n'ai jamais fait quoi que ce soit comme activité au conseil des étudiants avant."


hi "Mais peut-être que ça sera une expérience positive."


"Misha commence à applaudir, riant de manière exubérante comme elle sait le faire."

show misha hips_laugh
with charachange


mi "Félicitations, Hicchan !"

show shizu adjust_smug
with charachange

shi "…"


mi "Félicitations !"

show shizu behind_smile
with charachange

shi "…"


mi "Félicitations !"

show shizu adjust_happy
with charachange

shi "…"


mi "Félicitations !"


hi "J'ai compris le message."


"Je ne peux pas m'empêcher de sourire, de trouver mignonne une réaction aussi enfantine."

show misha hips_grin
with charachange


mi "Le conseil des étudiants est toujours occupé, tu sais ! Mais pour aujourd'hui, on a fini. À demain, Hicchan !"

show misha hips_smile
with charachange


mi "On a encore du travail à faire, donc on compte sur toi !"

stop music fadeout 4.0

scene bg school_hallway3
with locationchange


"Je quitte la salle, me sentant complètement anéanti. Les couloirs sont totalement déserts, et l'école a l'air plutôt inquiétante à cette heure de la journée. La salle du conseil des étudiants est la seule à avoir une fenêtre allumée maintenant."


"Ça sera toujours comme ça avec le conseil des étudiants ? Mon corps peut ne pas être en mesure de le supporter."





label fr_A23:

scene bg school_scienceroom at bgleft
with shorttimeskip

play music music_tranquil fadein 3.0


"Hanako n'est pas venue aux cours du matin, laissant son siège vide et solitaire à l'arrière de la salle de classe."


"Je dois lui dire que Lilly la cherchait si je la vois plus tard."


"Après les évènements de ce matin, les cours sont plutôt ennuyeux en comparaison. Je tourne paresseusement les pages de mon manuel."


"J'ai un peu de rattrapage à faire malgré mes tentatives de ne pas prendre de retard à l'hôpital, mais je ne me sens pas enthousiaste."


"L'horloge de la classe est insupportablement bruyante. Le professeur ne dit rien depuis un petit moment, préférant à la place recopier des rangées et des rangées d'équations tirées directement du livre."


"Le cliquetis rythmé de la craie sur le tableau semble se synchroniser à la perfection avec le tic-tac de l'horloge."


"Je commence à copier les équations juste pour passer le temps, même si elles sont déjà dans le livre."

scene bg school_scienceroom at bgright
with shorttimeskip

play sound sfx_normalbell


"Quand la cloche sonne, je ne suis pas pressé donc je reste un moment, relisant ce qu'on a vu en classe. Je préfère partir le dernier de toute façon, pour ne pas avoir affaire aux attroupements dans les couloirs."


"Je remarque que Shizune et Misha sont restées aussi, parlant à quelqu'un venant d'une autre classe."


"Shizune fait des signes si rapides que ses mains font les mêmes bruits que des épées fendant l'air."


"Peut-être qu'il y a de la colère refoulée là-dedans."


"Misha essaye désespérément de tenir le rythme, mais il est clair qu'elle parvient à peine à comprendre elle-même."


"Je baisse la tête. Je ne sais pas de quoi elles parlent, mais ça a l'air d'être une affaire sérieuse."


"Shizune signe au point que ses poignets craquent, et Misha lutte pour ressortir ça sous forme de mots."


"Parfois, elle bloque comme si elle disait une phrase difficile à prononcer. Et puis en plus de ça, elle doit traduire en signes tout ce que dit en retour l'autre jeune fille."


"Ça semble être une tâche difficile."


"Misha a l'air fatiguée, comme si elle était sur le point de s'évanouir."


"Heureusement pour elle, leur discussion est bientôt terminée et les filles s'asseyent de nouveau à leurs places."

show shizu behind_blank at tworight
show misha perky_sad at twoleft
with charaenter


mi "Uwaaah ! Je suis fatiguée !"


"Elle suspend sa tête mollement au-dessus de son bureau, l'air épuisée."


"Je vais saisir l'opportunité de me réconcilier un peu avec Shizune, sans me faire enrôler dans le conseil des étudiants encore une fois, quoique je suspecte la porte d'être maintenant fermée pour moi."


hi "Les préparations du festival doivent être dures pour toi."


"En effet, les gens de cette école semblent prendre le festival très au sérieux. Chaque fois que je les vois se balader avant et après les cours ils parlent toujours de leurs plans pour le festival."


"C'est plutôt agréable de voir tout le monde être aussi enthousiaste à ce sujet."


"Je suis probablement le seul qui n'a pas quelque chose à faire."

show shizu basic_angry
with charachange


"Shizune commence par se moquer de moi, comme si elle hésitait entre m'ignorer ou ricaner de moi, mais en fin de compte elle commence tout simplement à faire des signes."

show misha perky_confused
with charachange


"Misha redresse la tête, regardant ses mains avec les yeux un peu dans le vague."

show shizu behind_frown
with charachange

shi "…"


"Elle fait des signes durs, lourds, des grands gestes théâtraux."


"Misha traduit ses signes en langage pour moi."


"Elle le fait si bien que c'est presque Shizune qui parle, transmettant ses pensées directement par Misha."


"Elle doit avoir pratiqué vigoureusement."

show misha cross_frown
with charachange


mi "Eh bien évidemment, nous sommes du Conseil des Étudiants, tu sais, donc nous sommes très occupées."

show shizu basic_frown
with charachange

shi "…"

show misha sign_smile
with charachange


mi "C'est un devoir important qu'est le nôtre, assurer le succès du festival de toute notre force."

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange


mi "Nous aurions honte de nous-mêmes et vis-à-vis des générations passées du conseil des étudiants si le festival était un échec."

show shizu adjust_angry
with charachange

shi "…"

show misha sign_smile
with charachange


mi "C'est pourquoi il ne doit y avoir aucune faille, non... euh je pense que c'était “empêchement”, et rien qui pourrait éloigner le festival de la perfection."


"Le discours passionné de Shizune et le jeu théâtral de Misha vont curieusement bien ensemble."

stop music fadeout 2.0

show shizu adjust_blush
show misha perky_confused
with charachange


mi "Oh ? Bonjour~ !"

show shizu adjust_blush at offscreenleft
show misha perky_confused at Transform(xanchor=0.5, xpos=-0.45)
show bg school_scienceroom at bgleft
with charamove

show hanako emb_timid at Transform(xanchor=0.5, xpos=0.93)
with charamoveinright

play music music_pearly fadein 1.0


"Je regarde par-dessus mon épaule et vois Hanako regarder timidement dans la salle de classe, la plus grande partie de son corps étant cachée derrière la porte."

show misha perky_smile at Transform(xanchor=0.5, xpos=0.15)
with charamove


mi "Hey ! Encore à jouer la délinquante ?"

show hanako emb_blushtimid
with charachange


"Hanako rougit beaucoup à la pique de Misha, même si ce n'était qu'une blague."

show shizu basic_angry at Transform(xanchor=0.5, xpos=0.35)
with charamove

shi "…"

show hanako emb_downsad
with charachange

show hanako emb_downsad at Transform (xanchor=0.5, xpos=0.97)
with charamove


"Shizune la regarde fixement, ce qui pousse Hanako à baisser le regard et à revenir au point où seuls ses doigts sont visibles, repliés nerveusement sur le montant de la porte."


"Peut-être qu'elle montre son aversion pour Hanako par association avec celle pour Lilly."


"C'est apparemment ça, et Hanako en a aussi probablement conscience."


hi "Qu'est-ce qu'il y a, Hanako ?"

show hanako emb_timid
with charachange


ha "H... Lilly est là ?"


mi "Désolée, je n'ai pas vu Satou. Elle, eh, est venue ce matin cependant."

show hanako emb_downtimid
with charachange


"Hanako continue de regarder avec inquiétude Shizune qui la fixe aussi avec son regard analytique. Qu'est-ce qu'elle essaie de faire ?"


"Bien sûr, Shizune ne détourne pas le regard, et elle est suffisamment intimidante comme ça, je peux à peine imaginer à quel point Hanako doit être terrifiée."


"Ça reste drôle de regarder la réaction d'Hanako face au comportement normal de Shizune. C'est ce qui arrive lorsque deux personnes différentes à l'extrême se rencontrent, apparemment."

show hanako emb_timid
with charachange


ha "Vous... vous savez où elle est ?"

show shizu behind_frown
with charachange

shi "…"

show misha hips_frown
with charachange


mi "Si elle a un peu de bon sens, elle est dans sa salle de classe, à travailler sur leur projet du festival. Mais qui sait où cette fille est en train de flâner."



label fr_A23a:

scene bg school_scienceroom at bgleft
show hanako emb_timid at Transform (xanchor=0.5, xpos=0.97)
show shizu behind_frown at Transform(xanchor=0.5, xpos=0.35)
show misha hips_frown at Transform(xanchor=0.5, xpos=0.15)
with None

hide hanako
with charamoveoutright


"Hanako hoche rapidement la tête et s'en va hâtivement."

stop music fadeout 2.0

show misha hips_grin
with charachange


mi "De quoi est-ce qu'on parlait ? Ah ouais, on travaille vraiment dur pour le festival."


"Et pour rendre les autres gens complètement fous."


hi "Bon, bonne chance alors."


"Je me lève pour partir, sortant avant que l'une d'elles parvienne à me reprocher mon absence d'activité."

scene bg school_hallway3
with locationchange


"Le hall est plutôt silencieux, comme prévu. Tout le monde doit être à des réunions de club ou aux préparations du festival. Ou les deux."


"Les mots de Shizune sur le fait que j'étais un fainéant résonnent toujours dans ma tête."


"Je me sens un peu coupable de ne pas participer, mais je manque de volonté pour faire quelque chose de concret à ce sujet."


"Pour le festival, c'est déjà trop tard, sauf si je compte aider Shizune et Misha, ce que naturellement, je ne ferai pas. Et les clubs... je ne sais pas."


"Peut-être que je ne suis pas le genre à rejoindre un club."

play music music_soothing fadein 4.0

scene bg school_dormext_half
with locationskip


"À mi-chemin entre le bâtiment de l'école et celui du dortoir, je remarque une personne devant ceux-ci."


"C'est Rin."


"Apparemment elle travaille sur son mur aujourd'hui aussi."


"Je marche vers elle, mais elle ne semble pas remarquer que j'approche."

scene bg mural_unfinished
show rin basic_awayabsent_close at tworight
with locationchange


"Elle est assise sur une caisse retournée, regardant attentivement le mur qu'elle peint avec un pinceau tenu entre ses orteils."


"Le mur a considérablement progressé depuis hier, mais il est toujours uniquement à moitié fait pour autant que je puisse dire."


"Plus de couleurs ont fait leur apparition et les visages humains tordus se sont aussi répandus et ont augmenté en nombre."


"Je dois le dire, le style est plutôt accrocheur et très unique. Non pas que je m'y connaisse d'une quelconque façon en art, mais c'est très joli quand même."


"Je me racle la gorge pour attirer son attention, mais sans la surprendre pour ne pas briser sa concentration."


rin "Attends."


"Elle ne se tourne même pas pour vérifier qui c'est."


"Je vais attendre."

stop music fadeout 6.0

"…"

"…"

"…"

"…"

with shorttimeskip

"…"


"Quinze minutes plus tard, je constate que sa concentration est en effet toujours intacte, et aussi que j'ai attendu assez longtemps pour justifier une légère tape sur l'épaule pour lui rappeler ma présence."


"Rin tourne la tête mécaniquement dans ma direction, fixant directement mon entrejambes."

show rin basic_deadpan_close
with charachange


rin "Oh, c'est Hisao."

play music music_rin fadein 0.3


"Elle peut le deviner en me regardant là ? Je me sentirais beaucoup moins mal à l'aise si elle regardait mon visage."


hi "Une observation astucieuse. Tu travailles dur, à ce que je vois."


"La conversation commence comme si je n'étais pas là depuis déjà un quart d'heure, mais ce n'est pas grave. Au moins, elle commence."


hi "Ça a l'air bien."


"C'est le cas, les couches de peinture cachées sous d'autres couches de peinture, les visages humains mélangés et façonnés, cela crée un look vraiment impressionnant. Mais Rin semble vexée."

show rin basic_deadpanupset_close
with charachange


rin "Tu ne devrais pas commenter une œuvre en cours. Sept ans de malheur."


hi "Ça a l'air terrible. Je crois que je vais retirer ce que je viens de dire alors."


"Pourtant, ça a l'air bien. Je me demande si j'ai quatorze ans de malheur pour avoir pensé ça."

show rin basic_awayabsent_close
with charachange


"Rin se retourne pour regarder sa peinture et la pointe avec son gros orteil."

show rin relaxed_nonchalant_close
with charachange


rin "Tu veux bien me mixer un peu de cette couleur ? Je suis à court."


"Elle regarde vers le bas le bol à demi-vide avec le reste de la même peinture rose."


"Je n'ai pas vraiment l'intention de rester et de l'aider dans son projet mais... j'ai pas grand-chose de prévu après tout."

show rin basic_absent_close
with charachange


"Je regarde Rin, qui me fixe d'un regard neutre en retour."


hi "Juste cette fois."

show rin basic_awayabsent_close
with charachange


"Rin prend un autre pinceau et le trempe dans un autre ton de rouge pâle. Il y a des dizaines de bols similaires tout autour de son espace de travail. À la vue de cette scène, elle peut être assise là depuis des heures."


"Je me demande si c'est le cas. Ça voudrait dire qu'elle aurait loupé l'école, ce qui ne serait pas si étrange pour quelqu'un comme Rin."


"Je verse un peu de blanc et de rouge dans le bol, essayant de faire correspondre la couleur avec celle qui est déjà sur le mur."


"Je n'arrive pas à bien le faire."


"C'est vraiment embêtant qu'elle n'en ait pas mixé suffisamment d'abord. Arriver à l'exact même ton serait impossible, mais je peux au moins essayer de m'en rapprocher autant que possible."


hi "En parlant de dur travail, ce n'est pas trop pour toi aussi ? C'est vraiment une grande peinture et tout."

show rin basic_deadpan_close
with charachange


rin "Oh, je ne suis pas vieille et amère au point de penser comme ça."


hi "Je suppose que non."

show rin basic_deadpannormal_close
with charachange


rin "Tu supposes bien."

show rin basic_deadpancontemplation_close
with charachange


rin "Mal aux jambes cependant. J'ai l'impression que ce sont des limaces. Limaces faites de limaces de mer."


hi "À cause de la position ?"


rin "Ouais, je préfère faire ça dans une position horizontale, si tu vois de quoi je parle."


rin "Mais j'ai pas le choix. Je peux pas demander au mur de se coucher."

show rin negative_spaciness_close
with charachange


"Disant ça, elle s'étire un peu, pliant ses jambes et son dos bien plus loin qu'un humain devrait pouvoir les plier. C'est étonnant comme elle parvient à tourner son corps sans effort."

show rin negative_annoyed_close
with charachange

show rin negative_spaciness_close
with charachange


"Il y a une petite grimace dans son regard vide - une pointe de douleur peut-être - pendant qu'elle s'étire."


"Rin doit avoir bien plus d'énergie et de dextérité qu'une personne normale pour être capable de vivre comme elle le fait, mais ça doit l'épuiser."


hi "Pourquoi tu te pousses autant ? Prends une pause ou quelque chose au moins. Continue demain si ça va pas."

show rin basic_deadpannormal_close
with charachange

"Elle s'arrête de bouger pour réfléchir."


"Assez longtemps, comme un bâillement mental."

"…"

show rin basic_deadpan_close
with charachange


rin "Je ne pense pas, Hisao."


rin "Je ne me pousse pas, Hisao."


hi "Pourtant tu en as l'air."

show rin basic_deadpannormal_close
with charachange


rin "Non. Il ne s'agit pas de pousser ou de tirer ou quelque chose de ce genre."

show rin basic_awayabsent_close
with charachange


rin "Il y a ce garçon."


hi "Un garçon ?"

show rin basic_absent_close
with charachange


rin "Oui."


hi "Où ça ?"

show rin basic_deadpannormal_close
with charachange


rin "Au club d'art."


hi "Euh... et ?"

show rin basic_deadpan_close
with charachange


rin "Il est aveugle."


hi "Oh. Comment tu peux peindre si t'es aveugle ?"

show rin basic_awayabsent_close
with charachange


rin "Aucune idée."


hi "Donc pourquoi il est là ?"

show rin basic_absent_close
with charachange


rin "C'est ça le truc. Il est là."


"Elle devrait vraiment dire plus d'un mot à la fois pour avoir davantage l'impression de participer à une discussion et moins à un interrogatoire."

show rin basic_awayabsent_close
with charachange


rin "Il ne peut pas faire quoi que ce soit que tu appelles de l'art, pas vrai ? Mais il vient quand même. Et peint."

show rin basic_deadpannormal_close
with charachange


rin "Pourquoi ?"


hi "Je ne sais pas. Pourquoi ?"

show rin basic_deadpan_close
with charachange


rin "Je ne sais pas. C'est pourquoi j'ai demandé."


hi "Et donc ?"

show rin basic_deadpannormal_close
with charachange


rin "Il ne peint pas vraiment souvent mais je pense que ses peintures sont très intéressantes."


hi "Je suis sûr qu'elles le sont."

show rin basic_lucid_close
with charachange


rin "J'ai essayé une fois. Peindre avec les yeux fermés."

show rin basic_deadpannormal_close
with charachange


rin "Ce n'était pas trop intéressant. Et nettoyer le sol m'a pris des années. Je n'ai pas réessayé."

show rin basic_deadpandelight_close
with charachange


rin "Mais il devient meilleur à la sculpture."


hi "Je vois."


"Peut-être qu'elle essayait d'argumenter en disant ça. Peut-être qu'elle a oublié pourquoi."


hi "On dirait que le club d'art est plein de personnes intéressantes."

show rin basic_deadpan_close
with charachange


rin "Pas vraiment."


"Déclaration plutôt brutale, et elle a totalement loupé le sarcasme."


hi "Non ?"

show rin basic_awayabsent_close
with charachange


rin "Comme je t'ai dit. Elles ne sont pas très intéressantes. Et j'ai habituellement pas trop d'intérêt pour les gens qui ne sont pas intéressants."

show rin basic_absent_close
with charachange


rin "Peut-être que tu l'es."


hi "Peut-être."

"…"

show rin basic_awayabsent_close
with charachange


rin "Mais ce garçon est intéressant."

show rin basic_lucid_close
with charachange


rin "Peut-être que je suis comme ce garçon, ou peut-être que tu l'es. Peut-être que tout le monde l'est."


rin "Faire des choses que tu ne peux pas faire, juste parce que tu peux."


"Je trouve que c'est plutôt profond, et je lui dis."


hi "T'es quelqu'un de profond."

show rin basic_deadpannormal_close
with charachange


rin "Nan. Je suis vraiment quelqu'un de superficiel et irréfléchi. Les gens me disent toujours ça."

show rin basic_deadpanamused_close
with charachange


rin "Tu savais que je peux penser à seulement quatre choses en même temps ?"


hi "Non, mais maintenant si."

show rin basic_lucid_close
with charachange


rin "Actuellement je pense aux toilettes des filles du second étage, une glace, le doigt de pied du milieu, et une coupe de cheveux."

show rin basic_awayabsent_close
with charachange


rin "Je vais avoir besoin d'une coupe de cheveux."

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


"Elle secoue la tête vigoureusement, laissant ses cheveux courts et désordonnés se balancer de tous les côtés. Je peux voir que c'est une chose qu'elle aime bien faire."

show rin basic_awayabsent_close
with charachange


"Nous nous taisons pendant que Rin marche autour de nous distraitement, attrapant quelques pinceaux. Le truc à propos du club d'art continue de rester dans ma tête un petit moment."


"J'ai l'impression de marcher sur un territoire inconnu avec l'art. À chaque fois que je rencontre Rin, c'est comme si je commençais à fumer ou un truc du genre. Je devrais probablement arrêter de lui parler."


"Ce n'est pas que je ne l'aime pas, en dépit de la confusion dont elle est la cause, et je ne déteste pas l'art non plus. Même que parfois je dessine pour m'amuser. C'est juste que je n'ai aucun élan créatif, et aucune compétence technique."


"Donc en général, si je dois dessiner quelque chose, j'ai le syndrome du papier blanc, et je bloque complètement."


"Ça, ou je m'arrange pour dessiner quelque chose de défiguré, et je deviens rapidement frustré dans mon inhabileté à mettre sur le papier l'image que j'ai dans la tête et j'arrête tout sans vraiment essayer de faire un effort."


"Contrairement à cette fille. Elle me frustre aussi. Être avec elle est comme me regarder dans un miroir qui ne reflète rien."


"Ce qui fait que je me pose des questions sur l'intérêt de l'acte."

show rin basic_absent_close
with charachange


"Rin s'assied sur sa boîte, se balançant de droite à gauche, apparemment à l'aise dans le silence pesant. Elle me fixe de nouveau, ou peut-être derrière moi. Je n'arrive pas à vraiment savoir où ses yeux regardent."


"Je pense à m'en aller et après elle pourra s'occuper de son travail sans être distraite et je pourrai faire n'importe quel truc que je voudrai faire seul. Ce n'est pas comme si j'avais quoi que ce soit que je devais faire aujourd'hui..."


hi "Oh-oh."

show rin basic_deadpan_close
with charachange


rin "Quoi ?"


hi "Rien, j'ai juste oublié de dire à Hanako que Lilly la cherchait."


hi "Tu la connais ? Elle est dans ma classe."

show rin basic_deadpanamused_close
with charachange


rin "Oh, elle. La Mystérieuse Fille des Toilettes."

show rin basic_amused_close
with charachange


rin "Cette personne est amusante. Je l'ai vue aller aux toilettes cinq fois durant une recréation il y a trois semaines. Je suis sûre que c'est le record mondial."

show rin basic_deadpandelight_close
with charachange


rin "C'était très mystérieux."


hi "C'est pourquoi tu l'appelles la Mystérieuse Fille des Toilettes ?"

show rin basic_absent_close
with charachange


rin "Quelle autre raison pourrait-il y avoir ? Enfin, s'il y en a une, ça restera un éternel mystère. Je ne l'ai pas suivie à l'intérieur."

"…"

show rin basic_awayabsent_close
with charachange


rin "Peut-être que c'était la semaine d'avant ? C'est possible."

"…"


rin "La regarder me donne faim."


hi "Ne dis pas ça."


hi "Au moins, pas à côté d'elle."

show rin basic_deadpannormal_close
with charachange


"Rin se tourne vers moi l'air vide, comme si elle n'était pas sûre de savoir pourquoi je l'ai réprimandée."


"Mais elle ne semble pas comprendre plus qu'avant, donc je préfère abandonner à ce stade."


hi "Donc tu veux aller manger ?"

show rin basic_awayabsent_close
with charachange


rin "Non. Pas encore."


"Rin a tourné son regard affamé sur le mur, ayant l'air légèrement plus énergique, ou au moins un peu moins léthargique qu'elle ne l'était avant."


"C'est comme si le mur est un adversaire qu'elle doit vaincre, quelque chose qu'elle doit surmonter avant de pouvoir manger."


"C'est l'impression que j'en ai. Un étrange sens de l'empathie m'envahit et me fait un peu sourire intérieurement."


"Avec toute sa bizarrerie, Rin est plutôt cool après tout."


hi "Je dois y aller quand même."


hi "Amuse-toi bien."

stop music fadeout 3.0


"Rin a déjà saisi un pinceau et le trempe dans la peinture fraîche, donc bien sûr elle ne peut plus m'entendre ou répondre quoi que ce soit."





label fr_A24:

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


hi "Tu dois la trouver ? Elle te cherchait ce matin mais apparemment vous vous êtes loupées."


"Elle attend un peu sans répondre à cette simple question ; comme si elle n'était pas sûre que ce soit une bonne chose qu'elle réponde à une telle question."

show hanako emb_blushtimid
with charachange


ha "O... oui."


hi "Je peux venir avec toi."


hi "Si tu es d'accord."

show hanako emb_downtimid
with charachange

show hanako emb_blushtimid
with charachange


"Hanako hoche la tête par à-coups, toujours sur ses gardes, les épaules raides comme du bois. J'ai le sentiment qu'elle pourrait être plus à l'aise toute seule après tout, mais il est trop tard pour faire marche arrière maintenant."


"Elle a cette expression vraiment troublée qu'elle semble porter presque en permanence, celle qui me fait moi-même rester constamment sur mes gardes. Je me demande pourquoi."


"Je comprends un peu pourquoi elle semble toujours être aussi méfiante... ou peut-être plus, pourquoi il pourrait y avoir quelqu'un comme elle."


"Mais je n'ai toujours aucune idée de comment je devrais agir auprès d'une telle personne."


hi "C'est bientôt l'heure du repas. Tu as prévu de manger avec Lilly ?"

show hanako emb_downtimid
with charachange

show hanako emb_blushtimid
with charachange


"Elle hoche légèrement la tête."


"Donc elle a dû essayer d'aller à la cafétéria."


"Mais bon, il y a quasiment foule au dîner, comme pendant le déjeuner quand la cafétéria est bondée."


"Ce n'est pas si grave parce que la période du dîner est plus longue que celle du déjeuner, mais je peux comprendre pourquoi Hanako peut être découragée d'y aller."


"Je prends mon sac et nous partons. Hanako sautille un peu pour se mettre à mon rythme, donc je ralentis pour m'adapter à sa vitesse."

scene bg school_hallway3
with locationchange


"Il ne nous a pas fallu longtemps pour commencer à marcher à une vitesse confortable dans le couloir."

show hanako def_worry at right
with charaenter


"J'ai presque l'impression qu'on va faire une balade ensemble ; une chose que je ne peux pas vraiment dire avoir déjà fait avant avec une fille."


"Hanako ne semble pas penser la même chose cependant. Même si nous marchons au même rythme, elle ne vient jamais près de moi."


"Je pense qu'elle est toujours un peu mal à l'aise près de moi. Étant donné à quel point elle est timide, ça n'a pas l'air de s'améliorer, du moins pour le moment."

scene bg school_cafeteria
with locationchange

play music music_night fadein 3.0


"Au moment où nous arrivons à la cafétéria, il n'y a pas vraiment de foule, mais Lilly est introuvable."

show hanako emb_downsad at center
with charaenter


"Le visage d'Hanako est encore plus sombre que d'habitude."


hi "T'as déjà cherché autre part ?"

show hanako basic_worry
with charachange


ha "J-juste à la bibliothèque... Je lisais..."


"Donc quand elle loupe les cours, elle est à la bibliothèque."


hi "Ah, donc pas exactement une recherche approfondie alors. Eh bien, si je devais deviner, elle serait dans sa classe, comme Shizune l'a dit, non ?"

show hanako cover_worry
with charachange


ha "O-oui."


show hanako basic_normal
with charachange


"Avec le plus petit des hochements de tête, Hanako approuve mon raisonnement."


"Mon Dieu, elle est si maladroite."


"C'est comme si j'avais besoin d'une double couche de gants en soie avec rembourrage pour commencer une interaction avec elle."


"Parler un peu pourrait aider à ce qu'elle s'habitue à moi. Ce n'est pas si dur de dire que le silence entre nous est présent dans nos deux esprits."


hi "Donc Lilly et toi traînez habituellement ensemble après les cours, c'est ça ?"

show hanako emb_downtimid
with charachange


ha "O-oui."


"Je ne suis pas vraiment sûr de ce que j'espérais de sa réponse, ni pourquoi j'ai même posé la question. C'était plutôt évident, après tout."


"Elle ne semble pas du genre à cultiver un cercle social non plus, donc je suspecte le fait que Lilly puisse être sa seule amie."


hi "Ça doit être embêtant que vous soyez dans des classes différentes, je suppose."


"Elle donne un rapide, presque instinctif hochement de tête. Comparée à Lilly qui pense toujours à ses actions et ses dires, Hanako se hâte de faire des réponses aussi courtes et rapides que possible."

show hanako emb_downsmile
with charachange


ha "Lilly... vient dans la salle de classe, cependant. Même quand elle est occupée..."


"Elle affiche un petit sourire en disant ça, appréciant évidemment le fait que Lilly vienne toujours pour l'aider."


"C'est très mignon, vraiment. Il n'y a vraiment aucun besoin de dire quoi que ce soit de plus, étant tous deux arrivés à la fin de notre discussion."

scene bg school_staircase2
with locationchange


"Pendant que nous montons les escaliers, nous rencontrons un groupe d'étudiants descendant comme un banc de poissons se déplaçant d'une zone d'alimentation à une autre."

show hanako cover_worry_close at Transform(xanchor=0.4, xpos=0.0)
with easeinleft


"Ils semblent s'occuper de leurs affaires, mais avant que je puisse le remarquer, Hanako s'était mise derrière moi."


hi "Hé, ça va ?"

show hanako basic_worry_close
with charachange


ha "C-continue juste d'avancer..."

hide hanako
with easeoutleft


"Les étudiants passent sans même nous regarder, et Hanako reprend sa position à côté de moi quand nous arrivons en haut des escaliers, un sursis momentané dans son inquiétude qui n'est toujours pas partie."

scene bg school_lobby
show hanako basic_normal at center
with locationchange


"Même pendant que nous montons vers le troisième étage, elle ne semble pas se relaxer."


"Ce n'est pas comme si je n'avais jamais connu de personnes timides auparavant, ou même des filles timides, mais Hanako semble vraiment être bien plus loin de ce qui pourrait être normal en terme de peur des autres personnes."


"S'il n'y avait pas Lilly en tant que médiateur, je doute que Hanako aurait pu être capable de marcher à côté de moi comme ça. Elle semble être complètement renfermée en présence des autres."


"Le reste du chemin vers la classe de Lilly continue dans un silence tendu, pendant que je regrette son incapacité à sociabiliser."

scene bg school_hallway3
with locationskip

stop music fadeout 4.0
$ renpy.music.set_volume(0.1, 0.0, channel="ambient")
play ambient sfx_crowd_indoors fadein 2.0


"Après que nous ayons fait notre chemin par les escaliers, du bruit venant de la classe de Lilly est audible depuis le bout du couloir. Je ne m'attendais pas à un tel vacarme."


hi "Bon, j'imagine qu'on l'a trouvée..."


"Ce n'était pas dur. Je me demande si Hanako est venue ici en premier et est allée me chercher après en renfort."


"Bon, si c'est vrai, alors au moins elle commence à me faire un peu confiance. Ça ne peut qu'être une bonne chose."


"Finalement, nous atteignons tous deux la porte de la classe 3-2. Avec Hanako peu discrètement placée derrière moi, j'ouvre la porte."

play sound sfx_dooropen
$ renpy.music.set_volume(1.0, 1.0, channel="ambient")
play music music_another fadein 1.0

scene bg school_room32 at bgright
with locationchange


"L'intérieur est une vraie ruche, apparemment tous les élèves de la classe parlent tout en travaillant hâtivement sur leurs tâches respectives."


"À en juger par les pots de peintures, les décorations et bannières faites, ça doit être pour le festival scolaire."


"J'imagine que ma première priorité doit être de trouver Lilly..."


"…{w} Là."


"La trouver dans ce bazar est étonnamment facile, et son apparence n'y est pas étrangère."


"Avec le groupe d'étudiants rassemblés autour d'elle pendant qu'elle se tient à l'avant de la classe, elle doit être en charge des préparations, ou du moins occupée à les organiser."


"Négociant prudemment un chemin entre les divers étudiants courbés sur le sol par manque de place sur les bureaux, je lève une main, par habitude, quand nous atteignons enfin Lilly."


hi "Salut, Lilly."

show lilly basic_surprised at center
with charaenter


"Elle lève la tête, alors qu'elle parlait avec une fille nettement plus petite qu'elle qui devait être sa camarade de classe, essayant de l'écouter du mieux qu'elle peut."


li "Désolée, qui..."


hi "Ah, désolé, c'est Hisao. Je suis avec Hanako aussi."

show lilly basic_smile
with charachange

show lilly basic_smile at twoleft
show bg school_room32 at center
with charamove

show hanako basic_normal at tworight
with charaenter


ha "Sa-salut."


"Elle est assez inquiète. En considérant le nombre de gens autour, ce n'est pas trop dur de comprendre pourquoi."


"Lilly prend un moment pour évaluer la situation avant de se tourner vers l'autre étudiante encore une fois."

show lilly basic_smileclosed
with charachange


li "Pour le moment, demande des conseils à Moriya. Kenji est déjà occupé à peindre une des bannières."


"Un hochement de tête rapide et elle se retire, glissant avec précaution ses doigts le long du mur pour s'orienter."

$ renpy.music.set_volume(0.1,1.0)


"Attends... Kenji ? Ce Kenji ?"


"Je me tourne rapidement, me penchant sur le côté pour voir derrière Hanako."


"Et il s'avère que oui, dans un coin de la pièce, Kenji est penché sur un morceau de tissu et peint dessus. Ses yeux sont très proches du pinceau, me rappelant à quel point il devait être proche de mon visage quand je l'ai rencontré."

$ renpy.music.set_volume(1.0,1.0)

show lilly basic_smile
with charachange


li "Désolée pour ça. Notre classe n'a pas beaucoup d'étudiants avec une vue partielle, donc ils sont très demandés."


"C'est vrai, la classe 3-2 est spécialement pour les élèves avec une mauvaise vue. Préparer le festival doit être plutôt pénible pour eux."


hi "Besoin d'un coup de main ? Je peux vous aider si vous en avez besoin. Peut-être que Hanako peut aussi."


"L'opportunité de se concentrer sur quelque chose lui ferait du bien, mais je doute qu'elle ait le courage de le demander. Elle hoche rapidement la tête après la proposition, donc je pense avoir pris une bonne décision."


"Assez étrangement, Lilly pousse un grand soupir de soulagement."

show lilly basic_weaksmile
with charachange


li "Ah, c'est un soulagement. Ça doit être fini avant que tout le monde aille dîner, en fait."

show lilly basic_listen
with charachange


li "Tu voudrais bien aider la personne qui peint la bannière principale ? C'est une grande tâche pour lui, mais personne d'autre ne peut aider."


hi "Kenji ? Bien sûr."

show lilly basic_surprised
with charachange


"Elle semble surprise que je le connaisse. Je ne peux pas vraiment l'en blâmer."


li "Vous vous êtes déjà rencontrés ?"


hi "Nos chambres sont voisines dans le dortoir. Dur de se louper l'un l'autre, vraiment."

show lilly basic_ara
with charachange


li "Eh bien, c'est bien de voir que vous êtes devenus amis aussi vite."


"Ami... Je me demande si c'est le bon mot."


"Le silence d'Hanako pendant l'échange me rappelle la raison pour laquelle je l'ai poussée à aider."


hi "Nous allons l'aider alors. Il sait ce qu'il faut faire, hein ?"

show lilly basic_smileclosed
with charachange


li "C'est exact. Demandez si vous avez un problème."

hide lilly
hide hanako
with charaexit

$ renpy.music.set_volume(0.5, 2.0, channel="ambient")


"Attendant une approbation, Hanako et moi commençons un autre périple à travers la classe."


"Kenji est accroupi sur le sol, le regard fixé sur le calicot blanc en face de lui."

show kenji tsun at Transform(yanchor=0.45, ypos=1.0, xalign=0.5)
with charaenter


hi "Hey Kenji."


"...Aucune réponse. Il continue de faire glisser son pinceau plein de peinture le long du kanji à moitié peint qui est esquissé sur la feuille."


hi "Kenji ?"

show kenji tsun at center
with charamove


ke "Hein ? Quoi ? Qui est là ?"


"Si c'est la façon dont il traite les membres de sa classe, ce n'est pas étonnant qu'il travaille seul."


hi "C'est moi. Hisao. De la-{w=.5}{nw}"


ke "Ouais, ouais, je sais ça, mec. Qu'est-ce que tu fais là d'ailleurs ?"


"Son attitude dédaigneuse me gêne."


"Il doit être du genre à être vraiment concentré sur son travail, détestant être gêné par quelqu'un jusqu'à ce que ce soit fini, je suppose."

show kenji tsun at twoleft
show bg school_room32 at bgleft
with charamove

show hanako cover_distant at tworight
with charaenter


"Pendant que nous parlons, le bruit de pas de Hanako marchant derrière moi me rappelle qu'elle est là."


hi "Je venais juste aider avec la bannière. Hanako et moi, en fait."

show hanako cover_worry
with charachange


ha "B... Bonjour..."

show kenji happy
with charachange


ke "Oh. Euh, salut. Ça devrait pas poser de problème."


"Aussitôt que Hanako entre dans l'équation, sa démarche fait un complet volte-face. Sa soudaine fausse hospitalité est un peu troublante."


"Oh, c'est vrai. Une femme. Après réflexion, ce n'était peut-être pas une aussi bonne idée après tout."

stop music fadeout 2.0

scene bg school_room32 at bgleft
show kenji neutral_close at left
show hanako basic_distant_close at right
with locationskip


"Hanako et moi nous asseyons à contrecœur du côté opposé de la banderole par rapport à Kenji, notant les nombreux petits pots de peinture sur le sol autour."


"Classe 3-2... stand de nouilles ?"


hi "Vous vendez des nouilles au festival de dimanche ?"

show kenji happy_close
with charachange


ke "Ouais, des stands à l'extérieur. Ou un truc du genre."


"“Ou un truc du genre ?” Sa nature évasive ne fait que renforcer mes soupçons à son sujet. Mais la bannière passe avant, de toute façon."


hi "Alors, comment tu veux le partager ? On fait les bords pendant que tu fais le texte ? Ou tu veux échanger et faire les bords ?"

show kenji tsun_close
with charachange


ke "Le texte est à moi. Vous faites les bords."


"Il a l'air sacrément convaincu sur le sujet."

show hanako basic_distant_close
with charachange


"Pendant que j'attrape un pinceau, je remarque que Hanako est déjà en train de se demander quelles couleurs utiliser."

show hanako basic_normal_close
with charachange
show hanako basic_distant_close
with charachange
show hanako basic_normal_close
with charachange


"Au moment où je pose le pinceau sur le tissu, elle a déjà commencé un dessin délicat. On dirait que mon idée de l'occuper pour qu'elle pense à autre chose a marché."


"D'un coup de pinceau de couleur bleu foncé, nous commençons à travailler tous les trois."


"Mais pas avant que Kenji profite de la concentration d'Hanako pour se pencher vers moi et me parler d'un murmure complice."

show bg school_room32 at center
show kenji tsun_close at center
show hanako basic_normal_close at offscreenright
with charamove

show kenji neutral_close
with charachange

play music music_kenji fadein 0.5


ke "Ok mec, pourquoi est-ce que t'es là ?"


hi "Hanako avait juste besoin d'aide pour trouver Lilly, c'est tout."

show kenji tsun_close
with charachange


"Il désapprouve apparemment mes motivations."


ke "J'ai compris. Il semblerait que je t'aie mal jugé."

show kenji happy_close
with charachange


ke "Tu vas les infiltrer, c'est ça ? Y aller sous couverture ?"


"J'aurais dû m'en douter. Mais ne pas le corriger est surement mieux que de mentir ou le contrarier en tout cas."


hi "C'est pour ça que t'es là ?"


ke "Évidemment. C'est chiant, mais il y a pas de meilleur moyen d'avoir des renseignements que d'aller les chercher soi-même."

show kenji tsun_close
with charachange


ke "On doit se serrer les coudes, mec. C'est une école cruelle, un monde cruel."


hi "Ouais, très cruel."


"Il loupe le vrai sens de ma phrase et se repenche de l'autre côté, satisfait que je sois solidaire à sa cause. Je ferais mieux de me mettre au travail."

stop music fadeout 2.0
stop ambient fadeout 2.0

scene bg school_room32
show kenji neutral_close at left
show hanako basic_normal_close at right
with shorttimeskip


ha "Fini."


hi "Moi aussi apparemment. Bon travail."


"Nous relions tous deux les lignes de nos modèles, le mien étant à peu près ce que j'ai pu copier du sien."

scene bg school_room32
with locationskip


"Avec un grognement, je me lève et regarde autour de moi."

play music music_dreamy fadein 4.0


"En dehors de Hanako et moi-même, il ne reste que Kenji finissant un signe, Lilly, et un couple d'étudiants parlant entre eux dans la classe."


"Regardant ma montre, je ne suis pas étonné. Il est vraiment tard."


hi "Besoin d'aide ?"

show hanako basic_normal at center
with charamoveinbottom


"Je tends une main à Hanako, qui s'en sert pour se relever."


"Pendant qu'elle le fait, je ne peux pas m'empêcher de regarder son poignet ; si ses cicatrices s'étendent jusque-là, à quel point son corps a-t-il été brûlé ?"

show hanako emb_downtimid
with charachange


"Je ressens un pincement de culpabilité toutefois lorsqu'elle couvre rapidement son poignet de son autre main."


hi "Ça a l'air bien, hein ?"

show hanako emb_timid
with charachange


"Elle a l'air surprise pendant un moment avant de remarquer que je parle de la bannière."

show hanako basic_bashful
with charachange


ha "Ouais... Je suppose."


"Son sourire montre qu'elle ressent un peu de fierté face au résultat, et moi aussi."

hide hanako
with charaexit


"Avec le sol nettement plus dégagé, les décorations étant placées sur les bureaux et les étagères, il est beaucoup plus facile de rejoindre Lilly en traversant la salle."


hi "On a fini la bannière. Je suppose que c'est tout ce qui avait besoin d'être fait ?"

show hanako basic_smile at tworight
show lilly basic_smileclosed at twoleft
with charaenter


"Lilly fait un hochement de tête reconnaissant."

show lilly basic_smile
with charachange


li "Merci Hisao, Hanako. S'il y a un moyen pour que je puisse vous remercier..."


hi "C'est bon. C'est mieux que d'étudier dans ma chambre de toute façon."

show hanako basic_normal
with charachange


ha "Ça ne me gêne pas non plus."


"Elle hoche la tête, avant de se rappeler soudainement une dernière personne."

show lilly basic_surprised
with charachange


li "Oh, Kenji est toujours là ?"


"Juste quand j'allais ouvrir la bouche, Kenji répond depuis l'autre bout de la salle."


ke "Ouais, je viens de finir."


"Il glisse soigneusement son signe sur un emplacement vide pour qu'il puisse sécher, puis marche rapidement devant nous et franchit la porte."

show hanako basic_normal at center
show lilly basic_surprised at left

show bg school_room32 at bgleft
with charamove

show kenji neutral at Transform(xalign=1.15)
with charaenter


ke "À plus mec."

hi "Bye."

hide kenji
with charaexit

show hanako basic_normal at tworight
show lilly basic_surprised at twoleft
show bg school_room32 at center
with charamove


"Les deux étudiants restant disent au revoir à Lilly avant de s'en aller aussi, ne nous laissant qu'à trois."


hi "Bon, je pense que tout le monde est parti maintenant."

show lilly basic_displeased
with charachange


li "J'espère que nous n'aurons pas à refaire quelque chose comme ça."


hi "Travailler après les cours ?"

show lilly basic_concerned
with charachange


li "Évidemment. Les plans de classe de cette année étaient ambitieux. Peut-être trop ambitieux."

show hanako emb_smile
with charachange


ha "Le stand semble bien, pourtant."


hi "Elle a raison, il montre qu'énormément de travail y a été investi."

show lilly basic_ara
with charachange


li "Eh bien, eh bien, je suis sûre que beaucoup d'entre nous seraient heureux d'entendre ça. Au moins maintenant il ne reste plus grand-chose à faire jusqu'au festival lui-même."

show hanako basic_smile
with charachange


ha "Umm... Il se fait tard. On y va ?"

show lilly basic_smileclosed
with charachange


li "C'est probablement une bonne idée. Tu retournes aux dortoirs aussi, Hisao ?"


hi "Ouais, je pense que je vais vous suivre."

scene bg school_gardens2_ni
with locationskip


"L'éclairage nocturne donne vraiment un aspect différent aux jardins. Comparé à l'aspect habituel de verdure, c'est vraiment beaucoup plus calme."


"Étant donné qu'il est tard, le manque d'étudiants autour aide probablement. Les deux ou trois étudiants qu'on a aperçus, se précipitaient à l'intérieur ou à l'extérieur des dortoirs pour tenter de gagner le maximum de temps avant le couvre-feu."


"Les seules choses qui peuvent être entendues sont nos bruits de pas et la canne de Lilly qui, gentiment, frappe régulièrement le sol en face d'elle."


"C'est agréable de pouvoir finalement se détendre un peu, après toute l'excitation de la journée d'école."


"Sans même le remarquer, je laisse échapper un léger bâillement."

show lilly cane_smile_ni at twoleft
show hanako basic_normal_ni at tworight
with charaenter


li "Fatigué ?"


hi "Ouais. Encore à m'habituer au rythme des choses, je suppose."


hi "Le... uh... truc... avec Shizune m'a pris par surprise, cependant."


"Je serre un peu les dents à la mention de leur prise de bec en public. Cela dit, je tiens à découvrir ce qui se cachait derrière tout ça."

show lilly cane_displeased_ni
with charachange


li "Ah... à ce propos..."


li "Je suis désolée que tu aies eu à assister à ça. Shizune et moi... avons certains égards."


label fr_A24c:





"Sa voix semble légèrement agacée en se rappelant de Shizune, et après réflexion, peut-être à cause de mon rôle dans ce qui s'est passé."

show lilly cane_listen_ni
with charachange


li "J'apprécierais si tu ne l'aidais pas. La dernière chose dont elle ait besoin est qu'on la pousse."


"Eh bien, ça confirme mes soupçons de tout à l'heure. Je l'ai mise en colère."


"Cela dit, bien que j'aie accidentellement lâché les chiens sur elle, je ne pouvais pas savoir et je n'ai donc aucune raison de m'excuser."


"Quelques minutes de silence tendu passent entre nous, les yeux d'Hanako jonglant de gauche à droite."


"Abandonnant la perspective d'une quelconque sorte d'excuse, Lilly se rend et change de sujet."



label fr_A24d:




"Sa voix semble légèrement agacée en se rappelant de Shizune, de toute évidence elle n'est pas disposée à en discuter davantage."

show hanako basic_distant_ni
with charaenter


"Je jette un coup œil à Hanako pour voir sa position là-dessus, mais son expression est, sans surprise, évasive et difficile à lire."


"De toute façon je pense que le fait qu'elle s'excuse pour ça n'est pas rien, même si ma curiosité reste insatisfaite."



label fr_A24e:



show lilly cane_weaksmile_ni
with charachange


li "Je serai soulagée quand le festival sera fini, dans tous les cas."


"Le changement de sujet est bienvenu, allégeant rapidement la lourdeur de l'air."


hi "J'imagine. Le festival de mon ancienne école était beaucoup plus discret que ça."

show lilly cane_smileclosed_ni
with charachange


li "Yamaku insiste sur l'idée de communauté scolaire, donc le personnel aime faire des festivals à des occasions spéciales."


hi "Et pourtant les étudiants sont ceux qui font le travail. Quel monde injuste."

show lilly cane_giggle_ni
show hanako emb_emb_ni
with charachange


"Hanako et Lilly rient toutes deux de concert, savourant le fait qu'aucun membre du personnel ne soit aux alentours pour entendre notre protestation."

show lilly cane_smile_ni
show hanako basic_smile_ni
with charachange


li "Je suppose que venir d'une école stricte pour filles m'a aidée à Yamaku. Comparée à elle, Yamaku est beaucoup plus détendue."


"Ça expliquerait sa manière de s'exprimer et son comportement, en tout cas."

scene bg school_dormext_half_ni
show lilly cane_smile_ni at twoleft
show hanako basic_smile_ni at tworight
with locationskip


"Arrivant aux dortoirs, il est finalement l'heure de se séparer pour nos chambres respectives."


hi "À plus tard Lilly, Hanako."


"Elles hochent toutes deux poliment la tête avant de s'engouffrer dans le dortoir des filles, juste à côté de celui des garçons."

stop music fadeout 4.0

hide lilly
hide hanako
with charaexit


"Comme on pouvait s'y attendre d'un tel agencement, il y a un membre du personnel qui patrouille pour éviter toute manigance nocturne."


"Passant à côté de lui, j'étire rapidement mes bras et me frotte le cou, endolori d'avoir travaillé sur le sol pendant si longtemps, avant d'avancer vers ma chambre."


"Ça fait du bien d'avoir des directives, cela dit. Après tant de temps à l'hôpital, les trucs de tous les jours comme étudier, les devoirs et les professeurs, semblent presque être une bénédiction."


"Je pense que si les choses continuent comme ça, mon séjour à Yamaku pourrait se révéler être agréable."


label fr_A24a:

scene bg school_dormhisao_ni
with locationskip


"Adhérant à la voix lancinante de l'infirmier à l'arrière de ma tête, je mets mon alarme pour me réveiller assez tôt pour aller courir."


"J'ai fait une promesse et je vais la tenir. D'ailleurs, Emi me cafterait si je ne me montre pas."


"Mais ce n'est pas si mal que ça."

$ suppress_window_after_timeskip = True

scene black
with shuteye


label fr_A24b:

scene bg school_dormhisao_ni
with locationskip


"Je me sens fatigué donc je mets mon réveil pour me réveiller aussi tard que je peux me le permettre, tout en étant à l'heure pour la première heure."


"La voix de l'infirmier est presque lancinante à l'arrière de ma tête à propos du jogging du matin. Je prends la résolution de me rattraper en allant faire une balade après l'école demain."


"Je parie qu'Emi s'en moque de toute façon."

$ suppress_window_after_timeskip = True

scene black
with shuteye

return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
