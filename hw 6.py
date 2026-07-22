import faker  # библиотека для генерации рандомных фейковых данных
fake = faker.Faker()


print(fake.name())
print(fake.email())
print(fake.password())