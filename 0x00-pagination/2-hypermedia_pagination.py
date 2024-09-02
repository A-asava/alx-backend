#!/usr/bin/env python3
'''Simple helper function'''
import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
        page(int): page number
        page_size(int): number contents per page
        return:  tuple of (start, end) for the current page and next page.
    '''

    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''Retrieve the specified page of the dataset.
            Args:
                page (int): The page number (default is 1).
                page_size (int): The number of items per page (default is 10)
            Returns:
                list: The specified page of the dataset.
        '''

        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start >= len(data):
            return []
        else:
            return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 1) -> Dict[str, any]:
        '''Get hypermedia controls for navigating through pages.
           Args:
               page (int): The current page number.
               page_size (int): Number of items to display on each page.
           Returns:
               dict: A dictionary containing
               'first', 'previous', 'next' and 'last'
               keys. Each key maps to a URL that will
               dict: A dictionary containing
               'first', 'previous', 'next' and 'last'
               keys. Each key points to a URL that will return
        '''

        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
