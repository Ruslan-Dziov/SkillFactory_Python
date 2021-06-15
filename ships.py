import random, time


class ShipConstruction:
    coord_occup = []
    coord_environ = []
    count_small = 0
    count_medium = 0
    dict_ships = {}
    @staticmethod
    def input_coordinates(coord_occup, coord_environ):
        """
        Функция отвечает за ввод координат,
        проверяет занята ли координата,
        исключает ошибки ввода (1 - int, 2 - диапазон от 1 до 6)
        :return: возвращает проверенные координаты в кортеже - (x, y)
        """
        while True:
            try:
                x = int(input('x = '))
                y = int(input('y = '))
                if (x, y) in coord_occup:#ShipConstruction.coord_occup:
                    print('эта координата использовалась')
                    continue
                elif (x, y) in coord_environ:#ShipConstruction.coord_environ:
                    print('корабли должны находится на расстоянии 1 клетка друг от друга')
                    continue
                if 1 > x or x > 6 or 1 > y or y > 6:
                    raise ValueError
            except ValueError:
                print('координаты должны быть целыми числами, от 1 до 6')
            else:
                break
        return x, y

    def ship_modules(self, ship_size):
        """
        Функция отвечает за количество координат модулей корабля в соответствии с его размером,
        :param ship_size: принимает параметр размера корабля (1, 2 или 3-х палубный)
        :return: возвращает координаты корабля в виде списка кортежей (x, y)
        """
        ship_coord = []
        for coord in range(ship_size):
            modul = ShipConstruction.input_coordinates(ShipConstruction.coord_occup, ShipConstruction.coord_environ)
            ship_coord.append(modul)
        return ship_coord

    def ship_check_line(self, ship_size):
        """
        Функция овечает за проверку правильности постоения корабля игроком.
        Проверка по двум параметрам: 1 - корабль должен быть в линию по оси x или y,
        2 - корабль должен состоять из подряд идущих точек (без промежутков)
        координаты сохраняются в глобальный список класса.
        :param ship_size: принимает параметр размера корабля (1, 2 или 3-х палубный)
        :return: возвращает проверенные координаты корабля в виде списка кортежей (x, y)
        """
        ok_cond = 0
        ship_coord = []
        name = ''
        while ok_cond == 0:
            ship_coord = self.ship_modules(ship_size)
            if ship_size == 2:
                fir_cond2 = (ship_coord[0][0] == ship_coord[1][0] or ship_coord[0][1] == ship_coord[1][1])
                sec_cond2 = (abs(ship_coord[0][0] - ship_coord[1][0]) == 1 or abs(ship_coord[0][1] - \
                                                                                  ship_coord[1][1]) == 1)
                if fir_cond2 and sec_cond2:
                    ok_cond = 1
                    ShipConstruction.count_medium += 1
                    name = f'{ShipConstruction.count_medium}-й средний корабль'
            if ship_size == 3:
                list_x = [ship_coord[0][0], ship_coord[1][0], ship_coord[2][0]]
                list_y = [ship_coord[0][1], ship_coord[1][1], ship_coord[2][1]]
                list_x.sort()
                list_y.sort()
                fir_cond3 = (list_x[2] - list_x[1] == 1 and list_x[1] - list_x[0] == 1) or\
                            (list_y[2] - list_y[1] == 1 and list_y[1] - list_y[0] == 1)
                sec_cond3 = (ship_coord[0][0] == ship_coord[1][0] == ship_coord[2][0] or \
                             ship_coord[0][1] == ship_coord[1][1] == ship_coord[2][1])
                if fir_cond3 and sec_cond3:
                    ok_cond = 1
                    name = 'большой корабль'

            if ship_size == 1:
                ok_cond = 1
                ShipConstruction.count_small += 1
                name = f'{ShipConstruction.count_small}-й малый корабль'
            if ok_cond == 0:
                print('модули корабля должны быть в ряд по оси X или Y')
        dict_ = {name: ship_coord}
        ShipConstruction.dict_ships.update(dict_)
        for modul in ship_coord:
            ShipConstruction.coord_occup.append(modul)
        list_occup = self.ship_environ(ShipConstruction.coord_occup, ShipConstruction.coord_environ)
        for element in list_occup:
            ShipConstruction.coord_environ.append(element)
        return ship_coord

    def ship_environ(self, coord_occup, coord_environ):
        """
        Функция определяет зону вокруг корабля равную 1 клетке
        :param coord_occup: координаты всех кораблей списком
        :param coord_environ: список координат входящих в зону которая предусматривает расстояние
        1 клетка между кораблями
        :return: координаты зоны вокруг корабля
        """
        self.coord_occup = coord_occup
        self.coord_environ = coord_environ
        list__ = []
        for i in coord_occup:
            p1 = (i[0] + 1, i[1])
            p2 = (i[0] - 1, i[1])
            p3 = (i[0], i[1] + 1)
            p4 = (i[0], i[1] - 1)
            p5 = (i[0] + 1, i[1] + 1)
            p6 = (i[0] + 1, i[1] - 1)
            p7 = (i[0] - 1, i[1] + 1)
            p8 = (i[0] - 1, i[1] - 1)
            list__.extend((p1, p2, p3, p4, p5, p6, p7, p8))
        list_temp = []
        for coords in list__:
            list_coord = []
            for coord in coords:
                if coord == 0:
                    coord = 1
                    list_coord.append(coord)
                elif coord == 7:
                    coord = 6
                    list_coord.append(coord)
                else:
                    list_coord.append(coord)
            list_temp.append(list_coord)
        li = list(set(map(tuple, list_temp)))
        for element in li:
            coord_environ.append(element)
        return li

    @staticmethod
    def print_board():
        """
        Выводит доску
        :return:
        """
        # Game.computer_shots = computer_shots
        bm = ShipConstruction.data_board(Game.computer_shots, ShipConstruction.coord_occup)
        cm = ShipConstruction.data_board(Game.human_shots, Game.human_hit)
        print(f'''
        
              ТВОИ КОРАБЛИ                        ТВОИ ВЫСТРЕЛЫ
         И ВЫСТРЕЛЫ КОМПЬЮТЕРА                     И ПОПАДАНИЯ

     _ | 1 | 2 | 3 | 4 | 5 | 6 |           _ | 1 | 2 | 3 | 4 | 5 | 6 |
     1 | {bm[(1, 1)]} | {bm[(2, 1)]} | {bm[(3, 1)]} | {bm[(4, 1)]} | {bm[(5, 1)]} | {bm[(6, 1)]} |           1 | {cm[(1, 1)]} | {cm[(2, 1)]} | {cm[(3, 1)]} | {cm[(4, 1)]} | {cm[(5, 1)]} | {cm[(6, 1)]} |
     2 | {bm[(1, 2)]} | {bm[(2, 2)]} | {bm[(3, 2)]} | {bm[(4, 2)]} | {bm[(5, 2)]} | {bm[(6, 2)]} |           2 | {cm[(1, 2)]} | {cm[(2, 2)]} | {cm[(3, 2)]} | {cm[(4, 2)]} | {cm[(5, 2)]} | {cm[(6, 2)]} | 
     3 | {bm[(1, 3)]} | {bm[(2, 3)]} | {bm[(3, 3)]} | {bm[(4, 3)]} | {bm[(5, 3)]} | {bm[(6, 3)]} |           3 | {cm[(1, 3)]} | {cm[(2, 3)]} | {cm[(3, 3)]} | {cm[(4, 3)]} | {cm[(5, 3)]} | {cm[(6, 3)]} |
     4 | {bm[(1, 4)]} | {bm[(2, 4)]} | {bm[(3, 4)]} | {bm[(4, 4)]} | {bm[(5, 4)]} | {bm[(6, 4)]} |           4 | {cm[(1, 4)]} | {cm[(2, 4)]} | {cm[(3, 4)]} | {cm[(4, 4)]} | {cm[(5, 4)]} | {cm[(6, 4)]} |
     5 | {bm[(1, 5)]} | {bm[(2, 5)]} | {bm[(3, 5)]} | {bm[(4, 5)]} | {bm[(5, 5)]} | {bm[(6, 5)]} |           5 | {cm[(1, 5)]} | {cm[(2, 5)]} | {cm[(3, 5)]} | {cm[(4, 5)]} | {cm[(5, 5)]} | {cm[(6, 5)]} |
     6 | {bm[(1, 6)]} | {bm[(2, 6)]} | {bm[(3, 6)]} | {bm[(4, 6)]} | {bm[(5, 6)]} | {bm[(6, 6)]} |           6 | {cm[(1, 6)]} | {cm[(2, 6)]} | {cm[(3, 6)]} | {cm[(4, 6)]} | {cm[(5, 6)]} | {cm[(6, 6)]} |



        ''')

    @staticmethod
    def data_board(computer_shot, coord_occup):

        board_matrix = {(1, 1): '_', (2, 1): '_', (3, 1): '_', (4, 1): '_', (5, 1): '_', (6, 1): '_',
                        (1, 2): '_', (2, 2): '_', (3, 2): '_', (4, 2): '_', (5, 2): '_', (6, 2): '_',
                        (1, 3): '_', (2, 3): '_', (3, 3): '_', (4, 3): '_', (5, 3): '_', (6, 3): '_',
                        (1, 4): '_', (2, 4): '_', (3, 4): '_', (4, 4): '_', (5, 4): '_', (6, 4): '_',
                        (1, 5): '_', (2, 5): '_', (3, 5): '_', (4, 5): '_', (5, 5): '_', (6, 5): '_',
                        (1, 6): '_', (2, 6): '_', (3, 6): '_', (4, 6): '_', (5, 6): '_', (6, 6): '_',
                        }

        for shots in computer_shot:
            board_matrix[shots] = 'X'
        for coord in coord_occup:
            board_matrix[coord] = '■'


        return board_matrix


