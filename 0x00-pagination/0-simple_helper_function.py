#!/usr/bin/env python3
'''Simple helper function'''


def index_range(page, page_size):
    '''
        page(int): page number
        page_size(int): number contents per each page
        return:  tuple of (start, end) for the current page and next page.
    '''

    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size
    return (start, end)
