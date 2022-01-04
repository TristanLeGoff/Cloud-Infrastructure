# Cloud-Infrastructure

Nom du DataSet : SMMnet (A Temporal Dataset from Super Mario Maker)

Lien : [https://www.kaggle.com/leomauro/smmnet?select=course-meta.csv](https://www.kaggle.com/leomauro/smmnet?select=course-meta.csv)

Ce projet a pour but de passer d'une base de donnée relationnel simple type SQL a une base de donnée NoSql ici MongoDb.  

Pour cela nous devons d'abord réaliser une dernomalisation pour transformer les nombreux fichier csv en seulement 2 fichiers json.  

Ensuite nous exporterons cette dénormalisation sur une base de donnée MongoDB réparti sur des shards grâce à une clé de sharding.  
Sur ce projet nous avons donc dû créer une infrastructure complète grâce à 10 machines virtuelles afin de tester le temps de réponse de chaque requête en fonction du nombre de shards et nous sommes allés jusqu'à 8 shards ce qui réduit grandement le temps de réponse de la plupart des requêtes.

Nous pouvons ensuite créer plusieurs application "réelles" afin de tirer profit de cette base de données et de ces requêtes qui sont maintenant très scalable si l'on souhaite grandement augmenter le nombre de documents dans la base de données