class CompShipConstruction(ShipConstruction):
    coord_of_ship = []
    order = [] # хранит края доски (стороны) на которых расположенны корабли
    ships_dict = {} # словарь в котором хранятся корабли
    coord_environ = [] # координаты вокруг корабля в 1 клетку

    def ship_position(self):
        """
        функция размещает на доске корабли, стратегия выбрана таким образом, чтобы 3-х и 2-х палубные корабли
        размещались на краю доски, чтобы уменьшить зону исключения нахождения корабля. однопалубные корабли размещаются
        случайным образом в доступном месте, если не удается разместить последний корабль за 20 попыток, то флот
        строится заного.
        :return: возвращает координаты кораблей
        """
        while True:
            CompShipConstruction.coord_of_ship = []
            CompShipConstruction.order = []
            CompShipConstruction.ships_dict = {}
            CompShipConstruction.coord_environ = []
            small_ship_count = 0
            for i in range(7): # range(7) - 7 кораблей флота
                if i + 1 == 1:
                    name = 'большой корабль'
                elif 1 < i + 1 < 4:
                    name = f'{i}-й средний корабль'
                else:
                    name = f'{i - 2}-й малый корабль'
                if i > 2:
                    side = 0
                else:
                    while True:
                        side = random.randint(1, 4)     # случайным образом определяетсяя край доски на котором будет
                                                        # распологаться корабль
                        if side not in CompShipConstruction.order:
                            CompShipConstruction.order.append(side)
                            break
                if side == 1:
                    self.big_medium_ships(name, x=1, y=0)
                elif side == 2:
                    self.big_medium_ships(name, x=6, y=0)
                elif side == 3:
                    self.big_medium_ships(name, x=0, y=1)
                elif side == 4:
                    self.big_medium_ships(name, x=0, y=6)
                elif side == 0:
                    count = 0
                    while count < 20: # 20 попыток размещения 4-х однопалубных кораблей на оставшемся пространстве
                        x = random.randint(1, 6)
                        y = random.randint(1, 6)
                        if (x, y) in CompShipConstruction.coord_environ or (x, y) in CompShipConstruction.coord_of_ship:
                            count += 1
                        else:
                            CompShipConstruction.coord_of_ship.append((x, y))
                            list_size = [(x, y)]
                            dict_ = {name: list_size}
                            CompShipConstruction.ships_dict.update(dict_)
                            small_ship_count += 1
                            self.ship_environ(CompShipConstruction.coord_of_ship, CompShipConstruction.coord_environ)
                            break
            if small_ship_count == 4:
                break
        return CompShipConstruction.coord_of_ship

    def check_environ(self, x=0, y=0):
        """
        функция проверяет не попали ли координаты корабля в зону, которая предусматривает отдаленность кораблей друг
        от друга на 1 клетку. при вызове вункции в программе, указывается только одна координата в соответствии со
        стороной на которой будет находиться корабль, вторая координата определяется в этой функции.
        :param x: значение по оси Х (по умолчанию 0)
        :param y: значение по оси Y (по умолчанию 0)
        :return: координаты корабля
        """
        while True:
            list_size = []
            coord = self.second_coord()# получаем список вторых координат
            x_ = x
            y_ = y
            for c in coord:         # определяем какая координата равна 0,
                                    # с ней дальше работаем - присваеваем значения (2-х координат)
                if x_ == 0:
                    x = c
                elif y_ == 0:
                    y = c
                if (x, y) in CompShipConstruction.coord_environ:# проверяем каждую координату входит ли она в зону,
                                                                # если да то возвращаем значения и повторяем цикл
                    x = x_
                    y = y_
                    break
                else:
                    list_size.append((x, y))
            if len(list_size) == len(coord):        # условие выхода из цикла - количество вторых координат =
                                                    # количеству координат (x, y)
                break
        ship_size = list_size
        for list_ in ship_size:
            CompShipConstruction.coord_of_ship.append(list_)
        return ship_size

    def big_medium_ships(self, name, x, y):
        """
        Функция обновляет словарь с кораблями по мере их создания, получая координаты из функции check_environ(x, y),
        вызывает функцию которая определяет зону вокруг кораблей предусматривающую расстояние между кораблями 1 клетку
        :param name: название корабля
        :param x:
        :param y:
        :return: координаты зоны вокруг кораблей предусматривающую расстояние между кораблями 1 клетку
        """
        list_size = self.check_environ(x, y)
        dict_ = {name: list_size}
        CompShipConstruction.ships_dict.update(dict_)
        ship_size = self.ship_environ(CompShipConstruction.coord_of_ship, CompShipConstruction.coord_environ)
        return ship_size

    def second_coord(self):
        """
        эта функция размещает 3-х палубный корабль и 2-х палубные по краям доски, с учетом того, чтобы они не вышли за
        ее пределы. Первая координата определяетс исходя из стороны на которой находися корабль (side)
        :return: возвращает список вторых координат
        """
        a, b, c = 0, 0, 0
        sec_coord = []
        coord = random.randint(1, 6) # выбирается случайная величина второй координаты
        sec_coord.append(coord)
        if len(CompShipConstruction.order) == 1:# трехпалубный корабль
            a = 4   # максимальное число выше которого корабль не поместиться на этой стороне,
                    # для определения направления достройки корабля
            b = 2   # количество циклов для достройки корабля
            c = 3   # минимальное число ниже которого корабль не поместиться на этой стороне,
                    # для определения направления достройки корабля
        if len(CompShipConstruction.order) > 1:# двухпалубные корабли
            a = 5
            b = 1
            c = 2
        if coord > a:
            for _ in range(b):
                coord -= 1
                sec_coord.append(coord)
        elif coord < c:
            for _ in range(b):
                coord += 1
                sec_coord.append(coord)
        else:
            choice = random.randint(1, 2)
            for _ in range(b):
                if choice == 1:
                    coord += 1
                else:
                    coord -= 1
                sec_coord.append(coord)
        return sec_coord


