

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<tbody>
<tr>
<td rowspan="2"><img src="images/image1.jpeg"
style="width:1.38681in;height:1.47153in"
alt="logo_IGN_pour_lettre" /></td>
<td style="font-size: 24px;text-align: center;"><p><strong>Manuel utilisateur du plugin
« Jeux d’attributs »</strong></p>
<p><strong>V0.3.0</strong></p></td>
</tr>
<tr>
<td style="font-size: 16px;text-align: center;">Développeur  : Gérôme PECHEUR (IGN)</td>
</tr>
</tbody>
</table>

## Sommaire

- [1. Prérequis](#prerequis)

- [2. Résumé](#resume)

- [3. Installation](#installation)

- [4. Présentation](#presentation)

 - [5. Configuration](#configuration)

 - [6. Utilisation](#utilisation)

 - [7. A propos](#a-propos)



<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="prerequis" style="color: white;margin:0;" >1. Prérequis</h2>
</div>


Version de QGIS : 3.28 ou supérieur, y compris QGIS4

Le plugin « maitre » doit préalablement être installé : 
[maitre-qgis-plugin sur GitHub](https://github.com/IGNF/maitre-qgis-plugin)

<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="resume" style="color: white;margin:0;" >2. Résumé</h2>
</div>

Ce plugin facilite la modification des attributs des entités.

<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="installation" style="color: white;margin:0;" >3. Installation</h2>
</div>

Le plugin s’installe soit en chargeant le zip dans QGIS, soit en lançant
l’exécutable d’installation : (\*\_PluginIGN_Installer.exe).

<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="presentation" style="color: white;margin:0;" >4. Présentation</h2>
</div>

A l’ouverture du plugin on obtient :

<img src="images/image2.png"
style="width:2.29301in;height:0.48079in" />

Ici, pas de configuration

Exemple après configuration :

<img src="images/image3.png"
style="width:6.83889in;height:0.66111in" />

<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="configuration" style="color: white;margin:0;" >5. Configuration</h2>
</div>

<img src="images/image4.png"
style="width:0.2292in;height:0.2292in" /> : Permet de configurer la
valeur d’un champ à modifier sur les entités sélectionnées dans QGIS

<img src="images/image5.png"
style="width:2.0275in;height:2.4236in" />

Les champs et les valeurs proposés correspondent à ceux de la couche
active.

Il est possible de passer d’une couche à une autre, l’interface
s’actualisera.

La validation via <img src="images/image6.png"
style="width:0.9804in;height:0.17633in" />, va ajouter des boutons pour
chaque valeur dans l’interface.

Il est possible d’y ajouter plusieurs valeurs pour un même champ.

Après configuration on obtient :

<img src="images/image3.png"
style="width:6.83889in;height:0.66111in" />

Une fois cette étape effectuée, il est possible de modifier le nom d’un
bouton, d’y ajouter une icône ou de lui associer d’autres attributs à
modifier

Pour ce faire, faites un clic droit sur un bouton :

<img src="images/image7.png"
style="width:2.94962in;height:2.53499in" />

Un bouton doit avoir obligatoirement un nom et/ou une icône.

Si les deux sont renseigné, la priorité est l’icône.

On peut également choisir d’autre attributs à associer au bouton, via :
<img src="images/image8.png"
style="width:0.56258in;height:0.25003in" />

On obtient :

<img src="images/image9.png"
style="width:1.78804in;height:2.13736in" />

Cette fois-ci, vous ne pouvez sélectionner qu’une seule valeur par
champ, puisqu’une entité ne peut posséder qu’une seule valeur pour un
champ donné.

On obtient ainsi :

<img src="images/image10.png"
style="width:2.76232in;height:2.37402in" />

Répétez l’opération pour chaque bouton et pour chaque couche, si
nécessaire.

 
<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="utilisation" style="color: white;margin:0;" >6. Utilisation</h2>
</div>

Il est possible de réorganiser l’ordre des boutons par simple
glissé-déposé.

Clic gauche sur un bouton, on le déplace sur un autre bouton, il se
placera juste avant celui ci

Le survol d’un bouton affiche une info bulle avec toutes les valeurs des
différents champs pris en compte.

<img src="images/image11.png"
style="width:3.19836in;height:1.26059in" />

Dans QGIS, après la sélection d’une ou de plusieurs entités, l’appui sur
un bouton entraîne la modification sémantique correspondant à la
configuration du bouton activé.


<div  style="background-color: #00ADC5; border: 1px solid black; padding: 5px; text-align: justify;margin-bottom:10px;">
  <h2 id="a-propos" style="color: white;margin:0;" >7. A propos</h2>
</div>

Accessible via <img src="images/image4.png"
style="width:0.2292in;height:0.2292in" /> puis
<img src="images/image12.png"
style="width:1.44812in;height:0.26045in" />

On obtient :

<img src="images/image13.png"
style="width:3.15336in;height:2.42938in" />

Cette boite permet de suivre l’historique des différentes versions ainsi
que d’afficher cette documentation.
