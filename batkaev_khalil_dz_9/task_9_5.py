class Stationery():

    def __init__(self, title):
        self._title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):

    def draw(self):
        print('Рисуем ручкой')

class Pencil(Stationery):

    def draw(self):
        print('Набросок карандашом')

class Handle(Stationery):
    def draw(self):
        print('Отмечаем маркером')

stylus = Stationery('Перо')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')

stylus.draw()
pen.draw()
pencil.draw()
handle.draw()
