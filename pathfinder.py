import random
# Import file with elevations (fn at end of script)

# Initialize main array we'll populate in extract_coords()
xy_array= []

# Take coord .txt and create xy_array (this is a list of lists. each sublist is one x value (horizontal line on map) of elevations). 
# Calls pathmaker with finished xy_array as arg.
def extract_coords(file):
    with open(file, 'r') as coord_file:
        x_array = coord_file.readlines()
        for ele in x_array:
            xy_array.append(ele.split())
        pathmaker(xy_array) 


# Gets input from user for starting y-value (x=0).
# Gets elevation of current 'cell' and three cell options ahead using val_at_coords(curr_cell).
# Picks best option using path_choose(curr_cell), moves to that cell.
# Creates pathpoints[] which is list of all coords of path. (return that?)
def pathmaker(xy_array):        

    y_start = int(input(f"Where would you like to start your journey? Enter a y-coordinate from 1-{len(xy_array)}: "))-1
    curr_cell = [0,y_start]
    # print('****a****', curr_cell[0])
    # print('****a****', curr_cell[1])

    pathpoints = []

    while curr_cell[0] < len(xy_array[0])-1:
        templist = []
        templist.append((curr_cell[0],curr_cell[1]))
        if curr_cell[1] == 0:
            print("hit the top at", curr_cell)
            curr_cell = pathchoose_top(curr_cell)
        elif curr_cell[1] == len(xy_array)-1:
            print("hit the bottom at", curr_cell)
            curr_cell = pathchoose_bottom(curr_cell)    
        else:    
            curr_cell = pathchoose(curr_cell)
        pathpoints.append(templist)
        # print('****d****', pathpoints)
    print("Path finished at ", curr_cell)

    # print(pathpoints)
    # print(pathpoints[2])
    # print(pathpoints[2][0])
    # print(pathpoints[2][0][0]) #x coord
    # print(pathpoints[2][0][1]) #y coord


# Edge case for top of frame
def pathchoose_top(curr_cell):
    print('top check 0')
    fwd_s   = (curr_cell[0] + 1, curr_cell[1])
    fwd_d   = (curr_cell[0] + 1, curr_cell[1]+1)
    
    curr_alt= val_at_coords(curr_cell)
    alt_s   = val_at_coords(fwd_s)
    alt_d   = val_at_coords(fwd_d)

    step_s  = abs(curr_alt - alt_s)
    step_d  = abs(curr_alt - alt_d)
    
    if step_s <= step_d:
        next_cell = fwd_s
        print('top check 1')
    else:
        next_cell = fwd_d
        print('top check 2')
    return next_cell    


# Edge case for bottom of frame
def pathchoose_bottom(curr_cell):
    print('bottom check 0')
    fwd_u   = (curr_cell[0] + 1, curr_cell[1]-1)
    fwd_s   = (curr_cell[0] + 1, curr_cell[1])
    
    curr_alt= val_at_coords(curr_cell)
    alt_u   = val_at_coords(fwd_u)
    alt_s   = val_at_coords(fwd_s)

    step_u  = abs(curr_alt - alt_u)
    step_s  = abs(curr_alt - alt_s)

    if step_s <= step_u:
        next_cell = fwd_s
        print('bottom check 1')
    else:
        next_cell = fwd_u
        print('bottom check 2')
    return next_cell    


# Given current cell, finds best choice for next step. returns updated current cell. 
def pathchoose(curr_cell):
    
    fwd_u   = (curr_cell[0] + 1, curr_cell[1]-1)
    fwd_s   = (curr_cell[0] + 1, curr_cell[1])
    fwd_d   = (curr_cell[0] + 1, curr_cell[1]+1)

    curr_alt= val_at_coords(curr_cell)
    alt_u   = val_at_coords(fwd_u)
    alt_s   = val_at_coords(fwd_s)
    alt_d   = val_at_coords(fwd_d)


    step_u  = abs(curr_alt - alt_u)
    step_s  = abs(curr_alt - alt_s)
    step_d  = abs(curr_alt - alt_d)
    # print('pathchoose alts', alt_u, alt_s, alt_d)
    # print('pathchoose steps', step_u, step_s, step_d)
    if (step_s <= step_u) and (step_s <= step_d):
        next_cell = fwd_s
    elif (step_u < step_d):
        next_cell = fwd_u
    elif (step_d < step_u):
        next_cell = fwd_d
    else:
        up_or_down = [fwd_u, fwd_d]
        # print("got a tie here:", (alt_u, alt_s, alt_d))
        next_cell  = coinflip(up_or_down)
        # print("coin picked:", val_at_coords(next_cell))

    return next_cell


# Given current cell (x,y), returns elevation at that position in xy_array.
def val_at_coords(curr_cell):
    # print('val at coords', xy_array[curr_cell[1]][curr_cell[0]])
    return int(xy_array[curr_cell[1]][curr_cell[0]])


# Given tie between up and down, randomly pick one. Receives list of 2 choices, returns one of those choices. 
def coinflip(up_or_down):
    return up_or_down[random.randint(0,1)]


# allows user to call program and .txt coord file from terminal.
# Calls extract_coords, which then calls others. 
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Extract Coordinates from .txt file and output path image.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        extract_coords(file)
    else:
        print(f"{file} does not exist!")
        exit(1)


# return min(test_file.read().split())