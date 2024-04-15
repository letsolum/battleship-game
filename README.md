# Battleship

## Description

This is simple non-network realization of popular deck game [Battleship](https://en.wikipedia.org/wiki/Battleship_(game)).

## Configuration

By default, there is 'auto-input.txt', which contains simple version of ships-placement according to format:
 - each ship places at own line
 - at first written left/upper end of the ship, then right/lower, separated by space
 - both ends should match with position on game-desk ('A1', 'G7', ...)
 - obviously, it should follow [rules](https://ru.wikipedia.org/wiki/%D0%9C%D0%BE%D1%80%D1%81%D0%BA%D0%BE%D0%B9_%D0%B1%D0%BE%D0%B9_(%D0%B8%D0%B3%D1%80%D0%B0)#%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0_%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F_%D0%BA%D0%BE%D1%80%D0%B0%D0%B1%D0%BB%D0%B5%D0%B9_(%D1%84%D0%BB%D0%BE%D1%82%D0%B0)) of classic deck game

You can easily edit this file or even delete.

## Usage
There are two run-modes: console (```-c|--console```) & ui (```-u|--ui```). 
```bash
$ git clone git@gitlab.akhcheck.ru:egor.stepashin/battleship.git
$ cd battleship
$ pip install -r requirements.txt
$ python3 main.py [-c|--console  -u|--ui]
```
## Examples
### UI
![Alt Text](utils/ui_example_usage.gif)

### Console
#### Start board:
```bash
     A B C D E F G H I J
1  |✅ .✅ .✅ .✅ . . .
2  | . . . . . . . . . .
3  |✅✅ .✅✅ .✅✅ . .
4  | . . . . . . . . . .
5  |✅✅✅ .✅✅✅ . . .
6  | . . . . . . . . . .
7  |✅✅✅✅ . . . . . .
8  | . . . . . . . . . .
9  | . . . . . . . . . .
10 | . . . . . . . . . .
```

#### Missed shots:
```bash 
Your turn: A1
Missed.
     A B C D E F G H I J
1  | # . . . . . . . . .
2  | . . . . . . . . . .
3  | . . . . . . . . . .
4  | . . . . . . . . . .
5  | . . . . . . . . . .
6  | . . . . . . . . . .
7  | . . . . . . . . . .
8  | . . . . . . . . . .
9  | . . . . . . . . . .
10 | . . . . . . . . . .
```

#### Wounded shots:
```bash
Bot fired into the cage H2
Missed.
     A B C D E F G H I J
1  | . # . . . # . . . .
2  | . # . . . . . # . .
3  | . . . . . . . . . .
4  | . . # . # . . . . .
5  | . . . . . . . . . .
6  | . . . # . . . . . .
7  |❌ . . . . . . . . .
8  | . . . . . . # . . .
9  | # . . . . . . # . .
10 | . . . . . . . . # .
```

#### Dead shots:
```bash
Your turn: A1
Dead.
     A B C D E F G H I J
1  |❌ # . . . . . . . .
2  | # # . . . . . . . .
3  | . . . . . . . . . .
4  | . . . . . . . . . .
5  | . . . . . . . . . .
6  | . . . . . . . . . .
7  | . . . . . . . . . .
8  | . . . . . . . . . .
9  | . . . . . . . . . .
10 | . . . . . . . . . .
```



## Version 0.2 updates
  - Added UI interface
  - Refactored ```main.py``` according to [Model-View-Controller](https://ru.wikipedia.org/wiki/Model-View-Controller)
