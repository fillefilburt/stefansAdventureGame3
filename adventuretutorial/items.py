# used for items


class Item:
    # The base class for all items
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Coppers(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name='coppers',
                         description='Little pieces of metal that can be used as a means of exchange.',
                         value=self.amt)


class Broom(Item):
    def __init__(self):
        super().__init__(name='broom',
                         description='It\'s a broom. You can sweep floors with it. And chase away rats.',
                         value=0)


class Shovel(Item):
    def __init__(self):
        super().__init__(name='shovel',
                         description='A shovel can be used to shovel things, like horse shit, snow or what not.',
                         value=0)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name='Dagger',
                         description='A dagger. It\'s double edged with a reasonably sharp point.',
                         value=10,
                         damage=10)
