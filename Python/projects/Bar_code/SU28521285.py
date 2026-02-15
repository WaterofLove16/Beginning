import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import sys
import stdio
import stdarray
import stddraw

# global variables
# Your global variables go here
def error_check(Input):
    if len(Input) < 4:
        stdio.writeln("ERROR: Too few arguments")

    if len(Input) > 4:
        stdio.writeln("ERROR: Too many arguments")

    encoding = Input[0]
    grid_size = Input[1]
    position = Input[2]
    alignment = Input[3]

    if not (0 <= encoding < 32):
        stdio.write(f"ERROR: Invalid encodig argument: {encoding}\n")

    else:
        bit = format(encoding, '05b')
        a = bit[0]
        b = bit[1]
        c = bit[2:]

    if not(10 <= grid_size <= 48):
        stdio.write(f"ERROR: Invalid size argument: {grid_size}\n")

    for x in range(grid_size):
        for y in range(grid_size):
            

def payload_codeword(message):
    payload_bit = " "
    byte = "0 1 0 0 "
    message_len = len(message)
    terminator = "0 0 0 0 "
    payload_bit = payload_bit + byte + " ".join(format(message_len, "08b"))

    for i in range(message_len):
        codeword = message[i]
        Bin_rep = " ".join(format(ord(codeword), "08b"))
        payload_bit = payload_bit + Bin_rep

    payload_bit = payload_bit + terminator

    while payload_bit%8 != 0:
        payload_bit = payload_bit

    return payload_bit
    

