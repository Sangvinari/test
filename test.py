# import threading
# import time
# from datetime import datetime

# class Sim:
#     def __init__(self, name="Сим"):
#         self.name = name
#         # Потребности от 0 до 100, по умолчанию 100
#         self.hunger = 100      # Голод
#         self.energy = 100      # Энергия/Сон
#         self.bladder = 100     # Туалет
#         self.hygiene = 100    # Гигиена
#         self.social = 100     # Общение
#         self.fun = 100        # Развлечения
#         self.comfort = 100    # Комфорт
        
#         # Флаг для остановки потока
#         self.running = True
        
#         # Запускаем поток для уменьшения потребностей
#         self.thread = threading.Thread(target=self._decrease_needs, daemon=True)
#         self.thread.start()
    
#     def _decrease_needs(self):
#         """Уменьшает все потребности на 1 каждые 5 секунд"""
#         while self.running:
#             time.sleep(5)  # Каждые 5 секунд
            
#             # Уменьшаем все потребности на 1, но не ниже 0
#             self.hunger = max(0, self.hunger - 1)
#             self.energy = max(0, self.energy - 1)
#             self.bladder = max(0, self.bladder - 1)
#             self.hygiene = max(0, self.hygiene - 1)
#             self.social = max(0, self.social - 1)
#             self.fun = max(0, self.fun - 1)
#             self.comfort = max(0, self.comfort - 1)
    
#     def stop(self):
#         """Останавливает уменьшение потребностей"""
#         self.running = False
#         self.thread.join(timeout=1)
    
#     def show_needs(self):
#         """Показывает текущий уровень всех потребностей"""
#         print(f"\n=== Потребности {self.name} ===")
#         print(f"Голод:     {self.hunger}/100")
#         print(f"Энергия:   {self.energy}/100")
#         print(f"Туалет:    {self.bladder}/100")
#         print(f"Гигиена:   {self.hygiene}/100")
#         print(f"Общение:   {self.social}/100")
#         print(f"Развлеч:   {self.fun}/100")
#         print(f"Комфорт:   {self.comfort}/100")
#         print("=" * 30)
    
#     # Методы для восполнения потребностей
#     def eat(self, amount=20):
#         """Поесть"""
#         self.hunger = min(100, self.hunger + amount)
#         print(f"{self.name} поел. Голод: {self.hunger}/100")
    
#     def sleep(self, amount=30):
#         """Поспать"""
#         self.energy = min(100, self.energy + amount)
#         print(f"{self.name} поспал. Энергия: {self.energy}/100")
    
#     def use_toilet(self, amount=40):
#         """Сходить в туалет"""
#         self.bladder = min(100, self.bladder + amount)
#         print(f"{self.name} сходил в туалет. Потребность: {self.bladder}/100")
    
#     def shower(self, amount=50):
#         """Принять душ"""
#         self.hygiene = min(100, self.hygiene + amount)
#         print(f"{self.name} принял душ. Гигиена: {self.hygiene}/100")
    
#     def talk(self, amount=15):
#         """Поговорить"""
#         self.social = min(100, self.social + amount)
#         print(f"{self.name} пообщался. Общение: {self.social}/100")
    
#     def play(self, amount=25):
#         """Поиграть"""
#         self.fun = min(100, self.fun + amount)
#         print(f"{self.name} поиграл. Развлечения: {self.fun}/100")
    
#     def relax(self, amount=10):
#         """Отдохнуть"""
#         self.comfort = min(100, self.comfort + amount)
#         print(f"{self.name} отдохнул. Комфорт: {self.comfort}/100")


# # Пример использования
# if __name__ == "__main__":
#     # Создаем сима
#     sim = Sim("Елизавета")
    
#     try:
#         # Показываем начальные потребности
#         sim.show_needs()
        
#         # Ждем 15 секунд, потребности будут уменьшаться каждые 5 секунд
#         print("\nЖдем 15 секунд...")
#         time.sleep(15)
        
#         # Показываем потребности после уменьшения
#         sim.show_needs()
        
