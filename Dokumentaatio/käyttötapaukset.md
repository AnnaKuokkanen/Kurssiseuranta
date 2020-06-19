### Käyttäjänä haluan rekisteröityä.

```
INSERT INTO User (firstname, lastname, username, password) 
VALUES (etunimi, sukunimi, käyttäjänimi, salasana)
```

### Käyttäjänä haluan kirjautua sisään, jotta voin tarkastella henkilökohtaisia muistiinpanojani.

```
SELECT firstname, lastname FROM User
WHERE User.username = ? AND User.password = ?
```

### Käyttäjänä haluan lisätä käynnissäolevia kurssejani listaan, jotta voin pitää kirjaa opiskelustani.

```
INSERT INTO Course (name, content, time)
VALUES (nimi, sisältö, ajankohta)
```

### Käyttäjänä haluan lisätä kursseja toivelistaani, jotta voin suunnitella opiskeluani.

```
UPDATE Course
SET planned = True
WHERE Course.id = ?
```

### Käyttäjänä haluan merkitä käymiäni kursseja tehdyiksi.

```
UPDATE Course
SET completed = True
WHERE Course.id = ?
```

### Käyttäjänä haluan filtteröidä kursseja nimen perusteella.

```
SELECT name, content, time FROM Course
WHERE Course.name = ?
```

### Käyttäjänä haluan poistaa lisäämiäni kursseja.  

```
DELETE FROM Course
WHERE Course.id = ?
```

### Käyttäjänä haluan muokata henkilötietojani

```
UPDATE User
SET firstname = ? AND lastname = ?
WHERE User.id = current_user.id
```

### Käyttäjänä haluan poistaa profiilini

```
DELETE FROM User
WHERE User.id = current_user.id
```
