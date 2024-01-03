from faker import Faker

person = Faker("pl_PL")

for _ in range(10):
    print(person.name(), person.address(), person.credit_card_full())