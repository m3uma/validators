# ZESTAW WALIDATORÓW

> Waliduje:

* haslo

Hasło ma mieć minimum 7 znaków, powinno zawierać:
1. przynajmniej jedną wielką literę,
2. przynajmniej jedną małą literę,
3. przynajmniej jedną cyfrę,
4. przynajmniej jedną cyfrę,
5. przynajmniej jeden znak specjalny z zakresu: !@#$%^&*()_+-={}[]|\:";'<>?,./",

Dodatkowo zawiera funkcję haszującą hasło;

* pesel

Służy walidacji numeru PESEL dla osób urodzonych przed i po roku 1999. Zwraca również płeć i datę urodzenia;

* mail

Służy walidacji adresu email;

* id

Służy walidacji numeru dowodu osobistego;

* adres

Służy walidacji adresu wraz z kodem pocztowym;

> Zastosowanie

* walidacja nr pesel - walidacja pól np. logowanie, rejestracja (oba formaty PESEL);
* podczas rejestracji użytkownika może służyć to uzupełnienia pól "płeć" i "data urodzenia";
* walidacja danych osobowych we wszystkich formularzach rejetracyjnych;


> Przykłady

W formularzach logowania i rejestracji nr PESEL ma szerokie zastosowanie we wszelkich aplikacjach związanych z:
* wszelkimi organami publicznymi,
* profilem zaufanym,
* jednostkami służby zdrowia etc.

Wprowadzony od 01.01.2020 system e-recept opiera się na PESEL(login) i podany 4-cyfrowy, przypisany do PESEL nr recepty.









