# Loops

Complete the coding exercise using the pair programming technique outlined in lecture.

When coding, **do not delete any comments in the provided template.**

_Hint: Run the starter code before you start hacking things up!_

_Hint: Use the debugger to step through your code!_

## Program 1 - Doomsday Countdown

_Scenario_

You are a prominent scribe in a reclusive cult known as "Children of Moloch". The cult's charismatic leader, Mother Sharice, has tasked you with writing a software program to print a daily countdown to impact day ("Day of Joyous Arrival") on the cult's brand new LED display. The Dark Lord Moloch has given the following information to Mother Sharice, who in turn has given it to you:

- A comet is heading towards Earth.
- The comet is currently 100,000,000 km away from Earth.
- The comet is moving at a speed of 3,860,000 km per day towards earth.

_Instructions_

In this program you will edit the file `doomsday.py`.

Write a program that, each day, prints:

- The distance of the comet from Earth.
- The number of days remaining until the comet reaches Earth.

Make sure that any program input and output matches the format given in the example run exactly, including any capitalization, punctuation, and spacing. The program should work for any set of inputs - not just those specified in the example runs.

_Example Run:_

```
Date: 2024-09-23        Comet Distance:  100000000 km   Joyous Arrival:       25.9 days
Date: 2024-09-24        Comet Distance:   96140000 km   Joyous Arrival:       24.9 days
# ... remaining rows omitted ...
Date: 2024-10-18        Comet Distance:    3500000 km   Joyous Arrival:        0.9 days
Rejoice! Day of Joyous Arrival is upon us!
```

## Program 2 - Frog Racing

_Scenario_

Professional frog racing has the following rules:

- A series of boxes are set in a row.
- A frog may start on or before the start box (box 0).
- The goal is to land a hop in the finish box (box 10) without overshooting in the least amount of jumps.

Not all frogs are created equal. Some frogs can jump further than others. The current world leaders are:

- Crazy Bill: 3 boxes per jump
- Legs Johnson: 2 boxes per jump
- Steady Stu: 1 box per jump

_Instructions_

In this program you will edit the file `frograce.py`.

In the following simulation program the user will select a start position on or before position zero. The program will then print the position of each frog's jumps until the frogs either land in or overshoot the finish box.

Make sure that any program input and output matches the format given in the example run exactly, including any capitalization, punctuation, and spacing. The program should work for any set of inputs - not just those specified in the example runs.

_Example Run:_

```
Enter a starting position: 0
Steady Stu: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
Legs Johnson: 0, 2, 4, 6, 8, 10
Crazy Bill: 0, 3, 6, 9, 12
```

```
Enter a starting position: -3
Steady Stu: -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
Legs Johnson: -3, -1, 1, 3, 5, 7, 9, 11
Crazy Bill: -3, 0, 3, 6, 9, 12
```

_Bonus (+10)_

Calculate the winner as the frog that lands in the finish box with the least amount of jumps and print the winner at the end of the race.

## Submission

Make sure to submit your work via the Source Control tab on the left-side menu in VS Code before closing the browser window. You may check your submitted work in your GitHub Organization for the course. Make sure to deallocate (delete) your codespace after you are finished.
