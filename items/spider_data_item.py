# -*- coding: utf-8 -*-
"""
Created on 2022-11-08 17:57:15
---------
@summary:
---------
@author: ehnait
"""

from feapder import Item


class SpiderDataItem(Item):
    """
    This class was generated by feapder
    command: feapder create -i spider_data
    """

    __table_name__ = "spider_data"

    def __init__(self, *args, **kwargs):
        # self.id = None
        self.title = None
        self.img_url = None
        self.detail_url = None
        self.content = None