def median(llist):
    sortedl = sorted(llist)
    if len(llist) % 2 == 0:
        median = (sortedl[len(sortedl) / 2 - 1] + sortedl[len(sortedl) / 2]) * 1 / 2.0
    else:
        median = sortedl[len(sortedl) / 2]

    return median
