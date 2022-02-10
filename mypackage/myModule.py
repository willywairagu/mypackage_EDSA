def top_n(items, n):
    """ Returns the top n items in an array, in desc order

    Args:
        items (array): list or array-like object
        n (int): number of items to return

    Return:
        array: top n items to return, in desc order

    Egs:
        >> top_n([8, 3, 2, 7, 4], 3)
        answer:  [8, 7, 3]
    """
    for i in range(n):   # keep sorting until we have the top n items
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:  # if this item is bigger than the next one
                items[j], items[j+1] = items[j+1], items[j]  # swap the two

    # get the last two items
    top_n = items[-n:]

    # return in descending order
    return top_n[::-1]