#         # Восполняем потребности
#         print("\n--- Восполняем потребности ---")
#         sim.eat(30)
#         sim.sleep(40)
#         sim.use_toilet()
#         sim.shower()
#         sim.talk(25)
#         sim.play(35)
#         sim.relax(20)
        
#         # Финальные потребности
#         sim.show_needs()
        
#     finally:
#         # Останавливаем поток при завершении
#         sim.stop()

import time
#Hello world

class Sim:
    def __init__(self, name="Сим"):
        self.name = name
        # Потребности от 0 до 100
        self.hunger = 100      # Голод
        self.energy = 100      # Энергия/Сон
        self.bladder = 100     # Туалет
        self.hygiene = 100     # Гигиена
        self.social = 100      # Общение
        self.fun = 100         # Развлечения
    
    def decrease_needs(self):
        """Уменьшает все потребности на 1"""
        self.hunger = max(0, self.hunger - 1)
        self.energy = max(0, self.energy - 1)
        self.bladder = max(0, self.bladder - 1)
        self.hygiene = max(0, self.hygiene - 1)
        self.social = max(0, self.social - 1)
        self.fun = max(0, self.fun - 1)
    
    # Методы для восполнения потребностей
    def eat(self, amount=20):
        self.hunger = min(100, self.hunger + amount)
        print(f"🍽️  {self.name} поел. Голод: {self.hunger}/100")
    
    def sleep(self, amount=30):
        self.energy = min(100, self.energy + amount)
        print(f"😴 {self.name} поспал. Энергия: {self.energy}/100")
    
    def use_toilet(self, amount=40):
        self.bladder = min(100, self.bladder + amount)
        print(f"🚽 {self.name} сходил в туалет. Потребность: {self.bladder}/100")
    
    def shower(self, amount=50):
        self.hygiene = min(100, self.hygiene + amount)
        print(f"🚿 {self.name} принял душ. Гигиена: {self.hygiene}/100")
    
    def talk(self, amount=15):
        self.social = min(100, self.social + amount)
        print(f"🗣️  {self.name} пообщался. Общение: {self.social}/100")
    
    def play(self, amount=25):
        self.fun = min(100, self.fun + amount)
        print(f"🎮 {self.name} поиграл. Развлечения: {self.fun}/100")
    
    def show_needs(self):
        """Показывает текущий уровень всех потребностей"""
        print(f"\n=== {self.name} ===")
        print(f"Голод:     {'█' * (self.hunger//10)}{'░' * (10 - self.hunger//10)} {self.hunger:3d}/100")
        print(f"Энергия:   {'█' * (self.energy//10)}{'░' * (10 - self.energy//10)} {self.energy:3d}/100")
        print(f"Туалет:    {'█' * (self.bladder//10)}{'░' * (10 - self.bladder//10)} {self.bladder:3d}/100")
        print(f"Гигиена:   {'█' * (self.hygiene//10)}{'░' * (10 - self.hygiene//10)} {self.hygiene:3d}/100")
        print(f"Общение:   {'█' * (self.social//10)}{'░' * (10 - self.social//10)} {self.social:3d}/100")
        print(f"Развлеч:   {'█' * (self.fun//10)}{'░' * (10 - self.fun//10)} {self.fun:3d}/100")
        print("=" * 30)


# Пример использования - все последовательно
if __name__ == "__main__":
    sim = Sim("Елизавета")
    
    # Игровой цикл - все действия по очереди
    for hour in range(1, 25):  # 24 часа в сутках
        print(f"\n--- Час {hour} ---")
        
        # Уменьшаем потребности (как будто прошел час)
        sim.decrease_needs()
        sim.decrease_needs()  # два раза, чтобы было заметнее
        sim.show_needs()
        
        # Принимаем решения на основе потребностей
        if sim.hunger < 50:
            sim.eat()
        
        if sim.energy < 40:
            sim.sleep()
        
        if sim.bladder < 30:
            sim.use_toilet()
        
        if sim.hygiene < 40:
            sim.shower()
        
        if sim.social < 30:
            sim.talk()
        
        if sim.fun < 30:
            sim.play()
        
        time.sleep(1)  # пауза для наглядности