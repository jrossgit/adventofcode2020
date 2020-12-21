from src import day12


def test_ship_navigation():

    ship = day12.Ship(direction="E")

    assert ship.location == [0, 0]
    ship.execute("F10")
    assert ship.direction == "E"
    assert ship.location == [10, 0]

    ship.execute("N3")
    assert ship.direction == "E"
    assert ship.location == [10, 3]

    ship.execute("F7")
    assert ship.direction == "E"
    assert ship.location == [17, 3]

    ship.execute("R90")
    assert ship.direction == "S"
    assert ship.location == [17, 3]

    ship.execute("F11")
    assert ship.direction == "S"
    assert ship.location == [17, -8]

    assert ship.manhatten_distance == 25


def test_waypoint_navigation():

    ship = day12.ShipWaypoint(waypoint=10 + 1j)

    assert ship.location == 0 + 0j
    assert ship.waypoint == 10 + 1j
    ship.execute("F10")
    assert ship.location == 100 + 10j

    ship.execute("N3")
    assert ship.waypoint == 10 + 4j
    assert ship.location == 100 + 10j

    ship.execute("F7")
    assert ship.waypoint == 10 + 4j
    assert ship.location == 170 + 38j

    ship.execute("R90")
    assert ship.waypoint == 4 - 10j
    assert ship.location == 170 + 38j

    ship.execute("F11")
    assert ship.waypoint == 4 - 10j
    assert ship.location == 214 - 72j

    ship.execute("R180")
    assert ship.waypoint == -4 + 10j
    assert ship.location == 214 - 72j

    ship.execute("L90")
    assert ship.waypoint == -10 - 4j
    assert ship.location == 214 - 72j

    ship.execute("R180")
    assert ship.waypoint == 10 + 4j
    assert ship.location == 214 - 72j

    assert ship.manhatten_distance == 286


def test_waypoint_movement():

    ship = day12.ShipWaypoint(waypoint=10 + 1j)

    ship.execute("N1")
    assert ship.waypoint == 10 + 2j

    ship.execute("S1")
    assert ship.waypoint == 10 + 1j

    ship.execute("E1")
    assert ship.waypoint == 11 + 1j

    ship.execute("W1")
    assert ship.waypoint == 10 + 1j
