"""

Uzupełnij wyświetlany tekst o nazwiska aktorów zapisane w zmiennych  actor1, actor2 i actor3 (w tej kolejności). Nie zmieniając wartości samych zmiennych, zadbaj o to, aby w wyświetlanym komunikacie imiona i nazwiska zaczynały się z dużych liter oraz aby dane poszczególnych aktorów oddzielone były przecinkiem i spacją. W konsoli cały tekst ma znaleźć się w jednym wierszu. Na jego końcu wstaw kropkę.

Wyświetlony komunikat powinien wyglądać tak:
Gran Torino cast: Clint Eastwood, Bee Vang, Scott Eastwood.

Uwaga:  możesz użyć najwyżej dwóch funkcji print() i nie możesz używać operatora +. Do boju! :)
"""
actor1 = "clint eastwood"
actor2 = "bee vang"
actor3 = "scott eastwood"

print("Gran Torino cast: ", end="")
print(actor1.title(), actor2.title(), actor3.title(), sep=", ",end=".")