class Game(ShipConstruction):
    human_shots = []
    human_hit = []
    computer_shots = []
    computer_hit = []
    empty_list = []
    step = random.randint(1, 2)
    best_shots = [(1, 6), (1, 3), (2, 2), (2, 5), (3, 1), (3, 4), (4, 3), (4, 6), (5, 2), (5, 5), (6, 1), (6, 4)]

    @staticmethod
    def shots(x, y, list_of_ships, ships_dict, hit, shots):
        """
        Функция получает координаты выстрела, проверяет попадание, а так же ранен корабль или убит.
        обновляет списки и словарь с координатами кораблей после попадания
        :param x:
        :param y:
        :param list_of_ships: список с координатами кораблей
        :param ships_dict: словарь с кораблями
        :param hit: попадание - далее используется для посторения доски
        :param shots: список выстрелов - далее используется для посторения доски
        :return:
        """
        if (x, y) in list_of_ships:
            for coords in ships_dict.values():
                for coord in coords:
                    if (x, y) == coord:
                        print("ПОПАЛ!")
                        hit.append((x, y))
                        shots.append((x, y))
                        coords.remove(coord)
                        list_of_ships.remove((x, y))
                        if len(coords) > 0:
                            print('И ранил!')
                        else:
                            print('И убил!')
        else:
            print('мимо')
            shots.append((x, y))
            Game.step += 1

    @staticmethod
    def game():
        """
        Основная функция игры. случайным образом определяет кто ходит первым. проверяет условие победы
        :return:
        """
        while True:
            ShipConstruction.print_board()
            if not ShipConstruction.coord_occup:
                print('Компьютер выиграл!')
                break
            elif not CompShipConstruction.coord_of_ship:
                print('Ты выиграл, поздравляю!')
                break
            if Game.step % 2 == 1:
                human, computer = 1, 0
            if Game.step % 2 == 0:
                human, computer = 0, 1
            if human == 1:
                print('ты стреляешь')
                (x, y) = ShipConstruction.input_coordinates(Game.human_shots, Game.empty_list)
                Game.shots(x, y, CompShipConstruction.coord_of_ship, CompShipConstruction.ships_dict, Game.human_hit,\
                           Game.human_shots)
            if computer == 1:
                print('Компьютер стреляет')
                time.sleep(2)
                if len(Game.best_shots) > 0:
                    shot_number = random.randint(0, len(Game.best_shots) - 1)
                    (x, y) = Game.best_shots[shot_number]
                    Game.best_shots.pop(shot_number)
                    print('x = ', x, '\ny = ', y)
                    time.sleep(1)
                    Game.computer_shots.append((x, y))
                else:
                    while True:
                        x = random.randint(1, 6)
                        y = random.randint(1, 6)
                        if (x, y) in Game.computer_shots:
                            continue
                        else:
                            print('x = ', x, '\ny = ', y)
                            time.sleep(1)
                            Game.computer_shots.append((x, y))
                            break
                Game.shots(x, y, ShipConstruction.coord_occup, ShipConstruction.dict_ships, Game.computer_hit, \
                    Game.computer_shots)

input('Создаем свой флот!\npress Enter')
a = ShipConstruction()
print(f'создаем трехпалубный корабль')
a.ship_check_line(3)
a.print_board()
for _ in range(2):
    print(f'создаем {_ + 1}-й двухпалубный корабль')
    a.ship_check_line(2)
    a.print_board()
for _ in range(4):
    print(f'создаем {_ +1}-й однопалубный корабль')
    a.ship_check_line(1)
    a.print_board()

b = CompShipConstruction()
b.ship_position()


input('\nНачинаем игру!\npress Enter')
Game.game()
#хотел дописать алгоритм, чтобы он добивал корабли которые ранил, но в виду того что опаздываю по курсу решил
# сдать как есть

