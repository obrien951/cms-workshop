"""
Tests for geom_analysis.py
"""

import geom_analysis as ga


def test_calculate_distance():
    coord1 = [0, 0, 2]
    coord2 = [0, 0, 0]

    observed = ga.calculate_distance(coord1, coord2)

    assert observed == 2

def test_bond_check_false():
    big_dist = 1.7

    big_obs = ga.bond_check(big_dist)
    assert big_obs == False

def test_bond_check_true():
    gud_dist = 1.2

    gud_obs = ga.bond_check(gud_dist)
    assert gud_obs == True
