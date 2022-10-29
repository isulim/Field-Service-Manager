# Field Service Manager
Aplikacja do zarządzania pracą serwisu aparatury medycznej (Django, SQLite3, jQuery, Bootstrap). <br>

Aplikacja zawiera bazę danych złożoną z tabel szpitali, urządzeń (w tym opiekunów urządzeń), zleceń oraz raportów serwisowych.<br>
Można przeglądać listę urządzeń, ich historię. Urządzenia są skategoryzowane według producentów oraz typu.<br>
Na głównej stronie wyświetlany jest kalendarz, w którym zanotowane są umówione zlecenia z oddzielnym kolorem dla każdego inżyniera.

## Grupy użytkowników
#### Inżynierowie
Użytkownicy z grupy "inżynierowie" mogą wyświetlać urządzenia, ich historie (przeglądać przeszłe raporty), przeglądać zlecenia, dodawać raporty do umówionych niezamkniętych zleceń. Dodanie raportu serwisowego powoduje zamknięcie zlecenia. <br>
Uprawnienia grupy "inżynierowie" są otwarte bez zalogowania.

#### Biuro
Użytkownicy z grupy "biuro" mogą rejestrować nowe zlecenia, umawiać zlecenia w kalendarzu, dodawać nowe urządzenia do bazy oraz edytować ich dane (w ograniczonym zakresie), dodawać i edytować opiekunów sprzętu oraz dodawać i edytować szpitale w bazie.<br>
Użytkownicy "biuro" mają również wszystkie uprawnienia użytkowników "inżynierowie".
Aby skorzystać z uprawnień grupy "biuro" należy zalogować się następującymi danymi:<br>
<b>Użytkownik: biuro</b><br>
<b>Hasło: biuro</b>
