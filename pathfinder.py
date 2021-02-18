# import file with elevations
def extract_coords(file):
    with open(file, 'r') as coord_file:
        x_array = coord_file.readlines()
        xy_array= []
        for ele in x_array:
            xy_array.append(ele.split())

        pathseeker(xy_array) 


def pathseeker(xy_array):        

    y_start = int(input("Where would you like to start your journey? Enter a number from 1-600: "))-1
    print(y_start)
    curr_cell = [0,y_start]
    print(curr_cell)

    for x in range(0, len(xy_array[0])): 
        test_cell = xy_array[y_start][x]
        # test_cell = xy_array[x][y_start]
        print(test_cell)


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

