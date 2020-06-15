# Kurssiseurantatyökalu

[Kurssiseurantatyökaluun](https://courseeditor.herokuapp.com/)

Tämä on Helsingin yliopiston [tietokantasovellus](https://materiaalit.github.io/tsoha-20/osa0/)-kurssin projekti

Kurssiseurantatyökalun avulla opiskelija voi sisäänkirjautuneena tarkastella omia
käynnissäolevia kursseja, tulevia kursseja ja suorituksia. Opiskelija voi lisätä kursseja,
selailla lisäämiään kursseja ja suodattaa niitä nimen perusteella.
Opiskelija voi tallentaa itselleen muistiin kursseja, joita hän haluaisi käydä 
tulevaisuudessa tai jotka hän on jo suorittanut. Opiskelija voi poistaa kursseja toive- ja suorituslistoiltaan.

[Tietokantakaavio](https://github.com/AnnaKuokkanen/Kurssiseuranta/blob/master/Dokumentaatio/tietokantakaavio.md)

[Käyttötapaukset](https://github.com/AnnaKuokkanen/Kurssiseuranta/blob/master/Dokumentaatio/k%C3%A4ytt%C3%B6tapaukset.md)

[Käyttöohje](https://github.com/AnnaKuokkanen/Kurssiseuranta/blob/master/Dokumentaatio/k%C3%A4ytt%C3%B6ohje.md)

[Asennusohje](https://github.com/AnnaKuokkanen/Kurssiseuranta/blob/master/Dokumentaatio/asennusohje.md)

## Toimintoja: 

* rekisteröityminen
* sisäänkirjautuminen
* kurssien tarkastelu
* kurssien lisääminen
* kurssien poistaminen
* kurssien statuksen päivittäminen (sunnitelma/suoritus)
* kurssin tietojen päivittäminen (nimi/sisältö/ajankohta)
* kurssien hakeminen nimen perusteella
* kurssin suoritetuksi tai suunnitelluksi lisääminen
* sunnitelmien ja suoritusten tarkastelu
* omien tietojen (etu-/sukunimen) päivitys
* oman profiilin poistaminen

## Kirjautuminen

Sovellukseen rekisteröidytään tavallisena käyttäjänä. Tässä tunnukset, joilla saa käyttöönsä admin-tasoisen käyttäjän:
```
käyttäjänimi: ellavirta
salasana: salasana
```


## Huomioitavaa:

Toistaiseksi sovellukseen ei ole toteutettu ominaisuutta, jolla admin voisi antaa admin-oikeutensa tavallisille käyttäjille.
Sovellukseen rekisteröidytään tavalisena käyttäjänä. Tavallisen käyttäjän rajoituksiin kuuluu kurssien poisto.
