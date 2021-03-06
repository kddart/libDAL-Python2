#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""
 * dalclient library - provides utilities to assist in using KDDart-DAL servers
 * Copyright (C) 2017  Diversity Arrays Technology
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "alexs"
__copyright__ = "Copyright (C) 2017  Diversity Arrays Technology"
__license__ = "GPL 3.0"
__email__ = ""


class ResponseType(object):

    def __init__(self, xmlTrue=False):

        self._jsonVal = "json"
        self._xmlVal = "xml"

        self._xml = xmlTrue

        if xmlTrue:
            self._value = self._xmlVal
        else:
            self._value = self._jsonVal

    def isXML(self):
        """
        :return: whether content type for response is xml or json
        """
        return self._xml

    @property
    def value(self):
        return self._value

