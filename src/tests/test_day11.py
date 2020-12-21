from src import day11


def test_task_01_with_test_input():
    assert day11.task_1("day_11_test") == 37


def test_task_02_with_test_input():
    assert day11.task_2("day_11_test") == 26


def test_seat_iteration_immediate():

    plan = (
        True,
        [
            "#.##.L#.##",
            "#L###LL.L#",
            "L.#.#..#..",
            "#L##.##.L#",
            "#.##.LL.LL",
            "#.###L#.##",
            "..#.#.....",
            "#L######L#",
            "#.LL###L.L",
            "#.#L###.##",
        ],
    )

    plan = day11.iterate(plan[1], 4, day11.number_neighbours_immediate)
    assert plan == (
        True,
        [
            "#.#L.L#.##",
            "#LLL#LL.L#",
            "L.L.L..#..",
            "#LLL.##.L#",
            "#.LL.LL.LL",
            "#.LL#L#.##",
            "..L.L.....",
            "#L#LLLL#L#",
            "#.LLLLLL.L",
            "#.#L#L#.##",
        ],
    )

    plan = day11.iterate(plan[1], 4, day11.number_neighbours_immediate)
    assert plan == (
        True,
        [
            "#.#L.L#.##",
            "#LLL#LL.L#",
            "L.#.L..#..",
            "#L##.##.L#",
            "#.#L.LL.LL",
            "#.#L#L#.##",
            "..L.L.....",
            "#L#L##L#L#",
            "#.LLLLLL.L",
            "#.#L#L#.##",
        ],
    )


def test_seat_iteration_line_of_sight():

    plan = (
        True,
        [
            "#.##.##.##",
            "#######.##",
            "#.#.#..#..",
            "####.##.##",
            "#.##.##.##",
            "#.#####.##",
            "..#.#.....",
            "##########",
            "#.######.#",
            "#.#####.##",
        ],
    )

    plan = day11.iterate(plan[1], 5, day11.number_neighbours_line_of_sight)
    assert plan == (
        True,
        [
            "#.LL.LL.L#",
            "#LLLLLL.LL",
            "L.L.L..L..",
            "LLLL.LL.LL",
            "L.LL.LL.LL",
            "L.LLLLL.LL",
            "..L.L.....",
            "LLLLLLLLL#",
            "#.LLLLLL.L",
            "#.LLLLL.L#",
        ],
    )

    plan = day11.iterate(plan[1], 5, day11.number_neighbours_line_of_sight)
    assert plan == (
        True,
        [
            "#.L#.##.L#",
            "#L#####.LL",
            "L.#.#..#..",
            "##L#.##.##",
            "#.##.#L.##",
            "#.#####.#L",
            "..#.#.....",
            "LLL####LL#",
            "#.L#####.L",
            "#.L####.L#",
        ],
    )


def test_line_of_sight_adjacency():
    plan = [
        ".......#.",
        "...#.....",
        ".#.......",
        ".........",
        "..#L....#",
        "....#....",
        ".........",
        "#........",
        "...#.....",
    ]
    assert day11.number_neighbours_line_of_sight(plan, 3, 4) == 8

    plan = [
        ".............",
        ".L.L.#.#.#.#.",
        ".............",
    ]
    assert day11.number_neighbours_line_of_sight(plan, 1, 1) == 0

    plan = [
        ".##.##.",
        "#.#.#.#",
        "##...##",
        "...L...",
        "##...##",
        "#.#.#.#",
        ".##.##.",
    ]
    assert day11.number_neighbours_line_of_sight(plan, 3, 3) == 0

    plan = [
        "#.##.##.##",
        "#######.##",
        "#.#.#..#..",
        "####.##.##",
        "#.##.##.##",
        "#.#####.##",
        "..#.#.....",
        "##########",
        "#.######.#",
        "#.#####.##",
    ]
    assert day11.number_neighbours_line_of_sight(plan, 0, 1) == 4
