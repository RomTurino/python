import random
import time


class Character:
    def __init__(self, name, ultimate):
        self.name = name
        self.health = 100
        self.mana = 0
        self.ultimate = ultimate
    def attack(self, enemy):
        enemy -= random.randint(1,5)#отнимаем жизни врага
        self.mana += random.randint(1,5)#прибавление к нашей мане
        print(f'{self.name} атакует {enemy.name}, у него {enemy.health} hp')
        return enemy.health
    def super_attack(self, enemy):
        enemy.health -= random.randint(6,10)#отнимаем жизни врага
        self.mana -= 10 #Убавление маны
        ulta = random.choice(self.ultimate)
        print(f'{self.name} атакует {enemy.name}, используя {ulta}, у него {enemy.health} hp')
        if self.name == 'Бэтмен':
            enemy_health -= enemy_health
            print(f'{self.name} победил {enemy.name}.')
        return enemy.health  
        

scorpion = Character(name='Скорпион', ultimate=[
                     'GET OVER HERE!', 'Атака цепью'])
sab_zero = Character(name='Саб-зиро', ultimate=['Охладуся', 'Замерзайка'])
gorr = Character(name='Горр', ultimate=['Недружественное рукопожатие', 'Суперхват'])
predator = Character('Хищник', ['Лазерная указка', 'Удар невидимки'])
jason = Character('Джейсон', ['Удар бензопилой', 'Нечестивое воскрешение'])
reiden = Character("Рейден", ['Грозовой шквал', 'Чидори'])
batman = Character('Бэтмен', ['ПОТОМУ ЧТО Я БЭТМЕН', 'Непобедимая атака'])
divora = Character('Дивора', ['Желчная атака', 'Миллионы жуков'])


enemies = [scorpion, sab_zero, gorr, predator, jason, reiden, batman, divora]
def fighting():
    enemy1 = random.choice(enemies)#выбрали первого персонажа
    enemies.remove(enemy1)#убрали персонажа, который выпал
    enemy2 = random.choice(enemies)#выбрали второго персонажа
    print(f'{enemy1.name} VS {enemy2.name}')

    hit = 0
    while True:
        hit+=1
        print(f'\nУдар {hit}')
        time.sleep(2)
        enemy1.health = enemy2.attack(enemy1)
        enemy2.health = enemy1.attack(enemy2)
        
        coin = random.randint(1,2)
        if enemy1.mana > 7:
            if coin == 1:
                enemy2.health = enemy1.super_attack(enemy2)
                enemy1.mana -= 7
        if enemy2.mana > 7:
            if coin == 1:
                enemy1.health = enemy2.super_attack(enemy1)
                enemy2.mana-=7
        if enemy1.health <=0 and enemy2.health <=0:
            print('Ничья')
            break
        elif enemy1.health <=0:
            print(f'Победа игрока {enemy2.name}')
            break
        elif enemy2.health <=0:
            print(f'Победа игрока {enemy1.name}')
            break