#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""


if __name__ == "__main__":
    import sys

    total_size = 0
    status_code = {"200": 0, "301": 0, "400": 0, "401": 0,
                   "403": 0, "404": 0, "405": 0, "500": 0}
    counter = 0

    def print_stats():
        """print stats"""
        print("File size: {}".format(total_size))
        for key in sorted(status_code.keys()):
            if status_code[key] != 0:
                print("{}: {}".format(key, status_code[key]))

    try:
        for line in sys.stdin:
            counter += 1
            split_line = line.split()
            try:
                total_size += int(split_line[-1])
            except (IndexError, ValueError):
                pass
            try:
                if split_line[-2] in status_code:
                    status_code[split_line[-2]] += 1
            except IndexError:
                pass
            if counter % 10 == 0:
                print_stats()
        print_stats()
    except KeyboardInterrupt:
        print_stats()
        raise
