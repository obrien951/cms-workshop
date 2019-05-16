import numpy as np
import sys

def calculate_distance(atom1, atom2):
    """
    Calculate the distance between two atoms.

    Parameters
    ----------
    atom1 : list
        A list of coordinates [x,y,z]
    atom2 : list
        A list of coordinates [x,y,z]

    Returns
    -------
    bond_length: float
        The distance between atoms.

    Examples
    --------
    >>> calculate_distance([0, 0, 0], [0,0,1])
    1.0
    """
    x_dist = atom1[0] - atom2[0]
    y_dist = atom1[1] - atom2[1]
    z_dist = atom1[2] - atom2[2]
    bond_length = np.sqrt( x_dist*x_dist + y_dist*y_dist+z_dist*z_dist)

    return bond_length

def bond_check(atom_distance, minimum_length = 0, maximum_length=1.5):
    """
    Check if distance is a bond.

    Parameters
    ----------
    atom_distance: float
        The distance between atoms
    minimum_length: float
        The minimum distance for a bond.
    maximum_length: float
        The maximum distance for a bond.

    Return
    ------
    True if bond
    False if not a bond
    """
    print(type(atom_distance))
    if not isinstance(atom_distance, float):
        raise TypeError(F'atom_distance must be type float. {atom_distance}')

    if atom_distance > minimum_length and atom_distance <= maximum_length:
        return True
    else:
        return False

def open_xyz(filename):
    xyz_file = numpy.genfromtxt(fname = filename, skip_header=2, dtype='unicode')
    symbols = xyz_file[:,0]
    coord = (xyz_file[:,1:])
    coord = coord.astype(numpy.float)
    return symbols, coord


if __name__ == "__main__":
    if len (sys.argv) < 2:
        raise IndexError('No file name given. Script requires an xyz file')

    xyzfilename = sys.argv(xyzfilename)
    symbols, coord = open_xyz(xyzfilename)

    for numA, atomA in enumerate(coord):
        for num_B, atomB in enumerate(coord):
            if numB > numA:
                bond_length_AB = calculate_distance(atomA, atomB)
                if bond_check(bond_length_AB):
                    print(F'{symbols[numA]} to {symbols[numB]} : {bond_length_AB:.3f}')


