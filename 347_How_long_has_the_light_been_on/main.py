# Author(s): Michael Koeppl

def read_intervals(input_file_path):
    input_file = open(input_file_path)

    intervals = []

    print("Intervals:")
    for line in input_file.readlines():
        interval_start = int(line.split(" ")[0])
        interval_end = int(line.split(" ")[1])
        print("{0} {1}".format(interval_start, interval_end))
        intervals.append((interval_start, interval_end))

    return intervals 

def calc_hours(intervals):
    hour_count = 0
    last_exit = max(interval[1] for interval in intervals)
    for i in range(last_exit):
        # Check if the current value can be found within any of the intervals
        # using interval comparison (exclusive upper bound).
        if any(1 for start, end in intervals if start <= i < end):
            hour_count += 1
    return hour_count

def main():
    paths = ["./input1.txt", "./input2.txt", "./input3.txt"]
    for path in paths:
        intervals = read_intervals(path)
        hours = calc_hours(intervals)
        print("Hours: {0}\n".format(hours))

if __name__ == "__main__":
    main()