def mask_pattern(mask, grid):
    N = len(grid)
    if mask == "001":
        for row in range(N):
            for col in range(N):
                if col % 2 == 0:
                    flip_grid(grid, row, col)

    elif mask == "010":
        for row in range(N):
            for col in range(N):
                if row % 3 == 0:
                    flip_grid(grid, row, col)

    elif mask == "011":
        for row in range(N):
            for col in range(N):
                if (row + col) % 3 == 0:
                    flip_grid(grid, row, col)

    elif mask == "100":
        for row in range(N):
            for col in range(N):
                if (row // 3 + col // 2) % 2 == 0:
                    flip_grid(grid, row, col)

    elif mask == "101":
        for row in range(N):
            for col in range(N):
                if (row * col) % 2 + (row * col) % 3 == 0:
                    flip_grid(grid, row, col)

    elif mask == "110":
        for row in range(N):
            for col in range(N):
                if ((row * col) % 2 + (row * col) % 3) % 2 == 0:
                    flip_grid(grid, row, col) 

    elif mask == "111":
        for row in range(N):
            for col in range(N):
                if ((row + col) % 2 + (row * col) % 3) % 2 == 0:
                    flip_grid(grid, row, col)                                                                           

    

def flip_grid(qr_grid, x, y):
    if qr_grid[x][y] == 1:
        qr_grid[x][y] = 0

    else:
        qr_grid[x][y] = 1   



def draw_qr_grid(qr_grid):
    """
    Draws the given qr data onto the canvas of stddraw in the format specified in
    the project specification.

    Args:
        qr_grid (2D array of int): The data of the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def print_qr_grid(qr_grid):
    """
    Prints the given qr data out to the standard output in the format specified in
    the project specification.

    Args:
        qr_grid (2D array of int): The data of the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def make_position_pattern(pos_square_size):
    n = pos_square_size
    code = [["0 " for i in range(n)] for j in range(n)]
    low = 0
    high = n
    if not(n > 3) or (n%2 != 0):
        stdio.write(f"ERROR: Invalid position pattern size argument: {pos_square_size}\n")
        
    else:
        if n%4 != 0:
            for i in range(n):
                k = (n//2)-1
                if i%2 == 0:
                    value = "0 "
                else:
                    value = "1 "
                for j in range(low, high-1):
                    code[i][j] = value
                for j in range(low+1, high-1):
                    code[j][i] = value
                for j in range(low+1, high-1):
                    code[high-2][j] = value
                for j in range(low+1, high-2):
                    code[j][high-2] = value
                    
                low = low + 1
                high = high - 1
                code[i][n-1] = "1 "
                code[n-1][i] = "1 "
                code[k][k] = "1 "
                
        elif n%4 == 0:
            k = (n//2)-1
            for i in range(n):
                if i%2 == 0:
                    value = "1 "
                else:
                    value = "0 "
                for j in range(low, high-1):
                    code[i][j] = value
                for j in range(low+1, high-1):
                    code[j][i] = value
                for j in range(low+1, high-1):
                    code[high-2][j] = value
                for j in range(low+1, high-2):
                    code[j][high-2] = value
                    
                low = low + 1
                high = high - 1
                code[i][n-1] = "0 "
                code[n-1][i] = "0 "
                code[k][k] = "1 "
                
        for i in range(n):
            for j in range(n):
                stdio.write(code[i][j])
            stdio.writeln()


def make_alignment_pattern(align_square_size):
    pattern = None
    n = align_square_size
    lo = 0
    hi = n
    if n < 0 or (n-1)%4 != 0:
        stdio.write(f"ERROR: Invalid alignment pattern size argument: {n}\n")
        
    else:
        code = [["0" for i in range(n)] for j in range(n)]
        k = (n//2)+1
        for i in range(n):
            if i%2 == 0:
                value = "1"
            else:
                value = "0"
            for j in range(lo, hi):
                code[i][j] = value
            for j in range(lo+1, hi):
                code[j][i] = value
            for j in range(lo+1, hi):
                code[hi-1][j] = value
            for j in range(lo+1, hi-1):
                code[j][hi-1] = value
                
            lo = lo + 1
            hi = hi - 1
                
        pattern = code
    return pattern
    


def rotate_pattern_clockwise(data):
    """
    Rotates the values in data clock-wise by 90 degrees

    Args:
        data (2D array of int): The array that should be rotated
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def add_data_at_anchor(qr_grid, anchor_x, anchor_y, data):
    """
    Places values contained in data to the qr_grid starting as positions given
    by achnor_x and anchor_y.

    Args:
        qr_grid (2D array of int): The QR grid
        anchor_x (int): the x position from where the data should be added
        anchor_y (int): the y position from where the data should be added
        data (2D array of int): The data that should be added to the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def add_data_snake(qr_grid, data):
    """
    Places values contained in data to the qr_grid in the snake layout as
    specified in the project specifications.

    Args:
        qr_grid (2D array of int): The QR grid
        data (array of int): The bit sequence of data that should be added to
        the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def add_data_real(qr_grid, data):
    """
    Places values contained in data to the qr_grid in the real layout as
    specified in the project specifications.

    Args:
        qr_grid (2D array of int): The QR grid
        data (array of int): The bit sequence of data that should be added to
        the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def apply_mask(qr_grid, reserved_positions, mask_id):
    """
    Applies the masking pattern specified by mask_id to the QR grid following
    the masking rules as specified by the project specifications.

    Args:
        qr_grid (2D array of int): The QR grid
        reserved_positions (2D array of int): the reserved positions
        mask_id (str): The mask id to apply to the QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass

def encode_real(size, message, information_bits, pos_square_size, align_square_size):
    """
    Generates the QR code according to the project specifications using the
    real layout.

    Args:
        size (int): The size of the QR grid to be generated
        message (str): The message to be encoded
        information_bits (array of int): the 15-bit information pattern
        pos_square_size (int):  The size of the position pattern to generate
        align_square_size (int):  The size of the alignment pattern to generate

    Returns:
        2D array of int: The completed QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def encode_snake(size, message, pos_square_size, align_square_size):
    """
    Generates the QR code according to the project specifications using the
    snake layout.

    Args:
        size (int): The size of the QR grid to be generated
        message (str): The message to be encoded
        pos_square_size (int):  The size of the position pattern to generate
        align_square_size (int):  The size of the alignment pattern to generate

    Returns:
        2D array of int: The completed QR grid
    """
    # TODO: implement this function.
    # remove the following line when you add something to this function:
    pass


def main(args):
    # TODO: put logic here to check if the command-line arguments are correct,
    # and then call the game functions using these arguments.
    pass


if __name__ == "__main__":
    """USage: echo 'message' | python3 SUXXXXXXXX.py 'encoding_string' 'size' 'pos_size' 'align_size'"""
    main(sys.argv)