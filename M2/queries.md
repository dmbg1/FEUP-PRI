### Does Alex (author) write news about Russia?
```
q.op = AND

author:Alex;
title:Russia;
body_en:Russia OR body_de:Russia OR body_fr:Russia OR body_es:Russia OR body_ru:Russia;
```

### Conspiracy fake news about the FBI
TODO Adicionar palavra conspiracy e weights
```
title:FBI OR body_fr:FBI OR body_en:FBI OR body_de:FBI OR body_es:FBI OR body_ru:FBI;
type:conspiracy;
```

### What highly spammy news have there been about war?
```
sort = spam_score desc

title:war OR body_fr:war OR body_en:war OR body_de:war OR body_es:war OR body_ru:war;
```

### Fake news related to the presidential elections in the United States
```
q.op = AND

country:US
(title:"elections" OR body_fr:"elections" OR body_en:"elections" OR body_de:"elections" OR body_es:"elections" OR body_ru:"elections")
```

### Fake news in Colombia about the US
```
q.op = AND

country:CO
(title:US OR body_fr:US OR body_en:US OR body_de:US OR body_es:US OR body_ru:US) OR (title:"United States" OR body_fr:"United States" OR body_en:"United States" OR body_de:"United States" OR body_es:"United States" OR body_ru:"United States")
```
